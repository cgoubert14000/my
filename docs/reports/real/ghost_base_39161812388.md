# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-18T20:30:11+00:00 ; durée 18.37 min ; blocs 52782478 → 52783031 (551 vus)

## Connexion
- Requêtes RPC : 7863 ; erreurs : 0 ; latence p50/p95 : 279.5/806.8 ms
- Rafraîchissements d'état : 551 ; âge des données au dernier bloc : 3.0 s ; changements de frais LP observés (pools à frais dynamiques) : 1678
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 15489 ; cycles déclenchés par événement : 814 ; avance médiane sur le rafraîchissement multicall : 975 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,344.53 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 569 pools, 326 jetons, 20804 routes
- Par DEX : uniswap_v3 135, aerodrome 232 (quarantaine 2), aerodrome_slipstream 153, pancakeswap_v3 31, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 205 (rejetés 2) → 610 jetons ; pools candidats 3913 (énumérés 387, par paires 0), mesurés 571, sous le plancher de 10000.0 $ : 2 → gardés 569 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'DAI': 1.0, 'USDC': 1.0, 'WETH': 2337.16445, 'AERO': 0.771529, 'cbBTC': 80785.7814}
- Pools en quarantaine : 2 — aerodrome:fBOMB/AERO@0xbBf71A: simulation failed ×5 (model/chain mismatch) — until block 52783308; aerodrome:WETH/fBOMB@0x4F9Dc2: simulation failed ×5 (model/chain mismatch) — until block 52783083

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 144,375,073 | 2,344.507729 | 52783031 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 40,462,870 | 1.294040 | 52783031 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 500 | 17,741,472 | 0.029042 | 52783031 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 16,060,899 | 110.080079 | 52783031 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| aerodrome_slipstream | WETH/cbBTC | 2535 | 12,815,720 | 0.028989 | 52783031 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,147,666 | 0.028971 | 52783031 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,702,465 | 0.000012 | 52783031 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome_slipstream | USDC/cbBTC | 508 | 9,095,095 | 0.000012 | 52783031 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | WETH/USDC | 500 | 8,197,959 | 2,348.248626 | 52783031 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome_slipstream | USDC/cbBTC | 346 | 7,807,908 | 0.000012 | 52783031 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 669 | 7,158,697 | 2,347.769067 | 52783031 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,006,419 | 0.001631 | 52783031 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | WETH/USDC | 3000 | 5,399,747 | 2,344.707778 | 52783031 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | USDC/AERO | 10000 | 5,248,766 | 1.288769 | 52783031 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,137,894 | 0.029038 | 52783031 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/superOETHb | 400 | 5,091,315 | 1.000854 | 52783031 | `0x6446021F4E396dA3df4235C62537431372195D38` |
| aerodrome | fBOMB/AERO | 10000 | 4,842,098 | 0.026126 | 52783031 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,686,417 | 0.802398 | 52783031 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,475,482 | 0.000269 | 52783031 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,370,536 | 2,348.245494 | 52783031 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,297,967 | 0.998069 | 52783031 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,956,293 | 33,308.771098 | 52783031 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/AERO | 10000 | 3,173,312 | 3,014.284734 | 52783031 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | WETH/USDT | 430 | 3,007,527 | 2,352.606941 | 52783031 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,825,418 | 1.141832 | 52783031 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,824,574 | 0.000012 | 52783031 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,607,499 | 415.693724 | 52783031 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 2,453,727 | 0.000010 | 52783031 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/VVV | 2748 | 2,435,285 | 110.110054 | 52783031 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | WETH/FAI | 10000 | 2,150,559 | 1,206,525.597601 | 52783031 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,065,785 | 1.233147 | 52783031 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,036,703 | 1.372655 | 52783031 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,945,996 | 0.000000 | 52783031 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome_slipstream | EURC/USDC | 70 | 1,932,204 | 1.121629 | 52783031 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| aerodrome_slipstream | WETH/MORPHO | 2730 | 1,826,433 | 1,026.960436 | 52783031 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome | fBOMB/USDC | 10000 | 1,774,754 | 0.020700 | 52783031 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,758,788 | 0.000012 | 52783031 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,750,894 | 15.946124 | 52783031 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| uniswap_v3 | XDP/USDC | 100 | 1,728,252 | 0.017939 | 52783031 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome | weETH_04c0/WETH | 500 | 1,695,351 | 1.105523 | 52783031 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome | WETH/msETH (stable) | 500 | 1,625,719 | 2.301920 | 52783031 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | WETH/AERO | 3000 | 1,567,430 | 3,035.239155 | 52783031 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,551,440 | 14,360.165550 | 52783031 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,455,850 | 0.826850 | 52783031 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,422,453 | 0.916353 | 52783031 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,317,780 | 0.434746 | 52783031 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,292,452 | 0.000000 | 52783031 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,254,434 | 0.000267 | 52783031 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | WETH/cbBTC | 3000 | 1,243,475 | 0.028966 | 52783031 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| aerodrome | USDC/SEND | 3000 | 1,233,273 | 63.888794 | 52783031 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,228,450 | 0.004510 | 52783031 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | WETH/msETH | 500 | 1,227,046 | 1.130643 | 52783031 | `0x74F72788F4814D7fF3C49B44684aa98Eee140C0E` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,209,616 | 23.276011 | 52783031 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,186,568 | 2,348.217011 | 52783031 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | WETH/doginme | 10000 | 1,184,194 | 33,768,726.579415 | 52783031 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | WETH/WELL | 10000 | 1,126,387 | 1,174,659.991479 | 52783031 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,098,004 | 532,522.038641 | 52783031 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,074,815 | 15.606200 | 52783031 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | USDC/NOCK | 3000 | 1,069,790 | 55.057827 | 52783031 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,029,044 | 1.105812 | 52783031 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |

## Recherche d'opportunités
- Cycles : 1364 ; routes examinées : 28376656 ; candidats optimisés : 141093 ; net attendu > 0 : 199 ; dernier cycle 278.1 ms
- Rejets (moteur) : {'spread_below_threshold': 27888877, 'liquidity_below_min': 258761, 'negative_expected_net': 140894, 'pool_quarantined': 86162, 'borrow_bound_too_small': 1364, 'cycle_budget_exhausted': 399}
- Enregistrements de la session : 141093 ; net attendu > 0 : 199 ; simulés (eth_call de la vraie tx) : 18 (ok 0, échec 18) ; étiquettes ghost N+1 : 0/12 positives
- Décisions : {'REJECTED': 141093} ; motifs de rejet : {'below_safety_margin': 84, 'negative_expected_net': 140894, 'p_lower_below_threshold': 144, 'price_impact': 13, 'reliability_not_demonstrated': 55, 'simulation_failed': 18}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52782961 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 516.106625 USDC | 0.154973 USDC | 0.000000 USDC | 0.007399 USDC | 0.147574 USDC (0.1358 €) | — | 2.86 | 0.003 (n=2) | REJECTED | reliability_not_demonstrated |
| 52782961 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.006038 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1351 €) | — | 3.01 | 0.003 (n=2) | REJECTED | reliability_not_demonstrated |
| 52782961 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.216555 WETH | 0.000066 WETH | 0.000000 WETH | 0.000003 WETH | 0.000063 WETH (0.1350 €) | — | 2.89 | 0.003 (n=2) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52782961 | USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 530.350793 USDC | 0.145165 USDC | 0.000000 USDC | 0.007043 USDC | 0.138122 USDC (0.1271 €) | — | 2.60 | 0.123 (n=117) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52782961 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→cbBTC | 0.006195 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1269 €) | — | 2.76 | 0.123 (n=117) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52782961 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.232551 WETH | 0.000062 WETH | 0.000000 WETH | 0.000003 WETH | 0.000059 WETH (0.1265 €) | — | 2.52 | 0.123 (n=117) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.12<0.75) |
| 52782708 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 97.253897 USDC | 0.139738 USDC | 0.000000 USDC | 0.005252 USDC | 0.134486 USDC (0.1237 €) | — | 13.83 | 0.000 (n=24) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52782961 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→cbBTC | 0.006037 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1150 €) | — | 2.57 | 0.123 (n=117) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52782961 | USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 499.915405 USDC | 0.131749 USDC | 0.000000 USDC | 0.007043 USDC | 0.124706 USDC (0.1147 €) | — | 2.49 | 0.123 (n=117) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52782961 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.213187 WETH | 0.000056 WETH | 0.000000 WETH | 0.000003 WETH | 0.000053 WETH (0.1142 €) | — | 2.49 | 0.123 (n=117) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.12<0.75) |
| 52782961 | USDC→[aerodrome_slipstream]→USDT→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 335.455591 USDC | 0.115142 USDC | 0.000000 USDC | 0.007043 USDC | 0.108099 USDC (0.0995 €) | — | 3.22 | 0.138 (n=98) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 52782961 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→USDT→[uniswap_v3]→WETH | 0.142816 WETH | 0.000049 WETH | 0.000000 WETH | 0.000003 WETH | 0.000046 WETH (0.0991 €) | — | 3.22 | 0.138 (n=98) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 52782961 | USDC→[uniswap_v3]→USDT→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 325.095969 USDC | 0.108813 USDC | 0.000000 USDC | 0.007043 USDC | 0.101770 USDC (0.0936 €) | — | 3.13 | 0.138 (n=98) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 52782961 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→USDT→[uniswap_v3]→WETH | 0.138573 WETH | 0.000046 WETH | 0.000000 WETH | 0.000003 WETH | 0.000043 WETH (0.0933 €) | — | 3.12 | 0.138 (n=98) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 52782961 | USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 245.098566 USDC | 0.092319 USDC | 0.000000 USDC | 0.007043 USDC | 0.085276 USDC (0.0785 €) | — | 3.48 | 0.138 (n=98) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 52782961 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH | 0.104213 WETH | 0.000039 WETH | 0.000000 WETH | 0.000003 WETH | 0.000036 WETH (0.0782 €) | — | 3.48 | 0.138 (n=98) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 52782961 | USDC→[pancakeswap_v3]→USDT→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 277.639968 USDC | 0.084404 USDC | 0.000000 USDC | 0.007043 USDC | 0.077361 USDC (0.0712 €) | — | 2.79 | 0.123 (n=117) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52782961 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→USDT→[uniswap_v3]→WETH | 0.117817 WETH | 0.000036 WETH | 0.000000 WETH | 0.000003 WETH | 0.000033 WETH (0.0709 €) | — | 2.79 | 0.123 (n=117) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52782961 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 255.694294 USDC | 0.075859 USDC | 0.000000 USDC | 0.007399 USDC | 0.068460 USDC (0.0630 €) | — | 2.68 | 0.123 (n=117) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52782961 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→WETH | 0.103645 WETH | 0.000032 WETH | 0.000000 WETH | 0.000003 WETH | 0.000029 WETH (0.0627 €) | — | 2.81 | 0.123 (n=117) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52782961 | cbBTC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.002762 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0623 €) | — | 3.04 | 0.138 (n=98) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 52782961 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.003148 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0616 €) | — | 2.64 | 0.003 (n=2) | REJECTED | reliability_not_demonstrated |
| 52782961 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 252.265960 USDC | 0.073982 USDC | 0.000000 USDC | 0.007043 USDC | 0.066939 USDC (0.0616 €) | — | 2.65 | 0.003 (n=2) | REJECTED | reliability_not_demonstrated |
| 52782961 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.109417 WETH | 0.000032 WETH | 0.000000 WETH | 0.000003 WETH | 0.000029 WETH (0.0615 €) | — | 2.61 | 0.003 (n=2) | REJECTED | reliability_not_demonstrated |
| 52782961 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 265.112487 USDC | 0.073023 USDC | 0.000000 USDC | 0.007754 USDC | 0.065269 USDC (0.0600 €) | — | 2.46 | 0.123 (n=117) | REJECTED | p_lower_below_threshold(0.12<0.75) |

## Fiabilité et décision
- Observations ghost : 1085 ; taux observé 0.112 ; borne inférieure crédible (0.9) 0.100 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 10.0% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
