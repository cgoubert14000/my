#!/usr/bin/env python3
"""« Bot memecoin » : vérification sur données réelles (lecture seule, aucun secret, aucune transaction).

Question posée par l'opérateur : un bot qui achète les nouveaux jetons dès leur lancement peut-il avoir ≥ 75 % de
réussite ? Au lieu d'une opinion, ce script mesure sur les N derniers jours d'une chaîne :

1. toutes les paires créées (événements `PairCreated` Uniswap V2 / `PoolCreated` Aerodrome) dont un côté est WETH ;
2. pour chaque paire, la série complète des réserves (événements `Sync`) : liquidité initiale, pic, liquidité actuelle ;
   → « rug » = liquidité WETH finale < 10 % du pic (retrait de liquidité) ;
3. le P&L EXACT (maths V2, frais 0,3 %) d'un sniper naïf qui achète `--buy-eth` ETH 2 blocs après la création et
   revend après 1 h, 6 h, 24 h (ou à la dernière réserve connue si le pool meurt avant), gaz inclus.

Limites, annoncées : les honeypots (vente bloquée), taxes de transfert et listes noires NE SONT PAS détectés ici —
ils ne peuvent que dégrader le résultat. Ce rapport est donc une BORNE SUPÉRIEURE de ce qu'un tel bot aurait gagné.
Usage : python scripts/memecoin_reality_check.py --chain base --days 2 [--rpc URL ...] [--max-pairs 300]
"""
from __future__ import annotations

import argparse
import asyncio
import json
import pathlib
import random
import statistics
import sys
import time

REPO = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "backend"))

from arbbot.data.rpc import RpcClient, RpcError, event_topic  # noqa: E402

TOPIC_PAIR_CREATED = event_topic("PairCreated(address,address,address,uint256)")
TOPIC_POOL_CREATED_AERO = event_topic("PoolCreated(address,address,bool,address,uint256)")
TOPIC_SYNC_V2 = event_topic("Sync(uint112,uint112)")
TOPIC_SYNC_SOLIDLY = event_topic("Sync(uint256,uint256)")

CHAINS = {
    "base": {
        "chain_id": 8453, "block_time": 2.0, "weth": "0x4200000000000000000000000000000000000006",
        "factories": {"uniswap_v2": ("0x8909Dc15e40173Ff4699343b6eB8132c65e18eC6", TOPIC_PAIR_CREATED),
                      "aerodrome": ("0x420DD381b31aEf6683db6B902084cB0FFECe40Da", TOPIC_POOL_CREATED_AERO)},
        # Historical eth_getLogs on public Base endpoints (measured 2026-10-13): publicnode → "Archive requests require a
        # personal token"; blastapi → 10-block range max; mainnet.base.org → 429; drpc free → ≤ 10 000-block range.
        # drpc is therefore the only usable free endpoint; an archive URL with a key (ARB_RPC_ARCHIVE_URL / --rpc)
        # is used first when present.
        "rpcs": ["https://base.drpc.org"],
    },
}


def _addr(topic_or_word: str) -> str:
    return "0x" + topic_or_word[-40:]


def v2_out(amount_in: int, r_in: int, r_out: int, fee_ppm: int = 3000) -> int:
    if amount_in <= 0 or r_in <= 0 or r_out <= 0:
        return 0
    a = amount_in * (1_000_000 - fee_ppm)
    return a * r_out // (r_in * 1_000_000 + a)


async def get_logs_chunked(rpc: RpcClient, params: dict, start: int, end: int, chunk: int, floor: int = 1_000) -> list[dict]:
    """eth_getLogs over [start, end] in windows of `chunk` blocks; a provider error halves the window down to `floor`
    (public endpoints cap the range at 2 000–10 000 blocks), beyond which the error is raised to the caller."""
    out: list[dict] = []
    b = start
    while b <= end:
        e = min(end, b + chunk - 1)
        try:
            out.extend(await rpc.get_logs({**params, "fromBlock": hex(b), "toBlock": hex(e)}))
            b = e + 1
        except RpcError as ex:
            if chunk > floor:
                chunk = max(floor, chunk // 2)
                await asyncio.sleep(0.5)
                continue
            raise ex
    return out


async def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--chain", default="base")
    ap.add_argument("--days", type=float, default=1.0)
    ap.add_argument("--rpc", action="append", default=[])
    ap.add_argument("--max-pairs", type=int, default=150)
    ap.add_argument("--buy-eth", type=float, default=0.005, help="taille d'achat du sniper simulé (ETH)")
    ap.add_argument("--max-rps", type=float, default=4.0, help="eth_getLogs est coûteux : rester bas sur RPC public")
    ap.add_argument("--chunk", type=int, default=2_000, help="fenêtre eth_getLogs (blocs)")
    ap.add_argument("--out-dir", default=str(REPO / "docs" / "reports" / "real"))
    ap.add_argument("--tag", default="")
    ap.add_argument("--devnet", default="", help="chemin deployments.local.json (test local)")
    ap.add_argument("--eth-usd", type=float, default=0.0)
    args = ap.parse_args()

    if args.devnet:
        dep = json.loads(pathlib.Path(args.devnet).read_text())
        cfg = {"chain_id": dep["chain_id"], "block_time": 2.0, "weth": dep["native_wrapped"],
               "factories": {k: (v, TOPIC_PAIR_CREATED) for k, v in dep["v2_factories"].items()}, "rpcs": [dep["rpc"]]}
        chain = "local"
    else:
        chain = args.chain
        cfg = CHAINS[chain]
    import os

    rpcs = args.rpc or ([os.environ["ARB_RPC_ARCHIVE_URL"]] if os.environ.get("ARB_RPC_ARCHIVE_URL") else []) + cfg["rpcs"]
    weth = cfg["weth"].lower()
    buy_wei = int(args.buy_eth * 1e18)
    t_start = time.time()

    async with RpcClient(rpcs[0], rpcs[1:], timeout_s=20, max_rps=args.max_rps) as rpc:
        head = await rpc.block_number()
        span = int(args.days * 86400 / cfg["block_time"])
        start = max(1, head - span)
        head_block = await rpc.get_block(head)
        head_ts = int(head_block["timestamp"], 16)
        base_fee = int(head_block.get("baseFeePerGas", "0x0"), 16)
        gas_cost_wei = 2 * 160_000 * max(base_fee, 1)  # achat + vente, ~160 k gaz chacun, priorité négligeable sur L2

        # 1) paires créées -----------------------------------------------------------------------------------
        created: list[dict] = []
        for dex, (factory, topic) in cfg["factories"].items():
            try:
                logs = await get_logs_chunked(rpc, {"address": factory, "topics": [topic]}, start, head, args.chunk, floor=500)
            except RpcError as ex:
                out_dir = pathlib.Path(args.out_dir)
                out_dir.mkdir(parents=True, exist_ok=True)
                tag = args.tag or time.strftime("%Y%m%d-%H%M%S", time.gmtime())
                msg = (f"# Bot memecoin — vérification impossible sur RPC public ({chain})\n\n"
                       f"Généré le {time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}. Les journaux historiques (`eth_getLogs` sur {args.days:g} j) "
                       f"ne sont pas servis par les points d'accès publics essayés ({', '.join(rpcs)}) : `{ex}`.\n\n"
                       "Aucun chiffre n'est inventé à la place. Pour exécuter la mesure, fournir une URL RPC d'archive avec clé gratuite "
                       "(Alchemy, Infura, QuickNode…) dans le secret GitHub `RPC_ARCHIVE_URL_BASE` (ou `--rpc URL` en local).\n")
                (out_dir / f"memecoin_check_{chain}_{tag}.md").write_text(msg)
                print(msg)
                return 2
            for lg in logs:
                t0, t1 = _addr(lg["topics"][1]).lower(), _addr(lg["topics"][2]).lower()
                if weth not in (t0, t1):
                    continue
                data = lg["data"][2:]
                if topic == TOPIC_PAIR_CREATED:
                    pair = "0x" + data[24:64]
                else:  # Aerodrome: data = (address pool, uint256 n), stable in topics[3]
                    if int(lg["topics"][3], 16) == 1:
                        continue  # stable pools (x³y+xy³) : pas la formule V2, et pas des memecoins
                    pair = "0x" + data[24:64]
                created.append({"dex": dex, "pair": pair.lower(), "token": t1 if t0 == weth else t0, "weth_is_0": t0 == weth,
                                "block": int(lg["blockNumber"], 16)})
        n_created = len(created)
        created.sort(key=lambda c: c["block"])
        if len(created) > args.max_pairs:  # échantillon uniforme dans le temps (pas seulement les plus récentes)
            step = len(created) / args.max_pairs
            created = [created[int(i * step)] for i in range(args.max_pairs)]

        # 2) séries de réserves + 3) P&L exact du sniper -----------------------------------------------------
        results: list[dict] = []
        sync_topic = {"uniswap_v2": TOPIC_SYNC_V2, "sushiswap": TOPIC_SYNC_V2, "aerodrome": TOPIC_SYNC_SOLIDLY}
        horizons = {"1h": 3600, "6h": 6 * 3600, "24h": 24 * 3600}
        for i, c in enumerate(created):
            try:
                logs = await get_logs_chunked(rpc, {"address": c["pair"], "topics": [sync_topic.get(c["dex"], TOPIC_SYNC_V2)]},
                                              c["block"], head, max(args.chunk, 10_000))
            except RpcError as ex:
                results.append({**c, "error": str(ex)})
                continue
            series = []
            for lg in logs:
                d = bytes.fromhex(lg["data"][2:])
                if len(d) < 64:
                    continue
                r0, r1 = int.from_bytes(d[:32], "big"), int.from_bytes(d[32:64], "big")
                rw, rt = (r0, r1) if c["weth_is_0"] else (r1, r0)
                series.append((int(lg["blockNumber"], 16), rw, rt))
            if not series:
                results.append({**c, "no_liquidity": True})
                continue
            peak_w = max(s[1] for s in series)
            last_b, last_w, last_t = series[-1]
            first_b, first_w, first_t = series[0]
            rec = {**c, "syncs": len(series), "first_weth": first_w / 1e18, "peak_weth": peak_w / 1e18, "last_weth": last_w / 1e18,
                   "age_h": round((head - c["block"]) * cfg["block_time"] / 3600, 2),
                   "rug": last_w < 0.1 * peak_w or last_w < 10**16, "pnl": {}}
            # entrée : première réserve connue au moins 2 blocs après la création
            entry = next((s for s in series if s[0] >= c["block"] + 2), None)
            if entry is None or entry[1] < 10**16:
                rec["skipped"] = "pas de liquidité exploitable 2 blocs après la création"
                results.append(rec)
                continue
            eb, ew, et = entry
            tokens = v2_out(buy_wei, ew, et)
            # réserves après notre achat (le prix que nous payons déplace le pool)
            ew2, et2 = ew + buy_wei, et - tokens
            for name, secs in horizons.items():
                target = eb + int(secs / cfg["block_time"])
                if target > head:
                    rec["pnl"][name] = None  # horizon pas encore atteint
                    continue
                # dernière réserve connue avant l'horizon, en tenant compte de notre propre achat si rien n'a bougé
                sw, st = ew2, et2
                for b, w, t in series:
                    if b <= eb:
                        continue
                    if b > target:
                        break
                    sw, st = w, t
                out_wei = v2_out(tokens, st, sw)
                rec["pnl"][name] = (out_wei - buy_wei - gas_cost_wei) / 1e18
            results.append(rec)
            if (i + 1) % 25 == 0:
                print(f"  {i + 1}/{len(created)} paires analysées", flush=True)

    # ---------------------------------------------------------------- agrégats
    analysed = [r for r in results if "pnl" in r and "skipped" not in r]
    rugs = [r for r in results if r.get("rug")]
    summary: dict = {"chain": chain, "chain_id": cfg["chain_id"], "generated_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                     "window_days": args.days, "blocks": [start, head], "head_ts": head_ts, "pairs_created_with_weth": n_created,
                     "pairs_sampled": len(created), "pairs_analysed": len(analysed), "pairs_without_liquidity": sum(1 for r in results if r.get("no_liquidity")),
                     "pairs_skipped": sum(1 for r in results if r.get("skipped")), "errors": sum(1 for r in results if r.get("error")),
                     "rug_count": len(rugs), "rug_rate": (len(rugs) / len([r for r in results if "syncs" in r])) if any("syncs" in r for r in results) else None,
                     "buy_eth": args.buy_eth, "gas_cost_eth": gas_cost_wei / 1e18, "eth_usd": args.eth_usd or None, "horizons": {}}
    for name in ("1h", "6h", "24h"):
        vals = [r["pnl"][name] for r in analysed if r["pnl"].get(name) is not None]
        if not vals:
            summary["horizons"][name] = {"n": 0}
            continue
        wins = sum(1 for v in vals if v > 0)
        summary["horizons"][name] = {"n": len(vals), "win_rate": wins / len(vals), "total_eth": sum(vals), "median_eth": statistics.median(vals),
                                     "mean_eth": statistics.fmean(vals), "best_eth": max(vals), "worst_eth": min(vals),
                                     "p90_eth": sorted(vals)[int(0.9 * (len(vals) - 1))],
                                     "lost_more_than_half": sum(1 for v in vals if v < -0.5 * args.buy_eth) / len(vals)}
    med_first = statistics.median([r["first_weth"] for r in results if "first_weth" in r]) if any("first_weth" in r for r in results) else None
    summary["median_initial_liquidity_weth"] = med_first

    tag = args.tag or time.strftime("%Y%m%d-%H%M%S", time.gmtime())
    out_dir = pathlib.Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / f"memecoin_check_{chain}_{tag}.json").write_text(json.dumps({"summary": summary, "pairs": results}, indent=1))

    def eth(v: float | None, usd: float | None = None) -> str:
        if v is None:
            return "—"
        s = f"{v:+.5f} ETH"
        if usd:
            s += f" ({v * usd:+.2f} $)"
        return s

    usd = args.eth_usd or None
    L = [f"# Bot memecoin — vérification sur données réelles ({chain}, {args.days:g} j)", "",
         f"Généré le {summary['generated_at']} ; blocs {start} → {head} ; lecture seule, aucune transaction.", "",
         "**Méthode** : toutes les paires WETH/jeton créées sur Uniswap V2 et Aerodrome (volatiles) dans la fenêtre ; réserves reconstituées "
         "depuis les événements `Sync` ; P&L exact (maths V2, frais 0,3 %, gaz inclus) d'un sniper qui achète "
         f"{args.buy_eth:g} ETH 2 blocs après la création et revend à 1 h / 6 h / 24 h (ou à la dernière liquidité connue si le pool meurt avant).",
         "**Ce qui n'est PAS compté et ne peut qu'empirer le résultat** : honeypots (vente impossible), taxes de transfert, listes noires, "
         "concurrence des autres snipers dans le même bloc. Les chiffres ci-dessous sont donc une **borne supérieure**.", "",
         "## Résultats", "",
         f"- Paires WETH/jeton créées : **{n_created}** ; analysées : {len(analysed)} (échantillon {len(created)}, sans liquidité : "
         f"{summary['pairs_without_liquidity']}, inexploitables : {summary['pairs_skipped']}, erreurs RPC : {summary['errors']})",
         f"- Liquidité initiale médiane : {med_first:.3f} WETH" if med_first is not None else "- Liquidité initiale médiane : —",
         f"- **Retraits de liquidité (« rug », liquidité finale < 10 % du pic) : {len(rugs)} soit {100 * (summary['rug_rate'] or 0):.1f} %**", "",
         "| Horizon de revente | n | Trades gagnants | P&L total | Médiane | Moyenne | Meilleur | Pire | Perte > 50 % |",
         "|---|---:|---:|---:|---:|---:|---:|---:|---:|"]
    for name, h in summary["horizons"].items():
        if h.get("n"):
            L.append(f"| {name} | {h['n']} | **{100 * h['win_rate']:.1f} %** | {eth(h['total_eth'], usd)} | {eth(h['median_eth'], usd)} | "
                     f"{eth(h['mean_eth'], usd)} | {eth(h['best_eth'], usd)} | {eth(h['worst_eth'], usd)} | {100 * h['lost_more_than_half']:.1f} % |")
        else:
            L.append(f"| {name} | 0 | — | — | — | — | — | — | — |")
    L += ["", "## Lecture", "",
          "- « Trades gagnants » est le taux de réussite réel d'un tel bot sur la période, avant honeypots et taxes. À comparer au seuil de 75 % demandé.",
          "- Le P&L total est ce qu'aurait gagné (ou perdu) un bot qui aurait pris **toutes** les occasions de la fenêtre ; la médiane dit ce qui arrive au trade typique.",
          "- Un taux de rug élevé signifie que la plupart des lancements sont conçus pour prendre l'argent des acheteurs : aucun filtre « rapide » ne change l'espérance.",
          "", f"Fichier détaillé : `memecoin_check_{chain}_{tag}.json` (une ligne par paire : liquidité initiale/pic/finale, rug, P&L par horizon)."]
    (out_dir / f"memecoin_check_{chain}_{tag}.md").write_text("\n".join(L) + "\n")
    print(json.dumps(summary, indent=1))
    print(f"→ {out_dir / f'memecoin_check_{chain}_{tag}.md'} ({time.time() - t_start:.0f} s)")
    return 0


if __name__ == "__main__":
    sys.exit(asyncio.run(main()))
