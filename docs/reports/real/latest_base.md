# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-24T10:48:21+00:00 ; durée 300.07 min ; blocs 53015772 → 53024772 (8925 vus)

## Connexion
- Requêtes RPC : 109934 ; erreurs : 38 ; latence p50/p95 : 115.1/905.6 ms
- Rafraîchissements d'état : 8926 ; âge des données au dernier bloc : 1.54 s ; changements de frais LP observés (pools à frais dynamiques) : 10785
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 109520 ; cycles déclenchés par événement : 9269 ; avance médiane sur le rafraîchissement multicall : 412 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,363.69 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 540 pools, 312 jetons, 19252 routes
- Par DEX : uniswap_v3 140, aerodrome 217, aerodrome_slipstream 135, pancakeswap_v3 31, uniswap_v2 13, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 196 (rejetés 2) → 601 jetons ; pools candidats 3859 (énumérés 351, par paires 0), mesurés 542, sous le plancher de 10000.0 $ : 2 → gardés 540 (max 1500) ; prix des hubs : {'USDC': 1.0, 'USDbC': 1.0, 'DAI': 1.0, 'WETH': 2380.141625, 'AERO': 0.727873, 'cbBTC': 80675.114522}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 155,445,697 | 2,363.686382 | 53024772 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,982,676 | 0.029386 | 53024772 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 12,253,759 | 97.616848 | 53024772 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,139,215 | 0.029383 | 53024772 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,559,464 | 0.000012 | 53024772 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome | USDC/AERO | 3000 | 8,962,899 | 1.411059 | 53024772 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/USDC | 500 | 8,540,114 | 2,369.067480 | 53024772 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 8,494,887 | 0.029369 | 53024772 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,016,761 | 0.001648 | 53024772 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 330 | 6,298,815 | 0.000012 | 53024772 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 150 | 5,503,152 | 2,368.515875 | 53024772 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,457,683 | 0.029393 | 53024772 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | USDC/cbBTC | 400 | 4,860,190 | 0.000012 | 53024772 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,555,196 | 2,368.581805 | 53024772 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,234,464 | 0.998962 | 53024772 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,921,226 | 34,408.914086 | 53024772 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/USDC | 3000 | 3,828,826 | 2,363.522884 | 53024772 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome | VIRTUAL/WETH | 10000 | 3,288,087 | 0.000267 | 53024772 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/USDT | 406 | 2,777,546 | 2,376.349125 | 53024772 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome_slipstream | WETH/VVV | 2706 | 2,506,913 | 97.643881 | 53024772 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,245,285 | 408.903449 | 53024772 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | WETH/FAI | 10000 | 2,118,658 | 1,261,906.512700 | 53024772 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome | WETH/AERO | 10000 | 1,965,415 | 3,323.017810 | 53024772 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,920,313 | 0.000000 | 53024772 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,913,171 | 0.000012 | 53024772 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v3 | XDP/USDC | 100 | 1,778,067 | 0.018296 | 53024772 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,735,816 | 0.000012 | 53024772 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,549,717 | 1.610679 | 53024772 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | WETH/AERO | 3000 | 1,469,256 | 3,342.186063 | 53024772 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,459,069 | 0.825630 | 53024772 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,383,265 | 0.005174 | 53024772 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,377,719 | 13,932.118658 | 53024772 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,281,159 | 2,369.064763 | 53024772 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,260,365 | 0.000265 | 53024772 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | WETH/msETH (stable) | 500 | 1,232,167 | 2.305291 | 53024772 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome | USDC/SEND | 3000 | 1,225,124 | 64.741457 | 53024772 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | DRB/WETH | 10000 | 1,193,776 | 0.000000 | 53024772 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/doginme | 10000 | 1,178,579 | 35,296,733.949307 | 53024772 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | WETH/WELL | 10000 | 1,146,404 | 1,119,941.834879 | 53024772 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome | USDC/NOCK | 3000 | 1,133,809 | 48.723345 | 53024772 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,131,855 | 493,533.548554 | 53024772 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,095,820 | 16.864081 | 53024772 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | WETH/EDEL | 7000 | 1,077,172 | 73,810.257746 | 53024772 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,040,505 | 16.963351 | 53024772 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,039,433 | 21,654,616.189288 | 53024772 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | USDC/VVV | 3000 | 1,035,416 | 0.041300 | 53024772 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 955,262 | 23.314043 | 53024772 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| uniswap_v3 | WETH/MORPHO | 3000 | 925,356 | 1,091.120428 | 53024772 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | uXRP/WETH | 3000 | 895,891 | 0.000539 | 53024772 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 893,109 | 17.482039 | 53024772 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 857,022 | 0.000009 | 53024772 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v2 | WETH/USDC | 3000 | 852,591 | 2,363.618106 | 53024772 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| pancakeswap_v3 | QUID/USDC | 100 | 840,412 | 0.063797 | 53024772 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | weETH_04c0/WETH | 500 | 813,509 | 1.105904 | 53024772 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome | WETH/wstETH | 3000 | 800,369 | 0.803010 | 53024772 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | WETH/USDC | 10000 | 788,087 | 2,373.719186 | 53024772 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/VVV | 10000 | 774,500 | 96.931595 | 53024772 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 755,699 | 0.629129 | 53024772 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 748,743 | 4,702,905.626361 | 53024772 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 728,390 | 0.665325 | 53024772 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |

## Recherche d'opportunités
- Cycles : 18194 ; routes examinées : 350270888 ; candidats optimisés : 1381067 ; net attendu > 0 : 656 ; dernier cycle 125.7 ms
- Rejets (moteur) : {'spread_below_threshold': 344252510, 'liquidity_below_min': 4551435, 'negative_expected_net': 1380411, 'pool_quarantined': 66576, 'borrow_bound_too_small': 18497, 'cycle_budget_exhausted': 803}
- Enregistrements de la session : 1381067 ; net attendu > 0 : 656 ; simulés (eth_call de la vraie tx) : 55 (ok 37, échec 18) ; étiquettes ghost N+1 : 0/33 positives
- Décisions : {'REJECTED': 1381067} ; motifs de rejet : {'below_safety_margin': 359, 'negative_expected_net': 1380411, 'p_lower_below_threshold': 517, 'reliability_not_demonstrated': 139, 'simulation_failed': 18}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53019828 | USDC→[uniswap_v3]→ZORA→[aerodrome_slipstream]→USDC | 433.202296 USDC | 2.497024 USDC | 0.000000 USDC | 0.005697 USDC | 2.491327 USDC (2.2920 €) | — | 57.51 | 0.006 (n=1) | REJECTED | reliability_not_demonstrated |
| 53023291 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→ZORA→[aerodrome_slipstream]→USDC | 102.743356 USDC | 0.506254 USDC | 0.000000 USDC | 0.007459 USDC | 0.498795 USDC (0.4589 €) | — | 48.55 | 0.001 (n=11) | REJECTED | reliability_not_demonstrated |
| 53023291 | WETH→[uniswap_v3]→ZORA→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.043441 WETH | 0.000214 WETH | 0.000000 WETH | 0.000003 WETH | 0.000211 WETH (0.4580 €) | — | 48.53 | 0.001 (n=11) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53019828 | WETH→[uniswap_v3]→ZORA→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.035915 WETH | 0.000213 WETH | 0.000000 WETH | 0.000003 WETH | 0.000209 WETH (0.4580 €) | — | 58.32 | 0.001 (n=10) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53019828 | WETH→[uniswap_v3]→ZORA→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→WETH | 0.035861 WETH | 0.000212 WETH | 0.000000 WETH | 0.000003 WETH | 0.000209 WETH (0.4569 €) | — | 58.27 | 0.001 (n=10) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53019828 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→ZORA→[aerodrome_slipstream]→USDC | 84.993781 USDC | 0.504007 USDC | 0.000000 USDC | 0.007503 USDC | 0.496504 USDC (0.4568 €) | — | 58.42 | 0.001 (n=10) | REJECTED | reliability_not_demonstrated |
| 53023291 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→ZORA→[aerodrome_slipstream]→USDC | 102.306532 USDC | 0.503159 USDC | 0.000000 USDC | 0.007459 USDC | 0.495700 USDC (0.4560 €) | — | 48.45 | 0.001 (n=10) | REJECTED | reliability_not_demonstrated |
| 53019828 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→ZORA→[aerodrome_slipstream]→USDC | 84.883041 USDC | 0.502795 USDC | 0.000000 USDC | 0.007503 USDC | 0.495292 USDC (0.4557 €) | — | 58.35 | 0.001 (n=10) | REJECTED | reliability_not_demonstrated |
| 53023291 | WETH→[uniswap_v3]→ZORA→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.043285 WETH | 0.000213 WETH | 0.000000 WETH | 0.000003 WETH | 0.000209 WETH (0.4552 €) | — | 48.40 | 0.001 (n=10) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53019828 | WETH→[uniswap_v3]→ZORA→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.035568 WETH | 0.000210 WETH | 0.000000 WETH | 0.000003 WETH | 0.000207 WETH (0.4524 €) | — | 58.16 | 0.001 (n=10) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53019828 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→ZORA→[aerodrome_slipstream]→USDC | 84.325109 USDC | 0.497921 USDC | 0.000000 USDC | 0.007503 USDC | 0.490418 USDC (0.4512 €) | — | 58.16 | 0.001 (n=10) | REJECTED | reliability_not_demonstrated |
| 53023291 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→ZORA→[aerodrome_slipstream]→USDC | 101.485194 USDC | 0.485944 USDC | 0.000000 USDC | 0.007459 USDC | 0.478485 USDC (0.4402 €) | — | 47.15 | 0.001 (n=10) | REJECTED | reliability_not_demonstrated |
| 53023291 | WETH→[uniswap_v3]→ZORA→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.042898 WETH | 0.000205 WETH | 0.000000 WETH | 0.000003 WETH | 0.000202 WETH (0.4393 €) | — | 47.13 | 0.001 (n=10) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53023291 | USDC→[sushiswap_v3]→WETH→[uniswap_v3]→ZORA→[aerodrome_slipstream]→USDC | 99.749668 USDC | 0.483652 USDC | 0.000000 USDC | 0.007459 USDC | 0.476193 USDC (0.4381 €) | — | 47.74 | 0.001 (n=10) | REJECTED | reliability_not_demonstrated |
| 53023291 | WETH→[uniswap_v3]→ZORA→[aerodrome_slipstream]→USDC→[sushiswap_v3]→WETH | 0.042192 WETH | 0.000204 WETH | 0.000000 WETH | 0.000003 WETH | 0.000201 WETH (0.4371 €) | — | 47.68 | 0.001 (n=10) | REJECTED | reliability_not_demonstrated |
| 53023291 | USDC→[uniswap_v2]→WETH→[uniswap_v3]→ZORA→[aerodrome_slipstream]→USDC | 99.671890 USDC | 0.480912 USDC | 0.000000 USDC | 0.006726 USDC | 0.474186 USDC (0.4363 €) | — | 47.57 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 53023291 | WETH→[uniswap_v3]→ZORA→[aerodrome_slipstream]→USDC→[uniswap_v2]→WETH | 0.042125 WETH | 0.000203 WETH | 0.000000 WETH | 0.000003 WETH | 0.000200 WETH (0.4352 €) | — | 47.55 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 53023291 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→ZORA→[aerodrome_slipstream]→USDC | 100.441467 USDC | 0.470287 USDC | 0.000000 USDC | 0.007459 USDC | 0.462828 USDC (0.4258 €) | — | 46.08 | 0.001 (n=11) | REJECTED | reliability_not_demonstrated |
| 53023291 | WETH→[uniswap_v3]→ZORA→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.042448 WETH | 0.000199 WETH | 0.000000 WETH | 0.000003 WETH | 0.000196 WETH (0.4248 €) | — | 46.07 | 0.001 (n=11) | REJECTED | reliability_not_demonstrated |
| 53019828 | WETH→[uniswap_v3]→ZORA→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.033945 WETH | 0.000190 WETH | 0.000000 WETH | 0.000003 WETH | 0.000187 WETH (0.4096 €) | — | 55.18 | 0.001 (n=10) | REJECTED | reliability_not_demonstrated |
| 53019828 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→ZORA→[aerodrome_slipstream]→USDC | 80.399853 USDC | 0.451418 USDC | 0.000000 USDC | 0.007142 USDC | 0.444276 USDC (0.4087 €) | — | 55.26 | 0.001 (n=10) | REJECTED | reliability_not_demonstrated |
| 53023291 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→ZORA→[aerodrome_slipstream]→USDC | 99.279641 USDC | 0.451039 USDC | 0.000000 USDC | 0.007459 USDC | 0.443580 USDC (0.4081 €) | — | 44.68 | 0.001 (n=10) | REJECTED | reliability_not_demonstrated |
| 53023291 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→ZORA→[uniswap_v3]→USDC | 100.488789 USDC | 0.450528 USDC | 0.000000 USDC | 0.007459 USDC | 0.443069 USDC (0.4076 €) | — | 44.09 | 0.001 (n=11) | REJECTED | reliability_not_demonstrated |
| 53023291 | WETH→[uniswap_v3]→ZORA→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→WETH | 0.041948 WETH | 0.000191 WETH | 0.000000 WETH | 0.000003 WETH | 0.000187 WETH (0.4071 €) | — | 44.67 | 0.001 (n=10) | REJECTED | reliability_not_demonstrated |
| 53023291 | WETH→[uniswap_v3]→ZORA→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.042484 WETH | 0.000190 WETH | 0.000000 WETH | 0.000003 WETH | 0.000187 WETH (0.4069 €) | — | 44.08 | 0.001 (n=11) | REJECTED | reliability_not_demonstrated |

## Fiabilité et décision
- Observations ghost : 2126 ; taux observé 0.096 ; borne inférieure crédible (0.9) 0.088 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 8.8% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ✅ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
