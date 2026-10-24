# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-24T15:13:30+00:00 ; durée 229.24 min ; blocs 53025852 → 53032727 (6850 vus)

## Connexion
- Requêtes RPC : 85527 ; erreurs : 23 ; latence p50/p95 : 192.9/542.4 ms
- Rafraîchissements d'état : 6850 ; âge des données au dernier bloc : 3.0 s ; changements de frais LP observés (pools à frais dynamiques) : 11192
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 121922 ; cycles déclenchés par événement : 8299 ; avance médiane sur le rafraîchissement multicall : 293 ms
- Gaz : base fee 0.009706 gwei ; prix ETH (pool le plus profond) : 2,314.77 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 536 pools, 308 jetons, 19360 routes
- Par DEX : uniswap_v3 143, aerodrome 216, aerodrome_slipstream 133 (quarantaine 1), pancakeswap_v3 29 (quarantaine 1), uniswap_v2 12, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 193 (rejetés 2) → 598 jetons ; pools candidats 3806 (énumérés 348, par paires 0), mesurés 538, sous le plancher de 10000.0 $ : 2 → gardés 536 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDbC': 1.0, 'USDC': 1.0, 'WETH': 2363.674955, 'cbBTC': 80533.217668, 'AERO': 0.705694}
- Pools en quarantaine : 2 — aerodrome_slipstream:WETH/USDT@0x9785eF: simulation failed ×5 (model/chain mismatch) — until block 53032875; pancakeswap_v3:USDC/USDT@0x5f07bb: simulation failed ×5 (model/chain mismatch) — until block 53032875

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 152,962,776 | 2,314.770253 | 53032728 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,813,021 | 0.029044 | 53032728 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 11,994,307 | 97.712079 | 53032728 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,076,535 | 0.029090 | 53032728 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,550,861 | 0.000013 | 53032728 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome | USDC/AERO | 3000 | 8,844,531 | 1.433020 | 53032728 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/USDC | 500 | 8,420,492 | 2,314.613124 | 53032728 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome_slipstream | WETH/cbBTC | 2560 | 7,922,726 | 0.029076 | 53032728 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,921,039 | 0.001633 | 53032728 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 346 | 6,273,367 | 0.000013 | 53032728 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 862 | 5,391,343 | 2,313.976285 | 53032728 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,330,991 | 0.029038 | 53032728 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | USDC/cbBTC | 496 | 4,809,419 | 0.000013 | 53032728 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,432,119 | 2,313.696085 | 53032728 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,195,680 | 0.998962 | 53032728 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,839,977 | 34,408.991463 | 53032728 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/USDC | 3000 | 3,786,030 | 2,314.685461 | 53032728 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | WETH/USDT | 502 | 2,740,100 | 2,328.137000 | 53032728 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome_slipstream | WETH/VVV | 2757 | 2,454,159 | 97.694060 | 53032728 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,191,188 | 411.781025 | 53032728 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | WETH/FAI | 10000 | 2,079,122 | 1,256,680.946677 | 53032728 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,900,361 | 0.000013 | 53032728 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | WETH/AERO | 10000 | 1,896,534 | 3,349.192070 | 53032728 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,880,332 | 0.000000 | 53032728 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,778,112 | 0.017875 | 53032728 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,726,608 | 0.000013 | 53032728 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | VIRTUAL/WETH | 10000 | 1,563,195 | 0.000264 | 53032728 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,509,855 | 1.653156 | 53032728 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,457,952 | 0.826796 | 53032728 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,444,608 | 3,325.881223 | 53032728 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,376,194 | 0.005273 | 53032728 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,355,181 | 14,149.490462 | 53032728 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,250,138 | 2,314.786592 | 53032728 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,228,387 | 0.000265 | 53032728 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | USDC/SEND | 3000 | 1,225,022 | 64.752152 | 53032728 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome | WETH/msETH (stable) | 500 | 1,208,076 | 2.301286 | 53032728 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | DRB/WETH | 10000 | 1,176,246 | 0.000000 | 53032728 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/doginme | 10000 | 1,152,526 | 35,471,226.642133 | 53032728 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | USDC/NOCK | 3000 | 1,129,250 | 49.117508 | 53032728 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome | WETH/WELL | 10000 | 1,120,391 | 1,120,998.699385 | 53032728 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,101,536 | 501,975.878905 | 53032728 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,057,013 | 17.149607 | 53032728 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,037,101 | 17.135697 | 53032728 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | WETH/EDEL | 7000 | 1,029,580 | 77,482.602992 | 53032728 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,009,150 | 21,979,413.909832 | 53032728 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | USDC/VVV | 3000 | 940,414 | 0.042155 | 53032728 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 938,773 | 23.318715 | 53032728 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| uniswap_v3 | WETH/MORPHO | 3000 | 922,753 | 1,087.116721 | 53032728 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome_slipstream | USDC/SAPIEN | 4545 | 886,064 | 17.719544 | 53032728 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v3 | uXRP/WETH | 3000 | 881,580 | 0.000544 | 53032728 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| uniswap_v3 | WETH/VVV | 10000 | 855,521 | 97.927578 | 53032728 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v2 | WETH/USDC | 3000 | 843,749 | 2,314.806165 | 53032728 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 837,007 | 0.000009 | 53032728 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| pancakeswap_v3 | QUID/USDC | 100 | 820,020 | 0.060510 | 53032728 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | weETH_04c0/WETH | 500 | 796,673 | 1.105901 | 53032728 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome | WETH/wstETH | 3000 | 783,805 | 0.803010 | 53032728 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | WETH/USDC | 10000 | 778,969 | 2,327.627525 | 53032728 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 743,670 | 0.614139 | 53032728 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 733,191 | 4,703,937.242349 | 53032728 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 722,008 | 0.654138 | 53032728 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |

## Recherche d'opportunités
- Cycles : 15148 ; routes examinées : 293265280 ; candidats optimisés : 1145220 ; net attendu > 0 : 1758 ; dernier cycle 255.2 ms
- Rejets (moteur) : {'spread_below_threshold': 288319786, 'liquidity_below_min': 3490097, 'negative_expected_net': 1143462, 'pool_quarantined': 269916, 'borrow_bound_too_small': 24434, 'unquotable': 11197, 'cycle_budget_exhausted': 4630}
- Enregistrements de la session : 1145220 ; net attendu > 0 : 1758 ; simulés (eth_call de la vraie tx) : 119 (ok 51, échec 68) ; étiquettes ghost N+1 : 13/92 positives
- Décisions : {'REJECTED': 1145220} ; motifs de rejet : {'below_safety_margin': 1174, 'negative_expected_net': 1143462, 'p_lower_below_threshold': 1538, 'reliability_not_demonstrated': 220, 'sim_below_estimate': 7, 'simulated_net_nonpositive': 3, 'simulation_failed': 68, 'stale_data': 6}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53032626 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 1.332835 WETH | 0.000923 WETH | 0.000000 WETH | 0.000003 WETH | 0.000919 WETH (1.9605 €) | — | 6.90 | 0.002 (n=123) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 53032626 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 3,086.282102 USDC | 2.136965 USDC | 0.000000 USDC | 0.007231 USDC | 2.129734 USDC (1.9594 €) | — | 6.90 | 0.002 (n=123) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53026232 | USDC→[uniswap_v3]→ZORA→[aerodrome_slipstream]→USDC | 451.845630 USDC | 2.035784 USDC | 0.000000 USDC | 0.005666 USDC | 2.030118 USDC (1.8677 €) | — | 44.93 | 0.001 (n=8) | REJECTED | reliability_not_demonstrated |
| 53032626 | WETH→[pancakeswap_v3]→cbBTC→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 1.170560 WETH | 0.000841 WETH | 0.000000 WETH | 0.000004 WETH | 0.000837 WETH (1.7841 €) | — | 7.15 | 0.097 (n=228) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.10<0.75) |
| 53032626 | cbBTC→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.033654 cbBTC | 0.000024 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000024 cbBTC (1.7829 €) | — | 7.22 | 0.097 (n=228) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53032626 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[uniswap_v3]→USDC | 2,757.298059 USDC | 1.947708 USDC | 0.000000 USDC | 0.009813 USDC | 1.937895 USDC (1.7829 €) | — | 7.03 | 0.097 (n=228) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53032626 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 1.062736 WETH | 0.000765 WETH | 0.000000 WETH | 0.000003 WETH | 0.000762 WETH (1.6241 €) | — | 7.17 | — (n=0) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53032626 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 2,459.190455 USDC | 1.771885 USDC | 0.000000 USDC | 0.008089 USDC | 1.763796 USDC (1.6227 €) | — | 7.17 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 53032626 | WETH→[uniswap_v3]→cbBTC→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 1.160307 WETH | 0.000755 WETH | 0.000000 WETH | 0.000004 WETH | 0.000751 WETH (1.6014 €) | — | 6.47 | 0.097 (n=228) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53032626 | cbBTC→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→cbBTC | 0.033108 cbBTC | 0.000022 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000022 cbBTC (1.6003 €) | — | 6.59 | 0.097 (n=228) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53032626 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→cbBTC→[uniswap_v3]→USDC | 2,687.066121 USDC | 1.748437 USDC | 0.000000 USDC | 0.009384 USDC | 1.739053 USDC (1.5999 €) | — | 6.47 | 0.097 (n=228) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53032626 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 1.002486 WETH | 0.000652 WETH | 0.000000 WETH | 0.000004 WETH | 0.000648 WETH (1.3825 €) | — | 6.47 | 0.097 (n=228) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53032626 | cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.029053 cbBTC | 0.000019 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000019 cbBTC (1.3825 €) | — | 6.49 | 0.097 (n=228) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53032626 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 2,332.393912 USDC | 1.510907 USDC | 0.000000 USDC | 0.009384 USDC | 1.501523 USDC (1.3814 €) | — | 6.44 | 0.097 (n=228) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53032626 | WETH→[uniswap_v3]→cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.977188 WETH | 0.000572 WETH | 0.000000 WETH | 0.000004 WETH | 0.000568 WETH (1.2118 €) | — | 5.82 | 0.097 (n=228) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53032626 | cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→cbBTC | 0.028024 cbBTC | 0.000017 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000017 cbBTC (1.2116 €) | — | 5.89 | 0.097 (n=228) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53032626 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 2,265.762058 USDC | 1.324881 USDC | 0.000000 USDC | 0.008955 USDC | 1.315926 USDC (1.2107 €) | — | 5.81 | 0.097 (n=228) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53032626 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.980915 WETH | 0.000559 WETH | 0.000000 WETH | 0.000003 WETH | 0.000556 WETH (1.1857 €) | — | 5.67 | 0.002 (n=123) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53032626 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 2,270.455169 USDC | 1.294786 USDC | 0.000000 USDC | 0.007231 USDC | 1.287555 USDC (1.1846 €) | — | 5.67 | 0.002 (n=123) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53028022 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 291.241849 USDC | 1.237549 USDC | 0.000000 USDC | 0.005307 USDC | 1.232242 USDC (1.1337 €) | — | 42.31 | 0.001 (n=9) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53032626 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.780902 WETH | 0.000488 WETH | 0.000000 WETH | 0.000004 WETH | 0.000484 WETH (1.0322 €) | — | 6.20 | 0.002 (n=3) | REJECTED | reliability_not_demonstrated |
| 53032626 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.022442 cbBTC | 0.000014 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000014 cbBTC (1.0312 €) | — | 6.26 | 0.002 (n=3) | REJECTED | reliability_not_demonstrated |
| 53032626 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 1,871.420995 USDC | 1.130130 USDC | 0.000000 USDC | 0.010241 USDC | 1.119889 USDC (1.0303 €) | — | 5.98 | 0.002 (n=3) | REJECTED | reliability_not_demonstrated |
| 53032465 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 1.412996 WETH | 0.000431 WETH | 0.000000 WETH | 0.000003 WETH | 0.000428 WETH (0.9176 €) | — | 3.03 | 0.002 (n=120) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 53032465 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 3,281.379921 USDC | 1.002676 USDC | 0.000000 USDC | 0.007024 USDC | 0.995652 USDC (0.9160 €) | — | 3.03 | 0.002 (n=120) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |

## Fiabilité et décision
- Observations ghost : 2223 ; taux observé 0.098 ; borne inférieure crédible (0.9) 0.090 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 9.0% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
