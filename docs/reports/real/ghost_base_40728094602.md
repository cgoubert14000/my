# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-28T17:52:46+00:00 ; durée 67.2 min ; blocs 53208289 → 53210304 (1913 vus)

## Connexion
- Requêtes RPC : 21759 ; erreurs : 85 ; latence p50/p95 : 536.6/2,730.2 ms
- Rafraîchissements d'état : 1913 ; âge des données au dernier bloc : 9.59 s ; changements de frais LP observés (pools à frais dynamiques) : 2835
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 8473 ; cycles déclenchés par événement : 639 ; avance médiane sur le rafraîchissement multicall : 1,130 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,338.65 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 517 pools, 298 jetons, 19028 routes
- Par DEX : uniswap_v3 144, aerodrome_slipstream 121, aerodrome 210, pancakeswap_v3 28, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 183 (rejetés 2) → 588 jetons ; pools candidats 3758 (énumérés 330, par paires 0), mesurés 519, sous le plancher de 10000.0 $ : 2 → gardés 517 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDC': 1.0, 'USDbC': 1.0, 'WETH': 2331.23448, 'cbBTC': 80382.611332, 'AERO': 0.701638}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 157,550,833 | 2,338.652590 | 53210305 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,489,074 | 0.029026 | 53210305 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,863,800 | 0.000012 | 53210305 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,436,641 | 0.028977 | 53210305 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 8,494,719 | 2,344.237842 | 53210305 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 8,235,064 | 97.836555 | 53210305 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,024,385 | 0.001646 | 53210305 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 6,764,789 | 1.436025 | 53210305 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,798,839 | 0.029031 | 53210305 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/USDC | 728 | 4,932,838 | 2,345.082396 | 53210305 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,425,860 | 2,344.955929 | 53210305 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,242,898 | 0.998804 | 53210305 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,690,672 | 37,584.346079 | 53210305 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2505 | 2,931,286 | 0.028971 | 53210305 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2709 | 2,513,038 | 97.880540 | 53210305 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | USDC/cbBTC | 508 | 2,384,514 | 0.000012 | 53210305 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome | WETH/FAI | 10000 | 2,137,046 | 1,214,151.729099 | 53210305 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome | WETH/USDC | 3000 | 1,856,899 | 2,339.410426 | 53210305 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| uniswap_v3 | XDP/USDC | 100 | 1,823,788 | 0.018696 | 53210305 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,778,855 | 401.665062 | 53210305 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,775,454 | 0.000000 | 53210305 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,717,687 | 0.000012 | 53210305 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,692,105 | 0.000012 | 53210305 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | USDC/cbBTC | 348 | 1,665,341 | 0.000012 | 53210305 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,514,132 | 1.588195 | 53210305 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,488,938 | 0.005718 | 53210305 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,460,758 | 0.826986 | 53210305 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,455,099 | 3,359.455044 | 53210305 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,383,765 | 13,851.041189 | 53210305 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,244,514 | 2,344.283167 | 53210305 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,242,400 | 0.000265 | 53210305 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | USDC/SEND | 3000 | 1,193,805 | 68.182945 | 53210305 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome | VIRTUAL/WETH | 10000 | 1,157,135 | 0.000266 | 53210305 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | WETH/doginme | 10000 | 1,153,670 | 36,550,416.191071 | 53210305 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | WETH/WELL | 10000 | 1,152,298 | 1,080,107.736919 | 53210305 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,123,306 | 504,301.772759 | 53210305 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,117,852 | 0.000000 | 53210305 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,083,259 | 21,137,337.930642 | 53210305 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome | WETH/EDEL | 7000 | 1,077,205 | 72,008.760478 | 53210305 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | WETH/AERO | 10000 | 1,073,756 | 3,335.376067 | 53210305 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,052,111 | 16.470705 | 53210305 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | USDC/NOCK | 3000 | 1,007,008 | 61.732022 | 53210305 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/VVV | 10000 | 993,696 | 97.422201 | 53210305 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | USDC/VVV | 3000 | 993,531 | 0.041844 | 53210305 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/USDC | 10000 | 938,552 | 2,344.326232 | 53210305 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 927,302 | 1,060.872925 | 53210305 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | uXRP/WETH | 3000 | 903,950 | 0.000560 | 53210305 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome | WETH/msETH (stable) | 500 | 878,946 | 2.329445 | 53210305 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | USDC/SAPIEN | 4525 | 872,043 | 18.217120 | 53210305 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v2 | WETH/USDC | 3000 | 847,737 | 2,338.480992 | 53210305 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 835,402 | 17.702058 | 53210305 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| pancakeswap_v3 | QUID/USDC | 100 | 805,270 | 0.058205 | 53210305 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 791,910 | 0.802973 | 53210305 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 754,959 | 0.000009 | 53210305 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 746,562 | 4,632,969.863717 | 53210305 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 744,364 | 0.618755 | 53210305 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/NPC | 3000 | 706,336 | 138,059.516032 | 53210305 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | WETH/BRETT | 2102 | 692,391 | 502,169.567560 | 53210305 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 666,556 | 0.106756 | 53210305 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| uniswap_v3 | TIG/USDC | 10000 | 662,804 | 0.553976 | 53210305 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |

## Recherche d'opportunités
- Cycles : 2551 ; routes examinées : 48540428 ; candidats optimisés : 174738 ; net attendu > 0 : 261 ; dernier cycle 316.9 ms
- Rejets (moteur) : {'spread_below_threshold': 47739558, 'liquidity_below_min': 623268, 'negative_expected_net': 174477, 'borrow_bound_too_small': 2548, 'cycle_budget_exhausted': 316}
- Enregistrements de la session : 174738 ; net attendu > 0 : 261 ; simulés (eth_call de la vraie tx) : 8 (ok 2, échec 6) ; étiquettes ghost N+1 : 0/8 positives
- Décisions : {'REJECTED': 174738} ; motifs de rejet : {'below_safety_margin': 248, 'negative_expected_net': 174477, 'p_lower_below_threshold': 227, 'reliability_not_demonstrated': 34, 'simulation_failed': 6, 'stale_data': 70}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53210296 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 637.241527 USDC | 0.047417 USDC | 0.000000 USDC | 0.007408 USDC | 0.040009 USDC (0.0368 €) | — | 0.63 | 0.001 (n=7) | REJECTED | below_safety_margin(40009<127448), reliability_not_demonstrated |
| 53210297 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 637.241527 USDC | 0.047417 USDC | 0.000000 USDC | 0.007408 USDC | 0.040009 USDC (0.0368 €) | — | 0.63 | 0.001 (n=7) | REJECTED | below_safety_margin(40009<127448), reliability_not_demonstrated |
| 53210296 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.298264 WETH | 0.000020 WETH | 0.000000 WETH | 0.000003 WETH | 0.000017 WETH (0.0365 €) | — | 0.57 | 0.001 (n=7) | REJECTED | below_safety_margin(16960518600437<59652855271606), reliability_not_demonstrated |
| 53210297 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.298264 WETH | 0.000020 WETH | 0.000000 WETH | 0.000003 WETH | 0.000017 WETH (0.0365 €) | — | 0.57 | 0.001 (n=7) | REJECTED | below_safety_margin(16960518600437<59652855271606), reliability_not_demonstrated |
| 53210296 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.007632 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0363 €) | — | 0.64 | 0.001 (n=7) | REJECTED | below_safety_margin(49<152), reliability_not_demonstrated |
| 53210297 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.007632 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0363 €) | — | 0.64 | 0.001 (n=7) | REJECTED | below_safety_margin(49<152), reliability_not_demonstrated |
| 53208319 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.122130 WETH | 0.000013 WETH | 0.000000 WETH | 0.000003 WETH | 0.000010 WETH (0.0223 €) | — | 0.85 | 0.122 (n=412) | REJECTED | below_safety_margin(10414748764798<24426083849228), stale_data(5490ms>4000.0), p_lower_below_threshold(0.12<0.75) |
| 53208322 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.122130 WETH | 0.000013 WETH | 0.000000 WETH | 0.000003 WETH | 0.000010 WETH (0.0223 €) | — | 0.85 | 0.122 (n=412) | REJECTED | below_safety_margin(10414748764798<24426083849228), stale_data(6530ms>4000.0), p_lower_below_threshold(0.12<0.75) |
| 53208319 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 301.138389 USDC | 0.031316 USDC | 0.000000 USDC | 0.007037 USDC | 0.024279 USDC (0.0223 €) | — | 0.81 | 0.122 (n=412) | REJECTED | below_safety_margin(24279<60227), stale_data(5497ms>4000.0), p_lower_below_threshold(0.12<0.75) |
| 53208322 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 301.138389 USDC | 0.031316 USDC | 0.000000 USDC | 0.007037 USDC | 0.024279 USDC (0.0223 €) | — | 0.81 | 0.122 (n=412) | REJECTED | below_safety_margin(24279<60227), stale_data(6537ms>4000.0), p_lower_below_threshold(0.12<0.75) |
| 53208319 | cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.003647 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0222 €) | — | 0.82 | 0.122 (n=412) | REJECTED | below_safety_margin(30<72), stale_data(5504ms>4000.0), p_lower_below_threshold(0.12<0.75) |
| 53208322 | cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.003647 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0222 €) | — | 0.82 | 0.122 (n=412) | REJECTED | below_safety_margin(30<72), stale_data(6544ms>4000.0), p_lower_below_threshold(0.12<0.75) |
| 53208319 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 288.371092 USDC | 0.027508 USDC | 0.000000 USDC | 0.007037 USDC | 0.020471 USDC (0.0188 €) | — | 0.71 | 0.001 (n=7) | REJECTED | below_safety_margin(20471<57674), stale_data(5537ms>4000.0), reliability_not_demonstrated |
| 53208322 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 288.371092 USDC | 0.027508 USDC | 0.000000 USDC | 0.007037 USDC | 0.020471 USDC (0.0188 €) | — | 0.71 | 0.001 (n=7) | REJECTED | below_safety_margin(20471<57674), stale_data(6576ms>4000.0), reliability_not_demonstrated |
| 53208319 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.110251 WETH | 0.000012 WETH | 0.000000 WETH | 0.000003 WETH | 0.000009 WETH (0.0187 €) | — | 0.79 | 0.001 (n=7) | REJECTED | below_safety_margin(8741214283322<22050149691238), stale_data(5545ms>4000.0), reliability_not_demonstrated |
| 53208322 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.110251 WETH | 0.000012 WETH | 0.000000 WETH | 0.000003 WETH | 0.000009 WETH (0.0187 €) | — | 0.79 | 0.001 (n=7) | REJECTED | below_safety_margin(8741214283322<22050149691238), stale_data(6583ms>4000.0), reliability_not_demonstrated |
| 53208319 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.003647 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0185 €) | — | 0.69 | 0.001 (n=7) | REJECTED | below_safety_margin(25<72), stale_data(5530ms>4000.0), reliability_not_demonstrated |
| 53208322 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.003647 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0185 €) | — | 0.69 | 0.001 (n=7) | REJECTED | below_safety_margin(25<72), stale_data(6569ms>4000.0), reliability_not_demonstrated |
| 53210296 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 233.759353 USDC | 0.023321 USDC | 0.000000 USDC | 0.005271 USDC | 0.018050 USDC (0.0166 €) | — | 0.77 | 0.032 (n=111) | REJECTED | below_safety_margin(18050<46751), p_lower_below_threshold(0.03<0.75) |
| 53210297 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 233.759353 USDC | 0.023321 USDC | 0.000000 USDC | 0.005271 USDC | 0.018050 USDC (0.0166 €) | — | 0.77 | 0.032 (n=111) | REJECTED | below_safety_margin(18050<46751), p_lower_below_threshold(0.03<0.75) |
| 53210296 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.100354 WETH | 0.000010 WETH | 0.000000 WETH | 0.000002 WETH | 0.000008 WETH (0.0166 €) | — | 0.77 | 0.032 (n=111) | REJECTED | below_safety_margin(7693992761397<20070884406133), p_lower_below_threshold(0.03<0.75) |
| 53210297 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.100354 WETH | 0.000010 WETH | 0.000000 WETH | 0.000002 WETH | 0.000008 WETH (0.0166 €) | — | 0.77 | 0.032 (n=111) | REJECTED | below_safety_margin(7693992761397<20070884406133), p_lower_below_threshold(0.03<0.75) |
| 53208319 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 268.781622 USDC | 0.024180 USDC | 0.000000 USDC | 0.007037 USDC | 0.017143 USDC (0.0158 €) | — | 0.64 | 0.122 (n=412) | REJECTED | below_safety_margin(17143<53756), stale_data(5564ms>4000.0), p_lower_below_threshold(0.12<0.75) |
| 53208322 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 268.781622 USDC | 0.024180 USDC | 0.000000 USDC | 0.007037 USDC | 0.017143 USDC (0.0158 €) | — | 0.64 | 0.122 (n=412) | REJECTED | below_safety_margin(17143<53756), stale_data(6602ms>4000.0), p_lower_below_threshold(0.12<0.75) |
| 53208319 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.111410 WETH | 0.000010 WETH | 0.000000 WETH | 0.000003 WETH | 0.000007 WETH (0.0157 €) | — | 0.66 | 0.122 (n=412) | REJECTED | below_safety_margin(7313454472818<22281999774565), stale_data(5571ms>4000.0), p_lower_below_threshold(0.12<0.75) |

## Fiabilité et décision
- Observations ghost : 2973 ; taux observé 0.093 ; borne inférieure crédible (0.9) 0.087 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 8.7% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
