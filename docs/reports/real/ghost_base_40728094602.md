# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-28T20:33:30+00:00 ; durée 227.93 min ; blocs 53208289 → 53215128 (6323 vus)

## Connexion
- Requêtes RPC : 73019 ; erreurs : 200 ; latence p50/p95 : 319.7/1,948.4 ms
- Rafraîchissements d'état : 6324 ; âge des données au dernier bloc : 1.84 s ; changements de frais LP observés (pools à frais dynamiques) : 14640
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 46058 ; cycles déclenchés par événement : 2058 ; avance médiane sur le rafraîchissement multicall : 1,715 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,356.02 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 517 pools, 298 jetons, 19028 routes
- Par DEX : uniswap_v3 144, aerodrome_slipstream 121, aerodrome 210, pancakeswap_v3 28, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 183 (rejetés 2) → 588 jetons ; pools candidats 3758 (énumérés 330, par paires 0), mesurés 519, sous le plancher de 10000.0 $ : 2 → gardés 517 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDC': 1.0, 'USDbC': 1.0, 'WETH': 2331.23448, 'cbBTC': 80382.611332, 'AERO': 0.701638}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 158,369,630 | 2,356.023191 | 53215128 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,628,859 | 0.029005 | 53215128 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,912,239 | 0.000012 | 53215128 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,510,537 | 0.029065 | 53215128 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 8,439,006 | 2,354.244942 | 53215128 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 8,264,052 | 98.491894 | 53215128 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,079,904 | 0.001645 | 53215128 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 6,723,731 | 1.431869 | 53215128 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,843,352 | 0.029014 | 53215128 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/USDC | 150 | 4,845,481 | 2,354.885235 | 53215128 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,446,491 | 2,355.017340 | 53215128 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,277,615 | 0.998802 | 53215128 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,660,989 | 38,761.656170 | 53215128 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2545 | 2,955,269 | 0.029053 | 53215128 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2763 | 2,524,101 | 98.517753 | 53215128 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | WETH/FAI | 10000 | 2,151,034 | 1,216,280.415131 | 53215128 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 472 | 2,124,529 | 0.000012 | 53215128 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome | WETH/USDC | 3000 | 1,861,428 | 2,356.971016 | 53215128 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| uniswap_v3 | XDP/USDC | 100 | 1,826,176 | 0.018742 | 53215128 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,794,849 | 399.598930 | 53215128 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,774,632 | 0.000000 | 53215128 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,723,087 | 0.000012 | 53215128 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,694,402 | 0.000012 | 53215128 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | USDC/cbBTC | 342 | 1,614,160 | 0.000012 | 53215128 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,514,132 | 1.588195 | 53215128 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,496,341 | 0.005701 | 53215128 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v3 | WETH/AERO | 3000 | 1,462,821 | 3,366.289674 | 53215128 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,460,131 | 0.826609 | 53215128 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,397,510 | 13,757.853676 | 53215128 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,257,050 | 0.000267 | 53215128 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,252,531 | 2,354.241407 | 53215128 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,193,492 | 68.218702 | 53215128 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome | VIRTUAL/WETH | 10000 | 1,162,848 | 0.000266 | 53215128 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | WETH/doginme | 10000 | 1,161,614 | 36,610,175.590815 | 53215128 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | WETH/WELL | 10000 | 1,158,343 | 1,084,801.468908 | 53215128 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,128,323 | 493,782.415165 | 53215128 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,127,592 | 0.000000 | 53215128 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,085,190 | 21,137,377.203264 | 53215128 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome | WETH/AERO | 10000 | 1,076,391 | 3,350.985819 | 53215128 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | WETH/EDEL | 7000 | 1,074,920 | 73,393.391775 | 53215128 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,055,669 | 16.323283 | 53215128 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v2 | WETH/USDC | 3000 | 1,033,561 | 2,355.245294 | 53215128 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome | USDC/NOCK | 3000 | 1,029,196 | 59.099193 | 53215128 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/VVV | 10000 | 1,000,768 | 97.805503 | 53215128 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | USDC/VVV | 3000 | 995,664 | 0.041854 | 53215128 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/USDC | 10000 | 941,841 | 2,366.107395 | 53215128 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 933,597 | 1,057.803119 | 53215128 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | uXRP/WETH | 3000 | 909,795 | 0.000559 | 53215128 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | USDC/SAPIEN | 4530 | 882,207 | 17.880387 | 53215128 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome | WETH/msETH (stable) | 500 | 877,877 | 2.334551 | 53215128 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 855,914 | 17.381972 | 53215128 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| pancakeswap_v3 | QUID/USDC | 100 | 811,765 | 0.059207 | 53215128 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 797,792 | 0.802973 | 53215128 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 756,731 | 0.000009 | 53215128 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 753,571 | 0.627518 | 53215128 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 752,700 | 4,625,696.524836 | 53215128 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v2 | WETH/NPC | 3000 | 714,278 | 137,021.669101 | 53215128 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | WETH/BRETT | 2093 | 705,308 | 492,268.967438 | 53215128 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 671,256 | 0.107961 | 53215128 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| uniswap_v3 | TIG/USDC | 10000 | 667,893 | 0.561911 | 53215128 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |

## Recherche d'opportunités
- Cycles : 8381 ; routes examinées : 159473668 ; candidats optimisés : 577463 ; net attendu > 0 : 1083 ; dernier cycle 408.7 ms
- Rejets (moteur) : {'spread_below_threshold': 156593747, 'liquidity_below_min': 2255273, 'negative_expected_net': 576380, 'pool_quarantined': 31472, 'borrow_bound_too_small': 8366, 'cycle_budget_exhausted': 7345, 'no_price_reference': 2}
- Enregistrements de la session : 577463 ; net attendu > 0 : 1083 ; simulés (eth_call de la vraie tx) : 69 (ok 38, échec 31) ; étiquettes ghost N+1 : 19/58 positives
- Décisions : {'REJECTED': 577463} ; motifs de rejet : {'below_safety_margin': 898, 'negative_expected_net': 576380, 'p_lower_below_threshold': 987, 'reliability_not_demonstrated': 96, 'sim_below_estimate': 8, 'simulated_net_nonpositive': 6, 'simulation_failed': 31, 'stale_data': 171}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53211925 | cbBTC→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.031209 cbBTC | 0.000005 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000004 cbBTC (0.3337 €) | — | 1.43 | 0.120 (n=419) | REJECTED | below_safety_margin(447<624), p_lower_below_threshold(0.12<0.75) |
| 53211925 | WETH→[pancakeswap_v3]→cbBTC→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 1.126846 WETH | 0.000157 WETH | 0.000000 WETH | 0.000003 WETH | 0.000154 WETH (0.3334 €) | — | 1.36 | 0.120 (n=419) | REJECTED | below_safety_margin(153792573267676<225369292159619), p_lower_below_threshold(0.12<0.75) |
| 53211925 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[uniswap_v3]→USDC | 2,540.811848 USDC | 0.369215 USDC | 0.000000 USDC | 0.007850 USDC | 0.361365 USDC (0.3325 €) | — | 1.42 | 0.120 (n=419) | REJECTED | below_safety_margin(361365<508162), p_lower_below_threshold(0.12<0.75) |
| 53210692 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 290.909613 USDC | 0.331219 USDC | 0.000000 USDC | 0.008127 USDC | 0.323092 USDC (0.2972 €) | — | 11.11 | 0.004 (n=68) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53210692 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.003573 cbBTC | 0.000004 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000004 cbBTC (0.2969 €) | — | 11.17 | 0.004 (n=68) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53210692 | WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.143948 WETH | 0.000140 WETH | 0.000000 WETH | 0.000003 WETH | 0.000136 WETH (0.2943 €) | — | 9.47 | 0.004 (n=68) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 53210692 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.004156 cbBTC | 0.000004 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000004 cbBTC (0.2940 €) | — | 9.50 | 0.004 (n=68) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53210692 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→USDC | 279.413404 USDC | 0.300573 USDC | 0.000000 USDC | 0.008127 USDC | 0.292446 USDC (0.2691 €) | — | 10.47 | 0.000 (n=66) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53210692 | cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.003370 cbBTC | 0.000004 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000004 cbBTC (0.2687 €) | — | 10.71 | 0.000 (n=66) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53211925 | cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.018506 cbBTC | 0.000003 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000003 cbBTC (0.2471 €) | — | 1.79 | 0.120 (n=419) | REJECTED | below_safety_margin(331<370), p_lower_below_threshold(0.12<0.75) |
| 53211925 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.649598 WETH | 0.000117 WETH | 0.000000 WETH | 0.000003 WETH | 0.000114 WETH (0.2463 €) | — | 1.75 | 0.120 (n=419) | REJECTED | below_safety_margin(113581956707819<129919602990268), p_lower_below_threshold(0.12<0.75) |
| 53211925 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 1,494.448893 USDC | 0.275272 USDC | 0.000000 USDC | 0.007850 USDC | 0.267422 USDC (0.2460 €) | — | 1.79 | 0.120 (n=419) | REJECTED | below_safety_margin(267422<298889), p_lower_below_threshold(0.12<0.75) |
| 53210692 | cbBTC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.003090 cbBTC | 0.000003 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000003 cbBTC (0.2389 €) | — | 10.39 | 0.004 (n=68) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53210692 | WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→WETH | 0.106804 WETH | 0.000114 WETH | 0.000000 WETH | 0.000003 WETH | 0.000111 WETH (0.2388 €) | — | 10.35 | 0.004 (n=68) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 53210692 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→USDC | 256.262294 USDC | 0.235754 USDC | 0.000000 USDC | 0.008127 USDC | 0.227627 USDC (0.2094 €) | — | 8.88 | 0.000 (n=66) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53210692 | cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.002979 cbBTC | 0.000003 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000003 cbBTC (0.2091 €) | — | 9.43 | 0.000 (n=66) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53210692 | cbBTC→[uniswap_v3]→WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.003595 cbBTC | 0.000003 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000003 cbBTC (0.2076 €) | — | 7.76 | 0.096 (n=323) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53210692 | WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[uniswap_v3]→WETH | 0.121734 WETH | 0.000100 WETH | 0.000000 WETH | 0.000003 WETH | 0.000096 WETH (0.2075 €) | — | 7.89 | 0.096 (n=323) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.10<0.75) |
| 53210692 | cbBTC→[uniswap_v3]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.002931 cbBTC | 0.000003 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000003 cbBTC (0.1972 €) | — | 9.04 | 0.000 (n=66) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53210692 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[uniswap_v3]→USDC | 256.262294 USDC | 0.222443 USDC | 0.000000 USDC | 0.008127 USDC | 0.214316 USDC (0.1972 €) | — | 8.36 | 0.000 (n=66) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53211925 | cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.015449 cbBTC | 0.000003 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000003 cbBTC (0.1881 €) | — | 1.63 | 0.120 (n=419) | REJECTED | below_safety_margin(252<308), p_lower_below_threshold(0.12<0.75) |
| 53211925 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.513347 WETH | 0.000090 WETH | 0.000000 WETH | 0.000003 WETH | 0.000087 WETH (0.1880 €) | — | 1.69 | 0.120 (n=419) | REJECTED | below_safety_margin(86715494592832<102669425869433), p_lower_below_threshold(0.12<0.75) |
| 53211925 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 1,232.485807 USDC | 0.211614 USDC | 0.000000 USDC | 0.007492 USDC | 0.204122 USDC (0.1878 €) | — | 1.66 | 0.120 (n=419) | REJECTED | below_safety_margin(204122<246497), p_lower_below_threshold(0.12<0.75) |
| 53211925 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.015878 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1694 €) | — | 1.43 | 0.001 (n=7) | REJECTED | below_safety_margin(227<317), reliability_not_demonstrated |
| 53211925 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.575230 WETH | 0.000081 WETH | 0.000000 WETH | 0.000003 WETH | 0.000078 WETH (0.1694 €) | — | 1.36 | 0.001 (n=7) | REJECTED | below_safety_margin(78117343059275<115046010487922), reliability_not_demonstrated |

## Fiabilité et décision
- Observations ghost : 3023 ; taux observé 0.098 ; borne inférieure crédible (0.9) 0.091 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 9.1% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ✅ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
