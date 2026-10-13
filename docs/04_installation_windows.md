# 04 — Installation sur Windows et passage en réseau réel (Base)

Toutes les commandes sont pour **PowerShell** (Windows 10/11). Copiez-collez bloc par bloc. Aucune clé privée n'est
jamais saisie dans un fichier du dépôt ni dans le chat.

## 0. Pourquoi « devnet » d'abord, et comment passer en réel

L'environnement dans lequel ce projet a été construit n'avait **aucun accès aux RPC publics** (toutes les connexions
vers `mainnet.base.org`, `arb1.arbitrum.io`, etc. y sont coupées). Les preuves ont donc été produites sur un réseau
local anvil avec le vrai bytecode Uniswap. **Sur votre machine, le passage au réel ne demande que deux lignes dans
`.env`** (`ARB_CHAIN=base` et votre URL RPC) suivies de `arbbot verify-chain`. Le code exécuté est le même : la
découverte des pools par les factories, les mathématiques, le simulateur, le signer et la politique ont été testés sur
le devnet (`docs/reports/tests_latest.md`).

## 1. Prérequis

| Outil | Version | Installation |
|---|---|---|
| Git | ≥ 2.40 | `winget install Git.Git` |
| Python | **3.11** (3.12 fonctionne aussi) | `winget install Python.Python.3.11` |
| Node.js | ≥ 20 LTS | `winget install OpenJS.NodeJS.LTS` |
| Foundry (forge, anvil, cast) | ≥ 1.0 | voir §2 (optionnel pour le mode réel en lecture seule, **obligatoire** pour le devnet, les tests de contrat et le déploiement) |

Ouvrez un **nouveau** PowerShell après chaque `winget install` pour recharger le `PATH`.

## 2. Récupérer le projet et installer le backend

```powershell
git clone <URL_DE_CE_DEPOT> arbbot
cd arbbot
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1          # si bloqué : Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
python -m pip install --upgrade pip
pip install -e ".\backend[dev]"
arbbot --help                          # doit lister : serve, signer, ghost, lab, verify-chain, policy-example, policy-check, make-keystore, emergency-stop
```

Foundry (recommandé) :

```powershell
# Option A (officielle) : foundryup via Git Bash
#   curl -L https://foundry.paradigm.xyz | bash ; puis dans un nouveau terminal : foundryup
# Option B (sans Git Bash) : paquets npm utilisés pour construire ce projet
npm install -g @foundry-rs/forge@1.7.1 @foundry-rs/anvil@1.7.1 @foundry-rs/cast@1.7.1
forge --version ; anvil --version
```

## 3. Interface web

```powershell
cd frontend
npm install
npm run build        # produit frontend\dist, servi automatiquement par l'API sur http://localhost:8000
cd ..
```

Pour le développement de l'interface : `npm run dev` (http://localhost:5173, proxy vers l'API sur 8000).

## 4. Configuration `.env`

```powershell
Copy-Item .env.example .env
notepad .env
```

### 4a. Mode devnet (sans risque, pour vérifier que tout fonctionne)

Laissez `ARB_CHAIN=local`. Trois terminaux :

```powershell
# Terminal 1 — chaîne locale
anvil --port 8545 --chain-id 31337 --block-time 2 --balance 100000
# Terminal 2 — déploiement (vrai bytecode Uniswap V2/V3, pools, fournisseurs flash, exécuteur) puis API + UI
.\.venv\Scripts\Activate.ps1
python devnet\deploy_devnet.py
arbbot serve                                   # http://localhost:8000
# Terminal 3 (optionnel) — simulateur de marché qui crée des écarts de prix
.\.venv\Scripts\Activate.ps1
python devnet\market_sim.py --rate 0.7 --shock-every 20 --competitor 0.15 --reversion 0.25
```

### 4b. Mode RÉEL en lecture seule (Base) — aucune transaction possible

1. Obtenez une URL RPC Base. Gratuit et suffisant pour le mode ghost : Alchemy, Infura, QuickNode, dRPC, Ankr
   (créer un compte → « Base Mainnet » → copier l'URL HTTPS ; prenez aussi l'URL **WSS** si proposée).
   Le RPC public `https://mainnet.base.org` fonctionne mais est limité (≈ 10 req/s) : mettez `ARB_RPC_MAX_RPS=8`.
2. Dans `.env` :

```ini
ARB_CHAIN=base
ARB_RPC_HTTP_URL=https://base-mainnet.g.alchemy.com/v2/VOTRE_CLE
ARB_RPC_WS_URL=wss://base-mainnet.g.alchemy.com/v2/VOTRE_CLE      # optionnel
ARB_RPC_FALLBACK_HTTP_URLS=https://mainnet.base.org
ARB_RPC_MAX_RPS=20
ARB_EXECUTOR_ADDRESS=            # vide tant que vous n'avez pas déployé le contrat (simulation via stateOverride)
```

3. Vérifiez le réseau **avant** de lancer le moteur :

```powershell
arbbot verify-chain
```

Ce que la commande fait réellement (rapport `docs\reports\verify_chain_base_<date>.md`) :
chain id = 8453 ; latence et temps de bloc mesurés ; support de `eth_call` avec `stateOverride` (nécessaire pour simuler
sans contrat déployé), de Multicall3 et de `debug_traceTransaction` ; présence de code à **chaque** adresse
(tokens, factories, fournisseurs de flash loan, oracle de frais L1) avec la **source officielle** de chaque adresse ;
`symbol()`/`decimals()` de chaque token ; sondes de factories (`allPairsLength`, `feeAmountTickSpacing`,
`allPoolsLength`, `tickSpacingToFee`) ; frais Aave lus on-chain ; **capacité réelle** de flash loan par fournisseur
et par token ; découverte des pools par les factories et **profondeur en USD** de chacun ; prix ETH déduit du pool
WETH/USDC le plus profond. Si une vérification bloquante échoue, rien n'est marqué vérifié et l'interface l'affiche.

4. Lancez :

```powershell
arbbot serve
```

Ouvrez http://localhost:8000. Le bandeau vert « RÉSEAU RÉEL — Base » confirme la source des données ; le statut
démarre en **APPRENTISSAGE** : le mode ghost enregistre chaque opportunité réelle, la re-simule au bloc suivant et
construit la statistique de fiabilité. Laissez tourner **plusieurs heures au minimum** (le seuil mathématique est
≥ 30 observations, mais 75 % avec une borne inférieure crédible à 90 % demande en pratique 100–300 observations).

Sans signer configuré, l'interface affiche « PRÊT POUR TEST RÉEL — AUTORISATION FINANCIÈRE MANQUANTE » dès que les
autres critères sont verts : rien ne peut être signé, c'est voulu.

### 4b-bis. Le plus simple : la session « marché réel » tout-en-un

```powershell
# essaie les RPC publics Base (ou le vôtre avec --rpc), vérifie tout, puis tourne 30 min en ghost et écrit les rapports
python scripts\real_market_session.py --chain base --minutes 30 --rpc https://base-mainnet.g.alchemy.com/v2/VOTRE_CLE
```

Elle écrit `docs\reports\real\ghost_base_<tag>.md` (pools réels avec profondeur et prix au bloc, gaz, meilleures
opportunités avec toutes les charges, étiquettes ghost, fiabilité) + `.json` + `_opportunities.csv` (chaque candidat),
et laisse un `.env` prêt pour `arbbot serve` (interface en direct). Le même script tourne automatiquement sur
**GitHub Actions** (`.github/workflows/real-market-ghost.yml`) à chaque modification de `ops/real/run.json` :
les rapports arrivent dans la branche, sans aucune clé.

### 4c. Laboratoire de 60 minutes sur données réelles

```powershell
arbbot lab --minutes 60            # ou depuis l'interface, onglet « Laboratoire »
```

Le rapport est écrit dans `docs\reports\lab_<date>.md` (phases 0-5 / 5-15 / 15-30 / 30-45 / 45-55 / 55-60, décision
d'auto-correction avec métrique au bloc N+1, verdict de maturité). Il ne déclare jamais « prêt » du seul fait des
60 minutes écoulées.

## 5. Tests

```powershell
.\.venv\Scripts\Activate.ps1
python scripts\run_tests.py            # forge (si installé) + pytest ; écrit docs\reports\tests_latest.md et les JSON lus par le moteur
```

Les tests `devnet` ne s'exécutent que si anvil tourne sur 8545 (sinon ils sont ignorés et marqués comme tels).
Le moteur **refuse le mode réel** si les rapports de tests sont absents, rouges ou vieux de plus de 7 jours.

## 6. Préparer le mode réel limité (quand les critères sont verts)

Lisez `docs/06_wallet_securise.md` (portefeuille dédié + signer isolé) puis `docs/07_procedure_premier_test_reel.md`
(déploiement du contrat, politique d'autorisation, budget 10–20 €, critères d'arrêt). Résumé des commandes :

```powershell
arbbot make-keystore                                   # nouveau portefeuille dédié, keystore chiffré (mot de passe demandé)
arbbot policy-example                                   # écrit authorization.example.json → copier en authorization.json et éditer
arbbot policy-check                                     # valide la politique (enabled, wallet, contrat, plafonds, validité)
# Terminal signer (processus séparé, reste ouvert) :
$env:ARB_SIGNER_KEYSTORE="keystores\executor.json"; $env:ARB_SIGNER_TOKEN="<jeton long>"; arbbot signer
# Terminal moteur :
$env:ARB_SIGNER_TOKEN="<le même jeton>"; arbbot serve
```

## 7. Arrêt d'urgence

* Bouton rouge « ARRÊT D'URGENCE » dans l'interface, ou `arbbot emergency-stop`, ou `curl.exe -X POST http://127.0.0.1:8000/api/control/emergency-stop`.
* Fermer la fenêtre du signer (`Ctrl+C`) rend toute signature impossible, quel que soit l'état du moteur.
* Sur la chaîne : `cast send <EXECUTEUR> "pause()" --rpc-url <RPC> --keystore keystores\executor.json` (le gardien/propriétaire peut mettre le contrat en pause).

## 8. Dépannage rapide

Voir `docs/10_depannage.md`. Les trois causes les plus fréquentes : `.venv` non activé (`arbbot` introuvable),
RPC limité (`rpc_errors` dans le journal → baissez `ARB_RPC_MAX_RPS`, ajoutez un fallback), horloge Windows
désynchronisée (données jugées périmées → activez la synchronisation automatique de l'heure).
