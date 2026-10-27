# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-27T19:34:56+00:00 ; durée 76.61 min ; blocs 53167873 → 53170173 (2269 vus)

## Connexion
- Requêtes RPC : 26766 ; erreurs : 195 ; latence p50/p95 : 187.2/891.8 ms
- Rafraîchissements d'état : 2269 ; âge des données au dernier bloc : 2.33 s ; changements de frais LP observés (pools à frais dynamiques) : 2737
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 11660 ; cycles déclenchés par événement : 1451 ; avance médiane sur le rafraîchissement multicall : 456 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,344.66 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 519 pools, 301 jetons, 18846 routes
- Par DEX : uniswap_v3 145, aerodrome 211, aerodrome_slipstream 120, pancakeswap_v3 28, uniswap_v2 12, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 185 (rejetés 2) → 590 jetons ; pools candidats 3771 (énumérés 330, par paires 0), mesurés 521, sous le plancher de 10000.0 $ : 2 → gardés 519 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDbC': 1.0, 'USDC': 1.0, 'WETH': 2347.170972, 'cbBTC': 80539.356341, 'AERO': 0.69796}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 157,338,124 | 2,344.660573 | 53170173 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,611,318 | 0.029048 | 53170173 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,190,027 | 0.029106 | 53170173 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,629,567 | 0.000012 | 53170173 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome | WETH/VVV | 3000 | 8,645,308 | 90.074956 | 53170173 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/USDC | 500 | 8,426,512 | 2,340.691149 | 53170173 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,020,842 | 0.001638 | 53170173 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 6,974,148 | 1.438143 | 53170173 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,733,466 | 0.029059 | 53170173 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/USDC | 150 | 5,087,838 | 2,341.484375 | 53170173 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,538,985 | 2,341.668512 | 53170173 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,251,656 | 0.998745 | 53170173 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,732,342 | 36,938.864883 | 53170173 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,964,687 | 0.029103 | 53170173 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2700 | 2,579,829 | 90.090964 | 53170173 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | WETH/USDC | 3000 | 2,364,922 | 2,345.610629 | 53170173 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | USDC/cbBTC | 412 | 2,193,647 | 0.000012 | 53170173 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome | WETH/FAI | 10000 | 2,142,820 | 1,213,829.665615 | 53170173 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | XDP/USDC | 100 | 1,832,030 | 0.018750 | 53170173 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,819,738 | 0.000000 | 53170173 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,787,724 | 397.813100 | 53170173 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | USDC/cbBTC | 334 | 1,697,002 | 0.000012 | 53170173 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,688,345 | 0.000012 | 53170173 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,683,141 | 0.000012 | 53170173 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,525,127 | 0.005869 | 53170173 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,461,062 | 0.826538 | 53170173 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,453,146 | 1.698043 | 53170173 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | WETH/AERO | 3000 | 1,452,889 | 3,365.186409 | 53170173 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,391,761 | 13,682.948364 | 53170173 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,252,382 | 0.000268 | 53170173 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,250,797 | 2,340.637537 | 53170173 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | WETH/AERO | 10000 | 1,202,536 | 3,341.209433 | 53170173 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | USDC/SEND | 3000 | 1,201,201 | 67.345844 | 53170173 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome | VIRTUAL/WETH | 10000 | 1,185,115 | 0.000266 | 53170173 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | WETH/doginme | 10000 | 1,164,977 | 35,762,515.176186 | 53170173 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | WETH/WELL | 10000 | 1,162,210 | 1,067,251.779907 | 53170173 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | DRB/WETH | 10000 | 1,119,980 | 0.000000 | 53170173 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,111,494 | 507,612.581727 | 53170173 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | WETH/EDEL | 7000 | 1,077,708 | 72,326.481458 | 53170173 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,046,677 | 21,236,715.146711 | 53170173 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,044,892 | 16.776109 | 53170173 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | USDC/NOCK | 3000 | 1,042,328 | 57.618623 | 53170173 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | USDC/VVV | 3000 | 1,038,239 | 0.038471 | 53170173 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/USDC | 10000 | 943,724 | 2,331.655283 | 53170173 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 911,727 | 1,084.873095 | 53170173 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | uXRP/WETH | 3000 | 906,616 | 0.000560 | 53170173 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| uniswap_v3 | WETH/VVV | 10000 | 900,692 | 90.257348 | 53170173 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome | WETH/msETH (stable) | 500 | 885,613 | 2.312204 | 53170173 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 880,667 | 17.923897 | 53170173 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v2 | WETH/USDC | 3000 | 848,786 | 2,345.123097 | 53170173 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 837,271 | 17.692889 | 53170173 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 808,709 | 0.000009 | 53170173 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| pancakeswap_v3 | QUID/USDC | 100 | 802,270 | 0.057751 | 53170173 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 793,843 | 0.803179 | 53170173 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 757,525 | 4,522,547.673039 | 53170173 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 751,390 | 0.627265 | 53170173 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/NPC | 3000 | 701,197 | 140,739.756940 | 53170173 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 692,632 | 506,890.810022 | 53170173 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | TIG/USDC | 10000 | 684,508 | 0.589719 | 53170173 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 674,508 | 0.108864 | 53170173 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |

## Recherche d'opportunités
- Cycles : 3719 ; routes examinées : 70088274 ; candidats optimisés : 220755 ; net attendu > 0 : 80 ; dernier cycle 142.5 ms
- Rejets (moteur) : {'spread_below_threshold': 68950228, 'liquidity_below_min': 871903, 'negative_expected_net': 220675, 'borrow_bound_too_small': 45201, 'cycle_budget_exhausted': 187}
- Enregistrements de la session : 220755 ; net attendu > 0 : 80 ; simulés (eth_call de la vraie tx) : 0 (ok 0, échec 0) ; étiquettes ghost N+1 : 0/0 positives
- Décisions : {'REJECTED': 220755} ; motifs de rejet : {'below_safety_margin': 80, 'negative_expected_net': 220675, 'p_lower_below_threshold': 80}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53167952 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 19.270545 USDC | 0.008635 USDC | 0.000000 USDC | 0.005288 USDC | 0.003347 USDC (0.0031 €) | — | 1.74 | 0.020 (n=106) | REJECTED | below_safety_margin(3347<3854), p_lower_below_threshold(0.02<0.75) |
| 53167952 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 19.270545 USDC | 0.008635 USDC | 0.000000 USDC | 0.005288 USDC | 0.003347 USDC (0.0031 €) | — | 1.74 | 0.020 (n=106) | REJECTED | below_safety_margin(3347<3854), p_lower_below_threshold(0.02<0.75) |
| 53169993 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.004364 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0015 €) | — | 1.55 | 0.165 (n=196) | REJECTED | below_safety_margin(677965309094<872712089733), p_lower_below_threshold(0.16<0.75) |
| 53169993 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.004364 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0015 €) | — | 1.55 | 0.165 (n=196) | REJECTED | below_safety_margin(677965309094<872712089733), p_lower_below_threshold(0.16<0.75) |
| 53169993 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 10.124987 USDC | 0.008638 USDC | 0.000000 USDC | 0.007062 USDC | 0.001576 USDC (0.0014 €) | — | 1.56 | 0.165 (n=196) | REJECTED | below_safety_margin(1576<2024), p_lower_below_threshold(0.16<0.75) |
| 53169993 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 10.124987 USDC | 0.008638 USDC | 0.000000 USDC | 0.007062 USDC | 0.001576 USDC (0.0014 €) | — | 1.56 | 0.165 (n=196) | REJECTED | below_safety_margin(1576<2024), p_lower_below_threshold(0.16<0.75) |
| 53169993 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.004228 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0010 €) | — | 1.08 | 0.127 (n=391) | REJECTED | below_safety_margin(455079711985<845502890264), p_lower_below_threshold(0.13<0.75) |
| 53169993 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.004228 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0010 €) | — | 1.08 | 0.127 (n=391) | REJECTED | below_safety_margin(455079711985<845502890264), p_lower_below_threshold(0.13<0.75) |
| 53169993 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 9.846211 USDC | 0.008116 USDC | 0.000000 USDC | 0.007062 USDC | 0.001054 USDC (0.0010 €) | — | 1.07 | 0.127 (n=391) | REJECTED | below_safety_margin(1054<1969), p_lower_below_threshold(0.13<0.75) |
| 53169993 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 9.846211 USDC | 0.008116 USDC | 0.000000 USDC | 0.007062 USDC | 0.001054 USDC (0.0010 €) | — | 1.07 | 0.127 (n=391) | REJECTED | below_safety_margin(1054<1969), p_lower_below_threshold(0.13<0.75) |
| 53170026 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.004244 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0010 €) | — | 1.06 | 0.127 (n=391) | REJECTED | below_safety_margin(447786998833<848858725266), p_lower_below_threshold(0.13<0.75) |
| 53170024 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.004244 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0010 €) | — | 1.06 | 0.127 (n=391) | REJECTED | below_safety_margin(447786852696<848858725296), p_lower_below_threshold(0.13<0.75) |
| 53170024 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.004244 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0010 €) | — | 1.06 | 0.127 (n=391) | REJECTED | below_safety_margin(447786852696<848858725296), p_lower_below_threshold(0.13<0.75) |
| 53170025 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.004244 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0010 €) | — | 1.06 | 0.127 (n=391) | REJECTED | below_safety_margin(447786852696<848858725296), p_lower_below_threshold(0.13<0.75) |
| 53170026 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.004244 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0010 €) | — | 1.06 | 0.127 (n=391) | REJECTED | below_safety_margin(447786852696<848858725296), p_lower_below_threshold(0.13<0.75) |
| 53170024 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 9.904307 USDC | 0.008097 USDC | 0.000000 USDC | 0.007061 USDC | 0.001036 USDC (0.0010 €) | — | 1.05 | 0.127 (n=391) | REJECTED | below_safety_margin(1036<1980), p_lower_below_threshold(0.13<0.75) |
| 53170024 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 9.904307 USDC | 0.008097 USDC | 0.000000 USDC | 0.007061 USDC | 0.001036 USDC (0.0010 €) | — | 1.05 | 0.127 (n=391) | REJECTED | below_safety_margin(1036<1980), p_lower_below_threshold(0.13<0.75) |
| 53170025 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 9.904307 USDC | 0.008097 USDC | 0.000000 USDC | 0.007061 USDC | 0.001036 USDC (0.0010 €) | — | 1.05 | 0.127 (n=391) | REJECTED | below_safety_margin(1036<1980), p_lower_below_threshold(0.13<0.75) |
| 53170026 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 9.904307 USDC | 0.008097 USDC | 0.000000 USDC | 0.007061 USDC | 0.001036 USDC (0.0010 €) | — | 1.05 | 0.127 (n=391) | REJECTED | below_safety_margin(1036<1980), p_lower_below_threshold(0.13<0.75) |
| 53170026 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 9.904307 USDC | 0.008097 USDC | 0.000000 USDC | 0.007061 USDC | 0.001036 USDC (0.0010 €) | — | 1.05 | 0.127 (n=391) | REJECTED | below_safety_margin(1036<1980), p_lower_below_threshold(0.13<0.75) |
| 53170024 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.004209 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0009 €) | — | 1.03 | 0.165 (n=196) | REJECTED | below_safety_margin(432526044706<841831207897), p_lower_below_threshold(0.16<0.75) |
| 53170024 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.004209 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0009 €) | — | 1.03 | 0.165 (n=196) | REJECTED | below_safety_margin(432526044706<841831207897), p_lower_below_threshold(0.16<0.75) |
| 53170024 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 9.733536 USDC | 0.008060 USDC | 0.000000 USDC | 0.007061 USDC | 0.000999 USDC (0.0009 €) | — | 1.03 | 0.165 (n=196) | REJECTED | below_safety_margin(999<1946), p_lower_below_threshold(0.16<0.75) |
| 53170024 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 9.733536 USDC | 0.008060 USDC | 0.000000 USDC | 0.007061 USDC | 0.000999 USDC (0.0009 €) | — | 1.03 | 0.165 (n=196) | REJECTED | below_safety_margin(999<1946), p_lower_below_threshold(0.16<0.75) |
| 53170026 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.004170 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0009 €) | — | 0.97 | 0.165 (n=196) | REJECTED | below_safety_margin(402750342811<833975971991), p_lower_below_threshold(0.16<0.75) |

## Fiabilité et décision
- Observations ghost : 2856 ; taux observé 0.090 ; borne inférieure crédible (0.9) 0.084 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 8.4% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
