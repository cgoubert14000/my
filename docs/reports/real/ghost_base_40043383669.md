# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-24T02:59:20+00:00 ; durée 166.8 min ; blocs 53005699 → 53010704 (4997 vus)

## Connexion
- Requêtes RPC : 61102 ; erreurs : 0 ; latence p50/p95 : 198.6/779.3 ms
- Rafraîchissements d'état : 4998 ; âge des données au dernier bloc : 1.34 s ; changements de frais LP observés (pools à frais dynamiques) : 7381
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 31164 ; cycles déclenchés par événement : 3123 ; avance médiane sur le rafraîchissement multicall : 374 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,375.32 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 542 pools, 313 jetons, 19386 routes
- Par DEX : uniswap_v3 139, aerodrome 218, aerodrome_slipstream 136, pancakeswap_v3 32, uniswap_v2 13, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 197 (rejetés 2) → 602 jetons ; pools candidats 3863 (énumérés 353, par paires 0), mesurés 544, sous le plancher de 10000.0 $ : 2 → gardés 542 (max 1500) ; prix des hubs : {'USDC': 1.0, 'USDbC': 1.0, 'DAI': 1.0, 'WETH': 2378.764515, 'AERO': 0.72806, 'cbBTC': 80962.575526}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 156,352,945 | 2,375.317660 | 53010704 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,415,916 | 0.029439 | 53010704 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 12,373,862 | 96.709904 | 53010704 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,169,901 | 0.029379 | 53010704 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| aerodrome | USDC/AERO | 3000 | 9,865,246 | 1.367640 | 53010704 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,550,947 | 0.000012 | 53010704 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 8,712,799 | 0.029393 | 53010704 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/USDC | 500 | 8,626,786 | 2,380.618845 | 53010704 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,058,700 | 0.001657 | 53010704 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 330 | 6,308,124 | 0.000012 | 53010704 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 150 | 5,517,538 | 2,381.468495 | 53010704 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,420,196 | 0.029447 | 53010704 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | USDC/cbBTC | 412 | 4,870,805 | 0.000012 | 53010704 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,544,731 | 2,381.618525 | 53010704 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,246,896 | 0.999323 | 53010704 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/USDC | 3000 | 4,141,144 | 2,377.628853 | 53010704 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome | WETH/KTA | 3000 | 3,956,854 | 34,141.363050 | 53010704 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | VIRTUAL/WETH | 10000 | 3,334,966 | 0.000271 | 53010704 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/USDT | 400 | 2,786,468 | 2,384.853205 | 53010704 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome_slipstream | WETH/VVV | 2703 | 2,506,656 | 96.750787 | 53010704 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,265,929 | 404.033199 | 53010704 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | WETH/FAI | 10000 | 2,134,200 | 1,255,863.425253 | 53010704 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome | WETH/AERO | 10000 | 2,008,610 | 3,279.949236 | 53010704 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,929,131 | 0.000000 | 53010704 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,912,071 | 0.000012 | 53010704 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v3 | XDP/USDC | 100 | 1,743,336 | 0.017753 | 53010704 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,736,328 | 0.000012 | 53010704 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,551,022 | 1.610679 | 53010704 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | WETH/AERO | 3000 | 1,491,941 | 3,255.523581 | 53010704 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,460,071 | 0.824580 | 53010704 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,389,212 | 13,735.309242 | 53010704 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,379,645 | 0.005101 | 53010704 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,299,314 | 2,380.636680 | 53010704 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,276,559 | 0.000271 | 53010704 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | WETH/msETH (stable) | 500 | 1,243,756 | 2.308243 | 53010704 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome | USDC/SEND | 3000 | 1,225,403 | 64.711956 | 53010704 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | DRB/WETH | 10000 | 1,199,287 | 0.000000 | 53010704 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/doginme | 10000 | 1,181,902 | 35,516,134.488001 | 53010704 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | WETH/WELL | 10000 | 1,154,131 | 1,115,897.990754 | 53010704 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,139,354 | 491,277.872560 | 53010704 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | USDC/NOCK | 3000 | 1,134,518 | 48.662514 | 53010704 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,120,603 | 16.494763 | 53010704 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | WETH/EDEL | 7000 | 1,079,296 | 74,264.039398 | 53010704 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,054,207 | 21,315,212.131261 | 53010704 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | USDC/VVV | 3000 | 1,044,228 | 0.040630 | 53010704 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,038,120 | 17.068803 | 53010704 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 971,790 | 23.199085 | 53010704 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| uniswap_v3 | WETH/MORPHO | 3000 | 947,311 | 1,063.898455 | 53010704 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | uXRP/WETH | 3000 | 901,427 | 0.000540 | 53010704 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | USDC/SAPIEN | 4510 | 887,103 | 17.674609 | 53010704 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 879,385 | 0.070468 | 53010704 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 873,991 | 0.000009 | 53010704 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v2 | WETH/USDC | 3000 | 854,834 | 2,383.453466 | 53010704 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome | weETH_04c0/WETH | 500 | 817,514 | 1.105909 | 53010704 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome | WETH/wstETH | 3000 | 804,307 | 0.803010 | 53010704 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | WETH/USDC | 10000 | 790,603 | 2,373.719186 | 53010704 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/VVV | 10000 | 781,698 | 96.753443 | 53010704 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 767,120 | 0.643938 | 53010704 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 759,921 | 4,610,419.593907 | 53010704 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 733,074 | 0.673479 | 53010704 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |

## Recherche d'opportunités
- Cycles : 8120 ; routes examinées : 157414320 ; candidats optimisés : 670094 ; net attendu > 0 : 222 ; dernier cycle 308.0 ms
- Rejets (moteur) : {'spread_below_threshold': 154537670, 'liquidity_below_min': 2198016, 'negative_expected_net': 669872, 'borrow_bound_too_small': 8118, 'cycle_budget_exhausted': 344}
- Enregistrements de la session : 670094 ; net attendu > 0 : 222 ; simulés (eth_call de la vraie tx) : 9 (ok 4, échec 5) ; étiquettes ghost N+1 : 0/9 positives
- Décisions : {'REJECTED': 670094} ; motifs de rejet : {'below_safety_margin': 187, 'negative_expected_net': 669872, 'p_lower_below_threshold': 189, 'reliability_not_demonstrated': 33, 'simulation_failed': 5}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53006019 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 1.912070 WETH | 0.000570 WETH | 0.000000 WETH | 0.000003 WETH | 0.000567 WETH (1.2407 €) | — | 2.97 | 0.019 (n=74) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.02<0.75) |
| 53006019 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 4,540.158648 USDC | 1.352973 USDC | 0.000000 USDC | 0.006781 USDC | 1.346192 USDC (1.2385 €) | — | 2.97 | 0.019 (n=74) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 53006019 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 1.800439 WETH | 0.000512 WETH | 0.000000 WETH | 0.000003 WETH | 0.000509 WETH (1.1135 €) | — | 2.83 | 0.019 (n=74) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.02<0.75) |
| 53006019 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 4,272.411080 USDC | 1.214959 USDC | 0.000000 USDC | 0.006781 USDC | 1.208178 USDC (1.1115 €) | — | 2.83 | 0.019 (n=74) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 53006019 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH | 1.260197 WETH | 0.000371 WETH | 0.000000 WETH | 0.000003 WETH | 0.000367 WETH (0.8032 €) | — | 2.91 | 0.137 (n=255) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.14<0.75) |
| 53006019 | USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 2,986.961580 USDC | 0.879857 USDC | 0.000000 USDC | 0.008226 USDC | 0.871631 USDC (0.8019 €) | — | 2.92 | 0.137 (n=255) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 53006019 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→USDT→[aerodrome_slipstream]→WETH | 1.037899 WETH | 0.000267 WETH | 0.000000 WETH | 0.000003 WETH | 0.000263 WETH (0.5761 €) | — | 2.54 | 0.137 (n=255) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 53006019 | USDC→[uniswap_v3]→USDT→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 2,462.339431 USDC | 0.633103 USDC | 0.000000 USDC | 0.007865 USDC | 0.625238 USDC (0.5752 €) | — | 2.54 | 0.137 (n=255) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 53006019 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.935327 WETH | 0.000258 WETH | 0.000000 WETH | 0.000003 WETH | 0.000255 WETH (0.5574 €) | — | 2.72 | 0.001 (n=7) | REJECTED | reliability_not_demonstrated |
| 53006019 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.026414 cbBTC | 0.000008 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000007 cbBTC (0.5572 €) | — | 2.84 | 0.001 (n=7) | REJECTED | reliability_not_demonstrated |
| 53006019 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 2,213.233789 USDC | 0.613262 USDC | 0.000000 USDC | 0.008226 USDC | 0.605036 USDC (0.5566 €) | — | 2.73 | 0.001 (n=7) | REJECTED | reliability_not_demonstrated |
| 53006019 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→USDT→[aerodrome_slipstream]→WETH | 0.874512 WETH | 0.000237 WETH | 0.000000 WETH | 0.000003 WETH | 0.000233 WETH (0.5099 €) | — | 2.67 | 0.137 (n=255) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 53006019 | USDC→[pancakeswap_v3]→USDT→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 2,075.640666 USDC | 0.561606 USDC | 0.000000 USDC | 0.008226 USDC | 0.553380 USDC (0.5091 €) | — | 2.67 | 0.137 (n=255) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 53006019 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.757891 WETH | 0.000215 WETH | 0.000000 WETH | 0.000003 WETH | 0.000212 WETH (0.4638 €) | — | 2.80 | 0.003 (n=2) | REJECTED | reliability_not_demonstrated |
| 53006019 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 1,798.612704 USDC | 0.509400 USDC | 0.000000 USDC | 0.006059 USDC | 0.503341 USDC (0.4631 €) | — | 2.80 | 0.003 (n=2) | REJECTED | reliability_not_demonstrated |
| 53006019 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→cbBTC | 0.023217 cbBTC | 0.000004 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000004 cbBTC (0.2909 €) | — | 1.68 | 0.137 (n=255) | REJECTED | below_safety_margin(391<464), p_lower_below_threshold(0.14<0.75) |
| 53006019 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.803541 WETH | 0.000136 WETH | 0.000000 WETH | 0.000003 WETH | 0.000133 WETH (0.2909 €) | — | 1.65 | 0.137 (n=255) | REJECTED | below_safety_margin(132985850448231<160708108851091), p_lower_below_threshold(0.14<0.75) |
| 53006019 | USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 1,955.302447 USDC | 0.323673 USDC | 0.000000 USDC | 0.008226 USDC | 0.315447 USDC (0.2902 €) | — | 1.61 | 0.137 (n=255) | REJECTED | below_safety_margin(315447<391060), p_lower_below_threshold(0.14<0.75) |
| 53006019 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.324140 WETH | 0.000099 WETH | 0.000000 WETH | 0.000003 WETH | 0.000096 WETH (0.2107 €) | — | 2.97 | 0.019 (n=74) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 53006019 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 768.192735 USDC | 0.235485 USDC | 0.000000 USDC | 0.006781 USDC | 0.228704 USDC (0.2104 €) | — | 2.98 | 0.019 (n=74) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 53006019 | USDC→[uniswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 1,455.336440 USDC | 0.138569 USDC | 0.000000 USDC | 0.008226 USDC | 0.130343 USDC (0.1199 €) | — | 0.90 | 0.137 (n=255) | REJECTED | below_safety_margin(130343<291067), p_lower_below_threshold(0.14<0.75) |
| 53006019 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.640291 WETH | 0.000058 WETH | 0.000000 WETH | 0.000003 WETH | 0.000055 WETH (0.1196 €) | — | 0.85 | 0.137 (n=255) | REJECTED | below_safety_margin(54700643974662<128058186705793), p_lower_below_threshold(0.14<0.75) |
| 53006019 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→cbBTC | 0.018032 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1190 €) | — | 0.89 | 0.137 (n=255) | REJECTED | below_safety_margin(160<360), p_lower_below_threshold(0.14<0.75) |
| 53006019 | cbBTC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.002723 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0513 €) | — | 2.53 | 0.137 (n=255) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 53006019 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 223.151986 USDC | 0.063247 USDC | 0.000000 USDC | 0.007865 USDC | 0.055382 USDC (0.0510 €) | — | 2.48 | 0.137 (n=255) | REJECTED | p_lower_below_threshold(0.14<0.75) |

## Fiabilité et décision
- Observations ghost : 2093 ; taux observé 0.098 ; borne inférieure crédible (0.9) 0.090 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 9.0% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
