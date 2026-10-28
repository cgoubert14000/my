# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-28T22:25:57+00:00 ; durée 3.05 min ; blocs 53218407 → 53218504 (91 vus)

## Connexion
- Requêtes RPC : 1119 ; erreurs : 0 ; latence p50/p95 : 262.4/1,701.1 ms
- Rafraîchissements d'état : 92 ; âge des données au dernier bloc : 2.11 s ; changements de frais LP observés (pools à frais dynamiques) : 122
- Flux d'événements (WebSocket Swap/Sync) : non connecté ; événements appliqués : 751 ; cycles déclenchés par événement : 79 ; avance médiane sur le rafraîchissement multicall : 796 ms
- Gaz : base fee 0.005009 gwei ; prix ETH (pool le plus profond) : 2,360.56 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 522 pools, 300 jetons, 19152 routes
- Par DEX : uniswap_v3 147, aerodrome_slipstream 122, aerodrome 210, pancakeswap_v3 28, uniswap_v2 12, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 183 (rejetés 2) → 588 jetons ; pools candidats 3758 (énumérés 331, par paires 0), mesurés 524, sous le plancher de 10000.0 $ : 2 → gardés 522 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDC': 1.0, 'USDbC': 1.0, 'WETH': 2360.669373, 'cbBTC': 81164.401586, 'AERO': 0.699093}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 158,684,093 | 2,360.562287 | 53218504 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,652,824 | 0.029035 | 53218504 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,912,846 | 0.000012 | 53218504 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,525,509 | 0.029058 | 53218504 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 8,401,485 | 2,354.513650 | 53218504 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 8,281,025 | 98.478253 | 53218504 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,093,772 | 0.001648 | 53218504 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 6,704,869 | 1.432930 | 53218504 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,853,668 | 0.029025 | 53218504 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/USDC | 639 | 4,842,810 | 2,353.818806 | 53218504 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,476,514 | 2,353.568602 | 53218504 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,281,353 | 0.998802 | 53218504 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,656,511 | 39,005.504744 | 53218504 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,960,025 | 0.029044 | 53218504 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2700 | 2,518,304 | 98.522621 | 53218504 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | WETH/FAI | 10000 | 2,154,362 | 1,217,202.137836 | 53218504 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 448 | 2,124,874 | 0.000012 | 53218504 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome | WETH/USDC | 3000 | 1,852,551 | 2,360.792696 | 53218504 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| uniswap_v3 | XDP/USDC | 100 | 1,827,270 | 0.018761 | 53218504 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,802,830 | 398.440940 | 53218504 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,778,749 | 0.000000 | 53218504 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,724,477 | 0.000012 | 53218504 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,699,901 | 0.000012 | 53218504 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | USDC/cbBTC | 340 | 1,614,984 | 0.000012 | 53218504 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,514,132 | 1.588195 | 53218504 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,502,523 | 0.005701 | 53218504 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v3 | WETH/AERO | 3000 | 1,463,129 | 3,372.586989 | 53218504 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,460,131 | 0.826609 | 53218504 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,400,865 | 13,721.768432 | 53218504 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,267,485 | 2,354.513437 | 53218504 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,259,861 | 0.000267 | 53218504 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | USDC/SEND | 3000 | 1,193,549 | 68.212112 | 53218504 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome | VIRTUAL/WETH | 10000 | 1,165,405 | 0.000266 | 53218504 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | WETH/doginme | 10000 | 1,163,852 | 36,610,175.590815 | 53218504 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | WETH/WELL | 10000 | 1,159,376 | 1,087,007.678986 | 53218504 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,134,996 | 488,528.908928 | 53218504 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,125,876 | 0.000000 | 53218504 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,087,280 | 21,137,377.203264 | 53218504 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome | WETH/EDEL | 7000 | 1,076,981 | 73,394.744213 | 53218504 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | WETH/AERO | 10000 | 1,075,020 | 3,350.985819 | 53218504 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,055,265 | 16.339970 | 53218504 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v2 | WETH/USDC | 3000 | 1,034,560 | 2,360.574315 | 53218504 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome | USDC/NOCK | 3000 | 1,003,813 | 62.125840 | 53218504 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/VVV | 10000 | 1,002,190 | 98.481892 | 53218504 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | USDC/VVV | 3000 | 997,187 | 0.041796 | 53218504 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/USDC | 10000 | 942,104 | 2,366.107395 | 53218504 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 937,385 | 1,052.507083 | 53218504 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | uXRP/WETH | 3000 | 913,409 | 0.000561 | 53218504 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | USDC/SAPIEN | 4515 | 883,802 | 17.827937 | 53218504 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome | WETH/msETH (stable) | 500 | 880,078 | 2.332538 | 53218504 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 856,973 | 17.411584 | 53218504 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| pancakeswap_v3 | QUID/USDC | 100 | 810,942 | 0.059079 | 53218504 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 799,329 | 0.802973 | 53218504 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 756,914 | 0.628854 | 53218504 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 756,853 | 0.000009 | 53218504 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 752,399 | 4,647,306.935779 | 53218504 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v2 | WETH/NPC | 3000 | 715,854 | 136,946.654296 | 53218504 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | WETH/BRETT | 2093 | 710,661 | 486,052.226634 | 53218504 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 671,318 | 0.107972 | 53218504 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| uniswap_v3 | TIG/USDC | 10000 | 644,794 | 0.525389 | 53218504 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |

## Recherche d'opportunités
- Cycles : 170 ; routes examinées : 3255840 ; candidats optimisés : 11294 ; net attendu > 0 : 0 ; dernier cycle 219.5 ms
- Rejets (moteur) : {'spread_below_threshold': 3217902, 'liquidity_below_min': 26465, 'negative_expected_net': 11294, 'borrow_bound_too_small': 170, 'cycle_budget_exhausted': 9}
- Enregistrements de la session : 11294 ; net attendu > 0 : 0 ; simulés (eth_call de la vraie tx) : 0 (ok 0, échec 0) ; étiquettes ghost N+1 : 0/0 positives
- Décisions : {'REJECTED': 11294} ; motifs de rejet : {'negative_expected_net': 11294}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|

_Aucun candidat à net positif. Les 10 plus proches de la rentabilité (net attendu négatif) :_

| Bloc | Route | Montant | Brut | Frais flash | Gaz (dont L1) | Net attendu (€) | Marge (bps) |
|---:|---|---:|---:|---:|---:|---:|---:|
| 53218429 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.003506 WETH | 0.000000 WETH | 0.000000 WETH | 0.000002 WETH | -0.0040 | -5.26 |
| 53218429 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.003506 WETH | 0.000000 WETH | 0.000000 WETH | 0.000002 WETH | -0.0040 | -5.26 |
| 53218429 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 8.361472 USDC | 0.000947 USDC | 0.000000 USDC | 0.005302 USDC | -0.0040 | -5.21 |
| 53218429 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 8.361472 USDC | 0.000947 USDC | 0.000000 USDC | 0.005302 USDC | -0.0040 | -5.21 |
| 53218426 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.003498 WETH | 0.000000 WETH | 0.000000 WETH | 0.000002 WETH | -0.0040 | -5.30 |
| 53218426 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.003498 WETH | 0.000000 WETH | 0.000000 WETH | 0.000002 WETH | -0.0040 | -5.30 |
| 53218426 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 7.944000 USDC | 0.000919 USDC | 0.000000 USDC | 0.005302 USDC | -0.0040 | -5.52 |
| 53218426 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 7.944000 USDC | 0.000919 USDC | 0.000000 USDC | 0.005302 USDC | -0.0040 | -5.52 |
| 53218417 | WETH→[aerodrome_slipstream]→VIRTUAL→[uniswap_v2]→WETH | 0.002352 WETH | 0.000000 WETH | 0.000000 WETH | 0.000002 WETH | -0.0041 | -7.94 |
| 53218418 | WETH→[aerodrome_slipstream]→VIRTUAL→[uniswap_v2]→WETH | 0.002352 WETH | 0.000000 WETH | 0.000000 WETH | 0.000002 WETH | -0.0041 | -7.94 |

## Fiabilité et décision
- Observations ghost : 3041 ; taux observé 0.097 ; borne inférieure crédible (0.9) 0.091 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 9.1% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
