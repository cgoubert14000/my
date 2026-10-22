# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-22T12:28:48+00:00 ; durée 214.87 min ; blocs 52934940 → 52941383 (5842 vus)

## Connexion
- Requêtes RPC : 72972 ; erreurs : 93 ; latence p50/p95 : 417.1/1,436.9 ms
- Rafraîchissements d'état : 5842 ; âge des données au dernier bloc : 7.36 s ; changements de frais LP observés (pools à frais dynamiques) : 9491
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 46743 ; cycles déclenchés par événement : 3880 ; avance médiane sur le rafraîchissement multicall : 935 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,403.84 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 552 pools, 321 jetons, 20574 routes
- Par DEX : uniswap_v3 136, aerodrome 228, aerodrome_slipstream 141, pancakeswap_v3 31, uniswap_v2 13, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 201 (rejetés 2) → 606 jetons ; pools candidats 3839 (énumérés 370, par paires 0), mesurés 554, sous le plancher de 10000.0 $ : 2 → gardés 552 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'DAI': 1.0, 'USDC': 1.0, 'WETH': 2409.153844, 'AERO': 0.798022, 'cbBTC': 81873.188532}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 155,614,365 | 2,403.841867 | 52941384 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 21,036,237 | 1.231965 | 52941384 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,284,619 | 0.029385 | 52941384 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 16,117,679 | 87.778861 | 52941384 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,264,556 | 0.029399 | 52941384 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 9,438,781 | 0.029384 | 52941384 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,412,087 | 0.000012 | 52941384 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 8,617,997 | 2,403.613739 | 52941384 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,177,654 | 0.001667 | 52941384 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 330 | 7,035,774 | 0.000012 | 52941384 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 150 | 6,035,719 | 2,404.180232 | 52941384 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | USDC/cbBTC | 424 | 5,660,623 | 0.000012 | 52941384 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,403,138 | 0.029397 | 52941384 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,598,792 | 2,404.479773 | 52941384 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | WETH/USDC | 3000 | 4,318,508 | 2,402.111273 | 52941384 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,301,537 | 1.000001 | 52941384 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,987,392 | 34,459.928428 | 52941384 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | VIRTUAL/WETH | 10000 | 3,767,084 | 0.000275 | 52941384 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/USDT | 409 | 2,915,822 | 2,407.378681 | 52941384 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome_slipstream | WETH/VVV | 2736 | 2,622,089 | 87.797310 | 52941384 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | WETH/AERO | 10000 | 2,375,902 | 2,970.236535 | 52941384 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,306,252 | 397.833943 | 52941384 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,220,638 | 0.000012 | 52941384 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | WETH/FAI | 10000 | 2,203,733 | 1,207,117.448597 | 52941384 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 2,062,757 | 0.000012 | 52941384 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,900,676 | 0.000000 | 52941384 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,795,933 | 0.018515 | 52941384 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,662,778 | 1.531866 | 52941384 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | WETH/AERO | 3000 | 1,634,939 | 2,958.950014 | 52941384 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,455,987 | 0.822662 | 52941384 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,414,899 | 13,527.721708 | 52941384 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,367,265 | 0.004976 | 52941384 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome | WETH/msETH (stable) | 500 | 1,324,214 | 2.346103 | 52941384 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,300,925 | 0.000276 | 52941384 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| uniswap_v3 | DRB/WETH | 10000 | 1,292,060 | 0.000000 | 52941384 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,287,994 | 2,403.536381 | 52941384 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,229,679 | 64.262670 | 52941384 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 1,219,765 | 0.000010 | 52941384 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v3 | WETH/doginme | 10000 | 1,196,299 | 35,411,332.991799 | 52941384 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,187,727 | 16.279915 | 52941384 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | WETH/WELL | 10000 | 1,186,782 | 1,089,673.374884 | 52941384 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome | fBOMB/AERO | 10000 | 1,158,043 | 0.023206 | 52941384 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome | USDC/NOCK | 3000 | 1,152,994 | 47.357847 | 52941384 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,150,047 | 501,506.528206 | 52941384 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | WETH/EDEL | 7000 | 1,117,408 | 73,119.298494 | 52941384 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | fBOMB/USDC | 10000 | 1,101,844 | 0.018813 | 52941384 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| aerodrome | weETH_04c0/WETH | 500 | 1,098,253 | 1.105754 | 52941384 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,061,578 | 21,485,745.113481 | 52941384 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,032,497 | 17.357412 | 52941384 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | WETH/cbBTC | 3000 | 1,019,947 | 0.029398 | 52941384 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,013,412 | 23.031332 | 52941384 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| uniswap_v3 | USDC/VVV | 3000 | 1,002,972 | 0.036561 | 52941384 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/MORPHO | 3000 | 959,320 | 1,061.357012 | 52941384 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/USDC | 10000 | 933,612 | 2,417.961824 | 52941384 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | uXRP/WETH | 3000 | 917,873 | 0.000550 | 52941384 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | EURC/USDC | 70 | 902,186 | 1.120631 | 52941384 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| aerodrome | WETH/bsdETH | 100 | 895,400 | 0.916099 | 52941384 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 890,188 | 17.550707 | 52941384 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v2 | WETH/USDC | 3000 | 876,369 | 2,404.648128 | 52941384 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome | WETH/wstETH | 3000 | 816,243 | 0.803225 | 52941384 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |

## Recherche d'opportunités
- Cycles : 9721 ; routes examinées : 199999854 ; candidats optimisés : 950373 ; net attendu > 0 : 189 ; dernier cycle 573.4 ms
- Rejets (moteur) : {'spread_below_threshold': 197140752, 'liquidity_below_min': 1894039, 'negative_expected_net': 950184, 'borrow_bound_too_small': 9709, 'cycle_budget_exhausted': 4981}
- Enregistrements de la session : 950373 ; net attendu > 0 : 189 ; simulés (eth_call de la vraie tx) : 17 (ok 6, échec 11) ; étiquettes ghost N+1 : 0/17 positives
- Décisions : {'REJECTED': 950373} ; motifs de rejet : {'below_safety_margin': 70, 'negative_expected_net': 950184, 'p_lower_below_threshold': 155, 'reliability_not_demonstrated': 34, 'simulation_failed': 11, 'stale_data': 16}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52940243 | cbBTC→[aerodrome_slipstream]→AERO→[aerodrome]→USDC→[pancakeswap_v3]→cbBTC | 0.013410 cbBTC | 0.000004 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000004 cbBTC (0.2916 €) | — | 2.89 | 0.182 (n=29) | REJECTED | stale_data(11071ms>4000.0), reliability_not_demonstrated |
| 52940243 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→AERO→[aerodrome]→USDC | 1,119.170950 USDC | 0.323051 USDC | 0.000000 USDC | 0.006907 USDC | 0.316144 USDC (0.2909 €) | — | 2.82 | 0.182 (n=29) | REJECTED | stale_data(11065ms>4000.0), simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52938641 | cbBTC→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.005862 cbBTC | 0.000003 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000003 cbBTC (0.2338 €) | — | 5.29 | 0.099 (n=180) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 52935498 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.359582 WETH | 0.000108 WETH | 0.000000 WETH | 0.000002 WETH | 0.000106 WETH (0.2336 €) | 0.000106 WETH | 2.94 | 0.023 (n=63) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 52938641 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→USDC | 483.768011 USDC | 0.260782 USDC | 0.000000 USDC | 0.007249 USDC | 0.253533 USDC (0.2333 €) | — | 5.24 | 0.099 (n=180) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 52935498 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 860.319661 USDC | 0.259021 USDC | 0.000000 USDC | 0.005776 USDC | 0.253245 USDC (0.2330 €) | — | 2.94 | 0.023 (n=63) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 52940243 | cbBTC→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.005230 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1771 €) | — | 4.49 | 0.097 (n=183) | REJECTED | stale_data(11020ms>4000.0), p_lower_below_threshold(0.10<0.75) |
| 52940243 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→USDC | 426.532059 USDC | 0.198713 USDC | 0.000000 USDC | 0.007239 USDC | 0.191474 USDC (0.1762 €) | — | 4.49 | 0.097 (n=183) | REJECTED | stale_data(11006ms>4000.0), p_lower_below_threshold(0.10<0.75) |
| 52938641 | USDC→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→USDC | 431.669333 USDC | 0.191189 USDC | 0.000000 USDC | 0.007249 USDC | 0.183940 USDC (0.1692 €) | — | 4.26 | 0.124 (n=95) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52938641 | cbBTC→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→cbBTC | 0.004955 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1689 €) | — | 4.52 | 0.124 (n=95) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52938641 | WETH→[aerodrome_slipstream]→wstETH→[aerodrome_slipstream]→AERO→[pancakeswap_v3]→WETH | 0.065171 WETH | 0.000049 WETH | 0.000000 WETH | 0.000003 WETH | 0.000046 WETH (0.1017 €) | — | 7.06 | 0.099 (n=180) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.10<0.75) |
| 52938641 | WETH→[uniswap_v3]→wstETH→[aerodrome_slipstream]→AERO→[pancakeswap_v3]→WETH | 0.064612 WETH | 0.000048 WETH | 0.000000 WETH | 0.000003 WETH | 0.000045 WETH (0.0999 €) | — | 6.99 | 0.099 (n=180) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.10<0.75) |
| 52935498 | WETH→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.103454 WETH | 0.000046 WETH | 0.000000 WETH | 0.000003 WETH | 0.000043 WETH (0.0950 €) | 0.000043 WETH | 4.15 | 0.130 (n=91) | REJECTED | p_lower_below_threshold(0.13<0.75) |
| 52935498 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→USDC | 247.137886 USDC | 0.110224 USDC | 0.000000 USDC | 0.007240 USDC | 0.102984 USDC (0.0947 €) | — | 4.17 | 0.130 (n=91) | REJECTED | p_lower_below_threshold(0.13<0.75) |
| 52938641 | cbBTC→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→cbBTC | 0.003730 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0875 €) | — | 3.11 | 0.124 (n=95) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52938641 | USDC→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→USDC | 307.015328 USDC | 0.101744 USDC | 0.000000 USDC | 0.007249 USDC | 0.094495 USDC (0.0869 €) | — | 3.08 | 0.124 (n=95) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52938641 | cbBTC→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.002499 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0867 €) | — | 4.60 | 0.099 (n=180) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 52938641 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC | 191.834564 USDC | 0.101363 USDC | 0.000000 USDC | 0.007249 USDC | 0.094114 USDC (0.0866 €) | — | 4.91 | 0.099 (n=180) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 52938641 | cbBTC→[aerodrome_slipstream]→AERO→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.002752 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0860 €) | — | 4.14 | 0.099 (n=180) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 52938641 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→AERO→[pancakeswap_v3]→WETH | 0.095400 WETH | 0.000042 WETH | 0.000000 WETH | 0.000003 WETH | 0.000039 WETH (0.0858 €) | — | 4.07 | 0.099 (n=180) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.10<0.75) |
| 52940243 | cbBTC→[aerodrome_slipstream]→AERO→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.002769 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0814 €) | — | 3.90 | 0.097 (n=183) | REJECTED | stale_data(11059ms>4000.0), p_lower_below_threshold(0.10<0.75) |
| 52938641 | cbBTC→[aerodrome_slipstream]→AERO→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.002758 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0807 €) | — | 3.88 | 0.099 (n=180) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 52940243 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→AERO→[pancakeswap_v3]→WETH | 0.109760 WETH | 0.000040 WETH | 0.000000 WETH | 0.000003 WETH | 0.000036 WETH (0.0807 €) | — | 3.32 | 0.097 (n=183) | REJECTED | stale_data(11052ms>4000.0), simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.10<0.75) |
| 52938641 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→AERO→[pancakeswap_v3]→WETH | 0.103642 WETH | 0.000039 WETH | 0.000000 WETH | 0.000003 WETH | 0.000036 WETH (0.0807 €) | — | 3.52 | 0.099 (n=180) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 52935498 | WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.110845 WETH | 0.000037 WETH | 0.000000 WETH | 0.000003 WETH | 0.000034 WETH (0.0749 €) | 0.000034 WETH | 3.06 | 0.130 (n=91) | REJECTED | p_lower_below_threshold(0.13<0.75) |

## Fiabilité et décision
- Observations ghost : 1861 ; taux observé 0.095 ; borne inférieure crédible (0.9) 0.086 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 8.6% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
