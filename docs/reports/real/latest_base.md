# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-24T13:17:51+00:00 ; durée 113.58 min ; blocs 53025852 → 53029260 (3406 vus)

## Connexion
- Requêtes RPC : 42209 ; erreurs : 16 ; latence p50/p95 : 97.5/406.6 ms
- Rafraîchissements d'état : 3407 ; âge des données au dernier bloc : 1.59 s ; changements de frais LP observés (pools à frais dynamiques) : 3518
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 44681 ; cycles déclenchés par événement : 4029 ; avance médiane sur le rafraîchissement multicall : 173 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,363.72 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 536 pools, 308 jetons, 19360 routes
- Par DEX : uniswap_v3 143, aerodrome 216, aerodrome_slipstream 133, pancakeswap_v3 29, uniswap_v2 12, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 193 (rejetés 2) → 598 jetons ; pools candidats 3806 (énumérés 348, par paires 0), mesurés 538, sous le plancher de 10000.0 $ : 2 → gardés 536 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDbC': 1.0, 'USDC': 1.0, 'WETH': 2363.674955, 'cbBTC': 80533.217668, 'AERO': 0.705694}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 155,388,122 | 2,363.717467 | 53029260 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 17,002,519 | 0.029335 | 53029260 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 12,227,662 | 98.036497 | 53029260 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,145,564 | 0.029383 | 53029260 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,603,758 | 0.000012 | 53029260 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome | USDC/AERO | 3000 | 8,911,733 | 1.418895 | 53029260 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/USDC | 500 | 8,562,024 | 2,366.686281 | 53029260 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 8,286,343 | 0.029369 | 53029260 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,016,566 | 0.001642 | 53029260 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 330 | 6,303,207 | 0.000012 | 53029260 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 609 | 5,500,697 | 2,365.864519 | 53029260 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,431,070 | 0.029323 | 53029260 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | USDC/cbBTC | 400 | 4,852,064 | 0.000012 | 53029260 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,535,385 | 2,365.744281 | 53029260 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,241,932 | 0.998962 | 53029260 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,911,130 | 34,585.972159 | 53029260 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/USDC | 3000 | 3,825,871 | 2,364.664038 | 53029260 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | WETH/USDT | 409 | 2,777,972 | 2,375.710741 | 53029260 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome_slipstream | WETH/VVV | 2703 | 2,501,465 | 98.054550 | 53029260 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,244,182 | 409.473965 | 53029260 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | WETH/FAI | 10000 | 2,119,894 | 1,260,468.597676 | 53029260 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome | WETH/AERO | 10000 | 1,925,984 | 3,337.777600 | 53029260 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,918,750 | 0.000000 | 53029260 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,914,817 | 0.000012 | 53029260 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v3 | XDP/USDC | 100 | 1,783,881 | 0.017952 | 53029260 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,737,818 | 0.000012 | 53029260 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | VIRTUAL/WETH | 10000 | 1,604,149 | 0.000267 | 53029260 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,549,717 | 1.610679 | 53029260 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | WETH/AERO | 3000 | 1,466,648 | 3,361.503919 | 53029260 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,458,582 | 0.826139 | 53029260 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,410,340 | 0.005296 | 53029260 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,378,482 | 13,947.176684 | 53029260 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,281,725 | 2,366.650646 | 53029260 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,260,544 | 0.000266 | 53029260 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | WETH/msETH (stable) | 500 | 1,231,100 | 2.308317 | 53029260 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome | USDC/SEND | 3000 | 1,225,106 | 64.743312 | 53029260 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | DRB/WETH | 10000 | 1,199,041 | 0.000000 | 53029260 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/doginme | 10000 | 1,178,508 | 35,304,872.240175 | 53029260 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | WETH/WELL | 10000 | 1,144,095 | 1,120,973.367828 | 53029260 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome | USDC/NOCK | 3000 | 1,134,541 | 48.660482 | 53029260 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,131,870 | 493,533.548554 | 53029260 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,089,811 | 16.982372 | 53029260 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | WETH/EDEL | 7000 | 1,058,122 | 76,494.047977 | 53029260 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | USDC/VVV | 3000 | 1,046,416 | 0.041363 | 53029260 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,040,078 | 16.982254 | 53029260 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,039,338 | 21,654,616.189288 | 53029260 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 955,129 | 23.314015 | 53029260 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| uniswap_v3 | WETH/MORPHO | 3000 | 923,540 | 1,094.194009 | 53029260 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | uXRP/WETH | 3000 | 896,910 | 0.000540 | 53029260 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | USDC/SAPIEN | 4560 | 896,372 | 17.378974 | 53029260 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v2 | WETH/USDC | 3000 | 852,600 | 2,368.906230 | 53029260 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 845,702 | 0.000009 | 53029260 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| pancakeswap_v3 | QUID/USDC | 100 | 820,617 | 0.060605 | 53029260 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | weETH_04c0/WETH | 500 | 813,519 | 1.105901 | 53029260 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome | WETH/wstETH | 3000 | 800,379 | 0.803010 | 53029260 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | WETH/USDC | 10000 | 784,350 | 2,373.719186 | 53029260 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/VVV | 10000 | 777,826 | 97.929665 | 53029260 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 766,183 | 0.629158 | 53029260 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 745,681 | 4,741,825.366811 | 53029260 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v2 | WETH/NPC | 3000 | 721,821 | 134,894.689350 | 53029260 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |

## Recherche d'opportunités
- Cycles : 7435 ; routes examinées : 143941600 ; candidats optimisés : 511959 ; net attendu > 0 : 130 ; dernier cycle 126.9 ms
- Rejets (moteur) : {'spread_below_threshold': 141781668, 'liquidity_below_min': 1526790, 'negative_expected_net': 511829, 'pool_quarantined': 113692, 'borrow_bound_too_small': 7434, 'cycle_budget_exhausted': 57}
- Enregistrements de la session : 511959 ; net attendu > 0 : 130 ; simulés (eth_call de la vraie tx) : 15 (ok 4, échec 11) ; étiquettes ghost N+1 : 0/13 positives
- Décisions : {'REJECTED': 511959} ; motifs de rejet : {'below_safety_margin': 84, 'negative_expected_net': 511829, 'p_lower_below_threshold': 106, 'reliability_not_demonstrated': 24, 'simulation_failed': 11}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53026232 | USDC→[uniswap_v3]→ZORA→[aerodrome_slipstream]→USDC | 451.845630 USDC | 2.035784 USDC | 0.000000 USDC | 0.005666 USDC | 2.030118 USDC (1.8677 €) | — | 44.93 | 0.001 (n=8) | REJECTED | reliability_not_demonstrated |
| 53028022 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 291.241849 USDC | 1.237549 USDC | 0.000000 USDC | 0.005307 USDC | 1.232242 USDC (1.1337 €) | — | 42.31 | 0.001 (n=9) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53026232 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→ZORA→[aerodrome_slipstream]→USDC | 61.934750 USDC | 0.298651 USDC | 0.000000 USDC | 0.007461 USDC | 0.291190 USDC (0.2679 €) | — | 47.02 | 0.001 (n=12) | REJECTED | reliability_not_demonstrated |
| 53026232 | WETH→[uniswap_v3]→ZORA→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.026243 WETH | 0.000126 WETH | 0.000000 WETH | 0.000003 WETH | 0.000123 WETH (0.2678 €) | — | 46.93 | 0.001 (n=12) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53026232 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→ZORA→[aerodrome_slipstream]→USDC | 61.527832 USDC | 0.295603 USDC | 0.000000 USDC | 0.007461 USDC | 0.288142 USDC (0.2651 €) | — | 46.83 | 0.001 (n=12) | REJECTED | reliability_not_demonstrated |
| 53026232 | WETH→[uniswap_v3]→ZORA→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.026062 WETH | 0.000125 WETH | 0.000000 WETH | 0.000003 WETH | 0.000122 WETH (0.2650 €) | — | 46.76 | 0.001 (n=12) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53026232 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→ZORA→[aerodrome_slipstream]→USDC | 61.284891 USDC | 0.294052 USDC | 0.000000 USDC | 0.007461 USDC | 0.286591 USDC (0.2637 €) | — | 46.76 | 0.001 (n=12) | REJECTED | reliability_not_demonstrated |
| 53026232 | WETH→[uniswap_v3]→ZORA→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.025939 WETH | 0.000124 WETH | 0.000000 WETH | 0.000003 WETH | 0.000121 WETH (0.2636 €) | — | 46.72 | 0.001 (n=12) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53026232 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→ZORA→[aerodrome_slipstream]→USDC | 61.487946 USDC | 0.293868 USDC | 0.000000 USDC | 0.007461 USDC | 0.286407 USDC (0.2635 €) | — | 46.58 | 0.001 (n=12) | REJECTED | reliability_not_demonstrated |
| 53026232 | WETH→[uniswap_v3]→ZORA→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→WETH | 0.026013 WETH | 0.000124 WETH | 0.000000 WETH | 0.000003 WETH | 0.000121 WETH (0.2634 €) | — | 46.56 | 0.001 (n=12) | REJECTED | reliability_not_demonstrated |
| 53026232 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→ZORA→[aerodrome_slipstream]→USDC | 60.801465 USDC | 0.288406 USDC | 0.000000 USDC | 0.007461 USDC | 0.280945 USDC (0.2585 €) | — | 46.21 | 0.001 (n=12) | REJECTED | reliability_not_demonstrated |
| 53026232 | WETH→[uniswap_v3]→ZORA→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.025786 WETH | 0.000122 WETH | 0.000000 WETH | 0.000003 WETH | 0.000119 WETH (0.2583 €) | — | 46.07 | 0.001 (n=12) | REJECTED | reliability_not_demonstrated |
| 53026232 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→ZORA→[aerodrome_slipstream]→USDC | 55.293015 USDC | 0.278215 USDC | 0.000000 USDC | 0.007461 USDC | 0.270754 USDC (0.2491 €) | — | 48.97 | 0.001 (n=12) | REJECTED | reliability_not_demonstrated |
| 53026232 | WETH→[uniswap_v3]→ZORA→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→WETH | 0.023398 WETH | 0.000118 WETH | 0.000000 WETH | 0.000003 WETH | 0.000114 WETH (0.2487 €) | — | 48.89 | 0.001 (n=12) | REJECTED | reliability_not_demonstrated |
| 53026232 | USDC→[sushiswap_v3]→WETH→[uniswap_v3]→ZORA→[aerodrome_slipstream]→USDC | 58.273143 USDC | 0.272763 USDC | 0.000000 USDC | 0.007461 USDC | 0.265302 USDC (0.2441 €) | — | 45.53 | 0.001 (n=12) | REJECTED | reliability_not_demonstrated |
| 53026232 | WETH→[uniswap_v3]→ZORA→[aerodrome_slipstream]→USDC→[sushiswap_v3]→WETH | 0.024662 WETH | 0.000115 WETH | 0.000000 WETH | 0.000003 WETH | 0.000112 WETH (0.2439 €) | — | 45.47 | 0.001 (n=12) | REJECTED | reliability_not_demonstrated |
| 53028986 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 807.787634 USDC | 0.270964 USDC | 0.000000 USDC | 0.006744 USDC | 0.264220 USDC (0.2431 €) | — | 3.27 | 0.002 (n=117) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 53028986 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.341007 WETH | 0.000114 WETH | 0.000000 WETH | 0.000003 WETH | 0.000112 WETH (0.2427 €) | — | 3.27 | 0.002 (n=117) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 53026232 | USDC→[uniswap_v2]→WETH→[uniswap_v3]→ZORA→[aerodrome_slipstream]→USDC | 43.803670 USDC | 0.153877 USDC | 0.000000 USDC | 0.006368 USDC | 0.147509 USDC (0.1357 €) | — | 33.68 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 53026232 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→ZORA→[aerodrome_slipstream]→USDC | 44.618570 USDC | 0.154884 USDC | 0.000000 USDC | 0.007461 USDC | 0.147423 USDC (0.1356 €) | — | 33.04 | 0.001 (n=12) | REJECTED | reliability_not_demonstrated |
| 53026232 | WETH→[uniswap_v3]→ZORA→[aerodrome_slipstream]→USDC→[uniswap_v2]→WETH | 0.018500 WETH | 0.000065 WETH | 0.000000 WETH | 0.000003 WETH | 0.000062 WETH (0.1353 €) | — | 33.62 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 53026232 | WETH→[uniswap_v3]→ZORA→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.018827 WETH | 0.000065 WETH | 0.000000 WETH | 0.000003 WETH | 0.000062 WETH (0.1352 €) | — | 33.02 | 0.001 (n=12) | REJECTED | reliability_not_demonstrated |
| 53026232 | USDC→[aerodrome]→WETH→[uniswap_v3]→ZORA→[aerodrome_slipstream]→USDC | 41.599469 USDC | 0.135328 USDC | 0.000000 USDC | 0.006776 USDC | 0.128552 USDC (0.1183 €) | — | 30.90 | 0.003 (n=93) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53026232 | WETH→[uniswap_v3]→ZORA→[aerodrome_slipstream]→USDC→[aerodrome]→WETH | 0.017557 WETH | 0.000057 WETH | 0.000000 WETH | 0.000003 WETH | 0.000054 WETH (0.1178 €) | — | 30.86 | 0.003 (n=93) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53028986 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.200821 WETH | 0.000044 WETH | 0.000000 WETH | 0.000003 WETH | 0.000041 WETH (0.0884 €) | — | 2.02 | 0.133 (n=263) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.13<0.75) |

## Fiabilité et décision
- Observations ghost : 2144 ; taux observé 0.096 ; borne inférieure crédible (0.9) 0.088 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 8.8% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
