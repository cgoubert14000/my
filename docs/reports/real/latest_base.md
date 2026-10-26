# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-26T14:25:24+00:00 ; durée 12.28 min ; blocs 53117317 → 53117687 (369 vus)

## Connexion
- Requêtes RPC : 4568 ; erreurs : 5 ; latence p50/p95 : 91.5/1,101.2 ms
- Rafraîchissements d'état : 369 ; âge des données au dernier bloc : 3.16 s ; changements de frais LP observés (pools à frais dynamiques) : 1243
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 2717 ; cycles déclenchés par événement : 144 ; avance médiane sur le rafraîchissement multicall : 346 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,317.98 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 529 pools, 304 jetons, 19426 routes
- Par DEX : uniswap_v3 143, aerodrome 213, aerodrome_slipstream 128, pancakeswap_v3 29, uniswap_v2 13, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 189 (rejetés 2) → 594 jetons ; pools candidats 3787 (énumérés 341, par paires 0), mesurés 532, sous le plancher de 10000.0 $ : 3 → gardés 529 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2307.602823, 'cbBTC': 79842.460004, 'AERO': 0.67568}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 157,884,974 | 2,317.975196 | 53117687 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,730,632 | 0.028970 | 53117687 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,160,720 | 0.028964 | 53117687 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,466,660 | 0.000013 | 53117687 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome | WETH/VVV | 3000 | 8,840,329 | 93.121032 | 53117687 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/USDC | 500 | 8,306,159 | 2,312.380361 | 53117687 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | USDC/AERO | 3000 | 7,218,886 | 1.458749 | 53117687 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,004,452 | 0.001659 | 53117687 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,352,635 | 0.028959 | 53117687 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/USDC | 892 | 5,348,424 | 2,312.697475 | 53117687 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,458,442 | 2,311.847890 | 53117687 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,210,988 | 0.999584 | 53117687 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,798,149 | 34,862.626716 | 53117687 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/USDC | 3000 | 3,744,771 | 2,315.520381 | 53117687 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 3,199,912 | 0.028949 | 53117687 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2790 | 2,498,886 | 93.124361 | 53117687 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | USDC/cbBTC | 592 | 2,474,443 | 0.000013 | 53117687 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,202,318 | 405.644529 | 53117687 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | WETH/FAI | 10000 | 2,121,576 | 1,210,234.968788 | 53117687 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,887,439 | 0.000013 | 53117687 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,886,320 | 0.000000 | 53117687 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,817,539 | 0.018471 | 53117687 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,713,155 | 0.000013 | 53117687 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | USDC/cbBTC | 364 | 1,697,130 | 0.000013 | 53117687 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | VIRTUAL/WETH | 10000 | 1,552,880 | 0.000265 | 53117687 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,514,358 | 0.005902 | 53117687 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,457,958 | 0.826447 | 53117687 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,453,150 | 1.698035 | 53117687 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | WETH/AERO | 3000 | 1,435,040 | 3,378.389607 | 53117687 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,367,530 | 14,003.911174 | 53117687 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,231,606 | 0.000267 | 53117687 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | WETH/AERO | 10000 | 1,230,608 | 3,402.035433 | 53117687 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | USDC/SEND | 3000 | 1,221,560 | 65.119740 | 53117687 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,206,169 | 2,312.271832 | 53117687 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | DRB/WETH | 10000 | 1,168,146 | 0.000000 | 53117687 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | WETH/WELL | 10000 | 1,136,055 | 1,092,273.529269 | 53117687 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/doginme | 10000 | 1,131,374 | 37,579,806.280132 | 53117687 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,105,315 | 499,327.370307 | 53117687 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,068,613 | 20,057,418.320076 | 53117687 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome | WETH/EDEL | 7000 | 1,067,448 | 72,261.920208 | 53117687 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | USDC/NOCK | 3000 | 1,052,794 | 56.511011 | 53117687 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,028,370 | 17.516691 | 53117687 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | USDC/VVV | 3000 | 973,507 | 0.040279 | 53117687 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/USDC | 10000 | 922,293 | 2,311.179744 | 53117687 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome | WETH/msETH (stable) | 500 | 906,251 | 2.308515 | 53117687 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | uXRP/WETH | 3000 | 893,290 | 0.000557 | 53117687 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 880,714 | 17.033008 | 53117687 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| uniswap_v3 | WETH/MORPHO | 3000 | 879,233 | 1,142.046788 | 53117687 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome_slipstream | USDC/SAPIEN | 4525 | 878,288 | 17.995260 | 53117687 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v3 | WETH/VVV | 10000 | 867,455 | 93.744740 | 53117687 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v2 | WETH/USDC | 3000 | 844,452 | 2,317.504324 | 53117687 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 805,057 | 0.000009 | 53117687 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| pancakeswap_v3 | QUID/USDC | 100 | 795,881 | 0.056787 | 53117687 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 784,826 | 0.803142 | 53117687 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 743,777 | 0.618398 | 53117687 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 731,027 | 4,746,435.244168 | 53117687 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v2 | WETH/NPC | 3000 | 700,876 | 137,675.348140 | 53117687 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| uniswap_v3 | TIG/USDC | 10000 | 697,844 | 0.612711 | 53117687 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | WETH/BRETT | 2132 | 690,574 | 495,690.159738 | 53117687 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 677,788 | 0.109844 | 53117687 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |

## Recherche d'opportunités
- Cycles : 512 ; routes examinées : 9946112 ; candidats optimisés : 31478 ; net attendu > 0 : 135 ; dernier cycle 207.7 ms
- Rejets (moteur) : {'spread_below_threshold': 9755651, 'liquidity_below_min': 148403, 'negative_expected_net': 31343, 'unquotable': 10068, 'borrow_bound_too_small': 512}
- Enregistrements de la session : 31478 ; net attendu > 0 : 135 ; simulés (eth_call de la vraie tx) : 6 (ok 3, échec 3) ; étiquettes ghost N+1 : 0/6 positives
- Décisions : {'REJECTED': 31478} ; motifs de rejet : {'below_safety_margin': 111, 'negative_expected_net': 31343, 'p_lower_below_threshold': 123, 'price_impact': 4, 'reliability_not_demonstrated': 12, 'simulation_failed': 3}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53117512 | USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 166.418370 USDC | 0.044255 USDC | 0.000000 USDC | 0.001203 USDC | 0.043052 USDC (0.0396 €) | — | 2.59 | 0.138 (n=346) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 53117512 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH | 0.071718 WETH | 0.000019 WETH | 0.000000 WETH | 0.000001 WETH | 0.000019 WETH (0.0395 €) | 0.000019 WETH | 2.59 | 0.138 (n=346) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 53117512 | USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 493.169353 USDC | 0.029918 USDC | 0.000000 USDC | 0.001203 USDC | 0.028715 USDC (0.0264 €) | — | 0.58 | 0.138 (n=346) | REJECTED | below_safety_margin(28715<98633), p_lower_below_threshold(0.14<0.75) |
| 53117512 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH | 0.214196 WETH | 0.000013 WETH | 0.000000 WETH | 0.000001 WETH | 0.000012 WETH (0.0261 €) | — | 0.57 | 0.138 (n=346) | REJECTED | below_safety_margin(12232716902053<42839285508129), p_lower_below_threshold(0.14<0.75) |
| 53117512 | cbBTC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.005431 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0257 €) | — | 0.64 | 0.138 (n=346) | REJECTED | below_safety_margin(35<108), p_lower_below_threshold(0.14<0.75) |
| 53117512 | USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 101.471583 USDC | 0.020275 USDC | 0.000000 USDC | 0.001203 USDC | 0.019072 USDC (0.0175 €) | — | 1.88 | 0.182 (n=178) | REJECTED | below_safety_margin(19072<20294), p_lower_below_threshold(0.18<0.75) |
| 53117512 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH | 0.043976 WETH | 0.000009 WETH | 0.000000 WETH | 0.000001 WETH | 0.000008 WETH (0.0175 €) | — | 1.87 | 0.182 (n=178) | REJECTED | below_safety_margin(8216505034538<8795280748470), p_lower_below_threshold(0.18<0.75) |
| 53117541 | USDC→[aerodrome_slipstream]→USDT→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 127.494300 USDC | 0.022226 USDC | 0.000000 USDC | 0.007010 USDC | 0.015216 USDC (0.0140 €) | — | 1.19 | 0.182 (n=178) | REJECTED | below_safety_margin(15216<25498), p_lower_below_threshold(0.18<0.75) |
| 53117541 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→USDT→[uniswap_v3]→WETH | 0.054928 WETH | 0.000010 WETH | 0.000000 WETH | 0.000003 WETH | 0.000007 WETH (0.0139 €) | — | 1.19 | 0.182 (n=178) | REJECTED | below_safety_margin(6541833503514<10985597991880), p_lower_below_threshold(0.18<0.75) |
| 53117541 | USDC→[uniswap_v2]→WETH→[uniswap_v3]→USDC | 74.885535 USDC | 0.015495 USDC | 0.000000 USDC | 0.004520 USDC | 0.010975 USDC (0.0101 €) | — | 1.47 | 0.002 (n=4) | REJECTED | below_safety_margin(10975<14977), reliability_not_demonstrated |
| 53117541 | WETH→[uniswap_v3]→USDC→[uniswap_v2]→WETH | 0.032309 WETH | 0.000007 WETH | 0.000000 WETH | 0.000002 WETH | 0.000005 WETH (0.0101 €) | — | 1.46 | 0.002 (n=4) | REJECTED | below_safety_margin(4718888491445<6461727787267), reliability_not_demonstrated |
| 53117512 | USDC→[sushiswap_v3]→WETH→[pancakeswap_v3]→USDC | 67.245450 USDC | 0.011552 USDC | 0.000000 USDC | 0.000902 USDC | 0.010650 USDC (0.0098 €) | — | 1.58 | 0.022 (n=95) | REJECTED | below_safety_margin(10650<13449), p_lower_below_threshold(0.02<0.75) |
| 53117512 | WETH→[pancakeswap_v3]→USDC→[sushiswap_v3]→WETH | 0.029358 WETH | 0.000005 WETH | 0.000000 WETH | 0.000000 WETH | 0.000005 WETH (0.0098 €) | — | 1.56 | 0.022 (n=95) | REJECTED | below_safety_margin(4587254591267<5871660678500), p_lower_below_threshold(0.02<0.75) |
| 53117512 | USDC→[aerodrome_slipstream]→USDbC→[aerodrome]→WETH→[pancakeswap_v3]→USDC | 12.679256 USDC | 0.010192 USDC | 0.000000 USDC | 0.001150 USDC | 0.009042 USDC (0.0083 €) | — | 7.13 | 0.057 (n=50) | REJECTED | p_lower_below_threshold(0.06<0.75) |
| 53117512 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→USDbC→[aerodrome]→WETH | 0.005488 WETH | 0.000004 WETH | 0.000000 WETH | 0.000000 WETH | 0.000004 WETH (0.0083 €) | 0.000004 WETH | 7.09 | 0.057 (n=50) | REJECTED | p_lower_below_threshold(0.06<0.75) |
| 53117512 | USDC→[aerodrome_slipstream]→EURC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 47.945982 USDC | 0.009662 USDC | 0.000000 USDC | 0.001203 USDC | 0.008459 USDC (0.0078 €) | — | 1.76 | 0.138 (n=346) | REJECTED | below_safety_margin(8459<9589), p_lower_below_threshold(0.14<0.75) |
| 53117512 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→EURC→[pancakeswap_v3]→WETH | 0.020780 WETH | 0.000004 WETH | 0.000000 WETH | 0.000001 WETH | 0.000004 WETH (0.0078 €) | — | 1.75 | 0.138 (n=346) | REJECTED | below_safety_margin(3642631867153<4155985035358), p_lower_below_threshold(0.14<0.75) |
| 53117512 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 42.873106 USDC | 0.009044 USDC | 0.000000 USDC | 0.000961 USDC | 0.008083 USDC (0.0074 €) | — | 1.89 | 0.022 (n=95) | REJECTED | below_safety_margin(8083<8574), p_lower_below_threshold(0.02<0.75) |
| 53117512 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.018477 WETH | 0.000004 WETH | 0.000000 WETH | 0.000000 WETH | 0.000003 WETH (0.0074 €) | — | 1.88 | 0.022 (n=95) | REJECTED | below_safety_margin(3481008388997<3695448285772), p_lower_below_threshold(0.02<0.75) |
| 53117512 | USDC→[aerodrome_slipstream]→EURC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 47.018840 USDC | 0.009204 USDC | 0.000000 USDC | 0.001203 USDC | 0.008001 USDC (0.0074 €) | — | 1.70 | 0.138 (n=346) | REJECTED | below_safety_margin(8001<9403), p_lower_below_threshold(0.14<0.75) |
| 53117512 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→EURC→[pancakeswap_v3]→WETH | 0.020281 WETH | 0.000004 WETH | 0.000000 WETH | 0.000001 WETH | 0.000003 WETH (0.0073 €) | — | 1.70 | 0.138 (n=346) | REJECTED | below_safety_margin(3445165181495<4056219984609), p_lower_below_threshold(0.14<0.75) |
| 53117512 | USDC→[aerodrome_slipstream]→USDbC→[aerodrome]→WETH→[uniswap_v3]→USDC | 11.536210 USDC | 0.008503 USDC | 0.000000 USDC | 0.001150 USDC | 0.007353 USDC (0.0068 €) | — | 6.37 | 0.053 (n=157) | REJECTED | p_lower_below_threshold(0.05<0.75) |
| 53117512 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→USDbC→[aerodrome]→WETH | 0.005035 WETH | 0.000004 WETH | 0.000000 WETH | 0.000000 WETH | 0.000003 WETH (0.0067 €) | 0.000003 WETH | 6.29 | 0.053 (n=157) | REJECTED | p_lower_below_threshold(0.05<0.75) |
| 53117541 | USDC→[uniswap_v3]→USDT→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 100.512569 USDC | 0.014313 USDC | 0.000000 USDC | 0.007010 USDC | 0.007303 USDC (0.0067 €) | — | 0.73 | 0.182 (n=178) | REJECTED | below_safety_margin(7303<20102), p_lower_below_threshold(0.18<0.75) |
| 53117541 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→USDT→[uniswap_v3]→WETH | 0.043634 WETH | 0.000006 WETH | 0.000000 WETH | 0.000003 WETH | 0.000003 WETH (0.0067 €) | — | 0.72 | 0.182 (n=178) | REJECTED | below_safety_margin(3135683994448<8726822773131), p_lower_below_threshold(0.18<0.75) |

## Fiabilité et décision
- Observations ghost : 2630 ; taux observé 0.095 ; borne inférieure crédible (0.9) 0.088 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 8.8% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
