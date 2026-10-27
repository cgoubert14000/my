# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-27T11:24:33+00:00 ; durée 259.75 min ; blocs 53147666 → 53155459 (7702 vus)

## Connexion
- Requêtes RPC : 90217 ; erreurs : 23 ; latence p50/p95 : 141.1/1,183.1 ms
- Rafraîchissements d'état : 7702 ; âge des données au dernier bloc : 4.89 s ; changements de frais LP observés (pools à frais dynamiques) : 11807
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 25710 ; cycles déclenchés par événement : 2116 ; avance médiane sur le rafraîchissement multicall : 535 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,315.15 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 526 pools, 304 jetons, 19350 routes
- Par DEX : uniswap_v3 143, aerodrome_slipstream 127, aerodrome 212, pancakeswap_v3 28, uniswap_v2 13, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 189 (rejetés 2) → 594 jetons ; pools candidats 3790 (énumérés 338, par paires 0), mesurés 528, sous le plancher de 10000.0 $ : 2 → gardés 526 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2304.525597, 'cbBTC': 79510.140598, 'AERO': 0.665632}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 156,132,761 | 2,315.146677 | 53155460 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,125,960 | 0.028973 | 53155460 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,084,296 | 0.028956 | 53155460 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,503,036 | 0.000013 | 53155460 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome | WETH/VVV | 3000 | 8,538,607 | 90.865295 | 53155460 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/USDC | 500 | 8,320,172 | 2,312.245700 | 53155460 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | USDC/AERO | 3000 | 6,992,076 | 1.475730 | 53155460 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,950,122 | 0.001637 | 53155460 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,337,767 | 0.028975 | 53155460 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/USDC | 150 | 5,241,542 | 2,311.822905 | 53155460 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,448,790 | 2,312.006327 | 53155460 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,208,925 | 0.998745 | 53155460 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,656,180 | 37,530.839553 | 53155460 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 3,166,135 | 0.028971 | 53155460 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2700 | 2,537,424 | 90.845898 | 53155460 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | WETH/USDC | 3000 | 2,351,651 | 2,315.770238 | 53155460 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | USDC/cbBTC | 424 | 2,221,876 | 0.000013 | 53155460 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome | WETH/FAI | 10000 | 2,112,062 | 1,218,183.889145 | 53155460 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,838,588 | 0.000000 | 53155460 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,834,998 | 0.018800 | 53155460 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,757,407 | 403.721647 | 53155460 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,690,380 | 0.000013 | 53155460 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | USDC/cbBTC | 334 | 1,687,332 | 0.000013 | 53155460 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,662,480 | 0.000013 | 53155460 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,502,707 | 0.005854 | 53155460 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,460,781 | 0.826827 | 53155460 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,453,150 | 1.698035 | 53155460 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | WETH/AERO | 3000 | 1,435,152 | 3,412.703563 | 53155460 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,368,534 | 13,934.239278 | 53155460 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,232,011 | 0.000266 | 53155460 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,227,146 | 2,312.361616 | 53155460 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,216,886 | 65.620975 | 53155460 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome | WETH/AERO | 10000 | 1,191,848 | 3,435.363253 | 53155460 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | VIRTUAL/WETH | 10000 | 1,170,806 | 0.000266 | 53155460 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome | WETH/WELL | 10000 | 1,148,476 | 1,066,168.372942 | 53155460 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | DRB/WETH | 10000 | 1,136,701 | 0.000000 | 53155460 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/doginme | 10000 | 1,134,966 | 37,164,026.703077 | 53155460 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,101,300 | 502,748.585952 | 53155460 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | WETH/EDEL | 7000 | 1,066,945 | 71,946.928780 | 53155460 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,047,280 | 20,906,553.567026 | 53155460 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,027,506 | 17.558241 | 53155460 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | USDC/VVV | 3000 | 1,024,931 | 0.039273 | 53155460 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | USDC/NOCK | 3000 | 1,024,385 | 59.654742 | 53155460 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/USDC | 10000 | 938,543 | 2,317.653415 | 53155460 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 906,832 | 1,068.270589 | 53155460 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome | WETH/msETH (stable) | 500 | 905,077 | 2.308782 | 53155460 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | uXRP/WETH | 3000 | 894,753 | 0.000560 | 53155460 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| uniswap_v3 | WETH/VVV | 10000 | 890,743 | 91.514392 | 53155460 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 872,164 | 18.205625 | 53155460 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v2 | WETH/USDC | 3000 | 844,012 | 2,316.352584 | 53155460 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 830,526 | 17.621560 | 53155460 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 799,121 | 0.000009 | 53155460 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| pancakeswap_v3 | QUID/USDC | 100 | 796,679 | 0.056903 | 53155460 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 783,850 | 0.803179 | 53155460 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 741,123 | 4,606,561.274916 | 53155460 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 740,058 | 0.615635 | 53155460 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/NPC | 3000 | 695,569 | 139,432.827001 | 53155460 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| uniswap_v3 | TIG/USDC | 10000 | 692,700 | 0.603873 | 53155460 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 687,254 | 504,604.361914 | 53155460 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 671,696 | 0.108157 | 53155460 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |

## Recherche d'opportunités
- Cycles : 9817 ; routes examinées : 189958950 ; candidats optimisés : 505387 ; net attendu > 0 : 177 ; dernier cycle 258.9 ms
- Rejets (moteur) : {'spread_below_threshold': 186599930, 'liquidity_below_min': 2609626, 'negative_expected_net': 505210, 'borrow_bound_too_small': 161424, 'pool_quarantined': 65016, 'unquotable': 16368, 'cycle_budget_exhausted': 1199}
- Enregistrements de la session : 505387 ; net attendu > 0 : 177 ; simulés (eth_call de la vraie tx) : 24 (ok 8, échec 16) ; étiquettes ghost N+1 : 0/21 positives
- Décisions : {'REJECTED': 505387} ; motifs de rejet : {'below_safety_margin': 68, 'negative_expected_net': 505210, 'p_lower_below_threshold': 49, 'price_impact': 2, 'reliability_not_demonstrated': 128, 'simulation_failed': 16, 'stale_data': 16}

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
- Observations ghost : 2829 ; taux observé 0.090 ; borne inférieure crédible (0.9) 0.083 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 8.3% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
