# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-27T19:16:31+00:00 ; durée 58.18 min ; blocs 53167873 → 53169621 (1717 vus)

## Connexion
- Requêtes RPC : 20216 ; erreurs : 180 ; latence p50/p95 : 179.0/1,032.3 ms
- Rafraîchissements d'état : 1718 ; âge des données au dernier bloc : 1.34 s ; changements de frais LP observés (pools à frais dynamiques) : 2118
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 9054 ; cycles déclenchés par événement : 1126 ; avance médiane sur le rafraîchissement multicall : 546 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,346.62 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 519 pools, 301 jetons, 18846 routes
- Par DEX : uniswap_v3 145, aerodrome 211, aerodrome_slipstream 120, pancakeswap_v3 28, uniswap_v2 12, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 185 (rejetés 2) → 590 jetons ; pools candidats 3771 (énumérés 330, par paires 0), mesurés 521, sous le plancher de 10000.0 $ : 2 → gardés 519 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDbC': 1.0, 'USDC': 1.0, 'WETH': 2347.170972, 'cbBTC': 80539.356341, 'AERO': 0.69796}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 157,637,043 | 2,346.615717 | 53169621 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,624,265 | 0.029055 | 53169621 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,197,687 | 0.029106 | 53169621 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,641,975 | 0.000012 | 53169621 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome | WETH/VVV | 3000 | 8,651,933 | 90.087109 | 53169621 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/USDC | 500 | 8,431,581 | 2,340.797822 | 53169621 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,026,191 | 0.001639 | 53169621 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 6,998,439 | 1.430401 | 53169621 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,737,868 | 0.029043 | 53169621 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/USDC | 150 | 5,093,479 | 2,339.991293 | 53169621 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,489,922 | 2,339.946232 | 53169621 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,254,123 | 0.998745 | 53169621 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,734,743 | 36,952.936625 | 53169621 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2515 | 2,966,968 | 0.029114 | 53169621 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2736 | 2,581,851 | 90.112323 | 53169621 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | WETH/USDC | 3000 | 2,365,908 | 2,346.828339 | 53169621 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | USDC/cbBTC | 436 | 2,194,380 | 0.000012 | 53169621 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome | WETH/FAI | 10000 | 2,144,607 | 1,213,829.665615 | 53169621 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | XDP/USDC | 100 | 1,832,953 | 0.018768 | 53169621 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,818,006 | 0.000000 | 53169621 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,789,624 | 397.469247 | 53169621 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | USDC/cbBTC | 338 | 1,697,556 | 0.000012 | 53169621 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,688,947 | 0.000012 | 53169621 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,683,634 | 0.000012 | 53169621 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,526,382 | 0.005869 | 53169621 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,461,062 | 0.826538 | 53169621 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,457,611 | 3,353.829239 | 53169621 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,453,146 | 1.698043 | 53169621 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,393,149 | 13,669.962198 | 53169621 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,253,089 | 0.000268 | 53169621 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,249,864 | 2,340.815417 | 53169621 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | WETH/AERO | 10000 | 1,206,280 | 3,339.860965 | 53169621 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | USDC/SEND | 3000 | 1,201,201 | 67.345844 | 53169621 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome | VIRTUAL/WETH | 10000 | 1,185,783 | 0.000266 | 53169621 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | WETH/doginme | 10000 | 1,166,582 | 35,723,079.188239 | 53169621 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | WETH/WELL | 10000 | 1,163,709 | 1,066,281.134419 | 53169621 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | DRB/WETH | 10000 | 1,141,726 | 0.000000 | 53169621 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,112,407 | 507,629.468878 | 53169621 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | WETH/EDEL | 7000 | 1,078,607 | 72,326.481458 | 53169621 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,047,550 | 21,236,715.146711 | 53169621 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,042,126 | 16.896374 | 53169621 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | USDC/NOCK | 3000 | 1,039,232 | 57.962424 | 53169621 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | USDC/VVV | 3000 | 1,038,660 | 0.038471 | 53169621 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/USDC | 10000 | 944,055 | 2,331.655283 | 53169621 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 912,985 | 1,085.061399 | 53169621 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | uXRP/WETH | 3000 | 907,359 | 0.000560 | 53169621 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| uniswap_v3 | WETH/VVV | 10000 | 901,407 | 90.257385 | 53169621 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome | WETH/msETH (stable) | 500 | 886,197 | 2.312807 | 53169621 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 880,667 | 17.923897 | 53169621 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v2 | WETH/USDC | 3000 | 849,763 | 2,346.572706 | 53169621 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 837,969 | 17.692889 | 53169621 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 810,988 | 0.000009 | 53169621 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| pancakeswap_v3 | QUID/USDC | 100 | 802,310 | 0.057757 | 53169621 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 794,505 | 0.803179 | 53169621 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 757,892 | 4,525,709.531318 | 53169621 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 751,551 | 0.627265 | 53169621 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/NPC | 3000 | 701,782 | 140,739.756940 | 53169621 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | WETH/BRETT | 2159 | 693,196 | 505,336.827202 | 53169621 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | TIG/USDC | 10000 | 681,579 | 0.584963 | 53169621 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 674,508 | 0.108864 | 53169621 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |

## Recherche d'opportunités
- Cycles : 2843 ; routes examinées : 53579178 ; candidats optimisés : 159518 ; net attendu > 0 : 2 ; dernier cycle 129.8 ms
- Rejets (moteur) : {'spread_below_threshold': 52704340, 'liquidity_below_min': 690221, 'negative_expected_net': 159516, 'borrow_bound_too_small': 25099}
- Enregistrements de la session : 159518 ; net attendu > 0 : 2 ; simulés (eth_call de la vraie tx) : 0 (ok 0, échec 0) ; étiquettes ghost N+1 : 0/0 positives
- Décisions : {'REJECTED': 159518} ; motifs de rejet : {'below_safety_margin': 2, 'negative_expected_net': 159516, 'p_lower_below_threshold': 2}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53167952 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 19.270545 USDC | 0.008635 USDC | 0.000000 USDC | 0.005288 USDC | 0.003347 USDC (0.0031 €) | — | 1.74 | 0.020 (n=106) | REJECTED | below_safety_margin(3347<3854), p_lower_below_threshold(0.02<0.75) |
| 53167952 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 19.270545 USDC | 0.008635 USDC | 0.000000 USDC | 0.005288 USDC | 0.003347 USDC (0.0031 €) | — | 1.74 | 0.020 (n=106) | REJECTED | below_safety_margin(3347<3854), p_lower_below_threshold(0.02<0.75) |

## Fiabilité et décision
- Observations ghost : 2856 ; taux observé 0.090 ; borne inférieure crédible (0.9) 0.084 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 8.4% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
