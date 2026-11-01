# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-01T23:37:49+00:00 ; durée 107.59 min ; blocs 53390229 → 53393458 (3185 vus)

## Connexion
- Requêtes RPC : 36998 ; erreurs : 0 ; latence p50/p95 : 269.1/972.7 ms
- Rafraîchissements d'état : 3186 ; âge des données au dernier bloc : 1.99 s ; changements de frais LP observés (pools à frais dynamiques) : 4455
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 33585 ; cycles déclenchés par événement : 4358 ; avance médiane sur le rafraîchissement multicall : 597 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,268.03 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 495 pools, 288 jetons, 18180 routes
- Par DEX : uniswap_v3 138, aerodrome_slipstream 111, aerodrome 203, pancakeswap_v3 29, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 176 (rejetés 2) → 581 jetons ; pools candidats 3720 (énumérés 312, par paires 0), mesurés 498, sous le plancher de 10000.0 $ : 3 → gardés 495 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDbC': 1.0, 'USDC': 1.0, 'WETH': 2258.829928, 'cbBTC': 77854.490121, 'AERO': 0.63182}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 150,794,114 | 2,268.030272 | 53393458 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,202,900 | 0.029044 | 53393458 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,418,408 | 0.000013 | 53393458 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,179,315 | 0.029037 | 53393458 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 7,905,861 | 2,268.615729 | 53393458 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,831,357 | 99.100644 | 53393458 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,661,756 | 0.001576 | 53393458 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 5,535,088 | 1.593065 | 53393458 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,173,911 | 0.029043 | 53393458 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,111,639 | 0.998852 | 53393458 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome_slipstream | WETH/USDC | 150 | 4,060,060 | 2,269.487460 | 53393458 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/USDC | 100 | 3,952,808 | 2,269.418081 | 53393458 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | WETH/KTA | 3000 | 3,550,351 | 38,192.875677 | 53393458 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,700,593 | 0.029043 | 53393458 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2703 | 2,383,277 | 99.141140 | 53393458 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | USDC/cbBTC | 484 | 2,131,962 | 0.000013 | 53393458 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome | WETH/FAI | 10000 | 2,095,115 | 1,188,094.920793 | 53393458 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | XDP/USDC | 100 | 1,759,724 | 0.018134 | 53393458 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,737,823 | 0.000000 | 53393458 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,630,420 | 0.000013 | 53393458 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,586,010 | 0.000013 | 53393458 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,555,589 | 428.085753 | 53393458 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v2 | WETH/USDC | 3000 | 1,508,295 | 2,267.355082 | 53393458 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,484,903 | 1.552316 | 53393458 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,456,622 | 0.825524 | 53393458 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,418,621 | 3,609.937944 | 53393458 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | WETH/USDC | 3000 | 1,382,011 | 2,271.614782 | 53393458 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,341,060 | 2,268.766638 | 53393458 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,335,687 | 0.005204 | 53393458 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,309,502 | 14,750.164539 | 53393458 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome_slipstream | USDC/cbBTC | 346 | 1,305,803 | 0.000013 | 53393458 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/SEND | 3000 | 1,169,000 | 71.107173 | 53393458 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,118,876 | 36,173,080.877578 | 53393458 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,067,406 | 520,202.621768 | 53393458 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,052,634 | 0.000000 | 53393458 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,012,477 | 22,413,230.182816 | 53393458 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | WETH/VVV | 10000 | 994,766 | 98.702569 | 53393458 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome_slipstream | USDC/VELVET | 100 | 991,053 | 19.446562 | 53393458 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | WETH/EDEL | 7000 | 982,107 | 81,411.222199 | 53393458 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | WETH/WELL | 10000 | 953,172 | 1,181,102.347708 | 53393458 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/MORPHO | 3000 | 929,851 | 1,008.858196 | 53393458 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/USDC | 10000 | 923,726 | 2,252.785696 | 53393458 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | USDC/VVV | 3000 | 917,508 | 0.043715 | 53393458 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | USDC/NOCK | 3000 | 906,327 | 76.212420 | 53393458 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome | WETH/AERO | 10000 | 864,635 | 3,584.477015 | 53393458 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | uXRP/WETH | 3000 | 864,608 | 0.000546 | 53393458 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 834,219 | 19.577284 | 53393458 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 820,155 | 0.060499 | 53393458 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 768,519 | 0.801881 | 53393458 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| aerodrome | VIRTUAL/WETH | 10000 | 729,044 | 0.000261 | 53393458 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 727,855 | 0.594698 | 53393458 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 718,466 | 4,709,818.711150 | 53393458 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v2 | WETH/NPC | 3000 | 689,666 | 136,476.638204 | 53393458 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 686,817 | 0.000008 | 53393458 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v3 | TIG/USDC | 10000 | 674,041 | 0.570211 | 53393458 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 660,999 | 523,274.447166 | 53393458 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome | WETH/msETH (stable) | 500 | 660,644 | 2.340198 | 53393458 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome | WETH/bsdETH | 100 | 608,928 | 0.915597 | 53393458 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 606,892 | 0.091720 | 53393458 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| uniswap_v3 | FLOCK/USDC | 3000 | 579,471 | 0.040255 | 53393458 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |

## Recherche d'opportunités
- Cycles : 7543 ; routes examinées : 137131740 ; candidats optimisés : 490599 ; net attendu > 0 : 1655 ; dernier cycle 199.7 ms
- Rejets (moteur) : {'spread_below_threshold': 134782618, 'liquidity_below_min': 1826351, 'negative_expected_net': 488944, 'unquotable': 23416, 'borrow_bound_too_small': 7543, 'cycle_budget_exhausted': 1213}
- Enregistrements de la session : 490599 ; net attendu > 0 : 1655 ; simulés (eth_call de la vraie tx) : 75 (ok 41, échec 34) ; étiquettes ghost N+1 : 11/40 positives
- Décisions : {'REJECTED': 490599} ; motifs de rejet : {'below_safety_margin': 1322, 'negative_expected_net': 488944, 'p_lower_below_threshold': 1578, 'reliability_not_demonstrated': 77, 'sim_below_estimate': 12, 'simulated_net_nonpositive': 4, 'simulation_failed': 34, 'stale_data': 162}

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
| 53392875 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.219925 WETH | 0.000033 WETH | 0.000000 WETH | 0.000003 WETH | 0.000029 WETH (0.0614 €) | — | 1.34 | 0.135 (n=719) | REJECTED | below_safety_margin(29433390868230<43985007216153), p_lower_below_threshold(0.14<0.75) |
| 53392875 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 471.203152 USDC | 0.073796 USDC | 0.000000 USDC | 0.007160 USDC | 0.066636 USDC (0.0613 €) | — | 1.41 | 0.135 (n=719) | REJECTED | below_safety_margin(66636<94240), p_lower_below_threshold(0.14<0.75) |
| 53392875 | cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.006040 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0610 €) | — | 1.41 | 0.135 (n=719) | REJECTED | below_safety_margin(85<120), p_lower_below_threshold(0.14<0.75) |
| 53390877 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 838.715920 USDC | 0.070710 USDC | 0.000000 USDC | 0.006788 USDC | 0.063922 USDC (0.0588 €) | — | 0.76 | 0.136 (n=709) | REJECTED | below_safety_margin(63922<167743), p_lower_below_threshold(0.14<0.75) |
| 53390877 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.371303 WETH | 0.000031 WETH | 0.000000 WETH | 0.000003 WETH | 0.000028 WETH (0.0588 €) | — | 0.76 | 0.136 (n=709) | REJECTED | below_safety_margin(28290362649741<74260556055953), p_lower_below_threshold(0.14<0.75) |
| 53390877 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.009919 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0586 €) | — | 0.83 | 0.136 (n=709) | REJECTED | below_safety_margin(82<198), p_lower_below_threshold(0.14<0.75) |

## Fiabilité et décision
- Observations ghost : 4228 ; taux observé 0.127 ; borne inférieure crédible (0.9) 0.121 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 12.1% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ✅ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
