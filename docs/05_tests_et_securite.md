# 05 — Tests exécutés, sécurité du contrat, risques résiduels

Tout ce qui suit a été **exécuté** ; les sorties brutes sont dans `docs/reports/` (`tests_latest.md`,
`forge_tests.json`, `pytest_results.json`, `slither.json`). Le moteur relit ces fichiers au démarrage : rapports
absents, rouges ou vieux de plus de 7 jours ⇒ critères `tests_passed` / `contract_tested` rouges ⇒ pas de mode réel.

## 1. Contrat `FlashArbExecutor.sol` — Foundry : 36 tests, 0 échec

| Catégorie | Tests | Ce qui est prouvé |
|---|---|---|
| Unitaires (24) | profitable via Balancer / Aave (prime payée) / Morpho (0 frais) / auto-financé ; `revert` si profit < `minProfit`, si une route ne peut pas rembourser, si auto-financé non rentable (jamais de perte) ; `HopOutputTooLow` ; `Expired` ; `NotExecutor` ; `PoolNotAllowed` / `TokenNotAllowed` / `ProviderNotAllowed` ; `BorrowCap` ; route non cyclique ou discontinue ; nombre de sauts / montant nul ; **callbacks directs rejetés** (Balancer, Aave, Morpho, V3 swap/flash appelés par un tiers) ; pause par le gardien et le propriétaire ; propriété en deux étapes ; `withdraw` réservé au propriétaire ; token à frais de transfert détecté par delta de solde ; quote V2 identique au mock | gaz mesuré : 209 413 (Balancer), 213 992 (Aave), 211 084 (Morpho), 938 094 (route Solidly stable) |
| Fuzz (5 × 512 runs) | montants, frais, ordres de tokens, `minProfit` aléatoires : l'exécution ne réussit **que** si le solde final ≥ initial + `minProfit`, sinon revert, et l'état des listes blanches n'est jamais modifié | invariant économique sous entrées aléatoires |
| Invariants (4 × 128 × 4096 appels) | le contrat ne perd jamais de token de départ ; les listes blanches ne changent que par le propriétaire ; `totalExecutions` n'augmente que sur succès ; pas de réentrance possible via callbacks | propriétés globales sur séquences d'appels aléatoires |
| Uniswap V3 réel (3) | swaps à travers des ticks sur le **vrai bytecode** V3 déployé en test : montant reçu identique à la quote Python (bit-exact) | pas de divergence maths/chaîne |

### Protections implémentées

* `ReentrancyGuardTransient` (OpenZeppelin 5.4) sur l'entrée ; callbacks authentifiés : `msg.sender` doit être le
  fournisseur / pool attendu enregistré juste avant l'appel, `initiator == address(this)`, hash du payload vérifié.
* Listes blanches tokens / pools / fournisseurs, plafond d'emprunt par token, exécuteurs autorisés, gardien pouvant
  mettre en pause, propriété en deux étapes, retraits réservés au propriétaire.
* Profit mesuré par **delta de solde** (robuste aux tokens à frais / rebasing qui feraient mentir les valeurs de retour)
  ; `minAmountOut` **par saut** et `minProfit` global (slippage et MEV bornés on-chain) ; `deadline`.
* Aucun `delegatecall`, aucun `selfdestruct`, aucune approbation permanente (approve exact puis remise à zéro pour les
  fournisseurs à remboursement par `transferFrom`).

### Analyse statique — Slither 0.11 (102 détecteurs) : `docs/reports/slither.json`

| Sévérité | Détecteur | Nombre | Triage |
|---|---|---|---|
| High | `reentrancy-balance` | 8 | **Faux positif attendu** : le patron « solde avant → appels externes → solde après » est le mécanisme de mesure du profit ; l'entrée est `nonReentrant` (stockage transitoire) et chaque callback vérifie l'appelant attendu (`_pendingProvider`, `_expectedSwapPool`). Testé par `test_revert_direct_callbacks_are_rejected` et l'invariant de réentrance. |
| Medium | `incorrect-equality` (`received == 0`) | 1 | Intentionnel : un saut qui ne livre rien doit échouer même si `minAmountOut = 0`. |
| Medium | `unused-return` (`pool.swap`, `getReserves` partiel) | 3 | Intentionnel : les valeurs de retour ne sont pas fiables pour les tokens à frais ; on mesure les soldes. |
| Low | `calls-loop`, `reentrancy-benign`, `timestamp`, `missing-zero-check` | 71 | Boucle sur les sauts bornée (≤ 4) ; `block.timestamp` utilisé pour la deadline (précision seconde suffisante) ; zéro-check ajouté au `setGuardian` lors d'une prochaine révision (non bloquant : seul le propriétaire appelle). |
| Info | complexité cyclomatique de `_validate`, convention de nom `FLASHLOAN_PREMIUM_TOTAL` | 2 | Nom imposé par l'interface Aave. |

Aucune réécriture n'a été jugée nécessaire après triage ; les findings restent listés pour audit.

## 2. Backend Python — pytest : 72 tests, 0 échec (dont 10 bout-en-bout sur devnet)

| Fichier | Tests | Exigences couvertes |
|---|---|---|
| `test_math_vs_chain.py` | 3 | **bit-exact** vs vrai bytecode : V3 62 swaps multi-ticks, V2 12/12, Solidly 36/36 |
| `test_math_units.py` | 8 (+300 cas Hypothesis) | frais, conversions de décimales, monotonie, impact de prix, quote impossible (ticks manquants) → `QuoteError` |
| `test_engine_units.py` | 15 | optimiseur vs formule fermée (±1 %), sélection avec motifs (données périmées, impact, liquidité, net négatif), classement par espérance, erreurs RPC remontées (pas de silence) |
| `test_policy_risk_signer.py` | 27 | politique : budget, nb de tx, gaz, slippage, validité, listes, mauvais contrat, `value≠0`, `minProfit=0`, mauvais portefeuille, **clé uniquement depuis un keystore chiffré** (mauvais mot de passe ⇒ erreur, clé brute refusée hors devnet) ; risque : dépassement de budget, échecs consécutifs → SUSPENDU, retour en simulation, arrêt d'urgence ; signer : refus, comptabilité indépendante |
| `test_devnet_e2e.py` | 3 | détection → simulation exacte (profit `eth_call` = brut − frais flash) → étiquette ghost ; refus de pré-vol sans signer ; **exécution réelle sur devnet** par le signer sous politique (tx minée, net réalisé, compteurs), revert comptabilisé si l'état a bougé |
| `test_api_selfcorr_ghost.py` | 4 | dépôt git d'auto-correction (propose/accepte/rollback isolés), interdiction des clés financières, dédup ghost, API : statut, opportunités, fiabilité, **arrêt d'urgence via l'API**, reprise, garde des tunables (403) |
| `test_factory_discovery_devnet.py` | 1 | chemin « réseau réel » : découverte des pools via les **factories** (vrai bytecode V2/V3), métadonnées on-chain |
| `test_verify_chain.py` | 4 | provenance documentée de chaque adresse mainnet ; empreinte de configuration et révocation ; RPC injoignable ⇒ échec fermé ; vérification complète sur devnet |
| `test_state_override_sim_devnet.py` | 1 | mode lecture seule sans contrat déployé : la simulation par **state override** (bytecode injecté à une adresse fictive) donne le même profit, au wei, que le contrat déployé, et revert de la même façon |
| `test_l1_fee_opstack.py` | 6 | frais de données L1 (Base) : `getL1FeeUpperBound` (Fjord), repli `getL1Fee(bytes)`, oracle indisponible ⇒ coût **inconnu** (candidat rejeté, jamais 0 optimiste), une lecture par bloc et par taille (pas de rafale RPC), Arbitrum sans composante séparée |

Cas de la liste d'exigences et où ils sont testés : frais (`test_math_units`, `test_engine_units`) ; conversions
(`test_math_units`) ; chemins (`test_engine_units::routes`) ; montants de prêt (`optimizer`, `BorrowCap`) ;
remboursement (`test_revert_unprofitable_route_cannot_repay`, e2e) ; slippage (`HopOutputTooLow`, pré-vol) ;
changements de liquidité (ghost N+1, e2e revert) ; données périmées (`stale_data` rejet) ; erreurs RPC
(`test_rpc_error_surfaces`) ; tx non rentable (`InsufficientProfit`) ; routes malveillantes (listes blanches, route non
cyclique, callbacks directs) ; dépassement de budget (`test_signer_enforces_cumulative_budget_and_count`) ; erreurs de
signature (signer refuse / injoignable → `signer_unavailable`) ; tx échouée (e2e revert comptabilisé) ; retour en
simulation (`test_risk_returns_to_simulation`) ; arrêt d'urgence (API + CLI).

### Validation « maths vs chaîne » pendant le laboratoire — un faux positif analysé

Le laboratoire compare, sur les pools vivants, la sortie calculée en Python à celle du vrai bytecode. Une première
version comparait au bloc « latest » : avec le simulateur de marché qui échange toutes les ~1,4 s, quelques écarts
apparaissaient (0,02–0,09 %). Analyse (scripts conservés dans l'historique de la session, résultats reproduits
ci-dessous) :

* 9 352 puis 22 008 comparaisons épinglées au bloc de l'instantané : 0 écart dû aux maths — les sorties sont
  identiques au wei, y compris en franchissant 1 ou 2 ticks V3 ;
* les 2 écarts restants (1 sur ~8 000) ont été rejoués **au même bloc** : le nœud renvoyait alors exactement notre
  valeur, et la première réponse correspondait au bloc suivant. Il s'agit d'un artefact d'anvil (résolution de
  « bloc = latest » sur l'état vivant pendant le scellement d'un bloc), pas d'une erreur de calcul.

Le laboratoire compte désormais ces cas à part (`transient`) et ne garde dans `mismatch` que les écarts reproduits au
même bloc. Sur un nœud de production (geth/reth, fournisseurs RPC) un `eth_call` à un numéro de bloc donné est
déterministe.

## 3. Forks mainnet

Non exécutés ici : aucun RPC n'était joignable depuis l'environnement de construction. Sur votre machine :

```powershell
cd contracts
forge test --fork-url $env:RPC --match-contract Fork -vv     # tests Fork à écrire sur vos pools réels après verify-chain
```

Le script `arbbot executor-plan` fournit la liste des pools profonds à utiliser dans ces tests.

## 4. Procédure de rollback (contrat)

1. `pause()` par le gardien ou le propriétaire (immédiat, bloque `executeArbitrage`).
2. `withdraw(token, to, amount)` par le propriétaire pour rapatrier les profits/soldes.
3. Déployer la version corrigée, reconfigurer les listes (`arbbot executor-plan`), mettre à jour
   `ARB_EXECUTOR_ADDRESS` et `executor_contract`, relancer `verify-chain` et la campagne de tests complète.
4. L'ancien contrat reste en pause ; `setExecutor(ancien, false)` si nécessaire.

## 5. Risques résiduels (honnêtement)

* **Concurrence / Flashblocks (Base)** : même une simulation exacte au bloc N peut échouer à l'inclusion ; la perte est
  bornée au gaz (`InsufficientProfit`), mais répétée elle épuise le budget. Mesuré par le ghost, limité par la politique.
* **Tokens exotiques** : seules les listes blanches protègent ; n'ajoutez que des tokens standards.
* **Fournisseurs de flash loan** : Balancer V2 après l'exploit de nov. 2025 → capacité à vérifier à chaque
  `verify-chain` ; Aave peut changer la prime par gouvernance (lue à chaque session).
* **RPC** : un fournisseur gratuit peut renvoyer des données en retard ; la fraîcheur est contrôlée (< 4 s pour décider,
  < 10 s pour rester « sain ») mais un RPC menteur n'est pas détectable sans second fournisseur (configurez un fallback).
* **Clé chaude** : compromission du poste ⇒ perte du budget de gaz du portefeuille dédié (par construction pas plus).
* **Pas d'audit externe** : les tests, le fuzzing, les invariants et Slither réduisent le risque ; ils ne remplacent pas
  un audit indépendant pour des montants significatifs.
