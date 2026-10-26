# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-26T08:27:49+00:00 ; durée 326.46 min ; blocs 53097164 → 53106957 (9752 vus)

## Connexion
- Requêtes RPC : 115823 ; erreurs : 10 ; latence p50/p95 : 88.4/1,061.7 ms
- Rafraîchissements d'état : 9753 ; âge des données au dernier bloc : 2.07 s ; changements de frais LP observés (pools à frais dynamiques) : 15037
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 16418 ; cycles déclenchés par événement : 1008 ; avance médiane sur le rafraîchissement multicall : 349 ms
- Gaz : base fee 0.005025 gwei ; prix ETH (pool le plus profond) : 2,314.89 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 524 pools, 302 jetons, 19436 routes
- Par DEX : uniswap_v3 140, aerodrome 213, aerodrome_slipstream 125, pancakeswap_v3 31, uniswap_v2 12, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 189 (rejetés 2) → 594 jetons ; pools candidats 3787 (énumérés 337, par paires 0), mesurés 526, sous le plancher de 10000.0 $ : 2 → gardés 524 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2299.668664, 'cbBTC': 79491.484, 'AERO': 0.669155}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 157,132,957 | 2,314.892336 | 53106957 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 17,418,103 | 0.028970 | 53106957 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,148,467 | 0.028978 | 53106957 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,476,429 | 0.000012 | 53106957 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome | WETH/VVV | 3000 | 8,760,427 | 94.618085 | 53106957 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/USDC | 500 | 8,295,415 | 2,320.701556 | 53106957 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | USDC/AERO | 3000 | 7,163,632 | 1.493232 | 53106957 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,963,028 | 0.001645 | 53106957 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | WETH/USDC | 150 | 5,380,577 | 2,321.498007 | 53106957 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,346,291 | 0.028981 | 53106957 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,458,245 | 2,321.614834 | 53106957 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,206,432 | 0.998980 | 53106957 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,814,067 | 34,480.318705 | 53106957 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/USDC | 3000 | 3,755,558 | 2,314.672319 | 53106957 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 3,186,383 | 0.028970 | 53106957 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2787 | 2,477,021 | 94.599159 | 53106957 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | USDC/cbBTC | 600 | 2,476,754 | 0.000012 | 53106957 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,186,445 | 412.058859 | 53106957 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | WETH/FAI | 10000 | 2,118,827 | 1,210,151.770244 | 53106957 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,890,658 | 0.000013 | 53106957 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,884,451 | 0.000000 | 53106957 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,797,827 | 0.018091 | 53106957 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,711,254 | 0.000012 | 53106957 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | USDC/cbBTC | 374 | 1,695,608 | 0.000012 | 53106957 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | VIRTUAL/WETH | 10000 | 1,553,064 | 0.000265 | 53106957 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,455,113 | 0.825625 | 53106957 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,453,220 | 1.698035 | 53106957 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,429,707 | 0.005516 | 53106957 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v3 | WETH/AERO | 3000 | 1,414,175 | 3,458.868070 | 53106957 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,357,168 | 14,227.057150 | 53106957 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,232,831 | 2,320.565780 | 53106957 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | WETH/AERO | 10000 | 1,231,007 | 3,469.603693 | 53106957 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,229,947 | 0.000264 | 53106957 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | USDC/SEND | 3000 | 1,220,823 | 65.198383 | 53106957 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | DRB/WETH | 10000 | 1,154,796 | 0.000000 | 53106957 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/doginme | 10000 | 1,153,005 | 35,473,150.980825 | 53106957 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | WETH/WELL | 10000 | 1,126,723 | 1,107,491.218378 | 53106957 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,106,457 | 499,913.893915 | 53106957 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | USDC/NOCK | 3000 | 1,068,560 | 54.855711 | 53106957 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome | WETH/EDEL | 7000 | 1,063,514 | 72,604.066496 | 53106957 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,039,217 | 20,973,863.028263 | 53106957 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,031,366 | 17.377864 | 53106957 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | USDC/VVV | 3000 | 960,838 | 0.040756 | 53106957 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/USDC | 10000 | 921,663 | 2,298.594588 | 53106957 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome | WETH/msETH (stable) | 500 | 906,109 | 2.308521 | 53106957 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | uXRP/WETH | 3000 | 887,097 | 0.000551 | 53106957 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 873,129 | 17.211162 | 53106957 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| uniswap_v3 | WETH/MORPHO | 3000 | 871,145 | 1,151.721990 | 53106957 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 868,928 | 18.306508 | 53106957 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v3 | WETH/VVV | 10000 | 863,478 | 94.428498 | 53106957 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v2 | WETH/USDC | 3000 | 843,867 | 2,314.773711 | 53106957 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| pancakeswap_v3 | QUID/USDC | 100 | 814,347 | 0.059619 | 53106957 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 794,392 | 0.000008 | 53106957 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | WETH/wstETH | 3000 | 783,783 | 0.803142 | 53106957 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| aerodrome | weETH_04c0/WETH | 500 | 773,929 | 1.105941 | 53106957 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 742,593 | 0.612339 | 53106957 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 728,473 | 4,766,918.371116 | 53106957 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 711,114 | 0.635188 | 53106957 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/NPC | 3000 | 698,859 | 138,096.107418 | 53106957 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | WETH/BRETT | 2126 | 689,208 | 503,224.001581 | 53106957 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |

## Recherche d'opportunités
- Cycles : 10760 ; routes examinées : 209131360 ; candidats optimisés : 660958 ; net attendu > 0 : 403 ; dernier cycle 372.6 ms
- Rejets (moteur) : {'spread_below_threshold': 205055407, 'liquidity_below_min': 3172078, 'negative_expected_net': 660555, 'unquotable': 231872, 'borrow_bound_too_small': 10760, 'cycle_budget_exhausted': 285}
- Enregistrements de la session : 660958 ; net attendu > 0 : 403 ; simulés (eth_call de la vraie tx) : 24 (ok 22, échec 2) ; étiquettes ghost N+1 : 8/19 positives
- Décisions : {'REJECTED': 660958} ; motifs de rejet : {'below_safety_margin': 350, 'negative_expected_net': 660555, 'p_lower_below_threshold': 354, 'reliability_not_demonstrated': 49, 'sim_below_estimate': 3, 'simulation_failed': 2, 'stale_data': 5}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53106337 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.018825 WETH | 0.000057 WETH | 0.000000 WETH | 0.000003 WETH | 0.000054 WETH (0.1153 €) | 0.000054 WETH | 28.79 | 0.000 (n=21) | REJECTED | reliability_not_demonstrated |
| 53106337 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 43.244847 USDC | 0.131901 USDC | 0.000000 USDC | 0.006949 USDC | 0.124952 USDC (0.1150 €) | — | 28.89 | 0.000 (n=21) | REJECTED | reliability_not_demonstrated |
| 53106337 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.018705 WETH | 0.000057 WETH | 0.000000 WETH | 0.000003 WETH | 0.000054 WETH (0.1145 €) | 0.000054 WETH | 28.79 | 0.000 (n=29) | REJECTED | reliability_not_demonstrated |
| 53106337 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 42.986184 USDC | 0.131091 USDC | 0.000000 USDC | 0.006949 USDC | 0.124142 USDC (0.1142 €) | — | 28.88 | 0.000 (n=29) | REJECTED | reliability_not_demonstrated |
| 53106337 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.017671 WETH | 0.000054 WETH | 0.000000 WETH | 0.000003 WETH | 0.000051 WETH (0.1090 €) | 0.000051 WETH | 29.00 | 0.000 (n=29) | REJECTED | reliability_not_demonstrated |
| 53106337 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 40.833840 USDC | 0.125123 USDC | 0.000000 USDC | 0.006949 USDC | 0.118174 USDC (0.1087 €) | — | 28.94 | 0.000 (n=29) | REJECTED | reliability_not_demonstrated |
| 53106337 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.017318 WETH | 0.000049 WETH | 0.000000 WETH | 0.000003 WETH | 0.000046 WETH (0.0969 €) | — | 26.30 | 0.000 (n=29) | REJECTED | reliability_not_demonstrated |
| 53106337 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 39.906932 USDC | 0.112005 USDC | 0.000000 USDC | 0.006949 USDC | 0.105056 USDC (0.0967 €) | — | 26.33 | 0.000 (n=29) | REJECTED | reliability_not_demonstrated |
| 53106337 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.017207 WETH | 0.000048 WETH | 0.000000 WETH | 0.000003 WETH | 0.000045 WETH (0.0958 €) | — | 26.17 | 0.000 (n=21) | REJECTED | reliability_not_demonstrated |
| 53106337 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 39.617751 USDC | 0.110831 USDC | 0.000000 USDC | 0.006949 USDC | 0.103882 USDC (0.0956 €) | — | 26.22 | 0.000 (n=21) | REJECTED | reliability_not_demonstrated |
| 53106337 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[sushiswap_v3]→WETH | 0.016346 WETH | 0.000045 WETH | 0.000000 WETH | 0.000003 WETH | 0.000042 WETH (0.0885 €) | — | 25.47 | 0.000 (n=29) | REJECTED | reliability_not_demonstrated |
| 53106337 | USDC→[sushiswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 37.580775 USDC | 0.103021 USDC | 0.000000 USDC | 0.006949 USDC | 0.096072 USDC (0.0884 €) | — | 25.56 | 0.000 (n=29) | REJECTED | reliability_not_demonstrated |
| 53106337 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.016525 WETH | 0.000044 WETH | 0.000000 WETH | 0.000003 WETH | 0.000041 WETH (0.0874 €) | — | 24.87 | 0.000 (n=29) | REJECTED | reliability_not_demonstrated |
| 53106337 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 38.052653 USDC | 0.101781 USDC | 0.000000 USDC | 0.006949 USDC | 0.094832 USDC (0.0872 €) | — | 24.92 | 0.000 (n=29) | REJECTED | reliability_not_demonstrated |
| 53098029 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.142261 WETH | 0.000026 WETH | 0.000000 WETH | 0.000002 WETH | 0.000024 WETH (0.0501 €) | — | 1.66 | 0.022 (n=94) | REJECTED | below_safety_margin(23566127176808<28452265992404), p_lower_below_threshold(0.02<0.75) |
| 53098029 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 327.219771 USDC | 0.059835 USDC | 0.000000 USDC | 0.005543 USDC | 0.054292 USDC (0.0499 €) | — | 1.66 | 0.022 (n=94) | REJECTED | below_safety_margin(54292<65443), p_lower_below_threshold(0.02<0.75) |
| 53098029 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.098833 WETH | 0.000012 WETH | 0.000000 WETH | 0.000003 WETH | 0.000009 WETH (0.0198 €) | — | 0.94 | 0.129 (n=342) | REJECTED | below_safety_margin(9338811363951<19766565681607), p_lower_below_threshold(0.13<0.75) |
| 53098029 | cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.002899 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0198 €) | — | 0.93 | 0.129 (n=342) | REJECTED | below_safety_margin(27<57), p_lower_below_threshold(0.13<0.75) |
| 53098029 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 192.423773 USDC | 0.028144 USDC | 0.000000 USDC | 0.006948 USDC | 0.021196 USDC (0.0195 €) | — | 1.10 | 0.129 (n=342) | REJECTED | below_safety_margin(21196<38484), p_lower_below_threshold(0.13<0.75) |
| 53098029 | cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.002446 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0191 €) | — | 1.06 | 0.129 (n=342) | REJECTED | below_safety_margin(26<48), p_lower_below_threshold(0.13<0.75) |
| 53098029 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.093531 WETH | 0.000012 WETH | 0.000000 WETH | 0.000003 WETH | 0.000009 WETH (0.0189 €) | — | 0.95 | 0.129 (n=342) | REJECTED | below_safety_margin(8880679294217<18706197028796), p_lower_below_threshold(0.13<0.75) |
| 53098029 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 208.572973 USDC | 0.027344 USDC | 0.000000 USDC | 0.006948 USDC | 0.020396 USDC (0.0188 €) | — | 0.98 | 0.129 (n=342) | REJECTED | below_safety_margin(20396<41714), p_lower_below_threshold(0.13<0.75) |
| 53098029 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.002900 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0183 €) | — | 0.86 | 0.129 (n=342) | REJECTED | below_safety_margin(25<57), p_lower_below_threshold(0.13<0.75) |
| 53098029 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.098785 WETH | 0.000012 WETH | 0.000000 WETH | 0.000003 WETH | 0.000009 WETH (0.0182 €) | — | 0.87 | 0.129 (n=342) | REJECTED | below_safety_margin(8567298155534<19757042730904), p_lower_below_threshold(0.13<0.75) |
| 53098029 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 195.851277 USDC | 0.026645 USDC | 0.000000 USDC | 0.006948 USDC | 0.019697 USDC (0.0181 €) | — | 1.01 | 0.129 (n=342) | REJECTED | below_safety_margin(19697<39170), p_lower_below_threshold(0.13<0.75) |

## Fiabilité et décision
- Observations ghost : 2607 ; taux observé 0.095 ; borne inférieure crédible (0.9) 0.088 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 8.8% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ✅ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
