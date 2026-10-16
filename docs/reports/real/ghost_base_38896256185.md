# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-16T11:56:17+00:00 ; durée 3.06 min ; blocs 52681120 → 52681214 (93 vus)

## Connexion
- Requêtes RPC : 1314 ; erreurs : 0 ; latence p50/p95 : 83.3/1,556.3 ms
- Rafraîchissements d'état : 93 ; âge des données au dernier bloc : 2.28 s ; changements de frais LP observés (pools à frais dynamiques) : 166
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 1024 ; cycles déclenchés par événement : 87 ; avance médiane sur le rafraîchissement multicall : 829 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,482.31 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 575 pools, 328 jetons, 21482 routes
- Par DEX : uniswap_v3 136, aerodrome 236 (quarantaine 1), aerodrome_slipstream 153, pancakeswap_v3 32, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 209 (rejetés 2) → 614 jetons ; pools candidats 3925 (énumérés 391, par paires 0), mesurés 577, sous le plancher de 10000.0 $ : 2 → gardés 575 (max 1500) ; prix des hubs : {'USDC': 1.0, 'DAI': 1.0, 'USDbC': 1.0, 'WETH': 2482.328501, 'AERO': 0.918334, 'cbBTC': 82582.444221}
- Pools en quarantaine : 1 — aerodrome:fBOMB/AERO@0xbBf71A: simulation failed ×5 (model/chain mismatch) — until block 52681424

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 148,332,737 | 2,482.309234 | 52681215 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 47,033,889 | 1.088932 | 52681215 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 500 | 18,759,124 | 0.029983 | 52681215 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 16,803,476 | 100.031649 | 52681215 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 13,979,160 | 0.030036 | 52681215 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,650,044 | 0.030047 | 52681215 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,781,933 | 0.000012 | 52681215 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 9,224,520 | 2,476.070632 | 52681215 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome_slipstream | WETH/USDC | 549 | 8,488,904 | 2,475.668519 | 52681215 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | USDC/cbBTC | 336 | 8,123,960 | 0.000012 | 52681215 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | USDC/AERO | 10000 | 7,510,716 | 1.084050 | 52681215 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,301,975 | 0.001684 | 52681215 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 424 | 6,998,618 | 0.000012 | 52681215 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome | fBOMB/AERO | 10000 | 5,504,110 | 0.024788 | 52681215 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome | WETH/USDC | 3000 | 5,485,023 | 2,482.475310 | 52681215 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,479,370 | 0.029993 | 52681215 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/superOETHb | 400 | 5,304,265 | 1.000855 | 52681215 | `0x6446021F4E396dA3df4235C62537431372195D38` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,961,630 | 0.802398 | 52681215 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,829,602 | 0.000281 | 52681215 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,397,937 | 0.998889 | 52681215 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,369,543 | 2,475.595150 | 52681215 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | WETH/KTA | 3000 | 4,112,334 | 34,558.788851 | 52681215 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDT | 406 | 4,047,138 | 2,478.632671 | 52681215 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome | WETH/AERO | 10000 | 3,586,926 | 2,678.179041 | 52681215 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | cbETH/WETH | 60 | 3,081,461 | 1.141840 | 52681215 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,860,066 | 0.000012 | 52681215 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/VVV | 2724 | 2,713,995 | 100.007775 | 52681215 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 2,601,406 | 0.000011 | 52681215 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,469,157 | 400.196099 | 52681215 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | WETH/FAI | 10000 | 2,328,599 | 1,153,583.350645 | 52681215 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | BNKR/WETH | 10000 | 2,138,476 | 0.000000 | 52681215 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,111,736 | 1.195936 | 52681215 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | WETH/MORPHO | 2709 | 2,084,937 | 999.153962 | 52681215 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,008,461 | 1.403757 | 52681215 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,939,712 | 15.121516 | 52681215 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | fBOMB/USDC | 10000 | 1,867,337 | 0.023300 | 52681215 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,786,820 | 0.000012 | 52681215 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | XDP/USDC | 100 | 1,782,904 | 0.018910 | 52681215 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome | WETH/msETH (stable) | 500 | 1,713,833 | 2.312441 | 52681215 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | WETH/AERO | 3000 | 1,589,836 | 2,697.087323 | 52681215 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,542,972 | 0.916551 | 52681215 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| aerodrome | weETH_04c0/WETH | 500 | 1,534,828 | 1.105492 | 52681215 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome_slipstream | WETH/AERO | 3000 | 1,507,059 | 2,696.834314 | 52681215 | `0x82321f3BEB69f503380D6B233857d5C43562e2D0` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,456,120 | 0.825820 | 52681215 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,435,257 | 13,329.103532 | 52681215 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | DRB/WETH | 10000 | 1,392,976 | 0.000000 | 52681215 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome_slipstream | EURC/USDC | 70 | 1,391,434 | 1.125539 | 52681215 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,384,009 | 0.004814 | 52681215 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,355,798 | 0.000281 | 52681215 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,353,216 | 23.275357 | 52681215 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,310,034 | 0.437134 | 52681215 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| aerodrome | USDC/SEND | 3000 | 1,250,232 | 62.167285 | 52681215 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,231,805 | 1.105591 | 52681215 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |
| aerodrome | WETH/cbBTC | 3000 | 1,230,604 | 0.030036 | 52681215 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| uniswap_v3 | WETH/doginme | 10000 | 1,227,468 | 35,719,238.802015 | 52681215 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome_slipstream | msUSD/USDC | 500 | 1,223,932 | 0.886678 | 52681215 | `0x7501bc8Bb51616F79bfA524E464fb7B41f0B10fB` |
| aerodrome | WETH/WELL | 10000 | 1,223,878 | 1,115,541.578627 | 52681215 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,221,948 | 2,475.995254 | 52681215 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,184,832 | 496,085.125904 | 52681215 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | WETH/EDEL | 7000 | 1,150,031 | 81,119.922572 | 52681215 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |

## Recherche d'opportunités
- Cycles : 179 ; routes examinées : 3845278 ; candidats optimisés : 26039 ; net attendu > 0 : 22 ; dernier cycle 333.3 ms
- Rejets (moteur) : {'spread_below_threshold': 3767403, 'liquidity_below_min': 46729, 'negative_expected_net': 26017, 'pool_quarantined': 4928, 'borrow_bound_too_small': 179}
- Enregistrements de la session : 26039 ; net attendu > 0 : 22 ; simulés (eth_call de la vraie tx) : 12 (ok 6, échec 6) ; étiquettes ghost N+1 : 0/5 positives
- Décisions : {'REJECTED': 26039} ; motifs de rejet : {'negative_expected_net': 26017, 'p_lower_below_threshold': 15, 'price_impact': 6, 'reliability_not_demonstrated': 7, 'simulation_failed': 6}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52681126 | WETH→[aerodrome_slipstream]→CBDOGE→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→WETH | 0.020928 WETH | 0.000012 WETH | 0.000000 WETH | 0.000003 WETH | 0.000009 WETH (0.0215 €) | 0.000009 WETH | 4.51 | 0.213 (n=25) | REJECTED | reliability_not_demonstrated |
| 52681126 | WETH→[aerodrome_slipstream]→CBDOGE→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→WETH | 0.020928 WETH | 0.000012 WETH | 0.000000 WETH | 0.000003 WETH | 0.000009 WETH (0.0215 €) | 0.000009 WETH | 4.51 | 0.213 (n=25) | REJECTED | reliability_not_demonstrated |
| 52681126 | cbBTC→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→CBDOGE→[aerodrome_slipstream]→cbBTC | 0.000633 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0213 €) | — | 4.42 | 0.213 (n=25) | REJECTED | reliability_not_demonstrated |
| 52681126 | cbBTC→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→CBDOGE→[aerodrome_slipstream]→cbBTC | 0.000633 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0213 €) | — | 4.42 | 0.213 (n=25) | REJECTED | reliability_not_demonstrated |
| 52681126 | WETH→[aerodrome_slipstream]→CBDOGE→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.021966 WETH | 0.000011 WETH | 0.000000 WETH | 0.000003 WETH | 0.000008 WETH (0.0186 €) | 0.000008 WETH | 3.70 | 0.115 (n=59) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52681126 | WETH→[aerodrome_slipstream]→CBDOGE→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.021966 WETH | 0.000011 WETH | 0.000000 WETH | 0.000003 WETH | 0.000008 WETH (0.0186 €) | 0.000008 WETH | 3.70 | 0.115 (n=59) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52681126 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→CBDOGE→[aerodrome_slipstream]→cbBTC | 0.000633 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0183 €) | — | 3.79 | 0.115 (n=59) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52681126 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→CBDOGE→[aerodrome_slipstream]→cbBTC | 0.000633 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0183 €) | — | 3.79 | 0.115 (n=59) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52681126 | WETH→[aerodrome_slipstream]→CBDOGE→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.015264 WETH | 0.000007 WETH | 0.000000 WETH | 0.000003 WETH | 0.000004 WETH (0.0089 €) | 0.000004 WETH | 2.54 | 0.081 (n=54) | REJECTED | p_lower_below_threshold(0.08<0.75) |
| 52681126 | WETH→[aerodrome_slipstream]→CBDOGE→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.015264 WETH | 0.000007 WETH | 0.000000 WETH | 0.000003 WETH | 0.000004 WETH (0.0089 €) | 0.000004 WETH | 2.54 | 0.081 (n=54) | REJECTED | p_lower_below_threshold(0.08<0.75) |
| 52681126 | WETH→[aerodrome_slipstream]→CBDOGE→[aerodrome_slipstream]→cbBTC→[uniswap_v3]→WETH | 0.015264 WETH | 0.000007 WETH | 0.000000 WETH | 0.000003 WETH | 0.000004 WETH (0.0087 €) | — | 2.49 | 0.238 (n=40) | REJECTED | p_lower_below_threshold(0.24<0.75) |
| 52681126 | WETH→[aerodrome_slipstream]→CBDOGE→[aerodrome_slipstream]→cbBTC→[uniswap_v3]→WETH | 0.015264 WETH | 0.000007 WETH | 0.000000 WETH | 0.000003 WETH | 0.000004 WETH (0.0087 €) | — | 2.49 | 0.238 (n=40) | REJECTED | p_lower_below_threshold(0.24<0.75) |
| 52681126 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→CBDOGE→[aerodrome_slipstream]→cbBTC | 0.000431 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0084 €) | — | 2.55 | 0.081 (n=54) | REJECTED | p_lower_below_threshold(0.08<0.75) |
| 52681126 | cbBTC→[uniswap_v3]→WETH→[aerodrome_slipstream]→CBDOGE→[aerodrome_slipstream]→cbBTC | 0.000434 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0084 €) | — | 2.53 | 0.238 (n=40) | REJECTED | p_lower_below_threshold(0.24<0.75) |
| 52681126 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→CBDOGE→[aerodrome_slipstream]→cbBTC | 0.000431 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0084 €) | — | 2.55 | 0.081 (n=54) | REJECTED | p_lower_below_threshold(0.08<0.75) |
| 52681126 | cbBTC→[uniswap_v3]→WETH→[aerodrome_slipstream]→CBDOGE→[aerodrome_slipstream]→cbBTC | 0.000434 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0084 €) | — | 2.53 | 0.238 (n=40) | REJECTED | p_lower_below_threshold(0.24<0.75) |
| 52681123 | WETH→[pancakeswap_v3]→AERO→[aerodrome]→fBOMB→[aerodrome]→WETH | 0.000403 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0013 €) | — | 14.01 | 0.001 (n=9) | REJECTED | price_impact(205bps>150.0), simulation_failed:revert 0xa932492f, reliability_not_demonstrated |
| 52681124 | WETH→[pancakeswap_v3]→AERO→[aerodrome]→fBOMB→[aerodrome]→WETH | 0.000403 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0013 €) | — | 14.01 | 0.001 (n=10) | REJECTED | price_impact(205bps>150.0), simulation_failed:revert 0xa932492f, reliability_not_demonstrated |
| 52681124 | WETH→[pancakeswap_v3]→AERO→[aerodrome]→fBOMB→[aerodrome]→WETH | 0.000403 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0013 €) | — | 14.01 | 0.001 (n=10) | REJECTED | price_impact(205bps>150.0), simulation_failed:revert 0xa932492f, reliability_not_demonstrated |
| 52681123 | cbBTC→[aerodrome_slipstream]→AERO→[aerodrome]→fBOMB→[aerodrome]→cbBTC | 0.000012 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0008 €) | — | 8.29 | 0.009 (n=31) | REJECTED | price_impact(214bps>150.0), simulation_failed:revert 0xa932492f, p_lower_below_threshold(0.01<0.75) |
| 52681124 | cbBTC→[aerodrome_slipstream]→AERO→[aerodrome]→fBOMB→[aerodrome]→cbBTC | 0.000012 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0008 €) | — | 8.29 | 0.009 (n=32) | REJECTED | price_impact(214bps>150.0), simulation_failed:revert 0xa932492f, p_lower_below_threshold(0.01<0.75) |
| 52681124 | cbBTC→[aerodrome_slipstream]→AERO→[aerodrome]→fBOMB→[aerodrome]→cbBTC | 0.000012 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0008 €) | — | 8.29 | 0.009 (n=32) | REJECTED | price_impact(214bps>150.0), simulation_failed:revert 0xa932492f, p_lower_below_threshold(0.01<0.75) |

## Fiabilité et décision
- Observations ghost : 518 ; taux observé 0.118 ; borne inférieure crédible (0.9) 0.101 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 10.1% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
