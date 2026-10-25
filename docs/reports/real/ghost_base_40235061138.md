# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-25T22:55:08+00:00 ; durée 89.03 min ; blocs 53087107 → 53089779 (2664 vus)

## Connexion
- Requêtes RPC : 32634 ; erreurs : 5 ; latence p50/p95 : 82.7/1,260.5 ms
- Rafraîchissements d'état : 2665 ; âge des données au dernier bloc : 1.35 s ; changements de frais LP observés (pools à frais dynamiques) : 4013
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 12740 ; cycles déclenchés par événement : 1579 ; avance médiane sur le rafraîchissement multicall : 461 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,342.73 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 533 pools, 308 jetons, 19442 routes
- Par DEX : uniswap_v3 143, aerodrome 214, aerodrome_slipstream 129, pancakeswap_v3 31, uniswap_v2 13, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 192 (rejetés 2) → 597 jetons ; pools candidats 3802 (énumérés 342, par paires 0), mesurés 535, sous le plancher de 10000.0 $ : 2 → gardés 533 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'DAI': 1.0, 'USDC': 1.0, 'WETH': 2341.931042, 'cbBTC': 80341.676682, 'AERO': 0.683871}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 158,559,654 | 2,342.729153 | 53089779 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 17,508,782 | 0.029133 | 53089779 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,241,320 | 0.029134 | 53089779 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,531,021 | 0.000012 | 53089779 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome | WETH/VVV | 3000 | 8,965,869 | 92.517111 | 53089779 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/USDC | 500 | 8,458,433 | 2,343.234762 | 53089779 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | USDC/AERO | 3000 | 7,482,219 | 1.461904 | 53089779 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,018,986 | 0.001650 | 53089779 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | WETH/USDC | 150 | 5,497,011 | 2,342.982918 | 53089779 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,363,729 | 0.029122 | 53089779 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,460,731 | 2,342.681252 | 53089779 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,227,301 | 1.000002 | 53089779 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,827,538 | 35,066.436414 | 53089779 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/USDC | 3000 | 3,785,956 | 2,343.861882 | 53089779 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 3,230,016 | 0.029120 | 53089779 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2703 | 2,525,768 | 92.485655 | 53089779 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | USDC/cbBTC | 400 | 2,523,449 | 0.000012 | 53089779 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,219,048 | 409.775453 | 53089779 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | WETH/FAI | 10000 | 2,137,339 | 1,218,053.752992 | 53089779 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,902,088 | 0.000000 | 53089779 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,897,595 | 0.000012 | 53089779 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v3 | XDP/USDC | 100 | 1,809,472 | 0.018049 | 53089779 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | USDC/cbBTC | 332 | 1,719,266 | 0.000012 | 53089779 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,718,816 | 0.000012 | 53089779 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | VIRTUAL/WETH | 10000 | 1,572,664 | 0.000265 | 53089779 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,458,755 | 0.825980 | 53089779 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,453,220 | 1.698035 | 53089779 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | WETH/AERO | 3000 | 1,436,548 | 3,424.398529 | 53089779 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,435,087 | 0.005526 | 53089779 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,371,748 | 14,083.179600 | 53089779 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,289,350 | 2,343.088797 | 53089779 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | WETH/AERO | 10000 | 1,258,141 | 3,407.892526 | 53089779 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,244,862 | 0.000267 | 53089779 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | USDC/SEND | 3000 | 1,221,956 | 65.077573 | 53089779 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,167,066 | 35,446,952.567842 | 53089779 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | DRB/WETH | 10000 | 1,163,390 | 0.000000 | 53089779 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | WETH/WELL | 10000 | 1,139,806 | 1,108,395.777449 | 53089779 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,124,468 | 495,982.409025 | 53089779 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | USDC/NOCK | 3000 | 1,088,805 | 52.834565 | 53089779 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome | WETH/EDEL | 7000 | 1,070,300 | 73,420.743697 | 53089779 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,040,819 | 16.951604 | 53089779 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,022,668 | 21,969,859.621726 | 53089779 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | USDC/VVV | 3000 | 974,117 | 0.039457 | 53089779 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/USDC | 10000 | 925,940 | 2,339.202029 | 53089779 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome | WETH/msETH (stable) | 500 | 917,681 | 2.311225 | 53089779 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | WETH/MORPHO | 3000 | 910,778 | 1,129.637219 | 53089779 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | uXRP/WETH | 3000 | 899,561 | 0.000553 | 53089779 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 888,697 | 17.113708 | 53089779 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| uniswap_v3 | WETH/VVV | 10000 | 881,071 | 92.205258 | 53089779 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 874,220 | 18.123599 | 53089779 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v2 | WETH/USDC | 3000 | 848,861 | 2,342.112622 | 53089779 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 806,120 | 0.000008 | 53089779 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | WETH/wstETH | 3000 | 793,213 | 0.803130 | 53089779 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| pancakeswap_v3 | QUID/USDC | 100 | 791,046 | 0.056068 | 53089779 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | weETH_04c0/WETH | 500 | 783,204 | 1.105853 | 53089779 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 747,159 | 0.624357 | 53089779 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 736,067 | 4,781,807.102295 | 53089779 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 719,981 | 0.650490 | 53089779 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/NPC | 3000 | 717,776 | 134,068.673379 | 53089779 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 700,649 | 493,283.472976 | 53089779 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |

## Recherche d'opportunités
- Cycles : 4243 ; routes examinées : 82492406 ; candidats optimisés : 251771 ; net attendu > 0 : 150 ; dernier cycle 183.9 ms
- Rejets (moteur) : {'spread_below_threshold': 80830767, 'liquidity_below_min': 1312599, 'negative_expected_net': 251621, 'unquotable': 92896, 'borrow_bound_too_small': 4243, 'cycle_budget_exhausted': 130}
- Enregistrements de la session : 251771 ; net attendu > 0 : 150 ; simulés (eth_call de la vraie tx) : 13 (ok 3, échec 10) ; étiquettes ghost N+1 : 0/11 positives
- Décisions : {'REJECTED': 251771} ; motifs de rejet : {'below_safety_margin': 130, 'negative_expected_net': 251621, 'p_lower_below_threshold': 133, 'reliability_not_demonstrated': 17, 'sim_below_estimate': 2, 'simulated_net_nonpositive': 2, 'simulation_failed': 10}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53087522 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC | 0.016486 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1666 €) | — | 1.36 | 0.129 (n=327) | REJECTED | below_safety_margin(225<329), p_lower_below_threshold(0.13<0.75) |
| 53087522 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.577121 WETH | 0.000080 WETH | 0.000000 WETH | 0.000003 WETH | 0.000077 WETH (0.1663 €) | — | 1.34 | 0.129 (n=327) | REJECTED | below_safety_margin(77178992824150<115424216900843), p_lower_below_threshold(0.13<0.75) |
| 53087522 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 1,348.818293 USDC | 0.188160 USDC | 0.000000 USDC | 0.007747 USDC | 0.180413 USDC (0.1660 €) | — | 1.34 | 0.129 (n=327) | REJECTED | below_safety_margin(180413<269763), p_lower_below_threshold(0.13<0.75) |
| 53088047 | WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.079575 WETH | 0.000028 WETH | 0.000000 WETH | 0.000003 WETH | 0.000025 WETH (0.0528 €) | — | 3.09 | 0.119 (n=150) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.12<0.75) |
| 53088047 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC | 184.808006 USDC | 0.064257 USDC | 0.000000 USDC | 0.007020 USDC | 0.057237 USDC (0.0527 €) | — | 3.10 | 0.119 (n=150) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 53088047 | WETH→[aerodrome_slipstream]→USDT→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.076234 WETH | 0.000025 WETH | 0.000000 WETH | 0.000003 WETH | 0.000022 WETH (0.0480 €) | — | 2.93 | 0.191 (n=165) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.19<0.75) |
| 53088047 | WETH→[aerodrome_slipstream]→USDT→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.075973 WETH | 0.000025 WETH | 0.000000 WETH | 0.000003 WETH | 0.000022 WETH (0.0479 €) | — | 2.93 | 0.129 (n=327) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.13<0.75) |
| 53088047 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDT→[uniswap_v3]→USDC | 176.937266 USDC | 0.059079 USDC | 0.000000 USDC | 0.007020 USDC | 0.052059 USDC (0.0479 €) | — | 2.94 | 0.191 (n=165) | REJECTED | p_lower_below_threshold(0.19<0.75) |
| 53088047 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDT→[pancakeswap_v3]→USDC | 175.993196 USDC | 0.058953 USDC | 0.000000 USDC | 0.007020 USDC | 0.051933 USDC (0.0478 €) | — | 2.95 | 0.129 (n=327) | REJECTED | p_lower_below_threshold(0.13<0.75) |
| 53088030 | WETH→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.066256 WETH | 0.000016 WETH | 0.000000 WETH | 0.000003 WETH | 0.000013 WETH (0.0279 €) | — | 1.96 | 0.129 (n=327) | REJECTED | below_safety_margin(12983318229092<13251207740808), p_lower_below_threshold(0.13<0.75) |
| 53088030 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→USDC | 153.763631 USDC | 0.037605 USDC | 0.000000 USDC | 0.007377 USDC | 0.030228 USDC (0.0278 €) | — | 1.97 | 0.129 (n=327) | REJECTED | below_safety_margin(30228<30752), p_lower_below_threshold(0.13<0.75) |
| 53087687 | WETH→[aerodrome_slipstream]→LCAP→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.041309 WETH | 0.000015 WETH | 0.000000 WETH | 0.000003 WETH | 0.000012 WETH (0.0248 €) | — | 2.78 | 0.194 (n=162) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.19<0.75) |
| 53087687 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→LCAP→[aerodrome_slipstream]→USDC | 95.748422 USDC | 0.034192 USDC | 0.000000 USDC | 0.007389 USDC | 0.026803 USDC (0.0247 €) | — | 2.80 | 0.194 (n=162) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.19<0.75) |
| 53088047 | WETH→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.057047 WETH | 0.000014 WETH | 0.000000 WETH | 0.000003 WETH | 0.000011 WETH (0.0238 €) | — | 1.94 | 0.129 (n=327) | REJECTED | below_safety_margin(11075952089067<11409358309596), p_lower_below_threshold(0.13<0.75) |
| 53088047 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→cbBTC | 0.001455 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0237 €) | — | 2.20 | 0.129 (n=327) | REJECTED | p_lower_below_threshold(0.13<0.75) |
| 53088047 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 131.570644 USDC | 0.032637 USDC | 0.000000 USDC | 0.007020 USDC | 0.025617 USDC (0.0236 €) | — | 1.95 | 0.129 (n=327) | REJECTED | below_safety_margin(25617<26314), p_lower_below_threshold(0.13<0.75) |
| 53087522 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.292631 WETH | 0.000013 WETH | 0.000000 WETH | 0.000002 WETH | 0.000010 WETH (0.0222 €) | — | 0.35 | 0.022 (n=94) | REJECTED | below_safety_margin(10323917283576<58526124130582), p_lower_below_threshold(0.02<0.75) |
| 53087522 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 683.278827 USDC | 0.029382 USDC | 0.000000 USDC | 0.005257 USDC | 0.024125 USDC (0.0222 €) | — | 0.35 | 0.022 (n=94) | REJECTED | below_safety_margin(24125<136655), p_lower_below_threshold(0.02<0.75) |
| 53088047 | WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.060783 WETH | 0.000012 WETH | 0.000000 WETH | 0.000003 WETH | 0.000009 WETH (0.0198 €) | — | 1.52 | 0.129 (n=327) | REJECTED | below_safety_margin(9228000358070<12156614921570), p_lower_below_threshold(0.13<0.75) |
| 53088047 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC | 141.138985 USDC | 0.028506 USDC | 0.000000 USDC | 0.007020 USDC | 0.021486 USDC (0.0198 €) | — | 1.52 | 0.129 (n=327) | REJECTED | below_safety_margin(21486<28227), p_lower_below_threshold(0.13<0.75) |
| 53087522 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.099667 WETH | 0.000011 WETH | 0.000000 WETH | 0.000002 WETH | 0.000009 WETH (0.0193 €) | — | 0.90 | 0.018 (n=16) | REJECTED | below_safety_margin(8977677215883<19933430314713), reliability_not_demonstrated |
| 53087522 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 230.551841 USDC | 0.026234 USDC | 0.000000 USDC | 0.005257 USDC | 0.020977 USDC (0.0193 €) | — | 0.91 | 0.018 (n=16) | REJECTED | below_safety_margin(20977<46110), reliability_not_demonstrated |
| 53087687 | WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.063207 WETH | 0.000011 WETH | 0.000000 WETH | 0.000003 WETH | 0.000008 WETH (0.0169 €) | — | 1.24 | 0.194 (n=162) | REJECTED | below_safety_margin(7859076637200<12641337951922), p_lower_below_threshold(0.19<0.75) |
| 53087687 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC | 146.745784 USDC | 0.025695 USDC | 0.000000 USDC | 0.007389 USDC | 0.018306 USDC (0.0168 €) | — | 1.25 | 0.194 (n=162) | REJECTED | below_safety_margin(18306<29349), p_lower_below_threshold(0.19<0.75) |
| 53088047 | WETH→[aerodrome_slipstream]→USDT→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.056635 WETH | 0.000011 WETH | 0.000000 WETH | 0.000003 WETH | 0.000008 WETH (0.0163 €) | — | 1.34 | 0.129 (n=327) | REJECTED | below_safety_margin(7571241407882<11326987613384), p_lower_below_threshold(0.13<0.75) |

## Fiabilité et décision
- Observations ghost : 2549 ; taux observé 0.091 ; borne inférieure crédible (0.9) 0.084 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 8.4% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
