# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-09T11:18:28+00:00 ; durée 79.86 min ; blocs 55139673 → 55163552 (3029 vus)

## Connexion
- Requêtes RPC : 45465 ; erreurs : 5 ; latence p50/p95 : 372.9/1,933.0 ms
- Rafraîchissements d'état : 3029 ; âge des données au dernier bloc : 20.16 s ; changements de frais LP observés (pools à frais dynamiques) : 2140
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 3914 ; cycles déclenchés par événement : 1270 ; avance médiane sur le rafraîchissement multicall : 570 ms
- Gaz : base fee 0.006308 gwei ; prix ETH (pool le plus profond) : 2,121.04 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 465 pools, 272 jetons, 17388 routes
- Par DEX : uniswap_v3 131 (quarantaine 1), aerodrome_slipstream 99, aerodrome 193 (quarantaine 1), pancakeswap_v3 28, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 167 (rejetés 2) → 572 jetons ; pools candidats 3672 (énumérés 289, par paires 0), mesurés 467, sous le plancher de 10000.0 $ : 2 → gardés 465 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDbC': 1.0, 'USDC': 1.0, 'WETH': 2109.380964, 'cbBTC': 74235.499826, 'AERO': 0.565393}
- Pools en quarantaine : 2 — aerodrome:WETH/SLC@0x2AdfE8: simulation failed ×5 (model/chain mismatch) — until block 55163657; uniswap_v3:SLC/USDC@0x261479: simulation failed ×5 (model/chain mismatch) — until block 55163657

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 138,329,073 | 2,121.096245 | 55163622 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,448,698 | 0.028510 | 55163622 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,236,198 | 0.000013 | 55163622 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 8,710,946 | 0.028445 | 55163622 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 7,421,306 | 2,125.116275 | 55163622 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,150,881 | 102.613912 | 55163622 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,238,940 | 0.001524 | 55163622 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,631,916 | 0.028503 | 55163622 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 4,591,198 | 1.743371 | 55163622 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/USDC | 100 | 3,965,312 | 2,124.563584 | 55163622 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,917,637 | 0.998736 | 55163622 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,114,200 | 43,413.120665 | 55163622 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 150 | 3,020,963 | 2,124.724800 | 55163622 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2610 | 2,356,143 | 0.028461 | 55163622 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 1,993,543 | 1,147,475.453732 | 55163622 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 600 | 1,703,992 | 0.000013 | 55163622 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,646,748 | 0.000013 | 55163622 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,607,841 | 0.006822 | 55163622 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v3 | XDP/USDC | 100 | 1,570,049 | 0.015600 | 55163622 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,557,321 | 0.000000 | 55163622 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,476,122 | 1.418208 | 55163622 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,455,418 | 429.953591 | 55163622 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,453,452 | 0.821691 | 55163622 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,438,510 | 0.000013 | 55163622 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v3 | WETH/AERO | 3000 | 1,320,579 | 3,717.715165 | 55163622 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v2 | WETH/USDC | 3000 | 1,291,113 | 2,120.825392 | 55163622 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,237,411 | 15,109.000460 | 55163622 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/USDC | 3000 | 1,219,485 | 2,121.165529 | 55163622 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome | USDC/SEND | 3000 | 1,107,456 | 79.229296 | 55163622 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,098,108 | 2,125.051188 | 55163622 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | WETH/doginme | 10000 | 1,043,446 | 36,827,352.276577 | 55163622 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/VVV | 10000 | 1,021,287 | 103.317514 | 55163622 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome_slipstream | USDC/VELVET | 100 | 962,671 | 21.208424 | 55163622 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/BRETT | 10000 | 960,706 | 578,043.633008 | 55163622 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome_slipstream | USDC/cbBTC | 448 | 923,156 | 0.000013 | 55163622 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | WETH/TOSHI | 10000 | 922,477 | 23,484,902.655903 | 55163622 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | WETH/USDC | 10000 | 911,157 | 2,106.485556 | 55163622 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome | USDC/NOCK | 3000 | 909,530 | 75.745437 | 55163622 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/MORPHO | 3000 | 905,260 | 1,033.333459 | 55163622 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | DRB/WETH | 10000 | 903,254 | 0.000000 | 55163622 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | USDC/VVV | 3000 | 850,401 | 0.048271 | 55163622 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | WETH/EDEL | 7000 | 818,720 | 102,322.325848 | 55163622 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome_slipstream | USDC/SAPIEN | 4600 | 763,495 | 22.321997 | 55163622 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 760,516 | 0.051631 | 55163622 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/AERO | 10000 | 745,963 | 3,721.601102 | 55163622 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | WETH/wstETH | 3000 | 718,113 | 0.802916 | 55163622 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 698,376 | 0.539815 | 55163622 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 652,634 | 4,999,620.370065 | 55163622 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 641,730 | 0.521652 | 55163622 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 622,716 | 0.000008 | 55163622 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v2 | WETH/NPC | 3000 | 610,159 | 152,875.590602 | 55163622 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome | VIRTUAL/WETH | 10000 | 592,840 | 0.000253 | 55163622 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/BRETT | 2141 | 585,870 | 573,269.074364 | 55163622 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | FLOCK/USDC | 3000 | 570,535 | 0.038853 | 55163622 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome | WETH/msETH (stable) | 500 | 532,223 | 2.381266 | 55163622 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | WETH/MORPHO | 2748 | 514,349 | 1,033.016383 | 55163622 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome | cbBTC/EDGE | 7000 | 505,931 | 914,156.513345 | 55163622 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| uniswap_v3 | USDC/USDT | 100 | 497,519 | 1.001238 | 55163622 | `0xD56da2B74bA826f19015E6B7Dd9Dae1903E85DA1` |
| pancakeswap_v3 | ELSA/USDC | 100 | 484,876 | 0.070408 | 55163622 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| aerodrome | WETH/DRV | 3000 | 479,646 | 7,171.223882 | 55163622 | `0xaC4e562d7C6108f971321F14238E24AE2cC398ac` |

## Recherche d'opportunités
- Cycles : 4298 ; routes examinées : 74733624 ; candidats optimisés : 328937 ; net attendu > 0 : 931 ; dernier cycle 678.6 ms
- Rejets (moteur) : {'spread_below_threshold': 73359059, 'liquidity_below_min': 1033501, 'negative_expected_net': 328006, 'borrow_bound_too_small': 8552, 'cycle_budget_exhausted': 2679, 'pool_quarantined': 896}
- Enregistrements de la session : 328937 ; net attendu > 0 : 931 ; simulés (eth_call de la vraie tx) : 56 (ok 28, échec 28) ; étiquettes ghost N+1 : 17/47 positives
- Décisions : {'REJECTED': 328937} ; motifs de rejet : {'below_safety_margin': 599, 'negative_expected_net': 328006, 'p_lower_below_threshold': 911, 'reliability_not_demonstrated': 20, 'sim_below_estimate': 10, 'simulated_net_nonpositive': 4, 'simulation_failed': 28, 'stale_data': 235}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 55163450 | USDC→[aerodrome_slipstream]→USDT→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 284.849900 USDC | 0.103510 USDC | 0.000000 USDC | 0.007483 USDC | 0.096027 USDC (0.0883 €) | — | 3.37 | 0.177 (n=949) | REJECTED | p_lower_below_threshold(0.18<0.75) |
| 55163450 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→USDT→[uniswap_v3]→WETH | 0.134464 WETH | 0.000049 WETH | 0.000000 WETH | 0.000004 WETH | 0.000045 WETH (0.0881 €) | — | 3.36 | 0.177 (n=949) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.18<0.75) |
| 55149091 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 596.907834 USDC | 0.096224 USDC | 0.000000 USDC | 0.004729 USDC | 0.091495 USDC (0.0842 €) | — | 1.53 | 0.059 (n=301) | REJECTED | below_safety_margin(91495<119381), p_lower_below_threshold(0.06<0.75) |
| 55149092 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 596.907834 USDC | 0.096224 USDC | 0.000000 USDC | 0.004729 USDC | 0.091495 USDC (0.0842 €) | — | 1.53 | 0.059 (n=301) | REJECTED | below_safety_margin(91495<119381), p_lower_below_threshold(0.06<0.75) |
| 55149091 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.284633 WETH | 0.000046 WETH | 0.000000 WETH | 0.000002 WETH | 0.000043 WETH (0.0841 €) | — | 1.53 | 0.059 (n=301) | REJECTED | below_safety_margin(43444993489647<56926665444047), p_lower_below_threshold(0.06<0.75) |
| 55149092 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.284633 WETH | 0.000046 WETH | 0.000000 WETH | 0.000002 WETH | 0.000043 WETH (0.0841 €) | — | 1.53 | 0.059 (n=301) | REJECTED | below_safety_margin(43444993489647<56926665444047), p_lower_below_threshold(0.06<0.75) |
| 55163450 | USDC→[uniswap_v3]→USDT→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 275.194737 USDC | 0.095433 USDC | 0.000000 USDC | 0.007483 USDC | 0.087950 USDC (0.0809 €) | — | 3.20 | 0.177 (n=949) | REJECTED | p_lower_below_threshold(0.18<0.75) |
| 55163450 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→USDT→[uniswap_v3]→WETH | 0.129678 WETH | 0.000045 WETH | 0.000000 WETH | 0.000004 WETH | 0.000041 WETH (0.0807 €) | — | 3.19 | 0.177 (n=949) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.18<0.75) |
| 55163323 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 311.441788 USDC | 0.075536 USDC | 0.000000 USDC | 0.006855 USDC | 0.068681 USDC (0.0632 €) | — | 2.21 | 0.207 (n=1247) | REJECTED | stale_data(4230ms>4000.0), p_lower_below_threshold(0.21<0.75) |
| 55163354 | cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.004494 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0629 €) | — | 2.05 | 0.206 (n=1249) | REJECTED | stale_data(7465ms>4000.0), p_lower_below_threshold(0.21<0.75) |
| 55163323 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.143446 WETH | 0.000036 WETH | 0.000000 WETH | 0.000003 WETH | 0.000032 WETH (0.0628 €) | — | 2.25 | 0.207 (n=1247) | REJECTED | stale_data(4224ms>4000.0), simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.21<0.75) |
| 55163323 | cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.004050 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0628 €) | — | 2.27 | 0.207 (n=1247) | REJECTED | stale_data(4217ms>4000.0), p_lower_below_threshold(0.21<0.75) |
| 55163354 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 323.970165 USDC | 0.075206 USDC | 0.000000 USDC | 0.007149 USDC | 0.068057 USDC (0.0626 €) | — | 2.10 | 0.206 (n=1249) | REJECTED | stale_data(7478ms>4000.0), p_lower_below_threshold(0.21<0.75) |
| 55163354 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.144941 WETH | 0.000035 WETH | 0.000000 WETH | 0.000003 WETH | 0.000032 WETH (0.0624 €) | — | 2.21 | 0.206 (n=1249) | REJECTED | stale_data(7471ms>4000.0), simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.21<0.75) |
| 55163405 | USDC→[aerodrome_slipstream]→LCAP→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 109.023935 USDC | 0.072623 USDC | 0.000000 USDC | 0.007824 USDC | 0.064799 USDC (0.0596 €) | — | 5.94 | 0.294 (n=425) | REJECTED | p_lower_below_threshold(0.29<0.75) |
| 55163405 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→LCAP→[aerodrome_slipstream]→WETH | 0.051447 WETH | 0.000034 WETH | 0.000000 WETH | 0.000004 WETH | 0.000030 WETH (0.0594 €) | — | 5.92 | 0.294 (n=425) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.29<0.75) |
| 55163323 | USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 316.696560 USDC | 0.067805 USDC | 0.000000 USDC | 0.006855 USDC | 0.060950 USDC (0.0561 €) | — | 1.92 | 0.207 (n=1247) | REJECTED | below_safety_margin(60950<63339), stale_data(4354ms>4000.0), p_lower_below_threshold(0.21<0.75) |
| 55163354 | cbBTC→[uniswap_v3]→WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.003913 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0560 €) | — | 2.10 | 0.206 (n=1249) | REJECTED | stale_data(7596ms>4000.0), p_lower_below_threshold(0.21<0.75) |
| 55163323 | cbBTC→[uniswap_v3]→WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.003951 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0560 €) | — | 2.08 | 0.207 (n=1247) | REJECTED | stale_data(4342ms>4000.0), p_lower_below_threshold(0.21<0.75) |
| 55163323 | USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 299.031827 USDC | 0.067607 USDC | 0.000000 USDC | 0.006855 USDC | 0.060752 USDC (0.0559 €) | — | 2.03 | 0.207 (n=1247) | REJECTED | stale_data(4309ms>4000.0), p_lower_below_threshold(0.21<0.75) |
| 55163323 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH | 0.143066 WETH | 0.000032 WETH | 0.000000 WETH | 0.000003 WETH | 0.000029 WETH (0.0559 €) | — | 2.01 | 0.207 (n=1247) | REJECTED | stale_data(4348ms>4000.0), simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.21<0.75) |
| 55163323 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH | 0.145960 WETH | 0.000032 WETH | 0.000000 WETH | 0.000003 WETH | 0.000029 WETH (0.0558 €) | — | 1.97 | 0.207 (n=1247) | REJECTED | below_safety_margin(28713247066759<29191976865563), stale_data(4302ms>4000.0), p_lower_below_threshold(0.21<0.75) |
| 55163354 | USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 287.162131 USDC | 0.067791 USDC | 0.000000 USDC | 0.007149 USDC | 0.060642 USDC (0.0558 €) | — | 2.11 | 0.206 (n=1249) | REJECTED | stale_data(7608ms>4000.0), p_lower_below_threshold(0.21<0.75) |
| 55163354 | USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 300.845274 USDC | 0.067748 USDC | 0.000000 USDC | 0.007149 USDC | 0.060599 USDC (0.0558 €) | — | 2.01 | 0.206 (n=1249) | REJECTED | stale_data(7563ms>4000.0), p_lower_below_threshold(0.21<0.75) |
| 55163354 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH | 0.145170 WETH | 0.000032 WETH | 0.000000 WETH | 0.000003 WETH | 0.000029 WETH (0.0557 €) | — | 1.97 | 0.206 (n=1249) | REJECTED | below_safety_margin(28597508704955<29034059380065), stale_data(7602ms>4000.0), p_lower_below_threshold(0.21<0.75) |

## Fiabilité et décision
- Observations ghost : 6787 ; taux observé 0.178 ; borne inférieure crédible (0.9) 0.172 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 17.2% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ✅ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
