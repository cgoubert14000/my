# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-15T14:02:18+00:00 ; durée 33.71 min ; blocs 52640781 → 52641794 (904 vus)

## Connexion
- Requêtes RPC : 11994 ; erreurs : 203 ; latence p50/p95 : 212.0/1,864.3 ms
- Rafraîchissements d'état : 904 ; âge des données au dernier bloc : 2.78 s ; changements de frais LP observés (pools à frais dynamiques) : 4577
- Flux d'événements (WebSocket Swap/Sync) : non connecté ; événements appliqués : 0 ; cycles déclenchés par événement : 0 ; avance médiane sur le rafraîchissement multicall : — ms
- Gaz : base fee 0.005005 gwei ; prix ETH (pool le plus profond) : 2,335.95 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 570 pools, 326 jetons, 21328 routes
- Par DEX : uniswap_v3 136, aerodrome 235, aerodrome_slipstream 152, pancakeswap_v3 30, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 205 (rejetés 2) → 610 jetons ; pools candidats 3864 (énumérés 389, par paires 0), mesurés 572, sous le plancher de 10000.0 $ : 2 → gardés 570 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDC': 1.0, 'USDbC': 1.0, 'WETH': 2346.001193, 'AERO': 0.837627, 'cbBTC': 80168.530844}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 141,753,058 | 2,335.951144 | 52641794 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 44,126,969 | 1.182379 | 52641794 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 500 | 17,629,324 | 0.029185 | 52641794 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 15,599,002 | 102.937414 | 52641794 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 12,954,928 | 0.029162 | 52641794 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,184,297 | 0.029149 | 52641794 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,544,620 | 0.000012 | 52641794 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 8,830,423 | 2,341.830876 | 52641794 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/USDC | 3000 | 8,780,596 | 2,335.616546 | 52641794 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | USDC/cbBTC | 384 | 7,895,486 | 0.000012 | 52641794 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,991,702 | 0.001652 | 52641794 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | WETH/USDC | 1011 | 6,738,879 | 2,342.646980 | 52641794 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | USDC/cbBTC | 600 | 6,256,275 | 0.000012 | 52641794 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome | fBOMB/AERO | 10000 | 5,147,125 | 0.026341 | 52641794 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,077,742 | 0.029179 | 52641794 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,495,000 | 0.000274 | 52641794 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,393,069 | 0.802389 | 52641794 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome_slipstream | cbBTC/LBTC | 202 | 4,212,162 | 0.999755 | 52641794 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,209,813 | 2,342.593991 | 52641794 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | WETH/KTA | 3000 | 3,837,966 | 35,135.703628 | 52641794 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/AERO | 10000 | 3,397,512 | 2,786.358682 | 52641794 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | USDC/AERO | 10000 | 2,863,722 | 1.189966 | 52641794 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,808,167 | 0.000012 | 52641794 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 2,544,676 | 1,019.904788 | 52641794 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome_slipstream | WETH/VVV | 2733 | 2,514,129 | 102.955344 | 52641794 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,506,274 | 407.840793 | 52641794 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,440,306 | 1.141648 | 52641794 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 2,331,576 | 0.000011 | 52641794 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | WETH/FAI | 10000 | 2,129,677 | 1,221,311.263811 | 52641794 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,112,870 | 1.194579 | 52641794 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,008,820 | 1.403288 | 52641794 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| aerodrome_slipstream | WETH/USDT | 478 | 1,979,685 | 2,345.575215 | 52641794 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,937,457 | 0.000000 | 52641794 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome | fBOMB/USDC | 10000 | 1,845,447 | 0.022311 | 52641794 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,765,579 | 0.916541 | 52641794 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| uniswap_v3 | XDP/USDC | 100 | 1,754,824 | 0.018365 | 52641794 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,744,179 | 0.000012 | 52641794 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,715,714 | 15.790892 | 52641794 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,669,065 | 13,974.620029 | 52641794 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/msETH (stable) | 500 | 1,656,181 | 2.300259 | 52641794 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | WETH/AERO | 3000 | 1,462,423 | 2,765.980077 | 52641794 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,459,038 | 0.831422 | 52641794 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome | weETH_04c0/WETH | 500 | 1,444,296 | 1.105502 | 52641794 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome_slipstream | WETH/msETH | 500 | 1,362,998 | 1.130281 | 52641794 | `0x74F72788F4814D7fF3C49B44684aa98Eee140C0E` |
| uniswap_v3 | DRB/WETH | 10000 | 1,319,218 | 0.000000 | 52641794 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome_slipstream | WETH/AERO | 3020 | 1,313,780 | 2,766.650128 | 52641794 | `0x82321f3BEB69f503380D6B233857d5C43562e2D0` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,267,643 | 23.170710 | 52641794 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,262,940 | 0.004688 | 52641794 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,259,746 | 0.000273 | 52641794 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | USDC/SEND | 3000 | 1,247,214 | 62.468463 | 52641794 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome_slipstream | EURC/USDC | 70 | 1,246,398 | 1.121672 | 52641794 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,184,655 | 2,341.460608 | 52641794 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | WETH/doginme | 10000 | 1,161,292 | 35,164,506.167163 | 52641794 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,157,862 | 1.105591 | 52641794 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |
| aerodrome | WETH/cbBTC | 3000 | 1,125,965 | 0.029146 | 52641794 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| aerodrome | WETH/WELL | 10000 | 1,117,725 | 1,184,409.541937 | 52641794 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,106,449 | 506,647.182122 | 52641794 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,104,658 | 14.543364 | 52641794 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,103,139 | 0.434495 | 52641794 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| aerodrome | WETH/EDEL | 7000 | 1,100,694 | 78,373.185778 | 52641794 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |

## Recherche d'opportunités
- Cycles : 903 ; routes examinées : 19259184 ; candidats optimisés : 115095 ; net attendu > 0 : 239 ; dernier cycle 460.5 ms
- Rejets (moteur) : {'spread_below_threshold': 18956429, 'liquidity_below_min': 169223, 'negative_expected_net': 114856, 'borrow_bound_too_small': 14457, 'unquotable': 2984, 'cycle_budget_exhausted': 996}
- Enregistrements de la session : 115095 ; net attendu > 0 : 239 ; simulés (eth_call de la vraie tx) : 14 (ok 14, échec 0) ; étiquettes ghost N+1 : 0/14 positives
- Décisions : {'REJECTED': 115095} ; motifs de rejet : {'below_safety_margin': 203, 'negative_expected_net': 114856, 'p_lower_below_threshold': 136, 'reliability_not_demonstrated': 103, 'stale_data': 45}

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
