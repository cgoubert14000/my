# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-18T14:14:42+00:00 ; durée 316.49 min ; blocs 52762270 → 52771761 (9269 vus)

## Connexion
- Requêtes RPC : 127465 ; erreurs : 0 ; latence p50/p95 : 269.7/820.6 ms
- Rafraîchissements d'état : 9269 ; âge des données au dernier bloc : 2.34 s ; changements de frais LP observés (pools à frais dynamiques) : 17353
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 153864 ; cycles déclenchés par événement : 12782 ; avance médiane sur le rafraîchissement multicall : 607 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,388.16 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 578 pools, 328 jetons, 21580 routes
- Par DEX : uniswap_v3 136, aerodrome 235 (quarantaine 1), aerodrome_slipstream 157, pancakeswap_v3 32, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 207 (rejetés 2) → 612 jetons ; pools candidats 3915 (énumérés 394, par paires 0), mesurés 580, sous le plancher de 10000.0 $ : 2 → gardés 578 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'DAI': 1.0, 'USDC': 1.0, 'WETH': 2410.986474, 'AERO': 0.834015, 'cbBTC': 81629.281689}
- Pools en quarantaine : 1 — aerodrome:fBOMB/AERO@0xbBf71A: simulation failed ×5 (model/chain mismatch) — until block 52771998

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 145,460,401 | 2,388.159473 | 52771760 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 42,078,095 | 1.243823 | 52771760 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 19,106,753 | 0.029387 | 52771760 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 500 | 18,052,815 | 0.029379 | 52771760 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 16,510,582 | 108.345157 | 52771760 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,322,052 | 0.029399 | 52771760 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,748,855 | 0.000012 | 52771760 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 8,988,362 | 2,385.715861 | 52771760 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome_slipstream | USDC/cbBTC | 338 | 7,846,818 | 0.000012 | 52771760 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 594 | 7,279,907 | 2,384.912777 | 52771760 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,087,366 | 0.001646 | 52771760 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 460 | 6,787,848 | 0.000012 | 52771760 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome | WETH/USDC | 3000 | 5,449,208 | 2,388.128035 | 52771760 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,285,641 | 0.029379 | 52771760 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/superOETHb | 400 | 5,186,057 | 1.000855 | 52771760 | `0x6446021F4E396dA3df4235C62537431372195D38` |
| aerodrome_slipstream | WETH/USDT | 403 | 5,053,809 | 2,389.361542 | 52771760 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome | fBOMB/AERO | 10000 | 5,010,138 | 0.025774 | 52771760 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,773,625 | 0.802398 | 52771760 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,578,605 | 0.000271 | 52771760 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | USDC/AERO | 10000 | 4,425,509 | 1.238952 | 52771760 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,413,964 | 0.998809 | 52771760 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,396,227 | 2,384.949553 | 52771760 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | WETH/KTA | 3000 | 4,023,414 | 33,416.485542 | 52771760 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/AERO | 10000 | 3,270,850 | 2,949.526183 | 52771760 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,879,673 | 1.141821 | 52771760 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,831,956 | 0.000012 | 52771760 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | AERO/cbBTC | 2700 | 2,620,577 | 0.000010 | 52771760 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/VVV | 2742 | 2,520,610 | 108.369182 | 52771760 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,498,394 | 411.336882 | 52771760 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | WETH/FAI | 10000 | 2,148,386 | 1,254,386.905932 | 52771760 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,106,891 | 1.199655 | 52771760 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,035,564 | 1.373959 | 52771760 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| aerodrome_slipstream | EURC/USDC | 70 | 1,959,548 | 1.123313 | 52771760 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| aerodrome_slipstream | WETH/MORPHO | 2703 | 1,890,016 | 1,017.996281 | 52771760 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,845,173 | 0.000000 | 52771760 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome | fBOMB/USDC | 10000 | 1,800,186 | 0.021310 | 52771760 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,764,247 | 0.000012 | 52771760 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | XDP/USDC | 100 | 1,759,193 | 0.018503 | 52771760 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,755,564 | 15.790161 | 52771760 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | weETH_04c0/WETH | 500 | 1,726,861 | 1.105521 | 52771760 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,667,547 | 14,002.325891 | 52771760 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/msETH (stable) | 500 | 1,654,987 | 2.304383 | 52771760 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | WETH/AERO | 3000 | 1,484,195 | 2,966.440045 | 52771760 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,456,394 | 0.826238 | 52771760 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,448,923 | 0.916352 | 52771760 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,318,449 | 0.435380 | 52771760 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,310,676 | 0.000000 | 52771760 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,283,316 | 0.000270 | 52771760 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,280,191 | 0.004636 | 52771760 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome | WETH/cbBTC | 3000 | 1,246,660 | 0.029402 | 52771760 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| aerodrome | USDC/SEND | 3000 | 1,233,250 | 63.891160 | 52771760 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,226,098 | 23.333413 | 52771760 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| aerodrome_slipstream | WETH/msETH | 500 | 1,200,865 | 1.131038 | 52771760 | `0x74F72788F4814D7fF3C49B44684aa98Eee140C0E` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,197,438 | 2,385.721482 | 52771760 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | WETH/doginme | 10000 | 1,187,153 | 35,301,041.288967 | 52771760 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | WETH/WELL | 10000 | 1,152,330 | 1,164,557.484278 | 52771760 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,116,236 | 525,259.689133 | 52771760 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome_slipstream | msUSD/USDC | 500 | 1,105,030 | 0.885254 | 52771760 | `0x7501bc8Bb51616F79bfA524E464fb7B41f0B10fB` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,087,820 | 15.146986 | 52771760 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | USDC/NOCK | 3000 | 1,073,023 | 54.726175 | 52771760 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |

## Recherche d'opportunités
- Cycles : 22050 ; routes examinées : 475839000 ; candidats optimisés : 2445686 ; net attendu > 0 : 1790 ; dernier cycle 168.4 ms
- Rejets (moteur) : {'spread_below_threshold': 469483087, 'liquidity_below_min': 3564733, 'negative_expected_net': 2443896, 'pool_quarantined': 308798, 'borrow_bound_too_small': 22042, 'cycle_budget_exhausted': 14654}
- Enregistrements de la session : 2445686 ; net attendu > 0 : 1790 ; simulés (eth_call de la vraie tx) : 136 (ok 32, échec 104) ; étiquettes ghost N+1 : 0/97 positives
- Décisions : {'REJECTED': 2445686} ; motifs de rejet : {'below_safety_margin': 950, 'negative_expected_net': 2443896, 'p_lower_below_threshold': 932, 'price_impact': 53, 'reliability_not_demonstrated': 858, 'simulation_failed': 104, 'stale_data': 2}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52771041 | USDC→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 7,122.719600 USDC | 60.931384 USDC | 0.000000 USDC | 0.008276 USDC | 60.923108 USDC (56.0493 €) | — | 85.53 | 0.002 (n=3) | REJECTED | reliability_not_demonstrated |
| 52771040 | USDC→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 7,122.719600 USDC | 60.931384 USDC | 0.000000 USDC | 0.008276 USDC | 60.923108 USDC (56.0493 €) | — | 85.53 | 0.002 (n=3) | REJECTED | reliability_not_demonstrated |
| 52771041 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→cbBTC | 0.087255 cbBTC | 0.000749 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000749 cbBTC (55.9543 €) | — | 85.80 | 0.002 (n=3) | REJECTED | reliability_not_demonstrated |
| 52771040 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→cbBTC | 0.087255 cbBTC | 0.000749 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000749 cbBTC (55.9543 €) | — | 85.80 | 0.002 (n=3) | REJECTED | reliability_not_demonstrated |
| 52771041 | USDC→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→USDC | 7,124.821530 USDC | 59.402478 USDC | 0.000000 USDC | 0.007188 USDC | 59.395290 USDC (54.6437 €) | — | 83.36 | 0.002 (n=3) | REJECTED | reliability_not_demonstrated |
| 52771040 | USDC→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→USDC | 7,124.821530 USDC | 59.402478 USDC | 0.000000 USDC | 0.007188 USDC | 59.395290 USDC (54.6437 €) | — | 83.36 | 0.002 (n=3) | REJECTED | reliability_not_demonstrated |
| 52771041 | cbBTC→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→cbBTC | 0.087248 cbBTC | 0.000730 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000730 cbBTC (54.5552 €) | — | 83.66 | 0.002 (n=3) | REJECTED | reliability_not_demonstrated |
| 52771040 | cbBTC→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→cbBTC | 0.087248 cbBTC | 0.000730 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000730 cbBTC (54.5552 €) | — | 83.66 | 0.002 (n=3) | REJECTED | reliability_not_demonstrated |
| 52770826 | USDC→[aerodrome_slipstream]→LCAP→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 2,417.325434 USDC | 59.066396 USDC | 0.000000 USDC | 0.008276 USDC | 59.058120 USDC (54.3335 €) | — | 244.31 | 0.003 (n=2) | REJECTED | reliability_not_demonstrated |
| 52770826 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→LCAP→[aerodrome_slipstream]→WETH | 1.011007 WETH | 0.024704 WETH | 0.000000 WETH | 0.000003 WETH | 0.024700 WETH (54.2571 €) | — | 244.31 | 0.003 (n=2) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52771041 | USDC→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→USDC | 7,123.128067 USDC | 58.626565 USDC | 0.000000 USDC | 0.007188 USDC | 58.619377 USDC (53.9298 €) | — | 82.29 | 0.002 (n=3) | REJECTED | reliability_not_demonstrated |
| 52771040 | USDC→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→USDC | 7,123.128067 USDC | 58.626565 USDC | 0.000000 USDC | 0.007188 USDC | 58.619377 USDC (53.9298 €) | — | 82.29 | 0.002 (n=3) | REJECTED | reliability_not_demonstrated |
| 52771041 | cbBTC→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→cbBTC | 0.087381 cbBTC | 0.000720 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000720 cbBTC (53.8407 €) | — | 82.44 | 0.002 (n=3) | REJECTED | reliability_not_demonstrated |
| 52771040 | cbBTC→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→cbBTC | 0.087381 cbBTC | 0.000720 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000720 cbBTC (53.8407 €) | — | 82.44 | 0.002 (n=3) | REJECTED | reliability_not_demonstrated |
| 52771041 | USDC→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→cbBTC→[uniswap_v3]→USDC | 7,054.770032 USDC | 57.783546 USDC | 0.000000 USDC | 0.007188 USDC | 57.776358 USDC (53.1542 €) | — | 81.90 | 0.002 (n=3) | REJECTED | reliability_not_demonstrated |
| 52771040 | USDC→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→cbBTC→[uniswap_v3]→USDC | 7,054.770032 USDC | 57.783546 USDC | 0.000000 USDC | 0.007188 USDC | 57.776358 USDC (53.1542 €) | — | 81.90 | 0.002 (n=3) | REJECTED | reliability_not_demonstrated |
| 52771041 | cbBTC→[uniswap_v3]→USDC→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→cbBTC | 0.086472 cbBTC | 0.000710 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000710 cbBTC (53.0754 €) | — | 82.13 | 0.002 (n=3) | REJECTED | reliability_not_demonstrated |
| 52771040 | cbBTC→[uniswap_v3]→USDC→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→cbBTC | 0.086472 cbBTC | 0.000710 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000710 cbBTC (53.0754 €) | — | 82.13 | 0.002 (n=3) | REJECTED | reliability_not_demonstrated |
| 52770826 | USDC→[aerodrome_slipstream]→LCAP→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 2,312.634946 USDC | 56.708251 USDC | 0.000000 USDC | 0.007913 USDC | 56.700338 USDC (52.1643 €) | — | 245.18 | 0.006 (n=1) | REJECTED | reliability_not_demonstrated |
| 52770826 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→LCAP→[aerodrome_slipstream]→WETH | 0.967329 WETH | 0.023720 WETH | 0.000000 WETH | 0.000003 WETH | 0.023717 WETH (52.0967 €) | — | 245.18 | 0.006 (n=1) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52770826 | USDC→[aerodrome_slipstream]→LCAP→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→USDC | 2,274.640161 USDC | 55.554743 USDC | 0.000000 USDC | 0.007551 USDC | 55.547192 USDC (51.1034 €) | — | 244.20 | 0.006 (n=1) | REJECTED | reliability_not_demonstrated |
| 52770826 | WETH→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→LCAP→[aerodrome_slipstream]→WETH | 0.951562 WETH | 0.023241 WETH | 0.000000 WETH | 0.000003 WETH | 0.023237 WETH (51.0440 €) | — | 244.20 | 0.006 (n=1) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52770826 | USDC→[aerodrome_slipstream]→LCAP→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 2,243.288344 USDC | 55.084663 USDC | 0.000000 USDC | 0.007913 USDC | 55.076750 USDC (50.6706 €) | — | 245.52 | 0.003 (n=2) | REJECTED | reliability_not_demonstrated |
| 52770826 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→LCAP→[aerodrome_slipstream]→WETH | 0.939175 WETH | 0.023062 WETH | 0.000000 WETH | 0.000003 WETH | 0.023058 WETH (50.6508 €) | — | 245.52 | 0.003 (n=2) | REJECTED | reliability_not_demonstrated |
| 52770826 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→LCAP→[aerodrome_slipstream]→WETH | 0.914135 WETH | 0.022310 WETH | 0.000000 WETH | 0.000004 WETH | 0.022307 WETH (48.9994 €) | — | 244.02 | 0.006 (n=1) | REJECTED | reliability_not_demonstrated |

## Fiabilité et décision
- Observations ghost : 960 ; taux observé 0.118 ; borne inférieure crédible (0.9) 0.105 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 10.5% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
