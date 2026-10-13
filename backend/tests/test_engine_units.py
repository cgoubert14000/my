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


def opp(route, expected_net=10**7, **kw) -> Opportunity:  # 10 bps net: above the 2 bps on-chain safety floor
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
    small, big = opp(r, expected_net=10**7), opp(r, expected_net=15 * 10**6)  # same margin bucket (8–20 bps) as the trained one
    thin = opp(r, expected_net=10**6)  # 1 bps: positive but below the on-chain floor ⇒ never eligible
    sel.evaluate([neg, small, big, thin], ctx(), 0.75)
    assert neg.decision == Decision.REJECTED and thin.decision == Decision.REJECTED
    assert sel.pick([neg, small, big, thin]) is big


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
        # exact aggregates + ranking in SQL
        db.upsert_opportunity({"id": "pos", "ts": 1300.0, "chain_id": 8453, "block_number": 9, "route": "r+", "route_key": "k+", "token": "WETH",
                               "amount_in": 1, "expected_net": 5, "expected_net_eur": 0.5, "decision": "ELIGIBLE", "sim_ok": True,
                               "ghost_next_block_net": 3, "reasons": ["ghost_mode"]})
        db.upsert_opportunity({"id": "neg", "ts": 1300.0, "chain_id": 8453, "block_number": 9, "route": "r-", "route_key": "k-", "token": "WETH",
                               "amount_in": 1, "expected_net": -5, "expected_net_eur": -0.2, "decision": "REJECTED", "sim_ok": False,
                               "ghost_next_block_net": -1, "reasons": ["negative_expected_net: -5", "p_lower_below_threshold(0.1)"]})
        st = db.opportunity_stats()
        assert st["total"] == 252 and st["positive"] == 1 and st["simulated"] == 2 and st["sim_ok"] == 1 and st["sim_failed"] == 1
        assert st["ghost_labeled"] == 2 and st["ghost_positive"] == 1
        assert st["decisions"]["ELIGIBLE"] == 51
        if st["reject_reasons"] is not None:
            assert st["reject_reasons"] == {"ghost_mode": 1, "negative_expected_net": 1, "p_lower_below_threshold": 1}
        assert [o["id"] for o in db.top_opportunities(limit=5)] == ["pos", "neg"]
        assert [o["id"] for o in db.top_opportunities(limit=5, positive_only=True)] == ["pos"]
        # export stream: positives / simulated / labelled first, then the rest, capped
        ex = list(db.iter_export(None, max_rows=10))
        assert len(ex) == 10 and ex[0]["id"] == "pos" and ex[1]["id"] == "neg"
        assert len(list(db.iter_export(1300.0, max_rows=100))) == 2
    finally:
        db.close()


async def test_collector_refreshes_each_head_once_whatever_the_source():
    """WebSocket newHeads and polling may both see a block: it must be refreshed/published once."""
    import asyncio

    from arbbot.data.collector import StateCollector as Collector

    c = Collector.__new__(Collector)
    c._subscribers, c._stop, c._last_head, c._head_lock = [], asyncio.Event(), 0, asyncio.Lock()
    from arbbot.data.collector import CollectorStats

    c.stats = CollectorStats()
    refreshed: list[int] = []

    async def fake_refresh(bn, pools=None):
        await asyncio.sleep(0.01)
        refreshed.append(bn)
        return 0

    c.refresh = fake_refresh  # type: ignore[method-assign]
    q = c.subscribe()
    await asyncio.gather(c._on_head(100), c._on_head(100), c._on_head(99), c._on_head(101))
    assert refreshed == [100, 101] or refreshed == [101] or sorted(refreshed) == [100, 101]
    assert c.stats.blocks_seen == len(refreshed)
    assert q.qsize() == len(refreshed)


def test_selector_applies_the_onchain_safety_floor():
    """expected_net > 0 but below the safety margin ⇒ the contract would revert (minProfit = gas + margin) ⇒ not eligible."""
    _, _, r = two_pool_gap()
    sel, _ = trained_selector()
    t = TunableParams()
    amount_in = 10_000 * 10**6
    floor = int(amount_in * t.safety_margin_bps) // 10_000  # 2 bps of notional by default
    thin = opp(r, expected_net=floor - 1)
    fat = opp(r, expected_net=floor + 1)
    sel.evaluate([thin, fat], ctx(), 0.75)
    assert any(x.startswith("below_safety_margin") for x in thin.reasons)
    assert not any(x.startswith("below_safety_margin") for x in fat.reasons)
    assert "negative_expected_net" not in thin.reasons


def test_vectorised_screen_matches_per_route_formulas_and_is_fast():
    """The numpy screen must reproduce route_spread_bps/route_fee_bps and the depth rule for every route."""
    import time as _t

    import numpy as np

    from arbbot.engine.screen import RouteScreen

    p_a, p_b, _ = two_pool_gap()
    c = v2("0x" + "03" * 20, USDC, DAI, 10**12, 10**24)
    d = v2("0x" + "04" * 20, WETH, DAI, 10**21, 2 * 10**24, dex="sushiswap")
    routes = build_routes([p_a, p_b, c, d], [WETH, USDC], 3)
    assert routes
    sc = RouteScreen(routes)
    price = lambda tok: 1.0 if tok.symbol in ("USDC", "DAI") else 2000.0  # noqa: E731
    res = sc.run(min_spread_bps=-1e9, min_liquidity_usd=0, price_usd=price)
    for i, route in enumerate(routes):
        assert abs(res.spread_bps[i] - route_spread_bps(route)) < 1e-6 * max(1.0, abs(route_spread_bps(route)))
        assert abs((res.spread_bps[i] - res.edge_bps[i]) - route_fee_bps(route)) < 1e-9
    # survivors are sorted by edge, best first, and the depth rule rejects when any hop pool is too shallow
    assert list(res.edge_bps[res.survivors]) == sorted(res.edge_bps[res.survivors], reverse=True)
    deep = sc.run(min_spread_bps=-1e9, min_liquidity_usd=1e15, price_usd=price)
    assert len(deep.survivors) == 0 and deep.rejections.get("liquidity_below_min") == len(routes)
    noref = sc.run(min_spread_bps=-1e9, min_liquidity_usd=0, price_usd=lambda tok: None)
    assert len(noref.survivors) == 0 and noref.rejections.get("no_price_reference") == len(routes)
    # speed: 200k synthetic routes screened in well under a second
    big = RouteScreen(routes)
    reps = max(1, 200_000 // len(routes))
    big.idx = np.tile(big.idx, (reps, 1))
    big.sign = np.tile(big.sign, (reps, 1))
    t0 = _t.perf_counter()
    out = big.run(min_spread_bps=1.0, min_liquidity_usd=20_000, price_usd=price)
    assert (_t.perf_counter() - t0) < 1.0
    assert len(out.edge_bps) == len(routes) * reps
    # dynamic LP fees (Slipstream fee modules): a fee change on a pool is reflected at the next run, not cached
    pool0 = sc.pools[0]
    before = sc.run(min_spread_bps=-1e9, min_liquidity_usd=0, price_usd=price)
    pool0.fee_ppm += 1000  # +10 bps
    after = sc.run(min_spread_bps=-1e9, min_liquidity_usd=0, price_usd=price)
    uses = [i for i, r in enumerate(routes) if any(h.pool.address == pool0.address for h in r.hops)]
    assert uses, "fixture must contain routes through pool0"
    for i in uses:
        n_hops = sum(1 for h in routes[i].hops if h.pool.address == pool0.address)
        assert abs((before.edge_bps[i] - after.edge_bps[i]) - 10.0 * n_hops) < 1e-9
    pool0.fee_ppm -= 1000


async def test_collector_tracks_dynamic_lp_fee_changes():
    """Slipstream pools expose a dynamic fee(): the collector re-reads it every block and the pool/V3 state follow."""
    from arbbot.config.chains import get_chain
    from arbbot.core.math_v3 import V3PoolState
    from arbbot.data.collector import StateCollector
    from arbbot.data.rpc import encode_call

    chain = get_chain("base")
    pool = Pool("0x" + "aa" * 20, "aerodrome_slipstream", DexKind.UNIV3, WETH, USDC, 500, False, 100)
    pool.v3 = V3PoolState(2**96, 0, 10**18, 500, 100)

    class _Rpc:
        calls: list[tuple[str, bytes]] = []
        fee = 3000

        async def multicall(self, calls, block=None, chunk=300):
            self.calls = list(calls)
            out = []
            for _, data in calls:
                if data == encode_call("slot0()"):
                    out.append((True, abi_encode(["uint160", "int24"], [2**96, 0]) + b"\x00" * 160))
                elif data == encode_call("liquidity()"):
                    out.append((True, abi_encode(["uint128"], [10**18])))
                elif data == encode_call("fee()"):
                    out.append((True, abi_encode(["uint24"], [self.fee])))
                else:
                    out.append((True, abi_encode(["uint256"], [0])))
            return out

        async def get_block(self, block):
            return {"timestamp": hex(int(time.time())), "baseFeePerGas": hex(5_000_000)}

        async def block_number(self):
            return 1

    rpc = _Rpc()
    c = StateCollector(rpc, chain, [pool])  # type: ignore[arg-type]

    async def _noop(block, subset=None):
        return None

    c._refresh_ticks = _noop  # type: ignore[method-assign]
    c._refresh_balances = _noop  # type: ignore[method-assign]
    c._update_native_price = lambda: None  # type: ignore[method-assign]
    await c.refresh(block=101)
    assert any(d == encode_call("fee()") for _, d in rpc.calls), "dynamic-fee pools must be re-read every refresh"
    assert pool.fee_ppm == 3000 and pool.v3.fee_pips == 3000 and c.stats.fee_changes == 1
    rpc.fee = 3000
    await c.refresh(block=102)
    assert c.stats.fee_changes == 1  # unchanged fee → no event
    rpc.fee = 0  # invalid value is ignored, never applied
    await c.refresh(block=103)
    assert pool.fee_ppm == 3000
    # an immutable Uniswap V3 pool is only re-read on the periodic recheck block
    uni = Pool("0x" + "bb" * 20, "uniswap_v3", DexKind.UNIV3, WETH, USDC, 500, False, 10)
    c2 = StateCollector(rpc, chain, [uni])  # type: ignore[arg-type]
    c2._refresh_ticks = _noop  # type: ignore[method-assign]
    c2._refresh_balances = _noop  # type: ignore[method-assign]
    c2._update_native_price = lambda: None  # type: ignore[method-assign]
    await c2.refresh(block=101)
    assert not any(d == encode_call("fee()") for _, d in rpc.calls)
    await c2.refresh(block=300)
    assert any(d == encode_call("fee()") for _, d in rpc.calls)


def test_observations_survive_sessions_via_jsonl_export_import(tmp_path):
    """The CI runner is ephemeral: ghost labels are appended to docs/reports/real/observations_<chain>.jsonl at each
    snapshot and merged back (dedup on ts/source/route_key) at the next start-up, so the maturity decision accumulates."""
    from arbbot.app.runtime import Runtime
    from arbbot.config.chains import BASE
    from arbbot.config.settings import Settings
    from arbbot.storage.db import Database

    f = tmp_path / "obs.jsonl"
    db1 = Database(str(tmp_path / "s1.sqlite"))
    for i in range(5):
        db1.add_observation(1000.0 + i, "ghost", f"r{i}", i % 2, 0.1 * i, 0.2, {"margin_bps": 10 + i, "hops": 2})
    rt = Runtime.__new__(Runtime)
    rt.db, rt.chain = db1, BASE
    rt.settings = Settings(observations_file=str(f))
    assert rt.export_observations() == 5
    assert rt.export_observations() == 0            # idempotent: nothing new
    db1.add_observation(2000.0, "ghost", "r9", 1, 0.3, 0.2, {"margin_bps": 12, "hops": 3})
    assert rt.export_observations() == 1
    assert len(f.read_text().splitlines()) == 6
    # next session: fresh DB imports the history exactly once
    db2 = Database(str(tmp_path / "s2.sqlite"))
    rt2 = Runtime.__new__(Runtime)
    rt2.db, rt2.chain, rt2.settings = db2, BASE, rt.settings
    assert db2.import_observations(rt2._read_observations_file()) == 6
    assert db2.import_observations(rt2._read_observations_file()) == 0
    rows = db2.observations()
    assert len(rows) == 6 and rows[-1]["route_key"] == "r9" and rows[-1]["features"]["hops"] == 3
    assert len(db2.observations(since=1003.0)) == 3
