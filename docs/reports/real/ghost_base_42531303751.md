# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-09T01:40:26+00:00 ; durée 175.95 min ; blocs 54937445 → 54990191 (10411 vus)

## Connexion
- Requêtes RPC : 136655 ; erreurs : 560 ; latence p50/p95 : 212.3/926.7 ms
- Rafraîchissements d'état : 10411 ; âge des données au dernier bloc : 8.16 s ; changements de frais LP observés (pools à frais dynamiques) : 9251
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 12401 ; cycles déclenchés par événement : 3031 ; avance médiane sur le rafraîchissement multicall : 396 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,128.98 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 466 pools, 272 jetons, 17666 routes
- Par DEX : uniswap_v3 132, aerodrome_slipstream 98, aerodrome 194, pancakeswap_v3 28, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 166 (rejetés 2) → 571 jetons ; pools candidats 3664 (énumérés 289, par paires 0), mesurés 468, sous le plancher de 10000.0 $ : 2 → gardés 466 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2120.787264, 'cbBTC': 74286.143616, 'AERO': 0.573915}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 139,191,246 | 2,128.976777 | 54990212 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,378,733 | 0.028491 | 54990212 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 8,978,103 | 0.000013 | 54990212 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 8,780,430 | 0.028488 | 54990212 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 8,286,523 | 2,131.092481 | 54990212 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,083,747 | 105.536303 | 54990212 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,279,326 | 0.001529 | 54990212 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,935,105 | 0.028498 | 54990212 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 4,619,344 | 1.731034 | 54990212 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,932,925 | 0.999264 | 54990212 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| pancakeswap_v3 | WETH/USDC | 100 | 3,840,995 | 2,131.841464 | 54990212 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | WETH/KTA | 3000 | 3,151,622 | 42,705.985954 | 54990212 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 150 | 3,037,420 | 2,131.634042 | 54990212 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,372,512 | 0.028489 | 54990212 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 1,991,717 | 1,158,197.335472 | 54990212 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 400 | 1,709,680 | 0.000013 | 54990212 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,603,412 | 0.000013 | 54990212 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,568,230 | 0.006496 | 54990212 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,556,113 | 0.000000 | 54990212 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,538,138 | 0.015132 | 54990212 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,468,117 | 1.431451 | 54990212 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,458,031 | 432.812233 | 54990212 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,409,901 | 0.000013 | 54990212 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v3 | WETH/AERO | 3000 | 1,328,596 | 3,685.712412 | 54990212 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v2 | WETH/USDC | 3000 | 1,293,424 | 2,129.856320 | 54990212 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,239,062 | 15,219.572810 | 54990212 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/USDC | 3000 | 1,222,976 | 2,129.940751 | 54990212 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome | USDC/SEND | 3000 | 1,121,162 | 77.304049 | 54990212 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,046,042 | 36,959,791.265206 | 54990212 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,009,960 | 2,131.114677 | 54990212 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | WETH/VVV | 10000 | 1,006,283 | 106.137632 | 54990212 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/BRETT | 10000 | 958,134 | 589,168.703220 | 54990212 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome_slipstream | USDC/VELVET | 100 | 954,663 | 21.758769 | 54990212 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/TOSHI | 10000 | 943,891 | 22,732,275.567050 | 54990212 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/cbBTC | 332 | 926,648 | 0.000013 | 54990212 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | WETH/USDC | 10000 | 910,952 | 2,137.198475 | 54990212 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | DRB/WETH | 10000 | 908,117 | 0.000000 | 54990212 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | USDC/NOCK | 3000 | 907,488 | 76.089759 | 54990212 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/MORPHO | 3000 | 901,558 | 1,048.103382 | 54990212 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 855,286 | 0.824198 | 54990212 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome | WETH/EDEL | 7000 | 826,204 | 101,229.957105 | 54990212 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | USDC/VVV | 3000 | 806,120 | 0.049607 | 54990212 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| pancakeswap_v3 | QUID/USDC | 100 | 780,008 | 0.054371 | 54990212 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/AERO | 10000 | 750,699 | 3,710.542277 | 54990212 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 749,518 | 22.904875 | 54990212 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome | WETH/wstETH | 3000 | 721,504 | 0.801347 | 54990212 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 697,844 | 0.537760 | 54990212 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 651,180 | 5,059,409.098733 | 54990212 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 644,704 | 0.526298 | 54990212 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 626,853 | 0.000008 | 54990212 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v2 | WETH/NPC | 3000 | 619,346 | 149,454.747188 | 54990212 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome | VIRTUAL/WETH | 10000 | 593,225 | 0.000251 | 54990212 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 582,184 | 587,175.700113 | 54990212 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | FLOCK/USDC | 3000 | 570,571 | 0.038863 | 54990212 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome | WETH/msETH (stable) | 500 | 528,489 | 2.462292 | 54990212 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | WETH/MORPHO | 2706 | 511,182 | 1,047.539034 | 54990212 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome | cbBTC/EDGE | 7000 | 505,590 | 926,120.707338 | 54990212 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| uniswap_v3 | USDC/USDT | 100 | 497,191 | 1.001508 | 54990212 | `0xD56da2B74bA826f19015E6B7Dd9Dae1903E85DA1` |
| pancakeswap_v3 | ELSA/USDC | 100 | 495,986 | 0.072561 | 54990212 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| aerodrome | WETH/DRV | 3000 | 492,313 | 6,857.968845 | 54990212 | `0xaC4e562d7C6108f971321F14238E24AE2cC398ac` |

## Recherche d'opportunités
- Cycles : 13441 ; routes examinées : 237448706 ; candidats optimisés : 943491 ; net attendu > 0 : 4790 ; dernier cycle 220.5 ms
- Rejets (moteur) : {'spread_below_threshold': 232550227, 'liquidity_below_min': 3923504, 'negative_expected_net': 938701, 'borrow_bound_too_small': 13438, 'unquotable': 12034, 'cycle_budget_exhausted': 6012}
- Enregistrements de la session : 943491 ; net attendu > 0 : 4790 ; simulés (eth_call de la vraie tx) : 208 (ok 144, échec 64) ; étiquettes ghost N+1 : 84/174 positives
- Décisions : {'REJECTED': 943491} ; motifs de rejet : {'below_safety_margin': 4187, 'negative_expected_net': 938701, 'p_lower_below_threshold': 4455, 'price_impact': 8, 'reliability_not_demonstrated': 335, 'sim_below_estimate': 12, 'simulated_net_nonpositive': 4, 'simulation_failed': 64, 'stale_data': 81}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 54937865 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 369.838495 USDC | 0.450524 USDC | 0.000000 USDC | 0.007098 USDC | 0.443426 USDC (0.4080 €) | — | 11.99 | 0.129 (n=193) | REJECTED | p_lower_below_threshold(0.13<0.75) |
| 54937865 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.004758 cbBTC | 0.000006 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000006 cbBTC (0.4075 €) | — | 12.55 | 0.129 (n=193) | REJECTED | p_lower_below_threshold(0.13<0.75) |
| 54958471 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.724390 WETH | 0.000162 WETH | 0.000000 WETH | 0.000003 WETH | 0.000159 WETH (0.3119 €) | — | 2.20 | 0.053 (n=283) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.05<0.75) |
| 54958471 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 1,536.750926 USDC | 0.343836 USDC | 0.000000 USDC | 0.005436 USDC | 0.338400 USDC (0.3113 €) | — | 2.20 | 0.053 (n=283) | REJECTED | p_lower_below_threshold(0.05<0.75) |
| 54957279 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.003367 cbBTC | 0.000005 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000004 cbBTC (0.3076 €) | — | 13.25 | 0.133 (n=194) | REJECTED | p_lower_below_threshold(0.13<0.75) |
| 54957279 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 260.127433 USDC | 0.340704 USDC | 0.000000 USDC | 0.007419 USDC | 0.333285 USDC (0.3066 €) | — | 12.81 | 0.133 (n=194) | REJECTED | p_lower_below_threshold(0.13<0.75) |
| 54957536 | cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.003414 cbBTC | 0.000004 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000004 cbBTC (0.3021 €) | — | 12.83 | 0.043 (n=118) | REJECTED | p_lower_below_threshold(0.04<0.75) |
| 54957536 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→USDC | 269.547059 USDC | 0.334732 USDC | 0.000000 USDC | 0.006754 USDC | 0.327978 USDC (0.3017 €) | — | 12.17 | 0.043 (n=118) | REJECTED | p_lower_below_threshold(0.04<0.75) |
| 54937865 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→USDC | 328.781193 USDC | 0.334209 USDC | 0.000000 USDC | 0.006775 USDC | 0.327434 USDC (0.3012 €) | — | 9.96 | 0.031 (n=113) | REJECTED | p_lower_below_threshold(0.03<0.75) |
| 54937865 | cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.004323 cbBTC | 0.000005 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000004 cbBTC (0.3010 €) | — | 10.20 | 0.031 (n=113) | REJECTED | p_lower_below_threshold(0.03<0.75) |
| 54958471 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.015122 cbBTC | 0.000004 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000004 cbBTC (0.2778 €) | — | 2.67 | 0.050 (n=29) | REJECTED | reliability_not_demonstrated |
| 54958471 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.521560 WETH | 0.000145 WETH | 0.000000 WETH | 0.000003 WETH | 0.000142 WETH (0.2776 €) | — | 2.72 | 0.050 (n=29) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 54958471 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 1,129.696150 USDC | 0.308254 USDC | 0.000000 USDC | 0.007055 USDC | 0.301199 USDC (0.2771 €) | — | 2.67 | 0.050 (n=29) | REJECTED | reliability_not_demonstrated |
| 54957279 | WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.108597 WETH | 0.000141 WETH | 0.000000 WETH | 0.000003 WETH | 0.000137 WETH (0.2699 €) | — | 12.66 | 0.133 (n=194) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.13<0.75) |
| 54957279 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.003033 cbBTC | 0.000004 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000004 cbBTC (0.2697 €) | — | 12.89 | 0.133 (n=194) | REJECTED | p_lower_below_threshold(0.13<0.75) |
| 54957536 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.003081 cbBTC | 0.000004 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000004 cbBTC (0.2586 €) | — | 12.17 | 0.131 (n=197) | REJECTED | p_lower_below_threshold(0.13<0.75) |
| 54957536 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 241.501279 USDC | 0.287680 USDC | 0.000000 USDC | 0.006754 USDC | 0.280926 USDC (0.2585 €) | — | 11.63 | 0.131 (n=197) | REJECTED | p_lower_below_threshold(0.13<0.75) |
| 54958471 | cbBTC→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.016395 cbBTC | 0.000004 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000004 cbBTC (0.2523 €) | — | 2.24 | 0.189 (n=1164) | REJECTED | p_lower_below_threshold(0.19<0.75) |
| 54958471 | WETH→[pancakeswap_v3]→cbBTC→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.604420 WETH | 0.000132 WETH | 0.000000 WETH | 0.000003 WETH | 0.000129 WETH (0.2521 €) | — | 2.13 | 0.189 (n=1164) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.19<0.75) |
| 54958471 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[uniswap_v3]→USDC | 1,252.676789 USDC | 0.280851 USDC | 0.000000 USDC | 0.007377 USDC | 0.273474 USDC (0.2516 €) | — | 2.18 | 0.189 (n=1164) | REJECTED | p_lower_below_threshold(0.19<0.75) |
| 54937865 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[uniswap_v3]→USDC | 299.072510 USDC | 0.279400 USDC | 0.000000 USDC | 0.006775 USDC | 0.272625 USDC (0.2508 €) | — | 9.12 | 0.031 (n=113) | REJECTED | p_lower_below_threshold(0.03<0.75) |
| 54937865 | cbBTC→[uniswap_v3]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.003892 cbBTC | 0.000004 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000004 cbBTC (0.2505 €) | — | 9.43 | 0.031 (n=113) | REJECTED | p_lower_below_threshold(0.03<0.75) |
| 54937865 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→USDC | 280.437346 USDC | 0.268901 USDC | 0.000000 USDC | 0.006775 USDC | 0.262126 USDC (0.2412 €) | — | 9.35 | 0.031 (n=113) | REJECTED | p_lower_below_threshold(0.03<0.75) |
| 54937865 | cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.003718 cbBTC | 0.000004 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000004 cbBTC (0.2409 €) | — | 9.49 | 0.031 (n=113) | REJECTED | p_lower_below_threshold(0.03<0.75) |
| 54957536 | cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.002784 cbBTC | 0.000003 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000003 cbBTC (0.2124 €) | — | 11.06 | 0.043 (n=118) | REJECTED | p_lower_below_threshold(0.04<0.75) |

## Fiabilité et décision
- Observations ghost : 6609 ; taux observé 0.174 ; borne inférieure crédible (0.9) 0.168 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 16.8% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ✅ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
