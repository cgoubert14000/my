# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-25T21:29:07+00:00 ; durée 3.0 min ; blocs 53087107 → 53087199 (90 vus)

## Connexion
- Requêtes RPC : 1151 ; erreurs : 0 ; latence p50/p95 : 117.3/1,524.5 ms
- Rafraîchissements d'état : 90 ; âge des données au dernier bloc : 4.16 s ; changements de frais LP observés (pools à frais dynamiques) : 122
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 950 ; cycles déclenchés par événement : 122 ; avance médiane sur le rafraîchissement multicall : 365 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,341.93 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 533 pools, 308 jetons, 19442 routes
- Par DEX : uniswap_v3 143, aerodrome 214, aerodrome_slipstream 129, pancakeswap_v3 31, uniswap_v2 13, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 192 (rejetés 2) → 597 jetons ; pools candidats 3802 (énumérés 342, par paires 0), mesurés 535, sous le plancher de 10000.0 $ : 2 → gardés 533 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'DAI': 1.0, 'USDC': 1.0, 'WETH': 2341.931042, 'cbBTC': 80341.676682, 'AERO': 0.683871}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 158,461,060 | 2,341.930774 | 53087198 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 17,506,409 | 0.029094 | 53087198 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,240,302 | 0.029142 | 53087198 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,599,082 | 0.000012 | 53087198 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome | WETH/VVV | 3000 | 8,956,980 | 92.658325 | 53087198 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/USDC | 500 | 8,437,870 | 2,339.700991 | 53087198 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | USDC/AERO | 3000 | 7,487,035 | 1.462265 | 53087198 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,022,585 | 0.001648 | 53087198 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | WETH/USDC | 150 | 5,496,696 | 2,340.277466 | 53087198 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,361,010 | 0.029102 | 53087198 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,459,317 | 2,340.457171 | 53087198 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,231,537 | 1.000002 | 53087198 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,834,076 | 34,923.126351 | 53087198 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/USDC | 3000 | 3,785,311 | 2,341.838692 | 53087198 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | WETH/cbBTC | 2510 | 3,231,988 | 0.029147 | 53087198 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | USDC/cbBTC | 424 | 2,525,833 | 0.000012 | 53087198 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome_slipstream | WETH/VVV | 2763 | 2,523,296 | 92.665329 | 53087198 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,217,516 | 410.149676 | 53087198 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | WETH/FAI | 10000 | 2,137,190 | 1,217,392.988104 | 53087198 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,898,750 | 0.000000 | 53087198 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,898,389 | 0.000012 | 53087198 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v3 | XDP/USDC | 100 | 1,790,825 | 0.018043 | 53087198 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | USDC/cbBTC | 338 | 1,720,205 | 0.000012 | 53087198 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,720,009 | 0.000012 | 53087198 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | VIRTUAL/WETH | 10000 | 1,572,128 | 0.000265 | 53087198 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,459,135 | 0.825585 | 53087198 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,453,220 | 1.698035 | 53087198 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,438,078 | 0.005542 | 53087198 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v3 | WETH/AERO | 3000 | 1,436,132 | 3,424.468882 | 53087198 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,371,885 | 14,085.957310 | 53087198 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,288,870 | 2,339.464122 | 53087198 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | WETH/AERO | 10000 | 1,257,775 | 3,400.687041 | 53087198 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,244,433 | 0.000267 | 53087198 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | USDC/SEND | 3000 | 1,221,956 | 65.077583 | 53087198 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,166,668 | 35,446,952.567842 | 53087198 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | DRB/WETH | 10000 | 1,163,630 | 0.000000 | 53087198 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | WETH/WELL | 10000 | 1,138,344 | 1,110,488.482374 | 53087198 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,125,567 | 495,996.911990 | 53087198 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | USDC/NOCK | 3000 | 1,093,759 | 52.357031 | 53087198 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome | WETH/EDEL | 7000 | 1,069,586 | 73,468.648899 | 53087198 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,036,810 | 17.129725 | 53087198 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,022,346 | 21,969,859.621726 | 53087198 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | USDC/VVV | 3000 | 972,837 | 0.039658 | 53087198 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/USDC | 10000 | 925,857 | 2,339.202029 | 53087198 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome | WETH/msETH (stable) | 500 | 917,368 | 2.311225 | 53087198 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | WETH/MORPHO | 3000 | 912,422 | 1,133.440813 | 53087198 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | uXRP/WETH | 3000 | 898,213 | 0.000551 | 53087198 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 890,592 | 17.088102 | 53087198 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| uniswap_v3 | WETH/VVV | 10000 | 880,278 | 91.982411 | 53087198 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 876,215 | 18.056487 | 53087198 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v2 | WETH/USDC | 3000 | 848,711 | 2,341.993973 | 53087198 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 806,284 | 0.000008 | 53087198 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | WETH/wstETH | 3000 | 792,943 | 0.803130 | 53087198 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| pancakeswap_v3 | QUID/USDC | 100 | 788,984 | 0.055761 | 53087198 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | weETH_04c0/WETH | 500 | 782,938 | 1.105853 | 53087198 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 746,924 | 0.623650 | 53087198 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 736,033 | 4,778,980.419635 | 53087198 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 719,602 | 0.649846 | 53087198 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/NPC | 3000 | 715,943 | 134,658.882654 | 53087198 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 700,390 | 496,007.629302 | 53087198 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |

## Recherche d'opportunités
- Cycles : 211 ; routes examinées : 4102262 ; candidats optimisés : 13001 ; net attendu > 0 : 0 ; dernier cycle 249.6 ms
- Rejets (moteur) : {'spread_below_threshold': 3981532, 'liquidity_below_min': 102814, 'negative_expected_net': 13001, 'unquotable': 4620, 'borrow_bound_too_small': 210}
- Enregistrements de la session : 13001 ; net attendu > 0 : 0 ; simulés (eth_call de la vraie tx) : 0 (ok 0, échec 0) ; étiquettes ghost N+1 : 0/0 positives
- Décisions : {'REJECTED': 13001} ; motifs de rejet : {'negative_expected_net': 13001}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|

_Aucun candidat à net positif. Les 10 plus proches de la rentabilité (net attendu négatif) :_

| Bloc | Route | Montant | Brut | Frais flash | Gaz (dont L1) | Net attendu (€) | Marge (bps) |
|---:|---|---:|---:|---:|---:|---:|---:|
| 53087117 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.005292 WETH | 0.000001 WETH | 0.000000 WETH | 0.000002 WETH | -0.0030 | -2.62 |
| 53087118 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.005292 WETH | 0.000001 WETH | 0.000000 WETH | 0.000002 WETH | -0.0030 | -2.62 |
| 53087117 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 11.947590 USDC | 0.002004 USDC | 0.000000 USDC | 0.005258 USDC | -0.0030 | -2.72 |
| 53087118 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 11.947590 USDC | 0.002004 USDC | 0.000000 USDC | 0.005258 USDC | -0.0030 | -2.72 |
| 53087177 | USDC→[aerodrome_slipstream]→EURC→[pancakeswap_v3]→USDC | 32.973564 USDC | 0.001858 USDC | 0.000000 USDC | 0.005258 USDC | -0.0031 | -1.03 |
| 53087178 | USDC→[aerodrome_slipstream]→EURC→[pancakeswap_v3]→USDC | 32.973564 USDC | 0.001858 USDC | 0.000000 USDC | 0.005258 USDC | -0.0031 | -1.03 |
| 53087117 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.004753 WETH | 0.000001 WETH | 0.000000 WETH | 0.000002 WETH | -0.0033 | -3.20 |
| 53087118 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.004753 WETH | 0.000001 WETH | 0.000000 WETH | 0.000002 WETH | -0.0033 | -3.20 |
| 53087117 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 10.957558 USDC | 0.001687 USDC | 0.000000 USDC | 0.005258 USDC | -0.0033 | -3.26 |
| 53087118 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 10.957558 USDC | 0.001687 USDC | 0.000000 USDC | 0.005258 USDC | -0.0033 | -3.26 |

## Fiabilité et décision
- Observations ghost : 2538 ; taux observé 0.091 ; borne inférieure crédible (0.9) 0.084 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 8.4% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
