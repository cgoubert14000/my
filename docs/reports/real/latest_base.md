# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-23T01:25:27+00:00 ; durée 315.78 min ; blocs 52955211 → 52964681 (8774 vus)

## Connexion
- Requêtes RPC : 109232 ; erreurs : 38 ; latence p50/p95 : 364.2/1,815.5 ms
- Rafraîchissements d'état : 8774 ; âge des données au dernier bloc : 5.41 s ; changements de frais LP observés (pools à frais dynamiques) : 13469
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 103843 ; cycles déclenchés par événement : 7659 ; avance médiane sur le rafraîchissement multicall : 630 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,386.08 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 541 pools, 316 jetons, 19308 routes
- Par DEX : uniswap_v3 137, aerodrome 222, aerodrome_slipstream 136, pancakeswap_v3 30, uniswap_v2 13, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 198 (rejetés 2) → 603 jetons ; pools candidats 3822 (énumérés 360, par paires 0), mesurés 543, sous le plancher de 10000.0 $ : 2 → gardés 541 (max 1500) ; prix des hubs : {'USDC': 1.0, 'USDbC': 1.0, 'DAI': 1.0, 'WETH': 2383.836332, 'AERO': 0.803249, 'cbBTC': 81352.487956}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 156,552,336 | 2,386.077247 | 52964682 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,223,366 | 0.029343 | 52964682 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 13,390,143 | 92.257367 | 52964682 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| aerodrome | USDC/AERO | 3000 | 11,929,522 | 1.275087 | 52964682 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,241,794 | 0.029364 | 52964682 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,854,264 | 0.000012 | 52964682 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 8,906,817 | 0.029368 | 52964682 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/USDC | 500 | 8,644,923 | 2,386.663108 | 52964682 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,133,291 | 0.001666 | 52964682 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 342 | 6,778,490 | 0.000012 | 52964682 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 579 | 5,675,383 | 2,386.260697 | 52964682 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,388,400 | 0.029345 | 52964682 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | USDC/cbBTC | 496 | 5,256,036 | 0.000012 | 52964682 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,579,679 | 2,385.978605 | 52964682 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,282,733 | 0.998772 | 52964682 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/USDC | 3000 | 4,276,248 | 2,385.183202 | 52964682 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome | WETH/KTA | 3000 | 3,970,635 | 34,223.414560 | 52964682 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | VIRTUAL/WETH | 10000 | 3,430,253 | 0.000274 | 52964682 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/USDT | 418 | 2,899,895 | 2,390.994136 | 52964682 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome_slipstream | WETH/VVV | 2712 | 2,541,787 | 92.296445 | 52964682 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,300,926 | 390.949557 | 52964682 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | WETH/AERO | 10000 | 2,254,171 | 3,025.076784 | 52964682 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | WETH/FAI | 10000 | 2,210,141 | 1,182,410.796820 | 52964682 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,981,443 | 0.000000 | 52964682 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,920,577 | 0.000012 | 52964682 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v3 | XDP/USDC | 100 | 1,774,690 | 0.018074 | 52964682 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,747,800 | 0.000012 | 52964682 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,641,025 | 1.525684 | 52964682 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | WETH/AERO | 3000 | 1,610,165 | 3,045.096605 | 52964682 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,453,771 | 0.823199 | 52964682 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,414,838 | 13,313.020731 | 52964682 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,365,595 | 0.004989 | 52964682 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,289,726 | 0.000274 | 52964682 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | WETH/msETH (stable) | 500 | 1,278,227 | 2.361240 | 52964682 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,276,405 | 2,386.950102 | 52964682 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | DRB/WETH | 10000 | 1,266,254 | 0.000000 | 52964682 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | USDC/SEND | 3000 | 1,229,423 | 64.289389 | 52964682 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,183,494 | 35,764,166.460256 | 52964682 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,177,435 | 16.208310 | 52964682 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | WETH/WELL | 10000 | 1,169,506 | 1,105,060.065762 | 52964682 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome | USDC/NOCK | 3000 | 1,157,881 | 46.809139 | 52964682 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,143,036 | 498,148.209539 | 52964682 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | weETH_04c0/WETH | 500 | 1,086,735 | 1.105790 | 52964682 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome | WETH/EDEL | 7000 | 1,085,125 | 74,486.705694 | 52964682 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | USDC/VVV | 3000 | 1,083,304 | 0.038692 | 52964682 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,058,777 | 21,313,449.073659 | 52964682 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,035,021 | 17.206533 | 52964682 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 1,024,375 | 0.000010 | 52964682 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | WETH/cbBTC | 3000 | 1,009,133 | 0.029368 | 52964682 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,002,571 | 23.056386 | 52964682 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| uniswap_v3 | WETH/MORPHO | 3000 | 958,944 | 1,054.711908 | 52964682 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/USDC | 10000 | 937,436 | 2,381.973285 | 52964682 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | uXRP/WETH | 3000 | 910,444 | 0.000546 | 52964682 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome | WETH/bsdETH | 100 | 887,088 | 0.917079 | 52964682 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 881,214 | 17.849732 | 52964682 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v2 | WETH/USDC | 3000 | 873,213 | 2,393.125809 | 52964682 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome | WETH/wstETH | 3000 | 808,332 | 0.803225 | 52964682 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 787,489 | 0.650968 | 52964682 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| pancakeswap_v3 | QUID/USDC | 100 | 784,484 | 0.055122 | 52964682 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | fBOMB/USDC | 10000 | 769,744 | 0.018327 | 52964682 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |

## Recherche d'opportunités
- Cycles : 16432 ; routes examinées : 317269056 ; candidats optimisés : 1451427 ; net attendu > 0 : 841 ; dernier cycle 190.2 ms
- Rejets (moteur) : {'spread_below_threshold': 312769671, 'liquidity_below_min': 3027677, 'negative_expected_net': 1450586, 'borrow_bound_too_small': 16414, 'cycle_budget_exhausted': 3867}
- Enregistrements de la session : 1451427 ; net attendu > 0 : 841 ; simulés (eth_call de la vraie tx) : 38 (ok 8, échec 30) ; étiquettes ghost N+1 : 0/34 positives
- Décisions : {'REJECTED': 1451427} ; motifs de rejet : {'below_safety_margin': 447, 'negative_expected_net': 1450586, 'p_lower_below_threshold': 594, 'price_impact': 8, 'reliability_not_demonstrated': 247, 'sim_below_estimate': 1, 'simulated_net_nonpositive': 1, 'simulation_failed': 30, 'stale_data': 22}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52960458 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome]→AERO→[aerodrome_slipstream]→cbBTC | 0.035412 cbBTC | 0.000056 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000056 cbBTC (4.2161 €) | — | 15.89 | 0.051 (n=16) | REJECTED | reliability_not_demonstrated |
| 52960458 | USDC→[aerodrome]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 2,895.231752 USDC | 4.578912 USDC | 0.000000 USDC | 0.008301 USDC | 4.570611 USDC (4.2050 €) | — | 15.79 | 0.051 (n=16) | REJECTED | reliability_not_demonstrated |
| 52960458 | cbBTC→[aerodrome_slipstream]→USDC→[aerodrome]→AERO→[aerodrome_slipstream]→cbBTC | 0.035493 cbBTC | 0.000053 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000053 cbBTC (3.9389 €) | — | 14.81 | 0.021 (n=134) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 52960458 | USDC→[aerodrome]→AERO→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→USDC | 2,877.478724 USDC | 4.275915 USDC | 0.000000 USDC | 0.007213 USDC | 4.268702 USDC (3.9272 €) | — | 14.83 | 0.021 (n=134) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 52960458 | cbBTC→[aerodrome_slipstream]→USDC→[aerodrome]→AERO→[aerodrome_slipstream]→cbBTC | 0.034669 cbBTC | 0.000049 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000049 cbBTC (3.6466 €) | — | 14.04 | 0.021 (n=134) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 52960458 | USDC→[aerodrome]→AERO→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→USDC | 2,820.419579 USDC | 3.958755 USDC | 0.000000 USDC | 0.007213 USDC | 3.951542 USDC (3.6354 €) | — | 14.01 | 0.021 (n=134) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 52960458 | cbBTC→[uniswap_v3]→USDC→[aerodrome]→AERO→[aerodrome_slipstream]→cbBTC | 0.032410 cbBTC | 0.000043 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000043 cbBTC (3.2352 €) | — | 13.32 | 0.021 (n=134) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 52960458 | USDC→[aerodrome]→AERO→[aerodrome_slipstream]→cbBTC→[uniswap_v3]→USDC | 2,656.396106 USDC | 3.512901 USDC | 0.000000 USDC | 0.007213 USDC | 3.505688 USDC (3.2252 €) | — | 13.20 | 0.021 (n=134) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 52963544 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→BASECAT→[uniswap_v3]→USDC | 88.371977 USDC | 2.905859 USDC | 0.000000 USDC | 0.007171 USDC | 2.898688 USDC (2.6668 €) | — | 328.01 | 0.001 (n=9) | REJECTED | reliability_not_demonstrated |
| 52963544 | WETH→[uniswap_v3]→BASECAT→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.036922 WETH | 0.001214 WETH | 0.000000 WETH | 0.000003 WETH | 0.001211 WETH (2.6588 €) | — | 328.01 | 0.001 (n=9) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52963544 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→BASECAT→[uniswap_v3]→USDC | 87.278256 USDC | 2.871307 USDC | 0.000000 USDC | 0.007171 USDC | 2.864136 USDC (2.6350 €) | — | 328.16 | 0.001 (n=8) | REJECTED | reliability_not_demonstrated |
| 52963544 | WETH→[uniswap_v3]→BASECAT→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.036450 WETH | 0.001199 WETH | 0.000000 WETH | 0.000003 WETH | 0.001196 WETH (2.6260 €) | — | 328.16 | 0.001 (n=8) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52960458 | WETH→[aerodrome_slipstream]→USDC→[aerodrome]→AERO→[uniswap_v3]→WETH | 0.786690 WETH | 0.001035 WETH | 0.000000 WETH | 0.000003 WETH | 0.001032 WETH (2.2680 €) | — | 13.12 | 0.021 (n=134) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.02<0.75) |
| 52960458 | USDC→[aerodrome]→AERO→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 1,872.541635 USDC | 2.464489 USDC | 0.000000 USDC | 0.006851 USDC | 2.457638 USDC (2.2610 €) | — | 13.12 | 0.021 (n=134) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 52960458 | WETH→[pancakeswap_v3]→USDC→[aerodrome]→AERO→[uniswap_v3]→WETH | 0.769086 WETH | 0.000999 WETH | 0.000000 WETH | 0.000003 WETH | 0.000996 WETH (2.1875 €) | — | 12.94 | 0.051 (n=16) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52960458 | WETH→[uniswap_v3]→USDC→[aerodrome]→AERO→[uniswap_v3]→WETH | 0.770657 WETH | 0.000996 WETH | 0.000000 WETH | 0.000003 WETH | 0.000993 WETH (2.1819 €) | — | 12.89 | 0.021 (n=134) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.02<0.75) |
| 52960458 | USDC→[aerodrome]→AERO→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 1,832.023654 USDC | 2.377428 USDC | 0.000000 USDC | 0.007213 USDC | 2.370215 USDC (2.1806 €) | — | 12.94 | 0.051 (n=16) | REJECTED | reliability_not_demonstrated |
| 52960458 | USDC→[aerodrome]→AERO→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 1,833.895644 USDC | 2.371020 USDC | 0.000000 USDC | 0.006851 USDC | 2.364169 USDC (2.1750 €) | — | 12.89 | 0.021 (n=134) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 52963544 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→BASECAT→[uniswap_v3]→USDC | 69.803287 USDC | 2.309557 USDC | 0.000000 USDC | 0.007171 USDC | 2.302386 USDC (2.1182 €) | — | 329.84 | 0.001 (n=8) | REJECTED | reliability_not_demonstrated |
| 52963544 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→BASECAT→[uniswap_v3]→USDC | 69.517115 USDC | 2.308303 USDC | 0.000000 USDC | 0.007171 USDC | 2.301132 USDC (2.1170 €) | — | 331.02 | 0.001 (n=9) | REJECTED | reliability_not_demonstrated |
| 52963544 | WETH→[uniswap_v3]→BASECAT→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.029158 WETH | 0.000965 WETH | 0.000000 WETH | 0.000003 WETH | 0.000962 WETH (2.1114 €) | — | 329.84 | 0.001 (n=8) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52963544 | WETH→[uniswap_v3]→BASECAT→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.029038 WETH | 0.000964 WETH | 0.000000 WETH | 0.000003 WETH | 0.000961 WETH (2.1103 €) | — | 331.01 | 0.001 (n=9) | REJECTED | reliability_not_demonstrated |
| 52960458 | WETH→[pancakeswap_v3]→USDC→[aerodrome]→AERO→[uniswap_v3]→WETH | 0.734548 WETH | 0.000957 WETH | 0.000000 WETH | 0.000003 WETH | 0.000954 WETH (2.0961 €) | — | 12.99 | 0.051 (n=16) | REJECTED | reliability_not_demonstrated |
| 52960458 | USDC→[aerodrome]→AERO→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 1,747.812253 USDC | 2.277838 USDC | 0.000000 USDC | 0.006851 USDC | 2.270987 USDC (2.0893 €) | — | 12.99 | 0.051 (n=16) | REJECTED | reliability_not_demonstrated |
| 52960458 | USDC→[aerodrome]→AERO→[aerodrome_slipstream]→USDC | 1,414.742506 USDC | 2.172702 USDC | 0.000000 USDC | 0.005398 USDC | 2.167304 USDC (1.9939 €) | — | 15.32 | 0.001 (n=15) | REJECTED | reliability_not_demonstrated |

## Fiabilité et décision
- Observations ghost : 1962 ; taux observé 0.095 ; borne inférieure crédible (0.9) 0.087 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 8.7% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
