"""Exact Uniswap V3 swap math (TickMath, SqrtPriceMath, SwapMath, tick-bitmap walk).

Ported from Uniswap/v3-core (GPL-2.0-or-later) with Python big integers. Every rounding direction and
overflow-dependent branch of the Solidity code is reproduced so that `simulate_swap` returns the *same*
amounts the pool contract would. This is validated bit-for-bit against the real pool bytecode in
backend/tests/test_math_vs_chain.py (needs the local anvil devnet).

Also applicable (same core math) to: PancakeSwap V3, SushiSwap V3, Aerodrome Slipstream, Uniswap V4 pools
(for V4 the state must be read from the PoolManager via extsload — not implemented here).
"""
from __future__ import annotations

from dataclasses import dataclass, field

Q32 = 1 << 32
Q96 = 1 << 96
Q128 = 1 << 128
UINT160_MAX = (1 << 160) - 1
UINT256_MAX = (1 << 256) - 1
MIN_TICK = -887272
MAX_TICK = 887272
MIN_SQRT_RATIO = 4295128739
MAX_SQRT_RATIO = 1461446703485210103287273052203988822378723970342


class V3MathError(ValueError):
    pass


class IncompleteTickData(V3MathError):
    """The swap would cross into a tick-bitmap word that was not fetched; quote is unreliable."""


# --------------------------------------------------------------------------------------
# FullMath
# --------------------------------------------------------------------------------------


def mul_div(a: int, b: int, d: int) -> int:
    if d == 0:
        raise V3MathError("division by zero")
    return (a * b) // d


def mul_div_rounding_up(a: int, b: int, d: int) -> int:
    r = (a * b) // d
    if (a * b) % d != 0:
        r += 1
    if r > UINT256_MAX:
        raise V3MathError("mulDivRoundingUp overflow")
    return r


def div_rounding_up(x: int, y: int) -> int:
    return x // y + (1 if x % y != 0 else 0)


# --------------------------------------------------------------------------------------
# TickMath
# --------------------------------------------------------------------------------------

_TICK_CONSTS = [
    (0x2, 0xFFF97272373D413259A46990580E213A),
    (0x4, 0xFFF2E50F5F656932EF12357CF3C7FDCC),
    (0x8, 0xFFE5CACA7E10E4E61C3624EAA0941CD0),
    (0x10, 0xFFCB9843D60F6159C9DB58835C926644),
    (0x20, 0xFF973B41FA98C081472E6896DFB254C0),
    (0x40, 0xFF2EA16466C96A3843EC78B326B52861),
    (0x80, 0xFE5DEE046A99A2A811C461F1969C3053),
    (0x100, 0xFCBE86C7900A88AEDCFFC83B479AA3A4),
    (0x200, 0xF987A7253AC413176F2B074CF7815E54),
    (0x400, 0xF3392B0822B70005940C7A398E4B70F3),
    (0x800, 0xE7159475A2C29B7443B29C7FA6E889D9),
    (0x1000, 0xD097F3BDFD2022B8845AD8F792AA5825),
    (0x2000, 0xA9F746462D870FDF8A65DC1F90E061E5),
    (0x4000, 0x70D869A156D2A1B890BB3DF62BAF32F7),
    (0x8000, 0x31BE135F97D08FD981231505542FCFA6),
    (0x10000, 0x9AA508B5B7A84E1C677DE54F3E99BC9),
    (0x20000, 0x5D6AF8DEDB81196699C329225EE604),
    (0x40000, 0x2216E584F5FA1EA926041BEDFE98),
    (0x80000, 0x48A170391F7DC42444E8FA2),
]


def get_sqrt_ratio_at_tick(tick: int) -> int:
    abs_tick = -tick if tick < 0 else tick
    if abs_tick > MAX_TICK:
        raise V3MathError("T")
    ratio = 0xFFFCB933BD6FAD37AA2D162D1A594001 if abs_tick & 0x1 else 0x100000000000000000000000000000000
    for mask, c in _TICK_CONSTS:
        if abs_tick & mask:
            ratio = (ratio * c) >> 128
    if tick > 0:
        ratio = UINT256_MAX // ratio
    return (ratio >> 32) + (1 if ratio % Q32 != 0 else 0)


def get_tick_at_sqrt_ratio(sqrt_price_x96: int) -> int:
    if not (MIN_SQRT_RATIO <= sqrt_price_x96 < MAX_SQRT_RATIO):
        raise V3MathError("R")
    ratio = sqrt_price_x96 << 32
    r = ratio
    msb = 0
    for shift, threshold in (
        (7, 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF),
        (6, 0xFFFFFFFFFFFFFFFF),
        (5, 0xFFFFFFFF),
        (4, 0xFFFF),
        (3, 0xFF),
        (2, 0xF),
        (1, 0x3),
    ):
        f = (1 << shift) if r > threshold else 0
        msb |= f
        r >>= f
    f = 1 if r > 0x1 else 0
    msb |= f

    r = ratio >> (msb - 127) if msb >= 128 else ratio << (127 - msb)
    log_2 = (msb - 128) << 64
    for i in range(63, 49, -1):
        r = (r * r) >> 127
        f = r >> 128
        log_2 |= f << i
        r >>= f
    log_sqrt10001 = log_2 * 255738958999603826347141
    tick_low = (log_sqrt10001 - 3402992956809132418596140100660247210) >> 128
    tick_hi = (log_sqrt10001 + 291339464771989622907027621153398088495) >> 128
    if tick_low == tick_hi:
        return tick_low
    return tick_hi if get_sqrt_ratio_at_tick(tick_hi) <= sqrt_price_x96 else tick_low


# --------------------------------------------------------------------------------------
# SqrtPriceMath
# --------------------------------------------------------------------------------------


def get_next_sqrt_price_from_amount0_rounding_up(sqrt_px96: int, liquidity: int, amount: int, add: bool) -> int:
    if amount == 0:
        return sqrt_px96
    numerator1 = liquidity << 96
    product = amount * sqrt_px96
    if add:
        if product <= UINT256_MAX:
            denominator = numerator1 + product
            if denominator <= UINT256_MAX:
                return mul_div_rounding_up(numerator1, sqrt_px96, denominator)
        return div_rounding_up(numerator1, numerator1 // sqrt_px96 + amount)
    if not (product <= UINT256_MAX and numerator1 > product):
        raise V3MathError("price underflow")
    denominator = numerator1 - product
    res = mul_div_rounding_up(numerator1, sqrt_px96, denominator)
    if res > UINT160_MAX:
        raise V3MathError("price overflow")
    return res


def get_next_sqrt_price_from_amount1_rounding_down(sqrt_px96: int, liquidity: int, amount: int, add: bool) -> int:
    if add:
        quotient = (amount << 96) // liquidity if amount <= UINT160_MAX else mul_div(amount, Q96, liquidity)
        res = sqrt_px96 + quotient
        if res > UINT160_MAX:
            raise V3MathError("price overflow")
        return res
    quotient = (
        div_rounding_up(amount << 96, liquidity) if amount <= UINT160_MAX else mul_div_rounding_up(amount, Q96, liquidity)
    )
    if sqrt_px96 <= quotient:
        raise V3MathError("price underflow")
    return sqrt_px96 - quotient


def get_next_sqrt_price_from_input(sqrt_px96: int, liquidity: int, amount_in: int, zero_for_one: bool) -> int:
    if sqrt_px96 <= 0 or liquidity <= 0:
        raise V3MathError("bad state")
    if zero_for_one:
        return get_next_sqrt_price_from_amount0_rounding_up(sqrt_px96, liquidity, amount_in, True)
    return get_next_sqrt_price_from_amount1_rounding_down(sqrt_px96, liquidity, amount_in, True)


def get_next_sqrt_price_from_output(sqrt_px96: int, liquidity: int, amount_out: int, zero_for_one: bool) -> int:
    if sqrt_px96 <= 0 or liquidity <= 0:
        raise V3MathError("bad state")
    if zero_for_one:
        return get_next_sqrt_price_from_amount1_rounding_down(sqrt_px96, liquidity, amount_out, False)
    return get_next_sqrt_price_from_amount0_rounding_up(sqrt_px96, liquidity, amount_out, False)


def get_amount0_delta(sqrt_a: int, sqrt_b: int, liquidity: int, round_up: bool) -> int:
    if sqrt_a > sqrt_b:
        sqrt_a, sqrt_b = sqrt_b, sqrt_a
    numerator1 = liquidity << 96
    numerator2 = sqrt_b - sqrt_a
    if sqrt_a <= 0:
        raise V3MathError("sqrt_a == 0")
    if round_up:
        return div_rounding_up(mul_div_rounding_up(numerator1, numerator2, sqrt_b), sqrt_a)
    return mul_div(numerator1, numerator2, sqrt_b) // sqrt_a


def get_amount1_delta(sqrt_a: int, sqrt_b: int, liquidity: int, round_up: bool) -> int:
    if sqrt_a > sqrt_b:
        sqrt_a, sqrt_b = sqrt_b, sqrt_a
    if round_up:
        return mul_div_rounding_up(liquidity, sqrt_b - sqrt_a, Q96)
    return mul_div(liquidity, sqrt_b - sqrt_a, Q96)


# --------------------------------------------------------------------------------------
# SwapMath
# --------------------------------------------------------------------------------------


def compute_swap_step(
    sqrt_current: int, sqrt_target: int, liquidity: int, amount_remaining: int, fee_pips: int
) -> tuple[int, int, int, int]:
    """Returns (sqrt_next, amount_in, amount_out, fee_amount)."""
    zero_for_one = sqrt_current >= sqrt_target
    exact_in = amount_remaining >= 0

    if exact_in:
        amount_remaining_less_fee = mul_div(amount_remaining, 1_000_000 - fee_pips, 1_000_000)
        amount_in = (
            get_amount0_delta(sqrt_target, sqrt_current, liquidity, True)
            if zero_for_one
            else get_amount1_delta(sqrt_current, sqrt_target, liquidity, True)
        )
        if amount_remaining_less_fee >= amount_in:
            sqrt_next = sqrt_target
        else:
            sqrt_next = get_next_sqrt_price_from_input(sqrt_current, liquidity, amount_remaining_less_fee, zero_for_one)
        amount_out = 0
    else:
        amount_out = (
            get_amount1_delta(sqrt_target, sqrt_current, liquidity, False)
            if zero_for_one
            else get_amount0_delta(sqrt_current, sqrt_target, liquidity, False)
        )
        if -amount_remaining >= amount_out:
            sqrt_next = sqrt_target
        else:
            sqrt_next = get_next_sqrt_price_from_output(sqrt_current, liquidity, -amount_remaining, zero_for_one)
        amount_in = 0

    is_max = sqrt_target == sqrt_next
    if zero_for_one:
        if not (is_max and exact_in):
            amount_in = get_amount0_delta(sqrt_next, sqrt_current, liquidity, True)
        if not (is_max and not exact_in):
            amount_out = get_amount1_delta(sqrt_next, sqrt_current, liquidity, False)
    else:
        if not (is_max and exact_in):
            amount_in = get_amount1_delta(sqrt_current, sqrt_next, liquidity, True)
        if not (is_max and not exact_in):
            amount_out = get_amount0_delta(sqrt_current, sqrt_next, liquidity, False)

    if not exact_in and amount_out > -amount_remaining:
        amount_out = -amount_remaining

    if exact_in and sqrt_next != sqrt_target:
        fee_amount = amount_remaining - amount_in
    else:
        fee_amount = mul_div_rounding_up(amount_in, fee_pips, 1_000_000 - fee_pips)
    return sqrt_next, amount_in, amount_out, fee_amount


# --------------------------------------------------------------------------------------
# Tick bitmap
# --------------------------------------------------------------------------------------


def _msb(x: int) -> int:
    return x.bit_length() - 1


def _lsb(x: int) -> int:
    return (x & -x).bit_length() - 1


def _position(tick: int) -> tuple[int, int]:
    return tick >> 8, tick & 0xFF  # arithmetic shift == Solidity int24 >> 8 (floor)


def next_initialized_tick_within_one_word(
    bitmap: dict[int, int], tick: int, tick_spacing: int, lte: bool
) -> tuple[int, bool]:
    compressed = tick // tick_spacing  # Python floor division matches the Solidity adjustment for negatives
    if lte:
        word_pos, bit_pos = _position(compressed)
        if word_pos not in bitmap:
            raise IncompleteTickData(word_pos)
        mask = (1 << bit_pos) - 1 + (1 << bit_pos)
        masked = bitmap[word_pos] & mask
        initialized = masked != 0
        nxt = (compressed - (bit_pos - _msb(masked))) * tick_spacing if initialized else (compressed - bit_pos) * tick_spacing
        return nxt, initialized
    word_pos, bit_pos = _position(compressed + 1)
    if word_pos not in bitmap:
        raise IncompleteTickData(word_pos)
    mask = (~((1 << bit_pos) - 1)) & UINT256_MAX
    masked = bitmap[word_pos] & mask
    initialized = masked != 0
    nxt = (
        (compressed + 1 + (_lsb(masked) - bit_pos)) * tick_spacing
        if initialized
        else (compressed + 1 + (255 - bit_pos)) * tick_spacing
    )
    return nxt, initialized


# --------------------------------------------------------------------------------------
# Pool state + swap simulation
# --------------------------------------------------------------------------------------


@dataclass
class V3PoolState:
    sqrt_price_x96: int
    tick: int
    liquidity: int
    fee_pips: int
    tick_spacing: int
    tick_bitmap: dict[int, int] = field(default_factory=dict)  # word index -> 256-bit word
    ticks_liquidity_net: dict[int, int] = field(default_factory=dict)  # tick -> liquidityNet (int128)

    def copy(self) -> "V3PoolState":
        return V3PoolState(
            self.sqrt_price_x96,
            self.tick,
            self.liquidity,
            self.fee_pips,
            self.tick_spacing,
            dict(self.tick_bitmap),
            dict(self.ticks_liquidity_net),
        )


@dataclass
class SwapResult:
    amount_in: int  # input consumed (including fee)
    amount_out: int
    sqrt_price_after: int
    tick_after: int
    liquidity_after: int
    ticks_crossed: int
    fully_filled: bool  # False if liquidity ran out / price limit reached before the full input was used


def simulate_swap(
    state: V3PoolState, zero_for_one: bool, amount_specified: int, sqrt_price_limit_x96: int | None = None
) -> SwapResult:
    """Exact-input (amount_specified > 0) or exact-output (< 0) swap on an in-memory pool state.

    Raises IncompleteTickData when the walk leaves the fetched bitmap words.
    """
    if amount_specified == 0:
        raise V3MathError("AS")
    if sqrt_price_limit_x96 is None:
        sqrt_price_limit_x96 = MIN_SQRT_RATIO + 1 if zero_for_one else MAX_SQRT_RATIO - 1
    if zero_for_one:
        if not (sqrt_price_limit_x96 < state.sqrt_price_x96 and sqrt_price_limit_x96 > MIN_SQRT_RATIO):
            raise V3MathError("SPL")
    else:
        if not (sqrt_price_limit_x96 > state.sqrt_price_x96 and sqrt_price_limit_x96 < MAX_SQRT_RATIO):
            raise V3MathError("SPL")

    exact_input = amount_specified > 0
    remaining = amount_specified
    calculated = 0
    sqrt_price = state.sqrt_price_x96
    tick = state.tick
    liquidity = state.liquidity
    crossed = 0

    while remaining != 0 and sqrt_price != sqrt_price_limit_x96:
        sqrt_start = sqrt_price
        tick_next, initialized = next_initialized_tick_within_one_word(
            state.tick_bitmap, tick, state.tick_spacing, zero_for_one
        )
        if tick_next < MIN_TICK:
            tick_next = MIN_TICK
        elif tick_next > MAX_TICK:
            tick_next = MAX_TICK
        sqrt_next = get_sqrt_ratio_at_tick(tick_next)
        if zero_for_one:
            target = sqrt_price_limit_x96 if sqrt_next < sqrt_price_limit_x96 else sqrt_next
        else:
            target = sqrt_price_limit_x96 if sqrt_next > sqrt_price_limit_x96 else sqrt_next

        if liquidity > 0:
            sqrt_price, step_in, step_out, fee_amount = compute_swap_step(sqrt_price, target, liquidity, remaining, state.fee_pips)
        else:
            # No liquidity in range: price jumps to the target without trading (mirrors computeSwapStep with L=0
            # which the pool never calls; the pool loop still advances the tick).
            sqrt_price, step_in, step_out, fee_amount = target, 0, 0, 0

        if exact_input:
            remaining -= step_in + fee_amount
            calculated -= step_out
        else:
            remaining += step_out
            calculated += step_in + fee_amount

        if sqrt_price == sqrt_next:
            if initialized:
                liquidity_net = state.ticks_liquidity_net.get(tick_next)
                if liquidity_net is None:
                    raise IncompleteTickData(f"tick {tick_next}")
                if zero_for_one:
                    liquidity_net = -liquidity_net
                liquidity += liquidity_net
                if liquidity < 0:
                    raise V3MathError("negative liquidity")
                crossed += 1
            tick = tick_next - 1 if zero_for_one else tick_next
        elif sqrt_price != sqrt_start:
            tick = get_tick_at_sqrt_ratio(sqrt_price)

    if exact_input:
        amount_in = amount_specified - remaining
        amount_out = -calculated
    else:
        amount_in = calculated
        amount_out = -(amount_specified - remaining)
    return SwapResult(amount_in, amount_out, sqrt_price, tick, liquidity, crossed, remaining == 0)


def price_from_sqrt(sqrt_price_x96: int, decimals0: int, decimals1: int) -> float:
    """Human price of token0 in token1 units (display only)."""
    p = (sqrt_price_x96 / Q96) ** 2
    return p * (10**decimals0) / (10**decimals1)
