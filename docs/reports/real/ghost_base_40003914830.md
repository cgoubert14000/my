# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-23T22:49:24+00:00 ; durée 252.94 min ; blocs 52995614 → 53003204 (7093 vus)

## Connexion
- Requêtes RPC : 86450 ; erreurs : 118 ; latence p50/p95 : 309.5/2,002.0 ms
- Rafraîchissements d'état : 7094 ; âge des données au dernier bloc : 1.39 s ; changements de frais LP observés (pools à frais dynamiques) : 11468
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 55309 ; cycles déclenchés par événement : 3954 ; avance médiane sur le rafraîchissement multicall : 897 ms
- Gaz : base fee 0.005278 gwei ; prix ETH (pool le plus profond) : 2,372.99 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 546 pools, 317 jetons, 19488 routes
- Par DEX : uniswap_v3 138, aerodrome 222, aerodrome_slipstream 137, pancakeswap_v3 32, uniswap_v2 13, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 200 (rejetés 2) → 605 jetons ; pools candidats 3880 (énumérés 359, par paires 0), mesurés 548, sous le plancher de 10000.0 $ : 2 → gardés 546 (max 1500) ; prix des hubs : {'USDC': 1.0, 'DAI': 1.0, 'USDbC': 1.0, 'WETH': 2404.297357, 'AERO': 0.765849, 'cbBTC': 81434.30056}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 156,046,703 | 2,372.994170 | 53003204 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,404,991 | 0.029292 | 53003204 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 12,411,389 | 96.057313 | 53003204 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,181,360 | 0.029359 | 53003204 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| aerodrome | USDC/AERO | 3000 | 10,000,565 | 1.361491 | 53003204 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,751,070 | 0.000012 | 53003204 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome_slipstream | WETH/cbBTC | 2610 | 8,756,067 | 0.029351 | 53003204 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/USDC | 500 | 8,624,287 | 2,368.125401 | 53003204 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,081,088 | 0.001652 | 53003204 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 372 | 6,317,724 | 0.000012 | 53003204 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 1235 | 5,509,293 | 2,367.369597 | 53003204 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,394,396 | 0.029297 | 53003204 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | USDC/cbBTC | 600 | 4,884,768 | 0.000012 | 53003204 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,505,364 | 2,368.396909 | 53003204 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,263,932 | 0.999388 | 53003204 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/USDC | 3000 | 4,201,256 | 2,372.940088 | 53003204 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome | WETH/KTA | 3000 | 3,940,891 | 34,351.203637 | 53003204 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | VIRTUAL/WETH | 10000 | 3,345,210 | 0.000272 | 53003204 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/USDT | 532 | 2,789,750 | 2,372.480216 | 53003204 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome_slipstream | WETH/VVV | 2700 | 2,493,677 | 96.060937 | 53003204 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,265,757 | 402.900591 | 53003204 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | WETH/FAI | 10000 | 2,159,420 | 1,224,301.247088 | 53003204 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome | WETH/AERO | 10000 | 2,013,914 | 3,218.162269 | 53003204 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,930,312 | 0.000000 | 53003204 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,924,376 | 0.000012 | 53003204 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,739,928 | 0.000012 | 53003204 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | XDP/USDC | 100 | 1,735,602 | 0.017397 | 53003204 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,555,660 | 1.605883 | 53003204 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | WETH/AERO | 3000 | 1,496,283 | 3,230.581949 | 53003204 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,460,261 | 0.824379 | 53003204 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,393,596 | 13,739.336214 | 53003204 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,371,051 | 0.005034 | 53003204 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,281,620 | 2,367.984611 | 53003204 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,277,098 | 0.000270 | 53003204 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| uniswap_v3 | DRB/WETH | 10000 | 1,249,044 | 0.000000 | 53003204 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | WETH/msETH (stable) | 500 | 1,243,099 | 2.306692 | 53003204 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome | USDC/SEND | 3000 | 1,227,434 | 64.498001 | 53003204 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,180,223 | 35,609,935.701366 | 53003204 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | WETH/WELL | 10000 | 1,156,993 | 1,108,212.811609 | 53003204 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,138,579 | 490,887.331496 | 53003204 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | USDC/NOCK | 3000 | 1,132,868 | 48.817794 | 53003204 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,122,871 | 16.453877 | 53003204 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | WETH/EDEL | 7000 | 1,074,275 | 74,813.349521 | 53003204 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | USDC/VVV | 3000 | 1,056,753 | 0.040396 | 53003204 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,043,884 | 21,642,564.575133 | 53003204 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,037,721 | 17.086368 | 53003204 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 974,788 | 23.150386 | 53003204 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| uniswap_v3 | WETH/MORPHO | 3000 | 943,640 | 1,061.115863 | 53003204 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/USDC | 10000 | 935,314 | 2,389.873742 | 53003204 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | uXRP/WETH | 3000 | 904,265 | 0.000544 | 53003204 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | USDC/SAPIEN | 4725 | 883,596 | 17.784482 | 53003204 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 877,092 | 0.000009 | 53003204 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v2 | WETH/USDC | 3000 | 854,382 | 2,373.840905 | 53003204 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| pancakeswap_v3 | QUID/USDC | 100 | 831,009 | 0.062286 | 53003204 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | weETH_04c0/WETH | 500 | 820,452 | 1.105909 | 53003204 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome | WETH/wstETH | 3000 | 803,413 | 0.803225 | 53003204 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | WETH/VVV | 10000 | 782,790 | 95.404362 | 53003204 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 768,007 | 0.638907 | 53003204 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 761,395 | 4,583,449.917205 | 53003204 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 735,734 | 0.678119 | 53003204 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |

## Recherche d'opportunités
- Cycles : 11047 ; routes examinées : 215283936 ; candidats optimisés : 923234 ; net attendu > 0 : 345 ; dernier cycle 369.2 ms
- Rejets (moteur) : {'spread_below_threshold': 211099822, 'liquidity_below_min': 3247919, 'negative_expected_net': 922889, 'borrow_bound_too_small': 11046, 'cycle_budget_exhausted': 1915}
- Enregistrements de la session : 923234 ; net attendu > 0 : 345 ; simulés (eth_call de la vraie tx) : 14 (ok 11, échec 3) ; étiquettes ghost N+1 : 1/12 positives
- Décisions : {'REJECTED': 923234} ; motifs de rejet : {'below_safety_margin': 250, 'negative_expected_net': 922889, 'p_lower_below_threshold': 313, 'reliability_not_demonstrated': 32, 'simulation_failed': 3, 'stale_data': 17}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52997859 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.013052 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.1048 €) | — | 1.07 | 0.001 (n=7) | REJECTED | below_safety_margin(140<261), reliability_not_demonstrated |
| 52997859 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.013052 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.1048 €) | — | 1.07 | 0.001 (n=7) | REJECTED | below_safety_margin(140<261), reliability_not_demonstrated |
| 52997859 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.469736 WETH | 0.000051 WETH | 0.000000 WETH | 0.000003 WETH | 0.000047 WETH (0.1044 €) | — | 1.01 | 0.001 (n=7) | REJECTED | below_safety_margin(47310295624478<93947291756440), reliability_not_demonstrated |
| 52997859 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.469736 WETH | 0.000051 WETH | 0.000000 WETH | 0.000003 WETH | 0.000047 WETH (0.1044 €) | — | 1.01 | 0.001 (n=7) | REJECTED | below_safety_margin(47310295624478<93947291756440), reliability_not_demonstrated |
| 52997859 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 1,085.695509 USDC | 0.121282 USDC | 0.000000 USDC | 0.007951 USDC | 0.113331 USDC (0.1043 €) | — | 1.04 | 0.001 (n=7) | REJECTED | below_safety_margin(113331<217139), reliability_not_demonstrated |
| 52997859 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 1,085.695509 USDC | 0.121282 USDC | 0.000000 USDC | 0.007951 USDC | 0.113331 USDC (0.1043 €) | — | 1.04 | 0.001 (n=7) | REJECTED | below_safety_margin(113331<217139), reliability_not_demonstrated |
| 52997059 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 67.235756 USDC | 0.069204 USDC | 0.000000 USDC | 0.005568 USDC | 0.063636 USDC (0.0585 €) | — | 9.46 | 0.000 (n=48) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 52997045 | WETH→[pancakeswap_v3]→AERO→[aerodrome]→BRETT→[aerodrome_slipstream]→WETH | 0.011664 WETH | 0.000026 WETH | 0.000000 WETH | 0.000003 WETH | 0.000024 WETH (0.0519 €) | 0.000024 WETH | 20.17 | 0.001 (n=10) | REJECTED | reliability_not_demonstrated |
| 53003161 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→WETH | 0.078367 WETH | 0.000026 WETH | 0.000000 WETH | 0.000002 WETH | 0.000023 WETH (0.0509 €) | 0.000023 WETH | 2.96 | 0.020 (n=72) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 53003161 | cbBTC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC | 0.002264 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0508 €) | — | 3.00 | 0.003 (n=109) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53003161 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome]→cbBTC | 0.000776 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0261 €) | — | 4.51 | 0.018 (n=44) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 53003161 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome]→cbBTC | 0.000746 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0261 €) | — | 4.69 | 0.018 (n=44) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 53003161 | USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome]→cbBTC→[pancakeswap_v3]→USDC | 63.040420 USDC | 0.035206 USDC | 0.000000 USDC | 0.007203 USDC | 0.028003 USDC (0.0258 €) | — | 4.44 | 0.018 (n=44) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 53003161 | USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome]→cbBTC→[pancakeswap_v3]→USDC | 66.238683 USDC | 0.034672 USDC | 0.000000 USDC | 0.007203 USDC | 0.027469 USDC (0.0253 €) | — | 4.15 | 0.018 (n=44) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 53003161 | cbBTC→[uniswap_v3]→USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome]→cbBTC | 0.000693 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0231 €) | — | 4.47 | 0.023 (n=36) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 53003161 | USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome]→cbBTC→[uniswap_v3]→USDC | 56.595939 USDC | 0.031856 USDC | 0.000000 USDC | 0.007203 USDC | 0.024653 USDC (0.0227 €) | — | 4.36 | 0.023 (n=36) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 53003161 | cbBTC→[aerodrome_slipstream]→WETH→[uniswap_v3]→WBTC→[uniswap_v3]→cbBTC | 0.000688 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0224 €) | — | 4.36 | 0.122 (n=111) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 53003161 | cbBTC→[uniswap_v3]→USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome]→cbBTC | 0.000659 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0224 €) | — | 4.56 | 0.023 (n=36) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 53003161 | cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome]→cbBTC | 0.000666 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0224 €) | — | 4.51 | 0.023 (n=36) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 53003161 | USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome]→cbBTC→[uniswap_v3]→USDC | 64.704429 USDC | 0.031404 USDC | 0.000000 USDC | 0.007203 USDC | 0.024201 USDC (0.0223 €) | — | 3.74 | 0.023 (n=36) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 53003161 | USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome]→cbBTC→[aerodrome_slipstream]→USDC | 63.040420 USDC | 0.031231 USDC | 0.000000 USDC | 0.007203 USDC | 0.024028 USDC (0.0221 €) | — | 3.81 | 0.023 (n=36) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 53003161 | WETH→[uniswap_v3]→WBTC→[uniswap_v3]→cbBTC→[aerodrome_slipstream]→WETH | 0.026473 WETH | 0.000013 WETH | 0.000000 WETH | 0.000003 WETH | 0.000010 WETH (0.0221 €) | 0.000010 WETH | 3.81 | 0.122 (n=111) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 53003161 | WETH→[uniswap_v3]→WBTC→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.020525 WETH | 0.000013 WETH | 0.000000 WETH | 0.000003 WETH | 0.000010 WETH (0.0220 €) | 0.000010 WETH | 4.89 | 0.099 (n=216) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53003161 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→WBTC→[uniswap_v3]→USDC | 48.187956 USDC | 0.031048 USDC | 0.000000 USDC | 0.007170 USDC | 0.023878 USDC (0.0220 €) | — | 4.96 | 0.099 (n=216) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53003161 | cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome]→cbBTC | 0.000668 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0217 €) | — | 4.34 | 0.023 (n=36) | REJECTED | p_lower_below_threshold(0.02<0.75) |

## Fiabilité et décision
- Observations ghost : 2061 ; taux observé 0.096 ; borne inférieure crédible (0.9) 0.088 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 8.8% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
