# 02 — Choix du réseau, des protocoles et de la stratégie (Phase B)

## Contraintes de départ

* Budget personnel de l'utilisateur pour **frais de test et transactions échouées : 10–20 € maximum** (le montant du flash
  loan n'est pas un budget — il est emprunté et remboursé dans la même transaction, sinon tout est annulé).
* Une transaction échouée coûte le gaz consommé jusqu'au revert. Le nombre d'essais possibles avec 10–20 € est donc
  **directement** fonction du coût du gaz du réseau.
* Important : cet environnement de travail **n'a pas accès aux RPC publics**. Les chiffres ci-dessous proviennent de la
  documentation des réseaux et de publications récentes (références en bas) ; ils doivent être **remesurés** avec
  `arbbot verify-chain` sur votre machine, qui lit en direct le base fee, le prix L1, la liquidité des pools et les frais
  des fournisseurs de flash loans.

## Comparaison

| Critère | Ethereum L1 | Base (OP Stack) | Arbitrum One |
|---|---|---|---|
| Coût d'une tx d'arbitrage 3 sauts (~350–450 k gaz) | 5–40 € selon congestion | ≈ 0,01–0,05 € (base fee ~0,01 gwei + données L1) | ≈ 0,02–0,08 € |
| Essais possibles avec 15 € | 0–3 | plusieurs centaines | plusieurs centaines |
| Temps de bloc | 12 s | 2 s, sous-blocs **Flashblocks 200 ms** depuis juillet 2025 | ~250 ms |
| Mempool | publique + Flashbots | **privée** (séquenceur) → pas de frontrunning, MEV = backrunning | **privée** (séquenceur) + Timeboost (enchère de voie express, avril 2025) |
| DEX utiles | Uniswap V2/V3, Curve, Balancer, Sushi | Uniswap V3/V2, **Aerodrome** (Solidly), SushiSwap, PancakeSwap V3, BaseSwap | Uniswap V3, Camelot, SushiSwap, PancakeSwap V3, Balancer |
| Flash loans | Aave V3 (0,05 %), Balancer V2 (0 %), Morpho (0 %), Uniswap V3 flash (frais du pool) | Aave V3 (0,05 %), **Morpho Blue (0 %)**, Balancer V2 (0 %, liquidité incertaine depuis l'exploit de nov. 2025), Uniswap V3 flash | Aave V3 (0,05 %), Balancer V2 (0 %), Uniswap V3 flash ; Morpho adresse à vérifier |
| Concurrence | extrême (searchers professionnels, bundles) | forte : des études 2025–2026 estiment que **deux entités captent ≈ 80 %+ de la MEV** sur Base ; spam de reverts coûteux pendant les enchères de priorité | forte ; Timeboost donne un avantage de 200 ms à l'acheteur de la voie express |
| Pertinence pour un budget de 15 € | **exclu** (un échec = le budget) | **meilleur rapport coût/essai** | second choix |

## Décision

1. **Réseau de départ : Base** (chain id 8453). Raison principale : coût par essai le plus bas, écosystème DEX
   hétérogène (V2 + V3 + Solidly → plus d'écarts structurels entre courbes différentes), Morpho Blue à 0 % de frais.
   Risque principal : concurrence concentrée et Flashblocks (enchère de priorité toutes les 200 ms) → **le mode ghost
   doit d'abord mesurer la part réellement capturable au bloc N+1** avant tout test réel.
2. **Réseau secondaire : Arbitrum One** (chain id 42161), configuré dans `config/chains.py`, activable par
   `ARB_CHAIN=arbitrum`. Même code ; seul le calcul du coût L1 et la liste des pools changent.
3. **Ethereum L1 : exclu** pour ce budget. **Pas d'arbitrage inter-chaînes** : aucune atomicité possible entre deux
   chaînes, donc risque de perte réel — hors périmètre.

## Stratégie retenue

* **Arbitrage atomique intra-bloc** : flash loan → 2 ou 3 swaps formant un cycle qui revient au token emprunté →
  remboursement → profit. Si le profit est inférieur à `minProfit`, la transaction **revert** : la seule perte possible
  est le gaz.
* **Token de départ** : WETH ou USDC (les plus liquides, remboursables partout). Montant optimisé par route, plafonné à
  25 % de la profondeur du pool le moins liquide et à l'impact de prix maximal (150 bps).
* **Fournisseur de flash loan** : choisi par coût effectif pour le montant (Morpho 0 % → Balancer 0 % si liquidité →
  Aave 0,05 % → flash Uniswap V3 au prix du pool), avec vérification on-chain de la liquidité disponible.
* **Seuil d'entrée** : filtre vectorisé par bloc sur les ~190 000 cycles — l'écart brut des prix marginaux doit dépasser
  la somme des frais LP de la route d'au moins `min_spread_bps` (0,05 bps par défaut : un cycle dont l'écart est sous
  ses frais ne peut être rentable à aucune taille ; le laboratoire peut ajuster cette marge), puis dimensionnement des
  survivants par ordre d'écart décroissant dans un budget de temps (1,2 s), net prévu > 0 **et** supérieur au plancher
  de sécurité on-chain, **et** probabilité (borne inférieure) ≥ 75 % que le net reste positif au bloc suivant.
* **Soumission** : RPC public du séquenceur (pas de mempool publique sur Base/Arbitrum). Le gain possible d'un relais
  privé est nul ici ; la seule « protection MEV » utile est la garde `minProfit` on-chain et `minAmountOut` par saut.

## Univers surveillé (élargi le 13/10, sessions 9+)

Le but fixé par l'opérateur est de voir **le plus d'opportunités possible**. L'univers n'est donc plus une liste
fixe de 7 jetons mais est **construit à chaque démarrage** et mesuré on-chain :

1. **Hubs** = les jetons vérifiés de la configuration (WETH, USDC, USDbC, DAI, cbETH, cbBTC, AERO) ; seuls
   WETH, USDC et cbBTC sont **empruntables** (capacité de flash loan mesurée en direct).
2. **Longue traîne** = 407 jetons Base des listes publiques `@uniswap/default-token-list@22.26.0` et
   `ethereum-optimism.github.io` (v10.0.1769), plus tous les jetons ayant un pool Aerodrome/Slipstream contre un hub
   (énumération `allPools` des deux factories). Chaque jeton est contrôlé (`decimals()` cohérent) ; ils ne sont
   **jamais empruntés** et un faux « USDC » n'est jamais pris pour un dollar (les stables sont reconnus par adresse).
3. **Pools** = toutes les paires hub×jeton et hub×hub sur les 8 factories (Uniswap V2/V3, Sushi V2/V3, Pancake V2/V3,
   Aerodrome, Slipstream) + les pools énumérés : profondeur réelle (`balanceOf`) valorisée avec les prix des hubs ;
   plancher 10 k$, plafond 1 500 pools (les plus profonds), paramétrables.
4. **Routes** = cycles hub → X → hub (2 sauts, deux pools différents) et hub → X → Y → hub (3 sauts), table numpy.
5. **Protection** : un pool de la longue traîne dont les routes « positives » échouent 5 fois de suite en
   simulation est mis en quarantaine 300 blocs (modèle ≠ chaîne : frais dynamiques, jeton à frais de transfert,
   ticks périmés…) ; les pools hub×hub en sont exempts. La simulation du contrat reste le juge final.

Ce que cela change pour l'honnêteté des chiffres : plus de routes dimensionnées ne veut pas dire plus de profit ;
seuls les candidats **simulés avec succès puis confirmés au bloc N+1** comptent dans la fiabilité.

## Références

* Documentation Aave V3 — flash loans : premium initialisé à 0,05 % (`FLASHLOAN_PREMIUM_TOTAL`), remboursement par allowance.
* Documentation Morpho Blue — `flashLoan(token, assets, data)`, callback `onMorphoFlashLoan`, frais 0, remboursement par `transferFrom`.
* Balancer post-mortem (nov. 2025) : exploit des Composable Stable Pools V2 (~117–128 M$ sur Ethereum/Base/Arbitrum), migration vers V3 ; la Vault V2 reste immuable mais la liquidité disponible a chuté.
* arXiv 2506.01462 et arXiv 2601.19570 (MEV sur rollups), analyses Flashblocks (Base, 2025) : sous-blocs de 200 ms, enchère par priority fee, concentration de la capture ; Timeboost (Arbitrum, avril 2025).
* Les montants en euros affichés utilisent `ARB_EUR_PER_USD` (0,92 par défaut) et le prix ETH dérivé des pools ; à ajuster.
