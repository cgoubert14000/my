# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-10T08:03:01+00:00 ; durée 312.49 min ; blocs 55443239 → 55536948 (15561 vus)

## Connexion
- Requêtes RPC : 190212 ; erreurs : 115 ; latence p50/p95 : 321.7/1,824.3 ms
- Rafraîchissements d'état : 15561 ; âge des données au dernier bloc : 7.84 s ; changements de frais LP observés (pools à frais dynamiques) : 5688
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 3819 ; cycles déclenchés par événement : 1172 ; avance médiane sur le rafraîchissement multicall : 265 ms
- Gaz : base fee 0.005001 gwei ; prix ETH (pool le plus profond) : 2,116.75 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 465 pools, 270 jetons, 17662 routes
- Par DEX : uniswap_v3 133, aerodrome_slipstream 99, aerodrome 191, pancakeswap_v3 28, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 166 (rejetés 2) → 571 jetons ; pools candidats 3655 (énumérés 287, par paires 0), mesurés 467, sous le plancher de 10000.0 $ : 2 → gardés 465 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'DAI': 1.0, 'USDC': 1.0, 'WETH': 2121.500856, 'cbBTC': 74826.515907, 'AERO': 0.554783}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 139,032,611 | 2,116.750062 | 55536977 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,597,318 | 0.028270 | 55536977 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,382,494 | 0.000013 | 55536977 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 8,817,978 | 0.028336 | 55536977 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 7,478,973 | 2,114.555052 | 55536977 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,273,056 | 98.903186 | 55536977 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,962,037 | 0.028276 | 55536977 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 4,406,361 | 1.762772 | 55536977 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,026,855 | 2,115.096702 | 55536977 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,937,038 | 1.000001 | 55536977 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,108,766 | 43,388.869411 | 55536977 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 150 | 3,013,037 | 2,115.003161 | 55536977 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2530 | 2,337,503 | 0.028328 | 55536977 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 2,018,515 | 1,114,733.552638 | 55536977 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,710,994 | 0.000013 | 55536977 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | USDC/cbBTC | 400 | 1,684,440 | 0.000013 | 55536977 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | XDP/USDC | 100 | 1,617,450 | 0.016322 | 55536977 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,554,167 | 0.000000 | 55536977 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,544,403 | 0.006501 | 55536977 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,503,977 | 0.000013 | 55536977 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,459,608 | 423.107097 | 55536977 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,456,220 | 0.821434 | 55536977 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,424,441 | 1.429325 | 55536977 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | WETH/AERO | 3000 | 1,300,922 | 3,731.880340 | 55536977 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v2 | WETH/USDC | 3000 | 1,289,879 | 2,116.618797 | 55536977 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,250,076 | 14,968.867795 | 55536977 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/USDC | 3000 | 1,218,250 | 2,116.457392 | 55536977 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome | USDC/SEND | 3000 | 1,106,841 | 79.317450 | 55536977 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,076,856 | 2,114.398946 | 55536977 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | WETH/doginme | 10000 | 1,052,151 | 35,672,756.012871 | 55536977 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/VVV | 10000 | 973,662 | 98.537376 | 55536977 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/BRETT | 10000 | 964,173 | 568,560.795721 | 55536977 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome_slipstream | USDC/VELVET | 100 | 961,411 | 21.282438 | 55536977 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | USDC/VVV | 3000 | 960,169 | 0.046698 | 55536977 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 936,447 | 0.001507 | 55536977 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| uniswap_v3 | WETH/TOSHI | 10000 | 931,287 | 23,039,733.174810 | 55536977 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/cbBTC | 330 | 929,677 | 0.000013 | 55536977 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/NOCK | 3000 | 922,073 | 73.701734 | 55536977 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/MORPHO | 3000 | 905,219 | 1,038.115414 | 55536977 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | DRB/WETH | 10000 | 899,642 | 0.000000 | 55536977 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/USDC | 10000 | 886,997 | 2,127.157333 | 55536977 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome | WETH/EDEL | 7000 | 808,964 | 104,381.564712 | 55536977 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome_slipstream | USDC/SAPIEN | 4525 | 774,699 | 21.885245 | 55536977 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 764,402 | 0.052140 | 55536977 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/AERO | 10000 | 741,095 | 3,752.968754 | 55536977 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | WETH/wstETH | 3000 | 718,622 | 0.798536 | 55536977 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 664,188 | 0.544126 | 55536977 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 655,377 | 4,938,453.619412 | 55536977 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 648,234 | 0.527686 | 55536977 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 616,500 | 0.000008 | 55536977 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v2 | WETH/NPC | 3000 | 608,413 | 153,176.514170 | 55536977 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome | VIRTUAL/WETH | 10000 | 594,817 | 0.000256 | 55536977 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/BRETT | 2174 | 589,812 | 563,473.887714 | 55536977 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | FLOCK/USDC | 3000 | 569,465 | 0.038731 | 55536977 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome_slipstream | WETH/MORPHO | 2730 | 510,614 | 1,037.789698 | 55536977 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome | WETH/DRV | 3000 | 495,388 | 6,695.526997 | 55536977 | `0xaC4e562d7C6108f971321F14238E24AE2cC398ac` |
| aerodrome | WETH/msETH (stable) | 500 | 494,853 | 2.397327 | 55536977 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | WETH/uSOL | 3000 | 466,947 | 24.739805 | 55536977 | `0xab04A352D4EC8d0F1812A4E5EBe7807Fa67acD48` |
| uniswap_v3 | WETH/UNI | 10000 | 460,769 | 300.551982 | 55536977 | `0xAb365f161Dd501473a1ff0D2ef0dCE94E7398839` |
| pancakeswap_v3 | ELSA/USDC | 100 | 460,046 | 0.066068 | 55536977 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |

## Recherche d'opportunités
- Cycles : 16732 ; routes examinées : 295520584 ; candidats optimisés : 938254 ; net attendu > 0 : 603 ; dernier cycle 198.5 ms
- Rejets (moteur) : {'spread_below_threshold': 289697035, 'liquidity_below_min': 4849235, 'negative_expected_net': 937651, 'borrow_bound_too_small': 28203, 'cycle_budget_exhausted': 7473, 'pool_quarantined': 384}
- Enregistrements de la session : 938254 ; net attendu > 0 : 603 ; simulés (eth_call de la vraie tx) : 95 (ok 42, échec 53) ; étiquettes ghost N+1 : 17/76 positives
- Décisions : {'REJECTED': 938254} ; motifs de rejet : {'below_safety_margin': 400, 'negative_expected_net': 937651, 'p_lower_below_threshold': 591, 'reliability_not_demonstrated': 12, 'sim_below_estimate': 1, 'simulated_net_nonpositive': 1, 'simulation_failed': 53, 'stale_data': 184}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 55511896 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 67.539978 USDC | 0.132058 USDC | 0.000000 USDC | 0.004758 USDC | 0.127300 USDC (0.1171 €) | 0.127300 USDC | 18.85 | 0.007 (n=112) | REJECTED | p_lower_below_threshold(0.01<0.75) |
| 55465617 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.458007 WETH | 0.000054 WETH | 0.000000 WETH | 0.000003 WETH | 0.000051 WETH (0.0992 €) | — | 1.11 | 0.045 (n=32) | REJECTED | below_safety_margin(51040225282314<91601383649938), p_lower_below_threshold(0.05<0.75) |
| 55465617 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 983.919980 USDC | 0.114152 USDC | 0.000000 USDC | 0.006348 USDC | 0.107804 USDC (0.0992 €) | — | 1.10 | 0.045 (n=32) | REJECTED | below_safety_margin(107804<196783), p_lower_below_threshold(0.05<0.75) |
| 55465617 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.011247 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0987 €) | — | 1.28 | 0.045 (n=32) | REJECTED | below_safety_margin(144<224), p_lower_below_threshold(0.05<0.75) |
| 55463862 | USDC→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC | 2,704.783190 USDC | 0.097259 USDC | 0.000000 USDC | 0.005065 USDC | 0.092194 USDC (0.0848 €) | — | 0.34 | 0.051 (n=100) | REJECTED | below_safety_margin(92194<540956), p_lower_below_threshold(0.05<0.75) |
| 55463863 | USDC→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC | 2,704.783190 USDC | 0.097259 USDC | 0.000000 USDC | 0.005065 USDC | 0.092194 USDC (0.0848 €) | — | 0.34 | 0.051 (n=100) | REJECTED | below_safety_margin(92194<540956), p_lower_below_threshold(0.05<0.75) |
| 55513910 | USDC→[pancakeswap_v3]→PLAY→[aerodrome_slipstream]→USDC | 56.425773 USDC | 0.091265 USDC | 0.000000 USDC | 0.004758 USDC | 0.086507 USDC (0.0796 €) | — | 15.33 | 0.007 (n=113) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.01<0.75) |
| 55508170 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.010998 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0790 €) | — | 1.05 | 0.045 (n=32) | REJECTED | below_safety_margin(115<219), stale_data(4363ms>4000.0), p_lower_below_threshold(0.05<0.75) |
| 55508144 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.419143 WETH | 0.000043 WETH | 0.000000 WETH | 0.000003 WETH | 0.000040 WETH (0.0788 €) | — | 0.96 | 0.045 (n=32) | REJECTED | below_safety_margin(40405752388938<83828607238697), p_lower_below_threshold(0.05<0.75) |
| 55508170 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.404590 WETH | 0.000043 WETH | 0.000000 WETH | 0.000003 WETH | 0.000040 WETH (0.0787 €) | — | 1.00 | 0.045 (n=32) | REJECTED | below_safety_margin(40364654888878<80918034635010), stale_data(4353ms>4000.0), p_lower_below_threshold(0.05<0.75) |
| 55508170 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 895.031620 USDC | 0.091868 USDC | 0.000000 USDC | 0.006368 USDC | 0.085500 USDC (0.0787 €) | — | 0.96 | 0.045 (n=32) | REJECTED | below_safety_margin(85500<179006), stale_data(4374ms>4000.0), p_lower_below_threshold(0.05<0.75) |
| 55508144 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 847.524390 USDC | 0.091642 USDC | 0.000000 USDC | 0.006368 USDC | 0.085274 USDC (0.0785 €) | — | 1.01 | 0.045 (n=32) | REJECTED | below_safety_margin(85274<169504), p_lower_below_threshold(0.05<0.75) |
| 55508144 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.010732 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0783 €) | — | 1.06 | 0.045 (n=32) | REJECTED | below_safety_margin(114<214), p_lower_below_threshold(0.05<0.75) |
| 55459979 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.006065 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0514 €) | — | 1.24 | 0.223 (n=1341) | REJECTED | below_safety_margin(75<121), p_lower_below_threshold(0.22<0.75) |
| 55459979 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.210935 WETH | 0.000029 WETH | 0.000000 WETH | 0.000003 WETH | 0.000026 WETH (0.0514 €) | — | 1.25 | 0.223 (n=1341) | REJECTED | below_safety_margin(26442096607397<42186974098195), p_lower_below_threshold(0.22<0.75) |
| 55459979 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 480.224630 USDC | 0.061911 USDC | 0.000000 USDC | 0.006357 USDC | 0.055554 USDC (0.0511 €) | — | 1.16 | 0.223 (n=1341) | REJECTED | below_safety_margin(55554<96044), p_lower_below_threshold(0.22<0.75) |
| 55488168 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→AERO→[pancakeswap_v3]→WETH | 0.055380 WETH | 0.000029 WETH | 0.000000 WETH | 0.000003 WETH | 0.000026 WETH (0.0508 €) | 0.000026 WETH | 4.71 | 0.177 (n=1054) | REJECTED | stale_data(4319ms>4000.0), p_lower_below_threshold(0.18<0.75) |
| 55488168 | cbBTC→[aerodrome_slipstream]→AERO→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.001485 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0508 €) | — | 4.98 | 0.177 (n=1054) | REJECTED | stale_data(4326ms>4000.0), p_lower_below_threshold(0.18<0.75) |
| 55458728 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.296270 WETH | 0.000029 WETH | 0.000000 WETH | 0.000003 WETH | 0.000026 WETH (0.0505 €) | — | 0.88 | 0.045 (n=32) | REJECTED | below_safety_margin(25940610593474<59253963621889), p_lower_below_threshold(0.05<0.75) |
| 55458728 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 609.191657 USDC | 0.061105 USDC | 0.000000 USDC | 0.006554 USDC | 0.054551 USDC (0.0502 €) | — | 0.90 | 0.045 (n=32) | REJECTED | below_safety_margin(54551<121838), p_lower_below_threshold(0.05<0.75) |
| 55458728 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.007392 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0501 €) | — | 0.99 | 0.045 (n=32) | REJECTED | below_safety_margin(73<147), p_lower_below_threshold(0.05<0.75) |
| 55464395 | USDC→[pancakeswap_v3]→ICNT→[uniswap_v3]→USDC | 70.085432 USDC | 0.057836 USDC | 0.000000 USDC | 0.004744 USDC | 0.053092 USDC (0.0488 €) | — | 7.58 | 0.048 (n=437) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.05<0.75) |
| 55465617 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 341.310763 USDC | 0.051891 USDC | 0.000000 USDC | 0.006348 USDC | 0.045543 USDC (0.0419 €) | — | 1.33 | 0.045 (n=32) | REJECTED | below_safety_margin(45543<68262), p_lower_below_threshold(0.05<0.75) |
| 55465617 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.004404 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0418 €) | — | 1.39 | 0.045 (n=32) | REJECTED | below_safety_margin(61<88), p_lower_below_threshold(0.05<0.75) |
| 55465617 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.164679 WETH | 0.000024 WETH | 0.000000 WETH | 0.000003 WETH | 0.000021 WETH (0.0415 €) | — | 1.30 | 0.045 (n=32) | REJECTED | below_safety_margin(21374389514321<32935798286463), p_lower_below_threshold(0.05<0.75) |

## Fiabilité et décision
- Observations ghost : 7279 ; taux observé 0.187 ; borne inférieure crédible (0.9) 0.181 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 18.1% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
