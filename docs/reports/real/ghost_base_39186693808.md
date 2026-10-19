# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-19T06:48:45+00:00 ; durée 299.08 min ; blocs 52792613 → 52801578 (7989 vus)

## Connexion
- Requêtes RPC : 110511 ; erreurs : 333 ; latence p50/p95 : 246.9/1,663.5 ms
- Rafraîchissements d'état : 7989 ; âge des données au dernier bloc : 2.71 s ; changements de frais LP observés (pools à frais dynamiques) : 14754
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 142611 ; cycles déclenchés par événement : 8252 ; avance médiane sur le rafraîchissement multicall : 498 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,427.09 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 574 pools, 328 jetons, 21112 routes
- Par DEX : uniswap_v3 137, aerodrome 234, aerodrome_slipstream 156, pancakeswap_v3 30, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 207 (rejetés 2) → 612 jetons ; pools candidats 3877 (énumérés 392, par paires 0), mesurés 576, sous le plancher de 10000.0 $ : 2 → gardés 574 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'DAI': 1.0, 'USDC': 1.0, 'WETH': 2418.692382, 'AERO': 0.800914, 'cbBTC': 82392.905144}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 148,049,260 | 2,427.085294 | 52801579 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 35,472,393 | 1.249037 | 52801579 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 18,774,770 | 0.029377 | 52801579 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 500 | 18,341,877 | 0.029366 | 52801579 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 17,300,742 | 101.684441 | 52801579 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,471,809 | 0.029365 | 52801579 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,840,174 | 0.000012 | 52801579 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 8,470,065 | 2,428.703989 | 52801579 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome_slipstream | USDC/cbBTC | 436 | 8,446,927 | 0.000012 | 52801579 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome_slipstream | USDC/cbBTC | 336 | 7,846,143 | 0.000012 | 52801579 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 624 | 7,357,825 | 2,428.014986 | 52801579 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,254,510 | 0.001669 | 52801579 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | WETH/USDC | 3000 | 5,493,809 | 2,428.668661 | 52801579 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,314,499 | 0.029354 | 52801579 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/superOETHb | 400 | 5,270,588 | 1.000854 | 52801579 | `0x6446021F4E396dA3df4235C62537431372195D38` |
| aerodrome | fBOMB/AERO | 10000 | 4,930,901 | 0.025844 | 52801579 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,851,436 | 0.802398 | 52801579 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,663,929 | 0.000273 | 52801579 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | USDC/AERO | 10000 | 4,612,517 | 1.255627 | 52801579 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome_slipstream | WETH/USDT | 418 | 4,590,790 | 2,432.155429 | 52801579 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,454,903 | 2,427.934650 | 52801579 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,379,228 | 0.998772 | 52801579 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 4,106,941 | 33,125.068127 | 52801579 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/AERO | 10000 | 3,294,565 | 3,041.547314 | 52801579 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,924,877 | 1.141828 | 52801579 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,864,862 | 0.000012 | 52801579 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/VVV | 2829 | 2,636,446 | 101.662981 | 52801579 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,625,553 | 406.863868 | 52801579 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | AERO/cbBTC | 2700 | 2,554,857 | 0.000010 | 52801579 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/MORPHO | 2715 | 2,367,509 | 993.709396 | 52801579 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome | WETH/FAI | 10000 | 2,252,037 | 1,179,087.771936 | 52801579 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,065,866 | 1.233066 | 52801579 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,036,743 | 1.372638 | 52801579 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,995,341 | 0.000000 | 52801579 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,830,694 | 15.890856 | 52801579 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,783,778 | 0.000012 | 52801579 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,772,965 | 13,854.768107 | 52801579 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | weETH_04c0/WETH | 500 | 1,754,983 | 1.105523 | 52801579 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| uniswap_v3 | XDP/USDC | 100 | 1,749,492 | 0.018363 | 52801579 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome | fBOMB/USDC | 10000 | 1,730,347 | 0.020722 | 52801579 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| aerodrome | WETH/msETH (stable) | 500 | 1,686,505 | 2.309854 | 52801579 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | WETH/AERO | 3000 | 1,623,362 | 3,041.189393 | 52801579 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | EURC/USDC | 70 | 1,478,395 | 1.122133 | 52801579 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,472,540 | 0.916352 | 52801579 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,454,738 | 0.827106 | 52801579 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | DRB/WETH | 10000 | 1,328,545 | 0.000000 | 52801579 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,321,125 | 0.436559 | 52801579 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,307,283 | 0.000272 | 52801579 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,290,786 | 0.004562 | 52801579 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,287,872 | 23.118213 | 52801579 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| aerodrome | WETH/cbBTC | 3000 | 1,286,646 | 0.029358 | 52801579 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| aerodrome | USDC/SEND | 3000 | 1,233,126 | 63.904005 | 52801579 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,213,282 | 2,428.674027 | 52801579 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | WETH/doginme | 10000 | 1,210,106 | 35,040,930.127724 | 52801579 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome_slipstream | msUSD/USDC | 500 | 1,205,021 | 0.886176 | 52801579 | `0x7501bc8Bb51616F79bfA524E464fb7B41f0B10fB` |
| aerodrome | WETH/WELL | 10000 | 1,167,698 | 1,171,358.869963 | 52801579 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,138,748 | 519,758.450592 | 52801579 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | USDC/NOCK | 3000 | 1,096,700 | 52.389030 | 52801579 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,088,400 | 15.102910 | 52801579 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome_slipstream | WETH/msETH | 500 | 1,082,293 | 1.132140 | 52801579 | `0x74F72788F4814D7fF3C49B44684aa98Eee140C0E` |

## Recherche d'opportunités
- Cycles : 16240 ; routes examinées : 342858880 ; candidats optimisés : 2222594 ; net attendu > 0 : 392 ; dernier cycle 179.2 ms
- Rejets (moteur) : {'spread_below_threshold': 337549200, 'liquidity_below_min': 2671121, 'negative_expected_net': 2222202, 'pool_quarantined': 264466, 'borrow_bound_too_small': 149662, 'cycle_budget_exhausted': 1805, 'unquotable': 32}
- Enregistrements de la session : 2222594 ; net attendu > 0 : 392 ; simulés (eth_call de la vraie tx) : 54 (ok 8, échec 46) ; étiquettes ghost N+1 : 1/33 positives
- Décisions : {'REJECTED': 2222594} ; motifs de rejet : {'below_safety_margin': 199, 'negative_expected_net': 2222202, 'p_lower_below_threshold': 316, 'price_impact': 83, 'reliability_not_demonstrated': 76, 'simulation_failed': 46, 'stale_data': 7}

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
- Observations ghost : 1253 ; taux observé 0.103 ; borne inférieure crédible (0.9) 0.092 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 9.2% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
