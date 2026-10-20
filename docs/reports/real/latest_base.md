# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-20T06:43:13+00:00 ; durée 36.72 min ; blocs 52843518 → 52844622 (1102 vus)

## Connexion
- Requêtes RPC : 13899 ; erreurs : 0 ; latence p50/p95 : 73.1/1,262.9 ms
- Rafraîchissements d'état : 1103 ; âge des données au dernier bloc : 1.25 s ; changements de frais LP observés (pools à frais dynamiques) : 1875
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
| uniswap_v3 | WETH/USDC | 3000 | 146,152,703 | 2,395.979728 | 52844622 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 34,439,269 | 1.241551 | 52844622 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 18,791,000 | 0.029339 | 52844622 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 500 | 18,163,268 | 0.029316 | 52844622 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 17,397,913 | 98.023988 | 52844622 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,350,226 | 0.029323 | 52844622 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,876,618 | 0.000012 | 52844622 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 8,341,329 | 2,398.225132 | 52844622 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/USDC | 3000 | 8,297,731 | 2,396.322867 | 52844622 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | USDC/cbBTC | 448 | 8,264,600 | 0.000012 | 52844622 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome_slipstream | USDC/cbBTC | 340 | 7,824,305 | 0.000012 | 52844622 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 669 | 7,786,151 | 2,398.447963 | 52844622 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,184,259 | 0.001673 | 52844622 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,332,789 | 0.029328 | 52844622 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | fBOMB/AERO | 10000 | 4,972,368 | 0.025571 | 52844622 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,773,499 | 0.802395 | 52844622 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,621,627 | 0.000275 | 52844622 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,454,019 | 2,398.480814 | 52844622 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | USDC/AERO | 10000 | 4,377,271 | 1.238258 | 52844622 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,331,303 | 0.998768 | 52844622 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,959,343 | 34,733.108525 | 52844622 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDT | 418 | 3,579,005 | 2,401.149339 | 52844622 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome | WETH/AERO | 10000 | 3,247,185 | 2,983.562684 | 52844622 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,874,061 | 0.000012 | 52844622 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,752,768 | 399.301958 | 52844622 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,741,283 | 1.142105 | 52844622 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| aerodrome_slipstream | WETH/VVV | 2712 | 2,657,315 | 97.991143 | 52844622 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | WETH/FAI | 10000 | 2,183,262 | 1,222,592.439063 | 52844622 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 2,091,575 | 0.000010 | 52844622 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,059,504 | 1.238011 | 52844622 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,036,015 | 1.373598 | 52844622 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,945,175 | 0.000000 | 52844622 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome_slipstream | WETH/MORPHO | 2706 | 1,881,409 | 975.600082 | 52844622 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,837,295 | 13,638.264127 | 52844622 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | XDP/USDC | 100 | 1,793,402 | 0.019071 | 52844622 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,768,569 | 0.000012 | 52844622 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,754,958 | 16.025404 | 52844622 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | weETH_04c0/WETH | 500 | 1,733,567 | 1.105525 | 52844622 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome | fBOMB/USDC | 10000 | 1,678,286 | 0.020333 | 52844622 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| aerodrome_slipstream | EURC/USDC | 70 | 1,668,250 | 1.123103 | 52844622 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| aerodrome | WETH/msETH (stable) | 500 | 1,651,098 | 2.307033 | 52844622 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,551,913 | 0.916343 | 52844622 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| uniswap_v3 | WETH/AERO | 3000 | 1,507,514 | 2,976.116766 | 52844622 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,457,650 | 0.826605 | 52844622 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | DRB/WETH | 10000 | 1,306,166 | 0.000000 | 52844622 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,299,724 | 0.004702 | 52844622 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,295,741 | 0.000276 | 52844622 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | WETH/cbBTC | 3000 | 1,282,028 | 0.029321 | 52844622 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,248,310 | 2,397.709151 | 52844622 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,228,847 | 64.349833 | 52844622 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome | WETH/WELL | 10000 | 1,205,938 | 1,070,289.857301 | 52844622 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,200,693 | 23.000907 | 52844622 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| uniswap_v3 | WETH/doginme | 10000 | 1,192,328 | 35,427,093.560652 | 52844622 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,167,961 | 0.435770 | 52844622 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| aerodrome_slipstream | WETH/msETH | 500 | 1,135,179 | 1.131586 | 52844622 | `0x74F72788F4814D7fF3C49B44684aa98Eee140C0E` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,134,589 | 516,320.409502 | 52844622 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | USDC/NOCK | 3000 | 1,122,798 | 49.980309 | 52844622 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome | WETH/EDEL | 7000 | 1,117,994 | 79,247.522226 | 52844622 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome_slipstream | msUSD/USDC | 500 | 1,110,568 | 0.885510 | 52844622 | `0x7501bc8Bb51616F79bfA524E464fb7B41f0B10fB` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,077,280 | 15.530369 | 52844622 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |

## Recherche d'opportunités
- Cycles : 1225 ; routes examinées : 26023900 ; candidats optimisés : 101880 ; net attendu > 0 : 1 ; dernier cycle 233.3 ms
- Rejets (moteur) : {'spread_below_threshold': 25707676, 'liquidity_below_min': 183719, 'negative_expected_net': 101879, 'borrow_bound_too_small': 30625}
- Enregistrements de la session : 101880 ; net attendu > 0 : 1 ; simulés (eth_call de la vraie tx) : 0 (ok 0, échec 0) ; étiquettes ghost N+1 : 0/0 positives
- Décisions : {'REJECTED': 101880} ; motifs de rejet : {'below_safety_margin': 1, 'negative_expected_net': 101879, 'p_lower_below_threshold': 1}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52844622 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 20.372606 USDC | 0.009322 USDC | 0.000000 USDC | 0.005380 USDC | 0.003942 USDC (0.0036 €) | — | 1.93 | 0.016 (n=52) | REJECTED | below_safety_margin(3942<4074), p_lower_below_threshold(0.02<0.75) |

## Fiabilité et décision
- Observations ghost : 1388 ; taux observé 0.102 ; borne inférieure crédible (0.9) 0.092 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 9.2% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
