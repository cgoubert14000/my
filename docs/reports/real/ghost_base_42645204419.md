# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-09T17:35:32+00:00 ; durée 119.74 min ; blocs 55240823 → 55276710 (4908 vus)

## Connexion
- Requêtes RPC : 70817 ; erreurs : 0 ; latence p50/p95 : 381.4/1,478.4 ms
- Rafraîchissements d'état : 4908 ; âge des données au dernier bloc : 12.48 s ; changements de frais LP observés (pools à frais dynamiques) : 3940
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 1775 ; cycles déclenchés par événement : 518 ; avance médiane sur le rafraîchissement multicall : 756 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,128.15 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 473 pools, 274 jetons, 17868 routes
- Par DEX : uniswap_v3 135, aerodrome_slipstream 102, aerodrome 193, pancakeswap_v3 29, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 167 (rejetés 2) → 572 jetons ; pools candidats 3663 (énumérés 293, par paires 0), mesurés 475, sous le plancher de 10000.0 $ : 2 → gardés 473 (max 1500) ; prix des hubs : {'USDC': 1.0, 'USDbC': 1.0, 'DAI': 1.0, 'WETH': 2131.426069, 'cbBTC': 75169.710892, 'AERO': 0.579676}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 139,669,789 | 2,128.154239 | 55276743 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,645,035 | 0.028415 | 55276743 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,311,544 | 0.000013 | 55276743 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 8,774,342 | 0.028437 | 55276743 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 7,335,143 | 2,125.014840 | 55276743 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,278,342 | 99.826598 | 55276743 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,951,681 | 0.028422 | 55276743 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 4,587,534 | 1.741439 | 55276743 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,007,565 | 2,125.325046 | 55276743 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,946,173 | 0.998591 | 55276743 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,126,314 | 43,366.670266 | 55276743 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 150 | 3,030,358 | 2,125.590735 | 55276743 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,365,448 | 0.028431 | 55276743 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 1,999,288 | 1,148,554.063045 | 55276743 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,723,306 | 0.000013 | 55276743 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | USDC/cbBTC | 460 | 1,706,034 | 0.000013 | 55276743 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | XDP/USDC | 100 | 1,577,224 | 0.015703 | 55276743 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,566,736 | 0.006582 | 55276743 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,562,556 | 0.000000 | 55276743 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,512,348 | 0.000013 | 55276743 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,476,122 | 1.418208 | 55276743 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,469,045 | 421.426776 | 55276743 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,459,000 | 0.821800 | 55276743 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,323,429 | 3,699.913682 | 55276743 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v2 | WETH/USDC | 3000 | 1,293,313 | 2,128.384831 | 55276743 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,255,162 | 14,821.666146 | 55276743 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/USDC | 3000 | 1,221,529 | 2,123.373818 | 55276743 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome | USDC/SEND | 3000 | 1,107,257 | 79.257778 | 55276743 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,096,470 | 2,124.984927 | 55276743 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | WETH/doginme | 10000 | 1,048,218 | 36,690,111.620299 | 55276743 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/VVV | 10000 | 978,143 | 100.550028 | 55276743 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/BRETT | 10000 | 972,575 | 563,086.238370 | 55276743 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome_slipstream | USDC/VELVET | 100 | 959,545 | 21.419383 | 55276743 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | USDC/VVV | 3000 | 952,749 | 0.046988 | 55276743 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 938,681 | 0.001514 | 55276743 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 336 | 929,160 | 0.000013 | 55276743 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | WETH/TOSHI | 10000 | 928,381 | 23,537,564.740435 | 55276743 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome | USDC/NOCK | 3000 | 916,404 | 74.616291 | 55276743 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/MORPHO | 3000 | 911,018 | 1,030.193017 | 55276743 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | DRB/WETH | 10000 | 906,341 | 0.000000 | 55276743 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/USDC | 10000 | 887,599 | 2,127.924155 | 55276743 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome | WETH/EDEL | 7000 | 817,979 | 103,196.321435 | 55276743 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome_slipstream | USDC/SAPIEN | 4530 | 780,535 | 21.653033 | 55276743 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 772,372 | 0.053263 | 55276743 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/AERO | 10000 | 747,624 | 3,692.738593 | 55276743 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | WETH/wstETH | 3000 | 722,471 | 0.798586 | 55276743 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 671,979 | 0.550353 | 55276743 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 662,166 | 4,889,557.619673 | 55276743 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 648,271 | 0.527774 | 55276743 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 624,053 | 0.000008 | 55276743 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v2 | WETH/NPC | 3000 | 614,433 | 151,782.052667 | 55276743 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome | VIRTUAL/WETH | 10000 | 599,817 | 0.000257 | 55276743 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/BRETT | 2174 | 595,975 | 568,560.538467 | 55276743 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | FLOCK/USDC | 3000 | 573,442 | 0.039154 | 55276743 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome | WETH/msETH (stable) | 500 | 532,191 | 2.393307 | 55276743 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | WETH/MORPHO | 2727 | 517,492 | 1,030.463978 | 55276743 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome | cbBTC/EDGE | 7000 | 511,579 | 906,054.195506 | 55276743 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| uniswap_v3 | USDC/USDT | 100 | 493,736 | 1.001023 | 55276743 | `0xD56da2B74bA826f19015E6B7Dd9Dae1903E85DA1` |
| aerodrome | WETH/DRV | 3000 | 490,414 | 6,905.839292 | 55276743 | `0xaC4e562d7C6108f971321F14238E24AE2cC398ac` |
| uniswap_v3 | WETH/uSOL | 3000 | 470,323 | 24.652327 | 55276743 | `0xab04A352D4EC8d0F1812A4E5EBe7807Fa67acD48` |

## Recherche d'opportunités
- Cycles : 5425 ; routes examinées : 96933900 ; candidats optimisés : 333397 ; net attendu > 0 : 626 ; dernier cycle 126.9 ms
- Rejets (moteur) : {'spread_below_threshold': 95154270, 'liquidity_below_min': 1413564, 'negative_expected_net': 332771, 'borrow_bound_too_small': 30586, 'pool_quarantined': 1512, 'cycle_budget_exhausted': 571}
- Enregistrements de la session : 333397 ; net attendu > 0 : 626 ; simulés (eth_call de la vraie tx) : 50 (ok 37, échec 13) ; étiquettes ghost N+1 : 16/39 positives
- Décisions : {'REJECTED': 333397} ; motifs de rejet : {'below_safety_margin': 521, 'negative_expected_net': 332771, 'p_lower_below_threshold': 576, 'reliability_not_demonstrated': 50, 'sim_below_estimate': 6, 'simulated_net_nonpositive': 3, 'simulation_failed': 13, 'stale_data': 203}

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
| 55274014 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.206465 WETH | 0.000023 WETH | 0.000000 WETH | 0.000002 WETH | 0.000021 WETH (0.0402 €) | — | 0.99 | 0.063 (n=308) | REJECTED | below_safety_margin(20509469647955<41293006545002), stale_data(4278ms>4000.0), p_lower_below_threshold(0.06<0.75) |
| 55274014 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.206465 WETH | 0.000023 WETH | 0.000000 WETH | 0.000002 WETH | 0.000021 WETH (0.0402 €) | — | 0.99 | 0.063 (n=308) | REJECTED | below_safety_margin(20509469647955<41293006545002), stale_data(4468ms>4000.0), p_lower_below_threshold(0.06<0.75) |
| 55274015 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.206465 WETH | 0.000023 WETH | 0.000000 WETH | 0.000002 WETH | 0.000021 WETH (0.0402 €) | — | 0.99 | 0.063 (n=308) | REJECTED | below_safety_margin(20509469647955<41293006545002), p_lower_below_threshold(0.06<0.75) |
| 55274014 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 437.228741 USDC | 0.048355 USDC | 0.000000 USDC | 0.004810 USDC | 0.043545 USDC (0.0401 €) | — | 1.00 | 0.063 (n=308) | REJECTED | below_safety_margin(43545<87445), stale_data(4282ms>4000.0), p_lower_below_threshold(0.06<0.75) |
| 55274014 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 437.228741 USDC | 0.048355 USDC | 0.000000 USDC | 0.004810 USDC | 0.043545 USDC (0.0401 €) | — | 1.00 | 0.063 (n=308) | REJECTED | below_safety_margin(43545<87445), stale_data(4472ms>4000.0), p_lower_below_threshold(0.06<0.75) |
| 55274015 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 437.228741 USDC | 0.048355 USDC | 0.000000 USDC | 0.004810 USDC | 0.043545 USDC (0.0401 €) | — | 1.00 | 0.063 (n=308) | REJECTED | below_safety_margin(43545<87445), p_lower_below_threshold(0.06<0.75) |
| 55258675 | cbBTC→[aerodrome]→EDGE→[uniswap_v3]→USDC→[aerodrome_slipstream]→cbBTC | 0.000777 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0372 €) | — | 6.95 | 0.142 (n=278) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 55258675 | cbBTC→[aerodrome]→EDGE→[uniswap_v3]→USDC→[aerodrome_slipstream]→cbBTC | 0.000777 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0372 €) | — | 6.95 | 0.142 (n=278) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 55258676 | cbBTC→[aerodrome]→EDGE→[uniswap_v3]→USDC→[aerodrome_slipstream]→cbBTC | 0.000777 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0372 €) | — | 6.95 | 0.141 (n=279) | REJECTED | p_lower_below_threshold(0.14<0.75) |

## Fiabilité et décision
- Observations ghost : 6951 ; taux observé 0.184 ; borne inférieure crédible (0.9) 0.178 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 17.8% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ✅ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
