# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-15T13:43:53+00:00 ; durée 15.28 min ; blocs 52640781 → 52641240 (413 vus)

## Connexion
- Requêtes RPC : 5467 ; erreurs : 53 ; latence p50/p95 : 249.7/1,556.1 ms
- Rafraîchissements d'état : 413 ; âge des données au dernier bloc : 5.64 s ; changements de frais LP observés (pools à frais dynamiques) : 1859
- Flux d'événements (WebSocket Swap/Sync) : non connecté ; événements appliqués : 0 ; cycles déclenchés par événement : 0 ; avance médiane sur le rafraîchissement multicall : — ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,346.92 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 570 pools, 326 jetons, 21328 routes
- Par DEX : uniswap_v3 136, aerodrome 235, aerodrome_slipstream 152, pancakeswap_v3 30, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 205 (rejetés 2) → 610 jetons ; pools candidats 3864 (énumérés 389, par paires 0), mesurés 572, sous le plancher de 10000.0 $ : 2 → gardés 570 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDC': 1.0, 'USDbC': 1.0, 'WETH': 2346.001193, 'AERO': 0.837627, 'cbBTC': 80168.530844}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 142,400,363 | 2,346.919416 | 52641241 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 44,125,296 | 1.182445 | 52641241 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 500 | 17,706,111 | 0.029173 | 52641241 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 15,652,555 | 103.196071 | 52641241 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 13,006,397 | 0.029162 | 52641241 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,258,243 | 0.029149 | 52641241 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,590,660 | 0.000012 | 52641241 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 8,861,123 | 2,352.427162 | 52641241 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/USDC | 3000 | 8,801,185 | 2,346.953585 | 52641241 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | USDC/cbBTC | 386 | 7,912,925 | 0.000012 | 52641241 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,024,643 | 0.001651 | 52641241 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | WETH/USDC | 1041 | 6,742,630 | 2,352.842420 | 52641241 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | USDC/cbBTC | 600 | 6,283,039 | 0.000012 | 52641241 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome | fBOMB/AERO | 10000 | 5,147,623 | 0.026334 | 52641241 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,132,700 | 0.029177 | 52641241 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,516,101 | 0.000274 | 52641241 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,413,696 | 0.802389 | 52641241 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,232,410 | 0.999906 | 52641241 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,225,517 | 2,352.710184 | 52641241 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | WETH/KTA | 3000 | 3,863,884 | 34,992.226690 | 52641241 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/AERO | 10000 | 3,405,393 | 2,801.399763 | 52641241 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,817,234 | 0.000012 | 52641241 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,548,423 | 406.433037 | 52641241 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | WETH/VVV | 2841 | 2,522,786 | 103.192433 | 52641241 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,451,764 | 1.141649 | 52641241 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| aerodrome_slipstream | AERO/cbBTC | 2700 | 2,422,656 | 0.000011 | 52641241 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | WETH/FAI | 10000 | 2,130,639 | 1,231,694.328979 | 52641241 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,112,870 | 1.194579 | 52641241 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,008,820 | 1.403288 | 52641241 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,945,472 | 0.000000 | 52641241 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome_slipstream | WETH/USDT | 499 | 1,931,256 | 2,356.670167 | 52641241 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,905,039 | 15.838009 | 52641241 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | fBOMB/USDC | 10000 | 1,845,673 | 0.022316 | 52641241 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,773,869 | 0.916541 | 52641241 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| uniswap_v3 | XDP/USDC | 100 | 1,767,648 | 0.018603 | 52641241 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,750,370 | 0.000012 | 52641241 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,737,986 | 13,923.698659 | 52641241 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome_slipstream | USDC/AERO | 10000 | 1,703,436 | 1.190821 | 52641241 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome | WETH/msETH (stable) | 500 | 1,663,863 | 2.300422 | 52641241 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | WETH/AERO | 3000 | 1,466,998 | 2,781.732267 | 52641241 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,459,038 | 0.831422 | 52641241 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome | weETH_04c0/WETH | 500 | 1,451,077 | 1.105502 | 52641241 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome_slipstream | WETH/msETH | 500 | 1,359,574 | 1.130357 | 52641241 | `0x74F72788F4814D7fF3C49B44684aa98Eee140C0E` |
| uniswap_v3 | DRB/WETH | 10000 | 1,325,251 | 0.000000 | 52641241 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome_slipstream | WETH/AERO | 3052 | 1,317,002 | 2,781.763062 | 52641241 | `0x82321f3BEB69f503380D6B233857d5C43562e2D0` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,273,381 | 23.175114 | 52641241 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,268,895 | 0.004688 | 52641241 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,265,658 | 0.000274 | 52641241 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome_slipstream | EURC/USDC | 70 | 1,246,005 | 1.121142 | 52641241 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| aerodrome | USDC/SEND | 3000 | 1,245,639 | 62.626509 | 52641241 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,190,551 | 2,352.720793 | 52641241 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,163,298 | 1.105590 | 52641241 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |
| uniswap_v3 | WETH/doginme | 10000 | 1,163,269 | 35,429,651.925378 | 52641241 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | WETH/cbBTC | 3000 | 1,131,475 | 0.029146 | 52641241 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| aerodrome | WETH/WELL | 10000 | 1,122,973 | 1,184,409.541937 | 52641241 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,111,672 | 506,613.317111 | 52641241 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,110,159 | 0.434757 | 52641241 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| aerodrome | WETH/EDEL | 7000 | 1,107,305 | 78,169.088886 | 52641241 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,105,504 | 14.515202 | 52641241 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | USDC/NOCK | 3000 | 1,101,387 | 51.953270 | 52641241 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |

## Recherche d'opportunités
- Cycles : 412 ; routes examinées : 8787136 ; candidats optimisés : 52138 ; net attendu > 0 : 42 ; dernier cycle 262.6 ms
- Rejets (moteur) : {'spread_below_threshold': 8647833, 'liquidity_below_min': 76145, 'negative_expected_net': 52096, 'borrow_bound_too_small': 9470, 'unquotable': 1058, 'cycle_budget_exhausted': 492}
- Enregistrements de la session : 52138 ; net attendu > 0 : 42 ; simulés (eth_call de la vraie tx) : 4 (ok 4, échec 0) ; étiquettes ghost N+1 : 0/4 positives
- Décisions : {'REJECTED': 52138} ; motifs de rejet : {'below_safety_margin': 37, 'negative_expected_net': 52096, 'p_lower_below_threshold': 15, 'reliability_not_demonstrated': 27, 'stale_data': 5}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
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
| 52641019 | WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.016336 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0026 €) | — | 0.74 | 0.310 (n=23) | REJECTED | below_safety_margin(1209972767976<3267261584111), reliability_not_demonstrated |
| 52641019 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC | 37.747988 USDC | 0.010152 USDC | 0.000000 USDC | 0.007351 USDC | 0.002801 USDC (0.0026 €) | — | 0.74 | 0.310 (n=23) | REJECTED | below_safety_margin(2801<7549), reliability_not_demonstrated |
| 52641019 | WETH→[aerodrome]→SPARKLET→[aerodrome]→USDC→[uniswap_v3]→WETH | 0.003222 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0024 €) | 0.000001 WETH | 3.47 | 0.012 (n=24) | REJECTED | reliability_not_demonstrated |
| 52641019 | USDC→[uniswap_v3]→WETH→[aerodrome]→SPARKLET→[aerodrome]→USDC | 7.413496 USDC | 0.009274 USDC | 0.000000 USDC | 0.006684 USDC | 0.002590 USDC (0.0024 €) | 0.002590 USDC | 3.49 | 0.012 (n=24) | REJECTED | reliability_not_demonstrated |
| 52641126 | USDC→[aerodrome_slipstream]→EURC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 45.271312 USDC | 0.009171 USDC | 0.000000 USDC | 0.007245 USDC | 0.001926 USDC (0.0018 €) | — | 0.43 | 0.104 (n=35) | REJECTED | below_safety_margin(1926<9054), p_lower_below_threshold(0.10<0.75) |
| 52641126 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→EURC→[pancakeswap_v3]→WETH | 0.019319 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0017 €) | — | 0.42 | 0.104 (n=35) | REJECTED | below_safety_margin(810510775496<3863894293304), p_lower_below_threshold(0.10<0.75) |
| 52641019 | WETH→[aerodrome]→SPARKLET→[aerodrome]→USDC→[pancakeswap_v3]→WETH | 0.003037 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0015 €) | 0.000001 WETH | 2.28 | 0.001 (n=9) | REJECTED | reliability_not_demonstrated |

## Fiabilité et décision
- Observations ghost : 282 ; taux observé 0.184 ; borne inférieure crédible (0.9) 0.156 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 15.6% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
