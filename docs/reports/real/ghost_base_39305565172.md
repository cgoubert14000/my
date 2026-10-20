# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-20T00:24:02+00:00 ; durée 330.33 min ; blocs 52823333 → 52833237 (9462 vus)

## Connexion
- Requêtes RPC : 129266 ; erreurs : 220 ; latence p50/p95 : 356.2/1,591.0 ms
- Rafraîchissements d'état : 9462 ; âge des données au dernier bloc : 5.32 s ; changements de frais LP observés (pools à frais dynamiques) : 14281
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 141063 ; cycles déclenchés par événement : 8515 ; avance médiane sur le rafraîchissement multicall : 930 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,396.89 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 571 pools, 327 jetons, 21062 routes
- Par DEX : uniswap_v3 137, aerodrome 234, aerodrome_slipstream 153, pancakeswap_v3 30, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 206 (rejetés 2) → 611 jetons ; pools candidats 3873 (énumérés 387, par paires 0), mesurés 573, sous le plancher de 10000.0 $ : 2 → gardés 571 (max 1500) ; prix des hubs : {'USDC': 1.0, 'DAI': 1.0, 'USDbC': 1.0, 'WETH': 2395.019975, 'AERO': 0.776373, 'cbBTC': 81898.158416}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 146,062,358 | 2,396.886893 | 52833238 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 34,017,870 | 1.274048 | 52833238 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 500 | 18,188,115 | 0.029377 | 52833238 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 17,303,414 | 99.177157 | 52833238 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,340,474 | 0.029306 | 52833238 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 9,972,211 | 0.029321 | 52833238 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,867,575 | 0.000012 | 52833238 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 8,339,203 | 2,392.298669 | 52833238 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/USDC | 3000 | 8,300,907 | 2,396.727691 | 52833238 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | USDC/cbBTC | 360 | 7,816,474 | 0.000012 | 52833238 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 564 | 7,396,271 | 2,393.129838 | 52833238 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,170,068 | 0.001672 | 52833238 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 600 | 6,792,514 | 0.000012 | 52833238 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,333,956 | 0.029387 | 52833238 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | fBOMB/AERO | 10000 | 4,894,135 | 0.025626 | 52833238 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,775,305 | 0.802395 | 52833238 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,618,423 | 0.000274 | 52833238 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,432,889 | 2,393.182104 | 52833238 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,323,792 | 0.998768 | 52833238 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome_slipstream | WETH/USDT | 421 | 4,254,110 | 2,395.688495 | 52833238 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome | WETH/KTA | 3000 | 4,020,374 | 33,712.106784 | 52833238 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/AERO | 10000 | 3,223,957 | 3,045.567433 | 52833238 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | USDC/AERO | 10000 | 3,170,931 | 1.269249 | 52833238 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,853,039 | 0.000012 | 52833238 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,712,565 | 1.142180 | 52833238 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| aerodrome_slipstream | WETH/VVV | 2724 | 2,641,190 | 99.228434 | 52833238 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,626,304 | 402.081320 | 52833238 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | WETH/MORPHO | 2715 | 2,482,250 | 967.020195 | 52833238 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome | WETH/FAI | 10000 | 2,180,743 | 1,226,346.894757 | 52833238 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 2,148,441 | 0.000010 | 52833238 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,059,184 | 1.238174 | 52833238 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,036,084 | 1.373409 | 52833238 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| uniswap_v3 | BNKR/WETH | 10000 | 2,011,025 | 0.000000 | 52833238 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,815,721 | 16.130504 | 52833238 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| uniswap_v3 | XDP/USDC | 100 | 1,801,169 | 0.019275 | 52833238 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,773,770 | 0.000012 | 52833238 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | weETH_04c0/WETH | 500 | 1,733,981 | 1.105525 | 52833238 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome | fBOMB/USDC | 10000 | 1,672,718 | 0.020215 | 52833238 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| aerodrome | WETH/msETH (stable) | 500 | 1,644,067 | 2.307332 | 52833238 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,561,288 | 13,708.090381 | 52833238 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,552,501 | 0.916343 | 52833238 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| aerodrome_slipstream | EURC/USDC | 73 | 1,533,359 | 1.121640 | 52833238 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| uniswap_v3 | WETH/AERO | 3000 | 1,493,371 | 3,048.170825 | 52833238 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,457,172 | 0.826863 | 52833238 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | DRB/WETH | 10000 | 1,304,786 | 0.000000 | 52833238 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,301,733 | 0.004709 | 52833238 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,294,706 | 0.000276 | 52833238 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | WETH/cbBTC | 3000 | 1,281,202 | 0.029299 | 52833238 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| aerodrome | USDC/SEND | 3000 | 1,230,534 | 64.173528 | 52833238 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome | WETH/WELL | 10000 | 1,219,134 | 1,048,027.254496 | 52833238 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,211,734 | 23.009238 | 52833238 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,210,682 | 2,392.268874 | 52833238 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | WETH/doginme | 10000 | 1,193,345 | 35,376,680.519362 | 52833238 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,167,401 | 0.435758 | 52833238 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| aerodrome_slipstream | msUSD/USDC | 503 | 1,133,876 | 0.885551 | 52833238 | `0x7501bc8Bb51616F79bfA524E464fb7B41f0B10fB` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,133,367 | 508,665.214646 | 52833238 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome_slipstream | WETH/msETH | 500 | 1,129,897 | 1.131631 | 52833238 | `0x74F72788F4814D7fF3C49B44684aa98Eee140C0E` |
| aerodrome | USDC/NOCK | 3000 | 1,113,053 | 50.859895 | 52833238 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | USDC/USDT | 11 | 1,077,496 | 1.001406 | 52833238 | `0xa41Bc0AFfbA7Fd420d186b84899d7ab2aC57fcD1` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,074,756 | 15.625391 | 52833238 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |

## Recherche d'opportunités
- Cycles : 17976 ; routes examinées : 378610512 ; candidats optimisés : 2142820 ; net attendu > 0 : 41 ; dernier cycle 215.1 ms
- Rejets (moteur) : {'spread_below_threshold': 372982170, 'liquidity_below_min': 3033823, 'negative_expected_net': 2142779, 'borrow_bound_too_small': 449332, 'cycle_budget_exhausted': 2367}
- Enregistrements de la session : 2142820 ; net attendu > 0 : 41 ; simulés (eth_call de la vraie tx) : 1 (ok 0, échec 1) ; étiquettes ghost N+1 : 0/1 positives
- Décisions : {'REJECTED': 2142820} ; motifs de rejet : {'below_safety_margin': 40, 'negative_expected_net': 2142779, 'p_lower_below_threshold': 36, 'reliability_not_demonstrated': 5, 'simulation_failed': 1}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52829937 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 71.479846 USDC | 0.079497 USDC | 0.000000 USDC | 0.005776 USDC | 0.073721 USDC (0.0678 €) | — | 10.31 | 0.000 (n=35) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 52825003 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→EURC→[aerodrome_slipstream]→cbBTC | 0.002113 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0166 €) | — | 1.04 | 0.113 (n=158) | REJECTED | below_safety_margin(22<42), p_lower_below_threshold(0.11<0.75) |
| 52825003 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→EURC→[aerodrome_slipstream]→cbBTC | 0.002113 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0166 €) | — | 1.04 | 0.113 (n=158) | REJECTED | below_safety_margin(22<42), p_lower_below_threshold(0.11<0.75) |
| 52825003 | USDC→[aerodrome_slipstream]→EURC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 178.132705 USDC | 0.024804 USDC | 0.000000 USDC | 0.007210 USDC | 0.017594 USDC (0.0162 €) | — | 0.99 | 0.113 (n=158) | REJECTED | below_safety_margin(17594<35626), p_lower_below_threshold(0.11<0.75) |
| 52825003 | USDC→[aerodrome_slipstream]→EURC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 178.132705 USDC | 0.024804 USDC | 0.000000 USDC | 0.007210 USDC | 0.017594 USDC (0.0162 €) | — | 0.99 | 0.113 (n=158) | REJECTED | below_safety_margin(17594<35626), p_lower_below_threshold(0.11<0.75) |
| 52830940 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→USDC | 83.817978 USDC | 0.022036 USDC | 0.000000 USDC | 0.005410 USDC | 0.016626 USDC (0.0153 €) | — | 1.98 | 0.042 (n=7) | REJECTED | below_safety_margin(16626<16763), reliability_not_demonstrated |
| 52830941 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→USDC | 83.817978 USDC | 0.022036 USDC | 0.000000 USDC | 0.005410 USDC | 0.016626 USDC (0.0153 €) | — | 1.98 | 0.042 (n=7) | REJECTED | below_safety_margin(16626<16763), reliability_not_demonstrated |
| 52830941 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→USDC | 83.817978 USDC | 0.022036 USDC | 0.000000 USDC | 0.005410 USDC | 0.016626 USDC (0.0153 €) | — | 1.98 | 0.042 (n=7) | REJECTED | below_safety_margin(16626<16763), reliability_not_demonstrated |
| 52825003 | USDC→[aerodrome_slipstream]→EURC→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→USDC | 230.403378 USDC | 0.015615 USDC | 0.000000 USDC | 0.007210 USDC | 0.008405 USDC (0.0077 €) | — | 0.36 | 0.280 (n=75) | REJECTED | below_safety_margin(8405<46080), p_lower_below_threshold(0.28<0.75) |
| 52825003 | USDC→[aerodrome_slipstream]→EURC→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→USDC | 230.403378 USDC | 0.015615 USDC | 0.000000 USDC | 0.007210 USDC | 0.008405 USDC (0.0077 €) | — | 0.36 | 0.280 (n=75) | REJECTED | below_safety_margin(8405<46080), p_lower_below_threshold(0.28<0.75) |
| 52825003 | cbBTC→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→EURC→[aerodrome_slipstream]→cbBTC | 0.002551 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0075 €) | — | 0.39 | 0.280 (n=75) | REJECTED | below_safety_margin(10<51), p_lower_below_threshold(0.28<0.75) |
| 52825003 | cbBTC→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→EURC→[aerodrome_slipstream]→cbBTC | 0.002551 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0075 €) | — | 0.39 | 0.280 (n=75) | REJECTED | below_safety_margin(10<51), p_lower_below_threshold(0.28<0.75) |
| 52825003 | cbBTC→[uniswap_v3]→USDC→[aerodrome_slipstream]→EURC→[aerodrome_slipstream]→cbBTC | 0.002436 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0068 €) | — | 0.37 | 0.280 (n=75) | REJECTED | below_safety_margin(9<48), p_lower_below_threshold(0.28<0.75) |
| 52825003 | cbBTC→[uniswap_v3]→USDC→[aerodrome_slipstream]→EURC→[aerodrome_slipstream]→cbBTC | 0.002436 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0068 €) | — | 0.37 | 0.280 (n=75) | REJECTED | below_safety_margin(9<48), p_lower_below_threshold(0.28<0.75) |
| 52825003 | USDC→[aerodrome_slipstream]→EURC→[aerodrome_slipstream]→cbBTC→[uniswap_v3]→USDC | 230.403378 USDC | 0.013944 USDC | 0.000000 USDC | 0.007210 USDC | 0.006734 USDC (0.0062 €) | — | 0.29 | 0.280 (n=75) | REJECTED | below_safety_margin(6734<46080), p_lower_below_threshold(0.28<0.75) |
| 52825003 | USDC→[aerodrome_slipstream]→EURC→[aerodrome_slipstream]→cbBTC→[uniswap_v3]→USDC | 230.403378 USDC | 0.013944 USDC | 0.000000 USDC | 0.007210 USDC | 0.006734 USDC (0.0062 €) | — | 0.29 | 0.280 (n=75) | REJECTED | below_safety_margin(6734<46080), p_lower_below_threshold(0.28<0.75) |
| 52825003 | cbBTC→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→EURC→[aerodrome_slipstream]→cbBTC | 0.002551 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0045 €) | — | 0.24 | 0.280 (n=75) | REJECTED | below_safety_margin(6<51), p_lower_below_threshold(0.28<0.75) |
| 52825003 | cbBTC→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→EURC→[aerodrome_slipstream]→cbBTC | 0.002551 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0045 €) | — | 0.24 | 0.280 (n=75) | REJECTED | below_safety_margin(6<51), p_lower_below_threshold(0.28<0.75) |
| 52825003 | USDC→[aerodrome_slipstream]→EURC→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→USDC | 192.067166 USDC | 0.012104 USDC | 0.000000 USDC | 0.007210 USDC | 0.004894 USDC (0.0045 €) | — | 0.25 | 0.280 (n=75) | REJECTED | below_safety_margin(4894<38413), p_lower_below_threshold(0.28<0.75) |
| 52825003 | USDC→[aerodrome_slipstream]→EURC→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→USDC | 192.067166 USDC | 0.012104 USDC | 0.000000 USDC | 0.007210 USDC | 0.004894 USDC (0.0045 €) | — | 0.25 | 0.280 (n=75) | REJECTED | below_safety_margin(4894<38413), p_lower_below_threshold(0.28<0.75) |
| 52825003 | USDC→[aerodrome_slipstream]→EURC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 179.501113 USDC | 0.010639 USDC | 0.000000 USDC | 0.007210 USDC | 0.003429 USDC (0.0032 €) | — | 0.19 | 0.113 (n=158) | REJECTED | below_safety_margin(3429<35900), p_lower_below_threshold(0.11<0.75) |
| 52825003 | USDC→[aerodrome_slipstream]→EURC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 179.501113 USDC | 0.010639 USDC | 0.000000 USDC | 0.007210 USDC | 0.003429 USDC (0.0032 €) | — | 0.19 | 0.113 (n=158) | REJECTED | below_safety_margin(3429<35900), p_lower_below_threshold(0.11<0.75) |
| 52825003 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→EURC→[aerodrome_slipstream]→cbBTC | 0.002552 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0030 €) | — | 0.16 | 0.113 (n=158) | REJECTED | below_safety_margin(4<51), p_lower_below_threshold(0.11<0.75) |
| 52825003 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→EURC→[aerodrome_slipstream]→cbBTC | 0.002552 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0030 €) | — | 0.16 | 0.113 (n=158) | REJECTED | below_safety_margin(4<51), p_lower_below_threshold(0.11<0.75) |
| 52825003 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→EURC→[aerodrome_slipstream]→cbBTC | 0.001291 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0023 €) | — | 0.23 | 0.113 (n=158) | REJECTED | below_safety_margin(3<25), p_lower_below_threshold(0.11<0.75) |

## Fiabilité et décision
- Observations ghost : 1336 ; taux observé 0.103 ; borne inférieure crédible (0.9) 0.093 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 9.3% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
