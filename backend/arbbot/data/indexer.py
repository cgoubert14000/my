"""Pool discovery & metadata. Builds the universe of `Pool` objects the engine will watch.

Mainnet universe (all measured on-chain at start-up, nothing hard-coded beyond the verified hub tokens):
  1. tokens  = verified hub tokens (chain config)
             ∪ bundled public token lists (data/tokenlists/<chain>.json — sources documented per entry)
             ∪ tokens of Aerodrome / Slipstream pools (factory `allPools(i)` enumeration) that hold a hub token;
  2. pools   = every (hub, token) and (hub, hub) pair on every DEX factory (V2 getPair, V3 getPool per fee tier,
               Solidly getPool(stable), Slipstream getPool(tickSpacing)) ∪ the enumerated pools with a hub side;
  3. depth   = real ERC-20 balances of each pool, valued with hub prices bootstrapped from the deepest hub/stable
               pools; pools below `discovery_min_pool_usd` are dropped, the `discovery_max_pools` deepest are kept.
Long-tail tokens are *not* individually verified: they can only appear in the middle of a route (never borrowed),
and every candidate is simulated against the real contract before it may count. Devnet: from deployments.local.json.
"""
from __future__ import annotations

import json
import logging
import math
import pathlib
import re
import time
from itertools import combinations

from eth_utils import to_checksum_address

from ..config.chains import ChainConfig, DexConfig
from ..core.math_v3 import Q96
from ..core.types import DexKind, Pool, Token
from .rpc import RpcClient, decode_result, encode_call

log = logging.getLogger("arbbot.indexer")

ZERO = "0x0000000000000000000000000000000000000000"
SLIPSTREAM_TICK_SPACINGS = (1, 50, 100, 200, 2000)
TOKENLIST_DIR = pathlib.Path(__file__).parent / "tokenlists"
_ADDR = re.compile(r"^0x[0-9a-fA-F]{40}$")


class DiscoveryStats(dict):
    """Plain dict with a stable key set so reports can show how the universe was built."""

    def __init__(self) -> None:
        super().__init__(tokens_config=0, tokens_tokenlist=0, tokens_factory_enum=0, tokens_rejected=0, tokens_total=0,
                         pools_enumerated=0, pools_from_pairs=0, pools_candidates=0, pools_measured=0,
                         pools_below_min_depth=0, pools_kept=0, min_pool_usd=0.0, max_pools=0, hub_prices={},
                         per_dex={}, notes=[])


class PoolIndexer:
    def __init__(self, rpc: RpcClient, chain: ChainConfig, *, use_tokenlists: bool = True, factory_enum: bool = True,
                 factory_enum_max: int = 60_000, min_pool_usd: float = 0.0, max_pools: int = 0, max_tokens: int = 1_200,
                 cache_path: pathlib.Path | None = None, cache_max_age_s: float = 3600.0):
        """min_pool_usd=0 / max_pools=0 ⇒ no depth filtering (devnet, verification). The runtime passes Settings.
        cache_path: universe written after a full discovery and reused (depths re-measured, never trusted) while younger
        than cache_max_age_s — verify-chain and the ghost/serve process that follows it share one discovery."""
        self.rpc = rpc
        self.chain = chain
        self.use_tokenlists = use_tokenlists
        self.factory_enum = factory_enum
        self.factory_enum_max = factory_enum_max
        self.min_pool_usd = min_pool_usd
        self.max_pools = max_pools
        self.max_tokens = max_tokens
        self.cache_path = cache_path
        self.cache_max_age_s = cache_max_age_s
        self.pools: dict[str, Pool] = {}
        self.stats = DiscoveryStats()
        self.token_sources: dict[str, str] = {}  # address → provenance
        self._last_prices: dict[str, float] = {}  # hub address → USD, filled by the first depth measurement

    # ------------------------------------------------------------------ helpers

    async def _mc(self, calls: list[tuple[str, bytes]], per_batch: int = 4_800) -> list[tuple[bool, bytes]]:
        """Multicall in sequential batches (6 × 800 calls in flight at most): discovery issues ~10⁵ calls and public
        RPCs answer 429 to a burst of a hundred concurrent requests."""
        out: list[tuple[bool, bytes]] = []
        for i in range(0, len(calls), per_batch):
            out.extend(await self.rpc.multicall(calls[i : i + per_batch], chunk=800))
        return out

    # ------------------------------------------------------------------ public

    async def discover(self) -> list[Pool]:
        if self.chain.static_pools:
            pools = self._from_static()
            pools = await self._load_metadata(pools)
        else:
            pools = await self._from_cache()
            if pools is None:
                pools = await self._from_universe()
                self._write_cache(pools)
        self.pools = {p.address.lower(): p for p in pools}
        log.info("indexed %d pools on %s", len(pools), self.chain.name)
        return pools

    # ------------------------------------------------------------------ universe cache (verify-chain → ghost/serve)

    def _write_cache(self, pools: list[Pool]) -> None:
        if not self.cache_path:
            return
        try:
            doc = {
                "chain_id": self.chain.chain_id, "ts": time.time(),
                "tokens": [{"key": k, "address": t.address, "decimals": t.decimals, "source": self.token_sources.get(t.address.lower(), "")}
                           for k, t in self.chain.tokens.items()],
                "pools": [{"address": p.address, "dex": p.dex, "kind": p.kind.name, "token0": p.token0.address, "token1": p.token1.address,
                           "fee_ppm": p.fee_ppm, "stable": p.stable, "tick_spacing": p.tick_spacing, "source": p.source} for p in pools],
                "stats": dict(self.stats),
            }
            self.cache_path.parent.mkdir(parents=True, exist_ok=True)
            self.cache_path.write_text(json.dumps(doc))
        except (OSError, TypeError, ValueError) as e:  # pragma: no cover
            log.warning("universe cache not written: %s", e)

    async def _from_cache(self) -> list[Pool] | None:
        """Rebuild the universe discovered by a previous process (< cache_max_age_s) — depths are re-measured and the
        same floor/cap applied, so the cache only saves the factory/pair discovery requests, never the measurement."""
        f = self.cache_path
        if not f or not f.exists():
            return None
        try:
            doc = json.loads(f.read_text())
        except (OSError, ValueError):
            return None
        age = time.time() - float(doc.get("ts", 0))
        if int(doc.get("chain_id", -1)) != self.chain.chain_id or age > self.cache_max_age_s:
            return None
        hubs = {t.address.lower(): t for t in self.chain.hub_tokens()}
        for t in doc.get("tokens", []):
            if t["address"].lower() not in hubs:
                self._register_token(t["address"], t["key"], int(t["decimals"]), t.get("source", "cache"))
        for a in hubs:
            self.token_sources[a] = "chain config (verified, see ADDRESS_SOURCES)"
        pools: list[Pool] = []
        for d in doc.get("pools", []):
            t0, t1 = self.chain.token_by_address(d["token0"]), self.chain.token_by_address(d["token1"])
            if not t0 or not t1:
                continue
            pools.append(Pool(address=to_checksum_address(d["address"]), dex=d["dex"], kind=DexKind[d["kind"]], token0=t0, token1=t1,
                              fee_ppm=int(d["fee_ppm"]), stable=bool(d.get("stable")), tick_spacing=int(d.get("tick_spacing", 0)),
                              source=d.get("source", "")))
        saved = doc.get("stats", {})
        for k in ("tokens_config", "tokens_tokenlist", "tokens_factory_enum", "tokens_rejected", "tokens_total", "pools_enumerated",
                  "pools_candidates", "per_dex"):
            if k in saved:
                self.stats[k] = saved[k]
        self.stats["min_pool_usd"], self.stats["max_pools"] = self.min_pool_usd, self.max_pools
        self.stats["notes"] = list(saved.get("notes", [])) + [f"universe reloaded from {f.name} (age {age:.0f} s); depths re-measured now"]
        pools = await self._measure_and_filter(pools, hubs)
        per_dex: dict[str, dict] = self.stats["per_dex"]
        for d in per_dex.values():
            d.pop("kept", None)
        for p in pools:
            per_dex.setdefault(p.dex, {})["kept"] = per_dex.get(p.dex, {}).get("kept", 0) + 1
        self.stats["pools_kept"] = len(pools)
        self.chain.extra["token_sources"] = dict(self.token_sources)
        self.chain.extra["discovery"] = dict(self.stats)
        log.info("universe reloaded from cache (%d pools after re-measurement)", len(pools))
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
                    source="devnet deployments",
                )
            )
        return out

    # ------------------------------------------------------------------ mainnet: tokens

    def _bundled_tokens(self) -> list[dict]:
        f = TOKENLIST_DIR / f"{self.chain.id}.json"
        if not self.use_tokenlists or not f.exists():
            return []
        try:
            doc = json.loads(f.read_text())
        except (OSError, ValueError) as e:  # pragma: no cover - corrupt bundle
            log.warning("token list %s unreadable: %s", f, e)
            return []
        if int(doc.get("chain_id", -1)) != self.chain.chain_id:
            return []
        return [t for t in doc.get("tokens", []) if _ADDR.match(str(t.get("address", "")))]

    async def _enumerate_factories(self, hubs: dict[str, Token], prices: dict[str, float]) -> list[tuple[DexConfig, str, str, str]]:
        """(dex, pool, token0, token1) for every enumerable factory pool that has a hub on one side."""
        out: list[tuple[DexConfig, str, str, str]] = []
        for dex in self.chain.dexes:
            if not (dex.enabled and dex.factory and dex.enumerable and self.factory_enum):
                continue
            try:
                raw = await self.rpc.call(dex.factory, encode_call("allPoolsLength()"))
                (n,) = decode_result(["uint256"], raw)
            except Exception as e:  # noqa: BLE001 - enumeration is best effort, pair discovery still runs
                self.stats["notes"].append(f"{dex.id}: allPoolsLength() failed ({type(e).__name__}) — enumeration skipped")
                continue
            n = int(n)
            start = max(0, n - self.factory_enum_max)
            res = await self._mc([(dex.factory, encode_call("allPools(uint256)", [i])) for i in range(start, n)])
            addrs = [to_checksum_address(decode_result(["address"], d)[0]) for ok, d in res if ok and len(d) >= 32]
            calls = []
            for a in addrs:
                calls.append((a, encode_call("token0()")))
                calls.append((a, encode_call("token1()")))
            res = await self._mc(calls)
            with_hub: list[tuple[str, str, str]] = []
            for i, a in enumerate(addrs):
                ok0, d0 = res[2 * i]
                ok1, d1 = res[2 * i + 1]
                if not (ok0 and ok1 and len(d0) >= 32 and len(d1) >= 32):
                    continue
                t0 = decode_result(["address"], d0)[0].lower()
                t1 = decode_result(["address"], d1)[0].lower()
                if t0 in hubs or t1 in hubs:
                    with_hub.append((a, t0, t1))
            # pre-screen on the hub-side balance alone (one balanceOf per pool): factories hold tens of thousands of
            # abandoned long-tail pools whose tokens would otherwise cost millions of getPool calls downstream
            bal_calls = []
            for a, t0, t1 in with_hub:
                h = t0 if t0 in hubs else t1
                bal_calls.append((hubs[h].address, encode_call("balanceOf(address)", [a])))
            bres = await self._mc(bal_calls)
            kept = 0
            for (a, t0, t1), (okb, db) in zip(with_hub, bres):
                h = t0 if t0 in hubs else t1
                bal = int.from_bytes(db[:32], "big") if okb and len(db) >= 32 else 0
                usd = 2.0 * bal / 10**hubs[h].decimals * prices.get(h, 0.0)
                if self.min_pool_usd and usd < self.min_pool_usd:
                    continue
                out.append((dex, a, t0, t1))
                kept += 1
            self.stats["per_dex"].setdefault(dex.id, {})["enumerated"] = n
            self.stats["per_dex"][dex.id]["with_hub_side"] = len(with_hub)
            self.stats["per_dex"][dex.id]["deep_enough"] = kept
            log.info("%s: %d pools enumerated, %d with a hub side, %d deep enough (≥ %.0f $)", dex.id, n, len(with_hub), kept, self.min_pool_usd)
        self.stats["pools_enumerated"] = len(out)
        return out

    async def _token_metadata(self, addresses: list[str]) -> dict[str, tuple[str, int]]:
        """address → (symbol, decimals) read on-chain; tokens whose decimals() fails or is absurd are rejected."""
        calls = []
        for a in addresses:
            calls.append((a, encode_call("decimals()")))
            calls.append((a, encode_call("symbol()")))
        res = await self._mc(calls)
        out: dict[str, tuple[str, int]] = {}
        for i, a in enumerate(addresses):
            okd, dd = res[2 * i]
            oks, ds = res[2 * i + 1]
            if not okd or len(dd) < 32:
                continue
            dec = int(decode_result(["uint8"], dd[:32])[0]) if int.from_bytes(dd[:32], "big") < 256 else -1
            if dec < 0 or dec > 36:
                continue
            sym = ""
            if oks and ds:
                try:
                    sym = str(decode_result(["string"], ds)[0])
                except Exception:  # noqa: BLE001 - bytes32 symbols (MKR style)
                    sym = ds[:32].rstrip(b"\x00").decode("utf-8", "ignore")
            sym = re.sub(r"[^0-9A-Za-z_.$-]", "", sym)[:16] or f"T{a[2:8]}"
            out[a.lower()] = (sym, dec)
        return out

    def _register_token(self, address: str, symbol: str, decimals: int, source: str) -> Token:
        a = address.lower()
        existing = self.chain.token_by_address(a)
        if existing:
            self.token_sources.setdefault(a, source)
            return existing
        key = symbol
        if key in self.chain.tokens:  # symbol collisions are common in the long tail (fake "USDC"s): keep both distinct
            key = f"{symbol}_{address[2:6]}"
        tok = Token(to_checksum_address(address), key, decimals)
        self.chain.tokens[key] = tok
        self.token_sources[a] = source
        return tok

    # ------------------------------------------------------------------ mainnet: pools

    async def _from_universe(self) -> list[Pool]:
        hubs = {t.address.lower(): t for t in self.chain.hub_tokens()}  # snapshot BEFORE the long tail is added
        self.stats["tokens_config"] = len(hubs)
        self.stats["min_pool_usd"], self.stats["max_pools"] = self.min_pool_usd, self.max_pools
        for a in hubs:
            self.token_sources[a] = "chain config (verified, see ADDRESS_SOURCES)"
        # 1) candidate tokens ---------------------------------------------------------------------------------
        candidates: dict[str, tuple[str, int | None, str]] = {}  # address → (symbol hint, decimals hint, source)
        for t in self._bundled_tokens():
            a = t["address"].lower()
            if a not in hubs and a not in candidates:
                candidates[a] = (str(t.get("symbol", ""))[:16], t.get("decimals"), "tokenlist: " + "; ".join(t.get("sources", [])))
        self.stats["tokens_tokenlist"] = len(candidates)
        # hub×hub pools first: they give the USD prices every depth measurement below relies on
        hub_list = list(hubs.values())
        hub_pools = await self._load_metadata(await self._pools_for_pairs(list(combinations(hub_list, 2))))
        prices = await self._hub_prices(hub_pools, hubs)
        enumerated = await self._enumerate_factories(hubs, prices)
        n_enum_tokens = 0
        for dex, pool, t0, t1 in enumerated:
            for a in (t0, t1):
                if a not in hubs and a not in candidates:
                    candidates[a] = ("", None, f"on-chain: {dex.id} factory allPools → pool {pool}")
                    n_enum_tokens += 1
        self.stats["tokens_factory_enum"] = n_enum_tokens
        if self.max_tokens and len(candidates) > self.max_tokens:  # RPC budget: list tokens first, then enumerated ones
            self.stats["notes"].append(f"{len(candidates)} candidate tokens capped to {self.max_tokens}")
            candidates = dict(list(candidates.items())[: self.max_tokens])
        # 2) validate tokens on-chain (decimals/symbol) and register them ------------------------------------------
        meta = await self._token_metadata([to_checksum_address(a) for a in candidates])
        tokens: dict[str, Token] = dict(hubs)
        for a, (sym_hint, dec_hint, src) in candidates.items():
            if a not in meta:
                self.stats["tokens_rejected"] += 1
                continue
            sym, dec = meta[a]
            if dec_hint is not None and int(dec_hint) != dec:
                self.stats["tokens_rejected"] += 1
                self.stats["notes"].append(f"{a}: decimals mismatch list={dec_hint} chain={dec} — rejected")
                continue
            tokens[a] = self._register_token(a, sym_hint or sym, dec, src)
        self.stats["tokens_total"] = len(tokens)
        # 3) pools: enumerated ones + (hub, token) pairs on every factory ----------------------------------------
        pools: dict[str, Pool] = {}
        for dex, addr, t0, t1 in enumerated:
            if t0 in tokens and t1 in tokens and addr.lower() not in pools:
                pools[addr.lower()] = Pool(address=addr, dex=dex.id, kind=dex.kind, token0=tokens[t0], token1=tokens[t1],
                                           fee_ppm=0 if dex.kind == DexKind.SOLIDLY else dex.fee_ppm, stable=False,
                                           tick_spacing=0, source=f"{dex.id} allPools")
        for p in hub_pools:
            pools.setdefault(p.address.lower(), p)
        pairs: list[tuple[Token, Token]] = []
        for a, tok in tokens.items():
            if a in hubs:
                continue
            for h in hub_list:
                pairs.append((h, tok))
        for p in await self._pools_for_pairs(pairs):
            pools.setdefault(p.address.lower(), p)
        self.stats["pools_candidates"] = len(pools)
        plist = await self._load_metadata(list(pools.values()))
        # enumerated Solidly pools: stable flag is read from the pool itself
        await self._fill_solidly_stable(plist)
        # 4) measure depth and keep the deepest -----------------------------------------------------------------
        plist = await self._measure_and_filter(plist, hubs)
        per_dex: dict[str, dict] = self.stats["per_dex"]
        for p in plist:
            per_dex.setdefault(p.dex, {})["kept"] = per_dex.get(p.dex, {}).get("kept", 0) + 1
        self.stats["pools_kept"] = len(plist)
        self.chain.extra["token_sources"] = dict(self.token_sources)
        self.chain.extra["discovery"] = dict(self.stats)
        return plist

    async def _pools_for_pairs(self, pairs: list[tuple[Token, Token]]) -> list[Pool]:
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
        results = await self._mc(calls)
        pools: list[Pool] = []
        for (ok, data), (dex, a, b, fee, stable) in zip(results, meta):
            if not ok or len(data) < 32:
                continue
            (addr,) = decode_result(["address"], data)
            if addr.lower() == ZERO:
                continue
            t0, t1 = (a, b) if a.address.lower() < b.address.lower() else (b, a)
            pools.append(
                Pool(
                    address=to_checksum_address(addr),
                    dex=dex.id,
                    kind=dex.kind,
                    token0=t0,
                    token1=t1,
                    fee_ppm=fee if dex.kind != DexKind.SOLIDLY else 0,
                    stable=stable,
                    tick_spacing=fee if dex.id == "aerodrome_slipstream" else 0,
                    source=f"{dex.id} factory getPool",
                )
            )
        self.stats["pools_from_pairs"] += len(pools)
        log.info("factory discovery: %d candidate pools from %d queries over %d pairs", len(pools), len(calls), len(pairs))
        return pools

    async def _fill_solidly_stable(self, pools: list[Pool]) -> None:
        todo = [p for p in pools if p.kind == DexKind.SOLIDLY and p.source.endswith("allPools")]
        if not todo:
            return
        res = await self._mc([(p.address, encode_call("stable()")) for p in todo])
        for p, (ok, d) in zip(todo, res):
            if ok and len(d) >= 32:
                p.stable = bool(int.from_bytes(d[:32], "big"))
        # fee depends on the stable flag → re-read for those pools
        dex_by_id = {d.id: d for d in self.chain.dexes}
        calls = []
        for p in todo:
            dex = dex_by_id.get(p.dex)
            if dex and dex.solidly_fee_from_factory:
                calls.append((dex.factory, encode_call("getFee(address,bool)", [p.address, p.stable])))
            else:
                calls.append((p.address, encode_call("fee()")))
        res = await self._mc(calls)
        for p, (ok, d) in zip(todo, res):
            if ok and len(d) >= 32:
                p.fee_ppm = int(decode_result(["uint256"], d)[0]) * 100

    async def _measure_and_filter(self, pools: list[Pool], hubs: dict[str, Token]) -> list[Pool]:
        """Read every pool's token balances, bootstrap hub prices, drop shallow pools, keep the deepest."""
        if not pools:
            return []
        calls: list[tuple[str, bytes]] = []
        for p in pools:
            calls.append((p.token0.address, encode_call("balanceOf(address)", [p.address])))
            calls.append((p.token1.address, encode_call("balanceOf(address)", [p.address])))
        # price sources: slot0 for CL pools, reserves for the others (hub/stable pairs only are used for prices)
        price_calls: list[tuple[str, bytes]] = []
        price_idx: list[int] = []
        stables = self.chain.stable_addresses()
        for i, p in enumerate(pools):
            a0, a1 = p.token0.address.lower(), p.token1.address.lower()
            if (a0 in hubs and a1 in hubs) and (a0 in stables or a1 in stables):
                price_idx.append(i)
                if p.kind in (DexKind.UNIV3, DexKind.PANCAKE_V3):
                    price_calls.append((p.address, encode_call("slot0()")))
                else:
                    price_calls.append((p.address, encode_call("getReserves()")))
        res = await self._mc(calls + price_calls)
        bal = res[: len(calls)]
        for i, p in enumerate(pools):
            ok0, d0 = bal[2 * i]
            ok1, d1 = bal[2 * i + 1]
            p.balance0 = int.from_bytes(d0[:32], "big") if ok0 and len(d0) >= 32 else 0
            p.balance1 = int.from_bytes(d1[:32], "big") if ok1 and len(d1) >= 32 else 0
            p.balances_block = 1  # "measured once" — the collector refreshes with the real block number
        self.stats["pools_measured"] = len(pools)
        prices = self._prices_from(pools, hubs, stables, res[len(calls):], price_idx)
        return self._filter_by_depth(pools, prices)

    async def _hub_prices(self, hub_pools: list[Pool], hubs: dict[str, Token]) -> dict[str, float]:
        """USD prices of the hubs from the hub/stable pools (balances + slot0/reserves); stables = 1 by definition."""
        if not hub_pools:
            return {a: 1.0 for a in self.chain.stable_addresses() if a in hubs}
        await self._measure_and_filter(hub_pools, hubs)  # fills balances of the hub pools and self._last_prices
        self.stats["pools_below_min_depth"] = 0  # the hub pools are measured again with the whole universe
        return dict(self._last_prices)

    def _prices_from(self, pools: list[Pool], hubs: dict[str, Token], stables: set[str], price_res, price_idx: list[int]) -> dict[str, float]:
        # hub prices in USD: stables = 1; others from the hub/stable pool holding the most stable units
        prices: dict[str, float] = {a: 1.0 for a in stables if a in hubs}
        best_depth: dict[str, float] = {}
        for (ok, d), i in zip(price_res, price_idx):
            p = pools[i]
            if not ok or len(d) < 64:
                continue
            a0, a1 = p.token0.address.lower(), p.token1.address.lower()
            try:
                if p.kind in (DexKind.UNIV3, DexKind.PANCAKE_V3):
                    sqrt_p = int.from_bytes(d[:32], "big")
                    if sqrt_p == 0:
                        continue
                    mid = (sqrt_p / Q96) ** 2 * 10**p.token0.decimals / 10**p.token1.decimals  # token1 per token0
                else:
                    r0, r1 = int.from_bytes(d[:32], "big"), int.from_bytes(d[32:64], "big")
                    if r0 == 0 or r1 == 0:
                        continue
                    mid = (r1 / 10**p.token1.decimals) / (r0 / 10**p.token0.decimals)
            except (ZeroDivisionError, OverflowError, ValueError):
                continue
            if not (mid > 0 and math.isfinite(mid)):
                continue
            if a1 in stables and a0 not in stables:
                tok, px, depth = a0, mid, p.balance1 / 10**p.token1.decimals
            elif a0 in stables and a1 not in stables:
                tok, px, depth = a1, 1.0 / mid, p.balance0 / 10**p.token0.decimals
            else:
                continue
            if depth > best_depth.get(tok, 0.0):
                best_depth[tok], prices[tok] = depth, px
        for a, v in self._last_prices.items():  # keep prices found earlier (hub pools) when this batch has none
            prices.setdefault(a, v)
        self._last_prices = dict(prices)
        self.stats["hub_prices"] = {hubs[a].symbol: round(v, 6) for a, v in prices.items() if a in hubs}
        return prices

    def _filter_by_depth(self, pools: list[Pool], prices: dict[str, float]) -> list[Pool]:
        # depth in USD: hub-side balances valued (both sides when both are hubs)
        kept: list[Pool] = []
        for p in pools:
            a0, a1 = p.token0.address.lower(), p.token1.address.lower()
            v0 = p.balance0 / 10**p.token0.decimals * prices[a0] if a0 in prices else None
            v1 = p.balance1 / 10**p.token1.decimals * prices[a1] if a1 in prices else None
            if v0 is None and v1 is None:
                depth = 0.0
            elif v0 is None or v1 is None:
                depth = 2.0 * (v0 if v0 is not None else v1)  # the other side is worth about the same at the margin
            else:
                depth = v0 + v1
            p.depth_usd_hint = depth
            if depth < self.min_pool_usd:
                self.stats["pools_below_min_depth"] += 1
                continue
            kept.append(p)
        kept.sort(key=lambda p: -p.depth_usd_hint)
        if self.max_pools and len(kept) > self.max_pools:
            self.stats["notes"].append(f"{len(kept) - self.max_pools} pools above the depth floor dropped by max_pools={self.max_pools}")
            kept = kept[: self.max_pools]
        return kept

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
        results = await self._mc(calls)
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
