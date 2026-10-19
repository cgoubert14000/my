# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-19T06:21:55+00:00 ; durée 272.24 min ; blocs 52792613 → 52800772 (7307 vus)

## Connexion
- Requêtes RPC : 100778 ; erreurs : 145 ; latence p50/p95 : 392.5/1,770.7 ms
- Rafraîchissements d'état : 7308 ; âge des données au dernier bloc : 3.91 s ; changements de frais LP observés (pools à frais dynamiques) : 13141
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 131597 ; cycles déclenchés par événement : 7424 ; avance médiane sur le rafraîchissement multicall : 1,272 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,427.07 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 574 pools, 328 jetons, 21112 routes
- Par DEX : uniswap_v3 137, aerodrome 234, aerodrome_slipstream 156, pancakeswap_v3 30, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 207 (rejetés 2) → 612 jetons ; pools candidats 3877 (énumérés 392, par paires 0), mesurés 576, sous le plancher de 10000.0 $ : 2 → gardés 574 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'DAI': 1.0, 'USDC': 1.0, 'WETH': 2418.692382, 'AERO': 0.800914, 'cbBTC': 82392.905144}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 147,924,690 | 2,427.070524 | 52800773 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 35,375,769 | 1.255833 | 52800773 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 500 | 18,336,003 | 0.029407 | 52800773 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 17,789,317 | 0.029377 | 52800773 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/VVV | 3000 | 17,411,835 | 100.389798 | 52800773 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,466,272 | 0.029365 | 52800773 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,834,850 | 0.000012 | 52800773 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 8,470,071 | 2,433.161178 | 52800773 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome_slipstream | USDC/cbBTC | 336 | 7,848,507 | 0.000012 | 52800773 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | USDC/cbBTC | 412 | 7,809,061 | 0.000012 | 52800773 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,243,604 | 0.001668 | 52800773 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | WETH/USDC | 698 | 7,042,409 | 2,433.920737 | 52800773 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome | WETH/USDC | 3000 | 5,493,789 | 2,428.026768 | 52800773 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,312,606 | 0.029417 | 52800773 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/superOETHb | 400 | 5,270,556 | 1.000854 | 52800773 | `0x6446021F4E396dA3df4235C62537431372195D38` |
| aerodrome | fBOMB/AERO | 10000 | 4,917,498 | 0.025833 | 52800773 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome_slipstream | WETH/USDT | 424 | 4,874,206 | 2,436.491373 | 52800773 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,851,406 | 0.802398 | 52800773 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,663,901 | 0.000273 | 52800773 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,455,078 | 2,433.876811 | 52800773 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,373,038 | 0.998772 | 52800773 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome_slipstream | USDC/AERO | 10000 | 4,316,316 | 1.255627 | 52800773 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome | WETH/KTA | 3000 | 4,106,916 | 33,125.068127 | 52800773 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/AERO | 10000 | 3,285,626 | 3,041.544479 | 52800773 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,924,858 | 1.141828 | 52800773 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,862,567 | 0.000012 | 52800773 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/VVV | 2778 | 2,651,281 | 100.409988 | 52800773 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,648,121 | 406.642418 | 52800773 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 2,526,037 | 0.000010 | 52800773 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | WETH/FAI | 10000 | 2,245,477 | 1,185,972.768868 | 52800773 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,065,866 | 1.233066 | 52800773 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,036,743 | 1.372638 | 52800773 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,995,329 | 0.000000 | 52800773 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome_slipstream | WETH/MORPHO | 2715 | 1,882,821 | 991.532204 | 52800773 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,802,524 | 15.890856 | 52800773 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,782,133 | 0.000012 | 52800773 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | weETH_04c0/WETH | 500 | 1,754,972 | 1.105523 | 52800773 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| uniswap_v3 | XDP/USDC | 100 | 1,753,167 | 0.018434 | 52800773 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome | fBOMB/USDC | 10000 | 1,730,295 | 0.020721 | 52800773 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| aerodrome | WETH/msETH (stable) | 500 | 1,686,495 | 2.309854 | 52800773 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,626,071 | 13,854.768107 | 52800773 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | WETH/AERO | 3000 | 1,620,280 | 3,049.722800 | 52800773 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | EURC/USDC | 73 | 1,478,348 | 1.122087 | 52800773 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,472,531 | 0.916352 | 52800773 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,454,738 | 0.827106 | 52800773 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | DRB/WETH | 10000 | 1,330,453 | 0.000000 | 52800773 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,321,125 | 0.436559 | 52800773 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,307,274 | 0.000272 | 52800773 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,290,778 | 0.004562 | 52800773 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,287,857 | 23.118211 | 52800773 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| aerodrome | WETH/cbBTC | 3000 | 1,279,248 | 0.029358 | 52800773 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| aerodrome | USDC/SEND | 3000 | 1,233,282 | 63.887836 | 52800773 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,213,278 | 2,433.158527 | 52800773 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | WETH/doginme | 10000 | 1,210,098 | 35,040,930.127724 | 52800773 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome_slipstream | msUSD/USDC | 500 | 1,205,021 | 0.886176 | 52800773 | `0x7501bc8Bb51616F79bfA524E464fb7B41f0B10fB` |
| aerodrome | WETH/WELL | 10000 | 1,168,019 | 1,170,699.598270 | 52800773 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,135,818 | 523,491.512620 | 52800773 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | USDC/NOCK | 3000 | 1,096,223 | 52.434683 | 52800773 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,087,720 | 15.133163 | 52800773 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome_slipstream | WETH/msETH | 500 | 1,082,286 | 1.132140 | 52800773 | `0x74F72788F4814D7fF3C49B44684aa98Eee140C0E` |

## Recherche d'opportunités
- Cycles : 14730 ; routes examinées : 310979760 ; candidats optimisés : 2104376 ; net attendu > 0 : 389 ; dernier cycle 636.5 ms
- Rejets (moteur) : {'spread_below_threshold': 306029105, 'liquidity_below_min': 2439588, 'negative_expected_net': 2103987, 'pool_quarantined': 264466, 'borrow_bound_too_small': 140603, 'cycle_budget_exhausted': 1590, 'unquotable': 32}
- Enregistrements de la session : 2104376 ; net attendu > 0 : 389 ; simulés (eth_call de la vraie tx) : 53 (ok 8, échec 45) ; étiquettes ghost N+1 : 1/32 positives
- Décisions : {'REJECTED': 2104376} ; motifs de rejet : {'below_safety_margin': 197, 'negative_expected_net': 2103987, 'p_lower_below_threshold': 314, 'price_impact': 83, 'reliability_not_demonstrated': 75, 'simulation_failed': 45, 'stale_data': 5}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52800309 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC | 32,186.130697 USDC | 28.530253 USDC | 0.000000 USDC | 0.012807 USDC | 28.517446 USDC (26.2361 €) | — | 8.86 | 0.000 (n=20) | REJECTED | reliability_not_demonstrated |
| 52800309 | WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 13.256963 WETH | 0.011750 WETH | 0.000000 WETH | 0.000005 WETH | 0.011745 WETH (26.2006 €) | — | 8.86 | 0.000 (n=20) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52800309 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 30,325.210226 USDC | 27.854142 USDC | 0.000000 USDC | 0.010597 USDC | 27.843545 USDC (25.6161 €) | — | 9.18 | 0.000 (n=34) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 52800309 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 12.491211 WETH | 0.011473 WETH | 0.000000 WETH | 0.000004 WETH | 0.011469 WETH (25.5838 €) | — | 9.18 | 0.000 (n=34) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 52800309 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDT→[uniswap_v3]→USDC | 18,548.378827 USDC | 20.664996 USDC | 0.000000 USDC | 0.010966 USDC | 20.654030 USDC (19.0017 €) | — | 11.14 | 0.000 (n=20) | REJECTED | reliability_not_demonstrated |
| 52800309 | WETH→[aerodrome_slipstream]→USDT→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 7.651474 WETH | 0.008519 WETH | 0.000000 WETH | 0.000005 WETH | 0.008514 WETH (18.9930 €) | — | 11.13 | 0.000 (n=20) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52800309 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 22,839.890718 USDC | 20.270906 USDC | 0.000000 USDC | 0.012439 USDC | 20.258467 USDC (18.6378 €) | — | 8.87 | 0.000 (n=20) | REJECTED | reliability_not_demonstrated |
| 52800309 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 9.418207 WETH | 0.008352 WETH | 0.000000 WETH | 0.000005 WETH | 0.008347 WETH (18.6210 €) | — | 8.86 | 0.000 (n=20) | REJECTED | reliability_not_demonstrated |
| 52800309 | cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.275525 cbBTC | 0.000245 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000245 cbBTC (18.6136 €) | — | 8.90 | 0.000 (n=20) | REJECTED | reliability_not_demonstrated |
| 52800309 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 20,002.037928 USDC | 17.286654 USDC | 0.000000 USDC | 0.009124 USDC | 17.277530 USDC (15.8953 €) | — | 8.64 | 0.000 (n=34) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 52800309 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 8.243328 WETH | 0.007124 WETH | 0.000000 WETH | 0.000004 WETH | 0.007120 WETH (15.8830 €) | — | 8.64 | 0.000 (n=34) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 52800309 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[uniswap_v3]→USDC | 17,130.945367 USDC | 14.530984 USDC | 0.000000 USDC | 0.011334 USDC | 14.519650 USDC (13.3581 €) | — | 8.48 | 0.000 (n=20) | REJECTED | reliability_not_demonstrated |
| 52800309 | WETH→[pancakeswap_v3]→cbBTC→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 7.023591 WETH | 0.005989 WETH | 0.000000 WETH | 0.000005 WETH | 0.005984 WETH (13.3496 €) | — | 8.52 | 0.000 (n=20) | REJECTED | reliability_not_demonstrated |
| 52800309 | cbBTC→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.205948 cbBTC | 0.000176 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000176 cbBTC (13.3472 €) | — | 8.53 | 0.000 (n=20) | REJECTED | reliability_not_demonstrated |
| 52800309 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 14,934.241604 USDC | 13.574881 USDC | 0.000000 USDC | 0.010598 USDC | 13.564283 USDC (12.4791 €) | — | 9.08 | 0.000 (n=20) | REJECTED | reliability_not_demonstrated |
| 52800309 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 6.146610 WETH | 0.005595 WETH | 0.000000 WETH | 0.000004 WETH | 0.005591 WETH (12.4724 €) | — | 9.10 | 0.000 (n=20) | REJECTED | reliability_not_demonstrated |
| 52800309 | cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.179538 cbBTC | 0.000164 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000164 cbBTC (12.4708 €) | — | 9.15 | 0.000 (n=20) | REJECTED | reliability_not_demonstrated |
| 52800309 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 11,888.935547 USDC | 13.139630 USDC | 0.000000 USDC | 0.010966 USDC | 13.128664 USDC (12.0784 €) | — | 11.04 | 0.006 (n=1) | REJECTED | reliability_not_demonstrated |
| 52800309 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 4.929789 WETH | 0.005417 WETH | 0.000000 WETH | 0.000005 WETH | 0.005412 WETH (12.0734 €) | — | 10.98 | 0.006 (n=1) | REJECTED | reliability_not_demonstrated |
| 52800309 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.143459 cbBTC | 0.000159 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000159 cbBTC (12.0722 €) | — | 11.08 | 0.006 (n=1) | REJECTED | reliability_not_demonstrated |
| 52800309 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 18,347.839249 USDC | 9.345229 USDC | 0.000000 USDC | 0.010230 USDC | 9.334999 USDC (8.5882 €) | — | 5.09 | 0.128 (n=106) | REJECTED | p_lower_below_threshold(0.13<0.75) |
| 52800309 | WETH→[uniswap_v3]→cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 7.534885 WETH | 0.003851 WETH | 0.000000 WETH | 0.000004 WETH | 0.003847 WETH (8.5821 €) | — | 5.11 | 0.128 (n=106) | REJECTED | p_lower_below_threshold(0.13<0.75) |
| 52800309 | cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→cbBTC | 0.218811 cbBTC | 0.000113 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000113 cbBTC (8.5767 €) | — | 5.16 | 0.128 (n=106) | REJECTED | p_lower_below_threshold(0.13<0.75) |
| 52800309 | WETH→[aerodrome_slipstream]→USDT→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 1.975250 WETH | 0.002891 WETH | 0.000000 WETH | 0.000004 WETH | 0.002887 WETH (6.4404 €) | — | 14.62 | 0.000 (n=20) | REJECTED | reliability_not_demonstrated |
| 52800309 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDT→[pancakeswap_v3]→USDC | 4,788.318146 USDC | 7.008432 USDC | 0.000000 USDC | 0.008758 USDC | 6.999674 USDC (6.4397 €) | — | 14.62 | 0.000 (n=20) | REJECTED | reliability_not_demonstrated |

## Fiabilité et décision
- Observations ghost : 1252 ; taux observé 0.103 ; borne inférieure crédible (0.9) 0.092 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 9.2% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
