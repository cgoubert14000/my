"""Full-transaction simulation of `FlashArbExecutor.executeArbitrage` through eth_call.

Two modes:
  * deployed executor      – plain eth_call from the executor EOA against the real contract.
  * state-override mode    – the executor bytecode is injected at a scratch address with owner/executor/allowlist
                             storage slots overridden (geth/erigon/reth/anvil & major providers support the
                             3rd eth_call parameter). Lets the engine validate routes on mainnet BEFORE deploying.
The simulation runs the real flash loan + real swaps on the node's state, so its result includes every on-chain
effect (fees, rounding, callbacks, reverts). It does NOT include gas/L1 costs (added by the fee model) nor the
state change between now and inclusion (measured by ghost mode's next-block re-simulation).
"""
from __future__ import annotations

import json
import logging
import pathlib
import time
from dataclasses import dataclass

from eth_abi import decode as abi_decode, encode as abi_encode
from eth_utils import keccak, to_checksum_address

from ..core.types import FlashSource, Opportunity
from ..data.rpc import RevertError, RpcClient, RpcError, encode_call, selector

log = logging.getLogger("arbbot.sim")

ARB_PARAMS_T = "(uint8,address,address,uint256,uint256,uint256,(uint8,address,address,address,uint32,uint256)[])"
EXECUTE_SIG = f"executeArbitrage({ARB_PARAMS_T})"
SCRATCH_EXECUTOR = "0x00000000000000000000000000000000000A4bB0"

ERRORS = {
    "NotExecutor()": [], "NotGuardian()": [], "Expired()": [], "BadHopCount()": [], "TokenNotAllowed(address)": ["address"],
    "PoolNotAllowed(address)": ["address"], "ProviderNotAllowed(address)": ["address"], "RouteNotCyclic()": [],
    "RouteDiscontinuous(uint256)": ["uint256"], "BorrowCapExceeded()": [], "InsufficientProfit(uint256,uint256)": ["uint256", "uint256"],
    "InsufficientSelfFunds()": [], "UnauthorizedCallback()": [], "BadCallbackPayload()": [],
    "HopOutputTooLow(uint256,uint256,uint256)": ["uint256", "uint256", "uint256"], "ZeroAmount()": [], "BadFee()": [],
    "FlashRepaymentImpossible()": [], "EnforcedPause()": [], "ReentrancyGuardReentrantCall()": [],
    "Error(string)": ["string"], "Panic(uint256)": ["uint256"],
}
_ERR_BY_SEL = {selector(sig): (sig, types) for sig, types in ERRORS.items()}


def decode_revert(data) -> str:
    if not data:
        return "revert (no data)"
    if isinstance(data, str):
        try:
            data = bytes.fromhex(data[2:] if data.startswith("0x") else data)
        except ValueError:
            return f"revert: {data[:80]}"
    if len(data) < 4:
        return "revert (no data)"
    sig, types = _ERR_BY_SEL.get(bytes(data[:4]), (None, None))
    if not sig:
        return f"revert 0x{bytes(data[:4]).hex()}"
    try:
        args = abi_decode(types, bytes(data[4:])) if types else ()
    except Exception:  # noqa: BLE001
        return sig
    return f"{sig.split('(')[0]}{tuple(args)}" if args else sig.split("(")[0]


@dataclass
class SimResult:
    ok: bool
    profit: int | None
    error: str | None
    gas_estimate: int | None
    latency_ms: float
    mode: str
    block: int | str


def encode_execute(opp: Opportunity, min_profit: int, deadline: int, hop_min_outs: list[int] | None = None) -> bytes:
    hops = [h.to_contract_tuple(hop_min_outs[i] if hop_min_outs else 0) for i, h in enumerate(opp.route.hops)]
    params = (
        int(opp.flash_source), to_checksum_address(opp.flash_provider) if opp.flash_provider else "0x" + "00" * 20,
        to_checksum_address(opp.route.token.address), int(opp.profit.amount_in), int(min_profit), int(deadline), hops,
    )
    return selector(EXECUTE_SIG) + abi_encode([ARB_PARAMS_T], [params])


def _mapping_slot(key_address: str, slot: int) -> str:
    key = bytes.fromhex(key_address[2:].rjust(64, "0"))
    return "0x" + keccak(key + slot.to_bytes(32, "big")).hex()


class Simulator:
    def __init__(self, rpc: RpcClient, executor_address: str, sender: str, artifact_path: pathlib.Path | None = None,
                 use_state_override: bool = True):
        self.rpc = rpc
        self.executor = to_checksum_address(executor_address) if executor_address else ""
        self.sender = to_checksum_address(sender)
        self.use_override = use_state_override
        self._artifact = json.loads(pathlib.Path(artifact_path).read_text()) if artifact_path and pathlib.Path(artifact_path).exists() else None
        self._layout = {s["label"]: int(s["slot"]) for s in (self._artifact or {}).get("storageLayout", {}).get("storage", [])}

    def overrides_for(self, opp: Opportunity) -> dict:
        """State override injecting the executor with the simulating sender as owner+executor and the route allowlisted."""
        if not self._artifact:
            raise RuntimeError("executor artifact missing: run `forge build` in contracts/")
        code = self._artifact["deployedBytecode"]["object"]
        one = "0x" + "1".rjust(64, "0")
        state = {"0x" + (0).to_bytes(32, "big").hex(): "0x" + self.sender[2:].lower().rjust(64, "0")}
        state[_mapping_slot(self.sender, self._layout["isExecutor"])] = one
        tokens = {opp.route.token.address} | {h.token_in.address for h in opp.route.hops} | {h.token_out.address for h in opp.route.hops}
        for t in tokens:
            state[_mapping_slot(t, self._layout["allowedTokens"])] = one
        for h in opp.route.hops:
            state[_mapping_slot(h.pool.address, self._layout["allowedPools"])] = one
        if opp.flash_provider:
            state[_mapping_slot(opp.flash_provider, self._layout["allowedProviders"])] = one
        return {SCRATCH_EXECUTOR: {"code": code, "stateDiff": state}}

    async def simulate(self, opp: Opportunity, *, min_profit: int = 0, block: int | str = "latest",
                       with_gas: bool = False, deadline: int | None = None, hop_min_outs: list[int] | None = None) -> SimResult:
        t0 = time.perf_counter()
        deadline = deadline or int(time.time()) + 300
        data = encode_execute(opp, min_profit, deadline, hop_min_outs)
        target, overrides, mode = self.executor, None, "deployed"
        if not target:
            if not self.use_override:
                return SimResult(False, None, "no executor deployed and state override disabled", None, 0.0, "none", block)
            target, overrides, mode = SCRATCH_EXECUTOR, self.overrides_for(opp), "state-override"
        try:
            raw = await self.rpc.call(target, data, block, sender=self.sender, overrides=overrides, gas=3_000_000)
            (profit,) = abi_decode(["uint256"], raw)
            gas = None
            if with_gas and mode == "deployed":
                try:
                    gas = await self.rpc.estimate_gas({"from": self.sender, "to": target, "data": "0x" + data.hex()})
                except RpcError as e:
                    log.debug("estimateGas failed: %s", e)
            return SimResult(True, int(profit), None, gas, (time.perf_counter() - t0) * 1000, mode, block)
        except RevertError as e:
            return SimResult(False, None, decode_revert(e.data), None, (time.perf_counter() - t0) * 1000, mode, block)
        except RpcError as e:
            return SimResult(False, None, f"rpc: {e}", None, (time.perf_counter() - t0) * 1000, mode, block)
