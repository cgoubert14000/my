# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-19T15:10:13+00:00 ; durée 126.83 min ; blocs 52812825 → 52816630 (3664 vus)

## Connexion
- Requêtes RPC : 48268 ; erreurs : 143 ; latence p50/p95 : 290.3/852.6 ms
- Rafraîchissements d'état : 3664 ; âge des données au dernier bloc : 3.54 s ; changements de frais LP observés (pools à frais dynamiques) : 11966
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 71401 ; cycles déclenchés par événement : 2459 ; avance médiane sur le rafraîchissement multicall : 761 ms
- Gaz : base fee 0.005154 gwei ; prix ETH (pool le plus profond) : 2,410.35 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 571 pools, 327 jetons, 21004 routes
- Par DEX : uniswap_v3 137, aerodrome 234, aerodrome_slipstream 153, pancakeswap_v3 30, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 207 (rejetés 2) → 612 jetons ; pools candidats 3877 (énumérés 390, par paires 0), mesurés 574, sous le plancher de 10000.0 $ : 3 → gardés 571 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2419.85313, 'AERO': 0.782295, 'cbBTC': 82567.067054}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 146,847,117 | 2,410.345996 | 52816630 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 35,016,202 | 1.292497 | 52816630 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 500 | 18,312,640 | 0.029296 | 52816630 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 17,095,281 | 102.838618 | 52816630 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 16,102,866 | 0.029301 | 52816630 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,382,056 | 0.029289 | 52816630 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,858,222 | 0.000012 | 52816630 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome_slipstream | USDC/cbBTC | 412 | 8,479,323 | 0.000012 | 52816630 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | WETH/USDC | 500 | 8,389,561 | 2,407.985469 | 52816630 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/USDC | 3000 | 8,325,456 | 2,410.623407 | 52816630 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | USDC/cbBTC | 332 | 7,830,635 | 0.000012 | 52816630 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 535 | 7,306,297 | 2,407.509123 | 52816630 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,208,930 | 0.001662 | 52816630 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,365,239 | 0.029295 | 52816630 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | USDC/AERO | 10000 | 5,093,224 | 1.295387 | 52816630 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome | fBOMB/AERO | 10000 | 4,905,574 | 0.025993 | 52816630 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,817,538 | 0.802395 | 52816630 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,632,006 | 0.000273 | 52816630 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,414,196 | 2,407.013956 | 52816630 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,359,891 | 0.998770 | 52816630 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome_slipstream | WETH/USDT | 403 | 4,264,898 | 2,411.197366 | 52816630 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome | WETH/KTA | 3000 | 4,028,532 | 33,953.829490 | 52816630 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/AERO | 10000 | 3,227,606 | 3,097.656179 | 52816630 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,858,142 | 0.000012 | 52816630 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,628,776 | 404.904034 | 52816630 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | WETH/VVV | 2700 | 2,626,359 | 102.835901 | 52816630 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | WETH/FAI | 10000 | 2,185,131 | 1,235,182.139618 | 52816630 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,059,140 | 1.238200 | 52816630 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | BNKR/WETH | 10000 | 2,050,387 | 0.000000 | 52816630 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,036,743 | 1.372638 | 52816630 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 2,026,038 | 0.000009 | 52816630 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | cbETH/WETH | 60 | 1,999,429 | 1.142072 | 52816630 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,774,354 | 0.000012 | 52816630 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | XDP/USDC | 100 | 1,772,288 | 0.018741 | 52816630 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,765,073 | 13,821.755960 | 52816630 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | weETH_04c0/WETH | 500 | 1,742,582 | 1.105523 | 52816630 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,738,280 | 16.202913 | 52816630 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | fBOMB/USDC | 10000 | 1,722,050 | 0.020490 | 52816630 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| aerodrome | WETH/msETH (stable) | 500 | 1,667,368 | 2.308377 | 52816630 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | WETH/AERO | 3000 | 1,595,409 | 3,113.584698 | 52816630 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,561,203 | 0.916350 | 52816630 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,456,401 | 0.827137 | 52816630 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | EURC/USDC | 70 | 1,406,382 | 1.121616 | 52816630 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,338,838 | 0.435989 | 52816630 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,320,061 | 0.000000 | 52816630 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,298,397 | 0.000274 | 52816630 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,292,604 | 0.004610 | 52816630 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome | WETH/cbBTC | 3000 | 1,286,158 | 0.029283 | 52816630 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,277,724 | 23.126679 | 52816630 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| aerodrome | USDC/SEND | 3000 | 1,232,737 | 63.944286 | 52816630 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome | WETH/WELL | 10000 | 1,201,504 | 1,091,162.095251 | 52816630 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/doginme | 10000 | 1,201,035 | 35,252,730.105067 | 52816630 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,198,340 | 2,407.964992 | 52816630 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,134,267 | 515,481.870232 | 52816630 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome_slipstream | msUSD/USDC | 500 | 1,116,907 | 0.885737 | 52816630 | `0x7501bc8Bb51616F79bfA524E464fb7B41f0B10fB` |
| aerodrome_slipstream | WETH/msETH | 500 | 1,106,559 | 1.131870 | 52816630 | `0x74F72788F4814D7fF3C49B44684aa98Eee140C0E` |
| aerodrome | USDC/NOCK | 3000 | 1,092,209 | 52.819035 | 52816630 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,076,904 | 15.529652 | 52816630 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | WETH/EDEL | 7000 | 1,057,929 | 89,413.628457 | 52816630 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,048,186 | 1.105811 | 52816630 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |

## Recherche d'opportunités
- Cycles : 6122 ; routes examinées : 128586488 ; candidats optimisés : 939444 ; net attendu > 0 : 712 ; dernier cycle 259.9 ms
- Rejets (moteur) : {'spread_below_threshold': 126085175, 'liquidity_below_min': 1187550, 'negative_expected_net': 938732, 'pool_quarantined': 219050, 'borrow_bound_too_small': 102890, 'cycle_budget_exhausted': 52379}
- Enregistrements de la session : 939444 ; net attendu > 0 : 712 ; simulés (eth_call de la vraie tx) : 68 (ok 33, échec 35) ; étiquettes ghost N+1 : 7/39 positives
- Décisions : {'REJECTED': 939444} ; motifs de rejet : {'below_safety_margin': 520, 'negative_expected_net': 938732, 'p_lower_below_threshold': 602, 'price_impact': 30, 'reliability_not_demonstrated': 110, 'sim_below_estimate': 4, 'simulated_net_nonpositive': 3, 'simulation_failed': 35, 'stale_data': 3}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52815901 | USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 1,462.225373 USDC | 0.173380 USDC | 0.000000 USDC | 0.007902 USDC | 0.165478 USDC (0.1522 €) | — | 1.13 | 0.117 (n=152) | REJECTED | below_safety_margin(165478<292445), p_lower_below_threshold(0.12<0.75) |
| 52815901 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH | 0.607861 WETH | 0.000072 WETH | 0.000000 WETH | 0.000003 WETH | 0.000069 WETH (0.1518 €) | — | 1.13 | 0.117 (n=152) | REJECTED | below_safety_margin(68791946207429<121572211358974), p_lower_below_threshold(0.12<0.75) |
| 52815204 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 1,735.428521 USDC | 0.154603 USDC | 0.000000 USDC | 0.006144 USDC | 0.148459 USDC (0.1366 €) | — | 0.86 | 0.017 (n=49) | REJECTED | below_safety_margin(148459<347085), p_lower_below_threshold(0.02<0.75) |
| 52815204 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.726513 WETH | 0.000065 WETH | 0.000000 WETH | 0.000003 WETH | 0.000062 WETH (0.1365 €) | — | 0.85 | 0.017 (n=49) | REJECTED | below_safety_margin(61999402150527<145302574799060), p_lower_below_threshold(0.02<0.75) |
| 52815907 | USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 273.632671 USDC | 0.112662 USDC | 0.000000 USDC | 0.008367 USDC | 0.104295 USDC (0.0960 €) | — | 3.81 | 0.123 (n=110) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52815907 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH | 0.113520 WETH | 0.000047 WETH | 0.000000 WETH | 0.000003 WETH | 0.000043 WETH (0.0957 €) | 0.000043 WETH | 3.81 | 0.123 (n=110) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52815204 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→cbBTC | 0.011354 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0792 €) | — | 0.92 | 0.119 (n=150) | REJECTED | below_safety_margin(105<227), p_lower_below_threshold(0.12<0.75) |
| 52815204 | WETH→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.422030 WETH | 0.000039 WETH | 0.000000 WETH | 0.000003 WETH | 0.000036 WETH (0.0792 €) | — | 0.85 | 0.119 (n=150) | REJECTED | below_safety_margin(35963544596847<84406012305694), p_lower_below_threshold(0.12<0.75) |
| 52815204 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 942.588524 USDC | 0.093877 USDC | 0.000000 USDC | 0.007972 USDC | 0.085905 USDC (0.0790 €) | — | 0.91 | 0.119 (n=150) | REJECTED | below_safety_margin(85905<188517), p_lower_below_threshold(0.12<0.75) |
| 52815240 | cbBTC→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.003301 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0702 €) | 0.000001 cbBTC | 2.82 | 0.119 (n=150) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52815239 | cbBTC→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.003301 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0702 €) | — | 2.82 | 0.119 (n=150) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.12<0.75) |
| 52815240 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→USDC | 271.384886 USDC | 0.083095 USDC | 0.000000 USDC | 0.007243 USDC | 0.075852 USDC (0.0698 €) | 0.075852 USDC | 2.79 | 0.119 (n=150) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52815239 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→USDC | 271.384886 USDC | 0.083095 USDC | 0.000000 USDC | 0.007243 USDC | 0.075852 USDC (0.0698 €) | — | 2.79 | 0.119 (n=150) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.12<0.75) |
| 52815204 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→cbBTC | 0.011356 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0694 €) | — | 0.81 | 0.119 (n=150) | REJECTED | below_safety_margin(92<227), p_lower_below_threshold(0.12<0.75) |
| 52815204 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 991.357510 USDC | 0.083108 USDC | 0.000000 USDC | 0.007972 USDC | 0.075136 USDC (0.0691 €) | — | 0.76 | 0.119 (n=150) | REJECTED | below_safety_margin(75136<198271), p_lower_below_threshold(0.12<0.75) |
| 52815204 | WETH→[uniswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.413929 WETH | 0.000035 WETH | 0.000000 WETH | 0.000003 WETH | 0.000031 WETH (0.0691 €) | — | 0.76 | 0.119 (n=150) | REJECTED | below_safety_margin(31372499522352<82785743021120), p_lower_below_threshold(0.12<0.75) |
| 52815204 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→cbBTC | 0.011396 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0641 €) | — | 0.75 | 0.119 (n=150) | REJECTED | below_safety_margin(85<227), p_lower_below_threshold(0.12<0.75) |
| 52815204 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 886.244816 USDC | 0.077173 USDC | 0.000000 USDC | 0.007972 USDC | 0.069201 USDC (0.0637 €) | — | 0.78 | 0.119 (n=150) | REJECTED | below_safety_margin(69201<177248), p_lower_below_threshold(0.12<0.75) |
| 52815204 | WETH→[uniswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.366775 WETH | 0.000032 WETH | 0.000000 WETH | 0.000003 WETH | 0.000029 WETH (0.0636 €) | — | 0.79 | 0.119 (n=150) | REJECTED | below_safety_margin(28893202127362<73354944348218), p_lower_below_threshold(0.12<0.75) |
| 52815907 | USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 212.829066 USDC | 0.067681 USDC | 0.000000 USDC | 0.007966 USDC | 0.059715 USDC (0.0549 €) | — | 2.81 | 0.292 (n=72) | REJECTED | p_lower_below_threshold(0.29<0.75) |
| 52815907 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH | 0.088490 WETH | 0.000028 WETH | 0.000000 WETH | 0.000003 WETH | 0.000025 WETH (0.0548 €) | 0.000025 WETH | 2.80 | 0.292 (n=72) | REJECTED | p_lower_below_threshold(0.29<0.75) |
| 52815225 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 393.383697 USDC | 0.062903 USDC | 0.000000 USDC | 0.006146 USDC | 0.056757 USDC (0.0522 €) | — | 1.44 | 0.017 (n=49) | REJECTED | below_safety_margin(56757<78676), p_lower_below_threshold(0.02<0.75) |
| 52815225 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.164600 WETH | 0.000026 WETH | 0.000000 WETH | 0.000003 WETH | 0.000024 WETH (0.0522 €) | — | 1.44 | 0.017 (n=49) | REJECTED | below_safety_margin(23695395236658<32919958684015), p_lower_below_threshold(0.02<0.75) |
| 52815907 | USDC→[aerodrome_slipstream]→EURC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 124.512285 USDC | 0.062280 USDC | 0.000000 USDC | 0.008367 USDC | 0.053913 USDC (0.0496 €) | — | 4.33 | 0.123 (n=110) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52815907 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→EURC→[pancakeswap_v3]→WETH | 0.051622 WETH | 0.000026 WETH | 0.000000 WETH | 0.000003 WETH | 0.000022 WETH (0.0495 €) | 0.000022 WETH | 4.33 | 0.123 (n=110) | REJECTED | p_lower_below_threshold(0.12<0.75) |

## Fiabilité et décision
- Observations ghost : 1309 ; taux observé 0.105 ; borne inférieure crédible (0.9) 0.095 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 9.5% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
