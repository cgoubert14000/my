# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-09T00:07:13+00:00 ; durée 82.74 min ; blocs 54937445 → 54962245 (4935 vus)

## Connexion
- Requêtes RPC : 64288 ; erreurs : 368 ; latence p50/p95 : 324.2/1,129.4 ms
- Rafraîchissements d'état : 4935 ; âge des données au dernier bloc : 7.26 s ; changements de frais LP observés (pools à frais dynamiques) : 4927
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 5624 ; cycles déclenchés par événement : 1226 ; avance médiane sur le rafraîchissement multicall : 414 ms
- Gaz : base fee 0.006026 gwei ; prix ETH (pool le plus profond) : 2,122.34 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 466 pools, 272 jetons, 17666 routes
- Par DEX : uniswap_v3 132, aerodrome_slipstream 98, aerodrome 194, pancakeswap_v3 28, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 166 (rejetés 2) → 571 jetons ; pools candidats 3664 (énumérés 289, par paires 0), mesurés 468, sous le plancher de 10000.0 $ : 2 → gardés 466 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2120.787264, 'cbBTC': 74286.143616, 'AERO': 0.573915}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 138,001,370 | 2,122.336437 | 54962266 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,325,648 | 0.028489 | 54962266 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 8,948,260 | 0.000013 | 54962266 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 8,755,257 | 0.028478 | 54962266 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 8,259,516 | 2,125.443121 | 54962266 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,046,383 | 105.994180 | 54962266 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,237,795 | 0.001518 | 54962266 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,889,303 | 0.028492 | 54962266 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 4,610,497 | 1.741767 | 54962266 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,921,000 | 0.999264 | 54962266 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| pancakeswap_v3 | WETH/USDC | 100 | 3,903,717 | 2,126.473313 | 54962266 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | WETH/KTA | 3000 | 3,145,316 | 42,610.354716 | 54962266 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 150 | 3,028,914 | 2,125.898849 | 54962266 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2515 | 2,365,302 | 0.028466 | 54962266 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 1,985,505 | 1,158,197.335472 | 54962266 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 424 | 1,706,223 | 0.000013 | 54962266 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,599,758 | 0.000013 | 54962266 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,551,259 | 0.000000 | 54962266 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,548,646 | 0.006423 | 54962266 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v3 | XDP/USDC | 100 | 1,524,977 | 0.014959 | 54962266 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,468,117 | 1.431451 | 54962266 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,448,259 | 438.038988 | 54962266 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,406,072 | 0.000013 | 54962266 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v3 | WETH/AERO | 3000 | 1,321,984 | 3,700.618871 | 54962266 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v2 | WETH/USDC | 3000 | 1,291,387 | 2,122.540497 | 54962266 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,228,673 | 15,392.694572 | 54962266 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/USDC | 3000 | 1,221,067 | 2,122.896735 | 54962266 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome | USDC/SEND | 3000 | 1,122,761 | 77.084041 | 54962266 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,095,261 | 2,125.343423 | 54962266 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | WETH/doginme | 10000 | 1,042,779 | 36,959,791.265206 | 54962266 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/VVV | 10000 | 1,000,044 | 106.374513 | 54962266 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/BRETT | 10000 | 950,989 | 596,919.161426 | 54962266 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome_slipstream | USDC/VELVET | 100 | 948,947 | 22.122683 | 54962266 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/TOSHI | 10000 | 939,472 | 22,792,180.475676 | 54962266 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/cbBTC | 336 | 924,006 | 0.000013 | 54962266 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | WETH/USDC | 10000 | 910,206 | 2,137.198475 | 54962266 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome | USDC/NOCK | 3000 | 909,020 | 75.833578 | 54962266 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | DRB/WETH | 10000 | 903,827 | 0.000000 | 54962266 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/MORPHO | 3000 | 893,972 | 1,056.457787 | 54962266 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 855,294 | 0.824189 | 54962266 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome | WETH/EDEL | 7000 | 824,863 | 100,926.950106 | 54962266 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | USDC/VVV | 3000 | 801,112 | 0.049933 | 54962266 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| pancakeswap_v3 | QUID/USDC | 100 | 781,127 | 0.054534 | 54962266 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/AERO | 10000 | 747,213 | 3,716.942490 | 54962266 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | USDC/SAPIEN | 4555 | 744,700 | 23.109686 | 54962266 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome | WETH/wstETH | 3000 | 719,254 | 0.801347 | 54962266 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 699,030 | 0.535942 | 54962266 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 647,215 | 5,089,630.343227 | 54962266 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 638,547 | 0.516762 | 54962266 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 623,665 | 0.000008 | 54962266 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v2 | WETH/NPC | 3000 | 617,859 | 149,236.589869 | 54962266 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome | VIRTUAL/WETH | 10000 | 590,374 | 0.000250 | 54962266 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 576,410 | 592,773.108769 | 54962266 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | FLOCK/USDC | 3000 | 563,882 | 0.038180 | 54962266 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome | WETH/msETH (stable) | 500 | 526,841 | 2.462292 | 54962266 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome | cbBTC/EDGE | 7000 | 510,025 | 909,722.793933 | 54962266 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 506,563 | 1,056.230062 | 54962266 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| uniswap_v3 | USDC/USDT | 100 | 494,873 | 1.001806 | 54962266 | `0xD56da2B74bA826f19015E6B7Dd9Dae1903E85DA1` |
| aerodrome | WETH/DRV | 3000 | 493,927 | 6,770.775895 | 54962266 | `0xaC4e562d7C6108f971321F14238E24AE2cC398ac` |
| pancakeswap_v3 | ELSA/USDC | 100 | 492,881 | 0.072104 | 54962266 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |

## Recherche d'opportunités
- Cycles : 6160 ; routes examinées : 108822560 ; candidats optimisés : 454738 ; net attendu > 0 : 3109 ; dernier cycle 128.6 ms
- Rejets (moteur) : {'spread_below_threshold': 106483368, 'liquidity_below_min': 1873220, 'negative_expected_net': 451629, 'borrow_bound_too_small': 6158, 'cycle_budget_exhausted': 5076}
- Enregistrements de la session : 454738 ; net attendu > 0 : 3109 ; simulés (eth_call de la vraie tx) : 162 (ok 105, échec 57) ; étiquettes ghost N+1 : 65/131 positives
- Décisions : {'REJECTED': 454738} ; motifs de rejet : {'below_safety_margin': 2612, 'negative_expected_net': 451629, 'p_lower_below_threshold': 2849, 'price_impact': 8, 'reliability_not_demonstrated': 260, 'sim_below_estimate': 10, 'simulated_net_nonpositive': 2, 'simulation_failed': 57, 'stale_data': 49}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 54937865 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 369.838495 USDC | 0.450524 USDC | 0.000000 USDC | 0.007098 USDC | 0.443426 USDC (0.4080 €) | — | 11.99 | 0.129 (n=193) | REJECTED | p_lower_below_threshold(0.13<0.75) |
| 54937865 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.004758 cbBTC | 0.000006 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000006 cbBTC (0.4075 €) | — | 12.55 | 0.129 (n=193) | REJECTED | p_lower_below_threshold(0.13<0.75) |
| 54958471 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.724390 WETH | 0.000162 WETH | 0.000000 WETH | 0.000003 WETH | 0.000159 WETH (0.3119 €) | — | 2.20 | 0.053 (n=283) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.05<0.75) |
| 54958471 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 1,536.750926 USDC | 0.343836 USDC | 0.000000 USDC | 0.005436 USDC | 0.338400 USDC (0.3113 €) | — | 2.20 | 0.053 (n=283) | REJECTED | p_lower_below_threshold(0.05<0.75) |
| 54957279 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.003367 cbBTC | 0.000005 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000004 cbBTC (0.3076 €) | — | 13.25 | 0.133 (n=194) | REJECTED | p_lower_below_threshold(0.13<0.75) |
| 54957279 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 260.127433 USDC | 0.340704 USDC | 0.000000 USDC | 0.007419 USDC | 0.333285 USDC (0.3066 €) | — | 12.81 | 0.133 (n=194) | REJECTED | p_lower_below_threshold(0.13<0.75) |
| 54957536 | cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.003414 cbBTC | 0.000004 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000004 cbBTC (0.3021 €) | — | 12.83 | 0.043 (n=118) | REJECTED | p_lower_below_threshold(0.04<0.75) |
| 54957536 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→USDC | 269.547059 USDC | 0.334732 USDC | 0.000000 USDC | 0.006754 USDC | 0.327978 USDC (0.3017 €) | — | 12.17 | 0.043 (n=118) | REJECTED | p_lower_below_threshold(0.04<0.75) |
| 54937865 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→USDC | 328.781193 USDC | 0.334209 USDC | 0.000000 USDC | 0.006775 USDC | 0.327434 USDC (0.3012 €) | — | 9.96 | 0.031 (n=113) | REJECTED | p_lower_below_threshold(0.03<0.75) |
| 54937865 | cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.004323 cbBTC | 0.000005 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000004 cbBTC (0.3010 €) | — | 10.20 | 0.031 (n=113) | REJECTED | p_lower_below_threshold(0.03<0.75) |
| 54958471 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.015122 cbBTC | 0.000004 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000004 cbBTC (0.2778 €) | — | 2.67 | 0.050 (n=29) | REJECTED | reliability_not_demonstrated |
| 54958471 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.521560 WETH | 0.000145 WETH | 0.000000 WETH | 0.000003 WETH | 0.000142 WETH (0.2776 €) | — | 2.72 | 0.050 (n=29) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 54958471 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 1,129.696150 USDC | 0.308254 USDC | 0.000000 USDC | 0.007055 USDC | 0.301199 USDC (0.2771 €) | — | 2.67 | 0.050 (n=29) | REJECTED | reliability_not_demonstrated |
| 54957279 | WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.108597 WETH | 0.000141 WETH | 0.000000 WETH | 0.000003 WETH | 0.000137 WETH (0.2699 €) | — | 12.66 | 0.133 (n=194) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.13<0.75) |
| 54957279 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.003033 cbBTC | 0.000004 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000004 cbBTC (0.2697 €) | — | 12.89 | 0.133 (n=194) | REJECTED | p_lower_below_threshold(0.13<0.75) |
| 54957536 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.003081 cbBTC | 0.000004 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000004 cbBTC (0.2586 €) | — | 12.17 | 0.131 (n=197) | REJECTED | p_lower_below_threshold(0.13<0.75) |
| 54957536 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 241.501279 USDC | 0.287680 USDC | 0.000000 USDC | 0.006754 USDC | 0.280926 USDC (0.2585 €) | — | 11.63 | 0.131 (n=197) | REJECTED | p_lower_below_threshold(0.13<0.75) |
| 54958471 | cbBTC→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.016395 cbBTC | 0.000004 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000004 cbBTC (0.2523 €) | — | 2.24 | 0.189 (n=1164) | REJECTED | p_lower_below_threshold(0.19<0.75) |
| 54958471 | WETH→[pancakeswap_v3]→cbBTC→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.604420 WETH | 0.000132 WETH | 0.000000 WETH | 0.000003 WETH | 0.000129 WETH (0.2521 €) | — | 2.13 | 0.189 (n=1164) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.19<0.75) |
| 54958471 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[uniswap_v3]→USDC | 1,252.676789 USDC | 0.280851 USDC | 0.000000 USDC | 0.007377 USDC | 0.273474 USDC (0.2516 €) | — | 2.18 | 0.189 (n=1164) | REJECTED | p_lower_below_threshold(0.19<0.75) |
| 54937865 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[uniswap_v3]→USDC | 299.072510 USDC | 0.279400 USDC | 0.000000 USDC | 0.006775 USDC | 0.272625 USDC (0.2508 €) | — | 9.12 | 0.031 (n=113) | REJECTED | p_lower_below_threshold(0.03<0.75) |
| 54937865 | cbBTC→[uniswap_v3]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.003892 cbBTC | 0.000004 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000004 cbBTC (0.2505 €) | — | 9.43 | 0.031 (n=113) | REJECTED | p_lower_below_threshold(0.03<0.75) |
| 54937865 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→USDC | 280.437346 USDC | 0.268901 USDC | 0.000000 USDC | 0.006775 USDC | 0.262126 USDC (0.2412 €) | — | 9.35 | 0.031 (n=113) | REJECTED | p_lower_below_threshold(0.03<0.75) |
| 54937865 | cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.003718 cbBTC | 0.000004 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000004 cbBTC (0.2409 €) | — | 9.49 | 0.031 (n=113) | REJECTED | p_lower_below_threshold(0.03<0.75) |
| 54957536 | cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.002784 cbBTC | 0.000003 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000003 cbBTC (0.2124 €) | — | 11.06 | 0.043 (n=118) | REJECTED | p_lower_below_threshold(0.04<0.75) |

## Fiabilité et décision
- Observations ghost : 6566 ; taux observé 0.172 ; borne inférieure crédible (0.9) 0.166 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 16.6% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ✅ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
