"""The mainnet code path (pool discovery from DEX factories + on-chain metadata) exercised against the REAL Uniswap V2
and V3 factory bytecode deployed on the devnet. On Base/Arbitrum the very same code runs with the factories of
config/chains.py — this test is the proof that the path works before an RPC is available."""
from __future__ import annotations

import dataclasses

import pytest

from arbbot.config.chains import DexConfig, get_chain
from arbbot.core.types import DexKind
from arbbot.data.indexer import PoolIndexer
from arbbot.data.rpc import RpcClient
from tests.conftest import REPO, requires_devnet

pytestmark = [requires_devnet, pytest.mark.devnet]


async def test_factory_discovery_matches_deployed_pools(devnet_cfg):
    local = get_chain("local", REPO / "devnet" / "deployments.local.json")
    v2 = devnet_cfg["v2_factories"]
    dexes = [
        DexConfig("uniswap_v2", DexKind.UNIV2, v2["uniswap_v2"], fee_ppm=3000),
        DexConfig("sushiswap", DexKind.UNIV2, v2["sushiswap"], fee_ppm=3000),
        DexConfig("uniswap_v3", DexKind.UNIV3, devnet_cfg["v3_factory"], fee_tiers=(100, 500, 3000, 10000)),
    ]
    chain = dataclasses.replace(local, dexes=dexes, static_pools=[])  # force the factory path
    rpc = RpcClient(devnet_cfg["rpc"], timeout_s=10, max_rps=100)
    await rpc.open()
    try:
        pools = await PoolIndexer(rpc, chain).discover()
    finally:
        await rpc.close()
    expected = {p["address"].lower(): p for p in devnet_cfg["pools"] if p["kind"] in ("UNIV2", "UNIV3")}
    found = {p.address.lower(): p for p in pools}
    assert set(found) == set(expected), (sorted(set(expected) - set(found)), sorted(set(found) - set(expected)))
    for addr, p in found.items():
        e = expected[addr]
        assert p.kind.name == e["kind"] and p.dex == e["dex"]
        assert p.token0.address.lower() == e["token0"].lower() and p.token1.address.lower() == e["token1"].lower()
        assert p.fee_ppm == e["fee_ppm"]  # V3: fee() read on-chain; V2: configured fee
        if p.kind == DexKind.UNIV3:
            assert p.tick_spacing == {100: 1, 500: 10, 3000: 60, 10000: 200}[p.fee_ppm]
        assert not p.quarantined
