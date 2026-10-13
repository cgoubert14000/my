#!/usr/bin/env python3
"""Cross-session summary of the REAL market sessions (docs/reports/real/ghost_<chain>_<run>.json → sessions.md/json).

Run by ops/real/publish.sh at every snapshot, so the table always includes the session in progress (latest_<chain>.json
when its tag is not final yet). Nothing is computed here beyond sums of what the sessions reported.
"""
from __future__ import annotations

import json
import pathlib
import re
import sys
import time

REAL = pathlib.Path(__file__).resolve().parents[1] / "docs" / "reports" / "real"


def load(path: pathlib.Path) -> dict | None:
    try:
        return json.loads(path.read_text())
    except (OSError, ValueError):
        return None


def row(d: dict, final: bool) -> dict:
    o = d.get("opportunities", {})
    det = d.get("detector", {})
    rel = d.get("reliability", {})
    col = d.get("collector", {})
    u = d.get("universe", {})
    return {
        "run": d.get("tag"), "final": final, "generated_at": d.get("generated_at"), "duration_min": d.get("duration_min"),
        "blocks_seen": (d.get("blocks") or {}).get("seen"), "pools": u.get("pools") or len(d.get("pools") or []),
        "tokens": u.get("tokens"), "routes": d.get("routes"), "cycle_ms": det.get("last_cycle_ms"),
        "candidates": o.get("total"), "positive_expected_net": o.get("positive_expected_net"),
        "simulated": o.get("simulated"), "sim_ok": o.get("sim_ok"), "sim_failed": o.get("sim_failed"),
        "ghost_labeled": o.get("ghost_labeled"), "ghost_positive": o.get("ghost_positive"),
        "reliability_n": rel.get("n"), "reliability_lower": rel.get("global_lower"), "status": (d.get("risk") or {}).get("status"),
        "ws": col.get("ws_connected"), "rpc_errors": (d.get("rpc") or {}).get("errors"), "fee_changes": col.get("fee_changes"),
        "quarantined": len(u.get("quarantined") or []), "eth_usd": d.get("native_price_usd"),
    }


def main() -> int:
    chain = sys.argv[1] if len(sys.argv) > 1 else "base"
    rows: dict[str, dict] = {}
    for f in sorted(REAL.glob(f"ghost_{chain}_*.json")):
        m = re.match(rf"ghost_{chain}_(\d+)\.json$", f.name)
        if not m:
            continue
        d = load(f)
        if d:
            d.setdefault("tag", m.group(1))  # older reports did not carry their tag
            rows[m.group(1)] = row(d, True)
    latest = load(REAL / f"latest_{chain}.json")
    if latest and str(latest.get("tag")) not in rows:
        rows[str(latest.get("tag"))] = row(latest, False)
    ordered = [rows[k] for k in sorted(rows, key=lambda k: int(k) if k.isdigit() else 0)]
    tot = {k: sum((r.get(k) or 0) for r in ordered) for k in
           ("duration_min", "blocks_seen", "candidates", "positive_expected_net", "simulated", "sim_ok", "sim_failed", "ghost_labeled", "ghost_positive")}
    out = {"chain": chain, "generated_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "sessions": ordered, "totals": tot}
    (REAL / f"sessions_{chain}.json").write_text(json.dumps(out, indent=1, ensure_ascii=False))
    L = [f"# Sessions de marché réel — {chain} (généré {out['generated_at']})", "",
         "Chaque ligne vient du rapport final de la session (`ghost_<chain>_<run>.json`) ; la session en cours vient de `latest_<chain>.json`.",
         "Aucune transaction n'a été signée : « simulées » = eth_call du contrat sur l'état réel ; « ghost N+1 » = re-simulation au bloc suivant.", "",
         "| Run | Fin | Durée (min) | Blocs | Pools / jetons / routes | Cycle (ms) | Candidats | Net attendu > 0 | Simulées ok / échec | Ghost N+1 + / n | Fiabilité n / borne inf. | Statut |",
         "|---|---|---:|---:|---|---:|---:|---:|---:|---:|---:|---|"]
    for r in ordered:
        lo = r["reliability_lower"]
        L.append(f"| [{r['run']}](https://github.com/cgoubert14000/my/actions/runs/{r['run']}){'' if r['final'] else ' (en cours)'} | {r['generated_at']} | "
                 f"{(r['duration_min'] or 0):.0f} | {r['blocks_seen'] or 0} | {r['pools'] or 0} / {r['tokens'] or '—'} / {r['routes'] or 0} | {r['cycle_ms'] or 0:.0f} | "
                 f"{r['candidates'] or 0} | {r['positive_expected_net'] or 0} | {r['sim_ok'] or 0} / {r['sim_failed'] or 0} | {r['ghost_positive'] or 0} / {r['ghost_labeled'] or 0} | "
                 f"{r['reliability_n'] or 0} / {('%.1f %%' % (lo * 100)) if lo is not None else '—'} | {r['status'] or '—'} |")
    L += ["", f"**Totaux** : {tot['duration_min']:.0f} min, {tot['blocks_seen']} blocs, {tot['candidates']} candidats, {tot['positive_expected_net']} à net attendu > 0, "
          f"{tot['sim_ok']} simulations réussies / {tot['sim_failed']} échouées, {tot['ghost_positive']}/{tot['ghost_labeled']} étiquettes N+1 positives.", "",
          "Décision de maturité : elle n'est jamais prise sur cette table mais par le moteur (≥ 30 observations par segment, borne inférieure ≥ 75 %) ; "
          "tant que le statut est APPRENTISSAGE / FIABILITÉ INSUFFISANTE, aucun passage en réel n'est proposé."]
    (REAL / f"sessions_{chain}.md").write_text("\n".join(L) + "\n")
    print(f"sessions summary: {len(ordered)} sessions → {REAL / f'sessions_{chain}.md'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
