# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-18T20:17:57+00:00 ; durée 6.13 min ; blocs 52782478 → 52782664 (184 vus)

## Connexion
- Requêtes RPC : 2692 ; erreurs : 0 ; latence p50/p95 : 222.8/870.1 ms
- Rafraîchissements d'état : 185 ; âge des données au dernier bloc : 1.79 s ; changements de frais LP observés (pools à frais dynamiques) : 573
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 5633 ; cycles déclenchés par événement : 289 ; avance médiane sur le rafraîchissement multicall : 412 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,336.72 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 569 pools, 326 jetons, 20804 routes
- Par DEX : uniswap_v3 135, aerodrome 232 (quarantaine 1), aerodrome_slipstream 153, pancakeswap_v3 31, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 205 (rejetés 2) → 610 jetons ; pools candidats 3913 (énumérés 387, par paires 0), mesurés 571, sous le plancher de 10000.0 $ : 2 → gardés 569 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'DAI': 1.0, 'USDC': 1.0, 'WETH': 2337.16445, 'AERO': 0.771529, 'cbBTC': 80785.7814}
- Pools en quarantaine : 1 — aerodrome:fBOMB/AERO@0xbBf71A: simulation failed ×5 (model/chain mismatch) — until block 52782782

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 144,008,567 | 2,336.716020 | 52782664 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 40,398,012 | 1.298198 | 52782664 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 500 | 17,687,650 | 0.028958 | 52782664 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 16,025,888 | 109.825747 | 52782664 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,121,887 | 0.028910 | 52782664 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 9,818,063 | 0.028902 | 52782664 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,700,359 | 0.000012 | 52782664 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 8,176,984 | 2,336.951346 | 52782664 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome_slipstream | USDC/cbBTC | 346 | 7,806,386 | 0.000012 | 52782664 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | USDC/cbBTC | 496 | 7,206,540 | 0.000012 | 52782664 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,994,390 | 0.001627 | 52782664 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | WETH/USDC | 594 | 6,817,519 | 2,336.558366 | 52782664 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome | WETH/USDC | 3000 | 5,390,740 | 2,337.538311 | 52782664 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,123,242 | 0.028970 | 52782664 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/superOETHb | 400 | 5,074,344 | 1.000854 | 52782664 | `0x6446021F4E396dA3df4235C62537431372195D38` |
| aerodrome | fBOMB/AERO | 10000 | 4,834,455 | 0.026123 | 52782664 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,670,796 | 0.802398 | 52782664 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,460,564 | 0.000269 | 52782664 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,359,148 | 2,336.903852 | 52782664 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,296,072 | 0.998069 | 52782664 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,944,040 | 33,292.985532 | 52782664 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | USDC/AERO | 10000 | 3,755,518 | 1.288769 | 52782664 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome_slipstream | WETH/USDT | 415 | 3,390,790 | 2,341.596954 | 52782664 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome | WETH/AERO | 10000 | 3,162,949 | 3,009.925443 | 52782664 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,824,233 | 0.000012 | 52782664 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,816,001 | 1.141832 | 52782664 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,748,788 | 415.694123 | 52782664 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | AERO/cbBTC | 2700 | 2,515,540 | 0.000010 | 52782664 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/VVV | 2730 | 2,430,603 | 109.860066 | 52782664 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 2,167,486 | 1,025.854943 | 52782664 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome | WETH/FAI | 10000 | 2,143,432 | 1,206,478.919535 | 52782664 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,065,785 | 1.233147 | 52782664 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,036,703 | 1.372655 | 52782664 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,942,373 | 0.000000 | 52782664 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome_slipstream | EURC/USDC | 70 | 1,932,350 | 1.121737 | 52782664 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,852,644 | 15.946124 | 52782664 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | fBOMB/USDC | 10000 | 1,774,679 | 0.020699 | 52782664 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,758,273 | 0.000012 | 52782664 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | XDP/USDC | 100 | 1,726,372 | 0.017907 | 52782664 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome | weETH_04c0/WETH | 500 | 1,689,700 | 1.105523 | 52782664 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,640,395 | 14,384.267510 | 52782664 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/msETH (stable) | 500 | 1,620,350 | 2.301814 | 52782664 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,455,768 | 0.826942 | 52782664 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,429,952 | 3,032.005321 | 52782664 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,417,711 | 0.916353 | 52782664 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,317,780 | 0.434746 | 52782664 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,285,209 | 0.000000 | 52782664 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,250,253 | 0.000267 | 52782664 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | WETH/cbBTC | 3000 | 1,241,126 | 0.028918 | 52782664 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| aerodrome | USDC/SEND | 3000 | 1,233,273 | 63.888794 | 52782664 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome_slipstream | WETH/msETH | 500 | 1,227,863 | 1.130602 | 52782664 | `0x74F72788F4814D7fF3C49B44684aa98Eee140C0E` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,222,240 | 0.004500 | 52782664 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,183,498 | 2,336.983226 | 52782664 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | WETH/doginme | 10000 | 1,180,241 | 33,769,289.311157 | 52782664 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,161,084 | 23.270681 | 52782664 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| aerodrome | WETH/WELL | 10000 | 1,123,355 | 1,173,149.213795 | 52782664 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,094,371 | 532,485.414212 | 52782664 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,073,095 | 15.676392 | 52782664 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | USDC/NOCK | 3000 | 1,069,749 | 55.062036 | 52782664 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,025,614 | 1.105812 | 52782664 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |

## Recherche d'opportunités
- Cycles : 473 ; routes examinées : 9840292 ; candidats optimisés : 32636 ; net attendu > 0 : 48 ; dernier cycle 115.3 ms
- Rejets (moteur) : {'spread_below_threshold': 9701715, 'liquidity_below_min': 93222, 'negative_expected_net': 32588, 'pool_quarantined': 12246, 'borrow_bound_too_small': 473}
- Enregistrements de la session : 32636 ; net attendu > 0 : 48 ; simulés (eth_call de la vraie tx) : 6 (ok 0, échec 6) ; étiquettes ghost N+1 : 0/3 positives
- Décisions : {'REJECTED': 32636} ; motifs de rejet : {'below_safety_margin': 40, 'negative_expected_net': 32588, 'p_lower_below_threshold': 46, 'price_impact': 8, 'reliability_not_demonstrated': 2, 'simulation_failed': 6}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
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
| 52782617 | cbBTC→[aerodrome_slipstream]→tBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.001321 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0097 €) | — | 0.98 | 0.125 (n=115) | REJECTED | below_safety_margin(13<26), p_lower_below_threshold(0.13<0.75) |
| 52782617 | cbBTC→[uniswap_v3]→tBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.001321 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0097 €) | — | 0.98 | 0.125 (n=115) | REJECTED | below_safety_margin(13<26), p_lower_below_threshold(0.13<0.75) |
| 52782618 | cbBTC→[aerodrome_slipstream]→tBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.001321 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0097 €) | — | 0.98 | 0.125 (n=115) | REJECTED | below_safety_margin(13<26), p_lower_below_threshold(0.13<0.75) |
| 52782618 | cbBTC→[uniswap_v3]→tBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.001321 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0097 €) | — | 0.98 | 0.125 (n=115) | REJECTED | below_safety_margin(13<26), p_lower_below_threshold(0.13<0.75) |
| 52782616 | USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→tBTC→[aerodrome_slipstream]→USDC | 109.742325 USDC | 0.017808 USDC | 0.000000 USDC | 0.007387 USDC | 0.010421 USDC (0.0096 €) | — | 0.95 | 0.125 (n=115) | REJECTED | below_safety_margin(10421<21948), p_lower_below_threshold(0.13<0.75) |
| 52782616 | USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→tBTC→[aerodrome_slipstream]→USDC | 109.742325 USDC | 0.017808 USDC | 0.000000 USDC | 0.007387 USDC | 0.010421 USDC (0.0096 €) | — | 0.95 | 0.125 (n=115) | REJECTED | below_safety_margin(10421<21948), p_lower_below_threshold(0.13<0.75) |
| 52782616 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→tBTC→[aerodrome_slipstream]→USDC | 109.743171 USDC | 0.017642 USDC | 0.000000 USDC | 0.007387 USDC | 0.010255 USDC (0.0094 €) | — | 0.93 | 0.125 (n=115) | REJECTED | below_safety_margin(10255<21948), p_lower_below_threshold(0.13<0.75) |
| 52782616 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→tBTC→[aerodrome_slipstream]→USDC | 109.743171 USDC | 0.017642 USDC | 0.000000 USDC | 0.007387 USDC | 0.010255 USDC (0.0094 €) | — | 0.93 | 0.125 (n=115) | REJECTED | below_safety_margin(10255<21948), p_lower_below_threshold(0.13<0.75) |
| 52782616 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→tBTC→[aerodrome_slipstream]→USDC | 108.792720 USDC | 0.017619 USDC | 0.000000 USDC | 0.007387 USDC | 0.010232 USDC (0.0094 €) | — | 0.94 | 0.125 (n=115) | REJECTED | below_safety_margin(10232<21758), p_lower_below_threshold(0.13<0.75) |

## Fiabilité et décision
- Observations ghost : 1076 ; taux observé 0.112 ; borne inférieure crédible (0.9) 0.101 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 10.1% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
