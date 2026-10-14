# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-14T16:11:34+00:00 ; durée 67.63 min ; blocs 52600436 → 52602470 (1045 vus)

## Connexion
- Requêtes RPC : 17418 ; erreurs : 0 ; latence p50/p95 : 455.9/1,449.6 ms
- Rafraîchissements d'état : 1045 ; âge des données au dernier bloc : 3.76 s ; changements de frais LP observés (pools à frais dynamiques) : 3811
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 43100 ; cycles déclenchés par événement : 2314 ; avance médiane sur le rafraîchissement multicall : 1,086 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,433.15 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 575 pools, 327 jetons, 21004 routes
- Par DEX : uniswap_v3 140, aerodrome 235 (quarantaine 2), aerodrome_slipstream 153, pancakeswap_v3 30, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 207 (rejetés 2) → 612 jetons ; pools candidats 3920 (énumérés 391, par paires 0), mesurés 580, sous le plancher de 10000.0 $ : 5 → gardés 575 (max 1500) ; prix des hubs : {'USDC': 1.0, 'USDbC': 1.0, 'DAI': 1.0, 'WETH': 2425.371992, 'AERO': 0.862121, 'cbBTC': 81739.3593}
- Pools en quarantaine : 2 — aerodrome:fBOMB/USDbC@0xC39566: simulation failed ×5 (model/chain mismatch) — until block 52602588; aerodrome:fBOMB/USDC@0xFf8e0b: simulation failed ×5 (model/chain mismatch) — until block 52602588

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 147,819,276 | 2,433.148613 | 52602471 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 44,295,602 | 1.165640 | 52602471 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 500 | 17,874,625 | 0.029786 | 52602471 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 15,849,972 | 108.350309 | 52602471 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 14,863,678 | 0.029742 | 52602471 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,478,186 | 0.029728 | 52602471 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,227,536 | 0.000012 | 52602471 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 9,193,123 | 2,430.360411 | 52602471 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/USDC | 3000 | 8,974,033 | 2,433.221369 | 52602471 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | WETH/USDC | 713 | 8,248,708 | 2,429.672137 | 52602471 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | USDC/cbBTC | 334 | 8,073,907 | 0.000012 | 52602471 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,159,742 | 0.001663 | 52602471 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 424 | 6,954,939 | 0.000012 | 52602471 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,431,506 | 0.029775 | 52602471 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/superOETHb | 400 | 5,374,048 | 1.000859 | 52602471 | `0x6446021F4E396dA3df4235C62537431372195D38` |
| aerodrome | fBOMB/AERO | 10000 | 5,191,908 | 0.026582 | 52602471 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome_slipstream | USDC/AERO | 10000 | 5,012,863 | 1.159541 | 52602471 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,627,923 | 0.000278 | 52602471 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,576,144 | 0.802388 | 52602471 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,403,876 | 2,429.392473 | 52602471 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,337,651 | 0.998895 | 52602471 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 4,009,158 | 34,934.059613 | 52602471 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/AERO | 10000 | 3,576,259 | 2,817.920135 | 52602471 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,943,799 | 1.141644 | 52602471 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,838,400 | 0.000012 | 52602471 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/VVV | 2700 | 2,555,689 | 108.397204 | 52602471 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 2,518,650 | 0.000011 | 52602471 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | WETH/FAI | 10000 | 2,372,155 | 1,068,015.285516 | 52602471 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,334,587 | 403.671345 | 52602471 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | WETH/USDT | 427 | 2,325,786 | 2,433.805070 | 52602471 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,113,462 | 1.193532 | 52602471 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | BNKR/WETH | 10000 | 2,097,132 | 0.000000 | 52602471 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome | fBOMB/USDbC | 10000 | 1,947,157 | 0.022457 | 52602471 | `0xC395664B295ed5bf1D249Ae8be9740655AA174ef` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,905,993 | 0.916707 | 52602471 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| aerodrome | USDC/alUSDb (stable) | 500 | 1,838,167 | 1.400046 | 52602471 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,826,193 | 15.590908 | 52602471 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| uniswap_v3 | XDP/USDC | 100 | 1,811,072 | 0.018969 | 52602471 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,772,539 | 0.000012 | 52602471 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,660,518 | 13,552.318061 | 52602471 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/msETH (stable) | 500 | 1,631,679 | 2.305573 | 52602471 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | WETH/AERO | 3000 | 1,512,557 | 2,837.892868 | 52602471 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | weETH_04c0/WETH | 500 | 1,504,337 | 1.105776 | 52602471 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,465,190 | 0.835975 | 52602471 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | DRB/WETH | 10000 | 1,391,007 | 0.000000 | 52602471 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,359,364 | 0.000278 | 52602471 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,353,629 | 0.004851 | 52602471 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | WETH/AERO | 3000 | 1,337,100 | 2,837.813076 | 52602471 | `0x82321f3BEB69f503380D6B233857d5C43562e2D0` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,266,427 | 23.410813 | 52602471 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,252,186 | 2,430.329297 | 52602471 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,247,308 | 62.459029 | 52602471 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,236,318 | 33,231,744.623267 | 52602471 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome_slipstream | WETH/msETH | 500 | 1,227,903 | 1.131275 | 52602471 | `0x74F72788F4814D7fF3C49B44684aa98Eee140C0E` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,213,627 | 1.105594 | 52602471 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |
| aerodrome | WETH/EDEL | 7000 | 1,188,251 | 72,527.503438 | 52602471 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | USDC/NOCK | 3000 | 1,174,611 | 45.677388 | 52602471 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,163,979 | 493,173.304965 | 52602471 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | WETH/WELL | 10000 | 1,159,626 | 1,193,822.414149 | 52602471 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,137,225 | 13.535963 | 52602471 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome_slipstream | msUSD/USDC | 500 | 1,125,807 | 0.885549 | 52602471 | `0x7501bc8Bb51616F79bfA524E464fb7B41f0B10fB` |
| aerodrome_slipstream | WETH/MORPHO | 2766 | 1,040,533 | 1,042.081886 | 52602471 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |

## Recherche d'opportunités
- Cycles : 3358 ; routes examinées : 70531432 ; candidats optimisés : 483104 ; net attendu > 0 : 977 ; dernier cycle 355.6 ms
- Rejets (moteur) : {'spread_below_threshold': 68865654, 'liquidity_below_min': 596949, 'pool_quarantined': 488870, 'negative_expected_net': 482127, 'borrow_bound_too_small': 69574, 'unquotable': 21092, 'cycle_budget_exhausted': 6189}
- Enregistrements de la session : 483104 ; net attendu > 0 : 977 ; simulés (eth_call de la vraie tx) : 61 (ok 6, échec 55) ; étiquettes ghost N+1 : 0/29 positives
- Décisions : {'REJECTED': 483104} ; motifs de rejet : {'below_safety_margin': 903, 'negative_expected_net': 482127, 'price_impact': 40, 'reliability_not_demonstrated': 977, 'sim_below_estimate': 5, 'simulated_net_nonpositive': 5, 'simulation_failed': 55, 'stale_data': 517}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52600862 | WETH→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH | 1.236021 WETH | 0.000083 WETH | 0.000000 WETH | 0.000002 WETH | 0.000081 WETH (0.1803 €) | — | 0.65 | 0.003 (n=2) | REJECTED | below_safety_margin(80572873655235<247204155501096), reliability_not_demonstrated |
| 52600862 | cbBTC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.035155 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1798 €) | — | 0.68 | 0.003 (n=2) | REJECTED | below_safety_margin(239<703), reliability_not_demonstrated |
| 52600862 | WETH→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH | 1.040788 WETH | 0.000068 WETH | 0.000000 WETH | 0.000002 WETH | 0.000065 WETH (0.1465 €) | — | 0.63 | 0.003 (n=2) | REJECTED | below_safety_margin(65460329991419<208157582204409), reliability_not_demonstrated |
| 52600862 | cbBTC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.028712 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1459 €) | — | 0.68 | 0.003 (n=2) | REJECTED | below_safety_margin(194<574), reliability_not_demonstrated |
| 52600862 | cbBTC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC | 0.028837 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1354 €) | — | 0.62 | 0.003 (n=2) | REJECTED | below_safety_margin(180<576), reliability_not_demonstrated |
| 52600862 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→WETH | 0.892238 WETH | 0.000063 WETH | 0.000000 WETH | 0.000002 WETH | 0.000060 WETH (0.1353 €) | — | 0.68 | 0.003 (n=2) | REJECTED | below_safety_margin(60439176157500<178447505802959), reliability_not_demonstrated |
| 52600818 | USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 1,187.620992 USDC | 0.150904 USDC | 0.000000 USDC | 0.007995 USDC | 0.142909 USDC (0.1315 €) | — | 1.20 | 0.001 (n=14) | REJECTED | below_safety_margin(142909<237524), reliability_not_demonstrated |
| 52600818 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH | 0.489501 WETH | 0.000062 WETH | 0.000000 WETH | 0.000003 WETH | 0.000059 WETH (0.1310 €) | — | 1.20 | 0.001 (n=14) | REJECTED | below_safety_margin(58717639295016<97900106940413), reliability_not_demonstrated |
| 52600864 | USDC→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 1,290.524278 USDC | 0.136890 USDC | 0.000000 USDC | 0.008380 USDC | 0.128510 USDC (0.1182 €) | — | 1.00 | 0.000 (n=16) | REJECTED | below_safety_margin(128510<258104), stale_data(5226ms>4000.0), reliability_not_demonstrated |
| 52600864 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→WETH | 0.531096 WETH | 0.000056 WETH | 0.000000 WETH | 0.000003 WETH | 0.000053 WETH (0.1179 €) | — | 0.99 | 0.000 (n=16) | REJECTED | below_safety_margin(52663053278228<106219260097614), stale_data(5219ms>4000.0), reliability_not_demonstrated |
| 52600789 | USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 1,120.342147 USDC | 0.135269 USDC | 0.000000 USDC | 0.007990 USDC | 0.127279 USDC (0.1171 €) | — | 1.14 | 0.001 (n=14) | REJECTED | below_safety_margin(127279<224068), reliability_not_demonstrated |
| 52600789 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH | 0.461665 WETH | 0.000056 WETH | 0.000000 WETH | 0.000003 WETH | 0.000052 WETH (0.1169 €) | — | 1.13 | 0.001 (n=14) | REJECTED | below_safety_margin(52380512945299<92333025975433), reliability_not_demonstrated |
| 52600864 | USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 1,131.836208 USDC | 0.134275 USDC | 0.000000 USDC | 0.008008 USDC | 0.126267 USDC (0.1162 €) | — | 1.12 | 0.000 (n=16) | REJECTED | below_safety_margin(126267<226367), stale_data(5096ms>4000.0), reliability_not_demonstrated |
| 52600864 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH | 0.465027 WETH | 0.000055 WETH | 0.000000 WETH | 0.000003 WETH | 0.000052 WETH (0.1158 €) | — | 1.11 | 0.000 (n=16) | REJECTED | below_safety_margin(51723970702919<93005482134803), stale_data(5090ms>4000.0), reliability_not_demonstrated |
| 52600865 | USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 1,129.216008 USDC | 0.133335 USDC | 0.000000 USDC | 0.008008 USDC | 0.125327 USDC (0.1153 €) | — | 1.11 | 0.000 (n=16) | REJECTED | below_safety_margin(125327<225843), stale_data(5992ms>4000.0), reliability_not_demonstrated |
| 52600866 | USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 1,129.216008 USDC | 0.133335 USDC | 0.000000 USDC | 0.008008 USDC | 0.125327 USDC (0.1153 €) | — | 1.11 | 0.000 (n=16) | REJECTED | below_safety_margin(125327<225843), stale_data(8003ms>4000.0), reliability_not_demonstrated |
| 52600865 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH | 0.463551 WETH | 0.000055 WETH | 0.000000 WETH | 0.000003 WETH | 0.000051 WETH (0.1149 €) | — | 1.11 | 0.000 (n=16) | REJECTED | below_safety_margin(51338598726463<92710238940151), stale_data(5985ms>4000.0), reliability_not_demonstrated |
| 52600866 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH | 0.463551 WETH | 0.000055 WETH | 0.000000 WETH | 0.000003 WETH | 0.000051 WETH (0.1149 €) | — | 1.11 | 0.000 (n=16) | REJECTED | below_safety_margin(51338598726463<92710238940151), stale_data(7996ms>4000.0), reliability_not_demonstrated |
| 52601343 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.249307 WETH | 0.000053 WETH | 0.000000 WETH | 0.000002 WETH | 0.000050 WETH (0.1132 €) | — | 2.03 | 0.003 (n=2) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52601343 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 606.029468 USDC | 0.128648 USDC | 0.000000 USDC | 0.005607 USDC | 0.123041 USDC (0.1132 €) | — | 2.03 | 0.003 (n=2) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52601416 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.229207 WETH | 0.000045 WETH | 0.000000 WETH | 0.000002 WETH | 0.000042 WETH (0.0945 €) | — | 1.84 | 0.002 (n=4) | REJECTED | below_safety_margin(42136440864292<45841474081541), reliability_not_demonstrated |
| 52601416 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 557.052329 USDC | 0.108705 USDC | 0.000000 USDC | 0.006021 USDC | 0.102684 USDC (0.0945 €) | — | 1.84 | 0.002 (n=4) | REJECTED | below_safety_margin(102684<111410), reliability_not_demonstrated |
| 52600862 | WETH→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH | 0.916203 WETH | 0.000041 WETH | 0.000000 WETH | 0.000002 WETH | 0.000039 WETH (0.0868 €) | — | 0.42 | 0.003 (n=2) | REJECTED | below_safety_margin(38793785507145<183240659786817), reliability_not_demonstrated |
| 52600862 | cbBTC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.024812 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0865 €) | — | 0.46 | 0.003 (n=2) | REJECTED | below_safety_margin(115<496), reliability_not_demonstrated |
| 52601484 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.207739 WETH | 0.000037 WETH | 0.000000 WETH | 0.000003 WETH | 0.000034 WETH (0.0764 €) | — | 1.64 | 0.002 (n=4) | REJECTED | below_safety_margin(34062245910840<41547769899915), reliability_not_demonstrated |

## Fiabilité et décision
- Observations ghost : 166 ; taux observé 0.175 ; borne inférieure crédible (0.9) 0.140 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 14.0% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
