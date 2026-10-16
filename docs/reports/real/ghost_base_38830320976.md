# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-16T00:50:22+00:00 ; durée 9.17 min ; blocs 52660958 → 52661237 (251 vus)

## Connexion
- Requêtes RPC : 2941 ; erreurs : 0 ; latence p50/p95 : 351.1/2,343.8 ms
- Rafraîchissements d'état : 252 ; âge des données au dernier bloc : 1.52 s ; changements de frais LP observés (pools à frais dynamiques) : 551
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
| uniswap_v3 | WETH/USDC | 3000 | 146,553,640 | 2,444.061685 | 52661237 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 47,147,540 | 1.070830 | 52661237 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 500 | 18,506,592 | 0.029663 | 52661237 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 16,655,932 | 98.634049 | 52661237 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 15,018,844 | 0.029717 | 52661237 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,575,332 | 0.029732 | 52661237 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,755,224 | 0.000012 | 52661237 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 9,135,554 | 2,440.008023 | 52661237 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome_slipstream | USDC/cbBTC | 338 | 8,023,815 | 0.000012 | 52661237 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 654 | 7,425,186 | 2,439.586512 | 52661237 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | USDC/cbBTC | 448 | 7,305,879 | 0.000012 | 52661237 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,242,532 | 0.001673 | 52661237 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/AERO | 10000 | 6,690,813 | 1.073512 | 52661237 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome | fBOMB/AERO | 10000 | 5,458,236 | 0.024845 | 52661237 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome | WETH/USDC | 3000 | 5,441,846 | 2,445.044154 | 52661237 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,393,978 | 0.029667 | 52661237 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/superOETHb | 400 | 5,222,536 | 1.000855 | 52661237 | `0x6446021F4E396dA3df4235C62537431372195D38` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,885,445 | 0.802398 | 52661237 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,739,588 | 0.000278 | 52661237 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,445,403 | 2,439.087443 | 52661237 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,374,973 | 0.998878 | 52661237 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 4,034,062 | 34,814.692941 | 52661237 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/AERO | 10000 | 3,588,161 | 2,622.811560 | 52661237 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | cbETH/WETH | 60 | 3,071,593 | 1.141780 | 52661237 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,851,563 | 0.000012 | 52661237 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/VVV | 2706 | 2,670,867 | 98.705097 | 52661237 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,669,327 | 402.113231 | 52661237 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 2,659,409 | 1,005.450976 | 52661237 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 2,613,417 | 0.000011 | 52661237 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | WETH/FAI | 10000 | 2,277,749 | 1,168,797.078711 | 52661237 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,111,440 | 1.196097 | 52661237 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | BNKR/WETH | 10000 | 2,102,550 | 0.000000 | 52661237 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome_slipstream | WETH/USDT | 418 | 2,009,178 | 2,443.591336 | 52661237 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,007,548 | 1.404816 | 52661237 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,879,170 | 15.546874 | 52661237 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | fBOMB/USDC | 10000 | 1,822,664 | 0.022697 | 52661237 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| uniswap_v3 | XDP/USDC | 100 | 1,806,279 | 0.019337 | 52661237 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,781,586 | 0.000012 | 52661237 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,777,007 | 13,569.350749 | 52661237 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/msETH (stable) | 500 | 1,687,144 | 2.309115 | 52661237 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | WETH/AERO | 3000 | 1,579,984 | 2,614.956348 | 52661237 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | weETH_04c0/WETH | 500 | 1,511,179 | 1.105497 | 52661237 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,490,316 | 0.916551 | 52661237 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| aerodrome_slipstream | WETH/AERO | 3016 | 1,466,778 | 2,613.878647 | 52661237 | `0x82321f3BEB69f503380D6B233857d5C43562e2D0` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,456,377 | 0.830051 | 52661237 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,372,114 | 0.004839 | 52661237 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v3 | DRB/WETH | 10000 | 1,354,478 | 0.000000 | 52661237 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,350,471 | 23.255773 | 52661237 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,328,396 | 0.000279 | 52661237 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome_slipstream | EURC/USDC | 70 | 1,326,489 | 1.121064 | 52661237 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| aerodrome | USDC/SEND | 3000 | 1,248,881 | 62.301783 | 52661237 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome | WETH/cbBTC | 3000 | 1,218,154 | 0.029739 | 52661237 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,212,351 | 1.105591 | 52661237 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |
| uniswap_v3 | WETH/doginme | 10000 | 1,212,315 | 35,374,630.668579 | 52661237 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,202,428 | 2,440.109375 | 52661237 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | WETH/WELL | 10000 | 1,190,113 | 1,143,664.079159 | 52661237 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome_slipstream | msUSD/USDC | 500 | 1,176,256 | 0.886065 | 52661237 | `0x7501bc8Bb51616F79bfA524E464fb7B41f0B10fB` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,172,071 | 496,809.210529 | 52661237 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,164,255 | 0.436080 | 52661237 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,129,206 | 13.781711 | 52661237 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |

## Recherche d'opportunités
- Cycles : 251 ; routes examinées : 5357846 ; candidats optimisés : 34048 ; net attendu > 0 : 0 ; dernier cycle 554.4 ms
- Rejets (moteur) : {'spread_below_threshold': 5278380, 'liquidity_below_min': 44703, 'negative_expected_net': 34048, 'cycle_budget_exhausted': 464, 'borrow_bound_too_small': 251}
- Enregistrements de la session : 34048 ; net attendu > 0 : 0 ; simulés (eth_call de la vraie tx) : 0 (ok 0, échec 0) ; étiquettes ghost N+1 : 0/0 positives
- Décisions : {'REJECTED': 34048} ; motifs de rejet : {'negative_expected_net': 34048}

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
