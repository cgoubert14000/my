# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-15T13:50:03+00:00 ; durée 21.46 min ; blocs 52640781 → 52641427 (577 vus)

## Connexion
- Requêtes RPC : 7643 ; erreurs : 100 ; latence p50/p95 : 171.7/1,678.8 ms
- Rafraîchissements d'état : 578 ; âge des données au dernier bloc : 2.22 s ; changements de frais LP observés (pools à frais dynamiques) : 2678
- Flux d'événements (WebSocket Swap/Sync) : non connecté ; événements appliqués : 0 ; cycles déclenchés par événement : 0 ; avance médiane sur le rafraîchissement multicall : — ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,345.30 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 570 pools, 326 jetons, 21328 routes
- Par DEX : uniswap_v3 136, aerodrome 235, aerodrome_slipstream 152, pancakeswap_v3 30, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 205 (rejetés 2) → 610 jetons ; pools candidats 3864 (énumérés 389, par paires 0), mesurés 572, sous le plancher de 10000.0 $ : 2 → gardés 570 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDC': 1.0, 'USDbC': 1.0, 'WETH': 2346.001193, 'AERO': 0.837627, 'cbBTC': 80168.530844}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 142,297,477 | 2,345.295613 | 52641427 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 44,076,352 | 1.185072 | 52641427 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 500 | 17,701,217 | 0.029162 | 52641427 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 15,671,725 | 102.801373 | 52641427 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 11,528,510 | 0.029162 | 52641427 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,252,355 | 0.029149 | 52641427 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,568,826 | 0.000012 | 52641427 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 8,857,372 | 2,342.128145 | 52641427 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/USDC | 3000 | 8,798,139 | 2,345.215445 | 52641427 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | USDC/cbBTC | 372 | 7,911,936 | 0.000012 | 52641427 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,024,171 | 0.001652 | 52641427 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | WETH/USDC | 877 | 6,909,201 | 2,342.037644 | 52641427 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | USDC/cbBTC | 600 | 6,280,986 | 0.000012 | 52641427 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome | fBOMB/AERO | 10000 | 5,140,706 | 0.026334 | 52641427 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,129,570 | 0.029162 | 52641427 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,512,976 | 0.000274 | 52641427 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,410,642 | 0.802389 | 52641427 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,231,141 | 0.999904 | 52641427 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,223,210 | 2,341.193221 | 52641427 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | WETH/KTA | 3000 | 3,861,211 | 34,992.226690 | 52641427 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | USDC/AERO | 10000 | 3,710,792 | 1.189966 | 52641427 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome | WETH/AERO | 10000 | 3,400,418 | 2,798.755264 | 52641427 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,816,708 | 0.000012 | 52641427 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/VVV | 2793 | 2,525,547 | 102.704001 | 52641427 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,484,789 | 407.184059 | 52641427 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,450,067 | 1.141649 | 52641427 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| aerodrome_slipstream | AERO/cbBTC | 2700 | 2,426,748 | 0.000011 | 52641427 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | WETH/FAI | 10000 | 2,129,770 | 1,230,994.774157 | 52641427 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,112,870 | 1.194579 | 52641427 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,008,820 | 1.403288 | 52641427 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| aerodrome_slipstream | WETH/USDT | 469 | 1,998,210 | 2,346.224602 | 52641427 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,944,122 | 0.000000 | 52641427 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,856,017 | 15.828454 | 52641427 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | fBOMB/USDC | 10000 | 1,845,238 | 0.022306 | 52641427 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,772,642 | 0.916541 | 52641427 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| uniswap_v3 | XDP/USDC | 100 | 1,763,219 | 0.018520 | 52641427 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,749,790 | 0.000012 | 52641427 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,737,173 | 13,944.692604 | 52641427 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/msETH (stable) | 500 | 1,662,711 | 2.300422 | 52641427 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | WETH/MORPHO | 2733 | 1,508,443 | 1,020.429726 | 52641427 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| uniswap_v3 | WETH/AERO | 3000 | 1,465,248 | 2,778.439520 | 52641427 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,459,038 | 0.831422 | 52641427 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome | weETH_04c0/WETH | 500 | 1,450,074 | 1.105502 | 52641427 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome_slipstream | WETH/msETH | 500 | 1,356,121 | 1.130368 | 52641427 | `0x74F72788F4814D7fF3C49B44684aa98Eee140C0E` |
| uniswap_v3 | DRB/WETH | 10000 | 1,324,334 | 0.000000 | 52641427 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome_slipstream | WETH/AERO | 3028 | 1,315,029 | 2,778.837824 | 52641427 | `0x82321f3BEB69f503380D6B233857d5C43562e2D0` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,272,527 | 23.175119 | 52641427 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,268,017 | 0.004688 | 52641427 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,264,783 | 0.000274 | 52641427 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome_slipstream | EURC/USDC | 73 | 1,245,867 | 1.121005 | 52641427 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| aerodrome | USDC/SEND | 3000 | 1,245,639 | 62.626509 | 52641427 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,190,049 | 2,342.372750 | 52641427 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,162,494 | 1.105591 | 52641427 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |
| uniswap_v3 | WETH/doginme | 10000 | 1,162,464 | 35,429,651.925378 | 52641427 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | WETH/cbBTC | 3000 | 1,130,914 | 0.029146 | 52641427 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| aerodrome | WETH/WELL | 10000 | 1,122,196 | 1,184,409.541937 | 52641427 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,110,903 | 506,613.317111 | 52641427 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,110,159 | 0.434757 | 52641427 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| aerodrome | WETH/EDEL | 7000 | 1,106,552 | 78,167.162360 | 52641427 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,103,509 | 14.581710 | 52641427 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |

## Recherche d'opportunités
- Cycles : 577 ; routes examinées : 12306256 ; candidats optimisés : 68653 ; net attendu > 0 : 52 ; dernier cycle 251.5 ms
- Rejets (moteur) : {'spread_below_threshold': 12117826, 'liquidity_below_min': 105782, 'negative_expected_net': 68601, 'borrow_bound_too_small': 11455, 'unquotable': 2048, 'cycle_budget_exhausted': 492}
- Enregistrements de la session : 68653 ; net attendu > 0 : 52 ; simulés (eth_call de la vraie tx) : 4 (ok 4, échec 0) ; étiquettes ghost N+1 : 0/4 positives
- Décisions : {'REJECTED': 68653} ; motifs de rejet : {'below_safety_margin': 47, 'negative_expected_net': 68601, 'p_lower_below_threshold': 23, 'reliability_not_demonstrated': 29, 'stale_data': 5}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52641328 | WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.434863 WETH | 0.000053 WETH | 0.000000 WETH | 0.000003 WETH | 0.000049 WETH (0.1066 €) | — | 1.14 | 0.104 (n=35) | REJECTED | below_safety_margin(49359140518453<86972633703641), p_lower_below_threshold(0.10<0.75) |
| 52641328 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC | 1,017.802287 USDC | 0.123214 USDC | 0.000000 USDC | 0.007491 USDC | 0.115723 USDC (0.1065 €) | — | 1.14 | 0.104 (n=35) | REJECTED | below_safety_margin(115723<203560), p_lower_below_threshold(0.10<0.75) |
| 52641328 | WETH→[aerodrome_slipstream]→USDT→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.287475 WETH | 0.000025 WETH | 0.000000 WETH | 0.000003 WETH | 0.000021 WETH (0.0464 €) | — | 0.75 | 0.104 (n=35) | REJECTED | below_safety_margin(21468077853657<57494906879717), p_lower_below_threshold(0.10<0.75) |
| 52641328 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDT→[uniswap_v3]→USDC | 671.825063 USDC | 0.057816 USDC | 0.000000 USDC | 0.007491 USDC | 0.050325 USDC (0.0463 €) | — | 0.75 | 0.104 (n=35) | REJECTED | below_safety_margin(50325<134365), p_lower_below_threshold(0.10<0.75) |
| 52641328 | WETH→[aerodrome_slipstream]→USDT→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.184426 WETH | 0.000017 WETH | 0.000000 WETH | 0.000003 WETH | 0.000013 WETH (0.0290 €) | — | 0.73 | 0.104 (n=35) | REJECTED | below_safety_margin(13413924531529<36885104560863), p_lower_below_threshold(0.10<0.75) |
| 52641328 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDT→[pancakeswap_v3]→USDC | 434.062008 USDC | 0.039288 USDC | 0.000000 USDC | 0.007847 USDC | 0.031441 USDC (0.0289 €) | — | 0.72 | 0.104 (n=35) | REJECTED | below_safety_margin(31441<86812), p_lower_below_threshold(0.10<0.75) |
| 52641018 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.167926 WETH | 0.000012 WETH | 0.000000 WETH | 0.000003 WETH | 0.000009 WETH (0.0194 €) | — | 0.54 | 0.003 (n=2) | REJECTED | below_safety_margin(9011403854194<33585138149872), reliability_not_demonstrated |
| 52641018 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.004263 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0192 €) | — | 0.61 | 0.003 (n=2) | REJECTED | below_safety_margin(26<85), reliability_not_demonstrated |
| 52641018 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 414.668097 USDC | 0.028481 USDC | 0.000000 USDC | 0.007685 USDC | 0.020796 USDC (0.0191 €) | — | 0.50 | 0.003 (n=2) | REJECTED | below_safety_margin(20796<82933), reliability_not_demonstrated |
| 52641019 | WETH→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.044511 WETH | 0.000009 WETH | 0.000000 WETH | 0.000003 WETH | 0.000006 WETH (0.0132 €) | — | 1.38 | 0.310 (n=23) | REJECTED | below_safety_margin(6150945490636<8902292430630), reliability_not_demonstrated |
| 52641019 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→USDC | 103.137548 USDC | 0.021669 USDC | 0.000000 USDC | 0.007351 USDC | 0.014318 USDC (0.0132 €) | — | 1.39 | 0.310 (n=23) | REJECTED | below_safety_margin(14318<20627), reliability_not_demonstrated |
| 52640995 | USDC→[uniswap_v3]→OWB→[aerodrome]→USDC | 11.977654 USDC | 0.011818 USDC | 0.000000 USDC | 0.005158 USDC | 0.006660 USDC (0.0061 €) | 0.006660 USDC | 5.56 | 0.003 (n=2) | REJECTED | reliability_not_demonstrated |
| 52641018 | WETH→[uniswap_v3]→DIEM→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.028773 WETH | 0.000006 WETH | 0.000000 WETH | 0.000003 WETH | 0.000003 WETH (0.0055 €) | — | 0.89 | 0.310 (n=23) | REJECTED | below_safety_margin(2574158644465<5754692154494), reliability_not_demonstrated |
| 52641018 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→DIEM→[aerodrome_slipstream]→USDC | 66.624929 USDC | 0.013303 USDC | 0.000000 USDC | 0.007320 USDC | 0.005983 USDC (0.0055 €) | — | 0.90 | 0.310 (n=23) | REJECTED | below_safety_margin(5983<13324), reliability_not_demonstrated |
| 52641019 | WETH→[uniswap_v3]→DIEM→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.026654 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0048 €) | — | 0.84 | 0.310 (n=23) | REJECTED | below_safety_margin(2235872817837<5330742620963), reliability_not_demonstrated |
| 52641019 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→DIEM→[aerodrome_slipstream]→USDC | 61.764309 USDC | 0.012542 USDC | 0.000000 USDC | 0.007351 USDC | 0.005191 USDC (0.0048 €) | — | 0.84 | 0.310 (n=23) | REJECTED | below_safety_margin(5191<12352), reliability_not_demonstrated |
| 52641126 | USDC→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 41.064979 USDC | 0.011961 USDC | 0.000000 USDC | 0.007245 USDC | 0.004716 USDC (0.0043 €) | — | 1.15 | 0.104 (n=35) | REJECTED | below_safety_margin(4716<8212), p_lower_below_threshold(0.10<0.75) |
| 52641019 | WETH→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.038178 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0043 €) | — | 0.52 | 0.104 (n=35) | REJECTED | below_safety_margin(2004364194393<7635692018731), p_lower_below_threshold(0.10<0.75) |
| 52641126 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→WETH | 0.017610 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0043 €) | — | 1.13 | 0.104 (n=35) | REJECTED | below_safety_margin(1997119779451<3521942761276), p_lower_below_threshold(0.10<0.75) |
| 52641019 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→USDC | 88.799593 USDC | 0.012369 USDC | 0.000000 USDC | 0.007718 USDC | 0.004651 USDC (0.0043 €) | — | 0.52 | 0.104 (n=35) | REJECTED | below_safety_margin(4651<17759), p_lower_below_threshold(0.10<0.75) |
| 52641019 | WETH→[aerodrome_slipstream]→LCAP→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.026169 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0038 €) | — | 0.67 | 0.310 (n=23) | REJECTED | below_safety_margin(1758390076820<5233797759662), reliability_not_demonstrated |
| 52641019 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→LCAP→[aerodrome_slipstream]→USDC | 60.597998 USDC | 0.011429 USDC | 0.000000 USDC | 0.007351 USDC | 0.004078 USDC (0.0038 €) | — | 0.67 | 0.310 (n=23) | REJECTED | below_safety_margin(4078<12119), reliability_not_demonstrated |
| 52641126 | USDC→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 37.535334 USDC | 0.010584 USDC | 0.000000 USDC | 0.007245 USDC | 0.003339 USDC (0.0031 €) | — | 0.89 | 0.310 (n=23) | REJECTED | below_safety_margin(3339<7507), reliability_not_demonstrated |
| 52641126 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→WETH | 0.015948 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0030 €) | — | 0.89 | 0.310 (n=23) | REJECTED | below_safety_margin(1411748570738<3189584142114), reliability_not_demonstrated |
| 52641328 | WETH→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.034486 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0029 €) | — | 0.38 | 0.104 (n=35) | REJECTED | below_safety_margin(1321620031215<6897235651035), p_lower_below_threshold(0.10<0.75) |

## Fiabilité et décision
- Observations ghost : 282 ; taux observé 0.184 ; borne inférieure crédible (0.9) 0.156 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 15.6% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
