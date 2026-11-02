# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-02T03:35:44+00:00 ; durée 6.06 min ; blocs 53400413 → 53400598 (180 vus)

## Connexion
- Requêtes RPC : 2155 ; erreurs : 0 ; latence p50/p95 : 245.3/1,571.9 ms
- Rafraîchissements d'état : 181 ; âge des données au dernier bloc : 1.62 s ; changements de frais LP observés (pools à frais dynamiques) : 293
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 1996 ; cycles déclenchés par événement : 256 ; avance médiane sur le rafraîchissement multicall : 686 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,306.74 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 500 pools, 289 jetons, 18354 routes
- Par DEX : uniswap_v3 139, aerodrome_slipstream 112, aerodrome 204, pancakeswap_v3 30, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 177 (rejetés 2) → 582 jetons ; pools candidats 3760 (énumérés 314, par paires 0), mesurés 503, sous le plancher de 10000.0 $ : 3 → gardés 500 (max 1500) ; prix des hubs : {'USDC': 1.0, 'USDbC': 1.0, 'DAI': 1.0, 'WETH': 2306.725487, 'cbBTC': 78582.728029, 'AERO': 0.633283}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 152,153,721 | 2,306.743021 | 53400598 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,438,109 | 0.029375 | 53400598 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,372,645 | 0.000013 | 53400598 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,284,215 | 0.029318 | 53400598 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 8,003,786 | 2,307.520131 | 53400598 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,916,386 | 100.187508 | 53400598 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,731,016 | 0.001591 | 53400598 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 5,546,111 | 1.579074 | 53400598 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,242,203 | 0.029367 | 53400598 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,130,831 | 0.999946 | 53400598 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome_slipstream | WETH/USDC | 150 | 4,112,677 | 2,307.662198 | 53400598 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,016,097 | 2,307.946100 | 53400598 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | WETH/KTA | 3000 | 3,603,297 | 38,355.300877 | 53400598 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,739,173 | 0.029337 | 53400598 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2760 | 2,408,125 | 100.174733 | 53400598 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | USDC/cbBTC | 400 | 2,143,642 | 0.000013 | 53400598 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome | WETH/FAI | 10000 | 2,131,128 | 1,187,813.955255 | 53400598 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | XDP/USDC | 100 | 1,753,996 | 0.018061 | 53400598 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,708,747 | 0.000000 | 53400598 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,637,748 | 0.000013 | 53400598 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,593,551 | 0.000013 | 53400598 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,576,787 | 433.079333 | 53400598 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v2 | WETH/USDC | 3000 | 1,514,516 | 2,307.385775 | 53400598 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,484,903 | 1.552316 | 53400598 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,457,505 | 0.825116 | 53400598 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,436,026 | 3,643.381477 | 53400598 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | WETH/USDC | 3000 | 1,393,756 | 2,308.958110 | 53400598 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,366,865 | 0.005242 | 53400598 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,357,843 | 2,307.604560 | 53400598 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,316,735 | 14,754.866779 | 53400598 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome_slipstream | USDC/cbBTC | 330 | 1,311,060 | 0.000013 | 53400598 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/SEND | 3000 | 1,169,037 | 71.102315 | 53400598 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,129,455 | 37,007,869.252341 | 53400598 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,083,690 | 522,794.918703 | 53400598 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,070,878 | 0.000000 | 53400598 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,030,227 | 22,429,756.239120 | 53400598 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | WETH/VVV | 10000 | 1,005,302 | 99.698575 | 53400598 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome | WETH/EDEL | 7000 | 999,533 | 81,303.297808 | 53400598 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome_slipstream | USDC/VELVET | 100 | 990,257 | 19.492048 | 53400598 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | WETH/WELL | 10000 | 963,293 | 1,196,228.406551 | 53400598 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/MORPHO | 3000 | 942,666 | 1,027.976890 | 53400598 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/USDC | 10000 | 929,383 | 2,291.133952 | 53400598 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | USDC/VVV | 3000 | 921,655 | 0.043416 | 53400598 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | USDC/NOCK | 3000 | 899,266 | 77.414057 | 53400598 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | uXRP/WETH | 3000 | 877,817 | 0.000542 | 53400598 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome | WETH/AERO | 10000 | 873,143 | 3,618.241405 | 53400598 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 834,641 | 19.562952 | 53400598 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 814,306 | 0.059580 | 53400598 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 781,637 | 0.801881 | 53400598 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| aerodrome | VIRTUAL/WETH | 10000 | 740,305 | 0.000260 | 53400598 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 735,769 | 0.595218 | 53400598 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 725,494 | 4,778,142.918136 | 53400598 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v2 | WETH/NPC | 3000 | 702,987 | 135,879.071362 | 53400598 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 690,983 | 0.000008 | 53400598 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v3 | TIG/USDC | 10000 | 675,582 | 0.572678 | 53400598 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome | WETH/msETH (stable) | 500 | 671,391 | 2.342047 | 53400598 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | WETH/BRETT | 2102 | 670,542 | 524,952.312416 | 53400598 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome | WETH/bsdETH | 100 | 619,634 | 0.914674 | 53400598 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 608,569 | 0.092097 | 53400598 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| uniswap_v3 | FLOCK/USDC | 3000 | 565,725 | 0.038762 | 53400598 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |

## Recherche d'opportunités
- Cycles : 436 ; routes examinées : 8002344 ; candidats optimisés : 35495 ; net attendu > 0 : 17 ; dernier cycle 202.4 ms
- Rejets (moteur) : {'spread_below_threshold': 7832738, 'liquidity_below_min': 132683, 'negative_expected_net': 35478, 'unquotable': 992, 'borrow_bound_too_small': 436}
- Enregistrements de la session : 35495 ; net attendu > 0 : 17 ; simulés (eth_call de la vraie tx) : 0 (ok 0, échec 0) ; étiquettes ghost N+1 : 0/0 positives
- Décisions : {'REJECTED': 35495} ; motifs de rejet : {'below_safety_margin': 17, 'negative_expected_net': 35478, 'p_lower_below_threshold': 17}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53400449 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 806.985823 USDC | 0.050960 USDC | 0.000000 USDC | 0.005180 USDC | 0.045780 USDC (0.0421 €) | — | 0.57 | 0.041 (n=164) | REJECTED | below_safety_margin(45780<161397), p_lower_below_threshold(0.04<0.75) |
| 53400449 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.351275 WETH | 0.000022 WETH | 0.000000 WETH | 0.000002 WETH | 0.000020 WETH (0.0421 €) | — | 0.56 | 0.041 (n=164) | REJECTED | below_safety_margin(19839561118973<70254961923957), p_lower_below_threshold(0.04<0.75) |
| 53400555 | WETH→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.036757 WETH | 0.000005 WETH | 0.000000 WETH | 0.000002 WETH | 0.000002 WETH (0.0052 €) | — | 0.67 | 0.041 (n=164) | REJECTED | below_safety_margin(2471652950405<7351499430852), p_lower_below_threshold(0.04<0.75) |
| 53400556 | WETH→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.036757 WETH | 0.000005 WETH | 0.000000 WETH | 0.000002 WETH | 0.000002 WETH (0.0052 €) | — | 0.67 | 0.041 (n=164) | REJECTED | below_safety_margin(2471652950405<7351499430852), p_lower_below_threshold(0.04<0.75) |
| 53400555 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→cbBTC | 0.001343 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0051 €) | — | 0.52 | 0.041 (n=164) | REJECTED | below_safety_margin(7<26), p_lower_below_threshold(0.04<0.75) |
| 53400556 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→cbBTC | 0.001343 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0051 €) | — | 0.52 | 0.041 (n=164) | REJECTED | below_safety_margin(7<26), p_lower_below_threshold(0.04<0.75) |
| 53400555 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→cbBTC | 0.000800 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0007 €) | — | 0.12 | 0.136 (n=722) | REJECTED | below_safety_margin(1<16), p_lower_below_threshold(0.14<0.75) |
| 53400555 | cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→cbBTC | 0.000800 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0007 €) | — | 0.12 | 0.136 (n=722) | REJECTED | below_safety_margin(1<16), p_lower_below_threshold(0.14<0.75) |
| 53400556 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→cbBTC | 0.000800 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0007 €) | — | 0.12 | 0.136 (n=722) | REJECTED | below_safety_margin(1<16), p_lower_below_threshold(0.14<0.75) |
| 53400556 | cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→cbBTC | 0.000800 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0007 €) | — | 0.12 | 0.136 (n=722) | REJECTED | below_safety_margin(1<16), p_lower_below_threshold(0.14<0.75) |
| 53400449 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 135.016686 USDC | 0.005838 USDC | 0.000000 USDC | 0.005180 USDC | 0.000658 USDC (0.0006 €) | — | 0.05 | 0.006 (n=49) | REJECTED | below_safety_margin(658<27003), p_lower_below_threshold(0.01<0.75) |
| 53400449 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.058549 WETH | 0.000003 WETH | 0.000000 WETH | 0.000002 WETH | 0.000000 WETH (0.0006 €) | — | 0.05 | 0.006 (n=49) | REJECTED | below_safety_margin(284221267278<11709889735292), p_lower_below_threshold(0.01<0.75) |
| 53400555 | WETH→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.023300 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0005 €) | — | 0.10 | 0.136 (n=722) | REJECTED | below_safety_margin(225785815772<4660044031388), p_lower_below_threshold(0.14<0.75) |
| 53400556 | WETH→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.023300 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0005 €) | — | 0.10 | 0.136 (n=722) | REJECTED | below_safety_margin(225785815772<4660044031388), p_lower_below_threshold(0.14<0.75) |
| 53400555 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 53.550752 USDC | 0.007428 USDC | 0.000000 USDC | 0.006933 USDC | 0.000495 USDC (0.0005 €) | — | 0.09 | 0.136 (n=722) | REJECTED | below_safety_margin(495<10710), p_lower_below_threshold(0.14<0.75) |
| 53400556 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 53.550752 USDC | 0.007428 USDC | 0.000000 USDC | 0.006933 USDC | 0.000495 USDC (0.0005 €) | — | 0.09 | 0.136 (n=722) | REJECTED | below_safety_margin(495<10710), p_lower_below_threshold(0.14<0.75) |
| 53400462 | WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→WETH | 0.009545 WETH | 0.000002 WETH | 0.000000 WETH | 0.000002 WETH | 0.000000 WETH (0.0000 €) | — | 0.00 | 0.006 (n=49) | REJECTED | below_safety_margin(1109813716<1909063001394), p_lower_below_threshold(0.01<0.75) |

## Fiabilité et décision
- Observations ghost : 4287 ; taux observé 0.133 ; borne inférieure crédible (0.9) 0.126 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 12.6% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
