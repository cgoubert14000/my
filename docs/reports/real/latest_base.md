# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-21T04:35:48+00:00 ; durée 324.82 min ; blocs 52874252 → 52883990 (8945 vus)

## Connexion
- Requêtes RPC : 126710 ; erreurs : 505 ; latence p50/p95 : 290.0/1,737.1 ms
- Rafraîchissements d'état : 8945 ; âge des données au dernier bloc : 3.18 s ; changements de frais LP observés (pools à frais dynamiques) : 20412
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 136744 ; cycles déclenchés par événement : 9909 ; avance médiane sur le rafraîchissement multicall : 1,253 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,447.94 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 581 pools, 328 jetons, 22996 routes
- Par DEX : uniswap_v3 137, aerodrome 236, aerodrome_slipstream 158, pancakeswap_v3 32, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 208 (rejetés 2) → 613 jetons ; pools candidats 3925 (énumérés 395, par paires 0), mesurés 583, sous le plancher de 10000.0 $ : 2 → gardés 581 (max 1500) ; prix des hubs : {'USDC': 1.0, 'DAI': 1.0, 'USDbC': 1.0, 'WETH': 2453.717243, 'AERO': 0.88311, 'cbBTC': 82924.161646}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 148,504,378 | 2,447.941911 | 52883990 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 38,797,807 | 1.163497 | 52883990 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 18,549,053 | 0.029563 | 52883990 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/VVV | 3000 | 18,135,055 | 93.729768 | 52883990 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,486,371 | 0.029527 | 52883990 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,549,042 | 0.029573 | 52883990 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,929,711 | 0.000012 | 52883990 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 8,613,547 | 2,441.843263 | 52883990 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/USDC | 3000 | 8,378,537 | 2,447.876544 | 52883990 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | USDC/cbBTC | 332 | 8,168,917 | 0.000012 | 52883990 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 564 | 7,738,333 | 2,442.670602 | 52883990 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,270,669 | 0.001669 | 52883990 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 412 | 6,603,014 | 0.000012 | 52883990 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,543,863 | 0.029518 | 52883990 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | fBOMB/AERO | 10000 | 5,275,047 | 0.024753 | 52883990 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,718,539 | 0.802394 | 52883990 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,700,998 | 0.000277 | 52883990 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,508,919 | 2,442.647848 | 52883990 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,395,176 | 0.998741 | 52883990 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome_slipstream | WETH/USDT | 418 | 4,342,068 | 2,445.021863 | 52883990 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome | WETH/KTA | 3000 | 4,045,510 | 34,727.971498 | 52883990 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | USDC/AERO | 10000 | 3,481,697 | 1.156821 | 52883990 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome | WETH/AERO | 10000 | 3,374,205 | 2,828.529002 | 52883990 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,780,566 | 396.774941 | 52883990 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | WETH/VVV | 2718 | 2,770,840 | 93.705209 | 52883990 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,535,921 | 1.142084 | 52883990 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 2,351,499 | 0.000010 | 52883990 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,272,797 | 0.000012 | 52883990 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | WETH/FAI | 10000 | 2,241,753 | 1,210,470.665103 | 52883990 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 2,074,469 | 0.000012 | 52883990 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,058,907 | 1.238864 | 52883990 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,028,014 | 1.383164 | 52883990 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,948,716 | 0.000000 | 52883990 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome | weETH_04c0/WETH | 500 | 1,916,164 | 1.105697 | 52883990 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,912,722 | 15.719841 | 52883990 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| uniswap_v3 | XDP/USDC | 100 | 1,819,846 | 0.019423 | 52883990 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,775,278 | 13,432.180365 | 52883990 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | fBOMB/USDC | 10000 | 1,715,649 | 0.021478 | 52883990 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| aerodrome | WETH/msETH (stable) | 500 | 1,689,465 | 2.311241 | 52883990 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | WETH/AERO | 3000 | 1,684,889 | 2,844.523176 | 52883990 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,569,680 | 0.916062 | 52883990 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,456,348 | 0.826534 | 52883990 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | EURC/USDC | 73 | 1,424,112 | 1.122757 | 52883990 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,353,125 | 0.004809 | 52883990 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v3 | DRB/WETH | 10000 | 1,334,808 | 0.000000 | 52883990 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,328,357 | 0.000277 | 52883990 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | WETH/cbBTC | 3000 | 1,310,006 | 0.029583 | 52883990 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,260,731 | 2,441.828627 | 52883990 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,235,880 | 63.619362 | 52883990 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,222,695 | 34,988,111.001513 | 52883990 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,221,207 | 23.087745 | 52883990 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| aerodrome | WETH/EDEL | 7000 | 1,212,084 | 69,535.249779 | 52883990 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | WETH/WELL | 10000 | 1,194,393 | 1,138,861.018689 | 52883990 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,181,280 | 0.436726 | 52883990 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,179,213 | 484,625.715711 | 52883990 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 1,175,001 | 1,065.858691 | 52883990 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome_slipstream | msUSD/USDC | 500 | 1,160,548 | 0.886257 | 52883990 | `0x7501bc8Bb51616F79bfA524E464fb7B41f0B10fB` |
| aerodrome | USDC/NOCK | 3000 | 1,157,849 | 47.000369 | 52883990 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | WETH/VVV | 8000 | 1,154,984 | 94.197531 | 52883990 | `0x46D398A5b33709877f50c8918A7eE96F1Be1d7dd` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,153,730 | 1.106158 | 52883990 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |

## Recherche d'opportunités
- Cycles : 18853 ; routes examinées : 433543588 ; candidats optimisés : 2016117 ; net attendu > 0 : 308 ; dernier cycle 459.4 ms
- Rejets (moteur) : {'spread_below_threshold': 428800036, 'liquidity_below_min': 2704379, 'negative_expected_net': 2015809, 'borrow_bound_too_small': 18845, 'cycle_budget_exhausted': 2945, 'pool_quarantined': 1266}
- Enregistrements de la session : 2016117 ; net attendu > 0 : 308 ; simulés (eth_call de la vraie tx) : 30 (ok 2, échec 28) ; étiquettes ghost N+1 : 1/26 positives
- Décisions : {'REJECTED': 2016117} ; motifs de rejet : {'below_safety_margin': 214, 'negative_expected_net': 2015809, 'p_lower_below_threshold': 224, 'price_impact': 4, 'reliability_not_demonstrated': 84, 'simulation_failed': 28, 'stale_data': 3}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52875037 | cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.066092 cbBTC | 0.000013 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000013 cbBTC (1.0071 €) | — | 1.99 | 0.121 (n=191) | REJECTED | below_safety_margin(1318<1321), p_lower_below_threshold(0.12<0.75) |
| 52875037 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 2.265299 WETH | 0.000450 WETH | 0.000000 WETH | 0.000004 WETH | 0.000446 WETH (1.0070 €) | — | 1.97 | 0.121 (n=191) | REJECTED | below_safety_margin(446424932766654<453059794501778), p_lower_below_threshold(0.12<0.75) |
| 52875037 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 5,542.392478 USDC | 1.100381 USDC | 0.000000 USDC | 0.008858 USDC | 1.091523 USDC (1.0042 €) | — | 1.97 | 0.121 (n=191) | REJECTED | below_safety_margin(1091523<1108478), p_lower_below_threshold(0.12<0.75) |
| 52875037 | WETH→[pancakeswap_v3]→cbBTC→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 1.856803 WETH | 0.000405 WETH | 0.000000 WETH | 0.000003 WETH | 0.000402 WETH (0.9060 €) | — | 2.16 | 0.121 (n=191) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.12<0.75) |
| 52875037 | cbBTC→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.054128 cbBTC | 0.000012 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000012 cbBTC (0.9055 €) | — | 2.19 | 0.121 (n=191) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52875037 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[uniswap_v3]→USDC | 4,543.083362 USDC | 0.990633 USDC | 0.000000 USDC | 0.008486 USDC | 0.982147 USDC (0.9036 €) | — | 2.16 | 0.121 (n=191) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52875037 | cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.044885 cbBTC | 0.000010 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000010 cbBTC (0.7427 €) | — | 2.17 | 0.121 (n=191) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52875037 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 1.508351 WETH | 0.000333 WETH | 0.000000 WETH | 0.000003 WETH | 0.000329 WETH (0.7426 €) | — | 2.18 | 0.121 (n=191) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.12<0.75) |
| 52875037 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 3,746.366650 USDC | 0.813956 USDC | 0.000000 USDC | 0.008486 USDC | 0.805470 USDC (0.7410 €) | — | 2.15 | 0.121 (n=191) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52875037 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 1.097300 WETH | 0.000264 WETH | 0.000000 WETH | 0.000003 WETH | 0.000261 WETH (0.5886 €) | — | 2.38 | 0.002 (n=5) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52875037 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.031367 cbBTC | 0.000008 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000008 cbBTC (0.5884 €) | — | 2.45 | 0.002 (n=5) | REJECTED | reliability_not_demonstrated |
| 52875037 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 2,707.137311 USDC | 0.646054 USDC | 0.000000 USDC | 0.008113 USDC | 0.637941 USDC (0.5869 €) | — | 2.36 | 0.002 (n=5) | REJECTED | reliability_not_demonstrated |
| 52875037 | WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 1.670930 WETH | 0.000198 WETH | 0.000000 WETH | 0.000003 WETH | 0.000194 WETH (0.4380 €) | — | 1.16 | 0.121 (n=191) | REJECTED | below_safety_margin(194195621492476<334186067878125), p_lower_below_threshold(0.12<0.75) |
| 52875037 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC | 4,079.285042 USDC | 0.482887 USDC | 0.000000 USDC | 0.008113 USDC | 0.474774 USDC (0.4368 €) | — | 1.16 | 0.121 (n=191) | REJECTED | below_safety_margin(474774<815857), p_lower_below_threshold(0.12<0.75) |
| 52875037 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.444605 WETH | 0.000125 WETH | 0.000000 WETH | 0.000002 WETH | 0.000122 WETH (0.2759 €) | — | 2.75 | 0.014 (n=57) | REJECTED | p_lower_below_threshold(0.01<0.75) |
| 52875037 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 1,085.819408 USDC | 0.304823 USDC | 0.000000 USDC | 0.005878 USDC | 0.298945 USDC (0.2750 €) | — | 2.75 | 0.014 (n=57) | REJECTED | p_lower_below_threshold(0.01<0.75) |
| 52883688 | USDC→[aerodrome_slipstream]→LCAP→[aerodrome]→USDC | 9.591827 USDC | 0.302514 USDC | 0.000000 USDC | 0.005160 USDC | 0.297354 USDC (0.2736 €) | — | 310.01 | 0.002 (n=5) | REJECTED | reliability_not_demonstrated |
| 52878400 | WETH→[aerodrome_slipstream]→uNEAR→[uniswap_v3]→WETH | 0.076268 WETH | 0.000123 WETH | 0.000000 WETH | 0.000002 WETH | 0.000121 WETH (0.2730 €) | — | 15.89 | 0.002 (n=4) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52878399 | WETH→[aerodrome_slipstream]→uNEAR→[uniswap_v3]→WETH | 0.076268 WETH | 0.000123 WETH | 0.000000 WETH | 0.000002 WETH | 0.000121 WETH (0.2730 €) | — | 15.89 | 0.002 (n=4) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52883688 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→LCAP→[aerodrome_slipstream]→WETH | 0.003928 WETH | 0.000118 WETH | 0.000000 WETH | 0.000003 WETH | 0.000115 WETH (0.2591 €) | — | 292.85 | 0.001 (n=7) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52883688 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→LCAP→[aerodrome_slipstream]→WETH | 0.003928 WETH | 0.000118 WETH | 0.000000 WETH | 0.000003 WETH | 0.000115 WETH (0.2590 €) | — | 292.71 | 0.002 (n=5) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52883688 | WETH→[aerodrome]→USDC→[aerodrome_slipstream]→LCAP→[aerodrome_slipstream]→WETH | 0.003928 WETH | 0.000118 WETH | 0.000000 WETH | 0.000003 WETH | 0.000115 WETH (0.2585 €) | — | 292.09 | 0.001 (n=7) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52883688 | WETH→[sushiswap_v3]→USDC→[aerodrome_slipstream]→LCAP→[aerodrome_slipstream]→WETH | 0.003928 WETH | 0.000118 WETH | 0.000000 WETH | 0.000003 WETH | 0.000115 WETH (0.2585 €) | — | 292.06 | 0.002 (n=5) | REJECTED | reliability_not_demonstrated |
| 52883688 | USDC→[aerodrome_slipstream]→LCAP→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 9.591827 USDC | 0.288238 USDC | 0.000000 USDC | 0.007358 USDC | 0.280880 USDC (0.2584 €) | — | 292.83 | 0.001 (n=7) | REJECTED | reliability_not_demonstrated |
| 52883688 | USDC→[aerodrome_slipstream]→LCAP→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 9.591827 USDC | 0.288105 USDC | 0.000000 USDC | 0.007358 USDC | 0.280747 USDC (0.2583 €) | — | 292.69 | 0.002 (n=5) | REJECTED | reliability_not_demonstrated |

## Fiabilité et décision
- Observations ghost : 1593 ; taux observé 0.102 ; borne inférieure crédible (0.9) 0.093 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 9.3% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
