# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-24T07:11:13+00:00 ; durée 82.94 min ; blocs 53015772 → 53018262 (2488 vus)

## Connexion
- Requêtes RPC : 30803 ; erreurs : 3 ; latence p50/p95 : 200.0/656.8 ms
- Rafraîchissements d'état : 2488 ; âge des données au dernier bloc : 2.43 s ; changements de frais LP observés (pools à frais dynamiques) : 1884
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 22115 ; cycles déclenchés par événement : 2963 ; avance médiane sur le rafraîchissement multicall : 317 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,379.18 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 540 pools, 312 jetons, 19252 routes
- Par DEX : uniswap_v3 140, aerodrome 217, aerodrome_slipstream 135, pancakeswap_v3 31, uniswap_v2 13, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 196 (rejetés 2) → 601 jetons ; pools candidats 3859 (énumérés 351, par paires 0), mesurés 542, sous le plancher de 10000.0 $ : 2 → gardés 540 (max 1500) ; prix des hubs : {'USDC': 1.0, 'USDbC': 1.0, 'DAI': 1.0, 'WETH': 2380.141625, 'AERO': 0.727873, 'cbBTC': 80675.114522}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 156,182,135 | 2,379.183123 | 53018261 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 17,080,604 | 0.029448 | 53018261 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 12,403,219 | 96.532058 | 53018261 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,184,718 | 0.029387 | 53018261 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| aerodrome | USDC/AERO | 3000 | 9,752,722 | 1.377060 | 53018261 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,552,977 | 0.000012 | 53018261 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 8,636,250 | 2,376.647656 | 53018261 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 8,554,536 | 0.029400 | 53018261 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,058,813 | 0.001653 | 53018261 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 342 | 6,309,573 | 0.000012 | 53018261 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 150 | 5,505,472 | 2,376.828561 | 53018262 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,452,645 | 0.029441 | 53018261 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | USDC/cbBTC | 448 | 4,869,658 | 0.000012 | 53018261 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,497,634 | 2,376.951037 | 53018262 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,252,561 | 0.999263 | 53018261 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/USDC | 3000 | 4,100,216 | 2,376.148825 | 53018261 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome | WETH/KTA | 3000 | 3,968,940 | 34,028.409706 | 53018261 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | VIRTUAL/WETH | 10000 | 3,336,811 | 0.000271 | 53018261 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/USDT | 424 | 2,793,827 | 2,380.914216 | 53018261 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome_slipstream | WETH/VVV | 2700 | 2,536,957 | 96.573260 | 53018261 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,266,847 | 405.468360 | 53018261 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | WETH/FAI | 10000 | 2,131,357 | 1,263,317.112174 | 53018261 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome | WETH/AERO | 10000 | 2,001,652 | 3,273.352375 | 53018261 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,933,898 | 0.000000 | 53018261 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,913,277 | 0.000012 | 53018261 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v3 | XDP/USDC | 100 | 1,760,490 | 0.017996 | 53018261 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,740,680 | 0.000012 | 53018261 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,549,717 | 1.610679 | 53018261 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | WETH/AERO | 3000 | 1,492,345 | 3,272.370016 | 53018261 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,459,688 | 0.824979 | 53018261 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,389,358 | 13,758.127866 | 53018261 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,384,454 | 0.005139 | 53018261 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,319,880 | 2,376.692853 | 53018261 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,278,653 | 0.000269 | 53018261 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | WETH/msETH (stable) | 500 | 1,242,502 | 2.308433 | 53018261 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome | USDC/SEND | 3000 | 1,225,295 | 64.723347 | 53018261 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | DRB/WETH | 10000 | 1,199,308 | 0.000000 | 53018261 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/doginme | 10000 | 1,183,826 | 35,516,134.488001 | 53018261 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | WETH/WELL | 10000 | 1,154,652 | 1,118,523.028960 | 53018261 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,140,554 | 492,039.665164 | 53018261 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | USDC/NOCK | 3000 | 1,133,744 | 48.728923 | 53018261 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,116,212 | 16.610573 | 53018261 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | WETH/EDEL | 7000 | 1,084,189 | 73,835.111216 | 53018261 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,053,347 | 21,405,557.900989 | 53018261 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | USDC/VVV | 3000 | 1,046,487 | 0.040635 | 53018261 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,035,446 | 17.188912 | 53018261 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 972,052 | 23.248331 | 53018261 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| uniswap_v3 | WETH/MORPHO | 3000 | 941,817 | 1,069.521226 | 53018261 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | uXRP/WETH | 3000 | 902,894 | 0.000540 | 53018261 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| pancakeswap_v3 | QUID/USDC | 100 | 899,590 | 0.074122 | 53018261 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 885,407 | 17.731511 | 53018261 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 871,805 | 0.000009 | 53018261 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v2 | WETH/USDC | 3000 | 855,361 | 2,379.406394 | 53018261 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome | weETH_04c0/WETH | 500 | 818,843 | 1.105904 | 53018261 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome | WETH/wstETH | 3000 | 805,616 | 0.803010 | 53018261 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | WETH/USDC | 10000 | 789,653 | 2,373.719186 | 53018261 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/VVV | 10000 | 783,646 | 96.498774 | 53018261 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 768,176 | 0.639862 | 53018261 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 759,073 | 4,635,817.962834 | 53018261 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v2 | WETH/NPC | 3000 | 730,652 | 133,369.876928 | 53018261 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |

## Recherche d'opportunités
- Cycles : 5450 ; routes examinées : 104923400 ; candidats optimisés : 367058 ; net attendu > 0 : 9 ; dernier cycle 112.9 ms
- Rejets (moteur) : {'spread_below_threshold': 103070325, 'liquidity_below_min': 1480567, 'negative_expected_net': 367049, 'borrow_bound_too_small': 5450}
- Enregistrements de la session : 367058 ; net attendu > 0 : 9 ; simulés (eth_call de la vraie tx) : 8 (ok 6, échec 2) ; étiquettes ghost N+1 : 0/4 positives
- Décisions : {'REJECTED': 367058} ; motifs de rejet : {'below_safety_margin': 1, 'negative_expected_net': 367049, 'p_lower_below_threshold': 4, 'reliability_not_demonstrated': 5, 'simulation_failed': 2}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53015828 | USDC→[pancakeswap_v3]→PLAY→[aerodrome_slipstream]→USDC | 30.757704 USDC | 0.021524 USDC | 0.000000 USDC | 0.005347 USDC | 0.016177 USDC (0.0149 €) | — | 5.26 | 0.003 (n=111) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 53015828 | USDC→[pancakeswap_v3]→PLAY→[aerodrome]→USDC | 13.708061 USDC | 0.018663 USDC | 0.000000 USDC | 0.005018 USDC | 0.013645 USDC (0.0126 €) | — | 9.95 | 0.001 (n=10) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53018116 | USDC→[pancakeswap_v3]→PLAY→[aerodrome]→USDC | 10.213386 USDC | 0.010336 USDC | 0.000000 USDC | 0.005014 USDC | 0.005322 USDC (0.0049 €) | 0.005322 USDC | 5.21 | 0.025 (n=12) | REJECTED | reliability_not_demonstrated |
| 53018116 | USDC→[pancakeswap_v3]→PLAY→[aerodrome]→USDC | 10.213386 USDC | 0.010336 USDC | 0.000000 USDC | 0.005014 USDC | 0.005322 USDC (0.0049 €) | 0.005322 USDC | 5.21 | 0.025 (n=12) | REJECTED | reliability_not_demonstrated |
| 53018111 | USDC→[pancakeswap_v3]→PLAY→[aerodrome_slipstream]→USDC | 20.381325 USDC | 0.009483 USDC | 0.000000 USDC | 0.005342 USDC | 0.004141 USDC (0.0038 €) | 0.004141 USDC | 2.03 | 0.019 (n=77) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 53018111 | USDC→[pancakeswap_v3]→PLAY→[aerodrome_slipstream]→USDC | 20.381325 USDC | 0.009483 USDC | 0.000000 USDC | 0.005342 USDC | 0.004141 USDC (0.0038 €) | 0.004141 USDC | 2.03 | 0.019 (n=77) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 53018111 | USDC→[pancakeswap_v3]→PLAY→[aerodrome]→USDC | 9.361975 USDC | 0.008739 USDC | 0.000000 USDC | 0.005014 USDC | 0.003725 USDC (0.0034 €) | 0.003725 USDC | 3.98 | 0.027 (n=11) | REJECTED | reliability_not_demonstrated |
| 53018111 | USDC→[pancakeswap_v3]→PLAY→[aerodrome]→USDC | 9.361975 USDC | 0.008739 USDC | 0.000000 USDC | 0.005014 USDC | 0.003725 USDC (0.0034 €) | 0.003725 USDC | 3.98 | 0.027 (n=11) | REJECTED | reliability_not_demonstrated |
| 53018106 | USDC→[pancakeswap_v3]→PLAY→[aerodrome_slipstream]→USDC | 15.174717 USDC | 0.005384 USDC | 0.000000 USDC | 0.005342 USDC | 0.000042 USDC (0.0000 €) | — | 0.03 | 0.019 (n=77) | REJECTED | below_safety_margin(42<3034), p_lower_below_threshold(0.02<0.75) |

## Fiabilité et décision
- Observations ghost : 2097 ; taux observé 0.098 ; borne inférieure crédible (0.9) 0.090 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 9.0% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
