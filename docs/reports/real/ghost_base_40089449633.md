# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-24T15:07:12+00:00 ; durée 222.93 min ; blocs 53025852 → 53032538 (6665 vus)

## Connexion
- Requêtes RPC : 83118 ; erreurs : 23 ; latence p50/p95 : 225.9/590.8 ms
- Rafraîchissements d'état : 6665 ; âge des données au dernier bloc : 2.56 s ; changements de frais LP observés (pools à frais dynamiques) : 10484
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 115705 ; cycles déclenchés par événement : 8059 ; avance médiane sur le rafraîchissement multicall : 306 ms
- Gaz : base fee 0.007322 gwei ; prix ETH (pool le plus profond) : 2,323.82 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 536 pools, 308 jetons, 19360 routes
- Par DEX : uniswap_v3 143, aerodrome 216, aerodrome_slipstream 133, pancakeswap_v3 29, uniswap_v2 12, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 193 (rejetés 2) → 598 jetons ; pools candidats 3806 (énumérés 348, par paires 0), mesurés 538, sous le plancher de 10000.0 $ : 2 → gardés 536 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDbC': 1.0, 'USDC': 1.0, 'WETH': 2363.674955, 'cbBTC': 80533.217668, 'AERO': 0.705694}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 153,343,827 | 2,323.820851 | 53032538 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,879,387 | 0.029093 | 53032538 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 12,031,315 | 97.872935 | 53032538 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,110,459 | 0.029143 | 53032538 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,527,002 | 0.000013 | 53032538 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome | USDC/AERO | 3000 | 8,844,179 | 1.433134 | 53032538 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/USDC | 500 | 8,422,085 | 2,322.823371 | 53032538 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome_slipstream | WETH/cbBTC | 2615 | 7,948,532 | 0.029128 | 53032538 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,937,565 | 0.001633 | 53032538 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 370 | 6,280,906 | 0.000013 | 53032538 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 1116 | 5,419,200 | 2,323.165823 | 53032538 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,343,366 | 0.029098 | 53032538 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | USDC/cbBTC | 600 | 4,816,234 | 0.000013 | 53032538 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,446,565 | 2,323.470546 | 53032538 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,204,921 | 0.998962 | 53032538 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,847,366 | 34,545.512750 | 53032538 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/USDC | 3000 | 3,793,424 | 2,327.608072 | 53032538 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | WETH/USDT | 484 | 2,747,753 | 2,339.869635 | 53032538 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome_slipstream | WETH/VVV | 2706 | 2,461,619 | 97.900997 | 53032538 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,198,843 | 412.228347 | 53032538 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | WETH/FAI | 10000 | 2,087,251 | 1,256,680.946677 | 53032538 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,904,522 | 0.000013 | 53032538 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | WETH/AERO | 10000 | 1,900,158 | 3,358.807181 | 53032538 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,887,686 | 0.000000 | 53032538 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,795,342 | 0.018151 | 53032538 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,729,133 | 0.000013 | 53032538 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | VIRTUAL/WETH | 10000 | 1,569,307 | 0.000264 | 53032538 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,509,855 | 1.653156 | 53032538 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,457,955 | 0.826792 | 53032538 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,447,243 | 3,333.979825 | 53032538 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,383,641 | 0.005282 | 53032538 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,358,497 | 14,139.564566 | 53032538 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,253,948 | 2,322.833312 | 53032538 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,233,187 | 0.000264 | 53032538 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | USDC/SEND | 3000 | 1,225,057 | 64.748506 | 53032538 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome | WETH/msETH (stable) | 500 | 1,212,799 | 2.301286 | 53032538 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | DRB/WETH | 10000 | 1,181,473 | 0.000000 | 53032538 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/doginme | 10000 | 1,156,696 | 35,471,226.642133 | 53032538 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | USDC/NOCK | 3000 | 1,129,496 | 49.096079 | 53032538 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome | WETH/WELL | 10000 | 1,124,772 | 1,120,998.699385 | 53032538 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,105,843 | 501,975.878905 | 53032538 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,059,421 | 17.188206 | 53032538 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,033,789 | 17.264433 | 53032538 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | WETH/EDEL | 7000 | 1,032,172 | 77,697.963118 | 53032538 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,011,915 | 22,023,300.906432 | 53032538 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 942,383 | 23.321023 | 53032538 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| uniswap_v3 | USDC/VVV | 3000 | 941,851 | 0.042117 | 53032538 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/MORPHO | 3000 | 924,462 | 1,089.228922 | 53032538 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome_slipstream | USDC/SAPIEN | 4620 | 886,684 | 17.698990 | 53032538 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v3 | uXRP/WETH | 3000 | 883,695 | 0.000542 | 53032538 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| uniswap_v3 | WETH/VVV | 10000 | 858,191 | 97.927580 | 53032538 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v2 | WETH/USDC | 3000 | 845,393 | 2,324.879155 | 53032538 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | AERO/cbBTC | 2700 | 837,859 | 0.000009 | 53032538 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| pancakeswap_v3 | QUID/USDC | 100 | 817,759 | 0.060153 | 53032538 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | weETH_04c0/WETH | 500 | 799,788 | 1.105901 | 53032538 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome | WETH/wstETH | 3000 | 786,870 | 0.803010 | 53032538 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | WETH/USDC | 10000 | 779,944 | 2,340.929309 | 53032538 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 745,903 | 0.614876 | 53032538 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 735,608 | 4,709,679.962846 | 53032538 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 722,008 | 0.654138 | 53032538 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |

## Recherche d'opportunités
- Cycles : 14723 ; routes examinées : 285037280 ; candidats optimisés : 1100740 ; net attendu > 0 : 1305 ; dernier cycle 132.9 ms
- Rejets (moteur) : {'spread_below_threshold': 280396168, 'liquidity_below_min': 3355723, 'negative_expected_net': 1099435, 'pool_quarantined': 152276, 'borrow_bound_too_small': 18825, 'unquotable': 9991, 'cycle_budget_exhausted': 3557}
- Enregistrements de la session : 1100740 ; net attendu > 0 : 1305 ; simulés (eth_call de la vraie tx) : 107 (ok 51, échec 56) ; étiquettes ghost N+1 : 10/80 positives
- Décisions : {'REJECTED': 1100740} ; motifs de rejet : {'below_safety_margin': 1033, 'negative_expected_net': 1099435, 'p_lower_below_threshold': 1134, 'reliability_not_demonstrated': 171, 'sim_below_estimate': 7, 'simulated_net_nonpositive': 3, 'simulation_failed': 56, 'stale_data': 6}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53026232 | USDC→[uniswap_v3]→ZORA→[aerodrome_slipstream]→USDC | 451.845630 USDC | 2.035784 USDC | 0.000000 USDC | 0.005666 USDC | 2.030118 USDC (1.8677 €) | — | 44.93 | 0.001 (n=8) | REJECTED | reliability_not_demonstrated |
| 53028022 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 291.241849 USDC | 1.237549 USDC | 0.000000 USDC | 0.005307 USDC | 1.232242 USDC (1.1337 €) | — | 42.31 | 0.001 (n=9) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53032465 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 1.412996 WETH | 0.000431 WETH | 0.000000 WETH | 0.000003 WETH | 0.000428 WETH (0.9176 €) | — | 3.03 | 0.002 (n=120) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 53032465 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 3,281.379921 USDC | 1.002676 USDC | 0.000000 USDC | 0.007024 USDC | 0.995652 USDC (0.9160 €) | — | 3.03 | 0.002 (n=120) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 53031498 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 1,883.586118 USDC | 0.337839 USDC | 0.000000 USDC | 0.006326 USDC | 0.331513 USDC (0.3050 €) | — | 1.76 | 0.017 (n=84) | REJECTED | below_safety_margin(331513<376717), p_lower_below_threshold(0.02<0.75) |
| 53031498 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.803118 WETH | 0.000144 WETH | 0.000000 WETH | 0.000003 WETH | 0.000141 WETH (0.3046 €) | — | 1.76 | 0.017 (n=84) | REJECTED | below_safety_margin(141172880140727<160623590917078), p_lower_below_threshold(0.02<0.75) |
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
| 53032465 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.274749 WETH | 0.000103 WETH | 0.000000 WETH | 0.000003 WETH | 0.000100 WETH (0.2139 €) | — | 3.63 | 0.002 (n=120) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 53032465 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 637.650585 USDC | 0.238805 USDC | 0.000000 USDC | 0.006630 USDC | 0.232175 USDC (0.2136 €) | — | 3.64 | 0.002 (n=120) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53031498 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 1,228.592439 USDC | 0.184708 USDC | 0.000000 USDC | 0.007459 USDC | 0.177249 USDC (0.1631 €) | — | 1.44 | 0.135 (n=278) | REJECTED | below_safety_margin(177249<245718), p_lower_below_threshold(0.14<0.75) |

## Fiabilité et décision
- Observations ghost : 2211 ; taux observé 0.097 ; borne inférieure crédible (0.9) 0.089 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 8.9% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
