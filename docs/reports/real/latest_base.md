# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-05T07:00:18+00:00 ; durée 147.64 min ; blocs 53531902 → 53536334 (4368 vus)

## Connexion
- Requêtes RPC : 47264 ; erreurs : 0 ; latence p50/p95 : 284.1/1,401.1 ms
- Rafraîchissements d'état : 4369 ; âge des données au dernier bloc : 5.73 s ; changements de frais LP observés (pools à frais dynamiques) : 5256
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 1711 ; cycles déclenchés par événement : 263 ; avance médiane sur le rafraîchissement multicall : 1,165 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,423.29 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 500 pools, 288 jetons, 19590 routes
- Par DEX : uniswap_v3 143, aerodrome_slipstream 108, aerodrome 205, pancakeswap_v3 29, uniswap_v2 12, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 175 (rejetés 2) → 580 jetons ; pools candidats 3707 (énumérés 311, par paires 0), mesurés 503, sous le plancher de 10000.0 $ : 3 → gardés 500 (max 1500) ; prix des hubs : {'USDC': 1.0, 'USDbC': 1.0, 'DAI': 1.0, 'WETH': 2423.443645, 'cbBTC': 80372.656982, 'AERO': 0.644397}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 154,815,673 | 2,423.285724 | 53536332 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,307,900 | 0.030139 | 53536332 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,666,042 | 0.030091 | 53536332 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,275,165 | 0.000012 | 53536332 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 8,312,257 | 2,427.396969 | 53536333 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,886,797 | 110.393005 | 53536332 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,828,050 | 0.001561 | 53536332 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,397,363 | 0.030128 | 53536333 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 5,360,518 | 1.538336 | 53536332 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,452,224 | 2,426.471791 | 53536333 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,232,158 | 0.999062 | 53536332 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,676,624 | 40,656.113753 | 53536332 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 624 | 3,468,682 | 2,426.603174 | 53536334 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,747,295 | 0.030099 | 53536332 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 2,261,276 | 1,164,309.449368 | 53536332 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,897,021 | 0.007128 | 53536332 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/cbBTC | 400 | 1,824,728 | 0.000012 | 53536332 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,760,484 | 0.000000 | 53536332 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,760,319 | 0.018097 | 53536334 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,686,706 | 0.000012 | 53536334 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,641,679 | 446.989733 | 53536332 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,553,611 | 0.000012 | 53536332 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,524,437 | 1.472014 | 53536332 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | WETH/AERO | 3000 | 1,487,797 | 3,732.879045 | 53536332 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,457,251 | 0.816270 | 53536332 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,415,710 | 2,427.377050 | 53536333 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | WETH/USDC | 3000 | 1,379,841 | 2,428.912232 | 53536332 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| uniswap_v2 | WETH/USDC | 3000 | 1,379,227 | 2,423.141514 | 53536332 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,345,717 | 14,842.258900 | 53536332 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | WETH/doginme | 10000 | 1,185,667 | 37,487,996.465193 | 53536332 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | USDC/SEND | 3000 | 1,151,294 | 73.310640 | 53536332 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | DRB/WETH | 10000 | 1,149,792 | 0.000000 | 53536332 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,106,007 | 564,995.633578 | 53536332 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | WETH/VVV | 10000 | 1,094,927 | 111.165747 | 53536333 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,067,133 | 23,018,393.135731 | 53536332 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | WETH/MORPHO | 3000 | 1,001,785 | 1,069.726560 | 53536332 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome_slipstream | USDC/VELVET | 100 | 990,700 | 19.469451 | 53536332 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | USDC/NOCK | 3000 | 981,889 | 65.036031 | 53536332 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | USDC/cbBTC | 330 | 964,316 | 0.000012 | 53536332 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | WETH/EDEL | 7000 | 957,561 | 97,694.064037 | 53536332 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/USDC | 10000 | 957,084 | 2,419.823218 | 53536332 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | uXRP/WETH | 3000 | 918,152 | 0.000537 | 53536332 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| uniswap_v3 | USDC/VVV | 3000 | 878,333 | 0.045457 | 53536332 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | WETH/AERO | 10000 | 861,433 | 3,762.753900 | 53536332 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 831,305 | 19.720463 | 53536332 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome | WETH/wstETH | 3000 | 822,646 | 0.798911 | 53536332 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| pancakeswap_v3 | QUID/USDC | 100 | 820,954 | 0.060604 | 53536332 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 750,722 | 0.599589 | 53536332 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 740,504 | 5,066,442.643478 | 53536332 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v2 | WETH/NPC | 3000 | 740,068 | 135,465.398416 | 53536332 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome | VIRTUAL/WETH | 10000 | 732,945 | 0.000247 | 53536332 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 697,413 | 0.000008 | 53536332 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/BRETT | 2093 | 676,694 | 564,988.518795 | 53536332 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | TIG/USDC | 10000 | 670,466 | 0.568594 | 53536332 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome | WETH/bsdETH | 100 | 650,303 | 0.914439 | 53536332 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome | WETH/msETH (stable) | 500 | 645,666 | 2.484153 | 53536332 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 602,795 | 0.090588 | 53536332 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| pancakeswap_v3 | ELSA/USDC | 100 | 599,516 | 0.099255 | 53536333 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| aerodrome | cbBTC/EDGE | 7000 | 581,681 | 807,611.983209 | 53536334 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| uniswap_v3 | FLOCK/USDC | 3000 | 571,337 | 0.039214 | 53536332 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |

## Recherche d'opportunités
- Cycles : 4631 ; routes examinées : 90721290 ; candidats optimisés : 250648 ; net attendu > 0 : 36 ; dernier cycle 314.5 ms
- Rejets (moteur) : {'spread_below_threshold': 89529734, 'liquidity_below_min': 938599, 'negative_expected_net': 250612, 'borrow_bound_too_small': 2212, 'cycle_budget_exhausted': 97}
- Enregistrements de la session : 250648 ; net attendu > 0 : 36 ; simulés (eth_call de la vraie tx) : 10 (ok 9, échec 1) ; étiquettes ghost N+1 : 0/9 positives
- Décisions : {'REJECTED': 250648} ; motifs de rejet : {'below_safety_margin': 26, 'negative_expected_net': 250612, 'p_lower_below_threshold': 36, 'simulation_failed': 1, 'stale_data': 2}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53533889 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 47.867526 USDC | 0.057843 USDC | 0.000000 USDC | 0.005441 USDC | 0.052402 USDC (0.0482 €) | 0.052402 USDC | 10.95 | 0.000 (n=83) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53536005 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 42.543900 USDC | 0.024327 USDC | 0.000000 USDC | 0.005441 USDC | 0.018886 USDC (0.0174 €) | 0.018886 USDC | 4.44 | 0.031 (n=271) | REJECTED | p_lower_below_threshold(0.03<0.75) |
| 53535100 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 39.991871 USDC | 0.022053 USDC | 0.000000 USDC | 0.005441 USDC | 0.016612 USDC (0.0153 €) | 0.016612 USDC | 4.15 | 0.031 (n=268) | REJECTED | p_lower_below_threshold(0.03<0.75) |
| 53535300 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 39.001682 USDC | 0.020726 USDC | 0.000000 USDC | 0.005441 USDC | 0.015285 USDC (0.0141 €) | 0.015285 USDC | 3.92 | 0.031 (n=270) | REJECTED | p_lower_below_threshold(0.03<0.75) |
| 53533483 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 26.495646 USDC | 0.017835 USDC | 0.000000 USDC | 0.005443 USDC | 0.012392 USDC (0.0114 €) | 0.012392 USDC | 4.68 | 0.031 (n=266) | REJECTED | p_lower_below_threshold(0.03<0.75) |
| 53535217 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 25.717321 USDC | 0.016643 USDC | 0.000000 USDC | 0.005442 USDC | 0.011201 USDC (0.0103 €) | 0.011201 USDC | 4.36 | 0.031 (n=269) | REJECTED | p_lower_below_threshold(0.03<0.75) |
| 53534627 | WETH→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.041858 WETH | 0.000007 WETH | 0.000000 WETH | 0.000003 WETH | 0.000004 WETH (0.0096 €) | — | 1.03 | 0.244 (n=366) | REJECTED | below_safety_margin(4317715317567<8371687082946), p_lower_below_threshold(0.24<0.75) |
| 53534627 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→USDC | 100.118225 USDC | 0.017691 USDC | 0.000000 USDC | 0.007282 USDC | 0.010409 USDC (0.0096 €) | — | 1.04 | 0.244 (n=366) | REJECTED | below_safety_margin(10409<20023), p_lower_below_threshold(0.24<0.75) |
| 53533641 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 23.857983 USDC | 0.014443 USDC | 0.000000 USDC | 0.005442 USDC | 0.009001 USDC (0.0083 €) | 0.009001 USDC | 3.77 | 0.031 (n=267) | REJECTED | p_lower_below_threshold(0.03<0.75) |
| 53532801 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 21.020314 USDC | 0.011264 USDC | 0.000000 USDC | 0.005450 USDC | 0.005814 USDC (0.0053 €) | 0.005814 USDC | 2.77 | 0.042 (n=215) | REJECTED | p_lower_below_threshold(0.04<0.75) |
| 53536332 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 20.891642 USDC | 0.011230 USDC | 0.000000 USDC | 0.005442 USDC | 0.005788 USDC (0.0053 €) | — | 2.77 | 0.042 (n=216) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.04<0.75) |
| 53533332 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 62.528905 USDC | 0.012954 USDC | 0.000000 USDC | 0.007282 USDC | 0.005672 USDC (0.0052 €) | — | 0.91 | 0.178 (n=915) | REJECTED | below_safety_margin(5672<12505), stale_data(4128ms>4000.0), p_lower_below_threshold(0.18<0.75) |
| 53534126 | WETH→[aerodrome]→USDC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH | 0.016004 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0048 €) | — | 1.34 | 0.320 (n=120) | REJECTED | below_safety_margin(2151229062593<3200882279116), p_lower_below_threshold(0.32<0.75) |
| 53534126 | USDC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH→[aerodrome]→USDC | 38.567321 USDC | 0.012138 USDC | 0.000000 USDC | 0.006956 USDC | 0.005182 USDC (0.0048 €) | — | 1.34 | 0.320 (n=120) | REJECTED | below_safety_margin(5182<7713), p_lower_below_threshold(0.32<0.75) |
| 53533332 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.000858 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0044 €) | — | 0.70 | 0.178 (n=915) | REJECTED | below_safety_margin(6<17), stale_data(4123ms>4000.0), p_lower_below_threshold(0.18<0.75) |
| 53534126 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH | 0.017304 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0042 €) | — | 1.09 | 0.178 (n=915) | REJECTED | below_safety_margin(1879458324172<3460767269199), p_lower_below_threshold(0.18<0.75) |
| 53534126 | USDC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 41.569840 USDC | 0.011816 USDC | 0.000000 USDC | 0.007290 USDC | 0.004526 USDC (0.0042 €) | — | 1.09 | 0.178 (n=915) | REJECTED | below_safety_margin(4526<8313), p_lower_below_threshold(0.18<0.75) |
| 53532510 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 19.484318 USDC | 0.009709 USDC | 0.000000 USDC | 0.005500 USDC | 0.004209 USDC (0.0039 €) | 0.004209 USDC | 2.16 | 0.043 (n=214) | REJECTED | p_lower_below_threshold(0.04<0.75) |
| 53536331 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 190.404532 USDC | 0.007818 USDC | 0.000000 USDC | 0.005442 USDC | 0.002376 USDC (0.0022 €) | — | 0.12 | 0.042 (n=216) | REJECTED | below_safety_margin(2376<38080), p_lower_below_threshold(0.04<0.75) |
| 53536331 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 190.404532 USDC | 0.007818 USDC | 0.000000 USDC | 0.005442 USDC | 0.002376 USDC (0.0022 €) | — | 0.12 | 0.042 (n=216) | REJECTED | below_safety_margin(2376<38080), p_lower_below_threshold(0.04<0.75) |
| 53536330 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 190.404532 USDC | 0.007818 USDC | 0.000000 USDC | 0.005442 USDC | 0.002376 USDC (0.0022 €) | — | 0.12 | 0.042 (n=216) | REJECTED | below_safety_margin(2376<38080), p_lower_below_threshold(0.04<0.75) |
| 53536332 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 190.404532 USDC | 0.007818 USDC | 0.000000 USDC | 0.005442 USDC | 0.002376 USDC (0.0022 €) | — | 0.12 | 0.042 (n=216) | REJECTED | below_safety_margin(2376<38080), p_lower_below_threshold(0.04<0.75) |
| 53536331 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.079131 WETH | 0.000003 WETH | 0.000000 WETH | 0.000002 WETH | 0.000001 WETH (0.0022 €) | — | 0.12 | 0.042 (n=216) | REJECTED | below_safety_margin(975846584796<15826255829830), p_lower_below_threshold(0.04<0.75) |
| 53536331 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.079131 WETH | 0.000003 WETH | 0.000000 WETH | 0.000002 WETH | 0.000001 WETH (0.0022 €) | — | 0.12 | 0.042 (n=216) | REJECTED | below_safety_margin(975846584796<15826255829830), p_lower_below_threshold(0.04<0.75) |
| 53536330 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.079131 WETH | 0.000003 WETH | 0.000000 WETH | 0.000002 WETH | 0.000001 WETH (0.0022 €) | — | 0.12 | 0.042 (n=216) | REJECTED | below_safety_margin(975791613542<15826255829830), p_lower_below_threshold(0.04<0.75) |

## Fiabilité et décision
- Observations ghost : 5315 ; taux observé 0.161 ; borne inférieure crédible (0.9) 0.155 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 15.5% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
