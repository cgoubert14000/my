# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-20T06:37:02+00:00 ; durée 30.55 min ; blocs 52843518 → 52844437 (917 vus)

## Connexion
- Requêtes RPC : 11593 ; erreurs : 0 ; latence p50/p95 : 76.2/1,236.1 ms
- Rafraîchissements d'état : 918 ; âge des données au dernier bloc : 1.17 s ; changements de frais LP observés (pools à frais dynamiques) : 1543
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 2296 ; cycles déclenchés par événement : 123 ; avance médiane sur le rafraîchissement multicall : 435 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,395.98 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 572 pools, 327 jetons, 21244 routes
- Par DEX : uniswap_v3 136, aerodrome 235, aerodrome_slipstream 154, pancakeswap_v3 30, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 207 (rejetés 2) → 612 jetons ; pools candidats 3877 (énumérés 392, par paires 0), mesurés 574, sous le plancher de 10000.0 $ : 2 → gardés 572 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDC': 1.0, 'USDbC': 1.0, 'WETH': 2396.704066, 'AERO': 0.805188, 'cbBTC': 81576.404653}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 146,150,224 | 2,395.979728 | 52844437 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 34,430,421 | 1.242189 | 52844437 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 18,793,987 | 0.029339 | 52844437 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 500 | 18,164,110 | 0.029309 | 52844437 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 17,392,663 | 98.083177 | 52844437 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,351,120 | 0.029323 | 52844437 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,874,426 | 0.000012 | 52844437 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome_slipstream | USDC/cbBTC | 424 | 8,561,857 | 0.000012 | 52844437 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | WETH/USDC | 500 | 8,341,179 | 2,396.257540 | 52844437 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/USDC | 3000 | 8,297,731 | 2,396.207591 | 52844437 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | WETH/USDC | 535 | 8,006,242 | 2,396.045380 | 52844437 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | USDC/cbBTC | 334 | 7,825,029 | 0.000012 | 52844437 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,181,771 | 0.001671 | 52844437 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,333,100 | 0.029318 | 52844437 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | fBOMB/AERO | 10000 | 4,971,078 | 0.025571 | 52844437 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,773,499 | 0.802395 | 52844437 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome_slipstream | USDC/AERO | 10000 | 4,638,224 | 1.238258 | 52844437 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,621,627 | 0.000275 | 52844437 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,453,886 | 2,395.822474 | 52844437 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,332,329 | 0.998768 | 52844437 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,959,343 | 34,733.108559 | 52844437 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDT | 406 | 3,891,949 | 2,399.689154 | 52844437 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome | WETH/AERO | 10000 | 3,246,350 | 2,983.562684 | 52844437 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 2,903,566 | 975.989620 | 52844437 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,874,467 | 0.000012 | 52844437 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,741,283 | 1.142105 | 52844437 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| aerodrome_slipstream | WETH/VVV | 2703 | 2,656,633 | 98.047497 | 52844437 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,618,516 | 399.301871 | 52844437 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 2,242,570 | 0.000010 | 52844437 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | WETH/FAI | 10000 | 2,182,765 | 1,223,150.335868 | 52844437 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,059,504 | 1.238011 | 52844437 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,036,015 | 1.373598 | 52844437 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,945,175 | 0.000000 | 52844437 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,852,211 | 16.025404 | 52844437 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,831,315 | 13,638.264127 | 52844437 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | XDP/USDC | 100 | 1,795,441 | 0.019112 | 52844437 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,768,804 | 0.000012 | 52844437 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | weETH_04c0/WETH | 500 | 1,733,567 | 1.105525 | 52844437 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome | fBOMB/USDC | 10000 | 1,678,284 | 0.020333 | 52844437 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| aerodrome_slipstream | EURC/USDC | 70 | 1,668,302 | 1.123159 | 52844437 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| aerodrome | WETH/msETH (stable) | 500 | 1,651,098 | 2.307033 | 52844437 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,551,913 | 0.916343 | 52844437 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| uniswap_v3 | WETH/AERO | 3000 | 1,507,233 | 2,975.305576 | 52844437 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,457,650 | 0.826605 | 52844437 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | DRB/WETH | 10000 | 1,306,177 | 0.000000 | 52844437 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,299,724 | 0.004702 | 52844437 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,295,741 | 0.000276 | 52844437 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | WETH/cbBTC | 3000 | 1,282,180 | 0.029321 | 52844437 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,248,302 | 2,396.214246 | 52844437 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,228,847 | 64.349833 | 52844437 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome | WETH/WELL | 10000 | 1,206,854 | 1,068,665.872569 | 52844437 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,200,693 | 23.000907 | 52844437 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| uniswap_v3 | WETH/doginme | 10000 | 1,192,328 | 35,427,093.560652 | 52844437 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,167,961 | 0.435770 | 52844437 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| aerodrome_slipstream | WETH/msETH | 500 | 1,135,179 | 1.131586 | 52844437 | `0x74F72788F4814D7fF3C49B44684aa98Eee140C0E` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,134,186 | 516,831.795511 | 52844437 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | USDC/NOCK | 3000 | 1,122,797 | 49.980319 | 52844437 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome | WETH/EDEL | 7000 | 1,117,994 | 79,247.522226 | 52844437 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome_slipstream | msUSD/USDC | 500 | 1,110,568 | 0.885510 | 52844437 | `0x7501bc8Bb51616F79bfA524E464fb7B41f0B10fB` |
| aerodrome_slipstream | USDC/USDT | 8 | 1,075,224 | 1.001423 | 52844437 | `0xa41Bc0AFfbA7Fd420d186b84899d7ab2aC57fcD1` |

## Recherche d'opportunités
- Cycles : 1040 ; routes examinées : 22093760 ; candidats optimisés : 85336 ; net attendu > 0 : 0 ; dernier cycle 472.0 ms
- Rejets (moteur) : {'spread_below_threshold': 21827225, 'liquidity_below_min': 155199, 'negative_expected_net': 85336, 'borrow_bound_too_small': 26000}
- Enregistrements de la session : 85336 ; net attendu > 0 : 0 ; simulés (eth_call de la vraie tx) : 0 (ok 0, échec 0) ; étiquettes ghost N+1 : 0/0 positives
- Décisions : {'REJECTED': 85336} ; motifs de rejet : {'negative_expected_net': 85336}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|

_Aucun candidat à net positif. Les 10 plus proches de la rentabilité (net attendu négatif) :_

| Bloc | Route | Montant | Brut | Frais flash | Gaz (dont L1) | Net attendu (€) | Marge (bps) |
|---:|---|---:|---:|---:|---:|---:|---:|
| 52843833 | WETH→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.014557 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | -0.0012 | -0.39 |
| 52843833 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→USDC | 34.753518 USDC | 0.006206 USDC | 0.000000 USDC | 0.007567 USDC | -0.0013 | -0.39 |
| 52843754 | USDC→[aerodrome_slipstream]→AERO→[aerodrome]→AUKI→[aerodrome]→USDC | 6.419528 USDC | 0.005079 USDC | 0.000000 USDC | 0.006542 USDC | -0.0013 | -2.28 |
| 52843755 | USDC→[aerodrome_slipstream]→AERO→[aerodrome]→AUKI→[aerodrome]→USDC | 6.419528 USDC | 0.005079 USDC | 0.000000 USDC | 0.006542 USDC | -0.0013 | -2.28 |
| 52843756 | USDC→[aerodrome_slipstream]→AERO→[aerodrome]→AUKI→[aerodrome]→USDC | 6.419528 USDC | 0.005079 USDC | 0.000000 USDC | 0.006542 USDC | -0.0013 | -2.28 |
| 52843757 | USDC→[aerodrome_slipstream]→AERO→[aerodrome]→AUKI→[aerodrome]→USDC | 6.419528 USDC | 0.005079 USDC | 0.000000 USDC | 0.006542 USDC | -0.0013 | -2.28 |
| 52843758 | USDC→[aerodrome_slipstream]→AERO→[aerodrome]→AUKI→[aerodrome]→USDC | 6.419528 USDC | 0.005079 USDC | 0.000000 USDC | 0.006542 USDC | -0.0013 | -2.28 |
| 52843759 | USDC→[aerodrome_slipstream]→AERO→[aerodrome]→AUKI→[aerodrome]→USDC | 6.419528 USDC | 0.005079 USDC | 0.000000 USDC | 0.006542 USDC | -0.0013 | -2.28 |
| 52843760 | USDC→[aerodrome_slipstream]→AERO→[aerodrome]→AUKI→[aerodrome]→USDC | 6.419528 USDC | 0.005079 USDC | 0.000000 USDC | 0.006542 USDC | -0.0013 | -2.28 |
| 52843761 | USDC→[aerodrome_slipstream]→AERO→[aerodrome]→AUKI→[aerodrome]→USDC | 6.419528 USDC | 0.005079 USDC | 0.000000 USDC | 0.006542 USDC | -0.0013 | -2.28 |

## Fiabilité et décision
- Observations ghost : 1388 ; taux observé 0.102 ; borne inférieure crédible (0.9) 0.092 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 9.2% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
