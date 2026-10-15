# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-15T13:56:10+00:00 ; durée 27.57 min ; blocs 52640781 → 52641610 (742 vus)

## Connexion
- Requêtes RPC : 9765 ; erreurs : 108 ; latence p50/p95 : 130.2/1,723.3 ms
- Rafraîchissements d'état : 742 ; âge des données au dernier bloc : 2.76 s ; changements de frais LP observés (pools à frais dynamiques) : 3654
- Flux d'événements (WebSocket Swap/Sync) : non connecté ; événements appliqués : 0 ; cycles déclenchés par événement : 0 ; avance médiane sur le rafraîchissement multicall : — ms
- Gaz : base fee 0.007146 gwei ; prix ETH (pool le plus profond) : 2,330.62 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 570 pools, 326 jetons, 21328 routes
- Par DEX : uniswap_v3 136, aerodrome 235, aerodrome_slipstream 152, pancakeswap_v3 30, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 205 (rejetés 2) → 610 jetons ; pools candidats 3864 (énumérés 389, par paires 0), mesurés 572, sous le plancher de 10000.0 $ : 2 → gardés 570 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDC': 1.0, 'USDbC': 1.0, 'WETH': 2346.001193, 'AERO': 0.837627, 'cbBTC': 80168.530844}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 141,483,560 | 2,330.619396 | 52641610 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 44,064,150 | 1.185755 | 52641610 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 500 | 17,589,747 | 0.029177 | 52641610 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 15,551,816 | 103.090779 | 52641610 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 11,290,028 | 0.029162 | 52641610 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,186,561 | 0.029149 | 52641610 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,534,646 | 0.000012 | 52641610 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 8,791,224 | 2,336.158233 | 52641610 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/USDC | 3000 | 8,770,569 | 2,330.597174 | 52641610 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | USDC/cbBTC | 350 | 7,888,181 | 0.000012 | 52641610 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,974,345 | 0.001654 | 52641610 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | WETH/USDC | 564 | 6,726,003 | 2,335.576670 | 52641610 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | USDC/cbBTC | 508 | 6,251,570 | 0.000012 | 52641610 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome | fBOMB/AERO | 10000 | 5,139,799 | 0.026341 | 52641610 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,096,965 | 0.029185 | 52641610 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,484,740 | 0.000274 | 52641610 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,383,041 | 0.802389 | 52641610 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome_slipstream | cbBTC/LBTC | 202 | 4,202,548 | 0.999898 | 52641610 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,201,988 | 2,335.199127 | 52641610 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | WETH/KTA | 3000 | 3,839,417 | 34,949.071798 | 52641610 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/AERO | 10000 | 3,388,806 | 2,790.254955 | 52641610 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | USDC/AERO | 10000 | 3,289,815 | 1.189966 | 52641610 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,804,434 | 0.000013 | 52641610 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/VVV | 2784 | 2,506,571 | 103.068584 | 52641610 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,480,232 | 407.543193 | 52641610 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,434,736 | 1.141648 | 52641610 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| aerodrome_slipstream | AERO/cbBTC | 2700 | 2,415,574 | 0.000011 | 52641610 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/MORPHO | 2706 | 2,174,667 | 1,019.906733 | 52641610 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome | WETH/FAI | 10000 | 2,121,200 | 1,225,478.942149 | 52641610 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,112,870 | 1.194579 | 52641610 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,008,820 | 1.403288 | 52641610 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| aerodrome_slipstream | WETH/USDT | 412 | 1,987,471 | 2,340.254101 | 52641610 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,932,372 | 0.000000 | 52641610 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome | fBOMB/USDC | 10000 | 1,845,444 | 0.022311 | 52641610 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,761,549 | 0.916541 | 52641610 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| uniswap_v3 | XDP/USDC | 100 | 1,754,968 | 0.018368 | 52641610 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,741,823 | 0.000012 | 52641610 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,675,352 | 15.804207 | 52641610 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | WETH/msETH (stable) | 500 | 1,652,438 | 2.300259 | 52641610 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,596,850 | 13,974.620029 | 52641610 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,459,038 | 0.831422 | 52641610 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,458,813 | 2,770.985354 | 52641610 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | weETH_04c0/WETH | 500 | 1,440,999 | 1.105502 | 52641610 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome_slipstream | WETH/msETH | 500 | 1,361,300 | 1.130268 | 52641610 | `0x74F72788F4814D7fF3C49B44684aa98Eee140C0E` |
| uniswap_v3 | DRB/WETH | 10000 | 1,316,207 | 0.000000 | 52641610 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome_slipstream | WETH/AERO | 3068 | 1,310,391 | 2,770.936349 | 52641610 | `0x82321f3BEB69f503380D6B233857d5C43562e2D0` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,260,058 | 0.004688 | 52641610 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,256,869 | 0.000274 | 52641610 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome_slipstream | EURC/USDC | 82 | 1,246,341 | 1.121604 | 52641610 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| aerodrome | USDC/SEND | 3000 | 1,245,630 | 62.627443 | 52641610 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,242,561 | 23.170710 | 52641610 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,184,333 | 2,336.166357 | 52641610 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | WETH/doginme | 10000 | 1,158,114 | 35,164,506.167163 | 52641610 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,155,219 | 1.105591 | 52641610 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |
| aerodrome | WETH/cbBTC | 3000 | 1,123,543 | 0.029146 | 52641610 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| aerodrome | WETH/WELL | 10000 | 1,115,174 | 1,184,409.541937 | 52641610 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,104,429 | 14.551016 | 52641610 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,103,951 | 506,613.317111 | 52641610 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | WETH/EDEL | 7000 | 1,102,579 | 77,749.222487 | 52641610 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,100,751 | 0.432589 | 52641610 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |

## Recherche d'opportunités
- Cycles : 741 ; routes examinées : 15804048 ; candidats optimisés : 98690 ; net attendu > 0 : 239 ; dernier cycle 574.6 ms
- Rejets (moteur) : {'spread_below_threshold': 15548574, 'liquidity_below_min': 141565, 'negative_expected_net': 98451, 'borrow_bound_too_small': 11619, 'unquotable': 2604, 'cycle_budget_exhausted': 996}
- Enregistrements de la session : 98690 ; net attendu > 0 : 239 ; simulés (eth_call de la vraie tx) : 14 (ok 14, échec 0) ; étiquettes ghost N+1 : 0/14 positives
- Décisions : {'REJECTED': 98690} ; motifs de rejet : {'below_safety_margin': 203, 'negative_expected_net': 98451, 'p_lower_below_threshold': 136, 'reliability_not_demonstrated': 103, 'stale_data': 45}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52641554 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.516716 WETH | 0.000075 WETH | 0.000000 WETH | 0.000003 WETH | 0.000071 WETH (0.1533 €) | — | 1.38 | 0.104 (n=35) | REJECTED | below_safety_margin(71433138643533<103343199871391), p_lower_below_threshold(0.10<0.75) |
| 52641554 | USDC→[uniswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 1,203.605774 USDC | 0.174400 USDC | 0.000000 USDC | 0.008097 USDC | 0.166303 USDC (0.1530 €) | — | 1.38 | 0.104 (n=35) | REJECTED | below_safety_margin(166303<240721), p_lower_below_threshold(0.10<0.75) |
| 52641554 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→cbBTC | 0.014139 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1524 €) | — | 1.46 | 0.104 (n=35) | REJECTED | below_safety_margin(207<282), p_lower_below_threshold(0.10<0.75) |
| 52641540 | cbBTC→[aerodrome_slipstream]→tBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.005031 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1224 €) | — | 3.30 | 0.182 (n=38) | REJECTED | p_lower_below_threshold(0.18<0.75) |
| 52641540 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→tBTC→[aerodrome_slipstream]→USDC | 413.140761 USDC | 0.140506 USDC | 0.000000 USDC | 0.007578 USDC | 0.132928 USDC (0.1223 €) | 0.132928 USDC | 3.22 | 0.182 (n=38) | REJECTED | p_lower_below_threshold(0.18<0.75) |
| 52641540 | cbBTC→[uniswap_v3]→tBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.005161 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1180 €) | — | 3.10 | 0.182 (n=38) | REJECTED | p_lower_below_threshold(0.18<0.75) |
| 52641540 | USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→tBTC→[aerodrome_slipstream]→USDC | 421.139371 USDC | 0.135164 USDC | 0.000000 USDC | 0.007578 USDC | 0.127586 USDC (0.1174 €) | 0.127586 USDC | 3.03 | 0.182 (n=38) | REJECTED | p_lower_below_threshold(0.18<0.75) |
| 52641540 | cbBTC→[pancakeswap_v3]→tBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.005049 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1173 €) | — | 3.15 | 0.182 (n=38) | REJECTED | p_lower_below_threshold(0.18<0.75) |
| 52641540 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→tBTC→[aerodrome_slipstream]→USDC | 416.610436 USDC | 0.134859 USDC | 0.000000 USDC | 0.007938 USDC | 0.126921 USDC (0.1168 €) | 0.126921 USDC | 3.05 | 0.182 (n=38) | REJECTED | p_lower_below_threshold(0.18<0.75) |
| 52641554 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.305120 WETH | 0.000056 WETH | 0.000000 WETH | 0.000003 WETH | 0.000053 WETH (0.1134 €) | — | 1.73 | 0.104 (n=35) | REJECTED | below_safety_margin(52823489579169<61024098255965), p_lower_below_threshold(0.10<0.75) |
| 52641554 | USDC→[uniswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 710.150344 USDC | 0.131013 USDC | 0.000000 USDC | 0.008097 USDC | 0.122916 USDC (0.1131 €) | — | 1.73 | 0.104 (n=35) | REJECTED | below_safety_margin(122916<142030), p_lower_below_threshold(0.10<0.75) |
| 52641554 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→cbBTC | 0.008247 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1127 €) | — | 1.86 | 0.104 (n=35) | REJECTED | below_safety_margin(153<164), p_lower_below_threshold(0.10<0.75) |
| 52641328 | WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.434863 WETH | 0.000053 WETH | 0.000000 WETH | 0.000003 WETH | 0.000049 WETH (0.1066 €) | — | 1.14 | 0.104 (n=35) | REJECTED | below_safety_margin(49359140518453<86972633703641), p_lower_below_threshold(0.10<0.75) |
| 52641328 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC | 1,017.802287 USDC | 0.123214 USDC | 0.000000 USDC | 0.007491 USDC | 0.115723 USDC (0.1065 €) | — | 1.14 | 0.104 (n=35) | REJECTED | below_safety_margin(115723<203560), p_lower_below_threshold(0.10<0.75) |
| 52641554 | cbBTC→[aerodrome_slipstream]→tBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→cbBTC | 0.004337 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0810 €) | — | 2.54 | 0.310 (n=23) | REJECTED | reliability_not_demonstrated |
| 52641554 | USDC→[uniswap_v3]→cbBTC→[aerodrome_slipstream]→tBTC→[aerodrome_slipstream]→USDC | 351.048931 USDC | 0.095541 USDC | 0.000000 USDC | 0.007712 USDC | 0.087829 USDC (0.0808 €) | — | 2.50 | 0.310 (n=23) | REJECTED | reliability_not_demonstrated |
| 52641554 | cbBTC→[uniswap_v3]→tBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→cbBTC | 0.004165 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0766 €) | — | 2.50 | 0.310 (n=23) | REJECTED | reliability_not_demonstrated |
| 52641554 | USDC→[uniswap_v3]→cbBTC→[uniswap_v3]→tBTC→[aerodrome_slipstream]→USDC | 351.064858 USDC | 0.090822 USDC | 0.000000 USDC | 0.007712 USDC | 0.083110 USDC (0.0765 €) | — | 2.37 | 0.310 (n=23) | REJECTED | reliability_not_demonstrated |
| 52641554 | cbBTC→[pancakeswap_v3]→tBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→cbBTC | 0.004150 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0744 €) | — | 2.43 | 0.104 (n=35) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 52641554 | USDC→[uniswap_v3]→cbBTC→[pancakeswap_v3]→tBTC→[aerodrome_slipstream]→USDC | 339.399968 USDC | 0.088717 USDC | 0.000000 USDC | 0.008097 USDC | 0.080620 USDC (0.0742 €) | — | 2.38 | 0.104 (n=35) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 52641554 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→cbBTC→[aerodrome_slipstream]→WETH | 0.091969 WETH | 0.000026 WETH | 0.000000 WETH | 0.000003 WETH | 0.000023 WETH (0.0489 €) | 0.000023 WETH | 2.48 | 0.104 (n=35) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 52641554 | cbBTC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→cbBTC | 0.002494 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0486 €) | — | 2.65 | 0.104 (n=35) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 52641554 | USDC→[uniswap_v3]→cbBTC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 228.872291 USDC | 0.060274 USDC | 0.000000 USDC | 0.007712 USDC | 0.052562 USDC (0.0484 €) | — | 2.30 | 0.104 (n=35) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 52641554 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→cbBTC | 0.001955 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0479 €) | — | 3.32 | 0.001 (n=9) | REJECTED | reliability_not_demonstrated |
| 52641554 | USDC→[uniswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 178.501657 USDC | 0.057261 USDC | 0.000000 USDC | 0.005769 USDC | 0.051492 USDC (0.0474 €) | — | 2.88 | 0.001 (n=10) | REJECTED | reliability_not_demonstrated |

## Fiabilité et décision
- Observations ghost : 292 ; taux observé 0.178 ; borne inférieure crédible (0.9) 0.151 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 15.1% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
