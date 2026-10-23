# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-23T00:36:44+00:00 ; durée 267.06 min ; blocs 52955211 → 52963222 (7418 vus)

## Connexion
- Requêtes RPC : 91855 ; erreurs : 38 ; latence p50/p95 : 411.1/1,512.5 ms
- Rafraîchissements d'état : 7419 ; âge des données au dernier bloc : 1.89 s ; changements de frais LP observés (pools à frais dynamiques) : 11291
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 82103 ; cycles déclenchés par événement : 6287 ; avance médiane sur le rafraîchissement multicall : 778 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,386.15 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 541 pools, 316 jetons, 19308 routes
- Par DEX : uniswap_v3 137, aerodrome 222, aerodrome_slipstream 136, pancakeswap_v3 30, uniswap_v2 13, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 198 (rejetés 2) → 603 jetons ; pools candidats 3822 (énumérés 360, par paires 0), mesurés 543, sous le plancher de 10000.0 $ : 2 → gardés 541 (max 1500) ; prix des hubs : {'USDC': 1.0, 'USDbC': 1.0, 'DAI': 1.0, 'WETH': 2383.836332, 'AERO': 0.803249, 'cbBTC': 81352.487956}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 156,457,765 | 2,386.154907 | 52963222 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,217,722 | 0.029386 | 52963222 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 13,412,505 | 91.968398 | 52963222 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| aerodrome | USDC/AERO | 3000 | 11,964,442 | 1.274277 | 52963222 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,237,318 | 0.029364 | 52963222 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,849,261 | 0.000012 | 52963222 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 8,928,268 | 0.029368 | 52963222 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/USDC | 500 | 8,670,714 | 2,388.370523 | 52963222 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,128,056 | 0.001668 | 52963222 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 346 | 6,794,596 | 0.000012 | 52963222 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 150 | 5,688,777 | 2,388.936749 | 52963222 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,385,218 | 0.029398 | 52963222 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | USDC/cbBTC | 496 | 5,253,225 | 0.000012 | 52963222 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,579,732 | 2,388.839744 | 52963222 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,276,596 | 0.998772 | 52963222 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/USDC | 3000 | 4,276,317 | 2,387.804033 | 52963222 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome | WETH/KTA | 3000 | 3,964,029 | 34,339.809391 | 52963222 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | VIRTUAL/WETH | 10000 | 3,430,365 | 0.000274 | 52963222 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/USDT | 430 | 2,899,478 | 2,392.455563 | 52963222 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome_slipstream | WETH/VVV | 2700 | 2,544,815 | 91.985079 | 52963222 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,308,013 | 386.716789 | 52963222 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | WETH/AERO | 10000 | 2,255,030 | 3,025.076784 | 52963222 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | WETH/FAI | 10000 | 2,210,213 | 1,182,410.796820 | 52963222 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,980,561 | 0.000000 | 52963222 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,919,500 | 0.000012 | 52963222 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v3 | XDP/USDC | 100 | 1,772,748 | 0.017997 | 52963222 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,746,259 | 0.000012 | 52963222 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,641,025 | 1.525684 | 52963222 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | WETH/AERO | 3000 | 1,610,532 | 3,036.858941 | 52963222 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,453,741 | 0.823230 | 52963222 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,418,888 | 13,145.857318 | 52963222 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,365,845 | 0.004990 | 52963222 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,289,768 | 0.000273 | 52963222 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| uniswap_v3 | DRB/WETH | 10000 | 1,288,948 | 0.000000 | 52963222 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | WETH/msETH (stable) | 500 | 1,278,269 | 2.361240 | 52963222 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,276,189 | 2,388.200723 | 52963222 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,229,423 | 64.289389 | 52963222 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,183,532 | 35,764,166.460256 | 52963222 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,175,935 | 16.235786 | 52963222 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | WETH/WELL | 10000 | 1,169,554 | 1,105,040.584820 | 52963222 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome | USDC/NOCK | 3000 | 1,158,483 | 46.760513 | 52963222 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,145,115 | 498,148.209539 | 52963222 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | WETH/EDEL | 7000 | 1,087,018 | 74,232.385558 | 52963222 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | weETH_04c0/WETH | 500 | 1,086,770 | 1.105790 | 52963222 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| uniswap_v3 | USDC/VVV | 3000 | 1,085,092 | 0.038522 | 52963222 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,058,812 | 21,313,449.073659 | 52963222 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 1,053,453 | 0.000010 | 52963222 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,033,262 | 17.286362 | 52963222 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | WETH/cbBTC | 3000 | 1,008,425 | 0.029368 | 52963222 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,003,261 | 23.055939 | 52963222 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| uniswap_v3 | WETH/MORPHO | 3000 | 960,028 | 1,052.568909 | 52963222 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/USDC | 10000 | 937,765 | 2,381.973285 | 52963222 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | uXRP/WETH | 3000 | 911,018 | 0.000546 | 52963222 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome | WETH/bsdETH | 100 | 887,440 | 0.916411 | 52963222 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 881,214 | 17.849732 | 52963222 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v2 | WETH/USDC | 3000 | 874,219 | 2,388.637812 | 52963222 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome | WETH/wstETH | 3000 | 808,358 | 0.803225 | 52963222 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 787,494 | 0.650658 | 52963222 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| pancakeswap_v3 | QUID/USDC | 100 | 783,420 | 0.054966 | 52963222 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | fBOMB/USDC | 10000 | 769,744 | 0.018327 | 52963222 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |

## Recherche d'opportunités
- Cycles : 13705 ; routes examinées : 264616140 ; candidats optimisés : 1252630 ; net attendu > 0 : 664 ; dernier cycle 164.3 ms
- Rejets (moteur) : {'spread_below_threshold': 260904945, 'liquidity_below_min': 2441378, 'negative_expected_net': 1251966, 'borrow_bound_too_small': 13688, 'cycle_budget_exhausted': 3499}
- Enregistrements de la session : 1252630 ; net attendu > 0 : 664 ; simulés (eth_call de la vraie tx) : 31 (ok 7, échec 24) ; étiquettes ghost N+1 : 0/27 positives
- Décisions : {'REJECTED': 1252630} ; motifs de rejet : {'below_safety_margin': 411, 'negative_expected_net': 1251966, 'p_lower_below_threshold': 560, 'reliability_not_demonstrated': 104, 'simulation_failed': 24, 'stale_data': 22}

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
- Observations ghost : 1955 ; taux observé 0.095 ; borne inférieure crédible (0.9) 0.087 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 8.7% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
