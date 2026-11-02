# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-02T12:38:44+00:00 ; durée 210.53 min ; blocs 53410569 → 53416885 (6302 vus)

## Connexion
- Requêtes RPC : 75685 ; erreurs : 5 ; latence p50/p95 : 141.9/625.9 ms
- Rafraîchissements d'état : 6302 ; âge des données au dernier bloc : 2.43 s ; changements de frais LP observés (pools à frais dynamiques) : 5086
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 32601 ; cycles déclenchés par événement : 4736 ; avance médiane sur le rafraîchissement multicall : 492 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,287.28 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 494 pools, 286 jetons, 18438 routes
- Par DEX : uniswap_v3 136, aerodrome_slipstream 108, aerodrome 204, pancakeswap_v3 31, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 175 (rejetés 2) → 580 jetons ; pools candidats 3754 (énumérés 310, par paires 0), mesurés 497, sous le plancher de 10000.0 $ : 3 → gardés 494 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'DAI': 1.0, 'USDC': 1.0, 'WETH': 2295.27604, 'cbBTC': 78216.642548, 'AERO': 0.6263}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 151,614,438 | 2,287.284521 | 53416886 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,333,599 | 0.029381 | 53416886 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,291,808 | 0.000013 | 53416886 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,207,807 | 0.029324 | 53416886 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 7,941,872 | 2,285.153348 | 53416886 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,754,680 | 102.655432 | 53416886 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,656,415 | 0.001583 | 53416886 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 5,476,534 | 1.609370 | 53416886 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,791,145 | 0.029371 | 53416886 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,095,266 | 0.999940 | 53416886 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome_slipstream | WETH/USDC | 150 | 4,079,275 | 2,284.940635 | 53416886 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,001,801 | 2,285.121470 | 53416886 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | WETH/KTA | 3000 | 3,566,724 | 38,488.272424 | 53416886 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,713,834 | 0.029336 | 53416886 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2709 | 2,355,454 | 102.674524 | 53416886 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | USDC/cbBTC | 460 | 2,128,058 | 0.000013 | 53416886 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome | WETH/FAI | 10000 | 2,118,991 | 1,181,275.467329 | 53416886 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | XDP/USDC | 100 | 1,750,827 | 0.018005 | 53416886 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,700,980 | 0.000000 | 53416886 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,665,954 | 0.000013 | 53416886 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,585,382 | 0.000013 | 53416886 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,556,427 | 439.720241 | 53416886 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v2 | WETH/USDC | 3000 | 1,508,139 | 2,287.352925 | 53416886 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,484,903 | 1.552316 | 53416886 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,455,248 | 0.823623 | 53416886 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,421,148 | 3,684.919978 | 53416886 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | WETH/USDC | 3000 | 1,386,428 | 2,288.192303 | 53416886 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,323,118 | 2,285.156306 | 53416886 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,319,090 | 0.005074 | 53416886 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/cbBTC | 340 | 1,303,237 | 0.000013 | 53416886 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,296,841 | 14,958.899241 | 53416886 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | USDC/SEND | 3000 | 1,169,096 | 71.095034 | 53416886 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,122,324 | 37,011,152.892524 | 53416886 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | DRB/WETH | 10000 | 1,071,658 | 0.000000 | 53416886 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,067,328 | 532,755.994890 | 53416886 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,018,866 | 22,522,418.103158 | 53416886 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome | WETH/EDEL | 7000 | 987,824 | 81,807.544994 | 53416886 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome_slipstream | USDC/VELVET | 100 | 980,169 | 20.086374 | 53416886 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | WETH/WELL | 10000 | 954,660 | 1,197,500.001926 | 53416886 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/VVV | 10000 | 937,508 | 102.491248 | 53416886 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 931,565 | 1,026.587714 | 53416886 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/USDC | 10000 | 926,573 | 2,291.133952 | 53416886 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome | USDC/NOCK | 3000 | 904,872 | 76.457838 | 53416886 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | USDC/VVV | 3000 | 900,040 | 0.044876 | 53416886 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | uXRP/WETH | 3000 | 871,120 | 0.000543 | 53416886 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome | WETH/AERO | 10000 | 859,908 | 3,659.352431 | 53416886 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 824,072 | 19.944417 | 53416886 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 795,460 | 0.056692 | 53416886 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 775,038 | 0.801881 | 53416886 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| aerodrome | VIRTUAL/WETH | 10000 | 731,559 | 0.000259 | 53416886 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 724,237 | 0.589782 | 53416886 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 707,481 | 4,941,206.141347 | 53416886 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v2 | WETH/NPC | 3000 | 692,273 | 137,781.589282 | 53416886 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 680,729 | 0.000008 | 53416886 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v3 | TIG/USDC | 10000 | 671,326 | 0.571231 | 53416886 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome | WETH/msETH (stable) | 500 | 662,698 | 2.340905 | 53416886 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | WETH/BRETT | 2108 | 658,366 | 535,427.600478 | 53416886 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome | WETH/bsdETH | 100 | 614,250 | 0.915143 | 53416886 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 595,515 | 0.089100 | 53416886 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| uniswap_v3 | FLOCK/USDC | 3000 | 555,688 | 0.037701 | 53416886 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |

## Recherche d'opportunités
- Cycles : 11037 ; routes examinées : 203500206 ; candidats optimisés : 742814 ; net attendu > 0 : 2486 ; dernier cycle 140.9 ms
- Rejets (moteur) : {'spread_below_threshold': 199354621, 'liquidity_below_min': 3332405, 'negative_expected_net': 740328, 'unquotable': 58978, 'borrow_bound_too_small': 11031, 'cycle_budget_exhausted': 357}
- Enregistrements de la session : 742814 ; net attendu > 0 : 2486 ; simulés (eth_call de la vraie tx) : 342 (ok 329, échec 13) ; étiquettes ghost N+1 : 30/46 positives
- Décisions : {'REJECTED': 742814} ; motifs de rejet : {'below_safety_margin': 1573, 'negative_expected_net': 740328, 'p_lower_below_threshold': 2439, 'reliability_not_demonstrated': 47, 'sim_below_estimate': 10, 'simulated_net_nonpositive': 1, 'simulation_failed': 13, 'stale_data': 48}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53410595 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 1,447.032586 USDC | 0.157806 USDC | 0.000000 USDC | 0.005510 USDC | 0.152296 USDC (0.1401 €) | — | 1.05 | 0.040 (n=168) | REJECTED | below_safety_margin(152296<289406), p_lower_below_threshold(0.04<0.75) |
| 53410595 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.630564 WETH | 0.000069 WETH | 0.000000 WETH | 0.000002 WETH | 0.000066 WETH (0.1399 €) | — | 1.05 | 0.040 (n=168) | REJECTED | below_safety_margin(66270678981474<126112801891045), p_lower_below_threshold(0.04<0.75) |
| 53416066 | USDC→[pancakeswap_v3]→PLAY→[aerodrome_slipstream]→USDC | 54.237506 USDC | 0.072941 USDC | 0.000000 USDC | 0.005138 USDC | 0.067803 USDC (0.0624 €) | 0.067803 USDC | 12.50 | 0.000 (n=66) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53416066 | USDC→[pancakeswap_v3]→PLAY→[aerodrome_slipstream]→USDC | 54.237506 USDC | 0.072941 USDC | 0.000000 USDC | 0.005138 USDC | 0.067803 USDC (0.0624 €) | — | 12.50 | 0.000 (n=66) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 53410636 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.350589 WETH | 0.000027 WETH | 0.000000 WETH | 0.000003 WETH | 0.000024 WETH (0.0500 €) | — | 0.67 | 0.000 (n=18) | REJECTED | below_safety_margin(23656194212510<70117861151909), reliability_not_demonstrated |
| 53410636 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 765.851950 USDC | 0.061509 USDC | 0.000000 USDC | 0.007257 USDC | 0.054252 USDC (0.0499 €) | — | 0.71 | 0.000 (n=18) | REJECTED | below_safety_margin(54252<153170), reliability_not_demonstrated |
| 53410636 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.009456 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0496 €) | — | 0.73 | 0.000 (n=18) | REJECTED | below_safety_margin(69<189), reliability_not_demonstrated |
| 53410636 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 882.865442 USDC | 0.059287 USDC | 0.000000 USDC | 0.005511 USDC | 0.053776 USDC (0.0495 €) | — | 0.61 | 0.040 (n=168) | REJECTED | below_safety_margin(53776<176573), p_lower_below_threshold(0.04<0.75) |
| 53410636 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.386392 WETH | 0.000026 WETH | 0.000000 WETH | 0.000002 WETH | 0.000023 WETH (0.0495 €) | — | 0.61 | 0.040 (n=168) | REJECTED | below_safety_margin(23424222520824<77278424033372), p_lower_below_threshold(0.04<0.75) |
| 53413612 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.372496 WETH | 0.000024 WETH | 0.000000 WETH | 0.000002 WETH | 0.000022 WETH (0.0459 €) | — | 0.59 | 0.040 (n=168) | REJECTED | below_safety_margin(21809808950113<74499275646633), p_lower_below_threshold(0.04<0.75) |
| 53413612 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.372496 WETH | 0.000024 WETH | 0.000000 WETH | 0.000002 WETH | 0.000022 WETH (0.0459 €) | — | 0.59 | 0.040 (n=168) | REJECTED | below_safety_margin(21809808950113<74499275646633), p_lower_below_threshold(0.04<0.75) |
| 53413612 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 849.626409 USDC | 0.054991 USDC | 0.000000 USDC | 0.005144 USDC | 0.049847 USDC (0.0459 €) | — | 0.59 | 0.040 (n=168) | REJECTED | below_safety_margin(49847<169925), p_lower_below_threshold(0.04<0.75) |
| 53413612 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 849.626409 USDC | 0.054991 USDC | 0.000000 USDC | 0.005144 USDC | 0.049847 USDC (0.0459 €) | — | 0.59 | 0.040 (n=168) | REJECTED | below_safety_margin(49847<169925), p_lower_below_threshold(0.04<0.75) |
| 53410636 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 387.151185 USDC | 0.052234 USDC | 0.000000 USDC | 0.005511 USDC | 0.046723 USDC (0.0430 €) | — | 1.21 | 0.040 (n=168) | REJECTED | below_safety_margin(46723<77430), p_lower_below_threshold(0.04<0.75) |
| 53410636 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.168841 WETH | 0.000023 WETH | 0.000000 WETH | 0.000002 WETH | 0.000020 WETH (0.0430 €) | — | 1.21 | 0.040 (n=168) | REJECTED | below_safety_margin(20353315597733<33768283269838), p_lower_below_threshold(0.04<0.75) |
| 53416066 | USDC→[pancakeswap_v3]→PLAY→[aerodrome]→USDC | 17.433486 USDC | 0.032551 USDC | 0.000000 USDC | 0.004822 USDC | 0.027729 USDC (0.0255 €) | 0.027729 USDC | 15.91 | 0.055 (n=15) | REJECTED | reliability_not_demonstrated |
| 53416066 | USDC→[pancakeswap_v3]→PLAY→[aerodrome]→USDC | 17.433486 USDC | 0.032551 USDC | 0.000000 USDC | 0.004822 USDC | 0.027729 USDC (0.0255 €) | — | 15.91 | 0.055 (n=15) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53410595 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 259.656886 USDC | 0.023826 USDC | 0.000000 USDC | 0.005510 USDC | 0.018316 USDC (0.0169 €) | — | 0.71 | 0.006 (n=51) | REJECTED | below_safety_margin(18316<51931), p_lower_below_threshold(0.01<0.75) |
| 53410595 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.113329 WETH | 0.000010 WETH | 0.000000 WETH | 0.000002 WETH | 0.000008 WETH (0.0168 €) | — | 0.70 | 0.006 (n=51) | REJECTED | below_safety_margin(7968852859601<22665881144521), p_lower_below_threshold(0.01<0.75) |
| 53416808 | WETH→[pancakeswap_v3]→EURC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.043943 WETH | 0.000011 WETH | 0.000000 WETH | 0.000003 WETH | 0.000008 WETH (0.0164 €) | — | 1.77 | 0.140 (n=739) | REJECTED | below_safety_margin(7789800509342<8788555099835), p_lower_below_threshold(0.14<0.75) |
| 53416808 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→EURC→[aerodrome_slipstream]→USDC | 100.424227 USDC | 0.024666 USDC | 0.000000 USDC | 0.006882 USDC | 0.017784 USDC (0.0164 €) | — | 1.77 | 0.140 (n=739) | REJECTED | below_safety_margin(17784<20084), p_lower_below_threshold(0.14<0.75) |
| 53416808 | WETH→[pancakeswap_v3]→EURC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.043935 WETH | 0.000011 WETH | 0.000000 WETH | 0.000003 WETH | 0.000008 WETH (0.0162 €) | — | 1.76 | 0.140 (n=739) | REJECTED | below_safety_margin(7716431328358<8787000917102), p_lower_below_threshold(0.14<0.75) |
| 53416808 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→EURC→[aerodrome_slipstream]→USDC | 100.276377 USDC | 0.024498 USDC | 0.000000 USDC | 0.006882 USDC | 0.017616 USDC (0.0162 €) | — | 1.76 | 0.140 (n=739) | REJECTED | below_safety_margin(17616<20055), p_lower_below_threshold(0.14<0.75) |
| 53415439 | USDC→[pancakeswap_v3]→ICNT→[uniswap_v3]→USDC | 37.377443 USDC | 0.022471 USDC | 0.000000 USDC | 0.005138 USDC | 0.017333 USDC (0.0159 €) | 0.017333 USDC | 4.64 | 0.029 (n=200) | REJECTED | p_lower_below_threshold(0.03<0.75) |
| 53415439 | USDC→[pancakeswap_v3]→ICNT→[uniswap_v3]→USDC | 37.377443 USDC | 0.022471 USDC | 0.000000 USDC | 0.005138 USDC | 0.017333 USDC (0.0159 €) | 0.017333 USDC | 4.64 | 0.029 (n=200) | REJECTED | p_lower_below_threshold(0.03<0.75) |

## Fiabilité et décision
- Observations ghost : 4393 ; taux observé 0.139 ; borne inférieure crédible (0.9) 0.133 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 13.3% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ✅ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
