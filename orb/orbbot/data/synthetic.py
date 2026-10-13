"""Séries 1 minute SYNTHÉTIQUES (marche aléatoire) pour les tests et les démonstrations hors ligne.
Elles ne contiennent aucune information de marché : tout résultat obtenu dessus est, par construction, du bruit."""
from __future__ import annotations

import datetime as dt

import numpy as np
import pandas as pd


def random_walk_minutes(start: dt.date, days: int, seed: int = 1, price: float = 2000.0, vol_per_min: float = 0.00025,
                        open_boost: float = 3.0, trend_per_day: float = 0.0) -> pd.DataFrame:
    """Bougies 1 min UTC 24 h/24 pour `days` jours calendaires à partir de `start` (week-ends exclus)."""
    rng = np.random.default_rng(seed)
    frames = []
    p = price
    day = start
    for _ in range(days):
        if day.weekday() < 5:
            idx = pd.date_range(pd.Timestamp(day, tz="UTC"), periods=24 * 60, freq="min")
            hours = idx.hour + idx.minute / 60
            # volatilité plus forte autour de l'ouverture de New York (13:30–16:30 UTC approx.)
            boost = np.where((hours >= 13.5) & (hours < 16.5), open_boost, 1.0)
            rets = rng.normal(trend_per_day / (24 * 60), vol_per_min, size=len(idx)) * boost
            closes = p * np.exp(np.cumsum(rets))
            opens = np.r_[p, closes[:-1]]
            wiggle = np.abs(rng.normal(0, vol_per_min * 0.7, size=len(idx))) * boost * closes
            highs = np.maximum(opens, closes) + wiggle
            lows = np.minimum(opens, closes) - wiggle
            frames.append(pd.DataFrame({"open": opens, "high": highs, "low": lows, "close": closes, "volume": rng.integers(1, 500, len(idx)).astype(float)}, index=idx))
            p = float(closes[-1])
        day += dt.timedelta(days=1)
    return pd.concat(frames)
