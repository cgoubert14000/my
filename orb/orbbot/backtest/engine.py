"""Préparation des séances (heure de New York, EMA) et exécution d'une ou plusieurs variantes sur l'historique."""
from __future__ import annotations

import math
import os
from concurrent.futures import ProcessPoolExecutor
from dataclasses import dataclass

import numpy as np
import pandas as pd

from ..strategy.orb import OPEN_NY, Bar, Costs, OrbSession, Trade
from ..strategy.params import OrbParams

NY_TZ = "America/New_York"
SESSION_END = 16 * 60  # 16:00 New York


@dataclass
class DaySession:
    day: str                 # date New York (AAAA-MM-JJ)
    t: np.ndarray            # minutes depuis minuit (heure de New York)
    o: np.ndarray
    h: np.ndarray
    l: np.ndarray  # noqa: E741
    c: np.ndarray
    ema: dict[int, np.ndarray]   # période → EMA alignée
    ts: list[str] | None = None  # horodatages UTC (journal), facultatif

    def bars(self, ma: int, with_ts: bool = False) -> list[Bar]:
        e = self.ema.get(ma)
        nan = math.nan
        ts = self.ts if (with_ts and self.ts) else None
        return [Bar(int(self.t[i]), float(self.o[i]), float(self.h[i]), float(self.l[i]), float(self.c[i]),
                    float(e[i]) if e is not None else nan, ts[i] if ts else "") for i in range(len(self.t))]


def prepare_sessions(df: pd.DataFrame, ma_periods: tuple[int, ...] = (50, 200), min_bars: int = 200, with_ts: bool = False) -> list[DaySession]:
    """Découpe les bougies 1 min UTC en séances New York 09:30–16:00 ; EMA calculées sur la série continue (pas de
    réinitialisation quotidienne). Les journées avec moins de `min_bars` bougies (fériés, trous) sont ignorées."""
    if df.empty:
        return []
    df = df.sort_index()
    emas = {p: df["close"].ewm(span=p, adjust=False).mean().to_numpy() for p in ma_periods}
    local = df.index.tz_convert(NY_TZ)
    minutes = (local.hour * 60 + local.minute).to_numpy()
    days = local.strftime("%Y-%m-%d").to_numpy()
    mask = (minutes >= OPEN_NY) & (minutes < SESSION_END) & (np.asarray(local.weekday) < 5)
    o, h, l, c = (df[k].to_numpy(dtype=float) for k in ("open", "high", "low", "close"))
    ts_all = df.index.strftime("%Y-%m-%dT%H:%MZ").to_numpy() if with_ts else None
    out: list[DaySession] = []
    idx = np.flatnonzero(mask)
    if idx.size == 0:
        return out
    day_vals = days[idx]
    bounds = np.flatnonzero(np.r_[True, day_vals[1:] != day_vals[:-1], True])
    for a, b in zip(bounds[:-1], bounds[1:]):
        sel = idx[a:b]
        if sel.size < min_bars:
            continue
        out.append(DaySession(day=str(day_vals[a]), t=minutes[sel], o=o[sel], h=h[sel], l=l[sel], c=c[sel],
                              ema={p: emas[p][sel] for p in ma_periods}, ts=list(ts_all[sel]) if ts_all is not None else None))
    return out


def run_session(bars: list[Bar], params: OrbParams, costs: Costs, day: str) -> OrbSession:
    sess = OrbSession(params=params, costs=costs, day=day)
    for bar in bars:
        sess.on_bar(bar)
        if sess.done:
            break
    return sess


def run_variants(sessions: list[DaySession], variants: list[OrbParams], costs: Costs) -> dict[str, list[Trade]]:
    """Exécute toutes les variantes sur toutes les séances (séquentiel). Résultat : clé de variante → trades."""
    out: dict[str, list[Trade]] = {p.key(): [] for p in variants}
    mas = sorted({p.ma for p in variants})
    for s in sessions:
        bars_by_ma = {ma: s.bars(ma) for ma in mas}
        for p in variants:
            sess = run_session(bars_by_ma[p.ma], p, costs, s.day)
            if sess.trades:
                out[p.key()].extend(sess.trades)
    return out


_SESSIONS: list[DaySession] = []


def _init_worker(sessions: list[DaySession]) -> None:
    global _SESSIONS
    _SESSIONS = sessions


def _work(args: tuple[list[OrbParams], Costs]) -> dict[str, list[Trade]]:
    variants, costs = args
    return run_variants(_SESSIONS, variants, costs)


def run_grid(sessions: list[DaySession], variants: list[OrbParams], costs: Costs, workers: int | None = None, progress=None) -> dict[str, list[Trade]]:
    """Exécution parallèle (processus) de la grille ; `progress(done, total)` facultatif."""
    workers = workers or max(1, (os.cpu_count() or 2))
    if workers <= 1 or len(variants) < 8:
        return run_variants(sessions, variants, costs)
    chunk = max(4, math.ceil(len(variants) / (workers * 6)))
    batches = [(variants[i:i + chunk], costs) for i in range(0, len(variants), chunk)]
    out: dict[str, list[Trade]] = {}
    done = 0
    with ProcessPoolExecutor(max_workers=workers, initializer=_init_worker, initargs=(sessions,)) as ex:
        for res in ex.map(_work, batches):
            out.update(res)
            done += 1
            if progress:
                progress(done, len(batches))
    return out
