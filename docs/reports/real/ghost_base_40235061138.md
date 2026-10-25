# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-25T23:26:06+00:00 ; durée 119.98 min ; blocs 53087107 → 53090706 (3592 vus)

## Connexion
- Requêtes RPC : 43888 ; erreurs : 5 ; latence p50/p95 : 84.6/1,160.1 ms
- Rafraîchissements d'état : 3592 ; âge des données au dernier bloc : 4.53 s ; changements de frais LP observés (pools à frais dynamiques) : 5153
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 12740 ; cycles déclenchés par événement : 1579 ; avance médiane sur le rafraîchissement multicall : 461 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,337.47 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 533 pools, 308 jetons, 19442 routes
- Par DEX : uniswap_v3 143, aerodrome 214, aerodrome_slipstream 129, pancakeswap_v3 31, uniswap_v2 13, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 192 (rejetés 2) → 597 jetons ; pools candidats 3802 (énumérés 342, par paires 0), mesurés 535, sous le plancher de 10000.0 $ : 2 → gardés 533 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'DAI': 1.0, 'USDC': 1.0, 'WETH': 2341.931042, 'cbBTC': 80341.676682, 'AERO': 0.683871}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 158,306,457 | 2,337.077822 | 53090707 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 17,484,214 | 0.029081 | 53090707 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,224,131 | 0.029134 | 53090707 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,480,273 | 0.000012 | 53090707 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome | WETH/VVV | 3000 | 8,932,216 | 92.797117 | 53090707 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/USDC | 500 | 8,444,563 | 2,331.152591 | 53090707 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | USDC/AERO | 3000 | 7,466,025 | 1.468214 | 53090707 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,019,192 | 0.001651 | 53090707 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | WETH/USDC | 788 | 5,487,257 | 2,330.676130 | 53090707 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,354,311 | 0.029068 | 53090707 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,453,127 | 2,330.227976 | 53090707 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,225,142 | 1.000002 | 53090707 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,818,111 | 35,081.617490 | 53090707 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/USDC | 3000 | 3,781,701 | 2,337.136275 | 53090707 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 3,224,178 | 0.029120 | 53090707 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | USDC/cbBTC | 436 | 2,522,710 | 0.000012 | 53090707 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome_slipstream | WETH/VVV | 2706 | 2,517,175 | 92.775949 | 53090707 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,214,473 | 409.558304 | 53090707 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | WETH/FAI | 10000 | 2,132,536 | 1,218,053.752992 | 53090707 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,901,551 | 0.000000 | 53090707 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,897,121 | 0.000012 | 53090707 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v3 | XDP/USDC | 100 | 1,799,916 | 0.018020 | 53090707 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | USDC/cbBTC | 338 | 1,718,776 | 0.000012 | 53090707 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,718,287 | 0.000012 | 53090707 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | VIRTUAL/WETH | 10000 | 1,569,023 | 0.000265 | 53090707 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,456,681 | 0.826253 | 53090707 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,453,220 | 1.698035 | 53090707 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,431,862 | 0.005526 | 53090707 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v3 | WETH/AERO | 3000 | 1,431,698 | 3,427.992484 | 53090707 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,370,374 | 14,083.179600 | 53090707 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,287,222 | 2,331.068075 | 53090707 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | WETH/AERO | 10000 | 1,254,028 | 3,407.892526 | 53090707 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,242,066 | 0.000267 | 53090707 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | USDC/SEND | 3000 | 1,221,956 | 65.077573 | 53090707 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,166,860 | 35,229,530.381080 | 53090707 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | DRB/WETH | 10000 | 1,160,879 | 0.000000 | 53090707 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | WETH/WELL | 10000 | 1,137,245 | 1,108,395.777449 | 53090707 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,121,949 | 495,973.035662 | 53090707 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | USDC/NOCK | 3000 | 1,087,601 | 52.951661 | 53090707 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome | WETH/EDEL | 7000 | 1,067,895 | 73,420.743697 | 53090707 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,038,582 | 17.050636 | 53090707 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,020,780 | 21,969,859.621726 | 53090707 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | USDC/VVV | 3000 | 971,004 | 0.039706 | 53090707 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/USDC | 10000 | 925,076 | 2,339.202029 | 53090707 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome | WETH/msETH (stable) | 500 | 915,619 | 2.311225 | 53090707 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | WETH/MORPHO | 3000 | 908,443 | 1,130.526353 | 53090707 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | uXRP/WETH | 3000 | 898,400 | 0.000554 | 53090707 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 886,226 | 17.113708 | 53090707 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| uniswap_v3 | WETH/VVV | 10000 | 878,181 | 92.205254 | 53090707 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 874,220 | 18.123599 | 53090707 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v2 | WETH/USDC | 3000 | 847,907 | 2,336.997451 | 53090707 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 804,108 | 0.000008 | 53090707 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | WETH/wstETH | 3000 | 791,431 | 0.803130 | 53090707 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| pancakeswap_v3 | QUID/USDC | 100 | 789,279 | 0.055805 | 53090707 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | weETH_04c0/WETH | 500 | 781,445 | 1.105853 | 53090707 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 745,932 | 0.624357 | 53090707 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 734,375 | 4,782,306.737239 | 53090707 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 719,981 | 0.650490 | 53090707 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/NPC | 3000 | 716,927 | 133,784.161075 | 53090707 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 699,081 | 494,650.057419 | 53090707 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |

## Recherche d'opportunités
- Cycles : 5170 ; routes examinées : 100515140 ; candidats optimisés : 296159 ; net attendu > 0 : 162 ; dernier cycle 593.8 ms
- Rejets (moteur) : {'spread_below_threshold': 98508467, 'liquidity_below_min': 1591924, 'negative_expected_net': 295997, 'unquotable': 113290, 'borrow_bound_too_small': 5170, 'cycle_budget_exhausted': 130}
- Enregistrements de la session : 296159 ; net attendu > 0 : 162 ; simulés (eth_call de la vraie tx) : 13 (ok 3, échec 10) ; étiquettes ghost N+1 : 0/11 positives
- Décisions : {'REJECTED': 296159} ; motifs de rejet : {'below_safety_margin': 142, 'negative_expected_net': 295997, 'p_lower_below_threshold': 138, 'reliability_not_demonstrated': 24, 'sim_below_estimate': 2, 'simulated_net_nonpositive': 2, 'simulation_failed': 10}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53087522 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC | 0.016486 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1666 €) | — | 1.36 | 0.129 (n=327) | REJECTED | below_safety_margin(225<329), p_lower_below_threshold(0.13<0.75) |
| 53087522 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.577121 WETH | 0.000080 WETH | 0.000000 WETH | 0.000003 WETH | 0.000077 WETH (0.1663 €) | — | 1.34 | 0.129 (n=327) | REJECTED | below_safety_margin(77178992824150<115424216900843), p_lower_below_threshold(0.13<0.75) |
| 53087522 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 1,348.818293 USDC | 0.188160 USDC | 0.000000 USDC | 0.007747 USDC | 0.180413 USDC (0.1660 €) | — | 1.34 | 0.129 (n=327) | REJECTED | below_safety_margin(180413<269763), p_lower_below_threshold(0.13<0.75) |
| 53088047 | WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.079575 WETH | 0.000028 WETH | 0.000000 WETH | 0.000003 WETH | 0.000025 WETH (0.0528 €) | — | 3.09 | 0.119 (n=150) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.12<0.75) |
| 53088047 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC | 184.808006 USDC | 0.064257 USDC | 0.000000 USDC | 0.007020 USDC | 0.057237 USDC (0.0527 €) | — | 3.10 | 0.119 (n=150) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 53088047 | WETH→[aerodrome_slipstream]→USDT→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.076234 WETH | 0.000025 WETH | 0.000000 WETH | 0.000003 WETH | 0.000022 WETH (0.0480 €) | — | 2.93 | 0.191 (n=165) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.19<0.75) |
| 53088047 | WETH→[aerodrome_slipstream]→USDT→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.075973 WETH | 0.000025 WETH | 0.000000 WETH | 0.000003 WETH | 0.000022 WETH (0.0479 €) | — | 2.93 | 0.129 (n=327) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.13<0.75) |
| 53088047 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDT→[uniswap_v3]→USDC | 176.937266 USDC | 0.059079 USDC | 0.000000 USDC | 0.007020 USDC | 0.052059 USDC (0.0479 €) | — | 2.94 | 0.191 (n=165) | REJECTED | p_lower_below_threshold(0.19<0.75) |
| 53088047 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDT→[pancakeswap_v3]→USDC | 175.993196 USDC | 0.058953 USDC | 0.000000 USDC | 0.007020 USDC | 0.051933 USDC (0.0478 €) | — | 2.95 | 0.129 (n=327) | REJECTED | p_lower_below_threshold(0.13<0.75) |
| 53088030 | WETH→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.066256 WETH | 0.000016 WETH | 0.000000 WETH | 0.000003 WETH | 0.000013 WETH (0.0279 €) | — | 1.96 | 0.129 (n=327) | REJECTED | below_safety_margin(12983318229092<13251207740808), p_lower_below_threshold(0.13<0.75) |
| 53088030 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→USDC | 153.763631 USDC | 0.037605 USDC | 0.000000 USDC | 0.007377 USDC | 0.030228 USDC (0.0278 €) | — | 1.97 | 0.129 (n=327) | REJECTED | below_safety_margin(30228<30752), p_lower_below_threshold(0.13<0.75) |
| 53087687 | WETH→[aerodrome_slipstream]→LCAP→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.041309 WETH | 0.000015 WETH | 0.000000 WETH | 0.000003 WETH | 0.000012 WETH (0.0248 €) | — | 2.78 | 0.194 (n=162) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.19<0.75) |
| 53087687 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→LCAP→[aerodrome_slipstream]→USDC | 95.748422 USDC | 0.034192 USDC | 0.000000 USDC | 0.007389 USDC | 0.026803 USDC (0.0247 €) | — | 2.80 | 0.194 (n=162) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.19<0.75) |
| 53088047 | WETH→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.057047 WETH | 0.000014 WETH | 0.000000 WETH | 0.000003 WETH | 0.000011 WETH (0.0238 €) | — | 1.94 | 0.129 (n=327) | REJECTED | below_safety_margin(11075952089067<11409358309596), p_lower_below_threshold(0.13<0.75) |
| 53088047 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→cbBTC | 0.001455 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0237 €) | — | 2.20 | 0.129 (n=327) | REJECTED | p_lower_below_threshold(0.13<0.75) |
| 53088047 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 131.570644 USDC | 0.032637 USDC | 0.000000 USDC | 0.007020 USDC | 0.025617 USDC (0.0236 €) | — | 1.95 | 0.129 (n=327) | REJECTED | below_safety_margin(25617<26314), p_lower_below_threshold(0.13<0.75) |
| 53087522 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.292631 WETH | 0.000013 WETH | 0.000000 WETH | 0.000002 WETH | 0.000010 WETH (0.0222 €) | — | 0.35 | 0.022 (n=94) | REJECTED | below_safety_margin(10323917283576<58526124130582), p_lower_below_threshold(0.02<0.75) |
| 53087522 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 683.278827 USDC | 0.029382 USDC | 0.000000 USDC | 0.005257 USDC | 0.024125 USDC (0.0222 €) | — | 0.35 | 0.022 (n=94) | REJECTED | below_safety_margin(24125<136655), p_lower_below_threshold(0.02<0.75) |
| 53088047 | WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.060783 WETH | 0.000012 WETH | 0.000000 WETH | 0.000003 WETH | 0.000009 WETH (0.0198 €) | — | 1.52 | 0.129 (n=327) | REJECTED | below_safety_margin(9228000358070<12156614921570), p_lower_below_threshold(0.13<0.75) |
| 53088047 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC | 141.138985 USDC | 0.028506 USDC | 0.000000 USDC | 0.007020 USDC | 0.021486 USDC (0.0198 €) | — | 1.52 | 0.129 (n=327) | REJECTED | below_safety_margin(21486<28227), p_lower_below_threshold(0.13<0.75) |
| 53087522 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.099667 WETH | 0.000011 WETH | 0.000000 WETH | 0.000002 WETH | 0.000009 WETH (0.0193 €) | — | 0.90 | 0.018 (n=16) | REJECTED | below_safety_margin(8977677215883<19933430314713), reliability_not_demonstrated |
| 53087522 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 230.551841 USDC | 0.026234 USDC | 0.000000 USDC | 0.005257 USDC | 0.020977 USDC (0.0193 €) | — | 0.91 | 0.018 (n=16) | REJECTED | below_safety_margin(20977<46110), reliability_not_demonstrated |
| 53087687 | WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.063207 WETH | 0.000011 WETH | 0.000000 WETH | 0.000003 WETH | 0.000008 WETH (0.0169 €) | — | 1.24 | 0.194 (n=162) | REJECTED | below_safety_margin(7859076637200<12641337951922), p_lower_below_threshold(0.19<0.75) |
| 53087687 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC | 146.745784 USDC | 0.025695 USDC | 0.000000 USDC | 0.007389 USDC | 0.018306 USDC (0.0168 €) | — | 1.25 | 0.194 (n=162) | REJECTED | below_safety_margin(18306<29349), p_lower_below_threshold(0.19<0.75) |
| 53088047 | WETH→[aerodrome_slipstream]→USDT→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.056635 WETH | 0.000011 WETH | 0.000000 WETH | 0.000003 WETH | 0.000008 WETH (0.0163 €) | — | 1.34 | 0.129 (n=327) | REJECTED | below_safety_margin(7571241407882<11326987613384), p_lower_below_threshold(0.13<0.75) |

## Fiabilité et décision
- Observations ghost : 2549 ; taux observé 0.091 ; borne inférieure crédible (0.9) 0.084 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 8.4% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
