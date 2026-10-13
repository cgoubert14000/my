"""Exact Uniswap V2 constant-product math (integer, bit-for-bit identical to the pair contract).

Uniswap V2:   amountOut = amountIn*997*rOut / (rIn*1000 + amountIn*997)
Generalised:  fee expressed in parts-per-million (3000 = 0.30 %, 2500 = 0.25 % PancakeSwap V2, 1000 = 0.10 %).
Scaling numerator and denominator by the same factor does not change the floor division, so this is exact.
"""
from __future__ import annotations

PPM = 1_000_000


class InsufficientLiquidity(ValueError):
    pass


def get_amount_out(amount_in: int, reserve_in: int, reserve_out: int, fee_ppm: int = 3000) -> int:
    if amount_in <= 0:
        return 0
    if reserve_in <= 0 or reserve_out <= 0:
        raise InsufficientLiquidity("empty reserves")
    amount_in_with_fee = amount_in * (PPM - fee_ppm)
    numerator = amount_in_with_fee * reserve_out
    denominator = reserve_in * PPM + amount_in_with_fee
    return numerator // denominator


def get_amount_in(amount_out: int, reserve_in: int, reserve_out: int, fee_ppm: int = 3000) -> int:
    """Minimal input to receive exactly `amount_out` (mirrors UniswapV2Library.getAmountIn, rounds up)."""
    if amount_out <= 0:
        return 0
    if reserve_in <= 0 or reserve_out <= amount_out:
        raise InsufficientLiquidity("insufficient reserve_out")
    numerator = reserve_in * amount_out * PPM
    denominator = (reserve_out - amount_out) * (PPM - fee_ppm)
    return numerator // denominator + 1


def spot_price(reserve_in: int, reserve_out: int) -> float:
    """Marginal price (out per in) ignoring fees. For display / spread estimation only."""
    if reserve_in == 0:
        return 0.0
    return reserve_out / reserve_in


def optimal_two_pool_amount(r_in_a: int, r_out_a: int, r_in_b: int, r_out_b: int, fee_a_ppm: int, fee_b_ppm: int) -> int:
    """Closed-form optimal input for a 2-hop V2/V2 cycle (token -> A -> mid -> B -> token).

    Derived from maximising f(x) = out_B(out_A(x)) - x. Used as a warm start for the numeric optimiser;
    the optimiser still verifies with exact integer math because of rounding.
    """
    from math import isqrt

    ga = PPM - fee_a_ppm
    gb = PPM - fee_b_ppm
    # Effective combined pool: E_in = r_in_a * r_in_b * PPM / (r_in_b*PPM + ga*r_out_a) ... see docs/03_architecture.md
    # Use the standard result: x* = (sqrt(Ea*Eb*ga*gb/PPM^2) - Ea) / (ga/PPM)
    denom = r_in_b * PPM + ga * r_out_a
    if denom == 0:
        return 0
    ea = (r_in_a * r_in_b * PPM) // denom
    eb = (ga * r_out_a * r_out_b) // denom
    if ea <= 0 or eb <= 0:
        return 0
    root = isqrt(ea * eb * ga * gb) // PPM
    x = (root - ea) * PPM // ga
    return max(x, 0)
