# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-14T15:56:11+00:00 ; durée 52.25 min ; blocs 52600436 → 52602007 (733 vus)

## Connexion
- Requêtes RPC : 12988 ; erreurs : 0 ; latence p50/p95 : 416.2/1,422.6 ms
- Rafraîchissements d'état : 733 ; âge des données au dernier bloc : 7.54 s ; changements de frais LP observés (pools à frais dynamiques) : 3012
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 35245 ; cycles déclenchés par événement : 2058 ; avance médiane sur le rafraîchissement multicall : 712 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,435.20 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 575 pools, 327 jetons, 21004 routes
- Par DEX : uniswap_v3 140, aerodrome 235 (quarantaine 2), aerodrome_slipstream 153, pancakeswap_v3 30, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 207 (rejetés 2) → 612 jetons ; pools candidats 3920 (énumérés 391, par paires 0), mesurés 580, sous le plancher de 10000.0 $ : 5 → gardés 575 (max 1500) ; prix des hubs : {'USDC': 1.0, 'USDbC': 1.0, 'DAI': 1.0, 'WETH': 2425.371992, 'AERO': 0.862121, 'cbBTC': 81739.3593}
- Pools en quarantaine : 2 — aerodrome:fBOMB/USDbC@0xC39566: simulation failed ×5 (model/chain mismatch) — until block 52602285; aerodrome:fBOMB/USDC@0xFf8e0b: simulation failed ×5 (model/chain mismatch) — until block 52602285

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 147,905,866 | 2,435.198257 | 52602008 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 44,255,432 | 1.167706 | 52602008 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 500 | 17,890,871 | 0.029767 | 52602008 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 15,870,312 | 108.254974 | 52602008 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 13,447,604 | 0.029742 | 52602008 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,489,562 | 0.029728 | 52602008 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,233,598 | 0.000012 | 52602008 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 9,193,398 | 2,429.983531 | 52602008 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/USDC | 3000 | 8,977,812 | 2,434.687483 | 52602008 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | USDC/cbBTC | 332 | 8,114,344 | 0.000012 | 52602008 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 743 | 8,004,770 | 2,429.526599 | 52602008 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,170,812 | 0.001664 | 52602008 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 412 | 6,669,072 | 0.000012 | 52602008 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,436,869 | 0.029753 | 52602008 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/superOETHb | 400 | 5,378,575 | 1.000859 | 52602008 | `0x6446021F4E396dA3df4235C62537431372195D38` |
| aerodrome | fBOMB/AERO | 10000 | 5,189,527 | 0.026582 | 52602008 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,629,330 | 0.000278 | 52602008 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,579,999 | 0.802388 | 52602008 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,406,619 | 2,429.111874 | 52602008 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,344,011 | 0.998900 | 52602008 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 4,013,361 | 34,919.696368 | 52602008 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/AERO | 10000 | 3,574,617 | 2,817.920208 | 52602008 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | USDC/AERO | 10000 | 3,247,451 | 1.159432 | 52602008 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,946,278 | 1.141644 | 52602008 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,840,302 | 0.000012 | 52602008 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 2,601,967 | 0.000010 | 52602008 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/VVV | 2712 | 2,559,057 | 108.211274 | 52602008 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,557,128 | 403.213196 | 52602008 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | WETH/FAI | 10000 | 2,374,153 | 1,068,015.285516 | 52602008 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | WETH/USDT | 439 | 2,347,249 | 2,433.337184 | 52602008 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,113,462 | 1.193532 | 52602008 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | BNKR/WETH | 10000 | 2,098,897 | 0.000000 | 52602008 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome | fBOMB/USDbC | 10000 | 1,947,987 | 0.022457 | 52602008 | `0xC395664B295ed5bf1D249Ae8be9740655AA174ef` |
| aerodrome_slipstream | WETH/MORPHO | 2733 | 1,944,372 | 1,044.965676 | 52602008 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,907,599 | 0.916707 | 52602008 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,887,132 | 15.594328 | 52602008 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | USDC/alUSDb (stable) | 500 | 1,840,035 | 1.397535 | 52602008 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| uniswap_v3 | XDP/USDC | 100 | 1,795,321 | 0.019378 | 52602008 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,765,746 | 0.000012 | 52602008 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | WETH/msETH (stable) | 500 | 1,633,053 | 2.305573 | 52602008 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | WETH/AERO | 3000 | 1,512,492 | 2,837.892664 | 52602008 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | weETH_04c0/WETH | 500 | 1,505,604 | 1.105776 | 52602008 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,464,858 | 0.836331 | 52602008 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,416,846 | 13,539.909130 | 52602008 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | DRB/WETH | 10000 | 1,391,424 | 0.000000 | 52602008 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,359,776 | 0.000278 | 52602008 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,354,769 | 0.004851 | 52602008 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | WETH/AERO | 3008 | 1,335,907 | 2,837.813066 | 52602008 | `0x82321f3BEB69f503380D6B233857d5C43562e2D0` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,268,303 | 23.396054 | 52602008 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,252,250 | 2,429.882796 | 52602008 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,247,308 | 62.459029 | 52602008 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,237,060 | 33,231,744.623267 | 52602008 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome_slipstream | WETH/msETH | 500 | 1,224,497 | 1.131310 | 52602008 | `0x74F72788F4814D7fF3C49B44684aa98Eee140C0E` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,214,650 | 1.105594 | 52602008 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |
| aerodrome | WETH/EDEL | 7000 | 1,185,061 | 72,876.918895 | 52602008 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | USDC/NOCK | 3000 | 1,174,437 | 45.690851 | 52602008 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,164,959 | 493,173.304965 | 52602008 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | WETH/WELL | 10000 | 1,160,603 | 1,193,822.414145 | 52602008 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,143,460 | 13.353253 | 52602008 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome_slipstream | msUSD/USDC | 503 | 1,130,216 | 0.885592 | 52602008 | `0x7501bc8Bb51616F79bfA524E464fb7B41f0B10fB` |

## Recherche d'opportunités
- Cycles : 2790 ; routes examinées : 58601160 ; candidats optimisés : 403921 ; net attendu > 0 : 972 ; dernier cycle 100.6 ms
- Rejets (moteur) : {'spread_below_threshold': 57206013, 'liquidity_below_min': 489870, 'pool_quarantined': 421310, 'negative_expected_net': 402949, 'borrow_bound_too_small': 55374, 'unquotable': 19956, 'cycle_budget_exhausted': 4716}
- Enregistrements de la session : 403921 ; net attendu > 0 : 972 ; simulés (eth_call de la vraie tx) : 56 (ok 6, échec 50) ; étiquettes ghost N+1 : 0/28 positives
- Décisions : {'REJECTED': 403921} ; motifs de rejet : {'below_safety_margin': 903, 'negative_expected_net': 402949, 'price_impact': 35, 'reliability_not_demonstrated': 972, 'sim_below_estimate': 5, 'simulated_net_nonpositive': 5, 'simulation_failed': 50, 'stale_data': 515}

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
- Observations ghost : 165 ; taux observé 0.176 ; borne inférieure crédible (0.9) 0.141 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 14.1% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
