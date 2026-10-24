# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-24T14:20:02+00:00 ; durée 175.77 min ; blocs 53025852 → 53031124 (5268 vus)

## Connexion
- Requêtes RPC : 65481 ; erreurs : 23 ; latence p50/p95 : 201.3/538.3 ms
- Rafraîchissements d'état : 5268 ; âge des données au dernier bloc : 2.74 s ; changements de frais LP observés (pools à frais dynamiques) : 6306
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 73165 ; cycles déclenchés par événement : 6273 ; avance médiane sur le rafraîchissement multicall : 8 ms
- Gaz : base fee 0.009914 gwei ; prix ETH (pool le plus profond) : 2,337.44 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 536 pools, 308 jetons, 19360 routes
- Par DEX : uniswap_v3 143, aerodrome 216, aerodrome_slipstream 133 (quarantaine 2), pancakeswap_v3 29, uniswap_v2 12, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 193 (rejetés 2) → 598 jetons ; pools candidats 3806 (énumérés 348, par paires 0), mesurés 538, sous le plancher de 10000.0 $ : 2 → gardés 536 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDbC': 1.0, 'USDC': 1.0, 'WETH': 2363.674955, 'cbBTC': 80533.217668, 'AERO': 0.705694}
- Pools en quarantaine : 2 — aerodrome_slipstream:WETH/TIBBIR@0x0f664a: simulation failed ×5 (model/chain mismatch) — until block 53031331; aerodrome_slipstream:USDC/TIBBIR@0xe36A01: simulation failed ×5 (model/chain mismatch) — until block 53031331

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 154,077,940 | 2,337.436824 | 53031125 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,829,347 | 0.029229 | 53031125 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 12,055,606 | 98.624517 | 53031125 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,061,691 | 0.029230 | 53031125 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,549,785 | 0.000012 | 53031125 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome | USDC/AERO | 3000 | 8,801,263 | 1.449353 | 53031125 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/USDC | 500 | 8,468,179 | 2,341.604081 | 53031125 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome_slipstream | WETH/cbBTC | 2635 | 8,205,817 | 0.029220 | 53031125 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,943,066 | 0.001634 | 53031125 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 382 | 6,284,326 | 0.000012 | 53031125 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 937 | 5,449,671 | 2,342.160205 | 53031125 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,375,660 | 0.029237 | 53031125 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | USDC/cbBTC | 600 | 4,826,349 | 0.000012 | 53031125 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,437,751 | 2,342.640086 | 53031125 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,210,013 | 0.998962 | 53031125 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,870,359 | 34,537.486854 | 53031125 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/USDC | 3000 | 3,804,543 | 2,337.563529 | 53031125 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | WETH/USDT | 499 | 2,757,546 | 2,352.995912 | 53031125 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome_slipstream | WETH/VVV | 2712 | 2,466,242 | 98.653881 | 53031125 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,206,534 | 414.755619 | 53031125 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | WETH/FAI | 10000 | 2,097,250 | 1,259,356.225805 | 53031125 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,907,667 | 0.000012 | 53031125 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,898,463 | 0.000000 | 53031125 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome | WETH/AERO | 10000 | 1,895,018 | 3,364.950553 | 53031125 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | XDP/USDC | 100 | 1,764,379 | 0.017658 | 53031125 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,730,460 | 0.000012 | 53031125 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | VIRTUAL/WETH | 10000 | 1,579,057 | 0.000265 | 53031125 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,509,855 | 1.653156 | 53031125 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,458,962 | 0.825746 | 53031125 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,442,495 | 3,388.564715 | 53031125 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,403,949 | 0.005338 | 53031125 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,359,354 | 14,201.677359 | 53031125 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,258,716 | 2,341.559874 | 53031125 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,240,850 | 0.000263 | 53031125 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | USDC/SEND | 3000 | 1,225,082 | 64.745877 | 53031125 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome | WETH/msETH (stable) | 500 | 1,218,567 | 2.305054 | 53031125 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | DRB/WETH | 10000 | 1,186,793 | 0.000000 | 53031125 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/doginme | 10000 | 1,164,840 | 35,377,351.553929 | 53031125 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | WETH/WELL | 10000 | 1,131,362 | 1,120,998.699385 | 53031125 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome | USDC/NOCK | 3000 | 1,129,448 | 49.100254 | 53031125 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,112,324 | 501,973.467591 | 53031125 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,068,668 | 17.157260 | 53031125 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | WETH/EDEL | 7000 | 1,045,572 | 76,608.959653 | 53031125 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,038,647 | 17.045851 | 53031125 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,023,717 | 21,803,486.324071 | 53031125 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 943,315 | 23.360378 | 53031125 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| uniswap_v3 | USDC/VVV | 3000 | 935,783 | 0.042171 | 53031125 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/MORPHO | 3000 | 931,384 | 1,086.015023 | 53031125 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | uXRP/WETH | 3000 | 887,910 | 0.000541 | 53031125 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | USDC/SAPIEN | 4780 | 885,598 | 17.728941 | 53031125 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v3 | WETH/VVV | 10000 | 852,166 | 97.929665 | 53031125 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v2 | WETH/USDC | 3000 | 847,855 | 2,338.240947 | 53031125 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 833,343 | 0.000009 | 53031125 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| pancakeswap_v3 | QUID/USDC | 100 | 826,178 | 0.061488 | 53031125 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | weETH_04c0/WETH | 500 | 804,474 | 1.105901 | 53031125 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome | WETH/wstETH | 3000 | 791,480 | 0.803010 | 53031125 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | WETH/USDC | 10000 | 781,563 | 2,353.835235 | 53031125 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 749,646 | 0.613558 | 53031125 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 740,608 | 4,700,902.909582 | 53031125 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 720,593 | 0.651729 | 53031125 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |

## Recherche d'opportunités
- Cycles : 11540 ; routes examinées : 223414400 ; candidats optimisés : 830746 ; net attendu > 0 : 574 ; dernier cycle 141.9 ms
- Rejets (moteur) : {'spread_below_threshold': 220121207, 'liquidity_below_min': 2321993, 'negative_expected_net': 830172, 'pool_quarantined': 125732, 'borrow_bound_too_small': 11630, 'cycle_budget_exhausted': 1642, 'unquotable': 1450}
- Enregistrements de la session : 830746 ; net attendu > 0 : 574 ; simulés (eth_call de la vraie tx) : 48 (ok 18, échec 30) ; étiquettes ghost N+1 : 5/39 positives
- Décisions : {'REJECTED': 830746} ; motifs de rejet : {'below_safety_margin': 408, 'negative_expected_net': 830172, 'p_lower_below_threshold': 499, 'reliability_not_demonstrated': 75, 'sim_below_estimate': 1, 'simulated_net_nonpositive': 1, 'simulation_failed': 30}

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
| 53031011 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.417029 WETH | 0.000069 WETH | 0.000000 WETH | 0.000004 WETH | 0.000065 WETH (0.1414 €) | — | 1.57 | 0.001 (n=7) | REJECTED | below_safety_margin(65369432614061<83405863633006), reliability_not_demonstrated |
| 53031011 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.011784 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1414 €) | — | 1.62 | 0.001 (n=7) | REJECTED | below_safety_margin(191<235), reliability_not_demonstrated |
| 53031011 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 968.597064 USDC | 0.161482 USDC | 0.000000 USDC | 0.008473 USDC | 0.153009 USDC (0.1408 €) | — | 1.58 | 0.001 (n=7) | REJECTED | below_safety_margin(153009<193719), reliability_not_demonstrated |
| 53026232 | USDC→[uniswap_v2]→WETH→[uniswap_v3]→ZORA→[aerodrome_slipstream]→USDC | 43.803670 USDC | 0.153877 USDC | 0.000000 USDC | 0.006368 USDC | 0.147509 USDC (0.1357 €) | — | 33.68 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 53026232 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→ZORA→[aerodrome_slipstream]→USDC | 44.618570 USDC | 0.154884 USDC | 0.000000 USDC | 0.007461 USDC | 0.147423 USDC (0.1356 €) | — | 33.04 | 0.001 (n=12) | REJECTED | reliability_not_demonstrated |
| 53026232 | WETH→[uniswap_v3]→ZORA→[aerodrome_slipstream]→USDC→[uniswap_v2]→WETH | 0.018500 WETH | 0.000065 WETH | 0.000000 WETH | 0.000003 WETH | 0.000062 WETH (0.1353 €) | — | 33.62 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 53026232 | WETH→[uniswap_v3]→ZORA→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.018827 WETH | 0.000065 WETH | 0.000000 WETH | 0.000003 WETH | 0.000062 WETH (0.1352 €) | — | 33.02 | 0.001 (n=12) | REJECTED | reliability_not_demonstrated |

## Fiabilité et décision
- Observations ghost : 2170 ; taux observé 0.097 ; borne inférieure crédible (0.9) 0.089 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 8.9% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
