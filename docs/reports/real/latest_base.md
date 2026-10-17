# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-17T21:57:11+00:00 ; durée 12.21 min ; blocs 52742072 → 52742441 (349 vus)

## Connexion
- Requêtes RPC : 4680 ; erreurs : 0 ; latence p50/p95 : 337.8/1,359.2 ms
- Rafraîchissements d'état : 349 ; âge des données au dernier bloc : 3.31 s ; changements de frais LP observés (pools à frais dynamiques) : 1494
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 10623 ; cycles déclenchés par événement : 386 ; avance médiane sur le rafraîchissement multicall : 630 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,376.93 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 573 pools, 327 jetons, 21034 routes
- Par DEX : uniswap_v3 135, aerodrome 234, aerodrome_slipstream 155, pancakeswap_v3 31, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 206 (rejetés 2) → 611 jetons ; pools candidats 3915 (énumérés 391, par paires 0), mesurés 575, sous le plancher de 10000.0 $ : 2 → gardés 573 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDbC': 1.0, 'USDC': 1.0, 'WETH': 2370.395845, 'AERO': 0.840439, 'cbBTC': 80973.333664}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 144,837,107 | 2,376.925166 | 52742441 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 42,783,786 | 1.187466 | 52742441 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 500 | 17,970,059 | 0.029320 | 52742441 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 16,608,165 | 106.881630 | 52742441 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 15,475,210 | 0.029302 | 52742441 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,325,257 | 0.029289 | 52742441 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,732,541 | 0.000012 | 52742441 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 8,981,614 | 2,373.262913 | 52742441 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome_slipstream | USDC/cbBTC | 344 | 7,831,079 | 0.000012 | 52742441 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | USDC/cbBTC | 484 | 7,386,204 | 0.000012 | 52742441 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,060,947 | 0.001643 | 52742441 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | WETH/USDC | 713 | 6,894,699 | 2,372.761456 | 52742441 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome | WETH/USDC | 3000 | 5,363,892 | 2,376.755445 | 52742441 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,272,167 | 0.029317 | 52742441 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/superOETHb | 400 | 5,161,661 | 1.000855 | 52742441 | `0x6446021F4E396dA3df4235C62537431372195D38` |
| aerodrome | fBOMB/AERO | 10000 | 5,150,678 | 0.025517 | 52742441 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,751,150 | 0.802399 | 52742441 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,566,626 | 0.000273 | 52742441 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,402,131 | 0.998808 | 52742441 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,344,427 | 2,372.810895 | 52742441 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | WETH/KTA | 3000 | 4,030,420 | 32,987.848961 | 52742441 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | USDC/AERO | 10000 | 3,830,012 | 1.184581 | 52742441 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome_slipstream | WETH/USDT | 430 | 3,786,621 | 2,377.681665 | 52742441 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome | WETH/AERO | 10000 | 3,351,156 | 2,822.449829 | 52742441 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,869,198 | 1.141815 | 52742441 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,826,993 | 0.000012 | 52742441 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/VVV | 2712 | 2,526,852 | 106.858068 | 52742441 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,503,198 | 407.758850 | 52742441 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 2,477,608 | 0.000010 | 52742441 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | WETH/FAI | 10000 | 2,211,006 | 1,173,215.805170 | 52742441 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 2,204,078 | 1,018.324297 | 52742441 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome_slipstream | EURC/USDC | 70 | 2,128,799 | 1.123135 | 52742441 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,105,582 | 1.200159 | 52742441 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome | USDC/alUSDb (stable) | 500 | 1,998,540 | 1.418010 | 52742441 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,854,169 | 0.000000 | 52742441 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,830,786 | 15.813505 | 52742441 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | fBOMB/USDC | 10000 | 1,797,304 | 0.021508 | 52742441 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,770,290 | 0.000012 | 52742441 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,734,025 | 13,915.130042 | 52742441 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | XDP/USDC | 100 | 1,711,083 | 0.017657 | 52742441 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome | WETH/msETH (stable) | 500 | 1,647,681 | 2.303602 | 52742441 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,519,199 | 0.916543 | 52742441 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| uniswap_v3 | WETH/AERO | 3000 | 1,502,484 | 2,822.580785 | 52742441 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | weETH_04c0/WETH | 500 | 1,496,844 | 1.105495 | 52742441 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome_slipstream | WETH/AERO | 3000 | 1,456,562 | 2,822.994612 | 52742441 | `0x82321f3BEB69f503380D6B233857d5C43562e2D0` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,456,403 | 0.826226 | 52742441 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,325,968 | 0.435161 | 52742441 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,320,341 | 0.000000 | 52742441 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,289,148 | 0.004702 | 52742441 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,279,880 | 0.000271 | 52742441 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | USDC/SEND | 3000 | 1,249,187 | 62.271275 | 52742441 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome_slipstream | WETH/msETH | 500 | 1,237,108 | 1.130977 | 52742441 | `0x74F72788F4814D7fF3C49B44684aa98Eee140C0E` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,222,563 | 23.348953 | 52742441 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| aerodrome | WETH/cbBTC | 3000 | 1,219,178 | 0.029287 | 52742441 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,198,997 | 1.105716 | 52742441 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |
| uniswap_v3 | WETH/doginme | 10000 | 1,176,215 | 35,769,306.429768 | 52742441 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,164,841 | 2,373.275070 | 52742441 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | WETH/WELL | 10000 | 1,154,125 | 1,150,234.390163 | 52742441 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,118,965 | 514,828.993746 | 52742441 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,113,756 | 14.273125 | 52742441 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |

## Recherche d'opportunités
- Cycles : 734 ; routes examinées : 15438956 ; candidats optimisés : 81634 ; net attendu > 0 : 94 ; dernier cycle 329.0 ms
- Rejets (moteur) : {'spread_below_threshold': 15225302, 'liquidity_below_min': 131286, 'negative_expected_net': 81540, 'borrow_bound_too_small': 734}
- Enregistrements de la session : 81634 ; net attendu > 0 : 94 ; simulés (eth_call de la vraie tx) : 4 (ok 0, échec 4) ; étiquettes ghost N+1 : 0/4 positives
- Décisions : {'REJECTED': 81634} ; motifs de rejet : {'below_safety_margin': 79, 'negative_expected_net': 81540, 'p_lower_below_threshold': 63, 'reliability_not_demonstrated': 31, 'simulation_failed': 4, 'stale_data': 10}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52742255 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 123.814998 USDC | 0.238334 USDC | 0.000000 USDC | 0.006798 USDC | 0.231536 USDC (0.2130 €) | — | 18.70 | 0.001 (n=11) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52742202 | WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.611295 WETH | 0.000081 WETH | 0.000000 WETH | 0.000003 WETH | 0.000078 WETH (0.1709 €) | — | 1.28 | 0.123 (n=89) | REJECTED | below_safety_margin(78164265599601<122258937150799), p_lower_below_threshold(0.12<0.75) |
| 52742202 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC | 1,454.331007 USDC | 0.193676 USDC | 0.000000 USDC | 0.007891 USDC | 0.185785 USDC (0.1709 €) | — | 1.28 | 0.123 (n=89) | REJECTED | below_safety_margin(185785<290866), p_lower_below_threshold(0.12<0.75) |
| 52742236 | WETH→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.065212 WETH | 0.000075 WETH | 0.000000 WETH | 0.000003 WETH | 0.000072 WETH (0.1570 €) | — | 11.01 | 0.001 (n=11) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52742236 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→USDC | 154.844888 USDC | 0.177856 USDC | 0.000000 USDC | 0.007525 USDC | 0.170331 USDC (0.1567 €) | — | 11.00 | 0.001 (n=11) | REJECTED | reliability_not_demonstrated |
| 52742236 | WETH→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.060658 WETH | 0.000068 WETH | 0.000000 WETH | 0.000003 WETH | 0.000065 WETH (0.1411 €) | — | 10.64 | 0.001 (n=9) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52742236 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→USDC | 143.497973 USDC | 0.160321 USDC | 0.000000 USDC | 0.007164 USDC | 0.153157 USDC (0.1409 €) | — | 10.67 | 0.001 (n=9) | REJECTED | reliability_not_demonstrated |
| 52742236 | WETH→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→WETH | 0.031865 WETH | 0.000035 WETH | 0.000000 WETH | 0.000003 WETH | 0.000032 WETH (0.0701 €) | — | 10.06 | 0.001 (n=9) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52742236 | USDC→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→USDC | 75.656652 USDC | 0.083333 USDC | 0.000000 USDC | 0.007164 USDC | 0.076169 USDC (0.0701 €) | — | 10.07 | 0.001 (n=9) | REJECTED | reliability_not_demonstrated |
| 52742236 | WETH→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.043006 WETH | 0.000033 WETH | 0.000000 WETH | 0.000003 WETH | 0.000030 WETH (0.0663 €) | — | 7.05 | 0.141 (n=78) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 52742236 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→USDC | 102.131442 USDC | 0.079194 USDC | 0.000000 USDC | 0.007164 USDC | 0.072030 USDC (0.0663 €) | — | 7.05 | 0.141 (n=78) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 52742236 | WETH→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.043006 WETH | 0.000033 WETH | 0.000000 WETH | 0.000003 WETH | 0.000030 WETH (0.0648 €) | — | 6.89 | 0.180 (n=43) | REJECTED | p_lower_below_threshold(0.18<0.75) |
| 52742236 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→USDC | 102.211445 USDC | 0.077523 USDC | 0.000000 USDC | 0.007164 USDC | 0.070359 USDC (0.0647 €) | — | 6.88 | 0.180 (n=43) | REJECTED | p_lower_below_threshold(0.18<0.75) |
| 52742236 | WETH→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→WETH | 0.042451 WETH | 0.000032 WETH | 0.000000 WETH | 0.000003 WETH | 0.000029 WETH (0.0625 €) | — | 6.74 | 0.180 (n=43) | REJECTED | p_lower_below_threshold(0.18<0.75) |
| 52742236 | USDC→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→USDC | 100.441773 USDC | 0.075060 USDC | 0.000000 USDC | 0.007164 USDC | 0.067896 USDC (0.0625 €) | — | 6.76 | 0.180 (n=43) | REJECTED | p_lower_below_threshold(0.18<0.75) |
| 52742236 | WETH→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→USDC→[sushiswap_v3]→WETH | 0.033527 WETH | 0.000026 WETH | 0.000000 WETH | 0.000003 WETH | 0.000023 WETH (0.0508 €) | — | 6.92 | 0.180 (n=43) | REJECTED | p_lower_below_threshold(0.18<0.75) |
| 52742236 | USDC→[sushiswap_v3]→WETH→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→USDC | 79.365665 USDC | 0.062317 USDC | 0.000000 USDC | 0.007164 USDC | 0.055153 USDC (0.0507 €) | — | 6.95 | 0.180 (n=43) | REJECTED | p_lower_below_threshold(0.18<0.75) |
| 52742108 | USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 885.064337 USDC | 0.046482 USDC | 0.000000 USDC | 0.007535 USDC | 0.038947 USDC (0.0358 €) | — | 0.44 | 0.123 (n=89) | REJECTED | below_safety_margin(38947<177012), p_lower_below_threshold(0.12<0.75) |
| 52742108 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH | 0.371795 WETH | 0.000020 WETH | 0.000000 WETH | 0.000003 WETH | 0.000016 WETH (0.0357 €) | — | 0.44 | 0.123 (n=89) | REJECTED | below_safety_margin(16332658584626<74359001549241), p_lower_below_threshold(0.12<0.75) |
| 52742201 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC | 676.025357 USDC | 0.041708 USDC | 0.000000 USDC | 0.007530 USDC | 0.034178 USDC (0.0314 €) | — | 0.51 | 0.123 (n=89) | REJECTED | below_safety_margin(34178<135205), p_lower_below_threshold(0.12<0.75) |
| 52742201 | WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.283907 WETH | 0.000018 WETH | 0.000000 WETH | 0.000003 WETH | 0.000014 WETH (0.0314 €) | — | 0.51 | 0.123 (n=89) | REJECTED | below_safety_margin(14374015574297<56781320339516), p_lower_below_threshold(0.12<0.75) |
| 52742202 | WETH→[aerodrome_slipstream]→USDT→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.214519 WETH | 0.000017 WETH | 0.000000 WETH | 0.000003 WETH | 0.000014 WETH (0.0300 €) | — | 0.64 | 0.123 (n=89) | REJECTED | below_safety_margin(13710089921612<42903814859943), p_lower_below_threshold(0.12<0.75) |
| 52742202 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDT→[pancakeswap_v3]→USDC | 508.135404 USDC | 0.040114 USDC | 0.000000 USDC | 0.007530 USDC | 0.032584 USDC (0.0300 €) | — | 0.64 | 0.123 (n=89) | REJECTED | below_safety_margin(32584<101627), p_lower_below_threshold(0.12<0.75) |
| 52742202 | WETH→[aerodrome_slipstream]→USDT→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.253092 WETH | 0.000015 WETH | 0.000000 WETH | 0.000003 WETH | 0.000011 WETH (0.0251 €) | — | 0.45 | 0.123 (n=89) | REJECTED | below_safety_margin(11491344260535<50618384720022), p_lower_below_threshold(0.12<0.75) |
| 52742202 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDT→[uniswap_v3]→USDC | 601.895050 USDC | 0.034841 USDC | 0.000000 USDC | 0.007530 USDC | 0.027311 USDC (0.0251 €) | — | 0.45 | 0.123 (n=89) | REJECTED | below_safety_margin(27311<120379), p_lower_below_threshold(0.12<0.75) |

## Fiabilité et décision
- Observations ghost : 815 ; taux observé 0.131 ; borne inférieure crédible (0.9) 0.117 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 11.7% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
