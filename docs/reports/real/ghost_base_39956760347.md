# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-23T13:11:33+00:00 ; durée 12.1 min ; blocs 52985506 → 52985872 (350 vus)

## Connexion
- Requêtes RPC : 4392 ; erreurs : 0 ; latence p50/p95 : 232.5/1,440.7 ms
- Rafraîchissements d'état : 351 ; âge des données au dernier bloc : 2.13 s ; changements de frais LP observés (pools à frais dynamiques) : 503
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 5191 ; cycles déclenchés par événement : 569 ; avance médiane sur le rafraîchissement multicall : 558 ms
- Gaz : base fee 0.005022 gwei ; prix ETH (pool le plus profond) : 2,396.21 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 544 pools, 316 jetons, 19376 routes
- Par DEX : uniswap_v3 137, aerodrome 221, aerodrome_slipstream 137, pancakeswap_v3 32, uniswap_v2 13, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 200 (rejetés 2) → 605 jetons ; pools candidats 3880 (énumérés 358, par paires 0), mesurés 546, sous le plancher de 10000.0 $ : 2 → gardés 544 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDC': 1.0, 'USDbC': 1.0, 'WETH': 2396.209038, 'AERO': 0.783075, 'cbBTC': 81657.338706}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 156,688,356 | 2,396.209581 | 52985872 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,458,102 | 0.029384 | 52985872 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 13,315,978 | 92.574913 | 52985872 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| aerodrome | USDC/AERO | 3000 | 10,875,629 | 1.280176 | 52985872 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,326,030 | 0.029405 | 52985872 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,868,595 | 0.000012 | 52985872 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 8,893,604 | 0.029394 | 52985872 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/USDC | 500 | 8,681,819 | 2,396.380214 | 52985872 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,158,897 | 0.001669 | 52985872 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 336 | 6,351,514 | 0.000012 | 52985872 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 150 | 5,586,788 | 2,397.111060 | 52985872 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,444,628 | 0.029378 | 52985872 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | USDC/cbBTC | 448 | 5,092,592 | 0.000012 | 52985872 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,542,046 | 2,396.939165 | 52985872 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,291,712 | 0.999613 | 52985872 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/USDC | 3000 | 4,280,165 | 2,397.183800 | 52985872 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome | WETH/KTA | 3000 | 4,001,055 | 33,985.070581 | 52985872 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | VIRTUAL/WETH | 10000 | 3,402,136 | 0.000275 | 52985872 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/USDT | 418 | 2,902,266 | 2,400.550206 | 52985872 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome_slipstream | WETH/VVV | 2700 | 2,550,759 | 92.553136 | 52985872 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,310,270 | 391.463591 | 52985872 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | WETH/FAI | 10000 | 2,215,461 | 1,186,015.808845 | 52985872 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome | WETH/AERO | 10000 | 2,108,754 | 3,047.751616 | 52985872 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,988,435 | 0.000000 | 52985872 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,921,705 | 0.000012 | 52985872 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v3 | XDP/USDC | 100 | 1,760,543 | 0.017712 | 52985872 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,752,127 | 0.000012 | 52985872 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | WETH/AERO | 3000 | 1,603,821 | 3,069.325433 | 52985872 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,558,148 | 1.602726 | 52985872 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,458,271 | 0.823779 | 52985872 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,419,166 | 13,312.007063 | 52985872 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,384,031 | 0.005032 | 52985872 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome | WETH/msETH (stable) | 500 | 1,298,500 | 2.314608 | 52985872 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,295,689 | 0.000276 | 52985872 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,280,733 | 2,396.356860 | 52985872 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | DRB/WETH | 10000 | 1,255,933 | 0.000000 | 52985872 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | USDC/SEND | 3000 | 1,228,575 | 64.378255 | 52985872 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,182,161 | 36,279,696.618889 | 52985872 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,169,870 | 16.208467 | 52985872 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,165,463 | 482,603.731170 | 52985872 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | WETH/WELL | 10000 | 1,163,270 | 1,118,697.085973 | 52985872 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome | USDC/NOCK | 3000 | 1,143,612 | 47.904755 | 52985872 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | USDC/VVV | 3000 | 1,085,307 | 0.038614 | 52985872 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | WETH/EDEL | 7000 | 1,081,643 | 75,559.950068 | 52985872 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,075,424 | 20,901,603.416754 | 52985872 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,055,606 | 16.319038 | 52985872 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome_slipstream | AERO/cbBTC | 2700 | 1,023,611 | 0.000010 | 52985872 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,009,852 | 23.074963 | 52985872 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| uniswap_v3 | WETH/MORPHO | 3000 | 955,007 | 1,056.101527 | 52985872 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/USDC | 10000 | 938,610 | 2,390.321440 | 52985872 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | uXRP/WETH | 3000 | 916,074 | 0.000548 | 52985872 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 890,119 | 17.558099 | 52985872 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v2 | WETH/USDC | 3000 | 858,501 | 2,398.689477 | 52985872 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome | weETH_04c0/WETH | 500 | 835,449 | 1.105789 | 52985872 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome | WETH/wstETH | 3000 | 811,788 | 0.803225 | 52985872 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| pancakeswap_v3 | QUID/USDC | 100 | 799,928 | 0.057430 | 52985872 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 778,473 | 0.662109 | 52985872 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 776,811 | 4,489,707.569289 | 52985872 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v2 | WETH/NPC | 3000 | 733,777 | 134,114.117007 | 52985872 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| uniswap_v3 | TIG/USDC | 10000 | 731,477 | 0.670802 | 52985872 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |

## Recherche d'opportunités
- Cycles : 919 ; routes examinées : 17806544 ; candidats optimisés : 60276 ; net attendu > 0 : 14 ; dernier cycle 179.9 ms
- Rejets (moteur) : {'spread_below_threshold': 17490207, 'liquidity_below_min': 255087, 'negative_expected_net': 60262, 'borrow_bound_too_small': 919}
- Enregistrements de la session : 60273 ; net attendu > 0 : 14 ; simulés (eth_call de la vraie tx) : 0 (ok 0, échec 0) ; étiquettes ghost N+1 : 0/0 positives
- Décisions : {'REJECTED': 60273} ; motifs de rejet : {'below_safety_margin': 14, 'negative_expected_net': 60259, 'p_lower_below_threshold': 12, 'reliability_not_demonstrated': 2}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52985755 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC | 289.176647 USDC | 0.029169 USDC | 0.000000 USDC | 0.007213 USDC | 0.021956 USDC (0.0202 €) | — | 0.76 | 0.238 (n=118) | REJECTED | below_safety_margin(21956<57835), p_lower_below_threshold(0.24<0.75) |
| 52985755 | WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.121755 WETH | 0.000012 WETH | 0.000000 WETH | 0.000003 WETH | 0.000009 WETH (0.0202 €) | — | 0.75 | 0.238 (n=118) | REJECTED | below_safety_margin(9157928971941<24350924358503), p_lower_below_threshold(0.24<0.75) |
| 52985755 | USDC→[uniswap_v3]→WETH→[sushiswap_v3]→USDC | 48.036433 USDC | 0.006413 USDC | 0.000000 USDC | 0.005390 USDC | 0.001023 USDC (0.0009 €) | — | 0.21 | 0.020 (n=15) | REJECTED | below_safety_margin(1023<9607), reliability_not_demonstrated |
| 52985755 | WETH→[sushiswap_v3]→USDC→[uniswap_v3]→WETH | 0.020208 WETH | 0.000003 WETH | 0.000000 WETH | 0.000002 WETH | 0.000000 WETH (0.0009 €) | — | 0.21 | 0.020 (n=15) | REJECTED | below_safety_margin(426334042271<4041559444584), reliability_not_demonstrated |
| 52985755 | WETH→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.033637 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0009 €) | — | 0.12 | 0.116 (n=238) | REJECTED | below_safety_margin(412333434459<6727443415458), p_lower_below_threshold(0.12<0.75) |
| 52985755 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 64.092038 USDC | 0.008044 USDC | 0.000000 USDC | 0.007213 USDC | 0.000831 USDC (0.0008 €) | — | 0.13 | 0.116 (n=238) | REJECTED | below_safety_margin(831<12818), p_lower_below_threshold(0.12<0.75) |
| 52985755 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→cbBTC | 0.000834 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0007 €) | — | 0.12 | 0.116 (n=238) | REJECTED | below_safety_margin(1<16), p_lower_below_threshold(0.12<0.75) |
| 52985755 | cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→cbBTC | 0.000834 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0007 €) | — | 0.12 | 0.238 (n=118) | REJECTED | below_safety_margin(1<16), p_lower_below_threshold(0.24<0.75) |
| 52985755 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.001272 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0007 €) | — | 0.08 | 0.116 (n=238) | REJECTED | below_safety_margin(1<25), p_lower_below_threshold(0.12<0.75) |
| 52985755 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 137.798658 USDC | 0.007898 USDC | 0.000000 USDC | 0.007213 USDC | 0.000685 USDC (0.0006 €) | — | 0.05 | 0.116 (n=238) | REJECTED | below_safety_margin(685<27559), p_lower_below_threshold(0.12<0.75) |
| 52985755 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.056805 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0005 €) | — | 0.04 | 0.116 (n=238) | REJECTED | below_safety_margin(217032132791<11360901774582), p_lower_below_threshold(0.12<0.75) |
| 52985755 | WETH→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.031327 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0003 €) | — | 0.04 | 0.238 (n=118) | REJECTED | below_safety_margin(135955892089<6265393353516), p_lower_below_threshold(0.24<0.75) |
| 52985755 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→USDC | 72.493619 USDC | 0.007504 USDC | 0.000000 USDC | 0.007213 USDC | 0.000291 USDC (0.0003 €) | — | 0.04 | 0.238 (n=118) | REJECTED | below_safety_margin(291<14498), p_lower_below_threshold(0.24<0.75) |
| 52985755 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.045605 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0000 €) | — | 0.00 | 0.116 (n=238) | REJECTED | below_safety_margin(20037416366<9120909430393), p_lower_below_threshold(0.12<0.75) |

## Fiabilité et décision
- Observations ghost : 1984 ; taux observé 0.096 ; borne inférieure crédible (0.9) 0.088 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 8.8% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
