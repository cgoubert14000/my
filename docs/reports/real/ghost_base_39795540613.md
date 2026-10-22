# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-22T18:34:48+00:00 ; durée 243.12 min ; blocs 52945073 → 52952363 (6730 vus)

## Connexion
- Requêtes RPC : 83317 ; erreurs : 8 ; latence p50/p95 : 398.1/1,602.3 ms
- Rafraîchissements d'état : 6730 ; âge des données au dernier bloc : 3.41 s ; changements de frais LP observés (pools à frais dynamiques) : 16520
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 147833 ; cycles déclenchés par événement : 5611 ; avance médiane sur le rafraîchissement multicall : 1,150 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,378.82 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 546 pools, 318 jetons, 19398 routes
- Par DEX : uniswap_v3 137, aerodrome 226, aerodrome_slipstream 137, pancakeswap_v3 30, uniswap_v2 13, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 198 (rejetés 2) → 603 jetons ; pools candidats 3827 (énumérés 366, par paires 0), mesurés 549, sous le plancher de 10000.0 $ : 3 → gardés 546 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'DAI': 1.0, 'USDC': 1.0, 'WETH': 2404.811718, 'AERO': 0.81356, 'cbBTC': 81633.413427}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 155,448,009 | 2,378.819051 | 52952362 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 18,115,877 | 1.247521 | 52952362 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,181,480 | 0.029298 | 52952362 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 15,369,021 | 92.642222 | 52952362 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,223,158 | 0.029247 | 52952362 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,786,196 | 0.000012 | 52952362 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 9,122,852 | 0.029260 | 52952362 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/USDC | 500 | 8,667,349 | 2,376.538264 | 52952362 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,123,300 | 0.001667 | 52952362 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 340 | 6,796,576 | 0.000012 | 52952362 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 579 | 5,792,222 | 2,377.117094 | 52952362 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,355,387 | 0.029298 | 52952362 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | USDC/cbBTC | 436 | 5,268,810 | 0.000012 | 52952362 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,466,298 | 2,377.108234 | 52952362 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | WETH/USDC | 3000 | 4,293,008 | 2,380.304522 | 52952362 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,269,628 | 1.000001 | 52952362 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,943,569 | 34,484.037326 | 52952362 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | VIRTUAL/WETH | 10000 | 3,427,074 | 0.000274 | 52952362 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/USDT | 403 | 2,896,968 | 2,380.829597 | 52952362 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome_slipstream | WETH/VVV | 2790 | 2,542,631 | 92.663465 | 52952362 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | WETH/AERO | 10000 | 2,326,218 | 2,981.678209 | 52952362 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,280,987 | 398.621899 | 52952362 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | WETH/FAI | 10000 | 2,188,255 | 1,198,899.323792 | 52952362 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,911,771 | 0.000012 | 52952362 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,882,007 | 0.000000 | 52952362 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,810,371 | 0.018360 | 52952362 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,746,371 | 0.000012 | 52952362 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,657,271 | 1.525093 | 52952362 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | WETH/AERO | 3000 | 1,618,900 | 2,969.347920 | 52952362 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,457,509 | 0.823520 | 52952362 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,401,740 | 13,607.138227 | 52952362 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,362,492 | 0.004993 | 52952362 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,327,784 | 2,376.620834 | 52952362 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,285,431 | 0.000272 | 52952362 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | WETH/msETH (stable) | 500 | 1,284,094 | 2.369350 | 52952362 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | DRB/WETH | 10000 | 1,265,769 | 0.000000 | 52952362 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | USDC/SEND | 3000 | 1,229,636 | 64.267198 | 52952362 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,180,390 | 35,719,093.925702 | 52952362 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,166,817 | 16.372841 | 52952362 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | WETH/WELL | 10000 | 1,165,141 | 1,107,113.506419 | 52952362 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,138,661 | 500,017.713432 | 52952362 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | USDC/NOCK | 3000 | 1,132,565 | 48.925158 | 52952362 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 1,089,030 | 0.000010 | 52952362 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | weETH_04c0/WETH | 500 | 1,086,007 | 1.105751 | 52952362 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome | WETH/EDEL | 7000 | 1,077,384 | 75,268.757737 | 52952362 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,057,223 | 21,256,834.056548 | 52952362 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,039,606 | 17.008756 | 52952362 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | WETH/cbBTC | 3000 | 1,007,257 | 0.029253 | 52952362 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,003,134 | 22.993004 | 52952362 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| uniswap_v3 | USDC/VVV | 3000 | 980,074 | 0.038972 | 52952362 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/MORPHO | 3000 | 954,957 | 1,053.257965 | 52952362 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/USDC | 10000 | 936,680 | 2,381.973244 | 52952362 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | uXRP/WETH | 3000 | 908,781 | 0.000546 | 52952362 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome | WETH/bsdETH | 100 | 886,078 | 0.916103 | 52952362 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 881,164 | 17.851352 | 52952362 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v2 | WETH/USDC | 3000 | 872,858 | 2,372.981523 | 52952362 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome | WETH/wstETH | 3000 | 805,942 | 0.803225 | 52952362 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| aerodrome | fBOMB/USDC | 10000 | 800,730 | 0.018522 | 52952362 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 795,918 | 1.106137 | 52952362 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 785,101 | 0.647131 | 52952362 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |

## Recherche d'opportunités
- Cycles : 12340 ; routes examinées : 239371320 ; candidats optimisés : 1564917 ; net attendu > 0 : 914 ; dernier cycle 666.9 ms
- Rejets (moteur) : {'spread_below_threshold': 235295770, 'liquidity_below_min': 2153216, 'negative_expected_net': 1564003, 'pool_quarantined': 336472, 'borrow_bound_too_small': 12335, 'cycle_budget_exhausted': 8610}
- Enregistrements de la session : 1564917 ; net attendu > 0 : 914 ; simulés (eth_call de la vraie tx) : 50 (ok 23, échec 27) ; étiquettes ghost N+1 : 9/42 positives
- Décisions : {'REJECTED': 1564917} ; motifs de rejet : {'below_safety_margin': 570, 'negative_expected_net': 1564003, 'p_lower_below_threshold': 769, 'reliability_not_demonstrated': 145, 'sim_below_estimate': 7, 'simulated_net_nonpositive': 5, 'simulation_failed': 27, 'stale_data': 37}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52951944 | WETH→[pancakeswap_v3]→USDC→[aerodrome]→VIRTUAL→[aerodrome_slipstream]→WETH | 0.114400 WETH | 0.000530 WETH | 0.000000 WETH | 0.000003 WETH | 0.000527 WETH (1.1535 €) | — | 46.07 | 0.001 (n=7) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52951944 | USDC→[aerodrome]→VIRTUAL→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 272.048629 USDC | 1.260405 USDC | 0.000000 USDC | 0.007221 USDC | 1.253184 USDC (1.1529 €) | — | 46.06 | 0.001 (n=7) | REJECTED | reliability_not_demonstrated |
| 52951944 | WETH→[uniswap_v3]→USDC→[aerodrome]→VIRTUAL→[aerodrome_slipstream]→WETH | 0.113195 WETH | 0.000524 WETH | 0.000000 WETH | 0.000003 WETH | 0.000521 WETH (1.1407 €) | — | 46.05 | 0.003 (n=86) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 52951944 | USDC→[aerodrome]→VIRTUAL→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 268.915647 USDC | 1.246379 USDC | 0.000000 USDC | 0.007221 USDC | 1.239158 USDC (1.1400 €) | — | 46.08 | 0.003 (n=86) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 52951944 | WETH→[pancakeswap_v3]→USDC→[aerodrome]→VIRTUAL→[uniswap_v3]→WETH | 0.115631 WETH | 0.000510 WETH | 0.000000 WETH | 0.000003 WETH | 0.000508 WETH (1.1109 €) | — | 43.90 | 0.001 (n=7) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52951944 | USDC→[aerodrome]→VIRTUAL→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 274.569541 USDC | 1.213745 USDC | 0.000000 USDC | 0.006859 USDC | 1.206886 USDC (1.1103 €) | — | 43.96 | 0.001 (n=7) | REJECTED | reliability_not_demonstrated |
| 52951944 | WETH→[uniswap_v3]→USDC→[aerodrome]→VIRTUAL→[uniswap_v3]→WETH | 0.114198 WETH | 0.000505 WETH | 0.000000 WETH | 0.000003 WETH | 0.000502 WETH (1.0978 €) | — | 43.93 | 0.003 (n=86) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 52951944 | USDC→[aerodrome]→VIRTUAL→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 271.428494 USDC | 1.199465 USDC | 0.000000 USDC | 0.006859 USDC | 1.192606 USDC (1.0972 €) | — | 43.94 | 0.003 (n=86) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 52951944 | WETH→[pancakeswap_v3]→USDC→[aerodrome]→VIRTUAL→[aerodrome_slipstream]→WETH | 0.112125 WETH | 0.000479 WETH | 0.000000 WETH | 0.000003 WETH | 0.000477 WETH (1.0429 €) | — | 42.50 | 0.001 (n=7) | REJECTED | reliability_not_demonstrated |
| 52951944 | USDC→[aerodrome]→VIRTUAL→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 266.340631 USDC | 1.139901 USDC | 0.000000 USDC | 0.006859 USDC | 1.133042 USDC (1.0424 €) | — | 42.54 | 0.001 (n=7) | REJECTED | reliability_not_demonstrated |
| 52951944 | WETH→[uniswap_v3]→USDC→[aerodrome]→VIRTUAL→[aerodrome_slipstream]→WETH | 0.110744 WETH | 0.000474 WETH | 0.000000 WETH | 0.000003 WETH | 0.000471 WETH (1.0307 €) | — | 42.52 | 0.003 (n=86) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 52951944 | USDC→[aerodrome]→VIRTUAL→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 263.243093 USDC | 1.126488 USDC | 0.000000 USDC | 0.006859 USDC | 1.119629 USDC (1.0301 €) | — | 42.53 | 0.003 (n=86) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 52951944 | WETH→[aerodrome_slipstream]→USDC→[aerodrome]→VIRTUAL→[aerodrome_slipstream]→WETH | 0.107551 WETH | 0.000467 WETH | 0.000000 WETH | 0.000003 WETH | 0.000464 WETH (1.0156 €) | — | 43.15 | 0.003 (n=86) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 52951944 | USDC→[aerodrome]→VIRTUAL→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→USDC | 255.452968 USDC | 1.109949 USDC | 0.000000 USDC | 0.007221 USDC | 1.102728 USDC (1.0145 €) | — | 43.17 | 0.003 (n=86) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 52951944 | WETH→[uniswap_v3]→USDC→[aerodrome]→VIRTUAL→[aerodrome_slipstream]→WETH | 0.106858 WETH | 0.000461 WETH | 0.000000 WETH | 0.000003 WETH | 0.000458 WETH (1.0030 €) | — | 42.89 | 0.003 (n=86) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 52951944 | USDC→[aerodrome]→VIRTUAL→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 253.879274 USDC | 1.096273 USDC | 0.000000 USDC | 0.007221 USDC | 1.089052 USDC (1.0019 €) | — | 42.90 | 0.003 (n=86) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 52951944 | WETH→[pancakeswap_v3]→USDC→[aerodrome]→VIRTUAL→[aerodrome_slipstream]→WETH | 0.106558 WETH | 0.000460 WETH | 0.000000 WETH | 0.000003 WETH | 0.000457 WETH (1.0002 €) | — | 42.89 | 0.001 (n=7) | REJECTED | reliability_not_demonstrated |
| 52951944 | USDC→[aerodrome]→VIRTUAL→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 253.192610 USDC | 1.093137 USDC | 0.000000 USDC | 0.007221 USDC | 1.085916 USDC (0.9990 €) | — | 42.89 | 0.001 (n=7) | REJECTED | reliability_not_demonstrated |
| 52951944 | USDC→[aerodrome]→VIRTUAL→[pancakeswap_v3]→USDC | 243.659819 USDC | 1.067942 USDC | 0.000000 USDC | 0.005044 USDC | 1.062898 USDC (0.9779 €) | — | 43.62 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52951944 | WETH→[aerodrome_slipstream]→USDC→[aerodrome]→VIRTUAL→[uniswap_v3]→WETH | 0.108265 WETH | 0.000447 WETH | 0.000000 WETH | 0.000003 WETH | 0.000444 WETH (0.9719 €) | — | 41.02 | 0.003 (n=86) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 52951944 | USDC→[aerodrome]→VIRTUAL→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 257.000275 USDC | 1.062140 USDC | 0.000000 USDC | 0.006859 USDC | 1.055281 USDC (0.9709 €) | — | 41.06 | 0.003 (n=86) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 52951944 | WETH→[uniswap_v3]→USDC→[aerodrome]→VIRTUAL→[uniswap_v3]→WETH | 0.107510 WETH | 0.000441 WETH | 0.000000 WETH | 0.000003 WETH | 0.000438 WETH (0.9593 €) | — | 40.77 | 0.003 (n=86) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 52951944 | USDC→[aerodrome]→VIRTUAL→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 255.487767 USDC | 1.048381 USDC | 0.000000 USDC | 0.006859 USDC | 1.041522 USDC (0.9582 €) | — | 40.77 | 0.003 (n=86) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 52951944 | WETH→[pancakeswap_v3]→USDC→[aerodrome]→VIRTUAL→[uniswap_v3]→WETH | 0.107150 WETH | 0.000440 WETH | 0.000000 WETH | 0.000003 WETH | 0.000437 WETH (0.9564 €) | — | 40.78 | 0.001 (n=7) | REJECTED | reliability_not_demonstrated |
| 52951944 | USDC→[aerodrome]→VIRTUAL→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 254.584106 USDC | 1.045205 USDC | 0.000000 USDC | 0.006859 USDC | 1.038346 USDC (0.9553 €) | — | 40.79 | 0.001 (n=7) | REJECTED | reliability_not_demonstrated |

## Fiabilité et décision
- Observations ghost : 1927 ; taux observé 0.096 ; borne inférieure crédible (0.9) 0.088 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 8.8% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
