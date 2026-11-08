# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-08T21:47:11+00:00 ; durée 278.9 min ; blocs 54836572 → 54920199 (11779 vus)

## Connexion
- Requêtes RPC : 160543 ; erreurs : 15 ; latence p50/p95 : 489.4/1,864.7 ms
- Rafraîchissements d'état : 11779 ; âge des données au dernier bloc : 10.56 s ; changements de frais LP observés (pools à frais dynamiques) : 4257
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 3502 ; cycles déclenchés par événement : 1686 ; avance médiane sur le rafraîchissement multicall : 480 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,219.21 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 469 pools, 276 jetons, 17556 routes
- Par DEX : uniswap_v3 134, aerodrome_slipstream 97, aerodrome 196, pancakeswap_v3 28, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 168 (rejetés 2) → 573 jetons ; pools candidats 3671 (énumérés 291, par paires 0), mesurés 471, sous le plancher de 10000.0 $ : 2 → gardés 469 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDC': 1.0, 'USDbC': 1.0, 'WETH': 2231.430141, 'cbBTC': 75744.13603, 'AERO': 0.592088}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 144,673,722 | 2,219.205702 | 54920230 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,775,834 | 0.029401 | 54920230 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,256,453 | 0.000013 | 54920230 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,087,972 | 0.029451 | 54920230 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 8,485,312 | 2,215.887462 | 54920230 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,279,826 | 108.577752 | 54920230 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,360,956 | 0.001537 | 54920230 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,119,859 | 0.029405 | 54920230 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 4,654,430 | 1.709048 | 54920230 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,139,694 | 2,215.624250 | 54920230 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,972,898 | 0.999162 | 54920230 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,260,479 | 43,355.817785 | 54920230 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 150 | 3,153,837 | 2,215.612465 | 54920230 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2505 | 2,452,833 | 0.029435 | 54920230 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 2,072,975 | 1,161,724.493481 | 54920230 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 600 | 1,726,695 | 0.000013 | 54920230 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,624,940 | 0.000013 | 54920230 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,611,128 | 0.000000 | 54920230 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,593,752 | 0.006304 | 54920230 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v3 | XDP/USDC | 100 | 1,534,107 | 0.015079 | 54920230 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,507,674 | 444.300506 | 54920230 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,506,011 | 0.000013 | 54920230 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,468,117 | 1.431451 | 54920230 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,453,405 | 0.824203 | 54920230 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,360,139 | 3,786.244221 | 54920230 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v2 | WETH/USDC | 3000 | 1,320,285 | 2,219.538317 | 54920230 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,254,400 | 15,091.730865 | 54920230 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/USDC | 3000 | 1,251,172 | 2,219.110770 | 54920230 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,165,784 | 2,215.748543 | 54920230 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,122,761 | 77.084041 | 54920230 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,087,113 | 37,301,150.846749 | 54920230 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/VVV | 10000 | 1,028,987 | 108.140946 | 54920230 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/BRETT | 10000 | 989,337 | 606,190.212010 | 54920230 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | WETH/TOSHI | 10000 | 969,973 | 23,282,491.110903 | 54920230 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | DRB/WETH | 10000 | 960,487 | 0.000000 | 54920230 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome_slipstream | USDC/VELVET | 100 | 957,573 | 21.554732 | 54920230 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/USDC | 10000 | 933,371 | 2,228.787393 | 54920230 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome | USDC/NOCK | 3000 | 925,204 | 73.203734 | 54920230 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | USDC/cbBTC | 382 | 922,497 | 0.000013 | 54920230 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | WETH/MORPHO | 3000 | 921,030 | 1,076.495170 | 54920230 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome | WETH/EDEL | 7000 | 855,870 | 102,499.372304 | 54920230 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | USDC/VVV | 3000 | 814,398 | 0.048952 | 54920230 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| pancakeswap_v3 | QUID/USDC | 100 | 777,316 | 0.053981 | 54920230 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/AERO | 10000 | 771,354 | 3,772.507476 | 54920230 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | USDC/SAPIEN | 4585 | 758,361 | 22.530266 | 54920230 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome | WETH/wstETH | 3000 | 752,807 | 0.799805 | 54920230 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 702,217 | 0.554024 | 54920230 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 669,627 | 5,199,127.008480 | 54920230 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 666,105 | 0.560563 | 54920230 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/NPC | 3000 | 642,656 | 150,799.776666 | 54920230 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 642,565 | 0.000008 | 54920230 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | VIRTUAL/WETH | 10000 | 617,067 | 0.000250 | 54920230 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/BRETT | 2168 | 597,821 | 608,677.934164 | 54920230 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | FLOCK/USDC | 3000 | 574,852 | 0.039337 | 54920230 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome | WETH/msETH (stable) | 500 | 549,507 | 2.471463 | 54920230 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome | cbBTC/EDGE | 7000 | 522,032 | 886,104.065221 | 54920230 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| aerodrome_slipstream | WETH/MORPHO | 2703 | 521,093 | 1,076.362114 | 54920230 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| uniswap_v3 | WETH/USDC | 100 | 515,376 | 2,215.565221 | 54920230 | `0xb4CB800910B228ED3d0834cF79D697127BBB00e5` |
| aerodrome | WETH/DRV | 3000 | 508,020 | 6,997.916553 | 54920230 | `0xaC4e562d7C6108f971321F14238E24AE2cC398ac` |
| pancakeswap_v3 | ELSA/USDC | 100 | 507,410 | 0.074844 | 54920230 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |

## Recherche d'opportunités
- Cycles : 13464 ; routes examinées : 236373984 ; candidats optimisés : 671565 ; net attendu > 0 : 233 ; dernier cycle 516.8 ms
- Rejets (moteur) : {'spread_below_threshold': 232150062, 'liquidity_below_min': 3520562, 'negative_expected_net': 671332, 'borrow_bound_too_small': 30204, 'cycle_budget_exhausted': 1255, 'pool_quarantined': 336}
- Enregistrements de la session : 671565 ; net attendu > 0 : 233 ; simulés (eth_call de la vraie tx) : 35 (ok 21, échec 14) ; étiquettes ghost N+1 : 4/34 positives
- Décisions : {'REJECTED': 671565} ; motifs de rejet : {'below_safety_margin': 167, 'negative_expected_net': 671332, 'p_lower_below_threshold': 211, 'price_impact': 6, 'reliability_not_demonstrated': 22, 'simulation_failed': 14, 'stale_data': 58}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 54846483 | WETH→[aerodrome]→SLC→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.020353 WETH | 0.000213 WETH | 0.000000 WETH | 0.000003 WETH | 0.000210 WETH (0.4303 €) | — | 103.09 | 0.001 (n=9) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 54846483 | USDC→[pancakeswap_v3]→WETH→[aerodrome]→SLC→[uniswap_v3]→USDC | 45.336647 USDC | 0.473745 USDC | 0.000000 USDC | 0.006396 USDC | 0.467349 USDC (0.4300 €) | — | 103.08 | 0.001 (n=9) | REJECTED | reliability_not_demonstrated |
| 54846483 | WETH→[aerodrome]→SLC→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.020201 WETH | 0.000212 WETH | 0.000000 WETH | 0.000003 WETH | 0.000210 WETH (0.4299 €) | — | 103.77 | 0.000 (n=25) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 54846483 | USDC→[uniswap_v3]→WETH→[aerodrome]→SLC→[uniswap_v3]→USDC | 44.998596 USDC | 0.473353 USDC | 0.000000 USDC | 0.006396 USDC | 0.466957 USDC (0.4296 €) | — | 103.77 | 0.000 (n=25) | REJECTED | reliability_not_demonstrated |
| 54846483 | WETH→[aerodrome]→SLC→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.019755 WETH | 0.000209 WETH | 0.000000 WETH | 0.000003 WETH | 0.000206 WETH (0.4222 €) | — | 104.20 | 0.000 (n=25) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 54846483 | USDC→[aerodrome_slipstream]→WETH→[aerodrome]→SLC→[uniswap_v3]→USDC | 44.004281 USDC | 0.464900 USDC | 0.000000 USDC | 0.006396 USDC | 0.458504 USDC (0.4218 €) | — | 104.20 | 0.000 (n=25) | REJECTED | reliability_not_demonstrated |
| 54846483 | WETH→[aerodrome]→SLC→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.016068 WETH | 0.000174 WETH | 0.000000 WETH | 0.000003 WETH | 0.000172 WETH (0.3519 €) | — | 106.78 | 0.000 (n=25) | REJECTED | reliability_not_demonstrated |
| 54846483 | USDC→[uniswap_v3]→WETH→[aerodrome]→SLC→[uniswap_v3]→USDC | 35.792163 USDC | 0.388589 USDC | 0.000000 USDC | 0.006396 USDC | 0.382193 USDC (0.3516 €) | — | 106.78 | 0.000 (n=25) | REJECTED | reliability_not_demonstrated |
| 54846483 | WETH→[aerodrome]→SLC→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.016024 WETH | 0.000174 WETH | 0.000000 WETH | 0.000003 WETH | 0.000171 WETH (0.3509 €) | — | 106.78 | 0.001 (n=9) | REJECTED | reliability_not_demonstrated |
| 54846483 | USDC→[pancakeswap_v3]→WETH→[aerodrome]→SLC→[uniswap_v3]→USDC | 35.695903 USDC | 0.387545 USDC | 0.000000 USDC | 0.006396 USDC | 0.381149 USDC (0.3507 €) | — | 106.78 | 0.001 (n=9) | REJECTED | reliability_not_demonstrated |
| 54846483 | USDC→[sushiswap_v3]→WETH→[aerodrome]→SLC→[uniswap_v3]→USDC | 32.354036 USDC | 0.354903 USDC | 0.000000 USDC | 0.006734 USDC | 0.348169 USDC (0.3203 €) | — | 107.61 | 0.000 (n=25) | REJECTED | reliability_not_demonstrated |
| 54846483 | WETH→[aerodrome]→SLC→[uniswap_v3]→USDC→[sushiswap_v3]→WETH | 0.014509 WETH | 0.000159 WETH | 0.000000 WETH | 0.000003 WETH | 0.000156 WETH (0.3202 €) | — | 107.61 | 0.000 (n=25) | REJECTED | reliability_not_demonstrated |
| 54846483 | USDC→[aerodrome_slipstream]→WETH→[aerodrome]→SLC→[uniswap_v3]→USDC | 22.150892 USDC | 0.232521 USDC | 0.000000 USDC | 0.006734 USDC | 0.225787 USDC (0.2077 €) | — | 101.93 | 0.000 (n=25) | REJECTED | reliability_not_demonstrated |
| 54846483 | WETH→[aerodrome]→SLC→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.009881 WETH | 0.000104 WETH | 0.000000 WETH | 0.000003 WETH | 0.000101 WETH (0.2065 €) | — | 101.91 | 0.000 (n=25) | REJECTED | reliability_not_demonstrated |
| 54878591 | USDC→[pancakeswap_v3]→ICNT→[uniswap_v3]→USDC | 142.045523 USDC | 0.209539 USDC | 0.000000 USDC | 0.005008 USDC | 0.204531 USDC (0.1882 €) | 0.204531 USDC | 14.40 | 0.003 (n=105) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 54867973 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→BASECAT→[uniswap_v3]→USDC | 55.739894 USDC | 0.161222 USDC | 0.000000 USDC | 0.007037 USDC | 0.154185 USDC (0.1419 €) | — | 27.66 | 0.000 (n=49) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 54867973 | WETH→[uniswap_v3]→BASECAT→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.024947 WETH | 0.000072 WETH | 0.000000 WETH | 0.000003 WETH | 0.000069 WETH (0.1415 €) | — | 27.66 | 0.000 (n=49) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 54867973 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→BASECAT→[uniswap_v3]→USDC | 55.455616 USDC | 0.160479 USDC | 0.000000 USDC | 0.007037 USDC | 0.153442 USDC (0.1412 €) | — | 27.67 | 0.000 (n=59) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 54867973 | WETH→[uniswap_v3]→BASECAT→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.024819 WETH | 0.000072 WETH | 0.000000 WETH | 0.000003 WETH | 0.000069 WETH (0.1408 €) | — | 27.67 | 0.000 (n=59) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 54867973 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→BASECAT→[uniswap_v3]→USDC | 54.037924 USDC | 0.157110 USDC | 0.000000 USDC | 0.007037 USDC | 0.150073 USDC (0.1381 €) | — | 27.77 | 0.000 (n=59) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 54867973 | WETH→[uniswap_v3]→BASECAT→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.024183 WETH | 0.000070 WETH | 0.000000 WETH | 0.000003 WETH | 0.000067 WETH (0.1377 €) | — | 27.77 | 0.000 (n=59) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 54867973 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→BASECAT→[uniswap_v3]→USDC | 48.646842 USDC | 0.139022 USDC | 0.000000 USDC | 0.007037 USDC | 0.131985 USDC (0.1214 €) | — | 27.13 | 0.000 (n=59) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 54867973 | WETH→[uniswap_v3]→BASECAT→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.021757 WETH | 0.000062 WETH | 0.000000 WETH | 0.000003 WETH | 0.000059 WETH (0.1210 €) | — | 27.13 | 0.000 (n=59) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 54867973 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→BASECAT→[uniswap_v3]→USDC | 43.742544 USDC | 0.136607 USDC | 0.000000 USDC | 0.007037 USDC | 0.129570 USDC (0.1192 €) | — | 29.62 | 0.000 (n=49) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 54867973 | WETH→[uniswap_v3]→BASECAT→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.019574 WETH | 0.000061 WETH | 0.000000 WETH | 0.000003 WETH | 0.000058 WETH (0.1189 €) | — | 29.62 | 0.000 (n=49) | REJECTED | p_lower_below_threshold(0.00<0.75) |

## Fiabilité et décision
- Observations ghost : 6270 ; taux observé 0.160 ; borne inférieure crédible (0.9) 0.154 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 15.4% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ✅ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
