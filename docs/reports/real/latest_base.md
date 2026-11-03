# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-03T16:35:36+00:00 ; durée 203.98 min ; blocs 53461072 → 53467192 (6064 vus)

## Connexion
- Requêtes RPC : 70875 ; erreurs : 106 ; latence p50/p95 : 155.7/1,023.5 ms
- Rafraîchissements d'état : 6064 ; âge des données au dernier bloc : 2.36 s ; changements de frais LP observés (pools à frais dynamiques) : 11340
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 68991 ; cycles déclenchés par événement : 4713 ; avance médiane sur le rafraîchissement multicall : 448 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,289.46 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 492 pools, 286 jetons, 19214 routes
- Par DEX : uniswap_v3 138, aerodrome_slipstream 108, aerodrome 204, pancakeswap_v3 28, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 174 (rejetés 2) → 579 jetons ; pools candidats 3706 (énumérés 309, par paires 0), mesurés 495, sous le plancher de 10000.0 $ : 3 → gardés 492 (max 1500) ; prix des hubs : {'USDC': 1.0, 'DAI': 1.0, 'USDbC': 1.0, 'WETH': 2276.593928, 'cbBTC': 77247.513172, 'AERO': 0.617437}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 151,503,912 | 2,289.461284 | 53467191 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,378,678 | 0.029557 | 53467191 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,191,472 | 0.029576 | 53467191 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 8,999,134 | 0.000013 | 53467191 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 8,062,692 | 2,289.411952 | 53467191 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,718,211 | 103.747440 | 53467191 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,606,974 | 0.001575 | 53467191 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 5,465,845 | 1.556022 | 53467191 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,877,992 | 0.029561 | 53467191 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,160,154 | 2,288.970307 | 53467191 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 202 | 4,076,272 | 0.999666 | 53467191 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome_slipstream | WETH/USDC | 150 | 3,916,103 | 2,288.994875 | 53467192 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome | WETH/KTA | 3000 | 3,422,924 | 41,868.548258 | 53467191 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,709,763 | 0.029581 | 53467191 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 2,168,130 | 1,130,485.614086 | 53467191 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | WETH/VVV | 2703 | 2,099,864 | 103.775696 | 53467191 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | USDC/cbBTC | 448 | 1,811,728 | 0.000013 | 53467191 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | XDP/USDC | 100 | 1,733,362 | 0.017722 | 53467192 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,682,074 | 0.000000 | 53467191 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,639,274 | 0.000013 | 53467192 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,556,185 | 441.576545 | 53467191 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,554,793 | 1.429892 | 53467191 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,552,076 | 0.000013 | 53467191 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v2 | WETH/USDC | 3000 | 1,508,971 | 2,290.298707 | 53467191 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,454,645 | 0.821370 | 53467191 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,444,431 | 3,558.736179 | 53467191 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | WETH/USDC | 3000 | 1,344,374 | 2,291.456959 | 53467191 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,342,515 | 2,289.291310 | 53467191 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,320,189 | 0.005074 | 53467191 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,291,617 | 14,920.868627 | 53467191 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome_slipstream | USDC/cbBTC | 336 | 1,236,713 | 0.000013 | 53467191 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/SEND | 3000 | 1,158,709 | 72.375481 | 53467191 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,126,220 | 36,865,390.282140 | 53467191 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,061,566 | 542,640.755442 | 53467191 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,036,168 | 21,938,543.803452 | 53467191 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | DRB/WETH | 10000 | 1,019,731 | 0.000000 | 53467191 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome_slipstream | USDC/VELVET | 100 | 995,070 | 19.221497 | 53467191 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | WETH/EDEL | 7000 | 961,084 | 86,569.219540 | 53467191 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/MORPHO | 3000 | 942,735 | 1,061.435903 | 53467191 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/VVV | 10000 | 941,570 | 103.023324 | 53467191 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome | WETH/WELL | 10000 | 935,029 | 1,250,688.215368 | 53467191 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/USDC | 10000 | 929,353 | 2,282.122456 | 53467191 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome | USDC/NOCK | 3000 | 923,799 | 73.357416 | 53467191 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | USDC/VVV | 3000 | 885,347 | 0.045409 | 53467191 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | uXRP/WETH | 3000 | 878,346 | 0.000552 | 53467191 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome | WETH/AERO | 10000 | 857,695 | 3,570.513893 | 53467191 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 823,510 | 19.974697 | 53467191 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 798,841 | 0.057197 | 53467191 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 777,105 | 0.799140 | 53467191 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 735,820 | 0.589298 | 53467191 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| aerodrome | VIRTUAL/WETH | 10000 | 727,074 | 0.000257 | 53467191 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 717,313 | 4,817,339.736288 | 53467191 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 679,648 | 0.000008 | 53467191 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v2 | WETH/NPC | 3000 | 667,790 | 148,391.109004 | 53467191 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome | WETH/msETH (stable) | 500 | 662,602 | 2.343097 | 53467191 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | TIG/USDC | 10000 | 658,292 | 0.545000 | 53467191 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 652,743 | 546,878.948658 | 53467191 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome | WETH/bsdETH | 100 | 614,998 | 0.914657 | 53467191 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 585,317 | 0.086750 | 53467191 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| uniswap_v3 | FLOCK/USDC | 3000 | 568,126 | 0.038937 | 53467191 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |

## Recherche d'opportunités
- Cycles : 10776 ; routes examinées : 207050064 ; candidats optimisés : 577380 ; net attendu > 0 : 882 ; dernier cycle 86.9 ms
- Rejets (moteur) : {'spread_below_threshold': 202977724, 'liquidity_below_min': 3317859, 'negative_expected_net': 576498, 'pool_quarantined': 128124, 'unquotable': 33862, 'borrow_bound_too_small': 10768, 'cycle_budget_exhausted': 4347}
- Enregistrements de la session : 577380 ; net attendu > 0 : 882 ; simulés (eth_call de la vraie tx) : 64 (ok 11, échec 53) ; étiquettes ghost N+1 : 6/54 positives
- Décisions : {'REJECTED': 577380} ; motifs de rejet : {'below_safety_margin': 676, 'negative_expected_net': 576498, 'p_lower_below_threshold': 824, 'price_impact': 14, 'reliability_not_demonstrated': 58, 'sim_below_estimate': 2, 'simulated_net_nonpositive': 2, 'simulation_failed': 53}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53463332 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 2,541.897939 USDC | 0.510453 USDC | 0.000000 USDC | 0.005620 USDC | 0.504833 USDC (0.4644 €) | — | 1.99 | 0.034 (n=196) | REJECTED | below_safety_margin(504833<508379), p_lower_below_threshold(0.03<0.75) |
| 53463333 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 2,541.897939 USDC | 0.510453 USDC | 0.000000 USDC | 0.005620 USDC | 0.504833 USDC (0.4644 €) | — | 1.99 | 0.034 (n=196) | REJECTED | below_safety_margin(504833<508379), p_lower_below_threshold(0.03<0.75) |
| 53463332 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 1.112655 WETH | 0.000223 WETH | 0.000000 WETH | 0.000002 WETH | 0.000221 WETH (0.4634 €) | — | 1.98 | 0.034 (n=196) | REJECTED | below_safety_margin(220793398221565<222530927350268), p_lower_below_threshold(0.03<0.75) |
| 53463333 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 1.112655 WETH | 0.000223 WETH | 0.000000 WETH | 0.000002 WETH | 0.000221 WETH (0.4634 €) | — | 1.98 | 0.034 (n=196) | REJECTED | below_safety_margin(220793398221565<222530927350268), p_lower_below_threshold(0.03<0.75) |
| 53463325 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 2,161.011839 USDC | 0.458620 USDC | 0.000000 USDC | 0.007599 USDC | 0.451021 USDC (0.4149 €) | — | 2.09 | 0.039 (n=21) | REJECTED | reliability_not_demonstrated |
| 53463325 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.939134 WETH | 0.000201 WETH | 0.000000 WETH | 0.000003 WETH | 0.000197 WETH (0.4144 €) | — | 2.10 | 0.039 (n=21) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53463325 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.026928 cbBTC | 0.000006 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000006 cbBTC (0.4142 €) | — | 2.17 | 0.039 (n=21) | REJECTED | reliability_not_demonstrated |
| 53462613 | USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→USDC | 2,437.832122 USDC | 0.380030 USDC | 0.000000 USDC | 0.005524 USDC | 0.374506 USDC (0.3445 €) | — | 1.54 | 0.035 (n=191) | REJECTED | below_safety_margin(374506<487566), p_lower_below_threshold(0.03<0.75) |
| 53462613 | cbBTC→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.017895 cbBTC | 0.000003 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000003 cbBTC (0.2361 €) | — | 1.86 | 0.035 (n=191) | REJECTED | below_safety_margin(332<357), p_lower_below_threshold(0.03<0.75) |
| 53462613 | USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→USDC | 1,456.013948 USDC | 0.261195 USDC | 0.000000 USDC | 0.005177 USDC | 0.256018 USDC (0.2355 €) | — | 1.76 | 0.035 (n=191) | REJECTED | below_safety_margin(256018<291202), p_lower_below_threshold(0.03<0.75) |
| 53463086 | WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.080292 WETH | 0.000096 WETH | 0.000000 WETH | 0.000003 WETH | 0.000093 WETH (0.1953 €) | — | 11.59 | 0.104 (n=113) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.10<0.75) |
| 53463086 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC | 183.058743 USDC | 0.219783 USDC | 0.000000 USDC | 0.007608 USDC | 0.212175 USDC (0.1952 €) | — | 11.59 | 0.104 (n=113) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53464609 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.018425 cbBTC | 0.000003 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000003 cbBTC (0.1948 €) | — | 1.49 | 0.037 (n=22) | REJECTED | below_safety_margin(274<368), reliability_not_demonstrated |
| 53464609 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 1,469.043519 USDC | 0.219155 USDC | 0.000000 USDC | 0.007595 USDC | 0.211560 USDC (0.1946 €) | — | 1.44 | 0.037 (n=22) | REJECTED | below_safety_margin(211560<293808), reliability_not_demonstrated |
| 53464609 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.631609 WETH | 0.000096 WETH | 0.000000 WETH | 0.000003 WETH | 0.000093 WETH (0.1944 €) | — | 1.46 | 0.037 (n=22) | REJECTED | below_safety_margin(92530146250747<126321894567622), reliability_not_demonstrated |
| 53463086 | WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.077981 WETH | 0.000095 WETH | 0.000000 WETH | 0.000003 WETH | 0.000091 WETH (0.1911 €) | — | 11.68 | 0.104 (n=113) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.10<0.75) |
| 53463086 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC | 177.444601 USDC | 0.215528 USDC | 0.000000 USDC | 0.007954 USDC | 0.207574 USDC (0.1910 €) | — | 11.70 | 0.104 (n=113) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53463086 | WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.078998 WETH | 0.000093 WETH | 0.000000 WETH | 0.000003 WETH | 0.000090 WETH (0.1879 €) | — | 11.33 | 0.104 (n=113) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.10<0.75) |
| 53463086 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC | 179.899012 USDC | 0.211745 USDC | 0.000000 USDC | 0.007608 USDC | 0.204137 USDC (0.1878 €) | — | 11.35 | 0.104 (n=113) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53463086 | WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.078379 WETH | 0.000093 WETH | 0.000000 WETH | 0.000003 WETH | 0.000089 WETH (0.1875 €) | — | 11.40 | 0.104 (n=113) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53463086 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC | 178.637756 USDC | 0.211322 USDC | 0.000000 USDC | 0.007608 USDC | 0.203714 USDC (0.1874 €) | — | 11.40 | 0.104 (n=113) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53463086 | WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.078819 WETH | 0.000092 WETH | 0.000000 WETH | 0.000003 WETH | 0.000089 WETH (0.1867 €) | — | 11.29 | 0.104 (n=113) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53463086 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC | 179.287953 USDC | 0.210412 USDC | 0.000000 USDC | 0.007608 USDC | 0.202804 USDC (0.1866 €) | — | 11.31 | 0.104 (n=113) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53462613 | cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.014168 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1693 €) | — | 1.68 | 0.035 (n=191) | REJECTED | below_safety_margin(238<283), p_lower_below_threshold(0.03<0.75) |
| 53462613 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 1,040.360009 USDC | 0.188515 USDC | 0.000000 USDC | 0.005177 USDC | 0.183338 USDC (0.1687 €) | — | 1.76 | 0.035 (n=191) | REJECTED | below_safety_margin(183338<208072), p_lower_below_threshold(0.03<0.75) |

## Fiabilité et décision
- Observations ghost : 4889 ; taux observé 0.170 ; borne inférieure crédible (0.9) 0.163 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 16.3% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
