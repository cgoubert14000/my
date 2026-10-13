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
def verify_chain(no_pools: bool = typer.Option(False, help="skip pool discovery / depth measurement")):
    """Verify the configured chain on the connected RPC: addresses, tokens, factories, flash-loan capacity, pools,
    L1 fee oracle, RPC features. Writes docs/reports/verify_chain_<chain>_<ts>.md and data/verified_<chain>.json."""
    from .ops.verify import verify_chain as _verify

    s = get_settings()
    _logging("WARNING")
    rep = asyncio.run(_verify(s, discover_pools=not no_pools, log=typer.echo))
    for c in rep.checks:
        typer.echo(f"{'OK ' if c.ok else ('KO ' if c.blocking else 'WARN')} {c.name:28s} {c.detail}")
    for k, v in rep.network.items():
        typer.echo(f"    {k}: {v}")
    typer.echo(f"\n{'ALL BLOCKING CHECKS PASSED' if rep.ok else 'SOME BLOCKING CHECKS FAILED'} — chain={rep.chain} ({rep.chain_id}) rpc={rep.rpc_host} pools={len(rep.pools)}")
    raise typer.Exit(code=0 if rep.ok else 1)


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


@app.command("executor-plan")
def executor_plan(owner: str = typer.Option("", help="owner address (cold wallet recommended); default = policy wallet"),
                  min_depth_usd: float = typer.Option(20_000.0, help="only allow pools at least this deep (from the last verify-chain report)")):
    """Write the exact deployment + allowlist commands (forge/cast, signed by YOUR keystore, never by the engine) for
    the FlashArbExecutor on the configured chain, from the last `verify-chain` report and authorization.json."""
    import glob

    from .config.chains import get_chain
    from .config.policy import load_policy

    s = get_settings()
    chain = get_chain(s.chain, s.devnet_deployments)
    reports = sorted(glob.glob(str(REPO_ROOT / "docs" / "reports" / f"verify_chain_{chain.id}_*.json")))
    if not reports:
        typer.echo("no verify-chain report for this chain — run `arbbot verify-chain` first")
        raise typer.Exit(1)
    rep = json.loads(pathlib.Path(reports[-1]).read_text())
    if not rep.get("ok"):
        typer.echo(f"last verification FAILED ({reports[-1]}) — fix it before deploying anything")
        raise typer.Exit(1)
    try:
        pol = load_policy(s.policy_path)
    except Exception as e:  # noqa: BLE001
        typer.echo(f"authorization.json unreadable ({e}) — run `arbbot policy-example` and fill it first")
        raise typer.Exit(1) from e
    exec_wallet = pol.wallet_address
    owner = owner or exec_wallet
    allowed_dex = set(pol.allowed_dexes)
    pools = [p for p in rep.get("pools", []) if (p.get("depth_usd") or 0) >= min_depth_usd and p["dex"] in allowed_dex and not p.get("quarantined")]
    tokens = [chain.tokens[t] for t in pol.allowed_tokens if t in chain.tokens]
    caps = [int(pol.tokens[t.symbol].max_borrow * 10**t.decimals) if t.symbol in pol.tokens and pol.tokens[t.symbol].max_borrow else 0 for t in tokens]
    providers = [p.address for p in chain.flash_providers if p.source.name in pol.allowed_flash_providers]
    rpc = "%RPC%" if True else s.rpc_http_url
    lines = [f"# Plan de déploiement et de configuration de FlashArbExecutor — {chain.name} ({chain.chain_id})", "",
             f"Source : {pathlib.Path(reports[-1]).name} · politique `{pol.digest()}` · {len(pools)} pools ≥ {min_depth_usd:,.0f} $ dans les DEX autorisés", "",
             "Toutes les commandes se signent avec VOTRE keystore de propriétaire (`keystores\\owner.json`, créé par `cast wallet new keystores` ou `arbbot make-keystore --out keystores\\owner.json`). Le moteur n'intervient pas.", "",
             "```powershell", f'$env:RPC = "{s.rpc_http_url}"', 'cd contracts', "forge build",
             f'forge create src/FlashArbExecutor.sol:FlashArbExecutor --rpc-url $env:RPC --keystore ..\\keystores\\owner.json --broadcast --constructor-args {owner} {exec_wallet}',
             '# → noter "Deployed to: 0x..." puis :', '$env:EX = "0xADRESSE_DEPLOYEE"',
             f'cast send $env:EX "setGuardian(address)" {exec_wallet} --rpc-url $env:RPC --keystore ..\\keystores\\owner.json',
             f'cast send $env:EX "setTokens(address[],bool,uint256[])" "[{",".join(t.address for t in tokens)}]" true "[{",".join(str(c) for c in caps)}]" --rpc-url $env:RPC --keystore ..\\keystores\\owner.json',
             f'cast send $env:EX "setProviders(address[],bool)" "[{",".join(providers)}]" true --rpc-url $env:RPC --keystore ..\\keystores\\owner.json']
    for i in range(0, len(pools), 40):
        chunk = pools[i : i + 40]
        lines.append(f'cast send $env:EX "setPools(address[],bool)" "[{",".join(p["address"] for p in chunk)}]" true --rpc-url $env:RPC --keystore ..\\keystores\\owner.json')
    lines += ['# vérifications', 'cast call $env:EX "paused()(bool)" --rpc-url $env:RPC', f'cast call $env:EX "isExecutor(address)(bool)" {exec_wallet} --rpc-url $env:RPC',
              "```", "", "Ensuite : `ARB_EXECUTOR_ADDRESS=<adresse>` dans `.env`, `executor_contract` dans authorization.json, puis `arbbot verify-chain` à nouveau (vérifie le code du contrat).", "",
              "## Pools autorisés", "", "| adresse | DEX | paire | frais ppm | profondeur $ |", "|---|---|---|---|---|"]
    lines += [f"| `{p['address']}` | {p['dex']} | {p['pair']} | {p['fee_ppm']} | {p['depth_usd']} |" for p in pools]
    out = REPO_ROOT / "docs" / "reports" / f"executor_plan_{chain.id}.md"
    out.write_text("\n".join(lines))
    typer.echo("\n".join(lines[:20]))
    typer.echo(f"\n… plan complet écrit dans {out}")


@app.command("emergency-stop")
def emergency_stop(api: str = typer.Option("http://127.0.0.1:8000")):
    """Trigger the kill switch on a running engine via the API."""
    import httpx

    r = httpx.post(f"{api}/api/control/emergency-stop", json={"reason": "cli"}, timeout=5)
    typer.echo(r.text)


if __name__ == "__main__":
    app()
