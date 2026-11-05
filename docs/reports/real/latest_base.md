# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-05T16:52:42+00:00 ; durée 67.75 min ; blocs 53552072 → 53554106 (1905 vus)

## Connexion
- Requêtes RPC : 22050 ; erreurs : 5 ; latence p50/p95 : 127.5/883.3 ms
- Rafraîchissements d'état : 1906 ; âge des données au dernier bloc : 1.26 s ; changements de frais LP observés (pools à frais dynamiques) : 8390
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 31082 ; cycles déclenchés par événement : 816 ; avance médiane sur le rafraîchissement multicall : 562 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,268.76 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 485 pools, 283 jetons, 19058 routes
- Par DEX : uniswap_v3 137, aerodrome_slipstream 102, aerodrome 203, pancakeswap_v3 29, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 174 (rejetés 2) → 579 jetons ; pools candidats 3708 (énumérés 302, par paires 0), mesurés 488, sous le plancher de 10000.0 $ : 3 → gardés 485 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'DAI': 1.0, 'USDC': 1.0, 'WETH': 2284.245505, 'cbBTC': 76255.016176, 'AERO': 0.595113}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 148,991,169 | 2,268.764734 | 53554106 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,637,251 | 0.029642 | 53554106 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,156,391 | 0.029649 | 53554106 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 8,766,484 | 0.000013 | 53554106 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 7,952,586 | 2,266.469887 | 53554106 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,364,564 | 110.973326 | 53554106 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,472,655 | 0.001548 | 53554106 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 5,124,875 | 1.664371 | 53554106 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,068,707 | 0.029640 | 53554106 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,113,802 | 2,265.818456 | 53554106 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,032,673 | 0.998641 | 53554106 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,385,889 | 42,019.273816 | 53554106 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 150 | 3,294,646 | 2,266.004947 | 53554106 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,591,980 | 0.029635 | 53554106 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 2,120,557 | 1,160,500.715180 | 53554106 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,814,302 | 0.007220 | 53554106 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/cbBTC | 412 | 1,754,668 | 0.000013 | 53554106 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,657,357 | 0.000000 | 53554106 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,652,409 | 0.016572 | 53554106 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,635,352 | 0.000013 | 53554106 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,535,359 | 1.454334 | 53554106 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,530,831 | 453.066755 | 53554106 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,529,509 | 0.000013 | 53554106 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,456,467 | 0.816362 | 53554106 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,382,862 | 3,770.631646 | 53554106 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | WETH/USDC | 3000 | 1,334,992 | 2,267.926543 | 53554106 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| uniswap_v2 | WETH/USDC | 3000 | 1,334,659 | 2,268.747640 | 53554106 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,264,496 | 15,260.119322 | 53554106 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,191,824 | 2,266.427590 | 53554106 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,150,799 | 73.373683 | 53554106 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,108,745 | 37,588,045.504841 | 53554106 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | DRB/WETH | 10000 | 1,036,938 | 0.000000 | 53554106 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/VVV | 10000 | 1,033,589 | 110.588404 | 53554106 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,028,991 | 575,529.123105 | 53554106 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,002,192 | 22,877,229.480417 | 53554106 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome | USDC/NOCK | 3000 | 963,345 | 67.564819 | 53554106 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | USDC/VELVET | 100 | 961,065 | 21.316012 | 53554106 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/USDC | 10000 | 940,845 | 2,278.487113 | 53554106 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome_slipstream | USDC/cbBTC | 332 | 930,587 | 0.000013 | 53554106 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | WETH/MORPHO | 3000 | 928,796 | 1,093.896196 | 53554106 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome | WETH/EDEL | 7000 | 890,834 | 98,942.118964 | 53554106 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | uXRP/WETH | 3000 | 861,511 | 0.000549 | 53554106 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| uniswap_v3 | USDC/VVV | 3000 | 840,532 | 0.048906 | 53554106 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | WETH/AERO | 10000 | 801,326 | 3,790.582871 | 53554106 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| pancakeswap_v3 | QUID/USDC | 100 | 797,952 | 0.057044 | 53554106 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 780,669 | 21.617993 | 53554106 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome | WETH/wstETH | 3000 | 769,811 | 0.799698 | 53554106 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 707,718 | 0.561646 | 53554106 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 699,334 | 4,979,592.560868 | 53554106 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome | VIRTUAL/WETH | 10000 | 683,836 | 0.000246 | 53554106 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v2 | WETH/NPC | 3000 | 672,169 | 143,965.546258 | 53554106 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 652,842 | 0.000008 | 53554106 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v3 | TIG/USDC | 10000 | 647,233 | 0.531380 | 53554106 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | WETH/BRETT | 2093 | 627,661 | 578,445.341711 | 53554106 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome | WETH/bsdETH | 100 | 608,995 | 0.913964 | 53554106 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome | WETH/msETH (stable) | 500 | 605,063 | 2.480726 | 53554106 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | FLOCK/USDC | 3000 | 553,632 | 0.037352 | 53554106 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome | cbBTC/EDGE | 7000 | 551,498 | 819,534.403453 | 53554106 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| pancakeswap_v3 | ELSA/USDC | 100 | 533,650 | 0.080794 | 53554106 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| aerodrome | WETH/DRV | 3000 | 525,648 | 6,831.651653 | 53554106 | `0xaC4e562d7C6108f971321F14238E24AE2cC398ac` |

## Recherche d'opportunités
- Cycles : 2721 ; routes examinées : 51856818 ; candidats optimisés : 262734 ; net attendu > 0 : 2627 ; dernier cycle 277.1 ms
- Rejets (moteur) : {'spread_below_threshold': 50059576, 'liquidity_below_min': 1273690, 'negative_expected_net': 260107, 'pool_quarantined': 236526, 'unquotable': 16794, 'cycle_budget_exhausted': 7498}
- Enregistrements de la session : 262734 ; net attendu > 0 : 2627 ; simulés (eth_call de la vraie tx) : 57 (ok 23, échec 34) ; étiquettes ghost N+1 : 0/52 positives
- Décisions : {'REJECTED': 262734} ; motifs de rejet : {'below_safety_margin': 2351, 'negative_expected_net': 260107, 'p_lower_below_threshold': 2275, 'price_impact': 5, 'reliability_not_demonstrated': 352, 'sim_below_estimate': 1, 'simulation_failed': 34, 'stale_data': 26}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53553715 | USDC→[aerodrome]→OWB→[uniswap_v3]→USDC | 144.695729 USDC | 1.993485 USDC | 0.000000 USDC | 0.005193 USDC | 1.988292 USDC (1.8292 €) | — | 137.41 | 0.000 (n=19) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53552258 | cbBTC→[uniswap_v3]→WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.026532 cbBTC | 0.000008 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000008 cbBTC (0.5547 €) | — | 2.98 | 0.169 (n=990) | REJECTED | p_lower_below_threshold(0.17<0.75) |
| 53552258 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH | 0.912068 WETH | 0.000269 WETH | 0.000000 WETH | 0.000004 WETH | 0.000265 WETH (0.5545 €) | — | 2.90 | 0.169 (n=990) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.17<0.75) |
| 53552258 | USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 2,097.083342 USDC | 0.610892 USDC | 0.000000 USDC | 0.010208 USDC | 0.600684 USDC (0.5526 €) | — | 2.86 | 0.169 (n=990) | REJECTED | p_lower_below_threshold(0.17<0.75) |
| 53552258 | cbBTC→[uniswap_v3]→WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.019735 cbBTC | 0.000005 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000005 cbBTC (0.3639 €) | — | 2.63 | 0.169 (n=990) | REJECTED | p_lower_below_threshold(0.17<0.75) |
| 53552258 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH | 0.659335 WETH | 0.000178 WETH | 0.000000 WETH | 0.000004 WETH | 0.000173 WETH (0.3632 €) | — | 2.63 | 0.169 (n=990) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.17<0.75) |
| 53552258 | USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 1,516.653550 USDC | 0.403237 USDC | 0.000000 USDC | 0.009805 USDC | 0.393432 USDC (0.3620 €) | — | 2.59 | 0.169 (n=990) | REJECTED | p_lower_below_threshold(0.17<0.75) |
| 53552258 | cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.020368 cbBTC | 0.000005 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000005 cbBTC (0.3604 €) | — | 2.52 | 0.169 (n=990) | REJECTED | p_lower_below_threshold(0.17<0.75) |
| 53552258 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.718376 WETH | 0.000176 WETH | 0.000000 WETH | 0.000004 WETH | 0.000172 WETH (0.3602 €) | — | 2.39 | 0.169 (n=990) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.17<0.75) |
| 53552258 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 1,601.921125 USDC | 0.400158 USDC | 0.000000 USDC | 0.009805 USDC | 0.390353 USDC (0.3591 €) | — | 2.44 | 0.169 (n=990) | REJECTED | p_lower_below_threshold(0.17<0.75) |
| 53552258 | cbBTC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.014238 cbBTC | 0.000004 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000004 cbBTC (0.2868 €) | — | 2.87 | 0.169 (n=990) | REJECTED | p_lower_below_threshold(0.17<0.75) |
| 53552258 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH | 0.484150 WETH | 0.000141 WETH | 0.000000 WETH | 0.000004 WETH | 0.000137 WETH (0.2864 €) | — | 2.82 | 0.169 (n=990) | REJECTED | p_lower_below_threshold(0.17<0.75) |
| 53552258 | USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 1,073.308521 USDC | 0.320024 USDC | 0.000000 USDC | 0.009805 USDC | 0.310219 USDC (0.2854 €) | — | 2.89 | 0.169 (n=990) | REJECTED | p_lower_below_threshold(0.17<0.75) |
| 53552258 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→cbBTC→[uniswap_v3]→WETH | 0.502872 WETH | 0.000116 WETH | 0.000000 WETH | 0.000004 WETH | 0.000112 WETH (0.2355 €) | — | 2.23 | 0.169 (n=990) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.17<0.75) |
| 53552258 | cbBTC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→cbBTC | 0.014013 cbBTC | 0.000003 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000003 cbBTC (0.2347 €) | — | 2.39 | 0.169 (n=990) | REJECTED | p_lower_below_threshold(0.17<0.75) |
| 53552258 | USDC→[aerodrome_slipstream]→cbBTC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 1,103.822096 USDC | 0.264249 USDC | 0.000000 USDC | 0.009416 USDC | 0.254833 USDC (0.2344 €) | — | 2.31 | 0.169 (n=990) | REJECTED | p_lower_below_threshold(0.17<0.75) |
| 53552258 | cbBTC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.014087 cbBTC | 0.000003 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000003 cbBTC (0.2328 €) | — | 2.36 | 0.169 (n=990) | REJECTED | p_lower_below_threshold(0.17<0.75) |
| 53552258 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH | 0.490067 WETH | 0.000116 WETH | 0.000000 WETH | 0.000005 WETH | 0.000111 WETH (0.2328 €) | — | 2.27 | 0.169 (n=990) | REJECTED | p_lower_below_threshold(0.17<0.75) |
| 53552258 | USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 1,088.666081 USDC | 0.262671 USDC | 0.000000 USDC | 0.010611 USDC | 0.252060 USDC (0.2319 €) | — | 2.32 | 0.169 (n=990) | REJECTED | p_lower_below_threshold(0.17<0.75) |
| 53552258 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→cbBTC→[uniswap_v3]→WETH | 0.581731 WETH | 0.000114 WETH | 0.000000 WETH | 0.000004 WETH | 0.000110 WETH (0.2306 €) | — | 1.89 | 0.231 (n=391) | REJECTED | below_safety_margin(110029994644477<116346177193278), p_lower_below_threshold(0.23<0.75) |
| 53552258 | cbBTC→[uniswap_v3]→WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→cbBTC | 0.016774 cbBTC | 0.000003 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000003 cbBTC (0.2305 €) | — | 1.96 | 0.231 (n=391) | REJECTED | below_safety_margin(329<335), p_lower_below_threshold(0.23<0.75) |
| 53552258 | USDC→[aerodrome_slipstream]→cbBTC→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 1,318.542935 USDC | 0.259038 USDC | 0.000000 USDC | 0.009012 USDC | 0.250026 USDC (0.2300 €) | — | 1.90 | 0.231 (n=391) | REJECTED | below_safety_margin(250026<263708), p_lower_below_threshold(0.23<0.75) |
| 53552258 | cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.014842 cbBTC | 0.000003 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000003 cbBTC (0.2258 €) | — | 2.17 | 0.169 (n=990) | REJECTED | p_lower_below_threshold(0.17<0.75) |
| 53552258 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.504142 WETH | 0.000112 WETH | 0.000000 WETH | 0.000004 WETH | 0.000108 WETH (0.2255 €) | — | 2.13 | 0.169 (n=990) | REJECTED | p_lower_below_threshold(0.17<0.75) |
| 53552258 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 1,183.432601 USDC | 0.254359 USDC | 0.000000 USDC | 0.009805 USDC | 0.244554 USDC (0.2250 €) | — | 2.07 | 0.169 (n=990) | REJECTED | p_lower_below_threshold(0.17<0.75) |

## Fiabilité et décision
- Observations ghost : 5727 ; taux observé 0.156 ; borne inférieure crédible (0.9) 0.150 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 15.0% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
