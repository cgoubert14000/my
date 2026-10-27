# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-27T01:43:05+00:00 ; durée 15.31 min ; blocs 53137556 → 53138018 (451 vus)

## Connexion
- Requêtes RPC : 5726 ; erreurs : 0 ; latence p50/p95 : 289.1/1,573.0 ms
- Rafraîchissements d'état : 451 ; âge des données au dernier bloc : 3.78 s ; changements de frais LP observés (pools à frais dynamiques) : 827
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 5850 ; cycles déclenchés par événement : 401 ; avance médiane sur le rafraîchissement multicall : 604 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,322.40 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 530 pools, 305 jetons, 19446 routes
- Par DEX : uniswap_v3 143, aerodrome 212, aerodrome_slipstream 130, pancakeswap_v3 29, uniswap_v2 13, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 189 (rejetés 2) → 594 jetons ; pools candidats 3790 (énumérés 341, par paires 0), mesurés 533, sous le plancher de 10000.0 $ : 3 → gardés 530 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2322.398057, 'cbBTC': 80000.770706, 'AERO': 0.673032}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 156,387,803 | 2,322.397858 | 53138018 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,111,007 | 0.028992 | 53138018 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,126,374 | 0.028948 | 53138018 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,464,145 | 0.000012 | 53138018 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome | WETH/VVV | 3000 | 8,652,609 | 92.862000 | 53138018 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/USDC | 500 | 8,340,842 | 2,324.053551 | 53138018 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | USDC/AERO | 3000 | 7,018,451 | 1.484327 | 53138018 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,974,866 | 0.001642 | 53138018 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,382,027 | 0.029005 | 53138018 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/USDC | 150 | 5,254,308 | 2,324.828724 | 53138018 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,551,508 | 2,324.952210 | 53138018 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,216,037 | 0.999452 | 53138018 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,777,948 | 35,371.035999 | 53138018 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/USDC | 3000 | 3,363,950 | 2,321.625759 | 53138018 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 3,189,741 | 0.028964 | 53138018 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2715 | 2,505,939 | 92.836517 | 53138018 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | USDC/cbBTC | 460 | 2,452,405 | 0.000012 | 53138018 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome | WETH/FAI | 10000 | 2,120,247 | 1,216,380.983500 | 53138018 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,834,843 | 0.000000 | 53138018 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,832,450 | 0.018732 | 53138018 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,760,932 | 405.001592 | 53138018 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | USDC/cbBTC | 342 | 1,689,638 | 0.000012 | 53138018 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,678,613 | 0.000012 | 53138018 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,665,559 | 0.000012 | 53138018 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | VIRTUAL/WETH | 10000 | 1,555,047 | 0.000266 | 53138018 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,513,896 | 0.005885 | 53138018 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,460,925 | 0.826518 | 53138018 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,453,150 | 1.698035 | 53138018 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | WETH/AERO | 3000 | 1,429,181 | 3,442.901533 | 53138018 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,370,469 | 13,974.226796 | 53138018 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,242,301 | 2,323.999538 | 53138018 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,237,246 | 0.000266 | 53138018 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | USDC/SEND | 3000 | 1,217,284 | 65.578051 | 53138018 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome | WETH/AERO | 10000 | 1,207,086 | 3,444.389703 | 53138018 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | DRB/WETH | 10000 | 1,147,500 | 0.000000 | 53138018 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/doginme | 10000 | 1,141,492 | 36,863,515.097092 | 53138018 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | WETH/WELL | 10000 | 1,138,891 | 1,090,993.540534 | 53138018 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,108,414 | 498,031.875601 | 53138018 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | WETH/EDEL | 7000 | 1,070,061 | 72,179.423421 | 53138018 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,048,108 | 20,816,565.176003 | 53138018 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome | USDC/NOCK | 3000 | 1,039,242 | 57.961296 | 53138018 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,031,901 | 17.353773 | 53138018 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | USDC/VVV | 3000 | 1,001,810 | 0.039937 | 53138018 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/USDC | 10000 | 952,251 | 2,317.651270 | 53138018 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 920,050 | 1,080.856537 | 53138018 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome | WETH/msETH (stable) | 500 | 907,813 | 2.309154 | 53138018 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | uXRP/WETH | 3000 | 895,819 | 0.000558 | 53138018 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 879,695 | 17.950891 | 53138018 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v3 | WETH/VVV | 10000 | 872,662 | 92.391232 | 53138018 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 859,521 | 17.193154 | 53138018 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| uniswap_v2 | WETH/USDC | 3000 | 845,300 | 2,322.666004 | 53138018 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| pancakeswap_v3 | QUID/USDC | 100 | 796,997 | 0.056954 | 53138018 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 796,517 | 0.000008 | 53138018 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | WETH/wstETH | 3000 | 786,305 | 0.803179 | 53138018 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 742,235 | 0.617420 | 53138018 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 734,502 | 4,719,909.600110 | 53138018 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v2 | WETH/NPC | 3000 | 700,301 | 138,415.538833 | 53138018 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| uniswap_v3 | TIG/USDC | 10000 | 699,631 | 0.615511 | 53138018 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | WETH/BRETT | 2102 | 692,800 | 501,548.047880 | 53138018 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 674,417 | 0.108921 | 53138018 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |

## Recherche d'opportunités
- Cycles : 851 ; routes examinées : 16548546 ; candidats optimisés : 41812 ; net attendu > 0 : 7 ; dernier cycle 168.9 ms
- Rejets (moteur) : {'spread_below_threshold': 16257630, 'liquidity_below_min': 231233, 'negative_expected_net': 41805, 'unquotable': 17020, 'borrow_bound_too_small': 851}
- Enregistrements de la session : 41812 ; net attendu > 0 : 7 ; simulés (eth_call de la vraie tx) : 1 (ok 0, échec 1) ; étiquettes ghost N+1 : 0/1 positives
- Décisions : {'REJECTED': 41812} ; motifs de rejet : {'below_safety_margin': 6, 'negative_expected_net': 41805, 'p_lower_below_threshold': 5, 'reliability_not_demonstrated': 2, 'simulation_failed': 1}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53137626 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 34.617125 USDC | 0.017962 USDC | 0.000000 USDC | 0.005214 USDC | 0.012748 USDC (0.0117 €) | — | 3.68 | 0.002 (n=144) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 53137930 | USDC→[pancakeswap_v3]→PLAY→[aerodrome]→USDC | 7.365096 USDC | 0.005432 USDC | 0.000000 USDC | 0.005246 USDC | 0.000186 USDC (0.0002 €) | — | 0.25 | 0.001 (n=13) | REJECTED | below_safety_margin(186<1473), reliability_not_demonstrated |
| 53137930 | USDC→[pancakeswap_v3]→PLAY→[aerodrome]→USDC | 7.365096 USDC | 0.005432 USDC | 0.000000 USDC | 0.005246 USDC | 0.000186 USDC (0.0002 €) | — | 0.25 | 0.001 (n=13) | REJECTED | below_safety_margin(186<1473), reliability_not_demonstrated |
| 53137676 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.131309 WETH | 0.000002 WETH | 0.000000 WETH | 0.000002 WETH | 0.000000 WETH (0.0001 €) | — | 0.01 | 0.021 (n=102) | REJECTED | below_safety_margin(68032203442<26261817804490), p_lower_below_threshold(0.02<0.75) |
| 53137677 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.131309 WETH | 0.000002 WETH | 0.000000 WETH | 0.000002 WETH | 0.000000 WETH (0.0001 €) | — | 0.01 | 0.021 (n=102) | REJECTED | below_safety_margin(68032203442<26261817804490), p_lower_below_threshold(0.02<0.75) |
| 53137676 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 302.799137 USDC | 0.005371 USDC | 0.000000 USDC | 0.005214 USDC | 0.000157 USDC (0.0001 €) | — | 0.01 | 0.021 (n=102) | REJECTED | below_safety_margin(157<60559), p_lower_below_threshold(0.02<0.75) |
| 53137677 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 302.799137 USDC | 0.005371 USDC | 0.000000 USDC | 0.005214 USDC | 0.000157 USDC (0.0001 €) | — | 0.01 | 0.021 (n=102) | REJECTED | below_safety_margin(157<60559), p_lower_below_threshold(0.02<0.75) |

## Fiabilité et décision
- Observations ghost : 2776 ; taux observé 0.092 ; borne inférieure crédible (0.9) 0.085 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 8.5% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
