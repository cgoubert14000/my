# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-10T07:21:36+00:00 ; durée 271.08 min ; blocs 55443239 → 55524539 (13590 vus)

## Connexion
- Requêtes RPC : 165477 ; erreurs : 115 ; latence p50/p95 : 374.9/1,979.7 ms
- Rafraîchissements d'état : 13590 ; âge des données au dernier bloc : 6.54 s ; changements de frais LP observés (pools à frais dynamiques) : 4886
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 1616 ; cycles déclenchés par événement : 581 ; avance médiane sur le rafraîchissement multicall : 294 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,119.14 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 465 pools, 270 jetons, 17662 routes
- Par DEX : uniswap_v3 133, aerodrome_slipstream 99, aerodrome 191, pancakeswap_v3 28, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 166 (rejetés 2) → 571 jetons ; pools candidats 3655 (énumérés 287, par paires 0), mesurés 467, sous le plancher de 10000.0 $ : 2 → gardés 465 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'DAI': 1.0, 'USDC': 1.0, 'WETH': 2121.500856, 'cbBTC': 74826.515907, 'AERO': 0.554783}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 139,561,276 | 2,119.135105 | 55524540 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,610,056 | 0.028354 | 55524540 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,371,249 | 0.000013 | 55524540 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 8,820,983 | 0.028376 | 55524540 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 7,484,795 | 2,117.425669 | 55524540 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,294,600 | 98.541536 | 55524540 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,952,114 | 0.028363 | 55524540 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 4,401,033 | 1.767042 | 55524540 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,029,173 | 2,118.032370 | 55524540 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,929,820 | 1.000001 | 55524540 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,112,977 | 43,369.114771 | 55524540 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 150 | 3,016,267 | 2,118.132373 | 55524540 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,338,947 | 0.028353 | 55524540 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 2,020,790 | 1,114,733.552638 | 55524540 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,706,331 | 0.000013 | 55524540 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | USDC/cbBTC | 448 | 1,682,188 | 0.000013 | 55524540 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | XDP/USDC | 100 | 1,617,518 | 0.016323 | 55524540 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,555,918 | 0.000000 | 55524540 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,552,104 | 0.006531 | 55524540 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,502,299 | 0.000013 | 55524540 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,460,908 | 423.448720 | 55524540 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,456,369 | 0.821434 | 55524540 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,424,441 | 1.429325 | 55524540 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | WETH/AERO | 3000 | 1,299,516 | 3,739.289856 | 55524540 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v2 | WETH/USDC | 3000 | 1,290,604 | 2,119.374133 | 55524540 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,248,945 | 14,953.037714 | 55524540 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/USDC | 3000 | 1,218,936 | 2,120.585640 | 55524540 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome | USDC/SEND | 3000 | 1,106,841 | 79.317450 | 55524540 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,079,647 | 2,117.415011 | 55524540 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | WETH/doginme | 10000 | 1,052,294 | 35,778,394.576886 | 55524540 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/VVV | 10000 | 976,287 | 98.537388 | 55524540 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/BRETT | 10000 | 965,256 | 568,566.494479 | 55524540 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | USDC/VVV | 3000 | 963,411 | 0.046609 | 55524540 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome_slipstream | USDC/VELVET | 100 | 958,373 | 21.500248 | 55524540 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 935,821 | 0.001510 | 55524540 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| uniswap_v3 | WETH/TOSHI | 10000 | 932,336 | 23,039,733.174810 | 55524540 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/cbBTC | 340 | 928,141 | 0.000013 | 55524540 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/NOCK | 3000 | 922,045 | 73.706223 | 55524540 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/MORPHO | 3000 | 902,967 | 1,039.106126 | 55524540 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | DRB/WETH | 10000 | 900,656 | 0.000000 | 55524540 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/USDC | 10000 | 890,613 | 2,127.157274 | 55524540 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome | WETH/EDEL | 7000 | 809,677 | 104,432.770297 | 55524540 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 771,943 | 21.994566 | 55524540 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 762,548 | 0.051879 | 55524540 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/AERO | 10000 | 740,615 | 3,765.018600 | 55524540 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | WETH/wstETH | 3000 | 719,431 | 0.798536 | 55524540 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 664,808 | 0.544683 | 55524540 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 656,115 | 4,938,453.619412 | 55524540 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 648,234 | 0.527686 | 55524540 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 615,115 | 0.000008 | 55524540 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v2 | WETH/NPC | 3000 | 608,544 | 153,455.377702 | 55524540 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome | VIRTUAL/WETH | 10000 | 595,487 | 0.000256 | 55524540 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 590,467 | 566,174.257533 | 55524540 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | FLOCK/USDC | 3000 | 569,652 | 0.038751 | 55524540 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 510,862 | 1,039.081502 | 55524540 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome | WETH/DRV | 3000 | 497,744 | 6,647.235765 | 55524540 | `0xaC4e562d7C6108f971321F14238E24AE2cC398ac` |
| uniswap_v3 | USDC/USDT | 100 | 496,944 | 1.001047 | 55524540 | `0xD56da2B74bA826f19015E6B7Dd9Dae1903E85DA1` |
| aerodrome | WETH/msETH (stable) | 500 | 494,667 | 2.402660 | 55524540 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | WETH/uSOL | 3000 | 467,468 | 24.740295 | 55524540 | `0xab04A352D4EC8d0F1812A4E5EBe7807Fa67acD48` |
| uniswap_v3 | WETH/UNI | 10000 | 461,242 | 300.635888 | 55524540 | `0xAb365f161Dd501473a1ff0D2ef0dCE94E7398839` |

## Recherche d'opportunités
- Cycles : 14169 ; routes examinées : 250252878 ; candidats optimisés : 789578 ; net attendu > 0 : 394 ; dernier cycle 221.7 ms
- Rejets (moteur) : {'spread_below_threshold': 245336962, 'liquidity_below_min': 4094099, 'negative_expected_net': 789184, 'borrow_bound_too_small': 25640, 'cycle_budget_exhausted': 6210, 'pool_quarantined': 384}
- Enregistrements de la session : 789537 ; net attendu > 0 : 394 ; simulés (eth_call de la vraie tx) : 69 (ok 40, échec 29) ; étiquettes ghost N+1 : 12/57 positives
- Décisions : {'REJECTED': 789537} ; motifs de rejet : {'below_safety_margin': 288, 'negative_expected_net': 789143, 'p_lower_below_threshold': 394, 'sim_below_estimate': 1, 'simulated_net_nonpositive': 1, 'simulation_failed': 29, 'stale_data': 88}

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
- Observations ghost : 7260 ; taux observé 0.187 ; borne inférieure crédible (0.9) 0.181 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 18.1% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ✅ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
