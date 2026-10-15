# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-15T14:36:04+00:00 ; durée 67.47 min ; blocs 52640781 → 52642807 (1800 vus)

## Connexion
- Requêtes RPC : 23558 ; erreurs : 283 ; latence p50/p95 : 164.5/1,919.5 ms
- Rafraîchissements d'état : 1801 ; âge des données au dernier bloc : 1.53 s ; changements de frais LP observés (pools à frais dynamiques) : 10052
- Flux d'événements (WebSocket Swap/Sync) : non connecté ; événements appliqués : 0 ; cycles déclenchés par événement : 0 ; avance médiane sur le rafraîchissement multicall : — ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,369.09 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 570 pools, 326 jetons, 21328 routes
- Par DEX : uniswap_v3 136, aerodrome 235, aerodrome_slipstream 152, pancakeswap_v3 30, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 205 (rejetés 2) → 610 jetons ; pools candidats 3864 (énumérés 389, par paires 0), mesurés 572, sous le plancher de 10000.0 $ : 2 → gardés 570 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDC': 1.0, 'USDbC': 1.0, 'WETH': 2346.001193, 'AERO': 0.837627, 'cbBTC': 80168.530844}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 143,401,509 | 2,369.089880 | 52642807 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 44,779,537 | 1.148170 | 52642807 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 500 | 17,878,357 | 0.029214 | 52642807 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 15,996,821 | 100.882680 | 52642807 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 11,642,618 | 0.029197 | 52642807 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,311,423 | 0.029182 | 52642807 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,602,536 | 0.000012 | 52642807 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 8,926,351 | 2,372.404018 | 52642807 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/USDC | 3000 | 8,842,658 | 2,369.180660 | 52642807 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | USDC/cbBTC | 354 | 7,965,605 | 0.000012 | 52642807 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,096,897 | 0.001659 | 52642807 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | WETH/USDC | 818 | 6,818,459 | 2,372.471036 | 52642807 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | USDC/cbBTC | 556 | 6,551,915 | 0.000012 | 52642807 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome | fBOMB/AERO | 10000 | 5,253,246 | 0.026341 | 52642807 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,186,620 | 0.029226 | 52642807 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,561,304 | 0.000274 | 52642807 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,455,393 | 0.802388 | 52642807 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,267,626 | 0.999754 | 52642807 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,257,501 | 2,372.317837 | 52642807 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | USDC/AERO | 10000 | 4,202,896 | 1.155315 | 52642807 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome | WETH/KTA | 3000 | 3,890,533 | 35,169.675419 | 52642807 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/AERO | 10000 | 3,472,121 | 2,742.885321 | 52642807 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,833,293 | 0.000012 | 52642807 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,626,518 | 405.081339 | 52642807 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | WETH/VVV | 2727 | 2,567,202 | 100.859942 | 52642807 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,474,926 | 1.141648 | 52642807 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 2,466,351 | 0.000011 | 52642807 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | WETH/FAI | 10000 | 2,173,759 | 1,205,775.861383 | 52642807 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | WETH/USDT | 457 | 2,133,106 | 2,376.396710 | 52642807 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,112,870 | 1.194579 | 52642807 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,008,820 | 1.403288 | 52642807 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,972,738 | 0.000000 | 52642807 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome | fBOMB/USDC | 10000 | 1,855,578 | 0.022546 | 52642807 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,790,627 | 0.916541 | 52642807 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| uniswap_v3 | XDP/USDC | 100 | 1,790,042 | 0.019032 | 52642807 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,788,587 | 15.750435 | 52642807 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,759,010 | 0.000012 | 52642807 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | WETH/msETH (stable) | 500 | 1,678,936 | 2.301772 | 52642807 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,666,520 | 13,872.053982 | 52642807 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | WETH/AERO | 3000 | 1,490,503 | 2,722.696307 | 52642807 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | weETH_04c0/WETH | 500 | 1,464,785 | 1.105502 | 52642807 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,459,038 | 0.831422 | 52642807 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | WETH/AERO | 3000 | 1,340,673 | 2,723.725513 | 52642807 | `0x82321f3BEB69f503380D6B233857d5C43562e2D0` |
| uniswap_v3 | DRB/WETH | 10000 | 1,337,930 | 0.000000 | 52642807 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome_slipstream | WETH/msETH | 500 | 1,318,969 | 1.130750 | 52642807 | `0x74F72788F4814D7fF3C49B44684aa98Eee140C0E` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,292,322 | 23.111213 | 52642807 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,278,358 | 0.000276 | 52642807 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,277,521 | 0.004673 | 52642807 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome | USDC/SEND | 3000 | 1,247,214 | 62.468463 | 52642807 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome_slipstream | EURC/USDC | 82 | 1,246,661 | 1.121946 | 52642807 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,197,437 | 2,372.345004 | 52642807 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | WETH/doginme | 10000 | 1,175,780 | 35,293,678.832427 | 52642807 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,174,288 | 1.105591 | 52642807 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 1,152,309 | 1,011.725011 | 52642807 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome | WETH/cbBTC | 3000 | 1,141,365 | 0.029174 | 52642807 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| aerodrome | WETH/WELL | 10000 | 1,133,583 | 1,184,408.402905 | 52642807 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,123,426 | 505,056.837889 | 52642807 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | WETH/EDEL | 7000 | 1,118,942 | 78,004.729354 | 52642807 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,111,270 | 14.326701 | 52642807 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,105,199 | 0.435420 | 52642807 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |

## Recherche d'opportunités
- Cycles : 1800 ; routes examinées : 38390400 ; candidats optimisés : 265083 ; net attendu > 0 : 743 ; dernier cycle 593.6 ms
- Rejets (moteur) : {'spread_below_threshold': 37746308, 'liquidity_below_min': 334515, 'negative_expected_net': 264340, 'borrow_bound_too_small': 36878, 'unquotable': 4778, 'cycle_budget_exhausted': 2838}
- Enregistrements de la session : 265083 ; net attendu > 0 : 743 ; simulés (eth_call de la vraie tx) : 35 (ok 35, échec 0) ; étiquettes ghost N+1 : 3/34 positives
- Décisions : {'REJECTED': 265083} ; motifs de rejet : {'below_safety_margin': 417, 'negative_expected_net': 264340, 'p_lower_below_threshold': 305, 'reliability_not_demonstrated': 438, 'stale_data': 105}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52642035 | USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 442.062489 USDC | 0.298836 USDC | 0.000000 USDC | 0.008229 USDC | 0.290607 USDC (0.2674 €) | — | 6.57 | 0.164 (n=42) | REJECTED | p_lower_below_threshold(0.16<0.75) |
| 52642035 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH | 0.186091 WETH | 0.000126 WETH | 0.000000 WETH | 0.000003 WETH | 0.000122 WETH (0.2667 €) | 0.000122 WETH | 6.57 | 0.164 (n=42) | REJECTED | p_lower_below_threshold(0.16<0.75) |
| 52642035 | USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 420.852464 USDC | 0.288482 USDC | 0.000000 USDC | 0.007844 USDC | 0.280638 USDC (0.2582 €) | — | 6.67 | 0.164 (n=42) | REJECTED | p_lower_below_threshold(0.16<0.75) |
| 52642035 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH | 0.177158 WETH | 0.000121 WETH | 0.000000 WETH | 0.000003 WETH | 0.000118 WETH (0.2575 €) | 0.000118 WETH | 6.66 | 0.164 (n=42) | REJECTED | p_lower_below_threshold(0.16<0.75) |
| 52642035 | USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 307.929676 USDC | 0.182750 USDC | 0.000000 USDC | 0.007844 USDC | 0.174906 USDC (0.1609 €) | — | 5.68 | 0.346 (n=16) | REJECTED | reliability_not_demonstrated |
| 52642035 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH | 0.129817 WETH | 0.000077 WETH | 0.000000 WETH | 0.000003 WETH | 0.000074 WETH (0.1606 €) | 0.000074 WETH | 5.67 | 0.346 (n=16) | REJECTED | reliability_not_demonstrated |
| 52641554 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.516716 WETH | 0.000075 WETH | 0.000000 WETH | 0.000003 WETH | 0.000071 WETH (0.1533 €) | — | 1.38 | 0.104 (n=35) | REJECTED | below_safety_margin(71433138643533<103343199871391), p_lower_below_threshold(0.10<0.75) |
| 52641554 | USDC→[uniswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 1,203.605774 USDC | 0.174400 USDC | 0.000000 USDC | 0.008097 USDC | 0.166303 USDC (0.1530 €) | — | 1.38 | 0.104 (n=35) | REJECTED | below_safety_margin(166303<240721), p_lower_below_threshold(0.10<0.75) |
| 52641554 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→cbBTC | 0.014139 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1524 €) | — | 1.46 | 0.104 (n=35) | REJECTED | below_safety_margin(207<282), p_lower_below_threshold(0.10<0.75) |
| 52642035 | USDC→[uniswap_v3]→EDGE→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 127.730473 USDC | 0.143476 USDC | 0.000000 USDC | 0.007844 USDC | 0.135632 USDC (0.1248 €) | — | 10.62 | 0.001 (n=7) | REJECTED | reliability_not_demonstrated |
| 52642035 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→EDGE→[aerodrome_slipstream]→cbBTC | 0.001450 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1246 €) | — | 11.52 | 0.001 (n=7) | REJECTED | reliability_not_demonstrated |
| 52641540 | cbBTC→[aerodrome_slipstream]→tBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.005031 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1224 €) | — | 3.30 | 0.182 (n=38) | REJECTED | p_lower_below_threshold(0.18<0.75) |
| 52641540 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→tBTC→[aerodrome_slipstream]→USDC | 413.140761 USDC | 0.140506 USDC | 0.000000 USDC | 0.007578 USDC | 0.132928 USDC (0.1223 €) | 0.132928 USDC | 3.22 | 0.182 (n=38) | REJECTED | p_lower_below_threshold(0.18<0.75) |
| 52641540 | cbBTC→[uniswap_v3]→tBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.005161 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1180 €) | — | 3.10 | 0.182 (n=38) | REJECTED | p_lower_below_threshold(0.18<0.75) |
| 52641540 | USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→tBTC→[aerodrome_slipstream]→USDC | 421.139371 USDC | 0.135164 USDC | 0.000000 USDC | 0.007578 USDC | 0.127586 USDC (0.1174 €) | 0.127586 USDC | 3.03 | 0.182 (n=38) | REJECTED | p_lower_below_threshold(0.18<0.75) |
| 52641540 | cbBTC→[pancakeswap_v3]→tBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.005049 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1173 €) | — | 3.15 | 0.182 (n=38) | REJECTED | p_lower_below_threshold(0.18<0.75) |
| 52641540 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→tBTC→[aerodrome_slipstream]→USDC | 416.610436 USDC | 0.134859 USDC | 0.000000 USDC | 0.007938 USDC | 0.126921 USDC (0.1168 €) | 0.126921 USDC | 3.05 | 0.182 (n=38) | REJECTED | p_lower_below_threshold(0.18<0.75) |
| 52642035 | USDC→[uniswap_v3]→WBTC→[uniswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 144.097131 USDC | 0.131193 USDC | 0.000000 USDC | 0.007844 USDC | 0.123349 USDC (0.1135 €) | — | 8.56 | 0.001 (n=7) | REJECTED | reliability_not_demonstrated |
| 52642035 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WBTC→[uniswap_v3]→cbBTC | 0.001668 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1134 €) | — | 9.11 | 0.001 (n=7) | REJECTED | reliability_not_demonstrated |
| 52641554 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.305120 WETH | 0.000056 WETH | 0.000000 WETH | 0.000003 WETH | 0.000053 WETH (0.1134 €) | — | 1.73 | 0.104 (n=35) | REJECTED | below_safety_margin(52823489579169<61024098255965), p_lower_below_threshold(0.10<0.75) |
| 52641554 | USDC→[uniswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 710.150344 USDC | 0.131013 USDC | 0.000000 USDC | 0.008097 USDC | 0.122916 USDC (0.1131 €) | — | 1.73 | 0.104 (n=35) | REJECTED | below_safety_margin(122916<142030), p_lower_below_threshold(0.10<0.75) |
| 52641554 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→cbBTC | 0.008247 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1127 €) | — | 1.86 | 0.104 (n=35) | REJECTED | below_safety_margin(153<164), p_lower_below_threshold(0.10<0.75) |
| 52641328 | WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.434863 WETH | 0.000053 WETH | 0.000000 WETH | 0.000003 WETH | 0.000049 WETH (0.1066 €) | — | 1.14 | 0.104 (n=35) | REJECTED | below_safety_margin(49359140518453<86972633703641), p_lower_below_threshold(0.10<0.75) |
| 52641328 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC | 1,017.802287 USDC | 0.123214 USDC | 0.000000 USDC | 0.007491 USDC | 0.115723 USDC (0.1065 €) | — | 1.14 | 0.104 (n=35) | REJECTED | below_safety_margin(115723<203560), p_lower_below_threshold(0.10<0.75) |
| 52641554 | cbBTC→[aerodrome_slipstream]→tBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→cbBTC | 0.004337 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0810 €) | — | 2.54 | 0.310 (n=23) | REJECTED | reliability_not_demonstrated |

## Fiabilité et décision
- Observations ghost : 312 ; taux observé 0.176 ; borne inférieure crédible (0.9) 0.150 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 15.0% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ✅ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
