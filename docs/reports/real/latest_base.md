# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-19T16:07:10+00:00 ; durée 183.77 min ; blocs 52812825 → 52818336 (5318 vus)

## Connexion
- Requêtes RPC : 71086 ; erreurs : 168 ; latence p50/p95 : 328.8/1,024.0 ms
- Rafraîchissements d'état : 5318 ; âge des données au dernier bloc : 3.2 s ; changements de frais LP observés (pools à frais dynamiques) : 16731
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 112184 ; cycles déclenchés par événement : 4268 ; avance médiane sur le rafraîchissement multicall : 1,126 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,392.26 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 571 pools, 327 jetons, 21004 routes
- Par DEX : uniswap_v3 137, aerodrome 234, aerodrome_slipstream 153, pancakeswap_v3 30, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 207 (rejetés 2) → 612 jetons ; pools candidats 3877 (énumérés 390, par paires 0), mesurés 574, sous le plancher de 10000.0 $ : 3 → gardés 571 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2419.85313, 'AERO': 0.782295, 'cbBTC': 82567.067054}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 146,198,665 | 2,392.264202 | 52818336 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 34,972,649 | 1.292820 | 52818336 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 500 | 18,208,307 | 0.029240 | 52818336 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 17,097,003 | 101.281328 | 52818336 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| aerodrome_slipstream | WETH/cbBTC | 2505 | 16,004,731 | 0.029273 | 52818336 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,313,935 | 0.029287 | 52818336 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,845,694 | 0.000012 | 52818336 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome_slipstream | USDC/cbBTC | 412 | 9,206,694 | 0.000012 | 52818336 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | WETH/USDC | 500 | 8,347,165 | 2,392.291047 | 52818336 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/USDC | 3000 | 8,292,864 | 2,392.360886 | 52818336 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | USDC/cbBTC | 332 | 7,813,646 | 0.000012 | 52818336 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,167,113 | 0.001662 | 52818336 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | WETH/USDC | 698 | 6,990,720 | 2,393.122564 | 52818336 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,327,557 | 0.029251 | 52818336 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | fBOMB/AERO | 10000 | 4,905,500 | 0.025996 | 52818336 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome_slipstream | USDC/AERO | 10000 | 4,880,457 | 1.287191 | 52818336 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,781,399 | 0.802395 | 52818336 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,595,711 | 0.000272 | 52818336 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,392,331 | 2,393.303661 | 52818336 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,335,406 | 0.998770 | 52818336 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 4,004,909 | 33,842.056543 | 52818336 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDT | 424 | 3,917,868 | 2,395.907699 | 52818336 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome | WETH/AERO | 10000 | 3,197,283 | 3,097.803489 | 52818336 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,847,243 | 0.000012 | 52818336 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/VVV | 2784 | 2,625,654 | 101.259606 | 52818336 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,559,001 | 404.302540 | 52818336 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | WETH/FAI | 10000 | 2,168,739 | 1,235,182.139618 | 52818336 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 2,160,250 | 0.000009 | 52818336 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,059,139 | 1.238201 | 52818336 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,036,743 | 1.372638 | 52818336 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| uniswap_v3 | BNKR/WETH | 10000 | 2,023,313 | 0.000000 | 52818336 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome_slipstream | cbETH/WETH | 60 | 1,987,230 | 1.142173 | 52818336 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,776,983 | 0.000012 | 52818336 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | XDP/USDC | 100 | 1,773,506 | 0.018764 | 52818336 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,772,225 | 16.212789 | 52818336 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | weETH_04c0/WETH | 500 | 1,729,284 | 1.105523 | 52818336 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome | fBOMB/USDC | 10000 | 1,722,307 | 0.020494 | 52818336 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| aerodrome | WETH/msETH (stable) | 500 | 1,655,536 | 2.306971 | 52818336 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,549,492 | 0.916350 | 52818336 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| uniswap_v3 | WETH/AERO | 3000 | 1,484,566 | 3,094.194351 | 52818336 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,456,369 | 0.827173 | 52818336 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | EURC/USDC | 70 | 1,405,610 | 1.120686 | 52818336 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,402,681 | 13,841.024373 | 52818336 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,338,162 | 0.435660 | 52818336 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,310,239 | 0.000000 | 52818336 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,288,234 | 0.000274 | 52818336 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | WETH/cbBTC | 3000 | 1,277,739 | 0.029283 | 52818336 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,277,622 | 0.004615 | 52818336 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,260,566 | 23.102508 | 52818336 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| aerodrome | USDC/SEND | 3000 | 1,232,737 | 63.944286 | 52818336 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,206,219 | 2,392.370008 | 52818336 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | WETH/WELL | 10000 | 1,195,566 | 1,085,554.587669 | 52818336 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/doginme | 10000 | 1,192,025 | 35,252,730.105067 | 52818336 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome_slipstream | WETH/msETH | 500 | 1,130,950 | 1.131606 | 52818336 | `0x74F72788F4814D7fF3C49B44684aa98Eee140C0E` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,125,728 | 515,481.870232 | 52818336 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | USDC/NOCK | 3000 | 1,105,724 | 51.535765 | 52818336 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | msUSD/USDC | 503 | 1,082,864 | 0.885459 | 52818336 | `0x7501bc8Bb51616F79bfA524E464fb7B41f0B10fB` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,076,607 | 15.540847 | 52818336 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | WETH/EDEL | 7000 | 1,052,346 | 89,014.343891 | 52818336 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,038,497 | 22,085,691.239462 | 52818336 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |

## Recherche d'opportunités
- Cycles : 9585 ; routes examinées : 201323340 ; candidats optimisés : 1349173 ; net attendu > 0 : 891 ; dernier cycle 109.1 ms
- Rejets (moteur) : {'spread_below_threshold': 197650011, 'liquidity_below_min': 1850464, 'negative_expected_net': 1348282, 'pool_quarantined': 219050, 'borrow_bound_too_small': 189415, 'cycle_budget_exhausted': 65227}
- Enregistrements de la session : 1349173 ; net attendu > 0 : 891 ; simulés (eth_call de la vraie tx) : 76 (ok 36, échec 40) ; étiquettes ghost N+1 : 7/45 positives
- Décisions : {'REJECTED': 1349173} ; motifs de rejet : {'below_safety_margin': 690, 'negative_expected_net': 1348282, 'p_lower_below_threshold': 754, 'price_impact': 30, 'reliability_not_demonstrated': 137, 'sim_below_estimate': 5, 'simulated_net_nonpositive': 3, 'simulation_failed': 40, 'stale_data': 3}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52817668 | WETH→[aerodrome]→TEVA→[uniswap_v3]→WETH | 0.024385 WETH | 0.000112 WETH | 0.000000 WETH | 0.000002 WETH | 0.000110 WETH (0.2433 €) | — | 45.10 | 0.001 (n=13) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52815901 | USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 1,462.225373 USDC | 0.173380 USDC | 0.000000 USDC | 0.007902 USDC | 0.165478 USDC (0.1522 €) | — | 1.13 | 0.117 (n=152) | REJECTED | below_safety_margin(165478<292445), p_lower_below_threshold(0.12<0.75) |
| 52815901 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH | 0.607861 WETH | 0.000072 WETH | 0.000000 WETH | 0.000003 WETH | 0.000069 WETH (0.1518 €) | — | 1.13 | 0.117 (n=152) | REJECTED | below_safety_margin(68791946207429<121572211358974), p_lower_below_threshold(0.12<0.75) |
| 52815204 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 1,735.428521 USDC | 0.154603 USDC | 0.000000 USDC | 0.006144 USDC | 0.148459 USDC (0.1366 €) | — | 0.86 | 0.017 (n=49) | REJECTED | below_safety_margin(148459<347085), p_lower_below_threshold(0.02<0.75) |
| 52815204 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.726513 WETH | 0.000065 WETH | 0.000000 WETH | 0.000003 WETH | 0.000062 WETH (0.1365 €) | — | 0.85 | 0.017 (n=49) | REJECTED | below_safety_margin(61999402150527<145302574799060), p_lower_below_threshold(0.02<0.75) |
| 52815907 | USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 273.632671 USDC | 0.112662 USDC | 0.000000 USDC | 0.008367 USDC | 0.104295 USDC (0.0960 €) | — | 3.81 | 0.123 (n=110) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52815907 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH | 0.113520 WETH | 0.000047 WETH | 0.000000 WETH | 0.000003 WETH | 0.000043 WETH (0.0957 €) | 0.000043 WETH | 3.81 | 0.123 (n=110) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52815204 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→cbBTC | 0.011354 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0792 €) | — | 0.92 | 0.119 (n=150) | REJECTED | below_safety_margin(105<227), p_lower_below_threshold(0.12<0.75) |
| 52815204 | WETH→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.422030 WETH | 0.000039 WETH | 0.000000 WETH | 0.000003 WETH | 0.000036 WETH (0.0792 €) | — | 0.85 | 0.119 (n=150) | REJECTED | below_safety_margin(35963544596847<84406012305694), p_lower_below_threshold(0.12<0.75) |
| 52815204 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 942.588524 USDC | 0.093877 USDC | 0.000000 USDC | 0.007972 USDC | 0.085905 USDC (0.0790 €) | — | 0.91 | 0.119 (n=150) | REJECTED | below_safety_margin(85905<188517), p_lower_below_threshold(0.12<0.75) |
| 52817314 | WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.424748 WETH | 0.000035 WETH | 0.000000 WETH | 0.000003 WETH | 0.000032 WETH (0.0703 €) | — | 0.75 | 0.115 (n=155) | REJECTED | below_safety_margin(31747037953707<84949688758203), p_lower_below_threshold(0.12<0.75) |
| 52815240 | cbBTC→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.003301 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0702 €) | 0.000001 cbBTC | 2.82 | 0.119 (n=150) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52815239 | cbBTC→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.003301 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0702 €) | — | 2.82 | 0.119 (n=150) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.12<0.75) |
| 52817314 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC | 1,018.946138 USDC | 0.083960 USDC | 0.000000 USDC | 0.007763 USDC | 0.076197 USDC (0.0701 €) | — | 0.75 | 0.115 (n=155) | REJECTED | below_safety_margin(76197<203789), p_lower_below_threshold(0.12<0.75) |
| 52815240 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→USDC | 271.384886 USDC | 0.083095 USDC | 0.000000 USDC | 0.007243 USDC | 0.075852 USDC (0.0698 €) | 0.075852 USDC | 2.79 | 0.119 (n=150) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52815239 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→USDC | 271.384886 USDC | 0.083095 USDC | 0.000000 USDC | 0.007243 USDC | 0.075852 USDC (0.0698 €) | — | 2.79 | 0.119 (n=150) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.12<0.75) |
| 52815204 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→cbBTC | 0.011356 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0694 €) | — | 0.81 | 0.119 (n=150) | REJECTED | below_safety_margin(92<227), p_lower_below_threshold(0.12<0.75) |
| 52815204 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 991.357510 USDC | 0.083108 USDC | 0.000000 USDC | 0.007972 USDC | 0.075136 USDC (0.0691 €) | — | 0.76 | 0.119 (n=150) | REJECTED | below_safety_margin(75136<198271), p_lower_below_threshold(0.12<0.75) |
| 52815204 | WETH→[uniswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.413929 WETH | 0.000035 WETH | 0.000000 WETH | 0.000003 WETH | 0.000031 WETH (0.0691 €) | — | 0.76 | 0.119 (n=150) | REJECTED | below_safety_margin(31372499522352<82785743021120), p_lower_below_threshold(0.12<0.75) |
| 52815204 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→cbBTC | 0.011396 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0641 €) | — | 0.75 | 0.119 (n=150) | REJECTED | below_safety_margin(85<227), p_lower_below_threshold(0.12<0.75) |
| 52815204 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 886.244816 USDC | 0.077173 USDC | 0.000000 USDC | 0.007972 USDC | 0.069201 USDC (0.0637 €) | — | 0.78 | 0.119 (n=150) | REJECTED | below_safety_margin(69201<177248), p_lower_below_threshold(0.12<0.75) |
| 52815204 | WETH→[uniswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.366775 WETH | 0.000032 WETH | 0.000000 WETH | 0.000003 WETH | 0.000029 WETH (0.0636 €) | — | 0.79 | 0.119 (n=150) | REJECTED | below_safety_margin(28893202127362<73354944348218), p_lower_below_threshold(0.12<0.75) |
| 52815907 | USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 212.829066 USDC | 0.067681 USDC | 0.000000 USDC | 0.007966 USDC | 0.059715 USDC (0.0549 €) | — | 2.81 | 0.292 (n=72) | REJECTED | p_lower_below_threshold(0.29<0.75) |
| 52815907 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH | 0.088490 WETH | 0.000028 WETH | 0.000000 WETH | 0.000003 WETH | 0.000025 WETH (0.0548 €) | 0.000025 WETH | 2.80 | 0.292 (n=72) | REJECTED | p_lower_below_threshold(0.29<0.75) |
| 52815225 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 393.383697 USDC | 0.062903 USDC | 0.000000 USDC | 0.006146 USDC | 0.056757 USDC (0.0522 €) | — | 1.44 | 0.017 (n=49) | REJECTED | below_safety_margin(56757<78676), p_lower_below_threshold(0.02<0.75) |

## Fiabilité et décision
- Observations ghost : 1315 ; taux observé 0.105 ; borne inférieure crédible (0.9) 0.095 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 9.5% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
