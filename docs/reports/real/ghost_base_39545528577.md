# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-21T04:51:53+00:00 ; durée 3.05 min ; blocs 52884388 → 52884482 (83 vus)

## Connexion
- Requêtes RPC : 1159 ; erreurs : 0 ; latence p50/p95 : 374.9/1,901.4 ms
- Rafraîchissements d'état : 83 ; âge des données au dernier bloc : 2.82 s ; changements de frais LP observés (pools à frais dynamiques) : 160
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 496 ; cycles déclenchés par événement : 36 ; avance médiane sur le rafraîchissement multicall : 1,078 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,447.38 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 580 pools, 328 jetons, 21464 routes
- Par DEX : uniswap_v3 137, aerodrome 236, aerodrome_slipstream 158, pancakeswap_v3 31, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 208 (rejetés 2) → 613 jetons ; pools candidats 3925 (énumérés 396, par paires 0), mesurés 582, sous le plancher de 10000.0 $ : 2 → gardés 580 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2447.377823, 'AERO': 0.859444, 'cbBTC': 82692.945421}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 148,484,377 | 2,447.377822 | 52884483 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 38,795,170 | 1.163543 | 52884483 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 18,544,240 | 0.029563 | 52884483 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/VVV | 3000 | 18,097,036 | 94.080632 | 52884483 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,481,603 | 0.029524 | 52884483 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,548,032 | 0.029573 | 52884483 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,927,650 | 0.000012 | 52884483 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome_slipstream | USDC/cbBTC | 412 | 8,828,095 | 0.000012 | 52884483 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | WETH/USDC | 500 | 8,612,265 | 2,441.175655 | 52884483 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/USDC | 3000 | 8,377,571 | 2,447.374031 | 52884483 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | WETH/USDC | 535 | 8,225,230 | 2,441.572011 | 52884483 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | USDC/cbBTC | 332 | 8,193,226 | 0.000012 | 52884483 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,267,823 | 0.001669 | 52884483 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,542,583 | 0.029524 | 52884483 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | fBOMB/AERO | 10000 | 5,275,051 | 0.024753 | 52884483 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome_slipstream | WETH/USDT | 403 | 5,096,612 | 2,444.052133 | 52884483 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,717,452 | 0.802394 | 52884483 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,699,914 | 0.000277 | 52884483 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,455,517 | 2,441.456630 | 52884483 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | USDC/AERO | 10000 | 4,414,146 | 1.156821 | 52884483 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,394,163 | 0.998741 | 52884483 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 4,044,578 | 34,727.971498 | 52884483 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/AERO | 10000 | 3,373,747 | 2,828.534288 | 52884483 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,811,030 | 397.014374 | 52884483 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | WETH/VVV | 2745 | 2,766,358 | 94.103400 | 52884483 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 2,577,822 | 1,065.858058 | 52884483 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,535,337 | 1.142084 | 52884483 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,274,081 | 0.000012 | 52884483 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | AERO/cbBTC | 2700 | 2,252,367 | 0.000010 | 52884483 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | WETH/FAI | 10000 | 2,241,236 | 1,210,470.665103 | 52884483 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 2,074,194 | 0.000012 | 52884483 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,058,907 | 1.238864 | 52884483 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,028,014 | 1.383164 | 52884483 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,948,267 | 0.000000 | 52884483 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,925,612 | 15.719841 | 52884483 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | weETH_04c0/WETH | 500 | 1,915,722 | 1.105697 | 52884483 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| uniswap_v3 | XDP/USDC | 100 | 1,816,451 | 0.019352 | 52884483 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,770,761 | 13,434.805211 | 52884483 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | fBOMB/USDC | 10000 | 1,715,704 | 0.021479 | 52884483 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| aerodrome | WETH/msETH (stable) | 500 | 1,689,053 | 2.311287 | 52884483 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | WETH/AERO | 3000 | 1,684,602 | 2,844.559130 | 52884483 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,569,318 | 0.916062 | 52884483 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,456,348 | 0.826534 | 52884483 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | EURC/USDC | 70 | 1,424,089 | 1.122729 | 52884483 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,352,813 | 0.004809 | 52884483 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,328,058 | 0.000278 | 52884483 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| uniswap_v3 | DRB/WETH | 10000 | 1,327,706 | 0.000000 | 52884483 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | WETH/cbBTC | 3000 | 1,309,704 | 0.029583 | 52884483 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| aerodrome_slipstream | WETH/VVV | 8000 | 1,282,509 | 94.197531 | 52884483 | `0x46D398A5b33709877f50c8918A7eE96F1Be1d7dd` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,260,523 | 2,441.211600 | 52884483 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,235,876 | 63.619861 | 52884483 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,222,413 | 34,988,111.001513 | 52884483 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,220,925 | 23.087745 | 52884483 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| aerodrome | WETH/EDEL | 7000 | 1,211,804 | 69,535.249779 | 52884483 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | WETH/WELL | 10000 | 1,195,116 | 1,136,960.383950 | 52884483 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,181,280 | 0.436726 | 52884483 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,178,940 | 484,627.530132 | 52884483 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome_slipstream | msUSD/USDC | 500 | 1,159,219 | 0.886245 | 52884483 | `0x7501bc8Bb51616F79bfA524E464fb7B41f0B10fB` |
| aerodrome | USDC/NOCK | 3000 | 1,157,833 | 47.001665 | 52884483 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,153,464 | 1.106158 | 52884483 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |

## Recherche d'opportunités
- Cycles : 118 ; routes examinées : 2532752 ; candidats optimisés : 18452 ; net attendu > 0 : 0 ; dernier cycle 644.1 ms
- Rejets (moteur) : {'spread_below_threshold': 2499966, 'negative_expected_net': 18452, 'liquidity_below_min': 14216, 'borrow_bound_too_small': 118}
- Enregistrements de la session : 18452 ; net attendu > 0 : 0 ; simulés (eth_call de la vraie tx) : 0 (ok 0, échec 0) ; étiquettes ghost N+1 : 0/0 positives
- Décisions : {'REJECTED': 18452} ; motifs de rejet : {'negative_expected_net': 18452}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|

_Aucun candidat à net positif. Les 10 plus proches de la rentabilité (net attendu négatif) :_

| Bloc | Route | Montant | Brut | Frais flash | Gaz (dont L1) | Net attendu (€) | Marge (bps) |
|---:|---|---:|---:|---:|---:|---:|---:|
| 52884478 | USDC→[aerodrome_slipstream]→CARV→[aerodrome_slipstream]→USDC | 10.433852 USDC | 0.001797 USDC | 0.000000 USDC | 0.005494 USDC | -0.0034 | -3.54 |
| 52884479 | USDC→[aerodrome_slipstream]→CARV→[aerodrome_slipstream]→USDC | 10.433852 USDC | 0.001797 USDC | 0.000000 USDC | 0.005494 USDC | -0.0034 | -3.54 |
| 52884480 | USDC→[aerodrome_slipstream]→CARV→[aerodrome_slipstream]→USDC | 10.433852 USDC | 0.001797 USDC | 0.000000 USDC | 0.005494 USDC | -0.0034 | -3.54 |
| 52884482 | USDC→[aerodrome_slipstream]→CARV→[aerodrome_slipstream]→USDC | 10.433852 USDC | 0.001797 USDC | 0.000000 USDC | 0.005494 USDC | -0.0034 | -3.54 |
| 52884471 | USDC→[aerodrome_slipstream]→CARV→[aerodrome_slipstream]→USDC | 10.433852 USDC | 0.001797 USDC | 0.000000 USDC | 0.005495 USDC | -0.0034 | -3.54 |
| 52884472 | USDC→[aerodrome_slipstream]→CARV→[aerodrome_slipstream]→USDC | 10.433852 USDC | 0.001797 USDC | 0.000000 USDC | 0.005495 USDC | -0.0034 | -3.54 |
| 52884473 | USDC→[aerodrome_slipstream]→CARV→[aerodrome_slipstream]→USDC | 10.433852 USDC | 0.001797 USDC | 0.000000 USDC | 0.005495 USDC | -0.0034 | -3.54 |
| 52884474 | USDC→[aerodrome_slipstream]→CARV→[aerodrome_slipstream]→USDC | 10.433852 USDC | 0.001797 USDC | 0.000000 USDC | 0.005495 USDC | -0.0034 | -3.54 |
| 52884475 | USDC→[aerodrome_slipstream]→CARV→[aerodrome_slipstream]→USDC | 10.433852 USDC | 0.001797 USDC | 0.000000 USDC | 0.005495 USDC | -0.0034 | -3.54 |
| 52884476 | USDC→[aerodrome_slipstream]→CARV→[aerodrome_slipstream]→USDC | 10.433852 USDC | 0.001797 USDC | 0.000000 USDC | 0.005495 USDC | -0.0034 | -3.54 |

## Fiabilité et décision
- Observations ghost : 1593 ; taux observé 0.102 ; borne inférieure crédible (0.9) 0.093 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 9.3% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
