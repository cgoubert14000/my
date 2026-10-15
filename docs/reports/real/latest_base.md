# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-15T10:13:53+00:00 ; durée 141.8 min ; blocs 52630686 → 52634940 (3989 vus)

## Connexion
- Requêtes RPC : 46145 ; erreurs : 258 ; latence p50/p95 : 213.7/1,944.9 ms
- Rafraîchissements d'état : 3990 ; âge des données au dernier bloc : 1.18 s ; changements de frais LP observés (pools à frais dynamiques) : 8759
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 1 ; cycles déclenchés par événement : 1 ; avance médiane sur le rafraîchissement multicall : — ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,370.56 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 567 pools, 324 jetons, 20918 routes
- Par DEX : uniswap_v3 135, aerodrome 234, aerodrome_slipstream 152, pancakeswap_v3 29, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 204 (rejetés 2) → 609 jetons ; pools candidats 3862 (énumérés 388, par paires 0), mesurés 569, sous le plancher de 10000.0 $ : 2 → gardés 567 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2370.057693, 'AERO': 0.841029, 'cbBTC': 81234.761422}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 143,700,188 | 2,370.556279 | 52634940 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 43,922,666 | 1.191321 | 52634940 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 500 | 17,838,430 | 0.029212 | 52634940 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 15,636,942 | 105.495542 | 52634940 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 14,787,134 | 0.029166 | 52634940 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,332,915 | 0.029158 | 52634940 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,619,012 | 0.000012 | 52634940 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 8,949,075 | 2,365.843552 | 52634940 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/USDC | 3000 | 8,856,856 | 2,371.429799 | 52634940 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | USDC/cbBTC | 340 | 7,941,270 | 0.000012 | 52634940 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 669 | 7,795,359 | 2,365.325954 | 52634940 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,080,403 | 0.001648 | 52634940 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 472 | 6,635,833 | 0.000012 | 52634940 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,243,604 | 0.029201 | 52634940 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | fBOMB/AERO | 10000 | 5,152,260 | 0.026641 | 52634940 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,458,145 | 0.802389 | 52634940 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,366,867 | 0.000274 | 52634940 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,251,383 | 2,365.354514 | 52634940 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,163,821 | 1.000078 | 52634940 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome_slipstream | USDC/AERO | 10000 | 4,145,567 | 1.192760 | 52634940 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome | WETH/KTA | 3000 | 3,880,720 | 35,391.529011 | 52634940 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/AERO | 10000 | 3,409,798 | 2,803.379349 | 52634940 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | WETH/MORPHO | 2712 | 2,887,112 | 1,021.294222 | 52634940 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,821,999 | 0.000012 | 52634940 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/VVV | 2760 | 2,538,894 | 105.518732 | 52634940 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 2,511,322 | 0.000010 | 52634940 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,475,685 | 1.141650 | 52634940 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| aerodrome | WETH/FAI | 10000 | 2,330,531 | 1,050,309.238891 | 52634940 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,246,159 | 407.773828 | 52634940 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | WETH/USDT | 424 | 2,123,827 | 2,370.240156 | 52634940 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,112,489 | 1.194788 | 52634940 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,008,820 | 1.403288 | 52634940 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,958,987 | 0.000000 | 52634940 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome | fBOMB/USDC | 10000 | 1,869,516 | 0.022623 | 52634940 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,787,459 | 0.916541 | 52634940 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,783,725 | 15.771787 | 52634940 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,772,798 | 0.000012 | 52634940 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | XDP/USDC | 100 | 1,770,758 | 0.018870 | 52634940 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome | WETH/msETH (stable) | 500 | 1,680,090 | 2.301503 | 52634940 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,555,867 | 13,949.982815 | 52634940 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | WETH/AERO | 3000 | 1,472,575 | 2,819.025934 | 52634940 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | weETH_04c0/WETH | 500 | 1,465,695 | 1.105502 | 52634940 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,458,410 | 0.831299 | 52634940 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | DRB/WETH | 10000 | 1,330,358 | 0.000000 | 52634940 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome_slipstream | WETH/AERO | 3000 | 1,305,946 | 2,816.596167 | 52634940 | `0x82321f3BEB69f503380D6B233857d5C43562e2D0` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,305,431 | 0.004793 | 52634940 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,302,253 | 23.170310 | 52634940 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| aerodrome_slipstream | WETH/msETH | 500 | 1,286,843 | 1.130555 | 52634940 | `0x74F72788F4814D7fF3C49B44684aa98Eee140C0E` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,278,293 | 0.000273 | 52634940 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome_slipstream | EURC/USDC | 70 | 1,248,833 | 1.121311 | 52634940 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| aerodrome | USDC/SEND | 3000 | 1,246,459 | 62.544172 | 52634940 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,202,684 | 2,365.886699 | 52634940 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,179,162 | 1.105595 | 52634940 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |
| uniswap_v3 | WETH/doginme | 10000 | 1,173,951 | 35,591,418.210733 | 52634940 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | WETH/cbBTC | 3000 | 1,142,109 | 0.029217 | 52634940 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| aerodrome | WETH/WELL | 10000 | 1,136,333 | 1,180,140.375456 | 52634940 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,124,057 | 505,145.788086 | 52634940 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | WETH/EDEL | 7000 | 1,123,204 | 77,509.744495 | 52634940 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | USDC/NOCK | 3000 | 1,117,576 | 50.458962 | 52634940 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,114,243 | 14.229957 | 52634940 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |

## Recherche d'opportunités
- Cycles : 3990 ; routes examinées : 83462820 ; candidats optimisés : 578234 ; net attendu > 0 : 147 ; dernier cycle 594.3 ms
- Rejets (moteur) : {'spread_below_threshold': 82191078, 'liquidity_below_min': 680388, 'negative_expected_net': 578087, 'unquotable': 8719, 'borrow_bound_too_small': 3990, 'cycle_budget_exhausted': 411}
- Enregistrements de la session : 578234 ; net attendu > 0 : 147 ; simulés (eth_call de la vraie tx) : 0 (ok 0, échec 0) ; étiquettes ghost N+1 : 0/0 positives
- Décisions : {'REJECTED': 578234} ; motifs de rejet : {'below_safety_margin': 147, 'negative_expected_net': 578087, 'p_lower_below_threshold': 48, 'reliability_not_demonstrated': 99, 'stale_data': 8}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52633002 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→EURC→[aerodrome_slipstream]→cbBTC | 0.001862 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0030 €) | — | 0.21 | 0.071 (n=30) | REJECTED | below_safety_margin(4<37), p_lower_below_threshold(0.07<0.75) |
| 52633002 | USDC→[aerodrome_slipstream]→EURC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 194.176044 USDC | 0.010260 USDC | 0.000000 USDC | 0.007128 USDC | 0.003132 USDC (0.0029 €) | — | 0.16 | 0.071 (n=30) | REJECTED | below_safety_margin(3132<38835), p_lower_below_threshold(0.07<0.75) |
| 52633002 | USDC→[aerodrome_slipstream]→EURC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 161.706871 USDC | 0.008627 USDC | 0.000000 USDC | 0.007128 USDC | 0.001499 USDC (0.0014 €) | — | 0.09 | 0.071 (n=30) | REJECTED | below_safety_margin(1499<32341), p_lower_below_threshold(0.07<0.75) |
| 52633965 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 9.726653 USDC | 0.008608 USDC | 0.000000 USDC | 0.007131 USDC | 0.001477 USDC (0.0014 €) | — | 1.52 | 0.299 (n=21) | REJECTED | below_safety_margin(1477<1945), reliability_not_demonstrated |
| 52633965 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.004176 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0014 €) | — | 1.49 | 0.299 (n=21) | REJECTED | below_safety_margin(621265028040<835205070426), reliability_not_demonstrated |
| 52633965 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 9.726653 USDC | 0.008564 USDC | 0.000000 USDC | 0.007131 USDC | 0.001433 USDC (0.0013 €) | — | 1.47 | 0.071 (n=30) | REJECTED | below_safety_margin(1433<1945), p_lower_below_threshold(0.07<0.75) |
| 52633965 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.004178 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0013 €) | — | 1.44 | 0.071 (n=30) | REJECTED | below_safety_margin(602801913733<835657501441), p_lower_below_threshold(0.07<0.75) |
| 52633957 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 9.726653 USDC | 0.008469 USDC | 0.000000 USDC | 0.007131 USDC | 0.001338 USDC (0.0012 €) | — | 1.38 | 0.071 (n=30) | REJECTED | below_safety_margin(1338<1945), p_lower_below_threshold(0.07<0.75) |
| 52633958 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 9.726653 USDC | 0.008469 USDC | 0.000000 USDC | 0.007131 USDC | 0.001338 USDC (0.0012 €) | — | 1.38 | 0.071 (n=30) | REJECTED | below_safety_margin(1338<1945), p_lower_below_threshold(0.07<0.75) |
| 52633959 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 9.726653 USDC | 0.008469 USDC | 0.000000 USDC | 0.007131 USDC | 0.001338 USDC (0.0012 €) | — | 1.38 | 0.071 (n=30) | REJECTED | below_safety_margin(1338<1945), p_lower_below_threshold(0.07<0.75) |
| 52633960 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 9.726653 USDC | 0.008469 USDC | 0.000000 USDC | 0.007131 USDC | 0.001338 USDC (0.0012 €) | — | 1.38 | 0.071 (n=30) | REJECTED | below_safety_margin(1338<1945), p_lower_below_threshold(0.07<0.75) |
| 52633961 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 9.726653 USDC | 0.008469 USDC | 0.000000 USDC | 0.007131 USDC | 0.001338 USDC (0.0012 €) | — | 1.38 | 0.071 (n=30) | REJECTED | below_safety_margin(1338<1945), p_lower_below_threshold(0.07<0.75) |
| 52633962 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 9.726653 USDC | 0.008469 USDC | 0.000000 USDC | 0.007131 USDC | 0.001338 USDC (0.0012 €) | — | 1.38 | 0.071 (n=30) | REJECTED | below_safety_margin(1338<1945), p_lower_below_threshold(0.07<0.75) |
| 52633963 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 9.726653 USDC | 0.008469 USDC | 0.000000 USDC | 0.007131 USDC | 0.001338 USDC (0.0012 €) | — | 1.38 | 0.071 (n=30) | REJECTED | below_safety_margin(1338<1945), p_lower_below_threshold(0.07<0.75) |
| 52633964 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 9.726653 USDC | 0.008469 USDC | 0.000000 USDC | 0.007131 USDC | 0.001338 USDC (0.0012 €) | — | 1.38 | 0.071 (n=30) | REJECTED | below_safety_margin(1338<1945), p_lower_below_threshold(0.07<0.75) |
| 52633963 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.004162 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0012 €) | — | 1.35 | 0.071 (n=30) | REJECTED | below_safety_margin(562267695947<832434614783), p_lower_below_threshold(0.07<0.75) |
| 52633964 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.004162 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0012 €) | — | 1.35 | 0.071 (n=30) | REJECTED | below_safety_margin(562267695947<832434614783), p_lower_below_threshold(0.07<0.75) |
| 52633960 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.004162 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0012 €) | — | 1.35 | 0.071 (n=30) | REJECTED | below_safety_margin(562267695947<832434614783), p_lower_below_threshold(0.07<0.75) |
| 52633961 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.004162 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0012 €) | — | 1.35 | 0.071 (n=30) | REJECTED | below_safety_margin(562267695947<832434614783), p_lower_below_threshold(0.07<0.75) |
| 52633962 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.004162 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0012 €) | — | 1.35 | 0.071 (n=30) | REJECTED | below_safety_margin(562267695947<832434614783), p_lower_below_threshold(0.07<0.75) |
| 52633957 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.004162 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0012 €) | — | 1.35 | 0.071 (n=30) | REJECTED | below_safety_margin(562244208811<832434614783), p_lower_below_threshold(0.07<0.75) |
| 52633958 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.004162 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0012 €) | — | 1.35 | 0.071 (n=30) | REJECTED | below_safety_margin(562244208811<832434614783), p_lower_below_threshold(0.07<0.75) |
| 52633959 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.004162 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0012 €) | — | 1.35 | 0.071 (n=30) | REJECTED | below_safety_margin(562244208811<832434614783), p_lower_below_threshold(0.07<0.75) |
| 52633488 | USDC→[aerodrome_slipstream]→USDT→[pancakeswap_v3]→USDC | 251.901507 USDC | 0.006819 USDC | 0.000000 USDC | 0.005689 USDC | 0.001130 USDC (0.0010 €) | — | 0.04 | 0.001 (n=10) | REJECTED | below_safety_margin(1130<50380), reliability_not_demonstrated |
| 52633664 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.004064 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0010 €) | — | 1.16 | 0.299 (n=21) | REJECTED | below_safety_margin(469521915628<812704510653), reliability_not_demonstrated |

## Fiabilité et décision
- Observations ghost : 258 ; taux observé 0.190 ; borne inférieure crédible (0.9) 0.160 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 16.0% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
