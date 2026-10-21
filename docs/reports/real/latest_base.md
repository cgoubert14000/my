# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-21T13:24:50+00:00 ; durée 179.12 min ; blocs 52894493 → 52899869 (4050 vus)

## Connexion
- Requêtes RPC : 56827 ; erreurs : 75 ; latence p50/p95 : 552.8/2,241.6 ms
- Rafraîchissements d'état : 4051 ; âge des données au dernier bloc : 1.44 s ; changements de frais LP observés (pools à frais dynamiques) : 12343
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 44468 ; cycles déclenchés par événement : 1910 ; avance médiane sur le rafraîchissement multicall : 1,428 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,485.22 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 578 pools, 326 jetons, 21598 routes
- Par DEX : uniswap_v3 138, aerodrome 235, aerodrome_slipstream 155, pancakeswap_v3 32, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 206 (rejetés 2) → 611 jetons ; pools candidats 3912 (énumérés 393, par paires 0), mesurés 581, sous le plancher de 10000.0 $ : 3 → gardés 578 (max 1500) ; prix des hubs : {'USDC': 1.0, 'DAI': 1.0, 'USDbC': 1.0, 'WETH': 2451.17881, 'AERO': 0.838921, 'cbBTC': 83216.410353}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 150,385,304 | 2,485.216461 | 52899869 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 38,586,543 | 1.156554 | 52899869 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| aerodrome | WETH/VVV | 3000 | 18,072,744 | 94.669777 | 52899869 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,640,422 | 0.029625 | 52899869 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,566,725 | 0.029685 | 52899869 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| aerodrome_slipstream | WETH/cbBTC | 2510 | 10,189,226 | 0.029685 | 52899869 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,977,607 | 0.000012 | 52899869 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 8,857,920 | 2,479.073947 | 52899869 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/USDC | 3000 | 8,521,463 | 2,485.551410 | 52899869 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | USDC/cbBTC | 412 | 8,158,665 | 0.000012 | 52899869 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome_slipstream | USDC/cbBTC | 334 | 7,445,554 | 0.000012 | 52899869 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 684 | 7,388,247 | 2,478.132517 | 52899869 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,372,637 | 0.001672 | 52899869 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,683,120 | 0.029613 | 52899869 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/USDT | 421 | 5,118,994 | 2,482.156486 | 52899869 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome | fBOMB/AERO | 10000 | 4,996,678 | 0.023127 | 52899869 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,789,822 | 0.802393 | 52899869 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,487,618 | 2,478.082190 | 52899869 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,452,800 | 0.998741 | 52899869 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,313,568 | 0.000279 | 52899869 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome | WETH/KTA | 3000 | 4,105,738 | 34,749.948881 | 52899869 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | USDC/AERO | 10000 | 3,526,093 | 1.164397 | 52899869 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome | WETH/AERO | 10000 | 3,409,920 | 2,887.877791 | 52899869 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | WETH/VVV | 2721 | 2,805,500 | 94.690154 | 52899869 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,571,763 | 1.142095 | 52899869 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,459,684 | 391.340861 | 52899869 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | AERO/cbBTC | 2700 | 2,381,150 | 0.000010 | 52899869 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 2,298,436 | 0.915922 | 52899869 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,277,072 | 0.000012 | 52899869 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | WETH/FAI | 10000 | 2,275,016 | 1,210,727.444472 | 52899869 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 2,079,161 | 0.000012 | 52899869 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,027,072 | 1.383640 | 52899869 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,984,014 | 0.000000 | 52899869 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome | weETH_04c0/WETH | 500 | 1,936,121 | 1.105697 | 52899869 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,904,534 | 15.880019 | 52899869 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| uniswap_v3 | XDP/USDC | 100 | 1,801,360 | 0.019040 | 52899869 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome | WETH/msETH (stable) | 500 | 1,714,198 | 2.313765 | 52899869 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,708,077 | 1.494073 | 52899869 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | WETH/AERO | 3000 | 1,705,630 | 2,864.371260 | 52899869 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,656,114 | 13,221.069595 | 52899869 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome_slipstream | WETH/MORPHO | 2736 | 1,598,843 | 1,039.063836 | 52899869 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,457,236 | 0.826492 | 52899869 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome | fBOMB/USDC | 10000 | 1,447,263 | 0.019926 | 52899869 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| aerodrome_slipstream | EURC/USDC | 76 | 1,430,909 | 1.122994 | 52899869 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,364,322 | 0.004769 | 52899869 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,355,434 | 0.000281 | 52899869 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| uniswap_v3 | DRB/WETH | 10000 | 1,347,746 | 0.000000 | 52899869 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | WETH/cbBTC | 3000 | 1,328,571 | 0.029677 | 52899869 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,282,416 | 2,479.076741 | 52899869 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | WETH/doginme | 10000 | 1,241,056 | 35,011,263.634563 | 52899869 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | USDC/SEND | 3000 | 1,234,131 | 63.799906 | 52899869 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,232,812 | 23.096128 | 52899869 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| aerodrome | WETH/WELL | 10000 | 1,229,853 | 1,107,096.466975 | 52899869 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome_slipstream | msUSD/USDC | 500 | 1,221,505 | 0.886769 | 52899869 | `0x7501bc8Bb51616F79bfA524E464fb7B41f0B10fB` |
| aerodrome | WETH/EDEL | 7000 | 1,212,321 | 71,933.749817 | 52899869 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,198,022 | 483,699.724408 | 52899869 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,182,737 | 0.437300 | 52899869 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| aerodrome | USDC/NOCK | 3000 | 1,178,892 | 45.337411 | 52899869 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,176,153 | 1.106158 | 52899869 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,156,326 | 19,625,861.881136 | 52899869 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |

## Recherche d'opportunités
- Cycles : 5960 ; routes examinées : 128724080 ; candidats optimisés : 715332 ; net attendu > 0 : 536 ; dernier cycle 498.3 ms
- Rejets (moteur) : {'spread_below_threshold': 126879857, 'liquidity_below_min': 981023, 'negative_expected_net': 714796, 'pool_quarantined': 136358, 'borrow_bound_too_small': 5924, 'cycle_budget_exhausted': 5586}
- Enregistrements de la session : 715332 ; net attendu > 0 : 536 ; simulés (eth_call de la vraie tx) : 51 (ok 30, échec 21) ; étiquettes ghost N+1 : 2/37 positives
- Décisions : {'REJECTED': 715332} ; motifs de rejet : {'below_safety_margin': 376, 'negative_expected_net': 714796, 'p_lower_below_threshold': 409, 'price_impact': 67, 'reliability_not_demonstrated': 127, 'simulation_failed': 21, 'stale_data': 39}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52899326 | USDC→[aerodrome_slipstream]→oUSDT→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 184.388724 USDC | 0.073887 USDC | 0.000000 USDC | 0.009339 USDC | 0.064548 USDC (0.0594 €) | — | 3.50 | 0.115 (n=155) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52899326 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→oUSDT→[aerodrome_slipstream]→WETH | 0.074309 WETH | 0.000030 WETH | 0.000000 WETH | 0.000004 WETH | 0.000026 WETH (0.0592 €) | 0.000026 WETH | 3.48 | 0.115 (n=155) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52899325 | USDC→[aerodrome_slipstream]→oUSDT→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 176.029615 USDC | 0.066830 USDC | 0.000000 USDC | 0.008706 USDC | 0.058124 USDC (0.0535 €) | — | 3.30 | 0.105 (n=153) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 52899325 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→oUSDT→[aerodrome_slipstream]→WETH | 0.070579 WETH | 0.000027 WETH | 0.000000 WETH | 0.000004 WETH | 0.000023 WETH (0.0534 €) | 0.000023 WETH | 3.31 | 0.105 (n=153) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 52899325 | USDC→[aerodrome_slipstream]→oUSDT→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 172.855756 USDC | 0.066688 USDC | 0.000000 USDC | 0.008706 USDC | 0.057982 USDC (0.0533 €) | — | 3.35 | 0.105 (n=153) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 52899325 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→oUSDT→[aerodrome_slipstream]→WETH | 0.069353 WETH | 0.000027 WETH | 0.000000 WETH | 0.000004 WETH | 0.000023 WETH (0.0532 €) | 0.000023 WETH | 3.36 | 0.105 (n=153) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 52896492 | cbBTC→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→cbBTC | 0.003091 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0513 €) | — | 2.17 | 0.287 (n=92) | REJECTED | stale_data(8160ms>4000.0), simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.29<0.75) |
| 52896493 | cbBTC→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→cbBTC | 0.003091 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0513 €) | — | 2.17 | 0.287 (n=92) | REJECTED | stale_data(9527ms>4000.0), simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.29<0.75) |
| 52896492 | USDC→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→USDC | 260.497471 USDC | 0.062607 USDC | 0.000000 USDC | 0.007387 USDC | 0.055220 USDC (0.0508 €) | — | 2.12 | 0.287 (n=92) | REJECTED | stale_data(8156ms>4000.0), simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.29<0.75) |
| 52896493 | USDC→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→USDC | 260.497471 USDC | 0.062607 USDC | 0.000000 USDC | 0.007387 USDC | 0.055220 USDC (0.0508 €) | — | 2.12 | 0.287 (n=92) | REJECTED | stale_data(9524ms>4000.0), simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.29<0.75) |
| 52895732 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 27.839630 USDC | 0.068292 USDC | 0.000000 USDC | 0.015234 USDC | 0.053058 USDC (0.0488 €) | — | 19.06 | 0.000 (n=25) | REJECTED | reliability_not_demonstrated |
| 52895732 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.011374 WETH | 0.000028 WETH | 0.000000 WETH | 0.000006 WETH | 0.000022 WETH (0.0487 €) | 0.000022 WETH | 18.96 | 0.000 (n=25) | REJECTED | reliability_not_demonstrated |
| 52899326 | USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 204.540661 USDC | 0.062069 USDC | 0.000000 USDC | 0.009339 USDC | 0.052730 USDC (0.0485 €) | — | 2.58 | 0.116 (n=199) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52899326 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH | 0.081976 WETH | 0.000025 WETH | 0.000000 WETH | 0.000004 WETH | 0.000021 WETH (0.0484 €) | 0.000021 WETH | 2.58 | 0.116 (n=199) | REJECTED | p_lower_below_threshold(0.12<0.75) |
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
| 52899325 | USDC→[aerodrome_slipstream]→oUSDT→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 163.298636 USDC | 0.057441 USDC | 0.000000 USDC | 0.008706 USDC | 0.048735 USDC (0.0448 €) | — | 2.98 | 0.278 (n=95) | REJECTED | p_lower_below_threshold(0.28<0.75) |

## Fiabilité et décision
- Observations ghost : 1690 ; taux observé 0.100 ; borne inférieure crédible (0.9) 0.091 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 9.1% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ✅ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
