# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-20T22:53:55+00:00 ; durée 319.96 min ; blocs 52864139 → 52873733 (8485 vus)

## Connexion
- Requêtes RPC : 118228 ; erreurs : 330 ; latence p50/p95 : 500.1/1,912.2 ms
- Rafraîchissements d'état : 8485 ; âge des données au dernier bloc : 6.05 s ; changements de frais LP observés (pools à frais dynamiques) : 17931
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 145266 ; cycles déclenchés par événement : 7011 ; avance médiane sur le rafraîchissement multicall : 1,124 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,455.57 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 577 pools, 327 jetons, 22534 routes
- Par DEX : uniswap_v3 136, aerodrome 236, aerodrome_slipstream 158, pancakeswap_v3 30, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 207 (rejetés 2) → 612 jetons ; pools candidats 3877 (énumérés 395, par paires 0), mesurés 579, sous le plancher de 10000.0 $ : 2 → gardés 577 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDbC': 1.0, 'USDC': 1.0, 'WETH': 2447.454075, 'AERO': 0.860145, 'cbBTC': 82683.957961}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 148,671,067 | 2,455.568233 | 52873734 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 40,729,363 | 1.131911 | 52873734 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 18,859,979 | 0.029592 | 52873734 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/VVV | 3000 | 18,035,995 | 95.631529 | 52873734 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,500,010 | 0.029600 | 52873734 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,579,528 | 0.029573 | 52873734 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,935,919 | 0.000012 | 52873734 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome_slipstream | USDC/cbBTC | 424 | 9,259,950 | 0.000012 | 52873734 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | WETH/USDC | 500 | 8,626,430 | 2,455.891424 | 52873734 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/USDC | 3000 | 8,397,026 | 2,456.449337 | 52873734 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | USDC/cbBTC | 332 | 8,174,720 | 0.000012 | 52873734 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 564 | 7,597,837 | 2,455.435586 | 52873734 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,311,428 | 0.001681 | 52873734 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,453,358 | 0.029588 | 52873734 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | fBOMB/AERO | 10000 | 5,326,911 | 0.024511 | 52873734 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,741,323 | 0.000275 | 52873734 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,733,238 | 0.802394 | 52873734 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome_slipstream | USDC/AERO | 10000 | 4,580,327 | 1.130606 | 52873734 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,465,389 | 2,455.573298 | 52873734 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,404,768 | 0.998740 | 52873734 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome_slipstream | WETH/USDT | 403 | 4,347,884 | 2,458.645381 | 52873734 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome | WETH/KTA | 3000 | 4,057,910 | 34,731.487745 | 52873734 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/AERO | 10000 | 3,427,918 | 2,777.897804 | 52873734 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,875,686 | 0.000012 | 52873734 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/VVV | 2751 | 2,757,156 | 95.656698 | 52873734 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,732,499 | 401.432601 | 52873734 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,543,813 | 1.142084 | 52873734 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| aerodrome_slipstream | AERO/cbBTC | 2700 | 2,313,106 | 0.000011 | 52873734 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | WETH/FAI | 10000 | 2,251,537 | 1,207,461.097890 | 52873734 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,058,907 | 1.238865 | 52873734 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,027,920 | 1.383226 | 52873734 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,963,249 | 0.000000 | 52873734 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome | weETH_04c0/WETH | 500 | 1,922,133 | 1.105602 | 52873734 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,852,205 | 15.790320 | 52873734 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| uniswap_v3 | XDP/USDC | 100 | 1,815,416 | 0.019344 | 52873734 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,777,488 | 0.000012 | 52873734 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | fBOMB/USDC | 10000 | 1,711,172 | 0.021274 | 52873734 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| uniswap_v3 | WETH/AERO | 3000 | 1,695,464 | 2,779.891780 | 52873734 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | WETH/msETH (stable) | 500 | 1,694,696 | 2.311063 | 52873734 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,574,570 | 0.916062 | 52873734 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,493,378 | 13,545.262167 | 52873734 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,456,348 | 0.826534 | 52873734 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | EURC/USDC | 70 | 1,391,043 | 1.123139 | 52873734 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,356,096 | 0.004804 | 52873734 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v3 | DRB/WETH | 10000 | 1,349,525 | 0.000000 | 52873734 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,329,375 | 0.000277 | 52873734 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | WETH/cbBTC | 3000 | 1,313,439 | 0.029584 | 52873734 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,271,597 | 2,455.835216 | 52873734 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,235,879 | 63.619562 | 52873734 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,227,205 | 34,988,111.001513 | 52873734 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,226,714 | 23.060385 | 52873734 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| aerodrome | WETH/EDEL | 7000 | 1,226,482 | 68,721.826760 | 52873734 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,180,772 | 0.436728 | 52873734 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,174,425 | 493,960.319653 | 52873734 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | WETH/WELL | 10000 | 1,169,166 | 1,196,015.318849 | 52873734 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,157,279 | 1.106158 | 52873734 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |
| aerodrome | USDC/NOCK | 3000 | 1,133,821 | 49.013472 | 52873734 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | msUSD/USDC | 500 | 1,133,358 | 0.886326 | 52873734 | `0x7501bc8Bb51616F79bfA524E464fb7B41f0B10fB` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,108,289 | 20,669,685.326708 | 52873734 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,081,095 | 15.389075 | 52873734 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |

## Recherche d'opportunités
- Cycles : 15495 ; routes examinées : 349164330 ; candidats optimisés : 1760908 ; net attendu > 0 : 169 ; dernier cycle 282.2 ms
- Rejets (moteur) : {'spread_below_threshold': 344821207, 'liquidity_below_min': 2368284, 'negative_expected_net': 1760739, 'pool_quarantined': 194530, 'borrow_bound_too_small': 15470, 'cycle_budget_exhausted': 3931}
- Enregistrements de la session : 1760908 ; net attendu > 0 : 169 ; simulés (eth_call de la vraie tx) : 32 (ok 7, échec 25) ; étiquettes ghost N+1 : 4/18 positives
- Décisions : {'REJECTED': 1760908} ; motifs de rejet : {'below_safety_margin': 69, 'negative_expected_net': 1760739, 'p_lower_below_threshold': 128, 'price_impact': 10, 'reliability_not_demonstrated': 41, 'sim_below_estimate': 1, 'simulation_failed': 25, 'stale_data': 5}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52864215 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→ZORA→[aerodrome_slipstream]→WETH | 0.107790 WETH | 0.000142 WETH | 0.000000 WETH | 0.000003 WETH | 0.000139 WETH (0.3137 €) | — | 12.93 | 0.000 (n=23) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52864215 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→ZORA→[aerodrome_slipstream]→WETH | 0.107651 WETH | 0.000142 WETH | 0.000000 WETH | 0.000003 WETH | 0.000139 WETH (0.3131 €) | — | 12.92 | 0.000 (n=24) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52864215 | USDC→[uniswap_v3]→ZORA→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 263.009308 USDC | 0.347768 USDC | 0.000000 USDC | 0.007447 USDC | 0.340321 USDC (0.3131 €) | — | 12.94 | 0.000 (n=23) | REJECTED | reliability_not_demonstrated |
| 52864215 | USDC→[uniswap_v3]→ZORA→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 262.890606 USDC | 0.347145 USDC | 0.000000 USDC | 0.007447 USDC | 0.339698 USDC (0.3125 €) | — | 12.92 | 0.000 (n=24) | REJECTED | reliability_not_demonstrated |
| 52864215 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→ZORA→[aerodrome_slipstream]→WETH | 0.104793 WETH | 0.000140 WETH | 0.000000 WETH | 0.000003 WETH | 0.000137 WETH (0.3090 €) | — | 13.10 | 0.000 (n=23) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52864215 | USDC→[uniswap_v3]→ZORA→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 255.494914 USDC | 0.342672 USDC | 0.000000 USDC | 0.007447 USDC | 0.335225 USDC (0.3084 €) | — | 13.12 | 0.000 (n=23) | REJECTED | reliability_not_demonstrated |
| 52864215 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→ZORA→[aerodrome_slipstream]→WETH | 0.105902 WETH | 0.000139 WETH | 0.000000 WETH | 0.000003 WETH | 0.000136 WETH (0.3058 €) | — | 12.82 | 0.000 (n=24) | REJECTED | reliability_not_demonstrated |
| 52864215 | USDC→[uniswap_v3]→ZORA→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 258.491603 USDC | 0.339173 USDC | 0.000000 USDC | 0.007447 USDC | 0.331726 USDC (0.3052 €) | — | 12.83 | 0.000 (n=24) | REJECTED | reliability_not_demonstrated |
| 52864215 | USDC→[uniswap_v3]→ZORA→[aerodrome_slipstream]→USDC | 223.523660 USDC | 0.301346 USDC | 0.000000 USDC | 0.005571 USDC | 0.295775 USDC (0.2721 €) | — | 13.23 | 0.002 (n=4) | REJECTED | reliability_not_demonstrated |
| 52864215 | WETH→[sushiswap_v3]→USDC→[uniswap_v3]→ZORA→[aerodrome_slipstream]→WETH | 0.075471 WETH | 0.000103 WETH | 0.000000 WETH | 0.000003 WETH | 0.000100 WETH (0.2250 €) | — | 13.24 | 0.000 (n=23) | REJECTED | reliability_not_demonstrated |
| 52864215 | USDC→[uniswap_v3]→ZORA→[aerodrome_slipstream]→WETH→[sushiswap_v3]→USDC | 183.847545 USDC | 0.251751 USDC | 0.000000 USDC | 0.007818 USDC | 0.243933 USDC (0.2244 €) | — | 13.27 | 0.000 (n=23) | REJECTED | reliability_not_demonstrated |
| 52864215 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→ZORA→[aerodrome_slipstream]→WETH | 0.085936 WETH | 0.000090 WETH | 0.000000 WETH | 0.000003 WETH | 0.000087 WETH (0.1959 €) | — | 10.12 | 0.000 (n=23) | REJECTED | reliability_not_demonstrated |
| 52864215 | USDC→[uniswap_v3]→ZORA→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→USDC | 209.235903 USDC | 0.219816 USDC | 0.000000 USDC | 0.007447 USDC | 0.212369 USDC (0.1954 €) | — | 10.15 | 0.000 (n=23) | REJECTED | reliability_not_demonstrated |
| 52872012 | USDC→[aerodrome]→VIRTUAL→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 92.683541 USDC | 0.134522 USDC | 0.000000 USDC | 0.007042 USDC | 0.127480 USDC (0.1173 €) | — | 13.75 | 0.027 (n=11) | REJECTED | reliability_not_demonstrated |
| 52872012 | WETH→[pancakeswap_v3]→USDC→[aerodrome]→VIRTUAL→[aerodrome_slipstream]→WETH | 0.037868 WETH | 0.000055 WETH | 0.000000 WETH | 0.000003 WETH | 0.000052 WETH (0.1170 €) | 0.000052 WETH | 13.71 | 0.027 (n=11) | REJECTED | reliability_not_demonstrated |
| 52872012 | USDC→[aerodrome]→VIRTUAL→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 90.453283 USDC | 0.129444 USDC | 0.000000 USDC | 0.007042 USDC | 0.122402 USDC (0.1126 €) | — | 13.53 | 0.014 (n=105) | REJECTED | p_lower_below_threshold(0.01<0.75) |
| 52872012 | WETH→[uniswap_v3]→USDC→[aerodrome]→VIRTUAL→[aerodrome_slipstream]→WETH | 0.036841 WETH | 0.000053 WETH | 0.000000 WETH | 0.000003 WETH | 0.000050 WETH (0.1124 €) | 0.000050 WETH | 13.53 | 0.014 (n=105) | REJECTED | p_lower_below_threshold(0.01<0.75) |
| 52872012 | USDC→[aerodrome]→VIRTUAL→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 90.441307 USDC | 0.128716 USDC | 0.000000 USDC | 0.007042 USDC | 0.121674 USDC (0.1119 €) | — | 13.45 | 0.027 (n=11) | REJECTED | reliability_not_demonstrated |
| 52872012 | WETH→[pancakeswap_v3]→USDC→[aerodrome]→VIRTUAL→[aerodrome_slipstream]→WETH | 0.036887 WETH | 0.000052 WETH | 0.000000 WETH | 0.000003 WETH | 0.000050 WETH (0.1117 €) | 0.000050 WETH | 13.43 | 0.027 (n=11) | REJECTED | reliability_not_demonstrated |
| 52872012 | USDC→[aerodrome]→VIRTUAL→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 90.545957 USDC | 0.128106 USDC | 0.000000 USDC | 0.007042 USDC | 0.121064 USDC (0.1114 €) | — | 13.37 | 0.014 (n=105) | REJECTED | p_lower_below_threshold(0.01<0.75) |
| 52872012 | WETH→[uniswap_v3]→USDC→[aerodrome]→VIRTUAL→[aerodrome_slipstream]→WETH | 0.036888 WETH | 0.000052 WETH | 0.000000 WETH | 0.000003 WETH | 0.000049 WETH (0.1111 €) | — | 13.36 | 0.014 (n=105) | REJECTED | p_lower_below_threshold(0.01<0.75) |
| 52864215 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→ZORA→[aerodrome_slipstream]→WETH | 0.063447 WETH | 0.000049 WETH | 0.000000 WETH | 0.000003 WETH | 0.000046 WETH (0.1038 €) | — | 7.26 | 0.146 (n=81) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 52864215 | USDC→[uniswap_v3]→ZORA→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 154.894625 USDC | 0.119867 USDC | 0.000000 USDC | 0.007447 USDC | 0.112420 USDC (0.1034 €) | — | 7.26 | 0.146 (n=81) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 52872012 | USDC→[aerodrome]→VIRTUAL→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 81.373521 USDC | 0.102254 USDC | 0.000000 USDC | 0.007042 USDC | 0.095212 USDC (0.0876 €) | — | 11.70 | 0.027 (n=11) | REJECTED | reliability_not_demonstrated |
| 52872012 | WETH→[pancakeswap_v3]→USDC→[aerodrome]→VIRTUAL→[aerodrome_slipstream]→WETH | 0.033270 WETH | 0.000042 WETH | 0.000000 WETH | 0.000003 WETH | 0.000039 WETH (0.0874 €) | — | 11.65 | 0.027 (n=11) | REJECTED | reliability_not_demonstrated |

## Fiabilité et décision
- Observations ghost : 1563 ; taux observé 0.104 ; borne inférieure crédible (0.9) 0.094 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 9.4% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
