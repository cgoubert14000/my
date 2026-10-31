# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-31T12:22:00+00:00 ; durée 9.17 min ; blocs 53329707 → 53329986 (276 vus)

## Connexion
- Requêtes RPC : 3239 ; erreurs : 0 ; latence p50/p95 : 197.6/1,184.2 ms
- Rafraîchissements d'état : 277 ; âge des données au dernier bloc : 1.08 s ; changements de frais LP observés (pools à frais dynamiques) : 247
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 1798 ; cycles déclenchés par événement : 267 ; avance médiane sur le rafraîchissement multicall : 444 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,242.80 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 500 pools, 290 jetons, 18658 routes
- Par DEX : uniswap_v3 137, aerodrome_slipstream 113, aerodrome 207, pancakeswap_v3 29, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 178 (rejetés 2) → 583 jetons ; pools candidats 3735 (énumérés 318, par paires 0), mesurés 503, sous le plancher de 10000.0 $ : 3 → gardés 500 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2242.796031, 'cbBTC': 77486.299825, 'AERO': 0.625959}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 150,253,437 | 2,242.796034 | 53329986 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,013,603 | 0.028983 | 53329986 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,291,137 | 0.000013 | 53329986 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,026,259 | 0.029054 | 53329986 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 7,860,975 | 2,245.945369 | 53329986 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,732,554 | 99.766432 | 53329986 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,683,388 | 0.001615 | 53329986 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 5,852,462 | 1.595454 | 53329986 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,294,651 | 0.028985 | 53329986 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,139,698 | 2,245.699399 | 53329986 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | WETH/USDC | 150 | 4,122,165 | 2,245.635810 | 53329986 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,069,017 | 1.000001 | 53329986 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,530,310 | 37,772.959803 | 53329986 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,681,851 | 0.029040 | 53329986 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2712 | 2,348,729 | 99.741871 | 53329986 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | WETH/FAI | 10000 | 2,058,244 | 1,203,801.785954 | 53329986 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 412 | 1,977,587 | 0.000013 | 53329986 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,752,970 | 0.000000 | 53329986 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,727,779 | 0.017566 | 53329986 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,681,488 | 422.148459 | 53329986 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,642,167 | 0.000013 | 53329986 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v2 | WETH/USDC | 3000 | 1,591,620 | 2,243.254526 | 53329986 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,584,900 | 0.000013 | 53329986 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,542,998 | 1.498770 | 53329986 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome | WETH/USDC | 3000 | 1,523,633 | 2,251.551444 | 53329986 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,456,812 | 0.826388 | 53329986 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | USDC/cbBTC | 334 | 1,414,831 | 0.000013 | 53329986 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | WETH/AERO | 3000 | 1,411,665 | 3,582.449797 | 53329986 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,354,119 | 2,245.820503 | 53329986 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,350,382 | 0.005320 | 53329986 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,303,811 | 14,556.225879 | 53329986 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | USDC/SEND | 3000 | 1,176,519 | 70.201199 | 53329986 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,114,102 | 35,683,183.061138 | 53329986 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,058,500 | 514,969.705658 | 53329986 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,028,979 | 21,341,044.339289 | 53329986 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | DRB/WETH | 10000 | 1,023,991 | 0.000000 | 53329986 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | WETH/EDEL | 7000 | 1,017,597 | 74,189.010957 | 53329986 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome_slipstream | USDC/VELVET | 100 | 994,070 | 19.275460 | 53329986 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/VVV | 10000 | 966,027 | 100.472564 | 53329986 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome | USDC/NOCK | 3000 | 958,800 | 68.097764 | 53329986 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | USDC/VVV | 3000 | 958,580 | 0.044406 | 53329986 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | WETH/WELL | 10000 | 931,016 | 1,213,317.287780 | 53329986 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/USDC | 10000 | 920,394 | 2,235.963257 | 53329986 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 914,519 | 1,035.416984 | 53329986 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome | WETH/AERO | 10000 | 864,838 | 3,591.809465 | 53329986 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | uXRP/WETH | 3000 | 860,863 | 0.000552 | 53329986 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 848,157 | 19.079951 | 53329986 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 827,466 | 0.061644 | 53329986 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 759,513 | 0.802842 | 53329986 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| aerodrome | VIRTUAL/WETH | 10000 | 724,847 | 0.000257 | 53329986 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 723,211 | 4,543,798.630911 | 53329986 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 709,913 | 0.579041 | 53329986 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 684,239 | 0.000008 | 53329986 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v2 | WETH/NPC | 3000 | 666,987 | 142,593.146684 | 53329986 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome | WETH/msETH (stable) | 500 | 660,112 | 2.334749 | 53329986 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | WETH/BRETT | 2102 | 657,238 | 517,464.340292 | 53329986 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | TIG/USDC | 10000 | 628,169 | 0.499036 | 53329986 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 616,388 | 0.093975 | 53329986 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| aerodrome | WETH/bsdETH | 100 | 602,540 | 0.916631 | 53329986 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome_slipstream | WETH/MORPHO | 2772 | 552,035 | 1,034.840536 | 53329986 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |

## Recherche d'opportunités
- Cycles : 542 ; routes examinées : 10112636 ; candidats optimisés : 35381 ; net attendu > 0 : 0 ; dernier cycle 106.3 ms
- Rejets (moteur) : {'spread_below_threshold': 10012263, 'liquidity_below_min': 63366, 'negative_expected_net': 35381, 'unquotable': 1084, 'borrow_bound_too_small': 542}
- Enregistrements de la session : 35381 ; net attendu > 0 : 0 ; simulés (eth_call de la vraie tx) : 0 (ok 0, échec 0) ; étiquettes ghost N+1 : 0/0 positives
- Décisions : {'REJECTED': 35381} ; motifs de rejet : {'negative_expected_net': 35381}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|

_Aucun candidat à net positif. Les 10 plus proches de la rentabilité (net attendu négatif) :_

| Bloc | Route | Montant | Brut | Frais flash | Gaz (dont L1) | Net attendu (€) | Marge (bps) |
|---:|---|---:|---:|---:|---:|---:|---:|
| 53329877 | USDC→[aerodrome_slipstream]→FLOCK→[uniswap_v3]→USDC | 2.540770 USDC | 0.001363 USDC | 0.000000 USDC | 0.005035 USDC | -0.0034 | -14.45 |
| 53329878 | USDC→[aerodrome_slipstream]→FLOCK→[uniswap_v3]→USDC | 2.540770 USDC | 0.001363 USDC | 0.000000 USDC | 0.005035 USDC | -0.0034 | -14.45 |
| 53329878 | USDC→[aerodrome_slipstream]→FLOCK→[uniswap_v3]→USDC | 2.540770 USDC | 0.001363 USDC | 0.000000 USDC | 0.005035 USDC | -0.0034 | -14.45 |
| 53329879 | USDC→[aerodrome_slipstream]→FLOCK→[uniswap_v3]→USDC | 2.540770 USDC | 0.001363 USDC | 0.000000 USDC | 0.005035 USDC | -0.0034 | -14.45 |
| 53329879 | USDC→[aerodrome_slipstream]→FLOCK→[uniswap_v3]→USDC | 2.540770 USDC | 0.001363 USDC | 0.000000 USDC | 0.005035 USDC | -0.0034 | -14.45 |
| 53329880 | USDC→[aerodrome_slipstream]→FLOCK→[uniswap_v3]→USDC | 2.540770 USDC | 0.001363 USDC | 0.000000 USDC | 0.005035 USDC | -0.0034 | -14.45 |
| 53329880 | USDC→[aerodrome_slipstream]→FLOCK→[uniswap_v3]→USDC | 2.540770 USDC | 0.001363 USDC | 0.000000 USDC | 0.005035 USDC | -0.0034 | -14.45 |
| 53329881 | USDC→[aerodrome_slipstream]→FLOCK→[uniswap_v3]→USDC | 2.540770 USDC | 0.001363 USDC | 0.000000 USDC | 0.005035 USDC | -0.0034 | -14.45 |
| 53329881 | USDC→[aerodrome_slipstream]→FLOCK→[uniswap_v3]→USDC | 2.540770 USDC | 0.001363 USDC | 0.000000 USDC | 0.005035 USDC | -0.0034 | -14.45 |
| 53329882 | USDC→[aerodrome_slipstream]→FLOCK→[uniswap_v3]→USDC | 2.540770 USDC | 0.001363 USDC | 0.000000 USDC | 0.005035 USDC | -0.0034 | -14.45 |

## Fiabilité et décision
- Observations ghost : 3945 ; taux observé 0.129 ; borne inférieure crédible (0.9) 0.123 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 12.3% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
