"""Exact Aerodrome / Velodrome V2 pool math (stable x³y + xy³ = k and volatile xy = k).

Verbatim port of aerodrome-finance/contracts `Pool.sol` (`_f`, `_d`, `_get_y`, `_k`, `getAmountOut`), including
the `_k(x0, y + 1)` quirk (re-applies decimal scaling) which matters for non-18-decimal tokens.
Fee is in basis points as returned by `PoolFactory.getFee(pool, stable)`.
"""
from __future__ import annotations

from dataclasses import dataclass

E18 = 10**18


class SolidlyMathError(ValueError):
    pass


@dataclass
class SolidlyPoolState:
    reserve0: int
    reserve1: int
    decimals0: int  # 10 ** decimals (as stored in the pool)
    decimals1: int
    stable: bool
    fee_bps: int


def _f(x0: int, y: int) -> int:
    a = (x0 * y) // E18
    b = (x0 * x0) // E18 + (y * y) // E18
    return (a * b) // E18


def _d(x0: int, y: int) -> int:
    return (3 * x0 * ((y * y) // E18)) // E18 + ((((x0 * x0) // E18) * x0) // E18)


def _k(x: int, y: int, state: SolidlyPoolState) -> int:
    if state.stable:
        _x = (x * E18) // state.decimals0
        _y = (y * E18) // state.decimals1
        a = (_x * _y) // E18
        b = (_x * _x) // E18 + (_y * _y) // E18
        return (a * b) // E18
    return x * y


def _get_y(x0: int, xy: int, y: int, state: SolidlyPoolState) -> int:
    for _ in range(255):
        k = _f(x0, y)
        if k < xy:
            dy = ((xy - k) * E18) // _d(x0, y)
            if dy == 0:
                if k == xy:
                    return y
                if _k(x0, y + 1, state) > xy:
                    return y + 1
                dy = 1
            y = y + dy
        else:
            dy = ((k - xy) * E18) // _d(x0, y)
            if dy == 0:
                if k == xy or _f(x0, y - 1) < xy:
                    return y
                dy = 1
            y = y - dy
    raise SolidlyMathError("!y")


def get_amount_out(state: SolidlyPoolState, amount_in: int, token_in_is0: bool) -> int:
    """Mirrors `Pool.getAmountOut(amountIn, tokenIn)` (fee removed first, then curve)."""
    if amount_in <= 0:
        return 0
    amount_in = amount_in - (amount_in * state.fee_bps) // 10_000
    r0, r1 = state.reserve0, state.reserve1
    if state.stable:
        xy = _k(r0, r1, state)
        r0 = (r0 * E18) // state.decimals0
        r1 = (r1 * E18) // state.decimals1
        reserve_a, reserve_b = (r0, r1) if token_in_is0 else (r1, r0)
        amount_in = (amount_in * E18) // state.decimals0 if token_in_is0 else (amount_in * E18) // state.decimals1
        y = reserve_b - _get_y(amount_in + reserve_a, xy, reserve_b, state)
        return (y * (state.decimals1 if token_in_is0 else state.decimals0)) // E18
    reserve_a, reserve_b = (r0, r1) if token_in_is0 else (r1, r0)
    return (amount_in * reserve_b) // (reserve_a + amount_in)
