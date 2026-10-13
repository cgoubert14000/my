"""Ghost-session report: everything the engine observed on a network, written as JSON + Markdown + CSV.

Used by `arbbot ghost --report-dir …` (and the GitHub Actions real-market job). Nothing here is synthetic: the
figures are the live pool states, prices, gas and candidates of the session, stamped with block numbers so that any
line can be checked against a block explorer.
"""
from __future__ import annotations

import csv
import datetime as dt
import json
import pathlib
import time
from typing import Any

from ..core.types import DexKind


def _fmt(x: Any, nd: int = 4) -> str:
    if x is None:
        return "—"
    if isinstance(x, float):
        return f"{x:,.{nd}f}"
    return str(x)


def _json_safe(o: Any) -> Any:
    if isinstance(o, dict):
        return {str(k): _json_safe(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return [_json_safe(v) for v in o]
    if isinstance(o, int) and abs(o) > 2**53:
        return str(o)
    if hasattr(o, "name") and hasattr(o, "value"):  # enums
        return o.name
    return o


def pool_rows(rt) -> list[dict]:
    rows = []
    for p in rt.pools:
        x, y = p.liquidity_hint()
        px0 = rt.fees.token_price_usd(p.token0) or 0.0
        px1 = rt.fees.token_price_usd(p.token1) or 0.0
        usd = x / 10**p.token0.decimals * px0 + y / 10**p.token1.decimals * px1
        price = None
        try:
            if p.kind in (DexKind.UNIV3, DexKind.PANCAKE_V3) and p.v3 is not None:
                from ..core.math_v3 import price_from_sqrt

                price = price_from_sqrt(p.v3.sqrt_price_x96, p.token0.decimals, p.token1.decimals)
            elif x and y:
                price = (y / 10**p.token1.decimals) / (x / 10**p.token0.decimals)
        except Exception:  # noqa: BLE001
            price = None
        rows.append({
            "address": p.address, "dex": p.dex, "kind": p.kind.name, "fee_ppm": p.fee_ppm, "stable": p.stable,
            "pair": f"{p.token0.symbol}/{p.token1.symbol}", "token0": p.token0.address, "token1": p.token1.address,
            "reserve0": str(x), "reserve1": str(y), "depth_usd": round(usd, 2),
            "price_token1_per_token0": price, "updated_block": p.updated_block,
            "quarantined": p.quarantined, "quarantine_reason": p.quarantine_reason,
        })
    rows.sort(key=lambda r: -r["depth_usd"])
    return rows


def build(rt, *, started_at: float, started_block: int, extra: dict | None = None) -> dict:
    st = rt.status()
    since = started_at
    opps = rt.db.opportunities(limit=20000, since=since)
    sims = [o for o in opps if o.get("sim_ok") is not None]
    labeled = [o for o in opps if o.get("ghost_next_block_net") is not None]
    positives = [o for o in opps if (o.get("expected_net") is not None and int(o["expected_net"]) > 0)]
    best = sorted(positives, key=lambda o: -(o.get("expected_net_eur") or 0))[:25]
    decisions: dict[str, int] = {}
    reasons: dict[str, int] = {}
    for o in opps:
        decisions[o.get("decision") or "?"] = decisions.get(o.get("decision") or "?", 0) + 1
        for r in o.get("reasons") or []:
            key = r.split(":")[0].split("(")[0]
            reasons[key] = reasons.get(key, 0) + 1
    now = time.time()
    rep = {
        "kind": "ghost_session",
        "generated_at": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
        "chain": st["chain"],
        "is_devnet": st["chain"].get("is_devnet"),
        "duration_min": round((now - started_at) / 60, 2),
        "blocks": {"first": started_block, "last": rt.last_block, "seen": st["collector"].get("blocks_seen")},
        "rpc": st["rpc"], "collector": st["collector"], "gas": st["gas"],
        "native_price_usd": st.get("native_price_usd"),
        "flash_providers": {k.name if hasattr(k, "name") else str(k): {"fee_bps": v.fee_bps_x100 / 100, "verified": v.verified,
                                                                        "capacity": {t: str(c) for t, c in getattr(v, "capacity", {}).items()}}
                            for k, v in rt.fees.providers.items()},
        "pools": pool_rows(rt),
        "routes": st.get("routes"),
        "detector": st["detector"],
        "ghost": st["ghost"],
        "reliability": st["reliability"],
        "risk": st["risk"],
        "opportunities": {"total": len(opps), "positive_expected_net": len(positives), "simulated": len(sims),
                          "sim_ok": sum(1 for o in sims if o.get("sim_ok")), "sim_failed": sum(1 for o in sims if o.get("sim_ok") is False),
                          "ghost_labeled": len(labeled), "ghost_positive": sum(1 for o in labeled if int(o["ghost_next_block_net"]) > 0),
                          "decisions": decisions, "reject_reasons": reasons, "best": best},
        "extra": extra or {},
    }
    return _json_safe(rep)


def render_markdown(rep: dict) -> str:
    ch = rep["chain"]
    devnet = bool(rep.get("is_devnet"))
    lines = [
        f"# Session ghost — {ch.get('name')} (chain id {ch.get('chain_id')})",
        "",
        ("**⚠️ DEVNET LOCAL — aucune donnée de marché réelle.**" if devnet else
         f"**Réseau réel** — RPC `{ch.get('rpc_host')}` — adresses vérifiées en direct : {ch.get('verified')}"),
        f"Généré le {rep['generated_at']} ; durée {rep['duration_min']} min ; blocs {rep['blocks']['first']} → {rep['blocks']['last']} "
        f"({rep['blocks']['seen']} vus)",
        "",
        "## Connexion",
        f"- Requêtes RPC : {rep['rpc'].get('requests')} ; erreurs : {rep['rpc'].get('errors')} ; latence p50/p95 : "
        f"{_fmt(rep['rpc'].get('latency_p50_ms'), 1)}/{_fmt(rep['rpc'].get('latency_p95_ms'), 1)} ms",
        f"- Rafraîchissements d'état : {rep['collector'].get('refreshes')} ; âge des données au dernier bloc : {rep['collector'].get('block_age_s')} s",
        f"- Gaz : base fee {_fmt(rep['gas'].get('base_fee_gwei'), 6)} gwei ; prix ETH (pool le plus profond) : {_fmt(rep.get('native_price_usd'), 2)} $",
        f"- Fournisseurs de flash loan : " + ", ".join(f"{k} {v['fee_bps']} bps (vérifié={v['verified']})" for k, v in rep["flash_providers"].items()),
        "",
        f"## Pools suivis ({len(rep['pools'])}) — état au bloc indiqué",
        "",
        "| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |",
        "|---|---|---:|---:|---:|---:|---|",
    ]
    for p in rep["pools"][:60]:
        lines.append(f"| {p['dex']} | {p['pair']}{' (stable)' if p['stable'] else ''} | {p['fee_ppm']} | {p['depth_usd']:,.0f} | "
                     f"{_fmt(p['price_token1_per_token0'], 6)} | {p['updated_block']} | `{p['address']}` |")
    o = rep["opportunities"]
    d = rep["detector"]
    lines += [
        "",
        "## Recherche d'opportunités",
        f"- Cycles : {d.get('cycles')} ; routes examinées : {d.get('routes_screened')} ; candidats optimisés : {d.get('candidates')} ; "
        f"net attendu > 0 : {d.get('positive_net')} ; dernier cycle {d.get('last_cycle_ms')} ms",
        f"- Rejets (moteur) : {d.get('rejections')}",
        f"- Enregistrements de la session : {o['total']} ; net attendu > 0 : {o['positive_expected_net']} ; simulés (eth_call de la vraie tx) : "
        f"{o['simulated']} (ok {o['sim_ok']}, échec {o['sim_failed']}) ; étiquettes ghost N+1 : {o['ghost_positive']}/{o['ghost_labeled']} positives",
        f"- Décisions : {o['decisions']} ; motifs de rejet : {o['reject_reasons']}",
        "",
        "## Meilleures opportunités de la session (net attendu, toutes charges déduites)",
        "",
        "| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |",
        "|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|",
    ]
    for b in o["best"]:
        dec = b.get("token_decimals") or 18
        tok = b.get("token")

        def amt(v):
            return "—" if v is None else f"{int(v) / 10**dec:,.6f} {tok}"

        fees = b.get("fees") or {}
        lines.append(f"| {b.get('block_number')} | {b.get('route')} | {amt(b.get('amount_in'))} | {amt(b.get('gross_profit'))} | "
                     f"{amt(fees.get('flash_fee'))} | {amt(fees.get('gas_cost_token'))} | {amt(b.get('expected_net'))} ({_fmt(b.get('expected_net_eur'), 4)} €) | "
                     f"{amt(b.get('simulated_net'))} | {_fmt(b.get('margin_bps'), 2)} | {_fmt(b.get('p_lower'), 3)} (n={b.get('p_n')}) | {b.get('decision')} | "
                     f"{', '.join(b.get('reasons') or [])} |")
    r = rep["reliability"]
    rk = rep["risk"]
    lines += [
        "",
        "## Fiabilité et décision",
        f"- Observations ghost : {r.get('n')} ; taux observé {_fmt(r.get('rate'), 3)} ; borne inférieure crédible ({r.get('credible_level')}) "
        f"{_fmt(r.get('global_lower'), 3)} ; seuil {r.get('threshold')} → **{r.get('label')}**",
        f"- Statut de maturité : **{rk.get('status')}** — {rk.get('sub_status')}",
        "- Critères : " + "; ".join(f"{'✅' if c['ok'] else '❌'} {c['name']}" for c in rk.get("criteria", [])),
        "",
        "Fichiers : `*.json` (tout l'état), `*_opportunities.csv` (chaque candidat avec toutes les colonnes de coût).",
    ]
    if not devnet:
        lines += ["", "Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule)."]
    return "\n".join(lines) + "\n"


def write(rt, out_dir: pathlib.Path, *, started_at: float, started_block: int, tag: str, extra: dict | None = None) -> dict[str, str]:
    out_dir.mkdir(parents=True, exist_ok=True)
    rep = build(rt, started_at=started_at, started_block=started_block, extra=extra)
    base = out_dir / f"ghost_{rt.chain.id}_{tag}"
    (base.with_suffix(".json")).write_text(json.dumps(rep, indent=1, ensure_ascii=False))
    (base.with_suffix(".md")).write_text(render_markdown(rep))
    opps = rt.db.opportunities(limit=20000, since=started_at)
    cols = ["ts", "block_number", "route", "token", "flash_source", "amount_in", "amount_out", "gross_profit", "expected_net", "expected_net_eur",
            "simulated_net", "ghost_next_block_net", "margin_bps", "price_impact_bps", "spread_bps", "p_success", "p_lower", "p_upper", "p_n",
            "ev", "decision", "reasons", "sim_ok", "sim_error", "sim_gas_used", "data_age_ms", "uncertainty", "dexes", "pools"]
    fee_cols = ["flash_fee", "swap_fees", "gas_units", "gas_price_wei", "l1_data_fee_wei", "gas_cost_wei", "gas_cost_token", "failure_cost_wei", "unknowns"]
    csv_path = out_dir / f"ghost_{rt.chain.id}_{tag}_opportunities.csv"
    with csv_path.open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(cols + [f"fee_{c}" for c in fee_cols])
        for o in reversed(opps):
            fees = o.get("fees") or {}
            w.writerow([json.dumps(o.get(c), ensure_ascii=False) if isinstance(o.get(c), (list, dict)) else o.get(c) for c in cols]
                       + [json.dumps(fees.get(c)) if isinstance(fees.get(c), (list, dict)) else fees.get(c) for c in fee_cols])
    return {"json": str(base.with_suffix(".json")), "md": str(base.with_suffix(".md")), "csv": str(csv_path)}
