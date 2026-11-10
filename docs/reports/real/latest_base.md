# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-10T14:05:46+00:00 ; durée 3.05 min ; blocs 55644907 → 55645820 (160 vus)

## Connexion
- Requêtes RPC : 2218 ; erreurs : 3 ; latence p50/p95 : 339.8/1,557.3 ms
- Rafraîchissements d'état : 160 ; âge des données au dernier bloc : 7.79 s ; changements de frais LP observés (pools à frais dynamiques) : 119
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 169 ; cycles déclenchés par événement : 63 ; avance médiane sur le rafraîchissement multicall : 612 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,067.74 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 461 pools, 270 jetons, 16362 routes
- Par DEX : uniswap_v3 132, aerodrome_slipstream 99, aerodrome 190, pancakeswap_v3 26, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 164 (rejetés 2) → 569 jetons ; pools candidats 3648 (énumérés 286, par paires 0), mesurés 463, sous le plancher de 10000.0 $ : 2 → gardés 461 (max 1500) ; prix des hubs : {'USDC': 1.0, 'USDbC': 1.0, 'DAI': 1.0, 'WETH': 2067.744894, 'cbBTC': 73787.664735, 'AERO': 0.555242}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 136,994,324 | 2,067.744903 | 55645843 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,198,788 | 0.028024 | 55645843 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,197,428 | 0.000014 | 55645843 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 8,604,039 | 0.027977 | 55645843 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 7,319,976 | 2,068.080430 | 55645843 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 6,887,192 | 105.245676 | 55645843 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,642,502 | 0.028029 | 55645843 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 4,351,383 | 1.801015 | 55645843 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/USDC | 100 | 3,928,119 | 2,068.676002 | 55645843 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,877,165 | 1.000003 | 55645843 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,052,294 | 42,949.318291 | 55645843 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 150 | 2,946,881 | 2,068.497237 | 55645843 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2545 | 2,282,978 | 0.027963 | 55645843 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 1,979,673 | 1,105,866.935214 | 55645843 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,682,576 | 0.000014 | 55645843 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | USDC/cbBTC | 460 | 1,657,064 | 0.000014 | 55645843 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | XDP/USDC | 100 | 1,612,445 | 0.016247 | 55645843 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,545,206 | 0.006689 | 55645843 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,513,863 | 0.000000 | 55645843 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,491,665 | 0.000014 | 55645843 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,460,510 | 0.821956 | 55645843 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,432,667 | 416.110606 | 55645843 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,424,441 | 1.429325 | 55645843 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v2 | WETH/USDC | 3000 | 1,274,940 | 2,067.901878 | 55645843 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| uniswap_v3 | WETH/AERO | 3000 | 1,262,331 | 3,719.298238 | 55645843 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,236,169 | 14,870.396899 | 55645843 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/USDC | 3000 | 1,203,970 | 2,068.714254 | 55645843 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome | USDC/SEND | 3000 | 1,106,632 | 79.347361 | 55645843 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,060,083 | 2,068.105290 | 55645843 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | WETH/doginme | 10000 | 1,033,288 | 35,260,186.233240 | 55645843 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome_slipstream | USDC/VELVET | 100 | 957,512 | 21.560089 | 55645843 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/BRETT | 10000 | 945,053 | 562,951.162075 | 55645843 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | WETH/VVV | 10000 | 926,213 | 104.994244 | 55645843 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 918,680 | 0.001493 | 55645843 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 342 | 917,204 | 0.000014 | 55645843 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | WETH/TOSHI | 10000 | 916,103 | 22,771,465.285706 | 55645843 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | USDC/VVV | 3000 | 900,671 | 0.050866 | 55645843 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/MORPHO | 3000 | 890,228 | 1,025.428051 | 55645843 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/USDC | 10000 | 877,730 | 2,070.799405 | 55645843 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | DRB/WETH | 10000 | 867,218 | 0.000000 | 55645843 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | USDC/NOCK | 3000 | 788,726 | 75.610071 | 55645843 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome | WETH/EDEL | 7000 | 779,146 | 107,373.893752 | 55645843 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome_slipstream | USDC/SAPIEN | 4590 | 772,514 | 21.973520 | 55645843 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 759,853 | 0.051500 | 55645843 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/AERO | 10000 | 724,455 | 3,710.753909 | 55645843 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | WETH/wstETH | 3000 | 701,985 | 0.798536 | 55645843 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 653,951 | 0.536179 | 55645843 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v3 | TIG/USDC | 10000 | 646,162 | 0.524461 | 55645843 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 645,887 | 4,852,166.470250 | 55645843 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 604,953 | 0.000008 | 55645843 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v2 | WETH/NPC | 3000 | 587,260 | 156,917.677740 | 55645843 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome | VIRTUAL/WETH | 10000 | 582,480 | 0.000257 | 55645843 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/BRETT | 2114 | 579,172 | 557,821.712134 | 55645843 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | FLOCK/USDC | 3000 | 564,476 | 0.038218 | 55645843 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 502,395 | 1,025.590312 | 55645843 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome | WETH/DRV | 3000 | 482,876 | 6,724.483454 | 55645843 | `0xaC4e562d7C6108f971321F14238E24AE2cC398ac` |
| pancakeswap_v3 | ELSA/USDC | 100 | 473,907 | 0.068672 | 55645843 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| aerodrome_slipstream | USDC/USDT | 8 | 455,503 | 1.001169 | 55645843 | `0xa41Bc0AFfbA7Fd420d186b84899d7ab2aC57fcD1` |
| uniswap_v3 | WETH/UNI | 10000 | 452,154 | 297.418392 | 55645843 | `0xAb365f161Dd501473a1ff0D2ef0dCE94E7398839` |
| aerodrome | WETH/msETH (stable) | 500 | 444,617 | 2.390100 | 55645843 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |

## Recherche d'opportunités
- Cycles : 222 ; routes examinées : 3632364 ; candidats optimisés : 13939 ; net attendu > 0 : 24 ; dernier cycle 243.3 ms
- Rejets (moteur) : {'spread_below_threshold': 3569588, 'liquidity_below_min': 48524, 'negative_expected_net': 13915, 'borrow_bound_too_small': 313}
- Enregistrements de la session : 13939 ; net attendu > 0 : 24 ; simulés (eth_call de la vraie tx) : 0 (ok 0, échec 0) ; étiquettes ghost N+1 : 0/0 positives
- Décisions : {'REJECTED': 13939} ; motifs de rejet : {'below_safety_margin': 24, 'negative_expected_net': 13915, 'p_lower_below_threshold': 22, 'reliability_not_demonstrated': 2}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 55645593 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.198248 WETH | 0.000009 WETH | 0.000000 WETH | 0.000002 WETH | 0.000007 WETH (0.0135 €) | — | 0.36 | 0.081 (n=338) | REJECTED | below_safety_margin(7074638363013<39649626127205), p_lower_below_threshold(0.08<0.75) |
| 55645593 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.198248 WETH | 0.000009 WETH | 0.000000 WETH | 0.000002 WETH | 0.000007 WETH (0.0135 €) | — | 0.36 | 0.081 (n=338) | REJECTED | below_safety_margin(7074638363013<39649626127205), p_lower_below_threshold(0.08<0.75) |
| 55645593 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 404.965979 USDC | 0.019297 USDC | 0.000000 USDC | 0.004684 USDC | 0.014613 USDC (0.0134 €) | — | 0.36 | 0.081 (n=338) | REJECTED | below_safety_margin(14613<80993), p_lower_below_threshold(0.08<0.75) |
| 55645593 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 404.965979 USDC | 0.019297 USDC | 0.000000 USDC | 0.004684 USDC | 0.014613 USDC (0.0134 €) | — | 0.36 | 0.081 (n=338) | REJECTED | below_safety_margin(14613<80993), p_lower_below_threshold(0.08<0.75) |
| 55645154 | cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.003476 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0115 €) | — | 0.49 | 0.228 (n=1405) | REJECTED | below_safety_margin(17<69), p_lower_below_threshold(0.23<0.75) |
| 55645154 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 267.868612 USDC | 0.018645 USDC | 0.000000 USDC | 0.006282 USDC | 0.012363 USDC (0.0114 €) | — | 0.46 | 0.228 (n=1405) | REJECTED | below_safety_margin(12363<53573), p_lower_below_threshold(0.23<0.75) |
| 55645154 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.129546 WETH | 0.000009 WETH | 0.000000 WETH | 0.000003 WETH | 0.000006 WETH (0.0113 €) | — | 0.46 | 0.228 (n=1405) | REJECTED | below_safety_margin(5956343137584<25909254516343), p_lower_below_threshold(0.23<0.75) |
| 55645154 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.108607 WETH | 0.000008 WETH | 0.000000 WETH | 0.000002 WETH | 0.000005 WETH (0.0102 €) | — | 0.49 | 0.059 (n=14) | REJECTED | below_safety_margin(5367280676589<21721300402994), reliability_not_demonstrated |
| 55645154 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 222.387734 USDC | 0.016098 USDC | 0.000000 USDC | 0.005012 USDC | 0.011086 USDC (0.0102 €) | — | 0.50 | 0.059 (n=14) | REJECTED | below_safety_margin(11086<44477), reliability_not_demonstrated |
| 55645154 | cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.003133 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0095 €) | — | 0.45 | 0.228 (n=1405) | REJECTED | below_safety_margin(14<62), p_lower_below_threshold(0.23<0.75) |
| 55645154 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.111826 WETH | 0.000008 WETH | 0.000000 WETH | 0.000003 WETH | 0.000005 WETH (0.0093 €) | — | 0.44 | 0.228 (n=1405) | REJECTED | below_safety_margin(4885022783460<22365277331631), p_lower_below_threshold(0.23<0.75) |
| 55645154 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 246.761819 USDC | 0.016382 USDC | 0.000000 USDC | 0.006282 USDC | 0.010100 USDC (0.0093 €) | — | 0.41 | 0.228 (n=1405) | REJECTED | below_safety_margin(10100<49352), p_lower_below_threshold(0.23<0.75) |
| 55645154 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.046582 WETH | 0.000003 WETH | 0.000000 WETH | 0.000002 WETH | 0.000001 WETH (0.0020 €) | — | 0.23 | 0.081 (n=338) | REJECTED | below_safety_margin(1075967146948<9316422977095), p_lower_below_threshold(0.08<0.75) |
| 55645154 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 95.276396 USDC | 0.006916 USDC | 0.000000 USDC | 0.004697 USDC | 0.002219 USDC (0.0020 €) | — | 0.23 | 0.081 (n=338) | REJECTED | below_safety_margin(2219<19055), p_lower_below_threshold(0.08<0.75) |
| 55645154 | WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.015542 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0019 €) | — | 0.64 | 0.228 (n=1405) | REJECTED | below_safety_margin(989168584740<3108454054991), p_lower_below_threshold(0.23<0.75) |
| 55645154 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC | 32.045650 USDC | 0.008321 USDC | 0.000000 USDC | 0.006282 USDC | 0.002039 USDC (0.0019 €) | — | 0.64 | 0.228 (n=1405) | REJECTED | below_safety_margin(2039<6409), p_lower_below_threshold(0.23<0.75) |
| 55645592 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.011202 WETH | 0.000003 WETH | 0.000000 WETH | 0.000002 WETH | 0.000000 WETH (0.0008 €) | — | 0.38 | 0.081 (n=338) | REJECTED | below_safety_margin(426165209050<2240301658160), p_lower_below_threshold(0.08<0.75) |
| 55645592 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.011202 WETH | 0.000003 WETH | 0.000000 WETH | 0.000002 WETH | 0.000000 WETH (0.0008 €) | — | 0.38 | 0.081 (n=338) | REJECTED | below_safety_margin(426165209050<2240301658160), p_lower_below_threshold(0.08<0.75) |
| 55645592 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 22.953305 USDC | 0.005560 USDC | 0.000000 USDC | 0.004683 USDC | 0.000877 USDC (0.0008 €) | — | 0.38 | 0.081 (n=338) | REJECTED | below_safety_margin(877<4590), p_lower_below_threshold(0.08<0.75) |
| 55645592 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 22.953305 USDC | 0.005560 USDC | 0.000000 USDC | 0.004683 USDC | 0.000877 USDC (0.0008 €) | — | 0.38 | 0.081 (n=338) | REJECTED | below_safety_margin(877<4590), p_lower_below_threshold(0.08<0.75) |
| 55645154 | WETH→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.016857 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0002 €) | — | 0.07 | 0.228 (n=1405) | REJECTED | below_safety_margin(110702207398<3371435720559), p_lower_below_threshold(0.23<0.75) |
| 55645154 | WETH→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.014974 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0001 €) | — | 0.05 | 0.228 (n=1405) | REJECTED | below_safety_margin(72846781427<2994787954267), p_lower_below_threshold(0.23<0.75) |
| 55645154 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→USDC | 28.280621 USDC | 0.006319 USDC | 0.000000 USDC | 0.006282 USDC | 0.000037 USDC (0.0000 €) | — | 0.01 | 0.228 (n=1405) | REJECTED | below_safety_margin(37<5656), p_lower_below_threshold(0.23<0.75) |
| 55645154 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→USDC | 32.316508 USDC | 0.006297 USDC | 0.000000 USDC | 0.006282 USDC | 0.000015 USDC (0.0000 €) | — | 0.00 | 0.228 (n=1405) | REJECTED | below_safety_margin(15<6463), p_lower_below_threshold(0.23<0.75) |

## Fiabilité et décision
- Observations ghost : 7505 ; taux observé 0.193 ; borne inférieure crédible (0.9) 0.187 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 18.7% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
