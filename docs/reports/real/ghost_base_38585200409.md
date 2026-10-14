# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-14T15:16:06+00:00 ; durée 12.17 min ; blocs 52600436 → 52600809 (160 vus)

## Connexion
- Requêtes RPC : 2788 ; erreurs : 0 ; latence p50/p95 : 749.4/4,007.8 ms
- Rafraîchissements d'état : 160 ; âge des données au dernier bloc : 25.09 s ; changements de frais LP observés (pools à frais dynamiques) : 879
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 5706 ; cycles déclenchés par événement : 239 ; avance médiane sur le rafraîchissement multicall : 859 ms
- Gaz : base fee 0.005006 gwei ; prix ETH (pool le plus profond) : 2,425.73 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 575 pools, 327 jetons, 21004 routes
- Par DEX : uniswap_v3 140, aerodrome 235 (quarantaine 2), aerodrome_slipstream 153, pancakeswap_v3 30, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 207 (rejetés 2) → 612 jetons ; pools candidats 3920 (énumérés 391, par paires 0), mesurés 580, sous le plancher de 10000.0 $ : 5 → gardés 575 (max 1500) ; prix des hubs : {'USDC': 1.0, 'USDbC': 1.0, 'DAI': 1.0, 'WETH': 2425.371992, 'AERO': 0.862121, 'cbBTC': 81739.3593}
- Pools en quarantaine : 2 — aerodrome:fBOMB/AERO@0xbBf71A: simulation failed ×5 (model/chain mismatch) — until block 52600872; aerodrome:fBOMB/USDC@0xFf8e0b: simulation failed ×5 (model/chain mismatch) — until block 52600872

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 147,042,878 | 2,425.730423 | 52600805 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 44,388,716 | 1.160791 | 52600805 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 500 | 17,839,649 | 0.029692 | 52600805 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 15,809,527 | 108.242557 | 52600805 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 12,926,104 | 0.029647 | 52600805 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,458,037 | 0.029633 | 52600805 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,222,722 | 0.000012 | 52600808 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 9,166,988 | 2,431.876304 | 52600806 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/USDC | 3000 | 8,960,241 | 2,425.709965 | 52600805 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | USDC/cbBTC | 378 | 8,104,283 | 0.000012 | 52600805 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 1026 | 7,953,323 | 2,432.422592 | 52600806 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,147,708 | 0.001660 | 52600805 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 600 | 6,630,910 | 0.000012 | 52600805 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,404,700 | 0.029702 | 52600807 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/superOETHb | 400 | 5,357,662 | 1.000859 | 52600805 | `0x6446021F4E396dA3df4235C62537431372195D38` |
| aerodrome | fBOMB/AERO | 10000 | 5,215,892 | 0.026573 | 52600805 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome_slipstream | USDC/AERO | 10000 | 4,901,349 | 1.157179 | 52600805 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,610,631 | 0.000278 | 52600805 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,562,191 | 0.802388 | 52600805 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,374,695 | 2,432.363342 | 52600809 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 202 | 4,337,996 | 0.998901 | 52600805 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,993,737 | 34,990.015219 | 52600805 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/AERO | 10000 | 3,578,142 | 2,804.290000 | 52600805 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,934,814 | 1.141639 | 52600805 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,837,987 | 0.000012 | 52600805 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/VVV | 2814 | 2,549,128 | 108.211319 | 52600805 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 2,473,435 | 0.000011 | 52600809 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,441,467 | 404.092898 | 52600809 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | WETH/FAI | 10000 | 2,366,255 | 1,066,812.609594 | 52600805 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | WETH/USDT | 490 | 2,313,293 | 2,434.959626 | 52600805 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,116,947 | 1.189919 | 52600805 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | BNKR/WETH | 10000 | 2,090,765 | 0.000000 | 52600805 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome | fBOMB/USDbC | 10000 | 2,013,306 | 0.023446 | 52600805 | `0xC395664B295ed5bf1D249Ae8be9740655AA174ef` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,900,182 | 0.916707 | 52600805 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,884,856 | 15.592970 | 52600805 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | USDC/alUSDb (stable) | 500 | 1,840,035 | 1.397535 | 52600805 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| uniswap_v3 | XDP/USDC | 100 | 1,812,706 | 0.018903 | 52600809 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | WETH/MORPHO | 2847 | 1,793,354 | 1,044.553807 | 52600809 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,748,244 | 0.000012 | 52600808 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,739,633 | 13,613.855086 | 52600805 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/msETH (stable) | 500 | 1,627,310 | 2.304293 | 52600805 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | WETH/AERO | 3000 | 1,511,577 | 2,821.331825 | 52600805 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | weETH_04c0/WETH | 500 | 1,499,750 | 1.105776 | 52600805 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,465,055 | 0.836119 | 52600805 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | DRB/WETH | 10000 | 1,418,091 | 0.000000 | 52600805 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,354,284 | 0.000278 | 52600805 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,339,447 | 0.004808 | 52600805 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | WETH/AERO | 3020 | 1,339,048 | 2,820.947960 | 52600805 | `0x82321f3BEB69f503380D6B233857d5C43562e2D0` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,270,975 | 23.392853 | 52600805 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,248,605 | 2,431.930285 | 52600805 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,247,308 | 62.459029 | 52600805 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,232,030 | 33,248,568.751527 | 52600805 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome_slipstream | WETH/msETH | 500 | 1,212,464 | 1.130963 | 52600805 | `0x74F72788F4814D7fF3C49B44684aa98Eee140C0E` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,209,927 | 1.105594 | 52600805 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |
| aerodrome | WETH/EDEL | 7000 | 1,185,030 | 72,281.659931 | 52600805 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | USDC/NOCK | 3000 | 1,177,148 | 45.480648 | 52600805 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,160,430 | 493,173.304965 | 52600805 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | WETH/WELL | 10000 | 1,156,170 | 1,193,657.968819 | 52600805 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,131,956 | 13.694811 | 52600806 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | WETH/bsdETH | 100 | 1,030,012 | 0.916698 | 52600805 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |

## Recherche d'opportunités
- Cycles : 398 ; routes examinées : 8359592 ; candidats optimisés : 57659 ; net attendu > 0 : 115 ; dernier cycle 144.5 ms
- Rejets (moteur) : {'spread_below_threshold': 8171275, 'liquidity_below_min': 79860, 'negative_expected_net': 57544, 'pool_quarantined': 39390, 'unquotable': 10348, 'cycle_budget_exhausted': 662, 'borrow_bound_too_small': 398}
- Enregistrements de la session : 57659 ; net attendu > 0 : 115 ; simulés (eth_call de la vraie tx) : 6 (ok 0, échec 6) ; étiquettes ghost N+1 : 0/2 positives
- Décisions : {'REJECTED': 57659} ; motifs de rejet : {'below_safety_margin': 109, 'negative_expected_net': 57544, 'price_impact': 6, 'reliability_not_demonstrated': 115, 'simulation_failed': 6, 'stale_data': 14}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52600789 | USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 1,120.342147 USDC | 0.135269 USDC | 0.000000 USDC | 0.007990 USDC | 0.127279 USDC (0.1171 €) | — | 1.14 | 0.001 (n=14) | REJECTED | below_safety_margin(127279<224068), reliability_not_demonstrated |
| 52600789 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH | 0.461665 WETH | 0.000056 WETH | 0.000000 WETH | 0.000003 WETH | 0.000052 WETH (0.1169 €) | — | 1.13 | 0.001 (n=14) | REJECTED | below_safety_margin(52380512945299<92333025975433), reliability_not_demonstrated |
| 52600789 | USDC→[pancakeswap_v3]→USDT→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 690.558263 USDC | 0.072572 USDC | 0.000000 USDC | 0.007622 USDC | 0.064950 USDC (0.0598 €) | — | 0.94 | 0.001 (n=14) | REJECTED | below_safety_margin(64950<138111), reliability_not_demonstrated |
| 52600789 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→USDT→[aerodrome_slipstream]→WETH | 0.285319 WETH | 0.000030 WETH | 0.000000 WETH | 0.000003 WETH | 0.000027 WETH (0.0596 €) | — | 0.94 | 0.001 (n=14) | REJECTED | below_safety_margin(26725637883498<57063817681252), reliability_not_demonstrated |
| 52600789 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.005970 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0504 €) | — | 1.12 | 0.003 (n=2) | REJECTED | below_safety_margin(67<119), reliability_not_demonstrated |
| 52600789 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.201263 WETH | 0.000026 WETH | 0.000000 WETH | 0.000003 WETH | 0.000022 WETH (0.0500 €) | — | 1.11 | 0.003 (n=2) | REJECTED | below_safety_margin(22409794342174<40252597607769), reliability_not_demonstrated |
| 52600789 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 543.176611 USDC | 0.062109 USDC | 0.000000 USDC | 0.007990 USDC | 0.054119 USDC (0.0498 €) | — | 1.00 | 0.003 (n=2) | REJECTED | below_safety_margin(54119<108635), reliability_not_demonstrated |
| 52600789 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.195272 WETH | 0.000017 WETH | 0.000000 WETH | 0.000003 WETH | 0.000014 WETH (0.0313 €) | — | 0.72 | 0.001 (n=14) | REJECTED | below_safety_margin(14019467681848<39054462804664), reliability_not_demonstrated |
| 52600789 | USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 413.932740 USDC | 0.041213 USDC | 0.000000 USDC | 0.007622 USDC | 0.033591 USDC (0.0309 €) | — | 0.81 | 0.001 (n=14) | REJECTED | below_safety_margin(33591<82786), reliability_not_demonstrated |
| 52600789 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→cbBTC | 0.005264 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0308 €) | — | 0.78 | 0.001 (n=14) | REJECTED | below_safety_margin(41<105), reliability_not_demonstrated |
| 52600789 | USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 443.288705 USDC | 0.040622 USDC | 0.000000 USDC | 0.007622 USDC | 0.033000 USDC (0.0304 €) | — | 0.74 | 0.001 (n=14) | REJECTED | below_safety_margin(33000<88657), reliability_not_demonstrated |
| 52600789 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.190538 WETH | 0.000017 WETH | 0.000000 WETH | 0.000003 WETH | 0.000014 WETH (0.0304 €) | — | 0.71 | 0.001 (n=14) | REJECTED | below_safety_margin(13602884684797<38107684624740), reliability_not_demonstrated |
| 52600789 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→cbBTC | 0.005068 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0301 €) | — | 0.79 | 0.001 (n=14) | REJECTED | below_safety_margin(40<101), reliability_not_demonstrated |
| 52600789 | cbBTC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.006847 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0293 €) | — | 0.57 | 0.001 (n=14) | REJECTED | below_safety_margin(39<136), reliability_not_demonstrated |
| 52600789 | USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 574.088373 USDC | 0.039701 USDC | 0.000000 USDC | 0.007990 USDC | 0.031711 USDC (0.0292 €) | — | 0.55 | 0.001 (n=14) | REJECTED | below_safety_margin(31711<114817), reliability_not_demonstrated |
| 52600789 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH | 0.218088 WETH | 0.000016 WETH | 0.000000 WETH | 0.000003 WETH | 0.000013 WETH (0.0288 €) | — | 0.59 | 0.001 (n=14) | REJECTED | below_safety_margin(12911908198115<43617532612064), reliability_not_demonstrated |
| 52600739 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC | 305.639436 USDC | 0.038923 USDC | 0.000000 USDC | 0.008019 USDC | 0.030904 USDC (0.0284 €) | — | 1.01 | 0.170 (n=13) | REJECTED | below_safety_margin(30904<61127), reliability_not_demonstrated |
| 52600739 | WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.125868 WETH | 0.000016 WETH | 0.000000 WETH | 0.000003 WETH | 0.000013 WETH (0.0284 €) | — | 1.01 | 0.170 (n=13) | REJECTED | below_safety_margin(12741665043643<25173694583421), reliability_not_demonstrated |
| 52600789 | USDC→[uniswap_v3]→USDT→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 518.429781 USDC | 0.030883 USDC | 0.000000 USDC | 0.007990 USDC | 0.022893 USDC (0.0211 €) | — | 0.44 | 0.001 (n=14) | REJECTED | below_safety_margin(22893<103685), reliability_not_demonstrated |
| 52600789 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→USDT→[aerodrome_slipstream]→WETH | 0.214678 WETH | 0.000013 WETH | 0.000000 WETH | 0.000003 WETH | 0.000009 WETH (0.0210 €) | — | 0.44 | 0.001 (n=14) | REJECTED | below_safety_margin(9416205926499<42935570177732), reliability_not_demonstrated |
| 52600789 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 153.074222 USDC | 0.028235 USDC | 0.000000 USDC | 0.007622 USDC | 0.020613 USDC (0.0190 €) | — | 1.35 | 0.001 (n=14) | REJECTED | below_safety_margin(20613<30614), reliability_not_demonstrated |
| 52600789 | cbBTC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.001926 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0188 €) | — | 1.30 | 0.001 (n=14) | REJECTED | below_safety_margin(25<38), reliability_not_demonstrated |
| 52600789 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→WETH | 0.066465 WETH | 0.000012 WETH | 0.000000 WETH | 0.000003 WETH | 0.000008 WETH (0.0188 €) | — | 1.27 | 0.001 (n=14) | REJECTED | below_safety_margin(8416098415905<13293017682510), reliability_not_demonstrated |
| 52600662 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome_slipstream]→WETH | 0.040166 WETH | 0.000011 WETH | 0.000000 WETH | 0.000003 WETH | 0.000007 WETH (0.0167 €) | — | 1.86 | 0.001 (n=14) | REJECTED | below_safety_margin(7462223959115<8033240989289), reliability_not_demonstrated |
| 52600662 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome_slipstream]→WETH | 0.040166 WETH | 0.000011 WETH | 0.000000 WETH | 0.000003 WETH | 0.000007 WETH (0.0167 €) | — | 1.86 | 0.001 (n=14) | REJECTED | below_safety_margin(7462223959115<8033240989289), reliability_not_demonstrated |

## Fiabilité et décision
- Observations ghost : 139 ; taux observé 0.209 ; borne inférieure crédible (0.9) 0.168 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 16.8% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
