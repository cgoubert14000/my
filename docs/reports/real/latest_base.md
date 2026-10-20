# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-20T16:12:39+00:00 ; durée 256.46 min ; blocs 52854009 → 52861701 (7412 vus)

## Connexion
- Requêtes RPC : 93075 ; erreurs : 45 ; latence p50/p95 : 332.9/930.3 ms
- Rafraîchissements d'état : 7412 ; âge des données au dernier bloc : 2.65 s ; changements de frais LP observés (pools à frais dynamiques) : 26687
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 62807 ; cycles déclenchés par événement : 2739 ; avance médiane sur le rafraîchissement multicall : 512 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,434.03 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 573 pools, 327 jetons, 21172 routes
- Par DEX : uniswap_v3 135, aerodrome 235, aerodrome_slipstream 156, pancakeswap_v3 30, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 207 (rejetés 2) → 612 jetons ; pools candidats 3877 (énumérés 393, par paires 0), mesurés 575, sous le plancher de 10000.0 $ : 2 → gardés 573 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDbC': 1.0, 'USDC': 1.0, 'WETH': 2381.795213, 'AERO': 0.801082, 'cbBTC': 81409.268719}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 147,409,296 | 2,434.025286 | 52861701 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 39,447,995 | 1.173649 | 52861701 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 18,777,532 | 0.029540 | 52861701 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/VVV | 3000 | 17,865,866 | 95.887485 | 52861701 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,290,928 | 0.029540 | 52861701 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,494,863 | 0.029553 | 52861701 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,915,903 | 0.000012 | 52861701 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 8,457,017 | 2,433.170845 | 52861701 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/USDC | 3000 | 8,360,228 | 2,434.147578 | 52861701 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | USDC/cbBTC | 366 | 8,152,189 | 0.000012 | 52861701 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,243,796 | 0.001673 | 52861701 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | WETH/USDC | 847 | 7,178,167 | 2,432.419191 | 52861701 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | USDC/cbBTC | 592 | 7,029,943 | 0.000012 | 52861701 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,412,628 | 0.029535 | 52861701 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | fBOMB/AERO | 10000 | 5,229,892 | 0.024832 | 52861701 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,700,422 | 0.000275 | 52861701 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,692,893 | 0.802394 | 52861701 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,407,820 | 2,432.236174 | 52861701 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,367,150 | 0.998767 | 52861701 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 4,036,721 | 34,483.896510 | 52861701 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDT | 454 | 3,574,294 | 2,436.529035 | 52861701 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome_slipstream | USDC/AERO | 10000 | 3,560,427 | 1.169189 | 52861701 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome | WETH/AERO | 10000 | 3,350,979 | 2,840.272168 | 52861701 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,964,823 | 1.142084 | 52861701 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,884,282 | 0.000012 | 52861701 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,786,389 | 403.694892 | 52861701 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | WETH/VVV | 2706 | 2,728,041 | 95.867181 | 52861701 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 2,423,852 | 1,024.668203 | 52861701 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome | WETH/FAI | 10000 | 2,222,971 | 1,217,054.518168 | 52861701 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | AERO/cbBTC | 2700 | 2,198,826 | 0.000010 | 52861701 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,059,873 | 1.237789 | 52861701 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,028,987 | 1.381848 | 52861701 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,966,611 | 0.000000 | 52861701 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,870,123 | 16.047246 | 52861701 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,839,581 | 13,671.170528 | 52861701 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | XDP/USDC | 100 | 1,814,157 | 0.019403 | 52861701 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,771,923 | 0.000012 | 52861701 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | weETH_04c0/WETH | 500 | 1,761,119 | 1.105512 | 52861701 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome | fBOMB/USDC | 10000 | 1,705,582 | 0.021153 | 52861701 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| aerodrome | WETH/msETH (stable) | 500 | 1,680,254 | 2.311698 | 52861701 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | WETH/AERO | 3000 | 1,666,475 | 2,856.190027 | 52861701 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,563,776 | 0.916062 | 52861701 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,456,783 | 0.826046 | 52861701 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | EURC/USDC | 70 | 1,416,100 | 1.123006 | 52861701 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,345,885 | 0.004811 | 52861701 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v3 | DRB/WETH | 10000 | 1,337,304 | 0.000000 | 52861701 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,317,871 | 0.000276 | 52861701 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | WETH/cbBTC | 3000 | 1,303,077 | 0.029557 | 52861701 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,285,779 | 23.114707 | 52861701 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,254,353 | 2,433.162042 | 52861701 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,236,078 | 63.599131 | 52861701 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome | WETH/EDEL | 7000 | 1,221,343 | 67,882.918148 | 52861701 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/doginme | 10000 | 1,208,894 | 35,632,333.868523 | 52861701 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,180,648 | 0.436740 | 52861701 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| aerodrome_slipstream | msUSD/USDC | 500 | 1,179,404 | 0.886336 | 52861701 | `0x7501bc8Bb51616F79bfA524E464fb7B41f0B10fB` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,163,914 | 494,184.765086 | 52861701 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | WETH/WELL | 10000 | 1,155,805 | 1,202,447.653637 | 52861701 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome | USDC/NOCK | 3000 | 1,145,873 | 47.987898 | 52861701 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,082,065 | 21,209,566.564570 | 52861701 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/USDT | 8 | 1,073,517 | 1.001344 | 52861701 | `0xa41Bc0AFfbA7Fd420d186b84899d7ab2aC57fcD1` |

## Recherche d'opportunités
- Cycles : 10150 ; routes examinées : 214895800 ; candidats optimisés : 1250984 ; net attendu > 0 : 1235 ; dernier cycle 148.6 ms
- Rejets (moteur) : {'spread_below_threshold': 211552288, 'liquidity_below_min': 1729673, 'negative_expected_net': 1249749, 'pool_quarantined': 213176, 'borrow_bound_too_small': 136835, 'cycle_budget_exhausted': 12844}
- Enregistrements de la session : 1250984 ; net attendu > 0 : 1235 ; simulés (eth_call de la vraie tx) : 148 (ok 104, échec 44) ; étiquettes ghost N+1 : 17/107 positives
- Décisions : {'REJECTED': 1250984} ; motifs de rejet : {'below_safety_margin': 846, 'negative_expected_net': 1249749, 'p_lower_below_threshold': 1005, 'price_impact': 45, 'reliability_not_demonstrated': 230, 'sim_below_estimate': 5, 'simulated_net_nonpositive': 2, 'simulation_failed': 44, 'stale_data': 91}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52860553 | WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.269723 WETH | 0.000149 WETH | 0.000000 WETH | 0.000003 WETH | 0.000146 WETH (0.3266 €) | — | 5.41 | 0.109 (n=132) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.11<0.75) |
| 52860553 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.007574 cbBTC | 0.000004 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000004 cbBTC (0.3264 €) | — | 5.68 | 0.109 (n=132) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 52860377 | WETH→[aerodrome_slipstream]→BRETT→[aerodrome]→AERO→[pancakeswap_v3]→WETH | 0.028655 WETH | 0.000126 WETH | 0.000000 WETH | 0.000003 WETH | 0.000123 WETH (0.2754 €) | 0.000123 WETH | 42.94 | 0.002 (n=4) | REJECTED | reliability_not_demonstrated |
| 52861527 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 2,289.600704 USDC | 0.246212 USDC | 0.000000 USDC | 0.005934 USDC | 0.240278 USDC (0.2211 €) | — | 1.05 | 0.015 (n=55) | REJECTED | below_safety_margin(240278<457920), p_lower_below_threshold(0.01<0.75) |
| 52861528 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 2,289.600704 USDC | 0.246212 USDC | 0.000000 USDC | 0.005934 USDC | 0.240278 USDC (0.2211 €) | — | 1.05 | 0.015 (n=55) | REJECTED | below_safety_margin(240278<457920), p_lower_below_threshold(0.01<0.75) |
| 52861527 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.939641 WETH | 0.000101 WETH | 0.000000 WETH | 0.000002 WETH | 0.000098 WETH (0.2205 €) | — | 1.05 | 0.015 (n=55) | REJECTED | below_safety_margin(98465456722515<187928164483069), p_lower_below_threshold(0.01<0.75) |
| 52861528 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.939641 WETH | 0.000101 WETH | 0.000000 WETH | 0.000002 WETH | 0.000098 WETH (0.2205 €) | — | 1.05 | 0.015 (n=55) | REJECTED | below_safety_margin(98465456722515<187928164483069), p_lower_below_threshold(0.01<0.75) |
| 52860553 | USDC→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 484.914616 USDC | 0.189088 USDC | 0.000000 USDC | 0.007536 USDC | 0.181552 USDC (0.1670 €) | — | 3.74 | 0.109 (n=132) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 52860553 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→cbBTC | 0.005832 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1670 €) | — | 3.77 | 0.109 (n=132) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 52860553 | cbBTC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.003379 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1374 €) | — | 5.36 | 0.109 (n=132) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 52860553 | WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→WETH | 0.115149 WETH | 0.000064 WETH | 0.000000 WETH | 0.000003 WETH | 0.000061 WETH (0.1369 €) | — | 5.31 | 0.109 (n=132) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.11<0.75) |
| 52860377 | WETH→[aerodrome_slipstream]→BRETT→[aerodrome]→AERO→[uniswap_v3]→WETH | 0.019105 WETH | 0.000056 WETH | 0.000000 WETH | 0.000003 WETH | 0.000053 WETH (0.1181 €) | 0.000053 WETH | 27.61 | 0.005 (n=61) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 52860553 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.002547 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.1070 €) | — | 5.54 | 0.109 (n=132) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 52860553 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 204.066511 USDC | 0.123690 USDC | 0.000000 USDC | 0.007536 USDC | 0.116154 USDC (0.1069 €) | — | 5.69 | 0.109 (n=132) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 52855720 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 713.236514 USDC | 0.118318 USDC | 0.000000 USDC | 0.005387 USDC | 0.112931 USDC (0.1039 €) | — | 1.58 | 0.037 (n=8) | REJECTED | below_safety_margin(112931<142647), reliability_not_demonstrated |
| 52855720 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.298322 WETH | 0.000049 WETH | 0.000000 WETH | 0.000002 WETH | 0.000047 WETH (0.1039 €) | — | 1.58 | 0.037 (n=8) | REJECTED | below_safety_margin(47156112269631<59664491208030), reliability_not_demonstrated |
| 52860553 | WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[uniswap_v3]→WETH | 0.151034 WETH | 0.000044 WETH | 0.000000 WETH | 0.000003 WETH | 0.000041 WETH (0.0909 €) | — | 2.69 | 0.117 (n=183) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.12<0.75) |
| 52860553 | cbBTC→[uniswap_v3]→WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.003932 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0903 €) | — | 3.03 | 0.109 (n=132) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 52860377 | WETH→[aerodrome_slipstream]→BRETT→[aerodrome]→AERO→[aerodrome_slipstream]→WETH | 0.016502 WETH | 0.000042 WETH | 0.000000 WETH | 0.000003 WETH | 0.000039 WETH (0.0862 €) | 0.000039 WETH | 23.35 | 0.005 (n=61) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 52855720 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 538.043039 USDC | 0.088374 USDC | 0.000000 USDC | 0.007208 USDC | 0.081166 USDC (0.0747 €) | — | 1.51 | 0.105 (n=170) | REJECTED | below_safety_margin(81166<107608), p_lower_below_threshold(0.10<0.75) |
| 52855720 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.220537 WETH | 0.000037 WETH | 0.000000 WETH | 0.000003 WETH | 0.000034 WETH (0.0743 €) | — | 1.53 | 0.105 (n=170) | REJECTED | below_safety_margin(33743439129325<44107398343291), p_lower_below_threshold(0.10<0.75) |
| 52855720 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.006168 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0742 €) | — | 1.61 | 0.105 (n=170) | REJECTED | below_safety_margin(99<123), p_lower_below_threshold(0.10<0.75) |
| 52860553 | WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.106303 WETH | 0.000036 WETH | 0.000000 WETH | 0.000003 WETH | 0.000032 WETH (0.0726 €) | — | 3.05 | 0.109 (n=132) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 52860553 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.003688 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0721 €) | — | 2.58 | 0.117 (n=183) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52858173 | USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 233.952408 USDC | 0.082506 USDC | 0.000000 USDC | 0.008077 USDC | 0.074429 USDC (0.0685 €) | — | 3.18 | 0.111 (n=129) | REJECTED | p_lower_below_threshold(0.11<0.75) |

## Fiabilité et décision
- Observations ghost : 1520 ; taux observé 0.104 ; borne inférieure crédible (0.9) 0.094 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 9.4% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ✅ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
