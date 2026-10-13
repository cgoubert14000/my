"""Route enumeration: cyclic paths token → pool → ... → token over the indexed pool graph (2 or 3 hops).

Two representations:
  * `RouteTable` — compact numpy arrays (pool index + direction per hop) built once from the pool graph; this is what
    the vectorised screen consumes and it scales to ~10⁶ routes (a Python `Route` object per route does not);
  * `Route` objects — materialised on demand (`table.route(i)`) for the few survivors that get sized/simulated.
`build_routes()` keeps returning `Route` objects for small universes/tests.
"""
from __future__ import annotations

import logging
from collections import defaultdict
from itertools import product

import numpy as np

from ..core.types import Hop, Pool, Route, Token

log = logging.getLogger("arbbot.routes")


class RouteTable:
    def __init__(self, pools: list[Pool], idx: np.ndarray, sign: np.ndarray, n_hops: np.ndarray):
        self.pools = pools  # pool index → Pool (padding index == len(pools))
        self.idx = idx  # (R, H) int32
        self.sign = sign  # (R, H) float64: +1 token0→token1, −1 token1→token0, 0 padding
        self.n_hops = n_hops  # (R,) int8
        self.truncated = 0

    def __len__(self) -> int:
        return int(self.idx.shape[0])

    @property
    def n_pools(self) -> int:
        return len(self.pools)

    def route(self, i: int) -> Route:
        hops: list[Hop] = []
        for k in range(int(self.n_hops[i])):
            p = self.pools[int(self.idx[i, k])]
            if self.sign[i, k] > 0:
                hops.append(Hop(p, p.token0, p.token1))
            else:
                hops.append(Hop(p, p.token1, p.token0))
        return Route(hops)

    def routes(self, indices) -> list[Route]:
        return [self.route(int(i)) for i in indices]

    def start_token(self, i: int) -> Token:
        p = self.pools[int(self.idx[i, 0])]
        return p.token0 if self.sign[i, 0] > 0 else p.token1

    # ------------------------------------------------------------------ builders

    @classmethod
    def from_routes(cls, routes: list[Route]) -> "RouteTable":
        pools: dict[str, Pool] = {}
        for r in routes:
            for h in r.hops:
                pools.setdefault(h.pool.address, h.pool)
        plist = list(pools.values())
        index = {p.address: i for i, p in enumerate(plist)}
        R = len(routes)
        H = max((len(r.hops) for r in routes), default=1)
        idx = np.full((R, H), len(plist), dtype=np.int32)
        sign = np.zeros((R, H), dtype=np.float64)
        n_hops = np.zeros(R, dtype=np.int8)
        for ri, r in enumerate(routes):
            n_hops[ri] = len(r.hops)
            for k, h in enumerate(r.hops):
                idx[ri, k] = index[h.pool.address]
                sign[ri, k] = 1.0 if h.pool.is_token0(h.token_in.address) else -1.0
        return cls(plist, idx, sign, n_hops)

    @classmethod
    def build(cls, pools: list[Pool], start_tokens: list[Token], max_hops: int = 3, max_routes: int = 0) -> "RouteTable":
        """Enumerate s→X→s (two different pools of the same pair) and s→X→Y→s cycles for every start token.

        Pools are unique within a route by construction (each hop uses a different token pair, and 2-hop routes
        pair distinct pools). `max_routes` (0 = unlimited) truncates 3-hop routes first — the shallowest pools come
        last because the indexer sorts pools by depth.
        """
        plist = [p for p in pools if not p.quarantined]
        index = {p.address: i for i, p in enumerate(plist)}
        pair_pools: dict[tuple[str, str], list[int]] = defaultdict(list)  # (lower(a), lower(b)) sorted → pool idx
        adj: dict[str, set[str]] = defaultdict(set)  # token → neighbour tokens
        for p in plist:
            a, b = p.token0.address.lower(), p.token1.address.lower()
            key = (a, b) if a < b else (b, a)
            pair_pools[key].append(index[p.address])
            adj[a].add(b)
            adj[b].add(a)

        def pp(a: str, b: str) -> list[int]:
            return pair_pools.get((a, b) if a < b else (b, a), [])

        def sgn(pi: int, token_in: str) -> float:
            return 1.0 if plist[pi].token0.address.lower() == token_in else -1.0

        rows_idx: list[tuple[int, int, int]] = []
        rows_sign: list[tuple[float, float, float]] = []
        pad = len(plist)
        for start in start_tokens:
            s = start.address.lower()
            for x in sorted(adj.get(s, ())):
                sx = pp(s, x)
                # 2-hop: s→X on p, X→s on q (p ≠ q)
                for p_i in sx:
                    for q_i in sx:
                        if p_i != q_i:
                            rows_idx.append((p_i, q_i, pad))
                            rows_sign.append((sgn(p_i, s), sgn(q_i, x), 0.0))
                if max_hops < 3:
                    continue
                for y in adj.get(x, ()):
                    if y == s or y == x:
                        continue
                    ys = pp(y, s)
                    if not ys:
                        continue
                    xy = pp(x, y)
                    for p_i, q_i, r_i in product(sx, xy, ys):
                        rows_idx.append((p_i, q_i, r_i))
                        rows_sign.append((sgn(p_i, s), sgn(q_i, x), sgn(r_i, y)))
            if max_routes and len(rows_idx) > max_routes:
                break
        truncated = 0
        if max_routes and len(rows_idx) > max_routes:
            truncated = len(rows_idx) - max_routes
            rows_idx, rows_sign = rows_idx[:max_routes], rows_sign[:max_routes]
            log.warning("route table truncated: %d routes dropped (max_routes=%d)", truncated, max_routes)
        H = 3 if max_hops >= 3 else 2
        if rows_idx:
            idx = np.asarray(rows_idx, dtype=np.int32)[:, :H]
            sign = np.asarray(rows_sign, dtype=np.float64)[:, :H]
        else:
            idx = np.zeros((0, H), dtype=np.int32)
            sign = np.zeros((0, H), dtype=np.float64)
        n_hops = (sign != 0).sum(axis=1).astype(np.int8)
        t = cls(plist, idx, sign, n_hops)
        t.truncated = truncated
        return t


def build_routes(pools: list[Pool], start_tokens: list[Token], max_hops: int = 3) -> list[Route]:
    """Materialised `Route` objects (small universes, tests, devnet)."""
    t = RouteTable.build(pools, start_tokens, max_hops)
    return [t.route(i) for i in range(len(t))]


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
