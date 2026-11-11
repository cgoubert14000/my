# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-11T06:55:37+00:00 ; durée 3.03 min ; blocs 55947872 → 55948772 (134 vus)

## Connexion
- Requêtes RPC : 1853 ; erreurs : 0 ; latence p50/p95 : 180.1/1,661.2 ms
- Rafraîchissements d'état : 134 ; âge des données au dernier bloc : 7.32 s ; changements de frais LP observés (pools à frais dynamiques) : 70
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 147 ; cycles déclenchés par événement : 49 ; avance médiane sur le rafraîchissement multicall : 190 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,057.49 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 460 pools, 267 jetons, 16590 routes
- Par DEX : uniswap_v3 134, aerodrome_slipstream 98, aerodrome 187, pancakeswap_v3 27, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 161 (rejetés 2) → 566 jetons ; pools candidats 3638 (énumérés 282, par paires 0), mesurés 462, sous le plancher de 10000.0 $ : 2 → gardés 460 (max 1500) ; prix des hubs : {'USDC': 1.0, 'USDbC': 1.0, 'DAI': 1.0, 'WETH': 2057.512263, 'cbBTC': 73519.133148, 'AERO': 0.539928}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 134,144,999 | 2,057.486752 | 55948772 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,398,265 | 0.027925 | 55948772 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 8,587,570 | 0.027977 | 55948772 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 8,334,774 | 0.000014 | 55948772 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 7,075,004 | 2,053.744332 | 55948772 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 6,746,298 | 108.370731 | 55948772 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,356,384 | 0.027929 | 55948772 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 4,257,237 | 1.852099 | 55948772 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,085,471 | 2,054.292613 | 55948772 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,871,468 | 1.000003 | 55948772 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,067,254 | 42,110.122897 | 55948772 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 150 | 2,924,237 | 2,054.369776 | 55948772 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2505 | 2,212,973 | 0.027978 | 55948772 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 1,956,239 | 1,121,311.176185 | 55948772 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,681,400 | 0.000014 | 55948772 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | USDC/cbBTC | 412 | 1,618,713 | 0.000014 | 55948772 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | XDP/USDC | 100 | 1,608,072 | 0.016180 | 55948772 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,553,169 | 0.000000 | 55948772 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,530,522 | 0.006621 | 55948772 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,462,280 | 0.824485 | 55948772 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,458,001 | 1.373191 | 55948772 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,424,974 | 0.000014 | 55948772 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,420,653 | 417.499250 | 55948772 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v2 | WETH/USDC | 3000 | 1,271,851 | 2,057.639260 | 55948772 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| uniswap_v3 | WETH/AERO | 3000 | 1,260,769 | 3,801.672984 | 55948772 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,231,118 | 14,942.261978 | 55948772 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/USDC | 3000 | 1,157,883 | 2,057.821211 | 55948772 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome | USDC/SEND | 3000 | 1,063,702 | 85.881444 | 55948772 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,048,984 | 33,068,570.309921 | 55948772 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,015,104 | 2,053.650288 | 55948772 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome_slipstream | USDC/VELVET | 100 | 958,783 | 21.472493 | 55948772 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/BRETT | 10000 | 942,823 | 557,994.244774 | 55948772 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | WETH/VVV | 10000 | 935,479 | 107.614239 | 55948772 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome_slipstream | USDC/cbBTC | 334 | 911,401 | 0.000014 | 55948772 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 910,355 | 0.001471 | 55948772 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| uniswap_v3 | WETH/TOSHI | 10000 | 903,026 | 23,147,877.094335 | 55948772 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | WETH/USDC | 10000 | 879,035 | 2,050.503253 | 55948772 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 878,696 | 1,028.229887 | 55948772 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | DRB/WETH | 10000 | 877,212 | 0.000000 | 55948772 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | USDC/VVV | 3000 | 866,901 | 0.052715 | 55948772 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| pancakeswap_v3 | QUID/USDC | 100 | 768,581 | 0.052730 | 55948772 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | USDC/NOCK | 3000 | 767,239 | 79.904459 | 55948772 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | USDC/SAPIEN | 4525 | 757,463 | 22.593201 | 55948772 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome | WETH/EDEL | 7000 | 746,832 | 115,710.896363 | 55948772 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | WETH/AERO | 10000 | 706,493 | 3,774.622536 | 55948772 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | WETH/wstETH | 3000 | 696,585 | 0.802938 | 55948772 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 672,589 | 0.529242 | 55948772 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 658,675 | 4,620,890.270627 | 55948772 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 627,088 | 0.495023 | 55948772 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/NPC | 3000 | 592,270 | 152,845.169653 | 55948772 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 583,729 | 0.000007 | 55948772 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | VIRTUAL/WETH | 10000 | 580,881 | 0.000259 | 55948772 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/BRETT | 2093 | 579,069 | 562,214.844656 | 55948772 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | FLOCK/USDC | 3000 | 558,925 | 0.037626 | 55948772 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 491,213 | 1,028.512588 | 55948772 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| uniswap_v3 | USDC/MORPHO | 10000 | 460,644 | 0.496640 | 55948772 | `0x2043B296fFC6b2d3bf4A3F3167d2Afb3B0FBdbEE` |
| pancakeswap_v3 | ELSA/USDC | 100 | 455,962 | 0.065349 | 55948772 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| aerodrome_slipstream | USDC/USDT | 8 | 455,063 | 1.001024 | 55948772 | `0xa41Bc0AFfbA7Fd420d186b84899d7ab2aC57fcD1` |
| aerodrome | cbBTC/EDGE | 7000 | 448,048 | 871,095.601785 | 55948772 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| uniswap_v3 | WETH/uSOL | 3000 | 439,295 | 25.043147 | 55948772 | `0xab04A352D4EC8d0F1812A4E5EBe7807Fa67acD48` |

## Recherche d'opportunités
- Cycles : 182 ; routes examinées : 3019380 ; candidats optimisés : 17690 ; net attendu > 0 : 0 ; dernier cycle 340.5 ms
- Rejets (moteur) : {'spread_below_threshold': 2928448, 'liquidity_below_min': 72760, 'negative_expected_net': 17690, 'borrow_bound_too_small': 362, 'cycle_budget_exhausted': 120}
- Enregistrements de la session : 17690 ; net attendu > 0 : 0 ; simulés (eth_call de la vraie tx) : 0 (ok 0, échec 0) ; étiquettes ghost N+1 : 0/0 positives
- Décisions : {'REJECTED': 17690} ; motifs de rejet : {'negative_expected_net': 17690}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|

_Aucun candidat à net positif. Les 10 plus proches de la rentabilité (net attendu négatif) :_

| Bloc | Route | Montant | Brut | Frais flash | Gaz (dont L1) | Net attendu (€) | Marge (bps) |
|---:|---|---:|---:|---:|---:|---:|---:|
| 55948327 | WETH→[aerodrome_slipstream]→AAVE→[pancakeswap_v3]→WETH | 0.005972 WETH | 0.000001 WETH | 0.000000 WETH | 0.000002 WETH | -0.0031 | -2.77 |
| 55948287 | WETH→[aerodrome_slipstream]→AAVE→[pancakeswap_v3]→WETH | 0.005972 WETH | 0.000001 WETH | 0.000000 WETH | 0.000002 WETH | -0.0031 | -2.77 |
| 55948287 | WETH→[aerodrome_slipstream]→AAVE→[pancakeswap_v3]→WETH | 0.005972 WETH | 0.000001 WETH | 0.000000 WETH | 0.000002 WETH | -0.0031 | -2.77 |
| 55948288 | WETH→[aerodrome_slipstream]→AAVE→[pancakeswap_v3]→WETH | 0.005972 WETH | 0.000001 WETH | 0.000000 WETH | 0.000002 WETH | -0.0031 | -2.77 |
| 55948289 | WETH→[aerodrome_slipstream]→AAVE→[pancakeswap_v3]→WETH | 0.005972 WETH | 0.000001 WETH | 0.000000 WETH | 0.000002 WETH | -0.0031 | -2.77 |
| 55948290 | WETH→[aerodrome_slipstream]→AAVE→[pancakeswap_v3]→WETH | 0.005972 WETH | 0.000001 WETH | 0.000000 WETH | 0.000002 WETH | -0.0031 | -2.77 |
| 55948291 | WETH→[aerodrome_slipstream]→AAVE→[pancakeswap_v3]→WETH | 0.005972 WETH | 0.000001 WETH | 0.000000 WETH | 0.000002 WETH | -0.0031 | -2.77 |
| 55948255 | WETH→[aerodrome_slipstream]→AAVE→[pancakeswap_v3]→WETH | 0.005972 WETH | 0.000001 WETH | 0.000000 WETH | 0.000002 WETH | -0.0031 | -2.77 |
| 55948327 | WETH→[aerodrome_slipstream]→AAVE→[pancakeswap_v3]→WETH | 0.005972 WETH | 0.000001 WETH | 0.000000 WETH | 0.000002 WETH | -0.0031 | -2.77 |
| 55948328 | WETH→[aerodrome_slipstream]→AAVE→[pancakeswap_v3]→WETH | 0.005972 WETH | 0.000001 WETH | 0.000000 WETH | 0.000002 WETH | -0.0031 | -2.77 |

## Fiabilité et décision
- Observations ghost : 7988 ; taux observé 0.211 ; borne inférieure crédible (0.9) 0.205 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 20.5% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
