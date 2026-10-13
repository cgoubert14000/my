"""Validation honnête d'une grille de variantes : in-sample / out-of-sample, walk-forward, bootstrap, biais de sélection."""
from __future__ import annotations

import datetime as dt
import json
import math
import pathlib
from collections import defaultdict

import numpy as np

from ..strategy.orb import Trade
from ..strategy.params import VIDEO_CLAIM, OrbParams
from .metrics import bootstrap_ci, by_year, monthly_r, summarize

MIN_TRADES_SELECT = 50     # trades in-sample minimum pour qu'une variante soit candidate
MIN_TRADES_OOS = 100       # en dessous : « FIABILITÉ NON DÉMONTRÉE » quoi qu'il arrive


def _fmt(x, nd=2, suffix=""):
    if x is None:
        return "—"
    if isinstance(x, float):
        if math.isinf(x):
            return "∞"
        return f"{x:.{nd}f}{suffix}"
    return f"{x}{suffix}"


def _pct(x):
    return "—" if x is None else f"{100 * x:.1f} %"


def split_day(days: list[str], share: float) -> str:
    return days[min(len(days) - 1, int(len(days) * share))]


def evaluate(results: dict[str, list[Trade]], variants: list[OrbParams], days: list[str], split_share: float = 0.6,
             claim: OrbParams | None = VIDEO_CLAIM) -> dict:
    cut = split_day(days, split_share)
    rows = []
    for p in variants:
        tr = results.get(p.key(), [])
        is_tr = [t for t in tr if t.day < cut]
        oos_tr = [t for t in tr if t.day >= cut]
        rows.append({"key": p.key(), "params": p.as_dict(), "describe": p.describe(),
                     "all": summarize(tr, "total"), "is": summarize(is_tr, "in-sample"), "oos": summarize(oos_tr, "out-of-sample")})
    eligible = [r for r in rows if r["is"]["n"] >= MIN_TRADES_SELECT and r["is"]["profit_factor"] is not None]
    ranked_is = sorted(eligible, key=lambda r: -(r["is"]["profit_factor"] if math.isfinite(r["is"]["profit_factor"]) else 1e9))
    top_is = ranked_is[:10]
    oos_pfs = np.array([r["oos"]["profit_factor"] for r in rows if r["oos"]["n"] >= 20 and r["oos"]["profit_factor"] is not None and math.isfinite(r["oos"]["profit_factor"])])
    is_pfs = np.array([r["is"]["profit_factor"] for r in eligible if math.isfinite(r["is"]["profit_factor"])])
    # corrélation de rang IS/OOS parmi les variantes éligibles ayant ≥ 20 trades OOS
    pairs = [(r["is"]["profit_factor"], r["oos"]["profit_factor"]) for r in eligible
             if r["oos"]["n"] >= 20 and r["oos"]["profit_factor"] is not None and math.isfinite(r["is"]["profit_factor"]) and math.isfinite(r["oos"]["profit_factor"])]
    rank_corr = None
    if len(pairs) >= 10:
        a = np.array(pairs)
        ra, rb = a[:, 0].argsort().argsort(), a[:, 1].argsort().argsort()
        rank_corr = float(np.corrcoef(ra, rb)[0, 1])
    selected = top_is[0] if top_is else None
    sel_boot = bootstrap_ci([t for t in results[selected["key"]] if t.day >= cut]) if selected else None
    sel_boot_all = bootstrap_ci(results[selected["key"]]) if selected else None
    claim_row = None
    if claim is not None and claim.key() in results:
        claim_row = next(r for r in rows if r["key"] == claim.key())
        claim_row = {**claim_row, "boot_all": bootstrap_ci(results[claim.key()]), "boot_oos": bootstrap_ci([t for t in results[claim.key()] if t.day >= cut]),
                     "by_year": by_year(results[claim.key()])}
    wf = walk_forward(results, variants)
    status, reasons = verdict(selected, sel_boot, wf)
    return {
        "generated_at": dt.datetime.now(dt.UTC).isoformat(timespec="seconds"),
        "days": {"n": len(days), "first": days[0], "last": days[-1], "split_day": cut, "is_days": sum(1 for d in days if d < cut), "oos_days": sum(1 for d in days if d >= cut)},
        "variants": len(variants),
        "eligible_variants": len(eligible),
        "top_in_sample": top_is,
        "selected": selected, "selected_boot_oos": sel_boot, "selected_boot_all": sel_boot_all,
        "selected_by_year": by_year(results[selected["key"]]) if selected else {},
        "selected_monthly_r": monthly_r(results[selected["key"]]) if selected else {},
        "oos_distribution": {"n": int(oos_pfs.size), "share_pf_above_1": float(np.mean(oos_pfs > 1)) if oos_pfs.size else None,
                             "median_pf": float(np.median(oos_pfs)) if oos_pfs.size else None,
                             "is_median_pf": float(np.median(is_pfs)) if is_pfs.size else None, "rank_corr_is_oos": rank_corr},
        "best_oos_hindsight": sorted([r for r in rows if r["oos"]["n"] >= MIN_TRADES_SELECT and r["oos"]["profit_factor"] is not None],
                                     key=lambda r: -(r["oos"]["profit_factor"] if math.isfinite(r["oos"]["profit_factor"]) else 1e9))[:5],
        "claim": claim_row,
        "walk_forward": wf,
        "status": status,
        "status_reasons": reasons,
        "all_rows": rows,
    }


def walk_forward(results: dict[str, list[Trade]], variants: list[OrbParams], min_train: int = 30) -> dict:
    """Chaque année N : on retient la variante au meilleur PF sur les années < N (≥ min_train trades) et on
    l'applique en aveugle à l'année N. Le total est ce qu'une sélection automatique aurait réellement produit."""
    years = sorted({t.day[:4] for tr in results.values() for t in tr})
    steps = []
    chained: list[Trade] = []
    for y in years[1:]:
        best_key, best_pf, best_n = None, -1.0, 0
        for p in variants:
            train = [t for t in results.get(p.key(), []) if t.day[:4] < y]
            if len(train) < min_train:
                continue
            s = summarize(train)
            pf = s["profit_factor"]
            pf = pf if math.isfinite(pf) else 99.0
            if pf > best_pf:
                best_key, best_pf, best_n = p.key(), pf, len(train)
        if best_key is None:
            continue
        test = [t for t in results[best_key] if t.day[:4] == y]
        chained.extend(test)
        steps.append({"year": y, "variant": best_key, "train_pf": best_pf, "train_n": best_n, "test": summarize(test, y)})
    return {"steps": steps, "total": summarize(chained, "walk-forward"), "boot": bootstrap_ci(chained)}


def verdict(selected: dict | None, boot_oos: dict | None, wf: dict) -> tuple[str, list[str]]:
    reasons = []
    if selected is None:
        return "FIABILITÉ NON DÉMONTRÉE — DONNÉES INSUFFISANTES", ["aucune variante n'atteint le minimum de trades in-sample"]
    oos = selected["oos"]
    if oos["n"] < MIN_TRADES_OOS:
        reasons.append(f"seulement {oos['n']} trades hors échantillon (< {MIN_TRADES_OOS})")
    if oos["profit_factor"] is None or oos["profit_factor"] <= 1.0:
        reasons.append(f"profit factor hors échantillon {_fmt(oos['profit_factor'])} ≤ 1")
    if boot_oos and boot_oos["pf_low"] is not None and boot_oos["pf_low"] <= 1.0:
        reasons.append(f"borne basse (IC 95 %) du PF hors échantillon {_fmt(boot_oos['pf_low'])} ≤ 1")
    wft = wf["total"]
    if wft["n"] < MIN_TRADES_OOS or wft["profit_factor"] is None or wft["profit_factor"] <= 1.0:
        reasons.append(f"walk-forward : {wft['n']} trades, PF {_fmt(wft['profit_factor'])}")
    if reasons:
        return "FIABILITÉ NON DÉMONTRÉE", reasons
    return "ROBUSTESSE PLAUSIBLE HORS ÉCHANTILLON — À CONFIRMER EN PAPER TRADING", ["PF > 1 hors échantillon, IC 95 % au-dessus de 1, walk-forward positif"]


def _row_line(r: dict, which: tuple[str, ...] = ("is", "oos")) -> str:
    cells = [f"`{r['key']}`"]
    for w in which:
        s = r[w]
        cells.append(f"{s['n']} / {_pct(s['win_rate'])} / {_fmt(s['profit_factor'])} / {_fmt(s['expectancy_r'], 3)} / {_fmt(s['max_drawdown_r'], 1)}")
    return "| " + " | ".join(cells) + " |"


def to_markdown(ev: dict, instrument: str, costs: dict, sensitivity: list[dict] | None = None, data_note: str = "") -> str:
    d = ev["days"]
    L = [f"# Backtest ORB — {instrument}", "",
         f"Généré le {ev['generated_at']} · données : {d['n']} séances New York du {d['first']} au {d['last']} "
         f"(in-sample {d['is_days']} séances < {d['split_day']} ; out-of-sample {d['oos_days']} séances) · "
         f"{ev['variants']} variantes · coûts : spread {costs.get('spread')} , slippage {costs.get('slippage')} (unités de prix, par exécution au marché/stop).", ""]
    if data_note:
        L += [f"> {data_note}", ""]
    L += [f"## Verdict : **{ev['status']}**", ""]
    L += [f"- {x}" for x in ev["status_reasons"]]
    L += ["", f"> Rappel : avec {ev['variants']} variantes testées, la meilleure in-sample paraît toujours excellente même sans aucun avantage réel "
          "(biais de sélection). Seules les colonnes **hors échantillon** et le **walk-forward** sont informatives, et elles restent "
          "des estimations sur un passé limité — pas une promesse de rendement.", ""]
    sel = ev["selected"]
    if sel:
        s_all, s_is, s_oos = sel["all"], sel["is"], sel["oos"]
        b = ev["selected_boot_oos"] or {}
        L += ["## Variante sélectionnée (meilleur profit factor in-sample)", "",
              f"`{sel['key']}` — {sel['describe']}", "",
              "| période | trades | win rate | profit factor | espérance (R) | max DD (R) | plus longue série perdante |", "|---|---|---|---|---|---|---|"]
        for s in (s_is, s_oos, s_all):
            L.append(f"| {s['label']} | {s['n']} | {_pct(s['win_rate'])} | {_fmt(s['profit_factor'])} | {_fmt(s['expectancy_r'], 3)} | {_fmt(s['max_drawdown_r'], 1)} | {s['longest_losing_streak']} |")
        L += ["", f"IC bootstrap 95 % du PF hors échantillon : [{_fmt(b.get('pf_low'))} ; {_fmt(b.get('pf_high'))}] ; "
              f"probabilité (bootstrap) que le PF hors échantillon soit < 1 : {_pct(b.get('p_pf_below_1'))}.", ""]
        if ev["selected_by_year"]:
            L += ["| année | trades | win rate | PF | total R | max DD R |", "|---|---|---|---|---|---|"]
            for y, s in ev["selected_by_year"].items():
                L.append(f"| {y} | {s['n']} | {_pct(s['win_rate'])} | {_fmt(s['profit_factor'])} | {_fmt(s['total_r'], 1)} | {_fmt(s['max_drawdown_r'], 1)} |")
            L.append("")
        if sel["all"].get("exits"):
            L += [f"Sorties (toutes périodes) : {sel['all']['exits']} · longs {sel['all']['longs']} / shorts {sel['all']['shorts']}", ""]
    od = ev["oos_distribution"]
    L += ["## Que valent les 10 meilleures variantes in-sample une fois hors échantillon ?", "",
          "| variante | in-sample : n / WR / PF / esp. R / DD | out-of-sample : n / WR / PF / esp. R / DD |", "|---|---|---|"]
    L += [_row_line(r) for r in ev["top_in_sample"]]
    L += ["", f"Sur l'ensemble des variantes avec ≥ 20 trades hors échantillon ({od['n']}) : PF médian in-sample {_fmt(od['is_median_pf'])}, "
          f"PF médian hors échantillon {_fmt(od['median_pf'])}, part des variantes avec PF hors échantillon > 1 : {_pct(od['share_pf_above_1'])}, "
          f"corrélation de rang IS/OOS : {_fmt(od['rank_corr_is_oos'])} (proche de 0 ⇒ le classement in-sample ne prédit pas la suite).", ""]
    wf = ev["walk_forward"]
    L += ["## Walk-forward (sélection automatique année après année)", "",
          "Chaque année, la variante au meilleur PF sur toutes les années précédentes est appliquée en aveugle à l'année suivante.", "",
          "| année testée | variante retenue (PF / n en apprentissage) | trades | win rate | PF | total R |", "|---|---|---|---|---|---|"]
    for st in wf["steps"]:
        t = st["test"]
        L.append(f"| {st['year']} | `{st['variant']}` ({_fmt(st['train_pf'])} / {st['train_n']}) | {t['n']} | {_pct(t['win_rate'])} | {_fmt(t['profit_factor'])} | {_fmt(t['total_r'], 1)} |")
    t = wf["total"]
    bw = wf["boot"]
    L += [f"| **total** | | {t['n']} | {_pct(t['win_rate'])} | {_fmt(t['profit_factor'])} | {_fmt(t['total_r'], 1)} |", "",
          f"IC bootstrap 95 % du PF walk-forward : [{_fmt(bw.get('pf_low'))} ; {_fmt(bw.get('pf_high'))}].", ""]
    c = ev.get("claim")
    if c:
        L += ["## La variante annoncée dans la vidéo (or, range 30 min, retest FVG, RR 1, « PF ≈ 1,75 »)", "",
              f"`{c['key']}` — {c['describe']}", "",
              "| période | trades | win rate | profit factor | espérance (R) | max DD (R) |", "|---|---|---|---|---|---|"]
        for s in (c["is"], c["oos"], c["all"]):
            L.append(f"| {s['label']} | {s['n']} | {_pct(s['win_rate'])} | {_fmt(s['profit_factor'])} | {_fmt(s['expectancy_r'], 3)} | {_fmt(s['max_drawdown_r'], 1)} |")
        ba = c["boot_all"]
        L += ["", f"IC bootstrap 95 % du PF (toutes périodes) : [{_fmt(ba.get('pf_low'))} ; {_fmt(ba.get('pf_high'))}] — "
              f"probabilité que le vrai PF soit < 1 : {_pct(ba.get('p_pf_below_1'))}.", ""]
        if c.get("by_year"):
            L += ["| année | trades | win rate | PF | total R |", "|---|---|---|---|---|"]
            for y, s in c["by_year"].items():
                L.append(f"| {y} | {s['n']} | {_pct(s['win_rate'])} | {_fmt(s['profit_factor'])} | {_fmt(s['total_r'], 1)} |")
            L.append("")
    if ev["best_oos_hindsight"]:
        L += ["## Meilleures variantes hors échantillon (a posteriori — information, pas sélection)", "",
              "| variante | in-sample : n / WR / PF / esp. R / DD | out-of-sample : n / WR / PF / esp. R / DD |", "|---|---|---|"]
        L += [_row_line(r) for r in ev["best_oos_hindsight"]]
        L.append("")
    if sensitivity:
        L += ["## Sensibilité aux coûts (variante sélectionnée et variante « vidéo »)", "",
              "| variante | spread | slippage | trades | win rate | PF | espérance (R) |", "|---|---|---|---|---|---|---|"]
        for s in sensitivity:
            m = s["summary"]
            L.append(f"| `{s['key']}` | {s['spread']} | {s['slippage']} | {m['n']} | {_pct(m['win_rate'])} | {_fmt(m['profit_factor'])} | {_fmt(m['expectancy_r'], 3)} |")
        L.append("")
    L += ["## Méthode", "",
          "- Bougies 1 minute BID Dukascopy (flux public), séances New York 09:30–16:00 (heure d'été/hiver gérée), journées < 200 bougies ignorées.",
          "- Range = plus haut/plus bas des R premières minutes ; cassure = clôture 1 min au-delà ; entrée au marché à l'ouverture suivante (« close ») "
          "ou limite au bord de la première FVG après cassure (« fvg ») ; aucune entrée après l'heure limite ; tout est clôturé à 15:55 NY.",
          "- Coûts : achat à bid + spread, vente à bid ; slippage sur ordres au marché et stops ; stop prioritaire sur l'objectif dans une même bougie ; "
          "dans la bougie d'entrée seul le stop est vérifié.",
          "- In-sample = premiers 60 % des séances, out-of-sample = 40 % suivants ; sélection par PF in-sample (≥ 50 trades) ; "
          "IC par bootstrap (1 000 rééchantillonnages) ; walk-forward annuel.",
          "- Résultats en R (risque initial par trade) : ils ne dépendent pas de la taille du compte ; aucun rendement en € n'est annoncé.", ""]
    return "\n".join(L)


def write_outputs(ev: dict, instrument: str, costs: dict, out_dir: pathlib.Path, tag: str, results: dict[str, list[Trade]],
                  sensitivity: list[dict] | None = None, data_note: str = "") -> tuple[pathlib.Path, pathlib.Path]:
    out_dir.mkdir(parents=True, exist_ok=True)
    md = out_dir / f"backtest_{instrument}_{tag}.md"
    js = out_dir / f"backtest_{instrument}_{tag}.json"
    md.write_text(to_markdown(ev, instrument, costs, sensitivity, data_note), encoding="utf-8")
    slim = {k: v for k, v in ev.items() if k != "all_rows"}
    slim["all_rows"] = [{"key": r["key"], "is": r["is"], "oos": r["oos"], "all": {k: r["all"][k] for k in ("n", "win_rate", "profit_factor", "expectancy_r", "max_drawdown_r")}} for r in ev["all_rows"]]
    slim["sensitivity"] = sensitivity or []
    slim["instrument"], slim["costs"], slim["tag"] = instrument, costs, tag
    js.write_text(json.dumps(_sanitize(slim), ensure_ascii=False, indent=1), encoding="utf-8")
    keys = []
    if ev["selected"]:
        keys.append(ev["selected"]["key"])
    if ev.get("claim"):
        keys.append(ev["claim"]["key"])
    for k in dict.fromkeys(keys):
        rows = [t.as_dict() for t in results.get(k, [])]
        if rows:
            import csv
            with (out_dir / f"trades_{instrument}_{tag}_{k}.csv").open("w", newline="", encoding="utf-8") as f:
                w = csv.DictWriter(f, fieldnames=list(rows[0]))
                w.writeheader()
                w.writerows(rows)
    (out_dir / f"latest_{instrument}.md").write_text(md.read_text(encoding="utf-8"), encoding="utf-8")
    return md, js


def _sanitize(o):
    """JSON strict : inf/nan → null, types numpy → natifs."""
    if isinstance(o, dict):
        return {str(k): _sanitize(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return [_sanitize(v) for v in o]
    if isinstance(o, (np.floating, np.integer)):
        o = o.item()
    if isinstance(o, float) and (math.isinf(o) or math.isnan(o)):
        return None
    return o
