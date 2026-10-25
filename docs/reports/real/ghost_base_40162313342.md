# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-25T05:52:56+00:00 ; durée 73.52 min ; blocs 53056902 → 53059113 (2176 vus)

## Connexion
- Requêtes RPC : 26911 ; erreurs : 0 ; latence p50/p95 : 287.4/1,162.4 ms
- Rafraîchissements d'état : 2176 ; âge des données au dernier bloc : 2.34 s ; changements de frais LP observés (pools à frais dynamiques) : 2268
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 20355 ; cycles déclenchés par événement : 2936 ; avance médiane sur le rafraîchissement multicall : 776 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,351.81 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 541 pools, 309 jetons, 19696 routes
- Par DEX : uniswap_v3 144, aerodrome 216, aerodrome_slipstream 134, pancakeswap_v3 31, uniswap_v2 13, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 193 (rejetés 2) → 598 jetons ; pools candidats 3806 (énumérés 349, par paires 0), mesurés 543, sous le plancher de 10000.0 $ : 2 → gardés 541 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDbC': 1.0, 'USDC': 1.0, 'WETH': 2361.63016, 'cbBTC': 80803.612106, 'AERO': 0.690594}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 158,990,506 | 2,351.808766 | 53059113 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 17,338,848 | 0.029176 | 53059113 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,244,441 | 0.029192 | 53059113 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,525,825 | 0.000012 | 53059113 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome | WETH/VVV | 3000 | 8,994,695 | 95.164637 | 53059113 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/USDC | 500 | 8,429,628 | 2,348.327219 | 53059113 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | USDC/AERO | 3000 | 7,790,422 | 1.479120 | 53059113 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,040,989 | 0.001652 | 53059113 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | WETH/USDC | 150 | 5,665,934 | 2,349.067119 | 53059113 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,486,156 | 0.029187 | 53059113 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,450,518 | 2,349.145975 | 53059113 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,241,501 | 0.999832 | 53059113 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,899,986 | 34,433.469168 | 53059113 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/USDC | 3000 | 3,801,540 | 2,351.552608 | 53059113 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | WETH/cbBTC | 2505 | 3,267,091 | 0.029205 | 53059113 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | USDC/cbBTC | 400 | 2,855,963 | 0.000012 | 53059113 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome_slipstream | WETH/VVV | 2700 | 2,525,930 | 95.210511 | 53059113 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,229,202 | 410.520195 | 53059113 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | WETH/FAI | 10000 | 2,135,459 | 1,229,675.520279 | 53059113 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,905,271 | 0.000000 | 53059113 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,904,432 | 0.000012 | 53059113 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v3 | XDP/USDC | 100 | 1,790,679 | 0.018039 | 53059113 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,732,258 | 0.000012 | 53059113 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | USDC/cbBTC | 334 | 1,721,150 | 0.000012 | 53059113 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | VIRTUAL/WETH | 10000 | 1,580,862 | 0.000265 | 53059113 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,470,515 | 1.673913 | 53059113 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,457,859 | 0.826892 | 53059113 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,452,213 | 0.005515 | 53059113 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v3 | WETH/AERO | 3000 | 1,432,168 | 3,470.105439 | 53059113 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,374,944 | 14,066.301548 | 53059113 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,297,055 | 2,348.196253 | 53059113 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | WETH/AERO | 10000 | 1,262,974 | 3,445.976476 | 53059113 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,249,784 | 0.000265 | 53059113 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | USDC/SEND | 3000 | 1,222,545 | 65.014830 | 53059113 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | DRB/WETH | 10000 | 1,196,709 | 0.000000 | 53059113 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/doginme | 10000 | 1,171,592 | 35,446,293.114047 | 53059113 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | WETH/WELL | 10000 | 1,134,742 | 1,126,996.480542 | 53059113 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,130,018 | 491,864.954002 | 53059113 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | USDC/NOCK | 3000 | 1,084,927 | 53.212812 | 53059113 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,042,729 | 16.866727 | 53059113 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | WETH/EDEL | 7000 | 1,040,483 | 78,314.830274 | 53059113 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,039,205 | 21,489,605.354605 | 53059113 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | USDC/VVV | 3000 | 967,796 | 0.040516 | 53059113 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 952,289 | 17.160329 | 53059113 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| uniswap_v3 | WETH/USDC | 10000 | 927,845 | 2,344.953414 | 53059113 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome | WETH/msETH (stable) | 500 | 926,530 | 2.309502 | 53059113 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | WETH/MORPHO | 3000 | 910,563 | 1,118.309521 | 53059113 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | uXRP/WETH | 3000 | 901,894 | 0.000551 | 53059113 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | USDC/SAPIEN | 4525 | 882,181 | 17.852645 | 53059113 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v3 | WETH/VVV | 10000 | 873,801 | 95.781970 | 53059113 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v2 | WETH/USDC | 3000 | 850,471 | 2,352.026907 | 53059113 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 810,135 | 0.000008 | 53059113 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | weETH_04c0/WETH | 500 | 803,160 | 1.105854 | 53059113 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome | WETH/wstETH | 3000 | 796,288 | 0.803130 | 53059113 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| pancakeswap_v3 | QUID/USDC | 100 | 795,246 | 0.056699 | 53059113 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 750,213 | 4,638,418.950240 | 53059113 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 747,000 | 0.620737 | 53059113 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v3 | TIG/USDC | 10000 | 735,358 | 0.677016 | 53059113 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/NPC | 3000 | 721,028 | 133,873.876787 | 53059113 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | WETH/BRETT | 2117 | 706,428 | 492,816.741432 | 53059113 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |

## Recherche d'opportunités
- Cycles : 5111 ; routes examinées : 100666256 ; candidats optimisés : 266871 ; net attendu > 0 : 153 ; dernier cycle 279.3 ms
- Rejets (moteur) : {'spread_below_threshold': 99109536, 'liquidity_below_min': 1239137, 'negative_expected_net': 266718, 'pool_quarantined': 43624, 'borrow_bound_too_small': 5109, 'unquotable': 1758, 'cycle_budget_exhausted': 221}
- Enregistrements de la session : 266871 ; net attendu > 0 : 153 ; simulés (eth_call de la vraie tx) : 22 (ok 2, échec 20) ; étiquettes ghost N+1 : 0/21 positives
- Décisions : {'REJECTED': 266871} ; motifs de rejet : {'below_safety_margin': 96, 'negative_expected_net': 266718, 'p_lower_below_threshold': 115, 'reliability_not_demonstrated': 38, 'sim_below_estimate': 1, 'simulated_net_nonpositive': 1, 'simulation_failed': 20, 'stale_data': 10}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53058175 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 101.966309 USDC | 0.861736 USDC | 0.000000 USDC | 0.007094 USDC | 0.854642 USDC (0.7863 €) | — | 83.82 | 0.001 (n=14) | REJECTED | reliability_not_demonstrated |
| 53058175 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 102.137640 USDC | 0.861683 USDC | 0.000000 USDC | 0.007094 USDC | 0.854589 USDC (0.7862 €) | — | 83.67 | 0.001 (n=12) | REJECTED | reliability_not_demonstrated |
| 53058175 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.043138 WETH | 0.000364 WETH | 0.000000 WETH | 0.000003 WETH | 0.000361 WETH (0.7854 €) | — | 83.80 | 0.001 (n=14) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53058175 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.043243 WETH | 0.000364 WETH | 0.000000 WETH | 0.000003 WETH | 0.000361 WETH (0.7853 €) | — | 83.58 | 0.001 (n=12) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53058175 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 101.555983 USDC | 0.851676 USDC | 0.000000 USDC | 0.007094 USDC | 0.844582 USDC (0.7770 €) | — | 83.16 | 0.001 (n=14) | REJECTED | reliability_not_demonstrated |
| 53058175 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.042977 WETH | 0.000360 WETH | 0.000000 WETH | 0.000003 WETH | 0.000357 WETH (0.7762 €) | — | 83.12 | 0.001 (n=14) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53058175 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 100.467649 USDC | 0.834113 USDC | 0.000000 USDC | 0.007094 USDC | 0.827019 USDC (0.7609 €) | — | 82.32 | 0.001 (n=14) | REJECTED | reliability_not_demonstrated |
| 53058175 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.042568 WETH | 0.000353 WETH | 0.000000 WETH | 0.000003 WETH | 0.000350 WETH (0.7602 €) | — | 82.19 | 0.001 (n=14) | REJECTED | reliability_not_demonstrated |
| 53058175 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 99.866315 USDC | 0.824586 USDC | 0.000000 USDC | 0.007094 USDC | 0.817492 USDC (0.7521 €) | — | 81.86 | 0.001 (n=12) | REJECTED | reliability_not_demonstrated |
| 53058175 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.042269 WETH | 0.000349 WETH | 0.000000 WETH | 0.000003 WETH | 0.000346 WETH (0.7515 €) | — | 81.83 | 0.001 (n=12) | REJECTED | reliability_not_demonstrated |
| 53058175 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[sushiswap_v3]→USDC | 98.364297 USDC | 0.821963 USDC | 0.000000 USDC | 0.007094 USDC | 0.814869 USDC (0.7497 €) | — | 82.84 | 0.001 (n=14) | REJECTED | reliability_not_demonstrated |
| 53058175 | WETH→[sushiswap_v3]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.041638 WETH | 0.000348 WETH | 0.000000 WETH | 0.000003 WETH | 0.000345 WETH (0.7493 €) | — | 82.82 | 0.001 (n=14) | REJECTED | reliability_not_demonstrated |
| 53058175 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.037326 WETH | 0.000315 WETH | 0.000000 WETH | 0.000003 WETH | 0.000312 WETH (0.6778 €) | — | 83.57 | 0.001 (n=14) | REJECTED | reliability_not_demonstrated |
| 53058175 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 87.918625 USDC | 0.743641 USDC | 0.000000 USDC | 0.007811 USDC | 0.735830 USDC (0.6770 €) | — | 83.69 | 0.001 (n=14) | REJECTED | reliability_not_demonstrated |
| 53058175 | WETH→[aerodrome]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.030905 WETH | 0.000249 WETH | 0.000000 WETH | 0.000003 WETH | 0.000246 WETH (0.5338 €) | — | 79.49 | 0.001 (n=10) | REJECTED | reliability_not_demonstrated |
| 53058175 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[aerodrome]→USDC | 72.864735 USDC | 0.585955 USDC | 0.000000 USDC | 0.006769 USDC | 0.579186 USDC (0.5329 €) | — | 79.49 | 0.001 (n=10) | REJECTED | reliability_not_demonstrated |
| 53058175 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.031146 WETH | 0.000206 WETH | 0.000000 WETH | 0.000003 WETH | 0.000203 WETH (0.4413 €) | — | 65.21 | 0.001 (n=14) | REJECTED | reliability_not_demonstrated |
| 53058175 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 73.335285 USDC | 0.485324 USDC | 0.000000 USDC | 0.007094 USDC | 0.478230 USDC (0.4400 €) | — | 65.21 | 0.001 (n=14) | REJECTED | reliability_not_demonstrated |
| 53058175 | WETH→[uniswap_v2]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.030282 WETH | 0.000201 WETH | 0.000000 WETH | 0.000003 WETH | 0.000198 WETH (0.4303 €) | — | 65.40 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 53058175 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[uniswap_v2]→USDC | 71.273975 USDC | 0.472513 USDC | 0.000000 USDC | 0.006361 USDC | 0.466152 USDC (0.4289 €) | — | 65.40 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 53058099 | WETH→[aerodrome]→MOR→[uniswap_v3]→WETH | 0.012442 WETH | 0.000034 WETH | 0.000000 WETH | 0.000002 WETH | 0.000031 WETH (0.0683 €) | — | 25.27 | 0.000 (n=19) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53058437 | WETH→[sushiswap_v3]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.011610 WETH | 0.000027 WETH | 0.000000 WETH | 0.000003 WETH | 0.000024 WETH (0.0511 €) | — | 20.27 | 0.000 (n=21) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53058437 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[sushiswap_v3]→USDC | 27.343193 USDC | 0.062658 USDC | 0.000000 USDC | 0.007094 USDC | 0.055564 USDC (0.0511 €) | — | 20.32 | 0.000 (n=21) | REJECTED | reliability_not_demonstrated |
| 53058437 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.011636 WETH | 0.000026 WETH | 0.000000 WETH | 0.000003 WETH | 0.000023 WETH (0.0501 €) | — | 19.83 | 0.000 (n=38) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 53058437 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 27.470241 USDC | 0.061586 USDC | 0.000000 USDC | 0.007094 USDC | 0.054492 USDC (0.0501 €) | — | 19.84 | 0.000 (n=38) | REJECTED | p_lower_below_threshold(0.00<0.75) |

## Fiabilité et décision
- Observations ghost : 2375 ; taux observé 0.095 ; borne inférieure crédible (0.9) 0.088 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 8.8% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
