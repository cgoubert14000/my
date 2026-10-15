# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-15T13:37:42+00:00 ; durée 9.11 min ; blocs 52640781 → 52641057 (247 vus)

## Connexion
- Requêtes RPC : 3303 ; erreurs : 53 ; latence p50/p95 : 189.4/1,587.3 ms
- Rafraîchissements d'état : 248 ; âge des données au dernier bloc : 1.51 s ; changements de frais LP observés (pools à frais dynamiques) : 1145
- Flux d'événements (WebSocket Swap/Sync) : non connecté ; événements appliqués : 0 ; cycles déclenchés par événement : 0 ; avance médiane sur le rafraîchissement multicall : — ms
- Gaz : base fee 0.005378 gwei ; prix ETH (pool le plus profond) : 2,337.46 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 570 pools, 326 jetons, 21328 routes
- Par DEX : uniswap_v3 136, aerodrome 235, aerodrome_slipstream 152, pancakeswap_v3 30, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 205 (rejetés 2) → 610 jetons ; pools candidats 3864 (énumérés 389, par paires 0), mesurés 572, sous le plancher de 10000.0 $ : 2 → gardés 570 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDC': 1.0, 'USDbC': 1.0, 'WETH': 2346.001193, 'AERO': 0.837627, 'cbBTC': 80168.530844}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 141,975,909 | 2,337.455384 | 52641057 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 43,987,396 | 1.189868 | 52641057 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 500 | 17,642,351 | 0.029154 | 52641057 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 15,519,843 | 104.123635 | 52641057 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 12,966,655 | 0.029162 | 52641057 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,218,966 | 0.029149 | 52641057 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,567,433 | 0.000012 | 52641057 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 8,833,185 | 2,341.928571 | 52641057 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/USDC | 3000 | 8,783,421 | 2,337.604834 | 52641057 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | USDC/cbBTC | 352 | 7,901,158 | 0.000012 | 52641057 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,000,301 | 0.001650 | 52641057 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | WETH/USDC | 594 | 6,721,844 | 2,341.498657 | 52641057 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | USDC/cbBTC | 544 | 6,260,072 | 0.000012 | 52641057 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome | fBOMB/AERO | 10000 | 5,133,151 | 0.026334 | 52641057 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,114,827 | 0.029159 | 52641057 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,497,890 | 0.000274 | 52641057 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,395,897 | 0.802389 | 52641057 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,218,210 | 0.999906 | 52641057 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,212,193 | 2,341.267029 | 52641057 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | WETH/KTA | 3000 | 3,848,303 | 34,992.226690 | 52641057 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | USDC/AERO | 10000 | 3,766,922 | 1.192763 | 52641057 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome | WETH/AERO | 10000 | 3,387,892 | 2,805.437708 | 52641057 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,810,638 | 0.000012 | 52641057 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/VVV | 2766 | 2,520,592 | 104.143605 | 52641057 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,441,877 | 1.141649 | 52641057 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 2,331,038 | 0.000010 | 52641057 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,226,145 | 406.368279 | 52641057 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | WETH/FAI | 10000 | 2,118,655 | 1,235,641.383305 | 52641057 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,112,476 | 1.194801 | 52641057 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,008,820 | 1.403288 | 52641057 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| aerodrome_slipstream | WETH/USDT | 415 | 2,007,669 | 2,345.858173 | 52641057 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,937,202 | 0.000000 | 52641057 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome | fBOMB/USDC | 10000 | 1,846,233 | 0.022330 | 52641057 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,766,716 | 0.916541 | 52641057 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| uniswap_v3 | XDP/USDC | 100 | 1,766,563 | 0.018582 | 52641057 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,746,495 | 0.000012 | 52641057 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,678,745 | 15.840377 | 52641057 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | WETH/msETH (stable) | 500 | 1,657,153 | 2.300422 | 52641057 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,533,688 | 13,920.326191 | 52641057 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome_slipstream | WETH/MORPHO | 2736 | 1,523,540 | 1,025.502915 | 52641057 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| uniswap_v3 | WETH/AERO | 3000 | 1,460,012 | 2,784.516140 | 52641057 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,459,038 | 0.831422 | 52641057 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome | weETH_04c0/WETH | 500 | 1,445,226 | 1.105502 | 52641057 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome_slipstream | WETH/msETH | 500 | 1,358,051 | 1.130318 | 52641057 | `0x74F72788F4814D7fF3C49B44684aa98Eee140C0E` |
| uniswap_v3 | DRB/WETH | 10000 | 1,315,387 | 0.000000 | 52641057 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome_slipstream | WETH/AERO | 3068 | 1,310,099 | 2,786.454093 | 52641057 | `0x82321f3BEB69f503380D6B233857d5C43562e2D0` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,263,778 | 0.004688 | 52641057 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,260,900 | 23.189943 | 52641057 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,260,554 | 0.000274 | 52641057 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome_slipstream | EURC/USDC | 82 | 1,246,197 | 1.121433 | 52641057 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| aerodrome | USDC/SEND | 3000 | 1,245,639 | 62.626509 | 52641057 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,186,852 | 2,341.724369 | 52641057 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,158,607 | 1.105590 | 52641057 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |
| uniswap_v3 | WETH/doginme | 10000 | 1,156,944 | 35,579,061.887859 | 52641057 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | WETH/cbBTC | 3000 | 1,127,296 | 0.029146 | 52641057 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| aerodrome | WETH/WELL | 10000 | 1,118,933 | 1,183,375.921558 | 52641057 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,110,226 | 0.434796 | 52641057 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,107,189 | 506,613.317111 | 52641057 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,106,583 | 14.479448 | 52641057 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | WETH/EDEL | 7000 | 1,102,753 | 78,181.279541 | 52641057 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |

## Recherche d'opportunités
- Cycles : 247 ; routes examinées : 5268016 ; candidats optimisés : 28686 ; net attendu > 0 : 31 ; dernier cycle 324.1 ms
- Rejets (moteur) : {'spread_below_threshold': 5187133, 'liquidity_below_min': 45687, 'negative_expected_net': 28655, 'borrow_bound_too_small': 5345, 'unquotable': 728, 'cycle_budget_exhausted': 437}
- Enregistrements de la session : 28686 ; net attendu > 0 : 31 ; simulés (eth_call de la vraie tx) : 4 (ok 4, échec 0) ; étiquettes ghost N+1 : 0/4 positives
- Décisions : {'REJECTED': 28686} ; motifs de rejet : {'below_safety_margin': 26, 'negative_expected_net': 28655, 'p_lower_below_threshold': 6, 'reliability_not_demonstrated': 25, 'stale_data': 5}

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
| 52641019 | WETH→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.038178 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0043 €) | — | 0.52 | 0.104 (n=35) | REJECTED | below_safety_margin(2004364194393<7635692018731), p_lower_below_threshold(0.10<0.75) |
| 52641019 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→USDC | 88.799593 USDC | 0.012369 USDC | 0.000000 USDC | 0.007718 USDC | 0.004651 USDC (0.0043 €) | — | 0.52 | 0.104 (n=35) | REJECTED | below_safety_margin(4651<17759), p_lower_below_threshold(0.10<0.75) |
| 52641019 | WETH→[aerodrome_slipstream]→LCAP→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.026169 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0038 €) | — | 0.67 | 0.310 (n=23) | REJECTED | below_safety_margin(1758390076820<5233797759662), reliability_not_demonstrated |
| 52641019 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→LCAP→[aerodrome_slipstream]→USDC | 60.597998 USDC | 0.011429 USDC | 0.000000 USDC | 0.007351 USDC | 0.004078 USDC (0.0038 €) | — | 0.67 | 0.310 (n=23) | REJECTED | below_safety_margin(4078<12119), reliability_not_demonstrated |
| 52641019 | WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.016336 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0026 €) | — | 0.74 | 0.310 (n=23) | REJECTED | below_safety_margin(1209972767976<3267261584111), reliability_not_demonstrated |
| 52641019 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC | 37.747988 USDC | 0.010152 USDC | 0.000000 USDC | 0.007351 USDC | 0.002801 USDC (0.0026 €) | — | 0.74 | 0.310 (n=23) | REJECTED | below_safety_margin(2801<7549), reliability_not_demonstrated |
| 52641019 | WETH→[aerodrome]→SPARKLET→[aerodrome]→USDC→[uniswap_v3]→WETH | 0.003222 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0024 €) | 0.000001 WETH | 3.47 | 0.012 (n=24) | REJECTED | reliability_not_demonstrated |
| 52641019 | USDC→[uniswap_v3]→WETH→[aerodrome]→SPARKLET→[aerodrome]→USDC | 7.413496 USDC | 0.009274 USDC | 0.000000 USDC | 0.006684 USDC | 0.002590 USDC (0.0024 €) | 0.002590 USDC | 3.49 | 0.012 (n=24) | REJECTED | reliability_not_demonstrated |
| 52641019 | WETH→[aerodrome]→SPARKLET→[aerodrome]→USDC→[pancakeswap_v3]→WETH | 0.003037 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0015 €) | 0.000001 WETH | 2.28 | 0.001 (n=9) | REJECTED | reliability_not_demonstrated |
| 52641019 | USDC→[pancakeswap_v3]→WETH→[aerodrome]→SPARKLET→[aerodrome]→USDC | 7.053185 USDC | 0.008282 USDC | 0.000000 USDC | 0.006684 USDC | 0.001598 USDC (0.0015 €) | — | 2.27 | 0.001 (n=9) | REJECTED | reliability_not_demonstrated |
| 52641019 | WETH→[uniswap_v3]→USDT→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.014608 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0009 €) | — | 0.29 | 0.104 (n=35) | REJECTED | below_safety_margin(416451257691<2921645741342), p_lower_below_threshold(0.10<0.75) |
| 52641019 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→USDT→[pancakeswap_v3]→USDC | 33.569628 USDC | 0.008300 USDC | 0.000000 USDC | 0.007351 USDC | 0.000949 USDC (0.0009 €) | — | 0.28 | 0.104 (n=35) | REJECTED | below_safety_margin(949<6713), p_lower_below_threshold(0.10<0.75) |
| 52641018 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[sushiswap_v3]→USDC | 63.256891 USDC | 0.008253 USDC | 0.000000 USDC | 0.007320 USDC | 0.000933 USDC (0.0009 €) | — | 0.15 | 0.104 (n=35) | REJECTED | below_safety_margin(933<12651), p_lower_below_threshold(0.10<0.75) |
| 52641018 | WETH→[sushiswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.026851 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0008 €) | — | 0.14 | 0.104 (n=35) | REJECTED | below_safety_margin(382841664085<5370260454171), p_lower_below_threshold(0.10<0.75) |
| 52640811 | WETH→[uniswap_v2]→wIRON→[aerodrome]→USDC→[pancakeswap_v3]→WETH | 0.004398 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0003 €) | — | 0.33 | — (n=0) | REJECTED | below_safety_margin(144466124251<879519213685), stale_data(4302ms>4000.0), reliability_not_demonstrated |

## Fiabilité et décision
- Observations ghost : 282 ; taux observé 0.184 ; borne inférieure crédible (0.9) 0.156 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 15.6% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
