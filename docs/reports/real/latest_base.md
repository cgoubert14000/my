# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-17T16:51:07+00:00 ; durée 43.05 min ; blocs 52731965 → 52733255 (1196 vus)

## Connexion
- Requêtes RPC : 16039 ; erreurs : 0 ; latence p50/p95 : 255.7/1,536.5 ms
- Rafraîchissements d'état : 1196 ; âge des données au dernier bloc : 4.65 s ; changements de frais LP observés (pools à frais dynamiques) : 1708
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 24240 ; cycles déclenchés par événement : 1229 ; avance médiane sur le rafraîchissement multicall : 1,684 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,408.52 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 576 pools, 328 jetons, 21110 routes
- Par DEX : uniswap_v3 136, aerodrome 235 (quarantaine 1), aerodrome_slipstream 156, pancakeswap_v3 31, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 207 (rejetés 2) → 612 jetons ; pools candidats 3916 (énumérés 393, par paires 0), mesurés 578, sous le plancher de 10000.0 $ : 2 → gardés 576 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDC': 1.0, 'USDbC': 1.0, 'WETH': 2411.894998, 'AERO': 0.849168, 'cbBTC': 81312.167025}
- Pools en quarantaine : 1 — aerodrome:fBOMB/AERO@0xbBf71A: simulation failed ×5 (model/chain mismatch) — until block 52733477

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 146,110,712 | 2,408.518485 | 52733256 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 42,046,802 | 1.180651 | 52733256 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 500 | 18,170,938 | 0.029604 | 52733256 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 16,974,136 | 0.029663 | 52733256 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/VVV | 3000 | 15,734,571 | 107.762012 | 52733256 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,422,701 | 0.029678 | 52733256 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,753,319 | 0.000012 | 52733256 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 9,084,130 | 2,404.868260 | 52733256 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome_slipstream | USDC/cbBTC | 448 | 9,016,911 | 0.000012 | 52733256 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome_slipstream | WETH/USDC | 549 | 8,090,557 | 2,404.108833 | 52733256 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | USDC/cbBTC | 338 | 7,842,938 | 0.000012 | 52733256 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,125,087 | 0.001661 | 52733256 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | WETH/USDC | 3000 | 5,399,359 | 2,408.647877 | 52733256 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,318,093 | 0.029601 | 52733256 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | fBOMB/AERO | 10000 | 5,233,466 | 0.025349 | 52733256 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome_slipstream | WETH/superOETHb | 400 | 5,230,268 | 1.000855 | 52733256 | `0x6446021F4E396dA3df4235C62537431372195D38` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,814,272 | 0.802398 | 52733256 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,632,914 | 0.000273 | 52733256 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,418,131 | 0.998801 | 52733256 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,414,223 | 2,403.834758 | 52733256 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | WETH/KTA | 3000 | 4,021,931 | 34,013.734427 | 52733256 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | USDC/AERO | 10000 | 3,484,151 | 1.172258 | 52733256 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome | WETH/AERO | 10000 | 3,384,448 | 2,820.202616 | 52733256 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | WETH/USDT | 406 | 3,067,692 | 2,408.605125 | 52733256 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,908,984 | 1.141801 | 52733257 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,836,493 | 0.000012 | 52733256 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,792,152 | 407.565825 | 52733256 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 2,706,257 | 0.000010 | 52733256 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/VVV | 2703 | 2,548,024 | 107.756872 | 52733256 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | WETH/FAI | 10000 | 2,231,780 | 1,182,290.188062 | 52733256 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 2,144,908 | 1,025.949622 | 52733256 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome_slipstream | EURC/USDC | 70 | 2,125,788 | 1.123371 | 52733256 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,107,462 | 1.199039 | 52733256 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome | USDC/alUSDb (stable) | 500 | 1,998,480 | 1.418053 | 52733256 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| aerodrome | fBOMB/USDC | 10000 | 1,820,329 | 0.022074 | 52733256 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,803,735 | 0.000000 | 52733256 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,777,120 | 0.000012 | 52733256 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | XDP/USDC | 100 | 1,738,109 | 0.018113 | 52733256 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,719,833 | 15.872651 | 52733256 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | WETH/msETH (stable) | 500 | 1,667,771 | 2.306138 | 52733256 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,648,401 | 13,760.526679 | 52733256 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,539,382 | 0.916547 | 52733256 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| uniswap_v3 | WETH/AERO | 3000 | 1,520,024 | 2,838.612583 | 52733256 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | weETH_04c0/WETH | 500 | 1,516,740 | 1.105495 | 52733256 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome_slipstream | WETH/AERO | 3000 | 1,470,652 | 2,839.620222 | 52733256 | `0x82321f3BEB69f503380D6B233857d5C43562e2D0` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,455,756 | 0.826691 | 52733256 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | DRB/WETH | 10000 | 1,356,898 | 0.000000 | 52733256 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,327,026 | 0.435656 | 52733256 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,305,154 | 0.004696 | 52733256 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,298,433 | 0.000272 | 52733256 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | USDC/SEND | 3000 | 1,248,708 | 62.319117 | 52733256 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,245,630 | 23.342752 | 52733256 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| aerodrome | WETH/cbBTC | 3000 | 1,229,452 | 0.029679 | 52733256 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| aerodrome_slipstream | WETH/msETH | 500 | 1,228,579 | 1.131378 | 52733256 | `0x74F72788F4814D7fF3C49B44684aa98Eee140C0E` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,214,934 | 1.105716 | 52733256 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |
| uniswap_v3 | WETH/doginme | 10000 | 1,193,523 | 35,598,184.590662 | 52733256 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,169,227 | 2,404.841518 | 52733256 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | WETH/WELL | 10000 | 1,169,016 | 1,151,117.734969 | 52733256 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,136,736 | 511,211.436392 | 52733256 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,117,566 | 14.147444 | 52733256 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |

## Recherche d'opportunités
- Cycles : 2423 ; routes examinées : 51149530 ; candidats optimisés : 472928 ; net attendu > 0 : 100 ; dernier cycle 651.3 ms
- Rejets (moteur) : {'spread_below_threshold': 50062917, 'negative_expected_net': 472828, 'liquidity_below_min': 420687, 'pool_quarantined': 177242, 'cycle_budget_exhausted': 13335, 'borrow_bound_too_small': 2421}
- Enregistrements de la session : 472928 ; net attendu > 0 : 100 ; simulés (eth_call de la vraie tx) : 37 (ok 1, échec 36) ; étiquettes ghost N+1 : 0/21 positives
- Décisions : {'REJECTED': 472928} ; motifs de rejet : {'below_safety_margin': 62, 'negative_expected_net': 472828, 'p_lower_below_threshold': 66, 'price_impact': 43, 'reliability_not_demonstrated': 34, 'simulation_failed': 36}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52732232 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 264.379140 USDC | 0.953137 USDC | 0.000000 USDC | 0.005417 USDC | 0.947720 USDC (0.8719 €) | — | 35.85 | 0.003 (n=2) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52732691 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 82.007926 USDC | 0.093812 USDC | 0.000000 USDC | 0.005413 USDC | 0.088399 USDC (0.0813 €) | — | 10.78 | 0.001 (n=9) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52732602 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 71.137118 USDC | 0.070045 USDC | 0.000000 USDC | 0.005414 USDC | 0.064631 USDC (0.0595 €) | — | 9.09 | 0.001 (n=8) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52732142 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 66.177836 USDC | 0.061275 USDC | 0.000000 USDC | 0.005418 USDC | 0.055857 USDC (0.0514 €) | — | 8.44 | 0.001 (n=8) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52733101 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.003508 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0501 €) | — | 1.91 | 0.114 (n=81) | REJECTED | below_safety_margin(67<70), p_lower_below_threshold(0.11<0.75) |
| 52733100 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.003508 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0501 €) | — | 1.91 | 0.114 (n=81) | REJECTED | below_safety_margin(67<70), p_lower_below_threshold(0.11<0.75) |
| 52733101 | WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.129765 WETH | 0.000025 WETH | 0.000000 WETH | 0.000003 WETH | 0.000022 WETH (0.0495 €) | — | 1.72 | 0.114 (n=81) | REJECTED | below_safety_margin(22316890957272<25953007010325), p_lower_below_threshold(0.11<0.75) |
| 52733100 | WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.129765 WETH | 0.000025 WETH | 0.000000 WETH | 0.000003 WETH | 0.000022 WETH (0.0495 €) | — | 1.72 | 0.114 (n=81) | REJECTED | below_safety_margin(22316890957272<25953007010325), p_lower_below_threshold(0.11<0.75) |
| 52732133 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 63.237107 USDC | 0.055672 USDC | 0.000000 USDC | 0.005417 USDC | 0.050255 USDC (0.0462 €) | — | 7.95 | 0.000 (n=39) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 52732724 | USDC→[pancakeswap_v3]→ICNT→[uniswap_v3]→USDC | 57.353428 USDC | 0.045997 USDC | 0.000000 USDC | 0.005413 USDC | 0.040584 USDC (0.0373 €) | — | 7.08 | 0.000 (n=43) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 52732707 | USDC→[pancakeswap_v3]→ICNT→[uniswap_v3]→USDC | 56.643370 USDC | 0.045074 USDC | 0.000000 USDC | 0.005413 USDC | 0.039661 USDC (0.0365 €) | — | 7.00 | 0.000 (n=42) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 52733041 | WETH→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.029762 WETH | 0.000016 WETH | 0.000000 WETH | 0.000003 WETH | 0.000013 WETH (0.0283 €) | — | 4.29 | 0.187 (n=37) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.19<0.75) |
| 52733041 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→USDC | 71.475973 USDC | 0.038647 USDC | 0.000000 USDC | 0.007973 USDC | 0.030674 USDC (0.0282 €) | — | 4.29 | 0.187 (n=37) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.19<0.75) |
| 52731994 | USDC→[pancakeswap_v3]→ICNT→[uniswap_v3]→USDC | 49.123984 USDC | 0.035056 USDC | 0.000000 USDC | 0.005418 USDC | 0.029638 USDC (0.0273 €) | — | 6.03 | 0.000 (n=38) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 52732179 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 47.491583 USDC | 0.031398 USDC | 0.000000 USDC | 0.005418 USDC | 0.025980 USDC (0.0239 €) | — | 5.47 | 0.000 (n=40) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 52732563 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 43.225845 USDC | 0.026339 USDC | 0.000000 USDC | 0.005413 USDC | 0.020926 USDC (0.0193 €) | 0.020926 USDC | 4.84 | 0.000 (n=41) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 52733185 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 42.695240 USDC | 0.025486 USDC | 0.000000 USDC | 0.005409 USDC | 0.020077 USDC (0.0185 €) | — | 4.70 | 0.000 (n=43) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 52733186 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 33.357873 USDC | 0.015586 USDC | 0.000000 USDC | 0.005409 USDC | 0.010177 USDC (0.0094 €) | — | 3.05 | 0.000 (n=44) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 52732460 | WETH→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.019406 WETH | 0.000006 WETH | 0.000000 WETH | 0.000003 WETH | 0.000003 WETH (0.0065 €) | — | 1.52 | 0.290 (n=51) | REJECTED | below_safety_margin(2943520689558<3881143784511), p_lower_below_threshold(0.29<0.75) |
| 52732460 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→USDC | 46.869297 USDC | 0.015056 USDC | 0.000000 USDC | 0.007979 USDC | 0.007077 USDC (0.0065 €) | — | 1.51 | 0.290 (n=51) | REJECTED | below_safety_margin(7077<9373), p_lower_below_threshold(0.29<0.75) |
| 52732460 | WETH→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.019718 WETH | 0.000006 WETH | 0.000000 WETH | 0.000003 WETH | 0.000003 WETH (0.0064 €) | — | 1.46 | 0.114 (n=81) | REJECTED | below_safety_margin(2887808715383<3943537922103), p_lower_below_threshold(0.11<0.75) |
| 52732460 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→USDC | 47.437273 USDC | 0.014921 USDC | 0.000000 USDC | 0.007979 USDC | 0.006942 USDC (0.0064 €) | — | 1.46 | 0.114 (n=81) | REJECTED | below_safety_margin(6942<9487), p_lower_below_threshold(0.11<0.75) |
| 52732225 | WETH→[aerodrome_slipstream]→VIRTUAL→[aerodrome_slipstream]→WETH | 0.052177 WETH | 0.000005 WETH | 0.000000 WETH | 0.000002 WETH | 0.000003 WETH (0.0063 €) | — | 0.55 | 0.060 (n=5) | REJECTED | below_safety_margin(2848717723533<10435382408403), reliability_not_demonstrated |
| 52732225 | WETH→[uniswap_v3]→VIRTUAL→[aerodrome_slipstream]→WETH | 0.044966 WETH | 0.000005 WETH | 0.000000 WETH | 0.000002 WETH | 0.000003 WETH (0.0062 €) | — | 0.63 | 0.060 (n=5) | REJECTED | below_safety_margin(2811407128763<8993117040184), reliability_not_demonstrated |
| 52732703 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 28.271366 USDC | 0.011093 USDC | 0.000000 USDC | 0.005413 USDC | 0.005680 USDC (0.0052 €) | — | 2.01 | 0.039 (n=21) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |

## Fiabilité et décision
- Observations ghost : 763 ; taux observé 0.119 ; borne inférieure crédible (0.9) 0.105 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 10.5% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
