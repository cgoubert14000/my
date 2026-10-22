# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-22T23:16:46+00:00 ; durée 187.1 min ; blocs 52955211 → 52960824 (5143 vus)

## Connexion
- Requêtes RPC : 63006 ; erreurs : 38 ; latence p50/p95 : 270.3/1,623.0 ms
- Rafraîchissements d'état : 5143 ; âge des données au dernier bloc : 3.11 s ; changements de frais LP observés (pools à frais dynamiques) : 8072
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 51745 ; cycles déclenchés par événement : 3587 ; avance médiane sur le rafraîchissement multicall : 553 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,388.17 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 541 pools, 316 jetons, 19308 routes
- Par DEX : uniswap_v3 137, aerodrome 222, aerodrome_slipstream 136, pancakeswap_v3 30, uniswap_v2 13, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 198 (rejetés 2) → 603 jetons ; pools candidats 3822 (énumérés 360, par paires 0), mesurés 543, sous le plancher de 10000.0 $ : 2 → gardés 541 (max 1500) ; prix des hubs : {'USDC': 1.0, 'USDbC': 1.0, 'DAI': 1.0, 'WETH': 2383.836332, 'AERO': 0.803249, 'cbBTC': 81352.487956}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 156,547,078 | 2,388.165403 | 52960825 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,242,302 | 0.029317 | 52960825 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 13,470,302 | 91.443110 | 52960825 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| aerodrome | USDC/AERO | 3000 | 11,965,010 | 1.277331 | 52960825 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,257,042 | 0.029364 | 52960825 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,884,876 | 0.000012 | 52960825 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 8,944,751 | 0.029374 | 52960825 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/USDC | 500 | 8,675,021 | 2,382.262555 | 52960825 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,134,474 | 0.001660 | 52960825 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 330 | 6,803,333 | 0.000012 | 52960825 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 150 | 5,703,182 | 2,382.095416 | 52960825 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,382,826 | 0.029314 | 52960825 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | USDC/cbBTC | 400 | 5,272,446 | 0.000012 | 52960825 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,510,700 | 2,381.971752 | 52960825 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,290,383 | 0.998772 | 52960825 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/USDC | 3000 | 4,286,544 | 2,388.388408 | 52960825 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome | WETH/KTA | 3000 | 3,965,552 | 34,371.275640 | 52960825 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | VIRTUAL/WETH | 10000 | 3,433,900 | 0.000274 | 52960825 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/USDT | 403 | 2,905,246 | 2,386.195605 | 52960825 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome_slipstream | WETH/VVV | 2700 | 2,553,559 | 91.409316 | 52960825 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,299,738 | 392.496414 | 52960825 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | WETH/AERO | 10000 | 2,257,989 | 3,025.076784 | 52960825 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | WETH/FAI | 10000 | 2,205,676 | 1,189,282.625430 | 52960825 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,969,172 | 0.000000 | 52960825 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,922,391 | 0.000012 | 52960825 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v3 | XDP/USDC | 100 | 1,778,945 | 0.018105 | 52960825 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,749,609 | 0.000012 | 52960825 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,641,404 | 1.525096 | 52960825 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | WETH/AERO | 3000 | 1,608,482 | 3,044.317578 | 52960825 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,453,652 | 0.823324 | 52960825 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,414,729 | 13,403.024597 | 52960825 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,366,940 | 0.004990 | 52960825 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,325,908 | 2,382.180839 | 52960825 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,291,046 | 0.000273 | 52960825 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | WETH/msETH (stable) | 500 | 1,279,346 | 2.361240 | 52960825 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | DRB/WETH | 10000 | 1,264,188 | 0.000000 | 52960825 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | USDC/SEND | 3000 | 1,229,454 | 64.286145 | 52960825 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,184,529 | 35,764,166.460256 | 52960825 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,176,989 | 16.234606 | 52960825 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | WETH/WELL | 10000 | 1,169,268 | 1,107,444.724058 | 52960825 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome | USDC/NOCK | 3000 | 1,165,621 | 46.189543 | 52960825 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,146,080 | 498,148.209539 | 52960825 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | WETH/EDEL | 7000 | 1,089,039 | 74,172.945328 | 52960825 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | USDC/VVV | 3000 | 1,088,667 | 0.038356 | 52960825 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | weETH_04c0/WETH | 500 | 1,087,687 | 1.105792 | 52960825 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,061,332 | 21,256,860.378615 | 52960825 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 1,058,884 | 0.000010 | 52960825 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,035,009 | 17.206994 | 52960825 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | WETH/cbBTC | 3000 | 1,010,894 | 0.029368 | 52960825 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,003,590 | 23.057513 | 52960825 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| uniswap_v3 | WETH/MORPHO | 3000 | 956,174 | 1,055.006278 | 52960825 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/USDC | 10000 | 938,116 | 2,381.973285 | 52960825 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | uXRP/WETH | 3000 | 911,108 | 0.000545 | 52960825 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome | WETH/bsdETH | 100 | 888,197 | 0.916392 | 52960825 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 881,104 | 17.854087 | 52960825 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v2 | WETH/USDC | 3000 | 874,581 | 2,386.476966 | 52960825 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome | WETH/wstETH | 3000 | 809,039 | 0.803225 | 52960825 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 788,130 | 0.650022 | 52960825 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| pancakeswap_v3 | QUID/USDC | 100 | 786,001 | 0.055346 | 52960825 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | fBOMB/USDC | 10000 | 770,030 | 0.018341 | 52960825 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |

## Recherche d'opportunités
- Cycles : 8729 ; routes examinées : 168539532 ; candidats optimisés : 918652 ; net attendu > 0 : 470 ; dernier cycle 162.2 ms
- Rejets (moteur) : {'spread_below_threshold': 166083915, 'liquidity_below_min': 1524820, 'negative_expected_net': 918182, 'borrow_bound_too_small': 8713, 'cycle_budget_exhausted': 3432}
- Enregistrements de la session : 918652 ; net attendu > 0 : 470 ; simulés (eth_call de la vraie tx) : 22 (ok 7, échec 15) ; étiquettes ghost N+1 : 0/18 positives
- Décisions : {'REJECTED': 918652} ; motifs de rejet : {'below_safety_margin': 316, 'negative_expected_net': 918182, 'p_lower_below_threshold': 385, 'reliability_not_demonstrated': 85, 'simulation_failed': 15, 'stale_data': 22}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52960458 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome]→AERO→[aerodrome_slipstream]→cbBTC | 0.035412 cbBTC | 0.000056 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000056 cbBTC (4.2161 €) | — | 15.89 | 0.051 (n=16) | REJECTED | reliability_not_demonstrated |
| 52960458 | USDC→[aerodrome]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 2,895.231752 USDC | 4.578912 USDC | 0.000000 USDC | 0.008301 USDC | 4.570611 USDC (4.2050 €) | — | 15.79 | 0.051 (n=16) | REJECTED | reliability_not_demonstrated |
| 52960458 | cbBTC→[aerodrome_slipstream]→USDC→[aerodrome]→AERO→[aerodrome_slipstream]→cbBTC | 0.035493 cbBTC | 0.000053 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000053 cbBTC (3.9389 €) | — | 14.81 | 0.021 (n=134) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 52960458 | USDC→[aerodrome]→AERO→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→USDC | 2,877.478724 USDC | 4.275915 USDC | 0.000000 USDC | 0.007213 USDC | 4.268702 USDC (3.9272 €) | — | 14.83 | 0.021 (n=134) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 52960458 | cbBTC→[aerodrome_slipstream]→USDC→[aerodrome]→AERO→[aerodrome_slipstream]→cbBTC | 0.034669 cbBTC | 0.000049 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000049 cbBTC (3.6466 €) | — | 14.04 | 0.021 (n=134) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 52960458 | USDC→[aerodrome]→AERO→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→USDC | 2,820.419579 USDC | 3.958755 USDC | 0.000000 USDC | 0.007213 USDC | 3.951542 USDC (3.6354 €) | — | 14.01 | 0.021 (n=134) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 52960458 | cbBTC→[uniswap_v3]→USDC→[aerodrome]→AERO→[aerodrome_slipstream]→cbBTC | 0.032410 cbBTC | 0.000043 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000043 cbBTC (3.2352 €) | — | 13.32 | 0.021 (n=134) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 52960458 | USDC→[aerodrome]→AERO→[aerodrome_slipstream]→cbBTC→[uniswap_v3]→USDC | 2,656.396106 USDC | 3.512901 USDC | 0.000000 USDC | 0.007213 USDC | 3.505688 USDC (3.2252 €) | — | 13.20 | 0.021 (n=134) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 52960458 | WETH→[aerodrome_slipstream]→USDC→[aerodrome]→AERO→[uniswap_v3]→WETH | 0.786690 WETH | 0.001035 WETH | 0.000000 WETH | 0.000003 WETH | 0.001032 WETH (2.2680 €) | — | 13.12 | 0.021 (n=134) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.02<0.75) |
| 52960458 | USDC→[aerodrome]→AERO→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 1,872.541635 USDC | 2.464489 USDC | 0.000000 USDC | 0.006851 USDC | 2.457638 USDC (2.2610 €) | — | 13.12 | 0.021 (n=134) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 52960458 | WETH→[pancakeswap_v3]→USDC→[aerodrome]→AERO→[uniswap_v3]→WETH | 0.769086 WETH | 0.000999 WETH | 0.000000 WETH | 0.000003 WETH | 0.000996 WETH (2.1875 €) | — | 12.94 | 0.051 (n=16) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52960458 | WETH→[uniswap_v3]→USDC→[aerodrome]→AERO→[uniswap_v3]→WETH | 0.770657 WETH | 0.000996 WETH | 0.000000 WETH | 0.000003 WETH | 0.000993 WETH (2.1819 €) | — | 12.89 | 0.021 (n=134) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.02<0.75) |
| 52960458 | USDC→[aerodrome]→AERO→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 1,832.023654 USDC | 2.377428 USDC | 0.000000 USDC | 0.007213 USDC | 2.370215 USDC (2.1806 €) | — | 12.94 | 0.051 (n=16) | REJECTED | reliability_not_demonstrated |
| 52960458 | USDC→[aerodrome]→AERO→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 1,833.895644 USDC | 2.371020 USDC | 0.000000 USDC | 0.006851 USDC | 2.364169 USDC (2.1750 €) | — | 12.89 | 0.021 (n=134) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 52960458 | WETH→[pancakeswap_v3]→USDC→[aerodrome]→AERO→[uniswap_v3]→WETH | 0.734548 WETH | 0.000957 WETH | 0.000000 WETH | 0.000003 WETH | 0.000954 WETH (2.0961 €) | — | 12.99 | 0.051 (n=16) | REJECTED | reliability_not_demonstrated |
| 52960458 | USDC→[aerodrome]→AERO→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 1,747.812253 USDC | 2.277838 USDC | 0.000000 USDC | 0.006851 USDC | 2.270987 USDC (2.0893 €) | — | 12.99 | 0.051 (n=16) | REJECTED | reliability_not_demonstrated |
| 52960458 | USDC→[aerodrome]→AERO→[aerodrome_slipstream]→USDC | 1,414.742506 USDC | 2.172702 USDC | 0.000000 USDC | 0.005398 USDC | 2.167304 USDC (1.9939 €) | — | 15.32 | 0.001 (n=15) | REJECTED | reliability_not_demonstrated |
| 52960458 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome]→AERO→[aerodrome_slipstream]→cbBTC | 0.018158 cbBTC | 0.000025 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000024 cbBTC (1.8345 €) | — | 13.48 | 0.051 (n=16) | REJECTED | reliability_not_demonstrated |
| 52960458 | USDC→[aerodrome]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 1,497.267672 USDC | 1.994156 USDC | 0.000000 USDC | 0.007576 USDC | 1.986580 USDC (1.8277 €) | — | 13.27 | 0.051 (n=16) | REJECTED | reliability_not_demonstrated |
| 52960458 | WETH→[uniswap_v3]→USDC→[aerodrome]→AERO→[uniswap_v3]→WETH | 0.561536 WETH | 0.000756 WETH | 0.000000 WETH | 0.000003 WETH | 0.000753 WETH (1.6545 €) | — | 13.41 | 0.021 (n=134) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 52960458 | WETH→[uniswap_v3]→USDC→[aerodrome]→AERO→[aerodrome_slipstream]→WETH | 0.582177 WETH | 0.000755 WETH | 0.000000 WETH | 0.000003 WETH | 0.000752 WETH (1.6517 €) | — | 12.91 | 0.021 (n=134) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 52960458 | USDC→[aerodrome]→AERO→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 1,335.006939 USDC | 1.798720 USDC | 0.000000 USDC | 0.007213 USDC | 1.791507 USDC (1.6482 €) | — | 13.42 | 0.021 (n=134) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 52960458 | USDC→[aerodrome]→AERO→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 1,385.671983 USDC | 1.796740 USDC | 0.000000 USDC | 0.006851 USDC | 1.789889 USDC (1.6467 €) | — | 12.92 | 0.021 (n=134) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 52960458 | WETH→[aerodrome_slipstream]→USDC→[aerodrome]→AERO→[aerodrome_slipstream]→WETH | 0.573221 WETH | 0.000747 WETH | 0.000000 WETH | 0.000003 WETH | 0.000744 WETH (1.6345 €) | — | 12.98 | 0.021 (n=134) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 52960458 | USDC→[aerodrome]→AERO→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→USDC | 1,364.432330 USDC | 1.778025 USDC | 0.000000 USDC | 0.006851 USDC | 1.771174 USDC (1.6295 €) | — | 12.98 | 0.021 (n=134) | REJECTED | p_lower_below_threshold(0.02<0.75) |

## Fiabilité et décision
- Observations ghost : 1946 ; taux observé 0.096 ; borne inférieure crédible (0.9) 0.087 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 8.7% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
