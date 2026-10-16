# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-16T00:53:25+00:00 ; durée 12.2 min ; blocs 52660958 → 52661327 (333 vus)

## Connexion
- Requêtes RPC : 3886 ; erreurs : 0 ; latence p50/p95 : 409.9/2,356.6 ms
- Rafraîchissements d'état : 333 ; âge des données au dernier bloc : 3.54 s ; changements de frais LP observés (pools à frais dynamiques) : 699
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 0 ; cycles déclenchés par événement : 0 ; avance médiane sur le rafraîchissement multicall : — ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,444.06 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 573 pools, 327 jetons, 21346 routes
- Par DEX : uniswap_v3 134, aerodrome 235, aerodrome_slipstream 155, pancakeswap_v3 31, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 208 (rejetés 2) → 613 jetons ; pools candidats 3922 (énumérés 392, par paires 0), mesurés 575, sous le plancher de 10000.0 $ : 2 → gardés 573 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2444.060646, 'AERO': 0.934005, 'cbBTC': 82314.094538}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 146,556,188 | 2,444.059481 | 52661328 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 47,126,199 | 1.071801 | 52661328 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 500 | 18,506,575 | 0.029663 | 52661328 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 16,621,205 | 98.642517 | 52661328 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 14,286,555 | 0.029717 | 52661328 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,575,322 | 0.029732 | 52661328 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,757,020 | 0.000012 | 52661328 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 9,135,579 | 2,438.506690 | 52661328 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome_slipstream | USDC/cbBTC | 448 | 8,531,909 | 0.000012 | 52661328 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome_slipstream | WETH/USDC | 654 | 8,239,926 | 2,438.078457 | 52661328 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | USDC/cbBTC | 338 | 8,023,835 | 0.000012 | 52661328 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,241,083 | 0.001672 | 52661328 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/AERO | 10000 | 6,687,868 | 1.073512 | 52661328 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome | fBOMB/AERO | 10000 | 5,455,740 | 0.024845 | 52661328 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome | WETH/USDC | 3000 | 5,441,844 | 2,445.198388 | 52661328 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,393,974 | 0.029661 | 52661328 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/superOETHb | 400 | 5,222,532 | 1.000855 | 52661328 | `0x6446021F4E396dA3df4235C62537431372195D38` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,885,441 | 0.802398 | 52661328 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,739,584 | 0.000278 | 52661328 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,445,351 | 2,437.741950 | 52661328 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,374,969 | 0.998878 | 52661328 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 4,034,059 | 34,814.692941 | 52661328 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/AERO | 10000 | 3,586,533 | 2,622.811560 | 52661328 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | cbETH/WETH | 60 | 3,071,591 | 1.141780 | 52661328 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| aerodrome_slipstream | WETH/USDT | 418 | 2,992,400 | 2,442.399119 | 52661328 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,851,561 | 0.000012 | 52661328 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/VVV | 2700 | 2,670,769 | 98.705097 | 52661328 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 2,658,365 | 1,005.456327 | 52661328 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,629,772 | 401.910212 | 52661328 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | AERO/cbBTC | 2700 | 2,612,252 | 0.000011 | 52661328 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | WETH/FAI | 10000 | 2,277,747 | 1,168,797.078711 | 52661328 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,111,440 | 1.196097 | 52661328 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | BNKR/WETH | 10000 | 2,102,549 | 0.000000 | 52661328 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,007,548 | 1.404816 | 52661328 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,915,654 | 15.544559 | 52661328 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | fBOMB/USDC | 10000 | 1,822,665 | 0.022697 | 52661328 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| uniswap_v3 | XDP/USDC | 100 | 1,809,993 | 0.019408 | 52661328 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,781,592 | 0.000012 | 52661328 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,715,733 | 13,564.370504 | 52661328 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/msETH (stable) | 500 | 1,687,142 | 2.309115 | 52661328 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | WETH/AERO | 3000 | 1,579,569 | 2,614.956348 | 52661328 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,519,196 | 0.916551 | 52661328 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| aerodrome | weETH_04c0/WETH | 500 | 1,511,178 | 1.105497 | 52661328 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome_slipstream | WETH/AERO | 3000 | 1,478,751 | 2,613.878647 | 52661328 | `0x82321f3BEB69f503380D6B233857d5C43562e2D0` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,456,377 | 0.830051 | 52661328 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | DRB/WETH | 10000 | 1,354,476 | 0.000000 | 52661328 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,353,545 | 0.004821 | 52661328 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,342,418 | 23.255773 | 52661328 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,328,395 | 0.000279 | 52661328 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome_slipstream | EURC/USDC | 73 | 1,326,596 | 1.121194 | 52661328 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| aerodrome | USDC/SEND | 3000 | 1,248,881 | 62.301783 | 52661328 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome | WETH/cbBTC | 3000 | 1,218,153 | 0.029739 | 52661328 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,212,350 | 1.105591 | 52661328 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |
| uniswap_v3 | WETH/doginme | 10000 | 1,212,314 | 35,374,630.668579 | 52661328 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,202,439 | 2,438.489817 | 52661328 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | WETH/WELL | 10000 | 1,190,111 | 1,143,664.079159 | 52661328 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome_slipstream | msUSD/USDC | 500 | 1,176,256 | 0.886065 | 52661328 | `0x7501bc8Bb51616F79bfA524E464fb7B41f0B10fB` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,172,364 | 496,809.210529 | 52661328 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,164,255 | 0.436080 | 52661328 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,129,016 | 13.787454 | 52661328 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |

## Recherche d'opportunités
- Cycles : 332 ; routes examinées : 7086872 ; candidats optimisés : 54206 ; net attendu > 0 : 0 ; dernier cycle 1002.3 ms
- Rejets (moteur) : {'spread_below_threshold': 6967037, 'liquidity_below_min': 64833, 'negative_expected_net': 54206, 'cycle_budget_exhausted': 464, 'borrow_bound_too_small': 332}
- Enregistrements de la session : 54206 ; net attendu > 0 : 0 ; simulés (eth_call de la vraie tx) : 0 (ok 0, échec 0) ; étiquettes ghost N+1 : 0/0 positives
- Décisions : {'REJECTED': 54206} ; motifs de rejet : {'negative_expected_net': 54206}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|

_Aucun candidat à net positif. Les 10 plus proches de la rentabilité (net attendu négatif) :_

| Bloc | Route | Montant | Brut | Frais flash | Gaz (dont L1) | Net attendu (€) | Marge (bps) |
|---:|---|---:|---:|---:|---:|---:|---:|
| 52661112 | WETH→[aerodrome]→USDC→[pancakeswap_v3]→WETH | 0.002031 WETH | 0.000001 WETH | 0.000000 WETH | 0.000002 WETH | -0.0019 | -4.22 |
| 52661108 | WETH→[aerodrome]→USDC→[pancakeswap_v3]→WETH | 0.002031 WETH | 0.000001 WETH | 0.000000 WETH | 0.000002 WETH | -0.0019 | -4.22 |
| 52661110 | WETH→[aerodrome]→USDC→[pancakeswap_v3]→WETH | 0.002031 WETH | 0.000001 WETH | 0.000000 WETH | 0.000002 WETH | -0.0019 | -4.22 |
| 52661111 | WETH→[aerodrome]→USDC→[pancakeswap_v3]→WETH | 0.002031 WETH | 0.000001 WETH | 0.000000 WETH | 0.000002 WETH | -0.0019 | -4.22 |
| 52661108 | USDC→[pancakeswap_v3]→WETH→[aerodrome]→USDC | 4.873874 USDC | 0.003053 USDC | 0.000000 USDC | 0.005153 USDC | -0.0019 | -4.31 |
| 52661110 | USDC→[pancakeswap_v3]→WETH→[aerodrome]→USDC | 4.873874 USDC | 0.003053 USDC | 0.000000 USDC | 0.005153 USDC | -0.0019 | -4.31 |
| 52661111 | USDC→[pancakeswap_v3]→WETH→[aerodrome]→USDC | 4.873874 USDC | 0.003053 USDC | 0.000000 USDC | 0.005153 USDC | -0.0019 | -4.31 |
| 52661112 | USDC→[pancakeswap_v3]→WETH→[aerodrome]→USDC | 4.873874 USDC | 0.003053 USDC | 0.000000 USDC | 0.005153 USDC | -0.0019 | -4.31 |
| 52661105 | WETH→[aerodrome]→USDC→[pancakeswap_v3]→WETH | 0.001985 WETH | 0.000001 WETH | 0.000000 WETH | 0.000002 WETH | -0.0020 | -4.55 |
| 52661106 | WETH→[aerodrome]→USDC→[pancakeswap_v3]→WETH | 0.001985 WETH | 0.000001 WETH | 0.000000 WETH | 0.000002 WETH | -0.0020 | -4.55 |

## Fiabilité et décision
- Observations ghost : 419 ; taux observé 0.138 ; borne inférieure crédible (0.9) 0.118 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 11.8% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
