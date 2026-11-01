# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-01T22:26:58+00:00 ; durée 36.74 min ; blocs 53390229 → 53391334 (1094 vus)

## Connexion
- Requêtes RPC : 12741 ; erreurs : 0 ; latence p50/p95 : 268.3/1,160.2 ms
- Rafraîchissements d'état : 1094 ; âge des données au dernier bloc : 2.41 s ; changements de frais LP observés (pools à frais dynamiques) : 1466
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 11435 ; cycles déclenchés par événement : 1706 ; avance médiane sur le rafraîchissement multicall : 532 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,254.15 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 495 pools, 288 jetons, 18180 routes
- Par DEX : uniswap_v3 138, aerodrome_slipstream 111, aerodrome 203, pancakeswap_v3 29, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 176 (rejetés 2) → 581 jetons ; pools candidats 3720 (énumérés 312, par paires 0), mesurés 498, sous le plancher de 10000.0 $ : 3 → gardés 495 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDbC': 1.0, 'USDC': 1.0, 'WETH': 2258.829928, 'cbBTC': 77854.490121, 'AERO': 0.63182}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 150,197,522 | 2,254.154960 | 53391334 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,105,835 | 0.029035 | 53391334 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,311,789 | 0.000013 | 53391334 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,124,369 | 0.029037 | 53391334 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 7,877,078 | 2,253.297371 | 53391334 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,798,260 | 98.724514 | 53391334 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,620,373 | 0.001574 | 53391334 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 5,532,295 | 1.595186 | 53391334 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,142,002 | 0.029044 | 53391334 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,087,689 | 0.998850 | 53391334 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome_slipstream | WETH/USDC | 150 | 4,041,626 | 2,253.772375 | 53391334 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/USDC | 100 | 3,932,566 | 2,253.842396 | 53391334 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | WETH/KTA | 3000 | 3,536,480 | 38,023.521520 | 53391334 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2525 | 2,687,275 | 0.029034 | 53391334 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2718 | 2,373,351 | 98.735002 | 53391334 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | USDC/cbBTC | 424 | 2,123,701 | 0.000013 | 53391334 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome | WETH/FAI | 10000 | 2,082,298 | 1,188,094.920793 | 53391334 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | XDP/USDC | 100 | 1,755,364 | 0.018053 | 53391334 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,748,704 | 0.000000 | 53391334 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,624,031 | 0.000013 | 53391334 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,580,738 | 0.000013 | 53391334 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,544,748 | 429.338373 | 53391334 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v2 | WETH/USDC | 3000 | 1,503,666 | 2,251.495056 | 53391334 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,484,903 | 1.552316 | 53391334 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,457,642 | 0.825542 | 53391334 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,413,989 | 3,593.084075 | 53391334 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | WETH/USDC | 3000 | 1,377,777 | 2,252.846516 | 53391334 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,335,024 | 2,254.264370 | 53391334 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,328,745 | 0.005210 | 53391334 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/cbBTC | 332 | 1,300,291 | 0.000013 | 53391334 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,300,095 | 14,763.271835 | 53391334 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | USDC/SEND | 3000 | 1,169,003 | 71.106813 | 53391334 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,113,910 | 36,002,670.776723 | 53391334 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,060,894 | 520,184.169602 | 53391334 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,046,107 | 0.000000 | 53391334 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,006,301 | 22,413,230.182816 | 53391334 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | WETH/VVV | 10000 | 991,085 | 98.703042 | 53391334 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome_slipstream | USDC/VELVET | 100 | 988,175 | 19.611802 | 53391334 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | WETH/EDEL | 7000 | 973,324 | 81,876.007680 | 53391334 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | WETH/WELL | 10000 | 948,205 | 1,178,950.343524 | 53391334 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome | USDC/NOCK | 3000 | 942,922 | 70.411426 | 53391334 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/MORPHO | 3000 | 926,198 | 1,004.452893 | 53391334 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/USDC | 10000 | 921,556 | 2,252.785626 | 53391334 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | USDC/VVV | 3000 | 916,036 | 0.043825 | 53391334 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | uXRP/WETH | 3000 | 861,435 | 0.000548 | 53391334 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome | WETH/AERO | 10000 | 861,412 | 3,567.989120 | 53391334 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | USDC/SAPIEN | 4510 | 833,719 | 19.594831 | 53391334 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 821,182 | 0.060661 | 53391334 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 763,818 | 0.801881 | 53391334 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 725,113 | 0.589757 | 53391334 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| aerodrome | VIRTUAL/WETH | 10000 | 724,566 | 0.000261 | 53391334 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 714,374 | 4,705,794.573259 | 53391334 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v2 | WETH/NPC | 3000 | 689,398 | 134,906.561251 | 53391334 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | AERO/cbBTC | 2700 | 684,535 | 0.000008 | 53391334 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v3 | TIG/USDC | 10000 | 673,795 | 0.569765 | 53391334 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | WETH/BRETT | 2162 | 656,966 | 523,388.395537 | 53391334 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome | WETH/msETH (stable) | 500 | 656,603 | 2.340198 | 53391334 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 605,617 | 0.091427 | 53391334 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| aerodrome | WETH/bsdETH | 100 | 605,203 | 0.915597 | 53391334 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| uniswap_v3 | FLOCK/USDC | 3000 | 575,833 | 0.039806 | 53391334 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |

## Recherche d'opportunités
- Cycles : 2799 ; routes examinées : 50885820 ; candidats optimisés : 145759 ; net attendu > 0 : 438 ; dernier cycle 192.4 ms
- Rejets (moteur) : {'spread_below_threshold': 50037371, 'liquidity_below_min': 689440, 'negative_expected_net': 145321, 'unquotable': 10386, 'borrow_bound_too_small': 2799, 'cycle_budget_exhausted': 65}
- Enregistrements de la session : 145759 ; net attendu > 0 : 438 ; simulés (eth_call de la vraie tx) : 25 (ok 9, échec 16) ; étiquettes ghost N+1 : 2/16 positives
- Décisions : {'REJECTED': 145759} ; motifs de rejet : {'below_safety_margin': 329, 'negative_expected_net': 145321, 'p_lower_below_threshold': 415, 'reliability_not_demonstrated': 23, 'sim_below_estimate': 1, 'simulation_failed': 16, 'stale_data': 62}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53390954 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 599.027739 USDC | 0.135348 USDC | 0.000000 USDC | 0.005071 USDC | 0.130277 USDC (0.1199 €) | — | 2.17 | 0.042 (n=158) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.04<0.75) |
| 53390954 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.265345 WETH | 0.000060 WETH | 0.000000 WETH | 0.000002 WETH | 0.000058 WETH (0.1198 €) | — | 2.17 | 0.042 (n=158) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.04<0.75) |
| 53390786 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.013685 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0937 €) | — | 0.96 | 0.000 (n=18) | REJECTED | below_safety_margin(131<273), reliability_not_demonstrated |
| 53390786 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 1,064.663235 USDC | 0.108835 USDC | 0.000000 USDC | 0.007130 USDC | 0.101705 USDC (0.0936 €) | — | 0.96 | 0.000 (n=18) | REJECTED | below_safety_margin(101705<212932), reliability_not_demonstrated |
| 53390786 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.480798 WETH | 0.000048 WETH | 0.000000 WETH | 0.000003 WETH | 0.000045 WETH (0.0934 €) | — | 0.94 | 0.000 (n=18) | REJECTED | below_safety_margin(44960344685998<96159606306820), reliability_not_demonstrated |
| 53390954 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 467.009178 USDC | 0.084923 USDC | 0.000000 USDC | 0.005071 USDC | 0.079852 USDC (0.0735 €) | — | 1.71 | 0.007 (n=43) | REJECTED | below_safety_margin(79852<93401), p_lower_below_threshold(0.01<0.75) |
| 53390954 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.206972 WETH | 0.000038 WETH | 0.000000 WETH | 0.000002 WETH | 0.000035 WETH (0.0734 €) | — | 1.71 | 0.007 (n=43) | REJECTED | below_safety_margin(35341845922299<41394412411632), p_lower_below_threshold(0.01<0.75) |
| 53391158 | WETH→[uniswap_v3]→USDbC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.045267 WETH | 0.000037 WETH | 0.000000 WETH | 0.000003 WETH | 0.000033 WETH (0.0691 €) | — | 7.35 | 0.116 (n=529) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.12<0.75) |
| 53391159 | WETH→[uniswap_v3]→USDbC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.045267 WETH | 0.000037 WETH | 0.000000 WETH | 0.000003 WETH | 0.000033 WETH (0.0691 €) | — | 7.35 | 0.116 (n=529) | REJECTED | stale_data(4859ms>4000.0), simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.12<0.75) |
| 53391159 | WETH→[uniswap_v3]→USDbC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.045294 WETH | 0.000037 WETH | 0.000000 WETH | 0.000003 WETH | 0.000033 WETH (0.0690 €) | 0.000033 WETH | 7.34 | 0.118 (n=530) | REJECTED | stale_data(7410ms>4000.0), p_lower_below_threshold(0.12<0.75) |
| 53391159 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDbC→[aerodrome_slipstream]→USDC | 101.809977 USDC | 0.082212 USDC | 0.000000 USDC | 0.007458 USDC | 0.074754 USDC (0.0688 €) | — | 7.34 | 0.118 (n=530) | REJECTED | stale_data(7418ms>4000.0), p_lower_below_threshold(0.12<0.75) |
| 53391158 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDbC→[aerodrome_slipstream]→USDC | 101.809977 USDC | 0.082212 USDC | 0.000000 USDC | 0.007468 USDC | 0.074744 USDC (0.0688 €) | — | 7.34 | 0.116 (n=529) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 53391159 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDbC→[aerodrome_slipstream]→USDC | 101.809977 USDC | 0.082212 USDC | 0.000000 USDC | 0.007468 USDC | 0.074744 USDC (0.0688 €) | — | 7.34 | 0.116 (n=529) | REJECTED | stale_data(4868ms>4000.0), p_lower_below_threshold(0.12<0.75) |
| 53391158 | WETH→[pancakeswap_v3]→EURC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.074188 WETH | 0.000033 WETH | 0.000000 WETH | 0.000003 WETH | 0.000030 WETH (0.0632 €) | — | 4.10 | 0.116 (n=529) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.12<0.75) |
| 53391159 | WETH→[pancakeswap_v3]→EURC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.074188 WETH | 0.000033 WETH | 0.000000 WETH | 0.000003 WETH | 0.000030 WETH (0.0632 €) | — | 4.10 | 0.116 (n=529) | REJECTED | stale_data(5015ms>4000.0), simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.12<0.75) |
| 53391159 | WETH→[pancakeswap_v3]→EURC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.073958 WETH | 0.000033 WETH | 0.000000 WETH | 0.000003 WETH | 0.000030 WETH (0.0631 €) | 0.000030 WETH | 4.11 | 0.118 (n=530) | REJECTED | stale_data(7567ms>4000.0), p_lower_below_threshold(0.12<0.75) |
| 53391159 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→EURC→[aerodrome_slipstream]→USDC | 166.767496 USDC | 0.075167 USDC | 0.000000 USDC | 0.006774 USDC | 0.068393 USDC (0.0629 €) | — | 4.10 | 0.118 (n=530) | REJECTED | stale_data(7573ms>4000.0), p_lower_below_threshold(0.12<0.75) |
| 53391158 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→EURC→[aerodrome_slipstream]→USDC | 165.999845 USDC | 0.075166 USDC | 0.000000 USDC | 0.006782 USDC | 0.068384 USDC (0.0629 €) | — | 4.12 | 0.116 (n=529) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 53391159 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→EURC→[aerodrome_slipstream]→USDC | 165.999845 USDC | 0.075166 USDC | 0.000000 USDC | 0.006782 USDC | 0.068384 USDC (0.0629 €) | — | 4.12 | 0.116 (n=529) | REJECTED | stale_data(5022ms>4000.0), p_lower_below_threshold(0.12<0.75) |
| 53390877 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 838.715920 USDC | 0.070710 USDC | 0.000000 USDC | 0.006788 USDC | 0.063922 USDC (0.0588 €) | — | 0.76 | 0.136 (n=709) | REJECTED | below_safety_margin(63922<167743), p_lower_below_threshold(0.14<0.75) |
| 53390877 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.371303 WETH | 0.000031 WETH | 0.000000 WETH | 0.000003 WETH | 0.000028 WETH (0.0588 €) | — | 0.76 | 0.136 (n=709) | REJECTED | below_safety_margin(28290362649741<74260556055953), p_lower_below_threshold(0.14<0.75) |
| 53390877 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.009919 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0586 €) | — | 0.83 | 0.136 (n=709) | REJECTED | below_safety_margin(82<198), p_lower_below_threshold(0.14<0.75) |
| 53390586 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC | 92.916822 USDC | 0.060587 USDC | 0.000000 USDC | 0.006788 USDC | 0.053799 USDC (0.0495 €) | — | 5.79 | 0.117 (n=526) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 53390586 | WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.041203 WETH | 0.000027 WETH | 0.000000 WETH | 0.000003 WETH | 0.000024 WETH (0.0494 €) | — | 5.77 | 0.117 (n=526) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.12<0.75) |
| 53390586 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC | 94.739712 USDC | 0.060419 USDC | 0.000000 USDC | 0.006788 USDC | 0.053631 USDC (0.0493 €) | — | 5.66 | 0.117 (n=526) | REJECTED | p_lower_below_threshold(0.12<0.75) |

## Fiabilité et décision
- Observations ghost : 4204 ; taux observé 0.126 ; borne inférieure crédible (0.9) 0.120 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 12.0% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
