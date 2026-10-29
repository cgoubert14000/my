# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-29T15:40:10+00:00 ; durée 27.4 min ; blocs 53248705 → 53249530 (819 vus)

## Connexion
- Requêtes RPC : 9849 ; erreurs : 4 ; latence p50/p95 : 224.2/1,218.4 ms
- Rafraîchissements d'état : 819 ; âge des données au dernier bloc : 2.83 s ; changements de frais LP observés (pools à frais dynamiques) : 2189
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 17180 ; cycles déclenchés par événement : 1004 ; avance médiane sur le rafraîchissement multicall : 392 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,360.62 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 517 pools, 297 jetons, 19072 routes
- Par DEX : uniswap_v3 146, aerodrome_slipstream 120, aerodrome 208, pancakeswap_v3 29, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 182 (rejetés 2) → 587 jetons ; pools candidats 3756 (énumérés 327, par paires 0), mesurés 519, sous le plancher de 10000.0 $ : 2 → gardés 517 (max 1500) ; prix des hubs : {'USDC': 1.0, 'USDbC': 1.0, 'DAI': 1.0, 'WETH': 2355.875591, 'cbBTC': 81334.783192, 'AERO': 0.704357}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 158,941,173 | 2,360.620796 | 53249531 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,703,456 | 0.028981 | 53249531 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,795,068 | 0.000012 | 53249531 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,580,823 | 0.028943 | 53249531 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| aerodrome | WETH/VVV | 3000 | 8,507,789 | 93.303251 | 53249531 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/USDC | 500 | 8,342,989 | 2,363.378287 | 53249531 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,089,293 | 0.001640 | 53249531 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 6,557,084 | 1.414722 | 53249531 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,823,427 | 0.028991 | 53249531 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/USDC | 150 | 4,490,111 | 2,362.934754 | 53249531 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,451,079 | 2,362.884047 | 53249531 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,288,746 | 0.998884 | 53249531 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,727,913 | 37,527.502874 | 53249531 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,922,563 | 0.028948 | 53249531 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2766 | 2,577,814 | 93.319227 | 53249531 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | WETH/FAI | 10000 | 2,153,779 | 1,217,921.572386 | 53249531 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 472 | 2,121,792 | 0.000012 | 53249531 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome | WETH/USDC | 3000 | 1,830,633 | 2,361.349720 | 53249531 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,811,529 | 391.817209 | 53249531 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | XDP/USDC | 100 | 1,798,041 | 0.018784 | 53249531 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,795,459 | 0.000000 | 53249531 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,721,820 | 0.000012 | 53249531 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,712,483 | 0.000012 | 53249531 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | USDC/cbBTC | 344 | 1,615,392 | 0.000012 | 53249531 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,514,127 | 1.588199 | 53249531 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | WETH/AERO | 3000 | 1,473,979 | 3,342.824564 | 53249531 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,460,128 | 0.827412 | 53249531 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,420,375 | 0.005346 | 53249531 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,411,837 | 13,506.753654 | 53249531 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,278,925 | 2,363.329948 | 53249531 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,252,996 | 0.000264 | 53249531 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | USDC/SEND | 3000 | 1,181,925 | 69.560411 | 53249531 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,158,378 | 37,129,645.324049 | 53249531 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | WETH/WELL | 10000 | 1,153,778 | 1,096,975.523434 | 53249531 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,122,680 | 503,241.116868 | 53249531 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,089,256 | 0.000000 | 53249531 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,071,253 | 21,687,126.272257 | 53249531 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | USDC/VVV | 3000 | 1,063,819 | 0.039500 | 53249531 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | WETH/EDEL | 7000 | 1,063,168 | 75,267.027949 | 53249531 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,058,374 | 16.204996 | 53249531 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | VIRTUAL/WETH | 10000 | 1,052,064 | 0.000263 | 53249531 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome | WETH/AERO | 10000 | 1,037,825 | 3,364.813352 | 53249531 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v2 | WETH/USDC | 3000 | 1,034,657 | 2,360.187273 | 53249531 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| uniswap_v3 | WETH/VVV | 10000 | 1,033,294 | 93.429745 | 53249531 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome | USDC/NOCK | 3000 | 1,003,632 | 62.148363 | 53249531 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/USDC | 10000 | 942,613 | 2,344.485327 | 53249531 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 940,274 | 1,045.695095 | 53249531 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | uXRP/WETH | 3000 | 905,893 | 0.000552 | 53249531 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | USDC/SAPIEN | 4530 | 883,806 | 17.836456 | 53249531 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 860,350 | 17.345360 | 53249531 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| pancakeswap_v3 | QUID/USDC | 100 | 851,189 | 0.065547 | 53249531 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 799,030 | 0.803616 | 53249531 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| aerodrome_slipstream | AERO/cbBTC | 2700 | 761,384 | 0.000009 | 53249531 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 758,465 | 4,574,370.760358 | 53249531 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 752,587 | 0.623491 | 53249531 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| aerodrome | WETH/msETH (stable) | 500 | 717,654 | 2.337667 | 53249531 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v2 | WETH/NPC | 3000 | 702,435 | 142,261.334308 | 53249531 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 699,818 | 499,659.654013 | 53249531 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | TIG/USDC | 10000 | 650,911 | 0.534773 | 53249531 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 637,947 | 0.099410 | 53249531 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |

## Recherche d'opportunités
- Cycles : 1822 ; routes examinées : 34749184 ; candidats optimisés : 126575 ; net attendu > 0 : 99 ; dernier cycle 96.4 ms
- Rejets (moteur) : {'spread_below_threshold': 34184358, 'liquidity_below_min': 428069, 'negative_expected_net': 126476, 'borrow_bound_too_small': 9928, 'cycle_budget_exhausted': 254}
- Enregistrements de la session : 126575 ; net attendu > 0 : 99 ; simulés (eth_call de la vraie tx) : 0 (ok 0, échec 0) ; étiquettes ghost N+1 : 0/0 positives
- Décisions : {'REJECTED': 126575} ; motifs de rejet : {'below_safety_margin': 99, 'negative_expected_net': 126476, 'p_lower_below_threshold': 91, 'reliability_not_demonstrated': 8}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53249310 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 2,657.466186 USDC | 0.433718 USDC | 0.000000 USDC | 0.006054 USDC | 0.427664 USDC (0.3935 €) | — | 1.61 | 0.030 (n=118) | REJECTED | below_safety_margin(427664<531493), p_lower_below_threshold(0.03<0.75) |
| 53249310 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 1.126445 WETH | 0.000184 WETH | 0.000000 WETH | 0.000003 WETH | 0.000181 WETH (0.3929 €) | — | 1.61 | 0.030 (n=118) | REJECTED | below_safety_margin(181167683598700<225288950635663), p_lower_below_threshold(0.03<0.75) |
| 53249310 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.013590 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1146 €) | — | 1.13 | 0.122 (n=443) | REJECTED | below_safety_margin(153<271), p_lower_below_threshold(0.12<0.75) |
| 53249310 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 1,189.058784 USDC | 0.131434 USDC | 0.000000 USDC | 0.007139 USDC | 0.124295 USDC (0.1144 €) | — | 1.05 | 0.122 (n=443) | REJECTED | below_safety_margin(124295<237811), p_lower_below_threshold(0.12<0.75) |
| 53249310 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.503881 WETH | 0.000056 WETH | 0.000000 WETH | 0.000003 WETH | 0.000053 WETH (0.1142 €) | — | 1.05 | 0.122 (n=443) | REJECTED | below_safety_margin(52671607234772<100776154603833), p_lower_below_threshold(0.12<0.75) |
| 53249310 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 324.735296 USDC | 0.038887 USDC | 0.000000 USDC | 0.005696 USDC | 0.033191 USDC (0.0305 €) | — | 1.02 | 0.010 (n=30) | REJECTED | below_safety_margin(33191<64947), p_lower_below_threshold(0.01<0.75) |
| 53249310 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.137438 WETH | 0.000016 WETH | 0.000000 WETH | 0.000002 WETH | 0.000014 WETH (0.0305 €) | — | 1.02 | 0.010 (n=30) | REJECTED | below_safety_margin(14055263807266<27487672827153), p_lower_below_threshold(0.01<0.75) |
| 53249467 | cbBTC→[aerodrome_slipstream]→ZEN→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC | 0.002938 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0210 €) | — | 0.95 | 0.122 (n=443) | REJECTED | below_safety_margin(28<58), p_lower_below_threshold(0.12<0.75) |
| 53249466 | cbBTC→[aerodrome_slipstream]→ZEN→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC | 0.002938 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0210 €) | — | 0.95 | 0.122 (n=443) | REJECTED | below_safety_margin(28<58), p_lower_below_threshold(0.12<0.75) |
| 53249467 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→ZEN→[aerodrome_slipstream]→WETH | 0.102361 WETH | 0.000013 WETH | 0.000000 WETH | 0.000003 WETH | 0.000010 WETH (0.0207 €) | — | 0.93 | 0.122 (n=443) | REJECTED | below_safety_margin(9515464382105<20472240450631), p_lower_below_threshold(0.12<0.75) |
| 53249466 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→ZEN→[aerodrome_slipstream]→WETH | 0.102361 WETH | 0.000013 WETH | 0.000000 WETH | 0.000003 WETH | 0.000010 WETH (0.0207 €) | — | 0.93 | 0.122 (n=443) | REJECTED | below_safety_margin(9515464382105<20472240450631), p_lower_below_threshold(0.12<0.75) |
| 53249310 | WETH→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.217061 WETH | 0.000012 WETH | 0.000000 WETH | 0.000003 WETH | 0.000008 WETH (0.0184 €) | — | 0.39 | 0.122 (n=443) | REJECTED | below_safety_margin(8473894030469<43412147386226), p_lower_below_threshold(0.12<0.75) |
| 53249310 | USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 529.785663 USDC | 0.027028 USDC | 0.000000 USDC | 0.007139 USDC | 0.019889 USDC (0.0183 €) | — | 0.38 | 0.122 (n=443) | REJECTED | below_safety_margin(19889<105957), p_lower_below_threshold(0.12<0.75) |
| 53249310 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→cbBTC | 0.004662 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0180 €) | — | 0.51 | 0.122 (n=443) | REJECTED | below_safety_margin(24<93), p_lower_below_threshold(0.12<0.75) |
| 53249310 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→USDC | 122.287683 USDC | 0.019422 USDC | 0.000000 USDC | 0.007139 USDC | 0.012283 USDC (0.0113 €) | — | 1.00 | 0.122 (n=443) | REJECTED | below_safety_margin(12283<24457), p_lower_below_threshold(0.12<0.75) |
| 53249310 | cbBTC→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.001327 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0112 €) | — | 1.13 | 0.122 (n=443) | REJECTED | below_safety_margin(15<26), p_lower_below_threshold(0.12<0.75) |
| 53249310 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→WETH | 0.051430 WETH | 0.000008 WETH | 0.000000 WETH | 0.000003 WETH | 0.000005 WETH (0.0112 €) | — | 1.00 | 0.122 (n=443) | REJECTED | below_safety_margin(5162979700027<10286001621156), p_lower_below_threshold(0.12<0.75) |
| 53249467 | cbBTC→[aerodrome_slipstream]→ZEN→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→cbBTC | 0.001264 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0097 €) | — | 1.03 | 0.164 (n=224) | REJECTED | below_safety_margin(13<25), p_lower_below_threshold(0.16<0.75) |
| 53249466 | cbBTC→[aerodrome_slipstream]→ZEN→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→cbBTC | 0.001264 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0097 €) | — | 1.03 | 0.164 (n=224) | REJECTED | below_safety_margin(13<25), p_lower_below_threshold(0.16<0.75) |
| 53249467 | WETH→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→ZEN→[aerodrome_slipstream]→WETH | 0.041164 WETH | 0.000007 WETH | 0.000000 WETH | 0.000003 WETH | 0.000004 WETH (0.0091 €) | — | 1.02 | 0.164 (n=224) | REJECTED | below_safety_margin(4185240416947<8232714773796), p_lower_below_threshold(0.16<0.75) |
| 53249466 | WETH→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→ZEN→[aerodrome_slipstream]→WETH | 0.041164 WETH | 0.000007 WETH | 0.000000 WETH | 0.000003 WETH | 0.000004 WETH (0.0091 €) | — | 1.02 | 0.164 (n=224) | REJECTED | below_safety_margin(4185240416947<8232714773796), p_lower_below_threshold(0.16<0.75) |
| 53249310 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.002470 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0082 €) | — | 0.45 | 0.122 (n=443) | REJECTED | below_safety_margin(11<49), p_lower_below_threshold(0.12<0.75) |
| 53249310 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 190.531620 USDC | 0.015653 USDC | 0.000000 USDC | 0.007139 USDC | 0.008514 USDC (0.0078 €) | — | 0.45 | 0.122 (n=443) | REJECTED | below_safety_margin(8514<38106), p_lower_below_threshold(0.12<0.75) |
| 53249310 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.086116 WETH | 0.000007 WETH | 0.000000 WETH | 0.000003 WETH | 0.000004 WETH (0.0078 €) | — | 0.42 | 0.122 (n=443) | REJECTED | below_safety_margin(3589533570563<17223135264826), p_lower_below_threshold(0.12<0.75) |
| 53249348 | USDC→[aerodrome_slipstream]→EURC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 58.175196 USDC | 0.015496 USDC | 0.000000 USDC | 0.007141 USDC | 0.008355 USDC (0.0077 €) | — | 1.44 | 0.122 (n=443) | REJECTED | below_safety_margin(8355<11635), p_lower_below_threshold(0.12<0.75) |

## Fiabilité et décision
- Observations ghost : 3147 ; taux observé 0.100 ; borne inférieure crédible (0.9) 0.093 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 9.3% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
