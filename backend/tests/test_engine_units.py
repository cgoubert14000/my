"""Engine logic without a chain: optimizer, routes, selector gates, failure/edge paths."""
from __future__ import annotations

import asyncio
import time

import pytest

from arbbot.config.policy import AuthorizationPolicy, EXAMPLE
from arbbot.config.tunables import TunableParams
from arbbot.core.types import Decision, DexKind, FeeBreakdown, FlashSource, Hop, Opportunity, Pool, ProfitBreakdown, Route, Token
from arbbot.engine.optimizer import flash_fee_for, max_borrow_for_route, optimize_amount
from arbbot.engine.routes import build_routes, route_fee_bps, route_spread_bps
from arbbot.engine.selector import SelectionContext, Selector
from arbbot.reliability.model import Observation, ReliabilityModel
from arbbot.simulation.simulator import decode_revert
from arbbot.data.rpc import RpcClient, RpcError, selector as sel4
from eth_abi import encode as abi_encode

WETH = Token("0x" + "aa" * 20, "WETH", 18)
USDC = Token("0x" + "bb" * 20, "USDC", 6)
DAI = Token("0x" + "cc" * 20, "DAI", 18)


def v2(addr, t0, t1, r0, r1, dex="uniswap_v2", fee=3000):
    return Pool(address=addr, dex=dex, kind=DexKind.UNIV2, token0=t0, token1=t1, fee_ppm=fee, reserve0=r0, reserve1=r1,
                updated_at=time.time(), updated_block=1)


def two_pool_gap(gap=1.02):
    a = v2("0x" + "01" * 20, WETH, USDC, 1_000 * 10**18, 2_000_000 * 10**6)
    b = v2("0x" + "02" * 20, WETH, USDC, 1_000 * 10**18, int(2_000_000 * gap) * 10**6, dex="sushiswap")
    return a, b, Route([Hop(a, USDC, WETH), Hop(b, WETH, USDC)])


# ---------------------------------------------------------------- routes


def test_build_routes_2_and_3_hops_no_pool_reuse():
    a, b, _ = two_pool_gap()
    c = v2("0x" + "03" * 20, USDC, DAI, 10**12, 10**24)
    d = v2("0x" + "04" * 20, WETH, DAI, 10**21, 2 * 10**24, dex="sushiswap")
    routes = build_routes([a, b, c, d], [WETH, USDC], 3)
    assert routes
    for r in routes:
        pools = [h.pool.address for h in r.hops]
        assert len(set(pools)) == len(pools)
        assert r.hops[0].token_in.address == r.hops[-1].token_out.address
        for h1, h2 in zip(r.hops, r.hops[1:]):
            assert h1.token_out.address == h2.token_in.address
    assert any(len(r.hops) == 3 for r in routes)
    assert all(len(r.hops) <= 2 for r in build_routes([a, b, c, d], [WETH], 2))


def test_quarantined_pool_excluded():
    a, b, _ = two_pool_gap()
    b.quarantined = True
    assert build_routes([a, b], [USDC], 3) == []


def test_spread_and_fee_bps():
    _, _, r = two_pool_gap(1.02)
    assert 190 < route_spread_bps(r) < 210
    assert route_fee_bps(r) == 60


# ---------------------------------------------------------------- optimizer


def test_optimizer_finds_interior_optimum_matching_closed_form():
    from arbbot.core.math_v2 import optimal_two_pool_amount

    a, b, r = two_pool_gap(1.02)
    closed = optimal_two_pool_amount(a.reserve1, a.reserve0, b.reserve0, b.reserve1, 3000, 3000)
    res = optimize_amount(r, flash_fee_bps_x100=0, min_amount=10**6, max_amount=500_000 * 10**6)
    assert res.quote is not None and res.net_before_gas > 0
    # within 1 % of the analytical optimum (golden section on integers)
    assert abs(res.amount_in - closed) / closed < 0.01, (res.amount_in, closed)


def test_optimizer_reports_no_profit_when_gap_below_fees():
    _, _, r = two_pool_gap(1.003)  # 30 bps gap < 60 bps fees
    res = optimize_amount(r, flash_fee_bps_x100=0, min_amount=10**6, max_amount=100_000 * 10**6)
    assert res.net_before_gas <= 0 and res.reason == "no positive grid point"


def test_flash_fee_rounds_up_like_aave():
    assert flash_fee_for(10_000 * 10**6, 500) == 5 * 10**6  # 0.05 %
    assert flash_fee_for(1, 500) == 1  # ceil
    assert flash_fee_for(10**9, 0) == 0


def test_max_borrow_respects_depth_provider_and_policy():
    _, _, r = two_pool_gap()
    depth_cap = max_borrow_for_route(r, 0.25, None, None)
    assert 0 < depth_cap <= 2_000_000 * 10**6 * 0.25 + 1
    assert max_borrow_for_route(r, 0.25, 1_000 * 10**6, None) == 1_000 * 10**6
    assert max_borrow_for_route(r, 0.25, None, 500 * 10**6) == 500 * 10**6


# ---------------------------------------------------------------- selector gates


def opp(route, expected_net=10**6, **kw) -> Opportunity:
    fb = FeeBreakdown(flash_fee=0, gas_units=300_000, gas_price_wei=10**7, gas_cost_wei=3 * 10**12, gas_cost_token=6_000,
                      native_price_in_token=2000.0, failure_cost_wei=10**12)
    pb = ProfitBreakdown(amount_in=10_000 * 10**6, amount_out=10_000 * 10**6 + expected_net + 6_000, gross_profit=expected_net + 6_000,
                         expected_net=expected_net, fees=fb, margin_bps=expected_net / (10_000 * 10**6) * 1e4, price_impact_bps=20)
    o = Opportunity(id="x", ts=time.time(), chain_id=31337, block_number=1, route=route, flash_source=FlashSource.MORPHO,
                    flash_provider="0x" + "03" * 20, profit=pb, spread_bps=200, data_age_ms=100)
    for k, v in kw.items():
        setattr(o, k, v)
    return o


def ctx(policy=None, budget=None):
    return SelectionContext(TunableParams(), policy, budget, 2000.0, 1)


def trained_selector(n=60, rate=1.0) -> Selector:
    rel = ReliabilityModel(min_observations=30, credible_level=0.9, threshold=0.75)
    sel = Selector(rel)
    return sel, rel


def test_selector_requires_demonstrated_reliability():
    _, _, r = two_pool_gap()
    sel, rel = trained_selector()
    o = opp(r)
    sel.evaluate([o], ctx(), 0.75)
    assert o.decision == Decision.REJECTED and "reliability_not_demonstrated" in o.reasons
    # feed the matching bucket
    from arbbot.reliability.model import features_of

    f = features_of(o)
    for _ in range(40):
        rel.add(Observation(time.time(), f, 1, "ghost"))
    o2 = opp(r)
    sel.evaluate([o2], ctx(), 0.75)
    assert o2.decision == Decision.ELIGIBLE, o2.reasons
    assert sel.pick([o2]) is o2 and o2.decision == Decision.SELECTED


def _eligible_setup():
    _, _, r = two_pool_gap()
    sel, rel = trained_selector()
    from arbbot.reliability.model import features_of

    f = features_of(opp(r))
    for _ in range(40):
        rel.add(Observation(time.time(), f, 1, "ghost"))
    return r, sel


def test_gate_stale_data():
    r, sel = _eligible_setup()
    o = opp(r, data_age_ms=10_000)
    sel.evaluate([o], ctx(), 0.75)
    assert any(x.startswith("stale_data") for x in o.reasons)


def test_gate_simulation_failed_and_below_estimate():
    r, sel = _eligible_setup()
    o = opp(r, sim={"ok": False, "error": "FlashRepaymentImpossible"})
    sel.evaluate([o], ctx(), 0.75)
    assert any(x.startswith("simulation_failed") for x in o.reasons)
    o2 = opp(r, sim={"ok": True, "profit": 10})  # far below estimate → model wrong → reject
    sel.evaluate([o2], ctx(), 0.75)
    assert any(x.startswith("sim_below_estimate") for x in o2.reasons)


def test_gate_unknown_costs_block_eligibility():
    r, sel = _eligible_setup()
    o = opp(r)
    o.profit.fees.unknowns.append("l1 fee oracle unavailable")
    sel.evaluate([o], ctx(), 0.75)
    assert any(x.startswith("unknown_costs") for x in o.reasons)


def test_gate_policy_allowlists_and_budget():
    r, sel = _eligible_setup()
    pol = AuthorizationPolicy.model_validate({**EXAMPLE, "enabled": True, "allowed_dexes": ["uniswap_v3"], "allowed_tokens": ["WETH"],
                                              "allowed_flash_providers": ["AAVE_V3"], "min_net_profit_native": 0.5,
                                              "valid_until": time.time() + 100, "max_transactions": 1, "max_total_budget_native": 0.001,
                                              "max_gas_per_tx_native": 0.0004})
    o = opp(r)
    sel.evaluate([o], ctx(pol, budget=0.000001), 0.75)
    joined = " ".join(o.reasons)
    assert "dex_not_allowed" in joined and "flash_provider_not_allowed" in joined and "token_not_allowed" in joined
    assert "net_below_policy_min" in joined and "gas_exceeds_remaining_budget" in joined


def test_negative_net_never_eligible_and_ev_ranking():
    r, sel = _eligible_setup()
    neg = opp(r, expected_net=-5)
    neg.decision = Decision.REJECTED
    neg.reasons.append("negative_expected_net")
    small, big = opp(r, expected_net=10**6), opp(r, expected_net=2 * 10**6)  # same margin bucket (0–3 bps)
    sel.evaluate([neg, small, big], ctx(), 0.75)
    assert neg.decision == Decision.REJECTED
    assert sel.pick([neg, small, big]) is big


# ---------------------------------------------------------------- revert decoding / rpc errors


def test_decode_custom_errors():
    data = sel4("InsufficientProfit(uint256,uint256)") + abi_encode(["uint256", "uint256"], [5, 10])
    assert decode_revert(data) == "InsufficientProfit(5, 10)"
    assert decode_revert(sel4("FlashRepaymentImpossible()")) == "FlashRepaymentImpossible"
    assert decode_revert(b"") == "revert (no data)"
    err = sel4("Error(string)") + abi_encode(["string"], ["TransferHelper: TRANSFER_FROM_FAILED"])
    assert "TRANSFER_FROM_FAILED" in decode_revert(err)


async def test_rpc_client_surfaces_connection_errors():
    rpc = RpcClient("http://127.0.0.1:1", timeout_s=0.5, max_rps=100)
    try:
        with pytest.raises(RpcError):
            await rpc.open()  # probes eth_chainId → unreachable endpoint must surface as RpcError, never hang
        with pytest.raises(RpcError):
            await rpc.request("eth_blockNumber", retries=1)
        assert rpc.metrics.errors >= 2
    finally:
        await rpc.close()


def test_db_count_opportunities_is_exact_beyond_page_limit(tmp_path):
    """Session reports must count every record (opportunities() is paginated)."""
    from arbbot.storage.db import Database

    db = Database(tmp_path / "t.sqlite")
    try:
        for i in range(250):
            db.upsert_opportunity({"id": f"o{i}", "ts": 1000.0 + i, "chain_id": 8453, "block_number": i, "route": "r", "route_key": "k",
                                   "token": "WETH", "amount_in": 1, "expected_net": -1, "decision": "REJECTED" if i % 5 else "ELIGIBLE"})
        assert db.count_opportunities() == 250
        assert db.count_opportunities(since=1200.0) == 50
        assert db.count_opportunities(decision="ELIGIBLE") == 50
        assert len(db.opportunities(limit=100)) == 100
    finally:
        db.close()
