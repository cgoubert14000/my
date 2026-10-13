#!/usr/bin/env python
"""Real-market ghost session, end to end, on a machine that can reach the chain (your PC or a GitHub Actions runner).

1. tries every RPC URL given (public endpoints by default) with the `verify-chain` pre-flight (chain id, head
   freshness, Multicall3, eth_call state override, code at every configured address, token metadata, factories…);
2. keeps the first endpoint that passes every blocking check AND supports state-override simulation, the other
   healthy ones become fallbacks; writes the full verification report (docs/reports/verify_chain_<chain>_*.md);
3. writes `.env` for that endpoint (never any secret) and runs `arbbot ghost` for the requested duration with reports
   in docs/reports/real/.

Nothing is simulated locally: every number comes from the live network. No transaction is ever signed here.
Usage: python scripts/real_market_session.py --chain base --minutes 30 [--rpc URL ...] [--max-rps 12]
"""
from __future__ import annotations

import argparse
import asyncio
import json
import os
import pathlib
import subprocess
import sys
import time

REPO = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "backend"))

PUBLIC_RPCS = {
    "base": [
        "https://base-rpc.publicnode.com",
        "https://mainnet.base.org",
        "https://base.llamarpc.com",
        "https://base.drpc.org",
        "https://1rpc.io/base",
        "https://base-mainnet.public.blastapi.io",
        "https://base.meowrpc.com",
        "https://base.blockpi.network/v1/rpc/public",
        "https://endpoints.omniatech.io/v1/base/mainnet/public",
        "https://base.gateway.tenderly.co",
    ],
    "arbitrum": [
        "https://arbitrum-one-rpc.publicnode.com",
        "https://arb1.arbitrum.io/rpc",
        "https://arbitrum.llamarpc.com",
        "https://arbitrum.drpc.org",
        "https://1rpc.io/arb",
        "https://arbitrum-one.public.blastapi.io",
    ],
}


def host(u: str) -> str:
    return u.split("//")[-1].split("/")[0]


# Known WebSocket endpoints (newHeads subscription → block-driven refresh instead of polling)
WS_FOR_HOST = {
    "base-rpc.publicnode.com": "wss://base-rpc.publicnode.com",
    "base.drpc.org": "wss://base.drpc.org",
    "base-mainnet.public.blastapi.io": "wss://base-mainnet.public.blastapi.io",
    "base.gateway.tenderly.co": "wss://base.gateway.tenderly.co",
    "arbitrum-one-rpc.publicnode.com": "wss://arbitrum-one-rpc.publicnode.com",
    "arbitrum.drpc.org": "wss://arbitrum.drpc.org",
    "arbitrum-one.public.blastapi.io": "wss://arbitrum-one.public.blastapi.io",
}


async def test_ws(url: str, timeout: float = 15.0) -> tuple[bool, str]:
    """Subscribe to newHeads and wait for one real head."""
    try:
        import websockets
    except ImportError:
        return False, "websockets not installed"
    try:
        async with websockets.connect(url, open_timeout=timeout, ping_interval=None, max_size=2**22) as ws:
            await ws.send('{"jsonrpc":"2.0","id":1,"method":"eth_subscribe","params":["newHeads"]}')
            t0 = time.time()
            while time.time() - t0 < timeout:
                raw = await asyncio.wait_for(ws.recv(), timeout=timeout)
                msg = json.loads(raw)
                head = (msg.get("params") or {}).get("result") or {}
                if "number" in head:
                    return True, f"head {int(head['number'], 16)} after {time.time() - t0:.1f} s"
            return False, "no head received"
    except Exception as e:  # noqa: BLE001
        return False, repr(e)


async def preflight(chain: str, urls: list[str], max_rps: float, log) -> tuple[str | None, list[str], list[dict]]:
    from arbbot.config.settings import Settings
    from arbbot.ops.verify import verify_chain

    results = []
    healthy: list[str] = []
    chosen: str | None = None
    for u in urls:
        s = Settings(chain=chain, rpc_http_url=u, rpc_fallback_http_urls="", rpc_max_rps=max_rps, rpc_timeout_s=15)
        t0 = time.time()
        try:
            rep = await asyncio.wait_for(verify_chain(s, discover_pools=False, write=False, log=lambda *_: None), timeout=120)
        except Exception as e:  # noqa: BLE001
            log(f"[preflight] {host(u)}: EXCEPTION {e!r}")
            results.append({"url": u, "ok": False, "error": repr(e)})
            continue
        checks = {c.name: c for c in rep.checks}
        so = checks.get("eth_call_state_override")
        failed = [c.name for c in rep.checks if c.blocking and not c.ok]
        info = {"url": u, "ok": rep.ok, "state_override": bool(so and so.ok), "failed_blocking": failed,
                "latency_p50_ms": rep.network.get("latency_p50_ms"), "head_age_s": rep.network.get("head_age_s"),
                "seconds": round(time.time() - t0, 1)}
        results.append(info)
        log(f"[preflight] {host(u)}: ok={rep.ok} state_override={info['state_override']} p50={info['latency_p50_ms']} ms "
            f"head_age={info['head_age_s']} s failed={failed}")
        if rep.ok:
            healthy.append(u)
            if chosen is None and info["state_override"]:
                chosen = u
    return chosen, healthy, results


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--chain", default="base", choices=sorted(PUBLIC_RPCS))
    ap.add_argument("--minutes", type=float, default=30)
    ap.add_argument("--rpc", action="append", default=[], help="RPC URL(s) to try first (your own provider key, never committed)")
    ap.add_argument("--ws", default="", help="WebSocket URL (newHeads); auto-detected for known public endpoints")
    ap.add_argument("--on-snapshot", default=os.environ.get("ARB_SNAPSHOT_HOOK", ""), help="command run after each snapshot (publish)")
    ap.add_argument("--max-rps", type=float, default=12)
    ap.add_argument("--report-dir", default=str(REPO / "docs" / "reports" / "real"))
    ap.add_argument("--snapshot-every", type=float, default=2)
    ap.add_argument("--tag", default="")
    ap.add_argument("--preflight-only", action="store_true")
    args = ap.parse_args()

    def log(msg: str) -> None:
        print(msg, flush=True)

    urls = list(dict.fromkeys(args.rpc + [u for u in os.environ.get("ARB_RPC_CANDIDATES", "").split(",") if u.strip()] + PUBLIC_RPCS[args.chain]))
    log(f"=== real-market session: chain={args.chain} minutes={args.minutes} candidates={[host(u) for u in urls]}")
    chosen, healthy, results = asyncio.run(preflight(args.chain, urls, args.max_rps, log))
    report_dir = pathlib.Path(args.report_dir)
    report_dir.mkdir(parents=True, exist_ok=True)
    tag = args.tag or time.strftime("%Y%m%d-%H%M%S", time.gmtime())
    (report_dir / f"rpc_preflight_{args.chain}_{tag}.json").write_text(json.dumps(results, indent=1))
    if chosen is None:
        log("!!! no RPC endpoint passed the pre-flight with state-override support; nothing to run (and nothing invented)")
        return 2
    fallbacks = [u for u in healthy if u != chosen]
    log(f"=== chosen RPC: {host(chosen)} ; fallbacks: {[host(u) for u in fallbacks]}")
    ws_url = args.ws or WS_FOR_HOST.get(host(chosen), "")
    if ws_url:
        ok, detail = asyncio.run(test_ws(ws_url))
        log(f"=== websocket {host(ws_url)}: {'OK' if ok else 'KO'} ({detail})")
        if not ok:
            ws_url = ""

    env_lines = [
        "# generated by scripts/real_market_session.py — no secrets",
        f"ARB_CHAIN={args.chain}",
        f"ARB_RPC_HTTP_URL={chosen}",
        f"ARB_RPC_FALLBACK_HTTP_URLS={','.join(fallbacks)}",
        f"ARB_RPC_WS_URL={ws_url}",
        f"ARB_RPC_MAX_RPS={args.max_rps}",
        "ARB_RPC_TIMEOUT_S=15",
        "ARB_POLL_INTERVAL_S=0.5",
        "ARB_SIMULATE_WITH_STATE_OVERRIDE=true",
        "ARB_LOG_LEVEL=INFO",
    ]
    (REPO / ".env").write_text("\n".join(env_lines) + "\n")
    env = {**os.environ, "ARB_CHAIN": args.chain, "ARB_RUN_TAG": tag, "ARB_RPC_HTTP_URL": chosen, "ARB_RPC_FALLBACK_HTTP_URLS": ",".join(fallbacks),
           "ARB_RPC_WS_URL": ws_url, "ARB_RPC_MAX_RPS": str(args.max_rps), "ARB_RPC_TIMEOUT_S": "15", "ARB_POLL_INTERVAL_S": "0.5"}
    py = sys.executable
    log("=== full verify-chain (pools, depth, flash-loan capacity) on the chosen endpoint")
    r = subprocess.run([py, "-m", "arbbot.cli", "verify-chain"], cwd=REPO, env=env)
    if r.returncode != 0:
        log("!!! verify-chain failed on the chosen endpoint; aborting")
        return 3
    if args.preflight_only:
        return 0
    log(f"=== ghost session {args.minutes} min (read-only, every candidate recorded)")
    cmd = [py, "-m", "arbbot.cli", "ghost", "--minutes", str(args.minutes), "--report-dir", str(report_dir),
           "--snapshot-every", str(args.snapshot_every), "--tag", tag]
    if args.on_snapshot:
        cmd += ["--on-snapshot", args.on_snapshot]
    r = subprocess.run(cmd, cwd=REPO, env=env)
    return r.returncode


if __name__ == "__main__":
    raise SystemExit(main())
