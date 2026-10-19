# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-19T13:34:00+00:00 ; durée 30.6 min ; blocs 52812825 → 52813744 (918 vus)

## Connexion
- Requêtes RPC : 11270 ; erreurs : 0 ; latence p50/p95 : 170.6/811.6 ms
- Rafraîchissements d'état : 918 ; âge des données au dernier bloc : 4.06 s ; changements de frais LP observés (pools à frais dynamiques) : 2003
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 2148 ; cycles déclenchés par événement : 109 ; avance médiane sur le rafraîchissement multicall : 1,027 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,420.32 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 571 pools, 327 jetons, 21004 routes
- Par DEX : uniswap_v3 137, aerodrome 234, aerodrome_slipstream 153, pancakeswap_v3 30, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 207 (rejetés 2) → 612 jetons ; pools candidats 3877 (énumérés 390, par paires 0), mesurés 574, sous le plancher de 10000.0 $ : 3 → gardés 571 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2419.85313, 'AERO': 0.782295, 'cbBTC': 82567.067054}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 148,170,219 | 2,420.322849 | 52813745 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 35,102,405 | 1.274760 | 52813745 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 500 | 18,424,011 | 0.029346 | 52813745 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 17,224,988 | 102.135910 | 52813745 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| aerodrome_slipstream | WETH/cbBTC | 2505 | 12,909,919 | 0.029391 | 52813745 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,411,223 | 0.029384 | 52813745 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,868,265 | 0.000012 | 52813745 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 8,457,251 | 2,416.691996 | 52813745 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/USDC | 3000 | 8,342,661 | 2,421.036573 | 52813745 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | USDC/cbBTC | 346 | 7,840,167 | 0.000012 | 52813745 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | USDC/cbBTC | 508 | 7,364,705 | 0.000012 | 52813745 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome_slipstream | WETH/USDC | 698 | 7,248,828 | 2,416.638063 | 52813745 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,228,085 | 0.001663 | 52813745 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,367,159 | 0.029336 | 52813745 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | fBOMB/AERO | 10000 | 4,951,773 | 0.025987 | 52813745 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,837,479 | 0.802395 | 52813745 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome_slipstream | USDC/AERO | 10000 | 4,752,018 | 1.281750 | 52813745 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,652,283 | 0.000273 | 52813745 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,444,653 | 2,416.836570 | 52813745 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,370,227 | 0.998770 | 52813745 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 4,043,185 | 33,987.809218 | 52813745 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDT | 439 | 3,489,589 | 2,419.959605 | 52813745 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome | WETH/AERO | 10000 | 3,256,677 | 3,085.398532 | 52813745 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,861,943 | 0.000012 | 52813745 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,752,059 | 405.866438 | 52813745 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,737,974 | 1.142004 | 52813745 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| aerodrome_slipstream | WETH/VVV | 2751 | 2,645,481 | 102.159150 | 52813745 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 2,381,261 | 0.000010 | 52813745 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | WETH/FAI | 10000 | 2,194,285 | 1,235,059.554017 | 52813745 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 2,180,252 | 986.986012 | 52813745 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,062,172 | 1.234881 | 52813745 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | BNKR/WETH | 10000 | 2,052,428 | 0.000000 | 52813745 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,036,743 | 1.372638 | 52813745 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,877,546 | 16.021945 | 52813745 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,773,951 | 0.000012 | 52813745 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | XDP/USDC | 100 | 1,760,519 | 0.018515 | 52813745 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome | weETH_04c0/WETH | 500 | 1,750,093 | 1.105523 | 52813745 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,744,109 | 13,840.094665 | 52813745 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | fBOMB/USDC | 10000 | 1,726,218 | 0.020593 | 52813745 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| aerodrome | WETH/msETH (stable) | 500 | 1,674,033 | 2.308863 | 52813745 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | EURC/USDC | 76 | 1,612,329 | 1.122366 | 52813745 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| uniswap_v3 | WETH/AERO | 3000 | 1,607,460 | 3,086.093890 | 52813745 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,567,665 | 0.916350 | 52813745 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,456,163 | 0.827402 | 52813745 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,339,449 | 0.436285 | 52813745 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,325,290 | 0.000000 | 52813745 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,304,052 | 0.000274 | 52813745 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | WETH/cbBTC | 3000 | 1,290,370 | 0.029380 | 52813745 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,284,860 | 0.004581 | 52813745 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,263,455 | 23.129508 | 52813745 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| aerodrome | USDC/SEND | 3000 | 1,232,868 | 63.930699 | 52813745 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome | WETH/WELL | 10000 | 1,214,264 | 1,077,211.227828 | 52813745 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/doginme | 10000 | 1,207,154 | 35,153,103.776698 | 52813745 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,200,588 | 2,416.628511 | 52813745 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome_slipstream | msUSD/USDC | 500 | 1,177,665 | 0.885973 | 52813745 | `0x7501bc8Bb51616F79bfA524E464fb7B41f0B10fB` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,138,963 | 515,481.870232 | 52813745 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | USDC/NOCK | 3000 | 1,104,192 | 51.678854 | 52813745 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | WETH/msETH | 500 | 1,099,186 | 1.131964 | 52813745 | `0x74F72788F4814D7fF3C49B44684aa98Eee140C0E` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,081,472 | 15.359942 | 52813745 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | WETH/EDEL | 7000 | 1,058,934 | 89,984.435224 | 52813745 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |

## Recherche d'opportunités
- Cycles : 1026 ; routes examinées : 21550104 ; candidats optimisés : 165062 ; net attendu > 0 : 0 ; dernier cycle 210.7 ms
- Rejets (moteur) : {'spread_below_threshold': 21173682, 'liquidity_below_min': 187714, 'negative_expected_net': 165062, 'borrow_bound_too_small': 23646}
- Enregistrements de la session : 165062 ; net attendu > 0 : 0 ; simulés (eth_call de la vraie tx) : 0 (ok 0, échec 0) ; étiquettes ghost N+1 : 0/0 positives
- Décisions : {'REJECTED': 165062} ; motifs de rejet : {'negative_expected_net': 165062}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|

_Aucun candidat à net positif. Les 10 plus proches de la rentabilité (net attendu négatif) :_

| Bloc | Route | Montant | Brut | Frais flash | Gaz (dont L1) | Net attendu (€) | Marge (bps) |
|---:|---|---:|---:|---:|---:|---:|---:|
| 52813633 | USDC→[pancakeswap_v3]→PLAY→[aerodrome]→USDC | 1.616819 USDC | 0.000271 USDC | 0.000000 USDC | 0.000867 USDC | -0.0005 | -3.69 |
| 52813633 | cbBTC→[aerodrome]→tBTC→[pancakeswap_v3]→cbBTC | 0.000012 cbBTC | -0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | -0.0015 | -16.52 |
| 52813633 | cbBTC→[aerodrome]→tBTC→[uniswap_v3]→cbBTC | 0.000012 cbBTC | -0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | -0.0015 | -16.52 |
| 52813633 | cbBTC→[aerodrome]→tBTC→[aerodrome_slipstream]→cbBTC | 0.000012 cbBTC | -0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | -0.0015 | -16.52 |
| 52813666 | USDC→[aerodrome]→OWB→[uniswap_v3]→USDC | 5.918913 USDC | 0.003048 USDC | 0.000000 USDC | 0.005113 USDC | -0.0019 | -3.49 |
| 52813667 | USDC→[aerodrome]→OWB→[uniswap_v3]→USDC | 5.918913 USDC | 0.003048 USDC | 0.000000 USDC | 0.005113 USDC | -0.0019 | -3.49 |
| 52813668 | USDC→[aerodrome]→OWB→[uniswap_v3]→USDC | 5.918913 USDC | 0.003048 USDC | 0.000000 USDC | 0.005113 USDC | -0.0019 | -3.49 |
| 52813669 | USDC→[aerodrome]→OWB→[uniswap_v3]→USDC | 5.918913 USDC | 0.003048 USDC | 0.000000 USDC | 0.005113 USDC | -0.0019 | -3.49 |
| 52813670 | USDC→[aerodrome]→OWB→[uniswap_v3]→USDC | 5.918913 USDC | 0.003048 USDC | 0.000000 USDC | 0.005113 USDC | -0.0019 | -3.49 |
| 52813671 | USDC→[aerodrome]→OWB→[uniswap_v3]→USDC | 5.918913 USDC | 0.003048 USDC | 0.000000 USDC | 0.005113 USDC | -0.0019 | -3.49 |

## Fiabilité et décision
- Observations ghost : 1270 ; taux observé 0.103 ; borne inférieure crédible (0.9) 0.093 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 9.3% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
