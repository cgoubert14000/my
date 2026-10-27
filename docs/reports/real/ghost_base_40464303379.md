# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-27T10:28:23+00:00 ; durée 203.59 min ; blocs 53147666 → 53153776 (6025 vus)

## Connexion
- Requêtes RPC : 70505 ; erreurs : 3 ; latence p50/p95 : 132.6/1,228.2 ms
- Rafraîchissements d'état : 6026 ; âge des données au dernier bloc : 1.53 s ; changements de frais LP observés (pools à frais dynamiques) : 8524
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 25710 ; cycles déclenchés par événement : 2116 ; avance médiane sur le rafraîchissement multicall : 535 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,301.68 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 526 pools, 304 jetons, 19350 routes
- Par DEX : uniswap_v3 143, aerodrome_slipstream 127, aerodrome 212, pancakeswap_v3 28, uniswap_v2 13, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 189 (rejetés 2) → 594 jetons ; pools candidats 3790 (énumérés 338, par paires 0), mesurés 528, sous le plancher de 10000.0 $ : 2 → gardés 526 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2304.525597, 'cbBTC': 79510.140598, 'AERO': 0.665632}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 155,443,575 | 2,301.678090 | 53153776 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,035,641 | 0.028928 | 53153776 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,030,195 | 0.028956 | 53153776 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,481,007 | 0.000013 | 53153776 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome | WETH/VVV | 3000 | 8,465,933 | 91.362791 | 53153776 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/USDC | 500 | 8,255,913 | 2,300.470643 | 53153776 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | USDC/AERO | 3000 | 6,925,804 | 1.504108 | 53153776 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,908,907 | 0.001633 | 53153776 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,311,877 | 0.028930 | 53153776 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/USDC | 150 | 5,219,233 | 2,300.400293 | 53153776 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,428,705 | 2,300.507087 | 53153776 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,191,046 | 0.998744 | 53153776 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,633,661 | 37,556.634460 | 53153776 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 3,154,189 | 0.028971 | 53153776 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2721 | 2,520,556 | 91.344203 | 53153776 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | USDC/cbBTC | 424 | 2,412,712 | 0.000013 | 53153776 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome | WETH/USDC | 3000 | 2,345,299 | 2,302.866808 | 53153776 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome | WETH/FAI | 10000 | 2,100,315 | 1,217,557.512867 | 53153776 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | XDP/USDC | 100 | 1,834,072 | 0.018787 | 53153776 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,827,913 | 0.000000 | 53153776 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,744,248 | 405.937126 | 53153776 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,685,419 | 0.000013 | 53153776 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | USDC/cbBTC | 334 | 1,682,962 | 0.000013 | 53153776 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,658,548 | 0.000013 | 53153776 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,491,946 | 0.005844 | 53153776 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,461,100 | 0.826497 | 53153776 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,453,150 | 1.698035 | 53153776 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | WETH/AERO | 3000 | 1,416,022 | 3,453.318162 | 53153776 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,358,974 | 14,012.181042 | 53153776 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,222,725 | 0.000265 | 53153776 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | USDC/SEND | 3000 | 1,217,266 | 65.580017 | 53153776 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,214,267 | 2,300.507176 | 53153776 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | WETH/AERO | 10000 | 1,188,977 | 3,447.248911 | 53153776 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | VIRTUAL/WETH | 10000 | 1,162,009 | 0.000266 | 53153776 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome | WETH/WELL | 10000 | 1,142,247 | 1,065,324.060489 | 53153776 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/doginme | 10000 | 1,131,228 | 36,876,948.332279 | 53153776 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | DRB/WETH | 10000 | 1,131,065 | 0.000000 | 53153776 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,094,868 | 502,781.004257 | 53153776 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | WETH/EDEL | 7000 | 1,060,674 | 71,955.541747 | 53153776 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,037,772 | 20,873,122.760680 | 53153776 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,027,355 | 17.565261 | 53153776 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | USDC/NOCK | 3000 | 1,022,944 | 59.823042 | 53153776 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | USDC/VVV | 3000 | 1,017,789 | 0.039725 | 53153776 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/USDC | 10000 | 936,250 | 2,317.653415 | 53153776 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 901,973 | 1,067.274573 | 53153776 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome | WETH/msETH (stable) | 500 | 899,811 | 2.308782 | 53153776 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | uXRP/WETH | 3000 | 888,252 | 0.000558 | 53153776 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| uniswap_v3 | WETH/VVV | 10000 | 872,970 | 91.898518 | 53153776 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 868,164 | 18.339614 | 53153776 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v2 | WETH/USDC | 3000 | 841,544 | 2,300.850366 | 53153776 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 825,348 | 17.629532 | 53153776 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| pancakeswap_v3 | QUID/USDC | 100 | 793,121 | 0.056369 | 53153776 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 788,315 | 0.000008 | 53153776 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | WETH/wstETH | 3000 | 779,290 | 0.803179 | 53153776 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 735,153 | 4,627,314.738594 | 53153776 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 734,751 | 0.608497 | 53153776 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v3 | TIG/USDC | 10000 | 693,803 | 0.605717 | 53153776 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/NPC | 3000 | 692,523 | 139,029.481945 | 53153776 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 683,235 | 506,597.976522 | 53153776 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 664,706 | 0.106348 | 53153776 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |

## Recherche d'opportunités
- Cycles : 8141 ; routes examinées : 157528350 ; candidats optimisés : 414934 ; net attendu > 0 : 164 ; dernier cycle 281.5 ms
- Rejets (moteur) : {'spread_below_threshold': 154736590, 'liquidity_below_min': 2142814, 'negative_expected_net': 414770, 'borrow_bound_too_small': 151644, 'pool_quarantined': 65016, 'unquotable': 16368, 'cycle_budget_exhausted': 984}
- Enregistrements de la session : 414934 ; net attendu > 0 : 164 ; simulés (eth_call de la vraie tx) : 22 (ok 6, échec 16) ; étiquettes ghost N+1 : 0/19 positives
- Décisions : {'REJECTED': 414934} ; motifs de rejet : {'below_safety_margin': 57, 'negative_expected_net': 414770, 'p_lower_below_threshold': 38, 'price_impact': 2, 'reliability_not_demonstrated': 126, 'simulation_failed': 16, 'stale_data': 16}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53148662 | USDC→[pancakeswap_v3]→WETH→[uniswap_v2]→wIRON→[aerodrome]→USDC | 109.477751 USDC | 1.731562 USDC | 0.000000 USDC | 0.005893 USDC | 1.725669 USDC (1.5876 €) | — | 157.63 | 0.003 (n=2) | REJECTED | reliability_not_demonstrated |
| 53148662 | WETH→[uniswap_v2]→wIRON→[aerodrome]→USDC→[pancakeswap_v3]→WETH | 0.047473 WETH | 0.000751 WETH | 0.000000 WETH | 0.000003 WETH | 0.000748 WETH (1.5864 €) | — | 157.63 | 0.003 (n=2) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53148662 | USDC→[uniswap_v3]→WETH→[uniswap_v2]→wIRON→[aerodrome]→USDC | 108.909845 USDC | 1.715471 USDC | 0.000000 USDC | 0.005893 USDC | 1.709578 USDC (1.5728 €) | — | 156.97 | 0.002 (n=4) | REJECTED | reliability_not_demonstrated |
| 53148662 | WETH→[uniswap_v2]→wIRON→[aerodrome]→USDC→[uniswap_v3]→WETH | 0.047218 WETH | 0.000744 WETH | 0.000000 WETH | 0.000003 WETH | 0.000741 WETH (1.5713 €) | — | 156.97 | 0.002 (n=4) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53148662 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v2]→wIRON→[aerodrome]→USDC | 108.901043 USDC | 1.706436 USDC | 0.000000 USDC | 0.005893 USDC | 1.700543 USDC (1.5645 €) | — | 156.15 | 0.002 (n=4) | REJECTED | reliability_not_demonstrated |
| 53148662 | WETH→[uniswap_v2]→wIRON→[aerodrome]→USDC→[aerodrome_slipstream]→WETH | 0.047214 WETH | 0.000740 WETH | 0.000000 WETH | 0.000003 WETH | 0.000737 WETH (1.5630 €) | — | 156.15 | 0.002 (n=4) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53148662 | USDC→[uniswap_v3]→WETH→[uniswap_v2]→wIRON→[aerodrome]→USDC | 104.601254 USDC | 1.642655 USDC | 0.000000 USDC | 0.005893 USDC | 1.636762 USDC (1.5058 €) | — | 156.48 | 0.002 (n=4) | REJECTED | reliability_not_demonstrated |
| 53148662 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v2]→wIRON→[aerodrome]→USDC | 103.610523 USDC | 1.641828 USDC | 0.000000 USDC | 0.005893 USDC | 1.635935 USDC (1.5051 €) | — | 157.89 | 0.002 (n=4) | REJECTED | reliability_not_demonstrated |
| 53148662 | WETH→[uniswap_v2]→wIRON→[aerodrome]→USDC→[uniswap_v3]→WETH | 0.045335 WETH | 0.000712 WETH | 0.000000 WETH | 0.000003 WETH | 0.000709 WETH (1.5039 €) | — | 156.48 | 0.002 (n=4) | REJECTED | reliability_not_demonstrated |
| 53148662 | WETH→[uniswap_v2]→wIRON→[aerodrome]→USDC→[aerodrome_slipstream]→WETH | 0.044869 WETH | 0.000711 WETH | 0.000000 WETH | 0.000003 WETH | 0.000708 WETH (1.5019 €) | — | 157.89 | 0.002 (n=4) | REJECTED | reliability_not_demonstrated |
| 53148662 | USDC→[pancakeswap_v3]→WETH→[uniswap_v2]→wIRON→[aerodrome]→USDC | 104.541616 USDC | 1.636548 USDC | 0.000000 USDC | 0.005893 USDC | 1.630655 USDC (1.5002 €) | — | 155.98 | 0.003 (n=2) | REJECTED | reliability_not_demonstrated |
| 53148662 | WETH→[uniswap_v2]→wIRON→[aerodrome]→USDC→[pancakeswap_v3]→WETH | 0.045306 WETH | 0.000709 WETH | 0.000000 WETH | 0.000003 WETH | 0.000707 WETH (1.4982 €) | — | 155.98 | 0.003 (n=2) | REJECTED | reliability_not_demonstrated |
| 53148662 | USDC→[sushiswap_v3]→WETH→[uniswap_v2]→wIRON→[aerodrome]→USDC | 101.577311 USDC | 1.589476 USDC | 0.000000 USDC | 0.005893 USDC | 1.583583 USDC (1.4569 €) | — | 155.90 | 0.002 (n=4) | REJECTED | reliability_not_demonstrated |
| 53148662 | WETH→[uniswap_v2]→wIRON→[aerodrome]→USDC→[sushiswap_v3]→WETH | 0.043991 WETH | 0.000688 WETH | 0.000000 WETH | 0.000003 WETH | 0.000686 WETH (1.4540 €) | — | 155.90 | 0.002 (n=4) | REJECTED | reliability_not_demonstrated |
| 53148662 | USDC→[uniswap_v3]→WETH→[uniswap_v2]→wIRON→[aerodrome]→USDC | 73.843339 USDC | 1.216181 USDC | 0.000000 USDC | 0.005893 USDC | 1.210288 USDC (1.1135 €) | — | 163.90 | 0.002 (n=4) | REJECTED | reliability_not_demonstrated |
| 53148662 | WETH→[uniswap_v2]→wIRON→[aerodrome]→USDC→[uniswap_v3]→WETH | 0.031948 WETH | 0.000526 WETH | 0.000000 WETH | 0.000003 WETH | 0.000524 WETH (1.1101 €) | — | 163.90 | 0.002 (n=4) | REJECTED | reliability_not_demonstrated |
| 53148662 | USDC→[uniswap_v2]→WETH→[uniswap_v2]→wIRON→[aerodrome]→USDC | 71.764499 USDC | 1.179174 USDC | 0.000000 USDC | 0.005178 USDC | 1.173996 USDC (1.0801 €) | — | 163.59 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 53148662 | WETH→[uniswap_v2]→wIRON→[aerodrome]→USDC→[uniswap_v2]→WETH | 0.031028 WETH | 0.000510 WETH | 0.000000 WETH | 0.000002 WETH | 0.000508 WETH (1.0761 €) | — | 163.59 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 53148662 | USDC→[aerodrome]→WETH→[uniswap_v2]→wIRON→[aerodrome]→USDC | 73.247054 USDC | 1.040157 USDC | 0.000000 USDC | 0.005575 USDC | 1.034582 USDC (0.9518 €) | — | 141.25 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 53148662 | WETH→[uniswap_v2]→wIRON→[aerodrome]→USDC→[aerodrome]→WETH | 0.031613 WETH | 0.000449 WETH | 0.000000 WETH | 0.000002 WETH | 0.000447 WETH (0.9466 €) | — | 141.24 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 53147975 | WETH→[aerodrome]→USDC→[pancakeswap_v3]→WETH | 0.179027 WETH | 0.000066 WETH | 0.000000 WETH | 0.000002 WETH | 0.000064 WETH (0.1359 €) | — | 3.58 | 0.018 (n=16) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53147975 | USDC→[pancakeswap_v3]→WETH→[aerodrome]→USDC | 411.278833 USDC | 0.152220 USDC | 0.000000 USDC | 0.004856 USDC | 0.147364 USDC (0.1356 €) | — | 3.58 | 0.018 (n=16) | REJECTED | reliability_not_demonstrated |
| 53147975 | WETH→[aerodrome]→USDC→[aerodrome_slipstream]→WETH | 0.150927 WETH | 0.000048 WETH | 0.000000 WETH | 0.000002 WETH | 0.000046 WETH (0.0981 €) | — | 3.06 | 0.074 (n=29) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53147975 | USDC→[aerodrome_slipstream]→WETH→[aerodrome]→USDC | 345.738986 USDC | 0.111196 USDC | 0.000000 USDC | 0.004856 USDC | 0.106340 USDC (0.0978 €) | — | 3.08 | 0.074 (n=29) | REJECTED | reliability_not_demonstrated |
| 53149086 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 1,313.861066 USDC | 0.104875 USDC | 0.000000 USDC | 0.005549 USDC | 0.099326 USDC (0.0914 €) | — | 0.76 | 0.020 (n=105) | REJECTED | below_safety_margin(99326<262772), p_lower_below_threshold(0.02<0.75) |

## Fiabilité et décision
- Observations ghost : 2827 ; taux observé 0.090 ; borne inférieure crédible (0.9) 0.084 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 8.4% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
