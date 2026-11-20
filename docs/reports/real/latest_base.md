# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-20T23:04:45+00:00 ; durée 91.31 min ; blocs 60100131 → 60127517 (6597 vus)

## Connexion
- Requêtes RPC : 65996 ; erreurs : 60 ; latence p50/p95 : 323.0/927.5 ms
- Rafraîchissements d'état : 6597 ; âge des données au dernier bloc : 6.82 s ; changements de frais LP observés (pools à frais dynamiques) : 4942
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 16725 ; cycles déclenchés par événement : 4391 ; avance médiane sur le rafraîchissement multicall : 288 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 1,621.25 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 411 pools, 245 jetons, 12256 routes
- Par DEX : uniswap_v3 122, aerodrome_slipstream 86, aerodrome 166, pancakeswap_v3 26, uniswap_v2 9, sushiswap_v2 1, sushiswap_v3 1
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 143 (rejetés 2) → 548 jetons ; pools candidats 3595 (énumérés 251, par paires 0), mesurés 413, sous le plancher de 10000.0 $ : 2 → gardés 411 (max 1500) ; prix des hubs : {'USDC': 1.0, 'DAI': 1.0, 'USDbC': 1.0, 'WETH': 1605.51254, 'cbBTC': 58557.611788, 'AERO': 0.386499}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 77,423,227 | 1,621.249377 | 60127534 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 20,410,070 | 0.027466 | 60127534 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/USDC | 500 | 10,386,946 | 1,625.178284 | 60127534 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| uniswap_v3 | WETH/cbBTC | 3000 | 7,108,641 | 0.027458 | 60127534 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| aerodrome | WETH/VVV | 3000 | 6,254,189 | 78.026433 | 60127534 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | USDC/cbBTC | 500 | 5,395,652 | 0.000017 | 60127534 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 3,781,495 | 0.027470 | 60127534 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 3,319,371 | 2.529083 | 60127534 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,104,004 | 1.000001 | 60127534 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| pancakeswap_v3 | WETH/USDC | 100 | 2,918,862 | 1,624.971432 | 60127534 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | WETH/KTA | 3000 | 2,479,092 | 40,024.012513 | 60127534 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 286 | 2,115,062 | 1,625.284866 | 60127534 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,779,754 | 0.000017 | 60127534 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 1,588,909 | 0.027462 | 60127534 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 1,539,365 | 1,124,378.471239 | 60127534 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,454,267 | 0.844821 | 60127534 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | USDC/cbBTC | 556 | 1,264,488 | 0.000017 | 60127534 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,252,625 | 0.000000 | 60127534 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,159,500 | 0.006491 | 60127534 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,152,898 | 0.000017 | 60127534 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,083,956 | 15.258839 | 60127534 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | USDC/SEND | 3000 | 1,059,499 | 86.564217 | 60127534 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 966,514 | 451.207675 | 60127534 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v2 | WETH/USDC | 3000 | 955,295 | 1,622.771883 | 60127534 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 947,465 | 16,418.015953 | 60127534 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | WETH/AERO | 3000 | 932,134 | 4,098.832889 | 60127534 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v3 | USDC/VVV | 3000 | 926,647 | 0.047953 | 60127534 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/VVV | 10000 | 924,389 | 78.451534 | 60127534 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/doginme | 10000 | 854,673 | 30,778,738.095304 | 60127534 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 764,702 | 512,143.246580 | 60127534 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | USDC/NOCK | 3000 | 752,987 | 75.459055 | 60127534 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 745,818 | 0.001538 | 60127534 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| uniswap_v3 | WETH/TOSHI | 10000 | 741,418 | 21,771,079.934704 | 60127534 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | DRB/WETH | 10000 | 734,631 | 0.000000 | 60127534 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome_slipstream | USDC/SAPIEN | 4790 | 731,250 | 23.936599 | 60127534 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v3 | XDP/USDC | 100 | 718,233 | 0.014476 | 60127534 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | QUID/USDC | 100 | 703,172 | 0.043945 | 60127534 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/USDC | 3000 | 690,511 | 1,621.139843 | 60127534 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| uniswap_v3 | WETH/MORPHO | 3000 | 688,061 | 1,060.982691 | 60127534 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| pancakeswap_v3 | WETH/USDC | 500 | 649,167 | 1,625.141690 | 60127534 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | uXRP/WETH | 3000 | 644,287 | 0.000611 | 60127534 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| uniswap_v3 | WETH/USDC | 100 | 562,683 | 1,624.956278 | 60127534 | `0xb4CB800910B228ED3d0834cF79D697127BBB00e5` |
| aerodrome | WETH/wstETH | 3000 | 550,103 | 0.799406 | 60127534 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | TIG/USDC | 10000 | 549,742 | 0.381511 | 60127534 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 524,237 | 4,552,515.884900 | 60127534 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome | WETH/AERO | 10000 | 504,986 | 4,128.188737 | 60127534 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | FLOCK/USDC | 3000 | 489,400 | 0.030834 | 60127534 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| pancakeswap_v3 | ELSA/USDC | 100 | 481,181 | 0.069780 | 60127534 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| aerodrome_slipstream | WETH/BRETT | 4079 | 478,419 | 508,504.614137 | 60127534 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome | USDC/MAI (stable) | 3000 | 471,745 | 1.473937 | 60127534 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | WETH/USDC | 10000 | 446,887 | 1,613.105205 | 60127534 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v2 | WETH/NPC | 3000 | 423,029 | 187,102.638213 | 60127534 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | AERO/cbBTC | 1025 | 418,430 | 0.000007 | 60127534 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/MORPHO | 3169 | 374,026 | 1,060.801246 | 60127534 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome | cbBTC/EDGE | 7000 | 367,677 | 831,261.400020 | 60127534 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| uniswap_v3 | WETH/uSOL | 3000 | 367,230 | 21.716230 | 60127534 | `0xab04A352D4EC8d0F1812A4E5EBe7807Fa67acD48` |
| aerodrome | AWE/USDC | 3000 | 364,860 | 0.055355 | 60127534 | `0xcb7f520d18141E36956fE0b3A6Bc3D4F11245521` |
| uniswap_v3 | WETH/UNI | 10000 | 346,792 | 365.871981 | 60127534 | `0xAb365f161Dd501473a1ff0D2ef0dCE94E7398839` |
| aerodrome_slipstream | WETH/VVV | 2715 | 340,000 | 77.983394 | 60127534 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | VIRTUAL/WETH | 10000 | 335,143 | 0.000234 | 60127534 | `0x21594b992F68495dD28d605834b58889d0a727c7` |

## Recherche d'opportunités
- Cycles : 10987 ; routes examinées : 134656672 ; candidats optimisés : 187635 ; net attendu > 0 : 410 ; dernier cycle 607.0 ms
- Rejets (moteur) : {'spread_below_threshold': 131201301, 'liquidity_below_min': 2108572, 'negative_expected_net': 187225, 'borrow_bound_too_small': 19833, 'unquotable': 2333, 'cycle_budget_exhausted': 1291}
- Enregistrements de la session : 113838 ; net attendu > 0 : 410 ; simulés (eth_call de la vraie tx) : 22 (ok 5, échec 17) ; étiquettes ghost N+1 : 7/20 positives
- Décisions : {'REJECTED': 113838} ; motifs de rejet : {'below_safety_margin': 361, 'negative_expected_net': 113428, 'p_lower_below_threshold': 398, 'price_impact': 3, 'reliability_not_demonstrated': 12, 'sim_below_estimate': 1, 'simulation_failed': 17, 'stale_data': 40}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 60110169 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 441.669958 USDC | 0.179140 USDC | 0.000000 USDC | 0.003671 USDC | 0.175469 USDC (0.1614 €) | — | 3.97 | 0.083 (n=121) | REJECTED | p_lower_below_threshold(0.08<0.75) |
| 60110169 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.274289 WETH | 0.000111 WETH | 0.000000 WETH | 0.000002 WETH | 0.000109 WETH (0.1614 €) | — | 3.96 | 0.083 (n=121) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.08<0.75) |
| 60110169 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 388.462712 USDC | 0.140972 USDC | 0.000000 USDC | 0.004908 USDC | 0.136064 USDC (0.1252 €) | — | 3.50 | 0.225 (n=1323) | REJECTED | p_lower_below_threshold(0.22<0.75) |
| 60110169 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.236296 WETH | 0.000087 WETH | 0.000000 WETH | 0.000003 WETH | 0.000084 WETH (0.1250 €) | — | 3.56 | 0.225 (n=1323) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.22<0.75) |
| 60110169 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.006181 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1248 €) | — | 3.72 | 0.225 (n=1323) | REJECTED | p_lower_below_threshold(0.22<0.75) |
| 60110169 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 431.212801 USDC | 0.138715 USDC | 0.000000 USDC | 0.003916 USDC | 0.134799 USDC (0.1240 €) | — | 3.13 | 0.076 (n=514) | REJECTED | p_lower_below_threshold(0.08<0.75) |
| 60110169 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.266734 WETH | 0.000086 WETH | 0.000000 WETH | 0.000002 WETH | 0.000083 WETH (0.1240 €) | — | 3.13 | 0.076 (n=514) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.08<0.75) |
| 60122237 | WETH→[pancakeswap_v3]→cbBTC→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.372077 WETH | 0.000046 WETH | 0.000000 WETH | 0.000003 WETH | 0.000043 WETH (0.0634 €) | — | 1.14 | 0.280 (n=1682) | REJECTED | below_safety_margin(42547535035600<74415482743994), p_lower_below_threshold(0.28<0.75) |
| 60122237 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[uniswap_v3]→USDC | 588.718473 USDC | 0.074138 USDC | 0.000000 USDC | 0.005394 USDC | 0.068744 USDC (0.0632 €) | — | 1.17 | 0.280 (n=1682) | REJECTED | below_safety_margin(68744<117743), p_lower_below_threshold(0.28<0.75) |
| 60122237 | cbBTC→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.009313 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0630 €) | — | 1.25 | 0.280 (n=1682) | REJECTED | below_safety_margin(116<186), p_lower_below_threshold(0.28<0.75) |
| 60122237 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.253918 WETH | 0.000045 WETH | 0.000000 WETH | 0.000003 WETH | 0.000042 WETH (0.0626 €) | — | 1.65 | 0.167 (n=46) | REJECTED | below_safety_margin(42015363744851<50783606376479), p_lower_below_threshold(0.17<0.75) |
| 60122237 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 411.277784 USDC | 0.073158 USDC | 0.000000 USDC | 0.005148 USDC | 0.068010 USDC (0.0626 €) | — | 1.65 | 0.167 (n=46) | REJECTED | below_safety_margin(68010<82255), p_lower_below_threshold(0.17<0.75) |
| 60122237 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.006415 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0625 €) | — | 1.79 | 0.167 (n=46) | REJECTED | below_safety_margin(115<128), p_lower_below_threshold(0.17<0.75) |
| 60122237 | cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.004193 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0380 €) | — | 1.67 | 0.280 (n=1682) | REJECTED | below_safety_margin(70<83), p_lower_below_threshold(0.28<0.75) |
| 60122237 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.162854 WETH | 0.000029 WETH | 0.000000 WETH | 0.000003 WETH | 0.000025 WETH (0.0378 €) | — | 1.56 | 0.280 (n=1682) | REJECTED | below_safety_margin(25340036603883<32570824124865), p_lower_below_threshold(0.28<0.75) |
| 60122237 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 266.226905 USDC | 0.046028 USDC | 0.000000 USDC | 0.005148 USDC | 0.040880 USDC (0.0376 €) | — | 1.54 | 0.280 (n=1682) | REJECTED | below_safety_margin(40880<53245), p_lower_below_threshold(0.28<0.75) |
| 60122237 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.004256 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0359 €) | — | 1.55 | 0.280 (n=1682) | REJECTED | below_safety_margin(66<85), p_lower_below_threshold(0.28<0.75) |
| 60122237 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.155427 WETH | 0.000027 WETH | 0.000000 WETH | 0.000003 WETH | 0.000024 WETH (0.0357 €) | — | 1.54 | 0.280 (n=1682) | REJECTED | below_safety_margin(23984509100727<31085346828228), p_lower_below_threshold(0.28<0.75) |
| 60122237 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 241.647917 USDC | 0.043637 USDC | 0.000000 USDC | 0.004903 USDC | 0.038734 USDC (0.0356 €) | — | 1.60 | 0.280 (n=1682) | REJECTED | below_safety_margin(38734<48329), p_lower_below_threshold(0.28<0.75) |
| 60122237 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 153.346101 USDC | 0.037729 USDC | 0.000000 USDC | 0.005148 USDC | 0.032581 USDC (0.0300 €) | — | 2.12 | 0.167 (n=46) | REJECTED | p_lower_below_threshold(0.17<0.75) |
| 60122237 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.002420 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0299 €) | — | 2.27 | 0.167 (n=46) | REJECTED | p_lower_below_threshold(0.17<0.75) |
| 60122237 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.097075 WETH | 0.000023 WETH | 0.000000 WETH | 0.000003 WETH | 0.000020 WETH (0.0298 €) | — | 2.06 | 0.167 (n=46) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.17<0.75) |
| 60122237 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.135846 WETH | 0.000022 WETH | 0.000000 WETH | 0.000002 WETH | 0.000019 WETH (0.0290 €) | — | 1.43 | 0.110 (n=381) | REJECTED | below_safety_margin(19439958078170<27169166854218), p_lower_below_threshold(0.11<0.75) |
| 60122237 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 218.646673 USDC | 0.035357 USDC | 0.000000 USDC | 0.003911 USDC | 0.031446 USDC (0.0289 €) | — | 1.44 | 0.110 (n=381) | REJECTED | below_safety_margin(31446<43729), p_lower_below_threshold(0.11<0.75) |
| 60110169 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 171.483819 USDC | 0.031461 USDC | 0.000000 USDC | 0.003671 USDC | 0.027790 USDC (0.0256 €) | — | 1.62 | 0.110 (n=381) | REJECTED | below_safety_margin(27790<34296), p_lower_below_threshold(0.11<0.75) |

## Fiabilité et décision
- Observations ghost : 8786 ; taux observé 0.233 ; borne inférieure crédible (0.9) 0.227 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 22.7% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
