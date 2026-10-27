# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-27T15:22:57+00:00 ; durée 160.69 min ; blocs 53157790 → 53162611 (4749 vus)

## Connexion
- Requêtes RPC : 57254 ; erreurs : 20 ; latence p50/p95 : 317.8/1,218.2 ms
- Rafraîchissements d'état : 4749 ; âge des données au dernier bloc : 2.71 s ; changements de frais LP observés (pools à frais dynamiques) : 9017
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 70078 ; cycles déclenchés par événement : 4705 ; avance médiane sur le rafraîchissement multicall : 1,348 ms
- Gaz : base fee 0.005402 gwei ; prix ETH (pool le plus profond) : 2,344.97 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 524 pools, 301 jetons, 19174 routes
- Par DEX : uniswap_v3 145, aerodrome 212, aerodrome_slipstream 123, pancakeswap_v3 28, uniswap_v2 13, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 188 (rejetés 2) → 593 jetons ; pools candidats 3787 (énumérés 335, par paires 0), mesurés 527, sous le plancher de 10000.0 $ : 3 → gardés 524 (max 1500) ; prix des hubs : {'USDC': 1.0, 'USDbC': 1.0, 'DAI': 1.0, 'WETH': 2324.722428, 'cbBTC': 80182.929325, 'AERO': 0.68845}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 157,363,220 | 2,344.966188 | 53162612 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,426,392 | 0.029173 | 53162612 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,179,759 | 0.029106 | 53162612 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,647,787 | 0.000012 | 53162612 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome | WETH/VVV | 3000 | 8,655,322 | 90.644987 | 53162612 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/USDC | 500 | 8,419,275 | 2,346.412111 | 53162612 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | USDC/AERO | 3000 | 7,047,842 | 1.435885 | 53162612 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,995,309 | 0.001640 | 53162612 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,403,865 | 0.029161 | 53162612 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/USDC | 1160 | 5,131,224 | 2,345.595345 | 53162612 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,487,869 | 2,345.766761 | 53162612 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,233,803 | 0.998745 | 53162612 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,701,536 | 37,566.054011 | 53162612 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2615 | 3,198,511 | 0.029122 | 53162612 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2754 | 2,573,192 | 90.672743 | 53162612 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | WETH/USDC | 3000 | 2,366,538 | 2,345.991323 | 53162612 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | USDC/cbBTC | 600 | 2,194,747 | 0.000012 | 53162612 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome | WETH/FAI | 10000 | 2,138,129 | 1,219,479.503228 | 53162612 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,853,862 | 0.000000 | 53162612 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,833,383 | 0.018777 | 53162612 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,777,867 | 405.467975 | 53162612 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,696,892 | 0.000012 | 53162612 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | USDC/cbBTC | 368 | 1,693,315 | 0.000012 | 53162612 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,668,432 | 0.000012 | 53162612 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,531,218 | 0.005896 | 53162612 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,460,824 | 0.826783 | 53162612 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,453,146 | 1.698043 | 53162612 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | WETH/AERO | 3000 | 1,452,330 | 3,358.913430 | 53162612 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,378,069 | 13,924.986451 | 53162612 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,249,153 | 0.000266 | 53162612 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,239,348 | 2,346.487581 | 53162612 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | WETH/AERO | 10000 | 1,215,781 | 3,375.659529 | 53162612 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | USDC/SEND | 3000 | 1,201,426 | 67.320630 | 53162612 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome | VIRTUAL/WETH | 10000 | 1,182,060 | 0.000266 | 53162612 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome | WETH/WELL | 10000 | 1,160,767 | 1,070,187.443004 | 53162612 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | DRB/WETH | 10000 | 1,157,993 | 0.000000 | 53162612 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/doginme | 10000 | 1,150,529 | 37,177,108.460802 | 53162612 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,114,120 | 504,494.247202 | 53162612 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | WETH/EDEL | 7000 | 1,078,596 | 72,226.306141 | 53162612 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,053,033 | 21,195,085.327228 | 53162612 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,037,257 | 17.111656 | 53162612 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | USDC/VVV | 3000 | 1,034,391 | 0.038749 | 53162612 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | USDC/NOCK | 3000 | 1,022,680 | 59.853868 | 53162612 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/USDC | 10000 | 943,774 | 2,328.125208 | 53162612 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome | WETH/msETH (stable) | 500 | 916,374 | 2.310136 | 53162612 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | WETH/MORPHO | 3000 | 913,516 | 1,082.050535 | 53162612 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | uXRP/WETH | 3000 | 906,617 | 0.000560 | 53162612 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| uniswap_v3 | WETH/VVV | 10000 | 897,946 | 91.133788 | 53162612 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome_slipstream | USDC/SAPIEN | 4715 | 877,352 | 18.033213 | 53162612 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v2 | WETH/USDC | 3000 | 849,458 | 2,344.019610 | 53162612 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 837,565 | 17.704961 | 53162612 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 810,679 | 0.000009 | 53162612 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| pancakeswap_v3 | QUID/USDC | 100 | 799,170 | 0.057280 | 53162612 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 793,946 | 0.803179 | 53162612 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 752,232 | 4,587,499.523891 | 53162612 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 748,303 | 0.623858 | 53162612 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/NPC | 3000 | 707,649 | 138,207.722573 | 53162612 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | WETH/BRETT | 2135 | 694,919 | 501,471.744276 | 53162612 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | TIG/USDC | 10000 | 690,146 | 0.599193 | 53162612 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 674,354 | 0.108837 | 53162612 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |

## Recherche d'opportunités
- Cycles : 9453 ; routes examinées : 181251822 ; candidats optimisés : 633591 ; net attendu > 0 : 317 ; dernier cycle 250.7 ms
- Rejets (moteur) : {'spread_below_threshold': 178419479, 'liquidity_below_min': 2118741, 'negative_expected_net': 633274, 'borrow_bound_too_small': 78545, 'cycle_budget_exhausted': 1466}
- Enregistrements de la session : 633591 ; net attendu > 0 : 317 ; simulés (eth_call de la vraie tx) : 17 (ok 3, échec 14) ; étiquettes ghost N+1 : 3/16 positives
- Décisions : {'REJECTED': 633591} ; motifs de rejet : {'below_safety_margin': 271, 'negative_expected_net': 633274, 'p_lower_below_threshold': 297, 'reliability_not_demonstrated': 20, 'sim_below_estimate': 3, 'simulated_net_nonpositive': 3, 'simulation_failed': 14, 'stale_data': 38}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53159906 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.794482 WETH | 0.000094 WETH | 0.000000 WETH | 0.000002 WETH | 0.000091 WETH (0.1957 €) | — | 1.15 | 0.020 (n=106) | REJECTED | below_safety_margin(91426168727046<158896479878237), p_lower_below_threshold(0.02<0.75) |
| 53159907 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.794482 WETH | 0.000094 WETH | 0.000000 WETH | 0.000002 WETH | 0.000091 WETH (0.1957 €) | — | 1.15 | 0.020 (n=106) | REJECTED | below_safety_margin(91426168727046<158896479878237), p_lower_below_threshold(0.02<0.75) |
| 53159906 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 1,843.634528 USDC | 0.217677 USDC | 0.000000 USDC | 0.005610 USDC | 0.212067 USDC (0.1951 €) | — | 1.15 | 0.020 (n=106) | REJECTED | below_safety_margin(212067<368726), p_lower_below_threshold(0.02<0.75) |
| 53159907 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 1,843.634528 USDC | 0.217677 USDC | 0.000000 USDC | 0.005610 USDC | 0.212067 USDC (0.1951 €) | — | 1.15 | 0.020 (n=106) | REJECTED | below_safety_margin(212067<368726), p_lower_below_threshold(0.02<0.75) |
| 53162545 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 1,457.453219 USDC | 0.137624 USDC | 0.000000 USDC | 0.005604 USDC | 0.132020 USDC (0.1215 €) | — | 0.91 | 0.020 (n=106) | REJECTED | below_safety_margin(132020<291490), p_lower_below_threshold(0.02<0.75) |
| 53162547 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 1,457.453219 USDC | 0.137624 USDC | 0.000000 USDC | 0.005604 USDC | 0.132020 USDC (0.1215 €) | — | 0.91 | 0.020 (n=106) | REJECTED | below_safety_margin(132020<291490), p_lower_below_threshold(0.02<0.75) |
| 53162545 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.624317 WETH | 0.000059 WETH | 0.000000 WETH | 0.000002 WETH | 0.000056 WETH (0.1211 €) | — | 0.90 | 0.020 (n=106) | REJECTED | below_safety_margin(56476157983539<124863325293708), p_lower_below_threshold(0.02<0.75) |
| 53162547 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.624317 WETH | 0.000059 WETH | 0.000000 WETH | 0.000002 WETH | 0.000056 WETH (0.1211 €) | — | 0.90 | 0.020 (n=106) | REJECTED | below_safety_margin(56476157983539<124863325293708), p_lower_below_threshold(0.02<0.75) |
| 53162317 | WETH→[uniswap_v3]→VIRTUAL→[aerodrome_slipstream]→WETH | 0.102608 WETH | 0.000057 WETH | 0.000000 WETH | 0.000002 WETH | 0.000054 WETH (0.1168 €) | — | 5.31 | 0.047 (n=45) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.05<0.75) |
| 53157877 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 576.906943 USDC | 0.092155 USDC | 0.000000 USDC | 0.005585 USDC | 0.086570 USDC (0.0796 €) | — | 1.50 | 0.020 (n=105) | REJECTED | below_safety_margin(86570<115381), p_lower_below_threshold(0.02<0.75) |
| 53157877 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.247311 WETH | 0.000040 WETH | 0.000000 WETH | 0.000002 WETH | 0.000037 WETH (0.0794 €) | — | 1.50 | 0.020 (n=105) | REJECTED | below_safety_margin(37128881072348<49462128105230), p_lower_below_threshold(0.02<0.75) |
| 53157877 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 481.024479 USDC | 0.060505 USDC | 0.000000 USDC | 0.005232 USDC | 0.055273 USDC (0.0509 €) | — | 1.15 | 0.013 (n=22) | REJECTED | below_safety_margin(55273<96204), reliability_not_demonstrated |
| 53157877 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.206988 WETH | 0.000026 WETH | 0.000000 WETH | 0.000002 WETH | 0.000024 WETH (0.0507 €) | — | 1.15 | 0.013 (n=22) | REJECTED | below_safety_margin(23702945929398<41397618782382), reliability_not_demonstrated |
| 53162545 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 321.959550 USDC | 0.047441 USDC | 0.000000 USDC | 0.005250 USDC | 0.042191 USDC (0.0388 €) | — | 1.31 | 0.013 (n=22) | REJECTED | below_safety_margin(42191<64391), reliability_not_demonstrated |
| 53162547 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 321.959550 USDC | 0.047441 USDC | 0.000000 USDC | 0.005250 USDC | 0.042191 USDC (0.0388 €) | — | 1.31 | 0.013 (n=22) | REJECTED | below_safety_margin(42191<64391), reliability_not_demonstrated |
| 53162545 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.138057 WETH | 0.000020 WETH | 0.000000 WETH | 0.000002 WETH | 0.000018 WETH (0.0387 €) | — | 1.31 | 0.013 (n=22) | REJECTED | below_safety_margin(18045386588948<27611493462815), reliability_not_demonstrated |
| 53162547 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.138057 WETH | 0.000020 WETH | 0.000000 WETH | 0.000002 WETH | 0.000018 WETH (0.0387 €) | — | 1.31 | 0.013 (n=22) | REJECTED | below_safety_margin(18045386588948<27611493462815), reliability_not_demonstrated |
| 53162317 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→VIRTUAL→[pancakeswap_v3]→USDC | 120.179962 USDC | 0.043037 USDC | 0.000000 USDC | 0.007033 USDC | 0.036004 USDC (0.0331 €) | — | 3.00 | 0.128 (n=386) | REJECTED | p_lower_below_threshold(0.13<0.75) |
| 53162317 | WETH→[uniswap_v3]→VIRTUAL→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.051628 WETH | 0.000018 WETH | 0.000000 WETH | 0.000003 WETH | 0.000015 WETH (0.0331 €) | — | 2.99 | 0.128 (n=386) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.13<0.75) |
| 53162317 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→VIRTUAL→[pancakeswap_v3]→USDC | 113.478899 USDC | 0.040906 USDC | 0.000000 USDC | 0.007387 USDC | 0.033519 USDC (0.0308 €) | — | 2.95 | 0.128 (n=386) | REJECTED | p_lower_below_threshold(0.13<0.75) |
| 53162317 | WETH→[uniswap_v3]→VIRTUAL→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.048914 WETH | 0.000018 WETH | 0.000000 WETH | 0.000003 WETH | 0.000014 WETH (0.0308 €) | — | 2.94 | 0.128 (n=386) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.13<0.75) |
| 53158700 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.123732 WETH | 0.000016 WETH | 0.000000 WETH | 0.000003 WETH | 0.000013 WETH (0.0280 €) | — | 1.06 | 0.129 (n=383) | REJECTED | below_safety_margin(13058865119440<24746479515443), p_lower_below_threshold(0.13<0.75) |
| 53158700 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 279.295635 USDC | 0.037310 USDC | 0.000000 USDC | 0.007029 USDC | 0.030281 USDC (0.0279 €) | — | 1.08 | 0.129 (n=383) | REJECTED | below_safety_margin(30281<55859), p_lower_below_threshold(0.13<0.75) |
| 53158700 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.002966 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0273 €) | — | 1.25 | 0.129 (n=383) | REJECTED | below_safety_margin(37<59), p_lower_below_threshold(0.13<0.75) |
| 53158700 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.128840 WETH | 0.000015 WETH | 0.000000 WETH | 0.000002 WETH | 0.000013 WETH (0.0272 €) | — | 0.98 | 0.020 (n=105) | REJECTED | below_safety_margin(12663985308314<25768090761732), p_lower_below_threshold(0.02<0.75) |

## Fiabilité et décision
- Observations ghost : 2848 ; taux observé 0.091 ; borne inférieure crédible (0.9) 0.084 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 8.4% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
