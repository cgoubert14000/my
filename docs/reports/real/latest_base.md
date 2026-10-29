# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-29T20:14:11+00:00 ; durée 301.4 min ; blocs 53248705 → 53257745 (8824 vus)

## Connexion
- Requêtes RPC : 106832 ; erreurs : 100 ; latence p50/p95 : 261.4/1,565.4 ms
- Rafraîchissements d'état : 8824 ; âge des données au dernier bloc : 2.5 s ; changements de frais LP observés (pools à frais dynamiques) : 17204
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 138207 ; cycles déclenchés par événement : 8533 ; avance médiane sur le rafraîchissement multicall : 588 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,308.74 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 517 pools, 297 jetons, 19072 routes
- Par DEX : uniswap_v3 146, aerodrome_slipstream 120, aerodrome 208, pancakeswap_v3 29, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 182 (rejetés 2) → 587 jetons ; pools candidats 3756 (énumérés 327, par paires 0), mesurés 519, sous le plancher de 10000.0 $ : 2 → gardés 517 (max 1500) ; prix des hubs : {'USDC': 1.0, 'USDbC': 1.0, 'DAI': 1.0, 'WETH': 2355.875591, 'cbBTC': 81334.783192, 'AERO': 0.704357}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 156,970,938 | 2,308.742101 | 53257745 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,318,937 | 0.028792 | 53257745 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,728,083 | 0.000012 | 53257745 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,385,978 | 0.028825 | 53257745 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| aerodrome | WETH/VVV | 3000 | 8,258,315 | 94.720882 | 53257745 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/USDC | 500 | 8,252,040 | 2,314.032900 | 53257745 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,915,592 | 0.001611 | 53257745 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 6,310,662 | 1.496309 | 53257745 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,760,668 | 0.028797 | 53257745 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/USDC | 773 | 4,404,196 | 2,313.903167 | 53257745 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,378,217 | 2,313.790895 | 53257745 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,222,004 | 0.998878 | 53257745 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,637,686 | 37,698.935953 | 53257745 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,863,388 | 0.028816 | 53257745 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2763 | 2,458,800 | 94.690812 | 53257745 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | WETH/FAI | 10000 | 2,103,786 | 1,221,003.175718 | 53257745 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 532 | 2,101,824 | 0.000012 | 53257745 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome | WETH/USDC | 3000 | 1,809,145 | 2,309.731208 | 53257745 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| uniswap_v3 | XDP/USDC | 100 | 1,773,837 | 0.018334 | 53257745 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,764,277 | 398.854456 | 53257745 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,756,310 | 0.000000 | 53257745 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,711,034 | 0.000012 | 53257745 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,705,913 | 0.000012 | 53257745 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | USDC/cbBTC | 354 | 1,601,409 | 0.000012 | 53257745 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,514,127 | 1.588199 | 53257745 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,458,215 | 0.825639 | 53257745 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,415,498 | 3,459.209362 | 53257745 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,387,182 | 0.005336 | 53257745 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,377,393 | 13,868.733578 | 53257745 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,254,124 | 2,313.964510 | 53257745 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,213,134 | 0.000259 | 53257745 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | USDC/SEND | 3000 | 1,181,587 | 69.600279 | 53257745 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,135,962 | 36,872,162.424943 | 53257745 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | WETH/WELL | 10000 | 1,128,047 | 1,097,702.874124 | 53257745 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,096,660 | 504,958.275862 | 53257745 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,057,540 | 0.000000 | 53257745 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | USDC/VVV | 3000 | 1,052,042 | 0.040953 | 53257745 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,047,734 | 21,682,267.847916 | 53257745 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,046,454 | 16.711509 | 53257745 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | WETH/EDEL | 7000 | 1,039,670 | 75,319.722818 | 53257745 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v2 | WETH/USDC | 3000 | 1,023,255 | 2,308.544705 | 53257745 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome | VIRTUAL/WETH | 10000 | 1,018,617 | 0.000261 | 53257745 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome | USDC/NOCK | 3000 | 1,006,639 | 61.777910 | 53257745 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/VVV | 10000 | 1,005,055 | 94.007316 | 53257745 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome | WETH/AERO | 10000 | 997,972 | 3,434.672293 | 53257745 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | WETH/USDC | 10000 | 934,345 | 2,325.085818 | 53257745 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 919,778 | 1,043.934470 | 53257745 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | uXRP/WETH | 3000 | 882,669 | 0.000548 | 53257745 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | USDC/SAPIEN | 4530 | 868,629 | 18.348299 | 53257745 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 833,220 | 0.062584 | 53257745 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 831,397 | 17.566122 | 53257745 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | WETH/wstETH | 3000 | 781,469 | 0.803616 | 53257745 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 741,067 | 4,583,521.033471 | 53257745 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 733,511 | 0.000008 | 53257745 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 730,171 | 0.598630 | 53257745 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| aerodrome | WETH/msETH (stable) | 500 | 703,063 | 2.331832 | 53257745 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v2 | WETH/NPC | 3000 | 685,756 | 142,788.548472 | 53257745 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | WETH/BRETT | 2126 | 683,253 | 508,160.088699 | 53257745 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 644,351 | 0.100933 | 53257745 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| uniswap_v3 | TIG/USDC | 10000 | 642,482 | 0.521587 | 53257745 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |

## Recherche d'opportunités
- Cycles : 17356 ; routes examinées : 331013632 ; candidats optimisés : 1254082 ; net attendu > 0 : 1212 ; dernier cycle 148.9 ms
- Rejets (moteur) : {'spread_below_threshold': 325445706, 'liquidity_below_min': 3961676, 'negative_expected_net': 1252870, 'borrow_bound_too_small': 347446, 'cycle_budget_exhausted': 4722}
- Enregistrements de la session : 1254082 ; net attendu > 0 : 1212 ; simulés (eth_call de la vraie tx) : 87 (ok 60, échec 27) ; étiquettes ghost N+1 : 16/54 positives
- Décisions : {'REJECTED': 1254082} ; motifs de rejet : {'below_safety_margin': 932, 'negative_expected_net': 1252870, 'p_lower_below_threshold': 1157, 'price_impact': 32, 'reliability_not_demonstrated': 55, 'sim_below_estimate': 9, 'simulated_net_nonpositive': 6, 'simulation_failed': 27, 'stale_data': 18}

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
| 53257645 | WETH→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→USDC→[sushiswap_v3]→WETH | 0.046590 WETH | 0.000020 WETH | 0.000000 WETH | 0.000004 WETH | 0.000017 WETH (0.0354 €) | 0.000017 WETH | 3.58 | 0.148 (n=199) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 53257645 | WETH→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→USDC→[sushiswap_v3]→WETH | 0.046590 WETH | 0.000020 WETH | 0.000000 WETH | 0.000004 WETH | 0.000017 WETH (0.0354 €) | — | 3.58 | 0.148 (n=199) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.15<0.75) |
| 53257645 | USDC→[sushiswap_v3]→WETH→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→USDC | 107.107873 USDC | 0.046692 USDC | 0.000000 USDC | 0.008242 USDC | 0.038450 USDC (0.0354 €) | — | 3.59 | 0.148 (n=199) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 53257645 | USDC→[sushiswap_v3]→WETH→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→USDC | 107.107873 USDC | 0.046692 USDC | 0.000000 USDC | 0.008242 USDC | 0.038450 USDC (0.0354 €) | — | 3.59 | 0.148 (n=199) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 53257645 | USDC→[sushiswap_v3]→WETH→[pancakeswap_v3]→USDC | 132.845741 USDC | 0.044257 USDC | 0.000000 USDC | 0.006163 USDC | 0.038094 USDC (0.0350 €) | — | 2.87 | 0.036 (n=119) | REJECTED | p_lower_below_threshold(0.04<0.75) |

## Fiabilité et décision
- Observations ghost : 3201 ; taux observé 0.103 ; borne inférieure crédible (0.9) 0.096 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 9.6% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ✅ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
