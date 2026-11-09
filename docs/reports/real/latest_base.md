# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-09T20:54:20+00:00 ; durée 318.55 min ; blocs 55240823 → 55336310 (8302 vus)

## Connexion
- Requêtes RPC : 166133 ; erreurs : 25 ; latence p50/p95 : 527.3/1,752.0 ms
- Rafraîchissements d'état : 8302 ; âge des données au dernier bloc : 14.36 s ; changements de frais LP observés (pools à frais dynamiques) : 8389
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 38543 ; cycles déclenchés par événement : 12430 ; avance médiane sur le rafraîchissement multicall : 389 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,127.77 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 473 pools, 274 jetons, 17868 routes
- Par DEX : uniswap_v3 135, aerodrome_slipstream 102, aerodrome 193, pancakeswap_v3 29, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 167 (rejetés 2) → 572 jetons ; pools candidats 3663 (énumérés 293, par paires 0), mesurés 475, sous le plancher de 10000.0 $ : 2 → gardés 473 (max 1500) ; prix des hubs : {'USDC': 1.0, 'USDbC': 1.0, 'DAI': 1.0, 'WETH': 2131.426069, 'cbBTC': 75169.710892, 'AERO': 0.579676}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 139,778,885 | 2,127.766497 | 55336341 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,675,664 | 0.028473 | 55336341 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,323,775 | 0.000013 | 55336341 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 8,785,026 | 0.028437 | 55336341 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 7,480,066 | 2,130.191251 | 55336341 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,338,368 | 98.164381 | 55336341 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,947,514 | 0.028486 | 55336341 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 4,584,378 | 1.743699 | 55336341 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,007,422 | 2,129.924455 | 55336341 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,887,189 | 1.000033 | 55336341 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,106,696 | 43,900.101587 | 55336341 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 150 | 3,028,725 | 2,130.181843 | 55336341 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,363,812 | 0.028438 | 55336341 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 2,032,587 | 1,110,825.121995 | 55336341 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,723,017 | 0.000013 | 55336341 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | USDC/cbBTC | 424 | 1,708,912 | 0.000013 | 55336341 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | XDP/USDC | 100 | 1,585,840 | 0.015827 | 55336341 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,564,205 | 0.006566 | 55336341 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,562,255 | 0.000000 | 55336341 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,510,938 | 0.000013 | 55336341 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,481,281 | 1.407587 | 55336341 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,467,073 | 423.154800 | 55336341 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,456,949 | 0.821811 | 55336341 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,322,314 | 3,713.121954 | 55336341 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v2 | WETH/USDC | 3000 | 1,293,209 | 2,129.296008 | 55336341 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,251,318 | 14,844.393590 | 55336341 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/USDC | 3000 | 1,221,416 | 2,125.963578 | 55336341 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome | USDC/SEND | 3000 | 1,107,263 | 79.257048 | 55336341 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,102,788 | 2,129.703923 | 55336341 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | WETH/doginme | 10000 | 1,050,796 | 36,372,708.938556 | 55336341 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/VVV | 10000 | 986,320 | 98.507482 | 55336341 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/BRETT | 10000 | 970,655 | 566,049.887167 | 55336341 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | USDC/VVV | 3000 | 964,747 | 0.046141 | 55336341 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome_slipstream | USDC/VELVET | 100 | 961,952 | 21.255514 | 55336341 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 938,210 | 0.001518 | 55336341 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| uniswap_v3 | WETH/TOSHI | 10000 | 936,444 | 23,213,728.096903 | 55336341 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/cbBTC | 334 | 927,433 | 0.000013 | 55336341 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/NOCK | 3000 | 919,209 | 74.161721 | 55336341 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/MORPHO | 3000 | 909,970 | 1,032.354065 | 55336341 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/USDC | 10000 | 887,615 | 2,127.924155 | 55336341 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | DRB/WETH | 10000 | 886,279 | 0.000000 | 55336341 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | WETH/EDEL | 7000 | 816,406 | 103,556.506089 | 55336341 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome_slipstream | USDC/SAPIEN | 4515 | 776,684 | 21.805228 | 55336341 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 770,971 | 0.053062 | 55336341 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/AERO | 10000 | 747,072 | 3,692.738593 | 55336341 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | WETH/wstETH | 3000 | 722,419 | 0.798411 | 55336341 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 672,312 | 0.552592 | 55336341 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 664,758 | 4,849,858.490995 | 55336341 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 649,326 | 0.529404 | 55336341 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 623,139 | 0.000008 | 55336341 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v2 | WETH/NPC | 3000 | 616,357 | 150,789.038142 | 55336341 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome | VIRTUAL/WETH | 10000 | 601,085 | 0.000258 | 55336341 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/BRETT | 2120 | 594,236 | 567,233.791464 | 55336341 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | FLOCK/USDC | 3000 | 573,142 | 0.039120 | 55336341 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 516,753 | 1,032.602489 | 55336341 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome | WETH/msETH (stable) | 500 | 498,158 | 2.400596 | 55336341 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | USDC/USDT | 100 | 493,614 | 1.001012 | 55336341 | `0xD56da2B74bA826f19015E6B7Dd9Dae1903E85DA1` |
| aerodrome | WETH/DRV | 3000 | 491,703 | 6,867.166907 | 55336341 | `0xaC4e562d7C6108f971321F14238E24AE2cC398ac` |
| pancakeswap_v3 | ELSA/USDC | 100 | 475,195 | 0.068625 | 55336341 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| uniswap_v3 | WETH/uSOL | 3000 | 469,938 | 24.679366 | 55336341 | `0xab04A352D4EC8d0F1812A4E5EBe7807Fa67acD48` |

## Recherche d'opportunités
- Cycles : 20731 ; routes examinées : 370421508 ; candidats optimisés : 1230396 ; net attendu > 0 : 3776 ; dernier cycle 360.1 ms
- Rejets (moteur) : {'spread_below_threshold': 363538957, 'liquidity_below_min': 5584250, 'negative_expected_net': 1226620, 'borrow_bound_too_small': 61196, 'pool_quarantined': 6004, 'cycle_budget_exhausted': 691, 'no_price_reference': 14}
- Enregistrements de la session : 1230396 ; net attendu > 0 : 3776 ; simulés (eth_call de la vraie tx) : 268 (ok 82, échec 186) ; étiquettes ghost N+1 : 45/189 positives
- Décisions : {'REJECTED': 1230396} ; motifs de rejet : {'below_safety_margin': 3089, 'negative_expected_net': 1226620, 'p_lower_below_threshold': 3623, 'reliability_not_demonstrated': 153, 'sim_below_estimate': 9, 'simulated_net_nonpositive': 3, 'simulation_failed': 186, 'stale_data': 1430}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 55292046 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.628604 WETH | 0.000161 WETH | 0.000000 WETH | 0.000002 WETH | 0.000159 WETH (0.3108 €) | — | 2.53 | 0.048 (n=91) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.05<0.75) |
| 55292046 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 1,328.473302 USDC | 0.341590 USDC | 0.000000 USDC | 0.004798 USDC | 0.336792 USDC (0.3098 €) | — | 2.54 | 0.048 (n=91) | REJECTED | p_lower_below_threshold(0.05<0.75) |
| 55299317 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 1,145.230033 USDC | 0.328294 USDC | 0.000000 USDC | 0.005110 USDC | 0.323184 USDC (0.2973 €) | — | 2.82 | 0.063 (n=311) | REJECTED | p_lower_below_threshold(0.06<0.75) |
| 55299317 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.540159 WETH | 0.000155 WETH | 0.000000 WETH | 0.000002 WETH | 0.000152 WETH (0.2971 €) | — | 2.82 | 0.063 (n=311) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.06<0.75) |
| 55292046 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.489407 WETH | 0.000128 WETH | 0.000000 WETH | 0.000002 WETH | 0.000126 WETH (0.2460 €) | — | 2.58 | 0.063 (n=309) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.06<0.75) |
| 55292046 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 1,032.952111 USDC | 0.271387 USDC | 0.000000 USDC | 0.004798 USDC | 0.266589 USDC (0.2453 €) | — | 2.58 | 0.063 (n=309) | REJECTED | p_lower_below_threshold(0.06<0.75) |
| 55292068 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.486339 WETH | 0.000127 WETH | 0.000000 WETH | 0.000002 WETH | 0.000125 WETH (0.2438 €) | — | 2.57 | 0.063 (n=309) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.06<0.75) |
| 55292068 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 1,028.744064 USDC | 0.268963 USDC | 0.000000 USDC | 0.004798 USDC | 0.264165 USDC (0.2430 €) | — | 2.57 | 0.063 (n=309) | REJECTED | p_lower_below_threshold(0.06<0.75) |
| 55299524 | WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.101373 WETH | 0.000112 WETH | 0.000000 WETH | 0.000003 WETH | 0.000109 WETH (0.2127 €) | — | 10.75 | 0.129 (n=215) | REJECTED | stale_data(4279ms>4000.0), simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.13<0.75) |
| 55299524 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.002849 cbBTC | 0.000003 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000003 cbBTC (0.2125 €) | — | 10.88 | 0.129 (n=215) | REJECTED | stale_data(4284ms>4000.0), p_lower_below_threshold(0.13<0.75) |
| 55292046 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC | 0.011792 cbBTC | 0.000003 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000003 cbBTC (0.2107 €) | — | 2.60 | 0.219 (n=1279) | REJECTED | p_lower_below_threshold(0.22<0.75) |
| 55292046 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.435109 WETH | 0.000111 WETH | 0.000000 WETH | 0.000003 WETH | 0.000108 WETH (0.2101 €) | — | 2.47 | 0.219 (n=1279) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.22<0.75) |
| 55292046 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 927.984639 USDC | 0.233918 USDC | 0.000000 USDC | 0.006417 USDC | 0.227501 USDC (0.2093 €) | — | 2.45 | 0.219 (n=1279) | REJECTED | p_lower_below_threshold(0.22<0.75) |
| 55292046 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.461965 WETH | 0.000106 WETH | 0.000000 WETH | 0.000002 WETH | 0.000104 WETH (0.2032 €) | — | 2.25 | 0.048 (n=91) | REJECTED | p_lower_below_threshold(0.05<0.75) |
| 55292046 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 976.657356 USDC | 0.224972 USDC | 0.000000 USDC | 0.004798 USDC | 0.220174 USDC (0.2026 €) | — | 2.25 | 0.048 (n=91) | REJECTED | p_lower_below_threshold(0.05<0.75) |
| 55326068 | cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.006171 cbBTC | 0.000003 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000003 cbBTC (0.2013 €) | — | 4.73 | 0.176 (n=1011) | REJECTED | p_lower_below_threshold(0.18<0.75) |
| 55326068 | WETH→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.220571 WETH | 0.000106 WETH | 0.000000 WETH | 0.000003 WETH | 0.000103 WETH (0.2011 €) | — | 4.65 | 0.176 (n=1011) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.18<0.75) |
| 55299524 | WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[uniswap_v3]→WETH | 0.097442 WETH | 0.000101 WETH | 0.000000 WETH | 0.000003 WETH | 0.000097 WETH (0.1901 €) | — | 10.00 | 0.129 (n=215) | REJECTED | stale_data(4299ms>4000.0), simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.13<0.75) |
| 55299524 | cbBTC→[uniswap_v3]→WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.002727 cbBTC | 0.000003 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000003 cbBTC (0.1899 €) | — | 10.16 | 0.129 (n=215) | REJECTED | stale_data(4304ms>4000.0), p_lower_below_threshold(0.13<0.75) |
| 55299524 | cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.002710 cbBTC | 0.000003 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000003 cbBTC (0.1837 €) | — | 9.89 | 0.058 (n=130) | REJECTED | stale_data(4318ms>4000.0), p_lower_below_threshold(0.06<0.75) |
| 55299524 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→USDC | 206.948004 USDC | 0.206046 USDC | 0.000000 USDC | 0.006406 USDC | 0.199640 USDC (0.1837 €) | — | 9.65 | 0.058 (n=130) | REJECTED | stale_data(4322ms>4000.0), p_lower_below_threshold(0.06<0.75) |
| 55299524 | WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.087641 WETH | 0.000094 WETH | 0.000000 WETH | 0.000003 WETH | 0.000091 WETH (0.1769 €) | — | 10.34 | 0.129 (n=215) | REJECTED | stale_data(4309ms>4000.0), simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.13<0.75) |
| 55299524 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.002513 cbBTC | 0.000003 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000003 cbBTC (0.1768 €) | — | 10.27 | 0.129 (n=215) | REJECTED | stale_data(4314ms>4000.0), p_lower_below_threshold(0.13<0.75) |
| 55322988 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.015632 cbBTC | 0.000003 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000003 cbBTC (0.1759 €) | — | 1.63 | 0.045 (n=32) | REJECTED | below_safety_margin(255<312), p_lower_below_threshold(0.05<0.75) |
| 55322988 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.546765 WETH | 0.000093 WETH | 0.000000 WETH | 0.000003 WETH | 0.000090 WETH (0.1756 €) | — | 1.64 | 0.045 (n=32) | REJECTED | below_safety_margin(89571052907108<109353087336479), p_lower_below_threshold(0.05<0.75) |

## Fiabilité et décision
- Observations ghost : 7101 ; taux observé 0.184 ; borne inférieure crédible (0.9) 0.179 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 17.9% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
