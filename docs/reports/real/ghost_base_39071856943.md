# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-17T21:48:02+00:00 ; durée 3.07 min ; blocs 52742072 → 52742164 (84 vus)

## Connexion
- Requêtes RPC : 1163 ; erreurs : 0 ; latence p50/p95 : 400.9/1,624.0 ms
- Rafraîchissements d'état : 84 ; âge des données au dernier bloc : 9.75 s ; changements de frais LP observés (pools à frais dynamiques) : 486
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 3264 ; cycles déclenchés par événement : 84 ; avance médiane sur le rafraîchissement multicall : 1,082 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,376.93 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 573 pools, 327 jetons, 21034 routes
- Par DEX : uniswap_v3 135, aerodrome 234, aerodrome_slipstream 155, pancakeswap_v3 31, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 206 (rejetés 2) → 611 jetons ; pools candidats 3915 (énumérés 391, par paires 0), mesurés 575, sous le plancher de 10000.0 $ : 2 → gardés 573 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDbC': 1.0, 'USDC': 1.0, 'WETH': 2370.395845, 'AERO': 0.840439, 'cbBTC': 80973.333664}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 144,890,842 | 2,376.925678 | 52742164 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 42,806,258 | 1.186219 | 52742164 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 500 | 17,965,578 | 0.029364 | 52742164 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 16,590,310 | 107.111868 | 52742164 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,320,081 | 0.029289 | 52742164 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| aerodrome_slipstream | WETH/cbBTC | 2555 | 10,197,411 | 0.029302 | 52742164 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,725,942 | 0.000012 | 52742164 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 8,981,881 | 2,382.804543 | 52742164 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome_slipstream | USDC/cbBTC | 368 | 7,826,179 | 0.000012 | 52742164 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,054,602 | 0.001645 | 52742164 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | WETH/USDC | 1011 | 7,001,669 | 2,383.615417 | 52742164 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | USDC/cbBTC | 600 | 6,529,055 | 0.000012 | 52742164 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome | WETH/USDC | 3000 | 5,363,892 | 2,376.845743 | 52742164 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,270,364 | 0.029356 | 52742164 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/superOETHb | 400 | 5,161,662 | 1.000855 | 52742164 | `0x6446021F4E396dA3df4235C62537431372195D38` |
| aerodrome | fBOMB/AERO | 10000 | 5,153,378 | 0.025517 | 52742164 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,751,151 | 0.802399 | 52742164 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,566,629 | 0.000273 | 52742164 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,395,509 | 0.998808 | 52742164 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,344,533 | 2,383.164790 | 52742164 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | WETH/KTA | 3000 | 4,031,267 | 32,973.998190 | 52742164 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | USDC/AERO | 10000 | 3,741,168 | 1.184581 | 52742164 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome_slipstream | WETH/USDT | 484 | 3,443,441 | 2,386.818547 | 52742164 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome | WETH/AERO | 10000 | 3,352,918 | 2,822.443396 | 52742164 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,869,197 | 1.141815 | 52742164 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,824,336 | 0.000012 | 52742164 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/MORPHO | 2703 | 2,639,986 | 1,018.323868 | 52742164 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,638,689 | 407.822538 | 52742164 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 2,529,972 | 0.000010 | 52742164 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/VVV | 2775 | 2,523,742 | 107.101432 | 52742164 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | WETH/FAI | 10000 | 2,211,006 | 1,173,215.805170 | 52742164 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | EURC/USDC | 70 | 2,128,847 | 1.123173 | 52742164 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,105,582 | 1.200159 | 52742164 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome | USDC/alUSDb (stable) | 500 | 1,998,540 | 1.418010 | 52742164 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,844,186 | 0.000000 | 52742164 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome | fBOMB/USDC | 10000 | 1,797,300 | 0.021508 | 52742164 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,768,670 | 0.000012 | 52742164 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | XDP/USDC | 100 | 1,709,023 | 0.017625 | 52742164 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,707,817 | 15.813505 | 52742164 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | WETH/msETH (stable) | 500 | 1,647,681 | 2.303602 | 52742164 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,519,197 | 0.916544 | 52742164 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| uniswap_v3 | WETH/AERO | 3000 | 1,504,357 | 2,822.561154 | 52742164 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | weETH_04c0/WETH | 500 | 1,496,845 | 1.105495 | 52742164 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome_slipstream | WETH/AERO | 3000 | 1,457,972 | 2,822.922480 | 52742164 | `0x82321f3BEB69f503380D6B233857d5C43562e2D0` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,456,403 | 0.826226 | 52742164 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,384,375 | 13,921.741732 | 52742164 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,325,968 | 0.435161 | 52742164 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,319,527 | 0.000000 | 52742164 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,289,149 | 0.004702 | 52742164 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,279,881 | 0.000271 | 52742164 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | USDC/SEND | 3000 | 1,249,187 | 62.271275 | 52742164 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome_slipstream | WETH/msETH | 500 | 1,237,229 | 1.130977 | 52742164 | `0x74F72788F4814D7fF3C49B44684aa98Eee140C0E` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,222,563 | 23.348956 | 52742164 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| aerodrome | WETH/cbBTC | 3000 | 1,218,262 | 0.029287 | 52742164 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,198,997 | 1.105716 | 52742164 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |
| uniswap_v3 | WETH/doginme | 10000 | 1,176,215 | 35,769,306.429768 | 52742164 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,164,836 | 2,382.737684 | 52742164 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | WETH/WELL | 10000 | 1,154,125 | 1,150,234.390163 | 52742164 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,118,965 | 514,828.993746 | 52742164 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,115,138 | 14.228811 | 52742164 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |

## Recherche d'opportunités
- Cycles : 167 ; routes examinées : 3512678 ; candidats optimisés : 24364 ; net attendu > 0 : 20 ; dernier cycle 644.4 ms
- Rejets (moteur) : {'spread_below_threshold': 3456211, 'liquidity_below_min': 31936, 'negative_expected_net': 24344, 'borrow_bound_too_small': 167}
- Enregistrements de la session : 24364 ; net attendu > 0 : 20 ; simulés (eth_call de la vraie tx) : 0 (ok 0, échec 0) ; étiquettes ghost N+1 : 0/0 positives
- Décisions : {'REJECTED': 24364} ; motifs de rejet : {'below_safety_margin': 20, 'negative_expected_net': 24344, 'p_lower_below_threshold': 12, 'reliability_not_demonstrated': 8}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52742108 | USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 885.064337 USDC | 0.046482 USDC | 0.000000 USDC | 0.007535 USDC | 0.038947 USDC (0.0358 €) | — | 0.44 | 0.123 (n=89) | REJECTED | below_safety_margin(38947<177012), p_lower_below_threshold(0.12<0.75) |
| 52742108 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH | 0.371795 WETH | 0.000020 WETH | 0.000000 WETH | 0.000003 WETH | 0.000016 WETH (0.0357 €) | — | 0.44 | 0.123 (n=89) | REJECTED | below_safety_margin(16332658584626<74359001549241), p_lower_below_threshold(0.12<0.75) |
| 52742108 | USDC→[uniswap_v3]→USDT→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 710.243386 USDC | 0.032181 USDC | 0.000000 USDC | 0.007535 USDC | 0.024646 USDC (0.0227 €) | — | 0.35 | 0.123 (n=89) | REJECTED | below_safety_margin(24646<142048), p_lower_below_threshold(0.12<0.75) |
| 52742108 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→USDT→[aerodrome_slipstream]→WETH | 0.298288 WETH | 0.000014 WETH | 0.000000 WETH | 0.000003 WETH | 0.000010 WETH (0.0226 €) | — | 0.35 | 0.123 (n=89) | REJECTED | below_safety_margin(10331726368392<59657615398052), p_lower_below_threshold(0.12<0.75) |
| 52742108 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 160.737188 USDC | 0.011767 USDC | 0.000000 USDC | 0.005363 USDC | 0.006404 USDC (0.0059 €) | — | 0.40 | 0.034 (n=24) | REJECTED | below_safety_margin(6404<32147), reliability_not_demonstrated |
| 52742108 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.067824 WETH | 0.000005 WETH | 0.000000 WETH | 0.000002 WETH | 0.000003 WETH (0.0059 €) | — | 0.40 | 0.034 (n=24) | REJECTED | below_safety_margin(2680284544002<13564793047091), reliability_not_demonstrated |
| 52742108 | USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 83.969683 USDC | 0.010882 USDC | 0.000000 USDC | 0.007174 USDC | 0.003708 USDC (0.0034 €) | — | 0.44 | 0.123 (n=89) | REJECTED | below_safety_margin(3708<16793), p_lower_below_threshold(0.12<0.75) |
| 52742108 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH | 0.035504 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0034 €) | — | 0.44 | 0.123 (n=89) | REJECTED | below_safety_margin(1546517354510<7100788305571), p_lower_below_threshold(0.12<0.75) |
| 52742085 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 371.352119 USDC | 0.007605 USDC | 0.000000 USDC | 0.005357 USDC | 0.002248 USDC (0.0021 €) | — | 0.06 | 0.034 (n=24) | REJECTED | below_safety_margin(2248<74270), reliability_not_demonstrated |
| 52742086 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 371.352119 USDC | 0.007605 USDC | 0.000000 USDC | 0.005357 USDC | 0.002248 USDC (0.0021 €) | — | 0.06 | 0.034 (n=24) | REJECTED | below_safety_margin(2248<74270), reliability_not_demonstrated |
| 52742085 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.156817 WETH | 0.000003 WETH | 0.000000 WETH | 0.000002 WETH | 0.000001 WETH (0.0021 €) | — | 0.06 | 0.034 (n=24) | REJECTED | below_safety_margin(939516100823<31363347058630), reliability_not_demonstrated |
| 52742086 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.156817 WETH | 0.000003 WETH | 0.000000 WETH | 0.000002 WETH | 0.000001 WETH (0.0021 €) | — | 0.06 | 0.034 (n=24) | REJECTED | below_safety_margin(939516100823<31363347058630), reliability_not_demonstrated |
| 52742108 | USDC→[sushiswap_v3]→WETH→[pancakeswap_v3]→USDC | 59.313104 USDC | 0.007560 USDC | 0.000000 USDC | 0.005363 USDC | 0.002197 USDC (0.0020 €) | — | 0.37 | 0.034 (n=24) | REJECTED | below_safety_margin(2197<11862), reliability_not_demonstrated |
| 52742108 | WETH→[pancakeswap_v3]→USDC→[sushiswap_v3]→WETH | 0.025069 WETH | 0.000003 WETH | 0.000000 WETH | 0.000002 WETH | 0.000001 WETH (0.0020 €) | — | 0.36 | 0.034 (n=24) | REJECTED | below_safety_margin(914770340892<5013889053584), reliability_not_demonstrated |
| 52742108 | USDC→[aerodrome_slipstream]→USDT→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 89.998989 USDC | 0.008301 USDC | 0.000000 USDC | 0.007174 USDC | 0.001127 USDC (0.0010 €) | — | 0.13 | 0.123 (n=89) | REJECTED | below_safety_margin(1127<17999), p_lower_below_threshold(0.12<0.75) |
| 52742108 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→USDT→[uniswap_v3]→WETH | 0.038277 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0010 €) | — | 0.12 | 0.123 (n=89) | REJECTED | below_safety_margin(463408273994<7655445217863), p_lower_below_threshold(0.12<0.75) |
| 52742108 | USDC→[uniswap_v3]→AAVE→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 31.486270 USDC | 0.008018 USDC | 0.000000 USDC | 0.007174 USDC | 0.000844 USDC (0.0008 €) | — | 0.27 | 0.123 (n=89) | REJECTED | below_safety_margin(844<6297), p_lower_below_threshold(0.12<0.75) |
| 52742108 | USDC→[uniswap_v3]→AAVE→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 31.486270 USDC | 0.008018 USDC | 0.000000 USDC | 0.007174 USDC | 0.000844 USDC (0.0008 €) | — | 0.27 | 0.123 (n=89) | REJECTED | below_safety_margin(844<6297), p_lower_below_threshold(0.12<0.75) |
| 52742108 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→AAVE→[pancakeswap_v3]→WETH | 0.013268 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0008 €) | — | 0.26 | 0.123 (n=89) | REJECTED | below_safety_margin(344698103289<2653534928260), p_lower_below_threshold(0.12<0.75) |
| 52742108 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→AAVE→[pancakeswap_v3]→WETH | 0.013268 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0008 €) | — | 0.26 | 0.123 (n=89) | REJECTED | below_safety_margin(344698103289<2653534928260), p_lower_below_threshold(0.12<0.75) |

## Fiabilité et décision
- Observations ghost : 811 ; taux observé 0.132 ; borne inférieure crédible (0.9) 0.117 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 11.7% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
