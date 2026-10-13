"""OP-stack (Base) L1 data fee path, exercised with a stub RPC since no public RPC is reachable from the sandbox:
  * Fjord `getL1FeeUpperBound(uint256)` answer is used as-is;
  * pre-Fjord fallback to `getL1Fee(bytes)`;
  * oracle failure → fee 0 **and** an explicit unknown (candidates are then rejected by the selector);
  * one oracle read per (calldata size, block) — a rate-limited RPC must not be hammered per candidate."""
from __future__ import annotations

from dataclasses import dataclass, field

import pytest

from arbbot.config.chains import get_chain
from arbbot.config.tunables import TunableParams
from arbbot.data.rpc import RpcError, encode_call
from arbbot.engine.fees import FeeCalculator


@dataclass
class _Stats:
    last_block: int = 100


@dataclass
class _Collector:
    stats: _Stats = field(default_factory=_Stats)
    native_price_usd: float | None = 2000.0


class _StubRpc:
    def __init__(self, upper_bound: int | None, legacy: int | None):
        self.upper_bound, self.legacy, self.calls = upper_bound, legacy, []

    async def call(self, to, data: bytes, block="latest", **kw):
        self.calls.append((to, data[:4]))
        sel_upper = encode_call("getL1FeeUpperBound(uint256)", [0])[:4]
        sel_legacy = encode_call("getL1Fee(bytes)", [b""])[:4]
        if data[:4] == sel_upper:
            if self.upper_bound is None:
                raise RpcError("execution reverted", -32000)
            return self.upper_bound.to_bytes(32, "big")
        if data[:4] == sel_legacy:
            if self.legacy is None:
                raise RpcError("execution reverted", -32000)
            return self.legacy.to_bytes(32, "big")
        raise AssertionError(data)


def _calc(rpc, chain_name="base"):
    chain = get_chain(chain_name)
    return FeeCalculator(rpc, chain, _Collector(), TunableParams())


async def test_fjord_upper_bound_used_and_cached_per_block():
    rpc = _StubRpc(upper_bound=123_456_789, legacy=None)
    fc = _calc(rpc)
    fee, unk = await fc.l1_data_fee(500)
    assert (fee, unk) == (123_456_789, None)
    assert rpc.calls[0][0] == get_chain("base").opstack_gas_oracle == "0x420000000000000000000000000000000000000F"
    for _ in range(50):  # same block, same size → no new RPC traffic
        await fc.l1_data_fee(500)
    assert len(rpc.calls) == 1
    fc.collector.stats.last_block += 1  # new block → refreshed once
    await fc.l1_data_fee(500)
    assert len(rpc.calls) == 2


async def test_pre_fjord_fallback_to_getl1fee_bytes():
    rpc = _StubRpc(upper_bound=None, legacy=42_000_000)
    fee, unk = await _calc(rpc).l1_data_fee(300)
    assert (fee, unk) == (42_000_000, None)
    assert [c[1] for c in rpc.calls] == [encode_call("getL1FeeUpperBound(uint256)", [0])[:4], encode_call("getL1Fee(bytes)", [b""])[:4]]


async def test_oracle_failure_is_an_unknown_cost_not_zero():
    rpc = _StubRpc(upper_bound=None, legacy=None)
    fee, unk = await _calc(rpc).l1_data_fee(300)
    assert fee == 0 and unk and "l1 fee oracle unavailable" in unk


async def test_arbitrum_has_no_separate_l1_component():
    rpc = _StubRpc(upper_bound=1, legacy=1)
    fee, unk = await _calc(rpc, "arbitrum").l1_data_fee(300)
    assert (fee, unk) == (0, None) and rpc.calls == []  # L1 share is inside eth_estimateGas on Arbitrum


@pytest.mark.parametrize("name", ["base", "arbitrum"])
def test_mainnet_chain_configs_declare_l1_model(name):
    c = get_chain(name)
    assert c.l1_fee_model in ("opstack", "arbitrum")
    if c.l1_fee_model == "opstack":
        assert c.opstack_gas_oracle.lower() == "0x420000000000000000000000000000000000000f"
