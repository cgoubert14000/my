# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-22T20:24:51+00:00 ; durée 15.18 min ; blocs 52955211 → 52955670 (408 vus)

## Connexion
- Requêtes RPC : 5155 ; erreurs : 0 ; latence p50/p95 : 467.6/2,499.1 ms
- Rafraîchissements d'état : 408 ; âge des données au dernier bloc : 3.8 s ; changements de frais LP observés (pools à frais dynamiques) : 573
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 5490 ; cycles déclenchés par événement : 320 ; avance médiane sur le rafraîchissement multicall : 750 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,383.83 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 541 pools, 316 jetons, 19308 routes
- Par DEX : uniswap_v3 137, aerodrome 222, aerodrome_slipstream 136, pancakeswap_v3 30, uniswap_v2 13, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 198 (rejetés 2) → 603 jetons ; pools candidats 3822 (énumérés 360, par paires 0), mesurés 543, sous le plancher de 10000.0 $ : 2 → gardés 541 (max 1500) ; prix des hubs : {'USDC': 1.0, 'USDbC': 1.0, 'DAI': 1.0, 'WETH': 2383.836332, 'AERO': 0.803249, 'cbBTC': 81352.487956}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 156,260,578 | 2,383.832959 | 52955670 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,202,565 | 0.029291 | 52955670 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 13,470,924 | 91.140076 | 52955670 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| aerodrome | USDC/AERO | 3000 | 12,194,908 | 1.249570 | 52955670 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,245,760 | 0.029266 | 52955670 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,865,830 | 0.000012 | 52955670 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 8,931,782 | 0.029282 | 52955670 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/USDC | 500 | 8,638,305 | 2,380.866339 | 52955670 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,127,773 | 0.001661 | 52955670 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 330 | 6,800,964 | 0.000012 | 52955670 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 150 | 5,732,672 | 2,380.689170 | 52955670 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,367,158 | 0.029299 | 52955670 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | USDC/cbBTC | 400 | 5,272,141 | 0.000012 | 52955670 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,483,367 | 2,380.568145 | 52955670 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | WETH/USDC | 3000 | 4,284,606 | 2,385.505229 | 52955670 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,279,638 | 1.000001 | 52955670 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,958,161 | 34,374.696628 | 52955670 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | VIRTUAL/WETH | 10000 | 3,426,823 | 0.000274 | 52955670 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/USDT | 400 | 2,900,899 | 2,384.983177 | 52955670 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome_slipstream | WETH/VVV | 2772 | 2,550,606 | 91.116892 | 52955670 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,288,524 | 397.213251 | 52955670 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | WETH/AERO | 10000 | 2,282,762 | 2,981.809102 | 52955670 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | WETH/FAI | 10000 | 2,192,282 | 1,199,539.246897 | 52955670 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,916,325 | 0.000012 | 52955670 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,896,960 | 0.000000 | 52955670 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,789,124 | 0.018268 | 52955670 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,749,084 | 0.000012 | 52955670 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,641,407 | 1.525093 | 52955670 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | WETH/AERO | 3000 | 1,620,102 | 2,975.627639 | 52955670 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,456,662 | 0.823522 | 52955670 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,406,775 | 13,573.175081 | 52955670 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,365,267 | 0.004992 | 52955670 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,312,001 | 2,380.782716 | 52955670 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,288,140 | 0.000274 | 52955670 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | WETH/msETH (stable) | 500 | 1,279,464 | 2.359495 | 52955670 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | DRB/WETH | 10000 | 1,260,227 | 0.000000 | 52955670 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | USDC/SEND | 3000 | 1,229,636 | 64.267198 | 52955670 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,183,262 | 35,684,570.951739 | 52955670 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,174,123 | 16.268390 | 52955670 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | WETH/WELL | 10000 | 1,167,511 | 1,107,277.339786 | 52955670 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome | USDC/NOCK | 3000 | 1,165,288 | 46.215937 | 52955670 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,141,140 | 501,267.024733 | 52955670 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 1,087,739 | 0.000010 | 52955670 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | weETH_04c0/WETH | 500 | 1,085,694 | 1.105751 | 52955670 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome | WETH/EDEL | 7000 | 1,077,027 | 75,636.540411 | 52955670 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,059,410 | 21,256,860.378615 | 52955670 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,031,600 | 17.362377 | 52955670 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | WETH/cbBTC | 3000 | 1,009,499 | 0.029282 | 52955670 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,003,589 | 23.020941 | 52955670 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| uniswap_v3 | USDC/VVV | 3000 | 989,293 | 0.038258 | 52955670 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/MORPHO | 3000 | 956,266 | 1,055.539889 | 52955670 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/USDC | 10000 | 937,502 | 2,381.973244 | 52955670 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | uXRP/WETH | 3000 | 909,276 | 0.000543 | 52955670 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome | WETH/bsdETH | 100 | 886,577 | 0.916410 | 52955670 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 879,203 | 17.916817 | 52955670 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v2 | WETH/USDC | 3000 | 873,780 | 2,384.550362 | 52955670 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome | WETH/wstETH | 3000 | 807,640 | 0.803225 | 52955670 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| aerodrome | fBOMB/USDC | 10000 | 791,816 | 0.018537 | 52955670 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 786,670 | 0.651833 | 52955670 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| pancakeswap_v3 | QUID/USDC | 100 | 781,457 | 0.054678 | 52955670 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |

## Recherche d'opportunités
- Cycles : 727 ; routes examinées : 14036916 ; candidats optimisés : 53326 ; net attendu > 0 : 0 ; dernier cycle 205.3 ms
- Rejets (moteur) : {'spread_below_threshold': 13848893, 'liquidity_below_min': 133552, 'negative_expected_net': 53326, 'borrow_bound_too_small': 723, 'cycle_budget_exhausted': 344}
- Enregistrements de la session : 53326 ; net attendu > 0 : 0 ; simulés (eth_call de la vraie tx) : 0 (ok 0, échec 0) ; étiquettes ghost N+1 : 0/0 positives
- Décisions : {'REJECTED': 53326} ; motifs de rejet : {'negative_expected_net': 53326}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|

_Aucun candidat à net positif. Les 10 plus proches de la rentabilité (net attendu négatif) :_

| Bloc | Route | Montant | Brut | Frais flash | Gaz (dont L1) | Net attendu (€) | Marge (bps) |
|---:|---|---:|---:|---:|---:|---:|---:|
| 52955511 | WETH→[aerodrome]→USDC→[uniswap_v3]→WETH | 0.001838 WETH | 0.000001 WETH | 0.000000 WETH | 0.000002 WETH | -0.0024 | -6.03 |
| 52955511 | WETH→[aerodrome]→USDC→[uniswap_v3]→WETH | 0.001838 WETH | 0.000001 WETH | 0.000000 WETH | 0.000002 WETH | -0.0024 | -6.03 |
| 52955511 | USDC→[uniswap_v3]→WETH→[aerodrome]→USDC | 4.339074 USDC | 0.002394 USDC | 0.000000 USDC | 0.005039 USDC | -0.0024 | -6.10 |
| 52955511 | USDC→[uniswap_v3]→WETH→[aerodrome]→USDC | 4.339074 USDC | 0.002394 USDC | 0.000000 USDC | 0.005039 USDC | -0.0024 | -6.10 |
| 52955529 | WETH→[aerodrome]→USDC→[pancakeswap_v3]→WETH | 0.001777 WETH | 0.000001 WETH | 0.000000 WETH | 0.000002 WETH | -0.0025 | -6.37 |
| 52955529 | WETH→[aerodrome]→USDC→[pancakeswap_v3]→WETH | 0.001777 WETH | 0.000001 WETH | 0.000000 WETH | 0.000002 WETH | -0.0025 | -6.37 |
| 52955519 | WETH→[aerodrome]→USDC→[pancakeswap_v3]→WETH | 0.001777 WETH | 0.000001 WETH | 0.000000 WETH | 0.000002 WETH | -0.0025 | -6.38 |
| 52955519 | WETH→[aerodrome]→USDC→[pancakeswap_v3]→WETH | 0.001777 WETH | 0.000001 WETH | 0.000000 WETH | 0.000002 WETH | -0.0025 | -6.38 |
| 52955520 | WETH→[aerodrome]→USDC→[pancakeswap_v3]→WETH | 0.001777 WETH | 0.000001 WETH | 0.000000 WETH | 0.000002 WETH | -0.0025 | -6.38 |
| 52955520 | WETH→[aerodrome]→USDC→[pancakeswap_v3]→WETH | 0.001777 WETH | 0.000001 WETH | 0.000000 WETH | 0.000002 WETH | -0.0025 | -6.38 |

## Fiabilité et décision
- Observations ghost : 1928 ; taux observé 0.096 ; borne inférieure crédible (0.9) 0.088 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 8.8% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
