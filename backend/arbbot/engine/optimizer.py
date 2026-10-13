"""Borrow-amount optimiser: maximise net(x) = route_out(x) − x − flash_fee(x) over the admissible interval.

The objective is unimodal for constant-product legs and piecewise-smooth for concentrated liquidity, so a
log-spaced grid followed by a golden-section refinement on integers is robust and cheap (pure in-memory math).
All arithmetic is exact integer; nothing is approximated by floats except grid placement.
"""
from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Callable

from ..core.pricing import QuoteError, RouteQuote, quote_route
from ..core.types import DexKind, Route

PHI = (math.sqrt(5) - 1) / 2


@dataclass
class OptimizationResult:
    amount_in: int
    quote: RouteQuote | None
    net_before_gas: int  # out − in − flash fee
    evaluations: int
    upper_bound: int
    reason: str = ""


def flash_fee_for(amount: int, fee_bps_x100: int) -> int:
    """fee expressed in 1/100 bps (Aave 0.05 % = 500; Balancer/Morpho 0). Rounds up like the protocols."""
    if fee_bps_x100 == 0:
        return 0
    return -(-amount * fee_bps_x100 // 1_000_000)


def max_borrow_for_route(route: Route, fraction_of_depth: float, provider_capacity: int | None, policy_cap: int | None) -> int:
    """Upper bound = fraction of the shallowest input-side depth along the route (in start-token units)."""
    bound = None
    scale = 1.0
    from ..core.pricing import _mid_price

    for h in route.hops:
        x, y = h.pool.liquidity_hint()
        depth_in = x if h.pool.is_token0(h.token_in.address) else y
        if h.pool.kind in (DexKind.UNIV3, DexKind.PANCAKE_V3):
            depth_in = depth_in // 2  # virtual reserves overstate executable depth once concentrated ranges end
        m = _mid_price(h.pool, h.token_in)
        if h.pool.balances_block and m > 0:
            # the pool cannot pay out more token_out than it really holds → cap the input side accordingly
            bx, by = h.pool.depth_tokens()
            out_held = by if h.pool.is_token0(h.token_in.address) else bx
            depth_in = min(depth_in, int(out_held / m))
        cand = int(depth_in * fraction_of_depth / scale) if scale > 0 else 0
        bound = cand if bound is None else min(bound, cand)
        scale = scale * m if m > 0 else scale
    if bound is None:
        return 0
    if provider_capacity is not None:
        bound = min(bound, provider_capacity)
    if policy_cap is not None:
        bound = min(bound, policy_cap)
    return max(bound, 0)


def optimize_amount(
    route: Route,
    *,
    flash_fee_bps_x100: int,
    min_amount: int,
    max_amount: int,
    grid_points: int = 18,
    golden_iters: int = 24,
    objective: Callable[[int], int] | None = None,
    max_impact_bps: float | None = None,
) -> OptimizationResult:
    if max_amount <= min_amount:
        return OptimizationResult(0, None, 0, 0, max_amount, "max_amount <= min_amount")
    evals = 0
    cache: dict[int, tuple[int, RouteQuote | None]] = {}

    def f(x: int) -> int:
        nonlocal evals
        if x in cache:
            return cache[x][0]
        evals += 1
        try:
            q = quote_route(route, x)
            v = q.amount_out - x - flash_fee_for(x, flash_fee_bps_x100)
            if max_impact_bps is not None and q.price_impact_bps > max_impact_bps:
                v = -(10**39) - x  # size violates the impact cap: strictly worse, and worse the larger it is
        except QuoteError:
            q, v = None, -(10**40)
        if objective is not None and q is not None:
            v = objective(x)
        cache[x] = (v, q)
        return v

    # 1) log grid
    lo_log, hi_log = math.log(min_amount), math.log(max_amount)
    pts = sorted({int(math.exp(lo_log + (hi_log - lo_log) * i / (grid_points - 1))) for i in range(grid_points)})
    best_x = max(pts, key=f)
    best_v = f(best_x)
    if best_v <= -(10**39) or best_v <= 0:
        # Even the best grid point is a loss; refine once around the smallest sizes in case the optimum is tiny
        return OptimizationResult(best_x, cache[best_x][1], best_v, evals, max_amount, "no positive grid point")

    # 2) golden-section around the best grid point
    i = pts.index(best_x)
    a = pts[i - 1] if i > 0 else min_amount
    b = pts[i + 1] if i + 1 < len(pts) else max_amount
    c = int(b - PHI * (b - a))
    d = int(a + PHI * (b - a))
    for _ in range(golden_iters):
        if b - a <= max(2, min_amount // 1000):
            break
        if f(c) >= f(d):
            b, d = d, c
            c = int(b - PHI * (b - a))
        else:
            a, c = c, d
            d = int(a + PHI * (b - a))
    for x in (a, b, c, d):
        if min_amount <= x <= max_amount and f(x) > best_v:
            best_x, best_v = x, f(x)
    return OptimizationResult(best_x, cache[best_x][1], best_v, evals, max_amount)
