# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-29T19:16:16+00:00 ; durée 243.49 min ; blocs 53248705 → 53256009 (7202 vus)

## Connexion
- Requêtes RPC : 87130 ; erreurs : 100 ; latence p50/p95 : 263.8/1,147.7 ms
- Rafraîchissements d'état : 7202 ; âge des données au dernier bloc : 2.44 s ; changements de frais LP observés (pools à frais dynamiques) : 14217
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 108027 ; cycles déclenchés par événement : 7128 ; avance médiane sur le rafraîchissement multicall : 645 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,329.09 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 517 pools, 297 jetons, 19072 routes
- Par DEX : uniswap_v3 146, aerodrome_slipstream 120, aerodrome 208, pancakeswap_v3 29, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 182 (rejetés 2) → 587 jetons ; pools candidats 3756 (énumérés 327, par paires 0), mesurés 519, sous le plancher de 10000.0 $ : 2 → gardés 517 (max 1500) ; prix des hubs : {'USDC': 1.0, 'USDbC': 1.0, 'DAI': 1.0, 'WETH': 2355.875591, 'cbBTC': 81334.783192, 'AERO': 0.704357}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 157,847,622 | 2,329.091388 | 53256009 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,494,593 | 0.028821 | 53256009 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,764,138 | 0.000012 | 53256009 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,466,289 | 0.028893 | 53256009 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| aerodrome | WETH/VVV | 3000 | 8,371,336 | 93.812638 | 53256009 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/USDC | 500 | 8,293,027 | 2,326.190445 | 53256009 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,998,717 | 0.001624 | 53256009 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 6,352,315 | 1.476943 | 53256009 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,434,832 | 0.028810 | 53256009 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/USDC | 150 | 4,435,049 | 2,325.407752 | 53256009 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,408,390 | 2,325.602052 | 53256009 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,254,977 | 0.998879 | 53256009 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,668,067 | 37,733.513506 | 53256009 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2505 | 2,887,977 | 0.028879 | 53256009 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2700 | 2,463,593 | 93.861059 | 53256009 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | WETH/FAI | 10000 | 2,122,162 | 1,221,195.064323 | 53256009 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 424 | 2,111,547 | 0.000012 | 53256009 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome | WETH/USDC | 3000 | 1,817,101 | 2,332.301710 | 53256009 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,787,366 | 392.266782 | 53256009 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | XDP/USDC | 100 | 1,783,628 | 0.018513 | 53256009 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,772,474 | 0.000000 | 53256009 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,718,319 | 0.000012 | 53256009 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,713,463 | 0.000012 | 53256009 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | USDC/cbBTC | 334 | 1,608,543 | 0.000012 | 53256009 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,514,127 | 1.588199 | 53256009 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,457,136 | 0.826856 | 53256009 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,431,347 | 3,434.184655 | 53256009 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,401,389 | 0.005345 | 53256009 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,397,322 | 13,617.742210 | 53256009 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,262,546 | 2,326.126338 | 53256009 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,230,058 | 0.000262 | 53256009 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | USDC/SEND | 3000 | 1,181,789 | 69.576491 | 53256009 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,145,967 | 36,873,054.638385 | 53256009 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | WETH/WELL | 10000 | 1,138,258 | 1,097,185.920646 | 53256009 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,112,271 | 497,631.356518 | 53256009 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,067,739 | 0.000000 | 53256009 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | USDC/VVV | 3000 | 1,064,429 | 0.040347 | 53256009 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,056,994 | 21,682,267.847916 | 53256009 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,051,688 | 16.489569 | 53256009 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | WETH/EDEL | 7000 | 1,045,421 | 75,812.261187 | 53256009 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | VIRTUAL/WETH | 10000 | 1,032,834 | 0.000263 | 53256009 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v2 | WETH/USDC | 3000 | 1,027,745 | 2,331.584608 | 53256009 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| uniswap_v3 | WETH/VVV | 10000 | 1,018,002 | 93.308563 | 53256009 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome | WETH/AERO | 10000 | 1,008,916 | 3,409.951284 | 53256009 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | USDC/NOCK | 3000 | 1,005,965 | 61.860661 | 53256009 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/USDC | 10000 | 937,684 | 2,345.750927 | 53256009 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 929,744 | 1,037.229237 | 53256009 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | uXRP/WETH | 3000 | 891,593 | 0.000549 | 53256009 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | USDC/SAPIEN | 4540 | 876,765 | 18.073313 | 53256009 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 841,924 | 17.493517 | 53256009 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| pancakeswap_v3 | QUID/USDC | 100 | 825,255 | 0.061305 | 53256009 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 788,357 | 0.803616 | 53256009 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 747,700 | 4,582,281.369854 | 53256009 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome_slipstream | AERO/cbBTC | 2700 | 741,429 | 0.000008 | 53256009 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 740,915 | 0.608316 | 53256009 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| aerodrome | WETH/msETH (stable) | 500 | 708,476 | 2.335672 | 53256009 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | WETH/BRETT | 2126 | 694,574 | 501,971.941690 | 53256009 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v2 | WETH/NPC | 3000 | 691,384 | 142,958.071654 | 53256009 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 645,844 | 0.101327 | 53256009 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| uniswap_v3 | TIG/USDC | 10000 | 642,524 | 0.521652 | 53256009 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |

## Recherche d'opportunités
- Cycles : 14329 ; routes examinées : 273282688 ; candidats optimisés : 967865 ; net attendu > 0 : 713 ; dernier cycle 319.2 ms
- Rejets (moteur) : {'spread_below_threshold': 268821749, 'liquidity_below_min': 3205023, 'negative_expected_net': 967152, 'borrow_bound_too_small': 285932, 'cycle_budget_exhausted': 1994}
- Enregistrements de la session : 967865 ; net attendu > 0 : 713 ; simulés (eth_call de la vraie tx) : 52 (ok 39, échec 13) ; étiquettes ghost N+1 : 7/34 positives
- Décisions : {'REJECTED': 967865} ; motifs de rejet : {'below_safety_margin': 563, 'negative_expected_net': 967152, 'p_lower_below_threshold': 672, 'price_impact': 32, 'reliability_not_demonstrated': 41, 'sim_below_estimate': 1, 'simulated_net_nonpositive': 1, 'simulation_failed': 13, 'stale_data': 12}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53249310 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 2,657.466186 USDC | 0.433718 USDC | 0.000000 USDC | 0.006054 USDC | 0.427664 USDC (0.3935 €) | — | 1.61 | 0.030 (n=118) | REJECTED | below_safety_margin(427664<531493), p_lower_below_threshold(0.03<0.75) |
| 53249310 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 1.126445 WETH | 0.000184 WETH | 0.000000 WETH | 0.000003 WETH | 0.000181 WETH (0.3929 €) | — | 1.61 | 0.030 (n=118) | REJECTED | below_safety_margin(181167683598700<225288950635663), p_lower_below_threshold(0.03<0.75) |
| 53249310 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.013590 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1146 €) | — | 1.13 | 0.122 (n=443) | REJECTED | below_safety_margin(153<271), p_lower_below_threshold(0.12<0.75) |
| 53249310 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 1,189.058784 USDC | 0.131434 USDC | 0.000000 USDC | 0.007139 USDC | 0.124295 USDC (0.1144 €) | — | 1.05 | 0.122 (n=443) | REJECTED | below_safety_margin(124295<237811), p_lower_below_threshold(0.12<0.75) |
| 53249310 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.503881 WETH | 0.000056 WETH | 0.000000 WETH | 0.000003 WETH | 0.000053 WETH (0.1142 €) | — | 1.05 | 0.122 (n=443) | REJECTED | below_safety_margin(52671607234772<100776154603833), p_lower_below_threshold(0.12<0.75) |
| 53250013 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 1,424.800139 USDC | 0.123186 USDC | 0.000000 USDC | 0.005706 USDC | 0.117480 USDC (0.1081 €) | — | 0.82 | 0.030 (n=118) | REJECTED | below_safety_margin(117480<284960), p_lower_below_threshold(0.03<0.75) |
| 53250013 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.604235 WETH | 0.000052 WETH | 0.000000 WETH | 0.000002 WETH | 0.000050 WETH (0.1081 €) | — | 0.82 | 0.030 (n=118) | REJECTED | below_safety_margin(49689579718740<120847099433212), p_lower_below_threshold(0.03<0.75) |
| 53254922 | USDC→[aerodrome]→OWB→[uniswap_v3]→USDC | 31.568492 USDC | 0.077996 USDC | 0.000000 USDC | 0.004935 USDC | 0.073061 USDC (0.0672 €) | — | 23.14 | 0.000 (n=26) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53254673 | WETH→[uniswap_v3]→USDT→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.107284 WETH | 0.000027 WETH | 0.000000 WETH | 0.000003 WETH | 0.000024 WETH (0.0516 €) | 0.000024 WETH | 2.24 | 0.121 (n=447) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 53254673 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDT→[uniswap_v3]→USDC | 248.309669 USDC | 0.062965 USDC | 0.000000 USDC | 0.007035 USDC | 0.055930 USDC (0.0515 €) | — | 2.25 | 0.121 (n=447) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 53254673 | WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.101004 WETH | 0.000024 WETH | 0.000000 WETH | 0.000003 WETH | 0.000021 WETH (0.0456 €) | 0.000021 WETH | 2.10 | 0.121 (n=447) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 53254673 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC | 235.697109 USDC | 0.056512 USDC | 0.000000 USDC | 0.007035 USDC | 0.049477 USDC (0.0455 €) | — | 2.10 | 0.121 (n=447) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 53254673 | WETH→[uniswap_v3]→USDT→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.094043 WETH | 0.000022 WETH | 0.000000 WETH | 0.000003 WETH | 0.000019 WETH (0.0402 €) | — | 1.99 | 0.121 (n=447) | REJECTED | below_safety_margin(18745077915048<18808606607089), p_lower_below_threshold(0.12<0.75) |
| 53254673 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDT→[pancakeswap_v3]→USDC | 218.718527 USDC | 0.051014 USDC | 0.000000 USDC | 0.007389 USDC | 0.043625 USDC (0.0401 €) | — | 1.99 | 0.121 (n=447) | REJECTED | below_safety_margin(43625<43743), p_lower_below_threshold(0.12<0.75) |
| 53249310 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 324.735296 USDC | 0.038887 USDC | 0.000000 USDC | 0.005696 USDC | 0.033191 USDC (0.0305 €) | — | 1.02 | 0.010 (n=30) | REJECTED | below_safety_margin(33191<64947), p_lower_below_threshold(0.01<0.75) |
| 53249310 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.137438 WETH | 0.000016 WETH | 0.000000 WETH | 0.000002 WETH | 0.000014 WETH (0.0305 €) | — | 1.02 | 0.010 (n=30) | REJECTED | below_safety_margin(14055263807266<27487672827153), p_lower_below_threshold(0.01<0.75) |
| 53254673 | WETH→[uniswap_v3]→USDT→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.073803 WETH | 0.000016 WETH | 0.000000 WETH | 0.000003 WETH | 0.000013 WETH (0.0277 €) | — | 1.75 | 0.164 (n=225) | REJECTED | below_safety_margin(12914726902085<14760621606272), p_lower_below_threshold(0.16<0.75) |
| 53254673 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→USDT→[uniswap_v3]→USDC | 171.769465 USDC | 0.037093 USDC | 0.000000 USDC | 0.007035 USDC | 0.030058 USDC (0.0277 €) | — | 1.75 | 0.164 (n=225) | REJECTED | below_safety_margin(30058<34353), p_lower_below_threshold(0.16<0.75) |
| 53253166 | WETH→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.057343 WETH | 0.000014 WETH | 0.000000 WETH | 0.000003 WETH | 0.000011 WETH (0.0243 €) | — | 1.97 | 0.164 (n=225) | REJECTED | below_safety_margin(11287273507030<11468619061805), p_lower_below_threshold(0.16<0.75) |
| 53253166 | WETH→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.057343 WETH | 0.000014 WETH | 0.000000 WETH | 0.000003 WETH | 0.000011 WETH (0.0243 €) | — | 1.97 | 0.164 (n=225) | REJECTED | below_safety_margin(11287273507030<11468619061805), p_lower_below_threshold(0.16<0.75) |
| 53253166 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→USDC | 133.728373 USDC | 0.033534 USDC | 0.000000 USDC | 0.007165 USDC | 0.026369 USDC (0.0243 €) | — | 1.97 | 0.164 (n=225) | REJECTED | below_safety_margin(26369<26745), p_lower_below_threshold(0.16<0.75) |
| 53253166 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→USDC | 133.728373 USDC | 0.033534 USDC | 0.000000 USDC | 0.007165 USDC | 0.026369 USDC (0.0243 €) | — | 1.97 | 0.164 (n=225) | REJECTED | below_safety_margin(26369<26745), p_lower_below_threshold(0.16<0.75) |
| 53254673 | WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.068840 WETH | 0.000014 WETH | 0.000000 WETH | 0.000003 WETH | 0.000011 WETH (0.0237 €) | — | 1.60 | 0.164 (n=225) | REJECTED | below_safety_margin(11048197878653<13767919828893), p_lower_below_threshold(0.16<0.75) |
| 53254673 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC | 160.085936 USDC | 0.032746 USDC | 0.000000 USDC | 0.007035 USDC | 0.025711 USDC (0.0237 €) | — | 1.61 | 0.164 (n=225) | REJECTED | below_safety_margin(25711<32017), p_lower_below_threshold(0.16<0.75) |
| 53249467 | cbBTC→[aerodrome_slipstream]→ZEN→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC | 0.002938 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0210 €) | — | 0.95 | 0.122 (n=443) | REJECTED | below_safety_margin(28<58), p_lower_below_threshold(0.12<0.75) |

## Fiabilité et décision
- Observations ghost : 3181 ; taux observé 0.101 ; borne inférieure crédible (0.9) 0.094 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 9.4% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ✅ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
