# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-13T02:08:49+00:00 ; durée 236.77 min ; blocs 56655713 → 56726712 (15010 vus)

## Connexion
- Requêtes RPC : 189234 ; erreurs : 25 ; latence p50/p95 : 241.4/931.1 ms
- Rafraîchissements d'état : 15010 ; âge des données au dernier bloc : 4.49 s ; changements de frais LP observés (pools à frais dynamiques) : 6717
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 11652 ; cycles déclenchés par événement : 4439 ; avance médiane sur le rafraîchissement multicall : 467 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,010.25 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 457 pools, 266 jetons, 14822 routes
- Par DEX : uniswap_v3 133, aerodrome_slipstream 97, aerodrome 187, pancakeswap_v3 27, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 1
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 159 (rejetés 2) → 564 jetons ; pools candidats 3621 (énumérés 282, par paires 0), mesurés 459, sous le plancher de 10000.0 $ : 2 → gardés 457 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'DAI': 1.0, 'USDC': 1.0, 'WETH': 2015.232847, 'cbBTC': 71439.030081, 'AERO': 0.524681}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 132,395,122 | 2,010.249279 | 56726711 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,257,274 | 0.028359 | 56726711 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 8,491,303 | 0.028288 | 56726711 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 7,955,726 | 0.000014 | 56726711 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 6,838,836 | 2,005.928550 | 56726711 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 6,645,037 | 106.628734 | 56726711 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,189,694 | 0.028359 | 56726711 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 4,117,054 | 1.929675 | 56726711 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,104,542 | 2,006.624636 | 56726711 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,733,598 | 0.998722 | 56726711 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 2,999,405 | 42,037.227409 | 56726711 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 146 | 2,796,552 | 2,006.387303 | 56726711 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,146,087 | 0.028302 | 56726711 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 1,876,754 | 1,163,003.281972 | 56726711 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | XDP/USDC | 100 | 1,640,902 | 0.016678 | 56726711 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | USDC/cbBTC | 508 | 1,561,260 | 0.000014 | 56726711 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,558,028 | 0.000014 | 56726711 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,516,815 | 0.000000 | 56726711 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,487,243 | 0.006590 | 56726711 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,463,178 | 0.832833 | 56726711 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,462,624 | 0.000014 | 56726711 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,378,932 | 427.198231 | 56726711 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v2 | WETH/USDC | 3000 | 1,257,365 | 2,010.407106 | 56726711 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| uniswap_v3 | WETH/AERO | 3000 | 1,216,911 | 3,876.745223 | 56726711 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,180,842 | 15,063.466741 | 56726711 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/USDC | 3000 | 1,141,617 | 2,010.623963 | 56726711 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,097,715 | 2,005.937476 | 56726711 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,060,794 | 86.352961 | 56726711 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,045,316 | 1.383900 | 56726711 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | WETH/doginme | 10000 | 1,008,925 | 34,804,497.808386 | 56726711 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome_slipstream | USDC/VELVET | 100 | 980,840 | 20.050445 | 56726711 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/VVV | 10000 | 976,870 | 106.184938 | 56726711 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/BRETT | 10000 | 920,577 | 559,037.718544 | 56726711 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 884,736 | 0.001501 | 56726711 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| uniswap_v3 | WETH/TOSHI | 10000 | 882,242 | 23,179,176.896730 | 56726711 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | USDC/VVV | 3000 | 872,295 | 0.053124 | 56726711 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/MORPHO | 3000 | 868,882 | 999.536389 | 56726711 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/USDC | 10000 | 868,493 | 2,005.198605 | 56726711 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome_slipstream | USDC/cbBTC | 348 | 860,604 | 0.000014 | 56726711 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | DRB/WETH | 10000 | 805,845 | 0.000000 | 56726711 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | USDC/NOCK | 3000 | 768,732 | 79.594463 | 56726711 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| pancakeswap_v3 | QUID/USDC | 100 | 746,906 | 0.049701 | 56726711 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 745,552 | 23.106859 | 56726711 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome | WETH/AERO | 10000 | 683,163 | 3,864.686083 | 56726711 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | WETH/wstETH | 3000 | 681,075 | 0.801801 | 56726711 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 665,003 | 0.527632 | 56726711 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 639,437 | 4,687,349.420170 | 56726711 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 604,319 | 0.459461 | 56726711 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/NPC | 3000 | 579,020 | 152,823.401866 | 56726711 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome | VIRTUAL/WETH | 10000 | 567,604 | 0.000261 | 56726711 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 565,371 | 556,056.492229 | 56726711 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | FLOCK/USDC | 3000 | 560,176 | 0.037947 | 56726711 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome_slipstream | AERO/cbBTC | 1025 | 551,528 | 0.000007 | 56726711 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 485,173 | 1,000.135813 | 56726711 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| pancakeswap_v3 | ELSA/USDC | 100 | 463,982 | 0.066769 | 56726711 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| aerodrome_slipstream | USDC/USDT | 8 | 449,537 | 1.001023 | 56726711 | `0xa41Bc0AFfbA7Fd420d186b84899d7ab2aC57fcD1` |
| uniswap_v3 | USDC/MORPHO | 10000 | 449,379 | 0.495782 | 56726711 | `0x2043B296fFC6b2d3bf4A3F3167d2Afb3B0FBdbEE` |
| uniswap_v3 | WETH/UNI | 10000 | 435,182 | 332.338990 | 56726711 | `0xAb365f161Dd501473a1ff0D2ef0dCE94E7398839` |
| uniswap_v3 | WETH/uSOL | 3000 | 428,160 | 24.904087 | 56726711 | `0xab04A352D4EC8d0F1812A4E5EBe7807Fa67acD48` |
| aerodrome | cbBTC/EDGE | 7000 | 424,051 | 895,401.089970 | 56726711 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |

## Recherche d'opportunités
- Cycles : 19448 ; routes examinées : 288258256 ; candidats optimisés : 1475377 ; net attendu > 0 : 1756 ; dernier cycle 126.2 ms
- Rejets (moteur) : {'spread_below_threshold': 281957989, 'liquidity_below_min': 4813296, 'negative_expected_net': 1473621, 'borrow_bound_too_small': 8430, 'cycle_budget_exhausted': 2334, 'pool_quarantined': 588, 'unquotable': 242}
- Enregistrements de la session : 1475377 ; net attendu > 0 : 1756 ; simulés (eth_call de la vraie tx) : 100 (ok 68, échec 32) ; étiquettes ghost N+1 : 46/80 positives
- Décisions : {'REJECTED': 1475377} ; motifs de rejet : {'below_safety_margin': 1452, 'negative_expected_net': 1473621, 'p_lower_below_threshold': 1721, 'reliability_not_demonstrated': 35, 'sim_below_estimate': 17, 'simulated_net_nonpositive': 10, 'simulation_failed': 32, 'stale_data': 11}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 56677148 | cbBTC→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.030308 cbBTC | 0.000005 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000005 cbBTC (0.3542 €) | — | 1.78 | 0.270 (n=1623) | REJECTED | below_safety_margin(540<606), p_lower_below_threshold(0.27<0.75) |
| 56677148 | WETH→[pancakeswap_v3]→cbBTC→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 1.097479 WETH | 0.000195 WETH | 0.000000 WETH | 0.000003 WETH | 0.000191 WETH (0.3541 €) | — | 1.74 | 0.270 (n=1623) | REJECTED | below_safety_margin(191188791380326<219495888234063), p_lower_below_threshold(0.27<0.75) |
| 56677148 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[uniswap_v3]→USDC | 2,198.589497 USDC | 0.391142 USDC | 0.000000 USDC | 0.006683 USDC | 0.384459 USDC (0.3537 €) | — | 1.75 | 0.270 (n=1623) | REJECTED | below_safety_margin(384459<439717), p_lower_below_threshold(0.27<0.75) |
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
| 56703766 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 27.145960 USDC | 0.079506 USDC | 0.000000 USDC | 0.006029 USDC | 0.073477 USDC (0.0676 €) | — | 27.07 | 0.040 (n=71) | REJECTED | p_lower_below_threshold(0.04<0.75) |
| 56703766 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.013541 WETH | 0.000040 WETH | 0.000000 WETH | 0.000003 WETH | 0.000037 WETH (0.0675 €) | — | 27.02 | 0.040 (n=71) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.04<0.75) |

## Fiabilité et décision
- Observations ghost : 8548 ; taux observé 0.226 ; borne inférieure crédible (0.9) 0.220 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 22.0% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ✅ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
