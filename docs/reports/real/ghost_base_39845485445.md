# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-22T23:00:55+00:00 ; durée 171.24 min ; blocs 52955211 → 52960350 (4683 vus)

## Connexion
- Requêtes RPC : 57314 ; erreurs : 38 ; latence p50/p95 : 387.8/1,815.6 ms
- Rafraîchissements d'état : 4683 ; âge des données au dernier bloc : 2.44 s ; changements de frais LP observés (pools à frais dynamiques) : 7558
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 46116 ; cycles déclenchés par événement : 2968 ; avance médiane sur le rafraîchissement multicall : 601 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,388.33 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 541 pools, 316 jetons, 19308 routes
- Par DEX : uniswap_v3 137, aerodrome 222, aerodrome_slipstream 136, pancakeswap_v3 30, uniswap_v2 13, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 198 (rejetés 2) → 603 jetons ; pools candidats 3822 (énumérés 360, par paires 0), mesurés 543, sous le plancher de 10000.0 $ : 2 → gardés 541 (max 1500) ; prix des hubs : {'USDC': 1.0, 'USDbC': 1.0, 'DAI': 1.0, 'WETH': 2383.836332, 'AERO': 0.803249, 'cbBTC': 81352.487956}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 156,552,685 | 2,388.328261 | 52960350 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,242,660 | 0.029324 | 52960349 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 13,477,148 | 91.362851 | 52960349 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| aerodrome | USDC/AERO | 3000 | 12,045,271 | 1.270533 | 52960349 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,256,787 | 0.029364 | 52960349 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,884,115 | 0.000012 | 52960349 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 8,944,518 | 0.029377 | 52960349 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/USDC | 500 | 8,674,077 | 2,382.512348 | 52960349 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,132,031 | 0.001660 | 52960349 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 330 | 6,802,854 | 0.000012 | 52960349 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 150 | 5,706,548 | 2,382.432427 | 52960349 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,382,846 | 0.029319 | 52960349 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | USDC/cbBTC | 400 | 5,273,810 | 0.000012 | 52960349 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,562,858 | 2,382.636320 | 52960349 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,289,622 | 0.998772 | 52960349 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/USDC | 3000 | 4,287,388 | 2,388.633847 | 52960349 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome | WETH/KTA | 3000 | 3,965,615 | 34,374.884709 | 52960349 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | VIRTUAL/WETH | 10000 | 3,434,134 | 0.000274 | 52960349 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/USDT | 406 | 2,905,454 | 2,386.171147 | 52960349 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome_slipstream | WETH/VVV | 2718 | 2,554,556 | 91.410939 | 52960349 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,295,145 | 395.097497 | 52960349 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | WETH/AERO | 10000 | 2,265,367 | 3,008.544878 | 52960349 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | WETH/FAI | 10000 | 2,201,040 | 1,194,460.014081 | 52960349 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,967,460 | 0.000000 | 52960349 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,922,235 | 0.000012 | 52960349 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v3 | XDP/USDC | 100 | 1,782,503 | 0.018161 | 52960350 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,749,418 | 0.000012 | 52960349 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,641,404 | 1.525096 | 52960349 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | WETH/AERO | 3000 | 1,611,838 | 3,028.491123 | 52960349 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,453,634 | 0.823342 | 52960349 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,411,210 | 13,489.688062 | 52960349 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,367,034 | 0.004990 | 52960349 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,325,968 | 2,382.475708 | 52960349 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,291,134 | 0.000273 | 52960349 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | WETH/msETH (stable) | 500 | 1,281,239 | 2.361240 | 52960349 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | DRB/WETH | 10000 | 1,266,007 | 0.000000 | 52960349 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | USDC/SEND | 3000 | 1,229,454 | 64.286145 | 52960349 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,184,610 | 35,764,166.460256 | 52960349 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,177,069 | 16.234606 | 52960349 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | WETH/WELL | 10000 | 1,169,634 | 1,107,426.313389 | 52960349 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome | USDC/NOCK | 3000 | 1,163,423 | 46.364256 | 52960349 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,146,158 | 498,148.209539 | 52960349 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | USDC/VVV | 3000 | 1,089,199 | 0.038360 | 52960349 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | WETH/EDEL | 7000 | 1,089,154 | 74,167.505569 | 52960349 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | weETH_04c0/WETH | 500 | 1,087,761 | 1.105792 | 52960349 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,061,404 | 21,256,860.378615 | 52960349 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 1,061,384 | 0.000010 | 52960349 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,032,992 | 17.306837 | 52960350 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | WETH/cbBTC | 3000 | 1,010,839 | 0.029368 | 52960349 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,003,658 | 23.057513 | 52960349 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| uniswap_v3 | WETH/MORPHO | 3000 | 957,411 | 1,052.849418 | 52960349 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/USDC | 10000 | 938,143 | 2,381.973285 | 52960349 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | uXRP/WETH | 3000 | 910,751 | 0.000545 | 52960349 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome | WETH/bsdETH | 100 | 888,258 | 0.916392 | 52960349 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 881,104 | 17.854087 | 52960349 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v2 | WETH/USDC | 3000 | 874,611 | 2,386.452511 | 52960349 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome | WETH/wstETH | 3000 | 809,094 | 0.803225 | 52960349 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 788,151 | 0.650840 | 52960349 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| pancakeswap_v3 | QUID/USDC | 100 | 785,777 | 0.055313 | 52960349 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | fBOMB/USDC | 10000 | 770,030 | 0.018341 | 52960349 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |

## Recherche d'opportunités
- Cycles : 7650 ; routes examinées : 147706200 ; candidats optimisés : 847085 ; net attendu > 0 : 316 ; dernier cycle 159.6 ms
- Rejets (moteur) : {'spread_below_threshold': 145500399, 'liquidity_below_min': 1347650, 'negative_expected_net': 846769, 'borrow_bound_too_small': 7634, 'cycle_budget_exhausted': 3432}
- Enregistrements de la session : 847085 ; net attendu > 0 : 316 ; simulés (eth_call de la vraie tx) : 19 (ok 7, échec 12) ; étiquettes ghost N+1 : 0/15 positives
- Décisions : {'REJECTED': 847085} ; motifs de rejet : {'below_safety_margin': 265, 'negative_expected_net': 846769, 'p_lower_below_threshold': 291, 'reliability_not_demonstrated': 25, 'simulation_failed': 12, 'stale_data': 20}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52960245 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.280731 WETH | 0.000065 WETH | 0.000000 WETH | 0.000002 WETH | 0.000063 WETH (0.1389 €) | — | 2.25 | 0.021 (n=67) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.02<0.75) |
| 52960245 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 667.177472 USDC | 0.155988 USDC | 0.000000 USDC | 0.005365 USDC | 0.150623 USDC (0.1386 €) | — | 2.26 | 0.021 (n=67) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.02<0.75) |
| 52960245 | cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.005691 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0794 €) | — | 1.86 | 0.115 (n=232) | REJECTED | below_safety_margin(106<113), p_lower_below_threshold(0.12<0.75) |
| 52960245 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.210377 WETH | 0.000039 WETH | 0.000000 WETH | 0.000003 WETH | 0.000036 WETH (0.0791 €) | — | 1.71 | 0.115 (n=232) | REJECTED | below_safety_margin(36021192671711<42075438406189), p_lower_below_threshold(0.12<0.75) |
| 52960245 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 462.927648 USDC | 0.092959 USDC | 0.000000 USDC | 0.007542 USDC | 0.085417 USDC (0.0786 €) | — | 1.85 | 0.115 (n=232) | REJECTED | below_safety_margin(85417<92585), p_lower_below_threshold(0.12<0.75) |
| 52957222 | USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 223.673289 USDC | 0.076992 USDC | 0.000000 USDC | 0.007192 USDC | 0.069800 USDC (0.0642 €) | — | 3.12 | 0.099 (n=198) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 52957222 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH | 0.093230 WETH | 0.000032 WETH | 0.000000 WETH | 0.000003 WETH | 0.000029 WETH (0.0640 €) | 0.000029 WETH | 3.12 | 0.099 (n=198) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 52957222 | USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 201.659709 USDC | 0.073426 USDC | 0.000000 USDC | 0.007192 USDC | 0.066234 USDC (0.0609 €) | — | 3.28 | 0.119 (n=99) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52957222 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH | 0.084104 WETH | 0.000031 WETH | 0.000000 WETH | 0.000003 WETH | 0.000028 WETH (0.0607 €) | 0.000028 WETH | 3.29 | 0.119 (n=99) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52957435 | USDC→[uniswap_v3]→OWB→[aerodrome]→USDC | 24.546486 USDC | 0.050831 USDC | 0.000000 USDC | 0.005051 USDC | 0.045780 USDC (0.0421 €) | — | 18.65 | 0.001 (n=14) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52957304 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.002194 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0359 €) | — | 2.19 | 0.116 (n=230) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.12<0.75) |
| 52957304 | WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.064566 WETH | 0.000019 WETH | 0.000000 WETH | 0.000003 WETH | 0.000016 WETH (0.0356 €) | — | 2.50 | 0.116 (n=230) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.12<0.75) |
| 52956884 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome_slipstream]→WETH | 0.050938 WETH | 0.000017 WETH | 0.000000 WETH | 0.000003 WETH | 0.000014 WETH (0.0308 €) | 0.000014 WETH | 2.76 | 0.118 (n=226) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52956884 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome_slipstream]→WETH | 0.050938 WETH | 0.000017 WETH | 0.000000 WETH | 0.000003 WETH | 0.000014 WETH (0.0308 €) | — | 2.76 | 0.118 (n=226) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.12<0.75) |
| 52956884 | USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 121.229953 USDC | 0.040595 USDC | 0.000000 USDC | 0.007175 USDC | 0.033420 USDC (0.0307 €) | 0.033420 USDC | 2.76 | 0.118 (n=226) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52956884 | USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 121.229953 USDC | 0.040595 USDC | 0.000000 USDC | 0.007175 USDC | 0.033420 USDC (0.0307 €) | — | 2.76 | 0.118 (n=226) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.12<0.75) |
| 52956884 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome_slipstream]→WETH | 0.048346 WETH | 0.000017 WETH | 0.000000 WETH | 0.000003 WETH | 0.000014 WETH (0.0305 €) | 0.000014 WETH | 2.88 | 0.118 (n=226) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52956884 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome_slipstream]→WETH | 0.048346 WETH | 0.000017 WETH | 0.000000 WETH | 0.000003 WETH | 0.000014 WETH (0.0305 €) | — | 2.88 | 0.118 (n=226) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.12<0.75) |
| 52956884 | USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 115.203870 USDC | 0.040292 USDC | 0.000000 USDC | 0.007175 USDC | 0.033117 USDC (0.0305 €) | — | 2.87 | 0.118 (n=226) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52956884 | USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 115.203870 USDC | 0.040292 USDC | 0.000000 USDC | 0.007175 USDC | 0.033117 USDC (0.0305 €) | — | 2.87 | 0.118 (n=226) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52959989 | WETH→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→WETH | 0.008891 WETH | 0.000016 WETH | 0.000000 WETH | 0.000003 WETH | 0.000013 WETH (0.0283 €) | — | 14.50 | 0.000 (n=30) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 52959989 | WETH→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.008853 WETH | 0.000016 WETH | 0.000000 WETH | 0.000003 WETH | 0.000013 WETH (0.0283 €) | — | 14.55 | 0.000 (n=30) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 52959989 | USDC→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→USDC | 21.018089 USDC | 0.037878 USDC | 0.000000 USDC | 0.007181 USDC | 0.030697 USDC (0.0282 €) | — | 14.61 | 0.000 (n=30) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 52959989 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→USDC | 21.115916 USDC | 0.037848 USDC | 0.000000 USDC | 0.007181 USDC | 0.030667 USDC (0.0282 €) | — | 14.52 | 0.000 (n=30) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 52959989 | WETH→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.008832 WETH | 0.000016 WETH | 0.000000 WETH | 0.000003 WETH | 0.000013 WETH (0.0280 €) | — | 14.43 | 0.000 (n=31) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |

## Fiabilité et décision
- Observations ghost : 1943 ; taux observé 0.096 ; borne inférieure crédible (0.9) 0.087 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 8.7% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
