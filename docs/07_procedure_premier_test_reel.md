# 07 — Procédure du premier test réel limité (Base)

Budget personnel engagé : **10–20 € de gaz au maximum** (le flash loan n'est pas un budget). Ce document ne promet
aucun gain ; il décrit comment ne perdre, au pire, que le gaz plafonné par la politique.

## A. Conditions préalables — toutes obligatoires

Le bouton « activer le test réel limité » n'apparaît que si le statut est **PRÊT POUR TEST RÉEL LIMITÉ**, c'est-à-dire
quand chaque critère de l'onglet « Fiabilité » est vert :

| Critère | Comment il devient vert |
|---|---|
| `chain_verified` | `arbbot verify-chain` réussi pour la configuration courante (empreinte identique) |
| `tests_passed`, `contract_tested`, `financial_math_validated` | `python scripts/run_tests.py` vert il y a moins de 7 jours (forge + pytest, y compris les tests devnet) |
| `simulations_realistic` | ≥ 20 simulations `eth_call` réussies sur le réseau réel, pas plus d'échecs que de succès |
| `reliability_documented` | ≥ 30 observations ghost (re-simulation au bloc N+1) sur le réseau réel |
| `p_success_ge_threshold` | borne inférieure crédible (90 %) de la probabilité de net > 0 ≥ 75 % |
| `model_calibrated` | le taux observé récent n'est pas inférieur à la borne prédite au moment des décisions |
| `data_fresh` | données < 10 s, RPC sain |
| `emergency_stop_ok` | test d'arrêt d'urgence exécuté et réussi |
| `budget_and_limits_configured` | `authorization.json` valide : `enabled=true`, portefeuille, contrat, plafonds, fenêtre de validité en cours |
| `signer_available` | `arbbot signer` joignable, son adresse = `wallet_address`, jeton correct |

Si l'un d'eux reste rouge après des heures de ghost sur Base — en particulier `p_success_ge_threshold` — **la bonne
décision est de ne pas exécuter**. Le rapport de laboratoire (`arbbot lab`) donne alors les segments (marge × sauts ×
types de pools) où la fiabilité est la meilleure et le nombre d'observations encore nécessaires.

## B. Coût attendu et dimensionnement du budget

Sur Base, une transaction d'arbitrage 3 sauts consomme ≈ 350–450 k gaz. Avec un base fee de 0,01 gwei et ≈ 0,002 $
de données L1, une tx réussie coûte **≈ 0,01–0,03 €**, un revert ≈ 55 % de cela. `arbbot verify-chain` affiche les
valeurs **mesurées** du moment (`base_fee_gwei`, `l1_fee_900B_eth`). Avec `max_total_budget_native = 0.004 ETH`
(≈ 10 € à 2 500 $/ETH) la politique autorise au plus quelques centaines d'essais ; `max_transactions = 10` et
`max_consecutive_failures = 2` arrêtent bien avant.

## C. Déploiement du contrat (une fois, par vous)

1. `arbbot verify-chain` (rapport OK).
2. Politique remplie (`docs/06`), `arbbot policy-check` OK.
3. `arbbot executor-plan` → `docs/reports/executor_plan_base.md` : commandes `forge create` + `cast send`
   (`setGuardian`, `setTokens` avec plafonds, `setProviders`, `setPools` pour les pools profonds des DEX autorisés),
   signées par **votre** keystore propriétaire. Recommandé : propriétaire = portefeuille froid, exécuteur/gardien =
   portefeuille chaud dédié.
4. `ARB_EXECUTOR_ADDRESS` dans `.env`, `executor_contract` dans la politique, puis `arbbot verify-chain` à nouveau.
5. Redémarrez `arbbot serve` : les simulations utilisent désormais le contrat déployé (`mode: deployed`) ; vérifiez
   dans la table que `Net simulé` est renseigné et égal au net prévu (tolérance 1 bps) sur plusieurs blocs.

## D. Activation

1. Terminal 1 : `arbbot signer` (mot de passe du keystore saisi au clavier).
2. Terminal 2 : `arbbot serve` avec `ARB_SIGNER_TOKEN`.
3. Interface : vérifier le bandeau vert « RÉSEAU RÉEL — Base », le statut **PRÊT POUR TEST RÉEL LIMITÉ**, l'empreinte
   de la politique, le budget restant.
4. Bouton « réel autorisé » (interrupteur manuel) puis « activer le test réel limité ». Le statut passe à
   **MODE RÉEL ACTIF**.

Le moteur n'envoie une transaction que si, **au moment de l'envoi**, toutes les re-vérifications passent (prix et
liquidité re-lus, gaz re-estimé, frais recalculés, net ≥ `min_net_profit_native`, données fraîches, slippage par saut
encodé dans `minAmountOut`, remboursement du flash loan couvert, budget/compteur restants, listes blanches,
borne inférieure ≥ 75 %). Toute défaillance ⇒ rejet journalisé avec motif, pas de transaction.

## E. Pendant le test — ce que vous devez voir

* Onglet « Exécutions » : chaque tx avec hash, gaz, coût, net prévu, **net réalisé** (lu dans les reçus/soldes), erreur
  décodée en cas de revert.
* Onglet « Opportunités » : la décision `EXECUTED` ou `FAILED` sur la ligne concernée.
* KPI « Net réalisé (réel) » : cumul **gaz des échecs inclus**.

## F. Critères d'arrêt (automatiques) et retour en simulation

Suspension immédiate (statut **SUSPENDU**, aucune nouvelle signature, retour en mode ghost) si : 2 échecs consécutifs ;
perte cumulée ≥ `max_cumulative_loss_native` ; budget ou nombre de tx atteint ; politique expirée ; signer injoignable ;
données périmées ; dérive du modèle (succès réel < borne prédite − 15 pts) ; écart entre simulation et réalité
au-delà de la tolérance ; erreur RPC répétée. La reprise est **manuelle** (`auto_resume_after_suspension=false`).

Arrêt manuel : bouton rouge, `arbbot emergency-stop`, fermeture du signer, ou `pause()` sur le contrat.

## G. Lecture des résultats et décision suivante

Après la fenêtre de validité : exporter le rapport (`arbbot lab --minutes 10` produit un rapport de décision à jour) et
comparer **net réalisé** vs **net simulé** par transaction. Trois issues :

1. Net réalisé ≥ 0 sur la série et écart simulation/réalité ≤ 1 bps → on peut envisager une nouvelle fenêtre avec les
   mêmes plafonds (pas d'augmentation automatique : la politique est modifiée par vous seul).
2. Reverts dominants (`InsufficientProfit`, `HopOutputTooLow`) → la concurrence capte les écarts avant inclusion ;
   rester en ghost, laisser le laboratoire resserrer `min_spread_bps`/`safety_margin_bps`, mesurer à nouveau.
3. Écart simulation/réalité non expliqué → stop complet, analyse du trace (`debug_traceTransaction`), aucun nouveau
   test avant correction et nouvelle campagne de tests.

Le montant emprunté n'apparaît jamais dans les gains ; les profits restent dans le contrat jusqu'à `withdraw` par le
propriétaire.
