# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-23T13:17:39+00:00 ; durée 18.2 min ; blocs 52985506 → 52986055 (533 vus)

## Connexion
- Requêtes RPC : 6661 ; erreurs : 0 ; latence p50/p95 : 241.4/1,282.0 ms
- Rafraîchissements d'état : 534 ; âge des données au dernier bloc : 1.77 s ; changements de frais LP observés (pools à frais dynamiques) : 864
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 8451 ; cycles déclenchés par événement : 864 ; avance médiane sur le rafraîchissement multicall : 577 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,396.21 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 544 pools, 316 jetons, 19376 routes
- Par DEX : uniswap_v3 137, aerodrome 221, aerodrome_slipstream 137, pancakeswap_v3 32, uniswap_v2 13, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 200 (rejetés 2) → 605 jetons ; pools candidats 3880 (énumérés 358, par paires 0), mesurés 546, sous le plancher de 10000.0 $ : 2 → gardés 544 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDC': 1.0, 'USDbC': 1.0, 'WETH': 2396.209038, 'AERO': 0.783075, 'cbBTC': 81657.338706}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 156,694,960 | 2,396.208633 | 52986055 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,458,393 | 0.029382 | 52986055 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 12,821,328 | 92.601432 | 52986055 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| aerodrome | USDC/AERO | 3000 | 10,811,086 | 1.295507 | 52986055 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,326,298 | 0.029405 | 52986055 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,868,887 | 0.000012 | 52986055 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 8,893,832 | 0.029394 | 52986055 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/USDC | 500 | 8,681,846 | 2,395.596452 | 52986055 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,159,379 | 0.001669 | 52986055 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 334 | 6,351,675 | 0.000012 | 52986055 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 150 | 5,586,188 | 2,394.874221 | 52986055 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,444,734 | 0.029371 | 52986055 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | USDC/cbBTC | 424 | 5,092,941 | 0.000012 | 52986055 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,542,054 | 2,394.581247 | 52986055 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,292,001 | 0.999613 | 52986055 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/USDC | 3000 | 4,280,164 | 2,397.466961 | 52986055 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome | WETH/KTA | 3000 | 4,001,297 | 33,980.928696 | 52986055 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | VIRTUAL/WETH | 10000 | 3,402,134 | 0.000275 | 52986055 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/USDT | 415 | 2,902,922 | 2,399.381922 | 52986055 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome_slipstream | WETH/VVV | 2718 | 2,550,478 | 92.618298 | 52986055 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,310,126 | 391.544834 | 52986055 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | WETH/FAI | 10000 | 2,215,460 | 1,186,015.808845 | 52986055 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome | WETH/AERO | 10000 | 2,096,245 | 3,080.166157 | 52986055 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,988,434 | 0.000000 | 52986055 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,921,762 | 0.000012 | 52986055 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v3 | XDP/USDC | 100 | 1,757,575 | 0.017663 | 52986055 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,752,199 | 0.000012 | 52986055 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | WETH/AERO | 3000 | 1,596,224 | 3,101.959050 | 52986055 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,557,007 | 1.603839 | 52986055 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,458,271 | 0.823779 | 52986055 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,419,123 | 13,317.918155 | 52986055 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,384,031 | 0.005032 | 52986055 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome | WETH/msETH (stable) | 500 | 1,298,500 | 2.314608 | 52986055 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,295,690 | 0.000276 | 52986055 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,280,737 | 2,395.394537 | 52986055 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | DRB/WETH | 10000 | 1,255,932 | 0.000000 | 52986055 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | USDC/SEND | 3000 | 1,228,575 | 64.378255 | 52986055 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,182,160 | 36,279,696.618889 | 52986055 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,169,087 | 16.222508 | 52986055 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | WETH/WELL | 10000 | 1,163,253 | 1,118,728.799070 | 52986055 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,156,902 | 482,603.731170 | 52986055 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | USDC/NOCK | 3000 | 1,140,976 | 48.126372 | 52986055 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | USDC/VVV | 3000 | 1,085,145 | 0.038663 | 52986055 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | WETH/EDEL | 7000 | 1,082,347 | 75,461.659440 | 52986055 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,075,423 | 20,901,603.416754 | 52986055 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,054,030 | 16.384061 | 52986055 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome_slipstream | AERO/cbBTC | 2700 | 1,017,872 | 0.000009 | 52986055 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,009,851 | 23.074969 | 52986055 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| uniswap_v3 | WETH/MORPHO | 3000 | 954,511 | 1,056.101527 | 52986055 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/USDC | 10000 | 938,610 | 2,390.321440 | 52986055 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | uXRP/WETH | 3000 | 916,074 | 0.000548 | 52986055 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 890,119 | 17.558099 | 52986055 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v2 | WETH/USDC | 3000 | 858,501 | 2,398.690511 | 52986055 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome | weETH_04c0/WETH | 500 | 835,449 | 1.105789 | 52986055 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome | WETH/wstETH | 3000 | 811,787 | 0.803225 | 52986055 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| pancakeswap_v3 | QUID/USDC | 100 | 798,164 | 0.057163 | 52986055 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 778,473 | 0.661699 | 52986055 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 776,810 | 4,489,707.569289 | 52986055 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v2 | WETH/NPC | 3000 | 733,389 | 134,256.041035 | 52986055 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| uniswap_v3 | TIG/USDC | 10000 | 731,477 | 0.670802 | 52986055 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |

## Recherche d'opportunités
- Cycles : 1397 ; routes examinées : 27068272 ; candidats optimisés : 92029 ; net attendu > 0 : 25 ; dernier cycle 210.1 ms
- Rejets (moteur) : {'spread_below_threshold': 26578493, 'liquidity_below_min': 396353, 'negative_expected_net': 92004, 'borrow_bound_too_small': 1397}
- Enregistrements de la session : 92029 ; net attendu > 0 : 25 ; simulés (eth_call de la vraie tx) : 3 (ok 0, échec 3) ; étiquettes ghost N+1 : 3/3 positives
- Décisions : {'REJECTED': 92029} ; motifs de rejet : {'below_safety_margin': 18, 'negative_expected_net': 92004, 'p_lower_below_threshold': 23, 'reliability_not_demonstrated': 2, 'simulation_failed': 3}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52986006 | WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→wstETH→[uniswap_v3]→WETH | 0.046809 WETH | 0.000029 WETH | 0.000000 WETH | 0.000003 WETH | 0.000026 WETH (0.0569 €) | — | 5.51 | 0.097 (n=202) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.10<0.75) |
| 52986006 | WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→wstETH→[aerodrome_slipstream]→WETH | 0.045023 WETH | 0.000027 WETH | 0.000000 WETH | 0.000003 WETH | 0.000024 WETH (0.0521 €) | — | 5.25 | 0.097 (n=202) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.10<0.75) |
| 52986006 | WETH→[pancakeswap_v3]→AERO→[aerodrome]→wstETH→[uniswap_v3]→WETH | 0.017799 WETH | 0.000013 WETH | 0.000000 WETH | 0.000003 WETH | 0.000010 WETH (0.0214 €) | — | 5.46 | 0.000 (n=31) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 52985755 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC | 289.176647 USDC | 0.029169 USDC | 0.000000 USDC | 0.007213 USDC | 0.021956 USDC (0.0202 €) | — | 0.76 | 0.238 (n=118) | REJECTED | below_safety_margin(21956<57835), p_lower_below_threshold(0.24<0.75) |
| 52985755 | WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.121755 WETH | 0.000012 WETH | 0.000000 WETH | 0.000003 WETH | 0.000009 WETH (0.0202 €) | — | 0.75 | 0.238 (n=118) | REJECTED | below_safety_margin(9157928971941<24350924358503), p_lower_below_threshold(0.24<0.75) |
| 52986006 | WETH→[pancakeswap_v3]→AERO→[aerodrome]→wstETH→[aerodrome_slipstream]→WETH | 0.017202 WETH | 0.000012 WETH | 0.000000 WETH | 0.000003 WETH | 0.000009 WETH (0.0196 €) | — | 5.16 | 0.000 (n=31) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 52986006 | WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.051019 WETH | 0.000012 WETH | 0.000000 WETH | 0.000003 WETH | 0.000009 WETH (0.0195 €) | — | 1.73 | 0.116 (n=238) | REJECTED | below_safety_margin(8850100595114<10203803202785), p_lower_below_threshold(0.12<0.75) |
| 52986006 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.001279 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0195 €) | — | 2.03 | 0.116 (n=238) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52986006 | cbBTC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.000857 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0143 €) | — | 2.22 | 0.116 (n=238) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52986006 | WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→WETH | 0.031308 WETH | 0.000009 WETH | 0.000000 WETH | 0.000003 WETH | 0.000006 WETH (0.0143 €) | — | 2.07 | 0.116 (n=238) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52986006 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.000866 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0053 €) | — | 0.81 | 0.116 (n=238) | REJECTED | below_safety_margin(7<17), p_lower_below_threshold(0.12<0.75) |
| 52986006 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 70.643075 USDC | 0.013040 USDC | 0.000000 USDC | 0.007610 USDC | 0.005430 USDC (0.0050 €) | — | 0.77 | 0.116 (n=238) | REJECTED | below_safety_margin(5430<14128), p_lower_below_threshold(0.12<0.75) |
| 52986006 | USDC→[uniswap_v3]→AERO→[aerodrome]→USDbC→[aerodrome_slipstream]→USDC | 29.253893 USDC | 0.008457 USDC | 0.000000 USDC | 0.006913 USDC | 0.001544 USDC (0.0014 €) | — | 0.53 | 0.120 (n=91) | REJECTED | below_safety_margin(1544<5850), p_lower_below_threshold(0.12<0.75) |
| 52985755 | USDC→[uniswap_v3]→WETH→[sushiswap_v3]→USDC | 48.036433 USDC | 0.006413 USDC | 0.000000 USDC | 0.005390 USDC | 0.001023 USDC (0.0009 €) | — | 0.21 | 0.020 (n=15) | REJECTED | below_safety_margin(1023<9607), reliability_not_demonstrated |
| 52985755 | WETH→[sushiswap_v3]→USDC→[uniswap_v3]→WETH | 0.020208 WETH | 0.000003 WETH | 0.000000 WETH | 0.000002 WETH | 0.000000 WETH (0.0009 €) | — | 0.21 | 0.020 (n=15) | REJECTED | below_safety_margin(426334042271<4041559444584), reliability_not_demonstrated |
| 52985755 | WETH→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.033637 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0009 €) | — | 0.12 | 0.116 (n=238) | REJECTED | below_safety_margin(412333434459<6727443415458), p_lower_below_threshold(0.12<0.75) |
| 52985755 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 64.092038 USDC | 0.008044 USDC | 0.000000 USDC | 0.007213 USDC | 0.000831 USDC (0.0008 €) | — | 0.13 | 0.116 (n=238) | REJECTED | below_safety_margin(831<12818), p_lower_below_threshold(0.12<0.75) |
| 52985755 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→cbBTC | 0.000834 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0007 €) | — | 0.12 | 0.116 (n=238) | REJECTED | below_safety_margin(1<16), p_lower_below_threshold(0.12<0.75) |
| 52985755 | cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→cbBTC | 0.000834 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0007 €) | — | 0.12 | 0.238 (n=118) | REJECTED | below_safety_margin(1<16), p_lower_below_threshold(0.24<0.75) |
| 52985755 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.001272 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0007 €) | — | 0.08 | 0.116 (n=238) | REJECTED | below_safety_margin(1<25), p_lower_below_threshold(0.12<0.75) |
| 52985755 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 137.798658 USDC | 0.007898 USDC | 0.000000 USDC | 0.007213 USDC | 0.000685 USDC (0.0006 €) | — | 0.05 | 0.116 (n=238) | REJECTED | below_safety_margin(685<27559), p_lower_below_threshold(0.12<0.75) |
| 52985755 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.056805 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0005 €) | — | 0.04 | 0.116 (n=238) | REJECTED | below_safety_margin(217032132791<11360901774582), p_lower_below_threshold(0.12<0.75) |
| 52985755 | WETH→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.031327 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0003 €) | — | 0.04 | 0.238 (n=118) | REJECTED | below_safety_margin(135955892089<6265393353516), p_lower_below_threshold(0.24<0.75) |
| 52985755 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→USDC | 72.493619 USDC | 0.007504 USDC | 0.000000 USDC | 0.007213 USDC | 0.000291 USDC (0.0003 €) | — | 0.04 | 0.238 (n=118) | REJECTED | below_safety_margin(291<14498), p_lower_below_threshold(0.24<0.75) |
| 52985755 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.045605 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0000 €) | — | 0.00 | 0.116 (n=238) | REJECTED | below_safety_margin(20037416366<9120909430393), p_lower_below_threshold(0.12<0.75) |

## Fiabilité et décision
- Observations ghost : 1987 ; taux observé 0.098 ; borne inférieure crédible (0.9) 0.089 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 8.9% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
