# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-25T03:06:20+00:00 ; durée 256.76 min ; blocs 53046410 → 53054114 (7689 vus)

## Connexion
- Requêtes RPC : 91202 ; erreurs : 5 ; latence p50/p95 : 84.2/1,054.8 ms
- Rafraîchissements d'état : 7690 ; âge des données au dernier bloc : 0.93 s ; changements de frais LP observés (pools à frais dynamiques) : 7861
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 4231 ; cycles déclenchés par événement : 414 ; avance médiane sur le rafraîchissement multicall : 372 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,361.67 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 538 pools, 309 jetons, 19504 routes
- Par DEX : uniswap_v3 143, aerodrome 216, aerodrome_slipstream 134, pancakeswap_v3 30, uniswap_v2 12, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 194 (rejetés 2) → 599 jetons ; pools candidats 3810 (énumérés 349, par paires 0), mesurés 540, sous le plancher de 10000.0 $ : 2 → gardés 538 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'DAI': 1.0, 'USDC': 1.0, 'WETH': 2338.582041, 'cbBTC': 80471.362994, 'AERO': 0.693033}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 159,337,581 | 2,361.672534 | 53054114 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 17,383,395 | 0.029228 | 53054114 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,276,358 | 0.029192 | 53054114 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,537,160 | 0.000012 | 53054114 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome | WETH/VVV | 3000 | 9,017,845 | 95.472496 | 53054114 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/USDC | 500 | 8,455,394 | 2,361.986041 | 53054114 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | USDC/AERO | 3000 | 7,904,185 | 1.441120 | 53054114 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,061,668 | 0.001654 | 53054114 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | WETH/USDC | 150 | 5,704,251 | 2,362.240585 | 53054114 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,450,762 | 0.029223 | 53054114 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,460,257 | 2,362.389469 | 53054114 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,251,746 | 0.999824 | 53054114 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,911,319 | 34,521.977483 | 53054114 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/USDC | 3000 | 3,816,543 | 2,362.116836 | 53054114 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 3,280,030 | 0.029206 | 53054114 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | USDC/cbBTC | 400 | 2,842,279 | 0.000012 | 53054114 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome_slipstream | WETH/VVV | 2718 | 2,532,785 | 95.510538 | 53054114 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,239,026 | 410.260363 | 53054114 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | WETH/FAI | 10000 | 2,144,930 | 1,229,085.877653 | 53054114 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,919,706 | 0.000000 | 53054114 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,906,611 | 0.000012 | 53054114 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v3 | XDP/USDC | 100 | 1,791,707 | 0.018066 | 53054114 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,734,785 | 0.000012 | 53054114 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | USDC/cbBTC | 330 | 1,723,548 | 0.000012 | 53054114 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | VIRTUAL/WETH | 10000 | 1,587,492 | 0.000265 | 53054114 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,470,515 | 1.673913 | 53054114 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,457,859 | 0.826892 | 53054114 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,455,672 | 3,402.607137 | 53054114 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,440,691 | 0.005437 | 53054114 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,379,532 | 14,030.514144 | 53054114 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,303,793 | 2,362.082268 | 53054114 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | WETH/AERO | 10000 | 1,283,045 | 3,378.654049 | 53054114 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,255,021 | 0.000266 | 53054114 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | USDC/SEND | 3000 | 1,222,637 | 65.005044 | 53054114 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | DRB/WETH | 10000 | 1,202,565 | 0.000000 | 53054114 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/doginme | 10000 | 1,176,019 | 35,489,800.089428 | 53054114 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | WETH/WELL | 10000 | 1,140,607 | 1,124,812.504006 | 53054114 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,131,755 | 492,659.290723 | 53054114 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | USDC/NOCK | 3000 | 1,095,636 | 52.177732 | 53054114 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome | WETH/EDEL | 7000 | 1,046,791 | 78,024.212246 | 53054114 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,045,174 | 21,424,118.621904 | 53054114 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,040,308 | 16.972816 | 53054114 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | USDC/VVV | 3000 | 965,844 | 0.040429 | 53054114 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 958,100 | 17.133146 | 53054114 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | WETH/msETH (stable) | 500 | 930,416 | 2.309502 | 53054114 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | WETH/USDC | 10000 | 929,458 | 2,344.953414 | 53054114 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 928,075 | 1,111.715202 | 53054114 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | uXRP/WETH | 3000 | 905,682 | 0.000551 | 53054114 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | USDC/SAPIEN | 4510 | 885,179 | 17.752960 | 53054114 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v3 | WETH/VVV | 10000 | 876,193 | 95.980413 | 53054114 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v2 | WETH/USDC | 3000 | 852,249 | 2,361.406943 | 53054114 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 821,918 | 0.000009 | 53054114 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | weETH_04c0/WETH | 500 | 806,528 | 1.105854 | 53054114 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome | WETH/wstETH | 3000 | 799,627 | 0.803130 | 53054114 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| pancakeswap_v3 | QUID/USDC | 100 | 789,264 | 0.055806 | 53054114 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 752,852 | 4,644,597.685271 | 53054114 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 749,107 | 0.627744 | 53054114 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v3 | TIG/USDC | 10000 | 736,904 | 0.679715 | 53054114 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/NPC | 3000 | 722,904 | 134,298.768775 | 53054114 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 708,783 | 493,449.060368 | 53054114 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |

## Recherche d'opportunités
- Cycles : 8103 ; routes examinées : 158040912 ; candidats optimisés : 469354 ; net attendu > 0 : 405 ; dernier cycle 165.2 ms
- Rejets (moteur) : {'spread_below_threshold': 154552990, 'liquidity_below_min': 2964135, 'negative_expected_net': 468949, 'pool_quarantined': 34200, 'borrow_bound_too_small': 15311, 'unquotable': 4621, 'cycle_budget_exhausted': 301}
- Enregistrements de la session : 469354 ; net attendu > 0 : 405 ; simulés (eth_call de la vraie tx) : 29 (ok 22, échec 7) ; étiquettes ghost N+1 : 4/23 positives
- Décisions : {'REJECTED': 469354} ; motifs de rejet : {'below_safety_margin': 344, 'negative_expected_net': 468949, 'p_lower_below_threshold': 382, 'price_impact': 189, 'reliability_not_demonstrated': 23, 'simulation_failed': 7}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53047711 | USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 124.295542 USDC | 0.024332 USDC | 0.000000 USDC | 0.007121 USDC | 0.017211 USDC (0.0158 €) | — | 1.38 | 0.136 (n=297) | REJECTED | below_safety_margin(17211<24859), p_lower_below_threshold(0.14<0.75) |
| 53047711 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH | 0.053068 WETH | 0.000010 WETH | 0.000000 WETH | 0.000003 WETH | 0.000007 WETH (0.0158 €) | — | 1.38 | 0.136 (n=297) | REJECTED | below_safety_margin(7306780316630<10613623259965), p_lower_below_threshold(0.14<0.75) |
| 53047711 | USDC→[sushiswap_v3]→WETH→[pancakeswap_v3]→USDC | 88.907625 USDC | 0.019669 USDC | 0.000000 USDC | 0.005321 USDC | 0.014348 USDC (0.0132 €) | — | 1.61 | 0.024 (n=86) | REJECTED | below_safety_margin(14348<17781), p_lower_below_threshold(0.02<0.75) |
| 53047711 | WETH→[pancakeswap_v3]→USDC→[sushiswap_v3]→WETH | 0.037807 WETH | 0.000008 WETH | 0.000000 WETH | 0.000002 WETH | 0.000006 WETH (0.0132 €) | — | 1.61 | 0.024 (n=86) | REJECTED | below_safety_margin(6092038538017<7561415945893), p_lower_below_threshold(0.02<0.75) |
| 53047220 | USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→WETH→[sushiswap_v3]→USDC | 14.407409 USDC | 0.018464 USDC | 0.000000 USDC | 0.007026 USDC | 0.011438 USDC (0.0105 €) | — | 7.94 | 0.136 (n=132) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 53047220 | WETH→[sushiswap_v3]→USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→WETH | 0.006147 WETH | 0.000008 WETH | 0.000000 WETH | 0.000003 WETH | 0.000005 WETH (0.0105 €) | 0.000005 WETH | 7.95 | 0.136 (n=132) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 53047220 | USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→USDC | 14.532804 USDC | 0.018415 USDC | 0.000000 USDC | 0.007026 USDC | 0.011389 USDC (0.0105 €) | — | 7.84 | 0.136 (n=132) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 53047220 | WETH→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→WETH | 0.006271 WETH | 0.000008 WETH | 0.000000 WETH | 0.000003 WETH | 0.000005 WETH (0.0105 €) | 0.000005 WETH | 7.76 | 0.136 (n=132) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 53047220 | USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 14.476319 USDC | 0.018115 USDC | 0.000000 USDC | 0.007026 USDC | 0.011089 USDC (0.0102 €) | — | 7.66 | 0.090 (n=245) | REJECTED | p_lower_below_threshold(0.09<0.75) |
| 53047220 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→WETH | 0.006194 WETH | 0.000008 WETH | 0.000000 WETH | 0.000003 WETH | 0.000005 WETH (0.0102 €) | 0.000005 WETH | 7.65 | 0.090 (n=245) | REJECTED | p_lower_below_threshold(0.09<0.75) |
| 53047220 | USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 14.352394 USDC | 0.017898 USDC | 0.000000 USDC | 0.007026 USDC | 0.010872 USDC (0.0100 €) | — | 7.58 | 0.136 (n=132) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 53047220 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→WETH | 0.006127 WETH | 0.000008 WETH | 0.000000 WETH | 0.000003 WETH | 0.000005 WETH (0.0100 €) | — | 7.58 | 0.136 (n=132) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 53047220 | USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 14.283482 USDC | 0.017749 USDC | 0.000000 USDC | 0.007026 USDC | 0.010723 USDC (0.0099 €) | — | 7.51 | 0.090 (n=245) | REJECTED | p_lower_below_threshold(0.09<0.75) |
| 53047220 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→WETH | 0.006120 WETH | 0.000008 WETH | 0.000000 WETH | 0.000003 WETH | 0.000005 WETH (0.0099 €) | — | 7.48 | 0.090 (n=245) | REJECTED | p_lower_below_threshold(0.09<0.75) |
| 53047220 | USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 14.154246 USDC | 0.017507 USDC | 0.000000 USDC | 0.007026 USDC | 0.010481 USDC (0.0096 €) | — | 7.40 | 0.136 (n=132) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 53047220 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→WETH | 0.006091 WETH | 0.000007 WETH | 0.000000 WETH | 0.000003 WETH | 0.000004 WETH (0.0096 €) | — | 7.35 | 0.136 (n=132) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 53047724 | cbBTC→[aerodrome]→VIRTUAL→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC | 0.000469 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0089 €) | 0.000000 cbBTC | 2.56 | 0.179 (n=34) | REJECTED | p_lower_below_threshold(0.18<0.75) |
| 53047724 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome]→VIRTUAL→[aerodrome_slipstream]→WETH | 0.018468 WETH | 0.000007 WETH | 0.000000 WETH | 0.000003 WETH | 0.000004 WETH (0.0088 €) | 0.000004 WETH | 2.21 | 0.179 (n=34) | REJECTED | p_lower_below_threshold(0.18<0.75) |
| 53047723 | USDC→[uniswap_v3]→AAVE→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 41.624286 USDC | 0.016676 USDC | 0.000000 USDC | 0.007267 USDC | 0.009409 USDC (0.0087 €) | — | 2.26 | 0.135 (n=299) | REJECTED | p_lower_below_threshold(0.13<0.75) |
| 53047723 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→AAVE→[pancakeswap_v3]→WETH | 0.017679 WETH | 0.000007 WETH | 0.000000 WETH | 0.000003 WETH | 0.000004 WETH (0.0086 €) | 0.000004 WETH | 2.25 | 0.135 (n=299) | REJECTED | p_lower_below_threshold(0.13<0.75) |
| 53047220 | USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→USDC | 12.633464 USDC | 0.016053 USDC | 0.000000 USDC | 0.007026 USDC | 0.009027 USDC (0.0083 €) | — | 7.15 | 0.136 (n=132) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 53047220 | WETH→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→WETH | 0.005416 WETH | 0.000007 WETH | 0.000000 WETH | 0.000003 WETH | 0.000004 WETH (0.0083 €) | — | 7.12 | 0.136 (n=132) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 53047723 | USDC→[aerodrome]→AUKI→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 18.888291 USDC | 0.015345 USDC | 0.000000 USDC | 0.006933 USDC | 0.008412 USDC (0.0077 €) | — | 4.45 | 0.015 (n=54) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 53047723 | WETH→[pancakeswap_v3]→USDC→[aerodrome]→AUKI→[pancakeswap_v3]→WETH | 0.008075 WETH | 0.000007 WETH | 0.000000 WETH | 0.000003 WETH | 0.000004 WETH (0.0077 €) | 0.000004 WETH | 4.41 | 0.015 (n=54) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 53048351 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 13.386650 USDC | 0.015213 USDC | 0.000000 USDC | 0.007067 USDC | 0.008146 USDC (0.0075 €) | — | 6.09 | 0.133 (n=134) | REJECTED | p_lower_below_threshold(0.13<0.75) |

## Fiabilité et décision
- Observations ghost : 2354 ; taux observé 0.096 ; borne inférieure crédible (0.9) 0.088 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 8.8% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ✅ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
