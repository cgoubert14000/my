# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-22T05:52:36+00:00 ; durée 156.26 min ; blocs 52924813 → 52929498 (4523 vus)

## Connexion
- Requêtes RPC : 56968 ; erreurs : 0 ; latence p50/p95 : 321.9/1,217.0 ms
- Rafraîchissements d'état : 4523 ; âge des données au dernier bloc : 5.13 s ; changements de frais LP observés (pools à frais dynamiques) : 7010
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 66545 ; cycles déclenchés par événement : 4033 ; avance médiane sur le rafraîchissement multicall : 849 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,439.53 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 566 pools, 325 jetons, 21116 routes
- Par DEX : uniswap_v3 137, aerodrome 233, aerodrome_slipstream 146, pancakeswap_v3 32, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 205 (rejetés 2) → 610 jetons ; pools candidats 3904 (énumérés 382, par paires 0), mesurés 569, sous le plancher de 10000.0 $ : 3 → gardés 566 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDbC': 1.0, 'USDC': 1.0, 'WETH': 2442.747144, 'AERO': 0.821241, 'cbBTC': 82764.497741}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 156,585,275 | 2,439.526615 | 52929499 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 24,741,338 | 1.224763 | 52929499 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| aerodrome | WETH/VVV | 3000 | 16,707,587 | 88.901432 | 52929499 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,407,982 | 0.029454 | 52929499 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,405,208 | 0.029433 | 52929499 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 9,715,094 | 0.029448 | 52929499 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,466,821 | 0.000012 | 52929499 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 8,742,161 | 2,434.466753 | 52929499 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/USDC | 3000 | 7,393,476 | 2,438.727662 | 52929499 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,245,120 | 0.001657 | 52929499 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 344 | 7,079,514 | 0.000012 | 52929499 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 639 | 6,295,058 | 2,434.132091 | 52929499 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | USDC/cbBTC | 472 | 5,764,817 | 0.000012 | 52929499 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,516,783 | 0.029449 | 52929499 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,613,660 | 2,433.960634 | 52929499 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,357,831 | 1.000000 | 52929499 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,069,977 | 0.000277 | 52929499 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome | WETH/KTA | 3000 | 4,048,977 | 34,429.325842 | 52929499 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDT | 418 | 2,890,835 | 2,437.881483 | 52929499 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome_slipstream | WETH/VVV | 2793 | 2,653,711 | 88.923822 | 52929499 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | WETH/AERO | 10000 | 2,479,569 | 2,966.422879 | 52929499 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,346,293 | 394.929905 | 52929499 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,258,831 | 0.000012 | 52929499 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | WETH/FAI | 10000 | 2,247,324 | 1,195,461.313975 | 52929499 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 2,091,597 | 0.000012 | 52929499 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,932,632 | 0.000000 | 52929499 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,792,065 | 0.018478 | 52929499 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome | weETH_04c0/WETH | 500 | 1,763,203 | 1.105687 | 52929499 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,703,434 | 1.495412 | 52929499 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | WETH/AERO | 3000 | 1,653,164 | 2,986.636259 | 52929499 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | WETH/msETH (stable) | 500 | 1,614,578 | 2.339222 | 52929499 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome | fBOMB/AERO | 10000 | 1,548,471 | 0.023271 | 52929499 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,476,614 | 13,398.586979 | 52929499 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,457,063 | 0.826095 | 52929499 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | WETH/wstETH | 90 | 1,379,409 | 0.802239 | 52929499 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,372,644 | 0.004860 | 52929499 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v3 | DRB/WETH | 10000 | 1,371,082 | 0.000000 | 52929499 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | USDC/alUSDb (stable) | 500 | 1,349,052 | 1.422897 | 52929499 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,324,359 | 0.000275 | 52929499 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,301,758 | 2,434.470190 | 52929499 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 1,255,438 | 0.000010 | 52929499 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | USDC/SEND | 3000 | 1,231,841 | 64.037314 | 52929499 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,215,668 | 16.239549 | 52929499 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | WETH/WELL | 10000 | 1,215,665 | 1,085,275.394154 | 52929499 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/doginme | 10000 | 1,211,546 | 35,590,922.572187 | 52929499 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | USDC/NOCK | 3000 | 1,186,022 | 44.790491 | 52929499 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,165,332 | 495,838.066544 | 52929499 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | WETH/EDEL | 7000 | 1,155,969 | 71,435.561638 | 52929499 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | fBOMB/USDC | 10000 | 1,131,756 | 0.018985 | 52929499 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| uniswap_v2 | WETH/USDC | 3000 | 1,109,121 | 2,440.812459 | 52929499 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,084,510 | 21,240,255.844829 | 52929499 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | EURC/USDC | 76 | 1,073,389 | 1.124674 | 52929499 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,068,443 | 0.915940 | 52929499 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| aerodrome | WETH/cbBTC | 3000 | 1,065,358 | 0.029526 | 52929499 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,046,917 | 23.246715 | 52929499 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,043,920 | 16.859534 | 52929499 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | USDC/VVV | 3000 | 1,004,592 | 0.036530 | 52929499 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/MORPHO | 3000 | 973,324 | 1,061.336925 | 52929499 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/USDC | 10000 | 936,226 | 2,456.787960 | 52929499 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | uXRP/WETH | 3000 | 930,539 | 0.000549 | 52929499 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |

## Recherche d'opportunités
- Cycles : 8555 ; routes examinées : 180647380 ; candidats optimisés : 1102401 ; net attendu > 0 : 230 ; dernier cycle 139.5 ms
- Rejets (moteur) : {'spread_below_threshold': 178001817, 'liquidity_below_min': 1532813, 'negative_expected_net': 1102171, 'borrow_bound_too_small': 8555, 'cycle_budget_exhausted': 1794}
- Enregistrements de la session : 1102401 ; net attendu > 0 : 230 ; simulés (eth_call de la vraie tx) : 15 (ok 1, échec 14) ; étiquettes ghost N+1 : 0/14 positives
- Décisions : {'REJECTED': 1102401} ; motifs de rejet : {'below_safety_margin': 188, 'negative_expected_net': 1102171, 'p_lower_below_threshold': 197, 'price_impact': 2, 'reliability_not_demonstrated': 33, 'simulation_failed': 14}

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
| 52926420 | WETH→[aerodrome]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.016828 WETH | 0.000252 WETH | 0.000000 WETH | 0.000003 WETH | 0.000249 WETH (0.5595 €) | — | 148.13 | 0.001 (n=8) | REJECTED | reliability_not_demonstrated |
| 52926420 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[aerodrome]→USDC | 40.503833 USDC | 0.606878 USDC | 0.000000 USDC | 0.006994 USDC | 0.599884 USDC (0.5519 €) | — | 148.11 | 0.001 (n=8) | REJECTED | reliability_not_demonstrated |
| 52929044 | WETH→[aerodrome_slipstream]→VIRTUAL→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.078978 WETH | 0.000039 WETH | 0.000000 WETH | 0.000003 WETH | 0.000036 WETH (0.0809 €) | — | 4.57 | 0.104 (n=172) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.10<0.75) |
| 52929044 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→VIRTUAL→[pancakeswap_v3]→USDC | 193.158157 USDC | 0.095289 USDC | 0.000000 USDC | 0.007332 USDC | 0.087957 USDC (0.0809 €) | — | 4.55 | 0.104 (n=172) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 52929044 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→VIRTUAL→[pancakeswap_v3]→USDC | 179.857186 USDC | 0.088817 USDC | 0.000000 USDC | 0.007332 USDC | 0.081485 USDC (0.0750 €) | — | 4.53 | 0.104 (n=172) | REJECTED | p_lower_below_threshold(0.10<0.75) |

## Fiabilité et décision
- Observations ghost : 1812 ; taux observé 0.096 ; borne inférieure crédible (0.9) 0.087 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 8.7% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
