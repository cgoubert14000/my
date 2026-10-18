# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-18T09:04:17+00:00 ; durée 6.06 min ; blocs 52762270 → 52762454 (182 vus)

## Connexion
- Requêtes RPC : 2587 ; erreurs : 0 ; latence p50/p95 : 250.3/885.1 ms
- Rafraîchissements d'état : 183 ; âge des données au dernier bloc : 2.13 s ; changements de frais LP observés (pools à frais dynamiques) : 329
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 3004 ; cycles déclenchés par événement : 238 ; avance médiane sur le rafraîchissement multicall : 486 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,410.99 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 578 pools, 328 jetons, 21580 routes
- Par DEX : uniswap_v3 136, aerodrome 235, aerodrome_slipstream 157, pancakeswap_v3 32, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 207 (rejetés 2) → 612 jetons ; pools candidats 3915 (énumérés 394, par paires 0), mesurés 580, sous le plancher de 10000.0 $ : 2 → gardés 578 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'DAI': 1.0, 'USDC': 1.0, 'WETH': 2410.986474, 'AERO': 0.834015, 'cbBTC': 81629.281689}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 146,002,915 | 2,410.986474 | 52762454 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 41,943,409 | 1.199020 | 52762454 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 18,741,942 | 0.029544 | 52762454 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 500 | 18,199,696 | 0.029518 | 52762454 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 16,710,815 | 108.630407 | 52762454 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,397,688 | 0.029525 | 52762454 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,758,067 | 0.000012 | 52762454 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 9,056,978 | 2,411.607523 | 52762454 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome_slipstream | USDC/cbBTC | 336 | 7,854,325 | 0.000012 | 52762454 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 654 | 7,305,261 | 2,411.699195 | 52762454 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,131,123 | 0.001651 | 52762454 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 448 | 6,731,621 | 0.000012 | 52762454 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome | WETH/USDC | 3000 | 5,487,490 | 2,412.483415 | 52762454 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,325,843 | 0.029523 | 52762454 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/superOETHb | 400 | 5,235,628 | 1.000855 | 52762454 | `0x6446021F4E396dA3df4235C62537431372195D38` |
| aerodrome | fBOMB/AERO | 10000 | 5,130,979 | 0.025622 | 52762454 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,819,252 | 0.802398 | 52762454 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,622,280 | 0.000271 | 52762454 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,436,163 | 2,411.708074 | 52762454 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,435,173 | 0.998809 | 52762454 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome_slipstream | WETH/USDT | 424 | 4,399,705 | 2,414.858486 | 52762454 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome | WETH/KTA | 3000 | 4,085,409 | 33,032.545440 | 52762454 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | USDC/AERO | 10000 | 4,001,507 | 1.190506 | 52762454 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome | WETH/AERO | 10000 | 3,337,332 | 2,866.465547 | 52762454 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,912,140 | 1.141818 | 52762454 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,839,967 | 0.000012 | 52762454 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,739,384 | 409.810655 | 52762454 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | WETH/VVV | 2700 | 2,540,235 | 108.670809 | 52762454 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 2,515,237 | 0.000010 | 52762454 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | WETH/FAI | 10000 | 2,234,423 | 1,181,913.960766 | 52762454 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 2,174,265 | 1,008.717005 | 52762454 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,105,878 | 1.199991 | 52762454 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,035,374 | 1.374087 | 52762454 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| aerodrome_slipstream | EURC/USDC | 70 | 1,959,713 | 1.123477 | 52762454 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,953,781 | 15.851079 | 52762454 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,863,982 | 0.000000 | 52762454 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome | fBOMB/USDC | 10000 | 1,809,834 | 0.021550 | 52762454 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,789,980 | 13,891.622218 | 52762454 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,779,063 | 0.000012 | 52762454 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | XDP/USDC | 100 | 1,766,509 | 0.018614 | 52762454 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome | WETH/msETH (stable) | 500 | 1,670,177 | 2.306444 | 52762454 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome | weETH_04c0/WETH | 500 | 1,518,367 | 1.105495 | 52762454 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| uniswap_v3 | WETH/AERO | 3000 | 1,512,890 | 2,886.814836 | 52762454 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,465,413 | 0.916373 | 52762454 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,456,384 | 0.826249 | 52762454 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | WETH/AERO | 3000 | 1,451,916 | 2,886.606187 | 52762454 | `0x82321f3BEB69f503380D6B233857d5C43562e2D0` |
| uniswap_v3 | DRB/WETH | 10000 | 1,326,980 | 0.000000 | 52762454 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,318,580 | 0.435936 | 52762454 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,295,493 | 0.000270 | 52762454 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,295,477 | 0.004649 | 52762454 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome | WETH/cbBTC | 3000 | 1,255,606 | 0.029519 | 52762454 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| aerodrome | USDC/SEND | 3000 | 1,248,124 | 62.377421 | 52762454 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,243,807 | 23.372954 | 52762454 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,214,870 | 2,411.492978 | 52762454 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | WETH/doginme | 10000 | 1,191,511 | 35,920,805.594525 | 52762454 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome_slipstream | msUSD/USDC | 500 | 1,164,066 | 0.885699 | 52762454 | `0x7501bc8Bb51616F79bfA524E464fb7B41f0B10fB` |
| aerodrome | WETH/WELL | 10000 | 1,162,348 | 1,166,766.396236 | 52762454 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,160,976 | 1.105821 | 52762454 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |
| aerodrome_slipstream | WETH/msETH | 500 | 1,153,328 | 1.131512 | 52762454 | `0x74F72788F4814D7fF3C49B44684aa98Eee140C0E` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,133,378 | 516,942.421892 | 52762454 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |

## Recherche d'opportunités
- Cycles : 420 ; routes examinées : 9063600 ; candidats optimisés : 39424 ; net attendu > 0 : 7 ; dernier cycle 70.5 ms
- Rejets (moteur) : {'spread_below_threshold': 8958263, 'liquidity_below_min': 65493, 'negative_expected_net': 39417, 'borrow_bound_too_small': 420}
- Enregistrements de la session : 39424 ; net attendu > 0 : 7 ; simulés (eth_call de la vraie tx) : 0 (ok 0, échec 0) ; étiquettes ghost N+1 : 0/0 positives
- Décisions : {'REJECTED': 39424} ; motifs de rejet : {'below_safety_margin': 7, 'negative_expected_net': 39417, 'p_lower_below_threshold': 4, 'reliability_not_demonstrated': 3}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52762418 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 190.806253 USDC | 0.013787 USDC | 0.000000 USDC | 0.005413 USDC | 0.008374 USDC (0.0077 €) | — | 0.44 | 0.029 (n=28) | REJECTED | below_safety_margin(8374<38161), reliability_not_demonstrated |
| 52762418 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.079324 WETH | 0.000006 WETH | 0.000000 WETH | 0.000002 WETH | 0.000003 WETH (0.0077 €) | — | 0.44 | 0.029 (n=28) | REJECTED | below_safety_margin(3470697531420<15864845211956), reliability_not_demonstrated |
| 52762447 | USDC→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 45.394101 USDC | 0.015583 USDC | 0.000000 USDC | 0.007245 USDC | 0.008338 USDC (0.0077 €) | — | 1.84 | 0.340 (n=57) | REJECTED | below_safety_margin(8338<9078), p_lower_below_threshold(0.34<0.75) |
| 52762447 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→WETH | 0.018906 WETH | 0.000006 WETH | 0.000000 WETH | 0.000003 WETH | 0.000003 WETH (0.0077 €) | — | 1.83 | 0.340 (n=57) | REJECTED | below_safety_margin(3457677630276<3781255592517), p_lower_below_threshold(0.34<0.75) |
| 52762447 | USDC→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 46.204025 USDC | 0.015527 USDC | 0.000000 USDC | 0.007245 USDC | 0.008282 USDC (0.0076 €) | — | 1.79 | 0.138 (n=98) | REJECTED | below_safety_margin(8282<9240), p_lower_below_threshold(0.14<0.75) |
| 52762447 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→WETH | 0.019300 WETH | 0.000006 WETH | 0.000000 WETH | 0.000003 WETH | 0.000003 WETH (0.0076 €) | — | 1.78 | 0.138 (n=98) | REJECTED | below_safety_margin(3434465368246<3860081530203), p_lower_below_threshold(0.14<0.75) |
| 52762453 | USDC→[pancakeswap_v3]→PLAY→[aerodrome]→USDC | 7.404304 USDC | 0.005639 USDC | 0.000000 USDC | 0.005081 USDC | 0.000558 USDC (0.0005 €) | — | 0.75 | 0.001 (n=6) | REJECTED | below_safety_margin(558<1480), reliability_not_demonstrated |

## Fiabilité et décision
- Observations ghost : 863 ; taux observé 0.131 ; borne inférieure crédible (0.9) 0.117 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 11.7% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
