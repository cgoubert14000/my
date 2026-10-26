# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-26T19:19:31+00:00 ; durée 306.41 min ; blocs 53117317 → 53126505 (8579 vus)

## Connexion
- Requêtes RPC : 109172 ; erreurs : 145 ; latence p50/p95 : 86.1/858.4 ms
- Rafraîchissements d'état : 8580 ; âge des données au dernier bloc : 1.87 s ; changements de frais LP observés (pools à frais dynamiques) : 19380
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 133995 ; cycles déclenchés par événement : 13926 ; avance médiane sur le rafraîchissement multicall : 261 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,315.80 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 529 pools, 304 jetons, 19426 routes
- Par DEX : uniswap_v3 143, aerodrome 213, aerodrome_slipstream 128, pancakeswap_v3 29, uniswap_v2 13, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 189 (rejetés 2) → 594 jetons ; pools candidats 3787 (énumérés 341, par paires 0), mesurés 532, sous le plancher de 10000.0 $ : 3 → gardés 529 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2307.602823, 'cbBTC': 79842.460004, 'AERO': 0.67568}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 135,340,490 | 2,315.798261 | 53126505 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,747,562 | 0.028948 | 53126505 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,148,473 | 0.028964 | 53126505 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,475,759 | 0.000013 | 53126505 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome | WETH/VVV | 3000 | 8,894,683 | 91.713528 | 53126505 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/USDC | 500 | 8,317,626 | 2,316.246124 | 53126505 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | USDC/AERO | 3000 | 7,082,346 | 1.460189 | 53126505 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,969,317 | 0.001643 | 53126505 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,359,455 | 0.028959 | 53126505 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/USDC | 150 | 5,282,278 | 2,316.465734 | 53126505 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,507,032 | 2,316.625447 | 53126505 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,210,214 | 0.999579 | 53126505 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,782,258 | 35,090.174222 | 53126505 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/USDC | 3000 | 3,361,458 | 2,317.773732 | 53126505 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 3,185,209 | 0.028951 | 53126505 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2733 | 2,510,202 | 91.733076 | 53126505 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | USDC/cbBTC | 436 | 2,463,449 | 0.000013 | 53126505 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome | WETH/FAI | 10000 | 2,121,862 | 1,207,636.783972 | 53126505 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,902,520 | 0.000012 | 53126505 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,833,657 | 0.000000 | 53126505 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,823,937 | 0.018378 | 53126505 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,752,545 | 407.464538 | 53126505 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,712,966 | 0.000013 | 53126505 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | USDC/cbBTC | 336 | 1,697,148 | 0.000013 | 53126505 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | VIRTUAL/WETH | 10000 | 1,550,616 | 0.000266 | 53126505 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,480,853 | 0.005750 | 53126505 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,460,756 | 0.826133 | 53126505 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,453,150 | 1.698035 | 53126505 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | WETH/AERO | 3000 | 1,440,066 | 3,381.379420 | 53126505 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,364,539 | 14,085.692459 | 53126505 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,233,640 | 0.000266 | 53126505 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | USDC/SEND | 3000 | 1,220,089 | 65.276830 | 53126505 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome | WETH/AERO | 10000 | 1,216,247 | 3,388.322097 | 53126505 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,174,533 | 2,316.238049 | 53126505 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | DRB/WETH | 10000 | 1,151,835 | 0.000000 | 53126505 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | WETH/WELL | 10000 | 1,137,007 | 1,088,398.355637 | 53126505 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/doginme | 10000 | 1,134,851 | 37,123,987.616527 | 53126505 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,106,868 | 496,061.155820 | 53126505 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | WETH/EDEL | 7000 | 1,068,831 | 71,934.992349 | 53126505 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,057,895 | 20,374,467.033949 | 53126505 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome | USDC/NOCK | 3000 | 1,057,110 | 56.018436 | 53126505 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,030,358 | 17.424516 | 53126505 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | USDC/VVV | 3000 | 1,007,322 | 0.039601 | 53126505 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/USDC | 10000 | 951,339 | 2,317.651152 | 53126505 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 906,730 | 1,102.603108 | 53126505 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome | WETH/msETH (stable) | 500 | 905,233 | 2.309155 | 53126505 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | uXRP/WETH | 3000 | 892,312 | 0.000557 | 53126505 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 879,171 | 17.966876 | 53126505 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 875,463 | 17.127755 | 53126505 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| uniswap_v3 | WETH/VVV | 10000 | 873,833 | 91.816361 | 53126505 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v2 | WETH/USDC | 3000 | 844,079 | 2,315.970397 | 53126505 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 804,291 | 0.000009 | 53126505 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| pancakeswap_v3 | QUID/USDC | 100 | 794,068 | 0.056514 | 53126505 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 784,087 | 0.803146 | 53126505 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 745,692 | 0.614667 | 53126505 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 734,361 | 4,694,714.685888 | 53126505 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 700,790 | 0.617472 | 53126505 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/NPC | 3000 | 698,783 | 138,225.760033 | 53126505 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 692,328 | 499,772.500791 | 53126505 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 678,299 | 0.109956 | 53126505 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |

## Recherche d'opportunités
- Cycles : 22505 ; routes examinées : 437182130 ; candidats optimisés : 1361134 ; net attendu > 0 : 2327 ; dernier cycle 101.6 ms
- Rejets (moteur) : {'spread_below_threshold': 429460979, 'liquidity_below_min': 5556918, 'negative_expected_net': 1358807, 'pool_quarantined': 445344, 'unquotable': 334479, 'borrow_bound_too_small': 22569, 'cycle_budget_exhausted': 701, 'no_price_reference': 6}
- Enregistrements de la session : 1361134 ; net attendu > 0 : 2327 ; simulés (eth_call de la vraie tx) : 116 (ok 26, échec 90) ; étiquettes ghost N+1 : 3/98 positives
- Décisions : {'REJECTED': 1361134} ; motifs de rejet : {'below_safety_margin': 1934, 'negative_expected_net': 1358807, 'p_lower_below_threshold': 2046, 'price_impact': 6, 'reliability_not_demonstrated': 281, 'sim_below_estimate': 1, 'simulated_net_nonpositive': 1, 'simulation_failed': 90, 'stale_data': 16}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53122913 | WETH→[uniswap_v3]→BNKR→[aerodrome_slipstream]→WETH | 0.163867 WETH | 0.004067 WETH | 0.000000 WETH | 0.000002 WETH | 0.004064 WETH (8.7015 €) | — | 248.03 | 0.006 (n=1) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53120051 | USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 120.329548 USDC | 3.139296 USDC | 0.000000 USDC | 0.007146 USDC | 3.132150 USDC (2.8816 €) | — | 260.30 | 0.000 (n=19) | REJECTED | reliability_not_demonstrated |
| 53120051 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→WETH | 0.051530 WETH | 0.001344 WETH | 0.000000 WETH | 0.000003 WETH | 0.001341 WETH (2.8804 €) | — | 260.30 | 0.000 (n=19) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53120051 | USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 119.713759 USDC | 3.116817 USDC | 0.000000 USDC | 0.007146 USDC | 3.109671 USDC (2.8609 €) | — | 259.76 | 0.000 (n=25) | REJECTED | reliability_not_demonstrated |
| 53120051 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→WETH | 0.051278 WETH | 0.001335 WETH | 0.000000 WETH | 0.000003 WETH | 0.001332 WETH (2.8603 €) | — | 259.76 | 0.000 (n=25) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53120051 | USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 115.301260 USDC | 3.033443 USDC | 0.000000 USDC | 0.007146 USDC | 3.026297 USDC (2.7842 €) | — | 262.47 | 0.000 (n=25) | REJECTED | reliability_not_demonstrated |
| 53120051 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→WETH | 0.049386 WETH | 0.001299 WETH | 0.000000 WETH | 0.000003 WETH | 0.001296 WETH (2.7835 €) | — | 262.47 | 0.000 (n=25) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53120051 | USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 115.154911 USDC | 3.028476 USDC | 0.000000 USDC | 0.007146 USDC | 3.021330 USDC (2.7796 €) | — | 262.37 | 0.000 (n=19) | REJECTED | reliability_not_demonstrated |
| 53120051 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→WETH | 0.049326 WETH | 0.001297 WETH | 0.000000 WETH | 0.000003 WETH | 0.001294 WETH (2.7791 €) | — | 262.37 | 0.000 (n=19) | REJECTED | reliability_not_demonstrated |
| 53120051 | WETH→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→WETH | 0.048654 WETH | 0.001267 WETH | 0.000000 WETH | 0.000003 WETH | 0.001264 WETH (2.7145 €) | — | 259.81 | 0.000 (n=25) | REJECTED | reliability_not_demonstrated |
| 53120051 | USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→USDC | 113.547212 USDC | 2.957246 USDC | 0.000000 USDC | 0.007146 USDC | 2.950100 USDC (2.7141 €) | — | 259.81 | 0.000 (n=25) | REJECTED | reliability_not_demonstrated |
| 53120051 | WETH→[sushiswap_v3]→USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→WETH | 0.047938 WETH | 0.001256 WETH | 0.000000 WETH | 0.000003 WETH | 0.001253 WETH (2.6908 €) | — | 261.38 | 0.000 (n=25) | REJECTED | reliability_not_demonstrated |
| 53120051 | USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→WETH→[sushiswap_v3]→USDC | 111.792861 USDC | 2.929583 USDC | 0.000000 USDC | 0.007501 USDC | 2.922082 USDC (2.6883 €) | — | 261.38 | 0.000 (n=25) | REJECTED | reliability_not_demonstrated |
| 53120051 | WETH→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→WETH | 0.044259 WETH | 0.001167 WETH | 0.000000 WETH | 0.000003 WETH | 0.001164 WETH (2.5005 €) | — | 263.10 | 0.000 (n=25) | REJECTED | reliability_not_demonstrated |
| 53120051 | USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→USDC | 102.848347 USDC | 2.713047 USDC | 0.000000 USDC | 0.007146 USDC | 2.705901 USDC (2.4894 €) | — | 263.10 | 0.000 (n=25) | REJECTED | reliability_not_demonstrated |
| 53120051 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→WETH | 0.036019 WETH | 0.000920 WETH | 0.000000 WETH | 0.000003 WETH | 0.000917 WETH (1.9700 €) | — | 254.70 | 0.000 (n=25) | REJECTED | reliability_not_demonstrated |
| 53120051 | USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 83.821865 USDC | 2.142059 USDC | 0.000000 USDC | 0.007146 USDC | 2.134913 USDC (1.9641 €) | — | 254.70 | 0.000 (n=25) | REJECTED | reliability_not_demonstrated |
| 53120051 | WETH→[aerodrome]→USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→WETH | 0.035761 WETH | 0.000908 WETH | 0.000000 WETH | 0.000003 WETH | 0.000905 WETH (1.9441 €) | — | 253.16 | 0.001 (n=10) | REJECTED | reliability_not_demonstrated |
| 53120051 | USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→WETH→[aerodrome]→USDC | 83.188586 USDC | 2.112793 USDC | 0.000000 USDC | 0.006824 USDC | 2.105969 USDC (1.9375 €) | — | 253.16 | 0.001 (n=10) | REJECTED | reliability_not_demonstrated |
| 53120051 | WETH→[uniswap_v2]→USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→WETH | 0.034992 WETH | 0.000893 WETH | 0.000000 WETH | 0.000003 WETH | 0.000890 WETH (1.9111 €) | — | 254.33 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 53120051 | USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→WETH→[uniswap_v2]→USDC | 81.353474 USDC | 2.075483 USDC | 0.000000 USDC | 0.006421 USDC | 2.069062 USDC (1.9035 €) | — | 254.33 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 53123340 | WETH→[aerodrome]→MOR→[uniswap_v3]→WETH | 0.042448 WETH | 0.000536 WETH | 0.000000 WETH | 0.000002 WETH | 0.000534 WETH (1.1428 €) | — | 125.75 | 0.001 (n=11) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53124392 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 1,498.536782 USDC | 0.938386 USDC | 0.000000 USDC | 0.006990 USDC | 0.931396 USDC (0.8569 €) | — | 6.22 | 0.002 (n=141) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53124392 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.645400 WETH | 0.000403 WETH | 0.000000 WETH | 0.000003 WETH | 0.000400 WETH (0.8557 €) | — | 6.20 | 0.002 (n=141) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 53124827 | WETH→[uniswap_v3]→MEY→[aerodrome]→WETH | 0.068449 WETH | 0.000392 WETH | 0.000000 WETH | 0.000002 WETH | 0.000390 WETH (0.8330 €) | — | 56.95 | 0.001 (n=12) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |

## Fiabilité et décision
- Observations ghost : 2722 ; taux observé 0.093 ; borne inférieure crédible (0.9) 0.086 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 8.6% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
