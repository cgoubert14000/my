"""Pool discovery & metadata. Builds the universe of `Pool` objects the engine will watch.

Mainnet: discovered from DEX factories for every token pair in the chain config (V2 getPair, V3 getPool per fee
tier, Solidly getPool(stable), Slipstream getPool(tickSpacing)). Devnet: from deployments.local.json.
"""
from __future__ import annotations

import logging
from itertools import combinations

from eth_utils import to_checksum_address

from ..config.chains import ChainConfig, DexConfig
from ..core.types import DexKind, Pool, Token
from .rpc import RpcClient, decode_result, encode_call

log = logging.getLogger("arbbot.indexer")

ZERO = "0x0000000000000000000000000000000000000000"
SLIPSTREAM_TICK_SPACINGS = (1, 50, 100, 200, 2000)


class PoolIndexer:
    def __init__(self, rpc: RpcClient, chain: ChainConfig):
        self.rpc = rpc
        self.chain = chain
        self.pools: dict[str, Pool] = {}

    # ------------------------------------------------------------------ public

    async def discover(self) -> list[Pool]:
        if self.chain.static_pools:
            pools = self._from_static()
        else:
            pools = await self._from_factories()
        pools = await self._load_metadata(pools)
        self.pools = {p.address.lower(): p for p in pools}
        log.info("indexed %d pools on %s", len(pools), self.chain.name)
        return pools

    # ------------------------------------------------------------------ devnet

    def _from_static(self) -> list[Pool]:
        out = []
        for sp in self.chain.static_pools:
            t0 = self.chain.token_by_address(sp["token0"])
            t1 = self.chain.token_by_address(sp["token1"])
            if not t0 or not t1:
                continue
            out.append(
                Pool(
                    address=to_checksum_address(sp["address"]),
                    dex=sp["dex"],
                    kind=DexKind[sp["kind"]],
                    token0=t0,
                    token1=t1,
                    fee_ppm=int(sp["fee_ppm"]),
                    stable=bool(sp.get("stable", False)),
                    tick_spacing=int(sp.get("tick_spacing", 0)),
                )
            )
        return out

    # ------------------------------------------------------------------ mainnet

    async def _from_factories(self) -> list[Pool]:
        tokens = list(self.chain.tokens.values())
        pairs = list(combinations(tokens, 2))
        calls: list[tuple[str, bytes]] = []
        meta: list[tuple[DexConfig, Token, Token, int, bool]] = []  # (dex, a, b, fee_or_spacing, stable)
        for dex in self.chain.dexes:
            if not dex.enabled or not dex.factory:
                continue
            for a, b in pairs:
                if dex.kind == DexKind.UNIV2:
                    calls.append((dex.factory, encode_call("getPair(address,address)", [a.address, b.address])))
                    meta.append((dex, a, b, dex.fee_ppm, False))
                elif dex.kind in (DexKind.UNIV3, DexKind.PANCAKE_V3):
                    if dex.id == "aerodrome_slipstream":
                        for ts in SLIPSTREAM_TICK_SPACINGS:
                            calls.append((dex.factory, encode_call("getPool(address,address,int24)", [a.address, b.address, ts])))
                            meta.append((dex, a, b, ts, False))
                    else:
                        for fee in dex.fee_tiers:
                            calls.append((dex.factory, encode_call("getPool(address,address,uint24)", [a.address, b.address, fee])))
                            meta.append((dex, a, b, fee, False))
                elif dex.kind == DexKind.SOLIDLY:
                    for stable in (False, True):
                        calls.append((dex.factory, encode_call("getPool(address,address,bool)", [a.address, b.address, stable])))
                        meta.append((dex, a, b, 0, stable))
        results = await self.rpc.multicall(calls)
        pools: list[Pool] = []
        for (ok, data), (dex, a, b, fee, stable) in zip(results, meta):
            if not ok or len(data) < 32:
                continue
            (addr,) = decode_result(["address"], data)
            if addr.lower() == ZERO:
                continue
            t0, t1 = (a, b) if a.address.lower() < b.address.lower() else (b, a)
            kind = dex.kind
            pools.append(
                Pool(
                    address=to_checksum_address(addr),
                    dex=dex.id,
                    kind=kind,
                    token0=t0,
                    token1=t1,
                    fee_ppm=fee if kind != DexKind.SOLIDLY else 0,
                    stable=stable,
                    tick_spacing=fee if dex.id == "aerodrome_slipstream" else 0,
                )
            )
        log.info("factory discovery: %d candidate pools from %d queries", len(pools), len(calls))
        return pools

    async def _load_metadata(self, pools: list[Pool]) -> list[Pool]:
        """Fill fee/tickSpacing for V3 pools and Solidly fees; verify token ordering on-chain."""
        calls: list[tuple[str, bytes]] = []
        idx: list[tuple[int, str]] = []
        dex_by_id = {d.id: d for d in self.chain.dexes}
        for i, p in enumerate(pools):
            calls.append((p.address, encode_call("token0()")))
            idx.append((i, "token0"))
            if p.kind in (DexKind.UNIV3, DexKind.PANCAKE_V3):
                calls.append((p.address, encode_call("fee()")))
                idx.append((i, "fee"))
                calls.append((p.address, encode_call("tickSpacing()")))
                idx.append((i, "tickSpacing"))
            elif p.kind == DexKind.SOLIDLY:
                dex = dex_by_id.get(p.dex)
                if dex and dex.solidly_fee_from_factory:
                    calls.append((dex.factory, encode_call("getFee(address,bool)", [p.address, p.stable])))
                    idx.append((i, "solidlyFee"))
                else:
                    calls.append((p.address, encode_call("fee()")))
                    idx.append((i, "solidlyFeeDirect"))
        results = await self.rpc.multicall(calls)
        keep = set(range(len(pools)))
        for (ok, data), (i, what) in zip(results, idx):
            p = pools[i]
            if not ok or len(data) < 32:
                if what == "token0":
                    keep.discard(i)
                    p.quarantined, p.quarantine_reason = True, "token0() failed"
                continue
            if what == "token0":
                (t0,) = decode_result(["address"], data)
                if t0.lower() != p.token0.address.lower():
                    p.token0, p.token1 = p.token1, p.token0
            elif what == "fee":
                p.fee_ppm = decode_result(["uint24"], data)[0]
            elif what == "tickSpacing":
                p.tick_spacing = decode_result(["int24"], data)[0]
            elif what in ("solidlyFee", "solidlyFeeDirect"):
                p.fee_ppm = int(decode_result(["uint256"], data)[0]) * 100  # bps → ppm
        return [p for i, p in enumerate(pools) if i in keep]
