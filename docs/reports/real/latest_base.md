# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-20T12:42:20+00:00 ; durée 46.16 min ; blocs 52854009 → 52855395 (1384 vus)

## Connexion
- Requêtes RPC : 18839 ; erreurs : 0 ; latence p50/p95 : 302.3/866.0 ms
- Rafraîchissements d'état : 1385 ; âge des données au dernier bloc : 2.0 s ; changements de frais LP observés (pools à frais dynamiques) : 2758
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 25830 ; cycles déclenchés par événement : 1242 ; avance médiane sur le rafraîchissement multicall : 809 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,388.13 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 573 pools, 327 jetons, 21172 routes
- Par DEX : uniswap_v3 135, aerodrome 235, aerodrome_slipstream 156, pancakeswap_v3 30, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 207 (rejetés 2) → 612 jetons ; pools candidats 3877 (énumérés 393, par paires 0), mesurés 575, sous le plancher de 10000.0 $ : 2 → gardés 573 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDbC': 1.0, 'USDC': 1.0, 'WETH': 2381.795213, 'AERO': 0.801082, 'cbBTC': 81409.268719}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 146,087,188 | 2,388.128337 | 52855395 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 34,286,345 | 1.251107 | 52855395 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| aerodrome | WETH/VVV | 3000 | 17,311,732 | 98.472609 | 52855395 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,020,708 | 0.029350 | 52855395 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 11,170,223 | 0.029296 | 52855395 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,310,233 | 0.029310 | 52855395 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,868,618 | 0.000012 | 52855395 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome_slipstream | USDC/cbBTC | 460 | 9,651,660 | 0.000012 | 52855395 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | WETH/USDC | 500 | 8,305,437 | 2,391.646486 | 52855395 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/USDC | 3000 | 8,280,993 | 2,388.522762 | 52855395 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | USDC/cbBTC | 340 | 8,109,311 | 0.000012 | 52855395 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 150 | 7,365,619 | 2,392.282687 | 52855395 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,149,191 | 0.001672 | 52855395 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,351,054 | 0.029357 | 52855395 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | fBOMB/AERO | 10000 | 4,939,178 | 0.025412 | 52855395 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,757,858 | 0.802395 | 52855395 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome_slipstream | USDC/AERO | 10000 | 4,697,604 | 1.242540 | 52855395 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,606,517 | 0.000275 | 52855395 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/USDT | 418 | 4,507,722 | 2,395.082823 | 52855395 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,347,423 | 2,392.513145 | 52855395 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,312,190 | 0.998767 | 52855395 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,977,301 | 34,194.963509 | 52855395 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/AERO | 10000 | 3,214,905 | 2,963.554374 | 52855395 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,865,512 | 0.000012 | 52855395 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,732,281 | 1.142102 | 52855395 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| aerodrome_slipstream | WETH/VVV | 2715 | 2,644,198 | 98.490821 | 52855395 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,636,180 | 401.137952 | 52855395 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 2,621,310 | 984.833565 | 52855395 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 2,246,870 | 0.000010 | 52855395 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | WETH/FAI | 10000 | 2,179,134 | 1,219,199.413671 | 52855395 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,059,548 | 1.237984 | 52855395 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,036,015 | 1.373598 | 52855395 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,930,707 | 0.000000 | 52855395 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,857,592 | 16.030712 | 52855395 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,833,297 | 13,669.240409 | 52855395 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | XDP/USDC | 100 | 1,800,471 | 0.019100 | 52855395 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,756,344 | 0.000012 | 52855395 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | weETH_04c0/WETH | 500 | 1,727,910 | 1.105526 | 52855395 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome | fBOMB/USDC | 10000 | 1,678,628 | 0.020328 | 52855395 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| aerodrome | WETH/msETH (stable) | 500 | 1,649,026 | 2.305850 | 52855395 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | WETH/AERO | 3000 | 1,611,789 | 2,986.379766 | 52855395 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,546,832 | 0.916341 | 52855395 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,458,064 | 0.826189 | 52855395 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | EURC/USDC | 79 | 1,407,793 | 1.122657 | 52855395 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,304,178 | 0.000000 | 52855395 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,300,032 | 0.004722 | 52855395 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,291,560 | 0.000275 | 52855395 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | WETH/cbBTC | 3000 | 1,282,633 | 0.029315 | 52855395 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,238,847 | 2,391.713779 | 52855395 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,236,136 | 63.593116 | 52855395 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,209,003 | 23.000823 | 52855395 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| uniswap_v3 | WETH/doginme | 10000 | 1,189,374 | 35,339,904.339864 | 52855395 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,178,385 | 0.435540 | 52855395 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| aerodrome | WETH/WELL | 10000 | 1,161,783 | 1,145,645.806053 | 52855395 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome_slipstream | WETH/VVV | 8000 | 1,153,326 | 98.341899 | 52855395 | `0x46D398A5b33709877f50c8918A7eE96F1Be1d7dd` |
| aerodrome_slipstream | WETH/msETH | 500 | 1,150,958 | 1.131429 | 52855395 | `0x74F72788F4814D7fF3C49B44684aa98Eee140C0E` |
| aerodrome | WETH/EDEL | 7000 | 1,146,688 | 74,838.198816 | 52855395 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,128,448 | 509,988.290162 | 52855395 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | USDC/NOCK | 3000 | 1,115,352 | 50.649876 | 52855395 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | msUSD/USDC | 500 | 1,087,398 | 0.885352 | 52855395 | `0x7501bc8Bb51616F79bfA524E464fb7B41f0B10fB` |

## Recherche d'opportunités
- Cycles : 2626 ; routes examinées : 55597672 ; candidats optimisés : 339353 ; net attendu > 0 : 8 ; dernier cycle 230.8 ms
- Rejets (moteur) : {'spread_below_threshold': 54814934, 'liquidity_below_min': 377369, 'negative_expected_net': 339345, 'borrow_bound_too_small': 65600, 'cycle_budget_exhausted': 416}
- Enregistrements de la session : 339353 ; net attendu > 0 : 8 ; simulés (eth_call de la vraie tx) : 0 (ok 0, échec 0) ; étiquettes ghost N+1 : 0/0 positives
- Décisions : {'REJECTED': 339353} ; motifs de rejet : {'below_safety_margin': 8, 'negative_expected_net': 339345, 'p_lower_below_threshold': 8}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52854077 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→WETH | 0.015454 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0033 €) | — | 0.99 | 0.280 (n=78) | REJECTED | below_safety_margin(1522795865194<3090857581313), p_lower_below_threshold(0.28<0.75) |
| 52854077 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→WETH | 0.015454 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0033 €) | — | 0.99 | 0.280 (n=78) | REJECTED | below_safety_margin(1522795865194<3090857581313), p_lower_below_threshold(0.28<0.75) |
| 52854077 | USDC→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 36.544967 USDC | 0.010784 USDC | 0.000000 USDC | 0.007161 USDC | 0.003623 USDC (0.0033 €) | — | 0.99 | 0.280 (n=78) | REJECTED | below_safety_margin(3623<7308), p_lower_below_threshold(0.28<0.75) |
| 52854077 | USDC→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 36.544967 USDC | 0.010784 USDC | 0.000000 USDC | 0.007161 USDC | 0.003623 USDC (0.0033 €) | — | 0.99 | 0.280 (n=78) | REJECTED | below_safety_margin(3623<7308), p_lower_below_threshold(0.28<0.75) |
| 52854077 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→WETH | 0.014984 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0023 €) | — | 0.71 | 0.105 (n=170) | REJECTED | below_safety_margin(1064903925536<2996813387719), p_lower_below_threshold(0.10<0.75) |
| 52854077 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→WETH | 0.014984 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0023 €) | — | 0.71 | 0.105 (n=170) | REJECTED | below_safety_margin(1064903925536<2996813387719), p_lower_below_threshold(0.10<0.75) |
| 52854077 | USDC→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 35.538538 USDC | 0.009695 USDC | 0.000000 USDC | 0.007161 USDC | 0.002534 USDC (0.0023 €) | — | 0.71 | 0.105 (n=170) | REJECTED | below_safety_margin(2534<7107), p_lower_below_threshold(0.10<0.75) |
| 52854077 | USDC→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 35.538538 USDC | 0.009695 USDC | 0.000000 USDC | 0.007161 USDC | 0.002534 USDC (0.0023 €) | — | 0.71 | 0.105 (n=170) | REJECTED | below_safety_margin(2534<7107), p_lower_below_threshold(0.10<0.75) |

## Fiabilité et décision
- Observations ghost : 1413 ; taux observé 0.100 ; borne inférieure crédible (0.9) 0.090 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 9.0% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
