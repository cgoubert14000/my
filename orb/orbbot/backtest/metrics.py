"""Mesures de performance (en R) et intervalles de confiance par bootstrap."""
from __future__ import annotations

import math
from collections import defaultdict

import numpy as np

from ..strategy.orb import Trade


def profit_factor(r: np.ndarray) -> float:
    gains = float(r[r > 0].sum())
    losses = float(-r[r < 0].sum())
    if losses == 0:
        return math.inf if gains > 0 else 0.0
    return gains / losses


def max_drawdown(r: np.ndarray) -> float:
    if r.size == 0:
        return 0.0
    eq = np.cumsum(r)
    peak = np.maximum.accumulate(np.r_[0.0, eq])[1:]
    return float(np.max(peak - eq))


def longest_losing_streak(r: np.ndarray) -> int:
    best = cur = 0
    for x in r:
        cur = cur + 1 if x <= 0 else 0
        best = max(best, cur)
    return best


def summarize(trades: list[Trade], label: str = "") -> dict:
    r = np.array([t.r_multiple for t in trades if t.r_multiple is not None], dtype=float)
    n = int(r.size)
    if n == 0:
        return {"label": label, "n": 0, "win_rate": None, "profit_factor": None, "expectancy_r": None, "total_r": 0.0,
                "max_drawdown_r": 0.0, "avg_win_r": None, "avg_loss_r": None, "longest_losing_streak": 0, "days": 0}
    wins = r[r > 0]
    losses = r[r < 0]
    days = len({t.day for t in trades})
    return {
        "label": label,
        "n": n,
        "days": days,
        "win_rate": float(wins.size / n),
        "profit_factor": profit_factor(r),
        "expectancy_r": float(r.mean()),
        "std_r": float(r.std(ddof=1)) if n > 1 else None,
        "total_r": float(r.sum()),
        "max_drawdown_r": max_drawdown(r),
        "avg_win_r": float(wins.mean()) if wins.size else None,
        "avg_loss_r": float(losses.mean()) if losses.size else None,
        "longest_losing_streak": longest_losing_streak(r),
        "exits": dict(sorted(_count(t.exit_reason for t in trades).items())),
        "longs": int(sum(1 for t in trades if t.direction > 0)),
        "shorts": int(sum(1 for t in trades if t.direction < 0)),
    }


def _count(it) -> dict[str, int]:
    d: dict[str, int] = defaultdict(int)
    for x in it:
        d[x] += 1
    return d


def bootstrap_ci(trades: list[Trade], n_boot: int = 1000, seed: int = 7, level: float = 0.95) -> dict:
    """IC par bootstrap (rééchantillonnage des trades avec remise) du profit factor et de l'espérance."""
    r = np.array([t.r_multiple for t in trades if t.r_multiple is not None], dtype=float)
    n = r.size
    if n < 10:
        return {"n": int(n), "pf_low": None, "pf_high": None, "exp_low": None, "exp_high": None, "p_pf_below_1": None}
    rng = np.random.default_rng(seed)
    idx = rng.integers(0, n, size=(n_boot, n))
    samples = r[idx]
    gains = np.where(samples > 0, samples, 0.0).sum(axis=1)
    losses = -np.where(samples < 0, samples, 0.0).sum(axis=1)
    with np.errstate(divide="ignore", invalid="ignore"):
        pf = np.where(losses > 0, gains / np.where(losses > 0, losses, 1.0), np.inf)
    exp = samples.mean(axis=1)
    a = (1 - level) / 2
    return {
        "n": int(n),
        "pf_low": float(np.quantile(pf, a)),
        "pf_high": float(np.quantile(pf, 1 - a)),
        "exp_low": float(np.quantile(exp, a)),
        "exp_high": float(np.quantile(exp, 1 - a)),
        "p_pf_below_1": float(np.mean(pf < 1.0)),
    }


def by_year(trades: list[Trade]) -> dict[str, dict]:
    groups: dict[str, list[Trade]] = defaultdict(list)
    for t in trades:
        groups[t.day[:4]].append(t)
    return {y: summarize(groups[y], y) for y in sorted(groups)}


def monthly_r(trades: list[Trade]) -> dict[str, float]:
    out: dict[str, float] = defaultdict(float)
    for t in trades:
        out[t.day[:7]] += float(t.r_multiple or 0.0)
    return dict(sorted(out.items()))
