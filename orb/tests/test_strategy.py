"""Scénarios synthétiques dont le résultat est connu à l'avance : chaque règle de la machine à états est vérifiée."""
import math

import pytest

from orbbot.strategy.orb import OPEN_NY, Bar, Costs, OrbSession
from orbbot.strategy.params import FULL_GRID, QUICK_GRID, OrbParams, grid

SPREAD, SLIP = 0.30, 0.05


def bars_from(path, start_t=OPEN_NY, ema=math.nan):
    """path : liste de tuples (o, h, l, c) → bougies consécutives d'une minute à partir de 09:30 NY."""
    return [Bar(start_t + i, *ohlc, ema) for i, ohlc in enumerate(path)]


def run(params, path, costs=Costs(SPREAD, SLIP)):
    s = OrbSession(params=params, costs=costs, day="2025-01-02")
    for b in bars_from(path):
        s.on_bar(b)
        if s.done:
            break
    return s


def flat_range(n, hi=2000.0, lo=1990.0):
    """n bougies qui dessinent un range [lo, hi]."""
    return [(1995.0, hi, lo, 1995.0)] * n


def test_long_breakout_close_hits_tp_rr1():
    p = OrbParams(range_minutes=5, confirm="close", rr=1.0, stop="opposite")
    path = flat_range(5) + [(1996, 2003, 1995, 2002)]           # cassure : clôture 2002 > 2000
    path += [(2002, 2002.5, 2001.5, 2002)]                     # entrée au marché à l'ouverture 2002 (+ spread + slippage)
    entry = 2002 + SPREAD + SLIP
    risk = entry - 1990.0
    tp = entry + risk
    path += [(2002, tp + 1, 2001, tp + 0.5)]                   # objectif touché
    s = run(p, path)
    assert len(s.trades) == 1
    t = s.trades[0]
    assert t.direction == 1 and t.signal == "close"
    assert t.entry_price == pytest.approx(entry) and t.stop_price == 1990.0 and t.tp_price == pytest.approx(tp)
    assert t.exit_reason == "tp" and t.r_multiple == pytest.approx(1.0)
    assert s.done  # max_trades = 1 ⇒ journée terminée


def test_long_stop_loss_pays_slippage():
    p = OrbParams(range_minutes=5, confirm="close", rr=2.0, stop="structure")
    path = flat_range(5) + [(1996, 2003, 1994, 2002)]           # bougie de cassure, plus bas 1994 = stop structure
    path += [(2002, 2002.5, 2001.5, 2002)]                     # entrée 2002.35
    path += [(2002, 2002, 1993, 1993.5)]                       # stop 1994 touché
    s = run(p, path)
    t = s.trades[0]
    entry = 2002 + SPREAD + SLIP
    risk = entry - 1994
    assert t.stop_price == 1994.0
    assert t.exit_price == pytest.approx(1994 - SLIP)
    assert t.r_multiple == pytest.approx(-(risk + SLIP) / risk)
    assert t.r_multiple < -1.0


def test_short_breakout_symmetric():
    p = OrbParams(range_minutes=5, confirm="close", rr=1.0, stop="opposite")
    path = flat_range(5) + [(1994, 1995, 1987, 1988)]           # clôture 1988 < 1990
    path += [(1988, 1988.5, 1987.5, 1988)]                     # vente au marché 1988 − slippage
    entry = 1988 - SLIP
    risk = 2000.0 - entry
    tp = entry - risk                                          # niveau d'achat (ask)
    path += [(1988, 1988, tp - SPREAD - 1, tp - SPREAD)]       # bid ≤ tp − spread ⇒ ask ≤ tp
    s = run(p, path)
    t = s.trades[0]
    assert t.direction == -1 and t.exit_reason == "tp"
    assert t.r_multiple == pytest.approx(1.0)


def test_stop_has_priority_when_both_hit_in_same_bar():
    p = OrbParams(range_minutes=5, confirm="close", rr=1.0, stop="opposite")
    path = flat_range(5) + [(1996, 2003, 1995, 2002), (2002, 2002.5, 2001.5, 2002)]
    path += [(2002, 2030, 1980, 2010)]                         # touche objectif ET stop
    s = run(p, path)
    assert s.trades[0].exit_reason == "sl"


def test_fvg_retest_entry_and_structure_stop():
    p = OrbParams(range_minutes=5, confirm="fvg", rr=1.0, stop="structure")
    path = flat_range(5)                                        # bougies 0-4 (range 1990-2000)
    path += [(1996, 1998, 1995, 1997)]                          # bougie 5 : dans le range (sera « a » du triplet)
    path += [(1997, 2001, 1996.5, 2000.5)]                      # bougie 6 : cassure (clôture 2000.5 > 2000) ; triplet (4,5,6) : low 1996.5 ≤ high(4)=2000 ⇒ pas de FVG
    path += [(2000.5, 2006, 2000, 2005)]                        # bougie 7 : triplet (5,6,7) : low 2000 > high(5)=1998 ⇒ FVG [1998 ; 2000]
    path += [(2005, 2006, 2003, 2004)]                          # bougie 8 : pas de retest
    path += [(2004, 2004.5, 1999.5, 2001)]                      # bougie 9 : retest (low ≤ 2000) ⇒ achat limite 2000 + spread
    entry = 2000 + SPREAD
    risk = entry - 1998.0
    tp = entry + risk
    path += [(2001, tp + 0.5, 2000.5, tp)]                      # objectif
    s = run(p, path)
    assert "FVG haussière [1998.000 ; 2000.000]" in " ".join(s.events)
    assert len(s.trades) == 1
    t = s.trades[0]
    assert t.signal == "fvg" and t.entry_price == pytest.approx(entry) and t.stop_price == 1998.0
    assert t.exit_reason == "tp" and t.r_multiple == pytest.approx(1.0)


def test_fvg_signal_abandoned_when_price_closes_back_in_range():
    p = OrbParams(range_minutes=5, confirm="fvg", rr=1.0, stop="structure")
    path = flat_range(5) + [(1996, 2003, 1995, 2002)]           # cassure sans FVG (triplet avec la bougie de range)
    path += [(2002, 2002, 1996, 1997)]                          # reclôture dans le range ⇒ abandon
    path += [(1997, 1998, 1996, 1997)] * 3
    s = run(p, path)
    assert s.trades == [] and s.state == "armed" and s.allow_long


def test_partial_tp1_then_tp2_and_break_even():
    p = OrbParams(range_minutes=5, confirm="close", rr=2.0, stop="opposite", partial=True)
    base = flat_range(5) + [(1996, 2003, 1995, 2002), (2002, 2002.5, 2001.5, 2002)]
    entry = 2002 + SPREAD + SLIP
    risk = entry - 1990.0
    tp1, tp2 = entry + risk, entry + 2 * risk
    # a) TP1 puis TP2
    s = run(p, base + [(2002, tp1 + 0.2, 2001, tp1)] + [(tp1, tp2 + 0.2, tp1 - 0.1, tp2)])
    t = s.trades[0]
    assert t.partial_done and t.exit_reason == "tp2"
    assert t.r_multiple == pytest.approx(0.5 * 1 + 0.5 * 2)
    # b) TP1 puis retour au point d'entrée ⇒ break-even (moitié à +1R, moitié à −slippage)
    s = run(p, base + [(2002, tp1 + 0.2, 2001, tp1)] + [(tp1, tp1, entry - 1, entry - 0.5)])
    t = s.trades[0]
    assert t.exit_reason == "be"
    assert t.r_multiple == pytest.approx(0.5 - 0.5 * SLIP / risk)


def test_time_exit_at_flat_time():
    p = OrbParams(range_minutes=5, confirm="close", rr=3.0, stop="opposite", flat_at="09:45")
    path = flat_range(5) + [(1996, 2003, 1995, 2002), (2002, 2002.5, 2001.5, 2002)]
    path += [(2002, 2002.5, 2001.5, 2002.2)] * 20
    s = run(p, path)
    t = s.trades[0]
    assert t.exit_reason == "time" and t.exit_t == 9 * 60 + 45
    assert t.exit_price == pytest.approx(2002.2 - SLIP)


def test_no_entry_after_cutoff_and_session_done():
    p = OrbParams(range_minutes=5, confirm="close", rr=1.0, stop="opposite", entry_cutoff="09:40")
    path = flat_range(5) + [(1995, 1999, 1991, 1995)] * 5 + [(1996, 2003, 1995, 2002)] * 3
    s = run(p, path)
    assert s.trades == [] and s.done


def test_ma_filter_blocks_counter_trend():
    p = OrbParams(range_minutes=5, confirm="close", rr=1.0, stop="opposite", ma=50)
    path = flat_range(5) + [(1996, 2003, 1995, 2002), (2002, 2002.5, 2001.5, 2002), (2002, 2030, 2001, 2029)]
    s_block = OrbSession(params=p, costs=Costs(SPREAD, SLIP), day="d")
    for b in bars_from(path, ema=2050.0):   # prix sous l'EMA ⇒ pas d'achat
        s_block.on_bar(b)
    assert s_block.trades == [] and any("filtre EMA" in e for e in s_block.events)
    s_ok = OrbSession(params=p, costs=Costs(SPREAD, SLIP), day="d")
    for b in bars_from(path, ema=1950.0):
        s_ok.on_bar(b)
    assert len(s_ok.trades) == 1


def test_second_trade_requires_close_back_inside_range_or_opposite_side():
    p = OrbParams(range_minutes=5, confirm="close", rr=1.0, stop="opposite", max_trades=2)
    path = flat_range(5) + [(1996, 2003, 1995, 2002), (2002, 2002.5, 2001.5, 2002)]
    path += [(2002, 2002, 1989, 1989.5)]                       # stop du premier trade (long)
    path += [(1989.5, 1991, 1988, 1988.5)]                     # clôture sous le range ⇒ short autorisé (sens opposé)
    path += [(1988.5, 1989, 1988, 1988.5)]                     # entrée short
    path += [(1988.5, 1988.5, 1975, 1976)]                     # objectif short
    s = run(p, path)
    assert [t.direction for t in s.trades] == [1, -1]
    assert s.trades[1].exit_reason == "tp" and s.done


def test_same_direction_reentry_blocked_until_close_inside_range():
    p = OrbParams(range_minutes=5, confirm="close", rr=1.0, stop="mid", max_trades=2)
    path = flat_range(5) + [(1996, 2003, 1995, 2002), (2002, 2002.5, 2001.5, 2002)]
    path += [(2002, 2002, 1994, 1994.5)]                       # stop (milieu 1995) touché, clôture dans le range
    path += [(1994.5, 2004, 1994, 2003)]                       # nouvelle cassure haussière après clôture dans le range ⇒ autorisée
    path += [(2003, 2003.5, 2002.5, 2003)]
    path += [(2003, 2015, 2002, 2014)]
    s = run(p, path)
    assert [t.direction for t in s.trades] == [1, 1]


def test_missing_range_data_skips_day():
    p = OrbParams(range_minutes=5)
    s = OrbSession(params=p, costs=Costs(), day="d")
    s.on_bar(Bar(OPEN_NY + 10, 1, 1, 1, 1))   # première bougie après la fin du range
    assert s.done and s.trades == []


def test_grid_sizes_and_keys_unique():
    g = grid(FULL_GRID)
    assert len(g) == 1296 - 3 * 2 * 3 * 3 * 2 * 2 * 1  # les variantes partial=True avec rr=1 sont fusionnées
    assert len({p.key() for p in g}) == len(g)
    assert len(grid(QUICK_GRID)) == 32
    p = OrbParams()
    assert p.key() == "R30_close_rr1_opposite_ma0_p0_n1_cut1130"
