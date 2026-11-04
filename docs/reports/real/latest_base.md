# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-04T11:45:56+00:00 ; durée 3.0 min ; blocs 53501612 → 53501703 (90 vus)

## Connexion
- Requêtes RPC : 1129 ; erreurs : 0 ; latence p50/p95 : 186.7/1,234.7 ms
- Rafraîchissements d'état : 90 ; âge des données au dernier bloc : 5.65 s ; changements de frais LP observés (pools à frais dynamiques) : 98
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 1063 ; cycles déclenchés par événement : 160 ; avance médiane sur le rafraîchissement multicall : 565 ms
- Gaz : base fee 0.005006 gwei ; prix ETH (pool le plus profond) : 2,327.58 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 495 pools, 284 jetons, 19384 routes
- Par DEX : uniswap_v3 142, aerodrome_slipstream 106, aerodrome 204, pancakeswap_v3 29, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 174 (rejetés 2) → 579 jetons ; pools candidats 3706 (énumérés 308, par paires 0), mesurés 498, sous le plancher de 10000.0 $ : 3 → gardés 495 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDC': 1.0, 'USDbC': 1.0, 'WETH': 2327.57512, 'cbBTC': 78571.031441, 'AERO': 0.644724}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 152,352,943 | 2,327.579485 | 53501702 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,974,096 | 0.029682 | 53501702 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,362,070 | 0.029608 | 53501702 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,172,403 | 0.000013 | 53501702 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 8,147,736 | 2,333.042104 | 53501702 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 8,110,307 | 96.420361 | 53501702 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,664,404 | 0.001564 | 53501702 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 5,418,750 | 1.551052 | 53501702 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,910,275 | 0.029694 | 53501702 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,221,972 | 2,333.972433 | 53501702 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,125,463 | 0.999894 | 53501702 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome_slipstream | WETH/USDC | 654 | 3,899,350 | 2,333.853496 | 53501702 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome | WETH/KTA | 3000 | 3,514,738 | 41,042.973959 | 53501702 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,681,504 | 0.029622 | 53501703 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2703 | 2,228,134 | 96.413329 | 53501702 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | WETH/FAI | 10000 | 2,182,303 | 1,153,315.868669 | 53501702 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 400 | 1,826,071 | 0.000013 | 53501702 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | XDP/USDC | 100 | 1,744,539 | 0.017923 | 53501703 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,670,662 | 0.000000 | 53501702 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,639,272 | 0.006444 | 53501702 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,631,243 | 0.000013 | 53501703 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,590,269 | 434.342320 | 53501702 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,554,244 | 0.000013 | 53501702 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,552,810 | 1.433011 | 53501702 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | WETH/AERO | 3000 | 1,456,947 | 3,615.617373 | 53501702 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,454,396 | 0.818931 | 53501702 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,380,554 | 2,333.112980 | 53501703 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | WETH/USDC | 3000 | 1,352,132 | 2,331.658908 | 53501702 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| uniswap_v2 | WETH/USDC | 3000 | 1,351,530 | 2,327.265615 | 53501702 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,319,507 | 14,620.579281 | 53501702 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | USDC/SEND | 3000 | 1,158,306 | 72.425825 | 53501702 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,141,812 | 37,192,037.297593 | 53501702 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,071,125 | 551,635.897113 | 53501702 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,069,180 | 0.000000 | 53501702 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,045,703 | 22,207,069.108539 | 53501702 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | WETH/VVV | 10000 | 1,031,049 | 96.789805 | 53501702 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | USDC/VVV | 3000 | 997,170 | 0.041327 | 53501702 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome_slipstream | USDC/VELVET | 100 | 997,122 | 19.108575 | 53501703 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/MORPHO | 3000 | 977,985 | 1,040.967326 | 53501702 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome_slipstream | USDC/cbBTC | 332 | 949,787 | 0.000013 | 53501703 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | WETH/WELL | 10000 | 943,860 | 1,268,565.070221 | 53501702 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome | USDC/NOCK | 3000 | 935,617 | 71.516051 | 53501702 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/USDC | 10000 | 934,249 | 2,311.141733 | 53501702 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome | WETH/EDEL | 7000 | 932,942 | 94,956.263689 | 53501702 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | uXRP/WETH | 3000 | 893,118 | 0.000551 | 53501702 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome | WETH/AERO | 10000 | 861,063 | 3,632.791343 | 53501702 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 828,673 | 19.799017 | 53501702 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 797,719 | 0.057025 | 53501702 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 790,043 | 0.799140 | 53501702 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 740,601 | 0.593926 | 53501702 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| aerodrome | VIRTUAL/WETH | 10000 | 735,352 | 0.000254 | 53501702 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 718,301 | 4,965,945.251736 | 53501702 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v2 | WETH/NPC | 3000 | 688,281 | 144,424.914996 | 53501702 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 684,471 | 0.000008 | 53501702 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 657,973 | 550,428.918626 | 53501702 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | TIG/USDC | 10000 | 656,250 | 0.541523 | 53501702 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome | WETH/msETH (stable) | 500 | 647,694 | 2.483100 | 53501702 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome | WETH/bsdETH | 100 | 625,519 | 0.913833 | 53501702 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 612,347 | 0.092860 | 53501702 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| uniswap_v3 | FLOCK/USDC | 3000 | 573,918 | 0.039498 | 53501702 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |

## Recherche d'opportunités
- Cycles : 249 ; routes examinées : 4826616 ; candidats optimisés : 23829 ; net attendu > 0 : 12 ; dernier cycle 410.9 ms
- Rejets (moteur) : {'spread_below_threshold': 4731928, 'liquidity_below_min': 70610, 'negative_expected_net': 23817, 'borrow_bound_too_small': 249}
- Enregistrements de la session : 23829 ; net attendu > 0 : 12 ; simulés (eth_call de la vraie tx) : 1 (ok 0, échec 1) ; étiquettes ghost N+1 : 0/1 positives
- Décisions : {'REJECTED': 23829} ; motifs de rejet : {'below_safety_margin': 11, 'negative_expected_net': 23817, 'p_lower_below_threshold': 12, 'simulation_failed': 1}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53501641 | USDC→[pancakeswap_v3]→ICNT→[uniswap_v3]→USDC | 95.999795 USDC | 0.132980 USDC | 0.000000 USDC | 0.005238 USDC | 0.127742 USDC (0.1175 €) | — | 13.31 | 0.000 (n=80) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 53501630 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 70.325640 USDC | 0.019659 USDC | 0.000000 USDC | 0.007008 USDC | 0.012651 USDC (0.0116 €) | — | 1.80 | 0.183 (n=886) | REJECTED | below_safety_margin(12651<14065), p_lower_below_threshold(0.18<0.75) |
| 53501630 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.000877 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0115 €) | — | 1.82 | 0.183 (n=886) | REJECTED | below_safety_margin(16<17), p_lower_below_threshold(0.18<0.75) |
| 53501630 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.000877 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0115 €) | — | 1.82 | 0.183 (n=886) | REJECTED | below_safety_margin(16<17), p_lower_below_threshold(0.18<0.75) |
| 53501630 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 70.230403 USDC | 0.019055 USDC | 0.000000 USDC | 0.007008 USDC | 0.012047 USDC (0.0111 €) | — | 1.72 | 0.183 (n=886) | REJECTED | below_safety_margin(12047<14046), p_lower_below_threshold(0.18<0.75) |
| 53501629 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.000479 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0014 €) | — | 0.42 | 0.183 (n=886) | REJECTED | below_safety_margin(2<9), p_lower_below_threshold(0.18<0.75) |
| 53501629 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.000479 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0014 €) | — | 0.42 | 0.183 (n=886) | REJECTED | below_safety_margin(2<9), p_lower_below_threshold(0.18<0.75) |
| 53501629 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 51.463073 USDC | 0.008134 USDC | 0.000000 USDC | 0.007008 USDC | 0.001126 USDC (0.0010 €) | — | 0.22 | 0.183 (n=886) | REJECTED | below_safety_margin(1126<10292), p_lower_below_threshold(0.18<0.75) |
| 53501629 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 51.463073 USDC | 0.008134 USDC | 0.000000 USDC | 0.007008 USDC | 0.001126 USDC (0.0010 €) | — | 0.22 | 0.183 (n=886) | REJECTED | below_safety_margin(1126<10292), p_lower_below_threshold(0.18<0.75) |
| 53501659 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 61.651231 USDC | 0.008337 USDC | 0.000000 USDC | 0.007364 USDC | 0.000973 USDC (0.0009 €) | — | 0.16 | 0.183 (n=886) | REJECTED | below_safety_margin(973<12330), p_lower_below_threshold(0.18<0.75) |
| 53501659 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.000879 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0007 €) | — | 0.11 | 0.183 (n=886) | REJECTED | below_safety_margin(1<17), p_lower_below_threshold(0.18<0.75) |
| 53501630 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→USDC | 45.195363 USDC | 0.007051 USDC | 0.000000 USDC | 0.007008 USDC | 0.000043 USDC (0.0000 €) | — | 0.01 | 0.253 (n=354) | REJECTED | below_safety_margin(43<9039), p_lower_below_threshold(0.25<0.75) |

## Fiabilité et décision
- Observations ghost : 5073 ; taux observé 0.168 ; borne inférieure crédible (0.9) 0.161 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 16.1% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
