# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-22T07:13:18+00:00 ; durée 236.96 min ; blocs 52924813 → 52931918 (6773 vus)

## Connexion
- Requêtes RPC : 85195 ; erreurs : 0 ; latence p50/p95 : 297.3/1,171.7 ms
- Rafraîchissements d'état : 6773 ; âge des données au dernier bloc : 4.66 s ; changements de frais LP observés (pools à frais dynamiques) : 11166
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 102324 ; cycles déclenchés par événement : 6036 ; avance médiane sur le rafraîchissement multicall : 687 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,431.64 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 566 pools, 325 jetons, 21116 routes
- Par DEX : uniswap_v3 137, aerodrome 233, aerodrome_slipstream 146, pancakeswap_v3 32, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 205 (rejetés 2) → 610 jetons ; pools candidats 3904 (énumérés 382, par paires 0), mesurés 569, sous le plancher de 10000.0 $ : 3 → gardés 566 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDbC': 1.0, 'USDC': 1.0, 'WETH': 2442.747144, 'AERO': 0.821241, 'cbBTC': 82764.497741}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 156,289,778 | 2,431.638195 | 52931918 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 24,048,290 | 1.242618 | 52931918 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| aerodrome | WETH/VVV | 3000 | 16,551,415 | 89.416896 | 52931918 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,424,104 | 0.029500 | 52931918 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,357,732 | 0.029433 | 52931918 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 9,678,926 | 0.029448 | 52931918 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,425,929 | 0.000012 | 52931918 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 8,724,383 | 2,425.563894 | 52931918 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/USDC | 3000 | 7,371,147 | 2,425.940034 | 52931918 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,206,637 | 0.001655 | 52931918 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 346 | 7,066,995 | 0.000012 | 52931918 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 150 | 6,169,218 | 2,424.699931 | 52931918 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | USDC/cbBTC | 496 | 5,730,258 | 0.000012 | 52931918 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,507,280 | 0.029488 | 52931918 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,595,063 | 2,424.613547 | 52931918 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,334,233 | 1.000001 | 52931918 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,035,778 | 0.000275 | 52931918 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome | WETH/KTA | 3000 | 4,035,761 | 34,431.428386 | 52931918 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDT | 436 | 2,886,750 | 2,429.139775 | 52931918 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome_slipstream | WETH/VVV | 2820 | 2,638,306 | 89.402402 | 52931918 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | WETH/AERO | 10000 | 2,451,646 | 2,996.326113 | 52931918 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,336,811 | 395.962455 | 52931918 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | WETH/FAI | 10000 | 2,233,606 | 1,202,377.034974 | 52931918 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,232,301 | 0.000012 | 52931918 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 2,076,892 | 0.000012 | 52931918 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,925,582 | 0.000000 | 52931918 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,791,750 | 0.018463 | 52931918 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,703,434 | 1.495413 | 52931918 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | WETH/AERO | 3000 | 1,642,399 | 3,017.328664 | 52931918 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | fBOMB/AERO | 10000 | 1,528,625 | 0.023153 | 52931918 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,452,809 | 0.824474 | 52931918 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,430,011 | 13,415.096370 | 52931918 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome_slipstream | WETH/wstETH | 90 | 1,374,953 | 0.802252 | 52931918 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,368,716 | 0.004845 | 52931918 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome | USDC/alUSDb (stable) | 500 | 1,357,471 | 1.407176 | 52931918 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| uniswap_v3 | DRB/WETH | 10000 | 1,355,907 | 0.000000 | 52931918 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | WETH/msETH (stable) | 500 | 1,347,948 | 2.339626 | 52931918 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,316,767 | 0.000273 | 52931918 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,289,054 | 2,425.578016 | 52931918 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 1,243,116 | 0.000010 | 52931918 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | USDC/SEND | 3000 | 1,231,521 | 64.070530 | 52931918 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome | WETH/WELL | 10000 | 1,211,342 | 1,085,977.101493 | 52931918 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/doginme | 10000 | 1,208,763 | 35,491,788.032360 | 52931918 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,208,552 | 16.268614 | 52931918 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | USDC/NOCK | 3000 | 1,183,193 | 45.004916 | 52931918 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,159,881 | 497,795.004998 | 52931918 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | WETH/EDEL | 7000 | 1,147,118 | 71,756.853916 | 52931918 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | weETH_04c0/WETH | 500 | 1,134,915 | 1.105687 | 52931918 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome | fBOMB/USDC | 10000 | 1,130,489 | 0.018943 | 52931918 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,076,205 | 21,404,549.125666 | 52931918 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | EURC/USDC | 73 | 1,073,494 | 1.124820 | 52931918 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,064,988 | 0.915940 | 52931918 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| aerodrome | WETH/cbBTC | 3000 | 1,057,681 | 0.029550 | 52931918 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,040,240 | 17.020993 | 52931918 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,024,185 | 23.273012 | 52931918 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| uniswap_v3 | USDC/VVV | 3000 | 991,390 | 0.036823 | 52931918 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/MORPHO | 3000 | 972,462 | 1,060.454592 | 52931918 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/USDC | 10000 | 936,522 | 2,448.898563 | 52931918 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | uXRP/WETH | 3000 | 927,590 | 0.000549 | 52931918 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome | WETH/bsdETH | 100 | 905,742 | 0.916123 | 52931918 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |

## Recherche d'opportunités
- Cycles : 12808 ; routes examinées : 270453728 ; candidats optimisés : 1678243 ; net attendu > 0 : 480 ; dernier cycle 214.1 ms
- Rejets (moteur) : {'spread_below_threshold': 266399179, 'liquidity_below_min': 2360720, 'negative_expected_net': 1677763, 'borrow_bound_too_small': 12808, 'cycle_budget_exhausted': 2778}
- Enregistrements de la session : 1678243 ; net attendu > 0 : 480 ; simulés (eth_call de la vraie tx) : 33 (ok 10, échec 23) ; étiquettes ghost N+1 : 0/26 positives
- Décisions : {'REJECTED': 1678243} ; motifs de rejet : {'below_safety_margin': 334, 'negative_expected_net': 1677763, 'p_lower_below_threshold': 427, 'price_impact': 2, 'reliability_not_demonstrated': 53, 'simulation_failed': 23, 'stale_data': 44}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52926420 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 101.514809 USDC | 1.562586 USDC | 0.000000 USDC | 0.007331 USDC | 1.555255 USDC (1.4308 €) | — | 153.20 | 0.001 (n=8) | REJECTED | reliability_not_demonstrated |
| 52926420 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.041568 WETH | 0.000640 WETH | 0.000000 WETH | 0.000003 WETH | 0.000637 WETH (1.4293 €) | — | 153.20 | 0.001 (n=8) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52926420 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 101.275838 USDC | 1.556722 USDC | 0.000000 USDC | 0.007331 USDC | 1.549391 USDC (1.4254 €) | — | 152.99 | 0.001 (n=6) | REJECTED | reliability_not_demonstrated |
| 52926420 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.041474 WETH | 0.000637 WETH | 0.000000 WETH | 0.000003 WETH | 0.000634 WETH (1.4240 €) | — | 152.99 | 0.001 (n=6) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52926420 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 96.908899 USDC | 1.484555 USDC | 0.000000 USDC | 0.007331 USDC | 1.477224 USDC (1.3590 €) | — | 152.43 | 0.001 (n=6) | REJECTED | reliability_not_demonstrated |
| 52926420 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.039701 WETH | 0.000608 WETH | 0.000000 WETH | 0.000003 WETH | 0.000605 WETH (1.3583 €) | — | 152.43 | 0.001 (n=6) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52926420 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 96.851354 USDC | 1.482124 USDC | 0.000000 USDC | 0.007331 USDC | 1.474793 USDC (1.3568 €) | — | 152.27 | 0.001 (n=8) | REJECTED | reliability_not_demonstrated |
| 52926420 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.039679 WETH | 0.000607 WETH | 0.000000 WETH | 0.000003 WETH | 0.000604 WETH (1.3561 €) | — | 152.27 | 0.001 (n=8) | REJECTED | reliability_not_demonstrated |
| 52926420 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 95.833376 USDC | 1.467664 USDC | 0.000000 USDC | 0.007331 USDC | 1.460333 USDC (1.3435 €) | — | 152.38 | 0.001 (n=6) | REJECTED | reliability_not_demonstrated |
| 52926420 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.039264 WETH | 0.000601 WETH | 0.000000 WETH | 0.000003 WETH | 0.000598 WETH (1.3429 €) | — | 152.38 | 0.001 (n=6) | REJECTED | reliability_not_demonstrated |
| 52926420 | WETH→[sushiswap_v3]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.038647 WETH | 0.000587 WETH | 0.000000 WETH | 0.000003 WETH | 0.000584 WETH (1.3117 €) | — | 151.23 | 0.001 (n=6) | REJECTED | reliability_not_demonstrated |
| 52926420 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[sushiswap_v3]→USDC | 94.264258 USDC | 1.432861 USDC | 0.000000 USDC | 0.007331 USDC | 1.425530 USDC (1.3115 €) | — | 151.23 | 0.001 (n=6) | REJECTED | reliability_not_demonstrated |
| 52926420 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.033525 WETH | 0.000512 WETH | 0.000000 WETH | 0.000003 WETH | 0.000509 WETH (1.1425 €) | — | 151.84 | 0.001 (n=6) | REJECTED | reliability_not_demonstrated |
| 52926420 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 81.476666 USDC | 1.244426 USDC | 0.000000 USDC | 0.007331 USDC | 1.237095 USDC (1.1381 €) | — | 151.83 | 0.001 (n=6) | REJECTED | reliability_not_demonstrated |
| 52926420 | WETH→[uniswap_v2]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.027497 WETH | 0.000411 WETH | 0.000000 WETH | 0.000003 WETH | 0.000408 WETH (0.9153 €) | — | 148.31 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52926420 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[uniswap_v2]→USDC | 66.896175 USDC | 0.998717 USDC | 0.000000 USDC | 0.006573 USDC | 0.992144 USDC (0.9128 €) | — | 148.31 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52926420 | WETH→[aerodrome]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.027984 WETH | 0.000406 WETH | 0.000000 WETH | 0.000003 WETH | 0.000403 WETH (0.9051 €) | — | 144.11 | 0.001 (n=8) | REJECTED | reliability_not_demonstrated |
| 52926420 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[aerodrome]→USDC | 68.078251 USDC | 0.988044 USDC | 0.000000 USDC | 0.006994 USDC | 0.981050 USDC (0.9026 €) | — | 144.11 | 0.001 (n=8) | REJECTED | reliability_not_demonstrated |
| 52926420 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.028077 WETH | 0.000400 WETH | 0.000000 WETH | 0.000003 WETH | 0.000397 WETH (0.8901 €) | — | 141.24 | 0.001 (n=6) | REJECTED | reliability_not_demonstrated |
| 52926420 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 68.290646 USDC | 0.971862 USDC | 0.000000 USDC | 0.007331 USDC | 0.964531 USDC (0.8874 €) | — | 141.24 | 0.001 (n=6) | REJECTED | reliability_not_demonstrated |
| 52930095 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 1.858903 WETH | 0.000324 WETH | 0.000000 WETH | 0.000003 WETH | 0.000321 WETH (0.7208 €) | — | 1.73 | 0.023 (n=61) | REJECTED | below_safety_margin(321454829860443<371780545622116), p_lower_below_threshold(0.02<0.75) |
| 52930096 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 1.858903 WETH | 0.000324 WETH | 0.000000 WETH | 0.000003 WETH | 0.000321 WETH (0.7208 €) | — | 1.73 | 0.023 (n=61) | REJECTED | below_safety_margin(321454829860443<371780545622116), p_lower_below_threshold(0.02<0.75) |
| 52930095 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 4,525.486380 USDC | 0.789243 USDC | 0.000000 USDC | 0.006220 USDC | 0.783023 USDC (0.7204 €) | — | 1.73 | 0.023 (n=61) | REJECTED | below_safety_margin(783023<905097), p_lower_below_threshold(0.02<0.75) |
| 52930096 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 4,525.486380 USDC | 0.789243 USDC | 0.000000 USDC | 0.006220 USDC | 0.783023 USDC (0.7204 €) | — | 1.73 | 0.023 (n=61) | REJECTED | below_safety_margin(783023<905097), p_lower_below_threshold(0.02<0.75) |
| 52926420 | WETH→[aerodrome]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.016828 WETH | 0.000252 WETH | 0.000000 WETH | 0.000003 WETH | 0.000249 WETH (0.5595 €) | — | 148.13 | 0.001 (n=8) | REJECTED | reliability_not_demonstrated |

## Fiabilité et décision
- Observations ghost : 1824 ; taux observé 0.095 ; borne inférieure crédible (0.9) 0.087 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 8.7% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
