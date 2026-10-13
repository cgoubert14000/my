"""Moteur temps réel : alimente la même machine à états `OrbSession` que le backtest avec les bougies 1 min clôturées,
applique la politique de risque, transmet les ordres au courtier et tient un journal vérifiable."""
from __future__ import annotations

import dataclasses
import datetime as dt
import json
import pathlib
from dataclasses import dataclass, field
from zoneinfo import ZoneInfo

from ..strategy.orb import Bar, Costs, OrbSession, Trade
from ..strategy.params import OrbParams
from .brokers import PaperBroker, Position
from .feeds import LiveBar
from .policy import DayState, RiskPolicy, can_enter, position_units

NY = ZoneInfo("America/New_York")


@dataclass
class ExecutedTrade:
    model: Trade
    position: Position | None
    units: float
    executed: bool
    reason: str
    real_pnl: float = 0.0


@dataclass
class LiveEngine:
    params: OrbParams
    costs: Costs
    policy: RiskPolicy
    broker: object                      # PaperBroker | OandaBroker
    journal_dir: pathlib.Path
    repo_root: pathlib.Path = pathlib.Path(".")
    unit_step: float = 1.0
    verbose: bool = False

    session: OrbSession | None = None
    day: str = ""
    state: DayState = field(default_factory=DayState)
    ema: float | None = None
    ema_alpha: float = 0.0
    executed: list[ExecutedTrade] = field(default_factory=list)
    model_trades: list[Trade] = field(default_factory=list)
    _open: ExecutedTrade | None = None
    _partial_sent: bool = False
    bars_seen: int = 0

    def __post_init__(self) -> None:
        self.journal_dir.mkdir(parents=True, exist_ok=True)
        if self.params.ma:
            self.ema_alpha = 2.0 / (self.params.ma + 1)
        self.log("start", policy_sha256=self.policy.sha256(), policy=self.policy.model_dump(), variant=self.params.key(), costs=dataclasses.asdict(self.costs),
                 broker=type(self.broker).__name__)

    # ------------------------------------------------------------------ journal

    def log(self, event: str, **data) -> None:
        rec = {"at": dt.datetime.now(dt.UTC).isoformat(timespec="seconds"), "event": event, **data}
        with (self.journal_dir / "journal.jsonl").open("a", encoding="utf-8") as f:
            f.write(json.dumps(rec, ensure_ascii=False, default=str) + "\n")
        if self.verbose:
            print(json.dumps(rec, ensure_ascii=False, default=str), flush=True)

    def write_state(self) -> None:
        eq = getattr(self.broker, "equity", None)
        (self.journal_dir / "state.json").write_text(json.dumps({
            "updated_at": dt.datetime.now(dt.UTC).isoformat(timespec="seconds"), "day": self.day, "variant": self.params.key(),
            "policy_sha256": self.policy.sha256(), "policy_enabled": self.policy.enabled, "mode": self.policy.mode,
            "day_state": self.state.model_dump(), "bars_seen": self.bars_seen,
            "session_state": self.session.state if self.session else None,
            "open_trade": self.session.open_trade.as_dict() if self.session and self.session.open_trade else None,
            "model_trades": len(self.model_trades), "executed_trades": sum(1 for e in self.executed if e.executed),
            "model_total_r": round(sum(t.r_multiple or 0 for t in self.model_trades), 3),
            "executed_total_r": round(sum(e.model.r_multiple or 0 for e in self.executed if e.executed), 3),
            "paper_equity": eq, "recent_events": (self.session.events[-8:] if self.session else []),
        }, ensure_ascii=False, indent=1), encoding="utf-8")

    # ------------------------------------------------------------------ warm-up

    def warmup(self, closes: list[float]) -> None:
        if not self.params.ma or not closes:
            return
        e = closes[0]
        for c in closes[1:]:
            e += self.ema_alpha * (c - e)
        self.ema = e

    # ------------------------------------------------------------------ main loop

    async def run(self, feed, single_day: bool = False) -> None:
        last: LiveBar | None = None
        async for lb in feed.bars():
            last = lb
            await self.on_bar(lb)
            if single_day and self.session and self.session.done and not self._open:
                break
        # fin du flux (limite de temps, arrêt demandé) avec une position exécutée encore ouverte : on la ferme au marché
        # plutôt que de laisser le modèle et le courtier diverger.
        if self._open and self._open.executed and self._open.position and not self._open.position.closed and last is not None and self.session:
            tr = self._open.model
            px = (last.c - self.costs.slippage) if tr.direction > 0 else (last.c + self.costs.spread + self.costs.slippage)
            await self.broker.close(self._open.position.id, px, None, last.ts.strftime("%Y-%m-%dT%H:%MZ"), "time_limit")
            self.log("time_limit_close", trade_id=self._open.position.id, price=px, realized=round(self._open.position.realized, 2))
            self._open = None
        self.write_state()
        self.log("stop", model_trades=len(self.model_trades), executed=sum(1 for e in self.executed if e.executed))

    async def on_bar(self, lb: LiveBar) -> list[Trade]:
        self.bars_seen += 1
        if self.params.ma:
            self.ema = lb.c if self.ema is None else self.ema + self.ema_alpha * (lb.c - self.ema)
        ny = lb.ts.astimezone(NY)
        day = ny.strftime("%Y-%m-%d")
        if day != self.day:
            self._new_day(day)
        if ny.weekday() >= 5 or self.session is None:
            return []
        t = ny.hour * 60 + ny.minute
        bar = Bar(t, lb.o, lb.h, lb.l, lb.c, self.ema if (self.params.ma and self.ema is not None) else float("nan"), lb.ts.strftime("%Y-%m-%dT%H:%MZ"))
        prev_open = self.session.open_trade
        closed = self.session.on_bar(bar)
        # kill switch pendant une position : fermeture immédiate au marché
        kill = self.policy.kill_switch_active(self.repo_root)
        if self.session.open_trade is not None and prev_open is None:
            await self._on_model_entry(self.session.open_trade, bar, ny, kill)
        elif self.session.open_trade is not None and self._open and self._open.executed and self._open.position:
            tr = self.session.open_trade
            if tr.partial_done and not self._partial_sent:
                self._partial_sent = True
                await self.broker.close(self._open.position.id, tr.tp1_price, self._open.units / 2, bar.ts, "tp1")
                await self.broker.set_stop(self._open.position.id, tr.stop_price)
                self.log("partial", trade_id=self._open.position.id, price=tr.tp1_price, new_stop=tr.stop_price)
            if kill:
                px = (bar.c - self.costs.slippage) if tr.direction > 0 else (bar.c + self.costs.spread + self.costs.slippage)
                await self.broker.close(self._open.position.id, px, None, bar.ts, "kill_switch")
                self.log("kill_switch_close", trade_id=self._open.position.id, price=px)
                self._open.real_pnl = self._open.position.realized
                self._open = None
                self.session.open_trade = None
                self.session.done = True
                self.session.state = "done"
        for tr in closed:
            await self._on_model_exit(tr, bar)
        if closed or self.bars_seen % 5 == 0:
            self.write_state()
        return closed

    def _new_day(self, day: str) -> None:
        if self.session and self.session.open_trade is not None:
            self.log("warning", msg="changement de jour avec position modèle ouverte", day=self.day)
        self.day = day
        self.state = DayState(day=day)
        self.session = OrbSession(params=self.params, costs=self.costs, day=day)
        self._open = None
        self._partial_sent = False
        self.log("new_day", day=day)

    async def _on_model_entry(self, tr: Trade, bar: Bar, ny: dt.datetime, kill: bool) -> None:
        ok, why = can_enter(self.policy, self.state, kill, ny)
        units = 0.0
        if ok:
            equity = await self.broker.account_equity()
            units = position_units(equity, self.policy.risk_pct_per_trade, tr.risk, self.policy.max_units, self.unit_step)
            if units <= 0:
                ok, why = False, f"taille nulle (capital {equity:.0f}, risque/unité {tr.risk:.4f})"
        if not ok:
            self.state.refused += 1
            self._open = ExecutedTrade(tr, None, 0.0, False, why)
            self.log("entry_refused", reason=why, model=tr.as_dict())
            return
        pos = await self.broker.open_market(self.policy.instrument, tr.direction, units, tr.entry_price, tr.stop_price, tr.tp_price, bar.ts)
        self._open = ExecutedTrade(tr, pos, units, True, "ok")
        self._partial_sent = False
        self.state.trades += 1
        self.log("entry", trade_id=pos.id, direction=tr.direction, units=units, price=tr.entry_price, stop=tr.stop_price, tp=tr.tp_price,
                 tp1=tr.tp1_price, signal=tr.signal, risk_per_unit=tr.risk, broker_price=pos.entry_price)

    async def _on_model_exit(self, tr: Trade, bar: Bar) -> None:
        self.model_trades.append(tr)
        ex = self._open
        self._open = None
        if ex is None:
            ex = ExecutedTrade(tr, None, 0.0, False, "non suivi")
        if ex.executed and ex.position is not None:
            if not ex.position.closed:
                await self.broker.close(ex.position.id, tr.exit_price, None, bar.ts, tr.exit_reason)
            ex.real_pnl = ex.position.realized
            r = tr.r_multiple or 0.0
            self.state.r_total += r
            self.state.consecutive_losses = self.state.consecutive_losses + 1 if r < 0 else 0
            self.log("exit", trade_id=ex.position.id, reason=tr.exit_reason, price=tr.exit_price, r=r, real_pnl=round(ex.real_pnl, 2),
                     day_r=round(self.state.r_total, 3), history=ex.position.history)
        else:
            self.log("model_exit_not_executed", reason=tr.exit_reason, r=tr.r_multiple, why=ex.reason)
        self.executed.append(ex)
        self.write_state()


def default_costs_for(instrument: str) -> Costs:
    from ..data.dukascopy import INSTRUMENTS
    m = INSTRUMENTS.get(instrument)
    if not m:
        return Costs()
    return Costs(spread=m["spread"], slippage=m["slippage"], min_risk=m["spread"])


def paper_engine(params: OrbParams, policy: RiskPolicy, journal_dir: pathlib.Path, costs: Costs | None = None, repo_root: pathlib.Path = pathlib.Path(".")) -> LiveEngine:
    return LiveEngine(params=params, costs=costs or default_costs_for(policy.data_instrument), policy=policy,
                      broker=PaperBroker(policy.paper_equity), journal_dir=journal_dir, repo_root=repo_root)
