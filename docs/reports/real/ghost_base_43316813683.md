# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-12T23:47:33+00:00 ; durée 95.51 min ; blocs 56655713 → 56684349 (6119 vus)

## Connexion
- Requêtes RPC : 77401 ; erreurs : 13 ; latence p50/p95 : 219.2/849.6 ms
- Rafraîchissements d'état : 6119 ; âge des données au dernier bloc : 5.2 s ; changements de frais LP observés (pools à frais dynamiques) : 2279
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 7480 ; cycles déclenchés par événement : 2937 ; avance médiane sur le rafraîchissement multicall : 444 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,013.08 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 457 pools, 266 jetons, 14822 routes
- Par DEX : uniswap_v3 133, aerodrome_slipstream 97, aerodrome 187, pancakeswap_v3 27, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 1
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 159 (rejetés 2) → 564 jetons ; pools candidats 3621 (énumérés 282, par paires 0), mesurés 459, sous le plancher de 10000.0 $ : 2 → gardés 457 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'DAI': 1.0, 'USDC': 1.0, 'WETH': 2015.232847, 'cbBTC': 71439.030081, 'AERO': 0.524681}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 132,606,429 | 2,013.076723 | 56684349 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,324,237 | 0.028289 | 56684349 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 8,513,788 | 0.028218 | 56684349 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 8,123,436 | 0.000014 | 56684349 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 6,846,002 | 2,016.066480 | 56684349 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 6,665,379 | 106.277233 | 56684349 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,198,615 | 0.028283 | 56684349 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 4,122,477 | 1.924834 | 56684349 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,108,471 | 2,015.795071 | 56684349 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,748,150 | 0.998724 | 56684349 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 2,984,080 | 42,589.669652 | 56684349 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 154 | 2,803,387 | 2,016.032570 | 56684349 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,151,605 | 0.028230 | 56684349 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 1,879,394 | 1,163,003.281972 | 56684349 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | XDP/USDC | 100 | 1,637,686 | 0.016629 | 56684349 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | USDC/cbBTC | 508 | 1,595,530 | 0.000014 | 56684349 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,563,160 | 0.000014 | 56684349 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,503,079 | 0.000000 | 56684349 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,490,712 | 0.006583 | 56684349 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,466,845 | 0.000014 | 56684349 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,464,710 | 0.831859 | 56684349 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,382,708 | 425.220709 | 56684349 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v2 | WETH/USDC | 3000 | 1,258,242 | 2,014.076409 | 56684349 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| uniswap_v3 | WETH/AERO | 3000 | 1,219,493 | 3,876.562199 | 56684349 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,186,555 | 15,052.991792 | 56684349 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/USDC | 3000 | 1,143,505 | 2,018.861222 | 56684350 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,098,943 | 2,015.925709 | 56684349 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,060,920 | 86.332345 | 56684349 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,037,340 | 1.402298 | 56684349 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | WETH/doginme | 10000 | 1,003,992 | 35,458,223.889743 | 56684349 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/VVV | 10000 | 982,708 | 106.184698 | 56684349 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome_slipstream | USDC/VELVET | 100 | 980,772 | 20.054440 | 56684349 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/BRETT | 10000 | 921,871 | 559,037.877897 | 56684349 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 888,234 | 0.001501 | 56684349 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| uniswap_v3 | WETH/TOSHI | 10000 | 882,414 | 23,226,178.240886 | 56684349 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | WETH/MORPHO | 3000 | 873,064 | 996.543635 | 56684349 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | USDC/VVV | 3000 | 872,958 | 0.052832 | 56684349 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/USDC | 10000 | 869,132 | 2,005.198605 | 56684349 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome_slipstream | USDC/cbBTC | 356 | 863,934 | 0.000014 | 56684349 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | DRB/WETH | 10000 | 803,801 | 0.000000 | 56684349 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | USDC/NOCK | 3000 | 776,461 | 78.017767 | 56684349 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| pancakeswap_v3 | QUID/USDC | 100 | 747,990 | 0.049850 | 56684349 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 746,461 | 23.067643 | 56684349 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome | WETH/AERO | 10000 | 684,502 | 3,864.686083 | 56684349 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | WETH/wstETH | 3000 | 682,033 | 0.801801 | 56684349 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 662,906 | 0.526697 | 56684349 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 628,029 | 4,872,555.958281 | 56684349 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 603,464 | 0.458612 | 56684349 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/NPC | 3000 | 580,999 | 152,209.968936 | 56684349 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome | VIRTUAL/WETH | 10000 | 567,029 | 0.000260 | 56684349 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 566,162 | 555,076.109264 | 56684349 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | FLOCK/USDC | 3000 | 562,512 | 0.038191 | 56684349 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome_slipstream | AERO/cbBTC | 1025 | 553,129 | 0.000007 | 56684349 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/MORPHO | 2703 | 486,503 | 996.307395 | 56684349 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| pancakeswap_v3 | ELSA/USDC | 100 | 458,688 | 0.065805 | 56684349 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| uniswap_v3 | USDC/MORPHO | 10000 | 450,771 | 0.496582 | 56684349 | `0x2043B296fFC6b2d3bf4A3F3167d2Afb3B0FBdbEE` |
| aerodrome_slipstream | USDC/USDT | 8 | 449,546 | 1.000997 | 56684349 | `0xa41Bc0AFfbA7Fd420d186b84899d7ab2aC57fcD1` |
| uniswap_v3 | WETH/UNI | 10000 | 435,167 | 333.133817 | 56684349 | `0xAb365f161Dd501473a1ff0D2ef0dCE94E7398839` |
| uniswap_v3 | WETH/uSOL | 3000 | 429,304 | 24.862308 | 56684349 | `0xab04A352D4EC8d0F1812A4E5EBe7807Fa67acD48` |
| aerodrome | cbBTC/EDGE | 7000 | 423,148 | 914,999.414728 | 56684349 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |

## Recherche d'opportunités
- Cycles : 9055 ; routes examinées : 134213210 ; candidats optimisés : 637441 ; net attendu > 0 : 559 ; dernier cycle 97.3 ms
- Rejets (moteur) : {'spread_below_threshold': 131320168, 'liquidity_below_min': 2252296, 'negative_expected_net': 636882, 'borrow_bound_too_small': 1975, 'pool_quarantined': 588, 'cycle_budget_exhausted': 419, 'unquotable': 242}
- Enregistrements de la session : 637441 ; net attendu > 0 : 559 ; simulés (eth_call de la vraie tx) : 38 (ok 24, échec 14) ; étiquettes ghost N+1 : 19/30 positives
- Décisions : {'REJECTED': 637441} ; motifs de rejet : {'below_safety_margin': 463, 'negative_expected_net': 636882, 'p_lower_below_threshold': 551, 'reliability_not_demonstrated': 8, 'sim_below_estimate': 17, 'simulated_net_nonpositive': 10, 'simulation_failed': 14}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 56677148 | cbBTC→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.030308 cbBTC | 0.000005 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000005 cbBTC (0.3542 €) | — | 1.78 | 0.270 (n=1623) | REJECTED | below_safety_margin(540<606), p_lower_below_threshold(0.27<0.75) |
| 56677148 | WETH→[pancakeswap_v3]→cbBTC→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 1.097479 WETH | 0.000195 WETH | 0.000000 WETH | 0.000003 WETH | 0.000191 WETH (0.3541 €) | — | 1.74 | 0.270 (n=1623) | REJECTED | below_safety_margin(191188791380326<219495888234063), p_lower_below_threshold(0.27<0.75) |
| 56677148 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[uniswap_v3]→USDC | 2,198.589497 USDC | 0.391142 USDC | 0.000000 USDC | 0.006683 USDC | 0.384459 USDC (0.3537 €) | — | 1.75 | 0.270 (n=1623) | REJECTED | below_safety_margin(384459<439717), p_lower_below_threshold(0.27<0.75) |
| 56677148 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.015874 cbBTC | 0.000003 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000003 cbBTC (0.1987 €) | — | 1.91 | 0.160 (n=43) | REJECTED | below_safety_margin(303<317), p_lower_below_threshold(0.16<0.75) |
| 56677148 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.585107 WETH | 0.000111 WETH | 0.000000 WETH | 0.000003 WETH | 0.000107 WETH (0.1987 €) | — | 1.83 | 0.160 (n=43) | REJECTED | below_safety_margin(107287155161607<117021453991468), p_lower_below_threshold(0.16<0.75) |
| 56677148 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 1,167.904486 USDC | 0.222474 USDC | 0.000000 USDC | 0.006990 USDC | 0.215484 USDC (0.1982 €) | — | 1.85 | 0.160 (n=43) | REJECTED | below_safety_margin(215484<233580), p_lower_below_threshold(0.16<0.75) |
| 56677148 | WETH→[pancakeswap_v3]→cbBTC→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.370292 WETH | 0.000078 WETH | 0.000000 WETH | 0.000003 WETH | 0.000075 WETH (0.1398 €) | 0.000075 WETH | 2.04 | 0.270 (n=1623) | REJECTED | p_lower_below_threshold(0.27<0.75) |
| 56677148 | cbBTC→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC | 0.009892 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1397 €) | — | 2.15 | 0.270 (n=1623) | REJECTED | p_lower_below_threshold(0.27<0.75) |
| 56677148 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC→[uniswap_v3]→USDC | 748.414263 USDC | 0.157752 USDC | 0.000000 USDC | 0.006070 USDC | 0.151682 USDC (0.1395 €) | — | 2.03 | 0.270 (n=1623) | REJECTED | p_lower_below_threshold(0.27<0.75) |
| 56677148 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC | 0.008219 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1213 €) | — | 2.25 | 0.270 (n=1623) | REJECTED | p_lower_below_threshold(0.27<0.75) |
| 56677148 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.293220 WETH | 0.000069 WETH | 0.000000 WETH | 0.000003 WETH | 0.000065 WETH (0.1211 €) | 0.000065 WETH | 2.23 | 0.270 (n=1623) | REJECTED | p_lower_below_threshold(0.27<0.75) |
| 56677148 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 601.157797 USDC | 0.137720 USDC | 0.000000 USDC | 0.006377 USDC | 0.131343 USDC (0.1208 €) | — | 2.18 | 0.270 (n=1623) | REJECTED | p_lower_below_threshold(0.27<0.75) |
| 56677234 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.010581 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0878 €) | — | 1.27 | 0.160 (n=43) | REJECTED | below_safety_margin(134<211), p_lower_below_threshold(0.16<0.75) |
| 56677234 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.388869 WETH | 0.000050 WETH | 0.000000 WETH | 0.000003 WETH | 0.000047 WETH (0.0874 €) | — | 1.21 | 0.160 (n=43) | REJECTED | below_safety_margin(47182464725528<77773711888424), p_lower_below_threshold(0.16<0.75) |
| 56677234 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 792.635195 USDC | 0.100822 USDC | 0.000000 USDC | 0.006373 USDC | 0.094449 USDC (0.0869 €) | — | 1.19 | 0.160 (n=43) | REJECTED | below_safety_margin(94449<158527), p_lower_below_threshold(0.16<0.75) |
| 56676724 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 49.821309 USDC | 0.072294 USDC | 0.000000 USDC | 0.004520 USDC | 0.067774 USDC (0.0624 €) | — | 13.60 | 0.007 (n=118) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.01<0.75) |
| 56680536 | USDC→[pancakeswap_v3]→PLAY→[aerodrome_slipstream]→USDC | 49.946270 USDC | 0.069448 USDC | 0.000000 USDC | 0.004520 USDC | 0.064928 USDC (0.0597 €) | — | 13.00 | 0.012 (n=119) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.01<0.75) |
| 56677234 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.004077 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0465 €) | — | 1.74 | 0.160 (n=43) | REJECTED | below_safety_margin(71<81), p_lower_below_threshold(0.16<0.75) |
| 56677234 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.147657 WETH | 0.000028 WETH | 0.000000 WETH | 0.000003 WETH | 0.000025 WETH (0.0462 €) | — | 1.69 | 0.160 (n=43) | REJECTED | below_safety_margin(24930047586094<29531350520757), p_lower_below_threshold(0.16<0.75) |
| 56677234 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 299.775021 USDC | 0.056216 USDC | 0.000000 USDC | 0.006067 USDC | 0.050149 USDC (0.0461 €) | — | 1.67 | 0.160 (n=43) | REJECTED | below_safety_margin(50149<59955), p_lower_below_threshold(0.16<0.75) |
| 56677234 | USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 222.707570 USDC | 0.053240 USDC | 0.000000 USDC | 0.006067 USDC | 0.047173 USDC (0.0434 €) | — | 2.12 | 0.270 (n=1625) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.27<0.75) |
| 56677234 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH | 0.111691 WETH | 0.000026 WETH | 0.000000 WETH | 0.000003 WETH | 0.000023 WETH (0.0434 €) | — | 2.10 | 0.270 (n=1625) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.27<0.75) |
| 56677234 | cbBTC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.002858 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0432 €) | — | 2.31 | 0.270 (n=1625) | REJECTED | p_lower_below_threshold(0.27<0.75) |
| 56677234 | cbBTC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.006598 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0419 €) | — | 0.97 | 0.270 (n=1625) | REJECTED | below_safety_margin(64<131), p_lower_below_threshold(0.27<0.75) |
| 56677234 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→WETH | 0.232921 WETH | 0.000026 WETH | 0.000000 WETH | 0.000003 WETH | 0.000023 WETH (0.0418 €) | — | 0.97 | 0.270 (n=1625) | REJECTED | below_safety_margin(22556402510793<46584199735692), p_lower_below_threshold(0.27<0.75) |

## Fiabilité et décision
- Observations ghost : 8498 ; taux observé 0.224 ; borne inférieure crédible (0.9) 0.219 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 21.9% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ✅ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
