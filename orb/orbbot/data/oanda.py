"""Historique 1 minute via l'API OANDA v20 (compte de démonstration gratuit, jeton `OANDA_TOKEN`).

GET /v3/instruments/{instrument}/candles?granularity=M1&price=B&from=…&count=5000 — bougies BID, UTC, `complete` only.
Même source que le flux temps réel : le backtest et l'exécution voient exactement les mêmes prix.
Cache local par jour : data/orb/oanda/<INSTRUMENT>/<date>.csv.gz (jamais versionné).
"""
from __future__ import annotations

import datetime as dt
import gzip
import io
import logging
import pathlib
import time

import httpx
import pandas as pd

log = logging.getLogger("orbbot.data.oanda")
PRACTICE = "https://api-fxpractice.oanda.com"
LIVE = "https://api-fxtrade.oanda.com"
COLUMNS = ["open", "high", "low", "close", "volume"]
DUKASCOPY_TO_OANDA = {"XAUUSD": "XAU_USD", "EURUSD": "EUR_USD", "GBPUSD": "GBP_USD", "USA500IDXUSD": "SPX500_USD", "USATECHIDXUSD": "NAS100_USD"}


def _day_cache(root: pathlib.Path, instrument: str, day: dt.date) -> pathlib.Path:
    return root / "oanda" / instrument / f"{day.isoformat()}.csv.gz"


def _write_day(p: pathlib.Path, df: pd.DataFrame) -> None:
    p.parent.mkdir(parents=True, exist_ok=True)
    if df.empty:
        p.write_bytes(b"")
        return
    buf = io.StringIO()
    df.to_csv(buf)
    with gzip.open(p, "wt") as f:
        f.write(buf.getvalue())


def _read_day(p: pathlib.Path) -> pd.DataFrame:
    if p.stat().st_size == 0:
        return pd.DataFrame(columns=COLUMNS)
    with gzip.open(p, "rt") as f:
        df = pd.read_csv(f, index_col=0, parse_dates=True)
    df.index = pd.to_datetime(df.index, utc=True)
    return df


def load_minutes_oanda(instrument: str, start: dt.date, end: dt.date, root: pathlib.Path, token: str, practice: bool = True,
                       progress: bool = False) -> pd.DataFrame:
    """Bougies M1 BID entre `start` et `end` inclus. Les jours déjà en cache ne sont pas retéléchargés ; les jours
    manquants sont téléchargés par blocs de 5 000 bougies puis redécoupés par jour UTC."""
    oanda_instr = DUKASCOPY_TO_OANDA.get(instrument, instrument)
    days = [start + dt.timedelta(days=i) for i in range((end - start).days + 1)]
    cached = {d: _read_day(_day_cache(root, oanda_instr, d)) for d in days if _day_cache(root, oanda_instr, d).exists()}
    missing = [d for d in days if d not in cached and d < dt.date.today()]  # le jour courant n'est jamais mis en cache
    frames = [df for df in cached.values() if not df.empty]
    if missing:
        client = httpx.Client(base_url=PRACTICE if practice else LIVE, timeout=30,
                              headers={"Authorization": f"Bearer {token}", "Accept-Datetime-Format": "RFC3339"})
        # blocs contigus de jours manquants
        blocks: list[list[dt.date]] = []
        for d in missing:
            if blocks and (d - blocks[-1][-1]).days == 1:
                blocks[-1].append(d)
            else:
                blocks.append([d])
        for block in blocks:
            t_from = dt.datetime.combine(block[0], dt.time(0, 0), tzinfo=dt.UTC)
            t_end = dt.datetime.combine(block[-1] + dt.timedelta(days=1), dt.time(0, 0), tzinfo=dt.UTC)
            rows: list[tuple] = []
            cur = t_from
            while cur < t_end:
                params = {"granularity": "M1", "price": "B", "from": cur.isoformat().replace("+00:00", "Z"), "count": 5000}
                for attempt in range(5):
                    r = client.get(f"/v3/instruments/{oanda_instr}/candles", params=params)
                    if r.status_code == 429 or r.status_code >= 500:
                        time.sleep(2.0 * (attempt + 1))
                        continue
                    break
                if r.status_code >= 400:
                    raise RuntimeError(f"OANDA candles {oanda_instr} {cur:%Y-%m-%d}: HTTP {r.status_code} {r.text[:200]}")
                candles = r.json().get("candles", [])
                if not candles:  # rien après `cur` dans cette page : on saute au jour suivant (fin d'historique / trou)
                    cur = dt.datetime.combine(cur.date() + dt.timedelta(days=1), dt.time(0, 0), tzinfo=dt.UTC)
                    continue
                for c in candles:
                    if not c.get("complete"):
                        continue
                    ts = pd.Timestamp(c["time"]).tz_convert("UTC") if pd.Timestamp(c["time"]).tzinfo else pd.Timestamp(c["time"], tz="UTC")
                    if ts >= t_end:
                        break
                    b = c["bid"]
                    rows.append((ts, float(b["o"]), float(b["h"]), float(b["l"]), float(b["c"]), float(c.get("volume", 0))))
                last_ts = pd.Timestamp(candles[-1]["time"])
                last_ts = last_ts.tz_convert("UTC") if last_ts.tzinfo else last_ts.tz_localize("UTC")
                nxt = (last_ts + pd.Timedelta(minutes=1)).to_pydatetime()
                if nxt <= cur:
                    break
                cur = nxt
            df_block = pd.DataFrame(rows, columns=["ts", *COLUMNS]).set_index("ts") if rows else pd.DataFrame(columns=COLUMNS)
            for d in block:
                day_df = df_block[(df_block.index >= pd.Timestamp(d, tz="UTC")) & (df_block.index < pd.Timestamp(d + dt.timedelta(days=1), tz="UTC"))] if rows else pd.DataFrame(columns=COLUMNS)
                _write_day(_day_cache(root, oanda_instr, d), day_df)
                if not day_df.empty:
                    frames.append(day_df)
            if progress:
                print(f"  OANDA {oanda_instr}: {block[0]} → {block[-1]} ({len(rows)} bougies)", flush=True)
        client.close()
    if not frames:
        return pd.DataFrame(columns=COLUMNS)
    out = pd.concat(frames).sort_index()
    out.index.name = None
    return out[~out.index.duplicated(keep="last")]
