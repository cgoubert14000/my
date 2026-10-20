# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-20T09:09:43+00:00 ; durée 183.22 min ; blocs 52843518 → 52849013 (5444 vus)

## Connexion
- Requêtes RPC : 70858 ; erreurs : 40 ; latence p50/p95 : 82.8/966.9 ms
- Rafraîchissements d'état : 5444 ; âge des données au dernier bloc : 3.26 s ; changements de frais LP observés (pools à frais dynamiques) : 9915
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 44004 ; cycles déclenchés par événement : 2564 ; avance médiane sur le rafraîchissement multicall : 801 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,384.01 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 572 pools, 327 jetons, 21244 routes
- Par DEX : uniswap_v3 136, aerodrome 235, aerodrome_slipstream 154, pancakeswap_v3 30, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 207 (rejetés 2) → 612 jetons ; pools candidats 3877 (énumérés 392, par paires 0), mesurés 574, sous le plancher de 10000.0 $ : 2 → gardés 572 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDC': 1.0, 'USDbC': 1.0, 'WETH': 2396.704066, 'AERO': 0.805188, 'cbBTC': 81576.404653}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 145,704,954 | 2,384.013158 | 52849012 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 34,470,047 | 1.238389 | 52849012 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 500 | 18,086,149 | 0.029246 | 52849012 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 17,346,953 | 97.618995 | 52849012 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 17,156,631 | 0.029304 | 52849012 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,307,423 | 0.029318 | 52849012 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,870,725 | 0.000012 | 52849012 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome_slipstream | USDC/cbBTC | 448 | 8,729,860 | 0.000012 | 52849012 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | WETH/USDC | 500 | 8,301,960 | 2,379.584109 | 52849012 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/USDC | 3000 | 8,276,994 | 2,383.940699 | 52849012 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | USDC/cbBTC | 340 | 7,813,296 | 0.000012 | 52849012 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 549 | 7,626,713 | 2,380.402435 | 52849012 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,154,161 | 0.001668 | 52849012 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,314,572 | 0.029255 | 52849012 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/USDT | 415 | 5,046,501 | 2,383.446782 | 52849012 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome | fBOMB/AERO | 10000 | 4,978,992 | 0.025548 | 52849012 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,749,659 | 0.802395 | 52849012 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,598,546 | 0.000275 | 52849012 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,448,521 | 2,380.439279 | 52849012 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,319,960 | 0.998767 | 52849012 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome_slipstream | USDC/AERO | 10000 | 4,159,402 | 1.236545 | 52849012 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome | WETH/KTA | 3000 | 3,959,163 | 34,390.157650 | 52849012 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/AERO | 10000 | 3,243,200 | 2,962.643261 | 52849012 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,869,541 | 0.000012 | 52849012 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,727,597 | 1.142107 | 52849012 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,707,487 | 400.633663 | 52849012 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | WETH/VVV | 2706 | 2,648,707 | 97.614372 | 52849012 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | AERO/cbBTC | 2700 | 2,295,884 | 0.000010 | 52849012 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/MORPHO | 2721 | 2,242,290 | 983.298109 | 52849012 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome | WETH/FAI | 10000 | 2,175,002 | 1,219,622.054171 | 52849012 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,059,504 | 1.238011 | 52849012 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,036,015 | 1.373598 | 52849012 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,926,379 | 0.000000 | 52849012 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,789,337 | 0.018892 | 52849013 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,769,916 | 16.049278 | 52849012 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,766,032 | 0.000012 | 52849012 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,759,182 | 13,688.841294 | 52849012 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | weETH_04c0/WETH | 500 | 1,724,922 | 1.105525 | 52849012 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome | fBOMB/USDC | 10000 | 1,678,595 | 0.020335 | 52849012 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| aerodrome_slipstream | EURC/USDC | 79 | 1,650,984 | 1.121410 | 52849012 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| aerodrome | WETH/msETH (stable) | 500 | 1,643,383 | 2.305920 | 52849012 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | WETH/AERO | 3000 | 1,615,506 | 2,947.836422 | 52849012 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,544,165 | 0.916342 | 52849012 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,457,927 | 0.826341 | 52849012 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | DRB/WETH | 10000 | 1,299,626 | 0.000000 | 52849012 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,297,576 | 0.004721 | 52849012 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,289,280 | 0.000276 | 52849012 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | WETH/cbBTC | 3000 | 1,277,146 | 0.029321 | 52849012 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,247,453 | 2,379.559495 | 52849012 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,236,681 | 63.537119 | 52849012 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,206,932 | 23.000398 | 52849012 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| uniswap_v3 | WETH/doginme | 10000 | 1,185,627 | 35,488,398.342383 | 52849012 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | WETH/WELL | 10000 | 1,178,811 | 1,108,955.297280 | 52849012 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,178,288 | 0.435505 | 52849012 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| aerodrome_slipstream | WETH/msETH | 500 | 1,151,245 | 1.131410 | 52849012 | `0x74F72788F4814D7fF3C49B44684aa98Eee140C0E` |
| aerodrome | WETH/EDEL | 7000 | 1,142,168 | 75,171.926684 | 52849012 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,134,814 | 510,085.635711 | 52849012 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | USDC/NOCK | 3000 | 1,118,450 | 50.369615 | 52849012 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | msUSD/USDC | 500 | 1,085,742 | 0.885339 | 52849012 | `0x7501bc8Bb51616F79bfA524E464fb7B41f0B10fB` |
| aerodrome_slipstream | USDC/USDT | 8 | 1,075,225 | 1.001466 | 52849012 | `0xa41Bc0AFfbA7Fd420d186b84899d7ab2aC57fcD1` |

## Recherche d'opportunités
- Cycles : 8007 ; routes examinées : 170100708 ; candidats optimisés : 993342 ; net attendu > 0 : 75 ; dernier cycle 297.2 ms
- Rejets (moteur) : {'spread_below_threshold': 167529708, 'liquidity_below_min': 1318311, 'negative_expected_net': 993267, 'borrow_bound_too_small': 200150, 'pool_quarantined': 58800, 'cycle_budget_exhausted': 397}
- Enregistrements de la session : 993342 ; net attendu > 0 : 75 ; simulés (eth_call de la vraie tx) : 15 (ok 4, échec 11) ; étiquettes ghost N+1 : 0/7 positives
- Décisions : {'REJECTED': 993342} ; motifs de rejet : {'below_safety_margin': 59, 'negative_expected_net': 993267, 'p_lower_below_threshold': 68, 'price_impact': 10, 'reliability_not_demonstrated': 7, 'simulation_failed': 11, 'stale_data': 2}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52848456 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.590707 WETH | 0.000027 WETH | 0.000000 WETH | 0.000002 WETH | 0.000024 WETH (0.0537 €) | — | 0.41 | 0.016 (n=52) | REJECTED | below_safety_margin(24476682940086<118141400154432), p_lower_below_threshold(0.02<0.75) |
| 52848456 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 1,404.469589 USDC | 0.063558 USDC | 0.000000 USDC | 0.005356 USDC | 0.058202 USDC (0.0535 €) | — | 0.41 | 0.016 (n=52) | REJECTED | below_safety_margin(58202<280893), p_lower_below_threshold(0.02<0.75) |
| 52848264 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 62.426826 USDC | 0.062933 USDC | 0.000000 USDC | 0.005360 USDC | 0.057573 USDC (0.0530 €) | — | 9.22 | 0.000 (n=37) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 52845425 | WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.079741 WETH | 0.000023 WETH | 0.000000 WETH | 0.000003 WETH | 0.000020 WETH (0.0438 €) | 0.000020 WETH | 2.49 | 0.107 (n=167) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 52845425 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→USDC | 190.732769 USDC | 0.055145 USDC | 0.000000 USDC | 0.007563 USDC | 0.047582 USDC (0.0438 €) | 0.047582 USDC | 2.49 | 0.107 (n=167) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 52845425 | WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.071741 WETH | 0.000021 WETH | 0.000000 WETH | 0.000003 WETH | 0.000018 WETH (0.0396 €) | 0.000018 WETH | 2.50 | 0.107 (n=167) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 52845425 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→USDC | 171.469156 USDC | 0.050222 USDC | 0.000000 USDC | 0.007199 USDC | 0.043023 USDC (0.0396 €) | — | 2.51 | 0.107 (n=167) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 52848456 | WETH→[aerodrome]→USDC→[pancakeswap_v3]→WETH | 0.159443 WETH | 0.000017 WETH | 0.000000 WETH | 0.000002 WETH | 0.000014 WETH (0.0318 €) | — | 0.91 | 0.001 (n=6) | REJECTED | below_safety_margin(14480463120665<31888530910195), reliability_not_demonstrated |
| 52846999 | WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.304604 WETH | 0.000017 WETH | 0.000000 WETH | 0.000003 WETH | 0.000014 WETH (0.0317 €) | — | 0.47 | 0.105 (n=170) | REJECTED | below_safety_margin(14399719220522<60920760948827), p_lower_below_threshold(0.10<0.75) |
| 52848456 | USDC→[pancakeswap_v3]→WETH→[aerodrome]→USDC | 379.625146 USDC | 0.039451 USDC | 0.000000 USDC | 0.005027 USDC | 0.034424 USDC (0.0317 €) | — | 0.91 | 0.001 (n=6) | REJECTED | below_safety_margin(34424<75925), reliability_not_demonstrated |
| 52846999 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC | 726.607903 USDC | 0.041488 USDC | 0.000000 USDC | 0.007189 USDC | 0.034299 USDC (0.0316 €) | — | 0.47 | 0.105 (n=170) | REJECTED | below_safety_margin(34299<145321), p_lower_below_threshold(0.10<0.75) |
| 52846999 | WETH→[aerodrome_slipstream]→USDT→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.229182 WETH | 0.000011 WETH | 0.000000 WETH | 0.000003 WETH | 0.000008 WETH (0.0166 €) | — | 0.33 | 0.105 (n=170) | REJECTED | below_safety_margin(7538924608868<45836485509461), stale_data(4053ms>4000.0), p_lower_below_threshold(0.10<0.75) |
| 52846999 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDT→[uniswap_v3]→USDC | 546.024961 USDC | 0.025135 USDC | 0.000000 USDC | 0.007189 USDC | 0.017946 USDC (0.0165 €) | — | 0.33 | 0.105 (n=170) | REJECTED | below_safety_margin(17946<109204), stale_data(4060ms>4000.0), p_lower_below_threshold(0.10<0.75) |
| 52845425 | WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.033807 WETH | 0.000009 WETH | 0.000000 WETH | 0.000003 WETH | 0.000006 WETH (0.0137 €) | — | 1.83 | 0.107 (n=167) | REJECTED | below_safety_margin(6197568207277<6761494604185), p_lower_below_threshold(0.11<0.75) |
| 52845425 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC | 80.584874 USDC | 0.022399 USDC | 0.000000 USDC | 0.007563 USDC | 0.014836 USDC (0.0136 €) | — | 1.84 | 0.107 (n=167) | REJECTED | below_safety_margin(14836<16116), p_lower_below_threshold(0.11<0.75) |
| 52845425 | WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.032600 WETH | 0.000009 WETH | 0.000000 WETH | 0.000003 WETH | 0.000006 WETH (0.0131 €) | — | 1.82 | 0.107 (n=167) | REJECTED | below_safety_margin(5930589844909<6520068500255), p_lower_below_threshold(0.11<0.75) |
| 52845425 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC | 77.259731 USDC | 0.021761 USDC | 0.000000 USDC | 0.007563 USDC | 0.014198 USDC (0.0131 €) | — | 1.84 | 0.107 (n=167) | REJECTED | below_safety_margin(14198<15451), p_lower_below_threshold(0.11<0.75) |
| 52845136 | WETH→[aerodrome]→MEY→[uniswap_v3]→WETH | 0.007838 WETH | 0.000005 WETH | 0.000000 WETH | 0.000002 WETH | 0.000003 WETH (0.0061 €) | 0.000003 WETH | 3.51 | 0.051 (n=16) | REJECTED | reliability_not_demonstrated |
| 52848456 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 233.108017 USDC | 0.012075 USDC | 0.000000 USDC | 0.007169 USDC | 0.004906 USDC (0.0045 €) | — | 0.21 | 0.105 (n=170) | REJECTED | below_safety_margin(4906<46621), p_lower_below_threshold(0.10<0.75) |
| 52848456 | cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.002649 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0045 €) | — | 0.23 | 0.105 (n=170) | REJECTED | below_safety_margin(6<52), p_lower_below_threshold(0.10<0.75) |
| 52848456 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.104554 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0043 €) | — | 0.19 | 0.105 (n=170) | REJECTED | below_safety_margin(1963136156430<20910786641229), p_lower_below_threshold(0.10<0.75) |
| 52848340 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 24.738794 USDC | 0.009887 USDC | 0.000000 USDC | 0.005360 USDC | 0.004527 USDC (0.0042 €) | — | 1.83 | 0.016 (n=52) | REJECTED | below_safety_margin(4527<4947), p_lower_below_threshold(0.02<0.75) |
| 52846999 | WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.044801 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0040 €) | — | 0.40 | 0.105 (n=170) | REJECTED | below_safety_margin(1797957907295<8960248774532), p_lower_below_threshold(0.10<0.75) |
| 52846999 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC | 106.739443 USDC | 0.011451 USDC | 0.000000 USDC | 0.007189 USDC | 0.004262 USDC (0.0039 €) | — | 0.40 | 0.105 (n=170) | REJECTED | below_safety_margin(4262<21347), p_lower_below_threshold(0.10<0.75) |
| 52844622 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 20.372606 USDC | 0.009322 USDC | 0.000000 USDC | 0.005380 USDC | 0.003942 USDC (0.0036 €) | — | 1.93 | 0.016 (n=52) | REJECTED | below_safety_margin(3942<4074), p_lower_below_threshold(0.02<0.75) |

## Fiabilité et décision
- Observations ghost : 1395 ; taux observé 0.101 ; borne inférieure crédible (0.9) 0.091 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 9.1% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
