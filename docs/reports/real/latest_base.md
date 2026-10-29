# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-29T20:43:03+00:00 ; durée 330.28 min ; blocs 53248705 → 53258610 (9607 vus)

## Connexion
- Requêtes RPC : 116373 ; erreurs : 144 ; latence p50/p95 : 307.9/2,122.5 ms
- Rafraîchissements d'état : 9607 ; âge des données au dernier bloc : 3.95 s ; changements de frais LP observés (pools à frais dynamiques) : 19837
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 166368 ; cycles déclenchés par événement : 9210 ; avance médiane sur le rafraîchissement multicall : 349 ms
- Gaz : base fee 0.022294 gwei ; prix ETH (pool le plus profond) : 2,275.46 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 517 pools, 297 jetons, 19072 routes
- Par DEX : uniswap_v3 146, aerodrome_slipstream 120, aerodrome 208, pancakeswap_v3 29 (quarantaine 1), uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 182 (rejetés 2) → 587 jetons ; pools candidats 3756 (énumérés 327, par paires 0), mesurés 519, sous le plancher de 10000.0 $ : 2 → gardés 517 (max 1500) ; prix des hubs : {'USDC': 1.0, 'USDbC': 1.0, 'DAI': 1.0, 'WETH': 2355.875591, 'cbBTC': 81334.783192, 'AERO': 0.704357}
- Pools en quarantaine : 1 — pancakeswap_v3:VIRTUAL/USDC@0x7CB770: simulation failed ×5 (model/chain mismatch) — until block 53258899

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 155,211,863 | 2,275.461318 | 53258610 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,093,859 | 0.028629 | 53258610 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,684,725 | 0.000013 | 53258610 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,263,110 | 0.028632 | 53258610 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 8,157,824 | 2,267.747761 | 53258610 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 8,063,656 | 96.487747 | 53258610 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,839,398 | 0.001602 | 53258610 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 6,246,540 | 1.527147 | 53258610 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,694,789 | 0.028637 | 53258610 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/USDC | 2000 | 4,350,736 | 2,267.772653 | 53258610 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,327,273 | 2,268.595254 | 53258610 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,184,966 | 0.998868 | 53258610 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,587,120 | 37,659.554648 | 53258610 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2690 | 2,824,775 | 0.028617 | 53258610 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2853 | 2,412,619 | 96.505903 | 53258610 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | USDC/cbBTC | 600 | 2,090,372 | 0.000013 | 53258610 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome | WETH/FAI | 10000 | 2,079,040 | 1,214,455.838466 | 53258610 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | XDP/USDC | 100 | 1,765,496 | 0.018185 | 53258610 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,733,353 | 0.000000 | 53258610 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,733,137 | 403.557142 | 53258610 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | WETH/USDC | 3000 | 1,712,226 | 2,274.485527 | 53258610 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,701,375 | 0.000013 | 53258610 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,697,938 | 0.000013 | 53258610 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | USDC/cbBTC | 470 | 1,593,027 | 0.000013 | 53258610 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,514,130 | 1.588195 | 53258610 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,454,996 | 0.826523 | 53258610 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,390,486 | 3,466.822586 | 53258610 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,361,211 | 0.005309 | 53258610 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,356,149 | 14,068.591564 | 53258610 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,239,396 | 2,269.736086 | 53258610 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,186,900 | 0.000255 | 53258610 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | USDC/SEND | 3000 | 1,181,550 | 69.604611 | 53258610 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,122,963 | 36,539,598.147578 | 53258610 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | WETH/WELL | 10000 | 1,106,463 | 1,108,290.223607 | 53258610 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,073,796 | 514,136.629424 | 53258610 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | WETH/EDEL | 7000 | 1,046,406 | 72,224.860000 | 53258610 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | DRB/WETH | 10000 | 1,045,187 | 0.000000 | 53258610 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,038,831 | 17.044521 | 53258610 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,032,630 | 21,682,267.847916 | 53258610 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | USDC/VVV | 3000 | 1,029,125 | 0.042578 | 53258610 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v2 | WETH/USDC | 3000 | 1,015,870 | 2,268.093273 | 53258610 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome | USDC/NOCK | 3000 | 1,004,775 | 62.007296 | 53258610 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome | VIRTUAL/WETH | 10000 | 996,581 | 0.000257 | 53258610 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | WETH/VVV | 10000 | 982,349 | 95.844185 | 53258610 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome | WETH/AERO | 10000 | 980,707 | 3,439.601290 | 53258610 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | WETH/USDC | 10000 | 928,432 | 2,290.488791 | 53258610 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 906,966 | 1,042.419492 | 53258610 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | uXRP/WETH | 3000 | 868,236 | 0.000546 | 53258610 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | USDC/SAPIEN | 4895 | 859,756 | 18.652078 | 53258610 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 840,226 | 0.063726 | 53258610 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 813,547 | 17.703685 | 53258610 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | WETH/wstETH | 3000 | 770,204 | 0.803616 | 53258610 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 731,470 | 4,569,951.635335 | 53258610 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 722,219 | 0.000008 | 53258610 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 713,489 | 0.577679 | 53258610 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| aerodrome | WETH/msETH (stable) | 500 | 693,385 | 2.329548 | 53258610 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v2 | WETH/NPC | 3000 | 677,804 | 141,956.719380 | 53258610 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | WETH/BRETT | 2309 | 667,081 | 517,983.733219 | 53258610 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | TIG/USDC | 10000 | 641,563 | 0.520156 | 53258610 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 629,579 | 0.097307 | 53258610 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |

## Recherche d'opportunités
- Cycles : 18816 ; routes examinées : 358858752 ; candidats optimisés : 1374971 ; net attendu > 0 : 2357 ; dernier cycle 1112.8 ms
- Rejets (moteur) : {'spread_below_threshold': 352705262, 'liquidity_below_min': 4391790, 'negative_expected_net': 1372614, 'borrow_bound_too_small': 370215, 'cycle_budget_exhausted': 11849, 'pool_quarantined': 4440}
- Enregistrements de la session : 1374971 ; net attendu > 0 : 2357 ; simulés (eth_call de la vraie tx) : 152 (ok 88, échec 64) ; étiquettes ghost N+1 : 33/105 positives
- Décisions : {'REJECTED': 1374971} ; motifs de rejet : {'below_safety_margin': 1586, 'negative_expected_net': 1372614, 'p_lower_below_threshold': 2221, 'price_impact': 32, 'reliability_not_demonstrated': 136, 'sim_below_estimate': 17, 'simulated_net_nonpositive': 10, 'simulation_failed': 64, 'stale_data': 50}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53258593 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 1.503930 WETH | 0.000410 WETH | 0.000000 WETH | 0.000009 WETH | 0.000401 WETH (0.8420 €) | 0.000401 WETH | 2.67 | 0.036 (n=121) | REJECTED | p_lower_below_threshold(0.04<0.75) |
| 53258593 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 3,418.995331 USDC | 0.933359 USDC | 0.000000 USDC | 0.020933 USDC | 0.912426 USDC (0.8394 €) | — | 2.67 | 0.036 (n=121) | REJECTED | p_lower_below_threshold(0.04<0.75) |
| 53249310 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 2,657.466186 USDC | 0.433718 USDC | 0.000000 USDC | 0.006054 USDC | 0.427664 USDC (0.3935 €) | — | 1.61 | 0.030 (n=118) | REJECTED | below_safety_margin(427664<531493), p_lower_below_threshold(0.03<0.75) |
| 53249310 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 1.126445 WETH | 0.000184 WETH | 0.000000 WETH | 0.000003 WETH | 0.000181 WETH (0.3929 €) | — | 1.61 | 0.030 (n=118) | REJECTED | below_safety_margin(181167683598700<225288950635663), p_lower_below_threshold(0.03<0.75) |
| 53257374 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.774683 WETH | 0.000088 WETH | 0.000000 WETH | 0.000003 WETH | 0.000085 WETH (0.1823 €) | — | 1.10 | 0.036 (n=119) | REJECTED | below_safety_margin(85052788328194<154936619015248), p_lower_below_threshold(0.04<0.75) |
| 53257374 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 1,800.905487 USDC | 0.204194 USDC | 0.000000 USDC | 0.006183 USDC | 0.198011 USDC (0.1822 €) | — | 1.10 | 0.036 (n=119) | REJECTED | below_safety_margin(198011<360181), p_lower_below_threshold(0.04<0.75) |
| 53258593 | WETH→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.144785 WETH | 0.000080 WETH | 0.000000 WETH | 0.000009 WETH | 0.000071 WETH (0.1483 €) | 0.000071 WETH | 4.88 | 0.098 (n=356) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53258593 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→USDC | 328.228467 USDC | 0.181484 USDC | 0.000000 USDC | 0.020950 USDC | 0.160534 USDC (0.1477 €) | — | 4.89 | 0.098 (n=356) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53258599 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→VIRTUAL→[uniswap_v3]→WETH | 0.084445 WETH | 0.000072 WETH | 0.000000 WETH | 0.000009 WETH | 0.000062 WETH (0.1306 €) | — | 7.37 | 0.097 (n=358) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.10<0.75) |
| 53258599 | USDC→[pancakeswap_v3]→VIRTUAL→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 191.619136 USDC | 0.162803 USDC | 0.000000 USDC | 0.021472 USDC | 0.141331 USDC (0.1300 €) | — | 7.38 | 0.097 (n=358) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53258394 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.002834 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1213 €) | — | 5.82 | 0.098 (n=354) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53258394 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 231.388256 USDC | 0.142657 USDC | 0.000000 USDC | 0.010950 USDC | 0.131707 USDC (0.1212 €) | — | 5.69 | 0.098 (n=354) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53258394 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.099786 WETH | 0.000062 WETH | 0.000000 WETH | 0.000005 WETH | 0.000057 WETH (0.1210 €) | 0.000033 WETH | 5.76 | 0.098 (n=354) | REJECTED | sim_below_estimate(37441408233599<62232930982879), p_lower_below_threshold(0.10<0.75) |
| 53249310 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.013590 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1146 €) | — | 1.13 | 0.122 (n=443) | REJECTED | below_safety_margin(153<271), p_lower_below_threshold(0.12<0.75) |
| 53249310 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 1,189.058784 USDC | 0.131434 USDC | 0.000000 USDC | 0.007139 USDC | 0.124295 USDC (0.1144 €) | — | 1.05 | 0.122 (n=443) | REJECTED | below_safety_margin(124295<237811), p_lower_below_threshold(0.12<0.75) |
| 53249310 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.503881 WETH | 0.000056 WETH | 0.000000 WETH | 0.000003 WETH | 0.000053 WETH (0.1142 €) | — | 1.05 | 0.122 (n=443) | REJECTED | below_safety_margin(52671607234772<100776154603833), p_lower_below_threshold(0.12<0.75) |
| 53258571 | WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.181903 WETH | 0.000059 WETH | 0.000000 WETH | 0.000007 WETH | 0.000052 WETH (0.1105 €) | — | 2.88 | 0.122 (n=465) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.12<0.75) |
| 53258573 | WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.062052 WETH | 0.000059 WETH | 0.000000 WETH | 0.000006 WETH | 0.000052 WETH (0.1105 €) | — | 8.46 | 0.011 (n=75) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.01<0.75) |
| 53258571 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC | 414.768938 USDC | 0.135085 USDC | 0.000000 USDC | 0.015436 USDC | 0.119649 USDC (0.1101 €) | — | 2.88 | 0.122 (n=465) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 53258573 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC | 141.173897 USDC | 0.134393 USDC | 0.000000 USDC | 0.014827 USDC | 0.119566 USDC (0.1100 €) | — | 8.47 | 0.011 (n=75) | REJECTED | p_lower_below_threshold(0.01<0.75) |
| 53250013 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 1,424.800139 USDC | 0.123186 USDC | 0.000000 USDC | 0.005706 USDC | 0.117480 USDC (0.1081 €) | — | 0.82 | 0.030 (n=118) | REJECTED | below_safety_margin(117480<284960), p_lower_below_threshold(0.03<0.75) |
| 53250013 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.604235 WETH | 0.000052 WETH | 0.000000 WETH | 0.000002 WETH | 0.000050 WETH (0.1081 €) | — | 0.82 | 0.030 (n=118) | REJECTED | below_safety_margin(49689579718740<120847099433212), p_lower_below_threshold(0.03<0.75) |
| 53258394 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→WETH | 0.077827 WETH | 0.000055 WETH | 0.000000 WETH | 0.000005 WETH | 0.000051 WETH (0.1067 €) | 0.000056 WETH | 6.51 | 0.098 (n=354) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53258394 | cbBTC→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.002158 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.1066 €) | — | 6.72 | 0.098 (n=354) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53258394 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→USDC | 173.317610 USDC | 0.126252 USDC | 0.000000 USDC | 0.010950 USDC | 0.115302 USDC (0.1061 €) | — | 6.65 | 0.098 (n=354) | REJECTED | p_lower_below_threshold(0.10<0.75) |

## Fiabilité et décision
- Observations ghost : 3252 ; taux observé 0.107 ; borne inférieure crédible (0.9) 0.100 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 10.0% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ✅ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
