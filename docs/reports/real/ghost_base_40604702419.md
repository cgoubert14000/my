# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-27T23:56:56+00:00 ; durée 3.06 min ; blocs 53177940 → 53178034 (92 vus)

## Connexion
- Requêtes RPC : 1156 ; erreurs : 0 ; latence p50/p95 : 122.8/1,501.2 ms
- Rafraîchissements d'état : 93 ; âge des données au dernier bloc : 1.18 s ; changements de frais LP observés (pools à frais dynamiques) : 57
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 410 ; cycles déclenchés par événement : 106 ; avance médiane sur le rafraîchissement multicall : 266 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,351.40 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 524 pools, 303 jetons, 19128 routes
- Par DEX : uniswap_v3 147, aerodrome 211, aerodrome_slipstream 123, pancakeswap_v3 28, uniswap_v2 12, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 185 (rejetés 2) → 590 jetons ; pools candidats 3771 (énumérés 333, par paires 0), mesurés 526, sous le plancher de 10000.0 $ : 2 → gardés 524 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2351.399953, 'cbBTC': 80864.599929, 'AERO': 0.698092}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 157,915,174 | 2,351.399954 | 53178034 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,666,269 | 0.029054 | 53178034 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,647,832 | 0.000012 | 53178034 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,473,986 | 0.029025 | 53178034 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| aerodrome | WETH/VVV | 3000 | 8,640,162 | 90.066001 | 53178034 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/USDC | 500 | 8,438,280 | 2,350.180665 | 53178034 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,040,390 | 0.001638 | 53178034 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 6,954,623 | 1.432476 | 53178034 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,740,874 | 0.029058 | 53178034 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/USDC | 150 | 5,084,194 | 2,349.364900 | 53178034 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,494,235 | 2,349.244302 | 53178034 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,262,923 | 0.998745 | 53178034 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,734,373 | 37,111.110971 | 53178034 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,972,927 | 0.029022 | 53178034 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2706 | 2,588,243 | 90.181040 | 53178034 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | WETH/USDC | 3000 | 2,367,560 | 2,353.321021 | 53178034 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | USDC/cbBTC | 412 | 2,190,045 | 0.000012 | 53178034 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome | WETH/FAI | 10000 | 2,140,511 | 1,223,453.115946 | 53178034 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,829,303 | 0.000000 | 53178034 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,826,989 | 0.018654 | 53178034 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,792,873 | 397.849761 | 53178034 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | USDC/cbBTC | 334 | 1,699,602 | 0.000012 | 53178034 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,692,010 | 0.000012 | 53178034 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,688,298 | 0.000012 | 53178034 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,536,576 | 0.005901 | 53178034 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,474,280 | 1.658893 | 53178034 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,461,579 | 0.826489 | 53178034 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,458,591 | 3,362.054784 | 53178034 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,395,529 | 13,704.199515 | 53178034 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,256,532 | 0.000268 | 53178034 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,242,072 | 2,350.172653 | 53178034 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | WETH/AERO | 10000 | 1,206,560 | 3,358.072677 | 53178034 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | USDC/SEND | 3000 | 1,204,103 | 67.021598 | 53178034 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome | VIRTUAL/WETH | 10000 | 1,187,901 | 0.000266 | 53178034 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | WETH/doginme | 10000 | 1,167,355 | 35,864,396.477338 | 53178034 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | WETH/WELL | 10000 | 1,166,913 | 1,064,762.619516 | 53178034 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | DRB/WETH | 10000 | 1,130,304 | 0.000000 | 53178034 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,118,324 | 505,793.932972 | 53178034 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | WETH/EDEL | 7000 | 1,089,242 | 71,210.528265 | 53178034 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | USDC/NOCK | 3000 | 1,065,130 | 55.178028 | 53178034 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,058,542 | 16.204742 | 53178034 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,049,710 | 21,236,902.374132 | 53178034 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | USDC/VVV | 3000 | 1,041,042 | 0.038337 | 53178034 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/USDC | 10000 | 944,891 | 2,338.016459 | 53178034 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 926,501 | 1,074.097285 | 53178034 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | uXRP/WETH | 3000 | 911,103 | 0.000563 | 53178034 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| uniswap_v3 | WETH/VVV | 10000 | 907,109 | 90.276503 | 53178034 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome | WETH/msETH (stable) | 500 | 888,142 | 2.312268 | 53178034 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 885,572 | 17.762433 | 53178034 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v2 | WETH/USDC | 3000 | 850,016 | 2,350.686129 | 53178034 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 843,816 | 17.592645 | 53178034 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 811,466 | 0.000009 | 53178034 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| pancakeswap_v3 | QUID/USDC | 100 | 803,231 | 0.057897 | 53178034 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 796,125 | 0.803180 | 53178034 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 756,240 | 4,564,173.658348 | 53178034 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 753,634 | 0.629691 | 53178034 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/NPC | 3000 | 712,116 | 137,274.673322 | 53178034 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 695,959 | 502,737.041639 | 53178034 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | TIG/USDC | 10000 | 685,293 | 0.591143 | 53178034 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 675,870 | 0.109218 | 53178034 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |

## Recherche d'opportunités
- Cycles : 198 ; routes examinées : 3787344 ; candidats optimisés : 8454 ; net attendu > 0 : 0 ; dernier cycle 95.9 ms
- Rejets (moteur) : {'spread_below_threshold': 3716870, 'liquidity_below_min': 58612, 'negative_expected_net': 8454, 'borrow_bound_too_small': 3349}
- Enregistrements de la session : 8454 ; net attendu > 0 : 0 ; simulés (eth_call de la vraie tx) : 0 (ok 0, échec 0) ; étiquettes ghost N+1 : 0/0 positives
- Décisions : {'REJECTED': 8454} ; motifs de rejet : {'negative_expected_net': 8454}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|

_Aucun candidat à net positif. Les 10 plus proches de la rentabilité (net attendu négatif) :_

| Bloc | Route | Montant | Brut | Frais flash | Gaz (dont L1) | Net attendu (€) | Marge (bps) |
|---:|---|---:|---:|---:|---:|---:|---:|
| 53178011 | USDC→[aerodrome]→OWB→[uniswap_v3]→USDC | 4.468874 USDC | 0.001897 USDC | 0.000000 USDC | 0.004956 USDC | -0.0028 | -6.85 |
| 53178012 | USDC→[aerodrome]→OWB→[uniswap_v3]→USDC | 4.468874 USDC | 0.001897 USDC | 0.000000 USDC | 0.004956 USDC | -0.0028 | -6.85 |
| 53178012 | USDC→[aerodrome]→OWB→[uniswap_v3]→USDC | 4.468874 USDC | 0.001897 USDC | 0.000000 USDC | 0.004956 USDC | -0.0028 | -6.85 |
| 53178012 | USDC→[aerodrome]→OWB→[uniswap_v3]→USDC | 4.468874 USDC | 0.001897 USDC | 0.000000 USDC | 0.004956 USDC | -0.0028 | -6.85 |
| 53178013 | USDC→[aerodrome]→OWB→[uniswap_v3]→USDC | 4.468874 USDC | 0.001897 USDC | 0.000000 USDC | 0.004956 USDC | -0.0028 | -6.85 |
| 53178013 | USDC→[aerodrome]→OWB→[uniswap_v3]→USDC | 4.468874 USDC | 0.001897 USDC | 0.000000 USDC | 0.004956 USDC | -0.0028 | -6.85 |
| 53178014 | USDC→[aerodrome]→OWB→[uniswap_v3]→USDC | 4.468874 USDC | 0.001897 USDC | 0.000000 USDC | 0.004956 USDC | -0.0028 | -6.85 |
| 53178014 | USDC→[aerodrome]→OWB→[uniswap_v3]→USDC | 4.468874 USDC | 0.001897 USDC | 0.000000 USDC | 0.004956 USDC | -0.0028 | -6.85 |
| 53178015 | USDC→[aerodrome]→OWB→[uniswap_v3]→USDC | 4.468874 USDC | 0.001897 USDC | 0.000000 USDC | 0.004956 USDC | -0.0028 | -6.85 |
| 53178015 | USDC→[aerodrome]→OWB→[uniswap_v3]→USDC | 4.468874 USDC | 0.001897 USDC | 0.000000 USDC | 0.004956 USDC | -0.0028 | -6.85 |

## Fiabilité et décision
- Observations ghost : 2878 ; taux observé 0.091 ; borne inférieure crédible (0.9) 0.084 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 8.4% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
