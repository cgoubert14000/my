# 10 — Dépannage

| Symptôme | Cause probable | Solution |
|---|---|---|
| `arbbot : terme non reconnu` | venv non activé | `.\.venv\Scripts\Activate.ps1` (ou `python -m arbbot.cli …`) |
| `Activate.ps1 cannot be loaded` | politique d'exécution PowerShell | `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` |
| `runtime not started: RpcError … eth_chainId` ou `rpc_reachable KO` | URL RPC fausse, clé invalide, pare-feu/proxy, pas d'internet | tester `curl.exe -X POST -H "content-type: application/json" --data "{\"jsonrpc\":\"2.0\",\"id\":1,\"method\":\"eth_chainId\",\"params\":[]}" <URL>` ; doit renvoyer `0x2105` pour Base |
| `chain_id KO rpc=1 config=8453` | URL d'un autre réseau | prendre l'URL « Base Mainnet » du fournisseur |
| `rpc_errors` qui montent, `429 Too Many Requests` | quota du RPC gratuit | `ARB_RPC_MAX_RPS=8`, ajouter `ARB_RPC_FALLBACK_HTTP_URLS`, passer à un forfait |
| `eth_call_state_override WARN not supported` | RPC qui n'implémente pas le 3ᵉ paramètre d'`eth_call` | la simulation exige alors `ARB_EXECUTOR_ADDRESS` (contrat déployé) ; Alchemy/QuickNode/dRPC le supportent |
| Statut reste APPRENTISSAGE longtemps | peu d'opportunités positives sur le réseau (normal) | laisser tourner ; vérifier `pools_with_depth` dans le rapport de vérification ; élargir les tokens de `config/chains.py` seulement avec des adresses dont la source est documentée |
| « FIABILITÉ NON DÉMONTRÉE — DONNÉES INSUFFISANTES » | < 30 observations dans le segment | attendre ; ne pas baisser le seuil |
| `data_stale` / critère `data_fresh` rouge | RPC lent, horloge Windows décalée | activer la synchronisation de l'heure ; mesurer la latence (`verify-chain`) ; WS (`ARB_RPC_WS_URL`) |
| Table « Net simulé » vide (—) | seules les 3 meilleures opportunités positives sont simulées par bloc | normal ; les autres gardent `sim = None` |
| `PRÊT POUR TEST RÉEL — AUTORISATION FINANCIÈRE MANQUANTE` | aucun signer joignable ou politique `enabled=false` / `valid_until=0` | suivre `docs/06` ; `arbbot policy-check` ; vérifier `ARB_SIGNER_TOKEN` identique des deux côtés |
| Signer : `No key: set ARB_SIGNER_KEYSTORE` | variable absente dans le terminal du signer | `$env:ARB_SIGNER_KEYSTORE="keystores\executor.json"` dans **ce** terminal |
| Signer : `policy wallet differs` | keystore ≠ `wallet_address` | corriger la politique ou utiliser le bon keystore |
| Décision `REJECTED expected_net_nonpositive_with_estimated_gas` | `eth_estimateGas` > modèle et le net devient ≤ 0 | normal : opportunité trop fine ; le laboratoire recalibre le modèle de gaz |
| Décision `REJECTED pool_not_allowed_onchain` / revert `PoolNotAllowed` | contrat configuré sans ce pool | relancer `arbbot executor-plan` et envoyer le `setPools` manquant |
| Revert `InsufficientProfit` en réel | écart capté par un concurrent avant inclusion | attendu de temps en temps ; si fréquent, le risque suspend (2 consécutifs) ; rester en ghost |
| `SUSPENDU` | voir motif dans le bandeau et le journal | corriger la cause, puis bouton « Reprendre (simulation) » ; le réel se réactive manuellement |
| `forge: command not found` | Foundry absent du PATH | réinstaller (docs/04 §2) ou utiliser les paquets npm ; sans forge, `run_tests.py` saute les tests de contrat et `contract_tested` reste rouge (mode réel impossible, par conception) |
| `npm run build` échoue (`tsc`) | Node trop ancien | Node ≥ 20 |
| Port 8000 occupé | autre instance | `ARB_API_PORT=8010` ou fermer l'ancienne |
| Page `docs/live` : « aucun instantané disponible » | `latest_<chain>.json` absent (aucune session n'a encore publié) ou page ouverte en `file://` (fetch interdit) | servir la page (`python scripts\live_mirror.py …` ou GitHub Pages) ; lancer une session |
| Page `docs/live` : bandeau rouge « instantané il y a > 5 min » | session terminée, ou crochet de publication en échec (voir `snapshot hook rc=` dans `session_<run>.log`) | normal après la fin d'une session ; sinon lire le journal : `publish: push rejected` = concurrence sur la branche (réessayé au prochain instantané) |
| `cycle_budget_exhausted` élevé, `routes_optimized` faible | trop de survivants au filtre pour le budget de 1,2 s | normal : les routes sont dimensionnées par écart décroissant ; augmenter `cycle_time_budget_ms` seulement si les blocs ne sont pas manqués (`blocks_seen` ≈ durée/2 s) |
| Sessions GitHub Actions qui s'enchaînent sans fin | `continuous: true` dans `ops/real/run.json` | mettre `"continuous": false`, pousser : la session en cours se termine normalement et n'en relance pas d'autre |
| Arrêter la session en cours **proprement** (avec rapport final) | — | `"stop": true` (tout arrêter) ou `"stop_run_id": "<id du run>"` (une seule) dans `ops/real/run.json`, pousser : pris en compte au prochain instantané (≤ 3 min). Le bouton « Cancel » de GitHub tue le job sans rapport final |
| Démarrage long (2–4 min) sur le réseau réel | construction de l'univers (≈ 400 jetons, milliers de pools mesurés) | normal ; réduire `ARB_DISCOVERY_MAX_POOLS` / désactiver `ARB_DISCOVERY_FACTORY_ENUM=false` sur un RPC lent |
| `429` au démarrage sur RPC public | découverte = ~200 requêtes multicall | baisser `--max-rps`, ou fournir votre propre RPC (`--rpc`) |
| `blocks_seen` très inférieur à durée/2 s | cycle plus long que le bloc (RPC lent, ticks V3, trop d'optimisations) | vérifier `last_cycle_ms`, `last_screen_ms`, `refresh_p95_ms` dans le rapport ; `ARB_RPC_WS_URL` ; RPC payant plus rapide |

## Arrêt d'urgence — rappel

1. Interface : bouton rouge **ARRÊT D'URGENCE** (statut SUSPENDU immédiat).
2. Terminal : `arbbot emergency-stop`.
3. Couper le signer (`Ctrl+C` dans sa fenêtre) : plus aucune signature possible.
4. Contrat : `cast send <EXECUTEUR> "pause()" --rpc-url <RPC> --keystore keystores\executor.json` (le gardien peut mettre en pause).

## Journaux et données

* Journal du moteur : terminal `arbbot serve` + onglet « Journal » (`/api/events`).
* Base de données : `data\arbbot.sqlite` (tables opportunities, observations, executions, events, changes, metrics).
* Rapports : `docs\reports\` (tests, vérification réseau, laboratoire, plan de déploiement).
* Auto-correction : dépôt git interne `data\selfcorr` (`git -C data\selfcorr log --all --oneline`).
