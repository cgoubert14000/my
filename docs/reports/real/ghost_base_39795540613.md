# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-22T17:42:45+00:00 ; durée 191.08 min ; blocs 52945073 → 52950802 (5334 vus)

## Connexion
- Requêtes RPC : 65988 ; erreurs : 8 ; latence p50/p95 : 424.0/1,588.9 ms
- Rafraîchissements d'état : 5334 ; âge des données au dernier bloc : 3.83 s ; changements de frais LP observés (pools à frais dynamiques) : 14240
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 126620 ; cycles déclenchés par événement : 4421 ; avance médiane sur le rafraîchissement multicall : 1,206 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,378.82 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 546 pools, 318 jetons, 19398 routes
- Par DEX : uniswap_v3 137, aerodrome 226, aerodrome_slipstream 137, pancakeswap_v3 30, uniswap_v2 13, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 198 (rejetés 2) → 603 jetons ; pools candidats 3827 (énumérés 366, par paires 0), mesurés 549, sous le plancher de 10000.0 $ : 3 → gardés 546 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'DAI': 1.0, 'USDC': 1.0, 'WETH': 2404.811718, 'AERO': 0.81356, 'cbBTC': 81633.413427}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 155,395,222 | 2,378.820857 | 52950803 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 18,170,682 | 1.249227 | 52950803 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,172,559 | 0.029293 | 52950803 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 15,385,752 | 92.451106 | 52950803 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,217,271 | 0.029247 | 52950803 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,391,499 | 0.000012 | 52950803 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 9,157,205 | 0.029260 | 52950803 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/USDC | 500 | 8,666,069 | 2,378.662087 | 52950803 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,124,321 | 0.001666 | 52950803 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 336 | 6,796,955 | 0.000012 | 52950803 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 150 | 5,699,709 | 2,379.422185 | 52950803 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | USDC/cbBTC | 424 | 5,352,804 | 0.000012 | 52950803 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,349,408 | 0.029293 | 52950803 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,465,311 | 2,379.553116 | 52950803 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | WETH/USDC | 3000 | 4,293,010 | 2,379.132415 | 52950803 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,270,303 | 1.000001 | 52950803 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,937,597 | 34,588.776834 | 52950803 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | VIRTUAL/WETH | 10000 | 3,428,425 | 0.000274 | 52950803 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/USDT | 403 | 2,895,811 | 2,383.031128 | 52950803 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome_slipstream | WETH/VVV | 2703 | 2,544,648 | 92.471455 | 52950803 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | WETH/AERO | 10000 | 2,324,627 | 2,981.678209 | 52950803 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,281,011 | 398.599311 | 52950803 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,211,389 | 0.000012 | 52950803 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | WETH/FAI | 10000 | 2,188,257 | 1,198,899.323792 | 52950803 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 2,039,064 | 0.000012 | 52950803 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,884,849 | 0.000000 | 52950803 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,800,046 | 0.018476 | 52950803 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,657,271 | 1.525093 | 52950803 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | WETH/AERO | 3000 | 1,615,980 | 2,967.752216 | 52950803 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,457,509 | 0.823520 | 52950803 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,401,911 | 13,616.350096 | 52950803 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,364,366 | 0.005001 | 52950803 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,315,777 | 2,378.594021 | 52950803 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,285,421 | 0.000274 | 52950803 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | WETH/msETH (stable) | 500 | 1,284,095 | 2.369350 | 52950803 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | DRB/WETH | 10000 | 1,266,535 | 0.000000 | 52950803 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | USDC/SEND | 3000 | 1,229,636 | 64.267198 | 52950803 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,179,114 | 35,842,882.445006 | 52950803 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,166,492 | 16.372842 | 52950803 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | WETH/WELL | 10000 | 1,165,296 | 1,106,821.682140 | 52950803 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,138,662 | 500,017.713432 | 52950803 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | USDC/NOCK | 3000 | 1,130,838 | 49.074638 | 52950803 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 1,089,355 | 0.000010 | 52950803 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | weETH_04c0/WETH | 500 | 1,086,008 | 1.105751 | 52950803 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome | WETH/EDEL | 7000 | 1,079,971 | 74,908.733967 | 52950803 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,052,836 | 21,408,920.470197 | 52950803 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,039,340 | 17.020491 | 52950803 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,007,714 | 22.976964 | 52950803 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| aerodrome | WETH/cbBTC | 3000 | 1,007,339 | 0.029252 | 52950803 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| uniswap_v3 | USDC/VVV | 3000 | 981,253 | 0.038869 | 52950803 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/MORPHO | 3000 | 953,378 | 1,055.932168 | 52950803 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/USDC | 10000 | 936,680 | 2,381.973244 | 52950803 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | uXRP/WETH | 3000 | 908,770 | 0.000550 | 52950803 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome | WETH/bsdETH | 100 | 886,078 | 0.916103 | 52950803 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 881,164 | 17.851352 | 52950803 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v2 | WETH/USDC | 3000 | 872,855 | 2,383.776118 | 52950803 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome | WETH/wstETH | 3000 | 805,942 | 0.803225 | 52950803 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| aerodrome | fBOMB/USDC | 10000 | 800,730 | 0.018522 | 52950803 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 795,919 | 1.106136 | 52950803 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 784,520 | 0.648842 | 52950803 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |

## Recherche d'opportunités
- Cycles : 9754 ; routes examinées : 189208092 ; candidats optimisés : 1226949 ; net attendu > 0 : 535 ; dernier cycle 384.2 ms
- Rejets (moteur) : {'spread_below_threshold': 185937497, 'liquidity_below_min': 1688944, 'negative_expected_net': 1226414, 'pool_quarantined': 336472, 'borrow_bound_too_small': 9749, 'cycle_budget_exhausted': 8481}
- Enregistrements de la session : 1226949 ; net attendu > 0 : 535 ; simulés (eth_call de la vraie tx) : 40 (ok 16, échec 24) ; étiquettes ghost N+1 : 7/34 positives
- Décisions : {'REJECTED': 1226949} ; motifs de rejet : {'below_safety_margin': 371, 'negative_expected_net': 1226414, 'p_lower_below_threshold': 468, 'reliability_not_demonstrated': 67, 'sim_below_estimate': 7, 'simulated_net_nonpositive': 5, 'simulation_failed': 24, 'stale_data': 17}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52949317 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 1.098593 WETH | 0.000214 WETH | 0.000000 WETH | 0.000003 WETH | 0.000211 WETH (0.4601 €) | — | 1.92 | 0.022 (n=66) | REJECTED | below_safety_margin(211334195589695<219718505543851), p_lower_below_threshold(0.02<0.75) |
| 52949318 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 1.098593 WETH | 0.000214 WETH | 0.000000 WETH | 0.000003 WETH | 0.000211 WETH (0.4601 €) | — | 1.92 | 0.022 (n=66) | REJECTED | below_safety_margin(211334195589695<219718505543851), p_lower_below_threshold(0.02<0.75) |
| 52949317 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 2,592.723459 USDC | 0.506184 USDC | 0.000000 USDC | 0.007309 USDC | 0.498875 USDC (0.4590 €) | — | 1.92 | 0.022 (n=66) | REJECTED | below_safety_margin(498875<518544), p_lower_below_threshold(0.02<0.75) |
| 52949318 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 2,592.723459 USDC | 0.506184 USDC | 0.000000 USDC | 0.007309 USDC | 0.498875 USDC (0.4590 €) | — | 1.92 | 0.022 (n=66) | REJECTED | below_safety_margin(498875<518544), p_lower_below_threshold(0.02<0.75) |
| 52946299 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.017489 cbBTC | 0.000003 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000003 cbBTC (0.2258 €) | — | 1.72 | 0.001 (n=6) | REJECTED | below_safety_margin(301<349), reliability_not_demonstrated |
| 52946299 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.595274 WETH | 0.000106 WETH | 0.000000 WETH | 0.000003 WETH | 0.000102 WETH (0.2257 €) | — | 1.72 | 0.001 (n=6) | REJECTED | below_safety_margin(102399355594060<119054820899875), reliability_not_demonstrated |
| 52946299 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 1,478.363420 USDC | 0.252661 USDC | 0.000000 USDC | 0.008652 USDC | 0.244009 USDC (0.2245 €) | — | 1.65 | 0.001 (n=6) | REJECTED | below_safety_margin(244009<295672), reliability_not_demonstrated |
| 52946299 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.316550 WETH | 0.000099 WETH | 0.000000 WETH | 0.000003 WETH | 0.000096 WETH (0.2116 €) | — | 3.03 | 0.094 (n=190) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.09<0.75) |
| 52946299 | cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.009285 cbBTC | 0.000003 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000003 cbBTC (0.2116 €) | — | 3.04 | 0.094 (n=190) | REJECTED | p_lower_below_threshold(0.09<0.75) |
| 52946299 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 764.368596 USDC | 0.237843 USDC | 0.000000 USDC | 0.008282 USDC | 0.229561 USDC (0.2112 €) | — | 3.00 | 0.094 (n=190) | REJECTED | p_lower_below_threshold(0.09<0.75) |
| 52948349 | USDC→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→USDC | 491.552280 USDC | 0.231479 USDC | 0.000000 USDC | 0.007367 USDC | 0.224112 USDC (0.2062 €) | — | 4.56 | 0.120 (n=98) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.12<0.75) |
| 52948349 | cbBTC→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→cbBTC | 0.005630 cbBTC | 0.000003 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000003 cbBTC (0.2055 €) | — | 4.87 | 0.120 (n=98) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52948349 | USDC→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→USDC | 490.246119 USDC | 0.229508 USDC | 0.000000 USDC | 0.007367 USDC | 0.222141 USDC (0.2044 €) | — | 4.53 | 0.120 (n=98) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52948349 | cbBTC→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→cbBTC | 0.005630 cbBTC | 0.000003 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000003 cbBTC (0.2040 €) | — | 4.83 | 0.120 (n=98) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52948349 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→cbBTC | 0.005247 cbBTC | 0.000003 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000003 cbBTC (0.1883 €) | — | 4.78 | 0.093 (n=191) | REJECTED | p_lower_below_threshold(0.09<0.75) |
| 52948349 | USDC→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 452.628167 USDC | 0.212258 USDC | 0.000000 USDC | 0.007731 USDC | 0.204527 USDC (0.1882 €) | — | 4.52 | 0.093 (n=191) | REJECTED | p_lower_below_threshold(0.09<0.75) |
| 52948349 | USDC→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→cbBTC→[uniswap_v3]→USDC | 413.910120 USDC | 0.184965 USDC | 0.000000 USDC | 0.007367 USDC | 0.177598 USDC (0.1634 €) | — | 4.29 | 0.120 (n=98) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52948349 | cbBTC→[uniswap_v3]→USDC→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→cbBTC | 0.004931 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1628 €) | — | 4.40 | 0.120 (n=98) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52946299 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.269461 WETH | 0.000074 WETH | 0.000000 WETH | 0.000003 WETH | 0.000071 WETH (0.1573 €) | — | 2.65 | 0.022 (n=64) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.02<0.75) |
| 52946299 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 644.411865 USDC | 0.176635 USDC | 0.000000 USDC | 0.006021 USDC | 0.170614 USDC (0.1570 €) | — | 2.65 | 0.022 (n=64) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 52949143 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.232130 WETH | 0.000062 WETH | 0.000000 WETH | 0.000002 WETH | 0.000060 WETH (0.1311 €) | — | 2.58 | 0.022 (n=65) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.02<0.75) |
| 52949143 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 550.015814 USDC | 0.147965 USDC | 0.000000 USDC | 0.005852 USDC | 0.142113 USDC (0.1307 €) | — | 2.58 | 0.022 (n=65) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 52948349 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→USDC | 241.331339 USDC | 0.139162 USDC | 0.000000 USDC | 0.007367 USDC | 0.131795 USDC (0.1213 €) | — | 5.46 | 0.120 (n=98) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52948349 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→USDC | 242.243688 USDC | 0.138949 USDC | 0.000000 USDC | 0.007367 USDC | 0.131582 USDC (0.1211 €) | — | 5.43 | 0.120 (n=98) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52948349 | cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.002809 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1208 €) | — | 5.73 | 0.120 (n=98) | REJECTED | p_lower_below_threshold(0.12<0.75) |

## Fiabilité et décision
- Observations ghost : 1919 ; taux observé 0.095 ; borne inférieure crédible (0.9) 0.087 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 8.7% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
