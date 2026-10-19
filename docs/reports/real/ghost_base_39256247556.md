# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-19T16:42:11+00:00 ; durée 218.78 min ; blocs 52812825 → 52819386 (6097 vus)

## Connexion
- Requêtes RPC : 82955 ; erreurs : 180 ; latence p50/p95 : 197.5/986.9 ms
- Rafraîchissements d'état : 6097 ; âge des données au dernier bloc : 2.58 s ; changements de frais LP observés (pools à frais dynamiques) : 19142
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 133621 ; cycles déclenchés par événement : 5749 ; avance médiane sur le rafraîchissement multicall : 1,178 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,395.61 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 571 pools, 327 jetons, 21004 routes
- Par DEX : uniswap_v3 137, aerodrome 234, aerodrome_slipstream 153, pancakeswap_v3 30, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 207 (rejetés 2) → 612 jetons ; pools candidats 3877 (énumérés 390, par paires 0), mesurés 574, sous le plancher de 10000.0 $ : 3 → gardés 571 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2419.85313, 'AERO': 0.782295, 'cbBTC': 82567.067054}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 146,337,228 | 2,395.609018 | 52819387 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 35,062,888 | 1.286227 | 52819387 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 500 | 18,229,453 | 0.029289 | 52819387 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 17,229,097 | 100.007653 | 52819387 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 13,641,378 | 0.029275 | 52819387 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,322,197 | 0.029287 | 52819387 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,845,448 | 0.000012 | 52819387 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 8,350,247 | 2,400.257190 | 52819387 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/USDC | 3000 | 8,298,715 | 2,395.840805 | 52819387 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | USDC/cbBTC | 330 | 7,812,841 | 0.000012 | 52819387 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,170,372 | 0.001664 | 52819387 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | WETH/USDC | 594 | 7,003,667 | 2,401.058083 | 52819387 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | USDC/cbBTC | 412 | 6,694,843 | 0.000012 | 52819387 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,332,942 | 0.029303 | 52819387 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | fBOMB/AERO | 10000 | 4,913,178 | 0.025997 | 52819387 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome_slipstream | USDC/AERO | 10000 | 4,887,142 | 1.287191 | 52819387 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,788,084 | 0.802395 | 52819387 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,596,759 | 0.000272 | 52819387 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,397,035 | 2,401.217773 | 52819387 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,334,171 | 0.998770 | 52819387 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 4,010,191 | 33,847.419284 | 52819387 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDT | 409 | 3,777,705 | 2,403.908039 | 52819387 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome | WETH/AERO | 10000 | 3,207,715 | 3,096.445062 | 52819387 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,849,524 | 0.000012 | 52819387 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,695,456 | 1.142087 | 52819387 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| aerodrome_slipstream | WETH/VVV | 2724 | 2,627,711 | 100.035322 | 52819387 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,627,127 | 402.650639 | 52819387 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | WETH/FAI | 10000 | 2,173,556 | 1,233,154.890839 | 52819387 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,059,139 | 1.238201 | 52819387 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 2,047,742 | 0.000009 | 52819387 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,036,743 | 1.372638 | 52819387 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| uniswap_v3 | BNKR/WETH | 10000 | 2,025,228 | 0.000000 | 52819387 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome_slipstream | WETH/MORPHO | 2715 | 1,989,349 | 952.523710 | 52819387 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| uniswap_v3 | XDP/USDC | 100 | 1,785,201 | 0.018988 | 52819387 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,776,737 | 0.000012 | 52819387 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | weETH_04c0/WETH | 500 | 1,731,705 | 1.105525 | 52819387 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,722,460 | 16.172035 | 52819387 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | fBOMB/USDC | 10000 | 1,720,638 | 0.020453 | 52819387 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,669,734 | 13,753.931717 | 52819387 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/msETH (stable) | 500 | 1,657,851 | 2.306971 | 52819387 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,551,658 | 0.916350 | 52819387 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| uniswap_v3 | WETH/AERO | 3000 | 1,488,816 | 3,090.679269 | 52819387 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,456,369 | 0.827173 | 52819387 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | EURC/USDC | 73 | 1,406,201 | 1.121321 | 52819387 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,338,162 | 0.435660 | 52819387 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,311,711 | 0.000000 | 52819387 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,298,747 | 0.004662 | 52819387 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,288,510 | 0.000275 | 52819387 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | WETH/cbBTC | 3000 | 1,278,448 | 0.029283 | 52819387 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| aerodrome | USDC/SEND | 3000 | 1,232,737 | 63.944286 | 52819387 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,207,481 | 2,400.262274 | 52819387 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,204,197 | 23.099016 | 52819387 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| aerodrome | WETH/WELL | 10000 | 1,197,282 | 1,085,473.963197 | 52819387 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/doginme | 10000 | 1,193,692 | 35,252,730.105067 | 52819387 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome_slipstream | WETH/msETH | 500 | 1,132,532 | 1.131606 | 52819387 | `0x74F72788F4814D7fF3C49B44684aa98Eee140C0E` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,127,302 | 515,481.870232 | 52819387 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | USDC/NOCK | 3000 | 1,106,643 | 51.450190 | 52819387 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | msUSD/USDC | 500 | 1,082,864 | 0.885459 | 52819387 | `0x7501bc8Bb51616F79bfA524E464fb7B41f0B10fB` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,076,957 | 15.527764 | 52819387 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | WETH/EDEL | 7000 | 1,053,817 | 89,014.343891 | 52819387 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |

## Recherche d'opportunités
- Cycles : 11845 ; routes examinées : 248792380 ; candidats optimisés : 1602953 ; net attendu > 0 : 1007 ; dernier cycle 198.3 ms
- Rejets (moteur) : {'spread_below_threshold': 244440792, 'liquidity_below_min': 2217117, 'negative_expected_net': 1601946, 'borrow_bound_too_small': 245915, 'pool_quarantined': 220376, 'cycle_budget_exhausted': 65227}
- Enregistrements de la session : 1602953 ; net attendu > 0 : 1007 ; simulés (eth_call de la vraie tx) : 93 (ok 37, échec 56) ; étiquettes ghost N+1 : 7/59 positives
- Décisions : {'REJECTED': 1602953} ; motifs de rejet : {'below_safety_margin': 739, 'negative_expected_net': 1601946, 'p_lower_below_threshold': 822, 'price_impact': 30, 'reliability_not_demonstrated': 185, 'sim_below_estimate': 5, 'simulated_net_nonpositive': 3, 'simulation_failed': 56, 'stale_data': 3}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52819356 | WETH→[aerodrome_slipstream]→VIRTUAL→[uniswap_v2]→WETH | 0.235640 WETH | 0.000256 WETH | 0.000000 WETH | 0.000002 WETH | 0.000254 WETH (0.5590 €) | — | 10.76 | 0.006 (n=1) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52819356 | WETH→[uniswap_v3]→VIRTUAL→[uniswap_v2]→WETH | 0.216679 WETH | 0.000204 WETH | 0.000000 WETH | 0.000002 WETH | 0.000202 WETH (0.4445 €) | — | 9.31 | 0.006 (n=1) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52819356 | WETH→[aerodrome_slipstream]→VIRTUAL→[uniswap_v2]→WETH | 0.194512 WETH | 0.000153 WETH | 0.000000 WETH | 0.000002 WETH | 0.000151 WETH (0.3320 €) | — | 7.74 | 0.006 (n=1) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52817668 | WETH→[aerodrome]→TEVA→[uniswap_v3]→WETH | 0.024385 WETH | 0.000112 WETH | 0.000000 WETH | 0.000002 WETH | 0.000110 WETH (0.2433 €) | — | 45.10 | 0.001 (n=13) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52819356 | USDC→[pancakeswap_v3]→VIRTUAL→[uniswap_v2]→WETH→[pancakeswap_v3]→USDC | 231.591617 USDC | 0.188676 USDC | 0.000000 USDC | 0.006480 USDC | 0.182196 USDC (0.1676 €) | — | 7.87 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52819356 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→VIRTUAL→[uniswap_v2]→WETH | 0.096802 WETH | 0.000079 WETH | 0.000000 WETH | 0.000003 WETH | 0.000076 WETH (0.1674 €) | — | 7.85 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52815901 | USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 1,462.225373 USDC | 0.173380 USDC | 0.000000 USDC | 0.007902 USDC | 0.165478 USDC (0.1522 €) | — | 1.13 | 0.117 (n=152) | REJECTED | below_safety_margin(165478<292445), p_lower_below_threshold(0.12<0.75) |
| 52815901 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH | 0.607861 WETH | 0.000072 WETH | 0.000000 WETH | 0.000003 WETH | 0.000069 WETH (0.1518 €) | — | 1.13 | 0.117 (n=152) | REJECTED | below_safety_margin(68791946207429<121572211358974), p_lower_below_threshold(0.12<0.75) |
| 52819356 | USDC→[pancakeswap_v3]→VIRTUAL→[uniswap_v2]→WETH→[uniswap_v3]→USDC | 213.125629 USDC | 0.169874 USDC | 0.000000 USDC | 0.006480 USDC | 0.163394 USDC (0.1503 €) | — | 7.67 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52819356 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→VIRTUAL→[uniswap_v2]→WETH | 0.089001 WETH | 0.000071 WETH | 0.000000 WETH | 0.000003 WETH | 0.000068 WETH (0.1501 €) | — | 7.65 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52815204 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 1,735.428521 USDC | 0.154603 USDC | 0.000000 USDC | 0.006144 USDC | 0.148459 USDC (0.1366 €) | — | 0.86 | 0.017 (n=49) | REJECTED | below_safety_margin(148459<347085), p_lower_below_threshold(0.02<0.75) |
| 52815204 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.726513 WETH | 0.000065 WETH | 0.000000 WETH | 0.000003 WETH | 0.000062 WETH (0.1365 €) | — | 0.85 | 0.017 (n=49) | REJECTED | below_safety_margin(61999402150527<145302574799060), p_lower_below_threshold(0.02<0.75) |
| 52819147 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC | 226.046893 USDC | 0.145848 USDC | 0.000000 USDC | 0.007233 USDC | 0.138615 USDC (0.1275 €) | — | 6.13 | 0.120 (n=113) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.12<0.75) |
| 52819147 | cbBTC→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.002632 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1272 €) | — | 6.42 | 0.120 (n=113) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52819356 | USDC→[pancakeswap_v3]→VIRTUAL→[uniswap_v2]→WETH→[uniswap_v3]→USDC | 201.061661 USDC | 0.141341 USDC | 0.000000 USDC | 0.006480 USDC | 0.134861 USDC (0.1241 €) | — | 6.71 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52819356 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→VIRTUAL→[uniswap_v2]→WETH | 0.083880 WETH | 0.000059 WETH | 0.000000 WETH | 0.000003 WETH | 0.000056 WETH (0.1239 €) | — | 6.70 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52819356 | USDC→[pancakeswap_v3]→VIRTUAL→[uniswap_v2]→WETH→[pancakeswap_v3]→USDC | 194.569728 USDC | 0.136301 USDC | 0.000000 USDC | 0.006480 USDC | 0.129821 USDC (0.1194 €) | — | 6.67 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52819356 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→VIRTUAL→[uniswap_v2]→WETH | 0.081284 WETH | 0.000057 WETH | 0.000000 WETH | 0.000003 WETH | 0.000054 WETH (0.1193 €) | — | 6.66 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52819356 | WETH→[aerodrome]→VIRTUAL→[uniswap_v2]→WETH | 0.107048 WETH | 0.000054 WETH | 0.000000 WETH | 0.000002 WETH | 0.000052 WETH (0.1154 €) | — | 4.89 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52819042 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC | 1,644.346603 USDC | 0.112845 USDC | 0.000000 USDC | 0.007590 USDC | 0.105255 USDC (0.0968 €) | — | 0.64 | 0.114 (n=157) | REJECTED | below_safety_margin(105255<328869), p_lower_below_threshold(0.11<0.75) |
| 52819042 | WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.686947 WETH | 0.000047 WETH | 0.000000 WETH | 0.000003 WETH | 0.000044 WETH (0.0967 €) | — | 0.64 | 0.114 (n=157) | REJECTED | below_safety_margin(43891134148525<137389383382955), p_lower_below_threshold(0.11<0.75) |
| 52815907 | USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 273.632671 USDC | 0.112662 USDC | 0.000000 USDC | 0.008367 USDC | 0.104295 USDC (0.0960 €) | — | 3.81 | 0.123 (n=110) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52815907 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH | 0.113520 WETH | 0.000047 WETH | 0.000000 WETH | 0.000003 WETH | 0.000043 WETH (0.0957 €) | 0.000043 WETH | 3.81 | 0.123 (n=110) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52819147 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→AERO→[pancakeswap_v3]→WETH | 0.163436 WETH | 0.000046 WETH | 0.000000 WETH | 0.000003 WETH | 0.000043 WETH (0.0950 €) | — | 2.64 | 0.114 (n=157) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.11<0.75) |
| 52819147 | cbBTC→[aerodrome_slipstream]→AERO→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.004303 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0948 €) | — | 2.93 | 0.114 (n=157) | REJECTED | p_lower_below_threshold(0.11<0.75) |

## Fiabilité et décision
- Observations ghost : 1329 ; taux observé 0.104 ; borne inférieure crédible (0.9) 0.094 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 9.4% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
