# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-24T00:15:33+00:00 ; durée 3.02 min ; blocs 53005699 → 53005792 (91 vus)

## Connexion
- Requêtes RPC : 1208 ; erreurs : 0 ; latence p50/p95 : 242.8/1,108.6 ms
- Rafraîchissements d'état : 92 ; âge des données au dernier bloc : 2.07 s ; changements de frais LP observés (pools à frais dynamiques) : 154
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 1465 ; cycles déclenchés par événement : 171 ; avance médiane sur le rafraîchissement multicall : 424 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,378.77 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 542 pools, 313 jetons, 19386 routes
- Par DEX : uniswap_v3 139, aerodrome 218, aerodrome_slipstream 136, pancakeswap_v3 32, uniswap_v2 13, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 197 (rejetés 2) → 602 jetons ; pools candidats 3863 (énumérés 353, par paires 0), mesurés 544, sous le plancher de 10000.0 $ : 2 → gardés 542 (max 1500) ; prix des hubs : {'USDC': 1.0, 'USDbC': 1.0, 'DAI': 1.0, 'WETH': 2378.764515, 'AERO': 0.72806, 'cbBTC': 80962.575526}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 156,506,533 | 2,378.765860 | 53005792 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,435,406 | 0.029414 | 53005792 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 12,509,457 | 95.017672 | 53005792 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,190,924 | 0.029339 | 53005792 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| aerodrome | USDC/AERO | 3000 | 9,869,430 | 1.373513 | 53005792 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,565,625 | 0.000012 | 53005792 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome_slipstream | WETH/cbBTC | 2505 | 8,761,733 | 0.029355 | 53005792 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/USDC | 500 | 8,658,318 | 2,379.630007 | 53005792 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,070,763 | 0.001655 | 53005792 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 348 | 6,313,559 | 0.000012 | 53005792 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 150 | 5,520,059 | 2,380.173193 | 53005792 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,401,515 | 0.029424 | 53005792 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | USDC/cbBTC | 508 | 4,879,829 | 0.000012 | 53005792 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,514,705 | 2,380.071575 | 53005792 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,256,525 | 0.999387 | 53005792 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/USDC | 3000 | 4,144,679 | 2,379.188874 | 53005792 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome | WETH/KTA | 3000 | 3,951,633 | 34,331.092283 | 53005792 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | VIRTUAL/WETH | 10000 | 3,347,890 | 0.000271 | 53005792 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/USDT | 424 | 2,790,979 | 2,383.718949 | 53005792 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome_slipstream | WETH/VVV | 2700 | 2,512,193 | 94.999647 | 53005792 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,267,646 | 404.795247 | 53005792 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | WETH/FAI | 10000 | 2,138,571 | 1,254,368.510904 | 53005792 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome | WETH/AERO | 10000 | 2,007,420 | 3,246.057020 | 53005792 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,931,867 | 0.000000 | 53005792 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,922,655 | 0.000012 | 53005792 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,738,819 | 0.000012 | 53005792 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | XDP/USDC | 100 | 1,730,326 | 0.017529 | 53005792 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,554,300 | 1.607287 | 53005792 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | WETH/AERO | 3000 | 1,491,807 | 3,269.265378 | 53005792 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,459,945 | 0.824708 | 53005792 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,390,952 | 13,756.109995 | 53005792 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,376,288 | 0.005038 | 53005792 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,287,774 | 2,379.543363 | 53005792 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,278,394 | 0.000271 | 53005792 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | WETH/msETH (stable) | 500 | 1,245,548 | 2.308280 | 53005792 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | DRB/WETH | 10000 | 1,228,120 | 0.000000 | 53005792 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | USDC/SEND | 3000 | 1,227,436 | 64.497791 | 53005792 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,183,022 | 35,616,621.346345 | 53005792 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | WETH/WELL | 10000 | 1,158,486 | 1,110,741.788047 | 53005792 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,137,315 | 495,610.449757 | 53005792 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | USDC/NOCK | 3000 | 1,136,824 | 48.478620 | 53005792 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,121,842 | 16.524715 | 53005792 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | WETH/EDEL | 7000 | 1,079,846 | 74,403.905318 | 53005792 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | USDC/VVV | 3000 | 1,064,756 | 0.039864 | 53005792 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,044,733 | 21,703,169.053283 | 53005792 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,035,353 | 17.192901 | 53005792 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 973,566 | 23.184730 | 53005792 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| uniswap_v3 | WETH/MORPHO | 3000 | 949,186 | 1,062.599831 | 53005792 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | uXRP/WETH | 3000 | 903,810 | 0.000541 | 53005792 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 881,714 | 17.849459 | 53005792 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 871,412 | 0.000009 | 53005792 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v2 | WETH/USDC | 3000 | 855,433 | 2,378.497134 | 53005792 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| pancakeswap_v3 | QUID/USDC | 100 | 836,654 | 0.063200 | 53005792 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | weETH_04c0/WETH | 500 | 821,933 | 1.105909 | 53005792 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome | WETH/wstETH | 3000 | 805,475 | 0.803010 | 53005792 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | WETH/USDC | 10000 | 791,050 | 2,373.719135 | 53005792 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/VVV | 10000 | 788,792 | 95.403421 | 53005792 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 767,899 | 0.644360 | 53005792 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 763,170 | 4,584,426.580791 | 53005792 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 735,017 | 0.676866 | 53005792 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |

## Recherche d'opportunités
- Cycles : 262 ; routes examinées : 5079132 ; candidats optimisés : 24606 ; net attendu > 0 : 0 ; dernier cycle 107.7 ms
- Rejets (moteur) : {'spread_below_threshold': 4974116, 'liquidity_below_min': 80148, 'negative_expected_net': 24606, 'borrow_bound_too_small': 262}
- Enregistrements de la session : 24606 ; net attendu > 0 : 0 ; simulés (eth_call de la vraie tx) : 0 (ok 0, échec 0) ; étiquettes ghost N+1 : 0/0 positives
- Décisions : {'REJECTED': 24606} ; motifs de rejet : {'negative_expected_net': 24606}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|

_Aucun candidat à net positif. Les 10 plus proches de la rentabilité (net attendu négatif) :_

| Bloc | Route | Montant | Brut | Frais flash | Gaz (dont L1) | Net attendu (€) | Marge (bps) |
|---:|---|---:|---:|---:|---:|---:|---:|
| 53005776 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→USDC | 48.527748 USDC | 0.003699 USDC | 0.000000 USDC | 0.007147 USDC | -0.0032 | -0.71 |
| 53005776 | WETH→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.020747 WETH | 0.000002 WETH | 0.000000 WETH | 0.000003 WETH | -0.0032 | -0.70 |
| 53005778 | WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.009797 WETH | 0.000002 WETH | 0.000000 WETH | 0.000003 WETH | -0.0032 | -1.52 |
| 53005778 | WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.009797 WETH | 0.000002 WETH | 0.000000 WETH | 0.000003 WETH | -0.0032 | -1.52 |
| 53005778 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC | 23.005326 USDC | 0.003615 USDC | 0.000000 USDC | 0.007147 USDC | -0.0032 | -1.54 |
| 53005778 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC | 23.005326 USDC | 0.003615 USDC | 0.000000 USDC | 0.007147 USDC | -0.0032 | -1.54 |
| 53005786 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 11.146052 USDC | 0.001671 USDC | 0.000000 USDC | 0.005341 USDC | -0.0034 | -3.29 |
| 53005786 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.004716 WETH | 0.000001 WETH | 0.000000 WETH | 0.000002 WETH | -0.0034 | -3.27 |
| 53005785 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.004716 WETH | 0.000001 WETH | 0.000000 WETH | 0.000002 WETH | -0.0034 | -3.27 |
| 53005785 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.004716 WETH | 0.000001 WETH | 0.000000 WETH | 0.000002 WETH | -0.0034 | -3.27 |

## Fiabilité et décision
- Observations ghost : 2084 ; taux observé 0.098 ; borne inférieure crédible (0.9) 0.090 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 9.0% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
