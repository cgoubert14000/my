# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-14T10:02:59+00:00 ; durée 36.68 min ; blocs 52590312 → 52591414 (1101 vus)

## Connexion
- Requêtes RPC : 14683 ; erreurs : 0 ; latence p50/p95 : 275.9/739.5 ms
- Rafraîchissements d'état : 1101 ; âge des données au dernier bloc : 2.71 s ; changements de frais LP observés (pools à frais dynamiques) : 1936
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 66333 ; cycles déclenchés par événement : 1353 ; avance médiane sur le rafraîchissement multicall : 873 ms
- Gaz : base fee 0.005510 gwei ; prix ETH (pool le plus profond) : 2,499.77 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 584 pools, 329 jetons, 21950 routes
- Par DEX : uniswap_v3 142, aerodrome 236, aerodrome_slipstream 157, pancakeswap_v3 32, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 208 (rejetés 2) → 613 jetons ; pools candidats 3924 (énumérés 395, par paires 0), mesurés 586, sous le plancher de 10000.0 $ : 2 → gardés 584 (max 1500) ; prix des hubs : {'USDC': 1.0, 'DAI': 1.0, 'USDbC': 1.0, 'WETH': 2506.12853, 'AERO': 0.905993, 'cbBTC': 83225.723803}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 149,735,108 | 2,499.769636 | 52591415 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 41,893,100 | 1.106933 | 52591415 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 500 | 18,294,399 | 0.029995 | 52591415 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 16,169,284 | 109.761000 | 52591415 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 12,959,090 | 0.030049 | 52591415 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,709,669 | 0.030064 | 52591415 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 9,393,560 | 2,493.503729 | 52591415 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,305,144 | 0.000012 | 52591415 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome | WETH/USDC | 3000 | 9,107,847 | 2,499.673026 | 52591415 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | USDC/cbBTC | 336 | 8,133,203 | 0.000012 | 52591415 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 698 | 7,478,926 | 2,493.047475 | 52591415 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,321,336 | 0.001670 | 52591415 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 448 | 7,003,120 | 0.000012 | 52591415 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome_slipstream | USDC/AERO | 10000 | 6,301,366 | 1.101762 | 52591415 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,559,913 | 0.029983 | 52591415 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/superOETHb | 400 | 5,521,192 | 1.000859 | 52591415 | `0x6446021F4E396dA3df4235C62537431372195D38` |
| aerodrome | fBOMB/AERO | 10000 | 5,449,471 | 0.026711 | 52591415 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,764,683 | 0.000280 | 52591415 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,714,435 | 0.802390 | 52591415 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,508,378 | 2,492.877272 | 52591415 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,421,879 | 0.999018 | 52591415 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 4,102,099 | 35,221.348433 | 52591415 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/AERO | 10000 | 3,718,032 | 2,773.424019 | 52591415 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | cbETH/WETH | 60 | 3,024,459 | 1.141622 | 52591415 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,865,565 | 0.000012 | 52591415 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | AERO/cbBTC | 2700 | 2,662,075 | 0.000011 | 52591415 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/VVV | 2721 | 2,604,812 | 109.730558 | 52591415 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | WETH/FAI | 10000 | 2,447,354 | 1,059,089.868450 | 52591415 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,395,921 | 404.683181 | 52591415 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | WETH/USDT | 427 | 2,282,519 | 2,497.168777 | 52591415 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,116,960 | 1.189905 | 52591415 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | BNKR/WETH | 10000 | 2,104,534 | 0.000000 | 52591415 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome | fBOMB/USDbC | 10000 | 2,040,275 | 0.024089 | 52591415 | `0xC395664B295ed5bf1D249Ae8be9740655AA174ef` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,958,180 | 0.916707 | 52591415 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| aerodrome | USDC/alUSDb (stable) | 500 | 1,859,884 | 1.371858 | 52591415 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| uniswap_v3 | XDP/USDC | 100 | 1,817,157 | 0.019195 | 52591415 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,800,414 | 15.664258 | 52591415 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,706,355 | 0.000012 | 52591415 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | WETH/msETH (stable) | 500 | 1,675,938 | 2.306168 | 52591415 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 1,674,583 | 1,072.311493 | 52591415 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,634,145 | 13,484.456970 | 52591415 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | WETH/AERO | 3000 | 1,566,739 | 2,762.361577 | 52591415 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | weETH_04c0/WETH | 500 | 1,545,532 | 1.105776 | 52591415 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,461,149 | 0.832565 | 52591415 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | DRB/WETH | 10000 | 1,454,684 | 0.000000 | 52591415 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,399,476 | 0.000278 | 52591415 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome_slipstream | WETH/AERO | 3024 | 1,391,589 | 2,762.619542 | 52591415 | `0x82321f3BEB69f503380D6B233857d5C43562e2D0` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,390,924 | 0.004853 | 52591415 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | WETH/msETH | 500 | 1,377,875 | 1.131360 | 52591415 | `0x74F72788F4814D7fF3C49B44684aa98Eee140C0E` |
| aerodrome_slipstream | EURC/USDC | 70 | 1,357,673 | 1.119257 | 52591415 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,300,289 | 23.443910 | 52591415 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,271,941 | 2,493.710951 | 52591415 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | WETH/doginme | 10000 | 1,262,213 | 33,837,848.715991 | 52591415 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | USDC/SEND | 3000 | 1,247,670 | 62.422840 | 52591415 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,238,308 | 1.105594 | 52591415 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |
| aerodrome_slipstream | msUSD/USDC | 500 | 1,222,978 | 0.886137 | 52591415 | `0x7501bc8Bb51616F79bfA524E464fb7B41f0B10fB` |
| aerodrome | WETH/EDEL | 7000 | 1,215,681 | 72,821.982595 | 52591415 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,204,645 | 483,539.485072 | 52591415 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | WETH/WELL | 10000 | 1,191,303 | 1,193,971.144143 | 52591415 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,167,296 | 0.436583 | 52591415 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |

## Recherche d'opportunités
- Cycles : 2453 ; routes examinées : 53843350 ; candidats optimisés : 330155 ; net attendu > 0 : 54 ; dernier cycle 312.1 ms
- Rejets (moteur) : {'spread_below_threshold': 52847134, 'liquidity_below_min': 552434, 'negative_expected_net': 330101, 'borrow_bound_too_small': 61325, 'cycle_budget_exhausted': 47396, 'unquotable': 4906}
- Enregistrements de la session : 330155 ; net attendu > 0 : 54 ; simulés (eth_call de la vraie tx) : 4 (ok 1, échec 3) ; étiquettes ghost N+1 : 0/3 positives
- Décisions : {'REJECTED': 330155} ; motifs de rejet : {'below_safety_margin': 50, 'negative_expected_net': 330101, 'reliability_not_demonstrated': 54, 'simulation_failed': 3}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52591127 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 60.367657 USDC | 0.074584 USDC | 0.000000 USDC | 0.005622 USDC | 0.068962 USDC (0.0634 €) | — | 11.42 | — (n=0) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52591127 | USDC→[aerodrome]→PLAY→[pancakeswap_v3]→USDC | 12.367185 USDC | 0.013784 USDC | 0.000000 USDC | 0.005277 USDC | 0.008507 USDC (0.0078 €) | — | 6.88 | 0.006 (n=1) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52591363 | WETH→[aerodrome]→DRV→[uniswap_v3]→WETH | 0.020813 WETH | 0.000005 WETH | 0.000000 WETH | 0.000002 WETH | 0.000002 WETH (0.0056 €) | — | 1.17 | — (n=0) | REJECTED | below_safety_margin(2445515132706<4162648015695), reliability_not_demonstrated |
| 52591363 | WETH→[aerodrome]→DRV→[uniswap_v3]→WETH | 0.020813 WETH | 0.000005 WETH | 0.000000 WETH | 0.000002 WETH | 0.000002 WETH (0.0056 €) | — | 1.17 | — (n=0) | REJECTED | below_safety_margin(2438166218705<4162648015695), reliability_not_demonstrated |
| 52590981 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.016499 WETH | 0.000004 WETH | 0.000000 WETH | 0.000002 WETH | 0.000002 WETH (0.0044 €) | — | 1.15 | — (n=0) | REJECTED | below_safety_margin(1893556083282<3299730892581), reliability_not_demonstrated |
| 52590981 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.016499 WETH | 0.000004 WETH | 0.000000 WETH | 0.000002 WETH | 0.000002 WETH (0.0044 €) | — | 1.15 | — (n=0) | REJECTED | below_safety_margin(1893556083282<3299730892581), reliability_not_demonstrated |
| 52590982 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.016499 WETH | 0.000004 WETH | 0.000000 WETH | 0.000002 WETH | 0.000002 WETH (0.0044 €) | — | 1.15 | — (n=0) | REJECTED | below_safety_margin(1893556083282<3299730892581), reliability_not_demonstrated |
| 52590981 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 41.524802 USDC | 0.010337 USDC | 0.000000 USDC | 0.005630 USDC | 0.004707 USDC (0.0043 €) | — | 1.13 | — (n=0) | REJECTED | below_safety_margin(4707<8304), reliability_not_demonstrated |
| 52590981 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 41.524802 USDC | 0.010337 USDC | 0.000000 USDC | 0.005630 USDC | 0.004707 USDC (0.0043 €) | — | 1.13 | — (n=0) | REJECTED | below_safety_margin(4707<8304), reliability_not_demonstrated |
| 52590982 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 41.524802 USDC | 0.010337 USDC | 0.000000 USDC | 0.005630 USDC | 0.004707 USDC (0.0043 €) | — | 1.13 | — (n=0) | REJECTED | below_safety_margin(4707<8304), reliability_not_demonstrated |
| 52591365 | cbBTC→[aerodrome]→USDC→[pancakeswap_v3]→cbBTC | 0.000228 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0038 €) | 0.000000 cbBTC | 2.19 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52591365 | cbBTC→[aerodrome]→USDC→[pancakeswap_v3]→cbBTC | 0.000228 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0038 €) | — | 2.19 | — (n=0) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52591365 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome]→USDC | 18.417909 USDC | 0.009112 USDC | 0.000000 USDC | 0.005499 USDC | 0.003613 USDC (0.0033 €) | — | 1.96 | — (n=0) | REJECTED | below_safety_margin(3613<3683), reliability_not_demonstrated |
| 52591365 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome]→USDC | 18.417909 USDC | 0.009112 USDC | 0.000000 USDC | 0.005499 USDC | 0.003613 USDC (0.0033 €) | — | 1.96 | — (n=0) | REJECTED | below_safety_margin(3613<3683), reliability_not_demonstrated |
| 52591365 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 30.097411 USDC | 0.009226 USDC | 0.000000 USDC | 0.005859 USDC | 0.003367 USDC (0.0031 €) | — | 1.12 | — (n=0) | REJECTED | below_safety_margin(3367<6019), reliability_not_demonstrated |
| 52591365 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 30.097411 USDC | 0.009226 USDC | 0.000000 USDC | 0.005859 USDC | 0.003367 USDC (0.0031 €) | — | 1.12 | — (n=0) | REJECTED | below_safety_margin(3367<6019), reliability_not_demonstrated |
| 52591365 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.000374 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0031 €) | — | 1.07 | — (n=0) | REJECTED | below_safety_margin(4<7), reliability_not_demonstrated |
| 52591365 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.000374 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0031 €) | — | 1.07 | — (n=0) | REJECTED | below_safety_margin(4<7), reliability_not_demonstrated |
| 52591365 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 26.133585 USDC | 0.008545 USDC | 0.000000 USDC | 0.005859 USDC | 0.002686 USDC (0.0025 €) | — | 1.03 | 0.003 (n=2) | REJECTED | below_safety_margin(2686<5226), reliability_not_demonstrated |
| 52591365 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 26.133585 USDC | 0.008545 USDC | 0.000000 USDC | 0.005859 USDC | 0.002686 USDC (0.0025 €) | — | 1.03 | 0.003 (n=2) | REJECTED | below_safety_margin(2686<5226), reliability_not_demonstrated |
| 52591365 | cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.000229 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0023 €) | — | 1.31 | 0.003 (n=2) | REJECTED | below_safety_margin(3<4), reliability_not_demonstrated |
| 52591365 | cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.000229 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0023 €) | — | 1.31 | 0.003 (n=2) | REJECTED | below_safety_margin(3<4), reliability_not_demonstrated |
| 52591365 | USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→USDC | 26.133585 USDC | 0.008350 USDC | 0.000000 USDC | 0.005859 USDC | 0.002491 USDC (0.0023 €) | — | 0.95 | 0.003 (n=2) | REJECTED | below_safety_margin(2491<5226), reliability_not_demonstrated |
| 52591365 | USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→USDC | 26.133585 USDC | 0.008350 USDC | 0.000000 USDC | 0.005859 USDC | 0.002491 USDC (0.0023 €) | — | 0.95 | 0.003 (n=2) | REJECTED | below_safety_margin(2491<5226), reliability_not_demonstrated |
| 52591365 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 23.401857 USDC | 0.007745 USDC | 0.000000 USDC | 0.005859 USDC | 0.001886 USDC (0.0017 €) | — | 0.81 | 0.003 (n=2) | REJECTED | below_safety_margin(1886<4680), reliability_not_demonstrated |

## Fiabilité et décision
- Observations ghost : 24 ; taux observé 0.125 ; borne inférieure crédible (0.9) 0.060 ; seuil 0.75 → **FIABILITÉ NON DÉMONTRÉE — DONNÉES INSUFFISANTES**
- Statut de maturité : **APPRENTISSAGE** — FIABILITÉ NON DÉMONTRÉE — DONNÉES INSUFFISANTES
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ❌ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
