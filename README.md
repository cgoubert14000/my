# arbbot — bot d'arbitrage flash-loan multi-DEX, piloté par la preuve

> **État réel du projet au 2026-10-13** (lire avant toute chose)
>
> * Tout le code (contrat, moteur, simulateur, signer isolé, laboratoire, interface) est écrit et **exécuté**. Preuves
>   reproductibles : `docs/reports/tests_latest.md` — **36/36 tests Foundry** (unitaires, fuzz, invariants, Uniswap V3
>   réel), **76/76 tests Python** dont des tests bout-en-bout sur un devnet anvil avec **une vraie transaction signée et
>   minée** par le signer isolé sous politique ; `docs/reports/slither.json` ; `docs/reports/lab_*.md` (laboratoire 60 min).
> * **Sessions sur le réseau réel (Base mainnet, chain id 8453), en lecture seule** : elles tournent sur GitHub Actions
>   (`.github/workflows/real-market-ghost.yml`) parce que l'environnement de développement n'a accès à aucun RPC ; les
>   résultats bruts sont dans `docs/reports/real/` (journal, pré-vol RPC, rapport JSON/MD, chaque candidat en CSV) et
>   `docs/reports/verify_chain_base_*.md` (toutes les adresses et hypothèses vérifiées sur la chaîne). Suivi en direct :
>   `docs/live/index.html` (instantané publié toutes les 2 min pendant une session, cf. `docs/04`, § 4b-ter).
> * **Résultat réel à ce jour : aucune opportunité à net positif** après frais LP, frais de flash loan, gaz L2 et données
>   L1 n'a été observée sur Base pendant les sessions (251 pools, 8 DEX, routes 2 et 3 sauts, cotations exactes au bloc).
>   Le statut de maturité est donc **APPRENTISSAGE — FIABILITÉ NON DÉMONTRÉE (DONNÉES INSUFFISANTES)** et aucune
>   transaction réelle ne sera tentée : c'est le comportement voulu. **Aucune rentabilité n'est démontrée ni promise.**
> * Le statut affiché par le bot est calculé à partir des rapports exécutés, jamais déclaré à la main.

## Ce que fait le système

| Brique | Rôle | Où |
|---|---|---|
| Collecteur | lit l'état des pools (réserves, slot0, ticks, liquidités) à chaque bloc via multicall, mesure la fraîcheur et la latence RPC | `backend/arbbot/data/` |
| Mathématiques exactes | V2 (x·y=k, fees ppm), V3 (ticks, bit-exact vs chaîne), Solidly stable/volatile ; quotes multi-sauts | `backend/arbbot/core/` |
| Recherche de routes | cycles 2 sauts et 3 sauts à partir des tokens empruntables, multi-DEX | `engine/routes.py` |
| Optimisation du montant | recherche grille + nombre d'or sur le profit net après frais flash, bornée par la profondeur et l'impact de prix | `engine/optimizer.py` |
| Calcul des frais et du net | frais de swap, frais flash (0 %/0,05 %/0,09 % lus sur la chaîne), gaz L2 + données L1, conversion en token/€ ; brut théorique, net prévu, net simulé, net réalisé, cumul avec échecs | `engine/fees.py`, `core/types.py` |
| Simulateur | `eth_call` de la vraie transaction sur le contrat (ou via `stateOverride`), profit exact, décodage des reverts | `simulation/simulator.py` |
| Fiabilité | Beta-binomiale (borne inférieure crédible 90 %) par segment + régression logistique validée sur holdout (Brier/ECE) ; « FIABILITÉ NON DÉMONTRÉE — DONNÉES INSUFFISANTES » tant que l'échantillon est trop petit | `reliability/model.py` |
| Mode ghost | ré-simule chaque candidat au bloc N+1 sans signer, enregistre positifs **et** négatifs, déduplique | `ghost/labeler.py` |
| Sélection | classement par espérance `p_inf·net − (1−p_inf)·coût_échec`, motifs de rejet explicites | `engine/selector.py` |
| Gestion du risque | statuts APPRENTISSAGE / SIMULATION / FIABILITÉ INSUFFISANTE / PRÊT POUR TEST RÉEL LIMITÉ / MODE RÉEL ACTIF / SUSPENDU, critères vérifiables, suspension automatique | `risk/manager.py` |
| Politique d'autorisation | `authorization.json` (budget, plafonds gaz, nb tx, profit min, slippage, perte max, validité, listes blanches) **gelée** : le moteur ne peut pas la modifier | `config/policy.py` |
| Signer isolé | processus séparé, keystore chiffré, applique lui-même la politique, ne signe que `executeArbitrage` vers le contrat autorisé | `signer/service.py` |
| Exécuteur | re-vérification complète avant envoi (prix, liquidité, gaz, frais, net, fraîcheur, slippage, remboursement, budget restant, listes, probabilité ≥ 75 %), gardes on-chain `minProfit` + `minAmountOut` par saut | `execution/executor.py` |
| Contrat `FlashArbExecutor` | flash loans Balancer V2 / Aave V3 / Morpho Blue / Uniswap V3 flash, sauts V2/V3/Solidly, callbacks authentifiés, listes blanches, pause, 2-step ownership, garde par delta de solde (tokens à frais) | `contracts/src/` |
| Laboratoire 60 min + auto-correction | phases 0-5/5-15/15-30/30-45/45-55/55-60, OBSERVER→DIAGNOSTIQUER→MODIFIER→TESTER→COMPARER→ACCEPTER/ROLLBACK, candidats isolés dans un dépôt git interne, référence stable conservée | `lab/` |
| API + interface | FastAPI (REST + WebSocket), tableau de bord React/Recharts : métriques, graphiques temps réel, table des opportunités avec toutes les colonnes de coût, probabilité, incertitude, simulation, décision ; arrêt d'urgence | `api/`, `frontend/` |

## Démarrage rapide (Windows, PowerShell) — mode lecture seule, sans portefeuille

```powershell
git clone <URL_DE_CE_DEPOT> arbbot ; cd arbbot
py -3.11 -m venv .venv ; .\.venv\Scripts\Activate.ps1
pip install -e ".\backend[dev]"
Copy-Item .env.example .env            # ARB_CHAIN=local par défaut (devnet sans risque)
# terminal 1 : devnet local (nécessite Foundry, voir docs/04)
anvil --port 8545 --chain-id 31337 --block-time 2 --balance 100000
# terminal 2 : déploiement devnet + API
python devnet\deploy_devnet.py ; arbbot serve
# terminal 3 : interface
cd frontend ; npm install ; npm run dev     # http://localhost:5173
```

Pour un réseau réel (Base/Arbitrum) en **lecture seule** : `ARB_CHAIN=base`, `ARB_RPC_HTTP_URL=<votre RPC>`, puis
`arbbot verify-chain` et `arbbot serve`. Aucune transaction n'est possible tant qu'aucun signer n'est configuré :
l'interface affiche alors « PRÊT POUR TEST RÉEL — AUTORISATION FINANCIÈRE MANQUANTE » avec la marche à suivre.

Guide complet : `docs/04_installation_windows.md`.

## Documentation (français)

| Fichier | Contenu |
|---|---|
| `docs/01_analyse_open_source.md` | 21 dépôts analysés (URL, licence, maintenance, dépendances, risques, utilité), ce qui a été réutilisé et pourquoi rien n'a été copié |
| `docs/02_choix_reseau_et_strategie.md` | comparaison Ethereum / Base / Arbitrum sur frais, blocs, DEX, flash loans, MEV ; choix Base en primaire, Arbitrum en secondaire |
| `docs/03_architecture.md` | modules, flux de données, schéma de décision, base de données, modes |
| `docs/04_installation_windows.md` | installation complète copier-coller, RPC/WS, `.env`, lancement, tests, ghost, dépannage |
| `docs/05_tests_et_securite.md` | tests exécutés (contrats + backend), analyse statique, protections, risques résiduels, procédure de rollback |
| `docs/06_wallet_securise.md` | portefeuille dédié, keystore, signer isolé, politique d'autorisation, ce que le moteur ne peut jamais faire |
| `docs/07_procedure_premier_test_reel.md` | conditions, étapes, budget 10–20 €, critères d'arrêt, lecture des résultats |
| `docs/08_fiabilite_et_decision.md` | méthode statistique, calibration, seuil 75 %, statuts de maturité, protection continue |
| `docs/09_mev_et_qualite_execution.md` | mempools privés L2, Flashblocks, Timeboost, backrunning, ce que le bot mesure |
| `docs/10_depannage.md` | erreurs courantes et solutions, arrêt d'urgence |
| `docs/reports/` | rapports générés : tests, Slither, laboratoire, décisions |

## Arborescence

```
arbbot/
├── backend/arbbot/        moteur Python (voir tableau ci-dessus) + tests/
├── contracts/             Foundry : src/FlashArbExecutor.sol, interfaces, mocks, test/ (unit, fuzz, invariant, V3 réel), script/
├── devnet/                déploiement du devnet (vrai bytecode Uniswap), simulateur de marché, artefacts
├── frontend/              Vite + React + TypeScript + Recharts
├── scripts/run_tests.py   exécute toutes les suites et écrit docs/reports/*
├── docs/                  documentation + rapports
├── .env.example           configuration sans secret
├── authorization.example.json   politique d'autorisation (désactivée) à copier en authorization.json
└── data/ (ignoré)         base SQLite, paramètres, dépôt git interne d'auto-correction
```

## Arrêt d'urgence

Bouton rouge dans l'interface, ou `arbbot emergency-stop`, ou `curl -X POST http://127.0.0.1:8000/api/control/emergency-stop`.
Effet immédiat : aucune décision ni signature ; statut SUSPENDU ; reprise manuelle en simulation uniquement.
Couper le processus `arbbot signer` rend toute signature physiquement impossible.

## Licence et attribution

Code original (MIT). Dépendances : OpenZeppelin 5.4 (MIT), forge-std (MIT/Apache), bytecode Uniswap V2/V3 et Multicall3
pour le devnet uniquement (licences respectives), web3.py, FastAPI, Recharts. Aucun code provenant de dépôts sans licence
ou sous AGPL n'a été incorporé (détail dans `docs/01`).
