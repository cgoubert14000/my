# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-09T17:10:55+00:00 ; durée 95.13 min ; blocs 55240823 → 55269342 (3861 vus)

## Connexion
- Requêtes RPC : 55644 ; erreurs : 0 ; latence p50/p95 : 385.1/1,616.7 ms
- Rafraîchissements d'état : 3861 ; âge des données au dernier bloc : 9.33 s ; changements de frais LP observés (pools à frais dynamiques) : 3240
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 1283 ; cycles déclenchés par événement : 289 ; avance médiane sur le rafraîchissement multicall : 756 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,128.63 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 473 pools, 274 jetons, 17868 routes
- Par DEX : uniswap_v3 135, aerodrome_slipstream 102, aerodrome 193, pancakeswap_v3 29, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 167 (rejetés 2) → 572 jetons ; pools candidats 3663 (énumérés 293, par paires 0), mesurés 475, sous le plancher de 10000.0 $ : 2 → gardés 473 (max 1500) ; prix des hubs : {'USDC': 1.0, 'USDbC': 1.0, 'DAI': 1.0, 'WETH': 2131.426069, 'cbBTC': 75169.710892, 'AERO': 0.579676}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 139,747,829 | 2,128.630382 | 55269373 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,614,537 | 0.028425 | 55269373 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,305,748 | 0.000013 | 55269373 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 8,775,599 | 0.028437 | 55269373 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 7,336,391 | 2,125.975426 | 55269373 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,270,825 | 100.075227 | 55269373 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,950,418 | 0.028415 | 55269373 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 4,594,008 | 1.736686 | 55269373 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,007,753 | 2,126.414293 | 55269373 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,945,778 | 0.998586 | 55269373 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,108,086 | 43,896.483567 | 55269373 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 150 | 3,009,714 | 2,126.710638 | 55269373 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,382,034 | 0.028430 | 55269373 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 1,999,735 | 1,148,554.063045 | 55269373 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,722,724 | 0.000013 | 55269373 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | USDC/cbBTC | 496 | 1,705,883 | 0.000013 | 55269373 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | XDP/USDC | 100 | 1,576,793 | 0.015697 | 55269373 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,566,546 | 0.006580 | 55269373 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,562,905 | 0.000000 | 55269373 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,512,607 | 0.000013 | 55269373 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,476,122 | 1.418208 | 55269373 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,469,509 | 421.282858 | 55269373 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,459,737 | 0.821800 | 55269373 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,325,714 | 3,701.114676 | 55269373 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v2 | WETH/USDC | 3000 | 1,293,457 | 2,129.782149 | 55269373 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,255,383 | 14,822.638953 | 55269373 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/USDC | 3000 | 1,221,665 | 2,131.389002 | 55269373 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome | USDC/SEND | 3000 | 1,107,257 | 79.257778 | 55269373 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,096,637 | 2,126.169385 | 55269373 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | WETH/doginme | 10000 | 1,048,384 | 36,697,352.270661 | 55269373 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/VVV | 10000 | 980,914 | 100.750088 | 55269373 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/BRETT | 10000 | 973,293 | 562,240.868616 | 55269373 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome_slipstream | USDC/VELVET | 100 | 961,345 | 21.296594 | 55269373 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | USDC/VVV | 3000 | 951,182 | 0.047030 | 55269373 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 940,603 | 0.001520 | 55269373 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 344 | 929,055 | 0.000013 | 55269373 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | WETH/TOSHI | 10000 | 925,201 | 23,537,564.740435 | 55269373 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome | USDC/NOCK | 3000 | 916,411 | 74.615291 | 55269373 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/MORPHO | 3000 | 911,220 | 1,030.193461 | 55269373 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | DRB/WETH | 10000 | 907,659 | 0.000000 | 55269373 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/USDC | 10000 | 887,683 | 2,127.924155 | 55269373 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome | WETH/EDEL | 7000 | 815,851 | 103,781.664072 | 55269373 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 785,572 | 21.457324 | 55269373 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 772,357 | 0.053260 | 55269373 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/AERO | 10000 | 748,729 | 3,692.738593 | 55269373 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | WETH/wstETH | 3000 | 722,633 | 0.798586 | 55269373 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 672,102 | 0.550578 | 55269373 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 661,905 | 4,895,599.784659 | 55269373 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 648,219 | 0.527693 | 55269373 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 625,118 | 0.000008 | 55269373 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v2 | WETH/NPC | 3000 | 614,242 | 151,926.879828 | 55269373 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome | VIRTUAL/WETH | 10000 | 599,952 | 0.000257 | 55269373 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 596,568 | 565,866.686184 | 55269373 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | FLOCK/USDC | 3000 | 574,358 | 0.039251 | 55269373 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome | WETH/msETH (stable) | 500 | 532,310 | 2.393307 | 55269373 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 517,591 | 1,030.450468 | 55269373 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome | cbBTC/EDGE | 7000 | 511,519 | 906,054.195506 | 55269373 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| uniswap_v3 | USDC/USDT | 100 | 493,736 | 1.001023 | 55269373 | `0xD56da2B74bA826f19015E6B7Dd9Dae1903E85DA1` |
| aerodrome | WETH/DRV | 3000 | 490,548 | 6,905.150897 | 55269373 | `0xaC4e562d7C6108f971321F14238E24AE2cC398ac` |
| pancakeswap_v3 | ELSA/USDC | 100 | 472,116 | 0.068055 | 55269373 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |

## Recherche d'opportunités
- Cycles : 4149 ; routes examinées : 74134332 ; candidats optimisés : 256848 ; net attendu > 0 : 514 ; dernier cycle 294.9 ms
- Rejets (moteur) : {'spread_below_threshold': 72885666, 'liquidity_below_min': 961835, 'negative_expected_net': 256334, 'borrow_bound_too_small': 28036, 'pool_quarantined': 1512, 'cycle_budget_exhausted': 435}
- Enregistrements de la session : 256848 ; net attendu > 0 : 514 ; simulés (eth_call de la vraie tx) : 44 (ok 32, échec 12) ; étiquettes ghost N+1 : 16/34 positives
- Décisions : {'REJECTED': 256848} ; motifs de rejet : {'below_safety_margin': 426, 'negative_expected_net': 256334, 'p_lower_below_threshold': 478, 'reliability_not_demonstrated': 36, 'sim_below_estimate': 6, 'simulated_net_nonpositive': 3, 'simulation_failed': 12, 'stale_data': 152}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 55246974 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.354201 WETH | 0.000040 WETH | 0.000000 WETH | 0.000003 WETH | 0.000037 WETH (0.0729 €) | — | 1.04 | 0.048 (n=30) | REJECTED | below_safety_margin(36995411685845<70840226028216), stale_data(5713ms>4000.0), p_lower_below_threshold(0.05<0.75) |
| 55246974 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 833.027063 USDC | 0.085597 USDC | 0.000000 USDC | 0.006858 USDC | 0.078739 USDC (0.0724 €) | — | 0.95 | 0.048 (n=30) | REJECTED | below_safety_margin(78739<166605), stale_data(5719ms>4000.0), p_lower_below_threshold(0.05<0.75) |
| 55246974 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.009328 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0721 €) | — | 1.11 | 0.048 (n=30) | REJECTED | below_safety_margin(104<186), stale_data(5726ms>4000.0), p_lower_below_threshold(0.05<0.75) |
| 55258675 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome]→EDGE→[uniswap_v3]→USDC | 77.105407 USDC | 0.075267 USDC | 0.000000 USDC | 0.006282 USDC | 0.068985 USDC (0.0635 €) | — | 8.95 | 0.142 (n=54) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.14<0.75) |
| 55258676 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome]→EDGE→[uniswap_v3]→USDC | 77.105407 USDC | 0.075267 USDC | 0.000000 USDC | 0.006282 USDC | 0.068985 USDC (0.0635 €) | — | 8.95 | 0.139 (n=55) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.14<0.75) |
| 55258675 | cbBTC→[aerodrome]→EDGE→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.000988 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0633 €) | — | 9.31 | 0.142 (n=54) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 55258676 | cbBTC→[aerodrome]→EDGE→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.000988 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0633 €) | — | 9.31 | 0.139 (n=55) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 55258675 | cbBTC→[aerodrome]→EDGE→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.000848 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0489 €) | — | 8.37 | 0.142 (n=54) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 55258676 | cbBTC→[aerodrome]→EDGE→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.000848 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0489 €) | — | 8.37 | 0.139 (n=55) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 55258675 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome]→EDGE→[uniswap_v3]→USDC | 72.722809 USDC | 0.059162 USDC | 0.000000 USDC | 0.006282 USDC | 0.052880 USDC (0.0486 €) | — | 7.27 | 0.289 (n=187) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.29<0.75) |
| 55258676 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome]→EDGE→[uniswap_v3]→USDC | 72.722809 USDC | 0.059162 USDC | 0.000000 USDC | 0.006282 USDC | 0.052880 USDC (0.0486 €) | — | 7.27 | 0.287 (n=188) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.29<0.75) |
| 55253986 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.005697 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0436 €) | — | 1.11 | 0.216 (n=1274) | REJECTED | below_safety_margin(63<113), p_lower_below_threshold(0.22<0.75) |
| 55253986 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.221325 WETH | 0.000025 WETH | 0.000000 WETH | 0.000003 WETH | 0.000022 WETH (0.0435 €) | — | 1.00 | 0.216 (n=1274) | REJECTED | below_safety_margin(22118970982473<44265071018017), p_lower_below_threshold(0.22<0.75) |
| 55253986 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 485.256728 USDC | 0.053353 USDC | 0.000000 USDC | 0.006475 USDC | 0.046878 USDC (0.0431 €) | — | 0.97 | 0.216 (n=1274) | REJECTED | below_safety_margin(46878<97051), p_lower_below_threshold(0.22<0.75) |
| 55253986 | cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.006430 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0408 €) | — | 0.92 | 0.063 (n=307) | REJECTED | below_safety_margin(59<128), p_lower_below_threshold(0.06<0.75) |
| 55253986 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 516.615464 USDC | 0.048879 USDC | 0.000000 USDC | 0.004842 USDC | 0.044037 USDC (0.0405 €) | — | 0.85 | 0.063 (n=307) | REJECTED | below_safety_margin(44037<103323), p_lower_below_threshold(0.06<0.75) |
| 55258675 | cbBTC→[aerodrome]→EDGE→[uniswap_v3]→USDC→[aerodrome_slipstream]→cbBTC | 0.000777 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0372 €) | — | 6.95 | 0.142 (n=278) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 55258675 | cbBTC→[aerodrome]→EDGE→[uniswap_v3]→USDC→[aerodrome_slipstream]→cbBTC | 0.000777 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0372 €) | — | 6.95 | 0.142 (n=278) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 55258676 | cbBTC→[aerodrome]→EDGE→[uniswap_v3]→USDC→[aerodrome_slipstream]→cbBTC | 0.000777 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0372 €) | — | 6.95 | 0.141 (n=279) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 55258676 | cbBTC→[aerodrome]→EDGE→[uniswap_v3]→USDC→[aerodrome_slipstream]→cbBTC | 0.000777 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0372 €) | — | 6.95 | 0.141 (n=279) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 55258675 | USDC→[aerodrome_slipstream]→cbBTC→[aerodrome]→EDGE→[uniswap_v3]→USDC | 59.649912 USDC | 0.046451 USDC | 0.000000 USDC | 0.006282 USDC | 0.040169 USDC (0.0370 €) | — | 6.73 | 0.142 (n=278) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.14<0.75) |
| 55258676 | USDC→[aerodrome_slipstream]→cbBTC→[aerodrome]→EDGE→[uniswap_v3]→USDC | 59.649912 USDC | 0.046451 USDC | 0.000000 USDC | 0.006282 USDC | 0.040169 USDC (0.0370 €) | — | 6.73 | 0.141 (n=279) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.14<0.75) |
| 55258675 | USDC→[aerodrome_slipstream]→cbBTC→[aerodrome]→EDGE→[uniswap_v3]→USDC | 61.993626 USDC | 0.046336 USDC | 0.000000 USDC | 0.006282 USDC | 0.040054 USDC (0.0368 €) | — | 6.46 | 0.142 (n=278) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 55258676 | USDC→[aerodrome_slipstream]→cbBTC→[aerodrome]→EDGE→[uniswap_v3]→USDC | 61.993626 USDC | 0.046336 USDC | 0.000000 USDC | 0.006282 USDC | 0.040054 USDC (0.0368 €) | — | 6.46 | 0.141 (n=279) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 55241295 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.002374 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0345 €) | — | 2.11 | 0.027 (n=11) | REJECTED | stale_data(5044ms>4000.0), reliability_not_demonstrated |

## Fiabilité et décision
- Observations ghost : 6946 ; taux observé 0.184 ; borne inférieure crédible (0.9) 0.179 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 17.9% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ✅ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
