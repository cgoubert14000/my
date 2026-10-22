# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-22T22:22:52+00:00 ; durée 133.2 min ; blocs 52955211 → 52959206 (3695 vus)

## Connexion
- Requêtes RPC : 45207 ; erreurs : 5 ; latence p50/p95 : 352.7/2,257.7 ms
- Rafraîchissements d'état : 3695 ; âge des données au dernier bloc : 6.89 s ; changements de frais LP observés (pools à frais dynamiques) : 6439
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 40959 ; cycles déclenchés par événement : 2367 ; avance médiane sur le rafraîchissement multicall : 1,286 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,388.54 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 541 pools, 316 jetons, 19308 routes
- Par DEX : uniswap_v3 137, aerodrome 222, aerodrome_slipstream 136, pancakeswap_v3 30, uniswap_v2 13, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 198 (rejetés 2) → 603 jetons ; pools candidats 3822 (énumérés 360, par paires 0), mesurés 543, sous le plancher de 10000.0 $ : 2 → gardés 541 (max 1500) ; prix des hubs : {'USDC': 1.0, 'USDbC': 1.0, 'DAI': 1.0, 'WETH': 2383.836332, 'AERO': 0.803249, 'cbBTC': 81352.487956}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 156,561,565 | 2,388.543955 | 52959207 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,243,019 | 0.029332 | 52959207 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 13,478,313 | 91.363397 | 52959207 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| aerodrome | USDC/AERO | 3000 | 12,108,533 | 1.261328 | 52959207 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,256,690 | 0.029364 | 52959207 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,874,363 | 0.000012 | 52959207 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 8,945,168 | 0.029381 | 52959207 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/USDC | 500 | 8,654,065 | 2,382.532252 | 52959207 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,136,276 | 0.001663 | 52959207 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 348 | 6,802,631 | 0.000012 | 52959207 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 150 | 5,722,090 | 2,382.694998 | 52959207 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,383,209 | 0.029327 | 52959207 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | USDC/cbBTC | 496 | 5,273,723 | 0.000012 | 52959207 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,495,090 | 2,382.809828 | 52959207 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,288,880 | 0.998772 | 52959207 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/USDC | 3000 | 4,287,582 | 2,388.823444 | 52959207 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome | WETH/KTA | 3000 | 3,965,770 | 34,378.398847 | 52959207 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | VIRTUAL/WETH | 10000 | 3,435,020 | 0.000274 | 52959207 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/USDT | 448 | 2,905,348 | 2,386.836976 | 52959207 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome_slipstream | WETH/VVV | 2712 | 2,554,736 | 91.393195 | 52959207 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,293,545 | 396.325675 | 52959207 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | WETH/AERO | 10000 | 2,273,843 | 2,993.206664 | 52959207 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | WETH/FAI | 10000 | 2,201,239 | 1,194,460.014081 | 52959207 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,961,830 | 0.000000 | 52959207 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,916,787 | 0.000012 | 52959207 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v3 | XDP/USDC | 100 | 1,784,161 | 0.018196 | 52959207 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,749,226 | 0.000012 | 52959207 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,641,407 | 1.525093 | 52959207 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | WETH/AERO | 3000 | 1,616,437 | 3,013.797341 | 52959207 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,454,229 | 0.823342 | 52959207 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,409,500 | 13,509.297925 | 52959207 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,367,157 | 0.004990 | 52959207 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,316,547 | 2,382.541961 | 52959207 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,291,248 | 0.000273 | 52959207 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | WETH/msETH (stable) | 500 | 1,281,357 | 2.361233 | 52959207 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | DRB/WETH | 10000 | 1,265,911 | 0.000000 | 52959207 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | USDC/SEND | 3000 | 1,229,454 | 64.286145 | 52959207 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,185,740 | 35,672,032.627566 | 52959207 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,177,176 | 16.234606 | 52959207 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | WETH/WELL | 10000 | 1,169,750 | 1,107,406.012068 | 52959207 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome | USDC/NOCK | 3000 | 1,167,728 | 46.023022 | 52959207 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,147,791 | 496,333.388432 | 52959207 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | weETH_04c0/WETH | 500 | 1,087,859 | 1.105792 | 52959207 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome | WETH/EDEL | 7000 | 1,085,485 | 74,754.105040 | 52959207 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 1,067,852 | 0.000010 | 52959207 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,061,500 | 21,256,860.378615 | 52959207 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,031,665 | 17.363115 | 52959207 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | WETH/cbBTC | 3000 | 1,010,797 | 0.029368 | 52959207 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,004,323 | 23.071382 | 52959207 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| uniswap_v3 | USDC/VVV | 3000 | 989,224 | 0.038366 | 52959207 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/MORPHO | 3000 | 957,830 | 1,052.515783 | 52959207 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/USDC | 10000 | 938,177 | 2,381.973285 | 52959207 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | uXRP/WETH | 3000 | 908,163 | 0.000545 | 52959207 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome | WETH/bsdETH | 100 | 888,329 | 0.916410 | 52959207 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 881,104 | 17.854087 | 52959207 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v2 | WETH/USDC | 3000 | 874,649 | 2,388.325877 | 52959207 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome | WETH/wstETH | 3000 | 809,236 | 0.803225 | 52959207 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 788,157 | 0.653095 | 52959207 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| pancakeswap_v3 | QUID/USDC | 100 | 785,138 | 0.055219 | 52959207 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | fBOMB/USDC | 10000 | 770,030 | 0.018341 | 52959207 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |

## Recherche d'opportunités
- Cycles : 6061 ; routes examinées : 117025788 ; candidats optimisés : 738466 ; net attendu > 0 : 283 ; dernier cycle 498.1 ms
- Rejets (moteur) : {'spread_below_threshold': 115211327, 'liquidity_below_min': 1067068, 'negative_expected_net': 738183, 'borrow_bound_too_small': 6050, 'cycle_budget_exhausted': 2877}
- Enregistrements de la session : 738466 ; net attendu > 0 : 283 ; simulés (eth_call de la vraie tx) : 14 (ok 7, échec 7) ; étiquettes ghost N+1 : 0/10 positives
- Décisions : {'REJECTED': 738466} ; motifs de rejet : {'below_safety_margin': 250, 'negative_expected_net': 738183, 'p_lower_below_threshold': 258, 'reliability_not_demonstrated': 25, 'simulation_failed': 7, 'stale_data': 20}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52957222 | USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 223.673289 USDC | 0.076992 USDC | 0.000000 USDC | 0.007192 USDC | 0.069800 USDC (0.0642 €) | — | 3.12 | 0.099 (n=198) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 52957222 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH | 0.093230 WETH | 0.000032 WETH | 0.000000 WETH | 0.000003 WETH | 0.000029 WETH (0.0640 €) | 0.000029 WETH | 3.12 | 0.099 (n=198) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 52957222 | USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 201.659709 USDC | 0.073426 USDC | 0.000000 USDC | 0.007192 USDC | 0.066234 USDC (0.0609 €) | — | 3.28 | 0.119 (n=99) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52957222 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH | 0.084104 WETH | 0.000031 WETH | 0.000000 WETH | 0.000003 WETH | 0.000028 WETH (0.0607 €) | 0.000028 WETH | 3.29 | 0.119 (n=99) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52957435 | USDC→[uniswap_v3]→OWB→[aerodrome]→USDC | 24.546486 USDC | 0.050831 USDC | 0.000000 USDC | 0.005051 USDC | 0.045780 USDC (0.0421 €) | — | 18.65 | 0.001 (n=14) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52957304 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.002194 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0359 €) | — | 2.19 | 0.116 (n=230) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.12<0.75) |
| 52957304 | WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.064566 WETH | 0.000019 WETH | 0.000000 WETH | 0.000003 WETH | 0.000016 WETH (0.0356 €) | — | 2.50 | 0.116 (n=230) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.12<0.75) |
| 52956884 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome_slipstream]→WETH | 0.050938 WETH | 0.000017 WETH | 0.000000 WETH | 0.000003 WETH | 0.000014 WETH (0.0308 €) | 0.000014 WETH | 2.76 | 0.118 (n=226) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52956884 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome_slipstream]→WETH | 0.050938 WETH | 0.000017 WETH | 0.000000 WETH | 0.000003 WETH | 0.000014 WETH (0.0308 €) | — | 2.76 | 0.118 (n=226) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.12<0.75) |
| 52956884 | USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 121.229953 USDC | 0.040595 USDC | 0.000000 USDC | 0.007175 USDC | 0.033420 USDC (0.0307 €) | 0.033420 USDC | 2.76 | 0.118 (n=226) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52956884 | USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 121.229953 USDC | 0.040595 USDC | 0.000000 USDC | 0.007175 USDC | 0.033420 USDC (0.0307 €) | — | 2.76 | 0.118 (n=226) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.12<0.75) |
| 52956884 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome_slipstream]→WETH | 0.048346 WETH | 0.000017 WETH | 0.000000 WETH | 0.000003 WETH | 0.000014 WETH (0.0305 €) | 0.000014 WETH | 2.88 | 0.118 (n=226) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52956884 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome_slipstream]→WETH | 0.048346 WETH | 0.000017 WETH | 0.000000 WETH | 0.000003 WETH | 0.000014 WETH (0.0305 €) | — | 2.88 | 0.118 (n=226) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.12<0.75) |
| 52956884 | USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 115.203870 USDC | 0.040292 USDC | 0.000000 USDC | 0.007175 USDC | 0.033117 USDC (0.0305 €) | — | 2.87 | 0.118 (n=226) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52956884 | USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 115.203870 USDC | 0.040292 USDC | 0.000000 USDC | 0.007175 USDC | 0.033117 USDC (0.0305 €) | — | 2.87 | 0.118 (n=226) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52957222 | USDC→[aerodrome_slipstream]→EURC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 91.380331 USDC | 0.034079 USDC | 0.000000 USDC | 0.007192 USDC | 0.026887 USDC (0.0247 €) | — | 2.94 | 0.117 (n=229) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52957222 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→EURC→[pancakeswap_v3]→WETH | 0.038409 WETH | 0.000014 WETH | 0.000000 WETH | 0.000003 WETH | 0.000011 WETH (0.0246 €) | 0.000011 WETH | 2.92 | 0.117 (n=229) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52957222 | USDC→[aerodrome_slipstream]→EURC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 90.725856 USDC | 0.033436 USDC | 0.000000 USDC | 0.007192 USDC | 0.026244 USDC (0.0241 €) | — | 2.89 | 0.117 (n=229) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52957222 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→EURC→[pancakeswap_v3]→WETH | 0.037941 WETH | 0.000014 WETH | 0.000000 WETH | 0.000003 WETH | 0.000011 WETH (0.0241 €) | — | 2.88 | 0.117 (n=229) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52957222 | USDC→[aerodrome_slipstream]→EURC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 92.777874 USDC | 0.032685 USDC | 0.000000 USDC | 0.007192 USDC | 0.025493 USDC (0.0235 €) | — | 2.75 | 0.117 (n=229) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52957222 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→EURC→[pancakeswap_v3]→WETH | 0.038765 WETH | 0.000014 WETH | 0.000000 WETH | 0.000003 WETH | 0.000011 WETH (0.0234 €) | — | 2.74 | 0.117 (n=229) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52957222 | USDC→[aerodrome_slipstream]→EURC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 91.966474 USDC | 0.032034 USDC | 0.000000 USDC | 0.007192 USDC | 0.024842 USDC (0.0229 €) | — | 2.70 | 0.117 (n=229) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52957222 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→EURC→[pancakeswap_v3]→WETH | 0.038506 WETH | 0.000013 WETH | 0.000000 WETH | 0.000003 WETH | 0.000010 WETH (0.0228 €) | — | 2.69 | 0.117 (n=229) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52956495 | USDC→[uniswap_v3]→EURC→[aerodrome_slipstream]→USDC | 448.687304 USDC | 0.027933 USDC | 0.000000 USDC | 0.005362 USDC | 0.022571 USDC (0.0208 €) | — | 0.50 | 0.021 (n=14) | REJECTED | below_safety_margin(22571<89737), reliability_not_demonstrated |
| 52956496 | USDC→[uniswap_v3]→EURC→[aerodrome_slipstream]→USDC | 448.687304 USDC | 0.027933 USDC | 0.000000 USDC | 0.005362 USDC | 0.022571 USDC (0.0208 €) | — | 0.50 | 0.021 (n=14) | REJECTED | below_safety_margin(22571<89737), stale_data(4307ms>4000.0), reliability_not_demonstrated |

## Fiabilité et décision
- Observations ghost : 1938 ; taux observé 0.096 ; borne inférieure crédible (0.9) 0.088 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 8.8% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
