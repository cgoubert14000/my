# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-24T12:00:55+00:00 ; durée 36.65 min ; blocs 53025852 → 53026953 (1099 vus)

## Connexion
- Requêtes RPC : 13518 ; erreurs : 0 ; latence p50/p95 : 170.1/671.3 ms
- Rafraîchissements d'état : 1100 ; âge des données au dernier bloc : 1.8 s ; changements de frais LP observés (pools à frais dynamiques) : 830
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 17246 ; cycles déclenchés par événement : 1318 ; avance médiane sur le rafraîchissement multicall : 269 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,363.68 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 536 pools, 308 jetons, 19360 routes
- Par DEX : uniswap_v3 143, aerodrome 216, aerodrome_slipstream 133, pancakeswap_v3 29, uniswap_v2 12, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 193 (rejetés 2) → 598 jetons ; pools candidats 3806 (énumérés 348, par paires 0), mesurés 538, sous le plancher de 10000.0 $ : 2 → gardés 536 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDbC': 1.0, 'USDC': 1.0, 'WETH': 2363.674955, 'cbBTC': 80533.217668, 'AERO': 0.705694}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 155,352,992 | 2,363.678372 | 53026953 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,985,811 | 0.029356 | 53026953 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 12,229,524 | 98.003399 | 53026953 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,143,245 | 0.029383 | 53026953 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,564,447 | 0.000012 | 53026953 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome | USDC/AERO | 3000 | 8,924,535 | 1.421769 | 53026953 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/USDC | 500 | 8,538,761 | 2,363.373213 | 53026953 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 8,499,730 | 0.029369 | 53026953 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,019,171 | 0.001646 | 53026953 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 334 | 6,302,799 | 0.000012 | 53026953 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 150 | 5,503,953 | 2,362.537500 | 53026953 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,429,371 | 0.029352 | 53026953 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | USDC/cbBTC | 400 | 4,862,592 | 0.000012 | 53026953 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,586,357 | 2,362.457771 | 53026953 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,238,764 | 0.998962 | 53026953 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,916,186 | 34,497.307293 | 53026953 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/USDC | 3000 | 3,828,821 | 2,359.301745 | 53026953 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | WETH/USDT | 400 | 2,779,415 | 2,372.752954 | 53026953 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome_slipstream | WETH/VVV | 2712 | 2,501,598 | 98.029833 | 53026953 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,245,308 | 408.889376 | 53026953 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | WETH/FAI | 10000 | 2,118,651 | 1,261,906.512700 | 53026953 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome | WETH/AERO | 10000 | 1,922,002 | 3,330.627559 | 53026953 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,920,078 | 0.000000 | 53026953 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,914,118 | 0.000012 | 53026953 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v3 | XDP/USDC | 100 | 1,800,340 | 0.018238 | 53026953 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,736,952 | 0.000012 | 53026953 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | VIRTUAL/WETH | 10000 | 1,604,122 | 0.000267 | 53026953 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,549,717 | 1.610679 | 53026953 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | WETH/AERO | 3000 | 1,463,449 | 3,355.550993 | 53026953 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,458,989 | 0.825712 | 53026953 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,393,905 | 0.005222 | 53026953 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,378,594 | 13,932.086892 | 53026953 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,281,592 | 2,363.327335 | 53026953 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,260,521 | 0.000266 | 53026953 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | WETH/msETH (stable) | 500 | 1,231,079 | 2.308317 | 53026953 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome | USDC/SEND | 3000 | 1,225,112 | 64.742662 | 53026953 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | DRB/WETH | 10000 | 1,197,284 | 0.000000 | 53026953 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/doginme | 10000 | 1,178,475 | 35,296,733.949307 | 53026953 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | WETH/WELL | 10000 | 1,146,332 | 1,120,074.502516 | 53026953 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome | USDC/NOCK | 3000 | 1,134,654 | 48.650721 | 53026953 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,131,851 | 493,533.548554 | 53026953 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,095,816 | 16.864081 | 53026953 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | WETH/EDEL | 7000 | 1,077,135 | 73,814.911241 | 53026953 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,041,130 | 16.935893 | 53026953 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,039,430 | 21,654,616.189288 | 53026953 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | USDC/VVV | 3000 | 1,032,967 | 0.041469 | 53026953 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 955,259 | 23.314033 | 53026953 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| uniswap_v3 | WETH/MORPHO | 3000 | 925,163 | 1,091.676813 | 53026953 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | uXRP/WETH | 3000 | 895,889 | 0.000539 | 53026953 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 887,519 | 17.666203 | 53026953 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v2 | WETH/USDC | 3000 | 852,590 | 2,363.849963 | 53026953 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | AERO/cbBTC | 2700 | 845,004 | 0.000009 | 53026953 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | weETH_04c0/WETH | 500 | 813,506 | 1.105904 | 53026953 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| pancakeswap_v3 | QUID/USDC | 100 | 812,596 | 0.059348 | 53026953 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 800,366 | 0.803010 | 53026953 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | WETH/USDC | 10000 | 788,086 | 2,373.719186 | 53026953 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/VVV | 10000 | 772,893 | 97.313184 | 53026953 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 755,740 | 0.628255 | 53026953 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 749,091 | 4,698,503.819310 | 53026953 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 728,390 | 0.665325 | 53026953 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |

## Recherche d'opportunités
- Cycles : 2417 ; routes examinées : 46793120 ; candidats optimisés : 172438 ; net attendu > 0 : 71 ; dernier cycle 88.3 ms
- Rejets (moteur) : {'spread_below_threshold': 46147652, 'liquidity_below_min': 356921, 'negative_expected_net': 172367, 'pool_quarantined': 113692, 'borrow_bound_too_small': 2417}
- Enregistrements de la session : 172438 ; net attendu > 0 : 71 ; simulés (eth_call de la vraie tx) : 7 (ok 0, échec 7) ; étiquettes ghost N+1 : 0/7 positives
- Décisions : {'REJECTED': 172438} ; motifs de rejet : {'below_safety_margin': 35, 'negative_expected_net': 172367, 'p_lower_below_threshold': 50, 'reliability_not_demonstrated': 21, 'simulation_failed': 7}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53026232 | USDC→[uniswap_v3]→ZORA→[aerodrome_slipstream]→USDC | 451.845630 USDC | 2.035784 USDC | 0.000000 USDC | 0.005666 USDC | 2.030118 USDC (1.8677 €) | — | 44.93 | 0.001 (n=8) | REJECTED | reliability_not_demonstrated |
| 53026232 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→ZORA→[aerodrome_slipstream]→USDC | 61.934750 USDC | 0.298651 USDC | 0.000000 USDC | 0.007461 USDC | 0.291190 USDC (0.2679 €) | — | 47.02 | 0.001 (n=12) | REJECTED | reliability_not_demonstrated |
| 53026232 | WETH→[uniswap_v3]→ZORA→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.026243 WETH | 0.000126 WETH | 0.000000 WETH | 0.000003 WETH | 0.000123 WETH (0.2678 €) | — | 46.93 | 0.001 (n=12) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53026232 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→ZORA→[aerodrome_slipstream]→USDC | 61.527832 USDC | 0.295603 USDC | 0.000000 USDC | 0.007461 USDC | 0.288142 USDC (0.2651 €) | — | 46.83 | 0.001 (n=12) | REJECTED | reliability_not_demonstrated |
| 53026232 | WETH→[uniswap_v3]→ZORA→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.026062 WETH | 0.000125 WETH | 0.000000 WETH | 0.000003 WETH | 0.000122 WETH (0.2650 €) | — | 46.76 | 0.001 (n=12) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53026232 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→ZORA→[aerodrome_slipstream]→USDC | 61.284891 USDC | 0.294052 USDC | 0.000000 USDC | 0.007461 USDC | 0.286591 USDC (0.2637 €) | — | 46.76 | 0.001 (n=12) | REJECTED | reliability_not_demonstrated |
| 53026232 | WETH→[uniswap_v3]→ZORA→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.025939 WETH | 0.000124 WETH | 0.000000 WETH | 0.000003 WETH | 0.000121 WETH (0.2636 €) | — | 46.72 | 0.001 (n=12) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53026232 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→ZORA→[aerodrome_slipstream]→USDC | 61.487946 USDC | 0.293868 USDC | 0.000000 USDC | 0.007461 USDC | 0.286407 USDC (0.2635 €) | — | 46.58 | 0.001 (n=12) | REJECTED | reliability_not_demonstrated |
| 53026232 | WETH→[uniswap_v3]→ZORA→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→WETH | 0.026013 WETH | 0.000124 WETH | 0.000000 WETH | 0.000003 WETH | 0.000121 WETH (0.2634 €) | — | 46.56 | 0.001 (n=12) | REJECTED | reliability_not_demonstrated |
| 53026232 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→ZORA→[aerodrome_slipstream]→USDC | 60.801465 USDC | 0.288406 USDC | 0.000000 USDC | 0.007461 USDC | 0.280945 USDC (0.2585 €) | — | 46.21 | 0.001 (n=12) | REJECTED | reliability_not_demonstrated |
| 53026232 | WETH→[uniswap_v3]→ZORA→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.025786 WETH | 0.000122 WETH | 0.000000 WETH | 0.000003 WETH | 0.000119 WETH (0.2583 €) | — | 46.07 | 0.001 (n=12) | REJECTED | reliability_not_demonstrated |
| 53026232 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→ZORA→[aerodrome_slipstream]→USDC | 55.293015 USDC | 0.278215 USDC | 0.000000 USDC | 0.007461 USDC | 0.270754 USDC (0.2491 €) | — | 48.97 | 0.001 (n=12) | REJECTED | reliability_not_demonstrated |
| 53026232 | WETH→[uniswap_v3]→ZORA→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→WETH | 0.023398 WETH | 0.000118 WETH | 0.000000 WETH | 0.000003 WETH | 0.000114 WETH (0.2487 €) | — | 48.89 | 0.001 (n=12) | REJECTED | reliability_not_demonstrated |
| 53026232 | USDC→[sushiswap_v3]→WETH→[uniswap_v3]→ZORA→[aerodrome_slipstream]→USDC | 58.273143 USDC | 0.272763 USDC | 0.000000 USDC | 0.007461 USDC | 0.265302 USDC (0.2441 €) | — | 45.53 | 0.001 (n=12) | REJECTED | reliability_not_demonstrated |
| 53026232 | WETH→[uniswap_v3]→ZORA→[aerodrome_slipstream]→USDC→[sushiswap_v3]→WETH | 0.024662 WETH | 0.000115 WETH | 0.000000 WETH | 0.000003 WETH | 0.000112 WETH (0.2439 €) | — | 45.47 | 0.001 (n=12) | REJECTED | reliability_not_demonstrated |
| 53026232 | USDC→[uniswap_v2]→WETH→[uniswap_v3]→ZORA→[aerodrome_slipstream]→USDC | 43.803670 USDC | 0.153877 USDC | 0.000000 USDC | 0.006368 USDC | 0.147509 USDC (0.1357 €) | — | 33.68 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 53026232 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→ZORA→[aerodrome_slipstream]→USDC | 44.618570 USDC | 0.154884 USDC | 0.000000 USDC | 0.007461 USDC | 0.147423 USDC (0.1356 €) | — | 33.04 | 0.001 (n=12) | REJECTED | reliability_not_demonstrated |
| 53026232 | WETH→[uniswap_v3]→ZORA→[aerodrome_slipstream]→USDC→[uniswap_v2]→WETH | 0.018500 WETH | 0.000065 WETH | 0.000000 WETH | 0.000003 WETH | 0.000062 WETH (0.1353 €) | — | 33.62 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 53026232 | WETH→[uniswap_v3]→ZORA→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.018827 WETH | 0.000065 WETH | 0.000000 WETH | 0.000003 WETH | 0.000062 WETH (0.1352 €) | — | 33.02 | 0.001 (n=12) | REJECTED | reliability_not_demonstrated |
| 53026232 | USDC→[aerodrome]→WETH→[uniswap_v3]→ZORA→[aerodrome_slipstream]→USDC | 41.599469 USDC | 0.135328 USDC | 0.000000 USDC | 0.006776 USDC | 0.128552 USDC (0.1183 €) | — | 30.90 | 0.003 (n=93) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53026232 | WETH→[uniswap_v3]→ZORA→[aerodrome_slipstream]→USDC→[aerodrome]→WETH | 0.017557 WETH | 0.000057 WETH | 0.000000 WETH | 0.000003 WETH | 0.000054 WETH (0.1178 €) | — | 30.86 | 0.003 (n=93) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53025864 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 53.071423 USDC | 0.064455 USDC | 0.000000 USDC | 0.005307 USDC | 0.059148 USDC (0.0544 €) | — | 11.14 | 0.000 (n=50) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 53026140 | WETH→[uniswap_v3]→ZORA→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.009236 WETH | 0.000016 WETH | 0.000000 WETH | 0.000003 WETH | 0.000013 WETH (0.0277 €) | — | 13.78 | 0.000 (n=34) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 53026140 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→ZORA→[aerodrome_slipstream]→USDC | 21.754914 USDC | 0.037187 USDC | 0.000000 USDC | 0.007103 USDC | 0.030084 USDC (0.0277 €) | — | 13.83 | 0.000 (n=34) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53026140 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→ZORA→[aerodrome_slipstream]→USDC | 21.714709 USDC | 0.036699 USDC | 0.000000 USDC | 0.007103 USDC | 0.029596 USDC (0.0272 €) | — | 13.63 | 0.000 (n=39) | REJECTED | p_lower_below_threshold(0.00<0.75) |

## Fiabilité et décision
- Observations ghost : 2138 ; taux observé 0.096 ; borne inférieure crédible (0.9) 0.088 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 8.8% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
