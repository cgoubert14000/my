# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-26T14:37:39+00:00 ; durée 24.53 min ; blocs 53117317 → 53118055 (736 vus)

## Connexion
- Requêtes RPC : 8983 ; erreurs : 55 ; latence p50/p95 : 72.7/883.3 ms
- Rafraîchissements d'état : 737 ; âge des données au dernier bloc : 2.09 s ; changements de frais LP observés (pools à frais dynamiques) : 2334
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 3638 ; cycles déclenchés par événement : 222 ; avance médiane sur le rafraîchissement multicall : 384 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,312.68 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 529 pools, 304 jetons, 19426 routes
- Par DEX : uniswap_v3 143, aerodrome 213, aerodrome_slipstream 128, pancakeswap_v3 29, uniswap_v2 13, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 189 (rejetés 2) → 594 jetons ; pools candidats 3787 (énumérés 341, par paires 0), mesurés 532, sous le plancher de 10000.0 $ : 3 → gardés 529 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2307.602823, 'cbBTC': 79842.460004, 'AERO': 0.67568}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 157,614,039 | 2,312.676534 | 53118055 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,687,698 | 0.028981 | 53118055 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,136,351 | 0.028964 | 53118055 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,459,254 | 0.000013 | 53118055 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome | WETH/VVV | 3000 | 8,800,728 | 93.531886 | 53118055 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/USDC | 500 | 8,300,475 | 2,312.630387 | 53118055 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | USDC/AERO | 3000 | 7,189,949 | 1.468497 | 53118055 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,985,789 | 0.001659 | 53118055 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | WETH/USDC | 773 | 5,341,265 | 2,313.123807 | 53118055 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,339,986 | 0.028983 | 53118055 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,450,355 | 2,313.585741 | 53118055 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,199,727 | 0.999582 | 53118055 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,789,475 | 34,862.475723 | 53118055 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/USDC | 3000 | 3,359,195 | 2,312.575658 | 53118055 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 3,192,311 | 0.028949 | 53118055 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2709 | 2,488,812 | 93.560164 | 53118055 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | USDC/cbBTC | 532 | 2,470,266 | 0.000013 | 53118055 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,198,433 | 405.054012 | 53118055 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | WETH/FAI | 10000 | 2,116,726 | 1,210,234.968788 | 53118055 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,884,616 | 0.000013 | 53118055 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,882,008 | 0.000000 | 53118055 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,817,003 | 0.018461 | 53118055 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,710,159 | 0.000013 | 53118055 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | USDC/cbBTC | 356 | 1,694,439 | 0.000013 | 53118055 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | VIRTUAL/WETH | 10000 | 1,549,330 | 0.000265 | 53118055 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,512,863 | 0.005911 | 53118055 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,457,958 | 0.826447 | 53118055 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,453,150 | 1.698035 | 53118055 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | WETH/AERO | 3000 | 1,415,686 | 3,388.510008 | 53118055 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,364,856 | 13,986.901184 | 53118055 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,228,791 | 0.000267 | 53118055 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | WETH/AERO | 10000 | 1,225,109 | 3,402.035433 | 53118055 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | USDC/SEND | 3000 | 1,221,560 | 65.119739 | 53118055 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,208,084 | 2,312.742086 | 53118055 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | DRB/WETH | 10000 | 1,165,444 | 0.000000 | 53118055 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | WETH/WELL | 10000 | 1,133,458 | 1,092,273.723491 | 53118055 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/doginme | 10000 | 1,128,787 | 37,579,806.280132 | 53118055 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,102,788 | 499,327.370307 | 53118055 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,067,272 | 20,021,839.684538 | 53118055 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome | WETH/EDEL | 7000 | 1,063,656 | 72,445.739323 | 53118055 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | USDC/NOCK | 3000 | 1,053,856 | 56.397125 | 53118055 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,027,753 | 17.545567 | 53118055 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | USDC/VVV | 3000 | 969,506 | 0.040498 | 53118055 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/USDC | 10000 | 921,366 | 2,311.179744 | 53118055 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome | WETH/msETH (stable) | 500 | 904,180 | 2.308515 | 53118055 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | uXRP/WETH | 3000 | 891,247 | 0.000557 | 53118055 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| uniswap_v3 | WETH/MORPHO | 3000 | 878,728 | 1,140.042422 | 53118055 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 878,701 | 17.033008 | 53118055 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 878,288 | 17.995260 | 53118055 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v3 | WETH/VVV | 10000 | 865,396 | 93.744590 | 53118055 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v2 | WETH/USDC | 3000 | 843,488 | 2,313.079528 | 53118055 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 801,326 | 0.000009 | 53118055 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| pancakeswap_v3 | QUID/USDC | 100 | 799,023 | 0.057262 | 53118055 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 783,032 | 0.803142 | 53118055 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 742,493 | 0.616303 | 53118055 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 729,436 | 4,745,404.319337 | 53118055 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v2 | WETH/NPC | 3000 | 699,125 | 137,733.821490 | 53118055 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| uniswap_v3 | TIG/USDC | 10000 | 697,844 | 0.612711 | 53118055 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 688,996 | 495,622.680197 | 53118055 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 676,766 | 0.109573 | 53118055 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |

## Recherche d'opportunités
- Cycles : 958 ; routes examinées : 18610108 ; candidats optimisés : 55741 ; net attendu > 0 : 174 ; dernier cycle 186.0 ms
- Rejets (moteur) : {'spread_below_threshold': 18283368, 'liquidity_below_min': 251099, 'negative_expected_net': 55567, 'unquotable': 18942, 'borrow_bound_too_small': 958}
- Enregistrements de la session : 55741 ; net attendu > 0 : 174 ; simulés (eth_call de la vraie tx) : 8 (ok 3, échec 5) ; étiquettes ghost N+1 : 0/8 positives
- Décisions : {'REJECTED': 55741} ; motifs de rejet : {'below_safety_margin': 148, 'negative_expected_net': 55567, 'p_lower_below_threshold': 151, 'price_impact': 4, 'reliability_not_demonstrated': 23, 'simulation_failed': 5}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53117984 | USDC→[pancakeswap_v3]→PLAY→[aerodrome_slipstream]→USDC | 86.226081 USDC | 0.161516 USDC | 0.000000 USDC | 0.005222 USDC | 0.156294 USDC (0.1438 €) | — | 18.13 | 0.000 (n=52) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 53117512 | USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 166.418370 USDC | 0.044255 USDC | 0.000000 USDC | 0.001203 USDC | 0.043052 USDC (0.0396 €) | — | 2.59 | 0.138 (n=346) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 53117512 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH | 0.071718 WETH | 0.000019 WETH | 0.000000 WETH | 0.000001 WETH | 0.000019 WETH (0.0395 €) | 0.000019 WETH | 2.59 | 0.138 (n=346) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 53117512 | USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 493.169353 USDC | 0.029918 USDC | 0.000000 USDC | 0.001203 USDC | 0.028715 USDC (0.0264 €) | — | 0.58 | 0.138 (n=346) | REJECTED | below_safety_margin(28715<98633), p_lower_below_threshold(0.14<0.75) |
| 53117512 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH | 0.214196 WETH | 0.000013 WETH | 0.000000 WETH | 0.000001 WETH | 0.000012 WETH (0.0261 €) | — | 0.57 | 0.138 (n=346) | REJECTED | below_safety_margin(12232716902053<42839285508129), p_lower_below_threshold(0.14<0.75) |
| 53117512 | cbBTC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.005431 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0257 €) | — | 0.64 | 0.138 (n=346) | REJECTED | below_safety_margin(35<108), p_lower_below_threshold(0.14<0.75) |
| 53117512 | USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 101.471583 USDC | 0.020275 USDC | 0.000000 USDC | 0.001203 USDC | 0.019072 USDC (0.0175 €) | — | 1.88 | 0.182 (n=178) | REJECTED | below_safety_margin(19072<20294), p_lower_below_threshold(0.18<0.75) |
| 53117512 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH | 0.043976 WETH | 0.000009 WETH | 0.000000 WETH | 0.000001 WETH | 0.000008 WETH (0.0175 €) | — | 1.87 | 0.182 (n=178) | REJECTED | below_safety_margin(8216505034538<8795280748470), p_lower_below_threshold(0.18<0.75) |
| 53117541 | USDC→[aerodrome_slipstream]→USDT→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 127.494300 USDC | 0.022226 USDC | 0.000000 USDC | 0.007010 USDC | 0.015216 USDC (0.0140 €) | — | 1.19 | 0.182 (n=178) | REJECTED | below_safety_margin(15216<25498), p_lower_below_threshold(0.18<0.75) |
| 53117541 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→USDT→[uniswap_v3]→WETH | 0.054928 WETH | 0.000010 WETH | 0.000000 WETH | 0.000003 WETH | 0.000007 WETH (0.0139 €) | — | 1.19 | 0.182 (n=178) | REJECTED | below_safety_margin(6541833503514<10985597991880), p_lower_below_threshold(0.18<0.75) |
| 53118004 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 107.967161 USDC | 0.022442 USDC | 0.000000 USDC | 0.007339 USDC | 0.015103 USDC (0.0139 €) | — | 1.40 | 0.137 (n=347) | REJECTED | below_safety_margin(15103<21593), p_lower_below_threshold(0.14<0.75) |
| 53118004 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 107.967161 USDC | 0.022442 USDC | 0.000000 USDC | 0.007339 USDC | 0.015103 USDC (0.0139 €) | — | 1.40 | 0.137 (n=347) | REJECTED | below_safety_margin(15103<21593), p_lower_below_threshold(0.14<0.75) |
| 53118004 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH | 0.052624 WETH | 0.000009 WETH | 0.000000 WETH | 0.000003 WETH | 0.000006 WETH (0.0137 €) | — | 1.22 | 0.137 (n=347) | REJECTED | below_safety_margin(6446471621024<10524858044570), p_lower_below_threshold(0.14<0.75) |
| 53118004 | USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 122.076373 USDC | 0.021882 USDC | 0.000000 USDC | 0.006988 USDC | 0.014894 USDC (0.0137 €) | — | 1.22 | 0.137 (n=347) | REJECTED | below_safety_margin(14894<24415), p_lower_below_threshold(0.14<0.75) |
| 53118004 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.139570 WETH | 0.000009 WETH | 0.000000 WETH | 0.000002 WETH | 0.000006 WETH (0.0137 €) | — | 0.46 | 0.003 (n=2) | REJECTED | below_safety_margin(6426603932993<27914093876307), reliability_not_demonstrated |
| 53118004 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 323.751650 USDC | 0.020073 USDC | 0.000000 USDC | 0.005224 USDC | 0.014849 USDC (0.0137 €) | — | 0.46 | 0.003 (n=2) | REJECTED | below_safety_margin(14849<64750), reliability_not_demonstrated |
| 53118004 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH | 0.052568 WETH | 0.000009 WETH | 0.000000 WETH | 0.000003 WETH | 0.000006 WETH (0.0136 €) | — | 1.22 | 0.137 (n=347) | REJECTED | below_safety_margin(6411674538183<10513611014944), p_lower_below_threshold(0.14<0.75) |
| 53118004 | USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 121.643502 USDC | 0.021800 USDC | 0.000000 USDC | 0.006988 USDC | 0.014812 USDC (0.0136 €) | — | 1.22 | 0.137 (n=347) | REJECTED | below_safety_margin(14812<24328), p_lower_below_threshold(0.14<0.75) |
| 53118004 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→WETH | 0.049961 WETH | 0.000009 WETH | 0.000000 WETH | 0.000003 WETH | 0.000006 WETH (0.0134 €) | — | 1.26 | 0.137 (n=347) | REJECTED | below_safety_margin(6288716736802<9992131000702), p_lower_below_threshold(0.14<0.75) |
| 53118004 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→WETH | 0.049961 WETH | 0.000009 WETH | 0.000000 WETH | 0.000003 WETH | 0.000006 WETH (0.0134 €) | — | 1.26 | 0.137 (n=347) | REJECTED | below_safety_margin(6288716736802<9992131000702), p_lower_below_threshold(0.14<0.75) |
| 53118004 | cbBTC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.001113 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0132 €) | — | 1.62 | 0.137 (n=347) | REJECTED | below_safety_margin(18<22), p_lower_below_threshold(0.14<0.75) |
| 53118004 | cbBTC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.001113 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0132 €) | — | 1.62 | 0.137 (n=347) | REJECTED | below_safety_margin(18<22), p_lower_below_threshold(0.14<0.75) |
| 53118004 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.051551 WETH | 0.000008 WETH | 0.000000 WETH | 0.000003 WETH | 0.000005 WETH (0.0113 €) | — | 1.03 | 0.001 (n=7) | REJECTED | below_safety_margin(5328141256644<10310138453409), reliability_not_demonstrated |
| 53118004 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.051551 WETH | 0.000008 WETH | 0.000000 WETH | 0.000003 WETH | 0.000005 WETH (0.0113 €) | — | 1.03 | 0.001 (n=7) | REJECTED | below_safety_margin(5328141256644<10310138453409), reliability_not_demonstrated |
| 53118004 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 133.993945 USDC | 0.019062 USDC | 0.000000 USDC | 0.006988 USDC | 0.012074 USDC (0.0111 €) | — | 0.90 | 0.001 (n=7) | REJECTED | below_safety_margin(12074<26798), reliability_not_demonstrated |

## Fiabilité et décision
- Observations ghost : 2632 ; taux observé 0.095 ; borne inférieure crédible (0.9) 0.088 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 8.8% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
