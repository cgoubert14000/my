# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-03T19:38:25+00:00 ; durée 48.95 min ; blocs 53471207 → 53472677 (1392 vus)

## Connexion
- Requêtes RPC : 16606 ; erreurs : 185 ; latence p50/p95 : 181.2/1,438.4 ms
- Rafraîchissements d'état : 1392 ; âge des données au dernier bloc : 3.51 s ; changements de frais LP observés (pools à frais dynamiques) : 1342
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 11304 ; cycles déclenchés par événement : 1244 ; avance médiane sur le rafraîchissement multicall : 395 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,291.80 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 493 pools, 285 jetons, 19448 routes
- Par DEX : uniswap_v3 138, aerodrome_slipstream 107, aerodrome 205, pancakeswap_v3 29, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 174 (rejetés 2) → 579 jetons ; pools candidats 3706 (énumérés 309, par paires 0), mesurés 496, sous le plancher de 10000.0 $ : 3 → gardés 493 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'DAI': 1.0, 'USDC': 1.0, 'WETH': 2294.78828, 'cbBTC': 77607.185431, 'AERO': 0.633493}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 151,611,016 | 2,291.796236 | 53472678 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,416,513 | 0.029516 | 53472678 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,208,285 | 0.029576 | 53472678 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,055,979 | 0.000013 | 53472678 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 8,052,547 | 2,286.197521 | 53472678 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,816,191 | 100.769595 | 53472678 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,617,679 | 0.001573 | 53472678 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 5,399,730 | 1.585137 | 53472678 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,840,506 | 0.029508 | 53472678 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,164,623 | 2,286.591701 | 53472678 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 202 | 4,084,881 | 0.999899 | 53472678 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome_slipstream | WETH/USDC | 150 | 3,905,541 | 2,286.795863 | 53472678 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome | WETH/KTA | 3000 | 3,416,263 | 42,117.772385 | 53472678 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,713,442 | 0.029575 | 53472678 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 2,177,472 | 1,123,093.642341 | 53472678 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | WETH/VVV | 2802 | 2,146,554 | 100.735554 | 53472678 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | USDC/cbBTC | 400 | 1,814,678 | 0.000013 | 53472678 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | XDP/USDC | 100 | 1,737,990 | 0.017797 | 53472678 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,686,656 | 0.000000 | 53472678 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,641,746 | 0.000013 | 53472678 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,559,280 | 440.204489 | 53472678 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,554,902 | 0.000013 | 53472678 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,554,793 | 1.429892 | 53472678 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v2 | WETH/USDC | 3000 | 1,509,745 | 2,290.956144 | 53472678 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,454,808 | 0.821842 | 53472678 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,426,372 | 3,622.110326 | 53472678 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,409,779 | 0.005477 | 53472678 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome | WETH/USDC | 3000 | 1,342,517 | 2,292.454507 | 53472678 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,339,940 | 2,286.068028 | 53472678 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,295,724 | 14,921.000817 | 53472678 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome_slipstream | USDC/cbBTC | 332 | 1,195,576 | 0.000013 | 53472678 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/SEND | 3000 | 1,158,640 | 72.384086 | 53472678 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,128,091 | 36,828,337.485245 | 53472678 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,061,581 | 544,194.018783 | 53472678 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,052,707 | 0.000000 | 53472678 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,036,874 | 21,950,664.012046 | 53472678 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/VELVET | 100 | 993,274 | 19.322154 | 53472678 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/MORPHO | 3000 | 964,310 | 1,031.556615 | 53472678 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/VVV | 10000 | 960,292 | 101.482317 | 53472678 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome | WETH/EDEL | 7000 | 951,071 | 88,581.964681 | 53472678 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | USDC/NOCK | 3000 | 945,816 | 69.981966 | 53472678 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome | WETH/WELL | 10000 | 936,169 | 1,250,189.203738 | 53472678 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/USDC | 10000 | 929,210 | 2,282.122456 | 53472678 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | USDC/VVV | 3000 | 905,331 | 0.044058 | 53472678 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | uXRP/WETH | 3000 | 880,654 | 0.000555 | 53472678 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome | WETH/AERO | 10000 | 847,258 | 3,646.232124 | 53472678 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 821,697 | 20.040742 | 53472678 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 796,075 | 0.056780 | 53472678 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 777,898 | 0.799140 | 53472678 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 737,135 | 0.590956 | 53472678 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| aerodrome | VIRTUAL/WETH | 10000 | 728,265 | 0.000257 | 53472678 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 718,761 | 4,807,875.544270 | 53472678 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 672,304 | 0.000008 | 53472678 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v2 | WETH/NPC | 3000 | 669,155 | 148,091.026221 | 53472678 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| uniswap_v3 | TIG/USDC | 10000 | 665,227 | 0.555930 | 53472678 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome | WETH/msETH (stable) | 500 | 663,277 | 2.343097 | 53472678 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 652,432 | 548,093.303127 | 53472678 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome | WETH/bsdETH | 100 | 615,605 | 0.914716 | 53472678 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 585,884 | 0.086872 | 53472678 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| uniswap_v3 | FLOCK/USDC | 3000 | 566,186 | 0.038727 | 53472678 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |

## Recherche d'opportunités
- Cycles : 2635 ; routes examinées : 51245480 ; candidats optimisés : 115668 ; net attendu > 0 : 14 ; dernier cycle 91.7 ms
- Rejets (moteur) : {'spread_below_threshold': 50632981, 'liquidity_below_min': 488893, 'negative_expected_net': 115654, 'unquotable': 5268, 'borrow_bound_too_small': 2634, 'cycle_budget_exhausted': 36}
- Enregistrements de la session : 115668 ; net attendu > 0 : 14 ; simulés (eth_call de la vraie tx) : 2 (ok 0, échec 2) ; étiquettes ghost N+1 : 0/2 positives
- Décisions : {'REJECTED': 115668} ; motifs de rejet : {'below_safety_margin': 12, 'negative_expected_net': 115654, 'p_lower_below_threshold': 12, 'reliability_not_demonstrated': 2, 'simulation_failed': 2}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53472395 | WETH→[aerodrome_slipstream]→CLANKER→[uniswap_v3]→WETH | 0.026252 WETH | 0.000056 WETH | 0.000000 WETH | 0.000002 WETH | 0.000054 WETH (0.1137 €) | — | 20.53 | 0.001 (n=11) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53472362 | WETH→[aerodrome_slipstream]→CLANKER→[uniswap_v3]→WETH | 0.020014 WETH | 0.000033 WETH | 0.000000 WETH | 0.000002 WETH | 0.000030 WETH (0.0642 €) | — | 15.21 | 0.001 (n=13) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53471700 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.168881 WETH | 0.000007 WETH | 0.000000 WETH | 0.000003 WETH | 0.000004 WETH (0.0086 €) | — | 0.24 | 0.185 (n=852) | REJECTED | below_safety_margin(4067722060797<33776255979005), p_lower_below_threshold(0.18<0.75) |
| 53471700 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.168881 WETH | 0.000007 WETH | 0.000000 WETH | 0.000003 WETH | 0.000004 WETH (0.0086 €) | — | 0.24 | 0.185 (n=852) | REJECTED | below_safety_margin(4067722060797<33776255979005), p_lower_below_threshold(0.18<0.75) |
| 53471700 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.004337 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0086 €) | — | 0.28 | 0.185 (n=852) | REJECTED | below_safety_margin(12<86), p_lower_below_threshold(0.18<0.75) |
| 53471700 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.004337 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0086 €) | — | 0.28 | 0.185 (n=852) | REJECTED | below_safety_margin(12<86), p_lower_below_threshold(0.18<0.75) |
| 53471700 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 363.859527 USDC | 0.016213 USDC | 0.000000 USDC | 0.006897 USDC | 0.009316 USDC (0.0086 €) | — | 0.26 | 0.185 (n=852) | REJECTED | below_safety_margin(9316<72771), p_lower_below_threshold(0.18<0.75) |
| 53471700 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 363.859527 USDC | 0.016213 USDC | 0.000000 USDC | 0.006897 USDC | 0.009316 USDC (0.0086 €) | — | 0.26 | 0.185 (n=852) | REJECTED | below_safety_margin(9316<72771), p_lower_below_threshold(0.18<0.75) |
| 53471700 | cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.002331 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0043 €) | — | 0.26 | 0.185 (n=852) | REJECTED | below_safety_margin(6<46), p_lower_below_threshold(0.18<0.75) |
| 53471700 | cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.002331 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0043 €) | — | 0.26 | 0.185 (n=852) | REJECTED | below_safety_margin(6<46), p_lower_below_threshold(0.18<0.75) |
| 53471700 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.090141 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0043 €) | — | 0.22 | 0.185 (n=852) | REJECTED | below_safety_margin(2021325061000<18028142434123), p_lower_below_threshold(0.18<0.75) |
| 53471700 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.090141 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0043 €) | — | 0.22 | 0.185 (n=852) | REJECTED | below_safety_margin(2021325061000<18028142434123), p_lower_below_threshold(0.18<0.75) |
| 53471700 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 224.474377 USDC | 0.011869 USDC | 0.000000 USDC | 0.007245 USDC | 0.004624 USDC (0.0043 €) | — | 0.21 | 0.185 (n=852) | REJECTED | below_safety_margin(4624<44894), p_lower_below_threshold(0.18<0.75) |
| 53471700 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 224.474377 USDC | 0.011869 USDC | 0.000000 USDC | 0.007245 USDC | 0.004624 USDC (0.0043 €) | — | 0.21 | 0.185 (n=852) | REJECTED | below_safety_margin(4624<44894), p_lower_below_threshold(0.18<0.75) |

## Fiabilité et décision
- Observations ghost : 4907 ; taux observé 0.169 ; borne inférieure crédible (0.9) 0.162 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 16.2% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
