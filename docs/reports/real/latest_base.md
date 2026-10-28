# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-28T18:20:20+00:00 ; durée 94.76 min ; blocs 53208289 → 53211135 (2696 vus)

## Connexion
- Requêtes RPC : 31367 ; erreurs : 120 ; latence p50/p95 : 258.3/1,402.5 ms
- Rafraîchissements d'état : 2696 ; âge des données au dernier bloc : 2.75 s ; changements de frais LP observés (pools à frais dynamiques) : 4926
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 23782 ; cycles déclenchés par événement : 1384 ; avance médiane sur le rafraîchissement multicall : 569 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,344.76 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 517 pools, 298 jetons, 19028 routes
- Par DEX : uniswap_v3 144, aerodrome_slipstream 121, aerodrome 210, pancakeswap_v3 28, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 183 (rejetés 2) → 588 jetons ; pools candidats 3758 (énumérés 330, par paires 0), mesurés 519, sous le plancher de 10000.0 $ : 2 → gardés 517 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDC': 1.0, 'USDbC': 1.0, 'WETH': 2331.23448, 'cbBTC': 80382.611332, 'AERO': 0.701638}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 157,818,062 | 2,344.759728 | 53211135 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,521,736 | 0.029008 | 53211135 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,879,560 | 0.000012 | 53211135 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,462,934 | 0.028977 | 53211135 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 8,512,094 | 2,340.571316 | 53211135 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 8,257,002 | 97.719234 | 53211135 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,038,792 | 0.001642 | 53211135 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 6,775,360 | 1.425320 | 53211135 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,814,345 | 0.029001 | 53211135 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/USDC | 639 | 4,943,114 | 2,340.003605 | 53211135 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,428,222 | 2,339.625014 | 53211135 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,256,700 | 0.998804 | 53211135 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,688,444 | 37,826.544149 | 53211135 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,939,380 | 0.028991 | 53211135 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2736 | 2,520,969 | 97.784289 | 53211135 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | WETH/FAI | 10000 | 2,142,626 | 1,214,151.729099 | 53211135 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 412 | 2,122,105 | 0.000012 | 53211135 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome | WETH/USDC | 3000 | 1,859,322 | 2,345.342499 | 53211135 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| uniswap_v3 | XDP/USDC | 100 | 1,822,831 | 0.018678 | 53211135 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,782,778 | 402.264935 | 53211135 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,779,817 | 0.000000 | 53211135 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,721,154 | 0.000012 | 53211135 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,694,910 | 0.000012 | 53211135 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | USDC/cbBTC | 332 | 1,668,648 | 0.000012 | 53211135 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,514,132 | 1.588195 | 53211135 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,492,809 | 0.005718 | 53211135 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v3 | WETH/AERO | 3000 | 1,462,720 | 3,335.106462 | 53211135 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,460,758 | 0.826986 | 53211135 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,387,150 | 13,855.522036 | 53211135 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,247,671 | 2,340.735193 | 53211135 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,246,050 | 0.000265 | 53211135 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | USDC/SEND | 3000 | 1,193,805 | 68.182945 | 53211135 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome | VIRTUAL/WETH | 10000 | 1,160,419 | 0.000266 | 53211135 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | WETH/doginme | 10000 | 1,156,682 | 36,550,416.191071 | 53211135 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | WETH/WELL | 10000 | 1,154,980 | 1,080,719.080478 | 53211135 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,126,595 | 503,793.158862 | 53211135 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,120,772 | 0.000000 | 53211135 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,086,092 | 21,137,232.798371 | 53211135 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome | WETH/AERO | 10000 | 1,079,182 | 3,335.376067 | 53211135 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | WETH/EDEL | 7000 | 1,078,504 | 72,211.081198 | 53211135 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,052,495 | 16.454691 | 53211135 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v2 | WETH/USDC | 3000 | 1,031,062 | 2,344.365704 | 53211135 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome | USDC/NOCK | 3000 | 1,009,141 | 61.471437 | 53211135 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/VVV | 10000 | 996,798 | 97.473214 | 53211135 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | USDC/VVV | 3000 | 996,236 | 0.041797 | 53211135 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/USDC | 10000 | 939,597 | 2,344.326232 | 53211135 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 929,252 | 1,062.076663 | 53211135 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | uXRP/WETH | 3000 | 905,773 | 0.000559 | 53211135 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome | WETH/msETH (stable) | 500 | 880,923 | 2.330700 | 53211135 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | USDC/SAPIEN | 4520 | 872,938 | 18.189552 | 53211135 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 839,934 | 17.648576 | 53211135 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| pancakeswap_v3 | QUID/USDC | 100 | 805,471 | 0.058236 | 53211135 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 793,978 | 0.802973 | 53211135 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 759,048 | 0.000009 | 53211135 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 748,747 | 4,630,072.970233 | 53211135 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 746,255 | 0.619739 | 53211135 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/NPC | 3000 | 707,970 | 138,141.606798 | 53211135 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | WETH/BRETT | 2114 | 694,574 | 501,213.299631 | 53211135 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 666,508 | 0.106739 | 53211135 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| uniswap_v3 | TIG/USDC | 10000 | 665,288 | 0.557908 | 53211135 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |

## Recherche d'opportunités
- Cycles : 4079 ; routes examinées : 77615212 ; candidats optimisés : 259915 ; net attendu > 0 : 376 ; dernier cycle 144.5 ms
- Rejets (moteur) : {'spread_below_threshold': 76222342, 'liquidity_below_min': 1096802, 'negative_expected_net': 259539, 'pool_quarantined': 31472, 'borrow_bound_too_small': 4074, 'cycle_budget_exhausted': 605, 'no_price_reference': 2}
- Enregistrements de la session : 259915 ; net attendu > 0 : 376 ; simulés (eth_call de la vraie tx) : 23 (ok 2, échec 21) ; étiquettes ghost N+1 : 3/23 positives
- Décisions : {'REJECTED': 259915} ; motifs de rejet : {'below_safety_margin': 314, 'negative_expected_net': 259539, 'p_lower_below_threshold': 338, 'reliability_not_demonstrated': 38, 'simulation_failed': 21, 'stale_data': 70}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53210692 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 290.909613 USDC | 0.331219 USDC | 0.000000 USDC | 0.008127 USDC | 0.323092 USDC (0.2972 €) | — | 11.11 | 0.004 (n=68) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53210692 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.003573 cbBTC | 0.000004 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000004 cbBTC (0.2969 €) | — | 11.17 | 0.004 (n=68) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53210692 | WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.143948 WETH | 0.000140 WETH | 0.000000 WETH | 0.000003 WETH | 0.000136 WETH (0.2943 €) | — | 9.47 | 0.004 (n=68) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 53210692 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.004156 cbBTC | 0.000004 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000004 cbBTC (0.2940 €) | — | 9.50 | 0.004 (n=68) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53210692 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→USDC | 279.413404 USDC | 0.300573 USDC | 0.000000 USDC | 0.008127 USDC | 0.292446 USDC (0.2691 €) | — | 10.47 | 0.000 (n=66) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53210692 | cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.003370 cbBTC | 0.000004 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000004 cbBTC (0.2687 €) | — | 10.71 | 0.000 (n=66) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53210692 | cbBTC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.003090 cbBTC | 0.000003 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000003 cbBTC (0.2389 €) | — | 10.39 | 0.004 (n=68) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53210692 | WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→WETH | 0.106804 WETH | 0.000114 WETH | 0.000000 WETH | 0.000003 WETH | 0.000111 WETH (0.2388 €) | — | 10.35 | 0.004 (n=68) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 53210692 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→USDC | 256.262294 USDC | 0.235754 USDC | 0.000000 USDC | 0.008127 USDC | 0.227627 USDC (0.2094 €) | — | 8.88 | 0.000 (n=66) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53210692 | cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.002979 cbBTC | 0.000003 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000003 cbBTC (0.2091 €) | — | 9.43 | 0.000 (n=66) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53210692 | cbBTC→[uniswap_v3]→WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.003595 cbBTC | 0.000003 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000003 cbBTC (0.2076 €) | — | 7.76 | 0.096 (n=323) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53210692 | WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[uniswap_v3]→WETH | 0.121734 WETH | 0.000100 WETH | 0.000000 WETH | 0.000003 WETH | 0.000096 WETH (0.2075 €) | — | 7.89 | 0.096 (n=323) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.10<0.75) |
| 53210692 | cbBTC→[uniswap_v3]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.002931 cbBTC | 0.000003 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000003 cbBTC (0.1972 €) | — | 9.04 | 0.000 (n=66) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53210692 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[uniswap_v3]→USDC | 256.262294 USDC | 0.222443 USDC | 0.000000 USDC | 0.008127 USDC | 0.214316 USDC (0.1972 €) | — | 8.36 | 0.000 (n=66) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53210692 | WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.103020 WETH | 0.000076 WETH | 0.000000 WETH | 0.000003 WETH | 0.000073 WETH (0.1568 €) | — | 7.05 | 0.096 (n=323) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53210692 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.002847 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1563 €) | — | 7.38 | 0.096 (n=323) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53210692 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.002554 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1548 €) | — | 8.14 | 0.004 (n=68) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53210692 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 213.268070 USDC | 0.176206 USDC | 0.000000 USDC | 0.008127 USDC | 0.168079 USDC (0.1546 €) | — | 7.88 | 0.096 (n=323) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53210529 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.011595 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0870 €) | — | 1.01 | 0.001 (n=7) | REJECTED | below_safety_margin(117<231), reliability_not_demonstrated |
| 53210529 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.406438 WETH | 0.000043 WETH | 0.000000 WETH | 0.000003 WETH | 0.000040 WETH (0.0865 €) | — | 0.99 | 0.001 (n=7) | REJECTED | below_safety_margin(40092328619319<81287613159080), reliability_not_demonstrated |
| 53210529 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 951.804771 USDC | 0.101824 USDC | 0.000000 USDC | 0.007951 USDC | 0.093873 USDC (0.0864 €) | — | 0.99 | 0.001 (n=7) | REJECTED | below_safety_margin(93873<190360), reliability_not_demonstrated |
| 53210692 | WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.064784 WETH | 0.000034 WETH | 0.000000 WETH | 0.000003 WETH | 0.000031 WETH (0.0667 €) | — | 4.76 | 0.096 (n=323) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53210692 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.001919 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0662 €) | — | 4.64 | 0.096 (n=323) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53210528 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USD→[aerodrome_slipstream]→USDC | 53.324969 USDC | 0.056221 USDC | 0.000000 USDC | 0.007778 USDC | 0.048443 USDC (0.0446 €) | — | 9.08 | 0.000 (n=67) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53210528 | WETH→[aerodrome_slipstream]→USD→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.022710 WETH | 0.000024 WETH | 0.000000 WETH | 0.000003 WETH | 0.000021 WETH (0.0445 €) | — | 9.09 | 0.000 (n=67) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |

## Fiabilité et décision
- Observations ghost : 2988 ; taux observé 0.094 ; borne inférieure crédible (0.9) 0.087 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 8.7% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
