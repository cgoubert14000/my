# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-29T20:40:10+00:00 ; durée 327.39 min ; blocs 53248705 → 53258523 (9538 vus)

## Connexion
- Requêtes RPC : 115488 ; erreurs : 144 ; latence p50/p95 : 247.8/1,329.9 ms
- Rafraîchissements d'état : 9538 ; âge des données au dernier bloc : 4.65 s ; changements de frais LP observés (pools à frais dynamiques) : 19397
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 160607 ; cycles déclenchés par événement : 9159 ; avance médiane sur le rafraîchissement multicall : 921 ms
- Gaz : base fee 0.011487 gwei ; prix ETH (pool le plus profond) : 2,296.48 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 517 pools, 297 jetons, 19072 routes
- Par DEX : uniswap_v3 146, aerodrome_slipstream 120, aerodrome 208, pancakeswap_v3 29, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 182 (rejetés 2) → 587 jetons ; pools candidats 3756 (énumérés 327, par paires 0), mesurés 519, sous le plancher de 10000.0 $ : 2 → gardés 517 (max 1500) ; prix des hubs : {'USDC': 1.0, 'USDbC': 1.0, 'DAI': 1.0, 'WETH': 2355.875591, 'cbBTC': 81334.783192, 'AERO': 0.704357}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 156,378,359 | 2,296.477385 | 53258524 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,218,334 | 0.028819 | 53258524 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,697,728 | 0.000013 | 53258524 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,335,030 | 0.028746 | 53258524 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 8,218,056 | 2,299.530983 | 53258524 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 8,157,655 | 96.044279 | 53258524 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,876,440 | 0.001611 | 53258524 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 6,287,652 | 1.507273 | 53258524 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,740,929 | 0.028822 | 53258524 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/USDC | 150 | 4,384,208 | 2,300.232505 | 53258524 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,359,645 | 2,300.178034 | 53258524 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,195,786 | 0.998875 | 53258524 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,618,381 | 37,698.539799 | 53258524 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2520 | 2,847,298 | 0.028761 | 53258524 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2811 | 2,430,557 | 96.052157 | 53258524 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | USDC/cbBTC | 600 | 2,093,768 | 0.000013 | 53258524 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome | WETH/FAI | 10000 | 2,092,610 | 1,221,003.175718 | 53258524 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | XDP/USDC | 100 | 1,770,720 | 0.018293 | 53258524 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,749,449 | 403.304431 | 53258524 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,747,615 | 0.000000 | 53258524 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome | WETH/USDC | 3000 | 1,720,115 | 2,296.097065 | 53258524 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,704,253 | 0.000013 | 53258524 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,700,342 | 0.000013 | 53258524 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | USDC/cbBTC | 370 | 1,595,489 | 0.000013 | 53258524 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,514,130 | 1.588195 | 53258524 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,455,314 | 0.826193 | 53258524 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,406,417 | 3,459.544559 | 53258524 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,379,801 | 0.005336 | 53258524 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,363,503 | 13,995.857265 | 53258524 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,248,392 | 2,299.526493 | 53258524 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,202,484 | 0.000257 | 53258524 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | USDC/SEND | 3000 | 1,181,565 | 69.602892 | 53258524 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,133,337 | 36,539,598.147578 | 53258524 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | WETH/WELL | 10000 | 1,118,849 | 1,104,655.475277 | 53258524 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,086,503 | 510,504.060164 | 53258524 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,054,846 | 0.000000 | 53258524 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | WETH/EDEL | 7000 | 1,052,732 | 72,684.557826 | 53258524 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,044,077 | 16.814130 | 53258524 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,042,168 | 21,682,267.847916 | 53258524 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | USDC/VVV | 3000 | 1,038,875 | 0.041793 | 53258524 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v2 | WETH/USDC | 3000 | 1,020,543 | 2,296.310890 | 53258524 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome | VIRTUAL/WETH | 10000 | 1,009,667 | 0.000259 | 53258524 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome | USDC/NOCK | 3000 | 1,006,175 | 61.834851 | 53258524 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/VVV | 10000 | 993,670 | 95.347739 | 53258524 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome | WETH/AERO | 10000 | 991,694 | 3,435.772739 | 53258524 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | WETH/USDC | 10000 | 932,249 | 2,307.566867 | 53258524 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 914,132 | 1,045.437390 | 53258524 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | uXRP/WETH | 3000 | 876,078 | 0.000546 | 53258524 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | USDC/SAPIEN | 4620 | 864,726 | 18.481647 | 53258524 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 838,949 | 0.063516 | 53258524 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 820,013 | 17.728133 | 53258524 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | WETH/wstETH | 3000 | 777,318 | 0.803616 | 53258524 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 736,942 | 4,585,868.377018 | 53258524 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 728,530 | 0.000008 | 53258524 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 723,182 | 0.590849 | 53258524 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| aerodrome | WETH/msETH (stable) | 500 | 699,464 | 2.331159 | 53258524 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v2 | WETH/NPC | 3000 | 681,868 | 142,894.328804 | 53258524 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | WETH/BRETT | 2351 | 675,759 | 516,478.583060 | 53258524 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | TIG/USDC | 10000 | 641,694 | 0.520359 | 53258524 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 641,034 | 0.100105 | 53258524 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |

## Recherche d'opportunités
- Cycles : 18696 ; routes examinées : 356570112 ; candidats optimisés : 1355931 ; net attendu > 0 : 1977 ; dernier cycle 465.6 ms
- Rejets (moteur) : {'spread_below_threshold': 350495857, 'liquidity_below_min': 4341202, 'negative_expected_net': 1353954, 'borrow_bound_too_small': 370096, 'cycle_budget_exhausted': 7026}
- Enregistrements de la session : 1355931 ; net attendu > 0 : 1977 ; simulés (eth_call de la vraie tx) : 133 (ok 85, échec 48) ; étiquettes ghost N+1 : 24/86 positives
- Décisions : {'REJECTED': 1355931} ; motifs de rejet : {'below_safety_margin': 1399, 'negative_expected_net': 1353954, 'p_lower_below_threshold': 1879, 'price_impact': 32, 'reliability_not_demonstrated': 98, 'sim_below_estimate': 17, 'simulated_net_nonpositive': 10, 'simulation_failed': 48, 'stale_data': 28}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53249310 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 2,657.466186 USDC | 0.433718 USDC | 0.000000 USDC | 0.006054 USDC | 0.427664 USDC (0.3935 €) | — | 1.61 | 0.030 (n=118) | REJECTED | below_safety_margin(427664<531493), p_lower_below_threshold(0.03<0.75) |
| 53249310 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 1.126445 WETH | 0.000184 WETH | 0.000000 WETH | 0.000003 WETH | 0.000181 WETH (0.3929 €) | — | 1.61 | 0.030 (n=118) | REJECTED | below_safety_margin(181167683598700<225288950635663), p_lower_below_threshold(0.03<0.75) |
| 53257374 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.774683 WETH | 0.000088 WETH | 0.000000 WETH | 0.000003 WETH | 0.000085 WETH (0.1823 €) | — | 1.10 | 0.036 (n=119) | REJECTED | below_safety_margin(85052788328194<154936619015248), p_lower_below_threshold(0.04<0.75) |
| 53257374 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 1,800.905487 USDC | 0.204194 USDC | 0.000000 USDC | 0.006183 USDC | 0.198011 USDC (0.1822 €) | — | 1.10 | 0.036 (n=119) | REJECTED | below_safety_margin(198011<360181), p_lower_below_threshold(0.04<0.75) |
| 53258394 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.002834 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1213 €) | — | 5.82 | 0.098 (n=354) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53258394 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 231.388256 USDC | 0.142657 USDC | 0.000000 USDC | 0.010950 USDC | 0.131707 USDC (0.1212 €) | — | 5.69 | 0.098 (n=354) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53258394 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.099786 WETH | 0.000062 WETH | 0.000000 WETH | 0.000005 WETH | 0.000057 WETH (0.1210 €) | 0.000033 WETH | 5.76 | 0.098 (n=354) | REJECTED | sim_below_estimate(37441408233599<62232930982879), p_lower_below_threshold(0.10<0.75) |
| 53249310 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.013590 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1146 €) | — | 1.13 | 0.122 (n=443) | REJECTED | below_safety_margin(153<271), p_lower_below_threshold(0.12<0.75) |
| 53249310 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 1,189.058784 USDC | 0.131434 USDC | 0.000000 USDC | 0.007139 USDC | 0.124295 USDC (0.1144 €) | — | 1.05 | 0.122 (n=443) | REJECTED | below_safety_margin(124295<237811), p_lower_below_threshold(0.12<0.75) |
| 53249310 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.503881 WETH | 0.000056 WETH | 0.000000 WETH | 0.000003 WETH | 0.000053 WETH (0.1142 €) | — | 1.05 | 0.122 (n=443) | REJECTED | below_safety_margin(52671607234772<100776154603833), p_lower_below_threshold(0.12<0.75) |
| 53250013 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 1,424.800139 USDC | 0.123186 USDC | 0.000000 USDC | 0.005706 USDC | 0.117480 USDC (0.1081 €) | — | 0.82 | 0.030 (n=118) | REJECTED | below_safety_margin(117480<284960), p_lower_below_threshold(0.03<0.75) |
| 53250013 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.604235 WETH | 0.000052 WETH | 0.000000 WETH | 0.000002 WETH | 0.000050 WETH (0.1081 €) | — | 0.82 | 0.030 (n=118) | REJECTED | below_safety_margin(49689579718740<120847099433212), p_lower_below_threshold(0.03<0.75) |
| 53258394 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→WETH | 0.077827 WETH | 0.000055 WETH | 0.000000 WETH | 0.000005 WETH | 0.000051 WETH (0.1067 €) | 0.000056 WETH | 6.51 | 0.098 (n=354) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53258394 | cbBTC→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.002158 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.1066 €) | — | 6.72 | 0.098 (n=354) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53258394 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→USDC | 173.317610 USDC | 0.126252 USDC | 0.000000 USDC | 0.010950 USDC | 0.115302 USDC (0.1061 €) | — | 6.65 | 0.098 (n=354) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53257373 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.243467 WETH | 0.000043 WETH | 0.000000 WETH | 0.000003 WETH | 0.000040 WETH (0.0861 €) | — | 1.65 | 0.010 (n=30) | REJECTED | below_safety_margin(40152792362702<48693356055449), p_lower_below_threshold(0.01<0.75) |
| 53257374 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.243467 WETH | 0.000043 WETH | 0.000000 WETH | 0.000003 WETH | 0.000040 WETH (0.0861 €) | — | 1.65 | 0.010 (n=30) | REJECTED | below_safety_margin(40152792362702<48693356055449), p_lower_below_threshold(0.01<0.75) |
| 53257373 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 564.547423 USDC | 0.100033 USDC | 0.000000 USDC | 0.006550 USDC | 0.093483 USDC (0.0860 €) | — | 1.66 | 0.010 (n=30) | REJECTED | below_safety_margin(93483<112909), p_lower_below_threshold(0.01<0.75) |
| 53257374 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 564.547423 USDC | 0.100033 USDC | 0.000000 USDC | 0.006550 USDC | 0.093483 USDC (0.0860 €) | — | 1.66 | 0.010 (n=30) | REJECTED | below_safety_margin(93483<112909), p_lower_below_threshold(0.01<0.75) |
| 53258394 | cbBTC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.003515 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0853 €) | — | 3.30 | 0.098 (n=354) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53258394 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→WETH | 0.118601 WETH | 0.000045 WETH | 0.000000 WETH | 0.000005 WETH | 0.000040 WETH (0.0849 €) | 0.000089 WETH | 3.40 | 0.098 (n=354) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53258394 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 259.848438 USDC | 0.102450 USDC | 0.000000 USDC | 0.010950 USDC | 0.091500 USDC (0.0842 €) | — | 3.52 | 0.098 (n=354) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53258349 | WETH→[aerodrome_slipstream]→USD→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.021456 WETH | 0.000037 WETH | 0.000000 WETH | 0.000003 WETH | 0.000034 WETH (0.0711 €) | 0.000016 WETH | 15.69 | 0.004 (n=74) | REJECTED | sim_below_estimate(19741447158946<37010936851158), p_lower_below_threshold(0.00<0.75) |
| 53258349 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USD→[aerodrome_slipstream]→USDC | 49.098228 USDC | 0.084840 USDC | 0.000000 USDC | 0.007703 USDC | 0.077137 USDC (0.0710 €) | — | 15.71 | 0.004 (n=74) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53254922 | USDC→[aerodrome]→OWB→[uniswap_v3]→USDC | 31.568492 USDC | 0.077996 USDC | 0.000000 USDC | 0.004935 USDC | 0.073061 USDC (0.0672 €) | — | 23.14 | 0.000 (n=26) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |

## Fiabilité et décision
- Observations ghost : 3233 ; taux observé 0.105 ; borne inférieure crédible (0.9) 0.098 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 9.8% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ✅ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
