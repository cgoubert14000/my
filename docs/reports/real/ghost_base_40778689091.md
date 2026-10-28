# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-28T23:42:53+00:00 ; durée 79.98 min ; blocs 53218407 → 53220811 (2386 vus)

## Connexion
- Requêtes RPC : 27430 ; erreurs : 28 ; latence p50/p95 : 228.6/1,806.3 ms
- Rafraîchissements d'état : 2386 ; âge des données au dernier bloc : 2.49 s ; changements de frais LP observés (pools à frais dynamiques) : 2427
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 751 ; cycles déclenchés par événement : 79 ; avance médiane sur le rafraîchissement multicall : 796 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,360.02 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 522 pools, 300 jetons, 19152 routes
- Par DEX : uniswap_v3 147, aerodrome_slipstream 122, aerodrome 210, pancakeswap_v3 28, uniswap_v2 12, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 183 (rejetés 2) → 588 jetons ; pools candidats 3758 (énumérés 331, par paires 0), mesurés 524, sous le plancher de 10000.0 $ : 2 → gardés 522 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDC': 1.0, 'USDbC': 1.0, 'WETH': 2360.669373, 'cbBTC': 81164.401586, 'AERO': 0.699093}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 158,788,668 | 2,360.020367 | 53220811 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,651,868 | 0.029020 | 53220811 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,914,221 | 0.000012 | 53220811 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,524,805 | 0.029058 | 53220811 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 8,399,987 | 2,357.991778 | 53220811 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 8,292,188 | 98.168195 | 53220811 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,093,005 | 0.001647 | 53220811 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 6,706,833 | 1.431585 | 53220811 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,820,715 | 0.029009 | 53220811 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/USDC | 150 | 4,832,877 | 2,357.563744 | 53220811 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,527,059 | 2,357.609445 | 53220811 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,282,646 | 0.998802 | 53220811 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,662,292 | 38,864.602512 | 53220811 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,959,662 | 0.029044 | 53220811 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2751 | 2,521,903 | 98.108596 | 53220811 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | USDC/cbBTC | 412 | 2,361,679 | 0.000012 | 53220811 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome | WETH/FAI | 10000 | 2,153,868 | 1,217,202.137836 | 53220811 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome | WETH/USDC | 3000 | 1,831,706 | 2,356.919988 | 53220811 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| uniswap_v3 | XDP/USDC | 100 | 1,825,627 | 0.018730 | 53220811 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,801,893 | 398.871337 | 53220811 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,784,512 | 0.000000 | 53220811 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,724,371 | 0.000012 | 53220811 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,700,118 | 0.000012 | 53220811 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | USDC/cbBTC | 330 | 1,615,256 | 0.000012 | 53220811 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,514,132 | 1.588195 | 53220811 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,491,034 | 0.005664 | 53220811 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v3 | WETH/AERO | 3000 | 1,463,697 | 3,373.790861 | 53220811 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,460,080 | 0.826662 | 53220811 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,400,442 | 13,738.000902 | 53220811 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,268,578 | 2,357.710190 | 53220811 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,257,587 | 0.000266 | 53220811 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | USDC/SEND | 3000 | 1,192,122 | 68.375509 | 53220811 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome | VIRTUAL/WETH | 10000 | 1,163,298 | 0.000266 | 53220811 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | WETH/doginme | 10000 | 1,162,862 | 36,679,087.056816 | 53220811 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | WETH/WELL | 10000 | 1,159,501 | 1,086,273.213064 | 53220811 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,137,343 | 485,543.666594 | 53220811 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,095,548 | 0.000000 | 53220811 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,086,795 | 21,145,365.806407 | 53220811 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome | WETH/EDEL | 7000 | 1,076,734 | 73,394.744213 | 53220811 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | WETH/AERO | 10000 | 1,075,362 | 3,350.985819 | 53220811 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,055,920 | 16.313040 | 53220811 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v2 | WETH/USDC | 3000 | 1,034,441 | 2,359.907268 | 53220811 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome | USDC/NOCK | 3000 | 1,014,421 | 60.833263 | 53220811 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/VVV | 10000 | 1,003,749 | 98.481738 | 53220811 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | USDC/VVV | 3000 | 999,279 | 0.041625 | 53220811 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/USDC | 10000 | 942,024 | 2,366.107395 | 53220811 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 937,358 | 1,052.147439 | 53220811 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | uXRP/WETH | 3000 | 912,669 | 0.000560 | 53220811 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 883,553 | 17.836212 | 53220811 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome | WETH/msETH (stable) | 500 | 879,912 | 2.332399 | 53220811 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 851,483 | 17.529462 | 53220811 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| pancakeswap_v3 | QUID/USDC | 100 | 810,226 | 0.058968 | 53220811 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 799,146 | 0.802973 | 53220811 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 756,977 | 0.000009 | 53220811 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 755,076 | 0.627476 | 53220811 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 751,885 | 4,651,547.833682 | 53220811 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v2 | WETH/NPC | 3000 | 715,674 | 136,953.134194 | 53220811 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | WETH/BRETT | 2093 | 712,797 | 488,568.168024 | 53220811 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 667,711 | 0.107030 | 53220811 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| uniswap_v3 | TIG/USDC | 10000 | 648,935 | 0.531801 | 53220811 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |

## Recherche d'opportunités
- Cycles : 2464 ; routes examinées : 47190528 ; candidats optimisés : 163823 ; net attendu > 0 : 35 ; dernier cycle 484.6 ms
- Rejets (moteur) : {'spread_below_threshold': 46436352, 'liquidity_below_min': 587758, 'negative_expected_net': 163788, 'borrow_bound_too_small': 2463, 'cycle_budget_exhausted': 132}
- Enregistrements de la session : 163823 ; net attendu > 0 : 35 ; simulés (eth_call de la vraie tx) : 7 (ok 7, échec 0) ; étiquettes ghost N+1 : 0/7 positives
- Décisions : {'REJECTED': 163823} ; motifs de rejet : {'below_safety_margin': 8, 'negative_expected_net': 163788, 'p_lower_below_threshold': 35, 'stale_data': 4}

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
| 53218704 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 14.056658 USDC | 0.017001 USDC | 0.000000 USDC | 0.007098 USDC | 0.009903 USDC (0.0091 €) | — | 7.05 | 0.139 (n=186) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 53218704 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.005930 WETH | 0.000007 WETH | 0.000000 WETH | 0.000003 WETH | 0.000004 WETH (0.0091 €) | 0.000004 WETH | 7.05 | 0.139 (n=186) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 53218704 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 15.058811 USDC | 0.016742 USDC | 0.000000 USDC | 0.007098 USDC | 0.009644 USDC (0.0089 €) | — | 6.40 | 0.139 (n=186) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 53218704 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.006430 WETH | 0.000007 WETH | 0.000000 WETH | 0.000003 WETH | 0.000004 WETH (0.0088 €) | — | 6.33 | 0.139 (n=186) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 53218704 | USDC→[sushiswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 14.567689 USDC | 0.016262 USDC | 0.000000 USDC | 0.007098 USDC | 0.009164 USDC (0.0084 €) | — | 6.29 | 0.139 (n=186) | REJECTED | p_lower_below_threshold(0.14<0.75) |

## Fiabilité et décision
- Observations ghost : 3048 ; taux observé 0.097 ; borne inférieure crédible (0.9) 0.090 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 9.0% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
