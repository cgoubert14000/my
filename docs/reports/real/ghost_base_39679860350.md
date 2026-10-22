# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-22T02:08:20+00:00 ; durée 269.43 min ; blocs 52914691 → 52922768 (7652 vus)

## Connexion
- Requêtes RPC : 93996 ; erreurs : 35 ; latence p50/p95 : 102.8/2,039.1 ms
- Rafraîchissements d'état : 7652 ; âge des données au dernier bloc : 5.44 s ; changements de frais LP observés (pools à frais dynamiques) : 15896
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 20975 ; cycles déclenchés par événement : 1412 ; avance médiane sur le rafraîchissement multicall : 780 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,451.37 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 579 pools, 326 jetons, 22742 routes
- Par DEX : uniswap_v3 137, aerodrome 234, aerodrome_slipstream 158, pancakeswap_v3 32, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 206 (rejetés 2) → 611 jetons ; pools candidats 3912 (énumérés 393, par paires 0), mesurés 581, sous le plancher de 10000.0 $ : 2 → gardés 579 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'DAI': 1.0, 'USDC': 1.0, 'WETH': 2492.485305, 'AERO': 0.830593, 'cbBTC': 84747.685068}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 156,722,029 | 2,451.370935 | 52922769 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 26,239,150 | 1.216611 | 52922769 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| aerodrome | WETH/VVV | 3000 | 16,770,678 | 89.241724 | 52922769 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,470,930 | 0.029374 | 52922769 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,473,150 | 0.029404 | 52922769 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,892,472 | 0.000012 | 52922769 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 9,871,767 | 0.029387 | 52922769 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/USDC | 500 | 8,775,830 | 2,445.970055 | 52922769 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/USDC | 3000 | 7,413,522 | 2,451.419902 | 52922769 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,310,071 | 0.001662 | 52922769 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 344 | 7,199,050 | 0.000012 | 52922769 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 698 | 6,703,989 | 2,445.639661 | 52922769 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | USDC/cbBTC | 472 | 6,038,255 | 0.000012 | 52922769 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,564,872 | 0.029382 | 52922769 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,561,998 | 2,445.519234 | 52922769 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,391,490 | 0.999953 | 52922769 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,164,244 | 0.000278 | 52922769 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome | WETH/KTA | 3000 | 4,053,111 | 34,693.581837 | 52922769 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDT | 427 | 2,992,531 | 2,449.447611 | 52922769 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome_slipstream | WETH/VVV | 2709 | 2,835,344 | 89.234948 | 52922769 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | WETH/AERO | 10000 | 2,558,802 | 2,976.532056 | 52922769 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,423,200 | 393.121247 | 52922769 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,266,881 | 0.000012 | 52922769 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | WETH/FAI | 10000 | 2,256,745 | 1,197,040.597603 | 52922769 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 2,100,365 | 0.000012 | 52922769 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,942,299 | 0.000000 | 52922769 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome_slipstream | WETH/wstETH | 90 | 1,900,909 | 0.802237 | 52922769 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| uniswap_v3 | XDP/USDC | 100 | 1,799,892 | 0.018597 | 52922769 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome | weETH_04c0/WETH | 500 | 1,785,489 | 1.105712 | 52922769 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,703,276 | 1.496821 | 52922769 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome | fBOMB/AERO | 10000 | 1,686,461 | 0.023325 | 52922769 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome | USDC/alUSDb (stable) | 500 | 1,678,069 | 1.402960 | 52922769 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| aerodrome | WETH/msETH (stable) | 500 | 1,672,076 | 2.310757 | 52922769 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | WETH/AERO | 3000 | 1,662,392 | 2,978.748085 | 52922769 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,583,391 | 16.029102 | 52922769 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| uniswap_v2 | WETH/USDC | 3000 | 1,548,015 | 2,450.201114 | 52922769 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,487,846 | 13,399.377207 | 52922769 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,457,615 | 0.826754 | 52922769 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | DRB/WETH | 10000 | 1,397,566 | 0.000000 | 52922769 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,381,453 | 0.004886 | 52922769 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,334,085 | 0.000277 | 52922769 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 1,297,175 | 0.000010 | 52922769 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,284,264 | 2,445.965486 | 52922769 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,231,886 | 64.032620 | 52922769 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome | WETH/WELL | 10000 | 1,228,334 | 1,079,023.892203 | 52922769 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,222,231 | 0.915911 | 52922769 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| uniswap_v3 | WETH/doginme | 10000 | 1,221,904 | 35,199,717.435612 | 52922769 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | USDC/NOCK | 3000 | 1,200,276 | 43.736776 | 52922769 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,183,676 | 23.121703 | 52922769 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,181,951 | 492,403.031955 | 52922769 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | WETH/EDEL | 7000 | 1,164,884 | 71,192.385394 | 52922769 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | fBOMB/USDC | 10000 | 1,157,604 | 0.019356 | 52922769 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,091,978 | 21,166,261.097057 | 52922769 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome | WETH/cbBTC | 3000 | 1,080,460 | 0.029410 | 52922769 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| aerodrome_slipstream | EURC/USDC | 73 | 1,074,347 | 1.123463 | 52922769 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,057,765 | 16.276095 | 52922769 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | USDC/VVV | 3000 | 1,002,114 | 0.036402 | 52922769 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/MORPHO | 3000 | 980,172 | 1,052.158215 | 52922769 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome_slipstream | USDC/USDT | 11 | 952,934 | 1.001325 | 52922769 | `0xa41Bc0AFfbA7Fd420d186b84899d7ab2aC57fcD1` |
| aerodrome | msUSD/USDC (stable) | 500 | 939,983 | 0.433181 | 52922769 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |

## Recherche d'opportunités
- Cycles : 9063 ; routes examinées : 206110746 ; candidats optimisés : 1336541 ; net attendu > 0 : 293 ; dernier cycle 253.3 ms
- Rejets (moteur) : {'spread_below_threshold': 202218631, 'liquidity_below_min': 2033692, 'negative_expected_net': 1336248, 'pool_quarantined': 506172, 'borrow_bound_too_small': 9058, 'cycle_budget_exhausted': 6652}
- Enregistrements de la session : 1336541 ; net attendu > 0 : 293 ; simulés (eth_call de la vraie tx) : 85 (ok 9, échec 76) ; étiquettes ghost N+1 : 0/46 positives
- Décisions : {'REJECTED': 1336541} ; motifs de rejet : {'below_safety_margin': 171, 'negative_expected_net': 1336248, 'p_lower_below_threshold': 251, 'price_impact': 102, 'reliability_not_demonstrated': 42, 'simulation_failed': 76, 'stale_data': 10}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52915931 | USDC→[uniswap_v3]→OWB→[aerodrome]→USDC | 159.556387 USDC | 4.823624 USDC | 0.000000 USDC | 0.005306 USDC | 4.818318 USDC (4.4329 €) | — | 301.98 | 0.002 (n=5) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52921034 | WETH→[aerodrome_slipstream]→VVV→[aerodrome]→WETH | 0.528123 WETH | 0.000571 WETH | 0.000000 WETH | 0.000002 WETH | 0.000569 WETH (1.2944 €) | 0.000569 WETH | 10.78 | 0.001 (n=11) | REJECTED | reliability_not_demonstrated |
| 52915935 | USDC→[aerodrome]→OWB→[uniswap_v3]→USDC | 98.761994 USDC | 0.721808 USDC | 0.000000 USDC | 0.005311 USDC | 0.716497 USDC (0.6592 €) | — | 72.55 | 0.001 (n=6) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52921034 | WETH→[aerodrome_slipstream]→VIRTUAL→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.113620 WETH | 0.000077 WETH | 0.000000 WETH | 0.000003 WETH | 0.000074 WETH (0.1682 €) | 0.000074 WETH | 6.51 | 0.108 (n=165) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 52921034 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→VIRTUAL→[pancakeswap_v3]→USDC | 280.778322 USDC | 0.190310 USDC | 0.000000 USDC | 0.007512 USDC | 0.182798 USDC (0.1682 €) | — | 6.51 | 0.108 (n=165) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 52921034 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→VIRTUAL→[pancakeswap_v3]→USDC | 247.609122 USDC | 0.150127 USDC | 0.000000 USDC | 0.007512 USDC | 0.142615 USDC (0.1312 €) | — | 5.76 | 0.108 (n=165) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 52921034 | WETH→[aerodrome_slipstream]→VIRTUAL→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.100298 WETH | 0.000061 WETH | 0.000000 WETH | 0.000003 WETH | 0.000058 WETH (0.1312 €) | 0.000058 WETH | 5.75 | 0.108 (n=165) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 52921034 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→VIRTUAL→[pancakeswap_v3]→USDC | 232.816856 USDC | 0.139821 USDC | 0.000000 USDC | 0.007512 USDC | 0.132309 USDC (0.1217 €) | — | 5.68 | 0.108 (n=165) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 52921034 | WETH→[aerodrome_slipstream]→VIRTUAL→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.094320 WETH | 0.000057 WETH | 0.000000 WETH | 0.000003 WETH | 0.000054 WETH (0.1217 €) | — | 5.67 | 0.108 (n=165) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 52915567 | USDC→[aerodrome]→OWB→[uniswap_v3]→USDC | 31.983662 USDC | 0.077174 USDC | 0.000000 USDC | 0.005263 USDC | 0.071911 USDC (0.0662 €) | — | 22.48 | 0.000 (n=16) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52915729 | USDC→[uniswap_v3]→OWB→[aerodrome]→USDC | 31.332892 USDC | 0.075372 USDC | 0.000000 USDC | 0.005264 USDC | 0.070108 USDC (0.0645 €) | — | 22.38 | 0.000 (n=17) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52915437 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→WETH | 0.040504 WETH | 0.000028 WETH | 0.000000 WETH | 0.000003 WETH | 0.000025 WETH (0.0581 €) | — | 6.25 | 0.109 (n=163) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.11<0.75) |
| 52915437 | USDC→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 100.466132 USDC | 0.070583 USDC | 0.000000 USDC | 0.007495 USDC | 0.063088 USDC (0.0580 €) | — | 6.28 | 0.109 (n=163) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 52921034 | USDC→[sushiswap_v3]→WETH→[aerodrome_slipstream]→VIRTUAL→[pancakeswap_v3]→USDC | 121.326469 USDC | 0.070977 USDC | 0.000000 USDC | 0.007891 USDC | 0.063086 USDC (0.0580 €) | — | 5.20 | 0.108 (n=165) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 52921034 | WETH→[aerodrome_slipstream]→VIRTUAL→[pancakeswap_v3]→USDC→[sushiswap_v3]→WETH | 0.049227 WETH | 0.000029 WETH | 0.000000 WETH | 0.000003 WETH | 0.000025 WETH (0.0580 €) | — | 5.18 | 0.108 (n=165) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 52915437 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→WETH | 0.040412 WETH | 0.000028 WETH | 0.000000 WETH | 0.000003 WETH | 0.000025 WETH (0.0577 €) | — | 6.23 | 0.133 (n=89) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.13<0.75) |
| 52915437 | USDC→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 100.336417 USDC | 0.070164 USDC | 0.000000 USDC | 0.007495 USDC | 0.062669 USDC (0.0577 €) | — | 6.25 | 0.133 (n=89) | REJECTED | p_lower_below_threshold(0.13<0.75) |
| 52915437 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→WETH | 0.040023 WETH | 0.000028 WETH | 0.000000 WETH | 0.000003 WETH | 0.000025 WETH (0.0571 €) | — | 6.23 | 0.109 (n=163) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.11<0.75) |
| 52915437 | USDC→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 99.595363 USDC | 0.069558 USDC | 0.000000 USDC | 0.007495 USDC | 0.062063 USDC (0.0571 €) | — | 6.23 | 0.109 (n=163) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 52915437 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→WETH | 0.039020 WETH | 0.000027 WETH | 0.000000 WETH | 0.000003 WETH | 0.000024 WETH (0.0547 €) | — | 6.11 | 0.133 (n=89) | REJECTED | p_lower_below_threshold(0.13<0.75) |
| 52915437 | USDC→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 96.885708 USDC | 0.066862 USDC | 0.000000 USDC | 0.007495 USDC | 0.059367 USDC (0.0546 €) | — | 6.13 | 0.133 (n=89) | REJECTED | p_lower_below_threshold(0.13<0.75) |
| 52915437 | WETH→[sushiswap_v3]→USDC→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→WETH | 0.033505 WETH | 0.000026 WETH | 0.000000 WETH | 0.000003 WETH | 0.000023 WETH (0.0526 €) | — | 6.85 | 0.133 (n=89) | REJECTED | p_lower_below_threshold(0.13<0.75) |
| 52915437 | USDC→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→WETH→[sushiswap_v3]→USDC | 83.007657 USDC | 0.064632 USDC | 0.000000 USDC | 0.007495 USDC | 0.057137 USDC (0.0526 €) | — | 6.88 | 0.133 (n=89) | REJECTED | p_lower_below_threshold(0.13<0.75) |
| 52921034 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→VIRTUAL→[pancakeswap_v3]→USDC | 135.379872 USDC | 0.043973 USDC | 0.000000 USDC | 0.007512 USDC | 0.036461 USDC (0.0335 €) | — | 2.69 | 0.114 (n=203) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 52921034 | WETH→[aerodrome_slipstream]→VIRTUAL→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.054676 WETH | 0.000018 WETH | 0.000000 WETH | 0.000003 WETH | 0.000015 WETH (0.0335 €) | — | 2.70 | 0.114 (n=203) | REJECTED | p_lower_below_threshold(0.11<0.75) |

## Fiabilité et décision
- Observations ghost : 1796 ; taux observé 0.097 ; borne inférieure crédible (0.9) 0.088 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 8.8% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
