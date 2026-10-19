# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-19T13:06:25+00:00 ; durée 3.02 min ; blocs 52812825 → 52812918 (91 vus)

## Connexion
- Requêtes RPC : 1286 ; erreurs : 0 ; latence p50/p95 : 191.0/964.3 ms
- Rafraîchissements d'état : 92 ; âge des données au dernier bloc : 1.97 s ; changements de frais LP observés (pools à frais dynamiques) : 204
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 1576 ; cycles déclenchés par événement : 81 ; avance médiane sur le rafraîchissement multicall : 1,102 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,420.31 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 571 pools, 327 jetons, 21004 routes
- Par DEX : uniswap_v3 137, aerodrome 234, aerodrome_slipstream 153, pancakeswap_v3 30, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 207 (rejetés 2) → 612 jetons ; pools candidats 3877 (énumérés 390, par paires 0), mesurés 574, sous le plancher de 10000.0 $ : 3 → gardés 571 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2419.85313, 'AERO': 0.782295, 'cbBTC': 82567.067054}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 148,119,585 | 2,420.305123 | 52812918 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 35,053,581 | 1.278298 | 52812918 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 500 | 18,417,604 | 0.029356 | 52812918 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 17,700,116 | 0.029400 | 52812918 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/VVV | 3000 | 17,275,883 | 101.533523 | 52812918 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,410,549 | 0.029384 | 52812918 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,871,951 | 0.000012 | 52812918 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome_slipstream | USDC/cbBTC | 532 | 8,575,560 | 0.000012 | 52812918 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | WETH/USDC | 500 | 8,459,839 | 2,426.437856 | 52812918 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/USDC | 3000 | 8,342,630 | 2,420.381484 | 52812918 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | USDC/cbBTC | 354 | 7,836,139 | 0.000012 | 52812918 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 698 | 7,665,458 | 2,426.739608 | 52812918 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,230,280 | 0.001665 | 52812918 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,366,631 | 0.029360 | 52812918 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | fBOMB/AERO | 10000 | 4,945,182 | 0.025987 | 52812918 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,837,443 | 0.802395 | 52812918 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome_slipstream | USDC/AERO | 10000 | 4,745,888 | 1.281750 | 52812918 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,652,248 | 0.000273 | 52812918 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,446,203 | 2,426.629610 | 52812918 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,368,599 | 0.998771 | 52812918 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome_slipstream | WETH/USDT | 433 | 4,074,656 | 2,429.664333 | 52812918 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome | WETH/KTA | 3000 | 4,037,172 | 34,088.622025 | 52812918 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/AERO | 10000 | 3,252,158 | 3,085.397120 | 52812918 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,861,386 | 0.000012 | 52812918 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,737,953 | 1.142011 | 52812918 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,657,174 | 405.939938 | 52812918 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | WETH/VVV | 2706 | 2,652,681 | 101.564570 | 52812918 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 2,513,487 | 0.000009 | 52812918 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | WETH/FAI | 10000 | 2,194,269 | 1,235,059.554017 | 52812918 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,062,172 | 1.234881 | 52812918 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | BNKR/WETH | 10000 | 2,047,574 | 0.000000 | 52812918 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,036,743 | 1.372638 | 52812918 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,893,616 | 16.021945 | 52812918 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,773,624 | 0.000012 | 52812918 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | XDP/USDC | 100 | 1,765,999 | 0.018618 | 52812918 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome | weETH_04c0/WETH | 500 | 1,750,080 | 1.105523 | 52812918 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome | fBOMB/USDC | 10000 | 1,726,270 | 0.020594 | 52812918 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| aerodrome | WETH/msETH (stable) | 500 | 1,674,020 | 2.308863 | 52812918 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,662,010 | 13,840.094665 | 52812918 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome_slipstream | EURC/USDC | 76 | 1,612,633 | 1.122683 | 52812918 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| uniswap_v3 | WETH/AERO | 3000 | 1,605,819 | 3,103.014720 | 52812918 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,567,654 | 0.916350 | 52812918 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,456,163 | 0.827402 | 52812918 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,339,449 | 0.436285 | 52812918 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,325,306 | 0.000000 | 52812918 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,304,040 | 0.000274 | 52812918 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | WETH/cbBTC | 3000 | 1,286,150 | 0.029380 | 52812918 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,284,851 | 0.004581 | 52812918 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,259,042 | 23.157079 | 52812918 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| aerodrome | USDC/SEND | 3000 | 1,232,870 | 63.930475 | 52812918 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome_slipstream | WETH/MORPHO | 2718 | 1,228,815 | 982.958647 | 52812918 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome | WETH/WELL | 10000 | 1,213,642 | 1,078,301.125550 | 52812918 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/doginme | 10000 | 1,203,839 | 35,127,631.351010 | 52812918 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,200,565 | 2,426.442807 | 52812918 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome_slipstream | msUSD/USDC | 500 | 1,177,661 | 0.885973 | 52812918 | `0x7501bc8Bb51616F79bfA524E464fb7B41f0B10fB` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,138,954 | 515,481.870232 | 52812918 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | USDC/NOCK | 3000 | 1,104,364 | 51.662752 | 52812918 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | WETH/msETH | 500 | 1,099,160 | 1.131965 | 52812918 | `0x74F72788F4814D7fF3C49B44684aa98Eee140C0E` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,082,109 | 15.336556 | 52812918 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | WETH/EDEL | 7000 | 1,059,860 | 89,825.906924 | 52812918 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |

## Recherche d'opportunités
- Cycles : 172 ; routes examinées : 3612688 ; candidats optimisés : 38888 ; net attendu > 0 : 0 ; dernier cycle 320.3 ms
- Rejets (moteur) : {'spread_below_threshold': 3531302, 'negative_expected_net': 38888, 'liquidity_below_min': 38494, 'borrow_bound_too_small': 4004}
- Enregistrements de la session : 38888 ; net attendu > 0 : 0 ; simulés (eth_call de la vraie tx) : 0 (ok 0, échec 0) ; étiquettes ghost N+1 : 0/0 positives
- Décisions : {'REJECTED': 38888} ; motifs de rejet : {'negative_expected_net': 38888}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|

_Aucun candidat à net positif. Les 10 plus proches de la rentabilité (net attendu négatif) :_

| Bloc | Route | Montant | Brut | Frais flash | Gaz (dont L1) | Net attendu (€) | Marge (bps) |
|---:|---|---:|---:|---:|---:|---:|---:|
| 52812880 | USDC→[aerodrome]→WETH→[uniswap_v3]→USDC | 4.183505 USDC | 0.002293 USDC | 0.000000 USDC | 0.005106 USDC | -0.0026 | -6.72 |
| 52812880 | USDC→[aerodrome]→WETH→[uniswap_v3]→USDC | 4.183505 USDC | 0.002293 USDC | 0.000000 USDC | 0.005106 USDC | -0.0026 | -6.72 |
| 52812880 | WETH→[uniswap_v3]→USDC→[aerodrome]→WETH | 0.001749 WETH | 0.000001 WETH | 0.000000 WETH | 0.000002 WETH | -0.0026 | -6.66 |
| 52812880 | WETH→[uniswap_v3]→USDC→[aerodrome]→WETH | 0.001749 WETH | 0.000001 WETH | 0.000000 WETH | 0.000002 WETH | -0.0026 | -6.66 |
| 52812905 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 10.485993 USDC | 0.002594 USDC | 0.000000 USDC | 0.005441 USDC | -0.0026 | -2.72 |
| 52812906 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 10.485993 USDC | 0.002594 USDC | 0.000000 USDC | 0.005441 USDC | -0.0026 | -2.72 |
| 52812906 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 10.485993 USDC | 0.002594 USDC | 0.000000 USDC | 0.005441 USDC | -0.0026 | -2.72 |
| 52812907 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 10.485993 USDC | 0.002594 USDC | 0.000000 USDC | 0.005441 USDC | -0.0026 | -2.72 |
| 52812907 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 10.485993 USDC | 0.002594 USDC | 0.000000 USDC | 0.005441 USDC | -0.0026 | -2.72 |
| 52812881 | USDC→[aerodrome]→WETH→[uniswap_v3]→USDC | 4.153426 USDC | 0.002248 USDC | 0.000000 USDC | 0.005107 USDC | -0.0026 | -6.88 |

## Fiabilité et décision
- Observations ghost : 1270 ; taux observé 0.103 ; borne inférieure crédible (0.9) 0.093 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 9.3% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
