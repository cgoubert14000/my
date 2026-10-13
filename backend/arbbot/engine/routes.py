"""Route enumeration: cyclic paths token → pool → ... → token over the indexed pool graph (2 or 3 hops)."""
from __future__ import annotations

from collections import defaultdict

from ..core.types import Hop, Pool, Route, Token


def build_routes(pools: list[Pool], start_tokens: list[Token], max_hops: int = 3) -> list[Route]:
    by_token: dict[str, list[Pool]] = defaultdict(list)
    for p in pools:
        if p.quarantined:
            continue
        by_token[p.token0.address.lower()].append(p)
        by_token[p.token1.address.lower()].append(p)

    routes: list[Route] = []
    seen: set[str] = set()
    for start in start_tokens:
        s = start.address.lower()
        for p1 in by_token.get(s, []):
            m1 = p1.other(start.address)
            for p2 in by_token.get(m1.address.lower(), []):
                if p2.address == p1.address:
                    continue
                m2 = p2.other(m1.address)
                if m2.address.lower() == s:
                    r = Route([Hop(p1, start, m1), Hop(p2, m1, start)])
                    if r.key not in seen:
                        seen.add(r.key)
                        routes.append(r)
                    continue
                if max_hops < 3:
                    continue
                for p3 in by_token.get(m2.address.lower(), []):
                    if p3.address in (p1.address, p2.address):
                        continue
                    m3 = p3.other(m2.address)
                    if m3.address.lower() != s:
                        continue
                    r = Route([Hop(p1, start, m1), Hop(p2, m1, m2), Hop(p3, m2, start)])
                    if r.key not in seen:
                        seen.add(r.key)
                        routes.append(r)
    return routes


def route_spread_bps(route: Route) -> float:
    """Raw cyclic spread from marginal prices (before fees & impact): (∏ mid_i − 1) × 1e4."""
    from ..core.pricing import _mid_price

    prod = 1.0
    for h in route.hops:
        m = _mid_price(h.pool, h.token_in)
        if m <= 0:
            return -1e9
        prod *= m
    return (prod - 1.0) * 10_000


def route_fee_bps(route: Route) -> float:
    """Sum of LP fees along the route in bps (upper bound of what spread must beat before impact & gas)."""
    return sum(h.pool.fee_ppm / 100 for h in route.hops)
