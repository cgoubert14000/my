# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-03T18:52:31+00:00 ; durée 3.05 min ; blocs 53471207 → 53471301 (92 vus)

## Connexion
- Requêtes RPC : 1101 ; erreurs : 0 ; latence p50/p95 : 217.9/1,610.7 ms
- Rafraîchissements d'état : 92 ; âge des données au dernier bloc : 2.36 s ; changements de frais LP observés (pools à frais dynamiques) : 64
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 750 ; cycles déclenchés par événement : 97 ; avance médiane sur le rafraîchissement multicall : 373 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,294.79 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 493 pools, 285 jetons, 19448 routes
- Par DEX : uniswap_v3 138, aerodrome_slipstream 107, aerodrome 205, pancakeswap_v3 29, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 174 (rejetés 2) → 579 jetons ; pools candidats 3706 (énumérés 309, par paires 0), mesurés 496, sous le plancher de 10000.0 $ : 3 → gardés 493 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'DAI': 1.0, 'USDC': 1.0, 'WETH': 2294.78828, 'cbBTC': 77607.185431, 'AERO': 0.633493}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 151,719,600 | 2,294.788241 | 53471301 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,425,195 | 0.029562 | 53471301 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,211,989 | 0.029576 | 53471301 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,027,242 | 0.000013 | 53471301 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 8,060,012 | 2,293.095275 | 53471301 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,763,355 | 102.412789 | 53471301 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,621,294 | 0.001575 | 53471301 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 5,413,214 | 1.578549 | 53471301 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,843,740 | 0.029556 | 53471301 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,168,488 | 2,292.595040 | 53471301 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,083,888 | 0.999904 | 53471301 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome_slipstream | WETH/USDC | 150 | 3,922,077 | 2,292.384605 | 53471301 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome | WETH/KTA | 3000 | 3,421,403 | 42,101.012572 | 53471301 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,715,585 | 0.029581 | 53471301 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 2,180,816 | 1,122,577.884914 | 53471301 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | WETH/VVV | 2748 | 2,121,375 | 102.380307 | 53471301 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | USDC/cbBTC | 484 | 1,814,377 | 0.000013 | 53471301 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | XDP/USDC | 100 | 1,736,748 | 0.017779 | 53471301 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,688,863 | 0.000000 | 53471301 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,641,556 | 0.000013 | 53471301 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,560,860 | 440.627176 | 53471301 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,554,793 | 1.429892 | 53471301 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,554,029 | 0.000013 | 53471301 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v2 | WETH/USDC | 3000 | 1,510,729 | 2,294.200903 | 53471301 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,454,614 | 0.821402 | 53471301 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,430,579 | 3,619.886354 | 53471301 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | WETH/USDC | 3000 | 1,345,937 | 2,296.506710 | 53471301 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,341,156 | 2,293.099210 | 53471301 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,318,205 | 0.005051 | 53471301 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,295,747 | 14,923.621238 | 53471301 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome_slipstream | USDC/cbBTC | 340 | 1,195,347 | 0.000013 | 53471301 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/SEND | 3000 | 1,158,695 | 72.377202 | 53471301 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,129,388 | 36,845,770.635172 | 53471301 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,063,283 | 543,733.996877 | 53471301 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,041,289 | 0.000000 | 53471301 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,037,614 | 21,972,681.122588 | 53471301 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/VELVET | 100 | 996,959 | 19.116882 | 53471301 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/MORPHO | 3000 | 964,270 | 1,033.801143 | 53471301 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome | WETH/EDEL | 7000 | 956,853 | 87,743.331997 | 53471301 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/VVV | 10000 | 951,823 | 103.127692 | 53471301 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome | USDC/NOCK | 3000 | 946,274 | 69.914222 | 53471301 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome | WETH/WELL | 10000 | 937,392 | 1,250,187.884762 | 53471301 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/USDC | 10000 | 930,056 | 2,282.122456 | 53471301 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | USDC/VVV | 3000 | 895,600 | 0.044625 | 53471301 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | uXRP/WETH | 3000 | 883,300 | 0.000556 | 53471301 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome | WETH/AERO | 10000 | 849,581 | 3,646.232124 | 53471301 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 821,696 | 20.040775 | 53471301 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 796,874 | 0.056900 | 53471301 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 778,913 | 0.799140 | 53471301 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 737,934 | 0.591317 | 53471301 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| aerodrome | VIRTUAL/WETH | 10000 | 729,216 | 0.000257 | 53471301 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 717,959 | 4,831,193.566937 | 53471301 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 675,360 | 0.000008 | 53471301 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v2 | WETH/NPC | 3000 | 670,068 | 148,073.214709 | 53471301 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| uniswap_v3 | TIG/USDC | 10000 | 664,892 | 0.555399 | 53471301 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome | WETH/msETH (stable) | 500 | 664,143 | 2.343097 | 53471301 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 653,574 | 547,962.886700 | 53471301 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome | WETH/bsdETH | 100 | 616,408 | 0.914716 | 53471301 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 586,180 | 0.086937 | 53471301 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| uniswap_v3 | FLOCK/USDC | 3000 | 567,188 | 0.038833 | 53471301 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |

## Recherche d'opportunités
- Cycles : 188 ; routes examinées : 3656224 ; candidats optimisés : 7401 ; net attendu > 0 : 0 ; dernier cycle 242.5 ms
- Rejets (moteur) : {'spread_below_threshold': 3605748, 'liquidity_below_min': 42511, 'negative_expected_net': 7401, 'unquotable': 376, 'borrow_bound_too_small': 188}
- Enregistrements de la session : 7401 ; net attendu > 0 : 0 ; simulés (eth_call de la vraie tx) : 0 (ok 0, échec 0) ; étiquettes ghost N+1 : 0/0 positives
- Décisions : {'REJECTED': 7401} ; motifs de rejet : {'negative_expected_net': 7401}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|

_Aucun candidat à net positif. Les 10 plus proches de la rentabilité (net attendu négatif) :_

| Bloc | Route | Montant | Brut | Frais flash | Gaz (dont L1) | Net attendu (€) | Marge (bps) |
|---:|---|---:|---:|---:|---:|---:|---:|
| 53471210 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 8.811382 USDC | 0.000235 USDC | 0.000000 USDC | 0.005154 USDC | -0.0045 | -5.58 |
| 53471211 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 8.811382 USDC | 0.000235 USDC | 0.000000 USDC | 0.005154 USDC | -0.0045 | -5.58 |
| 53471210 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.004022 WETH | 0.000000 WETH | 0.000000 WETH | 0.000002 WETH | -0.0045 | -5.33 |
| 53471211 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.004022 WETH | 0.000000 WETH | 0.000000 WETH | 0.000002 WETH | -0.0045 | -5.33 |
| 53471276 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.002774 WETH | 0.000000 WETH | 0.000000 WETH | 0.000002 WETH | -0.0047 | -7.94 |
| 53471276 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.002774 WETH | 0.000000 WETH | 0.000000 WETH | 0.000002 WETH | -0.0047 | -7.94 |
| 53471276 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 5.824101 USDC | 0.000097 USDC | 0.000000 USDC | 0.005154 USDC | -0.0047 | -8.68 |
| 53471276 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 5.824101 USDC | 0.000097 USDC | 0.000000 USDC | 0.005154 USDC | -0.0047 | -8.68 |
| 53471274 | WETH→[sushiswap_v3]→USDC→[uniswap_v3]→WETH | 0.002965 WETH | 0.000000 WETH | 0.000000 WETH | 0.000002 WETH | -0.0047 | -7.44 |
| 53471274 | WETH→[sushiswap_v3]→USDC→[uniswap_v3]→WETH | 0.002965 WETH | 0.000000 WETH | 0.000000 WETH | 0.000002 WETH | -0.0047 | -7.44 |

## Fiabilité et décision
- Observations ghost : 4905 ; taux observé 0.169 ; borne inférieure crédible (0.9) 0.162 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 16.2% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
