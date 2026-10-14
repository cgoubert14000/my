# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-14T20:42:24+00:00 ; durée 3.04 min ; blocs 52610504 → 52610598 (90 vus)

## Connexion
- Requêtes RPC : 1092 ; erreurs : 0 ; latence p50/p95 : 85.6/1,908.9 ms
- Rafraîchissements d'état : 91 ; âge des données au dernier bloc : 0.98 s ; changements de frais LP observés (pools à frais dynamiques) : 168
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 1 ; cycles déclenchés par événement : 1 ; avance médiane sur le rafraîchissement multicall : — ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,422.37 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 580 pools, 327 jetons, 21784 routes
- Par DEX : uniswap_v3 139, aerodrome 235, aerodrome_slipstream 156, pancakeswap_v3 33, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 207 (rejetés 2) → 612 jetons ; pools candidats 3920 (énumérés 394, par paires 0), mesurés 583, sous le plancher de 10000.0 $ : 3 → gardés 580 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDC': 1.0, 'USDbC': 1.0, 'WETH': 2422.373052, 'AERO': 0.888199, 'cbBTC': 81793.071591}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 147,173,319 | 2,422.373747 | 52610598 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 45,059,171 | 1.126739 | 52610598 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 500 | 17,818,306 | 0.029597 | 52610598 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 16,908,112 | 0.029641 | 52610598 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/VVV | 3000 | 16,120,706 | 103.822801 | 52610598 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,457,628 | 0.029652 | 52610598 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,220,168 | 0.000012 | 52610598 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 9,173,016 | 2,418.303693 | 52610598 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/USDC | 3000 | 8,954,186 | 2,422.243876 | 52610598 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | USDC/cbBTC | 344 | 8,164,129 | 0.000012 | 52610598 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 698 | 7,842,711 | 2,419.094016 | 52610598 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,162,157 | 0.001658 | 52610598 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 484 | 6,640,054 | 0.000012 | 52610598 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome_slipstream | USDC/AERO | 10000 | 5,741,987 | 1.131133 | 52610598 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,429,834 | 0.029608 | 52610598 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/superOETHb | 400 | 5,350,279 | 1.000855 | 52610598 | `0x6446021F4E396dA3df4235C62537431372195D38` |
| aerodrome | fBOMB/AERO | 10000 | 5,331,830 | 0.026725 | 52610598 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,609,427 | 0.000279 | 52610598 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,555,884 | 0.802388 | 52610598 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,399,406 | 2,419.279913 | 52610598 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,118,046 | 1.000134 | 52610598 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,997,114 | 34,834.329592 | 52610598 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/AERO | 10000 | 3,629,319 | 2,747.800693 | 52610598 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,842,937 | 0.000012 | 52610598 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,657,969 | 405.417161 | 52610598 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | WETH/VVV | 2712 | 2,606,051 | 103.842260 | 52610598 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,578,620 | 1.141641 | 52610598 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| aerodrome_slipstream | AERO/cbBTC | 2700 | 2,491,348 | 0.000011 | 52610598 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/USDT | 451 | 2,363,202 | 2,422.100745 | 52610598 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome | WETH/FAI | 10000 | 2,361,391 | 1,068,249.817303 | 52610598 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | WETH/MORPHO | 2703 | 2,176,727 | 1,028.347589 | 52610598 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,113,871 | 1.193301 | 52610598 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | BNKR/WETH | 10000 | 2,066,699 | 0.000000 | 52610598 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome | fBOMB/USDbC | 10000 | 1,965,008 | 0.023388 | 52610598 | `0xC395664B295ed5bf1D249Ae8be9740655AA174ef` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,897,555 | 0.916707 | 52610598 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,847,909 | 15.710884 | 52610598 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | USDC/alUSDb (stable) | 500 | 1,836,402 | 1.402356 | 52610598 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| uniswap_v3 | XDP/USDC | 100 | 1,794,079 | 0.019179 | 52610598 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,776,810 | 0.000012 | 52610598 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,657,958 | 13,677.729203 | 52610598 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/msETH (stable) | 500 | 1,624,957 | 2.305032 | 52610598 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | WETH/AERO | 3000 | 1,525,376 | 2,724.245438 | 52610598 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | weETH_04c0/WETH | 500 | 1,497,675 | 1.105776 | 52610598 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,459,484 | 0.835124 | 52610598 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | DRB/WETH | 10000 | 1,376,540 | 0.000000 | 52610598 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,363,797 | 0.004892 | 52610598 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | WETH/AERO | 3000 | 1,360,837 | 2,728.607669 | 52610598 | `0x82321f3BEB69f503380D6B233857d5C43562e2D0` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,318,395 | 0.000280 | 52610598 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome_slipstream | EURC/USDC | 70 | 1,313,595 | 1.115378 | 52610598 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| aerodrome_slipstream | WETH/msETH | 500 | 1,279,173 | 1.131212 | 52610598 | `0x74F72788F4814D7fF3C49B44684aa98Eee140C0E` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,276,678 | 23.355018 | 52610598 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| aerodrome | USDC/SEND | 3000 | 1,247,000 | 62.489886 | 52610598 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,246,236 | 2,418.324587 | 52610598 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | WETH/doginme | 10000 | 1,227,856 | 33,313,445.430498 | 52610598 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,208,253 | 1.105594 | 52610598 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |
| aerodrome | WETH/EDEL | 7000 | 1,181,335 | 72,743.746406 | 52610598 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,162,769 | 488,691.317475 | 52610598 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | WETH/WELL | 10000 | 1,154,420 | 1,193,984.411649 | 52610598 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome | USDC/NOCK | 3000 | 1,145,428 | 48.034543 | 52610598 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,139,861 | 13.459571 | 52610598 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |

## Recherche d'opportunités
- Cycles : 91 ; routes examinées : 1982344 ; candidats optimisés : 11508 ; net attendu > 0 : 0 ; dernier cycle 384.4 ms
- Rejets (moteur) : {'spread_below_threshold': 1948298, 'liquidity_below_min': 20081, 'negative_expected_net': 11508, 'borrow_bound_too_small': 2275, 'unquotable': 182}
- Enregistrements de la session : 11508 ; net attendu > 0 : 0 ; simulés (eth_call de la vraie tx) : 0 (ok 0, échec 0) ; étiquettes ghost N+1 : 0/0 positives
- Décisions : {'REJECTED': 11508} ; motifs de rejet : {'negative_expected_net': 11508}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|

_Aucun candidat à net positif. Les 10 plus proches de la rentabilité (net attendu négatif) :_

| Bloc | Route | Montant | Brut | Frais flash | Gaz (dont L1) | Net attendu (€) | Marge (bps) |
|---:|---|---:|---:|---:|---:|---:|---:|
| 52610539 | WETH→[pancakeswap_v3]→AUKI→[aerodrome]→USDC→[pancakeswap_v3]→WETH | 0.003969 WETH | 0.000002 WETH | 0.000000 WETH | 0.000003 WETH | -0.0024 | -2.75 |
| 52610539 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→AUKI→[aerodrome]→USDC | 9.534016 USDC | 0.004328 USDC | 0.000000 USDC | 0.006973 USDC | -0.0024 | -2.77 |
| 52610561 | WETH→[pancakeswap_v3]→AUKI→[aerodrome]→USDC→[pancakeswap_v3]→WETH | 0.003758 WETH | 0.000002 WETH | 0.000000 WETH | 0.000003 WETH | -0.0028 | -3.39 |
| 52610562 | WETH→[pancakeswap_v3]→AUKI→[aerodrome]→USDC→[pancakeswap_v3]→WETH | 0.003758 WETH | 0.000002 WETH | 0.000000 WETH | 0.000003 WETH | -0.0028 | -3.39 |
| 52610561 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→AUKI→[aerodrome]→USDC | 9.098818 USDC | 0.003877 USDC | 0.000000 USDC | 0.006972 USDC | -0.0028 | -3.40 |
| 52610562 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→AUKI→[aerodrome]→USDC | 9.098818 USDC | 0.003877 USDC | 0.000000 USDC | 0.006972 USDC | -0.0028 | -3.40 |
| 52610561 | WETH→[pancakeswap_v3]→AUKI→[aerodrome]→USDC→[uniswap_v3]→WETH | 0.003646 WETH | 0.000002 WETH | 0.000000 WETH | 0.000003 WETH | -0.0030 | -3.74 |
| 52610562 | WETH→[pancakeswap_v3]→AUKI→[aerodrome]→USDC→[uniswap_v3]→WETH | 0.003646 WETH | 0.000002 WETH | 0.000000 WETH | 0.000003 WETH | -0.0030 | -3.74 |
| 52610561 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→AUKI→[aerodrome]→USDC | 8.823648 USDC | 0.003665 USDC | 0.000000 USDC | 0.006972 USDC | -0.0030 | -3.75 |
| 52610562 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→AUKI→[aerodrome]→USDC | 8.823648 USDC | 0.003665 USDC | 0.000000 USDC | 0.006972 USDC | -0.0030 | -3.75 |

## Fiabilité et décision
- Observations ghost : 181 ; taux observé 0.160 ; borne inférieure crédible (0.9) 0.128 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 12.8% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
