# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-29T16:23:21+00:00 ; durée 70.58 min ; blocs 53248705 → 53250824 (2112 vus)

## Connexion
- Requêtes RPC : 25621 ; erreurs : 5 ; latence p50/p95 : 128.4/743.3 ms
- Rafraîchissements d'état : 2112 ; âge des données au dernier bloc : 3.73 s ; changements de frais LP observés (pools à frais dynamiques) : 5477
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 39433 ; cycles déclenchés par événement : 2198 ; avance médiane sur le rafraîchissement multicall : 196 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,360.72 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 517 pools, 297 jetons, 19072 routes
- Par DEX : uniswap_v3 146, aerodrome_slipstream 120, aerodrome 208, pancakeswap_v3 29, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 182 (rejetés 2) → 587 jetons ; pools candidats 3756 (énumérés 327, par paires 0), mesurés 519, sous le plancher de 10000.0 $ : 2 → gardés 517 (max 1500) ; prix des hubs : {'USDC': 1.0, 'USDbC': 1.0, 'DAI': 1.0, 'WETH': 2355.875591, 'cbBTC': 81334.783192, 'AERO': 0.704357}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 158,927,101 | 2,360.724767 | 53250825 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,707,271 | 0.028954 | 53250825 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,798,340 | 0.000012 | 53250825 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,583,625 | 0.028943 | 53250825 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| aerodrome | WETH/VVV | 3000 | 8,557,335 | 92.234095 | 53250825 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/USDC | 500 | 8,354,108 | 2,357.442280 | 53250825 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,099,699 | 0.001642 | 53250825 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 6,535,290 | 1.422439 | 53250825 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,826,613 | 0.028961 | 53250825 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/USDC | 654 | 4,484,182 | 2,356.545435 | 53250825 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,452,398 | 2,356.426569 | 53250825 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,292,964 | 0.998884 | 53250825 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,729,384 | 37,501.207512 | 53250825 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,923,323 | 0.028954 | 53250825 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2835 | 2,569,403 | 92.223330 | 53250825 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | WETH/FAI | 10000 | 2,152,930 | 1,218,990.174856 | 53250825 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 544 | 2,122,310 | 0.000012 | 53250825 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome | WETH/USDC | 3000 | 1,830,673 | 2,360.872732 | 53250825 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,813,741 | 390.089464 | 53250825 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | XDP/USDC | 100 | 1,797,589 | 0.018775 | 53250825 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,795,488 | 0.000000 | 53250825 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,727,157 | 0.000012 | 53250825 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,713,229 | 0.000012 | 53250825 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | USDC/cbBTC | 348 | 1,616,302 | 0.000012 | 53250825 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,514,127 | 1.588199 | 53250825 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | WETH/AERO | 3000 | 1,469,773 | 3,350.912891 | 53250825 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,460,130 | 0.827409 | 53250825 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,443,053 | 0.005449 | 53250825 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,414,990 | 13,467.534214 | 53250825 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,279,038 | 2,357.371277 | 53250825 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,257,039 | 0.000266 | 53250825 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | USDC/SEND | 3000 | 1,181,932 | 69.559662 | 53250825 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,158,504 | 37,164,149.214114 | 53250825 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | WETH/WELL | 10000 | 1,153,833 | 1,096,966.560603 | 53250825 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,132,331 | 491,756.694538 | 53250825 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,077,218 | 0.000000 | 53250825 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,073,142 | 21,620,231.575433 | 53250825 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | USDC/VVV | 3000 | 1,071,220 | 0.039153 | 53250825 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | WETH/EDEL | 7000 | 1,064,438 | 75,094.109010 | 53250825 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,060,463 | 16.129140 | 53250825 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | VIRTUAL/WETH | 10000 | 1,055,505 | 0.000264 | 53250825 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | WETH/VVV | 10000 | 1,037,736 | 92.426177 | 53250825 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome | WETH/AERO | 10000 | 1,035,022 | 3,364.813352 | 53250825 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v2 | WETH/USDC | 3000 | 1,034,686 | 2,360.867677 | 53250825 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome | USDC/NOCK | 3000 | 1,003,177 | 62.204753 | 53250825 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/USDC | 10000 | 942,614 | 2,353.284700 | 53250825 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 942,254 | 1,039.874294 | 53250825 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | uXRP/WETH | 3000 | 905,229 | 0.000551 | 53250825 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 887,093 | 17.728538 | 53250825 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 861,479 | 17.309261 | 53250825 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| pancakeswap_v3 | QUID/USDC | 100 | 850,756 | 0.065396 | 53250825 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 799,065 | 0.803616 | 53250825 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 759,782 | 0.000009 | 53250825 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 759,645 | 4,560,613.329515 | 53250825 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 757,460 | 0.626434 | 53250825 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| aerodrome | WETH/msETH (stable) | 500 | 717,670 | 2.337743 | 53250825 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | WETH/BRETT | 2114 | 708,386 | 490,861.717580 | 53250825 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v2 | WETH/NPC | 3000 | 701,593 | 142,619.838579 | 53250825 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| uniswap_v3 | TIG/USDC | 10000 | 652,678 | 0.537532 | 53250825 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 640,952 | 0.100136 | 53250825 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |

## Recherche d'opportunités
- Cycles : 4309 ; routes examinées : 82181248 ; candidats optimisés : 297821 ; net attendu > 0 : 255 ; dernier cycle 166.6 ms
- Rejets (moteur) : {'spread_below_threshold': 80783030, 'liquidity_below_min': 1033449, 'negative_expected_net': 297566, 'borrow_bound_too_small': 66434, 'cycle_budget_exhausted': 514}
- Enregistrements de la session : 297821 ; net attendu > 0 : 255 ; simulés (eth_call de la vraie tx) : 23 (ok 22, échec 1) ; étiquettes ghost N+1 : 0/12 positives
- Décisions : {'REJECTED': 297821} ; motifs de rejet : {'below_safety_margin': 201, 'negative_expected_net': 297566, 'p_lower_below_threshold': 245, 'reliability_not_demonstrated': 10, 'sim_below_estimate': 1, 'simulated_net_nonpositive': 1, 'simulation_failed': 1}

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
| 53249310 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 324.735296 USDC | 0.038887 USDC | 0.000000 USDC | 0.005696 USDC | 0.033191 USDC (0.0305 €) | — | 1.02 | 0.010 (n=30) | REJECTED | below_safety_margin(33191<64947), p_lower_below_threshold(0.01<0.75) |
| 53249310 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.137438 WETH | 0.000016 WETH | 0.000000 WETH | 0.000002 WETH | 0.000014 WETH (0.0305 €) | — | 1.02 | 0.010 (n=30) | REJECTED | below_safety_margin(14055263807266<27487672827153), p_lower_below_threshold(0.01<0.75) |
| 53249467 | cbBTC→[aerodrome_slipstream]→ZEN→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC | 0.002938 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0210 €) | — | 0.95 | 0.122 (n=443) | REJECTED | below_safety_margin(28<58), p_lower_below_threshold(0.12<0.75) |
| 53249466 | cbBTC→[aerodrome_slipstream]→ZEN→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC | 0.002938 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0210 €) | — | 0.95 | 0.122 (n=443) | REJECTED | below_safety_margin(28<58), p_lower_below_threshold(0.12<0.75) |
| 53249467 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→ZEN→[aerodrome_slipstream]→WETH | 0.102361 WETH | 0.000013 WETH | 0.000000 WETH | 0.000003 WETH | 0.000010 WETH (0.0207 €) | — | 0.93 | 0.122 (n=443) | REJECTED | below_safety_margin(9515464382105<20472240450631), p_lower_below_threshold(0.12<0.75) |
| 53249466 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→ZEN→[aerodrome_slipstream]→WETH | 0.102361 WETH | 0.000013 WETH | 0.000000 WETH | 0.000003 WETH | 0.000010 WETH (0.0207 €) | — | 0.93 | 0.122 (n=443) | REJECTED | below_safety_margin(9515464382105<20472240450631), p_lower_below_threshold(0.12<0.75) |
| 53249310 | WETH→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.217061 WETH | 0.000012 WETH | 0.000000 WETH | 0.000003 WETH | 0.000008 WETH (0.0184 €) | — | 0.39 | 0.122 (n=443) | REJECTED | below_safety_margin(8473894030469<43412147386226), p_lower_below_threshold(0.12<0.75) |
| 53249310 | USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 529.785663 USDC | 0.027028 USDC | 0.000000 USDC | 0.007139 USDC | 0.019889 USDC (0.0183 €) | — | 0.38 | 0.122 (n=443) | REJECTED | below_safety_margin(19889<105957), p_lower_below_threshold(0.12<0.75) |
| 53249310 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→cbBTC | 0.004662 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0180 €) | — | 0.51 | 0.122 (n=443) | REJECTED | below_safety_margin(24<93), p_lower_below_threshold(0.12<0.75) |
| 53250024 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 41.070768 USDC | 0.021435 USDC | 0.000000 USDC | 0.005349 USDC | 0.016086 USDC (0.0148 €) | — | 3.92 | 0.009 (n=160) | REJECTED | p_lower_below_threshold(0.01<0.75) |
| 53250024 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.017339 WETH | 0.000009 WETH | 0.000000 WETH | 0.000002 WETH | 0.000007 WETH (0.0148 €) | 0.000007 WETH | 3.92 | 0.009 (n=160) | REJECTED | p_lower_below_threshold(0.01<0.75) |
| 53250024 | USDC→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→USDC | 37.905470 USDC | 0.018283 USDC | 0.000000 USDC | 0.005349 USDC | 0.012934 USDC (0.0119 €) | — | 3.41 | 0.058 (n=49) | REJECTED | p_lower_below_threshold(0.06<0.75) |
| 53250024 | WETH→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→WETH | 0.016077 WETH | 0.000008 WETH | 0.000000 WETH | 0.000002 WETH | 0.000005 WETH (0.0119 €) | 0.000005 WETH | 3.40 | 0.058 (n=49) | REJECTED | p_lower_below_threshold(0.06<0.75) |
| 53250024 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 37.309584 USDC | 0.018207 USDC | 0.000000 USDC | 0.005349 USDC | 0.012858 USDC (0.0118 €) | — | 3.45 | 0.058 (n=49) | REJECTED | p_lower_below_threshold(0.06<0.75) |
| 53250024 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.015754 WETH | 0.000008 WETH | 0.000000 WETH | 0.000002 WETH | 0.000005 WETH (0.0118 €) | 0.000005 WETH | 3.45 | 0.058 (n=49) | REJECTED | p_lower_below_threshold(0.06<0.75) |
| 53249310 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→USDC | 122.287683 USDC | 0.019422 USDC | 0.000000 USDC | 0.007139 USDC | 0.012283 USDC (0.0113 €) | — | 1.00 | 0.122 (n=443) | REJECTED | below_safety_margin(12283<24457), p_lower_below_threshold(0.12<0.75) |
| 53249310 | cbBTC→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.001327 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0112 €) | — | 1.13 | 0.122 (n=443) | REJECTED | below_safety_margin(15<26), p_lower_below_threshold(0.12<0.75) |
| 53249310 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→WETH | 0.051430 WETH | 0.000008 WETH | 0.000000 WETH | 0.000003 WETH | 0.000005 WETH (0.0112 €) | — | 1.00 | 0.122 (n=443) | REJECTED | below_safety_margin(5162979700027<10286001621156), p_lower_below_threshold(0.12<0.75) |

## Fiabilité et décision
- Observations ghost : 3159 ; taux observé 0.099 ; borne inférieure crédible (0.9) 0.093 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 9.3% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ✅ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
