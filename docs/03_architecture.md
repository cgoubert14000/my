# 03 — Architecture

## Vue d'ensemble

```
            ┌──────────────── RPC (HTTP + WS optionnel, fallbacks, limiteur de débit) ────────────────┐
            │                                                                                          │
   ┌────────▼────────┐   pools   ┌──────────────┐  état/bloc  ┌───────────────┐  candidats  ┌──────────────┐
   │ PoolIndexer     ├──────────►│ StateCollector├────────────►│ Detector      ├────────────►│ Selector     │
   │ (factories ou   │           │ multicall/bloc│             │ routes 2-3    │             │ p_inf, EV,   │
   │  deployments)   │           │ fraîcheur,gaz │             │ optimiseur,   │             │ motifs       │
   └─────────────────┘           └──────┬───────┘             │ FeeCalculator │             └──────┬───────┘
                                        │                     └───────┬───────┘                    │
                                        │                             │ 3 meilleurs                │
                                        │                     ┌───────▼───────┐             ┌──────▼───────┐
                                        │                     │ Simulator     │             │ RiskManager  │
                                        │                     │ eth_call /    │             │ statuts,     │
                                        │                     │ stateOverride │             │ critères,    │
                                        │                     └───────┬───────┘             │ registre     │
                                        │                             │                     └──────┬───────┘
                                 ┌──────▼───────┐             ┌───────▼───────┐                    │ LIVE + policy OK
                                 │ GhostLabeler │────────────►│ Reliability   │             ┌──────▼───────┐    HTTP 127.0.0.1:8787
                                 │ re-sim N+1   │ observations│ Beta-binomial │             │ LiveExecutor ├───────────────► Signer
                                 └──────────────┘             │ + logistique  │             │ pré-vol total│  payload non signé   (processus
                                                              └───────────────┘             └──────────────┘  ◄── tx signée        séparé,
                                                                                                   │                               keystore,
                                                                       SQLite (WAL) ◄──────────────┘ reçus, ledger                politique)
                                      FastAPI /api + /ws ──► Frontend React (dashboard, graphiques, table, contrôles)
                                      LabRunner (60 min) + SelfCorrector (git data/selfcorr)
```

## Modules (`backend/arbbot/`)

| Module | Rôle | Points clés |
|---|---|---|
| `config/settings.py` | variables `ARB_*` (`.env`) | aucun secret ; `chain=local|base|arbitrum` |
| `config/chains.py` | adresses par réseau + **provenance** (`ADDRESS_SOURCES`) | DEX, tokens, fournisseurs flash, oracle L1, `enabled` |
| `config/policy.py` | `AuthorizationPolicy` (gelée) | validité, plafonds, listes, empreinte |
| `config/tunables.py` | paramètres de stratégie modifiables | `ALLOWED_KEYS` = seul périmètre de l'auto-correction |
| `data/rpc.py` | client JSON-RPC asynchrone | retries, bascule de fallback, limiteur, métriques p50/p95, multicall concurrent |
| `data/indexer.py` | découverte des pools | factories (réel) ou `deployments.local.json` (devnet) ; métadonnées on-chain |
| `data/collector.py` | état par bloc | réserves V2, slot0/liquidité/ticks V3, Solidly ; âge des données ; gaz ; prix ETH |
| `core/math_*.py`, `core/pricing.py` | courbes exactes | entiers uniquement ; `QuoteError` si ticks insuffisants |
| `engine/routes.py` | cycles 2–3 sauts | multi-DEX, tokens de départ empruntables |
| `engine/screen.py` | filtre vectorisé par bloc | écart = Σ ±log(prix) par route (numpy), comparé aux frais LP + marge, profondeur réelle min ; ~30 ms pour 192 000 routes |
| `engine/optimizer.py` | montant optimal | grille + nombre d'or, contrainte d'impact |
| `engine/fees.py` | frais flash (lus on-chain), gaz, L1, conversion token | capacité des fournisseurs |
| `engine/detector.py` / `selector.py` | candidats, décisions | motifs, EV, quarantaine de pools |
| `simulation/simulator.py` | `eth_call` de la vraie tx | contrat déployé ou `stateOverride` (bytecode compilé) ; décodage des reverts |
| `reliability/model.py` | probabilité de succès | segments Beta-binomial, logistique holdout, dérive, taille d'échantillon |
| `ghost/labeler.py` | étiquetage N+1 | dédup par route/fenêtre, négatifs conservés |
| `risk/manager.py` | machine à états de maturité | critères vérifiables, suspension, registre |
| `execution/executor.py` | pré-vol + envoi | re-vérification complète, `minProfit`, `minAmountOut`, reçus, reasons |
| `signer/service.py` | processus signer | keystore, politique appliquée, comptabilité propre |
| `storage/db.py` | SQLite WAL | opportunités, observations, exécutions, événements, changements, métriques |
| `app/runtime.py` | orchestration | boucle par bloc, verrou de cycle, flags depuis rapports de tests, vérification réseau |
| `api/server.py` | REST + WebSocket + UI statique | contrôles opérateur, laboratoire |
| `lab/runner.py`, `lab/selfcorr.py` | laboratoire 60 min, auto-correction | A/B sur mêmes blocs, score N+1, git |
| `ops/verify.py` | `verify-chain` | pré-vol complet d'un réseau, empreinte de configuration |
| `cli.py` | commandes | `serve`, `signer`, `ghost`, `lab`, `verify-chain`, `executor-plan`, `policy-*`, `make-keystore`, `emergency-stop` |

## Modes

* **Lecture seule / ghost** : aucun portefeuille ; tout fonctionne (détection, simulation, fiabilité, laboratoire).
* **Réel limité** : + signer + politique + contrat déployé + critères verts ; retour automatique en ghost en cas de
  dégradation.

## Données

SQLite `data/arbbot.sqlite` (WAL). Tables : `opportunities` (toutes les colonnes de coût, décision, motifs, sim,
ghost), `observations` (features, étiquette, source), `executions`, `events`, `changes`, `metrics` (séries
temporelles pour les graphiques), `kv`. Les rapports humains sont dans `docs/reports/`.

## Session de marché réel et publication en continu

`scripts/real_market_session.py` (local ou GitHub Actions) : pré-vol des RPC publics → test de l'abonnement WebSocket
`newHeads` → `.env` sans secret → `arbbot verify-chain` (bloquant) → `arbbot ghost --snapshot-every 2 --on-snapshot
"bash ops/real/publish.sh"`. Toutes les 2 minutes, `ops/ghost_report.py` écrit `ghost_<chain>_<run>.{json,md}`,
`latest_<chain>.{json,md}` (noms stables), une ligne dans `history_<chain>_<run>.jsonl` (série temporelle, un fichier par session), et le crochet
pousse ces fichiers dans la branche (`[skip ci]`, `pull --rebase --autostash`). `docs/live/index.html` (statique,
sans dépendance) lit `latest_<chain>.json` + `history_<chain>_<run>.jsonl` par URL relative — servie par GitHub Pages ou par
`scripts/live_mirror.py` — et affiche l'âge de l'instantané. Le CSV complet (gzip) n'est écrit qu'au rapport final.

## Ajout d'un réseau

1. Ajouter un `ChainConfig` dans `config/chains.py` **avec la source de chaque adresse** dans `ADDRESS_SOURCES`
   (le test `test_every_mainnet_address_has_a_documented_source` échoue sinon).
2. `l1_fee_model` : `opstack` (Base, OP, etc.), `arbitrum` (frais L1 inclus dans l'estimation) ou `none`.
3. `arbbot verify-chain` sur ce réseau ; la découverte des pools est automatique.
4. Déploiement du contrat via `arbbot executor-plan`. Aucune hypothèse d'atomicité inter-chaînes n'existe dans le code.
