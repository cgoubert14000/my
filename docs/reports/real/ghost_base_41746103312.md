# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-04T00:57:06+00:00 ; durée 27.57 min ; blocs 53481408 → 53482237 (816 vus)

## Connexion
- Requêtes RPC : 8734 ; erreurs : 10 ; latence p50/p95 : 245.0/1,557.6 ms
- Rafraîchissements d'état : 816 ; âge des données au dernier bloc : 5.47 s ; changements de frais LP observés (pools à frais dynamiques) : 1722
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 102 ; cycles déclenchés par événement : 14 ; avance médiane sur le rafraîchissement multicall : 714 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,265.06 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 490 pools, 282 jetons, 19430 routes
- Par DEX : uniswap_v3 139, aerodrome_slipstream 105, aerodrome 203, pancakeswap_v3 29, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 172 (rejetés 2) → 577 jetons ; pools candidats 3703 (énumérés 305, par paires 0), mesurés 493, sous le plancher de 10000.0 $ : 3 → gardés 490 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2264.542979, 'cbBTC': 77119.048638, 'AERO': 0.629628}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 149,963,482 | 2,265.060254 | 53482238 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,604,486 | 0.029450 | 53482238 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,112,380 | 0.029422 | 53482238 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,021,901 | 0.000013 | 53482238 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 7,992,889 | 2,270.819765 | 53482238 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,698,910 | 101.329322 | 53482238 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,544,449 | 0.001567 | 53482238 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 5,393,851 | 1.587876 | 53482238 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,784,680 | 0.029458 | 53482238 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,189,849 | 2,271.516946 | 53482238 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,046,227 | 0.999909 | 53482238 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome_slipstream | WETH/USDC | 150 | 3,843,400 | 2,271.337966 | 53482238 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome | WETH/KTA | 3000 | 3,408,692 | 41,323.772870 | 53482238 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,660,169 | 0.029409 | 53482238 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 2,140,278 | 1,135,502.765144 | 53482238 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | WETH/VVV | 2700 | 2,111,465 | 101.323247 | 53482238 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | USDC/cbBTC | 556 | 1,803,193 | 0.000013 | 53482238 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | XDP/USDC | 100 | 1,730,094 | 0.017669 | 53482238 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,662,370 | 0.000000 | 53482238 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,644,623 | 0.006702 | 53482238 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,608,916 | 0.000013 | 53482238 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,554,793 | 1.429892 | 53482238 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,546,245 | 0.000013 | 53482238 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,542,253 | 439.171920 | 53482238 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v2 | WETH/USDC | 3000 | 1,500,994 | 2,264.961868 | 53482238 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,454,819 | 0.821830 | 53482238 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,416,729 | 3,599.344948 | 53482238 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,343,515 | 2,270.736089 | 53482238 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | WETH/USDC | 3000 | 1,334,662 | 2,266.289673 | 53482238 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,283,629 | 14,918.894702 | 53482238 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | USDC/SEND | 3000 | 1,158,466 | 72.405863 | 53482238 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,112,611 | 37,029,594.047280 | 53482238 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | DRB/WETH | 10000 | 1,050,433 | 0.000000 | 53482238 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,044,402 | 549,929.499250 | 53482238 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,024,247 | 21,970,183.467339 | 53482238 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/VELVET | 100 | 997,995 | 19.060170 | 53482238 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/VVV | 10000 | 956,460 | 101.018574 | 53482238 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome | WETH/EDEL | 7000 | 953,309 | 86,121.555971 | 53482238 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/MORPHO | 3000 | 943,258 | 1,054.190222 | 53482238 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome_slipstream | USDC/cbBTC | 358 | 935,347 | 0.000013 | 53482238 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/NOCK | 3000 | 933,974 | 71.767995 | 53482238 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/USDC | 10000 | 925,484 | 2,279.510176 | 53482238 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome | WETH/WELL | 10000 | 917,280 | 1,271,961.163077 | 53482238 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | USDC/VVV | 3000 | 881,582 | 0.044674 | 53482238 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | uXRP/WETH | 3000 | 869,493 | 0.000553 | 53482238 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome | WETH/AERO | 10000 | 841,383 | 3,611.587591 | 53482238 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 818,560 | 20.156324 | 53482238 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 787,188 | 0.055453 | 53482238 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 768,823 | 0.799140 | 53482238 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 731,441 | 0.585351 | 53482238 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| aerodrome | VIRTUAL/WETH | 10000 | 719,707 | 0.000257 | 53482238 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 704,194 | 4,892,146.069979 | 53482238 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 668,855 | 0.000008 | 53482238 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v2 | WETH/NPC | 3000 | 662,625 | 147,536.627496 | 53482238 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| uniswap_v3 | TIG/USDC | 10000 | 652,464 | 0.535712 | 53482238 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome | WETH/msETH (stable) | 500 | 651,567 | 2.364339 | 53482238 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | WETH/BRETT | 2129 | 641,294 | 552,295.111619 | 53482238 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome | WETH/bsdETH | 100 | 608,244 | 0.915255 | 53482238 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 585,602 | 0.086839 | 53482238 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| uniswap_v3 | FLOCK/USDC | 3000 | 561,782 | 0.038261 | 53482238 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |

## Recherche d'opportunités
- Cycles : 829 ; routes examinées : 16107470 ; candidats optimisés : 50931 ; net attendu > 0 : 8 ; dernier cycle 341.8 ms
- Rejets (moteur) : {'spread_below_threshold': 15846135, 'liquidity_below_min': 209134, 'negative_expected_net': 50923, 'borrow_bound_too_small': 822, 'cycle_budget_exhausted': 448}
- Enregistrements de la session : 50931 ; net attendu > 0 : 8 ; simulés (eth_call de la vraie tx) : 0 (ok 0, échec 0) ; étiquettes ghost N+1 : 0/0 positives
- Décisions : {'REJECTED': 50931} ; motifs de rejet : {'below_safety_margin': 8, 'negative_expected_net': 50923, 'p_lower_below_threshold': 7, 'reliability_not_demonstrated': 1, 'stale_data': 1}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53481758 | cbBTC→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.000473 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0028 €) | — | 0.85 | 0.184 (n=854) | REJECTED | below_safety_margin(4<9), p_lower_below_threshold(0.18<0.75) |
| 53481758 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC | 38.660444 USDC | 0.009597 USDC | 0.000000 USDC | 0.006805 USDC | 0.002792 USDC (0.0026 €) | — | 0.72 | 0.184 (n=854) | REJECTED | below_safety_margin(2792<7732), p_lower_below_threshold(0.18<0.75) |
| 53481949 | USDC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 31.641618 USDC | 0.007589 USDC | 0.000000 USDC | 0.006801 USDC | 0.000788 USDC (0.0007 €) | — | 0.25 | 0.184 (n=854) | REJECTED | below_safety_margin(788<6328), p_lower_below_threshold(0.18<0.75) |
| 53481758 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 164.630541 USDC | 0.005868 USDC | 0.000000 USDC | 0.005085 USDC | 0.000783 USDC (0.0007 €) | — | 0.05 | 0.034 (n=197) | REJECTED | below_safety_margin(783<32926), p_lower_below_threshold(0.03<0.75) |
| 53481949 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH | 0.014052 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0007 €) | — | 0.25 | 0.184 (n=854) | REJECTED | below_safety_margin(345426424345<2810408866478), p_lower_below_threshold(0.18<0.75) |
| 53481758 | cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.001821 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0007 €) | — | 0.05 | 0.034 (n=197) | REJECTED | below_safety_margin(1<36), p_lower_below_threshold(0.03<0.75) |
| 53482048 | USDC→[aerodrome_slipstream]→CARV→[aerodrome_slipstream]→USDC | 11.477160 USDC | 0.005800 USDC | 0.000000 USDC | 0.005080 USDC | 0.000720 USDC (0.0007 €) | — | 0.63 | 0.024 (n=59) | REJECTED | below_safety_margin(720<2295), stale_data(4189ms>4000.0), p_lower_below_threshold(0.02<0.75) |
| 53481942 | USDC→[aerodrome]→PLAY→[pancakeswap_v3]→USDC | 6.874513 USDC | 0.005106 USDC | 0.000000 USDC | 0.004770 USDC | 0.000336 USDC (0.0003 €) | — | 0.49 | 0.058 (n=25) | REJECTED | below_safety_margin(336<1374), reliability_not_demonstrated |

## Fiabilité et décision
- Observations ghost : 4940 ; taux observé 0.168 ; borne inférieure crédible (0.9) 0.162 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 16.2% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
