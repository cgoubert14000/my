# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-29T04:36:01+00:00 ; durée 36.7 min ; blocs 53228503 → 53229606 (1058 vus)

## Connexion
- Requêtes RPC : 12761 ; erreurs : 0 ; latence p50/p95 : 326.4/1,232.8 ms
- Rafraîchissements d'état : 1058 ; âge des données au dernier bloc : 2.32 s ; changements de frais LP observés (pools à frais dynamiques) : 1360
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 10429 ; cycles déclenchés par événement : 900 ; avance médiane sur le rafraîchissement multicall : 519 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,305.87 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 512 pools, 294 jetons, 18990 routes
- Par DEX : uniswap_v3 144, aerodrome_slipstream 116, aerodrome 210, pancakeswap_v3 28, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 182 (rejetés 2) → 587 jetons ; pools candidats 3756 (énumérés 325, par paires 0), mesurés 514, sous le plancher de 10000.0 $ : 2 → gardés 512 (max 1500) ; prix des hubs : {'USDC': 1.0, 'USDbC': 1.0, 'DAI': 1.0, 'WETH': 2304.739386, 'cbBTC': 79763.083067, 'AERO': 0.667567}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 156,539,351 | 2,305.874854 | 53229606 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,291,131 | 0.028926 | 53229606 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,677,305 | 0.000013 | 53229606 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,315,971 | 0.028854 | 53229606 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 8,207,719 | 2,311.723497 | 53229606 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 8,096,429 | 98.301941 | 53229606 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,920,421 | 0.001632 | 53229606 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 6,548,355 | 1.497977 | 53229606 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,689,440 | 0.028938 | 53229606 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/USDC | 150 | 4,743,077 | 2,312.056545 | 53229606 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,384,885 | 2,312.173621 | 53229606 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,196,587 | 0.998958 | 53229606 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,586,420 | 38,688.130815 | 53229606 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2510 | 2,892,275 | 0.028869 | 53229606 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2721 | 2,456,944 | 98.194732 | 53229606 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | USDC/cbBTC | 460 | 2,331,983 | 0.000013 | 53229606 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome | WETH/FAI | 10000 | 2,106,622 | 1,214,695.545645 | 53229606 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | XDP/USDC | 100 | 1,841,389 | 0.019131 | 53229606 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome | WETH/USDC | 3000 | 1,810,374 | 2,311.498451 | 53229606 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,755,159 | 403.354693 | 53229606 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,743,628 | 0.000000 | 53229606 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,702,966 | 0.000013 | 53229606 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,683,540 | 0.000013 | 53229606 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | USDC/cbBTC | 340 | 1,596,976 | 0.000013 | 53229606 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,514,127 | 1.588199 | 53229606 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,460,067 | 0.826762 | 53229606 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,413,011 | 3,455.919487 | 53229606 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,402,391 | 0.005410 | 53229606 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,365,322 | 13,956.371109 | 53229606 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,248,315 | 2,311.719329 | 53229606 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,218,077 | 0.000262 | 53229606 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | USDC/SEND | 3000 | 1,190,323 | 68.582376 | 53229606 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,136,063 | 36,690,852.155698 | 53229606 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | WETH/WELL | 10000 | 1,130,453 | 1,090,322.447538 | 53229606 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome | VIRTUAL/WETH | 10000 | 1,126,475 | 0.000263 | 53229606 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,098,582 | 500,808.040244 | 53229606 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,084,152 | 0.000000 | 53229606 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,055,155 | 21,379,851.748997 | 53229606 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome | WETH/EDEL | 7000 | 1,051,262 | 73,502.215451 | 53229606 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,048,084 | 16.641058 | 53229606 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | WETH/AERO | 10000 | 1,036,973 | 3,431.088863 | 53229606 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v2 | WETH/USDC | 3000 | 1,022,530 | 2,306.223915 | 53229606 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome | USDC/NOCK | 3000 | 1,021,198 | 60.028534 | 53229606 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | USDC/VVV | 3000 | 980,964 | 0.042522 | 53229606 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/VVV | 10000 | 980,947 | 98.999796 | 53229606 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/USDC | 10000 | 933,269 | 2,314.580420 | 53229606 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 912,213 | 1,060.369047 | 53229606 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | uXRP/WETH | 3000 | 889,242 | 0.000557 | 53229606 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 864,896 | 18.465102 | 53229606 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome | WETH/msETH (stable) | 500 | 861,115 | 2.326790 | 53229606 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| pancakeswap_v3 | QUID/USDC | 100 | 858,697 | 0.066832 | 53229606 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 820,335 | 17.798864 | 53229606 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | WETH/wstETH | 3000 | 780,811 | 0.802973 | 53229606 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 741,143 | 4,570,523.417413 | 53229606 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 732,394 | 0.603087 | 53229606 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 731,958 | 0.000008 | 53229606 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v2 | WETH/NPC | 3000 | 695,462 | 138,455.236307 | 53229606 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 685,268 | 502,961.853304 | 53229606 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | TIG/USDC | 10000 | 651,049 | 0.535144 | 53229606 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 632,907 | 0.098231 | 53229606 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |

## Recherche d'opportunités
- Cycles : 1957 ; routes examinées : 37163430 ; candidats optimisés : 118398 ; net attendu > 0 : 10 ; dernier cycle 115.1 ms
- Rejets (moteur) : {'spread_below_threshold': 36748985, 'liquidity_below_min': 293943, 'negative_expected_net': 118388, 'borrow_bound_too_small': 1955, 'cycle_budget_exhausted': 59}
- Enregistrements de la session : 118398 ; net attendu > 0 : 10 ; simulés (eth_call de la vraie tx) : 0 (ok 0, échec 0) ; étiquettes ghost N+1 : 0/0 positives
- Décisions : {'REJECTED': 118398} ; motifs de rejet : {'below_safety_margin': 10, 'negative_expected_net': 118388, 'p_lower_below_threshold': 4, 'reliability_not_demonstrated': 6}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53228815 | WETH→[aerodrome_slipstream]→cbETH→[pancakeswap_v3]→WETH | 0.093614 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0039 €) | — | 0.19 | 0.031 (n=113) | REJECTED | below_safety_margin(1820077115526<18722700193347), p_lower_below_threshold(0.03<0.75) |
| 53228815 | WETH→[aerodrome_slipstream]→cbETH→[pancakeswap_v3]→WETH | 0.093614 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0039 €) | — | 0.19 | 0.031 (n=113) | REJECTED | below_safety_margin(1820077115526<18722700193347), p_lower_below_threshold(0.03<0.75) |
| 53229511 | WETH→[uniswap_v3]→cbETH→[aerodrome_slipstream]→WETH | 0.026713 WETH | 0.000003 WETH | 0.000000 WETH | 0.000002 WETH | 0.000001 WETH (0.0021 €) | — | 0.36 | 0.010 (n=28) | REJECTED | below_safety_margin(974354844835<5342574407006), reliability_not_demonstrated |
| 53229511 | WETH→[uniswap_v3]→cbETH→[aerodrome_slipstream]→WETH | 0.026713 WETH | 0.000003 WETH | 0.000000 WETH | 0.000002 WETH | 0.000001 WETH (0.0021 €) | — | 0.36 | 0.010 (n=28) | REJECTED | below_safety_margin(974354844835<5342574407006), reliability_not_demonstrated |
| 53228815 | WETH→[aerodrome_slipstream]→cbETH→[uniswap_v3]→WETH | 0.092927 WETH | 0.000003 WETH | 0.000000 WETH | 0.000002 WETH | 0.000001 WETH (0.0018 €) | — | 0.09 | 0.010 (n=28) | REJECTED | below_safety_margin(848616227469<18585327985111), reliability_not_demonstrated |
| 53228815 | WETH→[aerodrome_slipstream]→cbETH→[uniswap_v3]→WETH | 0.092927 WETH | 0.000003 WETH | 0.000000 WETH | 0.000002 WETH | 0.000001 WETH (0.0018 €) | — | 0.09 | 0.010 (n=28) | REJECTED | below_safety_margin(848616227469<18585327985111), reliability_not_demonstrated |
| 53229511 | WETH→[pancakeswap_v3]→cbETH→[aerodrome_slipstream]→WETH | 0.024920 WETH | 0.000003 WETH | 0.000000 WETH | 0.000002 WETH | 0.000001 WETH (0.0013 €) | — | 0.24 | 0.031 (n=113) | REJECTED | below_safety_margin(595155918609<4983945387782), p_lower_below_threshold(0.03<0.75) |
| 53229511 | WETH→[pancakeswap_v3]→cbETH→[aerodrome_slipstream]→WETH | 0.024920 WETH | 0.000003 WETH | 0.000000 WETH | 0.000002 WETH | 0.000001 WETH (0.0013 €) | — | 0.24 | 0.031 (n=113) | REJECTED | below_safety_margin(595155918609<4983945387782), p_lower_below_threshold(0.03<0.75) |
| 53228702 | WETH→[aerodrome_slipstream]→cbETH→[uniswap_v3]→WETH | 0.070087 WETH | 0.000002 WETH | 0.000000 WETH | 0.000002 WETH | 0.000000 WETH (0.0002 €) | — | 0.01 | 0.010 (n=28) | REJECTED | below_safety_margin(73047279808<14017468998457), reliability_not_demonstrated |
| 53228702 | WETH→[aerodrome_slipstream]→cbETH→[uniswap_v3]→WETH | 0.070087 WETH | 0.000002 WETH | 0.000000 WETH | 0.000002 WETH | 0.000000 WETH (0.0002 €) | — | 0.01 | 0.010 (n=28) | REJECTED | below_safety_margin(73047279808<14017468998457), reliability_not_demonstrated |

## Fiabilité et décision
- Observations ghost : 3095 ; taux observé 0.100 ; borne inférieure crédible (0.9) 0.093 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 9.3% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
