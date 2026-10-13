"""Bougies 1 minute Dukascopy (flux public, sans clé) : téléchargement, décodage, cache local, chargement.

Format : https://datafeed.dukascopy.com/datafeed/{INSTRUMENT}/{AAAA}/{MM-1}/{JJ}/BID_candles_min_1.bi5
(mois indexé à partir de 0), fichier LZMA d'enregistrements de 24 octets big-endian :
    int32 décalage en secondes depuis 00:00 UTC, int32 open, int32 close, int32 low, int32 high, float32 volume
les prix étant des entiers à diviser par `price_scale` (or : 1 000 ; paires forex : 100 000).
L'ordre open/close/low/high est VÉRIFIÉ à la lecture (low ≤ min(open, close) et high ≥ max(open, close) sur ≥ 99 % des
lignes) et l'alternative open/high/low/close est essayée sinon ; l'échelle de prix est vérifiée contre une plage de
vraisemblance. Jour sans fichier (week-end, férié) ⇒ 404 ⇒ journée vide, jamais inventée.
"""
from __future__ import annotations

import datetime as dt
import gzip
import io
import logging
import lzma
import pathlib
import struct
import time

import httpx
import numpy as np
import pandas as pd

log = logging.getLogger("orbbot.data")

BASE_URL = "https://datafeed.dukascopy.com/datafeed"
INSTRUMENTS = {
    # symbole Dukascopy : (échelle de prix, plage plausible, spread retail typique en unités de prix)
    "XAUUSD": {"scale": 1000, "plausible": (800.0, 10_000.0), "spread": 0.30, "slippage": 0.05, "unit": "$/oz"},
    "EURUSD": {"scale": 100_000, "plausible": (0.7, 1.8), "spread": 0.00010, "slippage": 0.00002, "unit": ""},
    "GBPUSD": {"scale": 100_000, "plausible": (0.9, 2.2), "spread": 0.00012, "slippage": 0.00003, "unit": ""},
    "USA500IDXUSD": {"scale": 1000, "plausible": (1_500.0, 12_000.0), "spread": 0.40, "slippage": 0.10, "unit": "pts"},
    "USATECHIDXUSD": {"scale": 1000, "plausible": (5_000.0, 40_000.0), "spread": 1.5, "slippage": 0.25, "unit": "pts"},
}
RECORD = struct.Struct(">5if")
COLUMNS = ["open", "high", "low", "close", "volume"]


def day_url(instrument: str, day: dt.date, side: str = "BID") -> str:
    return f"{BASE_URL}/{instrument}/{day.year:04d}/{day.month - 1:02d}/{day.day:02d}/{side}_candles_min_1.bi5"


def decode_day(raw: bytes, day: dt.date, scale: int, plausible: tuple[float, float]) -> pd.DataFrame:
    """Décode un fichier .bi5 (LZMA) en DataFrame UTC indexé par minute. Vide si le fichier est vide."""
    if not raw:
        return pd.DataFrame(columns=COLUMNS)
    data = lzma.decompress(raw)
    n = len(data) // RECORD.size
    if n == 0:
        return pd.DataFrame(columns=COLUMNS)
    arr = np.frombuffer(data[: n * RECORD.size], dtype=np.dtype([("t", ">i4"), ("a", ">i4"), ("b", ">i4"), ("c", ">i4"), ("d", ">i4"), ("v", ">f4")]))
    t = arr["t"].astype(np.int64)
    a, b, c, d = (arr[k].astype(np.float64) / scale for k in ("a", "b", "c", "d"))
    # ordre documenté : open, close, low, high
    o, cl, lo, hi = a, b, c, d
    ok = np.mean((lo <= np.minimum(o, cl) + 1e-12) & (hi >= np.maximum(o, cl) - 1e-12)) if n else 0.0
    if ok < 0.99:  # alternative : open, high, low, close
        o2, hi2, lo2, cl2 = a, b, c, d
        ok2 = np.mean((lo2 <= np.minimum(o2, cl2) + 1e-12) & (hi2 >= np.maximum(o2, cl2) - 1e-12))
        if ok2 > ok:
            o, hi, lo, cl, ok = o2, hi2, lo2, cl2, ok2
            log.warning("%s %s: ordre des colonnes open/high/low/close détecté (%.3f cohérent)", day, scale, ok2)
    if ok < 0.95:
        raise ValueError(f"{day}: bougies incohérentes (low/high) dans {100 * (1 - ok):.1f} % des lignes — format inattendu")
    med = float(np.median(cl))
    if not (plausible[0] <= med <= plausible[1]):
        raise ValueError(f"{day}: prix médian {med} hors plage plausible {plausible} — échelle de prix incorrecte ?")
    idx = pd.to_datetime(np.datetime64(day.isoformat()) + t.astype("timedelta64[s]"), utc=True)
    df = pd.DataFrame({"open": o, "high": hi, "low": lo, "close": cl, "volume": arr["v"].astype(np.float64)}, index=idx)
    df = df[~df.index.duplicated(keep="last")].sort_index()
    return df


def cache_path(root: pathlib.Path, instrument: str, day: dt.date) -> pathlib.Path:
    return root / instrument / f"{day.isoformat()}.csv.gz"


LAST_STATS: dict = {}
HEADERS = {  # en-têtes de navigateur : le serveur répond 503 à certains clients « nus »
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36",
    "Accept": "*/*", "Accept-Language": "en-US,en;q=0.9", "Referer": "https://freeserv.dukascopy.com/2.0/",
    "Origin": "https://freeserv.dukascopy.com", "Connection": "keep-alive",
}


def fetch_day(client: httpx.Client, instrument: str, day: dt.date, root: pathlib.Path, retries: int = 4, stats: dict | None = None) -> pd.DataFrame:
    """Télécharge (ou relit le cache) la journée `day`. Un fichier vide dans le cache marque un jour sans données ;
    un jour indisponible (503/403 persistants) est compté dans `stats['unavailable']` et renvoyé vide, SANS être mis en
    cache (il sera retenté la prochaine fois)."""
    meta = INSTRUMENTS[instrument]
    stats = stats if stats is not None else LAST_STATS
    p = cache_path(root, instrument, day)
    if p.exists():
        stats["cached"] = stats.get("cached", 0) + 1
        if p.stat().st_size == 0:
            return pd.DataFrame(columns=COLUMNS)
        with gzip.open(p, "rt") as f:
            df = pd.read_csv(f, index_col=0, parse_dates=True)
        df.index = pd.to_datetime(df.index, utc=True)
        return df
    p.parent.mkdir(parents=True, exist_ok=True)
    url = day_url(instrument, day)
    last: Exception | str | None = None
    for attempt in range(retries):
        try:
            r = client.get(url, timeout=30)
            if r.status_code == 404:
                p.write_bytes(b"")
                stats["missing"] = stats.get("missing", 0) + 1
                return pd.DataFrame(columns=COLUMNS)
            if r.status_code in (403, 429, 500, 502, 503, 504):
                last = f"HTTP {r.status_code}"
                time.sleep(2.0 * (attempt + 1))
                continue
            r.raise_for_status()
            df = decode_day(r.content, day, meta["scale"], meta["plausible"])
            if df.empty:
                p.write_bytes(b"")
                stats["missing"] = stats.get("missing", 0) + 1
            else:
                buf = io.StringIO()
                df.to_csv(buf)
                with gzip.open(p, "wt") as f:
                    f.write(buf.getvalue())
                stats["downloaded"] = stats.get("downloaded", 0) + 1
            return df
        except (httpx.HTTPError, lzma.LZMAError) as e:  # réseau / fichier corrompu : nouvel essai
            last = e
            time.sleep(1.5 * (attempt + 1))
    stats["unavailable"] = stats.get("unavailable", 0) + 1
    stats.setdefault("errors", []).append(f"{day}: {last}")
    log.warning("%s %s: indisponible (%s)", instrument, day, last)
    return pd.DataFrame(columns=COLUMNS)


def load_minutes(instrument: str, start: dt.date, end: dt.date, root: pathlib.Path, progress: bool = False) -> pd.DataFrame:
    """Bougies 1 min BID entre `start` et `end` inclus (UTC), téléchargées si absentes du cache."""
    if instrument not in INSTRUMENTS:
        raise KeyError(f"instrument inconnu {instrument} (connus : {', '.join(INSTRUMENTS)})")
    frames: list[pd.DataFrame] = []
    day = start
    n = 0
    stats: dict = {"requested": 0}
    LAST_STATS.clear()
    LAST_STATS.update(stats)
    with httpx.Client(headers=HEADERS, follow_redirects=True, http2=False) as client:
        while day <= end:
            if day.weekday() != 5:  # samedi : aucune donnée ; dimanche : ouverture asiatique (on garde)
                LAST_STATS["requested"] += 1
                df = fetch_day(client, instrument, day, root, stats=LAST_STATS)
                if not df.empty:
                    frames.append(df)
                if LAST_STATS.get("unavailable", 0) >= 25 and LAST_STATS.get("downloaded", 0) == 0 and LAST_STATS.get("cached", 0) == 0:
                    log.error("%s: 25 jours consécutifs indisponibles sans aucun succès — source probablement bloquée, arrêt", instrument)
                    break
            n += 1
            if progress and n % 50 == 0:
                print(f"  {instrument}: {day} ({sum(len(f) for f in frames)} bougies ; {LAST_STATS})", flush=True)
            day += dt.timedelta(days=1)
    if not frames:
        return pd.DataFrame(columns=COLUMNS)
    out = pd.concat(frames).sort_index()
    return out[~out.index.duplicated(keep="last")]


def encode_day_for_tests(bars: list[tuple[int, float, float, float, float, float]], scale: int) -> bytes:
    """Inverse de decode_day (utilisé par les tests) : [(secondes, open, close, low, high, volume), …] → .bi5."""
    raw = b"".join(RECORD.pack(t, round(o * scale), round(c * scale), round(lo * scale), round(h * scale), v) for t, o, c, lo, h, v in bars)
    return lzma.compress(raw, format=lzma.FORMAT_ALONE)
