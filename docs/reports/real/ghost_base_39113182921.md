# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-18T09:13:29+00:00 ; durée 15.26 min ; blocs 52762270 → 52762730 (458 vus)

## Connexion
- Requêtes RPC : 6374 ; erreurs : 0 ; latence p50/p95 : 232.8/685.3 ms
- Rafraîchissements d'état : 458 ; âge des données au dernier bloc : 3.64 s ; changements de frais LP observés (pools à frais dynamiques) : 1216
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 9160 ; cycles déclenchés par événement : 651 ; avance médiane sur le rafraîchissement multicall : 371 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,415.06 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 578 pools, 328 jetons, 21580 routes
- Par DEX : uniswap_v3 136, aerodrome 235, aerodrome_slipstream 157, pancakeswap_v3 32, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 207 (rejetés 2) → 612 jetons ; pools candidats 3915 (énumérés 394, par paires 0), mesurés 580, sous le plancher de 10000.0 $ : 2 → gardés 578 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'DAI': 1.0, 'USDC': 1.0, 'WETH': 2410.986474, 'AERO': 0.834015, 'cbBTC': 81629.281689}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 146,166,545 | 2,415.058847 | 52762730 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 42,015,752 | 1.194919 | 52762730 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 500 | 18,228,477 | 0.029534 | 52762730 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 18,123,744 | 0.029544 | 52762730 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/VVV | 3000 | 16,746,929 | 108.527974 | 52762730 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,413,059 | 0.029525 | 52762730 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| aerodrome_slipstream | USDC/cbBTC | 460 | 9,949,140 | 0.000012 | 52762730 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,762,875 | 0.000012 | 52762730 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 9,067,473 | 2,417.325497 | 52762730 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome_slipstream | USDC/cbBTC | 336 | 7,857,952 | 0.000012 | 52762730 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,144,726 | 0.001653 | 52762730 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | WETH/USDC | 564 | 6,924,959 | 2,418.310863 | 52762730 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome | WETH/USDC | 3000 | 5,492,122 | 2,415.239068 | 52762730 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,334,120 | 0.029532 | 52762730 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/superOETHb | 400 | 5,244,471 | 1.000855 | 52762730 | `0x6446021F4E396dA3df4235C62537431372195D38` |
| aerodrome | fBOMB/AERO | 10000 | 5,139,753 | 0.025622 | 52762730 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome_slipstream | WETH/USDT | 406 | 5,065,576 | 2,420.937810 | 52762730 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,827,392 | 0.802398 | 52762730 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,630,087 | 0.000271 | 52762730 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,440,285 | 0.998809 | 52762730 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,437,889 | 2,418.468730 | 52762730 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | WETH/KTA | 3000 | 4,081,967 | 33,200.148390 | 52762730 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | USDC/AERO | 10000 | 4,037,490 | 1.190507 | 52762730 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome | WETH/AERO | 10000 | 3,345,865 | 2,866.465549 | 52762730 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,917,059 | 1.141818 | 52762730 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,841,921 | 0.000012 | 52762730 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | AERO/cbBTC | 2700 | 2,554,549 | 0.000010 | 52762730 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/VVV | 2718 | 2,546,045 | 108.491779 | 52762730 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,287,051 | 409.249355 | 52762730 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | WETH/FAI | 10000 | 2,238,197 | 1,181,913.960766 | 52762730 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,105,878 | 1.199991 | 52762730 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,035,374 | 1.374087 | 52762730 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| aerodrome_slipstream | EURC/USDC | 70 | 1,959,725 | 1.123485 | 52762730 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,947,653 | 15.851079 | 52762730 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,867,161 | 0.000000 | 52762730 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome | fBOMB/USDC | 10000 | 1,809,838 | 0.021550 | 52762730 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,779,433 | 0.000012 | 52762730 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,768,139 | 13,858.506639 | 52762730 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | XDP/USDC | 100 | 1,766,449 | 0.018612 | 52762730 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome | WETH/msETH (stable) | 500 | 1,672,998 | 2.306444 | 52762730 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome | weETH_04c0/WETH | 500 | 1,520,932 | 1.105495 | 52762730 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| uniswap_v3 | WETH/AERO | 3000 | 1,516,378 | 2,886.814836 | 52762730 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,467,888 | 0.916373 | 52762730 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,456,384 | 0.826249 | 52762730 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | WETH/AERO | 3000 | 1,456,351 | 2,886.606572 | 52762730 | `0x82321f3BEB69f503380D6B233857d5C43562e2D0` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 1,452,310 | 1,008.715818 | 52762730 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| uniswap_v3 | DRB/WETH | 10000 | 1,329,221 | 0.000000 | 52762730 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,318,580 | 0.435936 | 52762730 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,297,681 | 0.000270 | 52762730 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,297,665 | 0.004649 | 52762730 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome | WETH/cbBTC | 3000 | 1,257,390 | 0.029519 | 52762730 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| aerodrome | USDC/SEND | 3000 | 1,248,124 | 62.377421 | 52762730 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,241,437 | 23.372954 | 52762730 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,207,274 | 2,417.321795 | 52762730 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | WETH/doginme | 10000 | 1,193,524 | 35,920,805.594525 | 52762730 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome_slipstream | msUSD/USDC | 500 | 1,167,671 | 0.885726 | 52762730 | `0x7501bc8Bb51616F79bfA524E464fb7B41f0B10fB` |
| aerodrome | WETH/WELL | 10000 | 1,164,311 | 1,166,766.396236 | 52762730 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,162,937 | 1.105821 | 52762730 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,159,855 | 516,942.421892 | 52762730 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome_slipstream | WETH/msETH | 500 | 1,151,672 | 1.131541 | 52762730 | `0x74F72788F4814D7fF3C49B44684aa98Eee140C0E` |

## Recherche d'opportunités
- Cycles : 1108 ; routes examinées : 23910640 ; candidats optimisés : 109259 ; net attendu > 0 : 65 ; dernier cycle 92.5 ms
- Rejets (moteur) : {'spread_below_threshold': 23611426, 'liquidity_below_min': 188847, 'negative_expected_net': 109194, 'borrow_bound_too_small': 1108}
- Enregistrements de la session : 109259 ; net attendu > 0 : 65 ; simulés (eth_call de la vraie tx) : 5 (ok 0, échec 5) ; étiquettes ghost N+1 : 0/4 positives
- Décisions : {'REJECTED': 109259} ; motifs de rejet : {'below_safety_margin': 60, 'negative_expected_net': 109194, 'p_lower_below_threshold': 46, 'reliability_not_demonstrated': 19, 'simulation_failed': 5}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52762636 | WETH→[aerodrome_slipstream]→KTA→[aerodrome]→WETH | 0.107115 WETH | 0.000278 WETH | 0.000000 WETH | 0.000002 WETH | 0.000276 WETH (0.6125 €) | — | 25.74 | 0.002 (n=4) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52762566 | USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 1,272.855682 USDC | 0.121496 USDC | 0.000000 USDC | 0.007249 USDC | 0.114247 USDC (0.1051 €) | — | 0.90 | 0.137 (n=99) | REJECTED | below_safety_margin(114247<254571), p_lower_below_threshold(0.14<0.75) |
| 52762566 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH | 0.527897 WETH | 0.000050 WETH | 0.000000 WETH | 0.000003 WETH | 0.000047 WETH (0.1048 €) | — | 0.89 | 0.137 (n=99) | REJECTED | below_safety_margin(47204935156916<105579478800958), p_lower_below_threshold(0.14<0.75) |
| 52762566 | USDC→[pancakeswap_v3]→USDT→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 850.849852 USDC | 0.076440 USDC | 0.000000 USDC | 0.007249 USDC | 0.069191 USDC (0.0637 €) | — | 0.81 | 0.137 (n=99) | REJECTED | below_safety_margin(69191<170169), p_lower_below_threshold(0.14<0.75) |
| 52762566 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→USDT→[aerodrome_slipstream]→WETH | 0.352508 WETH | 0.000032 WETH | 0.000000 WETH | 0.000003 WETH | 0.000029 WETH (0.0634 €) | — | 0.81 | 0.137 (n=99) | REJECTED | below_safety_margin(28583796801784<70501568003788), p_lower_below_threshold(0.14<0.75) |
| 52762498 | WETH→[uniswap_v3]→TEVA→[aerodrome]→WETH | 0.011973 WETH | 0.000029 WETH | 0.000000 WETH | 0.000002 WETH | 0.000026 WETH (0.0586 €) | — | 22.08 | 0.002 (n=3) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52762566 | USDC→[uniswap_v3]→USDT→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 739.179848 USDC | 0.043147 USDC | 0.000000 USDC | 0.007249 USDC | 0.035898 USDC (0.0330 €) | — | 0.49 | 0.137 (n=99) | REJECTED | below_safety_margin(35898<147835), p_lower_below_threshold(0.14<0.75) |
| 52762566 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→USDT→[aerodrome_slipstream]→WETH | 0.305056 WETH | 0.000018 WETH | 0.000000 WETH | 0.000003 WETH | 0.000015 WETH (0.0329 €) | — | 0.49 | 0.137 (n=99) | REJECTED | below_safety_margin(14825048275491<61011218065792), p_lower_below_threshold(0.14<0.75) |
| 52762566 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 541.459271 USDC | 0.035309 USDC | 0.000000 USDC | 0.005417 USDC | 0.029892 USDC (0.0275 €) | — | 0.55 | — (n=0) | REJECTED | below_safety_margin(29892<108291), reliability_not_demonstrated |
| 52762566 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.225079 WETH | 0.000015 WETH | 0.000000 WETH | 0.000002 WETH | 0.000012 WETH (0.0274 €) | — | 0.55 | — (n=0) | REJECTED | below_safety_margin(12345904587921<45015887185890), reliability_not_demonstrated |
| 52762566 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 458.103691 USDC | 0.035036 USDC | 0.000000 USDC | 0.007249 USDC | 0.027787 USDC (0.0256 €) | — | 0.61 | 0.003 (n=2) | REJECTED | below_safety_margin(27787<91620), reliability_not_demonstrated |
| 52762566 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.005265 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0255 €) | — | 0.65 | 0.003 (n=2) | REJECTED | below_safety_margin(34<105), reliability_not_demonstrated |
| 52762566 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.181257 WETH | 0.000014 WETH | 0.000000 WETH | 0.000003 WETH | 0.000011 WETH (0.0254 €) | — | 0.63 | 0.003 (n=2) | REJECTED | below_safety_margin(11464490662036<36251417654387), reliability_not_demonstrated |
| 52762566 | cbBTC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.001596 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0120 €) | — | 1.00 | 0.137 (n=99) | REJECTED | below_safety_margin(16<31), p_lower_below_threshold(0.14<0.75) |
| 52762566 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 131.818615 USDC | 0.019696 USDC | 0.000000 USDC | 0.007249 USDC | 0.012447 USDC (0.0115 €) | — | 0.94 | 0.137 (n=99) | REJECTED | below_safety_margin(12447<26363), p_lower_below_threshold(0.14<0.75) |
| 52762566 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→WETH | 0.058570 WETH | 0.000008 WETH | 0.000000 WETH | 0.000003 WETH | 0.000005 WETH (0.0113 €) | — | 0.87 | 0.137 (n=99) | REJECTED | below_safety_margin(5079175241737<11714057045433), p_lower_below_threshold(0.14<0.75) |
| 52762660 | USDC→[pancakeswap_v3]→ICNT→[uniswap_v3]→USDC | 35.101996 USDC | 0.017553 USDC | 0.000000 USDC | 0.005423 USDC | 0.012130 USDC (0.0112 €) | — | 3.46 | 0.000 (n=55) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 52762661 | USDC→[pancakeswap_v3]→ICNT→[uniswap_v3]→USDC | 35.101996 USDC | 0.017553 USDC | 0.000000 USDC | 0.005423 USDC | 0.012130 USDC (0.0112 €) | — | 3.46 | 0.000 (n=55) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 52762566 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 201.577418 USDC | 0.015215 USDC | 0.000000 USDC | 0.005417 USDC | 0.009798 USDC (0.0090 €) | — | 0.49 | 0.029 (n=28) | REJECTED | below_safety_margin(9798<40315), reliability_not_demonstrated |
| 52762566 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.083852 WETH | 0.000006 WETH | 0.000000 WETH | 0.000002 WETH | 0.000004 WETH (0.0090 €) | — | 0.48 | 0.029 (n=28) | REJECTED | below_safety_margin(4041835939983<16770437123713), reliability_not_demonstrated |
| 52762418 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 190.806253 USDC | 0.013787 USDC | 0.000000 USDC | 0.005413 USDC | 0.008374 USDC (0.0077 €) | — | 0.44 | 0.029 (n=28) | REJECTED | below_safety_margin(8374<38161), reliability_not_demonstrated |
| 52762418 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.079324 WETH | 0.000006 WETH | 0.000000 WETH | 0.000002 WETH | 0.000003 WETH (0.0077 €) | — | 0.44 | 0.029 (n=28) | REJECTED | below_safety_margin(3470697531420<15864845211956), reliability_not_demonstrated |
| 52762447 | USDC→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 45.394101 USDC | 0.015583 USDC | 0.000000 USDC | 0.007245 USDC | 0.008338 USDC (0.0077 €) | — | 1.84 | 0.340 (n=57) | REJECTED | below_safety_margin(8338<9078), p_lower_below_threshold(0.34<0.75) |
| 52762447 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→WETH | 0.018906 WETH | 0.000006 WETH | 0.000000 WETH | 0.000003 WETH | 0.000003 WETH (0.0077 €) | — | 1.83 | 0.340 (n=57) | REJECTED | below_safety_margin(3457677630276<3781255592517), p_lower_below_threshold(0.34<0.75) |
| 52762447 | USDC→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 46.204025 USDC | 0.015527 USDC | 0.000000 USDC | 0.007245 USDC | 0.008282 USDC (0.0076 €) | — | 1.79 | 0.138 (n=98) | REJECTED | below_safety_margin(8282<9240), p_lower_below_threshold(0.14<0.75) |

## Fiabilité et décision
- Observations ghost : 867 ; taux observé 0.130 ; borne inférieure crédible (0.9) 0.116 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 11.6% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
