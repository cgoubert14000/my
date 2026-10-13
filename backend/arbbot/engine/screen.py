"""Vectorised route screen.

Per block, every route must be checked for (a) a raw cyclic spread above the sum of LP fees + margin and (b) enough
depth in every pool. Doing that route by route in Python costs ~35 µs per route — 7 s for the 192k routes of Base
(measured on the real-market session 38425105547: the screen alone exhausted the cycle budget and nothing was sized).

The spread of a cycle is multiplicative in the per-pool mid prices, so it is a sum of signed log-prices: with
p_i = token1-per-token0 mid price of pool i and s_h = +1 when hop h swaps token0→token1 (−1 otherwise),

    spread_bps(route) = (exp(Σ_h s_h·log p_{i_h}) − 1) · 1e4

Only the P per-pool values change from block to block; the (R × H) index/sign matrices are built once per route set.
With numpy the whole screen of 192k routes takes a few milliseconds.
"""
from __future__ import annotations

import math
from dataclasses import dataclass

import numpy as np

from ..core.pricing import _mid_price
from ..core.types import Pool, Route


@dataclass
class ScreenResult:
    survivors: np.ndarray  # route indices passing every screen, best edge first
    edge_bps: np.ndarray  # per route: spread − LP fees (bps)
    spread_bps: np.ndarray  # per route raw spread (bps)
    rejections: dict[str, int]


class RouteScreen:
    def __init__(self, routes: list[Route]):
        self.routes = routes
        pools: dict[str, Pool] = {}
        for r in routes:
            for h in r.hops:
                pools.setdefault(h.pool.address, h.pool)
        self.pools: list[Pool] = list(pools.values())
        index = {p.address: i for i, p in enumerate(self.pools)}
        self.n_pools = len(self.pools)
        dummy = self.n_pools  # padding slot for 2-hop routes: log-price 0, infinite depth, never quarantined
        R = len(routes)
        H = max((len(r.hops) for r in routes), default=1)
        self.idx = np.full((R, H), dummy, dtype=np.int64)
        self.sign = np.zeros((R, H), dtype=np.float64)
        for ri, r in enumerate(routes):
            for k, h in enumerate(r.hops):
                self.idx[ri, k] = index[h.pool.address]
                self.sign[ri, k] = 1.0 if h.pool.is_token0(h.token_in.address) else -1.0
        self.fee_bps = self._route_fees()  # recomputed every run: LP fees can change (Slipstream dynamic fee modules)

    def _route_fees(self) -> np.ndarray:
        fee_pool = np.zeros(self.n_pools + 1, dtype=np.float64)
        for i, p in enumerate(self.pools):
            fee_pool[i] = p.fee_ppm / 100.0
        return fee_pool[self.idx].sum(axis=1)

    # ------------------------------------------------------------------ per-cycle inputs

    def pool_vectors(self, price_usd) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
        """log mid price (token1 per token0), depth in USD (−1 = no price reference), quarantine flag, validity."""
        n = self.n_pools + 1
        cache: dict[str, float | None] = {}

        def px(token):
            k = token.address
            if k not in cache:
                cache[k] = price_usd(token)
            return cache[k]

        logp = np.zeros(n)
        depth = np.full(n, np.inf)
        quarantined = np.zeros(n, dtype=bool)
        valid = np.ones(n, dtype=bool)
        for i, p in enumerate(self.pools):
            quarantined[i] = p.quarantined
            m = _mid_price(p, p.token0)
            if not (m > 0.0) or not math.isfinite(m):
                valid[i] = False
                continue
            logp[i] = math.log(m)
            p0 = px(p.token0)
            p1 = px(p.token1)
            if p0 is None or p1 is None:
                depth[i] = -1.0
            else:
                x, y = p.depth_tokens()
                depth[i] = x / 10**p.token0.decimals * p0 + y / 10**p.token1.decimals * p1
        return logp, depth, quarantined, valid

    # ------------------------------------------------------------------ screen

    def run(self, *, min_spread_bps: float, min_liquidity_usd: float, price_usd) -> ScreenResult:
        logp, depth, quarantined, valid = self.pool_vectors(price_usd)
        self.fee_bps = self._route_fees()
        s = (self.sign * logp[self.idx]).sum(axis=1)
        spread = np.expm1(np.clip(s, -50, 50)) * 10_000.0
        edge = spread - self.fee_bps
        r_valid = valid[self.idx].all(axis=1)
        r_quar = quarantined[self.idx].any(axis=1)
        r_depth = depth[self.idx].min(axis=1)
        alive = r_valid & ~r_quar
        spread_ok = alive & (edge >= min_spread_bps)
        no_ref = spread_ok & (r_depth < 0)
        shallow = spread_ok & (r_depth >= 0) & (r_depth < min_liquidity_usd)
        keep = spread_ok & (r_depth >= min_liquidity_usd)
        rejections = {
            "pool_quarantined": int(r_quar.sum()),
            "pool_state_invalid": int((~r_valid & ~r_quar).sum()),
            "spread_below_threshold": int((alive & ~spread_ok).sum()),
            "no_price_reference": int(no_ref.sum()),
            "liquidity_below_min": int(shallow.sum()),
        }
        survivors = np.flatnonzero(keep)
        survivors = survivors[np.argsort(-edge[survivors], kind="stable")]
        return ScreenResult(survivors=survivors, edge_bps=edge, spread_bps=spread, rejections={k: v for k, v in rejections.items() if v})
