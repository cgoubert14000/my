# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-19T19:15:02+00:00 ; durée 21.34 min ; blocs 52823333 → 52823976 (628 vus)

## Connexion
- Requêtes RPC : 8568 ; erreurs : 35 ; latence p50/p95 : 389.3/1,231.0 ms
- Rafraîchissements d'état : 628 ; âge des données au dernier bloc : 2.8 s ; changements de frais LP observés (pools à frais dynamiques) : 862
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 8999 ; cycles déclenchés par événement : 544 ; avance médiane sur le rafraîchissement multicall : 885 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,394.98 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 571 pools, 327 jetons, 21062 routes
- Par DEX : uniswap_v3 137, aerodrome 234, aerodrome_slipstream 153, pancakeswap_v3 30, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 206 (rejetés 2) → 611 jetons ; pools candidats 3873 (énumérés 387, par paires 0), mesurés 573, sous le plancher de 10000.0 $ : 2 → gardés 571 (max 1500) ; prix des hubs : {'USDC': 1.0, 'DAI': 1.0, 'USDbC': 1.0, 'WETH': 2395.019975, 'AERO': 0.776373, 'cbBTC': 81898.158416}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 146,354,371 | 2,394.984832 | 52823977 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 33,868,425 | 1.285462 | 52823977 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 500 | 18,200,492 | 0.029292 | 52823977 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 17,335,233 | 98.735387 | 52823977 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 13,406,313 | 0.029274 | 52823977 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,343,146 | 0.029287 | 52823977 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,864,699 | 0.000012 | 52823977 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome_slipstream | USDC/cbBTC | 400 | 8,935,983 | 0.000012 | 52823977 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | WETH/USDC | 500 | 8,330,760 | 2,395.792172 | 52823977 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/USDC | 3000 | 8,297,631 | 2,396.048343 | 52823977 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | USDC/cbBTC | 330 | 7,824,648 | 0.000012 | 52823977 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,152,200 | 0.001657 | 52823977 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | WETH/USDC | 579 | 7,109,539 | 2,396.162119 | 52823977 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,330,292 | 0.029290 | 52823977 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | fBOMB/AERO | 10000 | 4,871,437 | 0.026002 | 52823977 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome_slipstream | USDC/AERO | 10000 | 4,867,244 | 1.286157 | 52823977 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,771,515 | 0.802395 | 52823977 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,602,904 | 0.000273 | 52823977 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,407,571 | 2,396.289093 | 52823977 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,333,507 | 0.998765 | 52823977 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 4,008,968 | 33,850.417929 | 52823977 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDT | 406 | 3,767,583 | 2,399.779605 | 52823977 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome | WETH/AERO | 10000 | 3,208,247 | 3,088.652408 | 52823977 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,874,347 | 0.000012 | 52823977 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,709,321 | 1.142127 | 52823977 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| aerodrome_slipstream | WETH/VVV | 2754 | 2,643,438 | 98.710342 | 52823977 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,367,102 | 404.128448 | 52823977 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 2,251,014 | 0.000010 | 52823977 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | WETH/FAI | 10000 | 2,179,013 | 1,226,346.894757 | 52823977 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,059,139 | 1.238201 | 52823977 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,036,084 | 1.373409 | 52823977 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| uniswap_v3 | BNKR/WETH | 10000 | 2,020,628 | 0.000000 | 52823977 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,778,396 | 0.018839 | 52823977 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,777,461 | 0.000012 | 52823977 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,732,258 | 16.272388 | 52823977 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | weETH_04c0/WETH | 500 | 1,730,288 | 1.105525 | 52823977 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome | fBOMB/USDC | 10000 | 1,710,430 | 0.020206 | 52823977 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| aerodrome | WETH/msETH (stable) | 500 | 1,657,303 | 2.307261 | 52823977 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | WETH/MORPHO | 2709 | 1,594,380 | 973.680578 | 52823977 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,583,076 | 13,810.725844 | 52823977 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,551,254 | 0.916349 | 52823977 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| uniswap_v3 | WETH/AERO | 3000 | 1,487,212 | 3,081.716626 | 52823977 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,456,815 | 0.827259 | 52823977 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | EURC/USDC | 70 | 1,406,382 | 1.121357 | 52823977 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,338,245 | 0.435693 | 52823977 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,315,510 | 0.000000 | 52823977 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,302,189 | 0.004691 | 52823977 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,290,315 | 0.000274 | 52823977 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | WETH/cbBTC | 3000 | 1,278,052 | 0.029281 | 52823977 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,263,141 | 23.136818 | 52823977 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| aerodrome | USDC/SEND | 3000 | 1,232,650 | 63.953345 | 52823977 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,227,210 | 2,395.766358 | 52823977 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | WETH/WELL | 10000 | 1,194,448 | 1,090,063.531515 | 52823977 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/doginme | 10000 | 1,192,595 | 35,357,041.192794 | 52823977 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome_slipstream | msUSD/USDC | 500 | 1,134,548 | 0.885650 | 52823977 | `0x7501bc8Bb51616F79bfA524E464fb7B41f0B10fB` |
| aerodrome_slipstream | WETH/msETH | 500 | 1,127,104 | 1.131643 | 52823977 | `0x74F72788F4814D7fF3C49B44684aa98Eee140C0E` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,126,901 | 515,618.431308 | 52823977 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | USDC/NOCK | 3000 | 1,112,649 | 50.896196 | 52823977 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,080,506 | 15.395841 | 52823977 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome_slipstream | USDC/USDT | 8 | 1,071,434 | 1.001428 | 52823977 | `0xa41Bc0AFfbA7Fd420d186b84899d7ab2aC57fcD1` |

## Recherche d'opportunités
- Cycles : 1171 ; routes examinées : 24663602 ; candidats optimisés : 127322 ; net attendu > 0 : 0 ; dernier cycle 146.9 ms
- Rejets (moteur) : {'spread_below_threshold': 24306871, 'liquidity_below_min': 200134, 'negative_expected_net': 127322, 'borrow_bound_too_small': 29275}
- Enregistrements de la session : 127322 ; net attendu > 0 : 0 ; simulés (eth_call de la vraie tx) : 0 (ok 0, échec 0) ; étiquettes ghost N+1 : 0/0 positives
- Décisions : {'REJECTED': 127322} ; motifs de rejet : {'negative_expected_net': 127322}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|

_Aucun candidat à net positif. Les 10 plus proches de la rentabilité (net attendu négatif) :_

| Bloc | Route | Montant | Brut | Frais flash | Gaz (dont L1) | Net attendu (€) | Marge (bps) |
|---:|---|---:|---:|---:|---:|---:|---:|
| 52823762 | USDC→[uniswap_v3]→WETH→[aerodrome]→USDC | 4.995327 USDC | 0.003242 USDC | 0.000000 USDC | 0.005058 USDC | -0.0017 | -3.64 |
| 52823762 | USDC→[uniswap_v3]→WETH→[aerodrome]→USDC | 4.995327 USDC | 0.003242 USDC | 0.000000 USDC | 0.005058 USDC | -0.0017 | -3.64 |
| 52823763 | USDC→[uniswap_v3]→WETH→[aerodrome]→USDC | 4.995327 USDC | 0.003242 USDC | 0.000000 USDC | 0.005058 USDC | -0.0017 | -3.64 |
| 52823764 | USDC→[uniswap_v3]→WETH→[aerodrome]→USDC | 4.995327 USDC | 0.003242 USDC | 0.000000 USDC | 0.005058 USDC | -0.0017 | -3.64 |
| 52823764 | USDC→[uniswap_v3]→WETH→[aerodrome]→USDC | 4.995327 USDC | 0.003242 USDC | 0.000000 USDC | 0.005058 USDC | -0.0017 | -3.64 |
| 52823762 | WETH→[aerodrome]→USDC→[uniswap_v3]→WETH | 0.002127 WETH | 0.000001 WETH | 0.000000 WETH | 0.000002 WETH | -0.0017 | -3.56 |
| 52823762 | WETH→[aerodrome]→USDC→[uniswap_v3]→WETH | 0.002127 WETH | 0.000001 WETH | 0.000000 WETH | 0.000002 WETH | -0.0017 | -3.56 |
| 52823763 | WETH→[aerodrome]→USDC→[uniswap_v3]→WETH | 0.002127 WETH | 0.000001 WETH | 0.000000 WETH | 0.000002 WETH | -0.0017 | -3.56 |
| 52823764 | WETH→[aerodrome]→USDC→[uniswap_v3]→WETH | 0.002127 WETH | 0.000001 WETH | 0.000000 WETH | 0.000002 WETH | -0.0017 | -3.56 |
| 52823764 | WETH→[aerodrome]→USDC→[uniswap_v3]→WETH | 0.002127 WETH | 0.000001 WETH | 0.000000 WETH | 0.000002 WETH | -0.0017 | -3.56 |

## Fiabilité et décision
- Observations ghost : 1335 ; taux observé 0.103 ; borne inférieure crédible (0.9) 0.093 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 9.3% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
