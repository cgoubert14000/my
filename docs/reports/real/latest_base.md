# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-09T09:04:26+00:00 ; durée 283.18 min ; blocs 55038467 → 55123334 (8847 vus)

## Connexion
- Requêtes RPC : 134507 ; erreurs : 10 ; latence p50/p95 : 890.7/3,543.4 ms
- Rafraîchissements d'état : 8847 ; âge des données au dernier bloc : 16.56 s ; changements de frais LP observés (pools à frais dynamiques) : 9342
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 14687 ; cycles déclenchés par événement : 3768 ; avance médiane sur le rafraîchissement multicall : 969 ms
- Gaz : base fee 0.005157 gwei ; prix ETH (pool le plus profond) : 2,119.76 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 467 pools, 272 jetons, 17562 routes
- Par DEX : uniswap_v3 134, aerodrome_slipstream 97, aerodrome 194, pancakeswap_v3 28, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 166 (rejetés 2) → 571 jetons ; pools candidats 3664 (énumérés 288, par paires 0), mesurés 469, sous le plancher de 10000.0 $ : 2 → gardés 467 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'DAI': 1.0, 'USDC': 1.0, 'WETH': 2141.212816, 'cbBTC': 74926.035696, 'AERO': 0.58265}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 138,769,333 | 2,119.763271 | 55123394 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,444,287 | 0.028478 | 55123394 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 8,804,746 | 0.000013 | 55123394 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 8,713,049 | 0.028432 | 55123394 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 7,428,214 | 2,123.987458 | 55123394 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,067,650 | 105.031123 | 55123394 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,254,402 | 0.001528 | 55123394 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,580,169 | 0.028477 | 55123394 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 4,569,780 | 1.762505 | 55123394 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,920,468 | 0.998733 | 55123394 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| pancakeswap_v3 | WETH/USDC | 100 | 3,884,354 | 2,124.139619 | 55123394 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | WETH/KTA | 3000 | 3,142,993 | 42,569.947374 | 55123394 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 150 | 2,998,100 | 2,123.954053 | 55123394 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,355,427 | 0.028442 | 55123394 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 1,992,341 | 1,147,475.453732 | 55123394 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 568 | 1,704,868 | 0.000013 | 55123394 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,670,518 | 0.007158 | 55123394 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,647,563 | 0.000013 | 55123394 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | XDP/USDC | 100 | 1,574,354 | 0.015591 | 55123394 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,556,370 | 0.000000 | 55123394 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,476,122 | 1.418208 | 55123394 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,455,366 | 429.252517 | 55123394 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,451,259 | 0.824398 | 55123394 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,444,009 | 0.000013 | 55123394 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v3 | WETH/AERO | 3000 | 1,311,404 | 3,745.573018 | 55123394 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v2 | WETH/USDC | 3000 | 1,290,705 | 2,125.643796 | 55123394 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,238,639 | 15,096.290101 | 55123394 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/USDC | 3000 | 1,220,305 | 2,119.665232 | 55123394 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome | USDC/SEND | 3000 | 1,120,769 | 77.358314 | 55123394 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,093,188 | 2,124.011578 | 55123394 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | WETH/doginme | 10000 | 1,042,460 | 36,865,069.416824 | 55123394 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/VVV | 10000 | 1,007,454 | 105.772511 | 55123394 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/BRETT | 10000 | 954,475 | 588,268.641887 | 55123394 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome_slipstream | USDC/VELVET | 100 | 952,053 | 21.945046 | 55123394 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome_slipstream | USDC/cbBTC | 352 | 923,687 | 0.000013 | 55123394 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | WETH/TOSHI | 10000 | 920,011 | 23,566,542.905991 | 55123394 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | WETH/USDC | 10000 | 910,907 | 2,104.880330 | 55123394 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome | USDC/NOCK | 3000 | 909,072 | 75.824851 | 55123394 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/MORPHO | 3000 | 901,939 | 1,038.678975 | 55123394 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | DRB/WETH | 10000 | 901,421 | 0.000000 | 55123394 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | USDC/VVV | 3000 | 835,113 | 0.049426 | 55123394 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | WETH/EDEL | 7000 | 820,469 | 101,763.703193 | 55123394 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| pancakeswap_v3 | QUID/USDC | 100 | 763,479 | 0.051999 | 55123394 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome_slipstream | USDC/SAPIEN | 4710 | 754,124 | 22.714610 | 55123394 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome | WETH/AERO | 10000 | 742,186 | 3,721.601102 | 55123394 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | WETH/wstETH | 3000 | 717,504 | 0.803308 | 55123394 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 694,396 | 0.535020 | 55123394 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 650,668 | 5,023,762.197650 | 55123394 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 641,730 | 0.521652 | 55123394 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 618,552 | 0.000008 | 55123394 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v2 | WETH/NPC | 3000 | 617,898 | 148,879.308077 | 55123394 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome | VIRTUAL/WETH | 10000 | 590,658 | 0.000251 | 55123394 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/BRETT | 2168 | 580,166 | 581,959.485101 | 55123394 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | FLOCK/USDC | 3000 | 565,461 | 0.038325 | 55123394 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome | WETH/msETH (stable) | 500 | 532,244 | 2.378996 | 55123394 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | WETH/MORPHO | 2718 | 512,374 | 1,038.408340 | 55123394 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome | cbBTC/EDGE | 7000 | 504,070 | 927,041.211116 | 55123394 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| uniswap_v3 | USDC/USDT | 100 | 497,684 | 1.001239 | 55123394 | `0xD56da2B74bA826f19015E6B7Dd9Dae1903E85DA1` |
| pancakeswap_v3 | ELSA/USDC | 100 | 486,313 | 0.070745 | 55123394 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| uniswap_v3 | WETH/USDC | 100 | 483,548 | 2,123.876196 | 55123394 | `0xb4CB800910B228ED3d0834cF79D697127BBB00e5` |

## Recherche d'opportunités
- Cycles : 12614 ; routes examinées : 221527068 ; candidats optimisés : 851326 ; net attendu > 0 : 1836 ; dernier cycle 215.6 ms
- Rejets (moteur) : {'spread_below_threshold': 217440440, 'liquidity_below_min': 3193377, 'negative_expected_net': 849490, 'pool_quarantined': 19570, 'borrow_bound_too_small': 15988, 'cycle_budget_exhausted': 6363, 'unquotable': 4}
- Enregistrements de la session : 851326 ; net attendu > 0 : 1836 ; simulés (eth_call de la vraie tx) : 98 (ok 67, échec 31) ; étiquettes ghost N+1 : 28/88 positives
- Décisions : {'REJECTED': 851326} ; motifs de rejet : {'below_safety_margin': 1622, 'negative_expected_net': 849490, 'p_lower_below_threshold': 1736, 'price_impact': 1, 'reliability_not_demonstrated': 100, 'simulation_failed': 31, 'stale_data': 451}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 55086133 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 1,037.319445 USDC | 0.163176 USDC | 0.000000 USDC | 0.004754 USDC | 0.158422 USDC (0.1457 €) | — | 1.53 | 0.059 (n=299) | REJECTED | below_safety_margin(158422<207463), p_lower_below_threshold(0.06<0.75) |
| 55086133 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.492571 WETH | 0.000077 WETH | 0.000000 WETH | 0.000002 WETH | 0.000075 WETH (0.1456 €) | — | 1.52 | 0.059 (n=299) | REJECTED | below_safety_margin(75025572299617<98514181116913), p_lower_below_threshold(0.06<0.75) |
| 55086134 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 954.319656 USDC | 0.138115 USDC | 0.000000 USDC | 0.004755 USDC | 0.133360 USDC (0.1227 €) | — | 1.40 | 0.059 (n=299) | REJECTED | below_safety_margin(133360<190863), p_lower_below_threshold(0.06<0.75) |
| 55086134 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.452882 WETH | 0.000065 WETH | 0.000000 WETH | 0.000002 WETH | 0.000063 WETH (0.1225 €) | — | 1.39 | 0.059 (n=299) | REJECTED | below_safety_margin(63154959045858<90576387333474), p_lower_below_threshold(0.06<0.75) |
| 55097311 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 494.995900 USDC | 0.122524 USDC | 0.000000 USDC | 0.006295 USDC | 0.116229 USDC (0.1069 €) | 0.116229 USDC | 2.35 | 0.204 (n=1222) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 55097311 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.236674 WETH | 0.000059 WETH | 0.000000 WETH | 0.000003 WETH | 0.000056 WETH (0.1068 €) | 0.000056 WETH | 2.35 | 0.204 (n=1222) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 55097311 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.006640 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1067 €) | 0.000002 cbBTC | 2.36 | 0.204 (n=1222) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 55045434 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.355434 WETH | 0.000047 WETH | 0.000000 WETH | 0.000003 WETH | 0.000044 WETH (0.0857 €) | — | 1.22 | 0.048 (n=30) | REJECTED | below_safety_margin(43516011434452<71086872293656), p_lower_below_threshold(0.05<0.75) |
| 55045434 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.355434 WETH | 0.000047 WETH | 0.000000 WETH | 0.000003 WETH | 0.000044 WETH (0.0857 €) | — | 1.22 | 0.048 (n=30) | REJECTED | below_safety_margin(43516011434452<71086872293656), p_lower_below_threshold(0.05<0.75) |
| 55045434 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 732.198649 USDC | 0.099587 USDC | 0.000000 USDC | 0.006433 USDC | 0.093154 USDC (0.0857 €) | — | 1.27 | 0.048 (n=30) | REJECTED | below_safety_margin(93154<146439), p_lower_below_threshold(0.05<0.75) |
| 55045434 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 732.198649 USDC | 0.099587 USDC | 0.000000 USDC | 0.006433 USDC | 0.093154 USDC (0.0857 €) | — | 1.27 | 0.048 (n=30) | REJECTED | below_safety_margin(93154<146439), p_lower_below_threshold(0.05<0.75) |
| 55045434 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.009259 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0855 €) | — | 1.34 | 0.048 (n=30) | REJECTED | below_safety_margin(124<185), p_lower_below_threshold(0.05<0.75) |
| 55045434 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.009259 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0855 €) | — | 1.34 | 0.048 (n=30) | REJECTED | below_safety_margin(124<185), p_lower_below_threshold(0.05<0.75) |
| 55073953 | USDC→[pancakeswap_v3]→ICNT→[uniswap_v3]→USDC | 88.285333 USDC | 0.083463 USDC | 0.000000 USDC | 0.004818 USDC | 0.078645 USDC (0.0724 €) | — | 8.91 | 0.007 (n=109) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.01<0.75) |
| 55045434 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.006493 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0690 €) | — | 1.54 | 0.204 (n=1207) | REJECTED | below_safety_margin(100<129), p_lower_below_threshold(0.20<0.75) |
| 55045434 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.006493 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0690 €) | — | 1.54 | 0.204 (n=1207) | REJECTED | below_safety_margin(100<129), p_lower_below_threshold(0.20<0.75) |
| 55045434 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 501.136491 USDC | 0.080969 USDC | 0.000000 USDC | 0.006433 USDC | 0.074536 USDC (0.0686 €) | — | 1.49 | 0.204 (n=1207) | REJECTED | below_safety_margin(74536<100227), p_lower_below_threshold(0.20<0.75) |
| 55045434 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 501.136491 USDC | 0.080969 USDC | 0.000000 USDC | 0.006433 USDC | 0.074536 USDC (0.0686 €) | — | 1.49 | 0.204 (n=1207) | REJECTED | below_safety_margin(74536<100227), p_lower_below_threshold(0.20<0.75) |
| 55045434 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.226863 WETH | 0.000038 WETH | 0.000000 WETH | 0.000003 WETH | 0.000035 WETH (0.0684 €) | — | 1.53 | 0.204 (n=1207) | REJECTED | below_safety_margin(34746748358204<45372651029136), p_lower_below_threshold(0.20<0.75) |
| 55045434 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.226863 WETH | 0.000038 WETH | 0.000000 WETH | 0.000003 WETH | 0.000035 WETH (0.0684 €) | — | 1.53 | 0.204 (n=1207) | REJECTED | below_safety_margin(34746748358204<45372651029136), p_lower_below_threshold(0.20<0.75) |
| 55104505 | USDC→[pancakeswap_v3]→ICNT→[uniswap_v3]→USDC | 84.291686 USDC | 0.078899 USDC | 0.000000 USDC | 0.004697 USDC | 0.074202 USDC (0.0683 €) | — | 8.80 | 0.007 (n=110) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.01<0.75) |
| 55104508 | USDC→[pancakeswap_v3]→ICNT→[uniswap_v3]→USDC | 84.291686 USDC | 0.078899 USDC | 0.000000 USDC | 0.004697 USDC | 0.074202 USDC (0.0683 €) | — | 8.80 | 0.007 (n=110) | REJECTED | stale_data(4537ms>4000.0), simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.01<0.75) |
| 55104512 | USDC→[pancakeswap_v3]→ICNT→[uniswap_v3]→USDC | 84.291686 USDC | 0.078899 USDC | 0.000000 USDC | 0.004697 USDC | 0.074202 USDC (0.0683 €) | — | 8.80 | 0.007 (n=110) | REJECTED | stale_data(5284ms>4000.0), simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.01<0.75) |
| 55097311 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.003593 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0469 €) | — | 1.92 | 0.204 (n=1222) | REJECTED | below_safety_margin(69<71), p_lower_below_threshold(0.20<0.75) |
| 55097311 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 257.384523 USDC | 0.057050 USDC | 0.000000 USDC | 0.006295 USDC | 0.050755 USDC (0.0467 €) | — | 1.97 | 0.204 (n=1222) | REJECTED | below_safety_margin(50755<51476), p_lower_below_threshold(0.20<0.75) |

## Fiabilité et décision
- Observations ghost : 6738 ; taux observé 0.177 ; borne inférieure crédible (0.9) 0.171 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 17.1% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ✅ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
