# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-22T09:06:07+00:00 ; durée 12.19 min ; blocs 52934940 → 52935309 (349 vus)

## Connexion
- Requêtes RPC : 4244 ; erreurs : 0 ; latence p50/p95 : 237.0/1,759.6 ms
- Rafraîchissements d'état : 349 ; âge des données au dernier bloc : 2.25 s ; changements de frais LP observés (pools à frais dynamiques) : 708
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 2176 ; cycles déclenchés par événement : 171 ; avance médiane sur le rafraîchissement multicall : 1,143 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,407.58 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 552 pools, 321 jetons, 20574 routes
- Par DEX : uniswap_v3 136, aerodrome 228, aerodrome_slipstream 141, pancakeswap_v3 31, uniswap_v2 13, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 201 (rejetés 2) → 606 jetons ; pools candidats 3839 (énumérés 370, par paires 0), mesurés 554, sous le plancher de 10000.0 $ : 2 → gardés 552 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'DAI': 1.0, 'USDC': 1.0, 'WETH': 2409.153844, 'AERO': 0.798022, 'cbBTC': 81873.188532}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 155,411,238 | 2,407.579369 | 52935309 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 23,268,465 | 1.255315 | 52935309 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,269,386 | 0.029392 | 52935309 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 16,262,786 | 87.015375 | 52935309 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,272,226 | 0.029447 | 52935309 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 9,590,903 | 0.029430 | 52935309 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,417,108 | 0.000012 | 52935309 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 8,651,940 | 2,401.538669 | 52935309 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/USDC | 3000 | 7,334,684 | 2,407.697270 | 52935309 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,163,603 | 0.001656 | 52935309 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 338 | 7,050,273 | 0.000012 | 52935309 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 713 | 6,080,582 | 2,401.440331 | 52935309 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | USDC/cbBTC | 448 | 5,681,327 | 0.000012 | 52935309 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,424,147 | 0.029401 | 52935309 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,580,273 | 2,402.233630 | 52935309 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,307,218 | 1.000001 | 52935309 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,996,485 | 34,410.050302 | 52935309 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | VIRTUAL/WETH | 10000 | 3,946,665 | 0.000275 | 52935309 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/USDT | 439 | 2,872,006 | 2,405.503290 | 52935309 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome_slipstream | WETH/VVV | 2850 | 2,632,528 | 87.031883 | 52935309 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | WETH/AERO | 10000 | 2,372,492 | 3,001.164909 | 52935309 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,309,619 | 397.930562 | 52935309 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,225,706 | 0.000012 | 52935309 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | WETH/FAI | 10000 | 2,212,577 | 1,201,213.060660 | 52935309 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 2,061,989 | 0.000012 | 52935309 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,905,773 | 0.000000 | 52935309 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,797,595 | 0.018568 | 52935309 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,662,906 | 1.531778 | 52935309 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | WETH/AERO | 3000 | 1,625,889 | 3,022.222153 | 52935309 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,455,691 | 0.821840 | 52935309 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,416,748 | 13,527.819953 | 52935309 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,359,438 | 0.004897 | 52935309 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome | WETH/msETH (stable) | 500 | 1,332,239 | 2.339661 | 52935309 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | DRB/WETH | 10000 | 1,306,348 | 0.000000 | 52935309 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,302,514 | 0.000273 | 52935309 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | USDC/alUSDb (stable) | 500 | 1,296,866 | 1.399491 | 52935309 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,277,536 | 2,401.485680 | 52935309 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,230,629 | 64.163528 | 52935309 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 1,228,816 | 0.000010 | 52935309 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v3 | WETH/doginme | 10000 | 1,196,807 | 35,491,476.186037 | 52935309 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,190,896 | 16.299391 | 52935309 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | WETH/WELL | 10000 | 1,190,696 | 1,086,059.546510 | 52935309 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome | USDC/NOCK | 3000 | 1,158,499 | 46.944096 | 52935309 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome | fBOMB/AERO | 10000 | 1,155,226 | 0.023215 | 52935309 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,150,637 | 503,008.258857 | 52935309 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | WETH/EDEL | 7000 | 1,136,261 | 71,233.329745 | 52935309 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | fBOMB/USDC | 10000 | 1,102,523 | 0.018835 | 52935309 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| aerodrome | weETH_04c0/WETH | 500 | 1,099,961 | 1.105754 | 52935309 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome_slipstream | EURC/USDC | 73 | 1,066,172 | 1.123737 | 52935309 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,064,329 | 21,447,301.659841 | 52935309 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,040,992 | 16.987922 | 52935309 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | WETH/cbBTC | 3000 | 1,022,241 | 0.029441 | 52935309 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,015,064 | 23.236269 | 52935309 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| uniswap_v3 | USDC/VVV | 3000 | 1,005,301 | 0.036236 | 52935309 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome_slipstream | WETH/wstETH | 90 | 967,271 | 0.802250 | 52935309 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| uniswap_v3 | WETH/MORPHO | 3000 | 953,398 | 1,066.278935 | 52935309 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/USDC | 10000 | 932,881 | 2,424.701285 | 52935309 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | uXRP/WETH | 3000 | 920,393 | 0.000551 | 52935309 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome | WETH/bsdETH | 100 | 896,781 | 0.916123 | 52935309 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 886,953 | 17.659460 | 52935309 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |

## Recherche d'opportunités
- Cycles : 519 ; routes examinées : 10677906 ; candidats optimisés : 80766 ; net attendu > 0 : 13 ; dernier cycle 874.1 ms
- Rejets (moteur) : {'spread_below_threshold': 10486254, 'liquidity_below_min': 110182, 'negative_expected_net': 80753, 'borrow_bound_too_small': 519, 'cycle_budget_exhausted': 185}
- Enregistrements de la session : 80766 ; net attendu > 0 : 13 ; simulés (eth_call de la vraie tx) : 0 (ok 0, échec 0) ; étiquettes ghost N+1 : 0/0 positives
- Décisions : {'REJECTED': 80766} ; motifs de rejet : {'below_safety_margin': 13, 'negative_expected_net': 80753, 'p_lower_below_threshold': 11, 'reliability_not_demonstrated': 2}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52935239 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.442022 WETH | 0.000026 WETH | 0.000000 WETH | 0.000002 WETH | 0.000023 WETH (0.0512 €) | — | 0.52 | 0.023 (n=63) | REJECTED | below_safety_margin(23119777902019<88404477608296), p_lower_below_threshold(0.02<0.75) |
| 52935239 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 1,060.890223 USDC | 0.061330 USDC | 0.000000 USDC | 0.005790 USDC | 0.055540 USDC (0.0511 €) | — | 0.52 | 0.023 (n=63) | REJECTED | below_safety_margin(55540<212178), p_lower_below_threshold(0.02<0.75) |
| 52935079 | cbBTC→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.001045 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0053 €) | — | 0.67 | 0.108 (n=213) | REJECTED | below_safety_margin(7<20), p_lower_below_threshold(0.11<0.75) |
| 52935079 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 81.878112 USDC | 0.012340 USDC | 0.000000 USDC | 0.007269 USDC | 0.005071 USDC (0.0047 €) | — | 0.62 | 0.108 (n=213) | REJECTED | below_safety_margin(5071<16375), p_lower_below_threshold(0.11<0.75) |
| 52935079 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→WETH | 0.046172 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0046 €) | — | 0.45 | 0.108 (n=213) | REJECTED | below_safety_margin(2076199974824<9234386745215), p_lower_below_threshold(0.11<0.75) |
| 52935079 | cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.001750 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0008 €) | — | 0.06 | 0.108 (n=213) | REJECTED | below_safety_margin(1<34), p_lower_below_threshold(0.11<0.75) |
| 52935079 | cbBTC→[uniswap_v3]→WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.001750 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0008 €) | — | 0.06 | 0.108 (n=213) | REJECTED | below_safety_margin(1<34), p_lower_below_threshold(0.11<0.75) |
| 52935239 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.084617 WETH | 0.000002 WETH | 0.000000 WETH | 0.000002 WETH | 0.000000 WETH (0.0005 €) | — | 0.03 | 0.003 (n=2) | REJECTED | below_safety_margin(235520924276<16923359283337), reliability_not_demonstrated |
| 52935239 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 201.034589 USDC | 0.005975 USDC | 0.000000 USDC | 0.005424 USDC | 0.000551 USDC (0.0005 €) | — | 0.03 | 0.003 (n=2) | REJECTED | below_safety_margin(551<40206), reliability_not_demonstrated |
| 52935079 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 179.537184 USDC | 0.007786 USDC | 0.000000 USDC | 0.007269 USDC | 0.000517 USDC (0.0005 €) | — | 0.03 | 0.108 (n=213) | REJECTED | below_safety_margin(517<35907), p_lower_below_threshold(0.11<0.75) |
| 52935079 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH | 0.069115 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0004 €) | — | 0.03 | 0.108 (n=213) | REJECTED | below_safety_margin(179469588008<13822967470557), p_lower_below_threshold(0.11<0.75) |
| 52935079 | USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 194.672824 USDC | 0.007488 USDC | 0.000000 USDC | 0.007269 USDC | 0.000219 USDC (0.0002 €) | — | 0.01 | 0.108 (n=213) | REJECTED | below_safety_margin(219<38934), p_lower_below_threshold(0.11<0.75) |
| 52935079 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.059480 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0002 €) | — | 0.02 | 0.108 (n=213) | REJECTED | below_safety_margin(90770456815<11895914901431), p_lower_below_threshold(0.11<0.75) |

## Fiabilité et décision
- Observations ghost : 1844 ; taux observé 0.095 ; borne inférieure crédible (0.9) 0.087 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 8.7% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
