"""Machine à états ORB (Opening Range Breakout) sur bougies 1 minute.

Le même objet `OrbSession` est utilisé par le backtest (on lui passe les bougies historiques une à une) et par le
moteur temps réel (on lui passe chaque bougie 1 min clôturée) : il ne peut pas y avoir d'écart entre ce qui est testé
et ce qui est exécuté.

Conventions (toutes documentées dans docs/orb/README.md) :
- les bougies sont des prix BID ; un achat se fait à bid + spread, une vente à bid ; glissement (slippage) ajouté aux
  ordres au marché et aux stops, jamais aux limites ;
- dans une même bougie, si le stop et l'objectif sont tous deux touchés, le STOP est supposé touché en premier
  (hypothèse défavorable) ; dans la bougie d'entrée d'un retest FVG, seul le stop est vérifié ;
- range = plus haut / plus bas des bougies [09:30, 09:30 + R) heure de New York ; cassure = clôture 1 min au-delà ;
- « fvg » : après une clôture au-delà du range, on cherche la première Fair Value Gap dans le sens de la cassure
  (haussière : low[i] > high[i-2]) ; entrée limite au bord proche de la zone lorsque le prix revient dessus ;
  si une bougie clôture de nouveau dans le range avant qu'une FVG n'apparaisse, le signal est abandonné ;
- un second trade (max_trades = 2) n'est pris que si le prix a reclôturé dans le range depuis la sortie (même sens)
  ou dans l'autre sens ; aucune entrée après `entry_cutoff` ; tout est clôturé à `flat_at`.
"""
from __future__ import annotations

import math
from dataclasses import dataclass, field

from .params import OrbParams, hhmm_to_minutes

OPEN_NY = 9 * 60 + 30  # 09:30 New York


@dataclass(frozen=True, slots=True)
class Bar:
    t: int          # minutes depuis minuit, heure de New York (début de la bougie)
    o: float
    h: float
    l: float  # noqa: E741
    c: float
    ema: float = math.nan  # EMA(ma) sur les clôtures, nan si non calculée
    ts: str = ""           # horodatage UTC ISO (pour le journal)


@dataclass(frozen=True, slots=True)
class Costs:
    spread: float = 0.0     # unités de prix (or : 0.30 $ par défaut)
    slippage: float = 0.0   # unités de prix, par exécution au marché / stop
    min_risk: float = 0.0   # distance d'entrée-stop minimale acceptée (sinon trade ignoré)


@dataclass
class Trade:
    day: str
    direction: int                 # +1 long, -1 short
    entry_t: int
    entry_price: float             # prix effectivement payé/reçu (coûts inclus)
    stop_price: float              # niveau bid du stop initial
    risk: float                    # |entry − stop|
    tp_price: float
    tp1_price: float | None = None
    exit_t: int | None = None
    exit_price: float | None = None
    exit_reason: str = ""
    r_multiple: float | None = None
    pnl_per_unit: float | None = None
    partial_done: bool = False
    partial_pnl: float = 0.0           # P&L (par unité) déjà encaissé au TP partiel
    entry_ts: str = ""
    exit_ts: str = ""
    signal: str = ""               # "close" | "fvg"
    mae_r: float = 0.0             # pire excursion défavorable (en R, négatif)
    mfe_r: float = 0.0             # meilleure excursion favorable (en R)

    def as_dict(self) -> dict:
        return {k: (round(v, 6) if isinstance(v, float) else v) for k, v in self.__dict__.items()}


@dataclass
class OrbSession:
    params: OrbParams
    costs: Costs = field(default_factory=Costs)
    day: str = ""
    open_minute: int = OPEN_NY

    # état
    range_high: float = -math.inf
    range_low: float = math.inf
    range_bars: int = 0
    range_done: bool = False
    done: bool = False
    state: str = "range"           # range | armed | pending_market | pending_fvg | in_trade | done
    allow_long: bool = True
    allow_short: bool = True
    trades: list[Trade] = field(default_factory=list)
    open_trade: Trade | None = None
    _pending_dir: int = 0
    _break_bar: Bar | None = None
    _zone_top: float = 0.0         # FVG : bord proche (entrée)
    _zone_bottom: float = 0.0      # FVG : bord éloigné
    _hist: list[Bar] = field(default_factory=list)   # 3 dernières bougies (détection FVG)
    _last_exit_t: int = -1
    events: list[str] = field(default_factory=list)   # journal lisible (temps réel)

    # ------------------------------------------------------------------ helpers

    @property
    def cutoff(self) -> int:
        return hhmm_to_minutes(self.params.entry_cutoff)

    @property
    def flat_at(self) -> int:
        return hhmm_to_minutes(self.params.flat_at)

    @property
    def range_mid(self) -> float:
        return (self.range_high + self.range_low) / 2

    def _log(self, bar: Bar, msg: str) -> None:
        self.events.append(f"{bar.t // 60:02d}:{bar.t % 60:02d} {msg}")

    def _ma_ok(self, direction: int, bar: Bar) -> bool:
        if not self.params.ma:
            return True
        if math.isnan(bar.ema):
            return False
        return bar.c > bar.ema if direction > 0 else bar.c < bar.ema

    def _trades_left(self) -> bool:
        return len(self.trades) < self.params.max_trades

    # ------------------------------------------------------------------ main entry point

    def on_bar(self, bar: Bar) -> list[Trade]:
        """Traite une bougie 1 min clôturée ; renvoie les trades clôturés pendant cette bougie."""
        closed: list[Trade] = []
        if self.done or bar.t < self.open_minute:
            return closed
        self._hist.append(bar)
        if len(self._hist) > 3:
            del self._hist[0]
        # 1) construction du range ---------------------------------------------------------------------
        if bar.t < self.open_minute + self.params.range_minutes:
            self.range_high = max(self.range_high, bar.h)
            self.range_low = min(self.range_low, bar.l)
            self.range_bars += 1
            return closed
        if not self.range_done:
            self.range_done = True
            if self.range_bars == 0 or not math.isfinite(self.range_high):
                self._log(bar, "pas de données pendant le range : journée ignorée")
                self.done = True
                self.state = "done"
                return closed
            self.state = "armed"
            self._log(bar, f"range {self.params.range_minutes} min : haut {self.range_high:.3f} bas {self.range_low:.3f}")
        # 2) position ouverte : sorties ------------------------------------------------------------------
        if self.open_trade is not None:
            tr = self._manage_open(bar)
            if tr is not None:
                closed.append(tr)
        # 3) fin de journée ----------------------------------------------------------------------------
        if bar.t >= self.flat_at:
            self.done = True
            self.state = "done"
            return closed
        if self.open_trade is not None:
            return closed
        # 4) ordre au marché en attente (variante « close ») : exécution à l'ouverture de cette bougie -----
        if self.state == "pending_market":
            self._fill_market(bar)
            if self.open_trade is not None:
                tr = self._manage_open(bar, entry_bar=True)
                if tr is not None:
                    closed.append(tr)
            return closed
        # 5) retest FVG en attente ---------------------------------------------------------------------
        if self.state == "pending_fvg":
            self._check_fvg_retest(bar)
            if self.open_trade is not None:
                tr = self._manage_open(bar, entry_bar=True)
                if tr is not None:
                    closed.append(tr)
            return closed
        if self.state == "seeking_fvg":
            self._seek_fvg(bar)
            return closed
        # 6) armé : détection de cassure ---------------------------------------------------------------
        if self.state == "armed":
            if bar.t == self._last_exit_t:
                return closed  # pas de nouvelle entrée dans la bougie de sortie
            # ré-armement d'un sens après un trade dans ce sens : il faut une clôture dans le range
            if self.range_low <= bar.c <= self.range_high:
                self.allow_long = self.allow_short = True
            if bar.t >= self.cutoff or not self._trades_left():
                self.done = True   # plus aucune entrée possible aujourd'hui
                self.state = "done"
                return closed
            direction = 0
            if bar.c > self.range_high and self.allow_long:
                direction = 1
            elif bar.c < self.range_low and self.allow_short:
                direction = -1
            if direction and self._ma_ok(direction, bar):
                self._break_bar = bar
                self._pending_dir = direction
                if self.params.confirm == "close":
                    self.state = "pending_market"
                    self._log(bar, f"cassure {'haussière' if direction > 0 else 'baissière'} (clôture {bar.c:.3f}) → ordre au marché à la prochaine bougie")
                else:
                    self.state = "seeking_fvg"
                    self._log(bar, f"cassure {'haussière' if direction > 0 else 'baissière'} (clôture {bar.c:.3f}) → recherche d'une FVG")
                    self._seek_fvg(bar)
            elif direction:
                self._log(bar, "cassure ignorée : filtre EMA défavorable")
        return closed

    # ------------------------------------------------------------------ entries

    def _stop_level(self, direction: int, structure_level: float) -> float:
        if self.params.stop == "opposite":
            return self.range_low if direction > 0 else self.range_high
        if self.params.stop == "mid":
            return self.range_mid
        return structure_level

    def _open(self, bar: Bar, direction: int, entry_price: float, stop: float, signal: str) -> None:
        risk = (entry_price - stop) if direction > 0 else (stop - entry_price)
        if risk <= max(self.costs.min_risk, 1e-12):
            self._log(bar, f"entrée ignorée : risque {risk:.4f} trop faible/invalide (entrée {entry_price:.3f}, stop {stop:.3f})")
            self.state = "armed"
            if direction > 0:
                self.allow_long = False
            else:
                self.allow_short = False
            return
        tp = entry_price + direction * self.params.rr * risk
        tp1 = entry_price + direction * risk if (self.params.partial and self.params.rr > 1) else None
        self.open_trade = Trade(day=self.day, direction=direction, entry_t=bar.t, entry_price=entry_price, stop_price=stop, risk=risk,
                                tp_price=tp, tp1_price=tp1, entry_ts=bar.ts, signal=signal)
        self.state = "in_trade"
        self._log(bar, f"{'ACHAT' if direction > 0 else 'VENTE'} {signal} @ {entry_price:.3f} stop {stop:.3f} (R = {risk:.3f}) objectif {tp:.3f}"
                  + (f" TP1 {tp1:.3f}" if tp1 else ""))

    def _fill_market(self, bar: Bar) -> None:
        d, bb = self._pending_dir, self._break_bar
        assert bb is not None
        if d > 0:
            entry = bar.o + self.costs.spread + self.costs.slippage
            stop = self._stop_level(d, bb.l)
        else:
            entry = bar.o - self.costs.slippage
            stop = self._stop_level(d, bb.h)
        self._open(bar, d, entry, stop, "close")

    def _seek_fvg(self, bar: Bar) -> None:
        d = self._pending_dir
        # abandon si le prix reclôture dans le range avant qu'une FVG n'apparaisse
        if (d > 0 and bar.c < self.range_high) or (d < 0 and bar.c > self.range_low):
            self._log(bar, "retour dans le range avant FVG : signal abandonné")
            self.state = "armed"
            return
        if bar.t >= self.cutoff:
            self.state = "armed"
            return
        if len(self._hist) < 3:
            return
        a, _, c = self._hist[-3], self._hist[-2], self._hist[-1]
        if d > 0 and c.l > a.h:
            self._zone_top, self._zone_bottom = c.l, a.h
        elif d < 0 and c.h < a.l:
            self._zone_top, self._zone_bottom = c.h, a.l
        else:
            return
        self.state = "pending_fvg"
        self._log(bar, f"FVG {'haussière' if d > 0 else 'baissière'} [{min(self._zone_top, self._zone_bottom):.3f} ; {max(self._zone_top, self._zone_bottom):.3f}] → limite au bord {self._zone_top:.3f}")

    def _check_fvg_retest(self, bar: Bar) -> None:
        d = self._pending_dir
        if bar.t >= self.cutoff:
            self._log(bar, "heure limite : retest FVG annulé")
            self.state = "armed"
            return
        if d > 0:
            if bar.l <= self._zone_top:
                fill = min(bar.o, self._zone_top)  # ouverture en gap sous la limite : exécuté à l'ouverture
                entry = fill + self.costs.spread
                self._open(bar, d, entry, self._stop_level(d, self._zone_bottom), "fvg")
            elif bar.c < self._zone_bottom:  # (ne peut arriver qu'avec un gap) zone traversée sans retest
                self.state = "armed"
        else:
            if bar.h >= self._zone_top:
                fill = max(bar.o, self._zone_top)
                entry = fill
                self._open(bar, d, entry, self._stop_level(d, self._zone_bottom), "fvg")
            elif bar.c > self._zone_bottom:
                self.state = "armed"

    # ------------------------------------------------------------------ exits

    def _close(self, bar: Bar, price: float, reason: str, fraction: float = 1.0) -> Trade | None:
        tr = self.open_trade
        assert tr is not None
        d = tr.direction
        pnl_unit = (price - tr.entry_price) * d
        if fraction < 1.0:  # TP partiel : moitié sortie, stop au point d'entrée
            tr.partial_done = True
            tr.partial_pnl = pnl_unit * fraction
            tr.stop_price = tr.entry_price
            self._log(bar, f"TP1 : {int(fraction * 100)} % clôturés @ {price:.3f}, stop déplacé au point d'entrée {tr.entry_price:.3f}")
            return None
        rest = 1.0 - (0.5 if tr.partial_done else 0.0)
        total = pnl_unit * rest + tr.partial_pnl
        tr.exit_t, tr.exit_price, tr.exit_reason, tr.exit_ts = bar.t, price, reason, bar.ts
        tr.pnl_per_unit = total
        tr.r_multiple = total / tr.risk
        self.trades.append(tr)
        self.open_trade = None
        self._last_exit_t = bar.t
        self.state = "armed" if self._trades_left() else "done"
        if d > 0:
            self.allow_long = False
        else:
            self.allow_short = False
        if self.range_low <= bar.c <= self.range_high:  # la bougie de sortie clôture dans le range : les deux sens sont ré-armés
            self.allow_long = self.allow_short = True
        if self.state == "done":
            self.done = True
        self._log(bar, f"sortie {reason} @ {price:.3f} → {tr.r_multiple:+.2f} R")
        return tr

    def _manage_open(self, bar: Bar, entry_bar: bool = False) -> Trade | None:
        tr = self.open_trade
        assert tr is not None
        d, sp, sl = tr.direction, self.costs.spread, self.costs.slippage
        # excursions (en R) pour le diagnostic
        if d > 0:
            tr.mae_r = min(tr.mae_r, (bar.l - tr.entry_price) / tr.risk)
            tr.mfe_r = max(tr.mfe_r, (bar.h - tr.entry_price) / tr.risk)
        else:
            tr.mae_r = min(tr.mae_r, (tr.entry_price - (bar.h + sp)) / tr.risk)
            tr.mfe_r = max(tr.mfe_r, (tr.entry_price - (bar.l + sp)) / tr.risk)
        # 1) stop (prioritaire)
        if d > 0 and bar.l <= tr.stop_price:
            fill = min(bar.o, tr.stop_price) - sl
            return self._close(bar, fill, "be" if tr.partial_done else "sl")
        if d < 0 and bar.h + sp >= tr.stop_price:  # le rachat se fait à l'ask
            fill = max(bar.o + sp, tr.stop_price) + sl
            return self._close(bar, fill, "be" if tr.partial_done else "sl")
        if entry_bar:
            return None  # dans la bougie d'entrée, seul le stop est vérifié (hypothèse défavorable)
        # 2) objectif partiel
        if tr.tp1_price is not None and not tr.partial_done:
            if (d > 0 and bar.h >= tr.tp1_price) or (d < 0 and bar.l + sp <= tr.tp1_price):
                self._close(bar, tr.tp1_price, "tp1", fraction=0.5)
        # 3) objectif final
        if (d > 0 and bar.h >= tr.tp_price) or (d < 0 and bar.l + sp <= tr.tp_price):
            return self._close(bar, tr.tp_price, "tp2" if tr.partial_done else "tp")
        # 4) fin de journée : au marché sur la clôture
        if bar.t >= self.flat_at:
            fill = (bar.c - sl) if d > 0 else (bar.c + sp + sl)
            return self._close(bar, fill, "time")
        return None
