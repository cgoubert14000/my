# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-02T12:41:52+00:00 ; durée 213.68 min ; blocs 53410569 → 53416979 (6390 vus)

## Connexion
- Requêtes RPC : 76883 ; erreurs : 8 ; latence p50/p95 : 112.0/1,352.7 ms
- Rafraîchissements d'état : 6390 ; âge des données au dernier bloc : 2.83 s ; changements de frais LP observés (pools à frais dynamiques) : 5210
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 33527 ; cycles déclenchés par événement : 4801 ; avance médiane sur le rafraîchissement multicall : 414 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,285.24 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 494 pools, 286 jetons, 18438 routes
- Par DEX : uniswap_v3 136, aerodrome_slipstream 108, aerodrome 204, pancakeswap_v3 31, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 175 (rejetés 2) → 580 jetons ; pools candidats 3754 (énumérés 310, par paires 0), mesurés 497, sous le plancher de 10000.0 $ : 3 → gardés 494 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'DAI': 1.0, 'USDC': 1.0, 'WETH': 2295.27604, 'cbBTC': 78216.642548, 'AERO': 0.6263}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 151,536,277 | 2,285.239546 | 53416979 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,324,532 | 0.029359 | 53416979 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,291,108 | 0.000013 | 53416979 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,202,668 | 0.029324 | 53416979 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 7,936,680 | 2,279.469138 | 53416979 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,747,747 | 102.655432 | 53416979 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,655,391 | 0.001583 | 53416979 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 5,472,875 | 1.611523 | 53416979 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,788,404 | 0.029355 | 53416979 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,094,636 | 0.999940 | 53416979 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome_slipstream | WETH/USDC | 150 | 4,076,539 | 2,279.762606 | 53416979 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/USDC | 100 | 3,999,101 | 2,279.429150 | 53416979 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | WETH/KTA | 3000 | 3,563,536 | 38,488.272424 | 53416979 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,670,930 | 0.029336 | 53416979 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2700 | 2,353,348 | 102.674524 | 53416979 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | USDC/cbBTC | 544 | 2,121,847 | 0.000013 | 53416979 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome | WETH/FAI | 10000 | 2,117,097 | 1,181,275.467329 | 53416979 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | XDP/USDC | 100 | 1,750,618 | 0.018001 | 53416979 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,699,459 | 0.000000 | 53416979 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,665,819 | 0.000013 | 53416979 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,585,251 | 0.000013 | 53416979 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,555,035 | 439.720241 | 53416979 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v2 | WETH/USDC | 3000 | 1,507,465 | 2,285.686002 | 53416979 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,484,903 | 1.552316 | 53416979 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,455,248 | 0.823623 | 53416979 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,419,495 | 3,684.921875 | 53416979 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | WETH/USDC | 3000 | 1,385,808 | 2,286.242476 | 53416979 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,322,293 | 2,279.526109 | 53416979 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,317,911 | 0.005074 | 53416979 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/cbBTC | 360 | 1,303,102 | 0.000013 | 53416979 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,296,227 | 14,958.899241 | 53416979 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | USDC/SEND | 3000 | 1,169,096 | 71.095034 | 53416979 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,121,320 | 37,011,152.892524 | 53416979 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | DRB/WETH | 10000 | 1,070,699 | 0.000000 | 53416979 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,066,374 | 532,755.994890 | 53416979 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,017,955 | 22,522,418.103158 | 53416979 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome | WETH/EDEL | 7000 | 986,940 | 81,807.544994 | 53416979 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome_slipstream | USDC/VELVET | 100 | 980,044 | 20.093927 | 53416979 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | WETH/WELL | 10000 | 953,806 | 1,197,500.001926 | 53416979 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/VVV | 10000 | 936,670 | 102.491248 | 53416979 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 930,732 | 1,026.587714 | 53416979 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/USDC | 10000 | 926,298 | 2,291.133952 | 53416979 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome | USDC/NOCK | 3000 | 904,872 | 76.457838 | 53416979 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | USDC/VVV | 3000 | 899,433 | 0.044954 | 53416979 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | uXRP/WETH | 3000 | 870,339 | 0.000543 | 53416979 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome | WETH/AERO | 10000 | 858,950 | 3,659.352431 | 53416979 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 824,072 | 19.944417 | 53416979 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 794,422 | 0.056536 | 53416979 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 774,345 | 0.801881 | 53416979 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| aerodrome | VIRTUAL/WETH | 10000 | 730,905 | 0.000259 | 53416979 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 723,748 | 0.587851 | 53416979 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 706,849 | 4,941,206.141347 | 53416979 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v2 | WETH/NPC | 3000 | 692,049 | 137,624.709043 | 53416979 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 680,137 | 0.000008 | 53416979 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v3 | TIG/USDC | 10000 | 671,298 | 0.571184 | 53416979 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome | WETH/msETH (stable) | 500 | 662,105 | 2.340905 | 53416979 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 657,778 | 535,427.600478 | 53416979 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome | WETH/bsdETH | 100 | 613,700 | 0.915143 | 53416979 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 595,216 | 0.089032 | 53416979 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 554,265 | 1,026.688513 | 53416979 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |

## Recherche d'opportunités
- Cycles : 11190 ; routes examinées : 206321220 ; candidats optimisés : 768838 ; net attendu > 0 : 4150 ; dernier cycle 620.0 ms
- Rejets (moteur) : {'spread_below_threshold': 202072702, 'liquidity_below_min': 3407103, 'negative_expected_net': 764688, 'unquotable': 60814, 'borrow_bound_too_small': 11184, 'cycle_budget_exhausted': 579}
- Enregistrements de la session : 768838 ; net attendu > 0 : 4150 ; simulés (eth_call de la vraie tx) : 485 (ok 463, échec 22) ; étiquettes ghost N+1 : 52/71 positives
- Décisions : {'REJECTED': 768838} ; motifs de rejet : {'below_safety_margin': 2735, 'negative_expected_net': 764688, 'p_lower_below_threshold': 4035, 'reliability_not_demonstrated': 115, 'sim_below_estimate': 26, 'simulated_net_nonpositive': 6, 'simulation_failed': 22, 'stale_data': 68}

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
| 53416929 | WETH→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.059525 WETH | 0.000013 WETH | 0.000000 WETH | 0.000003 WETH | 0.000010 WETH (0.0212 €) | — | 1.70 | 0.149 (n=747) | REJECTED | below_safety_margin(10093977755541<11904948760213), p_lower_below_threshold(0.15<0.75) |
| 53416929 | WETH→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.059525 WETH | 0.000013 WETH | 0.000000 WETH | 0.000003 WETH | 0.000010 WETH (0.0212 €) | — | 1.70 | 0.149 (n=747) | REJECTED | below_safety_margin(10093977755541<11904948760213), p_lower_below_threshold(0.15<0.75) |
| 53416929 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→USDC | 136.494321 USDC | 0.029901 USDC | 0.000000 USDC | 0.006885 USDC | 0.023016 USDC (0.0212 €) | — | 1.69 | 0.149 (n=747) | REJECTED | below_safety_margin(23016<27298), p_lower_below_threshold(0.15<0.75) |
| 53416929 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→USDC | 136.494321 USDC | 0.029901 USDC | 0.000000 USDC | 0.006885 USDC | 0.023016 USDC (0.0212 €) | — | 1.69 | 0.149 (n=747) | REJECTED | below_safety_margin(23016<27298), p_lower_below_threshold(0.15<0.75) |
| 53416967 | cbBTC→[aerodrome_slipstream]→EURC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.000887 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0208 €) | — | 3.27 | 0.138 (n=555) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 53416967 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→EURC→[aerodrome_slipstream]→USDC | 69.553694 USDC | 0.029092 USDC | 0.000000 USDC | 0.006882 USDC | 0.022210 USDC (0.0204 €) | — | 3.19 | 0.138 (n=555) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 53410595 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 259.656886 USDC | 0.023826 USDC | 0.000000 USDC | 0.005510 USDC | 0.018316 USDC (0.0169 €) | — | 0.71 | 0.006 (n=51) | REJECTED | below_safety_margin(18316<51931), p_lower_below_threshold(0.01<0.75) |
| 53410595 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.113329 WETH | 0.000010 WETH | 0.000000 WETH | 0.000002 WETH | 0.000008 WETH (0.0168 €) | — | 0.70 | 0.006 (n=51) | REJECTED | below_safety_margin(7968852859601<22665881144521), p_lower_below_threshold(0.01<0.75) |

## Fiabilité et décision
- Observations ghost : 4418 ; taux observé 0.144 ; borne inférieure crédible (0.9) 0.137 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 13.7% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ✅ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
