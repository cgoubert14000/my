"""Pure unit tests of the exact pricing math (no chain needed)."""
from __future__ import annotations

from hypothesis import given, settings as hsettings, strategies as st

from arbbot.core import math_v2, math_solidly
from arbbot.core.math_v3 import get_sqrt_ratio_at_tick, get_tick_at_sqrt_ratio
from arbbot.core.pricing import QuoteError, quote_hop, quote_route
from arbbot.core.types import DexKind, Hop, Pool, Route, Token

WETH = Token("0x" + "aa" * 20, "WETH", 18)
USDC = Token("0x" + "bb" * 20, "USDC", 6)
DAI = Token("0x" + "cc" * 20, "DAI", 18)


def v2(addr: str, t0: Token, t1: Token, r0: int, r1: int, fee_ppm: int = 3000, dex: str = "uniswap_v2") -> Pool:
    return Pool(address=addr, dex=dex, kind=DexKind.UNIV2, token0=t0, token1=t1, fee_ppm=fee_ppm, reserve0=r0, reserve1=r1)


def test_v2_matches_reference_formula():
    out = math_v2.get_amount_out(1_000_000, 10**24, 2_000 * 10**12, 3000)
    ref = 1_000_000 * 997 * (2_000 * 10**12) // (10**24 * 1000 + 1_000_000 * 997)
    assert out == ref


@given(st.integers(1, 10**30), st.integers(10**6, 10**30), st.integers(10**6, 10**30), st.integers(0, 10_000))
@hsettings(max_examples=300)
def test_v2_output_never_breaks_k(amount_in, r_in, r_out, fee_ppm):
    out = math_v2.get_amount_out(amount_in, r_in, r_out, fee_ppm)
    assert 0 <= out < r_out
    # Uniswap V2 invariant with fee taken on input: (r_in*1e6 + in*(1e6-fee)) * (r_out-out) >= r_in*r_out*1e6
    bal_in_adj = (r_in + amount_in) * 1_000_000 - amount_in * fee_ppm
    assert bal_in_adj * (r_out - out) >= r_in * r_out * 1_000_000


def test_v2_fee_on_input_reduces_output():
    a = math_v2.get_amount_out(10**18, 10**22, 10**22, 0)
    b = math_v2.get_amount_out(10**18, 10**22, 10**22, 3000)
    assert b < a


def test_v3_tick_sqrt_roundtrip():
    for tick in (-887272, -100_000, -1, 0, 1, 12345, 887271):
        s = get_sqrt_ratio_at_tick(tick)
        assert get_tick_at_sqrt_ratio(s) == tick


def test_solidly_stable_close_to_peg_and_volatile_equals_v2_shape():
    # stable USDC/DAI 1:1 with 1 bps fee: output ≈ input for a small trade
    state = math_solidly.SolidlyPoolState(reserve0=10**12, reserve1=10**24, decimals0=10**6, decimals1=10**18, stable=True, fee_bps=1)
    out = math_solidly.get_amount_out(state, 1_000 * 10**6, token_in_is0=True)
    assert abs(out / 10**18 - 1_000 * 0.9999) < 0.05
    vol = math_solidly.SolidlyPoolState(reserve0=10**21, reserve1=2_000 * 10**9, decimals0=10**18, decimals1=10**6, stable=False, fee_bps=30)
    out_v = math_solidly.get_amount_out(vol, 10**18, token_in_is0=True)
    amt = 10**18 - 10**18 * 30 // 10_000
    assert out_v == amt * (2_000 * 10**9) // (10**21 + amt)


def test_route_quote_two_hop_profit_and_loss():
    # pool A: 1 ETH = 2000 USDC ; pool B: 1 ETH = 2040 USDC → buy ETH on A, sell on B
    a = v2("0x" + "01" * 20, WETH, USDC, 1_000 * 10**18, 2_000_000 * 10**6)
    b = v2("0x" + "02" * 20, WETH, USDC, 1_000 * 10**18, 2_040_000 * 10**6, dex="sushiswap")
    route = Route([Hop(a, USDC, WETH), Hop(b, WETH, USDC)])
    q = quote_route(route, 10_000 * 10**6)
    assert q.amount_out > 10_000 * 10**6  # ~2 % gap minus 0.6 % fees minus impact
    reverse = Route([Hop(b, USDC, WETH), Hop(a, WETH, USDC)])
    q2 = quote_route(reverse, 10_000 * 10**6)
    assert q2.amount_out < 10_000 * 10**6


def test_quote_rejects_zero_and_token_not_in_pool():
    a = v2("0x" + "01" * 20, WETH, USDC, 10**21, 2 * 10**12)
    try:
        quote_hop(a, DAI, 10**18)
        raise AssertionError("expected QuoteError")
    except QuoteError:
        pass
    try:
        quote_hop(a, WETH, 0)
        raise AssertionError("expected QuoteError")
    except QuoteError:
        pass


def test_price_impact_grows_with_size():
    a = v2("0x" + "01" * 20, WETH, USDC, 1_000 * 10**18, 2_000_000 * 10**6)
    small = quote_hop(a, USDC, 1_000 * 10**6)
    big = quote_hop(a, USDC, 200_000 * 10**6)
    assert big.price_impact_bps > small.price_impact_bps > 0
