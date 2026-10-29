# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-29T00:53:53+00:00 ; durée 150.99 min ; blocs 53218407 → 53222941 (4492 vus)

## Connexion
- Requêtes RPC : 51667 ; erreurs : 83 ; latence p50/p95 : 251.1/1,851.8 ms
- Rafraîchissements d'état : 4493 ; âge des données au dernier bloc : 2.15 s ; changements de frais LP observés (pools à frais dynamiques) : 4677
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 751 ; cycles déclenchés par événement : 79 ; avance médiane sur le rafraîchissement multicall : 796 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,359.93 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 522 pools, 300 jetons, 19152 routes
- Par DEX : uniswap_v3 147, aerodrome_slipstream 122, aerodrome 210, pancakeswap_v3 28, uniswap_v2 12, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 183 (rejetés 2) → 588 jetons ; pools candidats 3758 (énumérés 331, par paires 0), mesurés 524, sous le plancher de 10000.0 $ : 2 → gardés 522 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDC': 1.0, 'USDbC': 1.0, 'WETH': 2360.669373, 'cbBTC': 81164.401586, 'AERO': 0.699093}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 158,729,937 | 2,359.933166 | 53222941 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,645,927 | 0.029030 | 53222941 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,915,959 | 0.000012 | 53222941 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,522,582 | 0.029058 | 53222941 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 8,399,114 | 2,354.524544 | 53222941 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 8,280,973 | 98.427011 | 53222941 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,081,499 | 0.001643 | 53222941 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 6,679,194 | 1.443063 | 53222941 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,816,620 | 0.029033 | 53222941 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/USDC | 150 | 4,832,891 | 2,353.729804 | 53222941 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,469,800 | 2,353.630765 | 53222941 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,279,533 | 0.998959 | 53222941 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,661,598 | 38,876.476930 | 53222941 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,959,296 | 0.029044 | 53222941 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2715 | 2,518,661 | 98.453738 | 53222941 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | USDC/cbBTC | 400 | 2,361,144 | 0.000012 | 53222941 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome | WETH/FAI | 10000 | 2,153,720 | 1,217,279.567811 | 53222941 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome | WETH/USDC | 3000 | 1,831,672 | 2,357.564177 | 53222941 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| uniswap_v3 | XDP/USDC | 100 | 1,829,270 | 0.018798 | 53222941 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,801,380 | 399.260456 | 53222941 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,782,947 | 0.000000 | 53222941 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,724,031 | 0.000012 | 53222941 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,699,746 | 0.000012 | 53222941 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | USDC/cbBTC | 332 | 1,614,930 | 0.000012 | 53222941 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,514,132 | 1.588195 | 53222941 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,460,999 | 0.826761 | 53222941 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,457,439 | 3,395.189138 | 53222941 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,449,018 | 0.005473 | 53222941 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,399,565 | 13,742.781766 | 53222941 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,268,168 | 2,354.582723 | 53222941 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,256,453 | 0.000266 | 53222941 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | USDC/SEND | 3000 | 1,192,122 | 68.375509 | 53222941 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,162,819 | 36,679,087.056816 | 53222941 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | VIRTUAL/WETH | 10000 | 1,162,247 | 0.000266 | 53222941 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome | WETH/WELL | 10000 | 1,160,300 | 1,084,689.644666 | 53222941 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,137,301 | 485,543.666594 | 53222941 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,113,001 | 0.000000 | 53222941 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,083,702 | 21,249,010.360294 | 53222941 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome | WETH/EDEL | 7000 | 1,072,617 | 73,953.768702 | 53222941 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | WETH/AERO | 10000 | 1,070,652 | 3,371.320948 | 53222941 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,054,915 | 16.354446 | 53222941 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v2 | WETH/USDC | 3000 | 1,034,424 | 2,355.672192 | 53222941 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome | USDC/NOCK | 3000 | 1,011,381 | 61.199601 | 53222941 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/VVV | 10000 | 1,002,310 | 98.205990 | 53222941 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | USDC/VVV | 3000 | 997,513 | 0.041806 | 53222941 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/USDC | 10000 | 941,914 | 2,366.107395 | 53222941 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 936,172 | 1,054.892680 | 53222941 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | uXRP/WETH | 3000 | 910,765 | 0.000558 | 53222941 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | USDC/SAPIEN | 4525 | 882,820 | 17.860638 | 53222941 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome | WETH/msETH (stable) | 500 | 879,877 | 2.332399 | 53222941 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| pancakeswap_v3 | QUID/USDC | 100 | 865,521 | 0.068010 | 53222941 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 850,672 | 17.546896 | 53222941 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | WETH/wstETH | 3000 | 799,116 | 0.802973 | 53222941 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 754,109 | 0.625764 | 53222941 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 753,631 | 0.000009 | 53222941 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 752,248 | 4,646,729.331527 | 53222941 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v2 | WETH/NPC | 3000 | 715,646 | 136,953.559876 | 53222941 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 712,772 | 485,200.839512 | 53222941 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 672,606 | 0.108298 | 53222941 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| uniswap_v3 | TIG/USDC | 10000 | 649,725 | 0.533020 | 53222941 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |

## Recherche d'opportunités
- Cycles : 4571 ; routes examinées : 87543792 ; candidats optimisés : 288914 ; net attendu > 0 : 66 ; dernier cycle 345.1 ms
- Rejets (moteur) : {'spread_below_threshold': 86288886, 'liquidity_below_min': 961148, 'negative_expected_net': 288848, 'borrow_bound_too_small': 4567, 'cycle_budget_exhausted': 277}
- Enregistrements de la session : 288914 ; net attendu > 0 : 66 ; simulés (eth_call de la vraie tx) : 11 (ok 11, échec 0) ; étiquettes ghost N+1 : 0/11 positives
- Décisions : {'REJECTED': 288914} ; motifs de rejet : {'below_safety_margin': 34, 'negative_expected_net': 288848, 'p_lower_below_threshold': 64, 'reliability_not_demonstrated': 2, 'stale_data': 16}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53220050 | USDC→[pancakeswap_v3]→USDT→[aerodrome_slipstream]→USDC | 1,720.189536 USDC | 0.194471 USDC | 0.000000 USDC | 0.006015 USDC | 0.188456 USDC (0.1734 €) | — | 1.10 | 0.032 (n=111) | REJECTED | below_safety_margin(188456<344037), p_lower_below_threshold(0.03<0.75) |
| 53220050 | USDC→[pancakeswap_v3]→USDT→[uniswap_v3]→USDC | 1,313.415456 USDC | 0.106189 USDC | 0.000000 USDC | 0.005657 USDC | 0.100532 USDC (0.0925 €) | — | 0.77 | 0.032 (n=111) | REJECTED | below_safety_margin(100532<262683), p_lower_below_threshold(0.03<0.75) |
| 53220644 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→WETH | 0.008013 WETH | 0.000013 WETH | 0.000000 WETH | 0.000003 WETH | 0.000010 WETH (0.0219 €) | 0.000010 WETH | 12.57 | 0.000 (n=67) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53220644 | USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 18.909534 USDC | 0.030843 USDC | 0.000000 USDC | 0.007091 USDC | 0.023752 USDC (0.0219 €) | — | 12.56 | 0.000 (n=67) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53220644 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→WETH | 0.007967 WETH | 0.000013 WETH | 0.000000 WETH | 0.000003 WETH | 0.000010 WETH (0.0214 €) | 0.000010 WETH | 12.35 | 0.004 (n=71) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53220644 | USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 18.755953 USDC | 0.030303 USDC | 0.000000 USDC | 0.007091 USDC | 0.023212 USDC (0.0214 €) | — | 12.38 | 0.004 (n=71) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53220644 | WETH→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→WETH | 0.007165 WETH | 0.000012 WETH | 0.000000 WETH | 0.000003 WETH | 0.000009 WETH (0.0191 €) | 0.000009 WETH | 12.31 | 0.000 (n=67) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53220644 | USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→USDC | 16.951352 USDC | 0.028238 USDC | 0.000000 USDC | 0.007450 USDC | 0.020788 USDC (0.0191 €) | — | 12.26 | 0.000 (n=67) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53220644 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→WETH | 0.007215 WETH | 0.000011 WETH | 0.000000 WETH | 0.000003 WETH | 0.000008 WETH (0.0164 €) | — | 10.44 | 0.004 (n=71) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53220644 | USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 16.961312 USDC | 0.024850 USDC | 0.000000 USDC | 0.007091 USDC | 0.017759 USDC (0.0163 €) | — | 10.47 | 0.004 (n=71) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53220644 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→WETH | 0.007138 WETH | 0.000010 WETH | 0.000000 WETH | 0.000003 WETH | 0.000007 WETH (0.0157 €) | — | 10.14 | 0.000 (n=67) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53220644 | USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 16.768812 USDC | 0.024161 USDC | 0.000000 USDC | 0.007091 USDC | 0.017070 USDC (0.0157 €) | — | 10.18 | 0.000 (n=67) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53220644 | WETH→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→WETH | 0.007014 WETH | 0.000010 WETH | 0.000000 WETH | 0.000003 WETH | 0.000007 WETH (0.0149 €) | — | 9.78 | 0.000 (n=67) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53220644 | USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→USDC | 16.426008 USDC | 0.023261 USDC | 0.000000 USDC | 0.007091 USDC | 0.016170 USDC (0.0149 €) | — | 9.84 | 0.000 (n=67) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53218704 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 17.735437 USDC | 0.023238 USDC | 0.000000 USDC | 0.007098 USDC | 0.016140 USDC (0.0148 €) | — | 9.10 | 0.004 (n=70) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53218704 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.007509 WETH | 0.000010 WETH | 0.000000 WETH | 0.000003 WETH | 0.000007 WETH (0.0148 €) | 0.000007 WETH | 9.08 | 0.004 (n=70) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53218704 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 17.595281 USDC | 0.022963 USDC | 0.000000 USDC | 0.007098 USDC | 0.015865 USDC (0.0146 €) | — | 9.02 | 0.000 (n=66) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53218704 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.007471 WETH | 0.000010 WETH | 0.000000 WETH | 0.000003 WETH | 0.000007 WETH (0.0146 €) | 0.000007 WETH | 8.97 | 0.000 (n=66) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53220644 | WETH→[sushiswap_v3]→USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→WETH | 0.006845 WETH | 0.000010 WETH | 0.000000 WETH | 0.000003 WETH | 0.000007 WETH (0.0142 €) | — | 9.57 | 0.000 (n=67) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53220644 | USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→WETH→[sushiswap_v3]→USDC | 16.078501 USDC | 0.022892 USDC | 0.000000 USDC | 0.007450 USDC | 0.015442 USDC (0.0142 €) | — | 9.60 | 0.000 (n=67) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53222585 | USDC→[aerodrome_slipstream]→EURC→[aerodrome_slipstream]→USDC | 382.997752 USDC | 0.019625 USDC | 0.000000 USDC | 0.005299 USDC | 0.014326 USDC (0.0132 €) | — | 0.37 | 0.010 (n=28) | REJECTED | below_safety_margin(14326<76599), reliability_not_demonstrated |
| 53220948 | cbBTC→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→VIRTUAL→[aerodrome]→cbBTC | 0.000448 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0112 €) | 0.000000 cbBTC | 3.35 | 0.066 (n=164) | REJECTED | p_lower_below_threshold(0.07<0.75) |
| 53220948 | WETH→[aerodrome_slipstream]→VIRTUAL→[aerodrome]→cbBTC→[aerodrome_slipstream]→WETH | 0.016113 WETH | 0.000008 WETH | 0.000000 WETH | 0.000003 WETH | 0.000005 WETH (0.0112 €) | 0.000005 WETH | 3.20 | 0.066 (n=164) | REJECTED | p_lower_below_threshold(0.07<0.75) |
| 53218704 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 14.056658 USDC | 0.017001 USDC | 0.000000 USDC | 0.007098 USDC | 0.009903 USDC (0.0091 €) | — | 7.05 | 0.139 (n=186) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 53218704 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.005930 WETH | 0.000007 WETH | 0.000000 WETH | 0.000003 WETH | 0.000004 WETH (0.0091 €) | 0.000004 WETH | 7.05 | 0.139 (n=186) | REJECTED | p_lower_below_threshold(0.14<0.75) |

## Fiabilité et décision
- Observations ghost : 3052 ; taux observé 0.097 ; borne inférieure crédible (0.9) 0.090 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 9.0% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
