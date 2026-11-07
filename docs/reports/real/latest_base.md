# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-07T00:41:13+00:00 ; durée 266.96 min ; blocs 54028370 → 54108397 (16028 vus)

## Connexion
- Requêtes RPC : 194211 ; erreurs : 0 ; latence p50/p95 : 194.7/1,519.8 ms
- Rafraîchissements d'état : 16028 ; âge des données au dernier bloc : 8.07 s ; changements de frais LP observés (pools à frais dynamiques) : 4673
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 10590 ; cycles déclenchés par événement : 4423 ; avance médiane sur le rafraîchissement multicall : 319 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,239.69 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 482 pools, 282 jetons, 17936 routes
- Par DEX : uniswap_v3 137, aerodrome_slipstream 103, aerodrome 198, pancakeswap_v3 29, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 172 (rejetés 2) → 577 jetons ; pools candidats 3742 (énumérés 299, par paires 0), mesurés 485, sous le plancher de 10000.0 $ : 3 → gardés 482 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'DAI': 1.0, 'USDC': 1.0, 'WETH': 2228.731074, 'cbBTC': 75812.648558, 'AERO': 0.606832}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 145,924,876 | 2,239.686901 | 54108422 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,776,369 | 0.029525 | 54108422 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,311,459 | 0.000013 | 54108422 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,165,831 | 0.029484 | 54108422 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 8,015,209 | 2,238.857213 | 54108422 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,384,809 | 107.489316 | 54108422 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,430,573 | 0.001556 | 54108422 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 4,906,264 | 1.632337 | 54108422 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,761,849 | 0.029519 | 54108422 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,229,548 | 2,239.213954 | 54108422 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,998,043 | 0.998508 | 54108422 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,315,551 | 42,704.973270 | 54108422 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 150 | 3,203,647 | 2,239.480943 | 54108422 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,560,748 | 0.029497 | 54108422 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 2,087,534 | 1,166,818.518415 | 54108422 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,737,690 | 0.006959 | 54108422 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/cbBTC | 400 | 1,736,031 | 0.000013 | 54108422 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,661,642 | 0.000000 | 54108422 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,641,521 | 0.000013 | 54108422 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | XDP/USDC | 100 | 1,621,847 | 0.016213 | 54108422 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,545,442 | 1.431595 | 54108422 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,538,812 | 0.000013 | 54108422 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,534,527 | 431.452528 | 54108422 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,460,379 | 0.819350 | 54108422 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,396,693 | 3,654.007791 | 54108422 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v2 | WETH/USDC | 3000 | 1,326,252 | 2,240.969448 | 54108422 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome | WETH/USDC | 3000 | 1,324,349 | 2,245.984215 | 54108422 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,278,468 | 14,626.103431 | 54108422 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,161,300 | 2,238.928209 | 54108422 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,122,373 | 77.137363 | 54108422 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,102,770 | 36,690,076.935376 | 54108422 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/VVV | 10000 | 1,048,269 | 106.771363 | 54108422 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,031,204 | 553,637.815104 | 54108422 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,019,481 | 0.000000 | 54108422 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,001,752 | 22,508,235.864785 | 54108422 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/VELVET | 100 | 979,352 | 20.137169 | 54108422 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/MORPHO | 3000 | 942,518 | 1,060.779497 | 54108422 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/USDC | 10000 | 936,194 | 2,228.788696 | 54108422 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome_slipstream | USDC/cbBTC | 330 | 926,272 | 0.000013 | 54108422 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/NOCK | 3000 | 923,515 | 73.471634 | 54108422 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome | WETH/EDEL | 7000 | 893,843 | 95,774.681852 | 54108422 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | uXRP/WETH | 3000 | 838,316 | 0.000526 | 54108422 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| uniswap_v3 | USDC/VVV | 3000 | 809,043 | 0.047997 | 54108422 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | WETH/AERO | 10000 | 803,929 | 3,646.819515 | 54108422 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 803,431 | 20.771044 | 54108422 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 798,847 | 0.057172 | 54108422 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 759,805 | 0.799699 | 54108422 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 721,736 | 0.568261 | 54108422 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 700,768 | 4,833,790.398069 | 54108422 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome | VIRTUAL/WETH | 10000 | 688,125 | 0.000256 | 54108422 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | TIG/USDC | 10000 | 668,289 | 0.559859 | 54108422 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/NPC | 3000 | 661,686 | 144,820.630553 | 54108422 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 659,499 | 0.000008 | 54108422 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 632,541 | 556,888.048077 | 54108422 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome | WETH/msETH (stable) | 500 | 588,692 | 2.472072 | 54108422 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | FLOCK/USDC | 3000 | 584,460 | 0.040517 | 54108422 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| uniswap_v3 | USDC/USDT | 100 | 557,781 | 1.001188 | 54108422 | `0xD56da2B74bA826f19015E6B7Dd9Dae1903E85DA1` |
| pancakeswap_v3 | ELSA/USDC | 100 | 532,976 | 0.080371 | 54108422 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| aerodrome | cbBTC/EDGE | 7000 | 532,457 | 857,533.693647 | 54108422 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 527,832 | 1,061.083078 | 54108422 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |

## Recherche d'opportunités
- Cycles : 20450 ; routes examinées : 366791200 ; candidats optimisés : 1028637 ; net attendu > 0 : 303 ; dernier cycle 122.4 ms
- Rejets (moteur) : {'spread_below_threshold': 361068736, 'liquidity_below_min': 4653152, 'negative_expected_net': 1028334, 'borrow_bound_too_small': 20442, 'pool_quarantined': 19012, 'cycle_budget_exhausted': 1221}
- Enregistrements de la session : 1028637 ; net attendu > 0 : 303 ; simulés (eth_call de la vraie tx) : 36 (ok 13, échec 23) ; étiquettes ghost N+1 : 8/20 positives
- Décisions : {'REJECTED': 1028637} ; motifs de rejet : {'below_safety_margin': 203, 'negative_expected_net': 1028334, 'p_lower_below_threshold': 274, 'price_impact': 15, 'reliability_not_demonstrated': 29, 'simulation_failed': 23, 'stale_data': 27}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 54060684 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 837.885496 USDC | 0.111051 USDC | 0.000000 USDC | 0.005054 USDC | 0.105997 USDC (0.0975 €) | — | 1.27 | 0.047 (n=247) | REJECTED | below_safety_margin(105997<167577), p_lower_below_threshold(0.05<0.75) |
| 54060684 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.374447 WETH | 0.000050 WETH | 0.000000 WETH | 0.000002 WETH | 0.000047 WETH (0.0972 €) | — | 1.26 | 0.047 (n=247) | REJECTED | below_safety_margin(47277268623202<74889389706557), p_lower_below_threshold(0.05<0.75) |
| 54060684 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 757.927748 USDC | 0.070574 USDC | 0.000000 USDC | 0.006764 USDC | 0.063810 USDC (0.0587 €) | — | 0.84 | 0.029 (n=28) | REJECTED | below_safety_margin(63810<151585), reliability_not_demonstrated |
| 54060684 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.008755 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0585 €) | — | 0.96 | 0.029 (n=28) | REJECTED | below_safety_margin(84<175), reliability_not_demonstrated |
| 54060684 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.329385 WETH | 0.000031 WETH | 0.000000 WETH | 0.000003 WETH | 0.000028 WETH (0.0581 €) | — | 0.86 | 0.029 (n=28) | REJECTED | below_safety_margin(28267304274076<65877091333329), reliability_not_demonstrated |
| 54057958 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 68.807723 USDC | 0.056511 USDC | 0.000000 USDC | 0.005004 USDC | 0.051507 USDC (0.0474 €) | — | 7.49 | 0.026 (n=319) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.03<0.75) |
| 54102295 | USDC→[pancakeswap_v3]→VIRTUAL→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 119.155898 USDC | 0.054005 USDC | 0.000000 USDC | 0.006730 USDC | 0.047275 USDC (0.0435 €) | — | 3.97 | 0.156 (n=794) | REJECTED | p_lower_below_threshold(0.16<0.75) |
| 54102295 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→VIRTUAL→[uniswap_v3]→WETH | 0.053250 WETH | 0.000024 WETH | 0.000000 WETH | 0.000003 WETH | 0.000021 WETH (0.0435 €) | 0.000021 WETH | 3.96 | 0.156 (n=794) | REJECTED | p_lower_below_threshold(0.16<0.75) |
| 54102295 | USDC→[pancakeswap_v3]→VIRTUAL→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 116.019900 USDC | 0.050157 USDC | 0.000000 USDC | 0.006730 USDC | 0.043427 USDC (0.0400 €) | — | 3.74 | 0.156 (n=794) | REJECTED | p_lower_below_threshold(0.16<0.75) |
| 54102295 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→VIRTUAL→[uniswap_v3]→WETH | 0.051966 WETH | 0.000022 WETH | 0.000000 WETH | 0.000003 WETH | 0.000019 WETH (0.0399 €) | 0.000019 WETH | 3.73 | 0.156 (n=794) | REJECTED | p_lower_below_threshold(0.16<0.75) |
| 54102295 | USDC→[pancakeswap_v3]→VIRTUAL→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 109.969871 USDC | 0.048524 USDC | 0.000000 USDC | 0.006730 USDC | 0.041794 USDC (0.0385 €) | — | 3.80 | 0.156 (n=794) | REJECTED | p_lower_below_threshold(0.16<0.75) |
| 54102295 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→VIRTUAL→[uniswap_v3]→WETH | 0.049209 WETH | 0.000022 WETH | 0.000000 WETH | 0.000003 WETH | 0.000019 WETH (0.0384 €) | 0.000019 WETH | 3.79 | 0.156 (n=794) | REJECTED | p_lower_below_threshold(0.16<0.75) |
| 54060684 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 304.872182 USDC | 0.038933 USDC | 0.000000 USDC | 0.005395 USDC | 0.033538 USDC (0.0309 €) | — | 1.10 | 0.053 (n=82) | REJECTED | below_safety_margin(33538<60974), p_lower_below_threshold(0.05<0.75) |
| 54060684 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.136291 WETH | 0.000017 WETH | 0.000000 WETH | 0.000002 WETH | 0.000015 WETH (0.0308 €) | — | 1.10 | 0.053 (n=82) | REJECTED | below_safety_margin(14951957098203<27258137402606), p_lower_below_threshold(0.05<0.75) |
| 54096299 | WETH→[pancakeswap_v3]→USDC→[aerodrome]→VIRTUAL→[uniswap_v2]→WETH | 0.017305 WETH | 0.000016 WETH | 0.000000 WETH | 0.000003 WETH | 0.000013 WETH (0.0275 €) | 0.000013 WETH | 7.72 | 0.121 (n=18) | REJECTED | reliability_not_demonstrated |
| 54096299 | USDC→[aerodrome]→VIRTUAL→[uniswap_v2]→WETH→[pancakeswap_v3]→USDC | 38.670657 USDC | 0.035595 USDC | 0.000000 USDC | 0.005725 USDC | 0.029870 USDC (0.0275 €) | — | 7.72 | 0.121 (n=18) | REJECTED | reliability_not_demonstrated |
| 54096299 | WETH→[uniswap_v3]→USDC→[aerodrome]→VIRTUAL→[uniswap_v2]→WETH | 0.016393 WETH | 0.000014 WETH | 0.000000 WETH | 0.000003 WETH | 0.000012 WETH (0.0245 €) | 0.000012 WETH | 7.26 | 0.083 (n=26) | REJECTED | reliability_not_demonstrated |
| 54096299 | USDC→[aerodrome]→VIRTUAL→[uniswap_v2]→WETH→[uniswap_v3]→USDC | 36.403647 USDC | 0.032341 USDC | 0.000000 USDC | 0.005725 USDC | 0.026616 USDC (0.0245 €) | — | 7.31 | 0.083 (n=26) | REJECTED | reliability_not_demonstrated |
| 54096299 | WETH→[aerodrome_slipstream]→USDC→[aerodrome]→VIRTUAL→[uniswap_v2]→WETH | 0.015521 WETH | 0.000013 WETH | 0.000000 WETH | 0.000003 WETH | 0.000010 WETH (0.0211 €) | 0.000010 WETH | 6.58 | 0.083 (n=26) | REJECTED | reliability_not_demonstrated |
| 54096299 | USDC→[aerodrome]→VIRTUAL→[uniswap_v2]→WETH→[aerodrome_slipstream]→USDC | 34.425277 USDC | 0.028562 USDC | 0.000000 USDC | 0.005725 USDC | 0.022837 USDC (0.0210 €) | — | 6.63 | 0.083 (n=26) | REJECTED | reliability_not_demonstrated |
| 54096299 | WETH→[aerodrome_slipstream]→USDC→[aerodrome]→VIRTUAL→[uniswap_v2]→WETH | 0.013760 WETH | 0.000012 WETH | 0.000000 WETH | 0.000003 WETH | 0.000010 WETH (0.0202 €) | — | 7.12 | 0.083 (n=26) | REJECTED | reliability_not_demonstrated |
| 54096299 | USDC→[aerodrome]→VIRTUAL→[uniswap_v2]→WETH→[aerodrome_slipstream]→USDC | 30.674307 USDC | 0.027613 USDC | 0.000000 USDC | 0.005725 USDC | 0.021888 USDC (0.0201 €) | — | 7.14 | 0.083 (n=26) | REJECTED | reliability_not_demonstrated |
| 54096299 | WETH→[pancakeswap_v3]→USDC→[aerodrome]→VIRTUAL→[aerodrome_slipstream]→WETH | 0.013867 WETH | 0.000011 WETH | 0.000000 WETH | 0.000003 WETH | 0.000008 WETH (0.0174 €) | — | 6.09 | 0.279 (n=167) | REJECTED | p_lower_below_threshold(0.28<0.75) |
| 54096299 | USDC→[aerodrome]→VIRTUAL→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 30.884656 USDC | 0.025642 USDC | 0.000000 USDC | 0.006761 USDC | 0.018881 USDC (0.0174 €) | — | 6.11 | 0.279 (n=167) | REJECTED | p_lower_below_threshold(0.28<0.75) |
| 54096299 | WETH→[aerodrome]→USDC→[aerodrome]→VIRTUAL→[uniswap_v2]→WETH | 0.013459 WETH | 0.000010 WETH | 0.000000 WETH | 0.000002 WETH | 0.000008 WETH (0.0161 €) | — | 5.80 | — (n=0) | REJECTED | reliability_not_demonstrated |

## Fiabilité et décision
- Observations ghost : 5917 ; taux observé 0.161 ; borne inférieure crédible (0.9) 0.155 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 15.5% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
