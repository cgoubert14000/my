"""Sources de bougies 1 minute clôturées : rejeu de l'historique (tests, validation) et OANDA v20 (pratique/réel)."""
from __future__ import annotations

import asyncio
import datetime as dt
from collections.abc import AsyncIterator
from dataclasses import dataclass

import httpx
import pandas as pd


@dataclass(frozen=True, slots=True)
class LiveBar:
    ts: dt.datetime     # début de la bougie, UTC
    o: float
    h: float
    l: float  # noqa: E741
    c: float
    volume: float = 0.0


class ReplayFeed:
    """Rejoue un DataFrame de bougies 1 min (index UTC). `speed` secondes de pause entre bougies (0 = instantané)."""

    def __init__(self, df: pd.DataFrame, speed: float = 0.0):
        self.df = df.sort_index()
        self.speed = speed

    async def warmup(self, n: int) -> list[float]:
        return []

    async def bars(self) -> AsyncIterator[LiveBar]:
        for ts, row in self.df.iterrows():
            yield LiveBar(ts.to_pydatetime(), float(row["open"]), float(row["high"]), float(row["low"]), float(row["close"]), float(row.get("volume", 0.0)))
            if self.speed:
                await asyncio.sleep(self.speed)


class OandaFeed:
    """Interroge GET /v3/instruments/{instrument}/candles (granularité M1, prix BID) et émet chaque bougie `complete`.
    Documentation : https://developer.oanda.com/rest-live-v20/instrument-ep/ — non testable depuis cet environnement
    (pas d'accès réseau) : à valider sur un compte de démonstration."""

    PRACTICE = "https://api-fxpractice.oanda.com"
    LIVE = "https://api-fxtrade.oanda.com"

    def __init__(self, token: str, instrument: str, practice: bool = True, poll_seconds: float = 5.0, stop_at: dt.datetime | None = None):
        self.host = self.PRACTICE if practice else self.LIVE
        self.instrument = instrument
        self.poll = poll_seconds
        self.stop_at = stop_at
        self.client = httpx.AsyncClient(base_url=self.host, headers={"Authorization": f"Bearer {token}", "Accept-Datetime-Format": "RFC3339"}, timeout=15)
        self.last_ts: dt.datetime | None = None

    async def _candles(self, count: int) -> list[dict]:
        r = await self.client.get(f"/v3/instruments/{self.instrument}/candles", params={"granularity": "M1", "count": count, "price": "B"})
        r.raise_for_status()
        return r.json().get("candles", [])

    @staticmethod
    def _to_bar(c: dict) -> LiveBar:
        ts = dt.datetime.fromisoformat(c["time"].replace("Z", "+00:00").split(".")[0] + "+00:00") if "." in c["time"] else dt.datetime.fromisoformat(c["time"].replace("Z", "+00:00"))
        b = c["bid"]
        return LiveBar(ts, float(b["o"]), float(b["h"]), float(b["l"]), float(b["c"]), float(c.get("volume", 0)))

    async def warmup(self, n: int) -> list[float]:
        cs = await self._candles(min(n, 5000))
        bars = [self._to_bar(c) for c in cs if c.get("complete")]
        if bars:
            self.last_ts = bars[-1].ts
        return [b.c for b in bars]

    async def bars(self) -> AsyncIterator[LiveBar]:
        backoff = self.poll
        while True:
            if self.stop_at and dt.datetime.now(dt.UTC) >= self.stop_at:
                return
            try:
                cs = await self._candles(5)
                backoff = self.poll
            except (httpx.HTTPError, ValueError) as e:  # réseau : on réessaie, on ne meurt pas
                await asyncio.sleep(min(60.0, backoff))
                backoff *= 2
                print(f"feed OANDA : erreur {e} — nouvel essai", flush=True)
                continue
            for c in cs:
                if not c.get("complete"):
                    continue
                b = self._to_bar(c)
                if self.last_ts is None or b.ts > self.last_ts:
                    self.last_ts = b.ts
                    yield b
            await asyncio.sleep(self.poll)

    async def aclose(self) -> None:
        await self.client.aclose()
