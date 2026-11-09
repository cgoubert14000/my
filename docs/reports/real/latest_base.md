# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-09T07:54:58+00:00 ; durée 213.71 min ; blocs 55038467 → 55102540 (7496 vus)

## Connexion
- Requêtes RPC : 109485 ; erreurs : 10 ; latence p50/p95 : 561.7/2,306.6 ms
- Rafraîchissements d'état : 7496 ; âge des données au dernier bloc : 9.5 s ; changements de frais LP observés (pools à frais dynamiques) : 6821
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 7838 ; cycles déclenchés par événement : 2438 ; avance médiane sur le rafraîchissement multicall : 755 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,088.53 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 467 pools, 272 jetons, 17562 routes
- Par DEX : uniswap_v3 134, aerodrome_slipstream 97, aerodrome 194, pancakeswap_v3 28, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 166 (rejetés 2) → 571 jetons ; pools candidats 3664 (énumérés 288, par paires 0), mesurés 469, sous le plancher de 10000.0 $ : 2 → gardés 467 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'DAI': 1.0, 'USDC': 1.0, 'WETH': 2141.212816, 'cbBTC': 74926.035696, 'AERO': 0.58265}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 137,211,849 | 2,088.531903 | 55102578 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,173,724 | 0.028289 | 55102578 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 8,767,442 | 0.000014 | 55102578 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 8,640,407 | 0.028282 | 55102578 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 7,339,191 | 2,089.933704 | 55102578 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,002,745 | 103.857744 | 55102578 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,176,065 | 0.001515 | 55102578 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 4,529,224 | 1.794211 | 55102578 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,501,997 | 0.028295 | 55102578 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,888,518 | 0.998733 | 55102578 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| pancakeswap_v3 | WETH/USDC | 100 | 3,775,553 | 2,090.228145 | 55102578 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | WETH/KTA | 3000 | 3,103,199 | 42,391.439105 | 55102578 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 150 | 2,964,013 | 2,090.315856 | 55102578 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,321,732 | 0.028284 | 55102578 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 1,963,374 | 1,147,023.460568 | 55102578 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 412 | 1,694,475 | 0.000014 | 55102578 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,592,929 | 0.006788 | 55102578 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,586,637 | 0.000014 | 55102578 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | XDP/USDC | 100 | 1,558,616 | 0.015414 | 55102578 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,533,988 | 0.000000 | 55102578 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,474,099 | 1.421539 | 55102578 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,452,662 | 0.824262 | 55102578 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,435,873 | 0.000014 | 55102578 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,429,362 | 433.884114 | 55102578 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | WETH/AERO | 3000 | 1,289,679 | 3,748.346769 | 55102578 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v2 | WETH/USDC | 3000 | 1,281,141 | 2,089.382277 | 55102578 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,219,095 | 15,318.374494 | 55102578 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/USDC | 3000 | 1,211,282 | 2,089.837809 | 55102578 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome | USDC/SEND | 3000 | 1,120,771 | 77.357958 | 55102578 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,070,759 | 2,090.151567 | 55102578 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | WETH/doginme | 10000 | 1,027,101 | 36,865,069.416824 | 55102578 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/VVV | 10000 | 998,364 | 104.273129 | 55102578 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome_slipstream | USDC/VELVET | 100 | 944,904 | 22.470444 | 55102578 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/BRETT | 10000 | 940,031 | 588,980.116488 | 55102578 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | WETH/TOSHI | 10000 | 917,490 | 23,089,915.590840 | 55102578 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/cbBTC | 330 | 916,679 | 0.000014 | 55102578 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/NOCK | 3000 | 909,581 | 75.746024 | 55102578 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/USDC | 10000 | 904,696 | 2,070.021302 | 55102578 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 889,284 | 1,039.127009 | 55102578 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | DRB/WETH | 10000 | 889,218 | 0.000000 | 55102578 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | USDC/VVV | 3000 | 832,497 | 0.049801 | 55102578 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | WETH/EDEL | 7000 | 806,941 | 102,127.089302 | 55102578 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| pancakeswap_v3 | QUID/USDC | 100 | 764,753 | 0.052180 | 55102578 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 741,494 | 23.251129 | 55102578 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome | WETH/AERO | 10000 | 730,164 | 3,718.313541 | 55102578 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | WETH/wstETH | 3000 | 706,926 | 0.803323 | 55102578 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 686,449 | 0.524789 | 55102578 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 641,781 | 5,012,799.261240 | 55102578 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 641,730 | 0.521652 | 55102578 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/NPC | 3000 | 610,745 | 147,927.519465 | 55102578 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 609,601 | 0.000008 | 55102578 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | VIRTUAL/WETH | 10000 | 581,955 | 0.000251 | 55102578 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/BRETT | 2144 | 571,241 | 592,478.831461 | 55102578 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | FLOCK/USDC | 3000 | 556,412 | 0.037392 | 55102578 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome | WETH/msETH (stable) | 500 | 524,171 | 2.380553 | 55102578 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 504,579 | 1,038.803841 | 55102578 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome | cbBTC/EDGE | 7000 | 497,732 | 932,578.776828 | 55102578 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| uniswap_v3 | USDC/USDT | 100 | 497,707 | 1.001254 | 55102578 | `0xD56da2B74bA826f19015E6B7Dd9Dae1903E85DA1` |
| pancakeswap_v3 | ELSA/USDC | 100 | 478,085 | 0.069118 | 55102578 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| uniswap_v3 | WETH/USDC | 100 | 477,575 | 2,090.553043 | 55102578 | `0xb4CB800910B228ED3d0834cF79D697127BBB00e5` |

## Recherche d'opportunités
- Cycles : 9933 ; routes examinées : 174443346 ; candidats optimisés : 623495 ; net attendu > 0 : 1328 ; dernier cycle 404.4 ms
- Rejets (moteur) : {'spread_below_threshold': 171293913, 'liquidity_below_min': 2512877, 'negative_expected_net': 622167, 'borrow_bound_too_small': 11277, 'cycle_budget_exhausted': 1782, 'unquotable': 2}
- Enregistrements de la session : 623495 ; net attendu > 0 : 1328 ; simulés (eth_call de la vraie tx) : 76 (ok 63, échec 13) ; étiquettes ghost N+1 : 24/71 positives
- Décisions : {'REJECTED': 623495} ; motifs de rejet : {'below_safety_margin': 1144, 'negative_expected_net': 622167, 'p_lower_below_threshold': 1256, 'price_impact': 1, 'reliability_not_demonstrated': 72, 'simulation_failed': 13, 'stale_data': 316}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 55086133 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 1,037.319445 USDC | 0.163176 USDC | 0.000000 USDC | 0.004754 USDC | 0.158422 USDC (0.1457 €) | — | 1.53 | 0.059 (n=299) | REJECTED | below_safety_margin(158422<207463), p_lower_below_threshold(0.06<0.75) |
| 55086133 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.492571 WETH | 0.000077 WETH | 0.000000 WETH | 0.000002 WETH | 0.000075 WETH (0.1456 €) | — | 1.52 | 0.059 (n=299) | REJECTED | below_safety_margin(75025572299617<98514181116913), p_lower_below_threshold(0.06<0.75) |
| 55086134 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 954.319656 USDC | 0.138115 USDC | 0.000000 USDC | 0.004755 USDC | 0.133360 USDC (0.1227 €) | — | 1.40 | 0.059 (n=299) | REJECTED | below_safety_margin(133360<190863), p_lower_below_threshold(0.06<0.75) |
| 55086134 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.452882 WETH | 0.000065 WETH | 0.000000 WETH | 0.000002 WETH | 0.000063 WETH (0.1225 €) | — | 1.39 | 0.059 (n=299) | REJECTED | below_safety_margin(63154959045858<90576387333474), p_lower_below_threshold(0.06<0.75) |
| 55097311 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 494.995900 USDC | 0.122524 USDC | 0.000000 USDC | 0.006295 USDC | 0.116229 USDC (0.1069 €) | 0.116229 USDC | 2.35 | 0.204 (n=1222) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 55097311 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.236674 WETH | 0.000059 WETH | 0.000000 WETH | 0.000003 WETH | 0.000056 WETH (0.1068 €) | 0.000056 WETH | 2.35 | 0.204 (n=1222) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 55097311 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.006640 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1067 €) | 0.000002 cbBTC | 2.36 | 0.204 (n=1222) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 55045434 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.355434 WETH | 0.000047 WETH | 0.000000 WETH | 0.000003 WETH | 0.000044 WETH (0.0857 €) | — | 1.22 | 0.048 (n=30) | REJECTED | below_safety_margin(43516011434452<71086872293656), p_lower_below_threshold(0.05<0.75) |
| 55045434 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.355434 WETH | 0.000047 WETH | 0.000000 WETH | 0.000003 WETH | 0.000044 WETH (0.0857 €) | — | 1.22 | 0.048 (n=30) | REJECTED | below_safety_margin(43516011434452<71086872293656), p_lower_below_threshold(0.05<0.75) |
| 55045434 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 732.198649 USDC | 0.099587 USDC | 0.000000 USDC | 0.006433 USDC | 0.093154 USDC (0.0857 €) | — | 1.27 | 0.048 (n=30) | REJECTED | below_safety_margin(93154<146439), p_lower_below_threshold(0.05<0.75) |
| 55045434 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 732.198649 USDC | 0.099587 USDC | 0.000000 USDC | 0.006433 USDC | 0.093154 USDC (0.0857 €) | — | 1.27 | 0.048 (n=30) | REJECTED | below_safety_margin(93154<146439), p_lower_below_threshold(0.05<0.75) |
| 55045434 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.009259 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0855 €) | — | 1.34 | 0.048 (n=30) | REJECTED | below_safety_margin(124<185), p_lower_below_threshold(0.05<0.75) |
| 55045434 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.009259 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0855 €) | — | 1.34 | 0.048 (n=30) | REJECTED | below_safety_margin(124<185), p_lower_below_threshold(0.05<0.75) |
| 55073953 | USDC→[pancakeswap_v3]→ICNT→[uniswap_v3]→USDC | 88.285333 USDC | 0.083463 USDC | 0.000000 USDC | 0.004818 USDC | 0.078645 USDC (0.0724 €) | — | 8.91 | 0.007 (n=109) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.01<0.75) |
| 55045434 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.006493 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0690 €) | — | 1.54 | 0.204 (n=1207) | REJECTED | below_safety_margin(100<129), p_lower_below_threshold(0.20<0.75) |
| 55045434 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.006493 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0690 €) | — | 1.54 | 0.204 (n=1207) | REJECTED | below_safety_margin(100<129), p_lower_below_threshold(0.20<0.75) |
| 55045434 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 501.136491 USDC | 0.080969 USDC | 0.000000 USDC | 0.006433 USDC | 0.074536 USDC (0.0686 €) | — | 1.49 | 0.204 (n=1207) | REJECTED | below_safety_margin(74536<100227), p_lower_below_threshold(0.20<0.75) |
| 55045434 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 501.136491 USDC | 0.080969 USDC | 0.000000 USDC | 0.006433 USDC | 0.074536 USDC (0.0686 €) | — | 1.49 | 0.204 (n=1207) | REJECTED | below_safety_margin(74536<100227), p_lower_below_threshold(0.20<0.75) |
| 55045434 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.226863 WETH | 0.000038 WETH | 0.000000 WETH | 0.000003 WETH | 0.000035 WETH (0.0684 €) | — | 1.53 | 0.204 (n=1207) | REJECTED | below_safety_margin(34746748358204<45372651029136), p_lower_below_threshold(0.20<0.75) |
| 55045434 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.226863 WETH | 0.000038 WETH | 0.000000 WETH | 0.000003 WETH | 0.000035 WETH (0.0684 €) | — | 1.53 | 0.204 (n=1207) | REJECTED | below_safety_margin(34746748358204<45372651029136), p_lower_below_threshold(0.20<0.75) |
| 55097311 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.003593 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0469 €) | — | 1.92 | 0.204 (n=1222) | REJECTED | below_safety_margin(69<71), p_lower_below_threshold(0.20<0.75) |
| 55097311 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 257.384523 USDC | 0.057050 USDC | 0.000000 USDC | 0.006295 USDC | 0.050755 USDC (0.0467 €) | — | 1.97 | 0.204 (n=1222) | REJECTED | below_safety_margin(50755<51476), p_lower_below_threshold(0.20<0.75) |
| 55097311 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.135532 WETH | 0.000027 WETH | 0.000000 WETH | 0.000003 WETH | 0.000024 WETH (0.0463 €) | — | 1.78 | 0.204 (n=1222) | REJECTED | below_safety_margin(24098941314749<27106378126960), p_lower_below_threshold(0.20<0.75) |
| 55072334 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.135415 WETH | 0.000024 WETH | 0.000000 WETH | 0.000003 WETH | 0.000021 WETH (0.0408 €) | — | 1.54 | 0.203 (n=1210) | REJECTED | below_safety_margin(20787072282793<27082935218889), p_lower_below_threshold(0.20<0.75) |
| 55072334 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.135415 WETH | 0.000024 WETH | 0.000000 WETH | 0.000003 WETH | 0.000021 WETH (0.0408 €) | — | 1.54 | 0.203 (n=1210) | REJECTED | below_safety_margin(20787072282793<27082935218889), p_lower_below_threshold(0.20<0.75) |

## Fiabilité et décision
- Observations ghost : 6721 ; taux observé 0.177 ; borne inférieure crédible (0.9) 0.171 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 17.1% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ✅ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
