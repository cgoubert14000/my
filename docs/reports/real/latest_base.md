# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-08T05:47:28+00:00 ; durée 330.14 min ; blocs 54533288 → 54632300 (15605 vus)

## Connexion
- Requêtes RPC : 215932 ; erreurs : 13 ; latence p50/p95 : 448.5/1,434.9 ms
- Rafraîchissements d'état : 15605 ; âge des données au dernier bloc : 7.49 s ; changements de frais LP observés (pools à frais dynamiques) : 4550
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 3036 ; cycles déclenchés par événement : 1460 ; avance médiane sur le rafraîchissement multicall : 426 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,231.64 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 470 pools, 276 jetons, 17708 routes
- Par DEX : uniswap_v3 135, aerodrome_slipstream 96, aerodrome 197, pancakeswap_v3 28, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 168 (rejetés 2) → 573 jetons ; pools candidats 3668 (énumérés 291, par paires 0), mesurés 473, sous le plancher de 10000.0 $ : 3 → gardés 470 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDC': 1.0, 'USDbC': 1.0, 'WETH': 2231.621019, 'cbBTC': 75753.631297, 'AERO': 0.627658}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 145,572,989 | 2,231.640699 | 54632327 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,844,217 | 0.029472 | 54632327 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,301,176 | 0.000013 | 54632327 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,152,706 | 0.029508 | 54632327 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 8,085,381 | 2,231.374318 | 54632327 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,272,872 | 110.008029 | 54632327 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,387,442 | 0.001540 | 54632327 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,143,625 | 0.029471 | 54632327 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 4,873,462 | 1.649055 | 54632327 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,185,268 | 2,231.665890 | 54632327 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,985,458 | 0.999186 | 54632327 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,302,798 | 42,726.721107 | 54632327 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 150 | 3,179,078 | 2,231.476032 | 54632327 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,542,181 | 0.029493 | 54632327 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 2,096,783 | 1,148,252.607284 | 54632327 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 412 | 1,737,129 | 0.000013 | 54632327 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,653,042 | 0.000013 | 54632327 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,623,493 | 0.006408 | 54632327 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,615,848 | 0.000000 | 54632327 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,571,163 | 0.015576 | 54632327 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,514,385 | 445.596810 | 54632327 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,503,496 | 0.000013 | 54632327 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,469,421 | 1.434825 | 54632327 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,460,111 | 0.819634 | 54632327 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,392,836 | 3,681.472215 | 54632327 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v2 | WETH/USDC | 3000 | 1,323,920 | 2,235.519413 | 54632327 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome | WETH/USDC | 3000 | 1,294,989 | 2,237.663986 | 54632327 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,257,887 | 15,104.315598 | 54632327 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,182,404 | 2,231.519392 | 54632327 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,123,406 | 76.995559 | 54632327 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,099,453 | 36,637,710.044978 | 54632327 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/VVV | 10000 | 1,032,391 | 109.375209 | 54632327 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,007,465 | 583,700.380599 | 54632327 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | WETH/TOSHI | 10000 | 983,365 | 22,956,173.027576 | 54632327 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/VELVET | 100 | 973,074 | 20.527626 | 54632327 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | DRB/WETH | 10000 | 959,361 | 0.000000 | 54632327 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/USDC | 10000 | 935,579 | 2,228.787514 | 54632327 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 931,007 | 1,068.748465 | 54632327 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome | USDC/NOCK | 3000 | 930,522 | 72.369413 | 54632327 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | USDC/cbBTC | 332 | 924,940 | 0.000013 | 54632327 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | WETH/EDEL | 7000 | 864,267 | 101,646.925288 | 54632327 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | USDC/VVV | 3000 | 808,006 | 0.049244 | 54632327 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | WETH/AERO | 10000 | 788,812 | 3,655.317486 | 54632327 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| pancakeswap_v3 | QUID/USDC | 100 | 783,632 | 0.054902 | 54632327 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 779,381 | 21.683576 | 54632327 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome | WETH/wstETH | 3000 | 757,025 | 0.799805 | 54632327 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 713,253 | 0.561729 | 54632327 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 687,870 | 4,981,770.242484 | 54632327 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome | VIRTUAL/WETH | 10000 | 681,405 | 0.000253 | 54632327 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | TIG/USDC | 10000 | 672,233 | 0.570490 | 54632327 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 656,787 | 0.000008 | 54632327 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v2 | WETH/NPC | 3000 | 638,529 | 154,454.476964 | 54632327 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | WETH/BRETT | 2093 | 613,192 | 588,161.488242 | 54632327 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | FLOCK/USDC | 3000 | 579,907 | 0.039865 | 54632327 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome | WETH/msETH (stable) | 500 | 553,856 | 2.471956 | 54632327 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome | cbBTC/EDGE | 7000 | 521,404 | 897,109.761768 | 54632327 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| aerodrome_slipstream | WETH/MORPHO | 2703 | 521,240 | 1,068.466113 | 54632327 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| uniswap_v3 | WETH/USDC | 100 | 514,115 | 2,231.651153 | 54632327 | `0xb4CB800910B228ED3d0834cF79D697127BBB00e5` |
| aerodrome | WETH/DRV | 3000 | 511,189 | 6,989.104189 | 54632327 | `0xaC4e562d7C6108f971321F14238E24AE2cC398ac` |
| pancakeswap_v3 | ELSA/USDC | 100 | 510,442 | 0.075506 | 54632327 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |

## Recherche d'opportunités
- Cycles : 17064 ; routes examinées : 302169312 ; candidats optimisés : 786390 ; net attendu > 0 : 130 ; dernier cycle 321.8 ms
- Rejets (moteur) : {'spread_below_threshold': 296894153, 'liquidity_below_min': 4480222, 'negative_expected_net': 786260, 'borrow_bound_too_small': 8401, 'cycle_budget_exhausted': 146}
- Enregistrements de la session : 786390 ; net attendu > 0 : 130 ; simulés (eth_call de la vraie tx) : 23 (ok 22, échec 1) ; étiquettes ghost N+1 : 2/22 positives
- Décisions : {'REJECTED': 786390} ; motifs de rejet : {'below_safety_margin': 91, 'negative_expected_net': 786260, 'p_lower_below_threshold': 130, 'sim_below_estimate': 1, 'simulated_net_nonpositive': 1, 'simulation_failed': 1, 'stale_data': 33}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 54565087 | WETH→[aerodrome]→SLC→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.014916 WETH | 0.000020 WETH | 0.000000 WETH | 0.000003 WETH | 0.000017 WETH (0.0347 €) | 0.000017 WETH | 11.35 | 0.128 (n=47) | REJECTED | stale_data(4168ms>4000.0), p_lower_below_threshold(0.13<0.75) |
| 54565087 | USDC→[pancakeswap_v3]→WETH→[aerodrome]→SLC→[uniswap_v3]→USDC | 33.235198 USDC | 0.044155 USDC | 0.000000 USDC | 0.006396 USDC | 0.037759 USDC (0.0347 €) | — | 11.36 | 0.128 (n=47) | REJECTED | stale_data(4171ms>4000.0), p_lower_below_threshold(0.13<0.75) |
| 54565087 | WETH→[aerodrome]→SLC→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.014700 WETH | 0.000019 WETH | 0.000000 WETH | 0.000003 WETH | 0.000016 WETH (0.0334 €) | 0.000016 WETH | 11.08 | 0.065 (n=180) | REJECTED | stale_data(4173ms>4000.0), p_lower_below_threshold(0.06<0.75) |
| 54565087 | USDC→[aerodrome_slipstream]→WETH→[aerodrome]→SLC→[uniswap_v3]→USDC | 32.629907 USDC | 0.042728 USDC | 0.000000 USDC | 0.006396 USDC | 0.036332 USDC (0.0334 €) | — | 11.13 | 0.065 (n=180) | REJECTED | stale_data(4176ms>4000.0), p_lower_below_threshold(0.06<0.75) |
| 54565087 | WETH→[aerodrome]→SLC→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.014543 WETH | 0.000019 WETH | 0.000000 WETH | 0.000003 WETH | 0.000016 WETH (0.0327 €) | 0.000016 WETH | 10.95 | 0.065 (n=180) | REJECTED | stale_data(4178ms>4000.0), p_lower_below_threshold(0.06<0.75) |
| 54565087 | USDC→[uniswap_v3]→WETH→[aerodrome]→SLC→[uniswap_v3]→USDC | 32.289475 USDC | 0.041914 USDC | 0.000000 USDC | 0.006396 USDC | 0.035518 USDC (0.0327 €) | — | 11.00 | 0.065 (n=180) | REJECTED | stale_data(4181ms>4000.0), p_lower_below_threshold(0.06<0.75) |
| 54626322 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 35.752988 USDC | 0.035482 USDC | 0.000000 USDC | 0.005010 USDC | 0.030472 USDC (0.0280 €) | -0.001058 USDC | 8.52 | 0.000 (n=101) | REJECTED | sim_below_estimate(3952<35482), simulated_net_nonpositive, p_lower_below_threshold(0.00<0.75) |
| 54626323 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 35.752988 USDC | 0.035482 USDC | 0.000000 USDC | 0.005010 USDC | 0.030472 USDC (0.0280 €) | — | 8.52 | 0.000 (n=101) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 54591803 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→USDC | 91.760653 USDC | 0.032602 USDC | 0.000000 USDC | 0.007051 USDC | 0.025551 USDC (0.0235 €) | 0.025551 USDC | 2.78 | 0.242 (n=416) | REJECTED | p_lower_below_threshold(0.24<0.75) |
| 54591739 | cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.001311 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0230 €) | 0.000000 cbBTC | 2.52 | 0.243 (n=414) | REJECTED | p_lower_below_threshold(0.24<0.75) |
| 54591803 | cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.001127 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0230 €) | — | 2.93 | 0.242 (n=416) | REJECTED | p_lower_below_threshold(0.24<0.75) |
| 54591739 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→USDC | 111.703344 USDC | 0.031494 USDC | 0.000000 USDC | 0.006713 USDC | 0.024781 USDC (0.0228 €) | 0.024781 USDC | 2.22 | 0.243 (n=414) | REJECTED | p_lower_below_threshold(0.24<0.75) |
| 54591803 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 105.267591 USDC | 0.030797 USDC | 0.000000 USDC | 0.007051 USDC | 0.023746 USDC (0.0218 €) | 0.023746 USDC | 2.26 | 0.182 (n=1068) | REJECTED | p_lower_below_threshold(0.18<0.75) |
| 54591803 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.001058 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0216 €) | — | 2.93 | 0.182 (n=1068) | REJECTED | p_lower_below_threshold(0.18<0.75) |
| 54591739 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.001153 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0188 €) | 0.000000 cbBTC | 2.34 | 0.183 (n=1067) | REJECTED | p_lower_below_threshold(0.18<0.75) |
| 54591803 | cbBTC→[uniswap_v3]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.001052 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0188 €) | — | 2.57 | 0.242 (n=416) | REJECTED | p_lower_below_threshold(0.24<0.75) |
| 54591739 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 102.789696 USDC | 0.027099 USDC | 0.000000 USDC | 0.006713 USDC | 0.020386 USDC (0.0188 €) | — | 1.98 | 0.183 (n=1067) | REJECTED | below_safety_margin(20386<20557), p_lower_below_threshold(0.18<0.75) |
| 54591803 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[uniswap_v3]→USDC | 95.044623 USDC | 0.027437 USDC | 0.000000 USDC | 0.007051 USDC | 0.020386 USDC (0.0188 €) | 0.020386 USDC | 2.14 | 0.242 (n=416) | REJECTED | p_lower_below_threshold(0.24<0.75) |
| 54588088 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→USDC | 85.628475 USDC | 0.027085 USDC | 0.000000 USDC | 0.007044 USDC | 0.020041 USDC (0.0184 €) | 0.020041 USDC | 2.34 | 0.245 (n=412) | REJECTED | p_lower_below_threshold(0.24<0.75) |
| 54588088 | cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.000976 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0181 €) | 0.000000 cbBTC | 2.66 | 0.245 (n=412) | REJECTED | p_lower_below_threshold(0.24<0.75) |
| 54591739 | cbBTC→[uniswap_v3]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.001122 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0146 €) | — | 1.87 | 0.243 (n=414) | REJECTED | below_safety_margin(21<22), p_lower_below_threshold(0.24<0.75) |
| 54591803 | cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.000948 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0146 €) | — | 2.22 | 0.242 (n=416) | REJECTED | p_lower_below_threshold(0.24<0.75) |
| 54591739 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[uniswap_v3]→USDC | 106.007876 USDC | 0.022443 USDC | 0.000000 USDC | 0.006713 USDC | 0.015730 USDC (0.0145 €) | — | 1.48 | 0.243 (n=414) | REJECTED | below_safety_margin(15730<21201), p_lower_below_threshold(0.24<0.75) |
| 54591803 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→USDC | 69.980908 USDC | 0.022689 USDC | 0.000000 USDC | 0.007051 USDC | 0.015638 USDC (0.0144 €) | — | 2.23 | 0.242 (n=416) | REJECTED | p_lower_below_threshold(0.24<0.75) |
| 54565087 | USDC→[pancakeswap_v3]→WETH→[aerodrome]→SLC→[uniswap_v3]→USDC | 23.269684 USDC | 0.021621 USDC | 0.000000 USDC | 0.006396 USDC | 0.015225 USDC (0.0140 €) | — | 6.54 | 0.268 (n=177) | REJECTED | stale_data(4190ms>4000.0), p_lower_below_threshold(0.27<0.75) |

## Fiabilité et décision
- Observations ghost : 6139 ; taux observé 0.161 ; borne inférieure crédible (0.9) 0.155 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 15.5% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ✅ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
