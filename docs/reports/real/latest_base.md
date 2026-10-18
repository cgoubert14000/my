# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-18T22:00:16+00:00 ; durée 108.45 min ; blocs 52782478 → 52785730 (3205 vus)

## Connexion
- Requêtes RPC : 44276 ; erreurs : 0 ; latence p50/p95 : 316.3/1,266.0 ms
- Rafraîchissements d'état : 3205 ; âge des données au dernier bloc : 4.56 s ; changements de frais LP observés (pools à frais dynamiques) : 7820
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 70127 ; cycles déclenchés par événement : 4362 ; avance médiane sur le rafraîchissement multicall : 1,557 ms
- Gaz : base fee 0.005021 gwei ; prix ETH (pool le plus profond) : 2,363.41 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 569 pools, 326 jetons, 20804 routes
- Par DEX : uniswap_v3 135, aerodrome 232, aerodrome_slipstream 153, pancakeswap_v3 31, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 205 (rejetés 2) → 610 jetons ; pools candidats 3913 (énumérés 387, par paires 0), mesurés 571, sous le plancher de 10000.0 $ : 2 → gardés 569 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'DAI': 1.0, 'USDC': 1.0, 'WETH': 2337.16445, 'AERO': 0.771529, 'cbBTC': 80785.7814}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 145,331,330 | 2,363.405812 | 52785729 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 34,910,630 | 1.297650 | 52785729 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 500 | 17,875,974 | 0.029185 | 52785730 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 16,257,200 | 109.174972 | 52785729 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| aerodrome_slipstream | WETH/cbBTC | 2525 | 10,797,945 | 0.029126 | 52785730 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,214,767 | 0.029111 | 52785729 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,745,360 | 0.000012 | 52785729 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 8,280,330 | 2,369.036794 | 52785729 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome_slipstream | USDC/cbBTC | 472 | 8,061,449 | 0.000012 | 52785729 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome_slipstream | USDC/cbBTC | 342 | 7,841,911 | 0.000012 | 52785729 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,049,099 | 0.001641 | 52785729 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | WETH/USDC | 713 | 6,871,602 | 2,368.959752 | 52785730 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome | WETH/USDC | 3000 | 5,421,439 | 2,362.847343 | 52785729 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | USDC/AERO | 10000 | 5,416,758 | 1.295932 | 52785729 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,180,760 | 0.029196 | 52785730 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/superOETHb | 400 | 5,132,303 | 1.000854 | 52785729 | `0x6446021F4E396dA3df4235C62537431372195D38` |
| aerodrome | fBOMB/AERO | 10000 | 4,827,689 | 0.026198 | 52785729 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,724,147 | 0.802398 | 52785729 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,510,250 | 0.000269 | 52785729 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,383,913 | 2,369.201543 | 52785730 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,311,659 | 0.998062 | 52785729 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,991,556 | 33,251.859408 | 52785729 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDT | 445 | 3,559,344 | 2,373.358371 | 52785729 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome | WETH/AERO | 10000 | 3,189,606 | 3,053.372023 | 52785729 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,848,165 | 1.141832 | 52785729 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,825,779 | 0.000012 | 52785729 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,607,366 | 414.410310 | 52785729 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | WETH/VVV | 2802 | 2,467,833 | 109.188441 | 52785729 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 2,247,373 | 0.000010 | 52785729 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 2,221,515 | 1,029.589651 | 52785729 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome | WETH/FAI | 10000 | 2,168,053 | 1,206,323.744350 | 52785729 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,065,829 | 1.233121 | 52785729 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,036,703 | 1.372655 | 52785729 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,960,593 | 0.000000 | 52785729 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,885,390 | 15.991826 | 52785729 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | fBOMB/USDC | 10000 | 1,772,701 | 0.020634 | 52785729 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,762,262 | 0.000012 | 52785729 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | XDP/USDC | 100 | 1,757,148 | 0.018445 | 52785729 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome | weETH_04c0/WETH | 500 | 1,708,999 | 1.105523 | 52785729 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,681,375 | 14,220.729216 | 52785729 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/msETH (stable) | 500 | 1,645,270 | 2.303038 | 52785729 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | WETH/AERO | 3000 | 1,573,997 | 3,073.128265 | 52785729 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | EURC/USDC | 91 | 1,478,506 | 1.120226 | 52785729 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,455,297 | 0.827470 | 52785729 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,433,904 | 0.916353 | 52785729 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,317,142 | 0.434918 | 52785729 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,305,365 | 0.000000 | 52785729 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,264,199 | 0.000269 | 52785729 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | WETH/cbBTC | 3000 | 1,250,425 | 0.029109 | 52785729 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,242,320 | 0.004503 | 52785729 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome | USDC/SEND | 3000 | 1,233,273 | 63.888794 | 52785729 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,220,442 | 23.291377 | 52785729 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| aerodrome_slipstream | WETH/msETH | 500 | 1,210,124 | 1.130862 | 52785729 | `0x74F72788F4814D7fF3C49B44684aa98Eee140C0E` |
| uniswap_v3 | WETH/doginme | 10000 | 1,192,719 | 33,855,318.554278 | 52785729 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,173,796 | 2,369.334327 | 52785729 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | WETH/WELL | 10000 | 1,135,137 | 1,175,319.393100 | 52785729 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,105,722 | 534,059.559101 | 52785729 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | USDC/NOCK | 3000 | 1,087,567 | 53.272600 | 52785729 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,082,799 | 15.314181 | 52785729 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,037,359 | 1.105812 | 52785729 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |

## Recherche d'opportunités
- Cycles : 7566 ; routes examinées : 157403064 ; candidats optimisés : 956245 ; net attendu > 0 : 686 ; dernier cycle 506.8 ms
- Rejets (moteur) : {'spread_below_threshold': 154258030, 'liquidity_below_min': 1434736, 'negative_expected_net': 955559, 'pool_quarantined': 741734, 'borrow_bound_too_small': 7561, 'cycle_budget_exhausted': 2671, 'unquotable': 2087}
- Enregistrements de la session : 956245 ; net attendu > 0 : 686 ; simulés (eth_call de la vraie tx) : 90 (ok 3, échec 87) ; étiquettes ghost N+1 : 0/68 positives
- Décisions : {'REJECTED': 956245} ; motifs de rejet : {'below_safety_margin': 375, 'negative_expected_net': 955559, 'p_lower_below_threshold': 475, 'price_impact': 52, 'reliability_not_demonstrated': 211, 'simulation_failed': 87}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52784851 | WETH→[aerodrome]→MEY→[uniswap_v3]→WETH | 0.120024 WETH | 0.007760 WETH | 0.000000 WETH | 0.000002 WETH | 0.007758 WETH (16.7917 €) | — | 646.36 | 0.003 (n=2) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52785724 | USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 4,552.177263 USDC | 1.124744 USDC | 0.000000 USDC | 0.008535 USDC | 1.116209 USDC (1.0269 €) | — | 2.45 | 0.116 (n=124) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52785724 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→cbBTC | 0.055050 cbBTC | 0.000014 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000014 cbBTC (1.0242 €) | — | 2.50 | 0.116 (n=124) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52785724 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 1.900097 WETH | 0.000475 WETH | 0.000000 WETH | 0.000004 WETH | 0.000471 WETH (1.0238 €) | — | 2.48 | 0.116 (n=124) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.12<0.75) |
| 52785724 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 3,172.069766 USDC | 1.012969 USDC | 0.000000 USDC | 0.008535 USDC | 1.004434 USDC (0.9241 €) | — | 3.17 | 0.003 (n=2) | REJECTED | reliability_not_demonstrated |
| 52785724 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.038827 cbBTC | 0.000012 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000012 cbBTC (0.9215 €) | — | 3.19 | 0.003 (n=2) | REJECTED | reliability_not_demonstrated |
| 52785724 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 1.350669 WETH | 0.000427 WETH | 0.000000 WETH | 0.000004 WETH | 0.000424 WETH (0.9211 €) | — | 3.14 | 0.003 (n=2) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52785724 | USDC→[uniswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 3,844.265288 USDC | 0.985803 USDC | 0.000000 USDC | 0.008894 USDC | 0.976909 USDC (0.8988 €) | — | 2.54 | 0.116 (n=124) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52785724 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→cbBTC | 0.047602 cbBTC | 0.000012 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000012 cbBTC (0.8969 €) | — | 2.53 | 0.116 (n=124) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52785724 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 1.622718 WETH | 0.000416 WETH | 0.000000 WETH | 0.000004 WETH | 0.000412 WETH (0.8962 €) | — | 2.54 | 0.116 (n=124) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.12<0.75) |
| 52785724 | USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 3,375.880815 USDC | 0.846803 USDC | 0.000000 USDC | 0.008176 USDC | 0.838627 USDC (0.7715 €) | — | 2.48 | 0.116 (n=124) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52785724 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→cbBTC | 0.041160 cbBTC | 0.000010 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000010 cbBTC (0.7695 €) | — | 2.51 | 0.116 (n=124) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52785724 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 1.394504 WETH | 0.000357 WETH | 0.000000 WETH | 0.000003 WETH | 0.000354 WETH (0.7686 €) | — | 2.54 | 0.116 (n=124) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52785724 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 2,807.245085 USDC | 0.664177 USDC | 0.000000 USDC | 0.008176 USDC | 0.656001 USDC (0.6035 €) | — | 2.34 | 0.116 (n=124) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52785724 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→WETH | 1.194276 WETH | 0.000280 WETH | 0.000000 WETH | 0.000003 WETH | 0.000277 WETH (0.6017 €) | — | 2.32 | 0.116 (n=124) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52785724 | cbBTC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.033571 cbBTC | 0.000008 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000008 cbBTC (0.6011 €) | — | 2.40 | 0.116 (n=124) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52785724 | USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 2,752.358918 USDC | 0.620058 USDC | 0.000000 USDC | 0.008176 USDC | 0.611882 USDC (0.5629 €) | — | 2.22 | 0.116 (n=124) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52785724 | cbBTC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.034174 cbBTC | 0.000008 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000008 cbBTC (0.5617 €) | — | 2.21 | 0.116 (n=124) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52785724 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH | 1.157750 WETH | 0.000262 WETH | 0.000000 WETH | 0.000003 WETH | 0.000258 WETH (0.5612 €) | — | 2.23 | 0.116 (n=124) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52785724 | USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 2,603.539838 USDC | 0.582341 USDC | 0.000000 USDC | 0.008176 USDC | 0.574165 USDC (0.5282 €) | — | 2.21 | 0.116 (n=124) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52785724 | cbBTC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.031566 cbBTC | 0.000007 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000007 cbBTC (0.5266 €) | — | 2.24 | 0.116 (n=124) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52785724 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH | 1.083340 WETH | 0.000246 WETH | 0.000000 WETH | 0.000003 WETH | 0.000242 WETH (0.5264 €) | — | 2.24 | 0.116 (n=124) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52785724 | USDC→[uniswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 2,237.617832 USDC | 0.533092 USDC | 0.000000 USDC | 0.007818 USDC | 0.525274 USDC (0.4833 €) | — | 2.35 | 0.116 (n=124) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52785724 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→cbBTC | 0.026745 cbBTC | 0.000007 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000006 cbBTC (0.4820 €) | — | 2.42 | 0.116 (n=124) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52785724 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.931020 WETH | 0.000225 WETH | 0.000000 WETH | 0.000003 WETH | 0.000222 WETH (0.4818 €) | — | 2.38 | 0.116 (n=124) | REJECTED | p_lower_below_threshold(0.12<0.75) |

## Fiabilité et décision
- Observations ghost : 1141 ; taux observé 0.106 ; borne inférieure crédible (0.9) 0.095 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 9.5% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
