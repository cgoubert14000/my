# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-15T18:46:52+00:00 ; durée 318.28 min ; blocs 52640781 → 52650328 (8256 vus)

## Connexion
- Requêtes RPC : 108575 ; erreurs : 515 ; latence p50/p95 : 176.3/1,555.8 ms
- Rafraîchissements d'état : 8257 ; âge des données au dernier bloc : 2.09 s ; changements de frais LP observés (pools à frais dynamiques) : 32617
- Flux d'événements (WebSocket Swap/Sync) : non connecté ; événements appliqués : 0 ; cycles déclenchés par événement : 0 ; avance médiane sur le rafraîchissement multicall : — ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,440.95 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 570 pools, 326 jetons, 21328 routes
- Par DEX : uniswap_v3 136, aerodrome 235, aerodrome_slipstream 152, pancakeswap_v3 30, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 205 (rejetés 2) → 610 jetons ; pools candidats 3864 (énumérés 389, par paires 0), mesurés 572, sous le plancher de 10000.0 $ : 2 → gardés 570 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDC': 1.0, 'USDbC': 1.0, 'WETH': 2346.001193, 'AERO': 0.837627, 'cbBTC': 80168.530844}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 146,416,210 | 2,440.946970 | 52650328 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 45,357,588 | 1.119558 | 52650328 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 500 | 18,406,326 | 0.029740 | 52650328 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 16,893,805 | 97.003685 | 52650328 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 11,935,287 | 0.029688 | 52650328 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,567,747 | 0.029675 | 52650328 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,736,250 | 0.000012 | 52650328 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 9,113,699 | 2,446.915700 | 52650328 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome_slipstream | USDC/cbBTC | 340 | 7,990,262 | 0.000012 | 52650328 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 728 | 7,927,443 | 2,447.229775 | 52650328 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | USDC/cbBTC | 460 | 7,760,984 | 0.000012 | 52650328 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,227,299 | 0.001678 | 52650328 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/AERO | 10000 | 5,670,660 | 1.126629 | 52650328 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome | WETH/USDC | 3000 | 5,438,384 | 2,441.827416 | 52650328 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,378,525 | 0.029750 | 52650328 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | fBOMB/AERO | 10000 | 5,280,188 | 0.024842 | 52650328 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,735,102 | 0.000278 | 52650328 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,725,677 | 0.802398 | 52650328 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,354,546 | 2,447.008820 | 52650328 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,330,471 | 0.997989 | 52650328 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,976,343 | 35,741.469828 | 52650328 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDT | 436 | 3,667,446 | 2,450.459865 | 52650328 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome | WETH/AERO | 10000 | 3,506,843 | 2,753.165172 | 52650328 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | WETH/MORPHO | 2781 | 3,150,915 | 1,014.438760 | 52650328 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,844,860 | 0.000012 | 52650328 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/VVV | 2724 | 2,683,039 | 97.033876 | 52650328 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 2,579,218 | 0.000011 | 52650328 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,557,535 | 402.921819 | 52650328 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,551,194 | 1.141629 | 52650328 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| aerodrome | WETH/FAI | 10000 | 2,260,581 | 1,183,594.563434 | 52650328 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,111,377 | 1.196132 | 52650328 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | BNKR/WETH | 10000 | 2,079,078 | 0.000000 | 52650328 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,008,820 | 1.403288 | 52650328 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,967,877 | 15.696131 | 52650328 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | fBOMB/USDC | 10000 | 1,801,799 | 0.022211 | 52650328 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| uniswap_v3 | XDP/USDC | 100 | 1,791,826 | 0.019036 | 52650328 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,780,688 | 13,563.497464 | 52650328 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,778,472 | 0.000012 | 52650328 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | WETH/msETH (stable) | 500 | 1,680,951 | 2.307697 | 52650328 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | WETH/AERO | 3000 | 1,557,007 | 2,733.629482 | 52650328 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | weETH_04c0/WETH | 500 | 1,509,214 | 1.105494 | 52650328 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,458,943 | 0.828028 | 52650328 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | WETH/AERO | 3012 | 1,389,424 | 2,733.853220 | 52650328 | `0x82321f3BEB69f503380D6B233857d5C43562e2D0` |
| uniswap_v3 | DRB/WETH | 10000 | 1,385,544 | 0.000000 | 52650328 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,364,886 | 23.176989 | 52650328 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,364,260 | 0.004873 | 52650328 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,327,128 | 0.000279 | 52650328 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,282,997 | 0.916559 | 52650328 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| aerodrome_slipstream | EURC/USDC | 73 | 1,260,161 | 1.121274 | 52650328 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| aerodrome | USDC/SEND | 3000 | 1,248,967 | 62.293193 | 52650328 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,227,025 | 2,446.702373 | 52650328 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,210,805 | 1.105591 | 52650328 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |
| uniswap_v3 | WETH/doginme | 10000 | 1,210,506 | 35,397,498.267493 | 52650328 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome_slipstream | WETH/msETH | 500 | 1,196,805 | 1.131929 | 52650328 | `0x74F72788F4814D7fF3C49B44684aa98Eee140C0E` |
| aerodrome | WETH/WELL | 10000 | 1,188,561 | 1,143,730.810941 | 52650328 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,167,212 | 493,727.267552 | 52650328 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | WETH/cbBTC | 3000 | 1,165,543 | 0.029671 | 52650328 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,163,855 | 0.436645 | 52650328 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,124,678 | 13.917940 | 52650328 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | WETH/EDEL | 7000 | 1,108,680 | 84,376.396889 | 52650328 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |

## Recherche d'opportunités
- Cycles : 8256 ; routes examinées : 176083968 ; candidats optimisés : 1124226 ; net attendu > 0 : 1656 ; dernier cycle 280.1 ms
- Rejets (moteur) : {'spread_below_threshold': 172768745, 'liquidity_below_min': 1873235, 'negative_expected_net': 1122570, 'pool_quarantined': 183450, 'borrow_bound_too_small': 113186, 'unquotable': 13802, 'cycle_budget_exhausted': 7324}
- Enregistrements de la session : 1124226 ; net attendu > 0 : 1656 ; simulés (eth_call de la vraie tx) : 133 (ok 96, échec 37) ; étiquettes ghost N+1 : 6/106 positives
- Décisions : {'REJECTED': 1124226} ; motifs de rejet : {'below_safety_margin': 862, 'negative_expected_net': 1122570, 'p_lower_below_threshold': 639, 'price_impact': 107, 'reliability_not_demonstrated': 1017, 'simulation_failed': 37, 'stale_data': 242}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52649351 | WETH→[pancakeswap_v3]→AERO→[aerodrome]→USDC→[pancakeswap_v3]→WETH | 0.454136 WETH | 0.000365 WETH | 0.000000 WETH | 0.000003 WETH | 0.000362 WETH (0.8127 €) | 0.000362 WETH | 7.96 | 0.001 (n=8) | REJECTED | reliability_not_demonstrated |
| 52649351 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→AERO→[aerodrome]→USDC | 1,105.915706 USDC | 0.888475 USDC | 0.000000 USDC | 0.007388 USDC | 0.881087 USDC (0.8106 €) | — | 7.97 | 0.001 (n=8) | REJECTED | reliability_not_demonstrated |
| 52649351 | WETH→[pancakeswap_v3]→AERO→[aerodrome]→USDC→[uniswap_v3]→WETH | 0.358389 WETH | 0.000299 WETH | 0.000000 WETH | 0.000003 WETH | 0.000296 WETH (0.6659 €) | 0.000296 WETH | 8.27 | 0.002 (n=3) | REJECTED | reliability_not_demonstrated |
| 52649351 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→AERO→[aerodrome]→USDC | 872.475491 USDC | 0.729196 USDC | 0.000000 USDC | 0.007017 USDC | 0.722179 USDC (0.6644 €) | — | 8.28 | 0.002 (n=3) | REJECTED | reliability_not_demonstrated |
| 52649351 | WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→WETH | 0.342414 WETH | 0.000198 WETH | 0.000000 WETH | 0.000002 WETH | 0.000196 WETH (0.4407 €) | 0.000196 WETH | 5.73 | 0.001 (n=11) | REJECTED | reliability_not_demonstrated |
| 52649351 | WETH→[pancakeswap_v3]→AERO→[aerodrome]→USDC→[aerodrome_slipstream]→WETH | 0.332901 WETH | 0.000186 WETH | 0.000000 WETH | 0.000003 WETH | 0.000183 WETH (0.4118 €) | — | 5.51 | 0.001 (n=9) | REJECTED | reliability_not_demonstrated |
| 52649351 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→AERO→[aerodrome]→USDC | 810.307855 USDC | 0.453657 USDC | 0.000000 USDC | 0.007017 USDC | 0.446640 USDC (0.4109 €) | — | 5.51 | 0.001 (n=9) | REJECTED | reliability_not_demonstrated |
| 52649351 | WETH→[pancakeswap_v3]→AERO→[aerodrome]→USDC→[uniswap_v3]→WETH | 0.285133 WETH | 0.000139 WETH | 0.000000 WETH | 0.000003 WETH | 0.000136 WETH (0.3059 €) | — | 4.77 | 0.001 (n=9) | REJECTED | reliability_not_demonstrated |
| 52649351 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→AERO→[aerodrome]→USDC | 694.169574 USDC | 0.338854 USDC | 0.000000 USDC | 0.007017 USDC | 0.331837 USDC (0.3053 €) | — | 4.78 | 0.001 (n=9) | REJECTED | reliability_not_demonstrated |
| 52649351 | WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.197196 WETH | 0.000126 WETH | 0.000000 WETH | 0.000003 WETH | 0.000123 WETH (0.2773 €) | — | 6.26 | 0.146 (n=47) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 52649351 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→USDC | 480.297597 USDC | 0.307931 USDC | 0.000000 USDC | 0.007354 USDC | 0.300577 USDC (0.2765 €) | — | 6.26 | 0.146 (n=47) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 52649351 | WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→wstETH→[uniswap_v3]→WETH | 0.135735 WETH | 0.000126 WETH | 0.000000 WETH | 0.000003 WETH | 0.000123 WETH (0.2758 €) | — | 9.04 | 0.001 (n=7) | REJECTED | reliability_not_demonstrated |
| 52642035 | USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 442.062489 USDC | 0.298836 USDC | 0.000000 USDC | 0.008229 USDC | 0.290607 USDC (0.2674 €) | — | 6.57 | 0.164 (n=42) | REJECTED | p_lower_below_threshold(0.16<0.75) |
| 52642035 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH | 0.186091 WETH | 0.000126 WETH | 0.000000 WETH | 0.000003 WETH | 0.000122 WETH (0.2667 €) | 0.000122 WETH | 6.57 | 0.164 (n=42) | REJECTED | p_lower_below_threshold(0.16<0.75) |
| 52649351 | WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→wstETH→[aerodrome_slipstream]→WETH | 0.133070 WETH | 0.000121 WETH | 0.000000 WETH | 0.000003 WETH | 0.000118 WETH (0.2641 €) | — | 8.83 | 0.001 (n=7) | REJECTED | reliability_not_demonstrated |
| 52649351 | WETH→[pancakeswap_v3]→AERO→[aerodrome]→USDC→[pancakeswap_v3]→WETH | 0.247371 WETH | 0.000120 WETH | 0.000000 WETH | 0.000003 WETH | 0.000117 WETH (0.2634 €) | — | 4.74 | 0.001 (n=8) | REJECTED | reliability_not_demonstrated |
| 52649351 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→AERO→[aerodrome]→USDC | 602.655975 USDC | 0.292740 USDC | 0.000000 USDC | 0.007017 USDC | 0.285723 USDC (0.2629 €) | — | 4.74 | 0.001 (n=8) | REJECTED | reliability_not_demonstrated |
| 52643960 | USDC→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC | 2,414.723624 USDC | 0.292685 USDC | 0.000000 USDC | 0.007510 USDC | 0.285175 USDC (0.2624 €) | — | 1.18 | 0.241 (n=29) | REJECTED | below_safety_margin(285175<482944), reliability_not_demonstrated |
| 52643960 | WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→WETH | 0.998317 WETH | 0.000121 WETH | 0.000000 WETH | 0.000003 WETH | 0.000118 WETH (0.2622 €) | — | 1.18 | 0.241 (n=29) | REJECTED | below_safety_margin(117845714349323<199663382839724), reliability_not_demonstrated |
| 52643631 | USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 402.676128 USDC | 0.291853 USDC | 0.000000 USDC | 0.007764 USDC | 0.284089 USDC (0.2614 €) | — | 7.06 | 0.324 (n=17) | REJECTED | stale_data(4844ms>4000.0), reliability_not_demonstrated |
| 52643631 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH | 0.167552 WETH | 0.000121 WETH | 0.000000 WETH | 0.000003 WETH | 0.000118 WETH (0.2605 €) | 0.000118 WETH | 7.05 | 0.324 (n=17) | REJECTED | stale_data(4838ms>4000.0), reliability_not_demonstrated |
| 52649351 | WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.176655 WETH | 0.000119 WETH | 0.000000 WETH | 0.000003 WETH | 0.000116 WETH (0.2602 €) | — | 6.55 | 0.146 (n=47) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 52649351 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→USDC | 429.929167 USDC | 0.289421 USDC | 0.000000 USDC | 0.007354 USDC | 0.282067 USDC (0.2595 €) | — | 6.56 | 0.146 (n=47) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 52642035 | USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 420.852464 USDC | 0.288482 USDC | 0.000000 USDC | 0.007844 USDC | 0.280638 USDC (0.2582 €) | — | 6.67 | 0.164 (n=42) | REJECTED | p_lower_below_threshold(0.16<0.75) |
| 52642035 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH | 0.177158 WETH | 0.000121 WETH | 0.000000 WETH | 0.000003 WETH | 0.000118 WETH (0.2575 €) | 0.000118 WETH | 6.66 | 0.164 (n=42) | REJECTED | p_lower_below_threshold(0.16<0.75) |

## Fiabilité et décision
- Observations ghost : 384 ; taux observé 0.151 ; borne inférieure crédible (0.9) 0.129 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 12.9% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ✅ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
