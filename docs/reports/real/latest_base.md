# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-18T20:27:05+00:00 ; durée 15.28 min ; blocs 52782478 → 52782938 (458 vus)

## Connexion
- Requêtes RPC : 6553 ; erreurs : 0 ; latence p50/p95 : 243.1/794.4 ms
- Rafraîchissements d'état : 458 ; âge des données au dernier bloc : 4.18 s ; changements de frais LP observés (pools à frais dynamiques) : 1416
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 13121 ; cycles déclenchés par événement : 702 ; avance médiane sur le rafraîchissement multicall : 529 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,341.17 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 569 pools, 326 jetons, 20804 routes
- Par DEX : uniswap_v3 135, aerodrome 232 (quarantaine 1), aerodrome_slipstream 153, pancakeswap_v3 31, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 205 (rejetés 2) → 610 jetons ; pools candidats 3913 (énumérés 387, par paires 0), mesurés 571, sous le plancher de 10000.0 $ : 2 → gardés 569 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'DAI': 1.0, 'USDC': 1.0, 'WETH': 2337.16445, 'AERO': 0.771529, 'cbBTC': 80785.7814}
- Pools en quarantaine : 1 — aerodrome:WETH/fBOMB@0x4F9Dc2: simulation failed ×5 (model/chain mismatch) — until block 52783083

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 144,213,324 | 2,342.562111 | 52782938 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 40,442,564 | 1.295340 | 52782938 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 500 | 17,716,923 | 0.029029 | 52782938 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 16,049,197 | 109.924350 | 52782938 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| aerodrome_slipstream | WETH/cbBTC | 2535 | 10,473,948 | 0.028970 | 52782938 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,134,523 | 0.028955 | 52782938 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,698,254 | 0.000012 | 52782938 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 8,189,012 | 2,348.490995 | 52782938 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome_slipstream | USDC/cbBTC | 556 | 7,917,726 | 0.000012 | 52782938 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome_slipstream | USDC/cbBTC | 360 | 7,804,807 | 0.000012 | 52782938 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 862 | 7,084,360 | 2,347.779720 | 52782938 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,998,131 | 0.001630 | 52782938 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | WETH/USDC | 3000 | 5,395,871 | 2,342.480429 | 52782938 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | USDC/AERO | 10000 | 5,246,049 | 1.288769 | 52782938 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,129,238 | 0.029039 | 52782938 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/superOETHb | 400 | 5,084,009 | 1.000854 | 52782938 | `0x6446021F4E396dA3df4235C62537431372195D38` |
| aerodrome | fBOMB/AERO | 10000 | 4,839,697 | 0.026126 | 52782938 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,679,692 | 0.802398 | 52782938 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,469,059 | 0.000269 | 52782938 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,365,507 | 2,348.905920 | 52782938 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,293,955 | 0.998069 | 52782938 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,950,615 | 33,308.771098 | 52782938 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDT | 463 | 3,471,160 | 2,352.082151 | 52782938 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome | WETH/AERO | 10000 | 3,169,441 | 3,014.284734 | 52782938 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,822,920 | 0.000012 | 52782938 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,821,364 | 1.141832 | 52782938 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,791,942 | 415.693724 | 52782938 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 2,442,492 | 0.000010 | 52782938 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/VVV | 2721 | 2,433,899 | 109.957409 | 52782938 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | WETH/FAI | 10000 | 2,147,514 | 1,206,478.919535 | 52782938 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,065,785 | 1.233147 | 52782938 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,036,703 | 1.372655 | 52782938 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,943,358 | 0.000000 | 52782938 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 1,936,734 | 1,025.900252 | 52782938 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome_slipstream | EURC/USDC | 70 | 1,932,344 | 1.121739 | 52782938 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,893,514 | 15.946124 | 52782938 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | fBOMB/USDC | 10000 | 1,774,753 | 0.020700 | 52782938 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,757,749 | 0.000012 | 52782938 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | XDP/USDC | 100 | 1,729,532 | 0.017962 | 52782938 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome | weETH_04c0/WETH | 500 | 1,692,918 | 1.105523 | 52782938 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome | WETH/msETH (stable) | 500 | 1,623,386 | 2.301920 | 52782938 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | WETH/AERO | 3000 | 1,565,535 | 3,035.239155 | 52782938 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,516,530 | 14,360.284437 | 52782938 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,455,768 | 0.826942 | 52782938 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,420,411 | 0.916353 | 52782938 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,317,780 | 0.434746 | 52782938 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,290,454 | 0.000000 | 52782938 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,252,634 | 0.000267 | 52782938 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | WETH/cbBTC | 3000 | 1,242,002 | 0.028956 | 52782938 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| aerodrome | USDC/SEND | 3000 | 1,233,273 | 63.888794 | 52782938 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome_slipstream | WETH/msETH | 500 | 1,227,824 | 1.130630 | 52782938 | `0x74F72788F4814D7fF3C49B44684aa98Eee140C0E` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,226,687 | 0.004510 | 52782938 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,206,326 | 23.271268 | 52782938 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,185,261 | 2,348.490995 | 52782938 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | WETH/doginme | 10000 | 1,182,495 | 33,768,726.579415 | 52782938 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | WETH/WELL | 10000 | 1,124,771 | 1,174,659.991479 | 52782938 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,096,429 | 532,522.038641 | 52782938 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,075,459 | 15.586720 | 52782938 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | USDC/NOCK | 3000 | 1,069,759 | 55.061011 | 52782938 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,027,567 | 1.105812 | 52782938 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |

## Recherche d'opportunités
- Cycles : 1159 ; routes examinées : 24111836 ; candidats optimisés : 102766 ; net attendu > 0 : 60 ; dernier cycle 295.4 ms
- Rejets (moteur) : {'spread_below_threshold': 23730536, 'liquidity_below_min': 214611, 'negative_expected_net': 102706, 'pool_quarantined': 62764, 'borrow_bound_too_small': 1159}
- Enregistrements de la session : 102766 ; net attendu > 0 : 60 ; simulés (eth_call de la vraie tx) : 12 (ok 0, échec 12) ; étiquettes ghost N+1 : 0/7 positives
- Décisions : {'REJECTED': 102766} ; motifs de rejet : {'below_safety_margin': 46, 'negative_expected_net': 102706, 'p_lower_below_threshold': 54, 'price_impact': 11, 'reliability_not_demonstrated': 6, 'simulation_failed': 12}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52782708 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 97.253897 USDC | 0.139738 USDC | 0.000000 USDC | 0.005252 USDC | 0.134486 USDC (0.1237 €) | — | 13.83 | 0.000 (n=24) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52782715 | USDC→[aerodrome_slipstream]→AERO→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 201.790613 USDC | 0.061459 USDC | 0.000000 USDC | 0.007028 USDC | 0.054431 USDC (0.0501 €) | — | 2.70 | 0.125 (n=115) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.13<0.75) |
| 52782715 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→AERO→[uniswap_v3]→WETH | 0.086322 WETH | 0.000026 WETH | 0.000000 WETH | 0.000003 WETH | 0.000023 WETH (0.0500 €) | — | 2.69 | 0.125 (n=115) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.13<0.75) |
| 52782715 | USDC→[aerodrome_slipstream]→AERO→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 119.449451 USDC | 0.027429 USDC | 0.000000 USDC | 0.007383 USDC | 0.020046 USDC (0.0184 €) | — | 1.68 | 0.306 (n=63) | REJECTED | below_safety_margin(20046<23889), p_lower_below_threshold(0.31<0.75) |
| 52782715 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→AERO→[uniswap_v3]→WETH | 0.051106 WETH | 0.000012 WETH | 0.000000 WETH | 0.000003 WETH | 0.000009 WETH (0.0184 €) | — | 1.68 | 0.306 (n=63) | REJECTED | below_safety_margin(8565993817297<10221179323370), p_lower_below_threshold(0.31<0.75) |
| 52782715 | USDC→[aerodrome_slipstream]→AERO→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 108.767595 USDC | 0.021155 USDC | 0.000000 USDC | 0.007028 USDC | 0.014127 USDC (0.0130 €) | — | 1.30 | 0.125 (n=115) | REJECTED | below_safety_margin(14127<21753), p_lower_below_threshold(0.13<0.75) |
| 52782715 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→AERO→[pancakeswap_v3]→WETH | 0.046481 WETH | 0.000009 WETH | 0.000000 WETH | 0.000003 WETH | 0.000006 WETH (0.0130 €) | — | 1.30 | 0.125 (n=115) | REJECTED | below_safety_margin(6033472141725<9296187388066), p_lower_below_threshold(0.13<0.75) |
| 52782727 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 188.934815 USDC | 0.018951 USDC | 0.000000 USDC | 0.005610 USDC | 0.013341 USDC (0.0123 €) | — | 0.71 | 0.019 (n=43) | REJECTED | below_safety_margin(13341<37786), p_lower_below_threshold(0.02<0.75) |
| 52782727 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.081240 WETH | 0.000008 WETH | 0.000000 WETH | 0.000002 WETH | 0.000006 WETH (0.0122 €) | — | 0.70 | 0.019 (n=43) | REJECTED | below_safety_margin(5693164396615<16248095555711), p_lower_below_threshold(0.02<0.75) |
| 52782617 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→tBTC→[aerodrome_slipstream]→USDC | 102.972905 USDC | 0.017881 USDC | 0.000000 USDC | 0.007032 USDC | 0.010849 USDC (0.0100 €) | — | 1.05 | 0.125 (n=115) | REJECTED | below_safety_margin(10849<20594), p_lower_below_threshold(0.13<0.75) |
| 52782617 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→tBTC→[aerodrome_slipstream]→USDC | 102.972905 USDC | 0.017881 USDC | 0.000000 USDC | 0.007032 USDC | 0.010849 USDC (0.0100 €) | — | 1.05 | 0.125 (n=115) | REJECTED | below_safety_margin(10849<20594), p_lower_below_threshold(0.13<0.75) |
| 52782617 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→tBTC→[aerodrome_slipstream]→USDC | 102.794059 USDC | 0.017734 USDC | 0.000000 USDC | 0.007032 USDC | 0.010702 USDC (0.0098 €) | — | 1.04 | 0.125 (n=115) | REJECTED | below_safety_margin(10702<20558), p_lower_below_threshold(0.13<0.75) |
| 52782618 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→tBTC→[aerodrome_slipstream]→USDC | 102.794059 USDC | 0.017734 USDC | 0.000000 USDC | 0.007032 USDC | 0.010702 USDC (0.0098 €) | — | 1.04 | 0.125 (n=115) | REJECTED | below_safety_margin(10702<20558), p_lower_below_threshold(0.13<0.75) |
| 52782617 | USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→tBTC→[aerodrome_slipstream]→USDC | 101.747493 USDC | 0.017585 USDC | 0.000000 USDC | 0.007032 USDC | 0.010553 USDC (0.0097 €) | — | 1.04 | 0.125 (n=115) | REJECTED | below_safety_margin(10553<20349), p_lower_below_threshold(0.13<0.75) |
| 52782617 | USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→tBTC→[aerodrome_slipstream]→USDC | 101.747493 USDC | 0.017585 USDC | 0.000000 USDC | 0.007032 USDC | 0.010553 USDC (0.0097 €) | — | 1.04 | 0.125 (n=115) | REJECTED | below_safety_margin(10553<20349), p_lower_below_threshold(0.13<0.75) |
| 52782617 | USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→tBTC→[aerodrome_slipstream]→USDC | 102.973047 USDC | 0.017572 USDC | 0.000000 USDC | 0.007032 USDC | 0.010540 USDC (0.0097 €) | — | 1.02 | 0.125 (n=115) | REJECTED | below_safety_margin(10540<20594), p_lower_below_threshold(0.13<0.75) |
| 52782618 | USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→tBTC→[aerodrome_slipstream]→USDC | 102.973047 USDC | 0.017572 USDC | 0.000000 USDC | 0.007032 USDC | 0.010540 USDC (0.0097 €) | — | 1.02 | 0.125 (n=115) | REJECTED | below_safety_margin(10540<20594), p_lower_below_threshold(0.13<0.75) |
| 52782616 | cbBTC→[pancakeswap_v3]→tBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.001150 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0097 €) | — | 1.13 | 0.125 (n=115) | REJECTED | below_safety_margin(13<23), p_lower_below_threshold(0.13<0.75) |
| 52782616 | cbBTC→[uniswap_v3]→tBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.001228 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0097 €) | — | 1.06 | 0.125 (n=115) | REJECTED | below_safety_margin(13<24), p_lower_below_threshold(0.13<0.75) |
| 52782616 | cbBTC→[pancakeswap_v3]→tBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.001150 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0097 €) | — | 1.13 | 0.125 (n=115) | REJECTED | below_safety_margin(13<23), p_lower_below_threshold(0.13<0.75) |
| 52782616 | cbBTC→[uniswap_v3]→tBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.001228 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0097 €) | — | 1.06 | 0.125 (n=115) | REJECTED | below_safety_margin(13<24), p_lower_below_threshold(0.13<0.75) |
| 52782617 | cbBTC→[aerodrome_slipstream]→tBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.001321 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0097 €) | — | 0.98 | 0.125 (n=115) | REJECTED | below_safety_margin(13<26), p_lower_below_threshold(0.13<0.75) |
| 52782617 | cbBTC→[uniswap_v3]→tBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.001321 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0097 €) | — | 0.98 | 0.125 (n=115) | REJECTED | below_safety_margin(13<26), p_lower_below_threshold(0.13<0.75) |
| 52782617 | cbBTC→[aerodrome_slipstream]→tBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.001321 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0097 €) | — | 0.98 | 0.125 (n=115) | REJECTED | below_safety_margin(13<26), p_lower_below_threshold(0.13<0.75) |
| 52782617 | cbBTC→[uniswap_v3]→tBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.001321 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0097 €) | — | 0.98 | 0.125 (n=115) | REJECTED | below_safety_margin(13<26), p_lower_below_threshold(0.13<0.75) |

## Fiabilité et décision
- Observations ghost : 1080 ; taux observé 0.112 ; borne inférieure crédible (0.9) 0.100 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 10.0% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
