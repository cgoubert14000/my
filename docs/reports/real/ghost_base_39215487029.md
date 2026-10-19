# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-19T10:46:11+00:00 ; durée 198.81 min ; blocs 52802745 → 52808707 (5925 vus)

## Connexion
- Requêtes RPC : 79997 ; erreurs : 23 ; latence p50/p95 : 232.5/539.7 ms
- Rafraîchissements d'état : 5925 ; âge des données au dernier bloc : 2.89 s ; changements de frais LP observés (pools à frais dynamiques) : 13507
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 74531 ; cycles déclenchés par événement : 4704 ; avance médiane sur le rafraîchissement multicall : 489 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,421.72 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 575 pools, 328 jetons, 21198 routes
- Par DEX : uniswap_v3 138, aerodrome 234, aerodrome_slipstream 156, pancakeswap_v3 30, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 207 (rejetés 2) → 612 jetons ; pools candidats 3877 (énumérés 392, par paires 0), mesurés 577, sous le plancher de 10000.0 $ : 2 → gardés 575 (max 1500) ; prix des hubs : {'USDC': 1.0, 'DAI': 1.0, 'USDbC': 1.0, 'WETH': 2427.085029, 'AERO': 0.802709, 'cbBTC': 82780.001526}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 147,671,036 | 2,421.720822 | 52808708 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 35,201,608 | 1.267800 | 52808708 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 500 | 18,352,125 | 0.029457 | 52808708 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 17,216,653 | 102.227876 | 52808708 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| aerodrome_slipstream | WETH/cbBTC | 2505 | 14,214,707 | 0.029398 | 52808708 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,436,755 | 0.029384 | 52808708 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,833,913 | 0.000012 | 52808708 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 8,463,414 | 2,424.352323 | 52808708 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome_slipstream | USDC/cbBTC | 332 | 7,827,382 | 0.000012 | 52808708 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 535 | 7,326,853 | 2,423.727456 | 52808708 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,202,721 | 0.001662 | 52808708 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 412 | 6,804,435 | 0.000012 | 52808708 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome | WETH/USDC | 3000 | 5,488,369 | 2,421.420228 | 52808708 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,365,123 | 0.029458 | 52808708 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/superOETHb | 400 | 5,258,939 | 1.000854 | 52808708 | `0x6446021F4E396dA3df4235C62537431372195D38` |
| aerodrome | fBOMB/AERO | 10000 | 4,841,268 | 0.025982 | 52808708 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,840,251 | 0.802398 | 52808708 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,653,498 | 0.000273 | 52808708 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,447,260 | 2,423.849103 | 52808708 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,355,972 | 0.998772 | 52808708 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome_slipstream | USDC/AERO | 10000 | 4,228,412 | 1.265095 | 52808708 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome | WETH/KTA | 3000 | 4,038,590 | 34,104.565851 | 52808708 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDT | 406 | 3,717,787 | 2,427.541246 | 52808708 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome | WETH/AERO | 10000 | 3,266,548 | 3,052.033299 | 52808708 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,929,113 | 407.463028 | 52808708 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,918,535 | 1.141897 | 52808708 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,856,524 | 0.000012 | 52808708 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/MORPHO | 2730 | 2,823,377 | 982.519248 | 52808708 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome_slipstream | WETH/VVV | 2733 | 2,645,580 | 102.200586 | 52808708 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 2,391,356 | 0.000010 | 52808708 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | WETH/FAI | 10000 | 2,200,938 | 1,229,022.349210 | 52808708 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,062,172 | 1.234881 | 52808708 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,036,743 | 1.372638 | 52808708 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| uniswap_v3 | BNKR/WETH | 10000 | 2,036,689 | 0.000000 | 52808708 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,840,937 | 15.968058 | 52808708 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,778,800 | 0.000012 | 52808708 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | XDP/USDC | 100 | 1,754,233 | 0.018464 | 52808708 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome | weETH_04c0/WETH | 500 | 1,751,104 | 1.105523 | 52808708 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome | fBOMB/USDC | 10000 | 1,722,200 | 0.020505 | 52808708 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,694,736 | 13,837.354002 | 52808708 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/msETH (stable) | 500 | 1,671,833 | 2.309576 | 52808708 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | WETH/AERO | 3000 | 1,611,103 | 3,073.687862 | 52808708 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,568,571 | 0.916350 | 52808708 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| aerodrome_slipstream | EURC/USDC | 70 | 1,470,849 | 1.121327 | 52808708 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,455,392 | 0.827288 | 52808708 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,340,033 | 0.436500 | 52808708 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,325,196 | 0.000000 | 52808708 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,304,376 | 0.000272 | 52808708 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | WETH/cbBTC | 3000 | 1,284,691 | 0.029380 | 52808708 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,280,349 | 0.004559 | 52808708 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,274,176 | 23.179417 | 52808708 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| aerodrome_slipstream | WETH/VVV | 8000 | 1,261,569 | 102.231103 | 52808708 | `0x46D398A5b33709877f50c8918A7eE96F1Be1d7dd` |
| aerodrome | USDC/SEND | 3000 | 1,232,995 | 63.917537 | 52808708 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome | WETH/WELL | 10000 | 1,220,188 | 1,068,010.221692 | 52808708 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/doginme | 10000 | 1,206,900 | 35,086,766.345887 | 52808708 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,201,642 | 2,424.352287 | 52808708 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome_slipstream | msUSD/USDC | 500 | 1,194,428 | 0.886092 | 52808708 | `0x7501bc8Bb51616F79bfA524E464fb7B41f0B10fB` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,139,621 | 515,481.870232 | 52808708 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | USDC/NOCK | 3000 | 1,095,946 | 52.461152 | 52808708 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | WETH/msETH | 500 | 1,087,384 | 1.132081 | 52808708 | `0x74F72788F4814D7fF3C49B44684aa98Eee140C0E` |

## Recherche d'opportunités
- Cycles : 10628 ; routes examinées : 225292344 ; candidats optimisés : 1359354 ; net attendu > 0 : 162 ; dernier cycle 218.7 ms
- Rejets (moteur) : {'spread_below_threshold': 221689578, 'liquidity_below_min': 1929925, 'negative_expected_net': 1359192, 'borrow_bound_too_small': 213751, 'pool_quarantined': 97812, 'cycle_budget_exhausted': 1924}
- Enregistrements de la session : 1359354 ; net attendu > 0 : 162 ; simulés (eth_call de la vraie tx) : 24 (ok 12, échec 12) ; étiquettes ghost N+1 : 2/15 positives
- Décisions : {'REJECTED': 1359354} ; motifs de rejet : {'below_safety_margin': 115, 'negative_expected_net': 1359192, 'p_lower_below_threshold': 125, 'reliability_not_demonstrated': 37, 'simulation_failed': 12}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52802789 | USDC→[pancakeswap_v3]→PLAY→[aerodrome_slipstream]→USDC | 103.887016 USDC | 0.252695 USDC | 0.000000 USDC | 0.005449 USDC | 0.247246 USDC (0.2275 €) | — | 23.80 | 0.002 (n=4) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52802771 | WETH→[uniswap_v3]→NPC→[uniswap_v2]→WETH | 0.015606 WETH | 0.000026 WETH | 0.000000 WETH | 0.000002 WETH | 0.000024 WETH (0.0534 €) | — | 15.33 | — (n=0) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52802789 | USDC→[pancakeswap_v3]→PLAY→[aerodrome]→USDC | 20.416455 USDC | 0.042548 USDC | 0.000000 USDC | 0.005114 USDC | 0.037434 USDC (0.0344 €) | — | 18.34 | 0.001 (n=6) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52807301 | WETH→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.080174 WETH | 0.000016 WETH | 0.000000 WETH | 0.000002 WETH | 0.000013 WETH (0.0300 €) | — | 1.67 | 0.017 (n=49) | REJECTED | below_safety_margin(13391648405460<16034862175564), p_lower_below_threshold(0.02<0.75) |
| 52807301 | WETH→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.080174 WETH | 0.000016 WETH | 0.000000 WETH | 0.000002 WETH | 0.000013 WETH (0.0300 €) | — | 1.67 | 0.017 (n=49) | REJECTED | below_safety_margin(13391648405460<16034862175564), p_lower_below_threshold(0.02<0.75) |
| 52807301 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→cbBTC | 0.002422 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0297 €) | — | 1.61 | 0.017 (n=49) | REJECTED | below_safety_margin(39<48), p_lower_below_threshold(0.02<0.75) |
| 52807301 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→cbBTC | 0.002422 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0297 €) | — | 1.61 | 0.017 (n=49) | REJECTED | below_safety_margin(39<48), p_lower_below_threshold(0.02<0.75) |
| 52802956 | USDC→[aerodrome]→MET→[aerodrome]→WETH→[uniswap_v3]→USDC | 49.367589 USDC | 0.035707 USDC | 0.000000 USDC | 0.006635 USDC | 0.029072 USDC (0.0267 €) | — | 5.89 | 0.031 (n=92) | REJECTED | p_lower_below_threshold(0.03<0.75) |
| 52802956 | WETH→[uniswap_v3]→USDC→[aerodrome]→MET→[aerodrome]→WETH | 0.020334 WETH | 0.000015 WETH | 0.000000 WETH | 0.000003 WETH | 0.000012 WETH (0.0266 €) | — | 5.86 | 0.031 (n=92) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.03<0.75) |
| 52802956 | USDC→[aerodrome]→MET→[aerodrome]→WETH→[pancakeswap_v3]→USDC | 45.876940 USDC | 0.030372 USDC | 0.000000 USDC | 0.006635 USDC | 0.023737 USDC (0.0218 €) | — | 5.17 | 0.009 (n=32) | REJECTED | p_lower_below_threshold(0.01<0.75) |
| 52802956 | WETH→[pancakeswap_v3]→USDC→[aerodrome]→MET→[aerodrome]→WETH | 0.018878 WETH | 0.000012 WETH | 0.000000 WETH | 0.000003 WETH | 0.000010 WETH (0.0217 €) | — | 5.15 | 0.009 (n=32) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.01<0.75) |
| 52807301 | WETH→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.060547 WETH | 0.000011 WETH | 0.000000 WETH | 0.000003 WETH | 0.000007 WETH (0.0165 €) | — | 1.22 | 0.098 (n=146) | REJECTED | below_safety_margin(7368747136994<12109364047159), p_lower_below_threshold(0.10<0.75) |
| 52807301 | WETH→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.060547 WETH | 0.000011 WETH | 0.000000 WETH | 0.000003 WETH | 0.000007 WETH (0.0165 €) | — | 1.22 | 0.098 (n=146) | REJECTED | below_safety_margin(7368747136994<12109364047159), p_lower_below_threshold(0.10<0.75) |
| 52807301 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 139.638563 USDC | 0.025585 USDC | 0.000000 USDC | 0.007703 USDC | 0.017882 USDC (0.0165 €) | — | 1.28 | 0.098 (n=146) | REJECTED | below_safety_margin(17882<27927), p_lower_below_threshold(0.10<0.75) |
| 52807301 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 139.638563 USDC | 0.025585 USDC | 0.000000 USDC | 0.007703 USDC | 0.017882 USDC (0.0165 €) | — | 1.28 | 0.098 (n=146) | REJECTED | below_safety_margin(17882<27927), p_lower_below_threshold(0.10<0.75) |
| 52807301 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→cbBTC | 0.001547 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0160 €) | — | 1.36 | 0.098 (n=146) | REJECTED | below_safety_margin(21<30), p_lower_below_threshold(0.10<0.75) |
| 52807301 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→cbBTC | 0.001547 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0160 €) | — | 1.36 | 0.098 (n=146) | REJECTED | below_safety_margin(21<30), p_lower_below_threshold(0.10<0.75) |
| 52803331 | WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.227161 WETH | 0.000009 WETH | 0.000000 WETH | 0.000003 WETH | 0.000006 WETH (0.0132 €) | — | 0.26 | 0.098 (n=146) | REJECTED | below_safety_margin(5909103348279<45432209893061), p_lower_below_threshold(0.10<0.75) |
| 52803331 | WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.227161 WETH | 0.000009 WETH | 0.000000 WETH | 0.000003 WETH | 0.000006 WETH (0.0132 €) | — | 0.26 | 0.098 (n=146) | REJECTED | below_safety_margin(5909103348279<45432209893061), p_lower_below_threshold(0.10<0.75) |
| 52803331 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC | 547.409941 USDC | 0.022032 USDC | 0.000000 USDC | 0.007686 USDC | 0.014346 USDC (0.0132 €) | — | 0.26 | 0.098 (n=146) | REJECTED | below_safety_margin(14346<109481), p_lower_below_threshold(0.10<0.75) |
| 52803331 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC | 547.409941 USDC | 0.022032 USDC | 0.000000 USDC | 0.007686 USDC | 0.014346 USDC (0.0132 €) | — | 0.26 | 0.098 (n=146) | REJECTED | below_safety_margin(14346<109481), p_lower_below_threshold(0.10<0.75) |
| 52808544 | USDC→[aerodrome]→VIRTUAL→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 34.640257 USDC | 0.019737 USDC | 0.000000 USDC | 0.006954 USDC | 0.012783 USDC (0.0118 €) | — | 3.69 | 0.000 (n=18) | REJECTED | reliability_not_demonstrated |
| 52808544 | USDC→[aerodrome]→VIRTUAL→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 34.640257 USDC | 0.019737 USDC | 0.000000 USDC | 0.006954 USDC | 0.012783 USDC (0.0118 €) | — | 3.69 | 0.000 (n=18) | REJECTED | reliability_not_demonstrated |
| 52808544 | WETH→[pancakeswap_v3]→USDC→[aerodrome]→VIRTUAL→[aerodrome_slipstream]→WETH | 0.014400 WETH | 0.000008 WETH | 0.000000 WETH | 0.000003 WETH | 0.000005 WETH (0.0118 €) | 0.000005 WETH | 3.66 | 0.000 (n=18) | REJECTED | reliability_not_demonstrated |
| 52808544 | WETH→[pancakeswap_v3]→USDC→[aerodrome]→VIRTUAL→[aerodrome_slipstream]→WETH | 0.014400 WETH | 0.000008 WETH | 0.000000 WETH | 0.000003 WETH | 0.000005 WETH (0.0118 €) | 0.000005 WETH | 3.66 | 0.000 (n=18) | REJECTED | reliability_not_demonstrated |

## Fiabilité et décision
- Observations ghost : 1270 ; taux observé 0.103 ; borne inférieure crédible (0.9) 0.093 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 9.3% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
