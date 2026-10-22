# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-22T10:04:35+00:00 ; durée 70.65 min ; blocs 52934940 → 52937060 (2056 vus)

## Connexion
- Requêtes RPC : 24480 ; erreurs : 10 ; latence p50/p95 : 354.1/1,993.1 ms
- Rafraîchissements d'état : 2056 ; âge des données au dernier bloc : 6.26 s ; changements de frais LP observés (pools à frais dynamiques) : 3705
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 2176 ; cycles déclenchés par événement : 171 ; avance médiane sur le rafraîchissement multicall : 1,143 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,403.88 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 552 pools, 321 jetons, 20574 routes
- Par DEX : uniswap_v3 136, aerodrome 228, aerodrome_slipstream 141, pancakeswap_v3 31, uniswap_v2 13, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 201 (rejetés 2) → 606 jetons ; pools candidats 3839 (énumérés 370, par paires 0), mesurés 554, sous le plancher de 10000.0 $ : 2 → gardés 552 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'DAI': 1.0, 'USDC': 1.0, 'WETH': 2409.153844, 'AERO': 0.798022, 'cbBTC': 81873.188532}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 155,392,838 | 2,403.876543 | 52937062 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 23,093,247 | 1.253263 | 52937062 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| aerodrome | WETH/VVV | 3000 | 16,318,998 | 86.025553 | 52937062 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,271,084 | 0.029387 | 52937062 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,256,849 | 0.029423 | 52937062 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 9,568,377 | 0.029408 | 52937062 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,413,518 | 0.000012 | 52937062 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 8,631,496 | 2,408.452281 | 52937062 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,169,378 | 0.001663 | 52937062 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | WETH/USDC | 3000 | 7,166,349 | 2,403.882762 | 52937062 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | USDC/cbBTC | 358 | 7,045,419 | 0.000012 | 52937062 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 150 | 5,965,427 | 2,409.693052 | 52937062 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | USDC/cbBTC | 556 | 5,665,737 | 0.000012 | 52937062 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,410,200 | 0.029391 | 52937062 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,548,157 | 2,409.454576 | 52937062 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,301,221 | 1.000001 | 52937062 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,999,526 | 34,252.141227 | 52937062 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | VIRTUAL/WETH | 10000 | 3,940,408 | 0.000275 | 52937062 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/USDT | 448 | 2,917,866 | 2,413.781266 | 52937062 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome_slipstream | WETH/VVV | 2775 | 2,637,638 | 85.985691 | 52937062 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | WETH/AERO | 10000 | 2,361,035 | 3,001.164909 | 52937062 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,310,229 | 395.728943 | 52937062 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,224,957 | 0.000012 | 52937062 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | WETH/FAI | 10000 | 2,202,906 | 1,208,059.202138 | 52937062 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 2,069,896 | 0.000012 | 52937062 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,902,308 | 0.000000 | 52937062 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,799,635 | 0.018596 | 52937062 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,662,906 | 1.531778 | 52937062 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | WETH/AERO | 3000 | 1,625,226 | 3,016.798855 | 52937062 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,455,301 | 0.822251 | 52937062 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,417,582 | 13,471.823421 | 52937062 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,378,233 | 0.005024 | 52937062 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome | WETH/msETH (stable) | 500 | 1,332,360 | 2.328802 | 52937062 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,300,516 | 0.000275 | 52937062 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,275,746 | 2,409.841894 | 52937062 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | DRB/WETH | 10000 | 1,261,496 | 0.000000 | 52937062 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | USDC/SEND | 3000 | 1,229,993 | 64.229854 | 52937062 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 1,225,430 | 0.000010 | 52937062 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v3 | WETH/doginme | 10000 | 1,194,509 | 35,532,300.267632 | 52937062 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,191,929 | 16.241820 | 52937062 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | WETH/WELL | 10000 | 1,187,937 | 1,087,661.462619 | 52937062 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome | USDC/NOCK | 3000 | 1,164,703 | 46.445322 | 52937062 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome | fBOMB/AERO | 10000 | 1,151,149 | 0.023224 | 52937062 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,148,865 | 503,010.454864 | 52937062 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | WETH/EDEL | 7000 | 1,132,205 | 71,222.619333 | 52937062 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | fBOMB/USDC | 10000 | 1,102,478 | 0.018834 | 52937062 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| aerodrome | weETH_04c0/WETH | 500 | 1,098,268 | 1.105754 | 52937062 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,062,692 | 21,447,301.659841 | 52937062 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,036,283 | 17.197863 | 52937062 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | WETH/cbBTC | 3000 | 1,020,743 | 0.029424 | 52937062 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,011,230 | 23.127506 | 52937062 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| uniswap_v3 | USDC/VVV | 3000 | 1,010,820 | 0.035674 | 52937062 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/MORPHO | 3000 | 953,934 | 1,061.158665 | 52937062 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/USDC | 10000 | 932,399 | 2,417.961824 | 52937062 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | uXRP/WETH | 3000 | 918,977 | 0.000551 | 52937062 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | EURC/USDC | 73 | 909,923 | 1.122094 | 52937062 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| aerodrome | WETH/bsdETH | 100 | 895,401 | 0.916123 | 52937062 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome_slipstream | USDC/SAPIEN | 4635 | 889,186 | 17.586616 | 52937062 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v2 | WETH/USDC | 3000 | 876,374 | 2,403.780681 | 52937062 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 817,344 | 1.106146 | 52937062 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |

## Recherche d'opportunités
- Cycles : 2226 ; routes examinées : 45797724 ; candidats optimisés : 258304 ; net attendu > 0 : 96 ; dernier cycle 895.1 ms
- Rejets (moteur) : {'spread_below_threshold': 45089291, 'liquidity_below_min': 444279, 'negative_expected_net': 258208, 'cycle_budget_exhausted': 3625, 'borrow_bound_too_small': 2225}
- Enregistrements de la session : 258304 ; net attendu > 0 : 96 ; simulés (eth_call de la vraie tx) : 6 (ok 6, échec 0) ; étiquettes ghost N+1 : 0/6 positives
- Décisions : {'REJECTED': 258304} ; motifs de rejet : {'below_safety_margin': 44, 'negative_expected_net': 258208, 'p_lower_below_threshold': 73, 'reliability_not_demonstrated': 23}

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
