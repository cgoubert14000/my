# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-19T14:45:11+00:00 ; durée 101.79 min ; blocs 52812825 → 52815879 (2925 vus)

## Connexion
- Requêtes RPC : 38115 ; erreurs : 78 ; latence p50/p95 : 118.4/592.3 ms
- Rafraîchissements d'état : 2925 ; âge des données au dernier bloc : 2.79 s ; changements de frais LP observés (pools à frais dynamiques) : 9186
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 49997 ; cycles déclenchés par événement : 1728 ; avance médiane sur le rafraîchissement multicall : 582 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,393.37 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 571 pools, 327 jetons, 21004 routes
- Par DEX : uniswap_v3 137, aerodrome 234 (quarantaine 2), aerodrome_slipstream 153, pancakeswap_v3 30, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 207 (rejetés 2) → 612 jetons ; pools candidats 3877 (énumérés 390, par paires 0), mesurés 574, sous le plancher de 10000.0 $ : 3 → gardés 571 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2419.85313, 'AERO': 0.782295, 'cbBTC': 82567.067054}
- Pools en quarantaine : 2 — aerodrome:fBOMB/AERO@0xbBf71A: simulation failed ×5 (model/chain mismatch) — until block 52815932; aerodrome:fBOMB/USDC@0xFf8e0b: simulation failed ×5 (model/chain mismatch) — until block 52815932

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 146,148,496 | 2,393.367855 | 52815880 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 34,713,286 | 1.303537 | 52815880 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 500 | 18,211,530 | 0.029237 | 52815880 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 16,940,492 | 103.256360 | 52815880 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 15,553,216 | 0.029224 | 52815880 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,315,205 | 0.029241 | 52815880 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,839,715 | 0.000012 | 52815880 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome_slipstream | USDC/cbBTC | 460 | 8,554,568 | 0.000012 | 52815880 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | WETH/USDC | 500 | 8,348,086 | 2,395.908587 | 52815880 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/USDC | 3000 | 8,296,083 | 2,393.612796 | 52815880 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | USDC/cbBTC | 342 | 7,815,307 | 0.000012 | 52815880 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 713 | 7,282,349 | 2,396.132133 | 52815880 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,158,666 | 0.001656 | 52815880 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,331,315 | 0.029248 | 52815880 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | USDC/AERO | 10000 | 5,125,039 | 1.295793 | 52815880 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome | fBOMB/AERO | 10000 | 4,862,374 | 0.025993 | 52815880 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,783,604 | 0.802395 | 52815880 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,600,616 | 0.000273 | 52815880 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/USDT | 436 | 4,586,596 | 2,399.037520 | 52815880 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,391,262 | 2,396.792826 | 52815880 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,338,250 | 0.998770 | 52815880 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 4,001,800 | 33,925.931430 | 52815880 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/AERO | 10000 | 3,202,577 | 3,097.615919 | 52815880 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,849,768 | 0.000012 | 52815880 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,712,255 | 1.142083 | 52815880 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,688,801 | 406.095471 | 52815880 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | WETH/VVV | 2706 | 2,602,623 | 103.231394 | 52815880 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | AERO/cbBTC | 2700 | 2,178,555 | 0.000009 | 52815880 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | WETH/FAI | 10000 | 2,171,489 | 1,233,192.674710 | 52815880 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,059,117 | 1.238200 | 52815880 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,036,743 | 1.372638 | 52815880 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| uniswap_v3 | BNKR/WETH | 10000 | 2,035,950 | 0.000000 | 52815880 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,805,668 | 13,900.948547 | 52815880 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,769,456 | 0.000012 | 52815880 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | XDP/USDC | 100 | 1,764,926 | 0.018607 | 52815880 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome | weETH_04c0/WETH | 500 | 1,730,602 | 1.105523 | 52815880 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome | fBOMB/USDC | 10000 | 1,714,177 | 0.020490 | 52815880 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| aerodrome_slipstream | WETH/MORPHO | 2745 | 1,700,873 | 969.588610 | 52815880 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,669,008 | 16.186674 | 52815880 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | WETH/msETH (stable) | 500 | 1,656,429 | 2.306702 | 52815880 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | WETH/AERO | 3000 | 1,583,309 | 3,119.512942 | 52815880 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,550,206 | 0.916350 | 52815880 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,456,364 | 0.827177 | 52815880 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | EURC/USDC | 73 | 1,406,275 | 1.121514 | 52815880 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,337,795 | 0.435482 | 52815880 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,310,762 | 0.000000 | 52815880 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,289,589 | 0.000274 | 52815880 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,283,505 | 0.004610 | 52815880 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome | WETH/cbBTC | 3000 | 1,278,436 | 0.029246 | 52815880 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,268,827 | 23.125669 | 52815880 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| aerodrome | USDC/SEND | 3000 | 1,232,735 | 63.944487 | 52815880 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,193,444 | 35,176,396.575847 | 52815880 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,192,194 | 2,395.971577 | 52815880 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | WETH/WELL | 10000 | 1,190,295 | 1,096,201.771263 | 52815880 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome_slipstream | WETH/msETH | 500 | 1,134,840 | 1.131578 | 52815880 | `0x74F72788F4814D7fF3C49B44684aa98Eee140C0E` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,126,278 | 515,481.870232 | 52815880 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | USDC/NOCK | 3000 | 1,092,795 | 52.762423 | 52815880 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | msUSD/USDC | 500 | 1,079,777 | 0.885437 | 52815880 | `0x7501bc8Bb51616F79bfA524E464fb7B41f0B10fB` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,074,842 | 15.607263 | 52815880 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | WETH/EDEL | 7000 | 1,050,666 | 89,392.643977 | 52815880 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |

## Recherche d'opportunités
- Cycles : 4652 ; routes examinées : 97710608 ; candidats optimisés : 706995 ; net attendu > 0 : 282 ; dernier cycle 193.0 ms
- Rejets (moteur) : {'spread_below_threshold': 95768175, 'liquidity_below_min': 909328, 'negative_expected_net': 706713, 'pool_quarantined': 206960, 'borrow_bound_too_small': 68748, 'cycle_budget_exhausted': 50402}
- Enregistrements de la session : 706995 ; net attendu > 0 : 282 ; simulés (eth_call de la vraie tx) : 50 (ok 21, échec 29) ; étiquettes ghost N+1 : 7/24 positives
- Décisions : {'REJECTED': 706995} ; motifs de rejet : {'below_safety_margin': 226, 'negative_expected_net': 706713, 'p_lower_below_threshold': 242, 'price_impact': 30, 'reliability_not_demonstrated': 40, 'sim_below_estimate': 4, 'simulated_net_nonpositive': 3, 'simulation_failed': 29, 'stale_data': 3}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52815204 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 1,735.428521 USDC | 0.154603 USDC | 0.000000 USDC | 0.006144 USDC | 0.148459 USDC (0.1366 €) | — | 0.86 | 0.017 (n=49) | REJECTED | below_safety_margin(148459<347085), p_lower_below_threshold(0.02<0.75) |
| 52815204 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.726513 WETH | 0.000065 WETH | 0.000000 WETH | 0.000003 WETH | 0.000062 WETH (0.1365 €) | — | 0.85 | 0.017 (n=49) | REJECTED | below_safety_margin(61999402150527<145302574799060), p_lower_below_threshold(0.02<0.75) |
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
| 52815225 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 393.383697 USDC | 0.062903 USDC | 0.000000 USDC | 0.006146 USDC | 0.056757 USDC (0.0522 €) | — | 1.44 | 0.017 (n=49) | REJECTED | below_safety_margin(56757<78676), p_lower_below_threshold(0.02<0.75) |
| 52815225 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.164600 WETH | 0.000026 WETH | 0.000000 WETH | 0.000003 WETH | 0.000024 WETH (0.0522 €) | — | 1.44 | 0.017 (n=49) | REJECTED | below_safety_margin(23695395236658<32919958684015), p_lower_below_threshold(0.02<0.75) |
| 52815240 | USDC→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→USDC | 270.392256 USDC | 0.059859 USDC | 0.000000 USDC | 0.007243 USDC | 0.052616 USDC (0.0484 €) | — | 1.95 | 0.296 (n=71) | REJECTED | below_safety_margin(52616<54078), p_lower_below_threshold(0.30<0.75) |
| 52815239 | USDC→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→USDC | 270.392256 USDC | 0.059859 USDC | 0.000000 USDC | 0.007243 USDC | 0.052616 USDC (0.0484 €) | — | 1.95 | 0.296 (n=71) | REJECTED | below_safety_margin(52616<54078), p_lower_below_threshold(0.30<0.75) |
| 52815240 | cbBTC→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→cbBTC | 0.002715 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0483 €) | 0.000001 cbBTC | 2.36 | 0.296 (n=71) | REJECTED | p_lower_below_threshold(0.30<0.75) |
| 52815239 | cbBTC→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→cbBTC | 0.002715 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0483 €) | — | 2.36 | 0.296 (n=71) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.30<0.75) |
| 52815204 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 753.505362 USDC | 0.057837 USDC | 0.000000 USDC | 0.007608 USDC | 0.050229 USDC (0.0462 €) | — | 0.67 | 0.002 (n=5) | REJECTED | below_safety_margin(50229<150701), reliability_not_demonstrated |
| 52815204 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.291064 WETH | 0.000024 WETH | 0.000000 WETH | 0.000003 WETH | 0.000021 WETH (0.0461 €) | — | 0.72 | 0.002 (n=5) | REJECTED | below_safety_margin(20937351503272<58212731814837), reliability_not_demonstrated |
| 52815204 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.008366 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0460 €) | — | 0.73 | 0.002 (n=5) | REJECTED | below_safety_margin(61<167), reliability_not_demonstrated |
| 52814592 | USDC→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→cbBTC→[aerodrome]→USDC | 72.995841 USDC | 0.047349 USDC | 0.000000 USDC | 0.006907 USDC | 0.040442 USDC (0.0372 €) | — | 5.54 | 0.037 (n=95) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.04<0.75) |

## Fiabilité et décision
- Observations ghost : 1294 ; taux observé 0.107 ; borne inférieure crédible (0.9) 0.096 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 9.6% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
