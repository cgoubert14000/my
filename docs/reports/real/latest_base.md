# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-21T13:03:13+00:00 ; durée 157.5 min ; blocs 52894493 → 52899219 (3466 vus)

## Connexion
- Requêtes RPC : 50039 ; erreurs : 73 ; latence p50/p95 : 269.2/981.7 ms
- Rafraîchissements d'état : 3466 ; âge des données au dernier bloc : 4.59 s ; changements de frais LP observés (pools à frais dynamiques) : 9649
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 44468 ; cycles déclenchés par événement : 1910 ; avance médiane sur le rafraîchissement multicall : 1,428 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,466.30 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 578 pools, 326 jetons, 21598 routes
- Par DEX : uniswap_v3 138, aerodrome 235, aerodrome_slipstream 155, pancakeswap_v3 32, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 206 (rejetés 2) → 611 jetons ; pools candidats 3912 (énumérés 393, par paires 0), mesurés 581, sous le plancher de 10000.0 $ : 3 → gardés 578 (max 1500) ; prix des hubs : {'USDC': 1.0, 'DAI': 1.0, 'USDbC': 1.0, 'WETH': 2451.17881, 'AERO': 0.838921, 'cbBTC': 83216.410353}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 149,743,663 | 2,466.298628 | 52899220 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 38,428,537 | 1.166083 | 52899220 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| aerodrome | WETH/VVV | 3000 | 18,042,429 | 93.547547 | 52899220 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,519,805 | 0.029580 | 52899220 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome_slipstream | WETH/cbBTC | 2505 | 13,707,927 | 0.029526 | 52899220 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,491,910 | 0.029506 | 52899220 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,461,470 | 0.000012 | 52899220 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome_slipstream | USDC/cbBTC | 556 | 9,396,254 | 0.000012 | 52899220 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | WETH/USDC | 500 | 8,815,241 | 2,471.580790 | 52899220 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/USDC | 3000 | 8,488,968 | 2,466.318411 | 52899220 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | USDC/cbBTC | 354 | 7,405,381 | 0.000012 | 52899220 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 743 | 7,404,591 | 2,471.041953 | 52899220 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,332,025 | 0.001674 | 52899220 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,642,593 | 0.029579 | 52899220 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | fBOMB/AERO | 10000 | 4,969,016 | 0.023127 | 52899220 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,753,361 | 0.802393 | 52899220 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,465,496 | 2,470.835899 | 52899220 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,425,538 | 0.998741 | 52899220 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,281,690 | 0.000279 | 52899220 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome | WETH/KTA | 3000 | 4,073,803 | 34,763.217159 | 52899220 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDT | 445 | 3,968,217 | 2,474.383378 | 52899220 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome | WETH/AERO | 10000 | 3,383,010 | 2,894.588640 | 52899220 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | USDC/AERO | 10000 | 3,062,467 | 1.173188 | 52899220 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome_slipstream | WETH/VVV | 2766 | 2,796,656 | 93.524305 | 52899220 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,772,465 | 392.531616 | 52899220 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,552,182 | 1.142094 | 52899220 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,271,159 | 0.000012 | 52899220 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 2,270,637 | 0.915922 | 52899220 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| aerodrome | WETH/FAI | 10000 | 2,258,618 | 1,209,742.010817 | 52899220 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | AERO/cbBTC | 2700 | 2,181,041 | 0.000010 | 52899220 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 2,142,611 | 1,031.804067 | 52899220 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 2,072,244 | 0.000012 | 52899220 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,027,072 | 1.383640 | 52899220 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,966,787 | 0.000000 | 52899220 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome | weETH_04c0/WETH | 500 | 1,921,382 | 1.105697 | 52899220 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,876,211 | 15.870971 | 52899220 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| uniswap_v3 | XDP/USDC | 100 | 1,802,452 | 0.019062 | 52899220 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,710,913 | 1.489914 | 52899220 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome | WETH/msETH (stable) | 500 | 1,701,989 | 2.312064 | 52899220 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | WETH/AERO | 3000 | 1,692,322 | 2,879.701259 | 52899220 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,673,522 | 13,279.183539 | 52899220 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,457,236 | 0.826492 | 52899220 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome | fBOMB/USDC | 10000 | 1,445,164 | 0.019868 | 52899220 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| aerodrome_slipstream | EURC/USDC | 70 | 1,431,052 | 1.123178 | 52899220 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,353,937 | 0.004769 | 52899220 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,345,112 | 0.000281 | 52899220 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| uniswap_v3 | DRB/WETH | 10000 | 1,337,479 | 0.000000 | 52899220 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | WETH/cbBTC | 3000 | 1,319,451 | 0.029502 | 52899220 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,276,381 | 2,471.661052 | 52899220 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,234,107 | 63.802382 | 52899220 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,232,672 | 34,921,488.905811 | 52899220 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,223,980 | 23.086051 | 52899220 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| aerodrome | WETH/WELL | 10000 | 1,219,153 | 1,109,528.270040 | 52899220 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome_slipstream | WETH/VVV | 8000 | 1,208,656 | 93.737962 | 52899220 | `0x46D398A5b33709877f50c8918A7eE96F1Be1d7dd` |
| aerodrome | WETH/EDEL | 7000 | 1,207,749 | 71,380.137454 | 52899220 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,188,903 | 483,699.722768 | 52899220 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome_slipstream | msUSD/USDC | 500 | 1,186,470 | 0.886478 | 52899220 | `0x7501bc8Bb51616F79bfA524E464fb7B41f0B10fB` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,182,089 | 0.436943 | 52899220 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| aerodrome | USDC/NOCK | 3000 | 1,180,043 | 45.249041 | 52899220 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,167,200 | 1.106158 | 52899220 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |

## Recherche d'opportunités
- Cycles : 5375 ; routes examinées : 116089250 ; candidats optimisés : 656340 ; net attendu > 0 : 224 ; dernier cycle 240.6 ms
- Rejets (moteur) : {'spread_below_threshold': 114402991, 'liquidity_below_min': 884358, 'negative_expected_net': 656116, 'pool_quarantined': 136358, 'borrow_bound_too_small': 5342, 'cycle_budget_exhausted': 3861}
- Enregistrements de la session : 656340 ; net attendu > 0 : 224 ; simulés (eth_call de la vraie tx) : 37 (ok 16, échec 21) ; étiquettes ghost N+1 : 0/24 positives
- Décisions : {'REJECTED': 656340} ; motifs de rejet : {'below_safety_margin': 168, 'negative_expected_net': 656116, 'p_lower_below_threshold': 149, 'price_impact': 67, 'reliability_not_demonstrated': 75, 'simulation_failed': 21, 'stale_data': 39}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52896492 | cbBTC→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→cbBTC | 0.003091 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0513 €) | — | 2.17 | 0.287 (n=92) | REJECTED | stale_data(8160ms>4000.0), simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.29<0.75) |
| 52896493 | cbBTC→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→cbBTC | 0.003091 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0513 €) | — | 2.17 | 0.287 (n=92) | REJECTED | stale_data(9527ms>4000.0), simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.29<0.75) |
| 52896492 | USDC→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→USDC | 260.497471 USDC | 0.062607 USDC | 0.000000 USDC | 0.007387 USDC | 0.055220 USDC (0.0508 €) | — | 2.12 | 0.287 (n=92) | REJECTED | stale_data(8156ms>4000.0), simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.29<0.75) |
| 52896493 | USDC→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→USDC | 260.497471 USDC | 0.062607 USDC | 0.000000 USDC | 0.007387 USDC | 0.055220 USDC (0.0508 €) | — | 2.12 | 0.287 (n=92) | REJECTED | stale_data(9524ms>4000.0), simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.29<0.75) |
| 52895732 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 27.839630 USDC | 0.068292 USDC | 0.000000 USDC | 0.015234 USDC | 0.053058 USDC (0.0488 €) | — | 19.06 | 0.000 (n=25) | REJECTED | reliability_not_demonstrated |
| 52895732 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.011374 WETH | 0.000028 WETH | 0.000000 WETH | 0.000006 WETH | 0.000022 WETH (0.0487 €) | 0.000022 WETH | 18.96 | 0.000 (n=25) | REJECTED | reliability_not_demonstrated |
| 52895732 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 27.539992 USDC | 0.066544 USDC | 0.000000 USDC | 0.015234 USDC | 0.051310 USDC (0.0472 €) | — | 18.63 | 0.000 (n=25) | REJECTED | reliability_not_demonstrated |
| 52895732 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.011221 WETH | 0.000027 WETH | 0.000000 WETH | 0.000006 WETH | 0.000021 WETH (0.0471 €) | 0.000021 WETH | 18.59 | 0.000 (n=25) | REJECTED | reliability_not_demonstrated |
| 52895732 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 27.419986 USDC | 0.066108 USDC | 0.000000 USDC | 0.015234 USDC | 0.050874 USDC (0.0468 €) | — | 18.55 | 0.000 (n=25) | REJECTED | reliability_not_demonstrated |
| 52895732 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.011190 WETH | 0.000027 WETH | 0.000000 WETH | 0.000006 WETH | 0.000021 WETH (0.0467 €) | 0.000021 WETH | 18.48 | 0.000 (n=25) | REJECTED | reliability_not_demonstrated |
| 52895732 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 27.299978 USDC | 0.065066 USDC | 0.000000 USDC | 0.015234 USDC | 0.049832 USDC (0.0458 €) | — | 18.25 | 0.000 (n=25) | REJECTED | reliability_not_demonstrated |
| 52895732 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.011101 WETH | 0.000026 WETH | 0.000000 WETH | 0.000006 WETH | 0.000020 WETH (0.0457 €) | — | 18.25 | 0.000 (n=25) | REJECTED | reliability_not_demonstrated |
| 52899165 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.280312 WETH | 0.000023 WETH | 0.000000 WETH | 0.000003 WETH | 0.000020 WETH (0.0453 €) | — | 0.71 | 0.001 (n=6) | REJECTED | below_safety_margin(19984495363938<56062409894286), reliability_not_demonstrated |
| 52899165 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 659.667589 USDC | 0.057567 USDC | 0.000000 USDC | 0.008369 USDC | 0.049198 USDC (0.0453 €) | — | 0.75 | 0.001 (n=6) | REJECTED | below_safety_margin(49198<131933), reliability_not_demonstrated |
| 52895732 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[sushiswap_v3]→USDC | 26.661639 USDC | 0.064178 USDC | 0.000000 USDC | 0.015234 USDC | 0.048944 USDC (0.0450 €) | — | 18.36 | 0.000 (n=25) | REJECTED | reliability_not_demonstrated |
| 52895732 | WETH→[sushiswap_v3]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.010882 WETH | 0.000026 WETH | 0.000000 WETH | 0.000006 WETH | 0.000020 WETH (0.0449 €) | — | 18.29 | 0.000 (n=25) | REJECTED | reliability_not_demonstrated |
| 52899165 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.009197 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0445 €) | — | 0.63 | 0.001 (n=6) | REJECTED | below_safety_margin(58<183), reliability_not_demonstrated |
| 52895732 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 24.964327 USDC | 0.054526 USDC | 0.000000 USDC | 0.015234 USDC | 0.039292 USDC (0.0361 €) | — | 15.74 | 0.000 (n=25) | REJECTED | reliability_not_demonstrated |
| 52895732 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.010207 WETH | 0.000022 WETH | 0.000000 WETH | 0.000006 WETH | 0.000016 WETH (0.0361 €) | — | 15.65 | 0.000 (n=25) | REJECTED | reliability_not_demonstrated |
| 52895732 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 22.008324 USDC | 0.053146 USDC | 0.000000 USDC | 0.015234 USDC | 0.037912 USDC (0.0349 €) | — | 17.23 | 0.000 (n=25) | REJECTED | reliability_not_demonstrated |
| 52895732 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.009021 WETH | 0.000022 WETH | 0.000000 WETH | 0.000006 WETH | 0.000015 WETH (0.0348 €) | — | 17.10 | 0.000 (n=25) | REJECTED | reliability_not_demonstrated |
| 52896492 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→cbBTC | 0.002578 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0276 €) | — | 1.40 | 0.118 (n=196) | REJECTED | below_safety_margin(36<51), stale_data(8193ms>4000.0), p_lower_below_threshold(0.12<0.75) |
| 52896493 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→cbBTC | 0.002578 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0276 €) | — | 1.40 | 0.118 (n=196) | REJECTED | below_safety_margin(36<51), stale_data(9560ms>4000.0), p_lower_below_threshold(0.12<0.75) |
| 52896492 | USDC→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 198.417427 USDC | 0.036754 USDC | 0.000000 USDC | 0.007387 USDC | 0.029367 USDC (0.0270 €) | — | 1.48 | 0.118 (n=196) | REJECTED | below_safety_margin(29367<39683), stale_data(8189ms>4000.0), p_lower_below_threshold(0.12<0.75) |
| 52896493 | USDC→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 198.417427 USDC | 0.036754 USDC | 0.000000 USDC | 0.007387 USDC | 0.029367 USDC (0.0270 €) | — | 1.48 | 0.118 (n=196) | REJECTED | below_safety_margin(29367<39683), stale_data(9557ms>4000.0), p_lower_below_threshold(0.12<0.75) |

## Fiabilité et décision
- Observations ghost : 1677 ; taux observé 0.100 ; borne inférieure crédible (0.9) 0.091 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 9.1% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
