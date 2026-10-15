# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-15T17:30:38+00:00 ; durée 242.04 min ; blocs 52640781 → 52648041 (6276 vus)

## Connexion
- Requêtes RPC : 82205 ; erreurs : 515 ; latence p50/p95 : 177.8/1,625.8 ms
- Rafraîchissements d'état : 6276 ; âge des données au dernier bloc : 3.06 s ; changements de frais LP observés (pools à frais dynamiques) : 28060
- Flux d'événements (WebSocket Swap/Sync) : non connecté ; événements appliqués : 0 ; cycles déclenchés par événement : 0 ; avance médiane sur le rafraîchissement multicall : — ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,448.22 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 570 pools, 326 jetons, 21328 routes
- Par DEX : uniswap_v3 136, aerodrome 235, aerodrome_slipstream 152, pancakeswap_v3 30, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 205 (rejetés 2) → 610 jetons ; pools candidats 3864 (énumérés 389, par paires 0), mesurés 572, sous le plancher de 10000.0 $ : 2 → gardés 570 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDC': 1.0, 'USDbC': 1.0, 'WETH': 2346.001193, 'AERO': 0.837627, 'cbBTC': 80168.530844}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 146,652,130 | 2,448.224520 | 52648042 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 45,422,616 | 1.115544 | 52648042 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 19,301,525 | 0.029688 | 52648042 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 500 | 18,439,173 | 0.029678 | 52648042 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 16,887,677 | 97.653739 | 52648042 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,608,278 | 0.029675 | 52648042 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,768,675 | 0.000012 | 52648042 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 9,133,807 | 2,442.559427 | 52648042 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome_slipstream | USDC/cbBTC | 340 | 8,005,439 | 0.000012 | 52648042 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 758 | 7,934,742 | 2,441.881358 | 52648042 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,266,415 | 0.001680 | 52648042 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 448 | 6,542,000 | 0.000012 | 52648042 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome_slipstream | USDC/AERO | 10000 | 5,890,831 | 1.119479 | 52648042 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome | WETH/USDC | 3000 | 5,446,477 | 2,448.713218 | 52648042 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,388,868 | 0.029667 | 52648042 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | fBOMB/AERO | 10000 | 5,380,222 | 0.025943 | 52648042 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,749,915 | 0.000278 | 52648042 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,739,730 | 0.802387 | 52648042 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,352,515 | 0.997987 | 52648042 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,345,773 | 2,442.215161 | 52648042 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | WETH/KTA | 3000 | 4,020,033 | 35,177.636318 | 52648042 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/AERO | 10000 | 3,518,357 | 2,737.412797 | 52648042 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,853,189 | 0.000012 | 52648042 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,756,375 | 404.276833 | 52648042 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 2,690,464 | 1,012.696920 | 52648042 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome_slipstream | WETH/VVV | 2709 | 2,689,195 | 97.650145 | 52648042 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,558,760 | 1.141860 | 52648042 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 2,556,721 | 0.000011 | 52648042 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | WETH/FAI | 10000 | 2,265,668 | 1,185,321.709395 | 52648042 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,111,377 | 1.196132 | 52648042 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | BNKR/WETH | 10000 | 2,079,372 | 0.000000 | 52648042 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome_slipstream | WETH/USDT | 442 | 2,053,259 | 2,446.118407 | 52648042 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,008,820 | 1.403288 | 52648042 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,858,976 | 15.666005 | 52648042 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | fBOMB/USDC | 10000 | 1,832,466 | 0.022977 | 52648042 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| uniswap_v3 | XDP/USDC | 100 | 1,787,904 | 0.018985 | 52648042 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,783,278 | 0.000012 | 52648042 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,762,066 | 13,620.413927 | 52648042 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/msETH (stable) | 500 | 1,732,012 | 2.308044 | 52648042 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | WETH/AERO | 3000 | 1,552,144 | 2,727.284691 | 52648042 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | weETH_04c0/WETH | 500 | 1,513,714 | 1.105494 | 52648042 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,457,096 | 0.831352 | 52648042 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | WETH/AERO | 3000 | 1,392,779 | 2,729.005902 | 52648042 | `0x82321f3BEB69f503380D6B233857d5C43562e2D0` |
| uniswap_v3 | DRB/WETH | 10000 | 1,381,150 | 0.000000 | 52648042 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,368,445 | 23.143994 | 52648042 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,331,274 | 0.000278 | 52648042 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,309,192 | 0.004593 | 52648042 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,249,531 | 0.916559 | 52648042 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| aerodrome | USDC/SEND | 3000 | 1,248,967 | 62.293193 | 52648042 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome_slipstream | EURC/USDC | 73 | 1,243,918 | 1.120921 | 52648042 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,219,922 | 2,442.560906 | 52648042 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,213,513 | 1.105591 | 52648042 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |
| aerodrome_slipstream | WETH/msETH | 500 | 1,213,050 | 1.131835 | 52648042 | `0x74F72788F4814D7fF3C49B44684aa98Eee140C0E` |
| uniswap_v3 | WETH/doginme | 10000 | 1,209,464 | 35,805,084.475842 | 52648042 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | WETH/WELL | 10000 | 1,181,114 | 1,165,116.220246 | 52648042 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,170,647 | 493,778.274137 | 52648042 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | WETH/cbBTC | 3000 | 1,170,239 | 0.029671 | 52648042 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,122,464 | 13.986181 | 52648042 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | WETH/EDEL | 7000 | 1,119,670 | 83,195.028670 | 52648042 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,118,250 | 0.436741 | 52648042 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |

## Recherche d'opportunités
- Cycles : 6275 ; routes examinées : 133833200 ; candidats optimisés : 884632 ; net attendu > 0 : 1591 ; dernier cycle 492.8 ms
- Rejets (moteur) : {'spread_below_threshold': 131292797, 'liquidity_below_min': 1367406, 'negative_expected_net': 883041, 'pool_quarantined': 156410, 'borrow_bound_too_small': 111169, 'unquotable': 13728, 'cycle_budget_exhausted': 7058}
- Enregistrements de la session : 884632 ; net attendu > 0 : 1591 ; simulés (eth_call de la vraie tx) : 119 (ok 91, échec 28) ; étiquettes ghost N+1 : 6/97 positives
- Décisions : {'REJECTED': 884632} ; motifs de rejet : {'below_safety_margin': 856, 'negative_expected_net': 883041, 'p_lower_below_threshold': 605, 'price_impact': 98, 'reliability_not_demonstrated': 986, 'simulation_failed': 28, 'stale_data': 239}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52642035 | USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 442.062489 USDC | 0.298836 USDC | 0.000000 USDC | 0.008229 USDC | 0.290607 USDC (0.2674 €) | — | 6.57 | 0.164 (n=42) | REJECTED | p_lower_below_threshold(0.16<0.75) |
| 52642035 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH | 0.186091 WETH | 0.000126 WETH | 0.000000 WETH | 0.000003 WETH | 0.000122 WETH (0.2667 €) | 0.000122 WETH | 6.57 | 0.164 (n=42) | REJECTED | p_lower_below_threshold(0.16<0.75) |
| 52643960 | USDC→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC | 2,414.723624 USDC | 0.292685 USDC | 0.000000 USDC | 0.007510 USDC | 0.285175 USDC (0.2624 €) | — | 1.18 | 0.241 (n=29) | REJECTED | below_safety_margin(285175<482944), reliability_not_demonstrated |
| 52643960 | WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→WETH | 0.998317 WETH | 0.000121 WETH | 0.000000 WETH | 0.000003 WETH | 0.000118 WETH (0.2622 €) | — | 1.18 | 0.241 (n=29) | REJECTED | below_safety_margin(117845714349323<199663382839724), reliability_not_demonstrated |
| 52643631 | USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 402.676128 USDC | 0.291853 USDC | 0.000000 USDC | 0.007764 USDC | 0.284089 USDC (0.2614 €) | — | 7.06 | 0.324 (n=17) | REJECTED | stale_data(4844ms>4000.0), reliability_not_demonstrated |
| 52643631 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH | 0.167552 WETH | 0.000121 WETH | 0.000000 WETH | 0.000003 WETH | 0.000118 WETH (0.2605 €) | 0.000118 WETH | 7.05 | 0.324 (n=17) | REJECTED | stale_data(4838ms>4000.0), reliability_not_demonstrated |
| 52642035 | USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 420.852464 USDC | 0.288482 USDC | 0.000000 USDC | 0.007844 USDC | 0.280638 USDC (0.2582 €) | — | 6.67 | 0.164 (n=42) | REJECTED | p_lower_below_threshold(0.16<0.75) |
| 52642035 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH | 0.177158 WETH | 0.000121 WETH | 0.000000 WETH | 0.000003 WETH | 0.000118 WETH (0.2575 €) | 0.000118 WETH | 6.66 | 0.164 (n=42) | REJECTED | p_lower_below_threshold(0.16<0.75) |
| 52643631 | USDC→[aerodrome_slipstream]→USDT→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 448.930237 USDC | 0.265334 USDC | 0.000000 USDC | 0.007399 USDC | 0.257935 USDC (0.2373 €) | — | 5.75 | 0.324 (n=17) | REJECTED | stale_data(4899ms>4000.0), reliability_not_demonstrated |
| 52643631 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→USDT→[uniswap_v3]→WETH | 0.186788 WETH | 0.000110 WETH | 0.000000 WETH | 0.000003 WETH | 0.000107 WETH (0.2366 €) | 0.000107 WETH | 5.75 | 0.324 (n=17) | REJECTED | stale_data(4893ms>4000.0), reliability_not_demonstrated |
| 52646659 | WETH→[aerodrome_slipstream]→doginme→[aerodrome]→WETH | 0.024369 WETH | 0.000100 WETH | 0.000000 WETH | 0.000002 WETH | 0.000098 WETH (0.2188 €) | 0.000098 WETH | 40.19 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52643631 | cbBTC→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→cbBTC | 0.009293 cbBTC | 0.000003 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000003 cbBTC (0.2117 €) | — | 3.03 | 0.324 (n=17) | REJECTED | stale_data(5421ms>4000.0), reliability_not_demonstrated |
| 52643631 | cbBTC→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→cbBTC | 0.009293 cbBTC | 0.000003 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000003 cbBTC (0.2117 €) | — | 3.03 | 0.324 (n=17) | REJECTED | stale_data(5453ms>4000.0), reliability_not_demonstrated |
| 52643631 | USDC→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 796.521943 USDC | 0.238242 USDC | 0.000000 USDC | 0.008129 USDC | 0.230113 USDC (0.2117 €) | — | 2.89 | 0.251 (n=28) | REJECTED | stale_data(5446ms>4000.0), reliability_not_demonstrated |
| 52643631 | USDC→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 796.568874 USDC | 0.238083 USDC | 0.000000 USDC | 0.008129 USDC | 0.229954 USDC (0.2116 €) | — | 2.89 | 0.251 (n=28) | REJECTED | stale_data(5434ms>4000.0), reliability_not_demonstrated |
| 52643631 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→WETH | 0.322276 WETH | 0.000099 WETH | 0.000000 WETH | 0.000003 WETH | 0.000096 WETH (0.2113 €) | 0.000096 WETH | 2.97 | 0.251 (n=28) | REJECTED | stale_data(5440ms>4000.0), reliability_not_demonstrated |
| 52643631 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→WETH | 0.310416 WETH | 0.000099 WETH | 0.000000 WETH | 0.000003 WETH | 0.000096 WETH (0.2107 €) | — | 3.08 | 0.324 (n=17) | REJECTED | stale_data(5427ms>4000.0), reliability_not_demonstrated |
| 52643631 | USDC→[pancakeswap_v3]→USDT→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 400.018425 USDC | 0.223531 USDC | 0.000000 USDC | 0.007399 USDC | 0.216132 USDC (0.1988 €) | — | 5.40 | 0.152 (n=45) | REJECTED | stale_data(4979ms>4000.0), p_lower_below_threshold(0.15<0.75) |
| 52643631 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→USDT→[uniswap_v3]→WETH | 0.166652 WETH | 0.000093 WETH | 0.000000 WETH | 0.000003 WETH | 0.000090 WETH (0.1982 €) | — | 5.40 | 0.152 (n=45) | REJECTED | stale_data(4973ms>4000.0), p_lower_below_threshold(0.15<0.75) |
| 52643631 | USDC→[uniswap_v3]→USDT→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 403.086292 USDC | 0.215122 USDC | 0.000000 USDC | 0.007399 USDC | 0.207723 USDC (0.1911 €) | — | 5.15 | 0.324 (n=17) | REJECTED | stale_data(5023ms>4000.0), reliability_not_demonstrated |
| 52642968 | WETH→[aerodrome_slipstream]→AERO→[aerodrome]→BRETT→[uniswap_v3]→WETH | 0.021903 WETH | 0.000090 WETH | 0.000000 WETH | 0.000003 WETH | 0.000087 WETH (0.1910 €) | 0.000087 WETH | 39.89 | 0.102 (n=3) | REJECTED | reliability_not_demonstrated |
| 52643631 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→USDT→[uniswap_v3]→WETH | 0.167680 WETH | 0.000090 WETH | 0.000000 WETH | 0.000003 WETH | 0.000086 WETH (0.1905 €) | — | 5.15 | 0.324 (n=17) | REJECTED | stale_data(5018ms>4000.0), reliability_not_demonstrated |
| 52642968 | WETH→[pancakeswap_v3]→AERO→[aerodrome]→BRETT→[uniswap_v3]→WETH | 0.021775 WETH | 0.000090 WETH | 0.000000 WETH | 0.000003 WETH | 0.000087 WETH (0.1903 €) | 0.000087 WETH | 40.00 | 0.003 (n=2) | REJECTED | reliability_not_demonstrated |
| 52642968 | WETH→[uniswap_v3]→AERO→[aerodrome]→BRETT→[uniswap_v3]→WETH | 0.020798 WETH | 0.000082 WETH | 0.000000 WETH | 0.000003 WETH | 0.000079 WETH (0.1724 €) | 0.000079 WETH | 37.92 | 0.102 (n=3) | REJECTED | reliability_not_demonstrated |
| 52642035 | USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 307.929676 USDC | 0.182750 USDC | 0.000000 USDC | 0.007844 USDC | 0.174906 USDC (0.1609 €) | — | 5.68 | 0.346 (n=16) | REJECTED | reliability_not_demonstrated |

## Fiabilité et décision
- Observations ghost : 375 ; taux observé 0.155 ; borne inférieure crédible (0.9) 0.132 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 13.2% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ✅ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
