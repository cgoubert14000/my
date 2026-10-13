"""Live executor: pre-submission re-check → build EIP-1559 tx → remote signer → broadcast → receipt accounting.

The executor never holds a key. Every submission goes through `SignerClient` (HTTP, shared secret). Before asking
for a signature it re-validates *everything* on fresh state (the "pre-flight"): prices/liquidity re-fetched for
the route's pools, route re-quoted, simulation at latest block with the on-chain minProfit guard, gas re-estimated,
fee model re-run, policy caps and remaining budget re-checked, reliability threshold re-checked.
"""
from __future__ import annotations

import logging
import time
from dataclasses import dataclass, field

import aiohttp
from eth_abi import decode as abi_decode
from eth_utils import keccak

from ..config.policy import AuthorizationPolicy
from ..core.pricing import QuoteError, quote_route
from ..core.types import Decision, Opportunity
from ..data.collector import StateCollector
from ..data.rpc import RpcClient, RpcError
from ..engine.fees import FeeCalculator
from ..engine.selector import SelectionContext, Selector
from ..risk.manager import RiskManager
from ..simulation.simulator import Simulator, encode_execute

log = logging.getLogger("arbbot.exec")
ARB_EVENT_TOPIC = "0x" + keccak(text="ArbitrageExecuted(address,address,uint8,uint256,uint256,uint256)").hex()


@dataclass
class PreflightResult:
    ok: bool
    reasons: list[str] = field(default_factory=list)
    gas_limit: int = 0
    max_fee_per_gas: int = 0
    max_priority_fee: int = 0
    min_profit: int = 0
    hop_min_outs: list[int] = field(default_factory=list)
    sim_profit: int | None = None
    expected_net_token: int = 0
    checks: dict = field(default_factory=dict)


@dataclass
class ExecutionResult:
    status: str  # "success" | "reverted" | "dropped" | "rejected" | "signer_refused" | "error"
    tx_hash: str | None = None
    gas_used: int | None = None
    effective_gas_price: int | None = None
    gas_cost_wei: int = 0
    realized_profit_token: int | None = None
    realized_net_token: int | None = None
    error: str | None = None
    block_number: int | None = None
    preflight: PreflightResult | None = None


class SignerClient:
    def __init__(self, url: str, token: str):
        self.url = url.rstrip("/")
        self.token = token

    async def health(self) -> dict | None:
        try:
            async with aiohttp.ClientSession() as s:
                async with s.get(f"{self.url}/health", headers={"X-Signer-Token": self.token}, timeout=aiohttp.ClientTimeout(total=3)) as r:
                    if r.status != 200:
                        return None
                    return await r.json()
        except Exception:  # noqa: BLE001
            return None

    async def sign(self, payload: dict) -> tuple[dict | None, str | None]:
        try:
            async with aiohttp.ClientSession() as s:
                async with s.post(f"{self.url}/sign", json=payload, headers={"X-Signer-Token": self.token},
                                  timeout=aiohttp.ClientTimeout(total=5)) as r:
                    body = await r.json()
                    if r.status != 200:
                        return None, str(body.get("detail", body))
                    return body, None
        except Exception as e:  # noqa: BLE001
            return None, f"signer unreachable: {e}"


class LiveExecutor:
    def __init__(self, rpc: RpcClient, collector: StateCollector, fees: FeeCalculator, selector: Selector,
                 simulator: Simulator, risk: RiskManager, policy: AuthorizationPolicy, signer: SignerClient | None,
                 wallet: str, dry_run: bool = True):
        self.rpc = rpc
        self.collector = collector
        self.fees = fees
        self.selector = selector
        self.sim = simulator
        self.risk = risk
        self.policy = policy
        self.signer = signer
        self.wallet = wallet
        self.dry_run = dry_run

    # ------------------------------------------------------------------ pre-flight

    async def preflight(self, opp: Opportunity, ctx: SelectionContext) -> PreflightResult:
        res = PreflightResult(ok=False)
        t = ctx.tunables
        # 1) fresh state for the route's pools
        try:
            await self.collector.refresh_pools([h.pool for h in opp.route.hops])
        except RpcError as e:
            res.reasons.append(f"refresh_failed:{e}")
            return res
        age = self.collector.data_age_ms([h.pool for h in opp.route.hops])
        res.checks["data_age_ms"] = age
        if age > t.max_data_age_ms:
            res.reasons.append(f"stale_after_refresh({age:.0f}ms)")
        # 2) re-quote on fresh state
        try:
            q = quote_route(opp.route, opp.profit.amount_in)
        except QuoteError as e:
            res.reasons.append(f"requote_failed:{e}")
            return res
        gross = q.amount_out - opp.profit.amount_in
        fb = await self.fees.breakdown(opp.route, opp.flash_source, opp.profit.amount_in, q.ticks_crossed, q.swap_fees_in_start_token)
        expected_net = gross - fb.flash_fee - fb.gas_cost_token
        res.expected_net_token = expected_net
        res.checks.update({"gross_fresh": gross, "expected_net_fresh": expected_net, "gross_at_detection": opp.profit.gross_profit,
                           "gas_cost_token": fb.gas_cost_token, "flash_fee": fb.flash_fee, "unknowns": fb.unknowns})
        if expected_net <= 0:
            res.reasons.append("expected_net_nonpositive_on_fresh_state")
        if fb.unknowns:
            res.reasons.append("unknown_costs:" + "|".join(fb.unknowns))
        opp.profit.fees = fb
        opp.profit.gross_profit = gross
        opp.profit.amount_out = q.amount_out
        opp.profit.expected_net = expected_net
        opp.profit.margin_bps = expected_net / opp.profit.amount_in * 10_000
        # 3) on-chain guards. (a) minProfit = gas + safety margin: the contract reverts instead of ever closing at a
        #    loss (profit is measured after flash-loan repayment). (b) per-hop minAmountOut = quoted output × (1 − policy
        #    max_slippage_bps): an intermediate pool moved/manipulated beyond the tolerance reverts with HopOutputTooLow.
        safety = int(opp.profit.amount_in * t.safety_margin_bps) // 10_000
        min_profit = max(fb.gas_cost_token + safety, 1)
        res.min_profit = min_profit
        res.hop_min_outs = [int(a * (10_000 - self.policy.max_slippage_bps)) // 10_000 for a in q.hop_amounts[1:]]  # hop_amounts[0] = amount_in
        res.checks["min_profit_onchain"] = min_profit
        res.checks["hop_min_outs"] = res.hop_min_outs
        if gross - fb.flash_fee < min_profit:
            res.reasons.append(f"profit_below_onchain_floor({gross - fb.flash_fee}<{min_profit})")
        # 4) simulation on latest state with the real guards + gas estimate
        sim = await self.sim.simulate(opp, min_profit=min_profit, with_gas=True, hop_min_outs=res.hop_min_outs)
        opp.sim = sim.__dict__
        res.sim_profit = sim.profit
        res.checks["sim"] = {"ok": sim.ok, "profit": sim.profit, "error": sim.error, "gas_estimate": sim.gas_estimate, "mode": sim.mode}
        if not sim.ok:
            res.reasons.append(f"simulation_failed:{sim.error}")
        else:
            tol = int(opp.profit.amount_in * t.sim_tolerance_bps) // 10_000
            if sim.profit + tol < gross - fb.flash_fee:
                res.reasons.append(f"sim_below_estimate({sim.profit}<{gross - fb.flash_fee})")
            if sim.gas_estimate:
                self.fees.record_gas(opp.route, opp.flash_source, sim.gas_estimate)
        gas_units = int((sim.gas_estimate or fb.gas_units) * t.gas_safety_multiplier)
        if sim.gas_estimate and sim.gas_estimate > fb.gas_units:
            # the node's estimate beats the model: re-price gas with it (the miss is recorded for self-correction)
            res.checks["gas_model_underestimate"] = {"model": fb.gas_units, "estimate": sim.gas_estimate}
            fb.gas_units = gas_units
            fb.gas_cost_wei = fb.gas_units * fb.gas_price_wei + fb.l1_data_fee_wei
            fb.failure_cost_wei = int(fb.gas_cost_wei * t.failure_gas_fraction)
            fb.gas_cost_token, fb.native_price_in_token, _ = self.fees.native_to_token(fb.gas_cost_wei, opp.route.token)
            expected_net = gross - fb.flash_fee - fb.gas_cost_token
            res.expected_net_token = expected_net
            opp.profit.expected_net = expected_net
            opp.profit.margin_bps = expected_net / opp.profit.amount_in * 10_000
            res.min_profit = max(fb.gas_cost_token + safety, 1)
            if expected_net <= 0:
                res.reasons.append("expected_net_nonpositive_with_estimated_gas")
        # 5) fee caps, budget, policy
        g = self.collector.gas
        max_fee = min(int(self.policy.max_fee_per_gas_gwei * 1e9), 2 * g.base_fee_wei + max(g.priority_fee_wei, int(t.priority_fee_floor_gwei * 1e9)))
        prio = min(max(g.priority_fee_wei, int(t.priority_fee_floor_gwei * 1e9)), max_fee)
        res.gas_limit, res.max_fee_per_gas, res.max_priority_fee = gas_units, max_fee, prio
        if max_fee < g.base_fee_wei:
            res.reasons.append("policy_fee_cap_below_base_fee")
        ok, why = self.risk.can_afford(gas_units, max_fee)
        res.checks["budget"] = why
        if not ok:
            res.reasons.append(f"budget:{why}")
        # 6) selector gates again (policy allowlists, net ≥ policy min, impact, freshness) + reliability
        opp.reasons = []
        self.selector.evaluate([opp], ctx, self.policy.min_success_probability)
        if opp.decision != Decision.ELIGIBLE:
            res.reasons.extend(opp.reasons)
        # 7) wallet balance covers worst case
        try:
            bal = await self.rpc.get_balance(self.wallet)
            res.checks["wallet_balance_native"] = bal / 1e18
            if bal < gas_units * max_fee:
                res.reasons.append("wallet_balance_below_worst_case_gas")
        except RpcError as e:
            res.reasons.append(f"balance_check_failed:{e}")
        res.ok = not res.reasons
        return res

    # ------------------------------------------------------------------ execution

    async def execute(self, opp: Opportunity, ctx: SelectionContext) -> ExecutionResult:
        pf = await self.preflight(opp, ctx)
        if not pf.ok:
            return ExecutionResult("rejected", error="; ".join(pf.reasons), preflight=pf)
        if self.dry_run or self.signer is None:
            return ExecutionResult("rejected", error="dry-run: no signer configured", preflight=pf)
        deadline = int(time.time()) + 120
        data = encode_execute(opp, pf.min_profit, deadline, pf.hop_min_outs)
        try:
            nonce = await self.rpc.get_nonce(self.wallet)
        except RpcError as e:
            return ExecutionResult("error", error=f"nonce: {e}", preflight=pf)
        payload = {
            "chain_id": self.collector.chain.chain_id, "to": self.sim.executor, "data": "0x" + data.hex(), "nonce": nonce,
            "gas": pf.gas_limit, "max_fee_per_gas": pf.max_fee_per_gas, "max_priority_fee_per_gas": pf.max_priority_fee, "value": 0,
            "context": {"opportunity": opp.id, "route": opp.route.describe(), "expected_net": pf.expected_net_token,
                        "block": opp.block_number},
        }
        worst = pf.gas_limit * pf.max_fee_per_gas
        self.risk.reserve(worst)
        try:
            signed, err = await self.signer.sign(payload)
            if signed is None:
                return ExecutionResult("signer_refused", error=err, preflight=pf)
            try:
                tx_hash = await self.rpc.send_raw(signed["raw_tx"])
            except RpcError as e:
                return ExecutionResult("error", error=f"broadcast: {e}", preflight=pf)
            opp.tx_hash = tx_hash
            opp.decision = Decision.EXECUTED
            receipt = await self.rpc.wait_receipt(tx_hash, timeout=90)
            if receipt is None:
                return ExecutionResult("dropped", tx_hash=tx_hash, error="no receipt within 90 s", preflight=pf)
            gas_used = int(receipt["gasUsed"], 16)
            egp = int(receipt.get("effectiveGasPrice", "0x0"), 16)
            l1 = int(receipt.get("l1Fee", "0x0"), 16) if receipt.get("l1Fee") else 0
            gas_cost = gas_used * egp + l1
            status = int(receipt["status"], 16)
            self.fees.record_gas(opp.route, opp.flash_source, gas_used)
            res = ExecutionResult("success" if status == 1 else "reverted", tx_hash=tx_hash, gas_used=gas_used,
                                  effective_gas_price=egp, gas_cost_wei=gas_cost, block_number=int(receipt["blockNumber"], 16), preflight=pf)
            if status == 1:
                profit = _profit_from_logs(receipt, self.sim.executor)
                res.realized_profit_token = profit
                gas_token = int(gas_cost / 1e18 * opp.profit.fees.native_price_in_token * 10**opp.route.token.decimals) if opp.profit.fees.native_price_in_token else 0
                res.realized_net_token = (profit or 0) - gas_token
                opp.profit.realized_net = res.realized_net_token
            else:
                opp.decision = Decision.FAILED
                opp.profit.realized_net = -int(gas_cost / 1e18 * opp.profit.fees.native_price_in_token * 10**opp.route.token.decimals) if opp.profit.fees.native_price_in_token else None
                res.realized_net_token = opp.profit.realized_net
                res.error = await self._revert_reason(tx_hash, receipt)
            net_native = (res.realized_net_token or 0) / 10**opp.route.token.decimals / (opp.profit.fees.native_price_in_token or 1)
            self.risk.record_execution(success=status == 1, gas_cost_wei=gas_cost, realized_net_native=net_native)
            return res
        finally:
            self.risk.release(worst)


    async def _revert_reason(self, tx_hash: str, receipt: dict) -> str:
        """Best-effort post-mortem of a reverted tx: debug_traceTransaction (anvil/geth) → decoded custom error."""
        try:
            trace = await self.rpc.request("debug_traceTransaction", [tx_hash, {"tracer": "callTracer"}], retries=0)
            out = trace.get("output") if isinstance(trace, dict) else None
            from ..simulation.simulator import decode_revert

            if out and out != "0x":
                return "reverted: " + decode_revert(out)
            if isinstance(trace, dict) and trace.get("error"):
                return f"reverted: {trace['error']}"
        except RpcError:
            pass
        gas_used = int(receipt.get("gasUsed", "0x0"), 16)
        return "reverted (reason unavailable; gasUsed=%d)" % gas_used


def _profit_from_logs(receipt: dict, executor: str) -> int | None:
    for lg in receipt.get("logs", []):
        if lg.get("address", "").lower() == executor.lower() and lg.get("topics") and lg["topics"][0].lower() == ARB_EVENT_TOPIC:
            data = bytes.fromhex(lg["data"][2:])
            _source, _amount, profit, _hops = abi_decode(["uint8", "uint256", "uint256", "uint256"], data)
            return int(profit)
    return None
