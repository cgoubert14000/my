"""Command line: `arbbot <command>` (installed by `pip install -e backend`)."""
from __future__ import annotations

import asyncio
import json
import logging
import pathlib
import time

import typer

from .config.settings import REPO_ROOT, get_settings

app = typer.Typer(help="Flash-loan arbitrage bot — ghost/simulation first, limited live only under a signed policy.", no_args_is_help=True)


def _logging(level: str | None = None) -> None:
    logging.basicConfig(level=level or get_settings().log_level, format="%(asctime)s %(levelname)s %(name)s: %(message)s")


@app.command()
def serve(host: str = typer.Option(None), port: int = typer.Option(None)):
    """Start the engine (collector, detector, ghost mode, risk manager) and the HTTP/WebSocket API."""
    import uvicorn

    from .api.server import create_app

    s = get_settings()
    _logging()
    uvicorn.run(create_app(s), host=host or s.api_host, port=port or s.api_port, log_level="warning")


@app.command()
def signer():
    """Start the isolated signer service (separate process; holds the key; enforces authorization.json itself)."""
    from .signer.service import main

    main()


@app.command()
def ghost(minutes: float = typer.Option(0, help="0 = run until Ctrl-C")):
    """Headless ghost mode (no API): detect, simulate, label, persist."""
    from .app.runtime import Runtime

    _logging()

    async def _run():
        rt = Runtime(get_settings())
        await rt.start()
        t_end = time.time() + minutes * 60 if minutes else None
        try:
            while t_end is None or time.time() < t_end:
                await asyncio.sleep(5)
                st = rt.status()
                typer.echo(f"block {rt.last_block} | {st['risk']['status']} | candidates {st['detector'].get('candidates')} "
                           f"| ghost {st['ghost']} | rel n={st['reliability'].get('n')}")
        finally:
            await rt.stop()

    asyncio.run(_run())


@app.command()
def lab(minutes: float = typer.Option(60.0), out: pathlib.Path = typer.Option(REPO_ROOT / "docs" / "reports")):
    """Run the autonomous optimisation lab headless (default 60 min) and write the report."""
    from .app.runtime import Runtime
    from .lab.runner import LabRunner

    _logging()

    async def _run():
        rt = Runtime(get_settings())
        await rt.start()
        try:
            res = await LabRunner(rt, total_minutes=minutes, reports_dir=out).run()
            typer.echo(json.dumps({"files": res.get("report_files"), "phases": list(res["phases"].keys())}, indent=1))
        finally:
            await rt.stop()

    asyncio.run(_run())


@app.command("verify-chain")
def verify_chain():
    """Verify configured addresses on the connected RPC (code present, factories/pools answer) — prints a report."""
    from .config.chains import get_chain
    from .data.rpc import RpcClient, RpcError, decode_result, encode_call

    s = get_settings()
    _logging("WARNING")
    chain = get_chain(s.chain, s.devnet_deployments)

    async def _run():
        rpc = RpcClient(s.rpc_http_url, s.fallback_urls, s.rpc_timeout_s, s.rpc_max_rps, chain.multicall3)
        await rpc.open()
        rows = []
        try:
            cid = int(await rpc.request("eth_chainId"), 16)
            rows.append(("chain_id", str(cid), cid == chain.chain_id))
            for name, addr in [("multicall3", chain.multicall3), ("wrapped_native", chain.wrapped_native)] + \
                    [(f"dex:{d.id}", d.factory) for d in chain.dexes if d.factory] + \
                    [(f"flash:{p.source.name}", p.address) for p in chain.flash_providers] + \
                    [(f"token:{k}", t.address) for k, t in chain.tokens.items()]:
                try:
                    code = await rpc.get_code(addr)
                    ok = len(code) > 0
                    extra = f"{len(code)} bytes"
                    if name.startswith("token:") and ok:
                        raw = await rpc.call(addr, encode_call("decimals()"))
                        extra += f", decimals={decode_result(['uint8'], raw)[0]}"
                except RpcError as e:
                    ok, extra = False, str(e)
                rows.append((name, f"{addr} ({extra})", ok))
        finally:
            await rpc.close()
        allok = all(r[2] for r in rows)
        for n, v, ok in rows:
            typer.echo(f"{'OK ' if ok else 'KO '} {n:22s} {v}")
        typer.echo(f"\n{'ALL VERIFIED' if allok else 'SOME CHECKS FAILED'} — chain={chain.id}")
        return allok

    ok = asyncio.run(_run())
    raise typer.Exit(code=0 if ok else 1)


@app.command("policy-example")
def policy_example(out: pathlib.Path = typer.Option(REPO_ROOT / "authorization.example.json")):
    """Write authorization.example.json (disabled by default)."""
    from .config.policy import EXAMPLE

    out.write_text(json.dumps(EXAMPLE, indent=2))
    typer.echo(f"wrote {out}")


@app.command("policy-check")
def policy_check():
    """Validate authorization.json and show its summary (never prints secrets — there are none in it)."""
    from .config.policy import load_policy

    s = get_settings()
    p = load_policy(s.policy_path)
    typer.echo(json.dumps(p.summary(), indent=2, default=str))


@app.command("make-keystore")
def make_keystore(out: pathlib.Path = typer.Option(REPO_ROOT / "keystores" / "executor.json")):
    """Generate a NEW dedicated hot wallet and save it as an encrypted keystore (password prompted, never stored)."""
    import getpass

    from eth_account import Account

    pw = getpass.getpass("Keystore password: ")
    pw2 = getpass.getpass("Repeat: ")
    if pw != pw2 or len(pw) < 10:
        typer.echo("passwords differ or shorter than 10 characters")
        raise typer.Exit(1)
    acct = Account.create()
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(Account.encrypt(acct.key, pw)))
    typer.echo(f"new wallet {acct.address} → {out}\nFund it ONLY with the gas budget you accept to lose. Put this address in authorization.json (wallet_address).")


@app.command("emergency-stop")
def emergency_stop(api: str = typer.Option("http://127.0.0.1:8000")):
    """Trigger the kill switch on a running engine via the API."""
    import httpx

    r = httpx.post(f"{api}/api/control/emergency-stop", json={"reason": "cli"}, timeout=5)
    typer.echo(r.text)


if __name__ == "__main__":
    app()
