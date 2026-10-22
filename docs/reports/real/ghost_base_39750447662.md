# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-22T09:18:21+00:00 ; durée 24.42 min ; blocs 52934940 → 52935675 (706 vus)

## Connexion
- Requêtes RPC : 8480 ; erreurs : 0 ; latence p50/p95 : 268.1/1,780.4 ms
- Rafraîchissements d'état : 706 ; âge des données au dernier bloc : 3.51 s ; changements de frais LP observés (pools à frais dynamiques) : 1616
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 2176 ; cycles déclenchés par événement : 171 ; avance médiane sur le rafraîchissement multicall : 1,143 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,401.54 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 552 pools, 321 jetons, 20574 routes
- Par DEX : uniswap_v3 136, aerodrome 228, aerodrome_slipstream 141, pancakeswap_v3 31, uniswap_v2 13, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 201 (rejetés 2) → 606 jetons ; pools candidats 3839 (énumérés 370, par paires 0), mesurés 554, sous le plancher de 10000.0 $ : 2 → gardés 552 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'DAI': 1.0, 'USDC': 1.0, 'WETH': 2409.153844, 'AERO': 0.798022, 'cbBTC': 81873.188532}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 155,127,648 | 2,401.542058 | 52935676 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 23,278,067 | 1.251130 | 52935676 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| aerodrome | WETH/VVV | 3000 | 16,302,662 | 86.153214 | 52935676 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,242,976 | 0.029370 | 52935676 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,249,532 | 0.029425 | 52935676 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| aerodrome_slipstream | WETH/cbBTC | 2510 | 9,567,884 | 0.029411 | 52935676 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,409,648 | 0.000012 | 52935676 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 8,636,382 | 2,403.589393 | 52935676 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/USDC | 3000 | 7,325,482 | 2,400.314967 | 52935676 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,155,024 | 0.001658 | 52935676 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 348 | 7,045,366 | 0.000012 | 52935676 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 150 | 5,978,166 | 2,403.591604 | 52935676 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | USDC/cbBTC | 496 | 5,674,974 | 0.000012 | 52935676 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,404,234 | 0.029381 | 52935676 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,568,607 | 2,403.423409 | 52935676 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,299,555 | 1.000001 | 52935676 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,986,565 | 34,408.292483 | 52935676 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | VIRTUAL/WETH | 10000 | 3,936,768 | 0.000275 | 52935676 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/USDT | 427 | 2,863,693 | 2,407.557472 | 52935676 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome_slipstream | WETH/VVV | 2823 | 2,633,827 | 86.173872 | 52935676 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | WETH/AERO | 10000 | 2,370,961 | 3,001.164909 | 52935676 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,305,900 | 396.838521 | 52935676 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,223,774 | 0.000012 | 52935676 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | WETH/FAI | 10000 | 2,200,148 | 1,208,738.451617 | 52935676 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 2,069,341 | 0.000012 | 52935676 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,900,993 | 0.000000 | 52935676 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,799,997 | 0.018611 | 52935676 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,662,906 | 1.531778 | 52935676 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | WETH/AERO | 3000 | 1,625,151 | 3,008.690858 | 52935676 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,455,301 | 0.822251 | 52935676 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,415,275 | 13,521.138099 | 52935676 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,356,022 | 0.004897 | 52935676 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome | WETH/msETH (stable) | 500 | 1,327,684 | 2.337629 | 52935676 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | DRB/WETH | 10000 | 1,301,258 | 0.000000 | 52935676 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,299,246 | 0.000273 | 52935676 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | USDC/alUSDb (stable) | 500 | 1,296,866 | 1.399491 | 52935676 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,275,276 | 2,403.429764 | 52935676 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,230,614 | 64.165025 | 52935676 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 1,228,971 | 0.000010 | 52935676 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v3 | WETH/doginme | 10000 | 1,193,448 | 35,523,450.941110 | 52935676 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,189,644 | 16.268604 | 52935676 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | WETH/WELL | 10000 | 1,187,710 | 1,086,059.546510 | 52935676 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome | fBOMB/AERO | 10000 | 1,157,129 | 0.023215 | 52935676 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome | USDC/NOCK | 3000 | 1,155,908 | 47.154769 | 52935676 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,147,751 | 503,008.258857 | 52935676 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | WETH/EDEL | 7000 | 1,133,420 | 71,232.276910 | 52935676 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | fBOMB/USDC | 10000 | 1,102,511 | 0.018834 | 52935676 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| aerodrome | weETH_04c0/WETH | 500 | 1,097,202 | 1.105754 | 52935676 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,061,660 | 21,447,301.659841 | 52935676 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,037,110 | 17.160635 | 52935676 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | WETH/cbBTC | 3000 | 1,020,050 | 0.029424 | 52935676 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,013,813 | 23.189410 | 52935676 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| uniswap_v3 | USDC/VVV | 3000 | 1,009,096 | 0.035847 | 52935676 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome_slipstream | WETH/wstETH | 90 | 964,845 | 0.802250 | 52935676 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| uniswap_v3 | WETH/MORPHO | 3000 | 953,805 | 1,061.896842 | 52935676 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome_slipstream | EURC/USDC | 70 | 943,236 | 1.123613 | 52935676 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| uniswap_v3 | WETH/USDC | 10000 | 932,022 | 2,417.961824 | 52935676 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | uXRP/WETH | 3000 | 918,085 | 0.000551 | 52935676 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome | WETH/bsdETH | 100 | 894,532 | 0.916123 | 52935676 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 886,953 | 17.659460 | 52935676 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |

## Recherche d'opportunités
- Cycles : 876 ; routes examinées : 18022824 ; candidats optimisés : 134418 ; net attendu > 0 : 96 ; dernier cycle 681.3 ms
- Rejets (moteur) : {'spread_below_threshold': 17697749, 'liquidity_below_min': 186275, 'negative_expected_net': 134322, 'cycle_budget_exhausted': 3506, 'borrow_bound_too_small': 876}
- Enregistrements de la session : 134418 ; net attendu > 0 : 96 ; simulés (eth_call de la vraie tx) : 6 (ok 6, échec 0) ; étiquettes ghost N+1 : 0/6 positives
- Décisions : {'REJECTED': 134418} ; motifs de rejet : {'below_safety_margin': 44, 'negative_expected_net': 134322, 'p_lower_below_threshold': 73, 'reliability_not_demonstrated': 23}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52935498 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.359582 WETH | 0.000108 WETH | 0.000000 WETH | 0.000002 WETH | 0.000106 WETH (0.2336 €) | 0.000106 WETH | 2.94 | 0.023 (n=63) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 52935498 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 860.319661 USDC | 0.259021 USDC | 0.000000 USDC | 0.005776 USDC | 0.253245 USDC (0.2330 €) | — | 2.94 | 0.023 (n=63) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 52935498 | WETH→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.103454 WETH | 0.000046 WETH | 0.000000 WETH | 0.000003 WETH | 0.000043 WETH (0.0950 €) | 0.000043 WETH | 4.15 | 0.130 (n=91) | REJECTED | p_lower_below_threshold(0.13<0.75) |
| 52935498 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→USDC | 247.137886 USDC | 0.110224 USDC | 0.000000 USDC | 0.007240 USDC | 0.102984 USDC (0.0947 €) | — | 4.17 | 0.130 (n=91) | REJECTED | p_lower_below_threshold(0.13<0.75) |
| 52935498 | WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.110845 WETH | 0.000037 WETH | 0.000000 WETH | 0.000003 WETH | 0.000034 WETH (0.0749 €) | 0.000034 WETH | 3.06 | 0.130 (n=91) | REJECTED | p_lower_below_threshold(0.13<0.75) |
| 52935498 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC | 263.716609 USDC | 0.088432 USDC | 0.000000 USDC | 0.007240 USDC | 0.081192 USDC (0.0747 €) | — | 3.08 | 0.130 (n=91) | REJECTED | p_lower_below_threshold(0.13<0.75) |
| 52935498 | WETH→[uniswap_v3]→USDT→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.106674 WETH | 0.000034 WETH | 0.000000 WETH | 0.000003 WETH | 0.000031 WETH (0.0696 €) | — | 2.95 | 0.108 (n=213) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 52935498 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→USDT→[pancakeswap_v3]→USDC | 255.548137 USDC | 0.082668 USDC | 0.000000 USDC | 0.007240 USDC | 0.075428 USDC (0.0694 €) | — | 2.95 | 0.108 (n=213) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 52935498 | WETH→[uniswap_v3]→USDT→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.105463 WETH | 0.000034 WETH | 0.000000 WETH | 0.000003 WETH | 0.000031 WETH (0.0678 €) | — | 2.91 | 0.243 (n=108) | REJECTED | p_lower_below_threshold(0.24<0.75) |
| 52935498 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→USDT→[uniswap_v3]→USDC | 252.097328 USDC | 0.080721 USDC | 0.000000 USDC | 0.007240 USDC | 0.073481 USDC (0.0676 €) | — | 2.91 | 0.243 (n=108) | REJECTED | p_lower_below_threshold(0.24<0.75) |
| 52935239 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.442022 WETH | 0.000026 WETH | 0.000000 WETH | 0.000002 WETH | 0.000023 WETH (0.0512 €) | — | 0.52 | 0.023 (n=63) | REJECTED | below_safety_margin(23119777902019<88404477608296), p_lower_below_threshold(0.02<0.75) |
| 52935239 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 1,060.890223 USDC | 0.061330 USDC | 0.000000 USDC | 0.005790 USDC | 0.055540 USDC (0.0511 €) | — | 0.52 | 0.023 (n=63) | REJECTED | below_safety_margin(55540<212178), p_lower_below_threshold(0.02<0.75) |
| 52935498 | WETH→[pancakeswap_v3]→EURC→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.038279 WETH | 0.000014 WETH | 0.000000 WETH | 0.000003 WETH | 0.000011 WETH (0.0248 €) | — | 2.94 | 0.108 (n=213) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 52935498 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→EURC→[aerodrome_slipstream]→USDC | 91.454084 USDC | 0.034148 USDC | 0.000000 USDC | 0.007240 USDC | 0.026908 USDC (0.0248 €) | — | 2.94 | 0.108 (n=213) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 52935498 | WETH→[pancakeswap_v3]→EURC→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.037520 WETH | 0.000014 WETH | 0.000000 WETH | 0.000003 WETH | 0.000011 WETH (0.0235 €) | — | 2.83 | 0.108 (n=213) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 52935498 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→EURC→[aerodrome_slipstream]→USDC | 89.499962 USDC | 0.032688 USDC | 0.000000 USDC | 0.007240 USDC | 0.025448 USDC (0.0234 €) | — | 2.84 | 0.108 (n=213) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 52935498 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.001694 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0226 €) | — | 1.77 | 0.108 (n=213) | REJECTED | below_safety_margin(30<33), p_lower_below_threshold(0.11<0.75) |
| 52935498 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.065048 WETH | 0.000013 WETH | 0.000000 WETH | 0.000003 WETH | 0.000010 WETH (0.0220 €) | — | 1.53 | 0.108 (n=213) | REJECTED | below_safety_margin(9956231407816<13009642859783), p_lower_below_threshold(0.11<0.75) |
| 52935498 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 138.515843 USDC | 0.031120 USDC | 0.000000 USDC | 0.007240 USDC | 0.023880 USDC (0.0220 €) | — | 1.72 | 0.108 (n=213) | REJECTED | below_safety_margin(23880<27703), p_lower_below_threshold(0.11<0.75) |
| 52935498 | WETH→[aerodrome]→OVER→[aerodrome]→USDC→[uniswap_v3]→WETH | 0.011471 WETH | 0.000012 WETH | 0.000000 WETH | 0.000003 WETH | 0.000010 WETH (0.0215 €) | — | 8.47 | 0.011 (n=130) | REJECTED | p_lower_below_threshold(0.01<0.75) |
| 52935498 | USDC→[uniswap_v3]→WETH→[aerodrome]→OVER→[aerodrome]→USDC | 27.437190 USDC | 0.029828 USDC | 0.000000 USDC | 0.006577 USDC | 0.023251 USDC (0.0214 €) | — | 8.47 | 0.011 (n=130) | REJECTED | p_lower_below_threshold(0.01<0.75) |
| 52935498 | WETH→[aerodrome]→MET→[aerodrome]→USDC→[uniswap_v3]→WETH | 0.013682 WETH | 0.000011 WETH | 0.000000 WETH | 0.000003 WETH | 0.000008 WETH (0.0173 €) | — | 5.74 | 0.032 (n=133) | REJECTED | p_lower_below_threshold(0.03<0.75) |
| 52935498 | USDC→[uniswap_v3]→WETH→[aerodrome]→MET→[aerodrome]→USDC | 32.713378 USDC | 0.025360 USDC | 0.000000 USDC | 0.006577 USDC | 0.018783 USDC (0.0173 €) | — | 5.74 | 0.032 (n=133) | REJECTED | p_lower_below_threshold(0.03<0.75) |
| 52935498 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.006913 WETH | 0.000010 WETH | 0.000000 WETH | 0.000003 WETH | 0.000007 WETH (0.0157 €) | — | 10.28 | 0.000 (n=28) | REJECTED | reliability_not_demonstrated |
| 52935498 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 16.439524 USDC | 0.024244 USDC | 0.000000 USDC | 0.007240 USDC | 0.017004 USDC (0.0156 €) | — | 10.34 | 0.000 (n=28) | REJECTED | reliability_not_demonstrated |

## Fiabilité et décision
- Observations ghost : 1850 ; taux observé 0.095 ; borne inférieure crédible (0.9) 0.087 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 8.7% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
