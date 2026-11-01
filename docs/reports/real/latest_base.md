# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-01T16:15:09+00:00 ; durée 3.03 min ; blocs 53380086 → 53380180 (91 vus)

## Connexion
- Requêtes RPC : 1081 ; erreurs : 0 ; latence p50/p95 : 251.2/1,643.7 ms
- Rafraîchissements d'état : 92 ; âge des données au dernier bloc : 2.1 s ; changements de frais LP observés (pools à frais dynamiques) : 83
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 1112 ; cycles déclenchés par événement : 95 ; avance médiane sur le rafraîchissement multicall : 421 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,264.23 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 500 pools, 289 jetons, 18734 routes
- Par DEX : uniswap_v3 140, aerodrome_slipstream 111, aerodrome 206, pancakeswap_v3 29, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 177 (rejetés 2) → 582 jetons ; pools candidats 3737 (énumérés 315, par paires 0), mesurés 503, sous le plancher de 10000.0 $ : 3 → gardés 500 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDbC': 1.0, 'USDC': 1.0, 'WETH': 2264.227713, 'cbBTC': 77906.671325, 'AERO': 0.64119}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 150,536,011 | 2,264.227773 | 53380180 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,165,575 | 0.029088 | 53380180 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,297,801 | 0.000013 | 53380180 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,156,845 | 0.029102 | 53380180 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 7,890,933 | 2,266.599946 | 53380180 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,859,869 | 98.053364 | 53380180 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,667,765 | 0.001589 | 53380180 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 5,691,300 | 1.559600 | 53380180 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,192,982 | 0.029100 | 53380180 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,098,550 | 0.998845 | 53380180 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome_slipstream | WETH/USDC | 684 | 4,052,797 | 2,267.437921 | 53380180 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,014,705 | 2,267.466343 | 53380180 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | WETH/KTA | 3000 | 3,551,908 | 38,031.550206 | 53380180 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,701,379 | 0.029087 | 53380180 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2700 | 2,410,238 | 98.149747 | 53380180 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | USDC/cbBTC | 400 | 2,179,261 | 0.000013 | 53380180 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome | WETH/FAI | 10000 | 2,084,819 | 1,195,839.173352 | 53380180 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | XDP/USDC | 100 | 1,771,981 | 0.018343 | 53380180 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,761,379 | 0.000000 | 53380180 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,638,737 | 0.000013 | 53380180 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,584,601 | 0.000013 | 53380180 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,558,725 | 422.606931 | 53380180 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,537,008 | 1.499750 | 53380180 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v2 | WETH/USDC | 3000 | 1,506,999 | 2,266.488924 | 53380180 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,457,051 | 0.826153 | 53380180 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,434,576 | 3,532.448856 | 53380180 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | WETH/USDC | 3000 | 1,408,478 | 2,271.222262 | 53380180 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,344,713 | 0.005257 | 53380180 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,330,071 | 2,266.497612 | 53380180 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,313,145 | 14,515.568378 | 53380180 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome_slipstream | USDC/cbBTC | 332 | 1,307,807 | 0.000013 | 53380180 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/SEND | 3000 | 1,169,550 | 71.040305 | 53380180 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,115,472 | 36,569,694.018981 | 53380180 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,073,574 | 509,395.710729 | 53380180 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,056,037 | 0.000000 | 53380180 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,014,734 | 22,273,804.776113 | 53380180 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | WETH/VVV | 10000 | 996,776 | 97.368537 | 53380180 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome_slipstream | USDC/VELVET | 100 | 994,025 | 19.278547 | 53380180 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | WETH/EDEL | 7000 | 971,573 | 82,907.205900 | 53380180 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | WETH/WELL | 10000 | 958,613 | 1,163,821.179723 | 53380180 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/MORPHO | 3000 | 950,765 | 994.110610 | 53380180 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | USDC/VVV | 3000 | 946,609 | 0.043293 | 53380180 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | USDC/NOCK | 3000 | 929,078 | 72.525208 | 53380180 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/USDC | 10000 | 923,207 | 2,252.785569 | 53380180 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome | WETH/AERO | 10000 | 873,809 | 3,514.646394 | 53380180 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | uXRP/WETH | 3000 | 863,865 | 0.000546 | 53380180 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | USDC/SAPIEN | 4515 | 839,942 | 19.372845 | 53380180 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 820,196 | 0.060506 | 53380180 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 767,231 | 0.801881 | 53380180 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| aerodrome | VIRTUAL/WETH | 10000 | 728,304 | 0.000261 | 53380180 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 727,893 | 0.595450 | 53380180 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 710,219 | 4,803,354.497062 | 53380180 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 693,942 | 0.000008 | 53380180 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v2 | WETH/NPC | 3000 | 688,268 | 136,514.255725 | 53380180 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| uniswap_v3 | TIG/USDC | 10000 | 678,281 | 0.577205 | 53380180 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | WETH/BRETT | 2117 | 667,170 | 513,959.405523 | 53380180 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome | WETH/msETH (stable) | 500 | 659,537 | 2.340198 | 53380180 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 612,151 | 0.092945 | 53380180 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| aerodrome | WETH/bsdETH | 100 | 607,582 | 0.916578 | 53380180 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| uniswap_v3 | FLOCK/USDC | 3000 | 583,670 | 0.040489 | 53380180 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |

## Recherche d'opportunités
- Cycles : 186 ; routes examinées : 3484524 ; candidats optimisés : 8609 ; net attendu > 0 : 12 ; dernier cycle 143.8 ms
- Rejets (moteur) : {'spread_below_threshold': 3425124, 'liquidity_below_min': 50233, 'negative_expected_net': 8597, 'unquotable': 372, 'borrow_bound_too_small': 186}
- Enregistrements de la session : 8609 ; net attendu > 0 : 12 ; simulés (eth_call de la vraie tx) : 0 (ok 0, échec 0) ; étiquettes ghost N+1 : 0/0 positives
- Décisions : {'REJECTED': 8609} ; motifs de rejet : {'below_safety_margin': 12, 'negative_expected_net': 8597, 'p_lower_below_threshold': 6, 'reliability_not_demonstrated': 6}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53380165 | cbBTC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.005986 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0129 €) | — | 0.30 | 0.138 (n=691) | REJECTED | below_safety_margin(18<119), p_lower_below_threshold(0.14<0.75) |
| 53380165 | cbBTC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.005986 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0129 €) | — | 0.30 | 0.138 (n=691) | REJECTED | below_safety_margin(18<119), p_lower_below_threshold(0.14<0.75) |
| 53380165 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH | 0.213075 WETH | 0.000009 WETH | 0.000000 WETH | 0.000003 WETH | 0.000006 WETH (0.0128 €) | — | 0.29 | 0.138 (n=691) | REJECTED | below_safety_margin(6141362778293<42615003529639), p_lower_below_threshold(0.14<0.75) |
| 53380165 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH | 0.213075 WETH | 0.000009 WETH | 0.000000 WETH | 0.000003 WETH | 0.000006 WETH (0.0128 €) | — | 0.29 | 0.138 (n=691) | REJECTED | below_safety_margin(6141362778293<42615003529639), p_lower_below_threshold(0.14<0.75) |
| 53380165 | USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 442.309141 USDC | 0.020468 USDC | 0.000000 USDC | 0.006804 USDC | 0.013664 USDC (0.0126 €) | — | 0.31 | 0.138 (n=691) | REJECTED | below_safety_margin(13664<88461), p_lower_below_threshold(0.14<0.75) |
| 53380165 | USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 442.309141 USDC | 0.020468 USDC | 0.000000 USDC | 0.006804 USDC | 0.013664 USDC (0.0126 €) | — | 0.31 | 0.138 (n=691) | REJECTED | below_safety_margin(13664<88461), p_lower_below_threshold(0.14<0.75) |
| 53380165 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.002625 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0050 €) | — | 0.27 | 0.000 (n=18) | REJECTED | below_safety_margin(7<52), reliability_not_demonstrated |
| 53380165 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.002625 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0050 €) | — | 0.27 | 0.000 (n=18) | REJECTED | below_safety_margin(7<52), reliability_not_demonstrated |
| 53380165 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 180.361513 USDC | 0.012087 USDC | 0.000000 USDC | 0.006804 USDC | 0.005283 USDC (0.0049 €) | — | 0.29 | 0.000 (n=18) | REJECTED | below_safety_margin(5283<36072), reliability_not_demonstrated |
| 53380165 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 180.361513 USDC | 0.012087 USDC | 0.000000 USDC | 0.006804 USDC | 0.005283 USDC (0.0049 €) | — | 0.29 | 0.000 (n=18) | REJECTED | below_safety_margin(5283<36072), reliability_not_demonstrated |
| 53380165 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.076896 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0048 €) | — | 0.30 | 0.000 (n=18) | REJECTED | below_safety_margin(2298315370719<15379137618091), reliability_not_demonstrated |
| 53380165 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.076896 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0048 €) | — | 0.30 | 0.000 (n=18) | REJECTED | below_safety_margin(2298315370719<15379137618091), reliability_not_demonstrated |

## Fiabilité et décision
- Observations ghost : 4131 ; taux observé 0.128 ; borne inférieure crédible (0.9) 0.121 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 12.1% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
