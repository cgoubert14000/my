"""Ligne de commande : `orbbot fetch | backtest | live | policy-check`."""
from __future__ import annotations

import asyncio
import datetime as dt
import json
import os
import pathlib
import sys
import time

import typer

from .strategy.orb import Costs
from .strategy.params import FULL_GRID, QUICK_GRID, VIDEO_CLAIM, OrbParams, grid

app = typer.Typer(add_completion=False, help="ORB / Opening Range Breakout : backtest exhaustif et exécution temps réel.")


def _costs(instrument: str, spread: float | None, slippage: float | None) -> Costs:
    from .data.dukascopy import INSTRUMENTS
    m = INSTRUMENTS.get(instrument, {"spread": 0.0, "slippage": 0.0})
    sp = m["spread"] if spread is None else spread
    sl = m["slippage"] if slippage is None else slippage
    return Costs(spread=sp, slippage=sl, min_risk=sp)


def _load(instrument: str, start: dt.date, end: dt.date, data_dir: pathlib.Path, synthetic: bool):
    if synthetic:
        from .data.synthetic import random_walk_minutes
        return random_walk_minutes(start, (end - start).days + 1, seed=42)
    from .data.dukascopy import load_minutes
    return load_minutes(instrument, start, end, data_dir, progress=True)


def _variant_from_key(key: str) -> OrbParams:
    for p in grid(FULL_GRID):
        if p.key() == key:
            return p
    if VIDEO_CLAIM.key() == key:
        return VIDEO_CLAIM
    raise typer.BadParameter(f"variante inconnue : {key}")


@app.command()
def fetch(instrument: str = "XAUUSD", start: str = "2022-01-01", end: str = "", data_dir: pathlib.Path = pathlib.Path("data/orb")):
    """Télécharge (cache local) les bougies 1 min Dukascopy."""
    end_d = dt.date.fromisoformat(end) if end else dt.date.today() - dt.timedelta(days=1)
    df = _load(instrument, dt.date.fromisoformat(start), end_d, data_dir, False)
    typer.echo(f"{instrument}: {len(df)} bougies 1 min de {df.index.min()} à {df.index.max()}" if len(df) else f"{instrument}: aucune donnée")


@app.command()
def backtest(instrument: str = "XAUUSD", start: str = "2022-01-01", end: str = "", grid_name: str = typer.Option("full", "--grid"),
             spread: float | None = None, slippage: float | None = None, split: float = 0.6,
             out: pathlib.Path = pathlib.Path("docs/reports/orb"), tag: str = "", data_dir: pathlib.Path = pathlib.Path("data/orb"),
             workers: int = 0, synthetic: bool = typer.Option(False, help="données SYNTHÉTIQUES (démo hors ligne, résultats sans valeur)")):
    """Exécute toute la grille de variantes et écrit le rapport (Markdown + JSON + CSV des trades)."""
    from .backtest.engine import prepare_sessions, run_grid, run_variants
    from .backtest.report import evaluate, write_outputs
    from .backtest.metrics import summarize
    t0 = time.time()
    end_d = dt.date.fromisoformat(end) if end else dt.date.today() - dt.timedelta(days=1)
    df = _load(instrument, dt.date.fromisoformat(start), end_d, data_dir, synthetic)
    if df.empty:
        typer.echo("aucune donnée : backtest impossible (rien n'est inventé)", err=True)
        raise typer.Exit(2)
    sessions = prepare_sessions(df)
    costs = _costs(instrument, spread, slippage)
    spec = {"full": FULL_GRID, "quick": QUICK_GRID}[grid_name]
    variants = grid(spec)
    if VIDEO_CLAIM.key() not in {p.key() for p in variants}:
        variants.append(VIDEO_CLAIM)
    typer.echo(f"{instrument}: {len(df)} bougies, {len(sessions)} séances NY ({sessions[0].day} → {sessions[-1].day}), {len(variants)} variantes, coûts {costs}")
    results = run_grid(sessions, variants, costs, workers=workers or None, progress=lambda d, n: typer.echo(f"  lot {d}/{n}", err=True))
    days = [s.day for s in sessions]
    ev = evaluate(results, variants, days, split_share=split)
    # sensibilité aux coûts : variante sélectionnée + variante « vidéo », spread ×1,5 et ×2
    sens = []
    keys = [k for k in [ev["selected"]["key"] if ev["selected"] else None, VIDEO_CLAIM.key()] if k]
    for k in dict.fromkeys(keys):
        p = _variant_from_key(k)
        for mult in (1.0, 1.5, 2.0):
            c2 = Costs(costs.spread * mult, costs.slippage * mult, costs.min_risk)
            tr = run_variants(sessions, [p], c2)[k]
            sens.append({"key": k, "spread": round(c2.spread, 6), "slippage": round(c2.slippage, 6), "summary": summarize(tr)})
    tag = tag or dt.datetime.now(dt.UTC).strftime("%Y%m%d-%H%M%S")
    note = ("DONNÉES SYNTHÉTIQUES (marche aléatoire) : démonstration du pipeline uniquement, aucun résultat n'a de valeur." if synthetic
            else f"Source : Dukascopy 1 min BID, {len(df)} bougies téléchargées le {dt.date.today().isoformat()}.")
    md, js = write_outputs(ev, instrument if not synthetic else f"SYNTHETIC-{instrument}", {"spread": costs.spread, "slippage": costs.slippage}, out, tag, results, sens, note)
    typer.echo(f"rapport : {md} ({time.time() - t0:.0f} s) — verdict : {ev['status']}")
    if ev["selected"]:
        s = ev["selected"]
        typer.echo(f"sélection {s['key']} : OOS n={s['oos']['n']} WR={s['oos']['win_rate']} PF={s['oos']['profit_factor']}")


@app.command("policy-check")
def policy_check(policy: pathlib.Path = pathlib.Path("ops/orb/policy.json")):
    """Valide la politique de risque et affiche son empreinte."""
    from .live.policy import RiskPolicy
    p = RiskPolicy.load(policy)
    typer.echo(json.dumps({"sha256": p.sha256(), **p.model_dump()}, ensure_ascii=False, indent=1))
    _variant_from_key(p.variant)
    typer.echo("variante connue ✔")


@app.command()
def live(policy: pathlib.Path = pathlib.Path("ops/orb/policy.json"), broker: str = typer.Option("paper", help="paper | oanda | replay"),
         journal_dir: pathlib.Path = pathlib.Path("docs/reports/orb/live"), practice: bool = True, poll_seconds: float = 5.0,
         replay_start: str = "", replay_end: str = "", data_dir: pathlib.Path = pathlib.Path("data/orb"), max_minutes: int = 0,
         repo_root: pathlib.Path = pathlib.Path("."), verbose: bool = True):
    """Moteur temps réel. `--broker paper` : flux OANDA réel (compte de démonstration, OANDA_TOKEN requis) mais exécution
    fictive ; `--broker oanda` : ordres réels sur le compte OANDA (OANDA_TOKEN + OANDA_ACCOUNT_ID) ; `--broker replay` :
    rejeu de l'historique local."""
    from .live.brokers import OandaBroker, PaperBroker
    from .live.engine import LiveEngine
    from .live.feeds import OandaFeed, ReplayFeed
    from .live.policy import RiskPolicy
    pol = RiskPolicy.load(policy)
    params = _variant_from_key(pol.variant)
    costs = _costs(pol.data_instrument, None, None)
    jd = journal_dir / (os.environ.get("ORB_RUN_TAG") or dt.datetime.now(dt.UTC).strftime("%Y%m%d-%H%M%S"))
    stop_at = (dt.datetime.now(dt.UTC) + dt.timedelta(minutes=max_minutes)) if max_minutes else None
    if broker == "replay":
        from .data.dukascopy import load_minutes
        end_d = dt.date.fromisoformat(replay_end) if replay_end else dt.date.today() - dt.timedelta(days=1)
        start_d = dt.date.fromisoformat(replay_start) if replay_start else end_d - dt.timedelta(days=30)
        df = load_minutes(pol.data_instrument, start_d, end_d, data_dir)
        feed, brk = ReplayFeed(df), PaperBroker(pol.paper_equity)
    else:
        token = os.environ.get("OANDA_TOKEN", "")
        if not token:
            typer.echo("OANDA_TOKEN absent : impossible de recevoir des prix en temps réel (créer un compte de démonstration OANDA, "
                       "générer un jeton API, puis `set OANDA_TOKEN=...`).", err=True)
            raise typer.Exit(2)
        feed = OandaFeed(token, pol.instrument, practice=practice, poll_seconds=poll_seconds, stop_at=stop_at)
        if broker == "oanda":
            account = os.environ.get("OANDA_ACCOUNT_ID", "")
            if not account:
                typer.echo("OANDA_ACCOUNT_ID absent", err=True)
                raise typer.Exit(2)
            if pol.mode not in ("oanda_practice", "oanda_live") or (pol.mode == "oanda_live" and not practice):
                typer.echo(f"politique mode={pol.mode} : exécution réelle refusée avec --broker oanda / practice={practice}", err=True)
                raise typer.Exit(3)
            brk = OandaBroker(token, account, practice=practice, price_precision=3 if "XAU" in pol.instrument else 5)
        else:
            brk = PaperBroker(pol.paper_equity)
    eng = LiveEngine(params=params, costs=costs, policy=pol, broker=brk, journal_dir=jd, repo_root=repo_root, verbose=verbose)

    async def main():
        closes = await feed.warmup(600) if params.ma else []
        eng.warmup(closes)
        await eng.run(feed)
        if hasattr(feed, "aclose"):
            await feed.aclose()
    asyncio.run(main())
    typer.echo(f"journal : {jd}")


if __name__ == "__main__":  # pragma: no cover
    sys.exit(app())
