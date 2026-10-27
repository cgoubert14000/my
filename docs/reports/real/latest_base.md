# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-27T17:13:33+00:00 ; durée 271.3 min ; blocs 53157790 → 53165928 (7985 vus)

## Connexion
- Requêtes RPC : 94540 ; erreurs : 50 ; latence p50/p95 : 276.8/1,262.6 ms
- Rafraîchissements d'état : 7985 ; âge des données au dernier bloc : 2.61 s ; changements de frais LP observés (pools à frais dynamiques) : 14287
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 90625 ; cycles déclenchés par événement : 6090 ; avance médiane sur le rafraîchissement multicall : 554 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,344.07 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 524 pools, 301 jetons, 19174 routes
- Par DEX : uniswap_v3 145, aerodrome 212, aerodrome_slipstream 123, pancakeswap_v3 28, uniswap_v2 13, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 188 (rejetés 2) → 593 jetons ; pools candidats 3787 (énumérés 335, par paires 0), mesurés 527, sous le plancher de 10000.0 $ : 3 → gardés 524 (max 1500) ; prix des hubs : {'USDC': 1.0, 'USDbC': 1.0, 'DAI': 1.0, 'WETH': 2324.722428, 'cbBTC': 80182.929325, 'AERO': 0.68845}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 157,325,487 | 2,344.067026 | 53165928 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,564,677 | 0.029156 | 53165928 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,178,076 | 0.029106 | 53165928 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,646,874 | 0.000012 | 53165928 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome | WETH/VVV | 3000 | 8,586,243 | 91.364464 | 53165928 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/USDC | 500 | 8,425,249 | 2,349.555495 | 53165928 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | USDC/AERO | 3000 | 7,068,862 | 1.419720 | 53165928 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,993,859 | 0.001638 | 53165928 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,402,101 | 0.029149 | 53165928 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/USDC | 150 | 5,070,342 | 2,349.082386 | 53165928 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,488,359 | 2,349.033563 | 53165928 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,234,873 | 0.998745 | 53165928 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,706,248 | 37,441.866947 | 53165928 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,997,058 | 0.029122 | 53165928 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2700 | 2,565,007 | 91.393584 | 53165928 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | WETH/USDC | 3000 | 2,364,616 | 2,347.119101 | 53165928 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | USDC/cbBTC | 436 | 2,187,554 | 0.000012 | 53165928 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome | WETH/FAI | 10000 | 2,142,595 | 1,213,470.230138 | 53165928 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,853,250 | 0.000000 | 53165928 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,829,597 | 0.018705 | 53165928 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,780,892 | 402.716057 | 53165928 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | USDC/cbBTC | 336 | 1,693,611 | 0.000012 | 53165928 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,684,606 | 0.000012 | 53165928 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,679,214 | 0.000012 | 53165928 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,529,145 | 0.005889 | 53165928 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v3 | WETH/AERO | 3000 | 1,462,620 | 3,334.551053 | 53165928 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,461,016 | 0.826585 | 53165928 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,453,146 | 1.698043 | 53165928 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,381,715 | 13,818.082707 | 53165928 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,249,815 | 0.000267 | 53165928 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,248,759 | 2,349.528662 | 53165928 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | WETH/AERO | 10000 | 1,220,004 | 3,325.169077 | 53165928 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | USDC/SEND | 3000 | 1,201,201 | 67.345844 | 53165928 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome | VIRTUAL/WETH | 10000 | 1,182,684 | 0.000266 | 53165928 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome | WETH/WELL | 10000 | 1,157,965 | 1,074,547.000565 | 53165928 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/doginme | 10000 | 1,156,564 | 36,552,393.297149 | 53165928 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | DRB/WETH | 10000 | 1,149,357 | 0.000000 | 53165928 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,115,188 | 502,651.789572 | 53165928 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | WETH/EDEL | 7000 | 1,077,665 | 72,295.634207 | 53165928 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,050,998 | 21,079,651.469437 | 53165928 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,036,276 | 17.155815 | 53165928 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | USDC/VVV | 3000 | 1,029,299 | 0.038972 | 53165928 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | USDC/NOCK | 3000 | 1,019,890 | 60.181749 | 53165928 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/USDC | 10000 | 943,638 | 2,328.125208 | 53165928 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 912,087 | 1,084.371397 | 53165928 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | uXRP/WETH | 3000 | 906,227 | 0.000560 | 53165928 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| uniswap_v3 | WETH/VVV | 10000 | 896,352 | 91.133759 | 53165928 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome | WETH/msETH (stable) | 500 | 884,418 | 2.315987 | 53165928 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 880,416 | 17.931797 | 53165928 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v2 | WETH/USDC | 3000 | 849,295 | 2,344.982495 | 53165928 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 838,741 | 17.670827 | 53165928 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 814,197 | 0.000009 | 53165928 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| pancakeswap_v3 | QUID/USDC | 100 | 801,639 | 0.057654 | 53165928 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 793,642 | 0.803179 | 53165928 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 752,081 | 4,585,831.306106 | 53165928 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 749,331 | 0.625070 | 53165928 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/NPC | 3000 | 701,832 | 140,413.465223 | 53165928 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 695,997 | 499,464.100958 | 53165928 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | TIG/USDC | 10000 | 681,845 | 0.585412 | 53165928 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 673,803 | 0.108684 | 53165928 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |

## Recherche d'opportunités
- Cycles : 14074 ; routes examinées : 269854876 ; candidats optimisés : 900179 ; net attendu > 0 : 419 ; dernier cycle 446.3 ms
- Rejets (moteur) : {'spread_below_threshold': 265529645, 'liquidity_below_min': 3335319, 'negative_expected_net': 899760, 'borrow_bound_too_small': 87707, 'cycle_budget_exhausted': 2026}
- Enregistrements de la session : 900179 ; net attendu > 0 : 419 ; simulés (eth_call de la vraie tx) : 25 (ok 7, échec 18) ; étiquettes ghost N+1 : 3/24 positives
- Décisions : {'REJECTED': 900179} ; motifs de rejet : {'below_safety_margin': 343, 'negative_expected_net': 899760, 'p_lower_below_threshold': 393, 'reliability_not_demonstrated': 26, 'sim_below_estimate': 3, 'simulated_net_nonpositive': 3, 'simulation_failed': 18, 'stale_data': 38}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53163475 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.004089 cbBTC | 0.000004 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000004 cbBTC (0.2877 €) | — | 9.51 | 0.000 (n=61) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53163475 | WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.146914 WETH | 0.000136 WETH | 0.000000 WETH | 0.000003 WETH | 0.000133 WETH (0.2868 €) | — | 9.05 | 0.000 (n=61) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 53163475 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 272.922832 USDC | 0.240492 USDC | 0.000000 USDC | 0.007090 USDC | 0.233402 USDC (0.2147 €) | — | 8.55 | 0.000 (n=61) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53163475 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.003154 cbBTC | 0.000003 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000003 cbBTC (0.2145 €) | — | 9.19 | 0.000 (n=61) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53159906 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.794482 WETH | 0.000094 WETH | 0.000000 WETH | 0.000002 WETH | 0.000091 WETH (0.1957 €) | — | 1.15 | 0.020 (n=106) | REJECTED | below_safety_margin(91426168727046<158896479878237), p_lower_below_threshold(0.02<0.75) |
| 53159907 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.794482 WETH | 0.000094 WETH | 0.000000 WETH | 0.000002 WETH | 0.000091 WETH (0.1957 €) | — | 1.15 | 0.020 (n=106) | REJECTED | below_safety_margin(91426168727046<158896479878237), p_lower_below_threshold(0.02<0.75) |
| 53159906 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 1,843.634528 USDC | 0.217677 USDC | 0.000000 USDC | 0.005610 USDC | 0.212067 USDC (0.1951 €) | — | 1.15 | 0.020 (n=106) | REJECTED | below_safety_margin(212067<368726), p_lower_below_threshold(0.02<0.75) |
| 53159907 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 1,843.634528 USDC | 0.217677 USDC | 0.000000 USDC | 0.005610 USDC | 0.212067 USDC (0.1951 €) | — | 1.15 | 0.020 (n=106) | REJECTED | below_safety_margin(212067<368726), p_lower_below_threshold(0.02<0.75) |
| 53163475 | cbBTC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.002668 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1708 €) | — | 8.66 | 0.000 (n=61) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53163475 | WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→WETH | 0.095794 WETH | 0.000082 WETH | 0.000000 WETH | 0.000003 WETH | 0.000079 WETH (0.1701 €) | — | 8.23 | 0.000 (n=61) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 53163475 | cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.002651 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1523 €) | — | 7.77 | 0.124 (n=165) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 53163475 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→USDC | 218.103405 USDC | 0.172592 USDC | 0.000000 USDC | 0.007090 USDC | 0.165502 USDC (0.1523 €) | — | 7.59 | 0.124 (n=165) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 53163475 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.002524 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1220 €) | — | 6.54 | 0.094 (n=302) | REJECTED | p_lower_below_threshold(0.09<0.75) |
| 53163475 | WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.087276 WETH | 0.000059 WETH | 0.000000 WETH | 0.000003 WETH | 0.000056 WETH (0.1216 €) | — | 6.46 | 0.094 (n=302) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.09<0.75) |
| 53162545 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 1,457.453219 USDC | 0.137624 USDC | 0.000000 USDC | 0.005604 USDC | 0.132020 USDC (0.1215 €) | — | 0.91 | 0.020 (n=106) | REJECTED | below_safety_margin(132020<291490), p_lower_below_threshold(0.02<0.75) |
| 53162547 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 1,457.453219 USDC | 0.137624 USDC | 0.000000 USDC | 0.005604 USDC | 0.132020 USDC (0.1215 €) | — | 0.91 | 0.020 (n=106) | REJECTED | below_safety_margin(132020<291490), p_lower_below_threshold(0.02<0.75) |
| 53162545 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.624317 WETH | 0.000059 WETH | 0.000000 WETH | 0.000002 WETH | 0.000056 WETH (0.1211 €) | — | 0.90 | 0.020 (n=106) | REJECTED | below_safety_margin(56476157983539<124863325293708), p_lower_below_threshold(0.02<0.75) |
| 53162547 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.624317 WETH | 0.000059 WETH | 0.000000 WETH | 0.000002 WETH | 0.000056 WETH (0.1211 €) | — | 0.90 | 0.020 (n=106) | REJECTED | below_safety_margin(56476157983539<124863325293708), p_lower_below_threshold(0.02<0.75) |
| 53162317 | WETH→[uniswap_v3]→VIRTUAL→[aerodrome_slipstream]→WETH | 0.102608 WETH | 0.000057 WETH | 0.000000 WETH | 0.000002 WETH | 0.000054 WETH (0.1168 €) | — | 5.31 | 0.047 (n=45) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.05<0.75) |
| 53163475 | cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.002260 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1124 €) | — | 6.73 | 0.124 (n=165) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 53163475 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→USDC | 183.933967 USDC | 0.129150 USDC | 0.000000 USDC | 0.007090 USDC | 0.122060 USDC (0.1123 €) | — | 6.64 | 0.124 (n=165) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 53163475 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[uniswap_v3]→USDC | 196.102605 USDC | 0.127845 USDC | 0.000000 USDC | 0.007090 USDC | 0.120755 USDC (0.1111 €) | — | 6.16 | 0.124 (n=165) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 53163475 | cbBTC→[uniswap_v3]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.002307 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1109 €) | — | 6.50 | 0.124 (n=165) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 53163475 | cbBTC→[uniswap_v3]→WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.002404 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.1050 €) | — | 5.91 | 0.094 (n=302) | REJECTED | p_lower_below_threshold(0.09<0.75) |
| 53163475 | WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[uniswap_v3]→WETH | 0.087276 WETH | 0.000052 WETH | 0.000000 WETH | 0.000003 WETH | 0.000049 WETH (0.1050 €) | — | 5.58 | 0.094 (n=302) | REJECTED | p_lower_below_threshold(0.09<0.75) |

## Fiabilité et décision
- Observations ghost : 2856 ; taux observé 0.090 ; borne inférieure crédible (0.9) 0.084 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 8.4% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
