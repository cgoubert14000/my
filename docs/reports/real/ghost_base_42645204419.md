# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-09T16:21:38+00:00 ; durée 45.85 min ; blocs 55240823 → 55254580 (1825 vus)

## Connexion
- Requêtes RPC : 26667 ; erreurs : 0 ; latence p50/p95 : 362.4/1,512.4 ms
- Rafraîchissements d'état : 1825 ; âge des données au dernier bloc : 6.47 s ; changements de frais LP observés (pools à frais dynamiques) : 1719
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 1283 ; cycles déclenchés par événement : 289 ; avance médiane sur le rafraîchissement multicall : 756 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,138.41 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 473 pools, 274 jetons, 17868 routes
- Par DEX : uniswap_v3 135, aerodrome_slipstream 102, aerodrome 193, pancakeswap_v3 29, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 167 (rejetés 2) → 572 jetons ; pools candidats 3663 (énumérés 293, par paires 0), mesurés 475, sous le plancher de 10000.0 $ : 2 → gardés 473 (max 1500) ; prix des hubs : {'USDC': 1.0, 'USDbC': 1.0, 'DAI': 1.0, 'WETH': 2131.426069, 'cbBTC': 75169.710892, 'AERO': 0.579676}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 140,312,615 | 2,138.411472 | 55254580 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,700,025 | 0.028449 | 55254580 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,362,804 | 0.000013 | 55254580 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 8,791,404 | 0.028437 | 55254580 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 7,361,626 | 2,135.574432 | 55254580 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,285,421 | 100.592762 | 55254580 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,972,344 | 0.028454 | 55254580 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 4,605,100 | 1.728330 | 55254580 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,015,513 | 2,135.443852 | 55254580 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 202 | 3,959,823 | 0.998660 | 55254580 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,129,259 | 43,703.342283 | 55254580 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 150 | 3,042,831 | 2,135.658832 | 55254580 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,376,346 | 0.028430 | 55254580 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 2,008,924 | 1,148,554.063045 | 55254580 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,727,446 | 0.000013 | 55254580 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | USDC/cbBTC | 424 | 1,710,480 | 0.000013 | 55254580 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | XDP/USDC | 100 | 1,593,151 | 0.015894 | 55254580 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,578,627 | 0.006604 | 55254580 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,570,088 | 0.000000 | 55254580 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,516,103 | 0.000013 | 55254580 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,476,122 | 1.418208 | 55254580 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,475,806 | 421.733110 | 55254580 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,459,737 | 0.821800 | 55254580 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,331,990 | 3,687.698548 | 55254580 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v2 | WETH/USDC | 3000 | 1,296,420 | 2,138.619353 | 55254580 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,259,961 | 14,823.887233 | 55254580 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/USDC | 3000 | 1,224,468 | 2,138.848969 | 55254580 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome | USDC/SEND | 3000 | 1,107,257 | 79.257778 | 55254580 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,100,322 | 2,135.590045 | 55254580 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | WETH/doginme | 10000 | 1,054,029 | 36,609,682.691449 | 55254580 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/VVV | 10000 | 1,045,472 | 100.747772 | 55254580 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/BRETT | 10000 | 977,760 | 562,252.567457 | 55254580 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome_slipstream | USDC/VELVET | 100 | 961,430 | 21.290849 | 55254580 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 944,083 | 0.001520 | 55254580 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 336 | 932,104 | 0.000013 | 55254580 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | WETH/TOSHI | 10000 | 929,003 | 23,564,492.550782 | 55254580 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome | USDC/NOCK | 3000 | 917,732 | 74.400518 | 55254580 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/MORPHO | 3000 | 917,048 | 1,024.302381 | 55254580 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | DRB/WETH | 10000 | 915,223 | 0.000000 | 55254580 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/USDC | 10000 | 889,398 | 2,127.924141 | 55254580 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | USDC/VVV | 3000 | 889,161 | 0.047084 | 55254580 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | WETH/EDEL | 7000 | 820,983 | 103,432.304236 | 55254580 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 789,722 | 21.297207 | 55254580 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 772,356 | 0.053260 | 55254580 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/AERO | 10000 | 752,259 | 3,692.738593 | 55254580 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | WETH/wstETH | 3000 | 725,982 | 0.798523 | 55254580 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 674,571 | 0.552239 | 55254580 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 664,887 | 4,896,468.524063 | 55254580 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 648,000 | 0.527352 | 55254580 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 627,974 | 0.000008 | 55254580 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v2 | WETH/NPC | 3000 | 619,384 | 150,834.999669 | 55254580 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome | VIRTUAL/WETH | 10000 | 602,708 | 0.000257 | 55254580 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/BRETT | 2126 | 599,299 | 564,434.072612 | 55254580 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | FLOCK/USDC | 3000 | 576,564 | 0.039484 | 55254580 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome | WETH/msETH (stable) | 500 | 534,757 | 2.393305 | 55254580 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | WETH/MORPHO | 2751 | 521,640 | 1,024.970501 | 55254580 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome | cbBTC/EDGE | 7000 | 511,897 | 916,490.618579 | 55254580 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| uniswap_v3 | USDC/USDT | 100 | 493,745 | 1.000996 | 55254580 | `0xD56da2B74bA826f19015E6B7Dd9Dae1903E85DA1` |
| aerodrome | WETH/DRV | 3000 | 492,431 | 6,915.579571 | 55254580 | `0xaC4e562d7C6108f971321F14238E24AE2cC398ac` |
| pancakeswap_v3 | ELSA/USDC | 100 | 473,810 | 0.068370 | 55254580 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |

## Recherche d'opportunités
- Cycles : 2113 ; routes examinées : 37755084 ; candidats optimisés : 145397 ; net attendu > 0 : 303 ; dernier cycle 323.6 ms
- Rejets (moteur) : {'spread_below_threshold': 37023560, 'liquidity_below_min': 562019, 'negative_expected_net': 145094, 'borrow_bound_too_small': 23967, 'cycle_budget_exhausted': 86}
- Enregistrements de la session : 145396 ; net attendu > 0 : 303 ; simulés (eth_call de la vraie tx) : 28 (ok 22, échec 6) ; étiquettes ghost N+1 : 11/21 positives
- Décisions : {'REJECTED': 145396} ; motifs de rejet : {'below_safety_margin': 249, 'negative_expected_net': 145093, 'p_lower_below_threshold': 271, 'reliability_not_demonstrated': 32, 'sim_below_estimate': 6, 'simulated_net_nonpositive': 3, 'simulation_failed': 6, 'stale_data': 94}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 55246974 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.354201 WETH | 0.000040 WETH | 0.000000 WETH | 0.000003 WETH | 0.000037 WETH (0.0729 €) | — | 1.04 | 0.048 (n=30) | REJECTED | below_safety_margin(36995411685845<70840226028216), stale_data(5713ms>4000.0), p_lower_below_threshold(0.05<0.75) |
| 55246974 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 833.027063 USDC | 0.085597 USDC | 0.000000 USDC | 0.006858 USDC | 0.078739 USDC (0.0724 €) | — | 0.95 | 0.048 (n=30) | REJECTED | below_safety_margin(78739<166605), stale_data(5719ms>4000.0), p_lower_below_threshold(0.05<0.75) |
| 55246974 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.009328 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0721 €) | — | 1.11 | 0.048 (n=30) | REJECTED | below_safety_margin(104<186), stale_data(5726ms>4000.0), p_lower_below_threshold(0.05<0.75) |
| 55253986 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.005697 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0436 €) | — | 1.11 | 0.216 (n=1274) | REJECTED | below_safety_margin(63<113), p_lower_below_threshold(0.22<0.75) |
| 55253986 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.221325 WETH | 0.000025 WETH | 0.000000 WETH | 0.000003 WETH | 0.000022 WETH (0.0435 €) | — | 1.00 | 0.216 (n=1274) | REJECTED | below_safety_margin(22118970982473<44265071018017), p_lower_below_threshold(0.22<0.75) |
| 55253986 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 485.256728 USDC | 0.053353 USDC | 0.000000 USDC | 0.006475 USDC | 0.046878 USDC (0.0431 €) | — | 0.97 | 0.216 (n=1274) | REJECTED | below_safety_margin(46878<97051), p_lower_below_threshold(0.22<0.75) |
| 55253986 | cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.006430 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0408 €) | — | 0.92 | 0.063 (n=307) | REJECTED | below_safety_margin(59<128), p_lower_below_threshold(0.06<0.75) |
| 55253986 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 516.615464 USDC | 0.048879 USDC | 0.000000 USDC | 0.004842 USDC | 0.044037 USDC (0.0405 €) | — | 0.85 | 0.063 (n=307) | REJECTED | below_safety_margin(44037<103323), p_lower_below_threshold(0.06<0.75) |
| 55241295 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.002374 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0345 €) | — | 2.11 | 0.027 (n=11) | REJECTED | stale_data(5044ms>4000.0), reliability_not_demonstrated |
| 55241295 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 178.950424 USDC | 0.042177 USDC | 0.000000 USDC | 0.004920 USDC | 0.037257 USDC (0.0343 €) | 0.037257 USDC | 2.08 | 0.027 (n=11) | REJECTED | stale_data(5041ms>4000.0), reliability_not_demonstrated |
| 55246974 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH | 0.254344 WETH | 0.000019 WETH | 0.000000 WETH | 0.000003 WETH | 0.000016 WETH (0.0313 €) | — | 0.62 | 0.216 (n=1274) | REJECTED | below_safety_margin(15882804364666<50868729122864), stale_data(5776ms>4000.0), p_lower_below_threshold(0.22<0.75) |
| 55246974 | USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 526.304034 USDC | 0.040890 USDC | 0.000000 USDC | 0.006858 USDC | 0.034032 USDC (0.0313 €) | — | 0.65 | 0.216 (n=1274) | REJECTED | below_safety_margin(34032<105260), stale_data(5782ms>4000.0), p_lower_below_threshold(0.22<0.75) |
| 55246974 | cbBTC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.006832 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0312 €) | — | 0.66 | 0.216 (n=1274) | REJECTED | below_safety_margin(45<136), stale_data(5789ms>4000.0), p_lower_below_threshold(0.22<0.75) |
| 55253986 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 554.197285 USDC | 0.037477 USDC | 0.000000 USDC | 0.006475 USDC | 0.031002 USDC (0.0285 €) | — | 0.56 | 0.048 (n=30) | REJECTED | below_safety_margin(31002<110839), p_lower_below_threshold(0.05<0.75) |
| 55253986 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.006040 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0284 €) | — | 0.68 | 0.048 (n=30) | REJECTED | below_safety_margin(41<120), p_lower_below_threshold(0.05<0.75) |
| 55253986 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.274040 WETH | 0.000017 WETH | 0.000000 WETH | 0.000003 WETH | 0.000014 WETH (0.0283 €) | — | 0.52 | 0.048 (n=30) | REJECTED | below_safety_margin(14370286415079<54807926396952), p_lower_below_threshold(0.05<0.75) |
| 55244252 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 512.207636 USDC | 0.034934 USDC | 0.000000 USDC | 0.006871 USDC | 0.028063 USDC (0.0258 €) | — | 0.55 | 0.048 (n=30) | REJECTED | below_safety_margin(28063<102441), p_lower_below_threshold(0.05<0.75) |
| 55244253 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 512.207636 USDC | 0.034934 USDC | 0.000000 USDC | 0.006871 USDC | 0.028063 USDC (0.0258 €) | — | 0.55 | 0.048 (n=30) | REJECTED | below_safety_margin(28063<102441), p_lower_below_threshold(0.05<0.75) |
| 55244252 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.005980 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0256 €) | — | 0.62 | 0.048 (n=30) | REJECTED | below_safety_margin(37<119), p_lower_below_threshold(0.05<0.75) |
| 55244253 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.005980 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0256 €) | — | 0.62 | 0.048 (n=30) | REJECTED | below_safety_margin(37<119), p_lower_below_threshold(0.05<0.75) |
| 55244252 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.223504 WETH | 0.000016 WETH | 0.000000 WETH | 0.000003 WETH | 0.000013 WETH (0.0256 €) | — | 0.58 | 0.048 (n=30) | REJECTED | below_safety_margin(12990862366430<44700750350483), p_lower_below_threshold(0.05<0.75) |
| 55244253 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.223504 WETH | 0.000016 WETH | 0.000000 WETH | 0.000003 WETH | 0.000013 WETH (0.0256 €) | — | 0.58 | 0.048 (n=30) | REJECTED | below_safety_margin(12990862366430<44700750350483), p_lower_below_threshold(0.05<0.75) |
| 55247047 | USDC→[pancakeswap_v3]→ICNT→[uniswap_v3]→USDC | 53.415374 USDC | 0.030798 USDC | 0.000000 USDC | 0.004886 USDC | 0.025912 USDC (0.0238 €) | 0.025912 USDC | 4.85 | 0.048 (n=425) | REJECTED | stale_data(4171ms>4000.0), p_lower_below_threshold(0.05<0.75) |
| 55244252 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH | 0.230315 WETH | 0.000014 WETH | 0.000000 WETH | 0.000003 WETH | 0.000011 WETH (0.0223 €) | — | 0.49 | 0.216 (n=1274) | REJECTED | below_safety_margin(11287587140945<46062925023518), p_lower_below_threshold(0.22<0.75) |
| 55244253 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH | 0.230315 WETH | 0.000014 WETH | 0.000000 WETH | 0.000003 WETH | 0.000011 WETH (0.0223 €) | — | 0.49 | 0.216 (n=1274) | REJECTED | below_safety_margin(11287587140945<46062925023518), p_lower_below_threshold(0.22<0.75) |

## Fiabilité et décision
- Observations ghost : 6933 ; taux observé 0.184 ; borne inférieure crédible (0.9) 0.178 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 17.8% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ✅ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
