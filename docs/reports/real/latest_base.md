# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-05T23:17:02+00:00 ; durée 113.06 min ; blocs 53617273 → 53651187 (1473 vus)

## Connexion
- Requêtes RPC : 46246 ; erreurs : 220 ; latence p50/p95 : 669.8/1,928.2 ms
- Rafraîchissements d'état : 1473 ; âge des données au dernier bloc : 8.16 s ; changements de frais LP observés (pools à frais dynamiques) : 3987
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 3578 ; cycles déclenchés par événement : 893 ; avance médiane sur le rafraîchissement multicall : 779 ms
- Gaz : base fee 0.005001 gwei ; prix ETH (pool le plus profond) : 2,212.60 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 482 pools, 280 jetons, 18100 routes
- Par DEX : uniswap_v3 136, aerodrome_slipstream 101, aerodrome 201, pancakeswap_v3 30, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 173 (rejetés 2) → 578 jetons ; pools candidats 3707 (énumérés 302, par paires 0), mesurés 487, sous le plancher de 10000.0 $ : 5 → gardés 482 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2231.121633, 'cbBTC': 75799.40241, 'AERO': 0.604242}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 144,971,037 | 2,212.595301 | 53651222 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,390,365 | 0.029399 | 53651222 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,162,321 | 0.000013 | 53651222 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,017,594 | 0.029375 | 53651222 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 7,894,752 | 2,217.861076 | 53651222 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,320,491 | 106.792209 | 53651222 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,348,231 | 0.001540 | 53651222 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 5,044,122 | 1.693922 | 53651222 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,624,215 | 0.029390 | 53651222 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,060,745 | 2,218.710357 | 53651222 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,965,206 | 0.998654 | 53651222 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,270,002 | 42,847.255187 | 53651222 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 150 | 3,184,411 | 2,218.583806 | 53651222 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,536,583 | 0.029384 | 53651222 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 2,059,216 | 1,170,297.440977 | 53651222 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,955,114 | 0.008243 | 53651222 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/cbBTC | 600 | 1,733,894 | 0.000013 | 53651222 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,624,219 | 0.000000 | 53651222 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,621,819 | 0.016216 | 53651222 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,614,932 | 0.000013 | 53651222 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,529,107 | 1.457700 | 53651222 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,506,123 | 0.000013 | 53651222 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,496,219 | 450.031072 | 53651222 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,459,340 | 0.816940 | 53651222 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,356,164 | 3,752.497806 | 53651222 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v2 | WETH/USDC | 3000 | 1,318,060 | 2,212.415020 | 53651222 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome | WETH/USDC | 3000 | 1,316,719 | 2,212.670726 | 53651222 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,242,658 | 15,282.922932 | 53651222 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,154,687 | 2,217.964585 | 53651222 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,123,791 | 76.942850 | 53651222 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,084,910 | 37,163,661.328170 | 53651222 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/VVV | 10000 | 1,040,275 | 106.059316 | 53651222 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,003,732 | 575,189.263507 | 53651222 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | DRB/WETH | 10000 | 996,991 | 0.000000 | 53651222 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/TOSHI | 10000 | 985,296 | 22,568,618.897092 | 53651222 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/VELVET | 100 | 952,163 | 21.934647 | 53651222 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | USDC/NOCK | 3000 | 948,521 | 69.693442 | 53651222 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/USDC | 10000 | 930,894 | 2,225.465428 | 53651222 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 920,936 | 1,072.459143 | 53651222 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome_slipstream | USDC/cbBTC | 372 | 918,208 | 0.000013 | 53651222 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | WETH/EDEL | 7000 | 870,996 | 98,429.075539 | 53651222 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | uXRP/WETH | 3000 | 840,580 | 0.000540 | 53651222 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| uniswap_v3 | USDC/VVV | 3000 | 838,723 | 0.048155 | 53651222 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| pancakeswap_v3 | QUID/USDC | 100 | 788,576 | 0.055641 | 53651222 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/AERO | 10000 | 784,412 | 3,730.662252 | 53651222 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | USDC/SAPIEN | 4530 | 780,299 | 21.636678 | 53651222 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome | WETH/wstETH | 3000 | 750,752 | 0.799698 | 53651222 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 708,199 | 0.554890 | 53651222 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 682,164 | 4,977,606.774565 | 53651222 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome | VIRTUAL/WETH | 10000 | 675,446 | 0.000253 | 53651222 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v2 | WETH/NPC | 3000 | 660,838 | 141,681.697239 | 53651222 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| uniswap_v3 | TIG/USDC | 10000 | 649,801 | 0.530869 | 53651222 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 642,385 | 0.000008 | 53651222 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/BRETT | 2144 | 612,362 | 579,160.847624 | 53651222 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome | WETH/bsdETH | 100 | 593,029 | 0.914700 | 53651222 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome | WETH/msETH (stable) | 500 | 591,140 | 2.474202 | 53651222 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| pancakeswap_v3 | ELSA/USDC | 100 | 544,865 | 0.083320 | 53651222 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| uniswap_v3 | FLOCK/USDC | 3000 | 539,790 | 0.035953 | 53651222 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome | cbBTC/EDGE | 7000 | 534,907 | 837,328.317061 | 53651222 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 515,963 | 1,072.773619 | 53651222 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |

## Recherche d'opportunités
- Cycles : 2365 ; routes examinées : 42806500 ; candidats optimisés : 140061 ; net attendu > 0 : 52 ; dernier cycle 311.6 ms
- Rejets (moteur) : {'spread_below_threshold': 41950350, 'liquidity_below_min': 711448, 'negative_expected_net': 140009, 'borrow_bound_too_small': 2328, 'cycle_budget_exhausted': 2313}
- Enregistrements de la session : 140061 ; net attendu > 0 : 52 ; simulés (eth_call de la vraie tx) : 5 (ok 4, échec 1) ; étiquettes ghost N+1 : 1/5 positives
- Décisions : {'REJECTED': 140061} ; motifs de rejet : {'below_safety_margin': 47, 'negative_expected_net': 140009, 'p_lower_below_threshold': 46, 'reliability_not_demonstrated': 6, 'simulation_failed': 1, 'stale_data': 34}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53617917 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.338587 WETH | 0.000069 WETH | 0.000000 WETH | 0.000003 WETH | 0.000066 WETH (0.1350 €) | — | 1.95 | 0.046 (n=233) | REJECTED | below_safety_margin(66042364924503<67717351541604), stale_data(6295ms>4000.0), p_lower_below_threshold(0.05<0.75) |
| 53617917 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 748.880467 USDC | 0.152184 USDC | 0.000000 USDC | 0.005683 USDC | 0.146501 USDC (0.1348 €) | — | 1.96 | 0.046 (n=233) | REJECTED | below_safety_margin(146501<149776), stale_data(6303ms>4000.0), p_lower_below_threshold(0.05<0.75) |
| 53617917 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.152255 WETH | 0.000047 WETH | 0.000000 WETH | 0.000003 WETH | 0.000044 WETH (0.0908 €) | 0.000044 WETH | 2.92 | 0.057 (n=76) | REJECTED | stale_data(6191ms>4000.0), p_lower_below_threshold(0.06<0.75) |
| 53617917 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 336.649658 USDC | 0.104612 USDC | 0.000000 USDC | 0.006041 USDC | 0.098571 USDC (0.0907 €) | 0.098571 USDC | 2.93 | 0.057 (n=76) | REJECTED | stale_data(6198ms>4000.0), p_lower_below_threshold(0.06<0.75) |
| 53649132 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 345.694814 USDC | 0.098995 USDC | 0.000000 USDC | 0.005847 USDC | 0.093148 USDC (0.0857 €) | 0.093148 USDC | 2.69 | 0.056 (n=78) | REJECTED | stale_data(5536ms>4000.0), p_lower_below_threshold(0.06<0.75) |
| 53649132 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.156617 WETH | 0.000045 WETH | 0.000000 WETH | 0.000003 WETH | 0.000042 WETH (0.0856 €) | 0.000042 WETH | 2.69 | 0.056 (n=78) | REJECTED | stale_data(5529ms>4000.0), p_lower_below_threshold(0.06<0.75) |
| 53649132 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 559.146380 USDC | 0.086896 USDC | 0.000000 USDC | 0.005499 USDC | 0.081397 USDC (0.0749 €) | — | 1.46 | 0.046 (n=233) | REJECTED | below_safety_margin(81397<111829), stale_data(5610ms>4000.0), p_lower_below_threshold(0.05<0.75) |
| 53649132 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.253280 WETH | 0.000039 WETH | 0.000000 WETH | 0.000002 WETH | 0.000037 WETH (0.0748 €) | — | 1.45 | 0.046 (n=233) | REJECTED | below_safety_margin(36761086370394<50656040952722), stale_data(5603ms>4000.0), p_lower_below_threshold(0.05<0.75) |
| 53649132 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 451.754794 USDC | 0.073504 USDC | 0.000000 USDC | 0.006894 USDC | 0.066610 USDC (0.0613 €) | — | 1.47 | 0.168 (n=1020) | REJECTED | below_safety_margin(66610<90350), stale_data(5582ms>4000.0), p_lower_below_threshold(0.17<0.75) |
| 53649132 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.210558 WETH | 0.000033 WETH | 0.000000 WETH | 0.000003 WETH | 0.000030 WETH (0.0612 €) | — | 1.43 | 0.168 (n=1020) | REJECTED | below_safety_margin(30045423179333<42111650811301), stale_data(5596ms>4000.0), p_lower_below_threshold(0.17<0.75) |
| 53649132 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.005940 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0610 €) | — | 1.48 | 0.168 (n=1020) | REJECTED | below_safety_margin(88<118), stale_data(5589ms>4000.0), p_lower_below_threshold(0.17<0.75) |
| 53618187 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 333.527485 USDC | 0.029762 USDC | 0.000000 USDC | 0.005283 USDC | 0.024479 USDC (0.0225 €) | — | 0.73 | 0.046 (n=233) | REJECTED | below_safety_margin(24479<66705), p_lower_below_threshold(0.05<0.75) |
| 53618187 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.149601 WETH | 0.000013 WETH | 0.000000 WETH | 0.000002 WETH | 0.000011 WETH (0.0225 €) | — | 0.74 | 0.046 (n=233) | REJECTED | below_safety_margin(11000756189724<29920206520439), p_lower_below_threshold(0.05<0.75) |
| 53626056 | WETH→[uniswap_v3]→MEY→[aerodrome]→WETH | 0.010874 WETH | 0.000010 WETH | 0.000000 WETH | 0.000002 WETH | 0.000008 WETH (0.0170 €) | — | 7.60 | 0.234 (n=59) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.23<0.75) |
| 53617917 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.064521 WETH | 0.000010 WETH | 0.000000 WETH | 0.000003 WETH | 0.000006 WETH (0.0130 €) | — | 0.99 | 0.168 (n=1020) | REJECTED | below_safety_margin(6373757605358<12904292848390), stale_data(6350ms>4000.0), p_lower_below_threshold(0.17<0.75) |
| 53617917 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 142.645611 USDC | 0.021504 USDC | 0.000000 USDC | 0.007481 USDC | 0.014023 USDC (0.0129 €) | — | 0.98 | 0.168 (n=1020) | REJECTED | below_safety_margin(14023<28529), stale_data(6368ms>4000.0), p_lower_below_threshold(0.17<0.75) |
| 53617917 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.001637 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0126 €) | — | 1.10 | 0.168 (n=1020) | REJECTED | below_safety_margin(18<32), stale_data(6359ms>4000.0), p_lower_below_threshold(0.17<0.75) |
| 53632809 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 179.344034 USDC | 0.018208 USDC | 0.000000 USDC | 0.005365 USDC | 0.012843 USDC (0.0118 €) | — | 0.72 | 0.046 (n=233) | REJECTED | below_safety_margin(12843<35868), stale_data(7275ms>4000.0), p_lower_below_threshold(0.05<0.75) |
| 53632809 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.080433 WETH | 0.000008 WETH | 0.000000 WETH | 0.000002 WETH | 0.000006 WETH (0.0118 €) | — | 0.71 | 0.046 (n=233) | REJECTED | below_safety_margin(5732207256396<16086674229864), stale_data(7270ms>4000.0), p_lower_below_threshold(0.05<0.75) |
| 53617917 | WETH→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.043508 WETH | 0.000009 WETH | 0.000000 WETH | 0.000004 WETH | 0.000005 WETH (0.0111 €) | — | 1.24 | 0.168 (n=1020) | REJECTED | below_safety_margin(5405219764860<8701692752134), stale_data(6259ms>4000.0), p_lower_below_threshold(0.17<0.75) |
| 53617917 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 101.697045 USDC | 0.019489 USDC | 0.000000 USDC | 0.007838 USDC | 0.011651 USDC (0.0107 €) | — | 1.15 | 0.168 (n=1020) | REJECTED | below_safety_margin(11651<20339), stale_data(6272ms>4000.0), p_lower_below_threshold(0.17<0.75) |
| 53649132 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.076779 WETH | 0.000008 WETH | 0.000000 WETH | 0.000003 WETH | 0.000005 WETH (0.0106 €) | — | 0.68 | 0.168 (n=1020) | REJECTED | below_safety_margin(5197637816906<15355815469641), stale_data(5624ms>4000.0), p_lower_below_threshold(0.17<0.75) |
| 53617917 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→cbBTC | 0.001342 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0105 €) | — | 1.12 | 0.168 (n=1020) | REJECTED | below_safety_margin(15<26), stale_data(6266ms>4000.0), p_lower_below_threshold(0.17<0.75) |
| 53649132 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.002634 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0104 €) | — | 0.57 | 0.168 (n=1020) | REJECTED | below_safety_margin(15<52), stale_data(5617ms>4000.0), p_lower_below_threshold(0.17<0.75) |
| 53649132 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 204.820487 USDC | 0.018112 USDC | 0.000000 USDC | 0.006894 USDC | 0.011218 USDC (0.0103 €) | — | 0.55 | 0.168 (n=1020) | REJECTED | below_safety_margin(11218<40964), stale_data(5630ms>4000.0), p_lower_below_threshold(0.17<0.75) |

## Fiabilité et décision
- Observations ghost : 5776 ; taux observé 0.158 ; borne inférieure crédible (0.9) 0.152 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 15.2% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
