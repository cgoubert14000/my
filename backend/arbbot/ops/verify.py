"""Live verification of a chain configuration against the connected RPC (`arbbot verify-chain`).

Everything the engine will rely on is probed BEFORE the first cycle:
  * chain id, RPC latency, block time (measured), base fee, priority fee, state-override and multicall support;
  * code present at every configured address; token symbol/decimals equal to the config;
  * factories answer the exact probes the indexer uses (V2 allPairsLength, V3 feeAmountTickSpacing, Solidly
    allPoolsLength/getFee, Slipstream tickSpacingToFee);
  * flash-loan providers: fee read on-chain where exposed and *live capacity* per borrowable token;
  * pool discovery through the factories + a full state refresh → depth in USD of every pool;
  * OP-stack L1 fee oracle (Base) answers.
The report is written to docs/reports/ and, when every blocking check passes, data/verified_<chain>.json records a
digest of the configuration so the runtime can display "adresses vérifiées" truthfully. A later config change
invalidates the digest automatically.
"""
from __future__ import annotations

import hashlib
import json
import pathlib
import statistics
import time
from dataclasses import asdict, dataclass, field

from ..config.chains import ChainConfig, address_source, get_chain
from ..config.settings import REPO_ROOT, Settings
from ..core.types import DexKind, FlashSource
from ..data.collector import StateCollector
from ..data.indexer import PoolIndexer
from ..data.rpc import RpcClient, RpcError, decode_result, encode_call
from ..engine.fees import FeeCalculator


@dataclass
class Check:
    name: str
    ok: bool
    detail: str = ""
    blocking: bool = True


@dataclass
class VerifyReport:
    chain: str
    chain_id: int
    rpc_host: str
    ts: float = field(default_factory=time.time)
    checks: list[Check] = field(default_factory=list)
    pools: list[dict] = field(default_factory=list)
    providers: dict = field(default_factory=dict)
    network: dict = field(default_factory=dict)
    config_digest: str = ""

    @property
    def ok(self) -> bool:
        return all(c.ok for c in self.checks if c.blocking)

    def add(self, name: str, ok: bool, detail: str = "", blocking: bool = True) -> None:
        self.checks.append(Check(name, bool(ok), detail, blocking))

    def as_dict(self) -> dict:
        d = asdict(self)
        d["ok"] = self.ok
        return d


def config_digest(chain: ChainConfig) -> str:
    """Digest of every address the engine trusts; changes → re-verification required."""
    parts = [str(chain.chain_id), chain.multicall3.lower(), chain.wrapped_native.lower(), chain.opstack_gas_oracle.lower()]
    parts += sorted(f"{k}:{t.address.lower()}:{t.decimals}" for k, t in chain.tokens.items())
    parts += sorted(f"{d.id}:{d.factory.lower()}:{d.enabled}" for d in chain.dexes)
    parts += sorted(f"{p.source.name}:{p.address.lower()}" for p in chain.flash_providers)
    return hashlib.sha256("|".join(parts).encode()).hexdigest()[:16]


def verified_file(settings: Settings, chain: ChainConfig) -> pathlib.Path:
    return settings.data_dir / f"verified_{chain.id}.json"


def load_verification(settings: Settings, chain: ChainConfig) -> dict | None:
    """Returns the stored verification if it matches the current config digest (else None)."""
    f = verified_file(settings, chain)
    if not f.exists():
        return None
    try:
        d = json.loads(f.read_text())
    except (OSError, json.JSONDecodeError):
        return None
    if d.get("config_digest") != config_digest(chain) or not d.get("ok"):
        return None
    return d


async def _probe_factory(rpc: RpcClient, dex, rep: VerifyReport) -> None:
    try:
        if dex.kind == DexKind.UNIV2:
            raw = await rpc.call(dex.factory, encode_call("allPairsLength()"))
            n = int(decode_result(["uint256"], raw)[0])
            rep.add(f"factory:{dex.id}", n > 0, f"V2 allPairsLength={n}")
        elif dex.kind in (DexKind.UNIV3, DexKind.PANCAKE_V3):
            if dex.id == "aerodrome_slipstream":
                raw = await rpc.call(dex.factory, encode_call("tickSpacingToFee(int24)", [100]))
                fee = int(decode_result(["uint24"], raw)[0])
                rep.add(f"factory:{dex.id}", fee > 0, f"Slipstream tickSpacingToFee(100)={fee}")
            else:
                tier = 2500 if dex.kind == DexKind.PANCAKE_V3 else 3000
                raw = await rpc.call(dex.factory, encode_call("feeAmountTickSpacing(uint24)", [tier]))
                ts = int(decode_result(["int24"], raw)[0])
                rep.add(f"factory:{dex.id}", ts > 0, f"V3 feeAmountTickSpacing({tier})={ts}")
        elif dex.kind == DexKind.SOLIDLY:
            raw = await rpc.call(dex.factory, encode_call("allPoolsLength()"))
            n = int(decode_result(["uint256"], raw)[0])
            rep.add(f"factory:{dex.id}", n > 0, f"Solidly allPoolsLength={n}")
        else:
            rep.add(f"factory:{dex.id}", False, f"unknown kind {dex.kind}")
    except RpcError as e:
        rep.add(f"factory:{dex.id}", False, f"probe failed: {e}")


async def verify_chain(settings: Settings, *, discover_pools: bool = True, write: bool = True, log=print) -> VerifyReport:
    chain = get_chain(settings.chain, settings.devnet_deployments)
    rpc = RpcClient(settings.rpc_http_url, settings.fallback_urls, settings.rpc_timeout_s, settings.rpc_max_rps, chain.multicall3)
    host = settings.rpc_http_url.split("//")[-1].split("/")[0]
    rep = VerifyReport(chain=chain.id, chain_id=chain.chain_id, rpc_host=host, config_digest=config_digest(chain))
    t0 = time.perf_counter()
    try:
        await rpc.open()
    except (RpcError, Exception) as e:  # noqa: BLE001 — unreachable/odd endpoints must not leak sessions
        rep.add("rpc_reachable", False, f"{host}: {e}")
        await rpc.close()
        return rep
    rep.add("rpc_reachable", True, f"{host} in {(time.perf_counter() - t0) * 1000:.0f} ms")
    try:
        # ---------------------------------------------------------------- chain id, blocks, fees
        cid = int(await rpc.request("eth_chainId"), 16)
        rep.add("chain_id", cid == chain.chain_id, f"rpc={cid} config={chain.chain_id}")
        head = await rpc.get_block("latest")
        n = int(head["number"], 16)
        older = await rpc.get_block(max(n - 20, 0))
        span = int(head["timestamp"], 16) - int(older["timestamp"], 16)
        measured_bt = span / max(n - int(older["number"], 16), 1)
        base_fee = int(head.get("baseFeePerGas", "0x0"), 16)
        try:
            prio = int(await rpc.request("eth_maxPriorityFeePerGas"), 16)
        except RpcError:
            prio = None
        lat = []
        for _ in range(10):
            t1 = time.perf_counter()
            await rpc.block_number()
            lat.append((time.perf_counter() - t1) * 1000)
        rep.network = {"block": n, "block_time_measured_s": round(measured_bt, 3), "block_time_config_s": chain.block_time_s,
                       "base_fee_gwei": base_fee / 1e9, "priority_fee_gwei": None if prio is None else prio / 1e9,
                       "latency_p50_ms": round(statistics.median(lat), 1), "latency_max_ms": round(max(lat), 1),
                       "head_age_s": round(time.time() - int(head["timestamp"], 16), 1)}
        rep.add("block_time", abs(measured_bt - chain.block_time_s) <= max(0.5, chain.block_time_s), f"measured {measured_bt:.2f} s vs config {chain.block_time_s} s", blocking=False)
        rep.add("head_fresh", rep.network["head_age_s"] < 60, f"head age {rep.network['head_age_s']} s")
        rep.add("rpc_latency", statistics.median(lat) < 1500, f"p50 {statistics.median(lat):.0f} ms, max {max(lat):.0f} ms", blocking=False)
        # ---------------------------------------------------------------- multicall + state override support
        try:
            res = await rpc.multicall([(chain.multicall3, encode_call("getChainId()")), (chain.multicall3, encode_call("getBlockNumber()"))])
            ok = all(r[0] for r in res) and int(decode_result(["uint256"], res[0][1])[0]) == cid
            rep.add("multicall3", ok, f"{chain.multicall3} aggregate3 ok={ok}")
        except RpcError as e:
            rep.add("multicall3", False, f"{chain.multicall3}: {e}")
        try:
            # PUSH1 0x2a PUSH1 0 MSTORE PUSH1 0x20 PUSH1 0 RETURN → returns 42 ; the override must be honoured by eth_call
            probe_addr = "0x00000000000000000000000000000000000000AA"
            raw = await rpc.call(probe_addr, b"", overrides={probe_addr: {"code": "0x602a60005260206000f3"}})
            ok = len(raw) == 32 and int.from_bytes(raw, "big") == 42
            rep.add("eth_call_state_override", ok, "supported" if ok else f"unexpected result {raw.hex()}", blocking=False)
        except RpcError as e:
            rep.add("eth_call_state_override", False, f"not supported by this RPC ({e}); simulation needs the deployed executor", blocking=False)
        try:
            await rpc.request("debug_traceTransaction", ["0x" + "00" * 32, {"tracer": "callTracer"}])
            rep.add("debug_traceTransaction", True, "available", blocking=False)
        except RpcError as e:
            msg = str(e).lower()
            avail = "not found" in msg and "method" not in msg  # tx unknown ⇒ method exists
            rep.add("debug_traceTransaction", avail, "available" if avail else f"unavailable ({e}) → revert reasons come from eth_call replay", blocking=False)
        # ---------------------------------------------------------------- code at every configured address
        targets = [("multicall3", chain.multicall3), ("wrapped_native", chain.wrapped_native)]
        targets += [(f"dex:{d.id}", d.factory) for d in chain.dexes if d.factory and d.enabled]
        targets += [(f"flash:{p.source.name}", p.address) for p in chain.flash_providers]
        targets += [(f"token:{k}", t.address) for k, t in chain.tokens.items()]
        if chain.l1_fee_model == "opstack":
            targets.append(("opstack_gas_oracle", chain.opstack_gas_oracle))
        if chain.executor:
            targets.append(("executor", chain.executor))
        if settings.executor_address:
            targets.append(("executor(.env)", settings.executor_address))
        for name, addr in targets:
            try:
                code = await rpc.get_code(addr)
                src = "" if chain.id == "local" else f" — source: {address_source(addr)}"
                rep.add(f"code:{name}", len(code) > 0, f"{addr} ({len(code)} bytes){src}")
            except RpcError as e:
                rep.add(f"code:{name}", False, f"{addr}: {e}")
        # ---------------------------------------------------------------- tokens: symbol + decimals must match
        calls = []
        for k, t in chain.tokens.items():
            calls += [(t.address, encode_call("decimals()")), (t.address, encode_call("symbol()"))]
        try:
            res = await rpc.multicall(calls)
            for i, (k, t) in enumerate(chain.tokens.items()):
                okd, rd = res[2 * i]
                oks, rs = res[2 * i + 1]
                dec = int(decode_result(["uint8"], rd)[0]) if okd and len(rd) >= 32 else None
                sym = None
                if oks and rs:
                    try:
                        sym = decode_result(["string"], rs)[0]
                    except Exception:  # noqa: BLE001  — bytes32 symbols (MKR-style)
                        sym = rs[:32].rstrip(b"\x00").decode(errors="replace")
                good = dec == t.decimals and sym is not None and sym.upper().replace(".", "") == t.symbol.upper().replace(".", "")
                rep.add(f"token:{k}", good, f"on-chain symbol={sym} decimals={dec} / config {t.symbol}/{t.decimals}")
        except RpcError as e:
            rep.add("tokens", False, f"metadata multicall failed: {e}")
        # ---------------------------------------------------------------- factories
        for dex in chain.dexes:
            if dex.enabled and dex.factory:
                await _probe_factory(rpc, dex, rep)
        # ---------------------------------------------------------------- L1 fee oracle (OP stack)
        if chain.l1_fee_model == "opstack":
            try:
                raw = await rpc.call(chain.opstack_gas_oracle, encode_call("getL1FeeUpperBound(uint256)", [900]))
                fee = int(decode_result(["uint256"], raw)[0])
                rep.add("l1_fee_oracle", True, f"getL1FeeUpperBound(900 B) = {fee / 1e18:.9f} ETH")
                rep.network["l1_fee_900B_eth"] = fee / 1e18
            except RpcError as e:
                rep.add("l1_fee_oracle", False, f"{chain.opstack_gas_oracle}: {e}")
        # ---------------------------------------------------------------- pools + providers (live)
        pools = []
        if discover_pools:
            try:
                pools = await PoolIndexer(rpc, chain, use_tokenlists=settings.discovery_tokenlists,
                                          factory_enum=settings.discovery_factory_enum,
                                          factory_enum_max=settings.discovery_factory_enum_max,
                                          min_pool_usd=settings.discovery_min_pool_usd,
                                          max_pools=settings.discovery_max_pools, max_tokens=settings.discovery_max_tokens,
                                          cache_path=settings.data_dir / f"universe_{chain.id}.json",
                                          cache_max_age_s=settings.discovery_cache_max_age_s).discover()
                by_dex: dict[str, int] = {}
                for p in pools:
                    by_dex[p.dex] = by_dex.get(p.dex, 0) + 1
                rep.add("pool_discovery", len(pools) > 0, f"{len(pools)} pools: {by_dex}")
            except RpcError as e:
                rep.add("pool_discovery", False, f"{e}")
        if pools:
            collector = StateCollector(rpc, chain, pools)
            try:
                await collector.refresh(n)
                fees = FeeCalculator(rpc, chain, collector, __import__("arbbot.config.tunables", fromlist=["TunableParams"]).TunableParams())
                await fees.refresh_providers(list(chain.tokens.values()))
                rows = []
                for p in pools:
                    x, y = p.depth_tokens()
                    p0, p1 = fees.token_price_usd(p.token0), fees.token_price_usd(p.token1)
                    depth = None
                    if p0 is not None and p1 is not None:
                        depth = x / 10**p.token0.decimals * p0 + y / 10**p.token1.decimals * p1
                    rows.append({"address": p.address, "dex": p.dex, "kind": p.kind.name, "pair": f"{p.token0.symbol}/{p.token1.symbol}",
                                 "fee_ppm": p.fee_ppm, "stable": p.stable, "depth_usd": None if depth is None else round(depth, 2),
                                 "quarantined": p.quarantined, "reason": p.quarantine_reason})
                rows.sort(key=lambda r: -(r["depth_usd"] or 0))
                rep.pools = rows
                deep = [r for r in rows if (r["depth_usd"] or 0) >= 20_000]
                rep.add("pools_with_depth", len(deep) >= 2, f"{len(deep)} pools ≥ 20 000 $ (deepest: {rows[0]['pair']} {rows[0]['dex']} {rows[0]['depth_usd']} $)" if rows else "none")
                rep.network["native_price_usd"] = collector.native_price_usd
                rep.add("native_price", collector.native_price_usd is not None, f"ETH ≈ {collector.native_price_usd} $ (from the deepest WETH/stable pool)")
                for src, live in fees.providers.items():
                    cap = {}
                    for sym in chain.borrowable:
                        t = chain.tokens.get(sym)
                        if t:
                            cap[sym] = live.capacity.get(t.address.lower(), 0) / 10**t.decimals
                    rep.providers[src.name] = {"address": live.address, "fee_bps": live.fee_bps_x100 / 100, "verified": live.verified, "capacity": cap}
                    rep.add(f"flash:{src.name}", live.verified and any(v > 0 for v in cap.values()),
                            f"fee {live.fee_bps_x100 / 100} bps, capacity {', '.join(f'{k} {v:,.2f}' for k, v in cap.items())}", blocking=False)
                rep.add("flash_any_capacity", any(any(v > 0 for v in p["capacity"].values()) for p in rep.providers.values()),
                        "at least one provider can lend a borrowable token")
            except RpcError as e:
                rep.add("state_refresh", False, f"{e}")
            finally:
                collector.stop()
    finally:
        await rpc.close()
    if write:
        _write(settings, chain, rep, log)
    return rep


def render_markdown(rep: VerifyReport) -> str:
    L = [f"# Vérification du réseau `{rep.chain}` (chain id {rep.chain_id}) — {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(rep.ts))}", "",
         f"RPC : `{rep.rpc_host}` · verdict : **{'TOUTES LES VÉRIFICATIONS BLOQUANTES PASSENT' if rep.ok else 'ÉCHEC — ne pas utiliser ce réseau tant que les points KO ne sont pas résolus'}**", ""]
    if rep.network:
        L.append("## Réseau")
        for k, v in rep.network.items():
            L.append(f"- {k} : {v}")
        L.append("")
    L.append("## Vérifications")
    for c in rep.checks:
        L.append(f"- {'✅' if c.ok else ('❌' if c.blocking else '⚠️')} `{c.name}` — {c.detail}")
    if rep.providers:
        L += ["", "## Fournisseurs de flash loan (capacité en direct)"]
        for k, v in rep.providers.items():
            L.append(f"- {k} `{v['address']}` : frais {v['fee_bps']} bps, vérifié={v['verified']}, capacité {v['capacity']}")
    if rep.pools:
        L += ["", "## Pools découverts (profondeur en USD, 30 premiers)", "", "| pool | DEX | paire | frais (ppm) | profondeur $ |", "|---|---|---|---|---|"]
        for r in rep.pools[:30]:
            L.append(f"| `{r['address'][:10]}…` | {r['dex']} | {r['pair']}{' (stable)' if r['stable'] else ''} | {r['fee_ppm']} | {r['depth_usd'] if r['depth_usd'] is not None else 'inconnu'} |")
    L += ["", f"Empreinte de configuration : `{rep.config_digest}` (toute modification des adresses exige une nouvelle vérification)."]
    return "\n".join(L)


def _write(settings: Settings, chain: ChainConfig, rep: VerifyReport, log=print) -> None:
    reports = REPO_ROOT / "docs" / "reports"
    reports.mkdir(parents=True, exist_ok=True)
    stamp = time.strftime("%Y%m%d-%H%M%S", time.localtime(rep.ts))
    (reports / f"verify_chain_{chain.id}_{stamp}.json").write_text(json.dumps(rep.as_dict(), indent=1, default=str))
    (reports / f"verify_chain_{chain.id}_{stamp}.md").write_text(render_markdown(rep))
    settings.data_dir.mkdir(parents=True, exist_ok=True)
    vf = verified_file(settings, chain)
    if rep.ok:
        vf.write_text(json.dumps({"ok": True, "ts": rep.ts, "config_digest": rep.config_digest, "rpc_host": rep.rpc_host,
                                  "pools": len(rep.pools), "network": rep.network, "providers": rep.providers}, indent=1, default=str))
    elif vf.exists():
        vf.unlink()  # a failed verification revokes the previous one
    log(f"report: {reports / f'verify_chain_{chain.id}_{stamp}.md'}")
