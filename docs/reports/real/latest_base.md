# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-25T02:13:19+00:00 ; durée 203.75 min ; blocs 53046410 → 53052524 (6102 vus)

## Connexion
- Requêtes RPC : 72611 ; erreurs : 5 ; latence p50/p95 : 87.1/1,061.3 ms
- Rafraîchissements d'état : 6103 ; âge des données au dernier bloc : 0.94 s ; changements de frais LP observés (pools à frais dynamiques) : 6381
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 4231 ; cycles déclenchés par événement : 414 ; avance médiane sur le rafraîchissement multicall : 372 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,357.39 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 538 pools, 309 jetons, 19504 routes
- Par DEX : uniswap_v3 143, aerodrome 216, aerodrome_slipstream 134, pancakeswap_v3 30, uniswap_v2 12, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 194 (rejetés 2) → 599 jetons ; pools candidats 3810 (énumérés 349, par paires 0), mesurés 540, sous le plancher de 10000.0 $ : 2 → gardés 538 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'DAI': 1.0, 'USDC': 1.0, 'WETH': 2338.582041, 'cbBTC': 80471.362994, 'AERO': 0.693033}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 159,130,101 | 2,357.386366 | 53052524 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 17,353,013 | 0.029218 | 53052524 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,258,765 | 0.029146 | 53052524 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,545,384 | 0.000012 | 53052524 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome | WETH/VVV | 3000 | 9,002,874 | 95.442914 | 53052524 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/USDC | 500 | 8,457,362 | 2,361.947610 | 53052524 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | USDC/AERO | 3000 | 7,933,838 | 1.435390 | 53052524 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,053,207 | 0.001655 | 53052524 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | WETH/USDC | 150 | 5,697,851 | 2,361.100921 | 53052524 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,429,587 | 0.029206 | 53052524 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,476,417 | 2,360.985664 | 53052524 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,245,518 | 0.999824 | 53052524 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,924,143 | 34,172.342905 | 53052524 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/USDC | 3000 | 3,813,351 | 2,357.188015 | 53052524 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 3,275,110 | 0.029163 | 53052524 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | USDC/cbBTC | 424 | 2,581,539 | 0.000012 | 53052524 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome_slipstream | WETH/VVV | 2700 | 2,528,473 | 95.479328 | 53052524 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,236,632 | 409.435657 | 53052524 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | WETH/FAI | 10000 | 2,141,037 | 1,229,085.877653 | 53052524 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,916,064 | 0.000000 | 53052524 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,904,793 | 0.000012 | 53052524 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v3 | XDP/USDC | 100 | 1,791,006 | 0.018054 | 53052524 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,733,234 | 0.000012 | 53052524 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | USDC/cbBTC | 334 | 1,722,134 | 0.000012 | 53052524 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | VIRTUAL/WETH | 10000 | 1,584,611 | 0.000265 | 53052524 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,470,515 | 1.673913 | 53052524 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,457,859 | 0.826892 | 53052524 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,456,202 | 3,387.474793 | 53052524 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,434,660 | 0.005422 | 53052524 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,378,404 | 14,020.421801 | 53052524 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,302,129 | 2,361.951284 | 53052524 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | WETH/AERO | 10000 | 1,286,197 | 3,363.953791 | 53052524 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,252,745 | 0.000267 | 53052524 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | USDC/SEND | 3000 | 1,222,637 | 65.005044 | 53052524 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | DRB/WETH | 10000 | 1,201,748 | 0.000000 | 53052524 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/doginme | 10000 | 1,173,815 | 35,496,022.485857 | 53052524 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | WETH/WELL | 10000 | 1,138,560 | 1,124,766.467505 | 53052524 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,126,574 | 496,267.212770 | 53052524 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | USDC/NOCK | 3000 | 1,092,755 | 52.453171 | 53052524 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome | WETH/EDEL | 7000 | 1,044,831 | 78,033.163477 | 53052524 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,038,353 | 17.059424 | 53052524 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,035,394 | 21,704,291.249444 | 53052524 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | USDC/VVV | 3000 | 964,453 | 0.040512 | 53052524 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 956,436 | 17.131613 | 53052524 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | WETH/msETH (stable) | 500 | 928,806 | 2.309213 | 53052524 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | WETH/USDC | 10000 | 928,744 | 2,340.462681 | 53052524 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 927,765 | 1,107.283162 | 53052524 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | uXRP/WETH | 3000 | 903,422 | 0.000551 | 53052524 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 888,366 | 17.647465 | 53052524 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v3 | WETH/VVV | 10000 | 874,714 | 96.069830 | 53052524 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v2 | WETH/USDC | 3000 | 851,475 | 2,357.457086 | 53052524 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 823,139 | 0.000009 | 53052524 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | weETH_04c0/WETH | 500 | 805,065 | 1.105854 | 53052524 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome | WETH/wstETH | 3000 | 798,176 | 0.803130 | 53052524 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| pancakeswap_v3 | QUID/USDC | 100 | 795,036 | 0.056668 | 53052524 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 751,192 | 4,648,214.803764 | 53052524 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 748,120 | 0.628981 | 53052524 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v3 | TIG/USDC | 10000 | 736,844 | 0.679611 | 53052524 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/NPC | 3000 | 721,592 | 134,298.768775 | 53052524 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 704,738 | 497,815.052013 | 53052524 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |

## Recherche d'opportunités
- Cycles : 6516 ; routes examinées : 127088064 ; candidats optimisés : 369984 ; net attendu > 0 : 379 ; dernier cycle 178.6 ms
- Rejets (moteur) : {'spread_below_threshold': 124199690, 'liquidity_below_min': 2473844, 'negative_expected_net': 369605, 'pool_quarantined': 34200, 'borrow_bound_too_small': 6514, 'unquotable': 3531, 'cycle_budget_exhausted': 301}
- Enregistrements de la session : 369984 ; net attendu > 0 : 379 ; simulés (eth_call de la vraie tx) : 26 (ok 20, échec 6) ; étiquettes ghost N+1 : 2/20 positives
- Décisions : {'REJECTED': 369984} ; motifs de rejet : {'below_safety_margin': 325, 'negative_expected_net': 369605, 'p_lower_below_threshold': 363, 'price_impact': 187, 'reliability_not_demonstrated': 16, 'simulation_failed': 6}

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
- Observations ghost : 2351 ; taux observé 0.095 ; borne inférieure crédible (0.9) 0.088 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 8.8% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ✅ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
