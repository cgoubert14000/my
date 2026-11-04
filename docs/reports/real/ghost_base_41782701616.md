# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-04T06:28:30+00:00 ; durée 21.41 min ; blocs 53491535 → 53492181 (636 vus)

## Connexion
- Requêtes RPC : 7289 ; erreurs : 0 ; latence p50/p95 : 223.5/1,331.4 ms
- Rafraîchissements d'état : 637 ; âge des données au dernier bloc : 1.46 s ; changements de frais LP observés (pools à frais dynamiques) : 921
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 1342 ; cycles déclenchés par événement : 180 ; avance médiane sur le rafraîchissement multicall : 611 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,292.39 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 494 pools, 284 jetons, 19492 routes
- Par DEX : uniswap_v3 141, aerodrome_slipstream 106, aerodrome 204, pancakeswap_v3 29, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 173 (rejetés 2) → 578 jetons ; pools candidats 3704 (énumérés 307, par paires 0), mesurés 497, sous le plancher de 10000.0 $ : 3 → gardés 494 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDC': 1.0, 'USDbC': 1.0, 'WETH': 2296.568203, 'cbBTC': 77781.37292, 'AERO': 0.62987}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 151,232,320 | 2,292.391468 | 53492181 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,801,634 | 0.029459 | 53492181 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,243,028 | 0.029470 | 53492181 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,143,503 | 0.000013 | 53492181 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 8,063,456 | 2,291.681828 | 53492181 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,881,171 | 99.044506 | 53492181 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,607,775 | 0.001562 | 53492181 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 5,378,559 | 1.592063 | 53492181 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,818,382 | 0.029451 | 53492181 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,193,029 | 2,292.618882 | 53492181 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,093,862 | 0.999894 | 53492181 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome_slipstream | WETH/USDC | 150 | 3,879,710 | 2,292.507896 | 53492181 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome | WETH/KTA | 3000 | 3,445,179 | 41,435.206889 | 53492181 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,690,970 | 0.029479 | 53492181 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2928 | 2,161,717 | 99.047903 | 53492181 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | WETH/FAI | 10000 | 2,158,838 | 1,143,158.968609 | 53492181 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 544 | 1,817,726 | 0.000013 | 53492181 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,753,729 | 0.007109 | 53492181 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v3 | XDP/USDC | 100 | 1,734,690 | 0.017744 | 53492181 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,682,556 | 0.000000 | 53492181 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,622,590 | 0.000013 | 53492181 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,565,969 | 434.526765 | 53492181 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,552,822 | 1.432992 | 53492181 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,550,343 | 0.000013 | 53492181 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,451,706 | 0.818329 | 53492181 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,425,460 | 3,640.978639 | 53492181 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,358,858 | 2,291.655132 | 53492181 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | WETH/USDC | 3000 | 1,341,873 | 2,294.039180 | 53492181 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| uniswap_v2 | WETH/USDC | 3000 | 1,341,258 | 2,292.558499 | 53492181 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,304,959 | 14,772.910410 | 53492181 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | USDC/SEND | 3000 | 1,158,309 | 72.425481 | 53492181 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,125,513 | 37,093,402.415533 | 53492181 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,052,881 | 556,112.269563 | 53492181 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,037,089 | 0.000000 | 53492181 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,030,290 | 22,201,054.916258 | 53492181 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/VELVET | 100 | 995,741 | 19.184764 | 53492181 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/VVV | 10000 | 981,620 | 99.751743 | 53492181 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 965,414 | 1,038.244014 | 53492181 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome | WETH/EDEL | 7000 | 962,730 | 86,494.410575 | 53492181 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome_slipstream | USDC/cbBTC | 354 | 944,238 | 0.000013 | 53492181 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | WETH/WELL | 10000 | 929,809 | 1,267,969.063898 | 53492181 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/USDC | 10000 | 929,742 | 2,279.828359 | 53492181 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome | USDC/NOCK | 3000 | 925,963 | 73.015167 | 53492181 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | USDC/VVV | 3000 | 903,897 | 0.043206 | 53492181 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | uXRP/WETH | 3000 | 879,497 | 0.000552 | 53492181 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome | WETH/AERO | 10000 | 843,942 | 3,625.917024 | 53492181 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 820,993 | 20.074215 | 53492181 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 792,450 | 0.056234 | 53492181 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 778,100 | 0.799140 | 53492181 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 738,301 | 0.591717 | 53492181 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| aerodrome | VIRTUAL/WETH | 10000 | 728,391 | 0.000257 | 53492181 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 711,487 | 4,909,529.529998 | 53492181 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 672,016 | 0.000008 | 53492181 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v2 | WETH/NPC | 3000 | 670,805 | 147,477.249971 | 53492181 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| uniswap_v3 | TIG/USDC | 10000 | 652,870 | 0.536249 | 53492181 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 645,279 | 551,769.938744 | 53492181 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome | WETH/msETH (stable) | 500 | 642,910 | 2.454689 | 53492181 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome | WETH/bsdETH | 100 | 615,987 | 0.914056 | 53492181 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 600,269 | 0.090101 | 53492181 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| uniswap_v3 | FLOCK/USDC | 3000 | 562,357 | 0.038312 | 53492181 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |

## Recherche d'opportunités
- Cycles : 816 ; routes examinées : 15905472 ; candidats optimisés : 44848 ; net attendu > 0 : 0 ; dernier cycle 350.5 ms
- Rejets (moteur) : {'spread_below_threshold': 15692013, 'liquidity_below_min': 167795, 'negative_expected_net': 44848, 'borrow_bound_too_small': 816}
- Enregistrements de la session : 44848 ; net attendu > 0 : 0 ; simulés (eth_call de la vraie tx) : 0 (ok 0, échec 0) ; étiquettes ghost N+1 : 0/0 positives
- Décisions : {'REJECTED': 44848} ; motifs de rejet : {'negative_expected_net': 44848}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|

_Aucun candidat à net positif. Les 10 plus proches de la rentabilité (net attendu négatif) :_

| Bloc | Route | Montant | Brut | Frais flash | Gaz (dont L1) | Net attendu (€) | Marge (bps) |
|---:|---|---:|---:|---:|---:|---:|---:|
| 53492067 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.000422 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.0000 | 0.00 |
| 53492067 | WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.018726 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | -0.0002 | -0.05 |
| 53491600 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.018956 WETH | 0.000002 WETH | 0.000000 WETH | 0.000002 WETH | -0.0002 | -0.06 |
| 53491600 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 42.726546 USDC | 0.004887 USDC | 0.000000 USDC | 0.005157 USDC | -0.0002 | -0.06 |
| 53491549 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.017923 WETH | 0.000002 WETH | 0.000000 WETH | 0.000002 WETH | -0.0007 | -0.18 |
| 53491549 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 40.626590 USDC | 0.004389 USDC | 0.000000 USDC | 0.005158 USDC | -0.0007 | -0.19 |
| 53491600 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.016908 WETH | 0.000002 WETH | 0.000000 WETH | 0.000002 WETH | -0.0008 | -0.22 |
| 53491600 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 38.907826 USDC | 0.004310 USDC | 0.000000 USDC | 0.005157 USDC | -0.0008 | -0.22 |
| 53492067 | cbBTC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.000345 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | -0.0014 | -0.58 |
| 53492067 | WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→WETH | 0.011697 WETH | 0.000002 WETH | 0.000000 WETH | 0.000003 WETH | -0.0017 | -0.69 |

## Fiabilité et décision
- Observations ghost : 5043 ; taux observé 0.169 ; borne inférieure crédible (0.9) 0.162 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 16.2% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
