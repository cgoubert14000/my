# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-19T14:04:45+00:00 ; durée 61.36 min ; blocs 52812825 → 52814667 (1824 vus)

## Connexion
- Requêtes RPC : 22760 ; erreurs : 35 ; latence p50/p95 : 419.2/1,124.0 ms
- Rafraîchissements d'état : 1824 ; âge des données au dernier bloc : 4.06 s ; changements de frais LP observés (pools à frais dynamiques) : 5294
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 17685 ; cycles déclenchés par événement : 471 ; avance médiane sur le rafraîchissement multicall : 1,123 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,390.34 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 571 pools, 327 jetons, 21004 routes
- Par DEX : uniswap_v3 137, aerodrome 234 (quarantaine 2), aerodrome_slipstream 153, pancakeswap_v3 30, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 207 (rejetés 2) → 612 jetons ; pools candidats 3877 (énumérés 390, par paires 0), mesurés 574, sous le plancher de 10000.0 $ : 3 → gardés 571 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2419.85313, 'AERO': 0.782295, 'cbBTC': 82567.067054}
- Pools en quarantaine : 2 — aerodrome:fBOMB/AERO@0xbBf71A: simulation failed ×5 (model/chain mismatch) — until block 52814933; aerodrome:fBOMB/USDC@0xFf8e0b: simulation failed ×5 (model/chain mismatch) — until block 52814933

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 146,782,648 | 2,390.335717 | 52814666 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 34,828,684 | 1.294801 | 52814666 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 500 | 18,191,900 | 0.029201 | 52814666 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 16,934,942 | 103.062985 | 52814667 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,306,139 | 0.029264 | 52814666 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| aerodrome_slipstream | WETH/cbBTC | 2550 | 10,087,667 | 0.029249 | 52814666 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,838,704 | 0.000012 | 52814666 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 8,346,920 | 2,386.614770 | 52814666 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/USDC | 3000 | 8,290,818 | 2,390.275341 | 52814667 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | USDC/cbBTC | 390 | 7,814,773 | 0.000012 | 52814666 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,154,663 | 0.001654 | 52814666 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | WETH/USDC | 1026 | 7,144,828 | 2,386.762293 | 52814666 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | USDC/cbBTC | 600 | 6,626,168 | 0.000012 | 52814666 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,315,185 | 0.029208 | 52814667 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | USDC/AERO | 10000 | 4,996,903 | 1.294576 | 52814666 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome | fBOMB/AERO | 10000 | 4,875,520 | 0.025987 | 52814666 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,777,544 | 0.802395 | 52814666 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,594,738 | 0.000273 | 52814666 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,403,639 | 2,386.942810 | 52814667 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,337,556 | 0.998770 | 52814666 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,996,259 | 33,933.944010 | 52814666 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDT | 505 | 3,261,027 | 2,389.690726 | 52814666 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome | WETH/AERO | 10000 | 3,211,299 | 3,085.313522 | 52814666 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,849,556 | 0.000012 | 52814666 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,704,057 | 1.142011 | 52814666 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,611,208 | 406.588465 | 52814666 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | WETH/VVV | 2982 | 2,601,627 | 103.059148 | 52814666 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | AERO/cbBTC | 2700 | 2,386,358 | 0.000009 | 52814666 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | WETH/FAI | 10000 | 2,168,123 | 1,233,892.687804 | 52814666 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,060,112 | 1.237119 | 52814666 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | BNKR/WETH | 10000 | 2,037,372 | 0.000000 | 52814666 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,036,743 | 1.372638 | 52814666 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,769,291 | 0.000012 | 52814667 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | XDP/USDC | 100 | 1,756,878 | 0.018451 | 52814666 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,756,427 | 16.013849 | 52814666 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,736,893 | 13,919.033520 | 52814666 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | weETH_04c0/WETH | 500 | 1,728,410 | 1.105523 | 52814666 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome | fBOMB/USDC | 10000 | 1,713,021 | 0.020593 | 52814666 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| aerodrome | WETH/msETH (stable) | 500 | 1,654,331 | 2.306702 | 52814666 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | EURC/USDC | 70 | 1,612,098 | 1.122131 | 52814666 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| uniswap_v3 | WETH/AERO | 3000 | 1,585,768 | 3,091.038100 | 52814666 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,548,243 | 0.916350 | 52814666 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| aerodrome_slipstream | WETH/MORPHO | 2718 | 1,527,911 | 988.346424 | 52814666 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,456,180 | 0.827383 | 52814666 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,337,795 | 0.435482 | 52814666 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,309,101 | 0.000000 | 52814666 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,287,942 | 0.000273 | 52814666 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,278,150 | 0.004581 | 52814666 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome | WETH/cbBTC | 3000 | 1,277,550 | 0.029267 | 52814666 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,267,252 | 23.125862 | 52814666 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| aerodrome | USDC/SEND | 3000 | 1,232,868 | 63.930699 | 52814666 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome | WETH/WELL | 10000 | 1,195,856 | 1,083,280.313004 | 52814666 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/doginme | 10000 | 1,192,252 | 35,148,301.060571 | 52814666 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,190,019 | 2,386.520811 | 52814666 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome_slipstream | WETH/msETH | 500 | 1,137,741 | 1.131543 | 52814666 | `0x74F72788F4814D7fF3C49B44684aa98Eee140C0E` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,124,851 | 515,481.870232 | 52814666 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | USDC/NOCK | 3000 | 1,100,980 | 51.980754 | 52814666 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,078,334 | 15.476100 | 52814666 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome_slipstream | msUSD/USDC | 509 | 1,075,559 | 0.885402 | 52814666 | `0x7501bc8Bb51616F79bfA524E464fb7B41f0B10fB` |
| aerodrome | WETH/EDEL | 7000 | 1,047,925 | 89,622.234483 | 52814667 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |

## Recherche d'opportunités
- Cycles : 2294 ; routes examinées : 48183176 ; candidats optimisés : 418353 ; net attendu > 0 : 146 ; dernier cycle 395.5 ms
- Rejets (moteur) : {'spread_below_threshold': 47191919, 'liquidity_below_min': 464601, 'negative_expected_net': 418207, 'borrow_bound_too_small': 53008, 'cycle_budget_exhausted': 48535, 'pool_quarantined': 6760}
- Enregistrements de la session : 418353 ; net attendu > 0 : 146 ; simulés (eth_call de la vraie tx) : 26 (ok 15, échec 11) ; étiquettes ghost N+1 : 4/14 positives
- Décisions : {'REJECTED': 418353} ; motifs de rejet : {'below_safety_margin': 116, 'negative_expected_net': 418207, 'p_lower_below_threshold': 126, 'price_impact': 16, 'reliability_not_demonstrated': 20, 'sim_below_estimate': 1, 'simulation_failed': 11, 'stale_data': 3}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52814592 | USDC→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→cbBTC→[aerodrome]→USDC | 72.995841 USDC | 0.047349 USDC | 0.000000 USDC | 0.006907 USDC | 0.040442 USDC (0.0372 €) | — | 5.54 | 0.037 (n=95) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.04<0.75) |
| 52814592 | cbBTC→[aerodrome]→USDC→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→cbBTC | 0.000881 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0370 €) | — | 5.56 | 0.037 (n=95) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.04<0.75) |
| 52814645 | USDC→[aerodrome_slipstream]→TITN→[aerodrome_slipstream]→USDC | 61.776813 USDC | 0.034377 USDC | 0.000000 USDC | 0.005411 USDC | 0.028966 USDC (0.0266 €) | — | 4.69 | 0.069 (n=21) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52814646 | USDC→[aerodrome_slipstream]→TITN→[aerodrome_slipstream]→USDC | 61.776813 USDC | 0.034377 USDC | 0.000000 USDC | 0.005411 USDC | 0.028966 USDC (0.0266 €) | — | 4.69 | 0.069 (n=21) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52814592 | cbBTC→[aerodrome]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.000587 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0204 €) | — | 4.60 | 0.037 (n=95) | REJECTED | p_lower_below_threshold(0.04<0.75) |
| 52814592 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[aerodrome]→USDC | 57.793470 USDC | 0.028980 USDC | 0.000000 USDC | 0.006907 USDC | 0.022073 USDC (0.0203 €) | — | 3.82 | 0.037 (n=95) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.04<0.75) |
| 52813880 | WETH→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.051297 WETH | 0.000011 WETH | 0.000000 WETH | 0.000003 WETH | 0.000008 WETH (0.0187 €) | — | 1.64 | 0.282 (n=68) | REJECTED | below_safety_margin(8432011708986<10259353737266), p_lower_below_threshold(0.28<0.75) |
| 52813880 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→USDC | 122.747609 USDC | 0.027572 USDC | 0.000000 USDC | 0.007287 USDC | 0.020285 USDC (0.0187 €) | — | 1.65 | 0.282 (n=68) | REJECTED | below_safety_margin(20285<24549), p_lower_below_threshold(0.28<0.75) |
| 52814555 | WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.047970 WETH | 0.000007 WETH | 0.000000 WETH | 0.000003 WETH | 0.000004 WETH (0.0090 €) | — | 0.85 | 0.287 (n=70) | REJECTED | below_safety_margin(4090544713030<9593931442744), p_lower_below_threshold(0.29<0.75) |
| 52814555 | WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.047970 WETH | 0.000007 WETH | 0.000000 WETH | 0.000003 WETH | 0.000004 WETH (0.0090 €) | — | 0.85 | 0.287 (n=70) | REJECTED | below_safety_margin(4090544713030<9593931442744), p_lower_below_threshold(0.29<0.75) |
| 52814555 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC | 114.321943 USDC | 0.017380 USDC | 0.000000 USDC | 0.007611 USDC | 0.009769 USDC (0.0090 €) | — | 0.85 | 0.287 (n=70) | REJECTED | below_safety_margin(9769<22864), p_lower_below_threshold(0.29<0.75) |
| 52814555 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC | 114.321943 USDC | 0.017380 USDC | 0.000000 USDC | 0.007611 USDC | 0.009769 USDC (0.0090 €) | — | 0.85 | 0.287 (n=70) | REJECTED | below_safety_margin(9769<22864), p_lower_below_threshold(0.29<0.75) |
| 52814227 | WETH→[uniswap_v2]→USDC→[pancakeswap_v3]→VIRTUAL→[uniswap_v2]→WETH | 0.019574 WETH | 0.000005 WETH | 0.000000 WETH | 0.000002 WETH | 0.000003 WETH (0.0065 €) | — | 1.49 | — (n=0) | REJECTED | below_safety_margin(2915509127906<3914741802686), reliability_not_demonstrated |
| 52814227 | USDC→[pancakeswap_v3]→VIRTUAL→[uniswap_v2]→WETH→[uniswap_v2]→USDC | 46.801913 USDC | 0.012810 USDC | 0.000000 USDC | 0.005796 USDC | 0.007014 USDC (0.0065 €) | — | 1.50 | — (n=0) | REJECTED | below_safety_margin(7014<9360), reliability_not_demonstrated |
| 52813880 | WETH→[aerodrome]→MET→[aerodrome]→USDC→[uniswap_v3]→WETH | 0.012282 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000003 WETH (0.0058 €) | 0.000003 WETH | 2.14 | 0.127 (n=60) | REJECTED | p_lower_below_threshold(0.13<0.75) |
| 52813880 | USDC→[uniswap_v3]→WETH→[aerodrome]→MET→[aerodrome]→USDC | 29.673821 USDC | 0.012939 USDC | 0.000000 USDC | 0.006620 USDC | 0.006319 USDC (0.0058 €) | 0.006319 USDC | 2.13 | 0.127 (n=60) | REJECTED | p_lower_below_threshold(0.13<0.75) |
| 52814469 | WETH→[aerodrome_slipstream]→uSOL→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→WETH | 0.027765 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0046 €) | — | 0.74 | 0.278 (n=69) | REJECTED | below_safety_margin(2067368269000<5552920803932), p_lower_below_threshold(0.28<0.75) |
| 52814469 | WETH→[aerodrome_slipstream]→uSOL→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→WETH | 0.027765 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0046 €) | — | 0.74 | 0.278 (n=69) | REJECTED | below_safety_margin(2067368269000<5552920803932), p_lower_below_threshold(0.28<0.75) |
| 52814469 | cbBTC→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→uSOL→[aerodrome_slipstream]→cbBTC | 0.001002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0045 €) | — | 0.60 | 0.278 (n=69) | REJECTED | below_safety_margin(6<20), p_lower_below_threshold(0.28<0.75) |
| 52814469 | cbBTC→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→uSOL→[aerodrome_slipstream]→cbBTC | 0.001002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0045 €) | — | 0.60 | 0.278 (n=69) | REJECTED | below_safety_margin(6<20), p_lower_below_threshold(0.28<0.75) |
| 52813898 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.004736 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0038 €) | 0.000002 WETH | 3.58 | 0.125 (n=108) | REJECTED | p_lower_below_threshold(0.13<0.75) |
| 52813898 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 11.347311 USDC | 0.011351 USDC | 0.000000 USDC | 0.007290 USDC | 0.004061 USDC (0.0037 €) | 0.004061 USDC | 3.58 | 0.125 (n=108) | REJECTED | p_lower_below_threshold(0.13<0.75) |
| 52814600 | WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.016000 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0029 €) | — | 0.82 | 0.287 (n=70) | REJECTED | below_safety_margin(1317303110103<3199950621146), p_lower_below_threshold(0.29<0.75) |
| 52814555 | WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.042866 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0029 €) | — | 0.31 | 0.109 (n=148) | REJECTED | below_safety_margin(1313647278628<8573245532532), p_lower_below_threshold(0.11<0.75) |
| 52814555 | WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.042866 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0029 €) | — | 0.31 | 0.109 (n=148) | REJECTED | below_safety_margin(1313647278628<8573245532532), p_lower_below_threshold(0.11<0.75) |

## Fiabilité et décision
- Observations ghost : 1284 ; taux observé 0.105 ; borne inférieure crédible (0.9) 0.095 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 9.5% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
