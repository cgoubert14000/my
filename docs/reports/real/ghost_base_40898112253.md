# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-29T20:04:27+00:00 ; durée 291.68 min ; blocs 53248705 → 53257452 (8558 vus)

## Connexion
- Requêtes RPC : 103532 ; erreurs : 100 ; latence p50/p95 : 293.7/1,722.8 ms
- Rafraîchissements d'état : 8558 ; âge des données au dernier bloc : 5.05 s ; changements de frais LP observés (pools à frais dynamiques) : 15931
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 126853 ; cycles déclenchés par événement : 8294 ; avance médiane sur le rafraîchissement multicall : 1,396 ms
- Gaz : base fee 0.006098 gwei ; prix ETH (pool le plus profond) : 2,320.89 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 517 pools, 297 jetons, 19072 routes
- Par DEX : uniswap_v3 146, aerodrome_slipstream 120, aerodrome 208, pancakeswap_v3 29, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 182 (rejetés 2) → 587 jetons ; pools candidats 3756 (énumérés 327, par paires 0), mesurés 519, sous le plancher de 10000.0 $ : 2 → gardés 517 (max 1500) ; prix des hubs : {'USDC': 1.0, 'USDbC': 1.0, 'DAI': 1.0, 'WETH': 2355.875591, 'cbBTC': 81334.783192, 'AERO': 0.704357}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 157,537,120 | 2,321.283704 | 53257452 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,401,077 | 0.028783 | 53257452 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,754,372 | 0.000012 | 53257452 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,436,092 | 0.028855 | 53257452 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| aerodrome | WETH/VVV | 3000 | 8,320,503 | 94.294518 | 53257452 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/USDC | 500 | 8,271,474 | 2,315.621593 | 53257452 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,961,310 | 0.001612 | 53257452 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 6,316,492 | 1.493590 | 53257452 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,802,787 | 0.028772 | 53257452 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/USDC | 1443 | 4,422,739 | 2,315.123818 | 53257452 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,396,251 | 2,314.451560 | 53257452 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,245,557 | 0.998879 | 53257452 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,657,563 | 37,683.639511 | 53257452 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2560 | 2,878,638 | 0.028840 | 53257452 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2748 | 2,449,657 | 94.303527 | 53257452 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | WETH/FAI | 10000 | 2,114,775 | 1,221,092.593375 | 53257452 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 600 | 2,108,820 | 0.000012 | 53257452 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome | WETH/USDC | 3000 | 1,813,897 | 2,321.371313 | 53257452 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| uniswap_v3 | XDP/USDC | 100 | 1,775,864 | 0.018377 | 53257452 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,775,123 | 397.508919 | 53257452 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,765,559 | 0.000000 | 53257452 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,716,974 | 0.000012 | 53257452 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,710,672 | 0.000012 | 53257452 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | USDC/cbBTC | 388 | 1,606,547 | 0.000012 | 53257452 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,514,127 | 1.588199 | 53257452 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,457,136 | 0.826856 | 53257452 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,420,201 | 3,457.581999 | 53257452 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,396,452 | 0.005345 | 53257452 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,386,668 | 13,791.093516 | 53257452 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,259,103 | 2,315.330637 | 53257452 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,220,937 | 0.000260 | 53257452 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | USDC/SEND | 3000 | 1,181,587 | 69.600279 | 53257452 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,141,939 | 36,872,162.424943 | 53257452 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | WETH/WELL | 10000 | 1,134,458 | 1,096,779.994261 | 53257452 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,103,304 | 503,860.523172 | 53257452 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,062,916 | 0.000000 | 53257452 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | USDC/VVV | 3000 | 1,058,680 | 0.040747 | 53257452 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,053,248 | 21,682,267.847916 | 53257452 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,048,656 | 16.617486 | 53257452 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | WETH/EDEL | 7000 | 1,042,947 | 75,636.575704 | 53257452 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v2 | WETH/USDC | 3000 | 1,025,936 | 2,320.885549 | 53257452 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome | VIRTUAL/WETH | 10000 | 1,025,180 | 0.000261 | 53257452 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | WETH/VVV | 10000 | 1,012,303 | 93.616268 | 53257452 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome | USDC/NOCK | 3000 | 1,006,982 | 61.735772 | 53257452 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome | WETH/AERO | 10000 | 1,001,510 | 3,434.672293 | 53257452 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | WETH/USDC | 10000 | 936,372 | 2,337.157255 | 53257452 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 925,349 | 1,042.059059 | 53257452 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | uXRP/WETH | 3000 | 887,539 | 0.000548 | 53257452 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | USDC/SAPIEN | 4825 | 871,772 | 18.241475 | 53257452 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 837,019 | 17.537613 | 53257452 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| pancakeswap_v3 | QUID/USDC | 100 | 827,649 | 0.061687 | 53257452 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 785,580 | 0.803616 | 53257452 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 744,991 | 4,583,210.159879 | 53257452 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome_slipstream | AERO/cbBTC | 2700 | 736,001 | 0.000008 | 53257452 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 734,464 | 0.600738 | 53257452 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| aerodrome | WETH/msETH (stable) | 500 | 706,213 | 2.334524 | 53257452 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v2 | WETH/NPC | 3000 | 689,016 | 142,931.488775 | 53257452 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | WETH/BRETT | 2387 | 687,625 | 508,289.882481 | 53257452 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 648,360 | 0.101934 | 53257452 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| uniswap_v3 | TIG/USDC | 10000 | 642,524 | 0.521652 | 53257452 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |

## Recherche d'opportunités
- Cycles : 16851 ; routes examinées : 321382272 ; candidats optimisés : 1212508 ; net attendu > 0 : 878 ; dernier cycle 1201.5 ms
- Rejets (moteur) : {'spread_below_threshold': 315997738, 'liquidity_below_min': 3830063, 'negative_expected_net': 1211630, 'borrow_bound_too_small': 338779, 'cycle_budget_exhausted': 3184}
- Enregistrements de la session : 1212508 ; net attendu > 0 : 878 ; simulés (eth_call de la vraie tx) : 69 (ok 51, échec 18) ; étiquettes ghost N+1 : 10/42 positives
- Décisions : {'REJECTED': 1212508} ; motifs de rejet : {'below_safety_margin': 708, 'negative_expected_net': 1211630, 'p_lower_below_threshold': 835, 'price_impact': 32, 'reliability_not_demonstrated': 43, 'sim_below_estimate': 3, 'simulated_net_nonpositive': 3, 'simulation_failed': 18, 'stale_data': 16}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53249310 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 2,657.466186 USDC | 0.433718 USDC | 0.000000 USDC | 0.006054 USDC | 0.427664 USDC (0.3935 €) | — | 1.61 | 0.030 (n=118) | REJECTED | below_safety_margin(427664<531493), p_lower_below_threshold(0.03<0.75) |
| 53249310 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 1.126445 WETH | 0.000184 WETH | 0.000000 WETH | 0.000003 WETH | 0.000181 WETH (0.3929 €) | — | 1.61 | 0.030 (n=118) | REJECTED | below_safety_margin(181167683598700<225288950635663), p_lower_below_threshold(0.03<0.75) |
| 53257374 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.774683 WETH | 0.000088 WETH | 0.000000 WETH | 0.000003 WETH | 0.000085 WETH (0.1823 €) | — | 1.10 | 0.036 (n=119) | REJECTED | below_safety_margin(85052788328194<154936619015248), p_lower_below_threshold(0.04<0.75) |
| 53257374 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 1,800.905487 USDC | 0.204194 USDC | 0.000000 USDC | 0.006183 USDC | 0.198011 USDC (0.1822 €) | — | 1.10 | 0.036 (n=119) | REJECTED | below_safety_margin(198011<360181), p_lower_below_threshold(0.04<0.75) |
| 53249310 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.013590 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1146 €) | — | 1.13 | 0.122 (n=443) | REJECTED | below_safety_margin(153<271), p_lower_below_threshold(0.12<0.75) |
| 53249310 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 1,189.058784 USDC | 0.131434 USDC | 0.000000 USDC | 0.007139 USDC | 0.124295 USDC (0.1144 €) | — | 1.05 | 0.122 (n=443) | REJECTED | below_safety_margin(124295<237811), p_lower_below_threshold(0.12<0.75) |
| 53249310 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.503881 WETH | 0.000056 WETH | 0.000000 WETH | 0.000003 WETH | 0.000053 WETH (0.1142 €) | — | 1.05 | 0.122 (n=443) | REJECTED | below_safety_margin(52671607234772<100776154603833), p_lower_below_threshold(0.12<0.75) |
| 53250013 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 1,424.800139 USDC | 0.123186 USDC | 0.000000 USDC | 0.005706 USDC | 0.117480 USDC (0.1081 €) | — | 0.82 | 0.030 (n=118) | REJECTED | below_safety_margin(117480<284960), p_lower_below_threshold(0.03<0.75) |
| 53250013 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.604235 WETH | 0.000052 WETH | 0.000000 WETH | 0.000002 WETH | 0.000050 WETH (0.1081 €) | — | 0.82 | 0.030 (n=118) | REJECTED | below_safety_margin(49689579718740<120847099433212), p_lower_below_threshold(0.03<0.75) |
| 53257373 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.243467 WETH | 0.000043 WETH | 0.000000 WETH | 0.000003 WETH | 0.000040 WETH (0.0861 €) | — | 1.65 | 0.010 (n=30) | REJECTED | below_safety_margin(40152792362702<48693356055449), p_lower_below_threshold(0.01<0.75) |
| 53257374 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.243467 WETH | 0.000043 WETH | 0.000000 WETH | 0.000003 WETH | 0.000040 WETH (0.0861 €) | — | 1.65 | 0.010 (n=30) | REJECTED | below_safety_margin(40152792362702<48693356055449), p_lower_below_threshold(0.01<0.75) |
| 53257373 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 564.547423 USDC | 0.100033 USDC | 0.000000 USDC | 0.006550 USDC | 0.093483 USDC (0.0860 €) | — | 1.66 | 0.010 (n=30) | REJECTED | below_safety_margin(93483<112909), p_lower_below_threshold(0.01<0.75) |
| 53257374 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 564.547423 USDC | 0.100033 USDC | 0.000000 USDC | 0.006550 USDC | 0.093483 USDC (0.0860 €) | — | 1.66 | 0.010 (n=30) | REJECTED | below_safety_margin(93483<112909), p_lower_below_threshold(0.01<0.75) |
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

## Fiabilité et décision
- Observations ghost : 3189 ; taux observé 0.102 ; borne inférieure crédible (0.9) 0.095 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 9.5% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ✅ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
