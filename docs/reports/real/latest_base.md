# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-21T06:02:41+00:00 ; durée 73.83 min ; blocs 52884388 → 52886605 (2090 vus)

## Connexion
- Requêtes RPC : 25417 ; erreurs : 58 ; latence p50/p95 : 430.3/1,993.4 ms
- Rafraîchissements d'état : 2091 ; âge des données au dernier bloc : 1.81 s ; changements de frais LP observés (pools à frais dynamiques) : 3891
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 496 ; cycles déclenchés par événement : 36 ; avance médiane sur le rafraîchissement multicall : 1,078 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,442.62 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 580 pools, 328 jetons, 21464 routes
- Par DEX : uniswap_v3 137, aerodrome 236, aerodrome_slipstream 158, pancakeswap_v3 31, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 208 (rejetés 2) → 613 jetons ; pools candidats 3925 (énumérés 396, par paires 0), mesurés 582, sous le plancher de 10000.0 $ : 2 → gardés 580 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2447.377823, 'AERO': 0.859444, 'cbBTC': 82692.945421}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 148,457,399 | 2,442.619777 | 52886605 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 38,510,291 | 1.180563 | 52886605 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| aerodrome | WETH/VVV | 3000 | 17,986,167 | 94.874077 | 52886605 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,465,472 | 0.029508 | 52886605 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 11,202,135 | 0.029563 | 52886605 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,535,770 | 0.029573 | 52886605 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,927,445 | 0.000012 | 52886605 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 8,600,649 | 2,436.498982 | 52886605 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/USDC | 3000 | 8,369,424 | 2,442.673698 | 52886605 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | USDC/cbBTC | 332 | 8,167,561 | 0.000012 | 52886605 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 639 | 7,503,898 | 2,435.707443 | 52886605 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,269,045 | 0.001669 | 52886605 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 412 | 6,609,074 | 0.000012 | 52886605 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,535,136 | 0.029496 | 52886605 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | fBOMB/AERO | 10000 | 5,237,034 | 0.024767 | 52886605 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,708,257 | 0.802393 | 52886605 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,690,359 | 0.000277 | 52886605 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,439,852 | 2,435.524914 | 52886605 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,393,795 | 0.998741 | 52886605 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 4,033,154 | 34,789.318582 | 52886605 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDT | 418 | 3,721,377 | 2,439.093086 | 52886605 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome | WETH/AERO | 10000 | 3,346,111 | 2,854.999892 | 52886605 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,787,295 | 397.274213 | 52886605 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | WETH/VVV | 2712 | 2,752,345 | 94.893690 | 52886605 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,530,466 | 1.142085 | 52886605 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 2,407,314 | 0.000010 | 52886605 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,274,003 | 0.000012 | 52886605 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | WETH/FAI | 10000 | 2,236,879 | 1,210,470.665103 | 52886605 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 2,074,437 | 0.000012 | 52886605 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,059,210 | 1.238682 | 52886605 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,028,014 | 1.383164 | 52886605 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,944,477 | 0.000000 | 52886605 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome | weETH_04c0/WETH | 500 | 1,902,935 | 1.105697 | 52886605 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 1,860,563 | 1,066.166293 | 52886605 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| uniswap_v3 | XDP/USDC | 100 | 1,808,899 | 0.019214 | 52886605 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,781,922 | 15.812419 | 52886605 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,736,165 | 13,461.283555 | 52886605 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | fBOMB/USDC | 10000 | 1,715,743 | 0.021478 | 52886605 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| aerodrome | WETH/msETH (stable) | 500 | 1,686,015 | 2.310784 | 52886605 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | WETH/AERO | 3000 | 1,674,592 | 2,875.371782 | 52886605 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,566,267 | 0.916062 | 52886605 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,456,348 | 0.826534 | 52886605 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | EURC/USDC | 70 | 1,423,206 | 1.122390 | 52886605 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,350,183 | 0.004809 | 52886605 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,325,476 | 0.000278 | 52886605 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| uniswap_v3 | DRB/WETH | 10000 | 1,325,143 | 0.000000 | 52886605 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome_slipstream | USDC/AERO | 10000 | 1,316,332 | 1.172358 | 52886605 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome | WETH/cbBTC | 3000 | 1,308,377 | 0.029583 | 52886605 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,284,808 | 2,436.544876 | 52886605 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,235,876 | 63.619861 | 52886605 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,220,037 | 34,988,111.001513 | 52886605 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,218,552 | 23.087741 | 52886605 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| aerodrome | WETH/EDEL | 7000 | 1,204,490 | 70,108.926830 | 52886605 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | WETH/WELL | 10000 | 1,192,928 | 1,136,701.097349 | 52886605 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,180,983 | 0.436545 | 52886605 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,177,199 | 484,015.691887 | 52886605 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,154,273 | 1.106158 | 52886605 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |
| aerodrome_slipstream | msUSD/USDC | 500 | 1,150,704 | 0.886169 | 52886605 | `0x7501bc8Bb51616F79bfA524E464fb7B41f0B10fB` |
| aerodrome | USDC/NOCK | 3000 | 1,148,878 | 47.737163 | 52886605 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,113,856 | 20,316,195.460132 | 52886605 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |

## Recherche d'opportunités
- Cycles : 2126 ; routes examinées : 45632464 ; candidats optimisés : 252068 ; net attendu > 0 : 31 ; dernier cycle 433.8 ms
- Rejets (moteur) : {'spread_below_threshold': 45071983, 'liquidity_below_min': 303545, 'negative_expected_net': 252037, 'cycle_budget_exhausted': 2747, 'borrow_bound_too_small': 2121}
- Enregistrements de la session : 252068 ; net attendu > 0 : 31 ; simulés (eth_call de la vraie tx) : 0 (ok 0, échec 0) ; étiquettes ghost N+1 : 0/0 positives
- Décisions : {'REJECTED': 252068} ; motifs de rejet : {'below_safety_margin': 31, 'negative_expected_net': 252037, 'p_lower_below_threshold': 28, 'reliability_not_demonstrated': 3, 'stale_data': 6}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52885990 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.004233 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0018 €) | — | 1.87 | 0.286 (n=89) | REJECTED | below_safety_margin(791748084320<846554872539), p_lower_below_threshold(0.29<0.75) |
| 52885990 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 10.339254 USDC | 0.009289 USDC | 0.000000 USDC | 0.007378 USDC | 0.001911 USDC (0.0018 €) | — | 1.85 | 0.286 (n=89) | REJECTED | below_safety_margin(1911<2067), p_lower_below_threshold(0.29<0.75) |
| 52885990 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.004162 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0015 €) | — | 1.62 | 0.119 (n=194) | REJECTED | below_safety_margin(675391846905<832447526675), p_lower_below_threshold(0.12<0.75) |
| 52885990 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 10.047831 USDC | 0.009005 USDC | 0.000000 USDC | 0.007378 USDC | 0.001627 USDC (0.0015 €) | — | 1.62 | 0.119 (n=194) | REJECTED | below_safety_margin(1627<2009), p_lower_below_threshold(0.12<0.75) |
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
| 52885998 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.003819 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0003 €) | — | 0.35 | 0.119 (n=194) | REJECTED | below_safety_margin(134208322591<763704072075), p_lower_below_threshold(0.12<0.75) |
| 52885998 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 9.297825 USDC | 0.007654 USDC | 0.000000 USDC | 0.007345 USDC | 0.000309 USDC (0.0003 €) | — | 0.33 | 0.119 (n=194) | REJECTED | below_safety_margin(309<1859), p_lower_below_threshold(0.12<0.75) |
| 52885998 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.003819 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0002 €) | — | 0.27 | 0.286 (n=89) | REJECTED | below_safety_margin(101512756857<763704072075), p_lower_below_threshold(0.29<0.75) |
| 52885999 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.003819 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0002 €) | — | 0.27 | 0.286 (n=89) | REJECTED | below_safety_margin(101512756857<763704072075), p_lower_below_threshold(0.29<0.75) |

## Fiabilité et décision
- Observations ghost : 1593 ; taux observé 0.102 ; borne inférieure crédible (0.9) 0.093 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 9.3% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
