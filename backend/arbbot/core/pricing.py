"""Unified exact quoting over heterogeneous pools, operating on in-memory state only (no RPC).

`quote_hop` mutates nothing; `apply_hop` returns the post-trade pool state so that multi-hop routes that
touch the same pool twice (or sequential opportunities) are priced consistently.
"""
from __future__ import annotations

from dataclasses import dataclass

from . import math_v2, math_v3, math_solidly
from .types import DexKind, Pool, Route, Token


class QuoteError(Exception):
    pass


@dataclass
class HopQuote:
    amount_in: int
    amount_out: int
    fee_paid: int  # LP fee in token_in units (approximate for V3: exact fee amount from the swap math)
    price_impact_bps: float
    ticks_crossed: int = 0
    complete: bool = True


def _mid_price(pool: Pool, token_in: Token) -> float:
    """Marginal out-per-in price before the trade (for price-impact estimation)."""
    is0 = pool.is_token0(token_in.address)
    if pool.kind in (DexKind.UNIV3, DexKind.PANCAKE_V3):
        if not pool.v3 or pool.v3.sqrt_price_x96 == 0:
            return 0.0
        p = (pool.v3.sqrt_price_x96 / math_v3.Q96) ** 2  # token1 per token0 (raw)
        return p if is0 else (1 / p if p else 0.0)
    r_in, r_out = (pool.reserve0, pool.reserve1) if is0 else (pool.reserve1, pool.reserve0)
    if pool.kind == DexKind.SOLIDLY and pool.stable:
        # numeric derivative with a tiny probe
        st = pool.solidly_state()
        probe = max(1, min(r_in // 10_000_000, 10 ** token_in.decimals))
        out = math_solidly.get_amount_out(
            math_solidly.SolidlyPoolState(st.reserve0, st.reserve1, st.decimals0, st.decimals1, st.stable, 0), probe, is0
        )
        return out / probe if probe else 0.0
    return r_out / r_in if r_in else 0.0


def quote_hop(pool: Pool, token_in: Token, amount_in: int) -> HopQuote:
    if amount_in <= 0:
        raise QuoteError("amount_in <= 0")
    if pool.quarantined:
        raise QuoteError(f"pool quarantined: {pool.quarantine_reason}")
    if not pool.has(token_in.address):
        raise QuoteError(f"token {token_in.symbol} not in pool {pool.short()}")
    is0 = pool.is_token0(token_in.address)
    mid = _mid_price(pool, token_in)

    if pool.kind == DexKind.UNIV2:
        r_in, r_out = (pool.reserve0, pool.reserve1) if is0 else (pool.reserve1, pool.reserve0)
        if r_in == 0 or r_out == 0:
            raise QuoteError("empty V2 reserves")
        out = math_v2.get_amount_out(amount_in, r_in, r_out, pool.fee_ppm)
        if out >= r_out:
            raise QuoteError("V2 output exceeds reserves")
        fee = amount_in * pool.fee_ppm // 1_000_000
        impact = _impact(mid, amount_in, out)
        return HopQuote(amount_in, out, fee, impact)

    if pool.kind == DexKind.SOLIDLY:
        st = pool.solidly_state()
        if st.reserve0 == 0 or st.reserve1 == 0:
            raise QuoteError("empty Solidly reserves")
        out = math_solidly.get_amount_out(st, amount_in, is0)
        r_out = st.reserve1 if is0 else st.reserve0
        if out >= r_out:
            raise QuoteError("Solidly output exceeds reserves")
        fee = amount_in * st.fee_bps // 10_000
        return HopQuote(amount_in, out, fee, _impact(mid, amount_in, out))

    if pool.kind in (DexKind.UNIV3, DexKind.PANCAKE_V3):
        if pool.v3 is None:
            raise QuoteError("V3 state missing")
        try:
            res = math_v3.simulate_swap(pool.v3, is0, amount_in)
        except math_v3.IncompleteTickData as e:
            raise QuoteError(f"incomplete tick data ({e})") from e
        except math_v3.V3MathError as e:
            raise QuoteError(f"v3 math: {e}") from e
        if not res.fully_filled:
            raise QuoteError("V3 liquidity exhausted for this size")
        fee = amount_in * pool.fee_ppm // 1_000_000
        return HopQuote(res.amount_in, res.amount_out, fee, _impact(mid, amount_in, res.amount_out), res.ticks_crossed, True)

    raise QuoteError(f"unsupported pool kind {pool.kind}")


def apply_hop(pool: Pool, token_in: Token, amount_in: int, amount_out: int) -> Pool:
    """Return a shallow copy of `pool` with state advanced by the trade (for same-pool re-use within a route)."""
    import copy

    p = copy.copy(pool)
    is0 = pool.is_token0(token_in.address)
    if pool.kind in (DexKind.UNIV3, DexKind.PANCAKE_V3) and pool.v3:
        res = math_v3.simulate_swap(pool.v3, is0, amount_in)
        st = pool.v3.copy()
        st.sqrt_price_x96, st.tick, st.liquidity = res.sqrt_price_after, res.tick_after, res.liquidity_after
        p.v3 = st
        return p
    if pool.kind == DexKind.SOLIDLY:
        fee = amount_in * (pool.fee_ppm // 100) // 10_000
        amount_in_net = amount_in - fee  # fees leave the pool in Solidly
    else:
        amount_in_net = amount_in
    if is0:
        p.reserve0, p.reserve1 = pool.reserve0 + amount_in_net, pool.reserve1 - amount_out
    else:
        p.reserve0, p.reserve1 = pool.reserve0 - amount_out, pool.reserve1 + amount_in_net
    return p


def _impact(mid: float, amount_in: int, amount_out: int) -> float:
    if mid <= 0 or amount_in <= 0:
        return 0.0
    exec_price = amount_out / amount_in
    return max(0.0, (1 - exec_price / mid) * 10_000)


@dataclass
class RouteQuote:
    amount_in: int
    amount_out: int
    hop_amounts: list[int]
    swap_fees_in_start_token: int
    price_impact_bps: float
    ticks_crossed: int

    @property
    def gross_profit(self) -> int:
        return self.amount_out - self.amount_in


def quote_route(route: Route, amount_in: int) -> RouteQuote:
    """Exact route output. Handles routes that touch the same pool more than once."""
    pools: dict[str, Pool] = {}
    amount = amount_in
    amounts = [amount_in]
    fees_start = 0
    impact = 0.0
    ticks = 0
    scale = 1.0  # converts current-token fee to start-token units via cumulative price
    for hop in route.hops:
        pool = pools.get(hop.pool.address.lower(), hop.pool)
        q = quote_hop(pool, hop.token_in, amount)
        fees_start += int(q.fee_paid * scale)
        impact += q.price_impact_bps
        ticks += q.ticks_crossed
        pools[hop.pool.address.lower()] = apply_hop(pool, hop.token_in, amount, q.amount_out)
        scale = scale * (amount / q.amount_out) if q.amount_out else scale
        amount = q.amount_out
        amounts.append(amount)
    return RouteQuote(amount_in, amount, amounts, fees_start, impact, ticks)
