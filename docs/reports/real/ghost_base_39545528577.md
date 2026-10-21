# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-21T07:07:54+00:00 ; durée 139.05 min ; blocs 52884388 → 52888560 (3837 vus)

## Connexion
- Requêtes RPC : 48363 ; erreurs : 150 ; latence p50/p95 : 413.0/1,390.3 ms
- Rafraîchissements d'état : 3838 ; âge des données au dernier bloc : 2.03 s ; changements de frais LP observés (pools à frais dynamiques) : 7218
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 12466 ; cycles déclenchés par événement : 748 ; avance médiane sur le rafraîchissement multicall : 779 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,441.97 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 580 pools, 328 jetons, 21464 routes
- Par DEX : uniswap_v3 137, aerodrome 236, aerodrome_slipstream 158, pancakeswap_v3 31, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 208 (rejetés 2) → 613 jetons ; pools candidats 3925 (énumérés 396, par paires 0), mesurés 582, sous le plancher de 10000.0 $ : 2 → gardés 580 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2447.377823, 'AERO': 0.859444, 'cbBTC': 82692.945421}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 148,443,411 | 2,441.966614 | 52888560 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 38,489,531 | 1.182116 | 52888560 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| aerodrome | WETH/VVV | 3000 | 17,983,747 | 94.848915 | 52888560 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,469,837 | 0.029478 | 52888560 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome_slipstream | WETH/cbBTC | 2505 | 11,581,494 | 0.029539 | 52888560 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,537,232 | 0.029551 | 52888560 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,949,615 | 0.000012 | 52888560 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 8,598,088 | 2,438.186546 | 52888560 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/USDC | 3000 | 8,368,305 | 2,442.601312 | 52888560 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | USDC/cbBTC | 336 | 8,169,902 | 0.000012 | 52888560 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 549 | 7,702,760 | 2,438.096415 | 52888560 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,278,670 | 0.001672 | 52888560 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 424 | 6,617,326 | 0.000012 | 52888560 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,578,236 | 0.029482 | 52888560 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | fBOMB/AERO | 10000 | 5,233,236 | 0.024768 | 52888560 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,706,998 | 0.802393 | 52888560 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,690,130 | 0.000277 | 52888560 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,501,496 | 2,438.246152 | 52888560 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,397,056 | 0.998741 | 52888560 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome_slipstream | WETH/USDT | 403 | 4,314,477 | 2,441.108729 | 52888560 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome_slipstream | USDC/AERO | 10000 | 4,194,811 | 1.174892 | 52888560 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome | WETH/KTA | 3000 | 4,030,191 | 34,822.257752 | 52888560 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/AERO | 10000 | 3,343,450 | 2,862.674408 | 52888560 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,825,900 | 396.887324 | 52888560 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | WETH/VVV | 2703 | 2,751,910 | 94.840186 | 52888560 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,529,739 | 1.142086 | 52888560 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,274,311 | 0.000012 | 52888560 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | WETH/FAI | 10000 | 2,237,188 | 1,209,488.803510 | 52888560 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | AERO/cbBTC | 2700 | 2,210,052 | 0.000010 | 52888560 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/MORPHO | 2712 | 2,183,111 | 1,053.798094 | 52888560 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 2,074,749 | 0.000012 | 52888560 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,027,316 | 1.383640 | 52888560 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,943,959 | 0.000000 | 52888560 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome | weETH_04c0/WETH | 500 | 1,902,427 | 1.105697 | 52888560 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,842,551 | 15.818807 | 52888560 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| uniswap_v3 | XDP/USDC | 100 | 1,811,525 | 0.019251 | 52888560 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,723,554 | 13,469.022154 | 52888560 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | fBOMB/USDC | 10000 | 1,715,725 | 0.021474 | 52888560 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,713,694 | 0.916061 | 52888560 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,710,785 | 1.490101 | 52888560 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome | WETH/msETH (stable) | 500 | 1,685,669 | 2.310610 | 52888560 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | WETH/AERO | 3000 | 1,673,506 | 2,881.995938 | 52888560 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,456,348 | 0.826534 | 52888560 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | EURC/USDC | 70 | 1,423,053 | 1.122199 | 52888560 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,349,822 | 0.004809 | 52888560 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,325,422 | 0.000279 | 52888560 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| uniswap_v3 | DRB/WETH | 10000 | 1,324,789 | 0.000000 | 52888560 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | WETH/cbBTC | 3000 | 1,308,689 | 0.029555 | 52888560 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,275,780 | 2,438.137083 | 52888560 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,235,876 | 63.619861 | 52888560 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,219,710 | 34,988,111.001513 | 52888560 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,218,260 | 23.086678 | 52888560 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| aerodrome | WETH/EDEL | 7000 | 1,199,832 | 70,616.575896 | 52888560 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | WETH/WELL | 10000 | 1,192,772 | 1,136,390.344564 | 52888560 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,181,212 | 0.436545 | 52888560 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,176,885 | 484,015.691887 | 52888560 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,155,684 | 1.106158 | 52888560 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |
| aerodrome_slipstream | msUSD/USDC | 500 | 1,148,239 | 0.886154 | 52888560 | `0x7501bc8Bb51616F79bfA524E464fb7B41f0B10fB` |
| aerodrome | USDC/NOCK | 3000 | 1,147,820 | 47.825281 | 52888560 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,109,895 | 20,432,688.606961 | 52888560 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |

## Recherche d'opportunités
- Cycles : 4585 ; routes examinées : 98412440 ; candidats optimisés : 577848 ; net attendu > 0 : 111 ; dernier cycle 189.0 ms
- Rejets (moteur) : {'spread_below_threshold': 97064084, 'liquidity_below_min': 657769, 'negative_expected_net': 577737, 'pool_quarantined': 104596, 'borrow_bound_too_small': 4576, 'cycle_budget_exhausted': 3567}
- Enregistrements de la session : 577848 ; net attendu > 0 : 111 ; simulés (eth_call de la vraie tx) : 12 (ok 0, échec 12) ; étiquettes ghost N+1 : 0/3 positives
- Décisions : {'REJECTED': 577848} ; motifs de rejet : {'below_safety_margin': 99, 'negative_expected_net': 577737, 'p_lower_below_threshold': 106, 'price_impact': 76, 'reliability_not_demonstrated': 5, 'simulation_failed': 12, 'stale_data': 13}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52887788 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 76.776773 USDC | 0.127547 USDC | 0.000000 USDC | 0.005482 USDC | 0.122065 USDC (0.1123 €) | — | 15.90 | 0.000 (n=44) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 52887787 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 53.684559 USDC | 0.062580 USDC | 0.000000 USDC | 0.005482 USDC | 0.057098 USDC (0.0525 €) | — | 10.64 | 0.000 (n=43) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 52885990 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.004233 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0018 €) | — | 1.87 | 0.286 (n=89) | REJECTED | below_safety_margin(791748084320<846554872539), p_lower_below_threshold(0.29<0.75) |
| 52885990 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 10.339254 USDC | 0.009289 USDC | 0.000000 USDC | 0.007378 USDC | 0.001911 USDC (0.0018 €) | — | 1.85 | 0.286 (n=89) | REJECTED | below_safety_margin(1911<2067), p_lower_below_threshold(0.29<0.75) |
| 52885990 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.004162 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0015 €) | — | 1.62 | 0.119 (n=194) | REJECTED | below_safety_margin(675391846905<832447526675), p_lower_below_threshold(0.12<0.75) |
| 52885990 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 10.047831 USDC | 0.009005 USDC | 0.000000 USDC | 0.007378 USDC | 0.001627 USDC (0.0015 €) | — | 1.62 | 0.119 (n=194) | REJECTED | below_safety_margin(1627<2009), p_lower_below_threshold(0.12<0.75) |
| 52887839 | USDC→[pancakeswap_v3]→PLAY→[aerodrome]→USDC | 8.378860 USDC | 0.006715 USDC | 0.000000 USDC | 0.005146 USDC | 0.001569 USDC (0.0014 €) | — | 1.87 | 0.001 (n=7) | REJECTED | below_safety_margin(1569<1675), reliability_not_demonstrated |
| 52887839 | USDC→[pancakeswap_v3]→PLAY→[aerodrome]→USDC | 8.378860 USDC | 0.006715 USDC | 0.000000 USDC | 0.005146 USDC | 0.001569 USDC (0.0014 €) | — | 1.87 | 0.001 (n=7) | REJECTED | below_safety_margin(1569<1675), reliability_not_demonstrated |
| 52886001 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.004097 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0013 €) | — | 1.45 | 0.286 (n=89) | REJECTED | below_safety_margin(592488913815<819454971974), p_lower_below_threshold(0.29<0.75) |
| 52886001 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 10.053350 USDC | 0.008770 USDC | 0.000000 USDC | 0.007345 USDC | 0.001425 USDC (0.0013 €) | — | 1.42 | 0.286 (n=89) | REJECTED | below_safety_margin(1425<2010), p_lower_below_threshold(0.29<0.75) |
| 52886001 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.004048 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0011 €) | — | 1.18 | 0.119 (n=194) | REJECTED | below_safety_margin(477669725534<809537137834), p_lower_below_threshold(0.12<0.75) |
| 52886001 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 9.754404 USDC | 0.008490 USDC | 0.000000 USDC | 0.007345 USDC | 0.001145 USDC (0.0011 €) | — | 1.17 | 0.119 (n=194) | REJECTED | below_safety_margin(1145<1950), p_lower_below_threshold(0.12<0.75) |
| 52885988 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.003949 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0008 €) | — | 0.84 | 0.119 (n=194) | REJECTED | below_safety_margin(333503695751<789830782116), stale_data(4609ms>4000.0), p_lower_below_threshold(0.12<0.75) |
| 52885988 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 9.583833 USDC | 0.008139 USDC | 0.000000 USDC | 0.007346 USDC | 0.000793 USDC (0.0007 €) | — | 0.83 | 0.119 (n=194) | REJECTED | below_safety_margin(793<1916), stale_data(4615ms>4000.0), p_lower_below_threshold(0.12<0.75) |
| 52885992 | USDC→[aerodrome_slipstream]→CARV→[aerodrome_slipstream]→USDC | 19.726878 USDC | 0.006191 USDC | 0.000000 USDC | 0.005488 USDC | 0.000703 USDC (0.0006 €) | — | 0.36 | 0.027 (n=11) | REJECTED | below_safety_margin(703<3945), reliability_not_demonstrated |
| 52885999 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.003949 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0006 €) | — | 0.70 | 0.119 (n=194) | REJECTED | below_safety_margin(277719272866<789753522689), p_lower_below_threshold(0.12<0.75) |
| 52886000 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.003949 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0006 €) | — | 0.70 | 0.119 (n=194) | REJECTED | below_safety_margin(277719272866<789753522689), p_lower_below_threshold(0.12<0.75) |
| 52885999 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 9.453670 USDC | 0.008003 USDC | 0.000000 USDC | 0.007345 USDC | 0.000658 USDC (0.0006 €) | — | 0.70 | 0.119 (n=194) | REJECTED | below_safety_margin(658<1890), p_lower_below_threshold(0.12<0.75) |
| 52886000 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 9.453670 USDC | 0.008003 USDC | 0.000000 USDC | 0.007345 USDC | 0.000658 USDC (0.0006 €) | — | 0.70 | 0.119 (n=194) | REJECTED | below_safety_margin(658<1890), p_lower_below_threshold(0.12<0.75) |
| 52885991 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.003880 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0004 €) | — | 0.47 | 0.286 (n=89) | REJECTED | below_safety_margin(181510219543<776015242396), p_lower_below_threshold(0.29<0.75) |
| 52885991 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 9.375169 USDC | 0.007771 USDC | 0.000000 USDC | 0.007347 USDC | 0.000424 USDC (0.0004 €) | — | 0.45 | 0.286 (n=89) | REJECTED | below_safety_margin(424<1875), p_lower_below_threshold(0.29<0.75) |
| 52885988 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.003826 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0004 €) | — | 0.41 | 0.286 (n=89) | REJECTED | below_safety_margin(157275524640<765294161888), stale_data(4632ms>4000.0), p_lower_below_threshold(0.29<0.75) |
| 52886218 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.006724 WETH | 0.000002 WETH | 0.000000 WETH | 0.000002 WETH | 0.000000 WETH (0.0004 €) | — | 0.23 | 0.027 (n=11) | REJECTED | below_safety_margin(156602045537<1344835532607), stale_data(5365ms>4000.0), reliability_not_demonstrated |
| 52886218 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 16.246033 USDC | 0.005860 USDC | 0.000000 USDC | 0.005487 USDC | 0.000373 USDC (0.0003 €) | — | 0.23 | 0.027 (n=11) | REJECTED | below_safety_margin(373<3249), stale_data(5369ms>4000.0), reliability_not_demonstrated |
| 52885988 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 9.307787 USDC | 0.007710 USDC | 0.000000 USDC | 0.007346 USDC | 0.000364 USDC (0.0003 €) | — | 0.39 | 0.286 (n=89) | REJECTED | below_safety_margin(364<1861), stale_data(4638ms>4000.0), p_lower_below_threshold(0.29<0.75) |

## Fiabilité et décision
- Observations ghost : 1596 ; taux observé 0.102 ; borne inférieure crédible (0.9) 0.093 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 9.3% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
