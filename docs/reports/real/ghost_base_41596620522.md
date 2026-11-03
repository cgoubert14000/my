# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-03T11:49:14+00:00 ; durée 254.15 min ; blocs 53450975 → 53458599 (6516 vus)

## Connexion
- Requêtes RPC : 76707 ; erreurs : 0 ; latence p50/p95 : 222.6/1,441.9 ms
- Rafraîchissements d'état : 6517 ; âge des données au dernier bloc : 4.84 s ; changements de frais LP observés (pools à frais dynamiques) : 7566
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 12505 ; cycles déclenchés par événement : 1807 ; avance médiane sur le rafraîchissement multicall : 1,218 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,265.22 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 491 pools, 284 jetons, 18380 routes
- Par DEX : uniswap_v3 137, aerodrome_slipstream 107, aerodrome 202, pancakeswap_v3 30, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 174 (rejetés 2) → 579 jetons ; pools candidats 3753 (énumérés 307, par paires 0), mesurés 494, sous le plancher de 10000.0 $ : 3 → gardés 491 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDC': 1.0, 'USDbC': 1.0, 'WETH': 2251.332101, 'cbBTC': 76780.974774, 'AERO': 0.596875}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 150,558,388 | 2,265.216943 | 53458599 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,241,174 | 0.029394 | 53458599 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,102,940 | 0.029405 | 53458599 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 8,978,567 | 0.000013 | 53458599 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 7,884,331 | 2,264.855928 | 53458599 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,582,734 | 105.287966 | 53458599 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,562,198 | 0.001570 | 53458599 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 5,306,472 | 1.654769 | 53458599 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,814,900 | 0.029407 | 53458599 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,152,005 | 2,265.764479 | 53458599 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,055,005 | 0.999818 | 53458599 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome_slipstream | WETH/USDC | 150 | 3,885,393 | 2,265.506742 | 53458599 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome | WETH/KTA | 3000 | 3,483,937 | 39,563.522952 | 53458599 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,691,064 | 0.029415 | 53458599 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 2,150,111 | 1,125,297.120203 | 53458599 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | WETH/VVV | 2766 | 2,054,041 | 105.284295 | 53458599 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | USDC/cbBTC | 448 | 1,806,411 | 0.000013 | 53458599 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | XDP/USDC | 100 | 1,746,487 | 0.017945 | 53458599 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,666,158 | 0.000000 | 53458599 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,632,756 | 0.000013 | 53458599 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,555,081 | 1.434999 | 53458599 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,544,745 | 0.000013 | 53458599 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,539,422 | 441.779483 | 53458599 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v2 | WETH/USDC | 3000 | 1,500,890 | 2,265.067829 | 53458599 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,453,152 | 0.821322 | 53458599 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,389,066 | 3,741.759115 | 53458599 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | WETH/USDC | 3000 | 1,337,270 | 2,268.207063 | 53458599 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,325,917 | 2,264.872952 | 53458599 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,321,040 | 0.005115 | 53458599 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,281,594 | 15,056.661486 | 53458599 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome_slipstream | USDC/cbBTC | 338 | 1,231,654 | 0.000013 | 53458599 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/SEND | 3000 | 1,164,536 | 71.652959 | 53458599 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,113,481 | 36,944,930.739561 | 53458599 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,050,343 | 542,613.916744 | 53458599 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,018,129 | 0.000000 | 53458599 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,010,742 | 22,467,355.786717 | 53458599 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/VELVET | 100 | 988,265 | 19.607458 | 53458599 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | WETH/EDEL | 7000 | 953,550 | 86,089.751150 | 53458599 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/USDC | 10000 | 925,850 | 2,257.234778 | 53458599 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome | WETH/WELL | 10000 | 922,225 | 1,258,573.163211 | 53458599 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/MORPHO | 3000 | 920,835 | 1,070.193283 | 53458599 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/VVV | 10000 | 919,213 | 106.039343 | 53458599 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome | USDC/NOCK | 3000 | 893,674 | 78.386217 | 53458599 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | uXRP/WETH | 3000 | 869,245 | 0.000551 | 53458599 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| uniswap_v3 | USDC/VVV | 3000 | 858,349 | 0.046467 | 53458599 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | WETH/AERO | 10000 | 827,668 | 3,748.167774 | 53458599 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | USDC/SAPIEN | 4610 | 814,279 | 20.308704 | 53458599 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 790,386 | 0.055929 | 53458599 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 768,883 | 0.799125 | 53458599 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 724,063 | 0.583508 | 53458599 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| aerodrome | VIRTUAL/WETH | 10000 | 719,193 | 0.000257 | 53458599 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 711,874 | 4,788,030.790473 | 53458599 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v2 | WETH/NPC | 3000 | 662,452 | 147,610.409098 | 53458599 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome | WETH/msETH (stable) | 500 | 656,556 | 2.337947 | 53458599 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | TIG/USDC | 10000 | 655,408 | 0.540485 | 53458599 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 654,768 | 0.000008 | 53458599 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/BRETT | 2102 | 645,819 | 540,623.868769 | 53458599 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome | WETH/bsdETH | 100 | 608,499 | 0.914615 | 53458599 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 589,853 | 0.087772 | 53458599 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| uniswap_v3 | FLOCK/USDC | 3000 | 583,422 | 0.040588 | 53458599 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |

## Recherche d'opportunités
- Cycles : 8323 ; routes examinées : 152976740 ; candidats optimisés : 565457 ; net attendu > 0 : 159 ; dernier cycle 313.2 ms
- Rejets (moteur) : {'spread_below_threshold': 150090329, 'liquidity_below_min': 2272435, 'negative_expected_net': 565298, 'unquotable': 39086, 'borrow_bound_too_small': 8307, 'cycle_budget_exhausted': 1086}
- Enregistrements de la session : 565454 ; net attendu > 0 : 159 ; simulés (eth_call de la vraie tx) : 20 (ok 12, échec 8) ; étiquettes ghost N+1 : 3/17 positives
- Décisions : {'REJECTED': 565454} ; motifs de rejet : {'below_safety_margin': 95, 'negative_expected_net': 565295, 'p_lower_below_threshold': 148, 'reliability_not_demonstrated': 11, 'simulation_failed': 8}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53452260 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→AAVE→[uniswap_v3]→USDC | 464.024973 USDC | 1.037007 USDC | 0.000000 USDC | 0.006767 USDC | 1.030240 USDC (0.9478 €) | — | 22.20 | 0.000 (n=48) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53452260 | WETH→[uniswap_v3]→AAVE→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.205746 WETH | 0.000459 WETH | 0.000000 WETH | 0.000003 WETH | 0.000456 WETH (0.9457 €) | — | 22.18 | 0.000 (n=48) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 53452260 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→AAVE→[uniswap_v3]→USDC | 464.198632 USDC | 1.034434 USDC | 0.000000 USDC | 0.006767 USDC | 1.027667 USDC (0.9455 €) | — | 22.14 | 0.000 (n=34) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53452260 | WETH→[uniswap_v3]→AAVE→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.205647 WETH | 0.000458 WETH | 0.000000 WETH | 0.000003 WETH | 0.000455 WETH (0.9433 €) | — | 22.14 | 0.000 (n=34) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 53452260 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→AAVE→[uniswap_v3]→USDC | 437.297961 USDC | 0.916744 USDC | 0.000000 USDC | 0.006767 USDC | 0.909977 USDC (0.8372 €) | — | 20.81 | 0.000 (n=48) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53452260 | WETH→[uniswap_v3]→AAVE→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.193724 WETH | 0.000406 WETH | 0.000000 WETH | 0.000003 WETH | 0.000403 WETH (0.8351 €) | — | 20.80 | 0.000 (n=48) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 53452260 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→AAVE→[uniswap_v3]→USDC | 424.663486 USDC | 0.877988 USDC | 0.000000 USDC | 0.006767 USDC | 0.871221 USDC (0.8015 €) | — | 20.52 | 0.000 (n=34) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53452260 | WETH→[uniswap_v3]→AAVE→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.188122 WETH | 0.000389 WETH | 0.000000 WETH | 0.000003 WETH | 0.000386 WETH (0.7994 €) | — | 20.51 | 0.000 (n=34) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53452260 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→AAVE→[uniswap_v3]→USDC | 402.839523 USDC | 0.827841 USDC | 0.000000 USDC | 0.006767 USDC | 0.821074 USDC (0.7554 €) | — | 20.38 | 0.000 (n=48) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53452260 | WETH→[uniswap_v3]→AAVE→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.178425 WETH | 0.000367 WETH | 0.000000 WETH | 0.000003 WETH | 0.000364 WETH (0.7532 €) | — | 20.37 | 0.000 (n=48) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53452260 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→AAVE→[uniswap_v3]→USDC | 387.140238 USDC | 0.714619 USDC | 0.000000 USDC | 0.006767 USDC | 0.707852 USDC (0.6512 €) | — | 18.28 | 0.030 (n=93) | REJECTED | p_lower_below_threshold(0.03<0.75) |
| 53452260 | WETH→[uniswap_v3]→AAVE→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.171498 WETH | 0.000316 WETH | 0.000000 WETH | 0.000003 WETH | 0.000313 WETH (0.6493 €) | — | 18.27 | 0.030 (n=93) | REJECTED | p_lower_below_threshold(0.03<0.75) |
| 53452260 | USDC→[sushiswap_v3]→WETH→[uniswap_v3]→AAVE→[uniswap_v3]→USDC | 309.065048 USDC | 0.621923 USDC | 0.000000 USDC | 0.006767 USDC | 0.615156 USDC (0.5659 €) | — | 19.90 | 0.030 (n=93) | REJECTED | p_lower_below_threshold(0.03<0.75) |
| 53452260 | WETH→[uniswap_v3]→AAVE→[uniswap_v3]→USDC→[sushiswap_v3]→WETH | 0.136769 WETH | 0.000275 WETH | 0.000000 WETH | 0.000003 WETH | 0.000272 WETH (0.5638 €) | — | 19.89 | 0.030 (n=93) | REJECTED | p_lower_below_threshold(0.03<0.75) |
| 53452260 | USDC→[uniswap_v2]→WETH→[uniswap_v3]→AAVE→[uniswap_v3]→USDC | 315.841474 USDC | 0.608997 USDC | 0.000000 USDC | 0.006068 USDC | 0.602929 USDC (0.5547 €) | — | 19.09 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 53452260 | WETH→[uniswap_v3]→AAVE→[uniswap_v3]→USDC→[uniswap_v2]→WETH | 0.139933 WETH | 0.000269 WETH | 0.000000 WETH | 0.000003 WETH | 0.000267 WETH (0.5526 €) | — | 19.06 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 53452260 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→AAVE→[uniswap_v3]→USDC | 230.758965 USDC | 0.538585 USDC | 0.000000 USDC | 0.006767 USDC | 0.531818 USDC (0.4893 €) | — | 23.05 | 0.000 (n=48) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53452260 | WETH→[uniswap_v3]→AAVE→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.102201 WETH | 0.000238 WETH | 0.000000 WETH | 0.000003 WETH | 0.000235 WETH (0.4871 €) | — | 23.00 | 0.000 (n=48) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53452260 | USDC→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→AAVE→[uniswap_v3]→USDC | 242.766664 USDC | 0.395214 USDC | 0.000000 USDC | 0.006767 USDC | 0.388447 USDC (0.3574 €) | — | 16.00 | 0.030 (n=93) | REJECTED | p_lower_below_threshold(0.03<0.75) |
| 53452260 | WETH→[aerodrome_slipstream]→AAVE→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.107570 WETH | 0.000175 WETH | 0.000000 WETH | 0.000003 WETH | 0.000172 WETH (0.3566 €) | — | 16.00 | 0.030 (n=93) | REJECTED | p_lower_below_threshold(0.03<0.75) |
| 53452260 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→AAVE→[uniswap_v3]→USDC | 242.225114 USDC | 0.393235 USDC | 0.000000 USDC | 0.006767 USDC | 0.386468 USDC (0.3556 €) | — | 15.95 | 0.097 (n=112) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53452260 | WETH→[aerodrome_slipstream]→AAVE→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.107487 WETH | 0.000174 WETH | 0.000000 WETH | 0.000003 WETH | 0.000171 WETH (0.3547 €) | — | 15.93 | 0.097 (n=112) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53452260 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→AAVE→[uniswap_v3]→USDC | 222.699437 USDC | 0.331993 USDC | 0.000000 USDC | 0.006767 USDC | 0.325226 USDC (0.2992 €) | — | 14.60 | 0.030 (n=93) | REJECTED | p_lower_below_threshold(0.03<0.75) |
| 53452260 | WETH→[aerodrome_slipstream]→AAVE→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.098681 WETH | 0.000147 WETH | 0.000000 WETH | 0.000003 WETH | 0.000144 WETH (0.2984 €) | — | 14.60 | 0.030 (n=93) | REJECTED | p_lower_below_threshold(0.03<0.75) |
| 53452260 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→AAVE→[uniswap_v3]→USDC | 216.049970 USDC | 0.315991 USDC | 0.000000 USDC | 0.006767 USDC | 0.309224 USDC (0.2845 €) | — | 14.31 | 0.097 (n=112) | REJECTED | p_lower_below_threshold(0.10<0.75) |

## Fiabilité et décision
- Observations ghost : 4816 ; taux observé 0.170 ; borne inférieure crédible (0.9) 0.163 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 16.3% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
