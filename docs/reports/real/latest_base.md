# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-09T04:42:38+00:00 ; durée 21.39 min ; blocs 55038467 → 55044866 (939 vus)

## Connexion
- Requêtes RPC : 12923 ; erreurs : 0 ; latence p50/p95 : 368.9/1,733.9 ms
- Rafraîchissements d'état : 939 ; âge des données au dernier bloc : 10.18 s ; changements de frais LP observés (pools à frais dynamiques) : 444
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 1118 ; cycles déclenchés par événement : 401 ; avance médiane sur le rafraîchissement multicall : 496 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,141.21 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 467 pools, 272 jetons, 17562 routes
- Par DEX : uniswap_v3 134, aerodrome_slipstream 97, aerodrome 194, pancakeswap_v3 28, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 166 (rejetés 2) → 571 jetons ; pools candidats 3664 (énumérés 288, par paires 0), mesurés 469, sous le plancher de 10000.0 $ : 2 → gardés 467 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'DAI': 1.0, 'USDC': 1.0, 'WETH': 2141.212816, 'cbBTC': 74926.035696, 'AERO': 0.58265}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 140,217,111 | 2,141.213372 | 55044894 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,480,559 | 0.028570 | 55044894 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 8,996,294 | 0.000013 | 55044894 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 8,827,159 | 0.028533 | 55044894 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 7,898,208 | 2,136.274579 | 55044894 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,192,995 | 103.534840 | 55044894 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,299,595 | 0.001529 | 55044894 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 4,624,718 | 1.724163 | 55044894 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,620,250 | 0.028560 | 55044894 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,944,647 | 0.999218 | 55044894 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| pancakeswap_v3 | WETH/USDC | 100 | 3,856,795 | 2,135.626368 | 55044894 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | WETH/KTA | 3000 | 3,161,524 | 42,917.284618 | 55044894 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 150 | 3,051,668 | 2,135.533778 | 55044894 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,384,938 | 0.028551 | 55044894 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 2,002,175 | 1,159,342.676479 | 55044894 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 592 | 1,713,477 | 0.000013 | 55044894 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,614,601 | 0.006663 | 55044894 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,607,423 | 0.000013 | 55044894 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,565,043 | 0.000000 | 55044894 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,563,441 | 0.015485 | 55044894 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,474,099 | 1.421539 | 55044894 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,466,121 | 433.153654 | 55044894 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,412,689 | 0.000013 | 55044894 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v3 | WETH/AERO | 3000 | 1,334,264 | 3,686.764331 | 55044894 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v2 | WETH/USDC | 3000 | 1,297,157 | 2,141.987819 | 55044894 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,243,875 | 15,154.829672 | 55044894 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/USDC | 3000 | 1,226,453 | 2,141.150767 | 55044894 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome | USDC/SEND | 3000 | 1,120,777 | 77.357246 | 55044894 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,097,703 | 2,136.412046 | 55044894 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | WETH/doginme | 10000 | 1,050,814 | 37,092,779.018412 | 55044894 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/VVV | 10000 | 1,024,479 | 104.274334 | 55044894 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/BRETT | 10000 | 963,787 | 588,898.684941 | 55044894 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome_slipstream | USDC/VELVET | 100 | 952,592 | 21.906148 | 55044894 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/TOSHI | 10000 | 948,932 | 22,747,860.254386 | 55044894 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/cbBTC | 368 | 929,188 | 0.000013 | 55044894 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/NOCK | 3000 | 917,610 | 74.420398 | 55044894 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | DRB/WETH | 10000 | 914,863 | 0.000000 | 55044894 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/USDC | 10000 | 913,761 | 2,137.198475 | 55044894 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 908,989 | 1,044.119981 | 55044894 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 856,251 | 0.824196 | 55044894 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome | WETH/EDEL | 7000 | 833,629 | 100,581.196815 | 55044894 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | USDC/VVV | 3000 | 822,519 | 0.048419 | 55044894 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| pancakeswap_v3 | QUID/USDC | 100 | 780,325 | 0.054417 | 55044894 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/AERO | 10000 | 754,349 | 3,677.033511 | 55044894 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 753,095 | 22.755175 | 55044894 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome | WETH/wstETH | 3000 | 725,651 | 0.801347 | 55044894 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 701,124 | 0.538640 | 55044894 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 654,886 | 5,060,013.820255 | 55044894 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 643,735 | 0.524790 | 55044894 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 628,924 | 0.000008 | 55044894 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v2 | WETH/NPC | 3000 | 620,663 | 150,538.805123 | 55044894 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome | VIRTUAL/WETH | 10000 | 596,634 | 0.000251 | 55044894 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/BRETT | 2105 | 585,677 | 588,298.458625 | 55044894 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | FLOCK/USDC | 3000 | 568,465 | 0.038640 | 55044894 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome | WETH/msETH (stable) | 500 | 531,417 | 2.463045 | 55044894 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 515,557 | 1,043.870713 | 55044894 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome | cbBTC/EDGE | 7000 | 507,733 | 926,895.260150 | 55044894 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| uniswap_v3 | USDC/USDT | 100 | 497,518 | 1.001286 | 55044894 | `0xD56da2B74bA826f19015E6B7Dd9Dae1903E85DA1` |
| uniswap_v3 | WETH/USDC | 100 | 492,010 | 2,135.501043 | 55044894 | `0xb4CB800910B228ED3d0834cF79D697127BBB00e5` |
| pancakeswap_v3 | ELSA/USDC | 100 | 489,314 | 0.071338 | 55044894 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |

## Recherche d'opportunités
- Cycles : 1339 ; routes examinées : 23515518 ; candidats optimisés : 62345 ; net attendu > 0 : 35 ; dernier cycle 161.3 ms
- Rejets (moteur) : {'spread_below_threshold': 23091378, 'liquidity_below_min': 360456, 'negative_expected_net': 62310, 'borrow_bound_too_small': 1339}
- Enregistrements de la session : 62345 ; net attendu > 0 : 35 ; simulés (eth_call de la vraie tx) : 5 (ok 2, échec 3) ; étiquettes ghost N+1 : 2/4 positives
- Décisions : {'REJECTED': 62345} ; motifs de rejet : {'below_safety_margin': 30, 'negative_expected_net': 62310, 'p_lower_below_threshold': 35, 'simulation_failed': 3, 'stale_data': 2}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 55040533 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 27.623305 USDC | 0.022893 USDC | 0.000000 USDC | 0.004807 USDC | 0.018086 USDC (0.0166 €) | — | 6.55 | 0.045 (n=412) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.04<0.75) |
| 55042939 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 24.542996 USDC | 0.017761 USDC | 0.000000 USDC | 0.004807 USDC | 0.012954 USDC (0.0119 €) | 0.012954 USDC | 5.28 | 0.047 (n=413) | REJECTED | stale_data(5228ms>4000.0), p_lower_below_threshold(0.05<0.75) |
| 55043302 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 22.784647 USDC | 0.015645 USDC | 0.000000 USDC | 0.004807 USDC | 0.010838 USDC (0.0100 €) | 0.010838 USDC | 4.76 | 0.047 (n=414) | REJECTED | stale_data(4765ms>4000.0), p_lower_below_threshold(0.05<0.75) |
| 55041630 | USDC→[pancakeswap_v3]→ICNT→[uniswap_v3]→USDC | 36.625131 USDC | 0.014277 USDC | 0.000000 USDC | 0.004808 USDC | 0.009469 USDC (0.0087 €) | — | 2.59 | 0.054 (n=295) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.05<0.75) |
| 55041631 | USDC→[pancakeswap_v3]→ICNT→[uniswap_v3]→USDC | 36.625131 USDC | 0.014277 USDC | 0.000000 USDC | 0.004808 USDC | 0.009469 USDC (0.0087 €) | — | 2.59 | 0.054 (n=295) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.05<0.75) |
| 55039944 | USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 41.803490 USDC | 0.009933 USDC | 0.000000 USDC | 0.006462 USDC | 0.003471 USDC (0.0032 €) | — | 0.83 | 0.204 (n=1207) | REJECTED | below_safety_margin(3471<8360), p_lower_below_threshold(0.20<0.75) |
| 55039944 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH | 0.019589 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0032 €) | — | 0.83 | 0.204 (n=1207) | REJECTED | below_safety_margin(1618061203521<3917762519820), p_lower_below_threshold(0.20<0.75) |
| 55039944 | USDC→[pancakeswap_v3]→USDT→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 41.209244 USDC | 0.009675 USDC | 0.000000 USDC | 0.006462 USDC | 0.003213 USDC (0.0030 €) | — | 0.78 | 0.204 (n=1207) | REJECTED | below_safety_margin(3213<8241), p_lower_below_threshold(0.20<0.75) |
| 55039944 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→USDT→[aerodrome_slipstream]→WETH | 0.019234 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0030 €) | — | 0.78 | 0.204 (n=1207) | REJECTED | below_safety_margin(1497659041386<3846745966365), p_lower_below_threshold(0.20<0.75) |
| 55039944 | USDC→[aerodrome_slipstream]→USDT→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 43.707550 USDC | 0.009646 USDC | 0.000000 USDC | 0.006789 USDC | 0.002857 USDC (0.0026 €) | — | 0.65 | 0.204 (n=1207) | REJECTED | below_safety_margin(2857<8741), p_lower_below_threshold(0.20<0.75) |
| 55039944 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→USDT→[uniswap_v3]→WETH | 0.020503 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0026 €) | — | 0.65 | 0.204 (n=1207) | REJECTED | below_safety_margin(1331803629011<4100605732847), p_lower_below_threshold(0.20<0.75) |
| 55039944 | USDC→[pancakeswap_v3]→USDT→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 42.799176 USDC | 0.009375 USDC | 0.000000 USDC | 0.006789 USDC | 0.002586 USDC (0.0024 €) | — | 0.60 | 0.204 (n=1207) | REJECTED | below_safety_margin(2586<8559), p_lower_below_threshold(0.20<0.75) |
| 55039944 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→USDT→[uniswap_v3]→WETH | 0.020135 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0024 €) | — | 0.60 | 0.204 (n=1207) | REJECTED | below_safety_margin(1205403502733<4026973412099), p_lower_below_threshold(0.20<0.75) |
| 55040925 | WETH→[uniswap_v3]→VIRTUAL→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.020277 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0023 €) | — | 0.58 | 0.204 (n=1207) | REJECTED | below_safety_margin(1182197901303<4055315527696), p_lower_below_threshold(0.20<0.75) |
| 55040931 | WETH→[uniswap_v3]→VIRTUAL→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.020277 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0023 €) | — | 0.58 | 0.204 (n=1207) | REJECTED | below_safety_margin(1182197901303<4055315527696), p_lower_below_threshold(0.20<0.75) |
| 55040925 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→VIRTUAL→[pancakeswap_v3]→USDC | 43.144049 USDC | 0.008962 USDC | 0.000000 USDC | 0.006434 USDC | 0.002528 USDC (0.0023 €) | — | 0.59 | 0.204 (n=1207) | REJECTED | below_safety_margin(2528<8628), p_lower_below_threshold(0.20<0.75) |
| 55040931 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→VIRTUAL→[pancakeswap_v3]→USDC | 43.144049 USDC | 0.008962 USDC | 0.000000 USDC | 0.006434 USDC | 0.002528 USDC (0.0023 €) | — | 0.59 | 0.204 (n=1207) | REJECTED | below_safety_margin(2528<8628), p_lower_below_threshold(0.20<0.75) |
| 55039944 | USDC→[uniswap_v3]→USDT→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 39.173695 USDC | 0.008785 USDC | 0.000000 USDC | 0.006462 USDC | 0.002323 USDC (0.0021 €) | — | 0.59 | 0.204 (n=1207) | REJECTED | below_safety_margin(2323<7834), p_lower_below_threshold(0.20<0.75) |
| 55039944 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→USDT→[aerodrome_slipstream]→WETH | 0.018520 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0021 €) | — | 0.58 | 0.204 (n=1207) | REJECTED | below_safety_margin(1082514557008<3704060043010), p_lower_below_threshold(0.20<0.75) |
| 55039944 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.000558 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0021 €) | — | 0.54 | 0.204 (n=1207) | REJECTED | below_safety_margin(3<11), p_lower_below_threshold(0.20<0.75) |
| 55039943 | USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 37.963478 USDC | 0.008264 USDC | 0.000000 USDC | 0.006441 USDC | 0.001823 USDC (0.0017 €) | — | 0.48 | 0.204 (n=1207) | REJECTED | below_safety_margin(1823<7592), p_lower_below_threshold(0.20<0.75) |
| 55039943 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH | 0.017849 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0017 €) | — | 0.48 | 0.204 (n=1207) | REJECTED | below_safety_margin(848968339503<3569869807785), p_lower_below_threshold(0.20<0.75) |
| 55039944 | USDC→[uniswap_v3]→USDT→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 40.687698 USDC | 0.008448 USDC | 0.000000 USDC | 0.006789 USDC | 0.001659 USDC (0.0015 €) | — | 0.41 | 0.204 (n=1207) | REJECTED | below_safety_margin(1659<8137), p_lower_below_threshold(0.20<0.75) |
| 55039944 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→USDT→[uniswap_v3]→WETH | 0.019206 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0015 €) | — | 0.40 | 0.204 (n=1207) | REJECTED | below_safety_margin(773000555241<3841129172340), p_lower_below_threshold(0.20<0.75) |
| 55039943 | USDC→[pancakeswap_v3]→USDT→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 37.536799 USDC | 0.008030 USDC | 0.000000 USDC | 0.006441 USDC | 0.001589 USDC (0.0015 €) | — | 0.42 | 0.204 (n=1207) | REJECTED | below_safety_margin(1589<7507), p_lower_below_threshold(0.20<0.75) |

## Fiabilité et décision
- Observations ghost : 6654 ; taux observé 0.175 ; borne inférieure crédible (0.9) 0.169 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 16.9% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
