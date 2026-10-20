# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-20T00:42:53+00:00 ; durée 12.22 min ; blocs 52833443 → 52833812 (360 vus)

## Connexion
- Requêtes RPC : 5046 ; erreurs : 43 ; latence p50/p95 : 269.1/1,343.2 ms
- Rafraîchissements d'état : 361 ; âge des données au dernier bloc : 1.77 s ; changements de frais LP observés (pools à frais dynamiques) : 730
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 6463 ; cycles déclenchés par événement : 347 ; avance médiane sur le rafraîchissement multicall : 581 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,396.87 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 572 pools, 327 jetons, 21078 routes
- Par DEX : uniswap_v3 136, aerodrome 234, aerodrome_slipstream 155, pancakeswap_v3 30, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 207 (rejetés 2) → 612 jetons ; pools candidats 3877 (énumérés 391, par paires 0), mesurés 575, sous le plancher de 10000.0 $ : 3 → gardés 572 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDC': 1.0, 'USDbC': 1.0, 'WETH': 2396.875305, 'AERO': 0.785623, 'cbBTC': 81488.469771}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 146,070,399 | 2,396.874886 | 52833812 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 34,148,323 | 1.264311 | 52833812 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 18,938,692 | 0.029333 | 52833812 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 500 | 18,190,634 | 0.029385 | 52833812 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 17,299,944 | 99.216827 | 52833812 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,339,478 | 0.029315 | 52833812 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,866,560 | 0.000012 | 52833812 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 8,339,253 | 2,397.819585 | 52833812 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/USDC | 3000 | 8,300,886 | 2,397.092247 | 52833812 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | USDC/cbBTC | 332 | 7,815,662 | 0.000012 | 52833812 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 549 | 7,448,780 | 2,398.068539 | 52833812 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,174,620 | 0.001675 | 52833812 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 412 | 6,661,720 | 0.000012 | 52833812 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,331,742 | 0.029381 | 52833812 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | fBOMB/AERO | 10000 | 4,913,008 | 0.025626 | 52833812 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,775,281 | 0.802395 | 52833812 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome_slipstream | WETH/USDT | 403 | 4,742,089 | 2,401.122005 | 52833812 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome_slipstream | USDC/AERO | 10000 | 4,705,613 | 1.269249 | 52833812 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,618,400 | 0.000274 | 52833812 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,432,813 | 2,398.227257 | 52833812 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,322,662 | 0.998768 | 52833812 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 4,021,069 | 33,700.123444 | 52833812 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/AERO | 10000 | 3,236,348 | 3,045.918143 | 52833812 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,852,589 | 0.000012 | 52833812 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/VVV | 2724 | 2,640,764 | 99.191993 | 52833812 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,629,674 | 1.142107 | 52833812 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,286,260 | 401.862006 | 52833812 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | AERO/cbBTC | 2700 | 2,235,289 | 0.000010 | 52833812 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | WETH/FAI | 10000 | 2,180,732 | 1,226,346.894757 | 52833812 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,059,184 | 1.238174 | 52833812 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,036,084 | 1.373409 | 52833812 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| uniswap_v3 | BNKR/WETH | 10000 | 2,011,015 | 0.000000 | 52833812 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,806,485 | 0.019377 | 52833812 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 1,786,875 | 971.068209 | 52833812 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,775,957 | 0.000012 | 52833812 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | weETH_04c0/WETH | 500 | 1,734,197 | 1.105525 | 52833812 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,719,511 | 16.130504 | 52833812 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | fBOMB/USDC | 10000 | 1,672,768 | 0.020216 | 52833812 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,669,817 | 13,689.522563 | 52833812 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/msETH (stable) | 500 | 1,644,059 | 2.307332 | 52833812 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,552,493 | 0.916343 | 52833812 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| uniswap_v3 | WETH/AERO | 3000 | 1,497,681 | 3,032.130400 | 52833812 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | EURC/USDC | 70 | 1,475,978 | 1.121863 | 52833812 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,457,245 | 0.826781 | 52833812 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | DRB/WETH | 10000 | 1,304,008 | 0.000000 | 52833812 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,301,727 | 0.004709 | 52833812 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,294,703 | 0.000276 | 52833812 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | WETH/cbBTC | 3000 | 1,281,031 | 0.029313 | 52833812 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| aerodrome | USDC/SEND | 3000 | 1,230,346 | 64.193056 | 52833812 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome | WETH/WELL | 10000 | 1,219,128 | 1,048,027.254496 | 52833812 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,211,728 | 23.009238 | 52833812 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,210,689 | 2,397.807726 | 52833812 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | WETH/doginme | 10000 | 1,193,621 | 35,351,980.698677 | 52833812 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,167,401 | 0.435758 | 52833812 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,132,953 | 509,169.018619 | 52833812 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome_slipstream | WETH/msETH | 500 | 1,129,891 | 1.131631 | 52833812 | `0x74F72788F4814D7fF3C49B44684aa98Eee140C0E` |
| aerodrome | USDC/NOCK | 3000 | 1,114,285 | 50.746891 | 52833812 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | msUSD/USDC | 500 | 1,113,820 | 0.885551 | 52833812 | `0x7501bc8Bb51616F79bfA524E464fb7B41f0B10fB` |
| aerodrome_slipstream | USDC/USDT | 8 | 1,075,516 | 1.001366 | 52833812 | `0xa41Bc0AFfbA7Fd420d186b84899d7ab2aC57fcD1` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,074,564 | 15.632662 | 52833812 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |

## Recherche d'opportunités
- Cycles : 707 ; routes examinées : 14902146 ; candidats optimisés : 69447 ; net attendu > 0 : 0 ; dernier cycle 113.7 ms
- Rejets (moteur) : {'spread_below_threshold': 14708781, 'liquidity_below_min': 106243, 'negative_expected_net': 69447, 'borrow_bound_too_small': 17675}
- Enregistrements de la session : 69447 ; net attendu > 0 : 0 ; simulés (eth_call de la vraie tx) : 0 (ok 0, échec 0) ; étiquettes ghost N+1 : 0/0 positives
- Décisions : {'REJECTED': 69447} ; motifs de rejet : {'negative_expected_net': 69447}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|

_Aucun candidat à net positif. Les 10 plus proches de la rentabilité (net attendu négatif) :_

| Bloc | Route | Montant | Brut | Frais flash | Gaz (dont L1) | Net attendu (€) | Marge (bps) |
|---:|---|---:|---:|---:|---:|---:|---:|
| 52833612 | USDC→[aerodrome]→WETH→[pancakeswap_v3]→USDC | 4.535790 USDC | 0.002676 USDC | 0.000000 USDC | 0.005054 USDC | -0.0022 | -5.24 |
| 52833612 | USDC→[aerodrome]→WETH→[pancakeswap_v3]→USDC | 4.535790 USDC | 0.002676 USDC | 0.000000 USDC | 0.005054 USDC | -0.0022 | -5.24 |
| 52833612 | WETH→[pancakeswap_v3]→USDC→[aerodrome]→WETH | 0.001920 WETH | 0.000001 WETH | 0.000000 WETH | 0.000002 WETH | -0.0022 | -5.17 |
| 52833612 | WETH→[pancakeswap_v3]→USDC→[aerodrome]→WETH | 0.001920 WETH | 0.000001 WETH | 0.000000 WETH | 0.000002 WETH | -0.0022 | -5.17 |
| 52833612 | USDC→[aerodrome]→WETH→[uniswap_v3]→USDC | 4.353155 USDC | 0.002439 USDC | 0.000000 USDC | 0.005054 USDC | -0.0024 | -6.01 |
| 52833612 | USDC→[aerodrome]→WETH→[uniswap_v3]→USDC | 4.353155 USDC | 0.002439 USDC | 0.000000 USDC | 0.005054 USDC | -0.0024 | -6.01 |
| 52833612 | WETH→[uniswap_v3]→USDC→[aerodrome]→WETH | 0.001849 WETH | 0.000001 WETH | 0.000000 WETH | 0.000002 WETH | -0.0024 | -5.91 |
| 52833612 | WETH→[uniswap_v3]→USDC→[aerodrome]→WETH | 0.001849 WETH | 0.000001 WETH | 0.000000 WETH | 0.000002 WETH | -0.0024 | -5.91 |
| 52833612 | USDC→[aerodrome]→WETH→[aerodrome_slipstream]→USDC | 3.899067 USDC | 0.002403 USDC | 0.000000 USDC | 0.005054 USDC | -0.0024 | -6.80 |
| 52833612 | USDC→[aerodrome]→WETH→[aerodrome_slipstream]→USDC | 3.899067 USDC | 0.002403 USDC | 0.000000 USDC | 0.005054 USDC | -0.0024 | -6.80 |

## Fiabilité et décision
- Observations ghost : 1336 ; taux observé 0.103 ; borne inférieure crédible (0.9) 0.093 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 9.3% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
