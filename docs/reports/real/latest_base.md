# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-30T02:34:11+00:00 ; durée 6.04 min ; blocs 53268968 → 53269151 (182 vus)

## Connexion
- Requêtes RPC : 2259 ; erreurs : 0 ; latence p50/p95 : 74.0/1,241.0 ms
- Rafraîchissements d'état : 183 ; âge des données au dernier bloc : 1.82 s ; changements de frais LP observés (pools à frais dynamiques) : 568
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 3857 ; cycles déclenchés par événement : 191 ; avance médiane sur le rafraîchissement multicall : 1,019 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,206.97 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 492 pools, 287 jetons, 18448 routes
- Par DEX : uniswap_v3 134, aerodrome 205, aerodrome_slipstream 111, pancakeswap_v3 28, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 178 (rejetés 2) → 583 jetons ; pools candidats 3735 (énumérés 314, par paires 0), mesurés 494, sous le plancher de 10000.0 $ : 2 → gardés 492 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2206.596047, 'cbBTC': 77084.188033, 'AERO': 0.611873}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 148,358,177 | 2,206.966594 | 53269151 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,889,916 | 0.028653 | 53269151 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,442,491 | 0.000013 | 53269151 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 8,957,176 | 0.028665 | 53269151 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 8,011,540 | 2,207.275900 | 53269151 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,718,715 | 99.060239 | 53269151 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,639,781 | 0.001609 | 53269151 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 6,034,923 | 1.633451 | 53269151 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,512,664 | 0.028650 | 53269151 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/USDC | 150 | 4,203,663 | 2,207.819206 | 53269151 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,121,540 | 2,208.024327 | 53269151 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,529,829 | 1.000384 | 53269151 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,475,474 | 37,739.142822 | 53269151 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,738,785 | 0.028677 | 53269151 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2739 | 2,290,281 | 99.031592 | 53269151 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | WETH/FAI | 10000 | 2,017,274 | 1,213,474.723704 | 53269151 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 496 | 1,981,178 | 0.000013 | 53269151 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | XDP/USDC | 100 | 1,744,652 | 0.017882 | 53269151 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,664,170 | 414.726634 | 53269151 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,649,550 | 0.000000 | 53269151 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,633,058 | 0.000013 | 53269151 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,607,880 | 0.000013 | 53269151 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | WETH/USDC | 3000 | 1,531,856 | 2,208.081214 | 53269151 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,514,116 | 1.588220 | 53269151 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | USDC/cbBTC | 346 | 1,461,049 | 0.000013 | 53269151 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,453,259 | 0.826796 | 53269151 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,329,163 | 3,612.190384 | 53269151 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,300,608 | 14,492.834362 | 53269151 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,286,453 | 0.005145 | 53269151 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,267,697 | 2,207.527112 | 53269151 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,178,295 | 69.989676 | 53269151 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,149,347 | 0.000254 | 53269151 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| uniswap_v3 | WETH/doginme | 10000 | 1,088,203 | 36,519,405.774328 | 53269151 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,036,770 | 520,674.742355 | 53269151 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | WETH/EDEL | 7000 | 1,007,744 | 73,255.617666 | 53269151 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,006,326 | 18.611256 | 53269151 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v2 | WETH/USDC | 3000 | 1,001,582 | 2,207.316503 | 53269151 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| uniswap_v3 | WETH/TOSHI | 10000 | 992,469 | 22,058,879.534593 | 53269151 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | DRB/WETH | 10000 | 984,155 | 0.000000 | 53269151 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | VIRTUAL/WETH | 10000 | 964,913 | 0.000253 | 53269151 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | USDC/VVV | 3000 | 959,095 | 0.044750 | 53269151 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/VVV | 10000 | 945,206 | 99.767694 | 53269151 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome | USDC/NOCK | 3000 | 934,980 | 71.610684 | 53269151 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome | WETH/AERO | 10000 | 933,867 | 3,594.057929 | 53269151 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | WETH/USDC | 10000 | 912,536 | 2,201.188701 | 53269151 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome | WETH/WELL | 10000 | 912,142 | 1,223,985.058655 | 53269151 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/MORPHO | 3000 | 855,128 | 1,097.958184 | 53269151 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | uXRP/WETH | 3000 | 844,469 | 0.000548 | 53269151 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | USDC/SAPIEN | 4510 | 832,523 | 19.616386 | 53269151 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 812,880 | 0.059351 | 53269151 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 766,492 | 18.246632 | 53269151 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | WETH/wstETH | 3000 | 747,020 | 0.803616 | 53269151 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 700,306 | 4,690,887.584205 | 53269151 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 690,490 | 0.562710 | 53269151 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 684,204 | 0.000008 | 53269151 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | WETH/msETH (stable) | 500 | 672,404 | 2.330114 | 53269151 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | WETH/BRETT | 2156 | 642,879 | 516,641.207844 | 53269151 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | TIG/USDC | 10000 | 636,839 | 0.512723 | 53269151 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/NPC | 3000 | 632,255 | 153,553.038204 | 53269151 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 604,404 | 0.091285 | 53269151 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |

## Recherche d'opportunités
- Cycles : 373 ; routes examinées : 6881104 ; candidats optimisés : 48342 ; net attendu > 0 : 31 ; dernier cycle 325.8 ms
- Rejets (moteur) : {'spread_below_threshold': 6705878, 'liquidity_below_min': 125765, 'negative_expected_net': 48311, 'unquotable': 746, 'borrow_bound_too_small': 373}
- Enregistrements de la session : 48342 ; net attendu > 0 : 31 ; simulés (eth_call de la vraie tx) : 0 (ok 0, échec 0) ; étiquettes ghost N+1 : 0/0 positives
- Décisions : {'REJECTED': 48342} ; motifs de rejet : {'below_safety_margin': 31, 'negative_expected_net': 48311, 'p_lower_below_threshold': 26, 'reliability_not_demonstrated': 5}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53268997 | USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 91.126172 USDC | 0.021526 USDC | 0.000000 USDC | 0.007966 USDC | 0.013560 USDC (0.0125 €) | — | 1.49 | 0.167 (n=253) | REJECTED | below_safety_margin(13560<18225), p_lower_below_threshold(0.17<0.75) |
| 53268997 | USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 91.126172 USDC | 0.021526 USDC | 0.000000 USDC | 0.007966 USDC | 0.013560 USDC (0.0125 €) | — | 1.49 | 0.167 (n=253) | REJECTED | below_safety_margin(13560<18225), p_lower_below_threshold(0.17<0.75) |
| 53268997 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH | 0.041637 WETH | 0.000010 WETH | 0.000000 WETH | 0.000004 WETH | 0.000006 WETH (0.0124 €) | — | 1.47 | 0.167 (n=253) | REJECTED | below_safety_margin(6116987069775<8327346213300), p_lower_below_threshold(0.17<0.75) |
| 53268997 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH | 0.041637 WETH | 0.000010 WETH | 0.000000 WETH | 0.000004 WETH | 0.000006 WETH (0.0124 €) | — | 1.47 | 0.167 (n=253) | REJECTED | below_safety_margin(6116987069775<8327346213300), p_lower_below_threshold(0.17<0.75) |
| 53269142 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 291.891738 USDC | 0.018930 USDC | 0.000000 USDC | 0.005848 USDC | 0.013082 USDC (0.0120 €) | — | 0.45 | 0.002 (n=5) | REJECTED | below_safety_margin(13082<58378), reliability_not_demonstrated |
| 53269142 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.133548 WETH | 0.000009 WETH | 0.000000 WETH | 0.000003 WETH | 0.000006 WETH (0.0120 €) | — | 0.44 | 0.002 (n=5) | REJECTED | below_safety_margin(5921906249026<26709697216603), reliability_not_demonstrated |
| 53269032 | USDC→[aerodrome_slipstream]→EURC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 83.761310 USDC | 0.018482 USDC | 0.000000 USDC | 0.007838 USDC | 0.010644 USDC (0.0098 €) | — | 1.27 | 0.135 (n=540) | REJECTED | below_safety_margin(10644<16752), p_lower_below_threshold(0.13<0.75) |
| 53269032 | USDC→[aerodrome_slipstream]→EURC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 83.761310 USDC | 0.018482 USDC | 0.000000 USDC | 0.007838 USDC | 0.010644 USDC (0.0098 €) | — | 1.27 | 0.135 (n=540) | REJECTED | below_safety_margin(10644<16752), p_lower_below_threshold(0.13<0.75) |
| 53269032 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→EURC→[aerodrome_slipstream]→cbBTC | 0.000913 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0092 €) | — | 1.42 | 0.135 (n=540) | REJECTED | below_safety_margin(13<18), p_lower_below_threshold(0.13<0.75) |
| 53269032 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→EURC→[aerodrome_slipstream]→cbBTC | 0.000913 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0092 €) | — | 1.42 | 0.135 (n=540) | REJECTED | below_safety_margin(13<18), p_lower_below_threshold(0.13<0.75) |
| 53269032 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→EURC→[aerodrome_slipstream]→cbBTC | 0.000773 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0057 €) | — | 1.04 | 0.135 (n=540) | REJECTED | below_safety_margin(8<15), p_lower_below_threshold(0.13<0.75) |
| 53269032 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→EURC→[aerodrome_slipstream]→cbBTC | 0.000773 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0057 €) | — | 1.04 | 0.135 (n=540) | REJECTED | below_safety_margin(8<15), p_lower_below_threshold(0.13<0.75) |
| 53269032 | USDC→[aerodrome_slipstream]→EURC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 61.523629 USDC | 0.013341 USDC | 0.000000 USDC | 0.007503 USDC | 0.005838 USDC (0.0054 €) | — | 0.95 | 0.135 (n=540) | REJECTED | below_safety_margin(5838<12304), p_lower_below_threshold(0.13<0.75) |
| 53269032 | USDC→[aerodrome_slipstream]→EURC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 61.523629 USDC | 0.013341 USDC | 0.000000 USDC | 0.007503 USDC | 0.005838 USDC (0.0054 €) | — | 0.95 | 0.135 (n=540) | REJECTED | below_safety_margin(5838<12304), p_lower_below_threshold(0.13<0.75) |
| 53269130 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 220.126484 USDC | 0.009819 USDC | 0.000000 USDC | 0.005828 USDC | 0.003991 USDC (0.0037 €) | — | 0.18 | 0.033 (n=132) | REJECTED | below_safety_margin(3991<44025), p_lower_below_threshold(0.03<0.75) |
| 53269130 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 220.126484 USDC | 0.009819 USDC | 0.000000 USDC | 0.005828 USDC | 0.003991 USDC (0.0037 €) | — | 0.18 | 0.033 (n=132) | REJECTED | below_safety_margin(3991<44025), p_lower_below_threshold(0.03<0.75) |
| 53269130 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.100781 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0037 €) | — | 0.18 | 0.033 (n=132) | REJECTED | below_safety_margin(1802829979225<20156171369815), p_lower_below_threshold(0.03<0.75) |
| 53269130 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.100781 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0037 €) | — | 0.18 | 0.033 (n=132) | REJECTED | below_safety_margin(1802829979225<20156171369815), p_lower_below_threshold(0.03<0.75) |
| 53268997 | USDC→[aerodrome_slipstream]→EURC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 43.770577 USDC | 0.010865 USDC | 0.000000 USDC | 0.007966 USDC | 0.002899 USDC (0.0027 €) | — | 0.66 | 0.135 (n=540) | REJECTED | below_safety_margin(2899<8754), p_lower_below_threshold(0.13<0.75) |
| 53268997 | USDC→[aerodrome_slipstream]→EURC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 43.770577 USDC | 0.010865 USDC | 0.000000 USDC | 0.007966 USDC | 0.002899 USDC (0.0027 €) | — | 0.66 | 0.135 (n=540) | REJECTED | below_safety_margin(2899<8754), p_lower_below_threshold(0.13<0.75) |
| 53268997 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→EURC→[pancakeswap_v3]→WETH | 0.019787 WETH | 0.000005 WETH | 0.000000 WETH | 0.000004 WETH | 0.000001 WETH (0.0026 €) | — | 0.66 | 0.135 (n=540) | REJECTED | below_safety_margin(1299161674010<3957493260483), p_lower_below_threshold(0.13<0.75) |
| 53268997 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→EURC→[pancakeswap_v3]→WETH | 0.019787 WETH | 0.000005 WETH | 0.000000 WETH | 0.000004 WETH | 0.000001 WETH (0.0026 €) | — | 0.66 | 0.135 (n=540) | REJECTED | below_safety_margin(1299161674010<3957493260483), p_lower_below_threshold(0.13<0.75) |
| 53269032 | USDC→[pancakeswap_v3]→EURC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 44.437441 USDC | 0.009927 USDC | 0.000000 USDC | 0.007503 USDC | 0.002424 USDC (0.0022 €) | — | 0.55 | 0.135 (n=540) | REJECTED | below_safety_margin(2424<8887), p_lower_below_threshold(0.13<0.75) |
| 53269032 | USDC→[pancakeswap_v3]→EURC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 44.437441 USDC | 0.009927 USDC | 0.000000 USDC | 0.007503 USDC | 0.002424 USDC (0.0022 €) | — | 0.55 | 0.135 (n=540) | REJECTED | below_safety_margin(2424<8887), p_lower_below_threshold(0.13<0.75) |
| 53268993 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.107853 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0022 €) | — | 0.10 | 0.001 (n=14) | REJECTED | below_safety_margin(1067724699380<21570523759257), reliability_not_demonstrated |

## Fiabilité et décision
- Observations ghost : 3476 ; taux observé 0.114 ; borne inférieure crédible (0.9) 0.107 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 10.7% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
