# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-13T03:15:54+00:00 ; durée 303.85 min ; blocs 56655713 → 56746811 (19006 vus)

## Connexion
- Requêtes RPC : 236792 ; erreurs : 65 ; latence p50/p95 : 240.3/1,012.9 ms
- Rafraîchissements d'état : 19006 ; âge des données au dernier bloc : 7.73 s ; changements de frais LP observés (pools à frais dynamiques) : 10179
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 12058 ; cycles déclenchés par événement : 4529 ; avance médiane sur le rafraîchissement multicall : 508 ms
- Gaz : base fee 0.005052 gwei ; prix ETH (pool le plus profond) : 1,982.11 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 457 pools, 266 jetons, 14822 routes
- Par DEX : uniswap_v3 133, aerodrome_slipstream 97, aerodrome 187, pancakeswap_v3 27, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 1
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 159 (rejetés 2) → 564 jetons ; pools candidats 3621 (énumérés 282, par paires 0), mesurés 459, sous le plancher de 10000.0 $ : 2 → gardés 457 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'DAI': 1.0, 'USDC': 1.0, 'WETH': 2015.232847, 'cbBTC': 71439.030081, 'AERO': 0.524681}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 130,882,691 | 1,980.249812 | 56746835 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,038,766 | 0.028407 | 56746835 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 8,376,346 | 0.028336 | 56746835 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 7,803,835 | 0.000014 | 56746835 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 6,774,925 | 1,975.636605 | 56746835 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 6,529,402 | 107.368780 | 56746835 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,129,252 | 0.028400 | 56746835 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 4,064,704 | 1.982355 | 56746835 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,003,859 | 1,975.026037 | 56746835 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,675,597 | 0.998720 | 56746835 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 2,958,368 | 42,010.287406 | 56746835 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 379 | 2,759,209 | 1,975.730118 | 56746835 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2540 | 2,116,924 | 0.028341 | 56746835 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 1,850,484 | 1,163,003.281972 | 56746835 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | XDP/USDC | 100 | 1,635,139 | 0.016582 | 56746835 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | USDC/cbBTC | 600 | 1,542,106 | 0.000014 | 56746835 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,537,570 | 0.000014 | 56746835 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,470,075 | 0.000000 | 56746835 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,465,746 | 0.006586 | 56746835 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,463,210 | 0.832801 | 56746835 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,358,843 | 428.108795 | 56746835 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,320,314 | 0.000014 | 56746835 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v2 | WETH/USDC | 3000 | 1,248,557 | 1,981.038656 | 56746835 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| uniswap_v3 | WETH/AERO | 3000 | 1,190,786 | 3,916.558270 | 56746835 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,162,271 | 15,097.478175 | 56746835 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/USDC | 3000 | 1,133,599 | 1,980.895950 | 56746835 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,086,666 | 1,975.797643 | 56746835 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,060,794 | 86.352961 | 56746835 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,045,316 | 1.383900 | 56746835 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | WETH/doginme | 10000 | 995,819 | 34,363,198.215308 | 56746835 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome_slipstream | USDC/VELVET | 100 | 971,968 | 20.630458 | 56746835 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/VVV | 10000 | 958,813 | 106.607602 | 56746835 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/BRETT | 10000 | 907,692 | 559,035.693317 | 56746835 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 870,005 | 0.001498 | 56746835 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| uniswap_v3 | WETH/TOSHI | 10000 | 866,316 | 23,341,018.408331 | 56746835 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | WETH/USDC | 10000 | 863,372 | 1,993.502997 | 56746835 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 857,027 | 998.069826 | 56746835 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | USDC/VVV | 3000 | 856,453 | 0.054258 | 56746835 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome_slipstream | USDC/cbBTC | 428 | 847,859 | 0.000014 | 56746835 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | DRB/WETH | 10000 | 790,693 | 0.000000 | 56746835 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | USDC/NOCK | 3000 | 768,856 | 79.572654 | 56746835 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| pancakeswap_v3 | QUID/USDC | 100 | 744,889 | 0.049427 | 56746835 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome_slipstream | USDC/SAPIEN | 4625 | 736,934 | 23.506691 | 56746835 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome | WETH/wstETH | 3000 | 671,541 | 0.801801 | 56746835 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| aerodrome | WETH/AERO | 10000 | 669,745 | 3,889.205172 | 56746835 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 652,886 | 0.517024 | 56746835 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 632,963 | 4,643,320.549968 | 56746835 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 602,681 | 0.457069 | 56746835 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/NPC | 3000 | 570,504 | 153,045.001313 | 56746835 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome | VIRTUAL/WETH | 10000 | 559,659 | 0.000261 | 56746835 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/BRETT | 2165 | 557,458 | 558,258.904100 | 56746835 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | FLOCK/USDC | 3000 | 553,921 | 0.037270 | 56746835 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome_slipstream | AERO/cbBTC | 1025 | 539,297 | 0.000007 | 56746835 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v3 | WETH/USDC | 100 | 498,154 | 1,975.225280 | 56746835 | `0xb4CB800910B228ED3d0834cF79D697127BBB00e5` |
| aerodrome_slipstream | WETH/MORPHO | 2706 | 478,726 | 998.339312 | 56746835 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| pancakeswap_v3 | ELSA/USDC | 100 | 455,278 | 0.065108 | 56746835 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| aerodrome_slipstream | USDC/USDT | 11 | 449,518 | 1.001159 | 56746835 | `0xa41Bc0AFfbA7Fd420d186b84899d7ab2aC57fcD1` |
| uniswap_v3 | USDC/MORPHO | 10000 | 445,374 | 0.501169 | 56746835 | `0x2043B296fFC6b2d3bf4A3F3167d2Afb3B0FBdbEE` |
| uniswap_v3 | WETH/UNI | 10000 | 426,926 | 335.097779 | 56746835 | `0xAb365f161Dd501473a1ff0D2ef0dCE94E7398839` |
| uniswap_v3 | WETH/uSOL | 3000 | 422,350 | 24.902317 | 56746835 | `0xab04A352D4EC8d0F1812A4E5EBe7807Fa67acD48` |

## Recherche d'opportunités
- Cycles : 23534 ; routes examinées : 348820948 ; candidats optimisés : 1757720 ; net attendu > 0 : 2409 ; dernier cycle 9632.0 ms
- Rejets (moteur) : {'spread_below_threshold': 340978608, 'liquidity_below_min': 5855996, 'negative_expected_net': 1755311, 'borrow_bound_too_small': 8579, 'cycle_budget_exhausted': 3638, 'unquotable': 1894, 'pool_quarantined': 588}
- Enregistrements de la session : 1756092 ; net attendu > 0 : 2409 ; simulés (eth_call de la vraie tx) : 130 (ok 95, échec 35) ; étiquettes ghost N+1 : 59/105 positives
- Décisions : {'REJECTED': 1756092} ; motifs de rejet : {'below_safety_margin': 1897, 'negative_expected_net': 1753683, 'p_lower_below_threshold': 2364, 'reliability_not_demonstrated': 45, 'sim_below_estimate': 28, 'simulated_net_nonpositive': 13, 'simulation_failed': 35, 'stale_data': 81}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 56677148 | cbBTC→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.030308 cbBTC | 0.000005 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000005 cbBTC (0.3542 €) | — | 1.78 | 0.270 (n=1623) | REJECTED | below_safety_margin(540<606), p_lower_below_threshold(0.27<0.75) |
| 56677148 | WETH→[pancakeswap_v3]→cbBTC→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 1.097479 WETH | 0.000195 WETH | 0.000000 WETH | 0.000003 WETH | 0.000191 WETH (0.3541 €) | — | 1.74 | 0.270 (n=1623) | REJECTED | below_safety_margin(191188791380326<219495888234063), p_lower_below_threshold(0.27<0.75) |
| 56677148 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[uniswap_v3]→USDC | 2,198.589497 USDC | 0.391142 USDC | 0.000000 USDC | 0.006683 USDC | 0.384459 USDC (0.3537 €) | — | 1.75 | 0.270 (n=1623) | REJECTED | below_safety_margin(384459<439717), p_lower_below_threshold(0.27<0.75) |
| 56727627 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→cbBTC | 0.019339 cbBTC | 0.000004 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000003 cbBTC (0.2260 €) | — | 1.79 | 0.109 (n=376) | REJECTED | below_safety_margin(347<386), stale_data(4274ms>4000.0), p_lower_below_threshold(0.11<0.75) |
| 56727627 | USDC→[uniswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 1,404.050425 USDC | 0.249504 USDC | 0.000000 USDC | 0.004556 USDC | 0.244948 USDC (0.2254 €) | — | 1.74 | 0.109 (n=376) | REJECTED | below_safety_margin(244948<280810), stale_data(4272ms>4000.0), p_lower_below_threshold(0.11<0.75) |
| 56677148 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.015874 cbBTC | 0.000003 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000003 cbBTC (0.1987 €) | — | 1.91 | 0.160 (n=43) | REJECTED | below_safety_margin(303<317), p_lower_below_threshold(0.16<0.75) |
| 56677148 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.585107 WETH | 0.000111 WETH | 0.000000 WETH | 0.000003 WETH | 0.000107 WETH (0.1987 €) | — | 1.83 | 0.160 (n=43) | REJECTED | below_safety_margin(107287155161607<117021453991468), p_lower_below_threshold(0.16<0.75) |
| 56677148 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 1,167.904486 USDC | 0.222474 USDC | 0.000000 USDC | 0.006990 USDC | 0.215484 USDC (0.1982 €) | — | 1.85 | 0.160 (n=43) | REJECTED | below_safety_margin(215484<233580), p_lower_below_threshold(0.16<0.75) |
| 56677148 | WETH→[pancakeswap_v3]→cbBTC→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.370292 WETH | 0.000078 WETH | 0.000000 WETH | 0.000003 WETH | 0.000075 WETH (0.1398 €) | 0.000075 WETH | 2.04 | 0.270 (n=1623) | REJECTED | p_lower_below_threshold(0.27<0.75) |
| 56677148 | cbBTC→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC | 0.009892 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1397 €) | — | 2.15 | 0.270 (n=1623) | REJECTED | p_lower_below_threshold(0.27<0.75) |
| 56677148 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC→[uniswap_v3]→USDC | 748.414263 USDC | 0.157752 USDC | 0.000000 USDC | 0.006070 USDC | 0.151682 USDC (0.1395 €) | — | 2.03 | 0.270 (n=1623) | REJECTED | p_lower_below_threshold(0.27<0.75) |
| 56677148 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC | 0.008219 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1213 €) | — | 2.25 | 0.270 (n=1623) | REJECTED | p_lower_below_threshold(0.27<0.75) |
| 56677148 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.293220 WETH | 0.000069 WETH | 0.000000 WETH | 0.000003 WETH | 0.000065 WETH (0.1211 €) | 0.000065 WETH | 2.23 | 0.270 (n=1623) | REJECTED | p_lower_below_threshold(0.27<0.75) |
| 56677148 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 601.157797 USDC | 0.137720 USDC | 0.000000 USDC | 0.006377 USDC | 0.131343 USDC (0.1208 €) | — | 2.18 | 0.270 (n=1623) | REJECTED | p_lower_below_threshold(0.27<0.75) |
| 56677234 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.010581 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0878 €) | — | 1.27 | 0.160 (n=43) | REJECTED | below_safety_margin(134<211), p_lower_below_threshold(0.16<0.75) |
| 56677234 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.388869 WETH | 0.000050 WETH | 0.000000 WETH | 0.000003 WETH | 0.000047 WETH (0.0874 €) | — | 1.21 | 0.160 (n=43) | REJECTED | below_safety_margin(47182464725528<77773711888424), p_lower_below_threshold(0.16<0.75) |
| 56677234 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 792.635195 USDC | 0.100822 USDC | 0.000000 USDC | 0.006373 USDC | 0.094449 USDC (0.0869 €) | — | 1.19 | 0.160 (n=43) | REJECTED | below_safety_margin(94449<158527), p_lower_below_threshold(0.16<0.75) |
| 56696663 | USDC→[pancakeswap_v3]→PLAY→[aerodrome_slipstream]→USDC | 55.878831 USDC | 0.093674 USDC | 0.000000 USDC | 0.004522 USDC | 0.089152 USDC (0.0820 €) | 0.089152 USDC | 15.95 | 0.012 (n=122) | REJECTED | p_lower_below_threshold(0.01<0.75) |
| 56707187 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC | 0.006282 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0704 €) | — | 1.72 | 0.273 (n=1634) | REJECTED | below_safety_margin(108<125), p_lower_below_threshold(0.27<0.75) |
| 56707187 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.239974 WETH | 0.000041 WETH | 0.000000 WETH | 0.000003 WETH | 0.000038 WETH (0.0704 €) | — | 1.59 | 0.273 (n=1634) | REJECTED | below_safety_margin(38159006957051<47994850780449), p_lower_below_threshold(0.27<0.75) |
| 56707187 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 474.298777 USDC | 0.082875 USDC | 0.000000 USDC | 0.006335 USDC | 0.076540 USDC (0.0704 €) | — | 1.61 | 0.273 (n=1634) | REJECTED | below_safety_margin(76540<94859), p_lower_below_threshold(0.27<0.75) |
| 56703766 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 27.586242 USDC | 0.082224 USDC | 0.000000 USDC | 0.006029 USDC | 0.076195 USDC (0.0701 €) | — | 27.62 | 0.040 (n=71) | REJECTED | p_lower_below_threshold(0.04<0.75) |
| 56703766 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.013774 WETH | 0.000041 WETH | 0.000000 WETH | 0.000003 WETH | 0.000038 WETH (0.0700 €) | — | 27.54 | 0.040 (n=71) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.04<0.75) |
| 56703766 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 27.229597 USDC | 0.079756 USDC | 0.000000 USDC | 0.006029 USDC | 0.073727 USDC (0.0678 €) | — | 27.08 | 0.087 (n=68) | REJECTED | p_lower_below_threshold(0.09<0.75) |
| 56703766 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.013596 WETH | 0.000040 WETH | 0.000000 WETH | 0.000003 WETH | 0.000037 WETH (0.0677 €) | — | 27.00 | 0.087 (n=68) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.09<0.75) |

## Fiabilité et décision
- Observations ghost : 8573 ; taux observé 0.227 ; borne inférieure crédible (0.9) 0.221 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 22.1% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ✅ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
