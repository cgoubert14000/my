# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-19T10:11:18+00:00 ; durée 163.93 min ; blocs 52802745 → 52807662 (4895 vus)

## Connexion
- Requêtes RPC : 65723 ; erreurs : 21 ; latence p50/p95 : 106.0/378.1 ms
- Rafraîchissements d'état : 4896 ; âge des données au dernier bloc : 1.88 s ; changements de frais LP observés (pools à frais dynamiques) : 10480
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 49677 ; cycles déclenchés par événement : 3613 ; avance médiane sur le rafraîchissement multicall : 475 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,436.67 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 575 pools, 328 jetons, 21198 routes
- Par DEX : uniswap_v3 138, aerodrome 234, aerodrome_slipstream 156, pancakeswap_v3 30, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 207 (rejetés 2) → 612 jetons ; pools candidats 3877 (énumérés 392, par paires 0), mesurés 577, sous le plancher de 10000.0 $ : 2 → gardés 575 (max 1500) ; prix des hubs : {'USDC': 1.0, 'DAI': 1.0, 'USDbC': 1.0, 'WETH': 2427.085029, 'AERO': 0.802709, 'cbBTC': 82780.001526}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 148,192,042 | 2,436.671239 | 52807662 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 35,360,876 | 1.256298 | 52807662 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 500 | 18,462,881 | 0.029431 | 52807662 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 18,444,709 | 0.029384 | 52807662 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/VVV | 3000 | 17,362,786 | 101.758809 | 52807662 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,504,673 | 0.029371 | 52807662 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,864,930 | 0.000012 | 52807662 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 8,497,905 | 2,433.282141 | 52807662 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome_slipstream | USDC/cbBTC | 344 | 7,851,496 | 0.000012 | 52807662 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 698 | 7,422,246 | 2,432.536235 | 52807662 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,257,622 | 0.001664 | 52807662 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 460 | 6,853,761 | 0.000012 | 52807662 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome | WETH/USDC | 3000 | 5,505,258 | 2,437.354021 | 52807662 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,397,774 | 0.029424 | 52807662 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/superOETHb | 400 | 5,291,404 | 1.000854 | 52807662 | `0x6446021F4E396dA3df4235C62537431372195D38` |
| aerodrome | fBOMB/AERO | 10000 | 4,879,760 | 0.025982 | 52807662 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,870,131 | 0.802398 | 52807662 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,682,153 | 0.000273 | 52807662 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,466,470 | 2,432.307667 | 52807662 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,386,765 | 0.998772 | 52807662 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome_slipstream | USDC/AERO | 10000 | 4,243,754 | 1.251497 | 52807662 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome | WETH/KTA | 3000 | 4,090,503 | 33,656.132849 | 52807662 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDT | 424 | 3,857,401 | 2,436.348018 | 52807662 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome | WETH/AERO | 10000 | 3,291,577 | 3,045.171794 | 52807662 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,936,534 | 1.141883 | 52807662 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,867,841 | 0.000012 | 52807662 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/MORPHO | 2718 | 2,862,757 | 984.107650 | 52807662 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,711,704 | 405.596069 | 52807662 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | WETH/VVV | 2733 | 2,667,460 | 101.739619 | 52807662 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 2,605,445 | 0.000010 | 52807662 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | WETH/FAI | 10000 | 2,214,525 | 1,229,022.349210 | 52807662 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,061,648 | 1.235099 | 52807662 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | BNKR/WETH | 10000 | 2,054,428 | 0.000000 | 52807662 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,036,743 | 1.372638 | 52807662 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,957,280 | 15.931749 | 52807662 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,785,422 | 0.000012 | 52807662 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | weETH_04c0/WETH | 500 | 1,761,914 | 1.105523 | 52807662 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| uniswap_v3 | XDP/USDC | 100 | 1,754,702 | 0.018457 | 52807662 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome | fBOMB/USDC | 10000 | 1,727,972 | 0.020644 | 52807662 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| aerodrome | WETH/msETH (stable) | 500 | 1,681,475 | 2.310928 | 52807662 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,669,170 | 13,778.554667 | 52807662 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | WETH/AERO | 3000 | 1,622,708 | 3,056.302270 | 52807662 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,578,254 | 0.916350 | 52807662 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| aerodrome_slipstream | EURC/USDC | 73 | 1,470,417 | 1.120880 | 52807662 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,454,592 | 0.827269 | 52807662 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,340,589 | 0.436773 | 52807662 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,333,335 | 0.000000 | 52807662 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,312,409 | 0.000273 | 52807662 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,295,579 | 0.004561 | 52807662 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,292,093 | 23.159771 | 52807662 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| aerodrome | WETH/cbBTC | 3000 | 1,289,680 | 0.029366 | 52807662 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| aerodrome | WETH/WELL | 10000 | 1,237,210 | 1,051,690.494236 | 52807662 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome | USDC/SEND | 3000 | 1,232,995 | 63.917537 | 52807662 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome_slipstream | msUSD/USDC | 500 | 1,231,375 | 0.886381 | 52807662 | `0x7501bc8Bb51616F79bfA524E464fb7B41f0B10fB` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,215,209 | 2,433.227225 | 52807662 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | WETH/doginme | 10000 | 1,214,317 | 35,089,624.498354 | 52807662 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,146,656 | 515,481.870232 | 52807662 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | USDC/NOCK | 3000 | 1,099,412 | 52.130939 | 52807662 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,080,690 | 15.388617 | 52807662 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,074,461 | 1.105810 | 52807662 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |

## Recherche d'opportunités
- Cycles : 8508 ; routes examinées : 180352584 ; candidats optimisés : 1060401 ; net attendu > 0 : 101 ; dernier cycle 153.0 ms
- Rejets (moteur) : {'spread_below_threshold': 177515224, 'liquidity_below_min': 1516244, 'negative_expected_net': 1060300, 'borrow_bound_too_small': 162249, 'pool_quarantined': 97812, 'cycle_budget_exhausted': 654}
- Enregistrements de la session : 1060401 ; net attendu > 0 : 101 ; simulés (eth_call de la vraie tx) : 18 (ok 6, échec 12) ; étiquettes ghost N+1 : 2/12 positives
- Décisions : {'REJECTED': 1060401} ; motifs de rejet : {'below_safety_margin': 78, 'negative_expected_net': 1060300, 'p_lower_below_threshold': 72, 'reliability_not_demonstrated': 29, 'simulation_failed': 12}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52802789 | USDC→[pancakeswap_v3]→PLAY→[aerodrome_slipstream]→USDC | 103.887016 USDC | 0.252695 USDC | 0.000000 USDC | 0.005449 USDC | 0.247246 USDC (0.2275 €) | — | 23.80 | 0.002 (n=4) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52802771 | WETH→[uniswap_v3]→NPC→[uniswap_v2]→WETH | 0.015606 WETH | 0.000026 WETH | 0.000000 WETH | 0.000002 WETH | 0.000024 WETH (0.0534 €) | — | 15.33 | — (n=0) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52802789 | USDC→[pancakeswap_v3]→PLAY→[aerodrome]→USDC | 20.416455 USDC | 0.042548 USDC | 0.000000 USDC | 0.005114 USDC | 0.037434 USDC (0.0344 €) | — | 18.34 | 0.001 (n=6) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52807301 | WETH→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.080174 WETH | 0.000016 WETH | 0.000000 WETH | 0.000002 WETH | 0.000013 WETH (0.0300 €) | — | 1.67 | 0.017 (n=49) | REJECTED | below_safety_margin(13391648405460<16034862175564), p_lower_below_threshold(0.02<0.75) |
| 52807301 | WETH→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.080174 WETH | 0.000016 WETH | 0.000000 WETH | 0.000002 WETH | 0.000013 WETH (0.0300 €) | — | 1.67 | 0.017 (n=49) | REJECTED | below_safety_margin(13391648405460<16034862175564), p_lower_below_threshold(0.02<0.75) |
| 52807301 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→cbBTC | 0.002422 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0297 €) | — | 1.61 | 0.017 (n=49) | REJECTED | below_safety_margin(39<48), p_lower_below_threshold(0.02<0.75) |
| 52807301 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→cbBTC | 0.002422 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0297 €) | — | 1.61 | 0.017 (n=49) | REJECTED | below_safety_margin(39<48), p_lower_below_threshold(0.02<0.75) |
| 52802956 | USDC→[aerodrome]→MET→[aerodrome]→WETH→[uniswap_v3]→USDC | 49.367589 USDC | 0.035707 USDC | 0.000000 USDC | 0.006635 USDC | 0.029072 USDC (0.0267 €) | — | 5.89 | 0.031 (n=92) | REJECTED | p_lower_below_threshold(0.03<0.75) |
| 52802956 | WETH→[uniswap_v3]→USDC→[aerodrome]→MET→[aerodrome]→WETH | 0.020334 WETH | 0.000015 WETH | 0.000000 WETH | 0.000003 WETH | 0.000012 WETH (0.0266 €) | — | 5.86 | 0.031 (n=92) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.03<0.75) |
| 52802956 | USDC→[aerodrome]→MET→[aerodrome]→WETH→[pancakeswap_v3]→USDC | 45.876940 USDC | 0.030372 USDC | 0.000000 USDC | 0.006635 USDC | 0.023737 USDC (0.0218 €) | — | 5.17 | 0.009 (n=32) | REJECTED | p_lower_below_threshold(0.01<0.75) |
| 52802956 | WETH→[pancakeswap_v3]→USDC→[aerodrome]→MET→[aerodrome]→WETH | 0.018878 WETH | 0.000012 WETH | 0.000000 WETH | 0.000003 WETH | 0.000010 WETH (0.0217 €) | — | 5.15 | 0.009 (n=32) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.01<0.75) |
| 52807301 | WETH→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.060547 WETH | 0.000011 WETH | 0.000000 WETH | 0.000003 WETH | 0.000007 WETH (0.0165 €) | — | 1.22 | 0.098 (n=146) | REJECTED | below_safety_margin(7368747136994<12109364047159), p_lower_below_threshold(0.10<0.75) |
| 52807301 | WETH→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.060547 WETH | 0.000011 WETH | 0.000000 WETH | 0.000003 WETH | 0.000007 WETH (0.0165 €) | — | 1.22 | 0.098 (n=146) | REJECTED | below_safety_margin(7368747136994<12109364047159), p_lower_below_threshold(0.10<0.75) |
| 52807301 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 139.638563 USDC | 0.025585 USDC | 0.000000 USDC | 0.007703 USDC | 0.017882 USDC (0.0165 €) | — | 1.28 | 0.098 (n=146) | REJECTED | below_safety_margin(17882<27927), p_lower_below_threshold(0.10<0.75) |
| 52807301 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 139.638563 USDC | 0.025585 USDC | 0.000000 USDC | 0.007703 USDC | 0.017882 USDC (0.0165 €) | — | 1.28 | 0.098 (n=146) | REJECTED | below_safety_margin(17882<27927), p_lower_below_threshold(0.10<0.75) |
| 52807301 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→cbBTC | 0.001547 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0160 €) | — | 1.36 | 0.098 (n=146) | REJECTED | below_safety_margin(21<30), p_lower_below_threshold(0.10<0.75) |
| 52807301 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→cbBTC | 0.001547 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0160 €) | — | 1.36 | 0.098 (n=146) | REJECTED | below_safety_margin(21<30), p_lower_below_threshold(0.10<0.75) |
| 52803331 | WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.227161 WETH | 0.000009 WETH | 0.000000 WETH | 0.000003 WETH | 0.000006 WETH (0.0132 €) | — | 0.26 | 0.098 (n=146) | REJECTED | below_safety_margin(5909103348279<45432209893061), p_lower_below_threshold(0.10<0.75) |
| 52803331 | WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.227161 WETH | 0.000009 WETH | 0.000000 WETH | 0.000003 WETH | 0.000006 WETH (0.0132 €) | — | 0.26 | 0.098 (n=146) | REJECTED | below_safety_margin(5909103348279<45432209893061), p_lower_below_threshold(0.10<0.75) |
| 52803331 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC | 547.409941 USDC | 0.022032 USDC | 0.000000 USDC | 0.007686 USDC | 0.014346 USDC (0.0132 €) | — | 0.26 | 0.098 (n=146) | REJECTED | below_safety_margin(14346<109481), p_lower_below_threshold(0.10<0.75) |
| 52803331 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC | 547.409941 USDC | 0.022032 USDC | 0.000000 USDC | 0.007686 USDC | 0.014346 USDC (0.0132 €) | — | 0.26 | 0.098 (n=146) | REJECTED | below_safety_margin(14346<109481), p_lower_below_threshold(0.10<0.75) |
| 52804839 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 26.372935 USDC | 0.016089 USDC | 0.000000 USDC | 0.005465 USDC | 0.010624 USDC (0.0098 €) | 0.010624 USDC | 4.03 | 0.000 (n=84) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 52804839 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 26.372935 USDC | 0.016089 USDC | 0.000000 USDC | 0.005465 USDC | 0.010624 USDC (0.0098 €) | 0.010624 USDC | 4.03 | 0.000 (n=84) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 52802956 | USDC→[aerodrome]→MET→[aerodrome]→WETH→[uniswap_v3]→USDC | 34.391612 USDC | 0.016977 USDC | 0.000000 USDC | 0.006635 USDC | 0.010342 USDC (0.0095 €) | — | 3.01 | 0.031 (n=92) | REJECTED | p_lower_below_threshold(0.03<0.75) |
| 52802956 | WETH→[uniswap_v3]→USDC→[aerodrome]→MET→[aerodrome]→WETH | 0.014144 WETH | 0.000007 WETH | 0.000000 WETH | 0.000003 WETH | 0.000004 WETH (0.0095 €) | — | 2.99 | 0.115 (n=59) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.12<0.75) |

## Fiabilité et décision
- Observations ghost : 1267 ; taux observé 0.103 ; borne inférieure crédible (0.9) 0.093 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 9.3% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
