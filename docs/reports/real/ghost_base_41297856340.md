# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-01T13:21:42+00:00 ; durée 165.74 min ; blocs 53370003 → 53374976 (4958 vus)

## Connexion
- Requêtes RPC : 58146 ; erreurs : 3 ; latence p50/p95 : 132.3/606.4 ms
- Rafraîchissements d'état : 4958 ; âge des données au dernier bloc : 2.46 s ; changements de frais LP observés (pools à frais dynamiques) : 3781
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 27378 ; cycles déclenchés par événement : 3318 ; avance médiane sur le rafraîchissement multicall : 285 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,260.18 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 501 pools, 289 jetons, 18668 routes
- Par DEX : uniswap_v3 139, aerodrome_slipstream 112, aerodrome 207, pancakeswap_v3 29, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 178 (rejetés 2) → 583 jetons ; pools candidats 3735 (énumérés 317, par paires 0), mesurés 504, sous le plancher de 10000.0 $ : 3 → gardés 501 (max 1500) ; prix des hubs : {'USDC': 1.0, 'USDbC': 1.0, 'DAI': 1.0, 'WETH': 2268.223075, 'cbBTC': 77979.526152, 'AERO': 0.640175}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 150,612,436 | 2,260.178687 | 53374975 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,142,227 | 0.029054 | 53374975 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,292,919 | 0.000013 | 53374975 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,115,467 | 0.029102 | 53374975 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| aerodrome | WETH/VVV | 3000 | 7,892,352 | 96.991627 | 53374975 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/USDC | 500 | 7,878,916 | 2,263.736093 | 53374975 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,674,165 | 0.001594 | 53374975 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 5,693,884 | 1.567150 | 53374975 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,185,087 | 0.029051 | 53374975 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,096,045 | 0.998845 | 53374975 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome_slipstream | WETH/USDC | 150 | 4,058,493 | 2,263.470149 | 53374975 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/USDC | 100 | 3,880,198 | 2,263.413831 | 53374975 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | WETH/KTA | 3000 | 3,559,127 | 37,742.074068 | 53374975 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,697,291 | 0.029087 | 53374975 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2730 | 2,418,502 | 96.963081 | 53374975 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | USDC/cbBTC | 412 | 2,185,690 | 0.000013 | 53374975 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome | WETH/FAI | 10000 | 2,079,734 | 1,197,399.229010 | 53374975 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,758,339 | 0.000000 | 53374975 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,752,599 | 0.017995 | 53374976 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,637,267 | 0.000013 | 53374975 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,585,429 | 0.000013 | 53374975 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,556,078 | 422.456124 | 53374975 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,537,008 | 1.499750 | 53374975 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v2 | WETH/USDC | 3000 | 1,505,917 | 2,260.779332 | 53374975 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,457,455 | 0.825724 | 53374975 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,429,361 | 3,544.915295 | 53374975 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | WETH/USDC | 3000 | 1,407,216 | 2,260.256822 | 53374975 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,326,854 | 2,263.669969 | 53374975 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,323,187 | 0.005168 | 53374975 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,311,880 | 14,554.893089 | 53374975 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome_slipstream | USDC/cbBTC | 330 | 1,307,197 | 0.000013 | 53374975 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/SEND | 3000 | 1,169,712 | 71.020549 | 53374975 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,117,180 | 36,185,541.361158 | 53374975 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,078,314 | 508,538.599286 | 53374975 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,059,745 | 0.000000 | 53374975 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,024,225 | 21,820,989.339576 | 53374975 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | WETH/VVV | 10000 | 998,741 | 96.712438 | 53374975 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome_slipstream | USDC/VELVET | 100 | 997,114 | 19.106894 | 53374975 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | WETH/EDEL | 7000 | 974,570 | 82,103.589489 | 53374975 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | USDC/NOCK | 3000 | 959,997 | 67.928728 | 53374975 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome | WETH/WELL | 10000 | 957,263 | 1,162,935.806093 | 53374975 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | USDC/VVV | 3000 | 952,779 | 0.042847 | 53374975 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/MORPHO | 3000 | 951,572 | 981.450645 | 53374975 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/USDC | 10000 | 922,577 | 2,252.785569 | 53374975 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome | WETH/AERO | 10000 | 871,081 | 3,523.374318 | 53374975 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | uXRP/WETH | 3000 | 865,208 | 0.000549 | 53374975 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | USDC/SAPIEN | 4505 | 843,222 | 19.256748 | 53374975 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 821,117 | 0.060651 | 53374975 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 765,859 | 0.801881 | 53374975 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| aerodrome | VIRTUAL/WETH | 10000 | 734,998 | 0.000261 | 53374975 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 723,588 | 0.594926 | 53374975 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 715,602 | 4,713,664.467451 | 53374975 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 692,208 | 0.000008 | 53374975 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v2 | WETH/NPC | 3000 | 683,553 | 137,899.711847 | 53374975 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | WETH/BRETT | 2114 | 666,551 | 510,479.060416 | 53374975 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | TIG/USDC | 10000 | 663,974 | 0.554414 | 53374975 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome | WETH/msETH (stable) | 500 | 657,665 | 2.344017 | 53374975 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 620,476 | 0.094904 | 53374975 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| aerodrome | WETH/bsdETH | 100 | 606,635 | 0.916155 | 53374975 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome_slipstream | WETH/MORPHO | 2757 | 556,083 | 981.390226 | 53374975 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |

## Recherche d'opportunités
- Cycles : 8275 ; routes examinées : 154477700 ; candidats optimisés : 523900 ; net attendu > 0 : 788 ; dernier cycle 48.9 ms
- Rejets (moteur) : {'spread_below_threshold': 151883020, 'liquidity_below_min': 2035434, 'negative_expected_net': 523112, 'borrow_bound_too_small': 18217, 'unquotable': 16542, 'cycle_budget_exhausted': 587}
- Enregistrements de la session : 523900 ; net attendu > 0 : 788 ; simulés (eth_call de la vraie tx) : 56 (ok 42, échec 14) ; étiquettes ghost N+1 : 0/42 positives
- Décisions : {'REJECTED': 523900} ; motifs de rejet : {'below_safety_margin': 517, 'negative_expected_net': 523112, 'p_lower_below_threshold': 708, 'price_impact': 14, 'reliability_not_demonstrated': 80, 'simulation_failed': 14, 'stale_data': 17}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53373620 | WETH→[aerodrome_slipstream]→TIG→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.036307 WETH | 0.000885 WETH | 0.000000 WETH | 0.000003 WETH | 0.000882 WETH (1.8341 €) | — | 242.94 | 0.000 (n=33) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 53373620 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→TIG→[uniswap_v3]→USDC | 81.979625 USDC | 1.998439 USDC | 0.000000 USDC | 0.006792 USDC | 1.991647 USDC (1.8323 €) | — | 242.94 | 0.000 (n=33) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53373620 | WETH→[aerodrome_slipstream]→TIG→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.035802 WETH | 0.000874 WETH | 0.000000 WETH | 0.000003 WETH | 0.000871 WETH (1.8108 €) | — | 243.24 | 0.000 (n=37) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 53373620 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→TIG→[uniswap_v3]→USDC | 80.865987 USDC | 1.973757 USDC | 0.000000 USDC | 0.006792 USDC | 1.966965 USDC (1.8096 €) | — | 243.24 | 0.000 (n=37) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53373620 | WETH→[aerodrome_slipstream]→TIG→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.035327 WETH | 0.000863 WETH | 0.000000 WETH | 0.000003 WETH | 0.000860 WETH (1.7879 €) | — | 243.39 | 0.000 (n=37) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 53373620 | USDC→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→TIG→[uniswap_v3]→USDC | 79.770095 USDC | 1.948323 USDC | 0.000000 USDC | 0.006792 USDC | 1.941531 USDC (1.7862 €) | — | 243.39 | 0.000 (n=37) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53373620 | WETH→[aerodrome_slipstream]→TIG→[uniswap_v3]→WETH | 0.035595 WETH | 0.000759 WETH | 0.000000 WETH | 0.000002 WETH | 0.000756 WETH (1.5730 €) | — | 212.52 | 0.001 (n=6) | REJECTED | reliability_not_demonstrated |
| 53373620 | USDC→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→TIG→[uniswap_v3]→USDC | 67.437266 USDC | 1.643882 USDC | 0.000000 USDC | 0.006792 USDC | 1.637090 USDC (1.5061 €) | — | 242.76 | 0.000 (n=37) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53373620 | WETH→[aerodrome_slipstream]→TIG→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.029721 WETH | 0.000725 WETH | 0.000000 WETH | 0.000003 WETH | 0.000721 WETH (1.5003 €) | — | 242.75 | 0.000 (n=37) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53373620 | WETH→[aerodrome_slipstream]→TIG→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.028659 WETH | 0.000705 WETH | 0.000000 WETH | 0.000003 WETH | 0.000702 WETH (1.4593 €) | — | 244.88 | 0.000 (n=37) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53373620 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→TIG→[uniswap_v3]→USDC | 64.723995 USDC | 1.591766 USDC | 0.000000 USDC | 0.006792 USDC | 1.584974 USDC (1.4582 €) | — | 244.88 | 0.000 (n=37) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53373620 | WETH→[aerodrome_slipstream]→TIG→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.028560 WETH | 0.000703 WETH | 0.000000 WETH | 0.000003 WETH | 0.000700 WETH (1.4558 €) | — | 245.14 | 0.000 (n=33) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53373620 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→TIG→[uniswap_v3]→USDC | 64.504232 USDC | 1.588066 USDC | 0.000000 USDC | 0.006792 USDC | 1.581274 USDC (1.4548 €) | — | 245.14 | 0.000 (n=33) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53373620 | USDC→[sushiswap_v3]→WETH→[aerodrome_slipstream]→TIG→[uniswap_v3]→USDC | 56.215788 USDC | 1.381799 USDC | 0.000000 USDC | 0.006792 USDC | 1.375007 USDC (1.2650 €) | — | 244.59 | 0.000 (n=37) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53373620 | WETH→[aerodrome_slipstream]→TIG→[uniswap_v3]→USDC→[sushiswap_v3]→WETH | 0.024806 WETH | 0.000610 WETH | 0.000000 WETH | 0.000003 WETH | 0.000607 WETH (1.2616 €) | — | 244.59 | 0.000 (n=37) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53373620 | WETH→[aerodrome_slipstream]→TIG→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.018515 WETH | 0.000588 WETH | 0.000000 WETH | 0.000003 WETH | 0.000584 WETH (1.2152 €) | — | 315.62 | 0.000 (n=33) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53373620 | WETH→[aerodrome_slipstream]→TIG→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.018487 WETH | 0.000587 WETH | 0.000000 WETH | 0.000003 WETH | 0.000584 WETH (1.2145 €) | — | 315.93 | 0.000 (n=37) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53373620 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→TIG→[aerodrome_slipstream]→USDC | 41.805418 USDC | 1.326609 USDC | 0.000000 USDC | 0.007135 USDC | 1.319474 USDC (1.2139 €) | — | 315.62 | 0.000 (n=33) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53373620 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→TIG→[aerodrome_slipstream]→USDC | 41.743933 USDC | 1.325938 USDC | 0.000000 USDC | 0.007135 USDC | 1.318803 USDC (1.2133 €) | — | 315.93 | 0.000 (n=37) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53373620 | WETH→[aerodrome_slipstream]→TIG→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→WETH | 0.018413 WETH | 0.000585 WETH | 0.000000 WETH | 0.000003 WETH | 0.000582 WETH (1.2102 €) | — | 316.09 | 0.000 (n=37) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53373620 | USDC→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→TIG→[aerodrome_slipstream]→USDC | 41.573764 USDC | 1.321235 USDC | 0.000000 USDC | 0.007135 USDC | 1.314100 USDC (1.2090 €) | — | 316.09 | 0.000 (n=37) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53373620 | WETH→[aerodrome_slipstream]→TIG→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→WETH | 0.018103 WETH | 0.000574 WETH | 0.000000 WETH | 0.000003 WETH | 0.000571 WETH (1.1879 €) | — | 315.58 | 0.000 (n=37) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53373620 | USDC→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→TIG→[aerodrome_slipstream]→USDC | 40.912689 USDC | 1.298257 USDC | 0.000000 USDC | 0.007135 USDC | 1.291122 USDC (1.1878 €) | — | 315.58 | 0.000 (n=37) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53373620 | WETH→[aerodrome_slipstream]→TIG→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.017698 WETH | 0.000566 WETH | 0.000000 WETH | 0.000003 WETH | 0.000563 WETH (1.1703 €) | — | 318.01 | 0.000 (n=33) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53373620 | WETH→[aerodrome_slipstream]→TIG→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.017704 WETH | 0.000566 WETH | 0.000000 WETH | 0.000003 WETH | 0.000563 WETH (1.1697 €) | — | 317.74 | 0.000 (n=37) | REJECTED | p_lower_below_threshold(0.00<0.75) |

## Fiabilité et décision
- Observations ghost : 4097 ; taux observé 0.129 ; borne inférieure crédible (0.9) 0.122 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 12.2% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ✅ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
