"""Courtiers : PaperBroker (exécution simulée aux prix du modèle, journal) et OandaBroker (REST v20).

Le modèle de stratégie reste la source de vérité des niveaux (entrée, stop, objectif) ; le courtier porte en plus les
ordres stop/objectif côté serveur afin qu'une coupure du bot ne laisse jamais une position sans protection.
"""
from __future__ import annotations

import datetime as dt
import itertools
from dataclasses import dataclass, field

import httpx


@dataclass
class Position:
    id: str
    instrument: str
    direction: int
    units: float
    entry_price: float
    stop: float
    tp: float
    opened_at: str
    closed_units: float = 0.0
    realized: float = 0.0
    closed: bool = False
    history: list[str] = field(default_factory=list)


class PaperBroker:
    """Compte fictif : les exécutions se font aux prix fournis par le moteur (eux-mêmes issus du modèle, coûts inclus)."""

    def __init__(self, equity: float = 10_000.0):
        self.equity = equity
        self.start_equity = equity
        self.positions: dict[str, Position] = {}
        self._ids = itertools.count(1)

    async def account_equity(self) -> float:
        return self.equity

    async def open_market(self, instrument: str, direction: int, units: float, price: float, stop: float, tp: float, ts: str) -> Position:
        p = Position(str(next(self._ids)), instrument, direction, units, price, stop, tp, ts)
        self.positions[p.id] = p
        return p

    async def close(self, pos_id: str, price: float, units: float | None, ts: str, reason: str) -> float:
        p = self.positions[pos_id]
        qty = p.units - p.closed_units if units is None else min(units, p.units - p.closed_units)
        pnl = (price - p.entry_price) * p.direction * qty
        p.realized += pnl
        p.closed_units += qty
        self.equity += pnl
        p.history.append(f"{ts} {reason} {qty:g} @ {price:.4f} → {pnl:+.2f}")
        if p.closed_units >= p.units - 1e-12:
            p.closed = True
        return pnl

    async def set_stop(self, pos_id: str, stop: float) -> None:
        self.positions[pos_id].stop = stop

    async def open_positions(self) -> list[Position]:
        return [p for p in self.positions.values() if not p.closed]


class OandaBroker:
    """Adaptateur OANDA v20 (https://developer.oanda.com/rest-live-v20/order-ep/). Ordres au marché avec stop et
    objectif attachés, clôture partielle, déplacement du stop. NON TESTÉ EN CONDITIONS RÉELLES (aucun accès réseau dans
    l'environnement de développement) : à valider d'abord sur un compte de démonstration (fxpractice)."""

    PRACTICE = "https://api-fxpractice.oanda.com"
    LIVE = "https://api-fxtrade.oanda.com"

    def __init__(self, token: str, account_id: str, practice: bool = True, price_precision: int = 3):
        self.account = account_id
        self.prec = price_precision
        self.client = httpx.AsyncClient(base_url=self.PRACTICE if practice else self.LIVE, timeout=20,
                                        headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json", "Accept-Datetime-Format": "RFC3339"})
        self.positions: dict[str, Position] = {}

    def _px(self, x: float) -> str:
        return f"{x:.{self.prec}f}"

    async def account_equity(self) -> float:
        r = await self.client.get(f"/v3/accounts/{self.account}/summary")
        r.raise_for_status()
        return float(r.json()["account"]["NAV"])

    async def open_market(self, instrument: str, direction: int, units: float, price: float, stop: float, tp: float, ts: str) -> Position:
        body = {"order": {"type": "MARKET", "instrument": instrument, "units": str(int(units) * direction), "timeInForce": "FOK",
                          "positionFill": "DEFAULT",
                          "stopLossOnFill": {"price": self._px(stop), "timeInForce": "GTC"},
                          "takeProfitOnFill": {"price": self._px(tp), "timeInForce": "GTC"}}}
        r = await self.client.post(f"/v3/accounts/{self.account}/orders", json=body)
        if r.status_code >= 400:
            raise RuntimeError(f"OANDA refuse l'ordre : {r.status_code} {r.text[:300]}")
        j = r.json()
        fill = j.get("orderFillTransaction")
        if not fill:
            raise RuntimeError(f"ordre non exécuté : {j.get('orderCancelTransaction', {}).get('reason', j)}")
        trade = fill.get("tradeOpened") or {}
        p = Position(str(trade.get("tradeID", fill.get("id"))), instrument, direction, float(abs(int(units))), float(fill.get("price", price)), stop, tp, ts)
        p.history.append(f"{ts} ouverture réelle @ {p.entry_price} (modèle {price:.4f})")
        self.positions[p.id] = p
        return p

    async def close(self, pos_id: str, price: float, units: float | None, ts: str, reason: str) -> float:
        p = self.positions[pos_id]
        qty = p.units - p.closed_units if units is None else min(units, p.units - p.closed_units)
        r = await self.client.put(f"/v3/accounts/{self.account}/trades/{pos_id}/close", json={"units": str(int(qty)) if units is not None else "ALL"})
        if r.status_code == 404:  # déjà clôturé côté courtier (stop/objectif serveur)
            p.history.append(f"{ts} {reason}: déjà clôturé côté courtier")
            p.closed = True
            return 0.0
        r.raise_for_status()
        fill = r.json().get("orderFillTransaction", {})
        pnl = float(fill.get("pl", 0.0))
        real_px = float(fill.get("price", price))
        p.realized += pnl
        p.closed_units += qty
        p.history.append(f"{ts} {reason} {qty:g} @ {real_px} (modèle {price:.4f}) → {pnl:+.2f}")
        if p.closed_units >= p.units - 1e-12:
            p.closed = True
        return pnl

    async def set_stop(self, pos_id: str, stop: float) -> None:
        r = await self.client.put(f"/v3/accounts/{self.account}/trades/{pos_id}/orders", json={"stopLoss": {"price": self._px(stop), "timeInForce": "GTC"}})
        r.raise_for_status()
        self.positions[pos_id].stop = stop

    async def open_positions(self) -> list[Position]:
        r = await self.client.get(f"/v3/accounts/{self.account}/openTrades")
        r.raise_for_status()
        ids = {t["id"] for t in r.json().get("trades", [])}
        for p in self.positions.values():
            if p.id not in ids and not p.closed:
                p.closed = True
                p.history.append(f"{dt.datetime.now(dt.UTC).isoformat(timespec='seconds')} clôturé côté courtier (stop/objectif serveur)")
        return [p for p in self.positions.values() if not p.closed]

    async def aclose(self) -> None:
        await self.client.aclose()
