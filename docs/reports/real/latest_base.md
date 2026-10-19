# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-19T14:14:02+00:00 ; durée 70.63 min ; blocs 52812825 → 52814945 (2093 vus)

## Connexion
- Requêtes RPC : 26409 ; erreurs : 45 ; latence p50/p95 : 251.9/924.4 ms
- Rafraîchissements d'état : 2093 ; âge des données au dernier bloc : 2.28 s ; changements de frais LP observés (pools à frais dynamiques) : 6556
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 28442 ; cycles déclenchés par événement : 697 ; avance médiane sur le rafraîchissement multicall : 675 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,392.94 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 571 pools, 327 jetons, 21004 routes
- Par DEX : uniswap_v3 137, aerodrome 234 (quarantaine 2), aerodrome_slipstream 153, pancakeswap_v3 30, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 207 (rejetés 2) → 612 jetons ; pools candidats 3877 (énumérés 390, par paires 0), mesurés 574, sous le plancher de 10000.0 $ : 3 → gardés 571 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2419.85313, 'AERO': 0.782295, 'cbBTC': 82567.067054}
- Pools en quarantaine : 2 — aerodrome:fBOMB/AERO@0xbBf71A: simulation failed ×5 (model/chain mismatch) — until block 52815234; aerodrome:fBOMB/USDC@0xFf8e0b: simulation failed ×5 (model/chain mismatch) — until block 52815234

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 146,136,946 | 2,392.939200 | 52814945 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 34,762,672 | 1.299761 | 52814945 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 500 | 18,212,832 | 0.029195 | 52814945 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 16,951,090 | 103.090358 | 52814945 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| aerodrome_slipstream | WETH/cbBTC | 2515 | 13,461,398 | 0.029242 | 52814945 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,318,136 | 0.029257 | 52814945 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,844,105 | 0.000012 | 52814945 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 8,353,227 | 2,395.221110 | 52814945 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/USDC | 3000 | 8,295,332 | 2,392.929996 | 52814945 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | USDC/cbBTC | 364 | 7,818,805 | 0.000012 | 52814945 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | USDC/cbBTC | 592 | 7,553,330 | 0.000012 | 52814945 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome_slipstream | WETH/USDC | 758 | 7,209,318 | 2,395.405712 | 52814945 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,164,121 | 0.001654 | 52814945 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,333,409 | 0.029206 | 52814945 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | fBOMB/AERO | 10000 | 4,868,934 | 0.025988 | 52814945 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,782,747 | 0.802395 | 52814945 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,599,792 | 0.000273 | 52814945 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,390,661 | 2,395.957612 | 52814945 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,343,229 | 0.998770 | 52814945 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 4,000,611 | 33,933.944010 | 52814945 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDT | 442 | 3,921,980 | 2,398.270127 | 52814945 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome_slipstream | USDC/AERO | 10000 | 3,284,106 | 1.294576 | 52814945 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome | WETH/AERO | 10000 | 3,206,944 | 3,085.635759 | 52814945 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,851,737 | 0.000012 | 52814945 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,707,005 | 1.142013 | 52814945 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,651,821 | 406.457294 | 52814945 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | WETH/VVV | 2700 | 2,604,149 | 103.083125 | 52814945 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 2,342,848 | 0.000009 | 52814945 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | WETH/FAI | 10000 | 2,170,484 | 1,233,892.687804 | 52814945 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,059,117 | 1.238200 | 52814945 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | BNKR/WETH | 10000 | 2,038,002 | 0.000000 | 52814945 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,036,743 | 1.372638 | 52814945 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,770,590 | 0.000012 | 52814945 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,768,925 | 13,894.133082 | 52814945 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,757,930 | 16.019009 | 52814945 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| uniswap_v3 | XDP/USDC | 100 | 1,756,809 | 0.018449 | 52814945 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome | weETH_04c0/WETH | 500 | 1,730,292 | 1.105523 | 52814945 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome | fBOMB/USDC | 10000 | 1,714,013 | 0.020558 | 52814945 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| aerodrome | WETH/msETH (stable) | 500 | 1,656,133 | 2.306702 | 52814945 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | EURC/USDC | 79 | 1,611,505 | 1.121565 | 52814945 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| uniswap_v3 | WETH/AERO | 3000 | 1,584,710 | 3,106.294604 | 52814945 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,549,929 | 0.916350 | 52814945 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,456,180 | 0.827383 | 52814945 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,337,795 | 0.435482 | 52814945 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,310,527 | 0.000000 | 52814945 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,289,353 | 0.000273 | 52814945 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | WETH/cbBTC | 3000 | 1,279,076 | 0.029260 | 52814945 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,270,318 | 0.004581 | 52814945 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,268,623 | 23.125698 | 52814945 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| aerodrome | USDC/SEND | 3000 | 1,232,735 | 63.944488 | 52814945 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,193,550 | 35,148,301.060571 | 52814945 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,190,969 | 2,395.049478 | 52814945 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | WETH/WELL | 10000 | 1,190,762 | 1,094,950.313726 | 52814945 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome_slipstream | WETH/msETH | 500 | 1,138,980 | 1.131543 | 52814945 | `0x74F72788F4814D7fF3C49B44684aa98Eee140C0E` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,126,076 | 515,481.870232 | 52814945 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | USDC/NOCK | 3000 | 1,094,805 | 52.568814 | 52814945 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,076,782 | 15.534132 | 52814945 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome_slipstream | msUSD/USDC | 500 | 1,075,558 | 0.885402 | 52814945 | `0x7501bc8Bb51616F79bfA524E464fb7B41f0B10fB` |
| aerodrome | WETH/EDEL | 7000 | 1,049,248 | 89,591.202759 | 52814945 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,040,617 | 1.105811 | 52814945 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |

## Recherche d'opportunités
- Cycles : 2789 ; routes examinées : 58580156 ; candidats optimisés : 483326 ; net attendu > 0 : 162 ; dernier cycle 236.6 ms
- Rejets (moteur) : {'spread_below_threshold': 57346401, 'liquidity_below_min': 563974, 'negative_expected_net': 483164, 'pool_quarantined': 70720, 'borrow_bound_too_small': 65333, 'cycle_budget_exhausted': 50402}
- Enregistrements de la session : 483326 ; net attendu > 0 : 162 ; simulés (eth_call de la vraie tx) : 38 (ok 18, échec 20) ; étiquettes ghost N+1 : 7/19 positives
- Décisions : {'REJECTED': 483326} ; motifs de rejet : {'below_safety_margin': 118, 'negative_expected_net': 483164, 'p_lower_below_threshold': 142, 'price_impact': 22, 'reliability_not_demonstrated': 20, 'sim_below_estimate': 4, 'simulated_net_nonpositive': 3, 'simulation_failed': 20, 'stale_data': 3}

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
- Observations ghost : 1289 ; taux observé 0.107 ; borne inférieure crédible (0.9) 0.096 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 9.6% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
