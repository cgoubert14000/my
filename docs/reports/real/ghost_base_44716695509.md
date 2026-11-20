# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-20T11:09:42+00:00 ; durée 54.76 min ; blocs 59896587 → 59912997 (5431 vus)

## Connexion
- Requêtes RPC : 50608 ; erreurs : 0 ; latence p50/p95 : 91.0/890.8 ms
- Rafraîchissements d'état : 5431 ; âge des données au dernier bloc : 7.56 s ; changements de frais LP observés (pools à frais dynamiques) : 2488
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 7233 ; cycles déclenchés par événement : 1759 ; avance médiane sur le rafraîchissement multicall : 140 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 1,756.63 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 423 pools, 248 jetons, 12740 routes
- Par DEX : uniswap_v3 127, aerodrome_slipstream 86, aerodrome 171, pancakeswap_v3 26, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 1
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 146 (rejetés 2) → 551 jetons ; pools candidats 3579 (énumérés 255, par paires 0), mesurés 425, sous le plancher de 10000.0 $ : 2 → gardés 423 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDbC': 1.0, 'USDC': 1.0, 'WETH': 1747.036684, 'cbBTC': 61757.075443, 'AERO': 0.420112}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 85,520,281 | 1,756.632998 | 59913022 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 21,241,599 | 0.028344 | 59913022 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/USDC | 500 | 11,244,645 | 1,752.622153 | 59913022 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| uniswap_v3 | WETH/cbBTC | 3000 | 7,694,057 | 0.028298 | 59913022 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| aerodrome | WETH/VVV | 3000 | 6,482,044 | 85.285378 | 59913022 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | USDC/cbBTC | 500 | 6,026,343 | 0.000016 | 59913022 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,166,234 | 0.028355 | 59913022 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 3,599,981 | 2.374555 | 59913022 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/USDC | 100 | 3,401,248 | 1,752.140414 | 59913022 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,259,098 | 1.000001 | 59913022 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 2,718,706 | 39,070.013683 | 59913022 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 177 | 2,299,425 | 1,752.185648 | 59913022 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,916,743 | 0.000016 | 59913022 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 1,713,042 | 0.028311 | 59913022 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 1,653,113 | 1,144,598.292141 | 59913022 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,454,366 | 0.844852 | 59913022 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | USDC/cbBTC | 556 | 1,384,191 | 0.000016 | 59913022 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,329,488 | 0.000000 | 59913022 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,257,775 | 0.006488 | 59913022 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,242,023 | 0.000016 | 59913022 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,120,788 | 14.022628 | 59913022 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | USDC/SEND | 3000 | 1,059,937 | 86.492551 | 59913022 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,045,099 | 454.935376 | 59913022 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,005,240 | 16,030.033848 | 59913022 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | WETH/VVV | 10000 | 1,005,094 | 85.849937 | 59913022 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/AERO | 3000 | 996,819 | 4,172.161091 | 59913022 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v2 | WETH/USDC | 3000 | 994,194 | 1,756.673086 | 59913022 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| uniswap_v3 | WETH/doginme | 10000 | 908,011 | 32,217,856.513152 | 59913022 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | WETH/USDC | 3000 | 898,702 | 1,757.401216 | 59913022 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| uniswap_v3 | USDC/VVV | 3000 | 897,582 | 0.048634 | 59913022 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/BRETT | 10000 | 821,398 | 524,916.856160 | 59913022 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | USDC/NOCK | 3000 | 805,481 | 65.943880 | 59913022 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | DRB/WETH | 10000 | 791,688 | 0.000000 | 59913022 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/TOSHI | 10000 | 788,544 | 22,347,233.410856 | 59913022 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 781,176 | 0.001530 | 59913022 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| uniswap_v3 | XDP/USDC | 100 | 748,639 | 0.015669 | 59913022 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | WETH/MORPHO | 3000 | 729,884 | 1,092.352935 | 59913022 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| pancakeswap_v3 | WETH/USDC | 500 | 726,872 | 1,752.724250 | 59913022 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| pancakeswap_v3 | QUID/USDC | 100 | 722,519 | 0.046394 | 59913022 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome_slipstream | USDC/SAPIEN | 4565 | 703,980 | 25.178843 | 59913022 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v3 | WETH/USDC | 10000 | 696,213 | 1,744.307706 | 59913022 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/USDC | 100 | 599,416 | 1,752.069789 | 59913022 | `0xb4CB800910B228ED3d0834cF79D697127BBB00e5` |
| aerodrome | WETH/wstETH | 3000 | 596,568 | 0.797992 | 59913022 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | TIG/USDC | 10000 | 583,938 | 0.428810 | 59913022 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 559,658 | 4,687,781.136577 | 59913022 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome | WETH/AERO | 10000 | 544,218 | 4,190.092648 | 59913022 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | WETH/BRETT | 3748 | 511,597 | 530,262.212738 | 59913022 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome | USDC/MAI (stable) | 3000 | 508,939 | 1.386531 | 59913022 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | FLOCK/USDC | 3000 | 496,225 | 0.031460 | 59913022 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| uniswap_v2 | WETH/NPC | 3000 | 466,350 | 180,533.233319 | 59913022 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | USDC/USDT | 8 | 456,628 | 1.001496 | 59913022 | `0xa41Bc0AFfbA7Fd420d186b84899d7ab2aC57fcD1` |
| aerodrome_slipstream | AERO/cbBTC | 1025 | 444,971 | 0.000007 | 59913022 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| pancakeswap_v3 | ELSA/USDC | 100 | 420,506 | 0.059009 | 59913022 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| aerodrome_slipstream | WETH/MORPHO | 3034 | 396,051 | 1,092.041212 | 59913022 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| uniswap_v3 | WETH/uSOL | 3000 | 386,077 | 23.772755 | 59913022 | `0xab04A352D4EC8d0F1812A4E5EBe7807Fa67acD48` |
| uniswap_v3 | WETH/UNI | 10000 | 381,359 | 361.906950 | 59913022 | `0xAb365f161Dd501473a1ff0D2ef0dCE94E7398839` |
| aerodrome | cbBTC/EDGE | 7000 | 380,405 | 851,906.574132 | 59913022 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| aerodrome | AWE/USDC | 3000 | 367,805 | 0.056252 | 59913022 | `0xcb7f520d18141E36956fE0b3A6Bc3D4F11245521` |
| aerodrome | VIRTUAL/WETH | 10000 | 362,393 | 0.000233 | 59913022 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/VVV | 2724 | 359,877 | 85.299253 | 59913022 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |

## Recherche d'opportunités
- Cycles : 7189 ; routes examinées : 91587860 ; candidats optimisés : 66665 ; net attendu > 0 : 0 ; dernier cycle 1437.1 ms
- Rejets (moteur) : {'spread_below_threshold': 89995935, 'liquidity_below_min': 702658, 'negative_expected_net': 66665, 'cycle_budget_exhausted': 19103, 'borrow_bound_too_small': 7202}
- Enregistrements de la session : 2366 ; net attendu > 0 : 0 ; simulés (eth_call de la vraie tx) : 0 (ok 0, échec 0) ; étiquettes ghost N+1 : 0/0 positives
- Décisions : {'REJECTED': 2366} ; motifs de rejet : {'negative_expected_net': 2366}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|

_Aucun candidat à net positif. Les 10 plus proches de la rentabilité (net attendu négatif) :_

| Bloc | Route | Montant | Brut | Frais flash | Gaz (dont L1) | Net attendu (€) | Marge (bps) |
|---:|---|---:|---:|---:|---:|---:|---:|
| 59912012 | WETH→[aerodrome_slipstream]→wstETH→[aerodrome]→WETH | 0.005142 WETH | 0.000001 WETH | 0.000000 WETH | 0.000002 WETH | -0.0025 | -3.04 |
| 59912012 | WETH→[aerodrome_slipstream]→wstETH→[aerodrome]→WETH | 0.005142 WETH | 0.000001 WETH | 0.000000 WETH | 0.000002 WETH | -0.0025 | -3.04 |
| 59912013 | WETH→[aerodrome_slipstream]→wstETH→[aerodrome]→WETH | 0.005142 WETH | 0.000001 WETH | 0.000000 WETH | 0.000002 WETH | -0.0025 | -3.04 |
| 59912013 | WETH→[aerodrome_slipstream]→wstETH→[aerodrome]→WETH | 0.005142 WETH | 0.000001 WETH | 0.000000 WETH | 0.000002 WETH | -0.0025 | -3.04 |
| 59912014 | WETH→[aerodrome_slipstream]→wstETH→[aerodrome]→WETH | 0.005142 WETH | 0.000001 WETH | 0.000000 WETH | 0.000002 WETH | -0.0025 | -3.04 |
| 59912015 | WETH→[aerodrome_slipstream]→wstETH→[aerodrome]→WETH | 0.005142 WETH | 0.000001 WETH | 0.000000 WETH | 0.000002 WETH | -0.0025 | -3.04 |
| 59912015 | WETH→[aerodrome_slipstream]→wstETH→[aerodrome]→WETH | 0.005142 WETH | 0.000001 WETH | 0.000000 WETH | 0.000002 WETH | -0.0025 | -3.04 |
| 59901916 | USDC→[sushiswap_v3]→WETH→[pancakeswap_v3]→USDC | 10.231471 USDC | 0.000670 USDC | 0.000000 USDC | 0.003945 USDC | -0.0030 | -3.20 |
| 59901917 | USDC→[sushiswap_v3]→WETH→[pancakeswap_v3]→USDC | 10.231471 USDC | 0.000670 USDC | 0.000000 USDC | 0.003945 USDC | -0.0030 | -3.20 |
| 59901917 | USDC→[sushiswap_v3]→WETH→[pancakeswap_v3]→USDC | 10.231471 USDC | 0.000670 USDC | 0.000000 USDC | 0.003945 USDC | -0.0030 | -3.20 |

## Fiabilité et décision
- Observations ghost : 8590 ; taux observé 0.228 ; borne inférieure crédible (0.9) 0.222 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 22.2% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
