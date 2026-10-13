# 01 — Analyse des projets open source (Phase A)

Méthode : chaque dépôt a été consulté via l'API GitHub (métadonnées, licence, date du dernier commit, dépendances
déclarées) et par lecture du code des parties pertinentes. Les chiffres (étoiles, dates) sont ceux relevés le
2026-10-13. « Utilité » indique ce qui a été **appris ou vérifié**, jamais copié : le code de ce projet est écrit à
partir des spécifications des protocoles et validé par des tests bit-exact contre le vrai bytecode.

## Bots et bibliothèques d'arbitrage

| Dépôt | ⭐ | Licence | Maintenance | Dépendances / stack | Vulnérabilités & risques | Compatibilité | Utilité pour ce projet |
|---|---|---|---|---|---|---|---|
| [BowTiedDevil/degenbot](https://github.com/BowTiedDevil/degenbot) | 571 | MIT | active (2025–2026) | Python 3.11+, web3.py, pydantic | Pas de CVE connue ; bibliothèque, pas un bot complet ; abstractions lourdes | Python, Uniswap V2/V3, Curve | Référence pour la structure « pool helper + quote exacte en Python » et le calcul de l'arbitrage optimal V2↔V3 ; nos tests bit-exact confirment la même approche |
| [pawurb/univ3-revm-arbitrage](https://github.com/pawurb/univ3-revm-arbitrage) | 150 | MIT | 2024, peu active | Rust, revm, alloy | Démonstration de simulation locale par REVM | Rust uniquement | Montre le gain de latence d'une simulation EVM locale ; nous utilisons `eth_call` + `stateOverride` (même garantie d'exactitude, pas de dépendance Rust pour Windows) |
| [flashbots/simple-arbitrage](https://github.com/flashbots/simple-arbitrage) | 2110 | **aucune** | archivé (2021) | TypeScript, ethers v5, Flashbots bundles | Pas de licence → inutilisable ; conçu pour Ethereum L1 et les bundles Flashbots (inexistants sur Base/Arbitrum) | Ethereum L1 | Rappel pédagogique de la structure « détecter → bundle » ; sans intérêt opérationnel sur L2 |
| [ccyanxyz/uniswap-arbitrage-analysis](https://github.com/ccyanxyz/uniswap-arbitrage-analysis) | 2120 | **aucune** | 2021, inactive | Python, notebooks | Pas de licence ; données obsolètes | — | Analyse historique des opportunités V2 ; confirme que l'essentiel des gains est capté par des acteurs très rapides |
| [paco0x/amm-arbitrageur](https://github.com/paco0x/amm-arbitrageur) | 1991 | WTFPL | archivé | Solidity 0.7, Hardhat, BSC | Contrat sans listes blanches ni gardes de profit ; flash swap Uniswap V2 uniquement | BSC/V2 | Formule fermée du montant optimal entre deux pools V2 (vérifiée indépendamment dans `core/math_v2.optimal_two_pool_amount` et testée contre notre optimiseur) |
| [johngrantuk/aaveFlashLoan](https://github.com/johngrantuk/aaveFlashLoan) | 741 | MIT | stale (2020) | Aave **V1** | Interfaces obsolètes (Aave V3 utilise `flashLoanSimple` + `executeOperation` avec `initiator`) | Non compatible V3 | Aucune réutilisation ; sert d'exemple de ce qu'il ne faut pas copier (interface périmée) |
| [AleRapchan/flash-swap-arbitrage-bot](https://github.com/AleRapchan/flash-swap-arbitrage-bot) | 239 | AGPL-3.0 | 2022 | Solidity, Hardhat | AGPL contaminante ; pas de tests sérieux | V2 | Exclu (licence) |
| [kaymen99/aave-flashloan-arbitrage](https://github.com/kaymen99/aave-flashloan-arbitrage) | 168 | MIT | 2023 | Solidity 0.8, Aave V3, Uniswap/Sushi routers | Utilise des **routers** (gaz élevé, pas de minOut par saut), pas de vérification du `initiator` dans le callback dans certaines versions | Aave V3 | Confirme le schéma `flashLoanSimple` → `executeOperation` → `approve(pool, amount+premium)` ; nous vérifions `initiator == address(this)` et `msg.sender == provider attendu` |
| [whisdev/flashloan-arbitrage-bot (et clones)](https://github.com/whisdev) | 103 | **aucune** | — | mixte | Code marketing, pas de tests, parfois des adresses de « récupération » suspectes | — | Exclu ; classé comme risque (dépôts de ce type contiennent régulièrement des portes dérobées) |
| [gebob19/uniswap-v3-flashswap](https://github.com/gebob19/uniswap-v3-flashswap) | 87 | **aucune** | 2022 | Solidity, Foundry | Pas de licence | V3 | Exemple de `IUniswapV3Pool.flash` + `uniswapV3FlashCallback` ; notre implémentation suit la documentation officielle |
| [skellet0r/arbie](https://github.com/skellet0r/arbie) | 85 | MIT | 2021 | Python, Brownie | Dépend de Brownie (abandonné) | — | Rien de réutilisable |
| [manuelinfosec/flash-arb-bot](https://github.com/manuelinfosec/flash-arb-bot) | 70 | MIT | 2023 | Python, web3 | Prix via routers `getAmountsOut` (lent, 1 appel par route) | V2 | Contre-exemple : nous lisons l'état des pools en multicall et quotons localement |

## Protocoles et outils (code de référence, pas des bots)

| Dépôt | Licence | Usage dans ce projet |
|---|---|---|
| [Uniswap/v2-core](https://github.com/Uniswap/v2-core), [v3-core](https://github.com/Uniswap/v3-core), [v3-periphery](https://github.com/Uniswap/v3-periphery) | GPL-2.0/3.0 / BUSL expirée (V3 core : GPL depuis 2023) | Bytecode compilé (paquets npm officiels `@uniswap/v2-core`, `@uniswap/v3-core`) déployé sur le **devnet uniquement** ; les interfaces Solidity minimales sont réécrites dans `contracts/src/interfaces` |
| [aave/aave-v3-core](https://github.com/aave/aave-v3-core) | BUSL-1.1 (interfaces MIT) | Interface `IPool.flashLoanSimple`, `FLASHLOAN_PREMIUM_TOTAL` lu on-chain (0,05 % à l'initialisation, modifiable par gouvernance) |
| [balancer/balancer-v2-monorepo](https://github.com/balancer/balancer-v2-monorepo) | GPL-3.0 | `IVault.flashLoan` + `receiveFlashLoan` ; **note : exploit CSP du 3 nov. 2025 (~117–128 M$)** — la Vault reste déployée mais la liquidité V2 a fortement chuté → disponibilité du flash loan 0 % **à mesurer** avant usage (`arbbot verify-chain` lit `maxFlashLoan` effectif) |
| [morpho-org/morpho-blue](https://github.com/morpho-org/morpho-blue) | BUSL-1.1 / GPL-2.0 interfaces | `flashLoan(token, assets, data)` + `onMorphoFlashLoan`, frais 0, remboursement par `transferFrom` (approve exact) — fournisseur par défaut |
| [aerodrome-finance/contracts](https://github.com/aerodrome-finance/contracts) | MIT (fork Velodrome) | Courbe Solidly stable `x³y + xy³ = k` et volatile ; formule reproduite et testée bit-exact (36/36 sur devnet) |
| [mds1/multicall](https://github.com/mds1/multicall) (Multicall3) | MIT | `aggregate3` pour lire des centaines de slots en un appel ; déployé sur le devnet à son adresse canonique |
| [foundry-rs/foundry](https://github.com/foundry-rs/foundry) | MIT/Apache-2.0 | Compilation, tests (unit/fuzz/invariant), anvil (devnet, forks) |
| [OpenZeppelin/openzeppelin-contracts](https://github.com/OpenZeppelin/openzeppelin-contracts) 5.4.0 | MIT | `Ownable2Step`, `Pausable`, `ReentrancyGuardTransient`, `SafeERC20` |
| [crytic/slither](https://github.com/crytic/slither) | AGPL-3.0 (outil, n'affecte pas le code analysé) | Analyse statique exécutée → `docs/reports/slither.json` (triage dans `docs/05`) |
| [pancakeswap/pancake-v3-contracts](https://github.com/pancakeswap/pancake-v3-contracts) | GPL-2.0 | Variante V3 (callback `pancakeV3SwapCallback`) ; supportée via le même chemin que Uniswap V3 avec sélecteur de callback dédié |

## Conclusions de la phase A

1. **Aucun dépôt ne fournit un système complet et sûr** : pas de simulation exacte, pas de politique financière gelée, pas de mesure de fiabilité, rarement des tests. Les plus populaires n'ont pas de licence ou visent Ethereum L1 avec Flashbots.
2. **Ce qui est réutilisé** : les spécifications des protocoles (interfaces, formules), le bytecode officiel pour le devnet, OpenZeppelin, Foundry/Slither comme outillage.
3. **Ce qui est écrit from scratch et prouvé par tests** : mathématiques V2/V3/Solidly (bit-exact vs chaîne), optimiseur de montant, calculateur de frais, contrat exécuteur (36 tests), simulateur, fiabilité, signer, politique, laboratoire, interface.
4. **Risques spécifiques identifiés dans l'écosystème** : dépôts « bots » contenant des adresses de récupération (vol de fonds) ; interfaces Aave V1 périmées ; absence de vérification `initiator`/`msg.sender` dans les callbacks ; utilisation de routers (gaz, slippage global au lieu de par saut) ; confiance dans les prix d'agrégateurs au lieu des montants réellement récupérables.
