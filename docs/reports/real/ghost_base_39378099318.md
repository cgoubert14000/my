# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-20T08:34:53+00:00 ; durée 148.39 min ; blocs 52843518 → 52847968 (4427 vus)

## Connexion
- Requêtes RPC : 56907 ; erreurs : 40 ; latence p50/p95 : 78.9/968.5 ms
- Rafraîchissements d'état : 4427 ; âge des données au dernier bloc : 3.87 s ; changements de frais LP observés (pools à frais dynamiques) : 7949
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 25818 ; cycles déclenchés par événement : 1496 ; avance médiane sur le rafraîchissement multicall : 921 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,387.32 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 572 pools, 327 jetons, 21244 routes
- Par DEX : uniswap_v3 136, aerodrome 235, aerodrome_slipstream 154, pancakeswap_v3 30, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 207 (rejetés 2) → 612 jetons ; pools candidats 3877 (énumérés 392, par paires 0), mesurés 574, sous le plancher de 10000.0 $ : 2 → gardés 572 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDC': 1.0, 'USDbC': 1.0, 'WETH': 2396.704066, 'AERO': 0.805188, 'cbBTC': 81576.404653}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 145,885,470 | 2,387.319985 | 52847969 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 34,473,492 | 1.238140 | 52847969 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 500 | 18,101,652 | 0.029290 | 52847969 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 17,669,320 | 0.029339 | 52847969 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/VVV | 3000 | 17,351,361 | 97.840269 | 52847969 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,316,158 | 0.029323 | 52847969 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,867,230 | 0.000012 | 52847969 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome_slipstream | USDC/cbBTC | 424 | 9,579,723 | 0.000012 | 52847969 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | WETH/USDC | 500 | 8,325,335 | 2,385.621843 | 52847969 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/USDC | 3000 | 8,282,722 | 2,387.730658 | 52847969 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | USDC/cbBTC | 334 | 7,837,881 | 0.000012 | 52847969 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 150 | 7,425,008 | 2,386.291964 | 52847969 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,156,098 | 0.001669 | 52847969 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,314,831 | 0.029302 | 52847969 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/USDT | 403 | 5,069,501 | 2,389.160397 | 52847969 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome | fBOMB/AERO | 10000 | 4,979,423 | 0.025567 | 52847969 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,756,247 | 0.802395 | 52847969 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,604,925 | 0.000275 | 52847969 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | USDC/AERO | 10000 | 4,517,586 | 1.236545 | 52847969 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,484,337 | 2,386.584747 | 52847969 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,319,477 | 0.998767 | 52847969 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,961,718 | 34,441.160281 | 52847969 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/AERO | 10000 | 3,245,773 | 2,962.631468 | 52847969 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 3,053,015 | 979.286674 | 52847969 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,869,345 | 0.000012 | 52847969 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,731,378 | 1.142106 | 52847969 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| aerodrome_slipstream | WETH/VVV | 2700 | 2,649,843 | 97.818421 | 52847969 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 2,497,457 | 0.000010 | 52847969 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,280,009 | 400.639182 | 52847969 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | WETH/FAI | 10000 | 2,177,669 | 1,220,013.668431 | 52847969 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,059,504 | 1.238011 | 52847969 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,036,015 | 1.373598 | 52847969 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,929,064 | 0.000000 | 52847969 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,800,898 | 0.019113 | 52847969 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,771,805 | 16.027064 | 52847969 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,765,888 | 0.000012 | 52847969 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | weETH_04c0/WETH | 500 | 1,727,302 | 1.105525 | 52847969 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,720,228 | 13,663.011707 | 52847969 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | fBOMB/USDC | 10000 | 1,678,450 | 0.020334 | 52847969 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| aerodrome_slipstream | EURC/USDC | 70 | 1,652,898 | 1.123258 | 52847969 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| aerodrome | WETH/msETH (stable) | 500 | 1,645,341 | 2.306593 | 52847969 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | WETH/AERO | 3000 | 1,611,913 | 2,956.423450 | 52847969 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,546,305 | 0.916343 | 52847969 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,458,585 | 0.826360 | 52847969 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,301,511 | 0.004730 | 52847969 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v3 | DRB/WETH | 10000 | 1,301,428 | 0.000000 | 52847969 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,291,062 | 0.000276 | 52847969 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | WETH/cbBTC | 3000 | 1,277,958 | 0.029321 | 52847969 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,246,796 | 2,385.526466 | 52847969 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,228,846 | 64.349930 | 52847969 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,208,593 | 23.000839 | 52847969 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| uniswap_v3 | WETH/doginme | 10000 | 1,187,466 | 35,471,092.216662 | 52847969 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,178,307 | 0.435582 | 52847969 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| aerodrome | WETH/WELL | 10000 | 1,177,771 | 1,113,999.945174 | 52847969 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome_slipstream | WETH/msETH | 500 | 1,146,858 | 1.131457 | 52847969 | `0x74F72788F4814D7fF3C49B44684aa98Eee140C0E` |
| aerodrome | WETH/EDEL | 7000 | 1,142,528 | 75,333.085810 | 52847969 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,136,390 | 510,083.108596 | 52847969 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | USDC/NOCK | 3000 | 1,118,725 | 50.344845 | 52847969 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | msUSD/USDC | 500 | 1,091,718 | 0.885385 | 52847969 | `0x7501bc8Bb51616F79bfA524E464fb7B41f0B10fB` |
| aerodrome_slipstream | USDC/USDT | 8 | 1,074,254 | 1.001456 | 52847969 | `0xa41Bc0AFfbA7Fd420d186b84899d7ab2aC57fcD1` |

## Recherche d'opportunités
- Cycles : 5922 ; routes examinées : 125806968 ; candidats optimisés : 740312 ; net attendu > 0 : 44 ; dernier cycle 518.5 ms
- Rejets (moteur) : {'spread_below_threshold': 123896818, 'liquidity_below_min': 962670, 'negative_expected_net': 740268, 'borrow_bound_too_small': 148025, 'pool_quarantined': 58800, 'cycle_budget_exhausted': 343}
- Enregistrements de la session : 740312 ; net attendu > 0 : 44 ; simulés (eth_call de la vraie tx) : 14 (ok 4, échec 10) ; étiquettes ghost N+1 : 0/6 positives
- Décisions : {'REJECTED': 740312} ; motifs de rejet : {'below_safety_margin': 29, 'negative_expected_net': 740268, 'p_lower_below_threshold': 43, 'price_impact': 10, 'reliability_not_demonstrated': 1, 'simulation_failed': 10, 'stale_data': 2}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52845425 | WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.079741 WETH | 0.000023 WETH | 0.000000 WETH | 0.000003 WETH | 0.000020 WETH (0.0438 €) | 0.000020 WETH | 2.49 | 0.107 (n=167) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 52845425 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→USDC | 190.732769 USDC | 0.055145 USDC | 0.000000 USDC | 0.007563 USDC | 0.047582 USDC (0.0438 €) | 0.047582 USDC | 2.49 | 0.107 (n=167) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 52845425 | WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.071741 WETH | 0.000021 WETH | 0.000000 WETH | 0.000003 WETH | 0.000018 WETH (0.0396 €) | 0.000018 WETH | 2.50 | 0.107 (n=167) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 52845425 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→USDC | 171.469156 USDC | 0.050222 USDC | 0.000000 USDC | 0.007199 USDC | 0.043023 USDC (0.0396 €) | — | 2.51 | 0.107 (n=167) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 52846999 | WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.304604 WETH | 0.000017 WETH | 0.000000 WETH | 0.000003 WETH | 0.000014 WETH (0.0317 €) | — | 0.47 | 0.105 (n=170) | REJECTED | below_safety_margin(14399719220522<60920760948827), p_lower_below_threshold(0.10<0.75) |
| 52846999 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC | 726.607903 USDC | 0.041488 USDC | 0.000000 USDC | 0.007189 USDC | 0.034299 USDC (0.0316 €) | — | 0.47 | 0.105 (n=170) | REJECTED | below_safety_margin(34299<145321), p_lower_below_threshold(0.10<0.75) |
| 52846999 | WETH→[aerodrome_slipstream]→USDT→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.229182 WETH | 0.000011 WETH | 0.000000 WETH | 0.000003 WETH | 0.000008 WETH (0.0166 €) | — | 0.33 | 0.105 (n=170) | REJECTED | below_safety_margin(7538924608868<45836485509461), stale_data(4053ms>4000.0), p_lower_below_threshold(0.10<0.75) |
| 52846999 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDT→[uniswap_v3]→USDC | 546.024961 USDC | 0.025135 USDC | 0.000000 USDC | 0.007189 USDC | 0.017946 USDC (0.0165 €) | — | 0.33 | 0.105 (n=170) | REJECTED | below_safety_margin(17946<109204), stale_data(4060ms>4000.0), p_lower_below_threshold(0.10<0.75) |
| 52845425 | WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.033807 WETH | 0.000009 WETH | 0.000000 WETH | 0.000003 WETH | 0.000006 WETH (0.0137 €) | — | 1.83 | 0.107 (n=167) | REJECTED | below_safety_margin(6197568207277<6761494604185), p_lower_below_threshold(0.11<0.75) |
| 52845425 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC | 80.584874 USDC | 0.022399 USDC | 0.000000 USDC | 0.007563 USDC | 0.014836 USDC (0.0136 €) | — | 1.84 | 0.107 (n=167) | REJECTED | below_safety_margin(14836<16116), p_lower_below_threshold(0.11<0.75) |
| 52845425 | WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.032600 WETH | 0.000009 WETH | 0.000000 WETH | 0.000003 WETH | 0.000006 WETH (0.0131 €) | — | 1.82 | 0.107 (n=167) | REJECTED | below_safety_margin(5930589844909<6520068500255), p_lower_below_threshold(0.11<0.75) |
| 52845425 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC | 77.259731 USDC | 0.021761 USDC | 0.000000 USDC | 0.007563 USDC | 0.014198 USDC (0.0131 €) | — | 1.84 | 0.107 (n=167) | REJECTED | below_safety_margin(14198<15451), p_lower_below_threshold(0.11<0.75) |
| 52845136 | WETH→[aerodrome]→MEY→[uniswap_v3]→WETH | 0.007838 WETH | 0.000005 WETH | 0.000000 WETH | 0.000002 WETH | 0.000003 WETH (0.0061 €) | 0.000003 WETH | 3.51 | 0.051 (n=16) | REJECTED | reliability_not_demonstrated |
| 52846999 | WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.044801 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0040 €) | — | 0.40 | 0.105 (n=170) | REJECTED | below_safety_margin(1797957907295<8960248774532), p_lower_below_threshold(0.10<0.75) |
| 52846999 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC | 106.739443 USDC | 0.011451 USDC | 0.000000 USDC | 0.007189 USDC | 0.004262 USDC (0.0039 €) | — | 0.40 | 0.105 (n=170) | REJECTED | below_safety_margin(4262<21347), p_lower_below_threshold(0.10<0.75) |
| 52844622 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 20.372606 USDC | 0.009322 USDC | 0.000000 USDC | 0.005380 USDC | 0.003942 USDC (0.0036 €) | — | 1.93 | 0.016 (n=52) | REJECTED | below_safety_margin(3942<4074), p_lower_below_threshold(0.02<0.75) |
| 52846999 | WETH→[uniswap_v3]→USDT→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.040455 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0018 €) | — | 0.21 | 0.105 (n=170) | REJECTED | below_safety_margin(830821009921<8090930856318), p_lower_below_threshold(0.10<0.75) |
| 52846999 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDT→[uniswap_v3]→USDC | 96.625550 USDC | 0.009146 USDC | 0.000000 USDC | 0.007189 USDC | 0.001957 USDC (0.0018 €) | — | 0.20 | 0.105 (n=170) | REJECTED | below_safety_margin(1957<19325), p_lower_below_threshold(0.10<0.75) |
| 52845687 | cbBTC→[aerodrome]→fBOMB→[aerodrome]→AERO→[aerodrome_slipstream]→cbBTC | 0.000012 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0015 €) | — | 16.35 | 0.014 (n=102) | REJECTED | price_impact(213bps>150.0), simulation_failed:revert 0xa932492f, p_lower_below_threshold(0.01<0.75) |
| 52846999 | WETH→[aerodrome]→OVER→[aerodrome]→USDC→[uniswap_v3]→WETH | 0.005858 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0011 €) | — | 0.85 | 0.119 (n=64) | REJECTED | below_safety_margin(495284044593<1171627208646), p_lower_below_threshold(0.12<0.75) |
| 52846999 | WETH→[aerodrome]→OVER→[aerodrome]→USDC→[uniswap_v3]→WETH | 0.005863 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0011 €) | — | 0.84 | 0.119 (n=64) | REJECTED | below_safety_margin(493763744569<1172521797829), p_lower_below_threshold(0.12<0.75) |
| 52846999 | USDC→[uniswap_v3]→WETH→[aerodrome]→OVER→[aerodrome]→USDC | 13.987872 USDC | 0.007684 USDC | 0.000000 USDC | 0.006521 USDC | 0.001163 USDC (0.0011 €) | — | 0.83 | 0.119 (n=64) | REJECTED | below_safety_margin(1163<2797), p_lower_below_threshold(0.12<0.75) |
| 52846999 | USDC→[uniswap_v3]→WETH→[aerodrome]→OVER→[aerodrome]→USDC | 13.987872 USDC | 0.007684 USDC | 0.000000 USDC | 0.006529 USDC | 0.001155 USDC (0.0011 €) | — | 0.83 | 0.119 (n=64) | REJECTED | below_safety_margin(1155<2797), p_lower_below_threshold(0.12<0.75) |
| 52846999 | WETH→[aerodrome]→OVER→[aerodrome]→USDC→[pancakeswap_v3]→WETH | 0.005858 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0010 €) | — | 0.77 | 0.052 (n=41) | REJECTED | below_safety_margin(449706959257<1171627208646), p_lower_below_threshold(0.05<0.75) |
| 52846999 | WETH→[aerodrome]→OVER→[aerodrome]→USDC→[pancakeswap_v3]→WETH | 0.005863 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0010 €) | — | 0.76 | 0.052 (n=41) | REJECTED | below_safety_margin(448167515924<1172521797829), p_lower_below_threshold(0.05<0.75) |

## Fiabilité et décision
- Observations ghost : 1394 ; taux observé 0.101 ; borne inférieure crédible (0.9) 0.091 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 9.1% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
