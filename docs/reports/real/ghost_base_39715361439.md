# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-22T04:12:02+00:00 ; durée 55.7 min ; blocs 52924813 → 52926485 (1626 vus)

## Connexion
- Requêtes RPC : 20656 ; erreurs : 0 ; latence p50/p95 : 292.7/1,215.2 ms
- Rafraîchissements d'état : 1626 ; âge des données au dernier bloc : 2.58 s ; changements de frais LP observés (pools à frais dynamiques) : 2727
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 26577 ; cycles déclenchés par événement : 1477 ; avance médiane sur le rafraîchissement multicall : 481 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,439.54 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 566 pools, 325 jetons, 21116 routes
- Par DEX : uniswap_v3 137, aerodrome 233, aerodrome_slipstream 146, pancakeswap_v3 32, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 205 (rejetés 2) → 610 jetons ; pools candidats 3904 (énumérés 382, par paires 0), mesurés 569, sous le plancher de 10000.0 $ : 3 → gardés 566 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDbC': 1.0, 'USDC': 1.0, 'WETH': 2442.747144, 'AERO': 0.821241, 'cbBTC': 82764.497741}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 156,554,613 | 2,439.539816 | 52926485 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 25,202,573 | 1.221634 | 52926485 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| aerodrome | WETH/VVV | 3000 | 16,633,838 | 89.696689 | 52926485 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,387,303 | 0.029479 | 52926485 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,402,109 | 0.029406 | 52926485 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 9,730,912 | 0.029422 | 52926485 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,466,681 | 0.000012 | 52926485 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 8,746,561 | 2,442.059542 | 52926485 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/USDC | 3000 | 7,394,356 | 2,440.287403 | 52926485 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,252,833 | 0.001663 | 52926485 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 334 | 7,097,572 | 0.000012 | 52926485 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 150 | 6,549,303 | 2,441.209218 | 52926485 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | USDC/cbBTC | 412 | 5,982,282 | 0.000012 | 52926485 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,514,984 | 0.029480 | 52926485 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,603,705 | 2,441.240753 | 52926485 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,354,769 | 0.999956 | 52926485 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,079,632 | 0.000278 | 52926485 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome | WETH/KTA | 3000 | 4,042,613 | 34,538.187683 | 52926485 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDT | 415 | 2,893,122 | 2,444.866397 | 52926485 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome_slipstream | WETH/VVV | 2712 | 2,817,302 | 89.685904 | 52926485 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | WETH/AERO | 10000 | 2,486,339 | 2,976.966827 | 52926485 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,347,113 | 394.573667 | 52926485 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,258,627 | 0.000012 | 52926485 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | WETH/FAI | 10000 | 2,247,268 | 1,195,533.776576 | 52926485 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 2,090,155 | 0.000012 | 52926485 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,933,694 | 0.000000 | 52926485 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,794,817 | 0.018521 | 52926485 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome | weETH_04c0/WETH | 500 | 1,763,232 | 1.105712 | 52926485 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,703,434 | 1.495412 | 52926485 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | WETH/AERO | 3000 | 1,654,586 | 2,982.762893 | 52926485 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | WETH/msETH (stable) | 500 | 1,624,851 | 2.330575 | 52926485 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome | fBOMB/AERO | 10000 | 1,567,925 | 0.023325 | 52926485 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,474,716 | 13,393.005455 | 52926485 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,457,057 | 0.826101 | 52926485 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | WETH/wstETH | 90 | 1,379,579 | 0.802239 | 52926485 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,373,000 | 0.004862 | 52926485 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v3 | DRB/WETH | 10000 | 1,372,643 | 0.000000 | 52926485 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | USDC/alUSDb (stable) | 500 | 1,349,463 | 1.422897 | 52926485 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,327,372 | 0.000276 | 52926485 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,290,578 | 2,442.046680 | 52926485 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 1,266,107 | 0.000010 | 52926485 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | USDC/SEND | 3000 | 1,231,841 | 64.037314 | 52926485 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,227,900 | 16.215515 | 52926485 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | WETH/WELL | 10000 | 1,215,904 | 1,084,859.947440 | 52926485 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/doginme | 10000 | 1,212,152 | 35,537,147.729566 | 52926485 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | USDC/NOCK | 3000 | 1,185,711 | 44.814027 | 52926485 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,176,904 | 492,403.031955 | 52926485 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,155,075 | 23.136524 | 52926485 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| aerodrome | WETH/EDEL | 7000 | 1,151,640 | 71,974.493890 | 52926485 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | fBOMB/USDC | 10000 | 1,149,353 | 0.019226 | 52926485 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| uniswap_v2 | WETH/USDC | 3000 | 1,109,118 | 2,441.218038 | 52926485 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,086,703 | 21,166,261.097057 | 52926485 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | EURC/USDC | 73 | 1,074,048 | 1.124749 | 52926485 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| aerodrome | WETH/cbBTC | 3000 | 1,073,266 | 0.029411 | 52926485 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,068,662 | 0.915940 | 52926485 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,046,082 | 16.765919 | 52926485 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | USDC/VVV | 3000 | 997,060 | 0.036722 | 52926485 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome_slipstream | USDC/AERO | 10000 | 993,656 | 1.213958 | 52926485 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| uniswap_v3 | WETH/MORPHO | 3000 | 969,738 | 1,062.120917 | 52926485 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/USDC | 10000 | 936,238 | 2,456.787960 | 52926485 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |

## Recherche d'opportunités
- Cycles : 3102 ; routes examinées : 65501832 ; candidats optimisés : 410263 ; net attendu > 0 : 171 ; dernier cycle 305.2 ms
- Rejets (moteur) : {'spread_below_threshold': 64452502, 'liquidity_below_min': 634675, 'negative_expected_net': 410092, 'borrow_bound_too_small': 3102, 'cycle_budget_exhausted': 1290}
- Enregistrements de la session : 410263 ; net attendu > 0 : 171 ; simulés (eth_call de la vraie tx) : 4 (ok 0, échec 4) ; étiquettes ghost N+1 : 0/4 positives
- Décisions : {'REJECTED': 410263} ; motifs de rejet : {'below_safety_margin': 146, 'negative_expected_net': 410092, 'p_lower_below_threshold': 147, 'price_impact': 2, 'reliability_not_demonstrated': 24, 'simulation_failed': 4}

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
| 52926420 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.000410 WETH | 0.000008 WETH | 0.000000 WETH | 0.000003 WETH | 0.000005 WETH (0.0119 €) | — | 129.41 | 0.001 (n=6) | REJECTED | price_impact(161bps>150.0), reliability_not_demonstrated |
| 52926420 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 0.999999 USDC | 0.020271 USDC | 0.000000 USDC | 0.007331 USDC | 0.012940 USDC (0.0119 €) | — | 129.40 | 0.001 (n=6) | REJECTED | price_impact(161bps>150.0), reliability_not_demonstrated |
| 52925059 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 34.487994 USDC | 0.017827 USDC | 0.000000 USDC | 0.005511 USDC | 0.012316 USDC (0.0113 €) | — | 3.57 | 0.003 (n=101) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |

## Fiabilité et décision
- Observations ghost : 1802 ; taux observé 0.097 ; borne inférieure crédible (0.9) 0.088 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 8.8% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
