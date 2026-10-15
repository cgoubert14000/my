# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-15T02:19:40+00:00 ; durée 3.01 min ; blocs 52620621 → 52620708 (61 vus)

## Connexion
- Requêtes RPC : 944 ; erreurs : 0 ; latence p50/p95 : 405.3/2,366.8 ms
- Rafraîchissements d'état : 61 ; âge des données au dernier bloc : 17.39 s ; changements de frais LP observés (pools à frais dynamiques) : 352
- Flux d'événements (WebSocket Swap/Sync) : non connecté ; événements appliqués : 0 ; cycles déclenchés par événement : 0 ; avance médiane sur le rafraîchissement multicall : — ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,410.45 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 576 pools, 326 jetons, 21316 routes
- Par DEX : uniswap_v3 139, aerodrome 235, aerodrome_slipstream 153, pancakeswap_v3 31, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 206 (rejetés 2) → 611 jetons ; pools candidats 3916 (énumérés 390, par paires 0), mesurés 578, sous le plancher de 10000.0 $ : 2 → gardés 576 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDbC': 1.0, 'USDC': 1.0, 'WETH': 2411.100006, 'AERO': 0.880097, 'cbBTC': 81403.044787}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 146,481,971 | 2,410.454944 | 52620711 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 44,920,205 | 1.138189 | 52620711 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 500 | 17,727,655 | 0.029561 | 52620711 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 15,698,290 | 108.423523 | 52620711 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 15,301,238 | 0.029599 | 52620711 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,406,298 | 0.029607 | 52620711 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,217,960 | 0.000012 | 52620711 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 9,167,510 | 2,409.685594 | 52620711 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/USDC | 3000 | 8,933,741 | 2,410.759711 | 52620711 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | USDC/cbBTC | 352 | 7,954,920 | 0.000012 | 52620711 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 743 | 7,337,820 | 2,410.375446 | 52620711 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,142,067 | 0.001661 | 52620711 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 520 | 6,326,777 | 0.000012 | 52620711 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome | fBOMB/AERO | 10000 | 5,374,598 | 0.026421 | 52620711 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,356,990 | 0.029557 | 52620711 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,576,946 | 0.000278 | 52620711 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,532,879 | 0.802387 | 52620711 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,361,455 | 2,410.550873 | 52620711 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | USDC/AERO | 10000 | 4,287,924 | 1.129650 | 52620711 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,184,407 | 1.000078 | 52620711 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,989,705 | 34,621.020799 | 52620711 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/AERO | 10000 | 3,523,139 | 2,718.694945 | 52620711 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,836,439 | 0.000012 | 52620711 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | AERO/cbBTC | 2700 | 2,613,557 | 0.000011 | 52620711 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,565,089 | 1.141646 | 52620711 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| aerodrome_slipstream | WETH/VVV | 2901 | 2,539,311 | 108.540699 | 52620711 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,428,568 | 408.786179 | 52620711 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | WETH/FAI | 10000 | 2,349,773 | 1,068,249.628419 | 52620711 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | WETH/USDT | 430 | 2,212,726 | 2,413.295697 | 52620711 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,113,498 | 1.193715 | 52620711 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | BNKR/WETH | 10000 | 2,058,207 | 0.000000 | 52620711 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome | fBOMB/USDC | 10000 | 1,850,053 | 0.023714 | 52620711 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| aerodrome | USDC/alUSDb (stable) | 500 | 1,837,844 | 1.402356 | 52620711 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,837,384 | 15.747767 | 52620711 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,814,825 | 0.916544 | 52620711 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,776,330 | 0.000012 | 52620711 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | XDP/USDC | 100 | 1,775,697 | 0.018864 | 52620711 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome | WETH/msETH (stable) | 500 | 1,617,642 | 2.303898 | 52620711 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,563,614 | 13,830.157392 | 52620711 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | WETH/AERO | 3000 | 1,511,306 | 2,738.056241 | 52620711 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | weETH_04c0/WETH | 500 | 1,490,363 | 1.105778 | 52620711 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,454,834 | 0.834032 | 52620711 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | DRB/WETH | 10000 | 1,363,798 | 0.000000 | 52620711 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,338,440 | 0.004841 | 52620711 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | WETH/AERO | 3076 | 1,338,223 | 2,737.813486 | 52620711 | `0x82321f3BEB69f503380D6B233857d5C43562e2D0` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,309,217 | 0.000276 | 52620711 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome_slipstream | WETH/msETH | 500 | 1,296,246 | 1.131019 | 52620711 | `0x74F72788F4814D7fF3C49B44684aa98Eee140C0E` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,280,968 | 23.269964 | 52620711 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| aerodrome_slipstream | EURC/USDC | 79 | 1,275,205 | 1.121580 | 52620711 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| aerodrome | USDC/SEND | 3000 | 1,246,903 | 62.499604 | 52620711 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,215,007 | 2,409.637609 | 52620711 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,202,226 | 1.105594 | 52620711 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |
| uniswap_v3 | WETH/doginme | 10000 | 1,199,400 | 35,104,185.824925 | 52620711 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome_slipstream | WETH/MORPHO | 2721 | 1,191,768 | 1,031.720920 | 52620711 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome | WETH/EDEL | 7000 | 1,169,518 | 73,777.424997 | 52620711 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,154,625 | 491,487.875126 | 52620711 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | WETH/cbBTC | 3000 | 1,153,620 | 0.029601 | 52620711 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| aerodrome | WETH/WELL | 10000 | 1,149,274 | 1,192,876.945164 | 52620711 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome_slipstream | msUSD/USDC | 500 | 1,139,980 | 0.885606 | 52620711 | `0x7501bc8Bb51616F79bfA524E464fb7B41f0B10fB` |
| aerodrome | USDC/NOCK | 3000 | 1,120,515 | 50.194648 | 52620711 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |

## Recherche d'opportunités
- Cycles : 60 ; routes examinées : 1278960 ; candidats optimisés : 5601 ; net attendu > 0 : 0 ; dernier cycle 324.7 ms
- Rejets (moteur) : {'spread_below_threshold': 1257275, 'liquidity_below_min': 13492, 'negative_expected_net': 5601, 'borrow_bound_too_small': 1440, 'cycle_budget_exhausted': 1032, 'unquotable': 120}
- Enregistrements de la session : 5601 ; net attendu > 0 : 0 ; simulés (eth_call de la vraie tx) : 0 (ok 0, échec 0) ; étiquettes ghost N+1 : 0/0 positives
- Décisions : {'REJECTED': 5601} ; motifs de rejet : {'negative_expected_net': 5601}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|

_Aucun candidat à net positif. Les 10 plus proches de la rentabilité (net attendu négatif) :_

| Bloc | Route | Montant | Brut | Frais flash | Gaz (dont L1) | Net attendu (€) | Marge (bps) |
|---:|---|---:|---:|---:|---:|---:|---:|
| 52620701 | WETH→[pancakeswap_v3]→USDC→[aerodrome]→WETH | 0.002485 WETH | 0.000002 WETH | 0.000000 WETH | 0.000002 WETH | -0.0006 | -1.04 |
| 52620701 | USDC→[aerodrome]→WETH→[pancakeswap_v3]→USDC | 6.041696 USDC | 0.004494 USDC | 0.000000 USDC | 0.005121 USDC | -0.0006 | -1.04 |
| 52620701 | WETH→[aerodrome_slipstream]→USDC→[aerodrome]→WETH | 0.002433 WETH | 0.000002 WETH | 0.000000 WETH | 0.000002 WETH | -0.0006 | -1.17 |
| 52620701 | USDC→[aerodrome]→WETH→[aerodrome_slipstream]→USDC | 5.799950 USDC | 0.004430 USDC | 0.000000 USDC | 0.005121 USDC | -0.0006 | -1.19 |
| 52620687 | USDC→[pancakeswap_v3]→PLAY→[aerodrome_slipstream]→USDC | 14.771901 USDC | 0.004594 USDC | 0.000000 USDC | 0.005426 USDC | -0.0008 | -0.56 |
| 52620701 | WETH→[uniswap_v3]→USDC→[aerodrome]→WETH | 0.002433 WETH | 0.000002 WETH | 0.000000 WETH | 0.000002 WETH | -0.0008 | -1.57 |
| 52620701 | USDC→[aerodrome]→WETH→[uniswap_v3]→USDC | 5.799950 USDC | 0.004196 USDC | 0.000000 USDC | 0.005121 USDC | -0.0009 | -1.59 |
| 52620687 | WETH→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.027999 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | -0.0009 | -0.15 |
| 52620687 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→USDC | 67.074546 USDC | 0.006247 USDC | 0.000000 USDC | 0.007261 USDC | -0.0009 | -0.15 |
| 52620688 | WETH→[aerodrome]→USDC→[pancakeswap_v3]→WETH | 0.001674 WETH | 0.000001 WETH | 0.000000 WETH | 0.000002 WETH | -0.0028 | -7.66 |

## Fiabilité et décision
- Observations ghost : 219 ; taux observé 0.151 ; borne inférieure crédible (0.9) 0.122 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 12.2% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
