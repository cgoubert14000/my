# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-18T09:56:32+00:00 ; durée 58.32 min ; blocs 52762270 → 52764020 (1749 vus)

## Connexion
- Requêtes RPC : 24293 ; erreurs : 0 ; latence p50/p95 : 305.9/691.0 ms
- Rafraîchissements d'état : 1749 ; âge des données au dernier bloc : 2.94 s ; changements de frais LP observés (pools à frais dynamiques) : 4031
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 32868 ; cycles déclenchés par événement : 2506 ; avance médiane sur le rafraîchissement multicall : 395 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,419.39 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 578 pools, 328 jetons, 21580 routes
- Par DEX : uniswap_v3 136, aerodrome 235, aerodrome_slipstream 157, pancakeswap_v3 32, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 207 (rejetés 2) → 612 jetons ; pools candidats 3915 (énumérés 394, par paires 0), mesurés 580, sous le plancher de 10000.0 $ : 2 → gardés 578 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'DAI': 1.0, 'USDC': 1.0, 'WETH': 2410.986474, 'AERO': 0.834015, 'cbBTC': 81629.281689}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 146,321,306 | 2,419.390778 | 52764021 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 42,349,920 | 1.176169 | 52764021 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 18,848,197 | 0.029545 | 52764021 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 500 | 18,264,910 | 0.029516 | 52764021 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 16,815,746 | 108.028008 | 52764021 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,434,264 | 0.029525 | 52764021 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,772,824 | 0.000012 | 52764021 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome_slipstream | USDC/cbBTC | 412 | 9,157,910 | 0.000012 | 52764021 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | WETH/USDC | 500 | 9,078,945 | 2,423.731984 | 52764021 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome_slipstream | USDC/cbBTC | 334 | 7,893,489 | 0.000012 | 52764021 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 624 | 7,521,254 | 2,423.143899 | 52764021 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,164,397 | 0.001654 | 52764021 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | WETH/USDC | 3000 | 5,496,866 | 2,419.594833 | 52764021 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,344,634 | 0.029517 | 52764021 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/superOETHb | 400 | 5,253,878 | 1.000855 | 52764021 | `0x6446021F4E396dA3df4235C62537431372195D38` |
| aerodrome | fBOMB/AERO | 10000 | 5,180,705 | 0.025622 | 52764021 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,836,051 | 0.802398 | 52764021 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,645,903 | 0.000272 | 52764021 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,451,043 | 0.998809 | 52764021 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,441,766 | 2,422.755777 | 52764021 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | WETH/USDT | 412 | 4,419,801 | 2,427.107066 | 52764021 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome_slipstream | USDC/AERO | 10000 | 4,257,968 | 1.180894 | 52764021 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome | WETH/KTA | 3000 | 4,079,098 | 33,366.245783 | 52764021 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/AERO | 10000 | 3,375,449 | 2,863.038615 | 52764021 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,922,293 | 1.141818 | 52764021 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,846,068 | 0.000012 | 52764021 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | AERO/cbBTC | 2700 | 2,662,715 | 0.000010 | 52764021 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/MORPHO | 2739 | 2,571,629 | 1,003.464740 | 52764021 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome_slipstream | WETH/VVV | 2742 | 2,557,582 | 107.998063 | 52764021 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,373,287 | 407.663270 | 52764021 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | WETH/FAI | 10000 | 2,242,212 | 1,181,913.960766 | 52764021 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,105,927 | 1.199962 | 52764021 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,035,374 | 1.374087 | 52764021 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| aerodrome_slipstream | EURC/USDC | 70 | 1,959,492 | 1.123276 | 52764021 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,870,510 | 0.000000 | 52764021 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome | fBOMB/USDC | 10000 | 1,809,899 | 0.021551 | 52764021 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,786,065 | 15.740225 | 52764021 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,781,859 | 0.000012 | 52764021 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | XDP/USDC | 100 | 1,759,978 | 0.018495 | 52764021 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome | weETH_04c0/WETH | 500 | 1,737,662 | 1.105495 | 52764021 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome | WETH/msETH (stable) | 500 | 1,675,108 | 2.307203 | 52764021 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,598,980 | 13,825.580237 | 52764021 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | WETH/AERO | 3000 | 1,526,646 | 2,850.706569 | 52764021 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | WETH/AERO | 3032 | 1,474,776 | 2,850.430707 | 52764021 | `0x82321f3BEB69f503380D6B233857d5C43562e2D0` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,471,457 | 0.916369 | 52764021 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,456,384 | 0.826249 | 52764021 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | DRB/WETH | 10000 | 1,331,605 | 0.000000 | 52764021 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,318,988 | 0.436104 | 52764021 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,302,117 | 0.000272 | 52764021 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,299,975 | 0.004649 | 52764021 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome | WETH/cbBTC | 3000 | 1,260,041 | 0.029519 | 52764021 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| aerodrome | USDC/SEND | 3000 | 1,248,124 | 62.377421 | 52764021 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,243,840 | 23.368113 | 52764021 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,208,839 | 2,423.716951 | 52764021 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | WETH/doginme | 10000 | 1,195,681 | 35,919,457.468583 | 52764021 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome_slipstream | msUSD/USDC | 500 | 1,181,568 | 0.885830 | 52764021 | `0x7501bc8Bb51616F79bfA524E464fb7B41f0B10fB` |
| aerodrome | WETH/WELL | 10000 | 1,166,399 | 1,166,766.396236 | 52764021 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,161,879 | 517,013.914854 | 52764021 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome_slipstream | WETH/msETH | 500 | 1,139,703 | 1.131653 | 52764021 | `0x74F72788F4814D7fF3C49B44684aa98Eee140C0E` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,103,187 | 14.614121 | 52764021 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |

## Recherche d'opportunités
- Cycles : 4254 ; routes examinées : 91801320 ; candidats optimisés : 523898 ; net attendu > 0 : 218 ; dernier cycle 178.8 ms
- Rejets (moteur) : {'spread_below_threshold': 90455487, 'liquidity_below_min': 816084, 'negative_expected_net': 523680, 'borrow_bound_too_small': 4254, 'pool_quarantined': 1478, 'cycle_budget_exhausted': 119}
- Enregistrements de la session : 523898 ; net attendu > 0 : 218 ; simulés (eth_call de la vraie tx) : 19 (ok 2, échec 17) ; étiquettes ghost N+1 : 0/16 positives
- Décisions : {'REJECTED': 523898} ; motifs de rejet : {'below_safety_margin': 198, 'negative_expected_net': 523680, 'p_lower_below_threshold': 155, 'reliability_not_demonstrated': 63, 'simulation_failed': 17}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52763312 | WETH→[uniswap_v3]→TEVA→[aerodrome]→WETH | 0.045860 WETH | 0.000451 WETH | 0.000000 WETH | 0.000002 WETH | 0.000449 WETH (0.9969 €) | — | 97.84 | — (n=0) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52763336 | WETH→[uniswap_v3]→TEVA→[aerodrome]→WETH | 0.044695 WETH | 0.000379 WETH | 0.000000 WETH | 0.000002 WETH | 0.000377 WETH (0.8390 €) | — | 84.36 | 0.006 (n=1) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52762636 | WETH→[aerodrome_slipstream]→KTA→[aerodrome]→WETH | 0.107115 WETH | 0.000278 WETH | 0.000000 WETH | 0.000002 WETH | 0.000276 WETH (0.6125 €) | — | 25.74 | 0.002 (n=4) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52763600 | USDC→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC | 3,878.632894 USDC | 0.327748 USDC | 0.000000 USDC | 0.007270 USDC | 0.320478 USDC (0.2948 €) | — | 0.83 | 0.322 (n=60) | REJECTED | below_safety_margin(320478<775726), p_lower_below_threshold(0.32<0.75) |
| 52763600 | WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→WETH | 1.603094 WETH | 0.000135 WETH | 0.000000 WETH | 0.000003 WETH | 0.000132 WETH (0.2943 €) | — | 0.82 | 0.322 (n=60) | REJECTED | below_safety_margin(132222049332856<320618754324269), p_lower_below_threshold(0.32<0.75) |
| 52763327 | WETH→[aerodrome]→TEVA→[uniswap_v3]→WETH | 0.023839 WETH | 0.000109 WETH | 0.000000 WETH | 0.000002 WETH | 0.000107 WETH (0.2388 €) | — | 45.05 | 0.002 (n=5) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52763600 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC | 2,367.368873 USDC | 0.209741 USDC | 0.000000 USDC | 0.007638 USDC | 0.202103 USDC (0.1859 €) | — | 0.85 | 0.137 (n=99) | REJECTED | below_safety_margin(202103<473473), p_lower_below_threshold(0.14<0.75) |
| 52763600 | WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.978603 WETH | 0.000087 WETH | 0.000000 WETH | 0.000003 WETH | 0.000083 WETH (0.1856 €) | — | 0.85 | 0.137 (n=99) | REJECTED | below_safety_margin(83378593383533<195720682064356), p_lower_below_threshold(0.14<0.75) |
| 52763363 | WETH→[aerodrome]→TEVA→[uniswap_v3]→WETH | 0.021083 WETH | 0.000082 WETH | 0.000000 WETH | 0.000002 WETH | 0.000080 WETH (0.1782 €) | — | 37.99 | 0.001 (n=6) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52762566 | USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 1,272.855682 USDC | 0.121496 USDC | 0.000000 USDC | 0.007249 USDC | 0.114247 USDC (0.1051 €) | — | 0.90 | 0.137 (n=99) | REJECTED | below_safety_margin(114247<254571), p_lower_below_threshold(0.14<0.75) |
| 52762566 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH | 0.527897 WETH | 0.000050 WETH | 0.000000 WETH | 0.000003 WETH | 0.000047 WETH (0.1048 €) | — | 0.89 | 0.137 (n=99) | REJECTED | below_safety_margin(47204935156916<105579478800958), p_lower_below_threshold(0.14<0.75) |
| 52763764 | USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 1,249.525889 USDC | 0.116194 USDC | 0.000000 USDC | 0.007637 USDC | 0.108557 USDC (0.0999 €) | — | 0.87 | 0.137 (n=99) | REJECTED | below_safety_margin(108557<249905), p_lower_below_threshold(0.14<0.75) |
| 52763764 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH | 0.516258 WETH | 0.000048 WETH | 0.000000 WETH | 0.000003 WETH | 0.000045 WETH (0.0996 €) | — | 0.87 | 0.137 (n=99) | REJECTED | below_safety_margin(44765079070361<103251549257064), p_lower_below_threshold(0.14<0.75) |
| 52762566 | USDC→[pancakeswap_v3]→USDT→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 850.849852 USDC | 0.076440 USDC | 0.000000 USDC | 0.007249 USDC | 0.069191 USDC (0.0637 €) | — | 0.81 | 0.137 (n=99) | REJECTED | below_safety_margin(69191<170169), p_lower_below_threshold(0.14<0.75) |
| 52762566 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→USDT→[aerodrome_slipstream]→WETH | 0.352508 WETH | 0.000032 WETH | 0.000000 WETH | 0.000003 WETH | 0.000029 WETH (0.0634 €) | — | 0.81 | 0.137 (n=99) | REJECTED | below_safety_margin(28583796801784<70501568003788), p_lower_below_threshold(0.14<0.75) |
| 52762498 | WETH→[uniswap_v3]→TEVA→[aerodrome]→WETH | 0.011973 WETH | 0.000029 WETH | 0.000000 WETH | 0.000002 WETH | 0.000026 WETH (0.0586 €) | — | 22.08 | 0.002 (n=3) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52763764 | USDC→[pancakeswap_v3]→USDT→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 734.907317 USDC | 0.056744 USDC | 0.000000 USDC | 0.007637 USDC | 0.049107 USDC (0.0452 €) | — | 0.67 | 0.137 (n=99) | REJECTED | below_safety_margin(49107<146981), p_lower_below_threshold(0.14<0.75) |
| 52763764 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→USDT→[aerodrome_slipstream]→WETH | 0.303758 WETH | 0.000023 WETH | 0.000000 WETH | 0.000003 WETH | 0.000020 WETH (0.0451 €) | — | 0.67 | 0.137 (n=99) | REJECTED | below_safety_margin(20245198116310<60751549247842), p_lower_below_threshold(0.14<0.75) |
| 52762566 | USDC→[uniswap_v3]→USDT→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 739.179848 USDC | 0.043147 USDC | 0.000000 USDC | 0.007249 USDC | 0.035898 USDC (0.0330 €) | — | 0.49 | 0.137 (n=99) | REJECTED | below_safety_margin(35898<147835), p_lower_below_threshold(0.14<0.75) |
| 52762566 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→USDT→[aerodrome_slipstream]→WETH | 0.305056 WETH | 0.000018 WETH | 0.000000 WETH | 0.000003 WETH | 0.000015 WETH (0.0329 €) | — | 0.49 | 0.137 (n=99) | REJECTED | below_safety_margin(14825048275491<61011218065792), p_lower_below_threshold(0.14<0.75) |
| 52763330 | USDC→[aerodrome_slipstream]→USDT→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 187.469085 USDC | 0.042620 USDC | 0.000000 USDC | 0.007266 USDC | 0.035354 USDC (0.0325 €) | — | 1.89 | 0.340 (n=57) | REJECTED | below_safety_margin(35354<37493), p_lower_below_threshold(0.34<0.75) |
| 52763330 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→USDT→[uniswap_v3]→WETH | 0.077004 WETH | 0.000018 WETH | 0.000000 WETH | 0.000003 WETH | 0.000015 WETH (0.0324 €) | — | 1.89 | 0.340 (n=57) | REJECTED | below_safety_margin(14566271622707<15400884006628), p_lower_below_threshold(0.34<0.75) |
| 52763330 | USDC→[pancakeswap_v3]→USDT→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 180.928725 USDC | 0.040894 USDC | 0.000000 USDC | 0.007266 USDC | 0.033628 USDC (0.0309 €) | — | 1.86 | 0.137 (n=99) | REJECTED | below_safety_margin(33628<36185), p_lower_below_threshold(0.14<0.75) |
| 52763330 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→USDT→[uniswap_v3]→WETH | 0.074723 WETH | 0.000017 WETH | 0.000000 WETH | 0.000003 WETH | 0.000014 WETH (0.0308 €) | — | 1.85 | 0.137 (n=99) | REJECTED | below_safety_margin(13854569206263<14944627826839), p_lower_below_threshold(0.14<0.75) |
| 52763764 | USDC→[uniswap_v3]→USDT→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 709.979295 USDC | 0.040030 USDC | 0.000000 USDC | 0.007637 USDC | 0.032393 USDC (0.0298 €) | — | 0.46 | 0.137 (n=99) | REJECTED | below_safety_margin(32393<141995), p_lower_below_threshold(0.14<0.75) |

## Fiabilité et décision
- Observations ghost : 879 ; taux observé 0.129 ; borne inférieure crédible (0.9) 0.115 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 11.5% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
