# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-16T11:02:27+00:00 ; durée 285.04 min ; blocs 52671044 → 52679593 (7929 vus)

## Connexion
- Requêtes RPC : 103643 ; erreurs : 400 ; latence p50/p95 : 193.1/1,204.4 ms
- Rafraîchissements d'état : 7930 ; âge des données au dernier bloc : 1.54 s ; changements de frais LP observés (pools à frais dynamiques) : 19117
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 89756 ; cycles déclenchés par événement : 4609 ; avance médiane sur le rafraîchissement multicall : 942 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,458.73 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 576 pools, 327 jetons, 21788 routes
- Par DEX : uniswap_v3 137, aerodrome 236 (quarantaine 2), aerodrome_slipstream 153, pancakeswap_v3 32, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 209 (rejetés 2) → 614 jetons ; pools candidats 3925 (énumérés 392, par paires 0), mesurés 579, sous le plancher de 10000.0 $ : 3 → gardés 576 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2445.329592, 'AERO': 0.931569, 'cbBTC': 81962.021553}
- Pools en quarantaine : 2 — aerodrome:fBOMB/AERO@0xbBf71A: simulation failed ×5 (model/chain mismatch) — until block 52679848; aerodrome:WETH/fBOMB@0x4F9Dc2: simulation failed ×5 (model/chain mismatch) — until block 52679848

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 147,642,632 | 2,458.733084 | 52679593 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 46,988,336 | 1.091001 | 52679593 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 500 | 18,559,050 | 0.029988 | 52679593 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome_slipstream | WETH/cbBTC | 2505 | 18,451,001 | 0.029927 | 52679593 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/VVV | 3000 | 16,529,740 | 101.312010 | 52679593 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,547,187 | 0.029913 | 52679593 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,746,532 | 0.000012 | 52679593 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 9,150,448 | 2,463.023801 | 52679593 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome_slipstream | USDC/cbBTC | 424 | 8,160,058 | 0.000012 | 52679593 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome_slipstream | USDC/cbBTC | 332 | 8,093,776 | 0.000012 | 52679593 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 564 | 7,669,773 | 2,463.779016 | 52679593 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,253,967 | 0.001695 | 52679593 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | fBOMB/AERO | 10000 | 5,500,077 | 0.024768 | 52679593 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome | WETH/USDC | 3000 | 5,458,913 | 2,458.936757 | 52679593 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,426,664 | 0.029985 | 52679593 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/superOETHb | 400 | 5,253,887 | 1.000855 | 52679593 | `0x6446021F4E396dA3df4235C62537431372195D38` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,914,506 | 0.802398 | 52679593 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,784,231 | 0.000281 | 52679593 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,355,335 | 0.998889 | 52679593 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,343,166 | 2,463.827411 | 52679593 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | WETH/KTA | 3000 | 4,082,633 | 34,400.561236 | 52679593 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/AERO | 10000 | 3,566,442 | 2,667.054310 | 52679593 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | USDC/AERO | 10000 | 3,451,253 | 1.084049 | 52679593 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome_slipstream | cbETH/WETH | 60 | 3,052,193 | 1.141844 | 52679593 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| aerodrome_slipstream | WETH/MORPHO | 2718 | 2,931,362 | 993.352494 | 52679593 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,844,147 | 0.000012 | 52679593 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/VVV | 2700 | 2,672,274 | 101.368440 | 52679593 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,599,918 | 398.794424 | 52679593 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 2,559,492 | 0.000011 | 52679593 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | WETH/FAI | 10000 | 2,305,970 | 1,154,095.794367 | 52679593 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | WETH/USDT | 400 | 2,245,208 | 2,465.771540 | 52679593 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| uniswap_v3 | BNKR/WETH | 10000 | 2,117,920 | 0.000000 | 52679593 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,111,736 | 1.195936 | 52679593 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 2,059,585 | 15.258109 | 52679593 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,008,461 | 1.403757 | 52679593 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| aerodrome | fBOMB/USDC | 10000 | 1,867,597 | 0.023309 | 52679593 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,796,398 | 13,296.102486 | 52679593 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | XDP/USDC | 100 | 1,790,372 | 0.019062 | 52679593 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,777,324 | 0.000012 | 52679593 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | WETH/msETH (stable) | 500 | 1,697,395 | 2.309342 | 52679593 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | WETH/AERO | 3000 | 1,578,487 | 2,685.843822 | 52679593 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,528,317 | 0.916551 | 52679593 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| aerodrome | weETH_04c0/WETH | 500 | 1,520,251 | 1.105492 | 52679593 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome_slipstream | WETH/AERO | 3016 | 1,497,015 | 2,685.709816 | 52679593 | `0x82321f3BEB69f503380D6B233857d5C43562e2D0` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,456,120 | 0.825820 | 52679593 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | EURC/USDC | 70 | 1,391,531 | 1.125730 | 52679593 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,378,273 | 0.000000 | 52679593 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,374,897 | 0.004825 | 52679593 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,373,403 | 23.206518 | 52679593 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,342,919 | 0.000281 | 52679593 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,308,515 | 0.436378 | 52679593 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| aerodrome | USDC/SEND | 3000 | 1,250,804 | 62.110350 | 52679593 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,220,106 | 1.105591 | 52679593 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |
| uniswap_v3 | WETH/doginme | 10000 | 1,219,652 | 35,403,535.080362 | 52679593 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | WETH/cbBTC | 3000 | 1,218,801 | 0.029909 | 52679593 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,214,862 | 2,463.036235 | 52679593 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | WETH/WELL | 10000 | 1,213,173 | 1,113,851.211759 | 52679593 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,178,823 | 496,085.125904 | 52679593 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome_slipstream | msUSD/USDC | 500 | 1,161,186 | 0.886101 | 52679593 | `0x7501bc8Bb51616F79bfA524E464fb7B41f0B10fB` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,146,496 | 13.285860 | 52679593 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |

## Recherche d'opportunités
- Cycles : 12538 ; routes examinées : 273177944 ; candidats optimisés : 1389163 ; net attendu > 0 : 345 ; dernier cycle 190.2 ms
- Rejets (moteur) : {'spread_below_threshold': 268886883, 'liquidity_below_min': 2161709, 'negative_expected_net': 1388818, 'pool_quarantined': 725254, 'borrow_bound_too_small': 12533, 'cycle_budget_exhausted': 2402}
- Enregistrements de la session : 1389163 ; net attendu > 0 : 345 ; simulés (eth_call de la vraie tx) : 85 (ok 14, échec 71) ; étiquettes ghost N+1 : 3/46 positives
- Décisions : {'REJECTED': 1389163} ; motifs de rejet : {'below_safety_margin': 206, 'negative_expected_net': 1388818, 'p_lower_below_threshold': 160, 'price_impact': 111, 'reliability_not_demonstrated': 185, 'simulation_failed': 71, 'stale_data': 6}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52671989 | cbBTC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.028664 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.1011 €) | — | 0.47 | 0.001 (n=10) | REJECTED | below_safety_margin(134<573), reliability_not_demonstrated |
| 52671989 | WETH→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH | 1.051068 WETH | 0.000047 WETH | 0.000000 WETH | 0.000002 WETH | 0.000045 WETH (0.1011 €) | — | 0.43 | 0.001 (n=10) | REJECTED | below_safety_margin(44910967314113<210213569031069), reliability_not_demonstrated |
| 52677220 | cbBTC→[uniswap_v3]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.002693 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0854 €) | — | 4.20 | 0.233 (n=23) | REJECTED | reliability_not_demonstrated |
| 52677220 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[uniswap_v3]→USDC | 221.202314 USDC | 0.099215 USDC | 0.000000 USDC | 0.007377 USDC | 0.091838 USDC (0.0845 €) | — | 4.15 | 0.233 (n=23) | REJECTED | reliability_not_demonstrated |
| 52677220 | cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.002694 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0839 €) | — | 4.12 | 0.233 (n=23) | REJECTED | reliability_not_demonstrated |
| 52677220 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→USDC | 219.481750 USDC | 0.098552 USDC | 0.000000 USDC | 0.007377 USDC | 0.091175 USDC (0.0839 €) | — | 4.15 | 0.233 (n=23) | REJECTED | reliability_not_demonstrated |
| 52677220 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.002694 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0832 €) | — | 4.08 | 0.119 (n=57) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52677220 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 222.439475 USDC | 0.097929 USDC | 0.000000 USDC | 0.007749 USDC | 0.090180 USDC (0.0830 €) | — | 4.05 | 0.119 (n=57) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52677220 | cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.002359 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0748 €) | — | 4.20 | 0.233 (n=23) | REJECTED | reliability_not_demonstrated |
| 52677220 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→USDC | 187.810486 USDC | 0.087479 USDC | 0.000000 USDC | 0.007377 USDC | 0.080102 USDC (0.0737 €) | — | 4.27 | 0.233 (n=23) | REJECTED | reliability_not_demonstrated |
| 52677220 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.002015 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0643 €) | — | 4.22 | 0.119 (n=57) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52677220 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 174.775027 USDC | 0.076985 USDC | 0.000000 USDC | 0.007749 USDC | 0.069236 USDC (0.0637 €) | — | 3.96 | 0.119 (n=57) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52677220 | USDC→[uniswap_v3]→AERO→[aerodrome]→USDC | 146.123767 USDC | 0.045955 USDC | 0.000000 USDC | 0.005174 USDC | 0.040781 USDC (0.0375 €) | — | 2.79 | 0.143 (n=6) | REJECTED | reliability_not_demonstrated |
| 52677221 | USDC→[uniswap_v3]→AERO→[aerodrome]→USDC | 146.123767 USDC | 0.045955 USDC | 0.000000 USDC | 0.005174 USDC | 0.040781 USDC (0.0375 €) | — | 2.79 | 0.143 (n=6) | REJECTED | reliability_not_demonstrated |
| 52671989 | cbBTC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.007406 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0264 €) | — | 0.47 | 0.072 (n=50) | REJECTED | below_safety_margin(35<148), p_lower_below_threshold(0.07<0.75) |
| 52671989 | USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 665.496868 USDC | 0.036012 USDC | 0.000000 USDC | 0.007407 USDC | 0.028605 USDC (0.0263 €) | — | 0.43 | 0.072 (n=50) | REJECTED | below_safety_margin(28605<133099), p_lower_below_threshold(0.07<0.75) |
| 52671989 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH | 0.232200 WETH | 0.000015 WETH | 0.000000 WETH | 0.000003 WETH | 0.000012 WETH (0.0262 €) | — | 0.50 | 0.072 (n=50) | REJECTED | below_safety_margin(11661461449146<46439988969480), p_lower_below_threshold(0.07<0.75) |
| 52677220 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→WETH | 0.052428 WETH | 0.000015 WETH | 0.000000 WETH | 0.000003 WETH | 0.000012 WETH (0.0261 €) | — | 2.21 | 0.248 (n=35) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.25<0.75) |
| 52677220 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 127.229995 USDC | 0.035656 USDC | 0.000000 USDC | 0.007377 USDC | 0.028279 USDC (0.0260 €) | — | 2.22 | 0.248 (n=35) | REJECTED | p_lower_below_threshold(0.25<0.75) |
| 52677220 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→WETH | 0.051409 WETH | 0.000014 WETH | 0.000000 WETH | 0.000003 WETH | 0.000011 WETH (0.0252 €) | — | 2.17 | 0.072 (n=50) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.07<0.75) |
| 52677220 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 125.273527 USDC | 0.034630 USDC | 0.000000 USDC | 0.007377 USDC | 0.027253 USDC (0.0251 €) | — | 2.18 | 0.072 (n=50) | REJECTED | p_lower_below_threshold(0.07<0.75) |
| 52677221 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→WETH | 0.051086 WETH | 0.000014 WETH | 0.000000 WETH | 0.000003 WETH | 0.000011 WETH (0.0247 €) | — | 2.14 | 0.248 (n=35) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.25<0.75) |
| 52677221 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 124.819694 USDC | 0.034132 USDC | 0.000000 USDC | 0.007377 USDC | 0.026755 USDC (0.0246 €) | — | 2.14 | 0.248 (n=35) | REJECTED | p_lower_below_threshold(0.25<0.75) |
| 52671989 | WETH→[pancakeswap_v3]→cbBTC→[uniswap_v3]→tBTC→[aerodrome_slipstream]→WETH | 0.093167 WETH | 0.000014 WETH | 0.000000 WETH | 0.000003 WETH | 0.000011 WETH (0.0245 €) | — | 1.17 | 0.072 (n=50) | REJECTED | below_safety_margin(10874860639808<18633447966148), p_lower_below_threshold(0.07<0.75) |
| 52671989 | cbBTC→[uniswap_v3]→tBTC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC | 0.002696 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0241 €) | — | 1.19 | 0.072 (n=50) | REJECTED | below_safety_margin(32<53), p_lower_below_threshold(0.07<0.75) |

## Fiabilité et décision
- Observations ghost : 489 ; taux observé 0.125 ; borne inférieure crédible (0.9) 0.107 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 10.7% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
