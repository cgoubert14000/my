# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-02T04:55:44+00:00 ; durée 86.05 min ; blocs 53400413 → 53402995 (2559 vus)

## Connexion
- Requêtes RPC : 30438 ; erreurs : 0 ; latence p50/p95 : 313.1/1,121.8 ms
- Rafraîchissements d'état : 2559 ; âge des données au dernier bloc : 3.65 s ; changements de frais LP observés (pools à frais dynamiques) : 2585
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 22428 ; cycles déclenchés par événement : 3403 ; avance médiane sur le rafraîchissement multicall : 517 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,296.54 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 500 pools, 289 jetons, 18354 routes
- Par DEX : uniswap_v3 139, aerodrome_slipstream 112, aerodrome 204, pancakeswap_v3 30, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 177 (rejetés 2) → 582 jetons ; pools candidats 3760 (énumérés 314, par paires 0), mesurés 503, sous le plancher de 10000.0 $ : 3 → gardés 500 (max 1500) ; prix des hubs : {'USDC': 1.0, 'USDbC': 1.0, 'DAI': 1.0, 'WETH': 2306.725487, 'cbBTC': 78582.728029, 'AERO': 0.633283}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 151,773,095 | 2,296.539849 | 53402995 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,392,979 | 0.029255 | 53402995 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,372,090 | 0.000013 | 53402995 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,259,763 | 0.029317 | 53402995 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 7,966,537 | 2,293.131663 | 53402996 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,902,966 | 99.640687 | 53402995 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,714,465 | 0.001584 | 53402995 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 5,519,064 | 1.589189 | 53402995 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,826,900 | 0.029260 | 53402995 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,129,416 | 0.999946 | 53402995 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome_slipstream | WETH/USDC | 150 | 4,097,709 | 2,293.259315 | 53402995 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,002,995 | 2,293.212263 | 53402995 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | WETH/KTA | 3000 | 3,593,145 | 38,231.872237 | 53402995 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2530 | 2,729,692 | 0.029302 | 53402995 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2700 | 2,404,836 | 99.679730 | 53402995 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | USDC/cbBTC | 424 | 2,142,685 | 0.000013 | 53402995 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome | WETH/FAI | 10000 | 2,124,791 | 1,184,362.980123 | 53402995 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | XDP/USDC | 100 | 1,755,377 | 0.018087 | 53402995 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,706,268 | 0.000000 | 53402995 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,637,228 | 0.000013 | 53402995 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,593,257 | 0.000013 | 53402995 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,571,082 | 431.910042 | 53402995 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v2 | WETH/USDC | 3000 | 1,511,169 | 2,296.781511 | 53402995 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,484,903 | 1.552316 | 53402995 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,457,505 | 0.825116 | 53402995 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,428,024 | 3,648.132239 | 53402995 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | WETH/USDC | 3000 | 1,389,894 | 2,297.505428 | 53402995 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,359,882 | 0.005238 | 53402995 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,353,792 | 2,292.512405 | 53402995 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,315,523 | 14,744.488931 | 53402995 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome_slipstream | USDC/cbBTC | 334 | 1,310,793 | 0.000013 | 53402995 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/SEND | 3000 | 1,169,037 | 71.102315 | 53402995 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,127,140 | 37,005,179.394270 | 53402995 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,078,577 | 523,227.747272 | 53402995 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,075,591 | 0.000000 | 53402995 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,023,739 | 22,502,007.197364 | 53402995 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | WETH/VVV | 10000 | 1,004,098 | 99.698590 | 53402995 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome | WETH/EDEL | 7000 | 995,113 | 81,303.099665 | 53402995 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome_slipstream | USDC/VELVET | 100 | 986,504 | 19.709123 | 53402995 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | WETH/WELL | 10000 | 959,028 | 1,196,238.672544 | 53402995 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/MORPHO | 3000 | 938,519 | 1,027.505410 | 53402995 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/USDC | 10000 | 927,928 | 2,291.133952 | 53402995 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | USDC/VVV | 3000 | 922,334 | 0.043369 | 53402995 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | USDC/NOCK | 3000 | 900,865 | 77.139566 | 53402995 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | uXRP/WETH | 3000 | 873,299 | 0.000541 | 53402995 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome | WETH/AERO | 10000 | 868,318 | 3,623.692885 | 53402995 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 834,657 | 19.562459 | 53402995 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 804,629 | 0.058085 | 53402995 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 778,180 | 0.801881 | 53402995 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| aerodrome | VIRTUAL/WETH | 10000 | 737,031 | 0.000260 | 53402995 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 733,244 | 0.594762 | 53402995 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 722,934 | 4,769,582.048593 | 53402995 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v2 | WETH/NPC | 3000 | 704,916 | 133,940.179296 | 53402995 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 688,296 | 0.000008 | 53402995 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v3 | TIG/USDC | 10000 | 672,207 | 0.572678 | 53402995 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome | WETH/msETH (stable) | 500 | 668,421 | 2.342047 | 53402995 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 667,308 | 526,196.319160 | 53402995 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome | WETH/bsdETH | 100 | 616,892 | 0.914678 | 53402995 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 606,145 | 0.091536 | 53402995 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| uniswap_v3 | FLOCK/USDC | 3000 | 560,065 | 0.038169 | 53402995 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |

## Recherche d'opportunités
- Cycles : 5961 ; routes examinées : 109408194 ; candidats optimisés : 406667 ; net attendu > 0 : 500 ; dernier cycle 278.2 ms
- Rejets (moteur) : {'spread_below_threshold': 107327220, 'liquidity_below_min': 1654991, 'negative_expected_net': 406167, 'unquotable': 12756, 'borrow_bound_too_small': 5961, 'cycle_budget_exhausted': 530}
- Enregistrements de la session : 406667 ; net attendu > 0 : 500 ; simulés (eth_call de la vraie tx) : 21 (ok 9, échec 12) ; étiquettes ghost N+1 : 6/17 positives
- Décisions : {'REJECTED': 406667} ; motifs de rejet : {'below_safety_margin': 342, 'negative_expected_net': 406167, 'p_lower_below_threshold': 428, 'reliability_not_demonstrated': 72, 'simulation_failed': 12, 'stale_data': 16}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53400900 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome]→EDGE→[uniswap_v3]→USDC | 398.983685 USDC | 5.500964 USDC | 0.000000 USDC | 0.006611 USDC | 5.494353 USDC (5.0548 €) | — | 137.71 | 0.002 (n=5) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53400900 | cbBTC→[aerodrome]→EDGE→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.005077 cbBTC | 0.000070 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000070 cbBTC (5.0544 €) | — | 137.71 | 0.002 (n=5) | REJECTED | reliability_not_demonstrated |
| 53400900 | USDC→[aerodrome_slipstream]→cbBTC→[aerodrome]→EDGE→[uniswap_v3]→USDC | 378.705614 USDC | 5.284768 USDC | 0.000000 USDC | 0.006611 USDC | 5.278157 USDC (4.8559 €) | — | 139.37 | 0.001 (n=15) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53400900 | cbBTC→[aerodrome]→EDGE→[uniswap_v3]→USDC→[aerodrome_slipstream]→cbBTC | 0.004814 cbBTC | 0.000067 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000067 cbBTC (4.8527 €) | — | 139.42 | 0.001 (n=15) | REJECTED | reliability_not_demonstrated |
| 53400900 | USDC→[aerodrome_slipstream]→cbBTC→[aerodrome]→EDGE→[uniswap_v3]→USDC | 371.280668 USDC | 5.225963 USDC | 0.000000 USDC | 0.006611 USDC | 5.219352 USDC (4.8018 €) | — | 140.58 | 0.001 (n=15) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53400900 | cbBTC→[aerodrome]→EDGE→[uniswap_v3]→USDC→[aerodrome_slipstream]→cbBTC | 0.004724 cbBTC | 0.000066 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000066 cbBTC (4.8013 €) | — | 140.59 | 0.001 (n=15) | REJECTED | reliability_not_demonstrated |
| 53400900 | USDC→[uniswap_v3]→cbBTC→[aerodrome]→EDGE→[uniswap_v3]→USDC | 367.992765 USDC | 5.113454 USDC | 0.000000 USDC | 0.006611 USDC | 5.106843 USDC (4.6983 €) | — | 138.78 | 0.001 (n=15) | REJECTED | reliability_not_demonstrated |
| 53400900 | cbBTC→[aerodrome]→EDGE→[uniswap_v3]→USDC→[uniswap_v3]→cbBTC | 0.004681 cbBTC | 0.000065 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000065 cbBTC (4.6972 €) | — | 138.79 | 0.001 (n=15) | REJECTED | reliability_not_demonstrated |
| 53400900 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome]→EDGE→[uniswap_v3]→USDC | 338.987786 USDC | 4.627907 USDC | 0.000000 USDC | 0.006611 USDC | 4.621296 USDC (4.2516 €) | — | 136.33 | 0.002 (n=5) | REJECTED | reliability_not_demonstrated |
| 53400900 | cbBTC→[aerodrome]→EDGE→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.004307 cbBTC | 0.000059 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000059 cbBTC (4.2446 €) | — | 136.33 | 0.002 (n=5) | REJECTED | reliability_not_demonstrated |
| 53400900 | USDC→[uniswap_v3]→cbBTC→[aerodrome]→EDGE→[uniswap_v3]→USDC | 162.817546 USDC | 2.508035 USDC | 0.000000 USDC | 0.006611 USDC | 2.501424 USDC (2.3013 €) | — | 153.63 | 0.001 (n=15) | REJECTED | reliability_not_demonstrated |
| 53400900 | cbBTC→[aerodrome]→EDGE→[uniswap_v3]→USDC→[uniswap_v3]→cbBTC | 0.002065 cbBTC | 0.000032 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000032 cbBTC (2.2947 €) | — | 153.70 | 0.001 (n=15) | REJECTED | reliability_not_demonstrated |
| 53400900 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome]→EDGE→[uniswap_v3]→USDC | 100.255246 USDC | 1.525307 USDC | 0.000000 USDC | 0.006611 USDC | 1.518696 USDC (1.3972 €) | — | 151.48 | 0.002 (n=5) | REJECTED | reliability_not_demonstrated |
| 53400900 | cbBTC→[aerodrome]→EDGE→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.001263 cbBTC | 0.000019 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000019 cbBTC (1.3831 €) | — | 151.52 | 0.002 (n=5) | REJECTED | reliability_not_demonstrated |
| 53400900 | USDC→[aerodrome]→cbBTC→[aerodrome]→EDGE→[uniswap_v3]→USDC | 84.792107 USDC | 1.320637 USDC | 0.000000 USDC | 0.006293 USDC | 1.314344 USDC (1.2092 €) | — | 155.01 | 0.001 (n=15) | REJECTED | reliability_not_demonstrated |
| 53400900 | cbBTC→[aerodrome]→EDGE→[uniswap_v3]→USDC→[aerodrome]→cbBTC | 0.001068 cbBTC | 0.000017 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000017 cbBTC (1.1973 €) | — | 155.03 | 0.001 (n=15) | REJECTED | reliability_not_demonstrated |
| 53401261 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.015260 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1554 €) | — | 1.41 | 0.000 (n=18) | REJECTED | below_safety_margin(215<305), reliability_not_demonstrated |
| 53401261 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 1,201.033340 USDC | 0.176218 USDC | 0.000000 USDC | 0.007280 USDC | 0.168938 USDC (0.1554 €) | — | 1.41 | 0.000 (n=18) | REJECTED | below_safety_margin(168938<240206), reliability_not_demonstrated |
| 53401261 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.520701 WETH | 0.000076 WETH | 0.000000 WETH | 0.000003 WETH | 0.000073 WETH (0.1554 €) | — | 1.41 | 0.000 (n=18) | REJECTED | below_safety_margin(73235850456892<104140175187580), reliability_not_demonstrated |
| 53402860 | WETH→[uniswap_v3]→cbBTC→[aerodrome_slipstream]→WETH | 0.151564 WETH | 0.000068 WETH | 0.000000 WETH | 0.000002 WETH | 0.000066 WETH (0.1396 €) | — | 4.35 | 0.058 (n=62) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.06<0.75) |
| 53402861 | WETH→[uniswap_v3]→cbBTC→[aerodrome_slipstream]→WETH | 0.151564 WETH | 0.000068 WETH | 0.000000 WETH | 0.000002 WETH | 0.000066 WETH (0.1396 €) | — | 4.35 | 0.058 (n=62) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.06<0.75) |
| 53402860 | cbBTC→[aerodrome_slipstream]→WETH→[uniswap_v3]→cbBTC | 0.004083 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1388 €) | — | 4.70 | 0.058 (n=62) | REJECTED | p_lower_below_threshold(0.06<0.75) |
| 53402861 | cbBTC→[aerodrome_slipstream]→WETH→[uniswap_v3]→cbBTC | 0.004083 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1388 €) | — | 4.70 | 0.058 (n=62) | REJECTED | p_lower_below_threshold(0.06<0.75) |
| 53402860 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→WETH | 0.120218 WETH | 0.000053 WETH | 0.000000 WETH | 0.000002 WETH | 0.000051 WETH (0.1071 €) | — | 4.21 | 0.026 (n=196) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.03<0.75) |
| 53402861 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→WETH | 0.120218 WETH | 0.000053 WETH | 0.000000 WETH | 0.000002 WETH | 0.000051 WETH (0.1071 €) | — | 4.21 | 0.026 (n=196) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.03<0.75) |

## Fiabilité et décision
- Observations ghost : 4304 ; taux observé 0.134 ; borne inférieure crédible (0.9) 0.127 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 12.7% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
