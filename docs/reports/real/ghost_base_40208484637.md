# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-25T15:53:15+00:00 ; durée 3.05 min ; blocs 53077030 → 53077124 (93 vus)

## Connexion
- Requêtes RPC : 1217 ; erreurs : 0 ; latence p50/p95 : 114.1/933.2 ms
- Rafraîchissements d'état : 93 ; âge des données au dernier bloc : 2.55 s ; changements de frais LP observés (pools à frais dynamiques) : 73
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 843 ; cycles déclenchés par événement : 141 ; avance médiane sur le rafraîchissement multicall : 281 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,340.83 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 531 pools, 306 jetons, 19476 routes
- Par DEX : uniswap_v3 142, aerodrome 215, aerodrome_slipstream 127, pancakeswap_v3 31, uniswap_v2 13, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 191 (rejetés 2) → 596 jetons ; pools candidats 3792 (énumérés 341, par paires 0), mesurés 533, sous le plancher de 10000.0 $ : 2 → gardés 531 (max 1500) ; prix des hubs : {'USDC': 1.0, 'USDbC': 1.0, 'DAI': 1.0, 'WETH': 2340.831442, 'cbBTC': 80585.156098, 'AERO': 0.694811}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 158,545,556 | 2,340.831443 | 53077124 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 17,496,993 | 0.029082 | 53077124 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,236,512 | 0.029036 | 53077124 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,528,762 | 0.000012 | 53077124 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome | WETH/VVV | 3000 | 8,877,305 | 94.274022 | 53077124 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/USDC | 500 | 8,435,268 | 2,343.209938 | 53077124 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | USDC/AERO | 3000 | 7,620,524 | 1.439241 | 53077124 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,019,728 | 0.001647 | 53077124 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | WETH/USDC | 150 | 5,496,741 | 2,342.620648 | 53077124 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,362,313 | 0.029072 | 53077124 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,434,645 | 2,342.475293 | 53077124 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,231,804 | 1.000001 | 53077124 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,824,368 | 35,067.700992 | 53077124 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/USDC | 3000 | 3,792,362 | 2,341.135308 | 53077124 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 3,231,274 | 0.029049 | 53077124 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | USDC/cbBTC | 400 | 2,800,208 | 0.000012 | 53077124 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome_slipstream | WETH/VVV | 2700 | 2,513,025 | 94.271195 | 53077124 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,222,302 | 408.845421 | 53077124 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | WETH/FAI | 10000 | 2,123,219 | 1,232,309.517849 | 53077124 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,905,738 | 0.000012 | 53077124 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,895,755 | 0.000000 | 53077124 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,779,598 | 0.017851 | 53077124 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,728,070 | 0.000012 | 53077124 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | USDC/cbBTC | 330 | 1,719,378 | 0.000012 | 53077124 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | VIRTUAL/WETH | 10000 | 1,569,822 | 0.000264 | 53077124 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,470,515 | 1.673913 | 53077124 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,458,798 | 0.825924 | 53077124 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,448,947 | 3,375.182890 | 53077124 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,417,091 | 0.005448 | 53077124 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,373,270 | 14,077.084724 | 53077124 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,288,673 | 2,343.408477 | 53077124 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | WETH/AERO | 10000 | 1,273,637 | 3,377.387910 | 53077124 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,242,563 | 0.000266 | 53077124 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | USDC/SEND | 3000 | 1,221,986 | 65.074320 | 53077124 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,166,168 | 35,442,699.207148 | 53077124 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | DRB/WETH | 10000 | 1,142,415 | 0.000000 | 53077124 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | WETH/WELL | 10000 | 1,128,475 | 1,128,935.071163 | 53077124 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,124,548 | 496,597.944493 | 53077124 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | USDC/NOCK | 3000 | 1,079,918 | 53.707752 | 53077124 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,044,559 | 16.787874 | 53077124 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | WETH/EDEL | 7000 | 1,033,455 | 78,623.418351 | 53077124 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,023,804 | 21,896,670.763972 | 53077124 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | USDC/VVV | 3000 | 969,461 | 0.040191 | 53077124 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/USDC | 10000 | 925,689 | 2,339.197561 | 53077124 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome | WETH/msETH (stable) | 500 | 918,086 | 2.310010 | 53077124 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | uXRP/WETH | 3000 | 897,824 | 0.000551 | 53077124 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| uniswap_v3 | WETH/MORPHO | 3000 | 897,529 | 1,121.553868 | 53077124 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 886,162 | 17.167207 | 53077124 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 880,598 | 17.909629 | 53077124 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v3 | WETH/VVV | 10000 | 873,337 | 94.396861 | 53077124 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v2 | WETH/USDC | 3000 | 848,504 | 2,340.827954 | 53077124 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 812,620 | 0.000009 | 53077124 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | WETH/wstETH | 3000 | 792,571 | 0.803130 | 53077124 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| pancakeswap_v3 | QUID/USDC | 100 | 786,995 | 0.055467 | 53077124 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | weETH_04c0/WETH | 500 | 782,570 | 1.105853 | 53077124 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 745,727 | 0.624374 | 53077124 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 744,315 | 4,668,648.923183 | 53077124 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 733,923 | 0.674637 | 53077124 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/NPC | 3000 | 711,804 | 136,092.169099 | 53077124 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | WETH/BRETT | 2120 | 699,599 | 493,477.448652 | 53077124 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |

## Recherche d'opportunités
- Cycles : 233 ; routes examinées : 4537908 ; candidats optimisés : 13864 ; net attendu > 0 : 43 ; dernier cycle 136.9 ms
- Rejets (moteur) : {'spread_below_threshold': 4440299, 'liquidity_below_min': 79784, 'negative_expected_net': 13821, 'unquotable': 3728, 'borrow_bound_too_small': 233}
- Enregistrements de la session : 13864 ; net attendu > 0 : 43 ; simulés (eth_call de la vraie tx) : 3 (ok 0, échec 3) ; étiquettes ghost N+1 : 0/3 positives
- Décisions : {'REJECTED': 13864} ; motifs de rejet : {'below_safety_margin': 7, 'negative_expected_net': 13821, 'p_lower_below_threshold': 9, 'reliability_not_demonstrated': 34, 'simulation_failed': 3}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53077050 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→USDC | 144.421525 USDC | 0.582084 USDC | 0.000000 USDC | 0.007034 USDC | 0.575050 USDC (0.5290 €) | — | 39.82 | 0.000 (n=19) | REJECTED | reliability_not_demonstrated |
| 53077050 | cbBTC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.001794 cbBTC | 0.000007 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000007 cbBTC (0.5286 €) | — | 39.79 | 0.000 (n=19) | REJECTED | reliability_not_demonstrated |
| 53077050 | USDC→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→USDC | 140.174229 USDC | 0.549960 USDC | 0.000000 USDC | 0.007034 USDC | 0.542926 USDC (0.4995 €) | — | 38.73 | 0.000 (n=26) | REJECTED | reliability_not_demonstrated |
| 53077050 | cbBTC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→cbBTC | 0.001723 cbBTC | 0.000007 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000007 cbBTC (0.4990 €) | — | 39.13 | 0.000 (n=26) | REJECTED | reliability_not_demonstrated |
| 53077050 | USDC→[uniswap_v3]→cbBTC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→USDC | 138.630106 USDC | 0.546939 USDC | 0.000000 USDC | 0.007034 USDC | 0.539905 USDC (0.4967 €) | — | 38.95 | 0.000 (n=26) | REJECTED | reliability_not_demonstrated |
| 53077050 | USDC→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→USDC | 140.172019 USDC | 0.546512 USDC | 0.000000 USDC | 0.007034 USDC | 0.539478 USDC (0.4963 €) | — | 38.49 | 0.000 (n=26) | REJECTED | reliability_not_demonstrated |
| 53077050 | cbBTC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→USDC→[uniswap_v3]→cbBTC | 0.001722 cbBTC | 0.000007 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000007 cbBTC (0.4960 €) | — | 38.91 | 0.000 (n=26) | REJECTED | reliability_not_demonstrated |
| 53077050 | cbBTC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→cbBTC | 0.001723 cbBTC | 0.000007 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000007 cbBTC (0.4960 €) | — | 38.89 | 0.000 (n=26) | REJECTED | reliability_not_demonstrated |
| 53077050 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→USDC | 135.753494 USDC | 0.517248 USDC | 0.000000 USDC | 0.007034 USDC | 0.510214 USDC (0.4694 €) | — | 37.58 | 0.000 (n=19) | REJECTED | reliability_not_demonstrated |
| 53077050 | cbBTC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.001622 cbBTC | 0.000006 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000006 cbBTC (0.4686 €) | — | 39.02 | 0.000 (n=19) | REJECTED | reliability_not_demonstrated |
| 53077050 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→USDC | 78.587488 USDC | 0.488701 USDC | 0.000000 USDC | 0.007034 USDC | 0.481667 USDC (0.4431 €) | — | 61.29 | 0.000 (n=16) | REJECTED | reliability_not_demonstrated |
| 53077050 | USDC→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→USDC | 78.494561 USDC | 0.488214 USDC | 0.000000 USDC | 0.007034 USDC | 0.481180 USDC (0.4427 €) | — | 61.30 | 0.000 (n=22) | REJECTED | reliability_not_demonstrated |
| 53077050 | WETH→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.033519 WETH | 0.000208 WETH | 0.000000 WETH | 0.000003 WETH | 0.000205 WETH (0.4425 €) | — | 61.30 | 0.000 (n=16) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53077050 | WETH→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→WETH | 0.033498 WETH | 0.000208 WETH | 0.000000 WETH | 0.000003 WETH | 0.000205 WETH (0.4421 €) | — | 61.28 | 0.000 (n=22) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53077050 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→USDC | 77.987693 USDC | 0.484268 USDC | 0.000000 USDC | 0.007034 USDC | 0.477234 USDC (0.4391 €) | — | 61.19 | 0.000 (n=22) | REJECTED | reliability_not_demonstrated |
| 53077050 | WETH→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.033301 WETH | 0.000207 WETH | 0.000000 WETH | 0.000003 WETH | 0.000204 WETH (0.4384 €) | — | 61.13 | 0.000 (n=22) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53077050 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→USDC | 76.715099 USDC | 0.466125 USDC | 0.000000 USDC | 0.007034 USDC | 0.459091 USDC (0.4224 €) | — | 59.84 | 0.000 (n=22) | REJECTED | reliability_not_demonstrated |
| 53077050 | WETH→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.032720 WETH | 0.000199 WETH | 0.000000 WETH | 0.000003 WETH | 0.000196 WETH (0.4216 €) | — | 59.84 | 0.000 (n=22) | REJECTED | reliability_not_demonstrated |
| 53077050 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→USDC | 75.799770 USDC | 0.456378 USDC | 0.000000 USDC | 0.007034 USDC | 0.449344 USDC (0.4134 €) | — | 59.28 | 0.000 (n=16) | REJECTED | reliability_not_demonstrated |
| 53077050 | WETH→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.032366 WETH | 0.000195 WETH | 0.000000 WETH | 0.000003 WETH | 0.000192 WETH (0.4126 €) | — | 59.20 | 0.000 (n=16) | REJECTED | reliability_not_demonstrated |
| 53077050 | USDC→[sushiswap_v3]→WETH→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→USDC | 73.499679 USDC | 0.441619 USDC | 0.000000 USDC | 0.007034 USDC | 0.434585 USDC (0.3998 €) | — | 59.13 | 0.000 (n=22) | REJECTED | reliability_not_demonstrated |
| 53077050 | WETH→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→USDC→[sushiswap_v3]→WETH | 0.031375 WETH | 0.000188 WETH | 0.000000 WETH | 0.000003 WETH | 0.000185 WETH (0.3989 €) | — | 59.04 | 0.000 (n=22) | REJECTED | reliability_not_demonstrated |
| 53077050 | USDC→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→USDC | 67.385578 USDC | 0.421060 USDC | 0.000000 USDC | 0.007389 USDC | 0.413671 USDC (0.3806 €) | — | 61.39 | 0.000 (n=22) | REJECTED | reliability_not_demonstrated |
| 53077050 | WETH→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→WETH | 0.028728 WETH | 0.000179 WETH | 0.000000 WETH | 0.000003 WETH | 0.000176 WETH (0.3794 €) | — | 61.32 | 0.000 (n=22) | REJECTED | reliability_not_demonstrated |
| 53077050 | USDC→[uniswap_v3]→cbBTC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→USDC | 121.316344 USDC | 0.407801 USDC | 0.000000 USDC | 0.007034 USDC | 0.400767 USDC (0.3687 €) | — | 33.03 | 0.000 (n=26) | REJECTED | reliability_not_demonstrated |

## Fiabilité et décision
- Observations ghost : 2457 ; taux observé 0.093 ; borne inférieure crédible (0.9) 0.086 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 8.6% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
