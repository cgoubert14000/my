# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-14T02:42:47+00:00 ; durée 269.89 min ; blocs 52570110 → 52578202 (7367 vus)

## Connexion
- Requêtes RPC : 97681 ; erreurs : 576 ; latence p50/p95 : 280.0/1,168.5 ms
- Rafraîchissements d'état : 7367 ; âge des données au dernier bloc : 2.25 s ; changements de frais LP observés (pools à frais dynamiques) : 11402
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 129706 ; cycles déclenchés par événement : 0 ; avance médiane sur le rafraîchissement multicall : 1,151 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,504.68 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 579 pools, 328 jetons, 21606 routes
- Par DEX : uniswap_v3 141, aerodrome 236, aerodrome_slipstream 154, pancakeswap_v3 31, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 208 (rejetés 2) → 613 jetons ; pools candidats 3923 (énumérés 392, par paires 0), mesurés 581, sous le plancher de 10000.0 $ : 2 → gardés 579 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2504.448027, 'AERO': 0.900554, 'cbBTC': 83392.589857}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 150,322,756 | 2,504.681459 | 52578202 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 41,920,376 | 1.111706 | 52578202 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 500 | 18,334,254 | 0.030066 | 52578202 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 15,729,608 | 110.550887 | 52578202 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 14,910,503 | 0.030077 | 52578202 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,703,289 | 0.030093 | 52578202 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| aerodrome_slipstream | WETH/USDC | 654 | 10,005,741 | 2,504.623638 | 52578202 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| uniswap_v3 | WETH/USDC | 500 | 9,406,965 | 2,504.162551 | 52578202 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,308,800 | 0.000012 | 52578202 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome | WETH/USDC | 3000 | 9,114,060 | 2,505.801302 | 52578202 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | USDC/cbBTC | 348 | 8,578,107 | 0.000012 | 52578202 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,343,831 | 0.001683 | 52578202 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 508 | 7,159,729 | 0.000012 | 52578202 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome_slipstream | USDC/AERO | 10000 | 6,114,979 | 1.106283 | 52578202 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,564,766 | 0.030065 | 52578202 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/superOETHb | 400 | 5,532,041 | 1.000859 | 52578202 | `0x6446021F4E396dA3df4235C62537431372195D38` |
| aerodrome | fBOMB/AERO | 10000 | 5,436,553 | 0.026741 | 52578202 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,781,492 | 0.000281 | 52578202 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,729,235 | 0.802386 | 52578202 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,523,586 | 2,504.683050 | 52578202 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,409,598 | 0.999352 | 52578202 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 4,114,105 | 35,153.818939 | 52578202 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/AERO | 10000 | 3,712,976 | 2,769.531341 | 52578202 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | cbETH/WETH | 60 | 3,038,540 | 1.141618 | 52578202 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,864,592 | 0.000012 | 52578202 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 2,661,273 | 0.000011 | 52578202 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/VVV | 2703 | 2,597,685 | 110.496588 | 52578202 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,590,159 | 398.958228 | 52578202 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | WETH/USDT | 424 | 2,462,219 | 2,507.485641 | 52578202 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome | WETH/FAI | 10000 | 2,452,848 | 1,058,498.079298 | 52578202 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,116,889 | 1.189953 | 52578202 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | BNKR/WETH | 10000 | 2,101,873 | 0.000000 | 52578202 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome | fBOMB/USDbC | 10000 | 2,039,197 | 0.024078 | 52578202 | `0xC395664B295ed5bf1D249Ae8be9740655AA174ef` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 1,937,241 | 1,052.062001 | 52578202 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,925,576 | 15.557776 | 52578202 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| uniswap_v3 | XDP/USDC | 100 | 1,894,148 | 0.021362 | 52578202 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,881,816 | 0.916708 | 52578202 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| aerodrome | USDC/alUSDb (stable) | 500 | 1,841,628 | 1.374454 | 52578202 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,705,381 | 0.000012 | 52578202 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,637,771 | 13,254.708724 | 52578202 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/msETH (stable) | 500 | 1,614,068 | 2.296962 | 52578202 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | WETH/AERO | 3000 | 1,566,308 | 2,781.891727 | 52578202 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | weETH_04c0/WETH | 500 | 1,548,568 | 1.105774 | 52578202 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| uniswap_v3 | DRB/WETH | 10000 | 1,471,123 | 0.000000 | 52578202 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,459,372 | 0.832324 | 52578202 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | EURC/USDC | 73 | 1,424,820 | 1.120715 | 52578202 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,404,379 | 0.000282 | 52578202 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,402,453 | 0.004865 | 52578202 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | WETH/AERO | 3024 | 1,389,894 | 2,781.442696 | 52578202 | `0x82321f3BEB69f503380D6B233857d5C43562e2D0` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,304,234 | 23.420713 | 52578202 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,287,623 | 1.105595 | 52578202 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,285,532 | 2,504.102656 | 52578202 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | WETH/doginme | 10000 | 1,257,593 | 34,542,423.834366 | 52578202 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | USDC/SEND | 3000 | 1,247,882 | 62.401582 | 52578202 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome_slipstream | msUSD/USDC | 500 | 1,229,316 | 0.886335 | 52578202 | `0x7501bc8Bb51616F79bfA524E464fb7B41f0B10fB` |
| aerodrome | WETH/EDEL | 7000 | 1,213,117 | 73,180.975479 | 52578202 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,207,002 | 483,539.485072 | 52578202 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | WETH/WELL | 10000 | 1,201,053 | 1,179,286.020225 | 52578202 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome | USDC/NOCK | 3000 | 1,199,246 | 43.819519 | 52578202 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,167,166 | 0.436676 | 52578202 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |

## Recherche d'opportunités
- Cycles : 13917 ; routes examinées : 300690702 ; candidats optimisés : 1597099 ; net attendu > 0 : 327 ; dernier cycle 254.4 ms
- Rejets (moteur) : {'spread_below_threshold': 296509625, 'liquidity_below_min': 2540137, 'negative_expected_net': 1596772, 'unquotable': 27808, 'borrow_bound_too_small': 13904, 'cycle_budget_exhausted': 2129}
- Enregistrements de la session : 1597099 ; net attendu > 0 : 327 ; simulés (eth_call de la vraie tx) : 19 (ok 9, échec 10) ; étiquettes ghost N+1 : 0/9 positives
- Décisions : {'REJECTED': 1597099} ; motifs de rejet : {'below_safety_margin': 80, 'negative_expected_net': 1596772, 'reliability_not_demonstrated': 327, 'simulation_failed': 10, 'stale_data': 142}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52570167 | USDC→[aerodrome_slipstream]→ZORA→[uniswap_v3]→USDC | 160.347048 USDC | 0.162817 USDC | 0.000000 USDC | 0.005640 USDC | 0.157177 USDC (0.1446 €) | 0.157177 USDC | 9.80 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52570167 | USDC→[aerodrome_slipstream]→ZORA→[uniswap_v3]→USDC | 160.347048 USDC | 0.162817 USDC | 0.000000 USDC | 0.005640 USDC | 0.157177 USDC (0.1446 €) | — | 9.80 | — (n=0) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52574242 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 528.078944 USDC | 0.069950 USDC | 0.000000 USDC | 0.005627 USDC | 0.064323 USDC (0.0592 €) | — | 1.22 | — (n=0) | REJECTED | below_safety_margin(64323<105615), reliability_not_demonstrated |
| 52574244 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 528.078944 USDC | 0.069950 USDC | 0.000000 USDC | 0.005627 USDC | 0.064323 USDC (0.0592 €) | — | 1.22 | — (n=0) | REJECTED | below_safety_margin(64323<105615), reliability_not_demonstrated |
| 52574242 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.210753 WETH | 0.000028 WETH | 0.000000 WETH | 0.000002 WETH | 0.000026 WETH (0.0590 €) | — | 1.22 | — (n=0) | REJECTED | below_safety_margin(25609057420982<42150590323936), reliability_not_demonstrated |
| 52574244 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.210753 WETH | 0.000028 WETH | 0.000000 WETH | 0.000002 WETH | 0.000026 WETH (0.0590 €) | — | 1.22 | — (n=0) | REJECTED | below_safety_margin(25609057420982<42150590323936), reliability_not_demonstrated |
| 52577416 | WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.185483 WETH | 0.000020 WETH | 0.000000 WETH | 0.000003 WETH | 0.000017 WETH (0.0401 €) | — | 0.94 | — (n=0) | REJECTED | below_safety_margin(17419649854083<37096512428921), reliability_not_demonstrated |
| 52577416 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC | 463.379617 USDC | 0.051119 USDC | 0.000000 USDC | 0.007530 USDC | 0.043589 USDC (0.0401 €) | — | 0.94 | — (n=0) | REJECTED | below_safety_margin(43589<92675), reliability_not_demonstrated |
| 52577416 | WETH→[aerodrome_slipstream]→USDT→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.165834 WETH | 0.000017 WETH | 0.000000 WETH | 0.000003 WETH | 0.000014 WETH (0.0314 €) | — | 0.82 | — (n=0) | REJECTED | below_safety_margin(13607942400417<33166710795945), reliability_not_demonstrated |
| 52577416 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDT→[uniswap_v3]→USDC | 413.417729 USDC | 0.041579 USDC | 0.000000 USDC | 0.007530 USDC | 0.034049 USDC (0.0313 €) | — | 0.82 | — (n=0) | REJECTED | below_safety_margin(34049<82683), reliability_not_demonstrated |
| 52574242 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH | 0.154016 WETH | 0.000016 WETH | 0.000000 WETH | 0.000003 WETH | 0.000013 WETH (0.0306 €) | — | 0.86 | — (n=0) | REJECTED | below_safety_margin(13258836601508<30803151013720), stale_data(4114ms>4000.0), reliability_not_demonstrated |
| 52574244 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH | 0.154016 WETH | 0.000016 WETH | 0.000000 WETH | 0.000003 WETH | 0.000013 WETH (0.0306 €) | — | 0.86 | — (n=0) | REJECTED | below_safety_margin(13258836601508<30803151013720), stale_data(4892ms>4000.0), reliability_not_demonstrated |
| 52574242 | USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 345.110078 USDC | 0.040313 USDC | 0.000000 USDC | 0.007530 USDC | 0.032783 USDC (0.0302 €) | — | 0.95 | — (n=0) | REJECTED | below_safety_margin(32783<69022), stale_data(4130ms>4000.0), reliability_not_demonstrated |
| 52574244 | USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 345.110078 USDC | 0.040313 USDC | 0.000000 USDC | 0.007530 USDC | 0.032783 USDC (0.0302 €) | — | 0.95 | — (n=0) | REJECTED | below_safety_margin(32783<69022), stale_data(4908ms>4000.0), reliability_not_demonstrated |
| 52574242 | cbBTC→[uniswap_v3]→WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.004090 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0299 €) | — | 0.95 | — (n=0) | REJECTED | below_safety_margin(39<81), stale_data(4122ms>4000.0), reliability_not_demonstrated |
| 52574244 | cbBTC→[uniswap_v3]→WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.004090 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0299 €) | — | 0.95 | — (n=0) | REJECTED | below_safety_margin(39<81), stale_data(4900ms>4000.0), reliability_not_demonstrated |
| 52574058 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→USDC | 227.858475 USDC | 0.037864 USDC | 0.000000 USDC | 0.007525 USDC | 0.030339 USDC (0.0279 €) | — | 1.33 | — (n=0) | REJECTED | below_safety_margin(30339<45571), reliability_not_demonstrated |
| 52574060 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→USDC | 227.858475 USDC | 0.037864 USDC | 0.000000 USDC | 0.007525 USDC | 0.030339 USDC (0.0279 €) | — | 1.33 | — (n=0) | REJECTED | below_safety_margin(30339<45571), reliability_not_demonstrated |
| 52574058 | cbBTC→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.002900 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0276 €) | — | 1.24 | — (n=0) | REJECTED | below_safety_margin(36<58), reliability_not_demonstrated |
| 52574060 | cbBTC→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.002900 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0276 €) | — | 1.24 | — (n=0) | REJECTED | below_safety_margin(36<58), reliability_not_demonstrated |
| 52576892 | WETH→[aerodrome_slipstream]→USDC→[aerodrome]→WETH | 0.006042 WETH | 0.000012 WETH | 0.000000 WETH | 0.000002 WETH | 0.000009 WETH (0.0217 €) | — | 15.60 | — (n=0) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52576894 | WETH→[aerodrome_slipstream]→USDC→[aerodrome]→WETH | 0.006042 WETH | 0.000012 WETH | 0.000000 WETH | 0.000002 WETH | 0.000009 WETH (0.0217 €) | — | 15.60 | — (n=0) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52576892 | USDC→[aerodrome]→WETH→[aerodrome_slipstream]→USDC | 14.995229 USDC | 0.028883 USDC | 0.000000 USDC | 0.005282 USDC | 0.023601 USDC (0.0217 €) | — | 15.74 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52576894 | USDC→[aerodrome]→WETH→[aerodrome_slipstream]→USDC | 14.995229 USDC | 0.028883 USDC | 0.000000 USDC | 0.005282 USDC | 0.023601 USDC (0.0217 €) | — | 15.74 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52576892 | WETH→[pancakeswap_v3]→USDC→[aerodrome]→WETH | 0.006006 WETH | 0.000011 WETH | 0.000000 WETH | 0.000002 WETH | 0.000009 WETH (0.0207 €) | — | 14.93 | — (n=0) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |

## Fiabilité et décision
- Observations ghost : 9 ; taux observé 0.000 ; borne inférieure crédible (0.9) 0.001 ; seuil 0.75 → **FIABILITÉ NON DÉMONTRÉE — DONNÉES INSUFFISANTES**
- Statut de maturité : **APPRENTISSAGE** — FIABILITÉ NON DÉMONTRÉE — DONNÉES INSUFFISANTES
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ❌ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
