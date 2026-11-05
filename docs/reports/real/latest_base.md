# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-05T06:35:36+00:00 ; durée 122.93 min ; blocs 53531902 → 53535591 (3664 vus)

## Connexion
- Requêtes RPC : 39452 ; erreurs : 0 ; latence p50/p95 : 224.2/1,475.1 ms
- Rafraîchissements d'état : 3664 ; âge des données au dernier bloc : 5.63 s ; changements de frais LP observés (pools à frais dynamiques) : 4418
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 498 ; cycles déclenchés par événement : 71 ; avance médiane sur le rafraîchissement multicall : 492 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,423.15 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 500 pools, 288 jetons, 19590 routes
- Par DEX : uniswap_v3 143, aerodrome_slipstream 108, aerodrome 205, pancakeswap_v3 29, uniswap_v2 12, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 175 (rejetés 2) → 580 jetons ; pools candidats 3707 (énumérés 311, par paires 0), mesurés 503, sous le plancher de 10000.0 $ : 3 → gardés 500 (max 1500) ; prix des hubs : {'USDC': 1.0, 'USDbC': 1.0, 'DAI': 1.0, 'WETH': 2423.443645, 'cbBTC': 80372.656982, 'AERO': 0.644397}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 154,704,580 | 2,423.151729 | 53535592 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,307,865 | 0.030136 | 53535592 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,665,665 | 0.030091 | 53535592 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,274,955 | 0.000012 | 53535592 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 8,312,621 | 2,424.036020 | 53535592 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,861,896 | 111.080579 | 53535592 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,825,241 | 0.001560 | 53535592 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,396,484 | 0.030145 | 53535592 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 5,353,621 | 1.543051 | 53535592 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,449,241 | 2,424.326350 | 53535592 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,232,309 | 0.999062 | 53535592 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,676,744 | 40,648.980640 | 53535592 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 150 | 3,468,527 | 2,424.500383 | 53535592 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,747,249 | 0.030099 | 53535592 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 2,261,151 | 1,164,309.449368 | 53535592 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,862,066 | 0.006968 | 53535592 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/cbBTC | 460 | 1,824,768 | 0.000012 | 53535592 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,775,596 | 0.000000 | 53535592 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,761,628 | 0.018081 | 53535592 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,686,794 | 0.000012 | 53535592 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,641,297 | 447.244748 | 53535592 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,553,634 | 0.000012 | 53535592 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,524,438 | 1.472013 | 53535592 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | WETH/AERO | 3000 | 1,484,935 | 3,743.636916 | 53535592 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,457,174 | 0.816352 | 53535592 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,415,643 | 2,424.063631 | 53535592 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | WETH/USDC | 3000 | 1,379,802 | 2,427.043817 | 53535592 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| uniswap_v2 | WETH/USDC | 3000 | 1,379,189 | 2,422.903051 | 53535592 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,345,383 | 14,849.550148 | 53535592 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | WETH/doginme | 10000 | 1,185,704 | 37,487,996.465193 | 53535592 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | USDC/SEND | 3000 | 1,151,294 | 73.310640 | 53535592 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | DRB/WETH | 10000 | 1,149,727 | 0.000000 | 53535592 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,105,947 | 564,993.286874 | 53535592 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | WETH/VVV | 10000 | 1,089,171 | 111.863374 | 53535592 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,067,074 | 23,018,393.135731 | 53535592 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | WETH/MORPHO | 3000 | 995,547 | 1,077.424366 | 53535592 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome_slipstream | USDC/VELVET | 100 | 991,069 | 19.448416 | 53535592 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | USDC/NOCK | 3000 | 984,655 | 64.671048 | 53535592 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | USDC/cbBTC | 338 | 964,330 | 0.000012 | 53535592 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | WETH/EDEL | 7000 | 957,310 | 97,734.523569 | 53535592 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/USDC | 10000 | 957,074 | 2,419.823218 | 53535592 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | uXRP/WETH | 3000 | 918,102 | 0.000537 | 53535592 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| uniswap_v3 | USDC/VVV | 3000 | 874,103 | 0.045811 | 53535592 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | WETH/AERO | 10000 | 860,089 | 3,767.676292 | 53535592 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| pancakeswap_v3 | QUID/USDC | 100 | 833,051 | 0.062539 | 53535592 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 831,305 | 19.720463 | 53535592 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome | WETH/wstETH | 3000 | 822,601 | 0.798911 | 53535592 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 750,676 | 0.596642 | 53535592 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 740,429 | 5,066,912.856820 | 53535592 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v2 | WETH/NPC | 3000 | 740,027 | 135,465.398416 | 53535592 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome | VIRTUAL/WETH | 10000 | 732,904 | 0.000247 | 53535592 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 696,205 | 0.000008 | 53535592 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/BRETT | 2105 | 676,655 | 564,801.072364 | 53535592 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | TIG/USDC | 10000 | 670,466 | 0.568594 | 53535592 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome | WETH/bsdETH | 100 | 650,267 | 0.914439 | 53535592 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome | WETH/msETH (stable) | 500 | 645,630 | 2.484153 | 53535592 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| pancakeswap_v3 | ELSA/USDC | 100 | 604,527 | 0.100670 | 53535592 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 603,394 | 0.090726 | 53535592 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| aerodrome | cbBTC/EDGE | 7000 | 585,716 | 798,540.621232 | 53535592 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| aerodrome | WETH/DRV | 3000 | 571,435 | 6,594.227413 | 53535592 | `0xaC4e562d7C6108f971321F14238E24AE2cC398ac` |

## Recherche d'opportunités
- Cycles : 3734 ; routes examinées : 73149060 ; candidats optimisés : 213090 ; net attendu > 0 : 26 ; dernier cycle 257.5 ms
- Rejets (moteur) : {'spread_below_threshold': 72134055, 'liquidity_below_min': 800536, 'negative_expected_net': 213064, 'borrow_bound_too_small': 1315, 'cycle_budget_exhausted': 64}
- Enregistrements de la session : 213090 ; net attendu > 0 : 26 ; simulés (eth_call de la vraie tx) : 8 (ok 8, échec 0) ; étiquettes ghost N+1 : 0/8 positives
- Décisions : {'REJECTED': 213090} ; motifs de rejet : {'below_safety_margin': 18, 'negative_expected_net': 213064, 'p_lower_below_threshold': 26, 'stale_data': 2}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53533889 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 47.867526 USDC | 0.057843 USDC | 0.000000 USDC | 0.005441 USDC | 0.052402 USDC (0.0482 €) | 0.052402 USDC | 10.95 | 0.000 (n=83) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53535100 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 39.991871 USDC | 0.022053 USDC | 0.000000 USDC | 0.005441 USDC | 0.016612 USDC (0.0153 €) | 0.016612 USDC | 4.15 | 0.031 (n=268) | REJECTED | p_lower_below_threshold(0.03<0.75) |
| 53535300 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 39.001682 USDC | 0.020726 USDC | 0.000000 USDC | 0.005441 USDC | 0.015285 USDC (0.0141 €) | 0.015285 USDC | 3.92 | 0.031 (n=270) | REJECTED | p_lower_below_threshold(0.03<0.75) |
| 53533483 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 26.495646 USDC | 0.017835 USDC | 0.000000 USDC | 0.005443 USDC | 0.012392 USDC (0.0114 €) | 0.012392 USDC | 4.68 | 0.031 (n=266) | REJECTED | p_lower_below_threshold(0.03<0.75) |
| 53535217 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 25.717321 USDC | 0.016643 USDC | 0.000000 USDC | 0.005442 USDC | 0.011201 USDC (0.0103 €) | 0.011201 USDC | 4.36 | 0.031 (n=269) | REJECTED | p_lower_below_threshold(0.03<0.75) |
| 53534627 | WETH→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.041858 WETH | 0.000007 WETH | 0.000000 WETH | 0.000003 WETH | 0.000004 WETH (0.0096 €) | — | 1.03 | 0.244 (n=366) | REJECTED | below_safety_margin(4317715317567<8371687082946), p_lower_below_threshold(0.24<0.75) |
| 53534627 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→USDC | 100.118225 USDC | 0.017691 USDC | 0.000000 USDC | 0.007282 USDC | 0.010409 USDC (0.0096 €) | — | 1.04 | 0.244 (n=366) | REJECTED | below_safety_margin(10409<20023), p_lower_below_threshold(0.24<0.75) |
| 53533641 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 23.857983 USDC | 0.014443 USDC | 0.000000 USDC | 0.005442 USDC | 0.009001 USDC (0.0083 €) | 0.009001 USDC | 3.77 | 0.031 (n=267) | REJECTED | p_lower_below_threshold(0.03<0.75) |
| 53532801 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 21.020314 USDC | 0.011264 USDC | 0.000000 USDC | 0.005450 USDC | 0.005814 USDC (0.0053 €) | 0.005814 USDC | 2.77 | 0.042 (n=215) | REJECTED | p_lower_below_threshold(0.04<0.75) |
| 53533332 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 62.528905 USDC | 0.012954 USDC | 0.000000 USDC | 0.007282 USDC | 0.005672 USDC (0.0052 €) | — | 0.91 | 0.178 (n=915) | REJECTED | below_safety_margin(5672<12505), stale_data(4128ms>4000.0), p_lower_below_threshold(0.18<0.75) |
| 53534126 | WETH→[aerodrome]→USDC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH | 0.016004 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0048 €) | — | 1.34 | 0.320 (n=120) | REJECTED | below_safety_margin(2151229062593<3200882279116), p_lower_below_threshold(0.32<0.75) |
| 53534126 | USDC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH→[aerodrome]→USDC | 38.567321 USDC | 0.012138 USDC | 0.000000 USDC | 0.006956 USDC | 0.005182 USDC (0.0048 €) | — | 1.34 | 0.320 (n=120) | REJECTED | below_safety_margin(5182<7713), p_lower_below_threshold(0.32<0.75) |
| 53533332 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.000858 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0044 €) | — | 0.70 | 0.178 (n=915) | REJECTED | below_safety_margin(6<17), stale_data(4123ms>4000.0), p_lower_below_threshold(0.18<0.75) |
| 53534126 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH | 0.017304 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0042 €) | — | 1.09 | 0.178 (n=915) | REJECTED | below_safety_margin(1879458324172<3460767269199), p_lower_below_threshold(0.18<0.75) |
| 53534126 | USDC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 41.569840 USDC | 0.011816 USDC | 0.000000 USDC | 0.007290 USDC | 0.004526 USDC (0.0042 €) | — | 1.09 | 0.178 (n=915) | REJECTED | below_safety_margin(4526<8313), p_lower_below_threshold(0.18<0.75) |
| 53532510 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 19.484318 USDC | 0.009709 USDC | 0.000000 USDC | 0.005500 USDC | 0.004209 USDC (0.0039 €) | 0.004209 USDC | 2.16 | 0.043 (n=214) | REJECTED | p_lower_below_threshold(0.04<0.75) |
| 53533562 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 17.226311 USDC | 0.007590 USDC | 0.000000 USDC | 0.005442 USDC | 0.002148 USDC (0.0020 €) | — | 1.25 | 0.042 (n=216) | REJECTED | below_safety_margin(2148<3445), p_lower_below_threshold(0.04<0.75) |
| 53534175 | USDC→[uniswap_v3]→ELSA→[pancakeswap_v3]→USDC | 18.498351 USDC | 0.007294 USDC | 0.000000 USDC | 0.005442 USDC | 0.001852 USDC (0.0017 €) | — | 1.00 | 0.042 (n=216) | REJECTED | below_safety_margin(1852<3699), p_lower_below_threshold(0.04<0.75) |
| 53534126 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH | 0.015292 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0017 €) | — | 0.50 | 0.178 (n=915) | REJECTED | below_safety_margin(757299529408<3058378555135), p_lower_below_threshold(0.18<0.75) |
| 53534126 | USDC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 36.719446 USDC | 0.009102 USDC | 0.000000 USDC | 0.007290 USDC | 0.001812 USDC (0.0017 €) | — | 0.49 | 0.178 (n=915) | REJECTED | below_safety_margin(1812<7343), p_lower_below_threshold(0.18<0.75) |
| 53532434 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 16.378652 USDC | 0.006727 USDC | 0.000000 USDC | 0.005522 USDC | 0.001205 USDC (0.0011 €) | — | 0.74 | 0.043 (n=214) | REJECTED | below_safety_margin(1205<3275), p_lower_below_threshold(0.04<0.75) |
| 53534126 | WETH→[sushiswap_v3]→USDC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH | 0.012377 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0007 €) | — | 0.27 | 0.178 (n=915) | REJECTED | below_safety_margin(335316247102<2475306896460), p_lower_below_threshold(0.18<0.75) |
| 53534126 | USDC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH→[sushiswap_v3]→USDC | 29.889677 USDC | 0.008082 USDC | 0.000000 USDC | 0.007290 USDC | 0.000792 USDC (0.0007 €) | — | 0.26 | 0.178 (n=915) | REJECTED | below_safety_margin(792<5977), p_lower_below_threshold(0.18<0.75) |
| 53534126 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH | 0.013766 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0000 €) | — | 0.01 | 0.178 (n=915) | REJECTED | below_safety_margin(17793057255<2753230875289), p_lower_below_threshold(0.18<0.75) |
| 53534126 | USDC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 32.957345 USDC | 0.007314 USDC | 0.000000 USDC | 0.007290 USDC | 0.000024 USDC (0.0000 €) | — | 0.01 | 0.178 (n=915) | REJECTED | below_safety_margin(24<6591), p_lower_below_threshold(0.18<0.75) |

## Fiabilité et décision
- Observations ghost : 5314 ; taux observé 0.161 ; borne inférieure crédible (0.9) 0.155 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 15.5% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
