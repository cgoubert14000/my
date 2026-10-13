"""Universe discovery (mainnet path) against a scripted RPC: token lists + factory enumeration + pair discovery +
on-chain measurement + depth filter. No network: every selector is answered by the stub."""
from __future__ import annotations

import dataclasses
import json

import pytest
from eth_abi import encode as abi_encode

from arbbot.config.chains import BASE, DexConfig
from arbbot.core.types import DexKind, Token
from arbbot.data import indexer as ix
from arbbot.data.indexer import PoolIndexer
from arbbot.data.rpc import selector

WETH = BASE.tokens["WETH"]
USDC = BASE.tokens["USDC"]
TOK = "0x" + "77" * 20  # long-tail token from the bundled list (valid)
BAD = "0x" + "66" * 20  # bundled list says 18 decimals, chain says 6 → rejected
ENU = "0x" + "55" * 20  # token only known through factory enumeration
NOHUB = "0x" + "44" * 20
P_UNI = "0x" + "a1" * 20  # WETH/USDC uniswap_v3 500 (hub/hub, price source)
P_AERO_TOK = "0x" + "a2" * 20  # enumerated aerodrome pool WETH/TOK (deep)
P_AERO_ENU = "0x" + "a3" * 20  # enumerated aerodrome pool USDC/ENU (shallow → dropped)
P_AERO_NOHUB = "0x" + "a4" * 20  # enumerated pool NOHUB/TOK (no hub side → ignored)
P_PAIR_TOK = "0x" + "a5" * 20  # uniswap_v3 TOK/USDC 3000 from pair discovery (deep)
SQRT_2500 = int((2500 * 10**6 / 10**18) ** 0.5 * 2**96)  # WETH/USDC: 2500 USDC per WETH (token0 WETH, token1 USDC)


def sel(sig: str) -> bytes:
    return selector(sig)


class ScriptedRpc:
    def __init__(self) -> None:
        self.pools = {  # address → (token0, token1)
            P_UNI: (WETH.address, USDC.address), P_AERO_TOK: (WETH.address, TOK), P_AERO_ENU: (ENU, USDC.address),
            P_AERO_NOHUB: (NOHUB, TOK), P_PAIR_TOK: (TOK, USDC.address),
        }
        self.enumerated = [P_AERO_TOK, P_AERO_ENU, P_AERO_NOHUB]
        self.decimals = {TOK: 18, BAD: 6, ENU: 18, NOHUB: 18, WETH.address: 18, USDC.address: 6}
        self.balances = {  # (token, pool) → raw
            (WETH.address, P_UNI): 10_000 * 10**18, (USDC.address, P_UNI): 25_000_000 * 10**6,
            (WETH.address, P_AERO_TOK): 40 * 10**18, (TOK, P_AERO_TOK): 10**24,
            (ENU, P_AERO_ENU): 10**24, (USDC.address, P_AERO_ENU): 500 * 10**6,
            (TOK, P_PAIR_TOK): 10**24, (USDC.address, P_PAIR_TOK): 90_000 * 10**6,
        }

    async def call(self, to, data, block="latest"):
        if data[:4] == sel("allPoolsLength()"):
            return abi_encode(["uint256"], [len(self.enumerated)])
        raise AssertionError(f"unexpected call {data[:4].hex()} to {to}")

    async def multicall(self, calls, block="latest", chunk=300):
        out = []
        for to, data in calls:
            out.append(self._one(to.lower(), data))
        return out

    def _one(self, to, data):
        s = data[:4]
        lo = {k.lower(): v for k, v in self.pools.items()}
        if s == sel("allPools(uint256)"):
            i = int.from_bytes(data[4:36], "big")
            return True, abi_encode(["address"], [self.enumerated[i]])
        if s == sel("token0()") and to in lo:
            return True, abi_encode(["address"], [lo[to][0]])
        if s == sel("token1()") and to in lo:
            return True, abi_encode(["address"], [lo[to][1]])
        if s == sel("decimals()"):
            d = {k.lower(): v for k, v in self.decimals.items()}.get(to)
            return (True, abi_encode(["uint8"], [d])) if d is not None else (False, b"")
        if s == sel("symbol()"):
            return True, abi_encode(["string"], ["SYM"])
        if s == sel("getPool(address,address,uint24)"):
            a = "0x" + data[4 + 12 : 36].hex()
            b = "0x" + data[36 + 12 : 68].hex()
            fee = int.from_bytes(data[68:100], "big")
            pair = {a.lower(), b.lower()}
            if to == BASE.dexes[0].factory.lower():
                if pair == {WETH.address.lower(), USDC.address.lower()} and fee == 500:
                    return True, abi_encode(["address"], [P_UNI])
                if pair == {TOK.lower(), USDC.address.lower()} and fee == 3000:
                    return True, abi_encode(["address"], [P_PAIR_TOK])
            return True, abi_encode(["address"], [ix.ZERO])
        if s in (sel("getPool(address,address,int24)"), sel("getPool(address,address,bool)"), sel("getPair(address,address)")):
            return True, abi_encode(["address"], [ix.ZERO])
        if s == sel("fee()"):
            return True, abi_encode(["uint24"], [500 if to == P_UNI.lower() else 3000])
        if s == sel("tickSpacing()"):
            return True, abi_encode(["int24"], [10 if to == P_UNI.lower() else 60])
        if s == sel("getFee(address,bool)"):
            return True, abi_encode(["uint256"], [30])
        if s == sel("stable()"):
            return True, abi_encode(["bool"], [False])
        if s == sel("balanceOf(address)"):
            pool = "0x" + data[4 + 12 : 36].hex()
            v = {(t.lower(), p.lower()): x for (t, p), x in self.balances.items()}.get((to, pool.lower()), 0)
            return True, abi_encode(["uint256"], [v])
        if s == sel("slot0()"):
            return True, abi_encode(["uint160", "int24", "uint16", "uint16", "uint16", "uint8", "bool"], [SQRT_2500, 0, 0, 0, 0, 0, True])
        if s == sel("getReserves()"):
            return True, abi_encode(["uint112", "uint112", "uint32"], [1, 1, 0])
        return False, b""


@pytest.fixture
def chain(tmp_path, monkeypatch):
    tokens = {"WETH": WETH, "USDC": USDC}
    dexes = [
        dataclasses.replace(BASE.dexes[0]),  # uniswap_v3
        DexConfig("aerodrome", DexKind.SOLIDLY, "0x" + "f1" * 20, solidly_fee_from_factory=True, enumerable=True),
    ]
    c = dataclasses.replace(BASE, tokens=tokens, dexes=dexes, extra={})
    bundle = {"chain_id": 8453, "tokens": [
        {"address": TOK, "symbol": "TOK", "decimals": 18, "sources": ["test-list"]},
        {"address": BAD, "symbol": "BAD", "decimals": 18, "sources": ["test-list"]},
        {"address": USDC.address, "symbol": "USDC", "decimals": 6, "sources": ["test-list"]},  # already a hub → no duplicate
    ]}
    (tmp_path / "base.json").write_text(json.dumps(bundle))
    monkeypatch.setattr(ix, "TOKENLIST_DIR", tmp_path)
    return c


async def test_universe_discovery_tokens_pools_depth_and_sources(chain):
    idx = PoolIndexer(ScriptedRpc(), chain, min_pool_usd=10_000, max_pools=100)  # type: ignore[arg-type]
    pools = await idx.discover()
    by_addr = {p.address.lower(): p for p in pools}
    st = idx.stats
    # tokens: 2 hubs + TOK (list) + ENU (enumeration); BAD rejected (decimals mismatch); NOHUB never considered
    assert st["tokens_config"] == 2 and st["tokens_tokenlist"] == 2 and st["tokens_factory_enum"] == 1
    assert st["tokens_rejected"] == 1 and st["tokens_total"] == 4
    assert any("decimals mismatch" in n for n in st["notes"])
    # the fake-symbol collision rule: a long-tail token is registered under a distinct key, never by symbol alone
    assert chain.tokens["TOK"].address.lower() == TOK.lower()
    assert chain.extra["token_sources"][TOK.lower()].startswith("tokenlist: test-list")
    assert chain.extra["token_sources"][ENU.lower()].startswith("on-chain: aerodrome factory allPools")
    # pools: WETH/USDC (hub/hub, 50 M$), WETH/TOK aerodrome (40 WETH ≈ 200 k$ ×2), TOK/USDC (180 k$); USDC/ENU dropped (1 k$)
    assert set(by_addr) == {P_UNI.lower(), P_AERO_TOK.lower(), P_PAIR_TOK.lower()}
    assert st["pools_below_min_depth"] == 1 and st["pools_kept"] == 3 and st["pools_enumerated"] == 2
    assert st["hub_prices"]["WETH"] == pytest.approx(2500, rel=1e-3) and st["hub_prices"]["USDC"] == 1.0
    assert by_addr[P_UNI.lower()].depth_usd_hint == pytest.approx(10_000 * 2500 + 25_000_000, rel=1e-6)
    assert by_addr[P_AERO_TOK.lower()].depth_usd_hint == pytest.approx(2 * 40 * 2500, rel=1e-6)
    assert by_addr[P_PAIR_TOK.lower()].depth_usd_hint == pytest.approx(2 * 90_000, rel=1e-6)
    # ordering: deepest first (route truncation drops the shallow end first)
    assert [p.address.lower() for p in pools] == [P_UNI.lower(), P_AERO_TOK.lower(), P_PAIR_TOK.lower()]
    # metadata: fees/tick spacing read from the pools, aerodrome fee from the factory (30 bps → 3000 ppm)
    assert by_addr[P_UNI.lower()].fee_ppm == 500 and by_addr[P_UNI.lower()].tick_spacing == 10
    assert by_addr[P_AERO_TOK.lower()].fee_ppm == 3000 and by_addr[P_AERO_TOK.lower()].source == "aerodrome allPools"
    assert by_addr[P_PAIR_TOK.lower()].source == "uniswap_v3 factory getPool"


async def test_universe_without_filters_keeps_everything_measured(chain):
    idx = PoolIndexer(ScriptedRpc(), chain)  # type: ignore[arg-type]  (min_pool_usd=0, max_pools=0: devnet/verify behaviour)
    pools = await idx.discover()
    assert len(pools) == 4  # the shallow USDC/ENU pool is kept too
    assert idx.stats["pools_below_min_depth"] == 0


async def test_max_pools_keeps_the_deepest(chain):
    idx = PoolIndexer(ScriptedRpc(), chain, min_pool_usd=0, max_pools=2)  # type: ignore[arg-type]
    pools = await idx.discover()
    assert [p.address.lower() for p in pools] == [P_UNI.lower(), P_AERO_TOK.lower()]
    assert any("dropped by max_pools" in n for n in idx.stats["notes"])
