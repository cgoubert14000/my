# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-13T00:50:03+00:00 ; durée 158.0 min ; blocs 56655713 → 56703082 (10387 vus)

## Connexion
- Requêtes RPC : 129228 ; erreurs : 25 ; latence p50/p95 : 188.7/922.6 ms
- Rafraîchissements d'état : 10387 ; âge des données au dernier bloc : 5.8 s ; changements de frais LP observés (pools à frais dynamiques) : 4214
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 8699 ; cycles déclenchés par événement : 3428 ; avance médiane sur le rafraîchissement multicall : 360 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,005.37 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 457 pools, 266 jetons, 14822 routes
- Par DEX : uniswap_v3 133, aerodrome_slipstream 97, aerodrome 187, pancakeswap_v3 27, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 1
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 159 (rejetés 2) → 564 jetons ; pools candidats 3621 (énumérés 282, par paires 0), mesurés 459, sous le plancher de 10000.0 $ : 2 → gardés 457 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'DAI': 1.0, 'USDC': 1.0, 'WETH': 2015.232847, 'cbBTC': 71439.030081, 'AERO': 0.524681}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 132,268,625 | 2,005.368576 | 56703105 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,265,945 | 0.028282 | 56703105 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 8,480,798 | 0.028241 | 56703105 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 8,085,663 | 0.000014 | 56703105 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 6,824,631 | 2,009.066820 | 56703105 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 6,630,737 | 106.569772 | 56703105 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,183,014 | 0.028293 | 56703105 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 4,117,942 | 1.929071 | 56703105 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,016,771 | 2,008.885818 | 56703105 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,734,952 | 0.998722 | 56703105 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 2,982,249 | 42,316.049459 | 56703105 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 255 | 2,790,504 | 2,009.329505 | 56703105 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,143,489 | 0.028251 | 56703105 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 1,872,198 | 1,163,003.281972 | 56703105 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | XDP/USDC | 100 | 1,639,743 | 0.016663 | 56703105 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | USDC/cbBTC | 556 | 1,591,135 | 0.000014 | 56703105 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,557,989 | 0.000014 | 56703105 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,496,522 | 0.000000 | 56703105 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,483,914 | 0.006592 | 56703105 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,464,372 | 0.832812 | 56703105 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,463,106 | 0.000014 | 56703105 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,376,731 | 425.954705 | 56703105 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v2 | WETH/USDC | 3000 | 1,255,835 | 2,005.134459 | 56703105 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| uniswap_v3 | WETH/AERO | 3000 | 1,216,137 | 3,868.963415 | 56703105 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,181,323 | 15,061.173662 | 56703105 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/USDC | 3000 | 1,141,313 | 2,009.444822 | 56703105 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,095,898 | 2,009.221961 | 56703105 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,060,920 | 86.332345 | 56703105 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,037,340 | 1.402298 | 56703105 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | WETH/doginme | 10000 | 1,001,410 | 35,325,871.530177 | 56703105 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome_slipstream | USDC/VELVET | 100 | 978,524 | 20.191252 | 56703105 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/VVV | 10000 | 974,853 | 106.184908 | 56703105 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/BRETT | 10000 | 918,337 | 559,046.593963 | 56703105 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 885,112 | 0.001501 | 56703105 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| uniswap_v3 | WETH/TOSHI | 10000 | 879,663 | 23,198,414.506234 | 56703105 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | USDC/VVV | 3000 | 870,842 | 0.053094 | 56703105 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/USDC | 10000 | 867,729 | 2,005.198605 | 56703105 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 867,564 | 996.922685 | 56703105 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome_slipstream | USDC/cbBTC | 352 | 860,900 | 0.000014 | 56703105 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | DRB/WETH | 10000 | 803,251 | 0.000000 | 56703105 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | USDC/NOCK | 3000 | 770,400 | 79.250127 | 56703105 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| pancakeswap_v3 | QUID/USDC | 100 | 751,680 | 0.050356 | 56703105 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 744,680 | 23.144251 | 56703105 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome | WETH/AERO | 10000 | 682,439 | 3,864.686083 | 56703105 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | WETH/wstETH | 3000 | 679,421 | 0.801801 | 56703105 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 662,805 | 0.526338 | 56703105 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 626,126 | 4,864,761.205121 | 56703105 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 603,464 | 0.458612 | 56703105 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/NPC | 3000 | 578,056 | 152,589.565334 | 56703105 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome | VIRTUAL/WETH | 10000 | 565,816 | 0.000260 | 56703105 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 563,993 | 555,417.301837 | 56703105 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | FLOCK/USDC | 3000 | 560,834 | 0.038016 | 56703105 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome_slipstream | AERO/cbBTC | 1025 | 551,688 | 0.000007 | 56703105 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/MORPHO | 2709 | 484,478 | 997.623955 | 56703105 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| pancakeswap_v3 | ELSA/USDC | 100 | 462,755 | 0.066545 | 56703105 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| aerodrome_slipstream | USDC/USDT | 8 | 449,535 | 1.001017 | 56703105 | `0xa41Bc0AFfbA7Fd420d186b84899d7ab2aC57fcD1` |
| uniswap_v3 | USDC/MORPHO | 10000 | 449,439 | 0.495782 | 56703105 | `0x2043B296fFC6b2d3bf4A3F3167d2Afb3B0FBdbEE` |
| uniswap_v3 | WETH/UNI | 10000 | 433,745 | 332.339112 | 56703105 | `0xAb365f161Dd501473a1ff0D2ef0dCE94E7398839` |
| uniswap_v3 | WETH/uSOL | 3000 | 427,351 | 24.889692 | 56703105 | `0xab04A352D4EC8d0F1812A4E5EBe7807Fa67acD48` |
| aerodrome | cbBTC/EDGE | 7000 | 425,464 | 888,656.808808 | 56703105 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |

## Recherche d'opportunités
- Cycles : 13814 ; routes examinées : 204751108 ; candidats optimisés : 976078 ; net attendu > 0 : 1171 ; dernier cycle 308.8 ms
- Rejets (moteur) : {'spread_below_threshold': 200219441, 'liquidity_below_min': 3550162, 'negative_expected_net': 974907, 'borrow_bound_too_small': 2902, 'cycle_budget_exhausted': 1695, 'pool_quarantined': 588, 'unquotable': 242}
- Enregistrements de la session : 976078 ; net attendu > 0 : 1171 ; simulés (eth_call de la vraie tx) : 73 (ok 48, échec 25) ; étiquettes ghost N+1 : 36/61 positives
- Décisions : {'REJECTED': 976078} ; motifs de rejet : {'below_safety_margin': 960, 'negative_expected_net': 974907, 'p_lower_below_threshold': 1146, 'reliability_not_demonstrated': 25, 'sim_below_estimate': 17, 'simulated_net_nonpositive': 10, 'simulation_failed': 25, 'stale_data': 11}

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
| 56696663 | USDC→[pancakeswap_v3]→PLAY→[aerodrome_slipstream]→USDC | 55.878831 USDC | 0.093674 USDC | 0.000000 USDC | 0.004522 USDC | 0.089152 USDC (0.0820 €) | 0.089152 USDC | 15.95 | 0.012 (n=122) | REJECTED | p_lower_below_threshold(0.01<0.75) |
| 56676724 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 49.821309 USDC | 0.072294 USDC | 0.000000 USDC | 0.004520 USDC | 0.067774 USDC (0.0624 €) | — | 13.60 | 0.007 (n=118) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.01<0.75) |
| 56690198 | USDC→[pancakeswap_v3]→PLAY→[aerodrome_slipstream]→USDC | 48.859761 USDC | 0.071110 USDC | 0.000000 USDC | 0.004522 USDC | 0.066588 USDC (0.0613 €) | 0.066588 USDC | 13.63 | 0.012 (n=120) | REJECTED | p_lower_below_threshold(0.01<0.75) |
| 56680536 | USDC→[pancakeswap_v3]→PLAY→[aerodrome_slipstream]→USDC | 49.946270 USDC | 0.069448 USDC | 0.000000 USDC | 0.004520 USDC | 0.064928 USDC (0.0597 €) | — | 13.00 | 0.012 (n=119) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.01<0.75) |
| 56677234 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.004077 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0465 €) | — | 1.74 | 0.160 (n=43) | REJECTED | below_safety_margin(71<81), p_lower_below_threshold(0.16<0.75) |
| 56677234 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.147657 WETH | 0.000028 WETH | 0.000000 WETH | 0.000003 WETH | 0.000025 WETH (0.0462 €) | — | 1.69 | 0.160 (n=43) | REJECTED | below_safety_margin(24930047586094<29531350520757), p_lower_below_threshold(0.16<0.75) |
| 56677234 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 299.775021 USDC | 0.056216 USDC | 0.000000 USDC | 0.006067 USDC | 0.050149 USDC (0.0461 €) | — | 1.67 | 0.160 (n=43) | REJECTED | below_safety_margin(50149<59955), p_lower_below_threshold(0.16<0.75) |
| 56677234 | USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 222.707570 USDC | 0.053240 USDC | 0.000000 USDC | 0.006067 USDC | 0.047173 USDC (0.0434 €) | — | 2.12 | 0.270 (n=1625) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.27<0.75) |
| 56677234 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH | 0.111691 WETH | 0.000026 WETH | 0.000000 WETH | 0.000003 WETH | 0.000023 WETH (0.0434 €) | — | 2.10 | 0.270 (n=1625) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.27<0.75) |
| 56677234 | cbBTC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.002858 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0432 €) | — | 2.31 | 0.270 (n=1625) | REJECTED | p_lower_below_threshold(0.27<0.75) |

## Fiabilité et décision
- Observations ghost : 8529 ; taux observé 0.225 ; borne inférieure crédible (0.9) 0.220 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 22.0% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ✅ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
