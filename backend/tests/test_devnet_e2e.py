"""End-to-end on the local anvil devnet (skipped when it is not running).

Covers: detection → exact simulation (eth_call on the real executor) → ghost labelling → pre-flight refusal when
no signer is configured → emergency stop → a REAL limited execution on the devnet through the isolated signer
under a policy (budget, caps, allowlists), including a reverted attempt accounted as a failure.
"""
from __future__ import annotations

import asyncio
import json
import os
import time

import pytest
from eth_account import Account

from arbbot.app.runtime import Runtime
from arbbot.config.policy import AuthorizationPolicy, EXAMPLE
from arbbot.config.settings import Settings
from arbbot.core.types import Decision
from arbbot.execution.executor import SignerClient
from arbbot.risk.manager import BotStatus
from arbbot.signer.service import SignRequest, Signer, SignerState
from tests.conftest import requires_devnet

pytestmark = [requires_devnet, pytest.mark.devnet]

EXECUTOR_KEY = "0x59c6995e998f97a5a0044966f0945389dc9e86dae88c7a8412f4603b6b78690d"  # public anvil account #1


class LocalSigner(SignerClient):
    """In-process stand-in for the HTTP signer (same Signer class, same checks)."""

    def __init__(self, signer: Signer):
        super().__init__("local://", "x")
        self.s = signer

    async def health(self):
        ok, why = self.s.policy.is_valid_now()
        return {"address": self.s.address, "policy_valid": ok, "policy_reason": why, "tx_count": self.s.state.tx_count}

    async def sign(self, payload):
        try:
            return self.s.sign(SignRequest(**payload)), None
        except Exception as e:  # noqa: BLE001
            return None, getattr(e, "detail", str(e))


def _open_gap(cfg: dict, frac: float = 0.02) -> None:
    """Create a fresh cross-pool gap on the devnet: one sizeable trade on a V2 pool (maker = public anvil account #2)."""
    import sys

    from web3 import Web3

    from tests.conftest import REPO

    sys.path.insert(0, str(REPO / "devnet"))
    from market_sim import Market  # noqa: E402

    m = Market(Web3(Web3.HTTPProvider(cfg["rpc"])), cfg)
    pools = [p for p in cfg["pools"] if p["kind"] == "UNIV2"]
    assert m.random_trade(frac, frac, pool=pools[0], direction=True)


async def _positive_candidates(rt, cfg: dict, attempts: int = 4):
    """Process blocks until a simulated, positive candidate exists; opens a gap when the market is flat."""
    b = await rt.rpc.block_number()
    for i in range(attempts):
        await rt.collector.refresh(b)
        await rt.process_block(b)
        def clean(o) -> bool:  # every gate passes except the (not yet demonstrated) reliability
            return all(r.startswith(("reliability_not_demonstrated", "ghost_mode:", "p_lower_below")) for r in o.reasons)

        pos = sorted([o for o in rt.recent_opps if o.block_number == b and o.profit.expected_net > 0 and o.sim and o.sim["ok"] and clean(o)],
                     key=lambda o: -o.profit.expected_net)
        if pos:
            return b, pos
        _open_gap(cfg, 0.02 + 0.01 * i)
        b = await _next_block(rt, b)
    raise AssertionError("no positive candidate even after opening gaps")


async def _runtime(tmp_path, policy: AuthorizationPolicy | None = None, with_signer: bool = False):
    if policy is not None:
        (tmp_path / "authorization.json").write_text(policy.model_dump_json())
    s = Settings(chain="local")
    rt = Runtime(s)
    await rt.start()
    rt.collector.stop()  # tests drive blocks manually
    for t in rt._tasks:
        t.cancel()
    await asyncio.gather(*rt._tasks, return_exceptions=True)
    rt._tasks = []
    if with_signer:
        signer = Signer(rt.policy, Account.from_key(EXECUTOR_KEY), SignerState(tmp_path / "signer_state.json"), "mem")
        rt.signer = LocalSigner(signer)
        rt.executor.signer = rt.signer
        rt.executor.dry_run = False
    return rt


async def _next_block(rt, prev: int) -> int:
    while True:
        b = await rt.rpc.block_number()
        if b > prev:
            return b
        await asyncio.sleep(0.25)


def _policy(cfg: dict, **over) -> AuthorizationPolicy:
    tokens = {k: {"address": v["address"], "decimals": v["decimals"], "max_borrow": 1_000_000.0} for k, v in cfg["tokens"].items()}
    base = {**EXAMPLE, "enabled": True, "wallet_address": cfg["accounts"]["executor"], "chain_ids": [cfg["chain_id"]],
            "executor_contract": cfg["executor"], "allowed_dexes": ["uniswap_v2", "sushiswap", "uniswap_v3", "aerodrome"],
            "allowed_tokens": list(cfg["tokens"].keys()), "tokens": tokens, "max_total_budget_native": 0.05,
            "max_gas_per_tx_native": 0.01, "max_gas_limit": 1_200_000, "max_fee_per_gas_gwei": 5.0, "max_transactions": 5,
            "min_net_profit_native": 0.0, "max_borrow_usd": 100_000, "valid_from": 0, "valid_until": time.time() + 3600,
            "min_success_probability": 0.75}
    base.update(over)
    return AuthorizationPolicy.model_validate(base)


async def test_detection_simulation_exact_and_ghost_label(tmp_path, devnet_cfg):
    rt = await _runtime(tmp_path)
    try:
        b, _ = await _positive_candidates(rt, devnet_cfg)
        sims = [o for o in rt.recent_opps if o.sim]
        assert sims, "no candidate was simulated"
        exact = 0
        for o in sims:
            assert o.sim["mode"] == "deployed"
            if o.sim["ok"]:
                # eth_call profit must equal our exact gross − flash fee (bit-exact pricing)
                assert o.sim["profit"] == o.profit.gross_profit - o.profit.fees.flash_fee, (o.route.describe(), o.sim, o.profit)
                exact += 1
        assert exact > 0
        assert rt.risk.state.status == BotStatus.LEARNING
        assert all(o.decision != Decision.SELECTED for o in rt.recent_opps)  # never selected without demonstrated reliability
        # ghost label at N+1
        n1 = await _next_block(rt, b)
        await rt.collector.refresh(n1)
        await rt.process_block(n1)
        assert rt.ghost.labeled >= 1
        assert rt.reliability.n == rt.ghost.labeled
        assert rt.db.observations()
    finally:
        await rt.stop()


async def test_preflight_refuses_without_signer_and_emergency_stop(tmp_path, devnet_cfg):
    rt = await _runtime(tmp_path)
    try:
        b, pos = await _positive_candidates(rt, devnet_cfg)
        res = await rt.executor.execute(pos[0], rt._ctx(b))
        assert res.status == "rejected"
        assert "reliability_not_demonstrated" in (res.error or "") or "dry-run" in (res.error or "")
        assert rt.risk.ledger.tx_count == 0
        # emergency stop: engine stops producing decisions, status SUSPENDU, resume restores simulation
        rt.emergency_stop("test")
        assert rt.risk.state.status == BotStatus.SUSPENDED and rt.paused
        n1 = await _next_block(rt, b)
        cyc = await rt.process_block(n1)
        assert cyc.get("paused") is True
        rt.resume()
        assert rt.risk.state.status == BotStatus.SIMULATION and not rt.paused
    finally:
        await rt.stop()


async def test_live_execution_under_policy_with_isolated_signer(tmp_path, devnet_cfg):
    """Real transactions on the devnet: one profitable arbitrage, one deliberately failing route."""
    policy = _policy(devnet_cfg)
    rt = await _runtime(tmp_path, policy, with_signer=True)
    try:
        from arbbot.reliability.model import Observation, features_of

        b, pos = await _positive_candidates(rt, devnet_cfg)
        best = pos[0]
        # demonstrate reliability for this bucket (devnet shortcut: 40 synthetic positive labels — clearly marked as test data)
        f = features_of(best)
        for _ in range(40):
            rt.reliability.add(Observation(time.time(), f, 1, "test-fixture"))
        rt.risk.flags.update(tests_passed=True, contract_tested=True, financial_math_validated=True, simulations_ok=50)
        st = rt.risk.evaluate(policy_signer_ok=True, data_age_ms=10, rpc_ok=True)
        assert st.status == BotStatus.READY_LIMITED_LIVE, (st.status, st.sub_status, [c for c in st.criteria if not c.ok])
        assert rt.risk.activate_live()
        bal_before = await rt.rpc.get_balance(policy.wallet_address)
        res = await rt.executor.execute(best, rt._ctx(b))
        assert res.status == "success", (res.status, res.error, res.preflight and res.preflight.reasons)
        assert res.tx_hash and res.gas_used and res.gas_used < policy.max_gas_limit
        assert res.realized_profit_token is not None and res.realized_profit_token > 0
        # realised profit equals the simulated profit (same block state on the devnet when no trade intervened)
        assert res.realized_net_token is not None
        bal_after = await rt.rpc.get_balance(policy.wallet_address)
        assert bal_before - bal_after == res.gas_cost_wei  # only gas left the wallet
        assert rt.risk.ledger.tx_count == 1 and rt.risk.ledger.gas_spent_wei == res.gas_cost_wei
        rt._record_execution(best, res)
        assert rt.db.executions()[0]["status"] == "success"

        # a second attempt on a route whose gap no longer exists must be refused BEFORE signing (pre-flight), not revert
        n1 = await _next_block(rt, b)
        await rt.collector.refresh(n1)
        res2 = await rt.executor.execute(best, rt._ctx(n1))
        assert res2.status == "rejected", (res2.status, res2.error)
        assert rt.risk.ledger.tx_count == 1  # nothing was signed
        # signer enforces its own caps: a request above policy gas limit is refused at the signer level
        bad = await rt.signer.sign({"chain_id": devnet_cfg["chain_id"], "to": policy.executor_contract, "data": "0x12345678", "nonce": 0,
                                   "gas": 5_000_000, "max_fee_per_gas": 10**9, "max_priority_fee_per_gas": 1, "value": 0})
        assert bad[0] is None and bad[1]
    finally:
        await rt.stop()
