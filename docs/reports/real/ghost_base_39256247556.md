# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-19T13:37:03+00:00 ; durée 33.66 min ; blocs 52812825 → 52813837 (1010 vus)

## Connexion
- Requêtes RPC : 12383 ; erreurs : 0 ; latence p50/p95 : 160.0/852.8 ms
- Rafraîchissements d'état : 1011 ; âge des données au dernier bloc : 1.52 s ; changements de frais LP observés (pools à frais dynamiques) : 2371
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 2148 ; cycles déclenchés par événement : 109 ; avance médiane sur le rafraîchissement multicall : 1,027 ms
- Gaz : base fee 0.005093 gwei ; prix ETH (pool le plus profond) : 2,416.97 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 571 pools, 327 jetons, 21004 routes
- Par DEX : uniswap_v3 137, aerodrome 234, aerodrome_slipstream 153, pancakeswap_v3 30, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 207 (rejetés 2) → 612 jetons ; pools candidats 3877 (énumérés 390, par paires 0), mesurés 574, sous le plancher de 10000.0 $ : 3 → gardés 571 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2419.85313, 'AERO': 0.782295, 'cbBTC': 82567.067054}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 148,048,617 | 2,416.973434 | 52813837 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 35,089,885 | 1.275674 | 52813837 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 500 | 18,402,515 | 0.029315 | 52813837 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 17,201,189 | 102.135456 | 52813837 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| aerodrome_slipstream | WETH/cbBTC | 2525 | 11,235,489 | 0.029374 | 52813837 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,400,976 | 0.029384 | 52813837 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,867,059 | 0.000012 | 52813837 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome_slipstream | USDC/cbBTC | 544 | 8,735,993 | 0.000012 | 52813837 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | WETH/USDC | 500 | 8,449,340 | 2,410.828476 | 52813837 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/USDC | 3000 | 8,336,886 | 2,416.624518 | 52813837 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | USDC/cbBTC | 358 | 7,839,225 | 0.000012 | 52813837 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 847 | 7,259,734 | 2,411.203371 | 52813837 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,223,911 | 0.001662 | 52813837 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,361,097 | 0.029316 | 52813837 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | fBOMB/AERO | 10000 | 4,950,070 | 0.025987 | 52813837 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,830,784 | 0.802395 | 52813837 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome_slipstream | USDC/AERO | 10000 | 4,750,431 | 1.281750 | 52813837 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,645,844 | 0.000273 | 52813837 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,439,635 | 2,411.644827 | 52813837 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,368,808 | 0.998770 | 52813837 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 4,040,252 | 33,943.019298 | 52813837 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDT | 472 | 3,459,416 | 2,414.069375 | 52813837 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome | WETH/AERO | 10000 | 3,253,257 | 3,085.307271 | 52813837 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,861,412 | 0.000012 | 52813837 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,747,059 | 405.872538 | 52813837 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,734,185 | 1.142005 | 52813837 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| aerodrome_slipstream | WETH/VVV | 2712 | 2,641,825 | 102.159150 | 52813837 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 2,568,885 | 0.000010 | 52813837 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | WETH/FAI | 10000 | 2,191,248 | 1,235,059.554017 | 52813837 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,062,172 | 1.234881 | 52813837 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | BNKR/WETH | 10000 | 2,052,017 | 0.000000 | 52813837 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,036,743 | 1.372638 | 52813837 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,800,644 | 16.021945 | 52813837 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,773,657 | 0.000012 | 52813837 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | XDP/USDC | 100 | 1,759,579 | 0.018497 | 52813837 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome | weETH_04c0/WETH | 500 | 1,747,671 | 1.105523 | 52813837 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,742,916 | 13,840.094665 | 52813837 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | fBOMB/USDC | 10000 | 1,726,261 | 0.020593 | 52813837 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| aerodrome | WETH/msETH (stable) | 500 | 1,671,716 | 2.308863 | 52813837 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | EURC/USDC | 73 | 1,612,258 | 1.122295 | 52813837 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| uniswap_v3 | WETH/AERO | 3000 | 1,605,621 | 3,084.454034 | 52813837 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,565,496 | 0.916350 | 52813837 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,456,163 | 0.827402 | 52813837 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,339,449 | 0.436285 | 52813837 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,323,456 | 0.000000 | 52813837 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,302,248 | 0.000274 | 52813837 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | WETH/cbBTC | 3000 | 1,289,268 | 0.029380 | 52813837 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,283,082 | 0.004581 | 52813837 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,261,727 | 23.129506 | 52813837 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| aerodrome | USDC/SEND | 3000 | 1,232,868 | 63.930699 | 52813837 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome | WETH/WELL | 10000 | 1,212,584 | 1,077,211.227828 | 52813837 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/doginme | 10000 | 1,205,483 | 35,153,103.776698 | 52813837 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,199,435 | 2,410.901741 | 52813837 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome_slipstream | msUSD/USDC | 500 | 1,177,665 | 0.885970 | 52813837 | `0x7501bc8Bb51616F79bfA524E464fb7B41f0B10fB` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,137,386 | 515,481.870232 | 52813837 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | USDC/NOCK | 3000 | 1,104,114 | 51.686078 | 52813837 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | WETH/msETH | 500 | 1,097,710 | 1.131961 | 52813837 | `0x74F72788F4814D7fF3C49B44684aa98Eee140C0E` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,081,157 | 15.371514 | 52813837 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | WETH/EDEL | 7000 | 1,057,556 | 89,969.561115 | 52813837 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,057,165 | 22,041,739.332313 | 52813837 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |

## Recherche d'opportunités
- Cycles : 1119 ; routes examinées : 23503476 ; candidats optimisés : 173784 ; net attendu > 0 : 24 ; dernier cycle 453.7 ms
- Rejets (moteur) : {'spread_below_threshold': 23098864, 'liquidity_below_min': 205043, 'negative_expected_net': 173760, 'borrow_bound_too_small': 25785}
- Enregistrements de la session : 173784 ; net attendu > 0 : 24 ; simulés (eth_call de la vraie tx) : 0 (ok 0, échec 0) ; étiquettes ghost N+1 : 0/0 positives
- Décisions : {'REJECTED': 173784} ; motifs de rejet : {'below_safety_margin': 24, 'negative_expected_net': 173760, 'p_lower_below_threshold': 24}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52813804 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.004144 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0013 €) | — | 1.43 | 0.098 (n=146) | REJECTED | below_safety_margin(593942958774<828825150175), p_lower_below_threshold(0.10<0.75) |
| 52813805 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.004152 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0013 €) | — | 1.41 | 0.098 (n=146) | REJECTED | below_safety_margin(584409191829<830362453590), p_lower_below_threshold(0.10<0.75) |
| 52813804 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 9.949683 USDC | 0.008698 USDC | 0.000000 USDC | 0.007286 USDC | 0.001412 USDC (0.0013 €) | — | 1.42 | 0.098 (n=146) | REJECTED | below_safety_margin(1412<1989), p_lower_below_threshold(0.10<0.75) |
| 52813805 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 9.947531 USDC | 0.008686 USDC | 0.000000 USDC | 0.007297 USDC | 0.001389 USDC (0.0013 €) | — | 1.40 | 0.098 (n=146) | REJECTED | below_safety_margin(1389<1989), p_lower_below_threshold(0.10<0.75) |
| 52813831 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.003994 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0008 €) | — | 0.92 | 0.098 (n=146) | REJECTED | below_safety_margin(368875072634<798842227760), p_lower_below_threshold(0.10<0.75) |
| 52813831 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 9.628025 USDC | 0.008157 USDC | 0.000000 USDC | 0.007287 USDC | 0.000870 USDC (0.0008 €) | — | 0.90 | 0.098 (n=146) | REJECTED | below_safety_margin(870<1925), p_lower_below_threshold(0.10<0.75) |
| 52813831 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.003974 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0007 €) | — | 0.80 | 0.282 (n=68) | REJECTED | below_safety_margin(318936575720<794817108183), p_lower_below_threshold(0.28<0.75) |
| 52813831 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 9.536565 USDC | 0.008036 USDC | 0.000000 USDC | 0.007287 USDC | 0.000749 USDC (0.0007 €) | — | 0.79 | 0.282 (n=68) | REJECTED | below_safety_margin(749<1907), p_lower_below_threshold(0.28<0.75) |
| 52813831 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.003464 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0006 €) | — | 0.82 | 0.282 (n=68) | REJECTED | below_safety_margin(285583276218<692862386630), p_lower_below_threshold(0.28<0.75) |
| 52813798 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.003957 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0006 €) | — | 0.70 | 0.282 (n=68) | REJECTED | below_safety_margin(278376931757<791377318253), p_lower_below_threshold(0.28<0.75) |
| 52813831 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 8.304169 USDC | 0.007957 USDC | 0.000000 USDC | 0.007287 USDC | 0.000670 USDC (0.0006 €) | — | 0.81 | 0.282 (n=68) | REJECTED | below_safety_margin(670<1660), p_lower_below_threshold(0.28<0.75) |
| 52813798 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 9.536940 USDC | 0.007936 USDC | 0.000000 USDC | 0.007285 USDC | 0.000651 USDC (0.0006 €) | — | 0.68 | 0.282 (n=68) | REJECTED | below_safety_margin(651<1907), p_lower_below_threshold(0.28<0.75) |
| 52813806 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.003949 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0005 €) | — | 0.62 | 0.282 (n=68) | REJECTED | below_safety_margin(244560031629<789881455488), p_lower_below_threshold(0.28<0.75) |
| 52813805 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.003949 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0005 €) | — | 0.61 | 0.282 (n=68) | REJECTED | below_safety_margin(239976250042<789881455488), p_lower_below_threshold(0.28<0.75) |
| 52813806 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 9.535538 USDC | 0.007856 USDC | 0.000000 USDC | 0.007286 USDC | 0.000570 USDC (0.0005 €) | — | 0.60 | 0.282 (n=68) | REJECTED | below_safety_margin(570<1907), p_lower_below_threshold(0.28<0.75) |
| 52813805 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 9.535538 USDC | 0.007856 USDC | 0.000000 USDC | 0.007297 USDC | 0.000559 USDC (0.0005 €) | — | 0.59 | 0.282 (n=68) | REJECTED | below_safety_margin(559<1907), p_lower_below_threshold(0.28<0.75) |
| 52813806 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.003898 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0004 €) | — | 0.40 | 0.098 (n=146) | REJECTED | below_safety_margin(157735730047<779506605458), p_lower_below_threshold(0.10<0.75) |
| 52813806 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 9.314590 USDC | 0.007647 USDC | 0.000000 USDC | 0.007286 USDC | 0.000361 USDC (0.0003 €) | — | 0.39 | 0.098 (n=146) | REJECTED | below_safety_margin(361<1862), p_lower_below_threshold(0.10<0.75) |
| 52813830 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.003857 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0003 €) | — | 0.33 | 0.282 (n=68) | REJECTED | below_safety_margin(125500650883<771339062131), p_lower_below_threshold(0.28<0.75) |
| 52813830 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 9.235630 USDC | 0.007570 USDC | 0.000000 USDC | 0.007287 USDC | 0.000283 USDC (0.0003 €) | — | 0.31 | 0.282 (n=68) | REJECTED | below_safety_margin(283<1847), p_lower_below_threshold(0.28<0.75) |
| 52813804 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.003813 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0001 €) | — | 0.15 | 0.282 (n=68) | REJECTED | below_safety_margin(57194289791<762504296807), p_lower_below_threshold(0.28<0.75) |
| 52813804 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 9.158915 USDC | 0.007405 USDC | 0.000000 USDC | 0.007286 USDC | 0.000119 USDC (0.0001 €) | — | 0.13 | 0.282 (n=68) | REJECTED | below_safety_margin(119<1831), p_lower_below_threshold(0.28<0.75) |
| 52813830 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.003824 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0001 €) | — | 0.12 | 0.098 (n=146) | REJECTED | below_safety_margin(45249568251<764866609046), p_lower_below_threshold(0.10<0.75) |
| 52813830 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 9.158733 USDC | 0.007377 USDC | 0.000000 USDC | 0.007287 USDC | 0.000090 USDC (0.0001 €) | — | 0.10 | 0.098 (n=146) | REJECTED | below_safety_margin(90<1831), p_lower_below_threshold(0.10<0.75) |

## Fiabilité et décision
- Observations ghost : 1270 ; taux observé 0.103 ; borne inférieure crédible (0.9) 0.093 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 9.3% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
