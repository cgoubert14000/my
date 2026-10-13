"""Décodage Dukascopy, découpage des séances New York (heure d'été/hiver), grille parallèle, rapport, cohérence
rejeu temps réel == backtest, politique de risque."""
import asyncio
import datetime as dt
import json
import pathlib

import numpy as np
import pandas as pd
import pytest

from orbbot.backtest.engine import prepare_sessions, run_grid, run_variants
from orbbot.backtest.metrics import bootstrap_ci, max_drawdown, profit_factor, summarize
from orbbot.backtest.report import evaluate, to_markdown, write_outputs
from orbbot.data.dukascopy import INSTRUMENTS, decode_day, encode_day_for_tests
from orbbot.data.synthetic import random_walk_minutes
from orbbot.live.engine import LiveEngine
from orbbot.live.brokers import PaperBroker
from orbbot.live.feeds import ReplayFeed
from orbbot.live.policy import DayState, RiskPolicy, can_enter, position_units
from orbbot.strategy.orb import Costs
from orbbot.strategy.params import QUICK_GRID, VIDEO_CLAIM, OrbParams, grid


# ---------------------------------------------------------------- données

def test_decode_day_roundtrip_and_order_check():
    day = dt.date(2025, 3, 3)
    bars = [(60 * i, 2000.0 + i, 2000.5 + i, 1999.5 + i, 2001.0 + i, 12.5) for i in range(100)]  # (s, open, close, low, high, vol)
    raw = encode_day_for_tests(bars, 1000)
    df = decode_day(raw, day, 1000, INSTRUMENTS["XAUUSD"]["plausible"])
    assert len(df) == 100 and list(df.columns) == ["open", "high", "low", "close", "volume"]
    assert df.index[0] == pd.Timestamp("2025-03-03 00:00", tz="UTC") and df.index[1] - df.index[0] == pd.Timedelta(minutes=1)
    assert df["open"].iloc[3] == pytest.approx(2003.0) and df["close"].iloc[3] == pytest.approx(2003.5)
    assert df["low"].iloc[3] == pytest.approx(2002.5) and df["high"].iloc[3] == pytest.approx(2004.0)
    assert (df["low"] <= df[["open", "close"]].min(axis=1)).all() and (df["high"] >= df[["open", "close"]].max(axis=1)).all()
    # échelle incohérente ⇒ refus explicite (jamais de données silencieusement fausses)
    with pytest.raises(ValueError, match="plausible"):
        decode_day(raw, day, 100_000, INSTRUMENTS["XAUUSD"]["plausible"])
    # fichier vide ⇒ journée vide
    assert decode_day(b"", day, 1000, (0, 1)).empty


def test_sessions_respect_new_york_dst():
    # 2025-01-15 (hiver : 09:30 NY = 14:30 UTC) et 2025-07-15 (été : 09:30 NY = 13:30 UTC)
    df = pd.concat([random_walk_minutes(dt.date(2025, 1, 15), 1, seed=3), random_walk_minutes(dt.date(2025, 7, 15), 1, seed=4)])
    sessions = prepare_sessions(df, with_ts=True)
    assert [s.day for s in sessions] == ["2025-01-15", "2025-07-15"]
    winter, summer = sessions
    assert winter.t[0] == 570 and winter.ts[0] == "2025-01-15T14:30Z"
    assert summer.t[0] == 570 and summer.ts[0] == "2025-07-15T13:30Z"
    assert winter.t[-1] == 16 * 60 - 1 and len(winter.t) == 390
    assert np.isfinite(winter.ema[200]).all()


# ---------------------------------------------------------------- backtest

@pytest.fixture(scope="module")
def synthetic_sessions():
    df = random_walk_minutes(dt.date(2024, 1, 1), 40, seed=11)
    return df, prepare_sessions(df)


def test_grid_parallel_matches_sequential(synthetic_sessions):
    _, sessions = synthetic_sessions
    variants = grid(QUICK_GRID)
    costs = Costs(0.30, 0.05, 0.30)
    seq = run_variants(sessions, variants, costs)
    par = run_grid(sessions, variants, costs, workers=2)
    assert seq.keys() == par.keys()
    for k in seq:
        assert [t.r_multiple for t in seq[k]] == [t.r_multiple for t in par[k]]
    assert sum(len(v) for v in seq.values()) > 0


def test_metrics_and_bootstrap():
    r = np.array([1.0, -1.0, 2.0, -1.0, -1.0, 1.0])
    assert profit_factor(r) == pytest.approx(4 / 3)
    assert max_drawdown(r) == pytest.approx(2.0)
    from orbbot.strategy.orb import Trade
    trades = [Trade("2024-01-0%d" % (i % 9 + 1), 1, 600, 1, 0, 1, 2, r_multiple=float(x), exit_reason="tp" if x > 0 else "sl") for i, x in enumerate(np.tile(r, 10))]
    s = summarize(trades)
    assert s["n"] == 60 and s["win_rate"] == pytest.approx(0.5) and s["profit_factor"] == pytest.approx(4 / 3)
    b = bootstrap_ci(trades, n_boot=300)
    assert b["pf_low"] < 4 / 3 < b["pf_high"] and 0 <= b["p_pf_below_1"] <= 1


def test_report_on_synthetic_data_is_honest(tmp_path, synthetic_sessions):
    _, sessions = synthetic_sessions
    variants = grid(QUICK_GRID) + [VIDEO_CLAIM]
    costs = Costs(0.30, 0.05, 0.30)
    results = run_variants(sessions, variants, costs)
    days = [s.day for s in sessions]
    ev = evaluate(results, variants, days, split_share=0.6)
    assert ev["variants"] == len(variants) and ev["days"]["n"] == len(days)
    assert ev["status"].startswith("FIABILITÉ NON DÉMONTRÉE")  # 40 jours de bruit : jamais « robuste »
    md = to_markdown(ev, "SYNTHETIC", {"spread": 0.3, "slippage": 0.05})
    assert "biais de sélection" in md and "Verdict" in md
    md_path, js_path = write_outputs(ev, "SYNTHETIC", {"spread": 0.3, "slippage": 0.05}, tmp_path, "t1", results)
    data = json.loads(js_path.read_text(encoding="utf-8"))  # JSON strict (pas d'Infinity)
    assert data["status"] == ev["status"] and len(data["all_rows"]) == len(variants)
    assert (tmp_path / "latest_SYNTHETIC.md").exists()


# ---------------------------------------------------------------- temps réel : rejeu == backtest

def test_live_replay_matches_backtest(tmp_path, synthetic_sessions):
    df, sessions = synthetic_sessions
    params = OrbParams(range_minutes=15, confirm="close", rr=2.0, stop="opposite", ma=50, partial=True, max_trades=2)
    costs = Costs(0.30, 0.05, 0.30)
    bt = run_variants(sessions, [params], costs)[params.key()]
    assert len(bt) >= 5
    policy = RiskPolicy(enabled=True, mode="paper", max_trades_per_day=2, max_daily_loss_r=100, max_units=100, paper_equity=10_000)
    eng = LiveEngine(params=params, costs=costs, policy=policy, broker=PaperBroker(10_000), journal_dir=tmp_path / "j", repo_root=tmp_path)
    asyncio.run(eng.run(ReplayFeed(df)))
    live_r = [round(t.r_multiple, 9) for t in eng.model_trades]
    assert live_r == [round(t.r_multiple, 9) for t in bt]
    assert [t.day for t in eng.model_trades] == [t.day for t in bt]
    assert all(e.executed for e in eng.executed)
    # le compte fictif bouge exactement du P&L modèle × unités
    expected = sum(e.model.pnl_per_unit * e.units for e in eng.executed)
    assert eng.broker.equity - 10_000 == pytest.approx(expected)
    state = json.loads((tmp_path / "j" / "state.json").read_text(encoding="utf-8"))
    assert state["executed_trades"] == len(bt) and state["policy_enabled"] is True
    lines = [json.loads(x) for x in (tmp_path / "j" / "journal.jsonl").read_text(encoding="utf-8").splitlines()]
    assert lines[0]["event"] == "start" and lines[0]["policy_sha256"] == policy.sha256()
    assert sum(1 for x in lines if x["event"] == "entry") == len(bt)


def test_live_policy_disabled_refuses_but_keeps_tracking(tmp_path, synthetic_sessions):
    df, sessions = synthetic_sessions
    params = OrbParams(range_minutes=15, confirm="close", rr=1.0, stop="opposite")
    costs = Costs(0.30, 0.05, 0.30)
    bt = run_variants(sessions, [params], costs)[params.key()]
    eng = LiveEngine(params=params, costs=costs, policy=RiskPolicy(enabled=False), broker=PaperBroker(), journal_dir=tmp_path / "j", repo_root=tmp_path)
    asyncio.run(eng.run(ReplayFeed(df)))
    assert len(eng.model_trades) == len(bt) and not any(e.executed for e in eng.executed)
    assert eng.broker.equity == 10_000.0


def test_kill_switch_closes_open_position(tmp_path):
    df = random_walk_minutes(dt.date(2024, 2, 5), 3, seed=5)
    params = OrbParams(range_minutes=5, confirm="close", rr=3.0, stop="opposite")
    policy = RiskPolicy(enabled=True, max_units=100)
    eng = LiveEngine(params=params, costs=Costs(0.3, 0.05, 0.3), policy=policy, broker=PaperBroker(), journal_dir=tmp_path / "j", repo_root=tmp_path)
    stop_file = tmp_path / policy.kill_switch_file

    async def scenario():
        async for lb in ReplayFeed(df).bars():
            await eng.on_bar(lb)
            if eng._open and eng._open.executed and not stop_file.exists():
                stop_file.parent.mkdir(parents=True, exist_ok=True)
                stop_file.write_text("stop")
    asyncio.run(scenario())
    events = [json.loads(x)["event"] for x in (tmp_path / "j" / "journal.jsonl").read_text(encoding="utf-8").splitlines()]
    assert "entry" in events and "kill_switch_close" in events
    assert all(p.closed for p in eng.broker.positions.values())
    assert events.count("entry") == 1  # plus aucune entrée après le kill switch


def test_policy_rules_and_sizing():
    pol = RiskPolicy(enabled=True, max_trades_per_day=2, max_daily_loss_r=2.0, max_consecutive_losses=3)
    now = dt.datetime(2025, 3, 3, 10, 0, tzinfo=dt.UTC)
    assert can_enter(pol, DayState(), False, now) == (True, "ok")
    assert not can_enter(pol, DayState(trades=2), False, now)[0]
    assert not can_enter(pol, DayState(r_total=-2.0), False, now)[0]
    assert not can_enter(pol, DayState(consecutive_losses=3), False, now)[0]
    assert not can_enter(pol, DayState(), True, now)[0]
    assert not can_enter(pol, DayState(), False, dt.datetime(2025, 3, 1, 10, 0, tzinfo=dt.UTC))[0]  # samedi
    assert not can_enter(RiskPolicy(enabled=False), DayState(), False, now)[0]
    # 10 000 × 0,5 % = 50 de risque ; 12,5 $ par unité ⇒ 4 unités
    assert position_units(10_000, 0.5, 12.5, max_units=5) == 4.0
    assert position_units(10_000, 0.5, 12.5, max_units=3) == 3.0
    assert position_units(10_000, 0.5, 80.0, max_units=5) == 0.0   # trop petit ⇒ pas de trade
    assert position_units(10_000, 0.5, 0.0, max_units=5) == 0.0
    assert len(pol.sha256()) == 16
    pathlib.Path  # (import utilisé par d'autres tests)
