# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-03T07:41:11+00:00 ; durée 6.1 min ; blocs 53450975 → 53451161 (178 vus)

## Connexion
- Requêtes RPC : 2105 ; erreurs : 0 ; latence p50/p95 : 240.5/1,413.8 ms
- Rafraîchissements d'état : 179 ; âge des données au dernier bloc : 2.19 s ; changements de frais LP observés (pools à frais dynamiques) : 146
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 1314 ; cycles déclenchés par événement : 206 ; avance médiane sur le rafraîchissement multicall : 537 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,251.33 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 491 pools, 284 jetons, 18380 routes
- Par DEX : uniswap_v3 137, aerodrome_slipstream 107, aerodrome 202, pancakeswap_v3 30, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 174 (rejetés 2) → 579 jetons ; pools candidats 3753 (énumérés 307, par paires 0), mesurés 494, sous le plancher de 10000.0 $ : 3 → gardés 491 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDC': 1.0, 'USDbC': 1.0, 'WETH': 2251.332101, 'cbBTC': 76780.974774, 'AERO': 0.596875}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 149,926,157 | 2,251.332131 | 53451161 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,131,673 | 0.029363 | 53451161 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,012,295 | 0.029314 | 53451161 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,000,295 | 0.000013 | 53451161 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 7,846,392 | 2,252.896212 | 53451161 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,508,059 | 106.080195 | 53451161 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,525,464 | 0.001568 | 53451161 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 5,325,512 | 1.675393 | 53451161 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,780,409 | 0.029357 | 53451161 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,147,643 | 2,252.689762 | 53451161 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,034,480 | 0.999819 | 53451161 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome_slipstream | WETH/USDC | 150 | 3,903,870 | 2,252.306137 | 53451161 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome | WETH/KTA | 3000 | 3,470,258 | 39,388.684552 | 53451161 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,682,627 | 0.029323 | 53451161 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 2,148,442 | 1,113,271.032218 | 53451161 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 424 | 2,027,870 | 0.000013 | 53451161 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome_slipstream | WETH/VVV | 2748 | 1,951,983 | 106.104054 | 53451161 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| uniswap_v3 | XDP/USDC | 100 | 1,763,138 | 0.018240 | 53451161 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,658,122 | 0.000000 | 53451161 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,626,427 | 0.000013 | 53451161 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,555,208 | 1.436224 | 53451161 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,538,871 | 0.000013 | 53451161 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,526,358 | 445.147270 | 53451161 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v2 | WETH/USDC | 3000 | 1,496,275 | 2,251.491291 | 53451161 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,453,013 | 0.822541 | 53451161 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,375,121 | 3,769.099474 | 53451161 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | WETH/USDC | 3000 | 1,333,429 | 2,251.791836 | 53451161 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,310,866 | 2,252.885338 | 53451161 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,270,212 | 15,147.971544 | 53451161 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,265,275 | 0.004898 | 53451161 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/cbBTC | 334 | 1,256,045 | 0.000013 | 53451161 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/SEND | 3000 | 1,164,539 | 71.652617 | 53451161 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,097,882 | 37,831,159.724088 | 53451161 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,044,087 | 542,341.914671 | 53451161 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,007,534 | 0.000000 | 53451161 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,000,667 | 22,613,085.553156 | 53451161 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/VELVET | 100 | 977,829 | 20.229707 | 53451161 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | WETH/EDEL | 7000 | 954,961 | 84,786.522974 | 53451161 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/USDC | 10000 | 923,713 | 2,257.234778 | 53451161 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome | WETH/WELL | 10000 | 914,468 | 1,264,370.737318 | 53451161 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/VVV | 10000 | 902,724 | 105.334284 | 53451161 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 901,568 | 1,059.582033 | 53451161 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome | USDC/NOCK | 3000 | 883,681 | 80.169020 | 53451161 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | uXRP/WETH | 3000 | 865,429 | 0.000553 | 53451161 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| uniswap_v3 | USDC/VVV | 3000 | 853,649 | 0.047086 | 53451161 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | WETH/AERO | 10000 | 820,325 | 3,742.526106 | 53451161 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 807,516 | 20.556904 | 53451161 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 782,886 | 0.054822 | 53451161 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 764,240 | 0.798978 | 53451161 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 721,574 | 0.574892 | 53451161 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| aerodrome | VIRTUAL/WETH | 10000 | 715,542 | 0.000257 | 53451161 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 709,679 | 4,758,725.965736 | 53451161 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v2 | WETH/NPC | 3000 | 660,113 | 146,837.328098 | 53451161 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| uniswap_v3 | TIG/USDC | 10000 | 659,972 | 0.547712 | 53451161 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome | WETH/msETH (stable) | 500 | 652,532 | 2.337947 | 53451161 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 648,406 | 0.000008 | 53451161 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 642,025 | 546,414.042214 | 53451161 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome | WETH/bsdETH | 100 | 604,769 | 0.914615 | 53451161 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 582,337 | 0.086115 | 53451161 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| uniswap_v3 | FLOCK/USDC | 3000 | 546,411 | 0.036726 | 53451161 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |

## Recherche d'opportunités
- Cycles : 384 ; routes examinées : 7057920 ; candidats optimisés : 18619 ; net attendu > 0 : 7 ; dernier cycle 50.8 ms
- Rejets (moteur) : {'spread_below_threshold': 6972034, 'liquidity_below_min': 66115, 'negative_expected_net': 18612, 'unquotable': 768, 'borrow_bound_too_small': 384}
- Enregistrements de la session : 18619 ; net attendu > 0 : 7 ; simulés (eth_call de la vraie tx) : 6 (ok 2, échec 4) ; étiquettes ghost N+1 : 0/3 positives
- Décisions : {'REJECTED': 18619} ; motifs de rejet : {'below_safety_margin': 1, 'negative_expected_net': 18612, 'p_lower_below_threshold': 7, 'simulation_failed': 4}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53450999 | USDC→[pancakeswap_v3]→ICNT→[uniswap_v3]→USDC | 45.243399 USDC | 0.030301 USDC | 0.000000 USDC | 0.005055 USDC | 0.025246 USDC (0.0232 €) | — | 5.58 | 0.033 (n=225) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.03<0.75) |
| 53451015 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 40.521701 USDC | 0.024603 USDC | 0.000000 USDC | 0.005056 USDC | 0.019547 USDC (0.0180 €) | — | 4.82 | 0.033 (n=227) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.03<0.75) |
| 53451017 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 40.521701 USDC | 0.024603 USDC | 0.000000 USDC | 0.005056 USDC | 0.019547 USDC (0.0180 €) | — | 4.82 | 0.033 (n=227) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.03<0.75) |
| 53450998 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 38.473082 USDC | 0.021834 USDC | 0.000000 USDC | 0.005055 USDC | 0.016779 USDC (0.0154 €) | 0.016779 USDC | 4.36 | 0.033 (n=225) | REJECTED | p_lower_below_threshold(0.03<0.75) |
| 53450998 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 38.473082 USDC | 0.021834 USDC | 0.000000 USDC | 0.005055 USDC | 0.016779 USDC (0.0154 €) | 0.016779 USDC | 4.36 | 0.033 (n=225) | REJECTED | p_lower_below_threshold(0.03<0.75) |
| 53451105 | USDC→[pancakeswap_v3]→ICNT→[uniswap_v3]→USDC | 30.663600 USDC | 0.014283 USDC | 0.000000 USDC | 0.005054 USDC | 0.009229 USDC (0.0085 €) | — | 3.01 | 0.033 (n=227) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.03<0.75) |
| 53451104 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 19.151185 USDC | 0.005575 USDC | 0.000000 USDC | 0.005054 USDC | 0.000521 USDC (0.0005 €) | — | 0.27 | 0.036 (n=184) | REJECTED | below_safety_margin(521<3830), p_lower_below_threshold(0.04<0.75) |

## Fiabilité et décision
- Observations ghost : 4802 ; taux observé 0.170 ; borne inférieure crédible (0.9) 0.163 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 16.3% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
