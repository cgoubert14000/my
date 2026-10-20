# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-20T04:42:29+00:00 ; durée 251.83 min ; blocs 52833443 → 52840995 (7350 vus)

## Connexion
- Requêtes RPC : 103219 ; erreurs : 125 ; latence p50/p95 : 171.0/822.9 ms
- Rafraîchissements d'état : 7351 ; âge des données au dernier bloc : 0.66 s ; changements de frais LP observés (pools à frais dynamiques) : 16016
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 141286 ; cycles déclenchés par événement : 8882 ; avance médiane sur le rafraîchissement multicall : 340 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,407.76 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 572 pools, 327 jetons, 21078 routes
- Par DEX : uniswap_v3 136, aerodrome 234, aerodrome_slipstream 155, pancakeswap_v3 30, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 207 (rejetés 2) → 612 jetons ; pools candidats 3877 (énumérés 391, par paires 0), mesurés 575, sous le plancher de 10000.0 $ : 3 → gardés 572 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDC': 1.0, 'USDbC': 1.0, 'WETH': 2396.875305, 'AERO': 0.785623, 'cbBTC': 81488.469771}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 146,598,577 | 2,407.758638 | 52840995 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 34,519,328 | 1.235662 | 52840995 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 500 | 18,225,844 | 0.029390 | 52840995 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 17,536,244 | 97.434527 | 52840995 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 11,235,844 | 0.029339 | 52840995 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,394,920 | 0.029323 | 52840995 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,882,929 | 0.000012 | 52840995 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome_slipstream | USDC/cbBTC | 436 | 8,782,838 | 0.000012 | 52840995 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | WETH/USDC | 500 | 8,369,045 | 2,410.728654 | 52840995 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/USDC | 3000 | 8,318,079 | 2,408.123666 | 52840995 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | USDC/cbBTC | 336 | 7,831,527 | 0.000012 | 52840995 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 564 | 7,456,675 | 2,411.312035 | 52840995 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,202,306 | 0.001674 | 52840995 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,360,155 | 0.029402 | 52840995 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/USDT | 400 | 5,052,773 | 2,414.118487 | 52840995 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome | fBOMB/AERO | 10000 | 4,984,090 | 0.025578 | 52840995 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,796,966 | 0.802395 | 52840995 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,644,289 | 0.000275 | 52840995 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,482,206 | 2,411.388771 | 52840995 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | USDC/AERO | 10000 | 4,383,474 | 1.238258 | 52840995 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,341,467 | 0.998768 | 52840995 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 4,035,032 | 33,771.911293 | 52840995 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/AERO | 10000 | 3,262,890 | 2,982.723586 | 52840995 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,878,048 | 0.000012 | 52840995 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,754,757 | 1.142105 | 52840995 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| aerodrome_slipstream | WETH/VVV | 2700 | 2,670,496 | 97.448808 | 52840995 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,383,428 | 400.068229 | 52840995 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 2,235,071 | 0.000010 | 52840995 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | WETH/FAI | 10000 | 2,193,495 | 1,223,150.560610 | 52840995 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,059,504 | 1.238011 | 52840995 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,036,017 | 1.373596 | 52840995 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,978,375 | 0.000000 | 52840995 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,960,609 | 15.882600 | 52840995 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| uniswap_v3 | XDP/USDC | 100 | 1,801,619 | 0.019232 | 52840995 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,770,886 | 0.000012 | 52840995 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,762,616 | 13,604.537040 | 52840995 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | weETH_04c0/WETH | 500 | 1,742,090 | 1.105525 | 52840995 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome_slipstream | EURC/USDC | 70 | 1,728,996 | 1.123140 | 52840995 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| aerodrome | fBOMB/USDC | 10000 | 1,677,993 | 0.020331 | 52840995 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| aerodrome | WETH/msETH (stable) | 500 | 1,658,771 | 2.307691 | 52840995 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,559,543 | 0.916343 | 52840995 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| uniswap_v3 | WETH/AERO | 3000 | 1,514,790 | 2,983.918803 | 52840995 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,458,561 | 0.826524 | 52840995 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | DRB/WETH | 10000 | 1,309,285 | 0.000000 | 52840995 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,306,115 | 0.004702 | 52840995 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,302,026 | 0.000277 | 52840995 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | WETH/cbBTC | 3000 | 1,286,704 | 0.029321 | 52840995 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| aerodrome | WETH/WELL | 10000 | 1,258,498 | 992,444.044663 | 52840995 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,250,896 | 2,410.782922 | 52840995 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,230,445 | 64.182807 | 52840995 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,207,275 | 22.980595 | 52840995 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| uniswap_v3 | WETH/doginme | 10000 | 1,198,573 | 35,393,340.558692 | 52840995 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,168,296 | 0.435976 | 52840995 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,143,872 | 511,519.337817 | 52840995 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome_slipstream | msUSD/USDC | 500 | 1,135,945 | 0.885710 | 52840995 | `0x7501bc8Bb51616F79bfA524E464fb7B41f0B10fB` |
| aerodrome_slipstream | WETH/msETH | 500 | 1,115,111 | 1.131792 | 52840995 | `0x74F72788F4814D7fF3C49B44684aa98Eee140C0E` |
| aerodrome | USDC/NOCK | 3000 | 1,095,192 | 52.532010 | 52840995 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome | WETH/EDEL | 7000 | 1,089,573 | 84,246.577315 | 52840995 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,076,364 | 15.565137 | 52840995 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome_slipstream | USDC/USDT | 8 | 1,074,363 | 1.001408 | 52840995 | `0xa41Bc0AFfbA7Fd420d186b84899d7ab2aC57fcD1` |

## Recherche d'opportunités
- Cycles : 16232 ; routes examinées : 342138096 ; candidats optimisés : 2005196 ; net attendu > 0 : 544 ; dernier cycle 186.3 ms
- Rejets (moteur) : {'spread_below_threshold': 336871337, 'liquidity_below_min': 2760807, 'negative_expected_net': 2004652, 'borrow_bound_too_small': 405766, 'pool_quarantined': 91780, 'cycle_budget_exhausted': 3150}
- Enregistrements de la session : 2005192 ; net attendu > 0 : 544 ; simulés (eth_call de la vraie tx) : 49 (ok 17, échec 32) ; étiquettes ghost N+1 : 3/34 positives
- Décisions : {'REJECTED': 2005192} ; motifs de rejet : {'below_safety_margin': 327, 'negative_expected_net': 2004648, 'p_lower_below_threshold': 426, 'price_impact': 8, 'reliability_not_demonstrated': 118, 'sim_below_estimate': 2, 'simulated_net_nonpositive': 2, 'simulation_failed': 32}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52837704 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 2,357.403929 USDC | 1.618250 USDC | 0.000000 USDC | 0.007212 USDC | 1.611038 USDC (1.4822 €) | — | 6.83 | 0.000 (n=88) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 52837704 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.983362 WETH | 0.000675 WETH | 0.000000 WETH | 0.000003 WETH | 0.000672 WETH (1.4812 €) | — | 6.83 | 0.000 (n=88) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 52837704 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 1,960.783478 USDC | 1.243120 USDC | 0.000000 USDC | 0.009035 USDC | 1.234085 USDC (1.1354 €) | — | 6.29 | 0.115 (n=117) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52837704 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.826484 WETH | 0.000518 WETH | 0.000000 WETH | 0.000004 WETH | 0.000515 WETH (1.1345 €) | — | 6.23 | 0.115 (n=117) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.12<0.75) |
| 52837704 | cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.023970 cbBTC | 0.000015 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000015 cbBTC (1.1341 €) | — | 6.30 | 0.115 (n=117) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52839614 | USDC→[aerodrome_slipstream]→USDbC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 281.209092 USDC | 0.969297 USDC | 0.000000 USDC | 0.009435 USDC | 0.959862 USDC (0.8831 €) | — | 34.13 | 0.001 (n=8) | REJECTED | reliability_not_demonstrated |
| 52839614 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→USDbC→[uniswap_v3]→WETH | 0.116721 WETH | 0.000402 WETH | 0.000000 WETH | 0.000004 WETH | 0.000398 WETH (0.8810 €) | — | 34.12 | 0.001 (n=8) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52839614 | USDC→[aerodrome_slipstream]→USDbC→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 276.030520 USDC | 0.950791 USDC | 0.000000 USDC | 0.009435 USDC | 0.941356 USDC (0.8660 €) | — | 34.10 | 0.001 (n=7) | REJECTED | reliability_not_demonstrated |
| 52839614 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→USDbC→[uniswap_v3]→WETH | 0.114583 WETH | 0.000395 WETH | 0.000000 WETH | 0.000004 WETH | 0.000391 WETH (0.8641 €) | — | 34.09 | 0.001 (n=7) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52839614 | USDC→[aerodrome_slipstream]→USDbC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 266.947343 USDC | 0.870907 USDC | 0.000000 USDC | 0.009435 USDC | 0.861472 USDC (0.7926 €) | — | 32.27 | 0.001 (n=7) | REJECTED | reliability_not_demonstrated |
| 52839614 | WETH→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→USDbC→[uniswap_v3]→WETH | 0.110831 WETH | 0.000361 WETH | 0.000000 WETH | 0.000004 WETH | 0.000358 WETH (0.7910 €) | — | 32.26 | 0.001 (n=7) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52837704 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 1,805.192585 USDC | 0.866038 USDC | 0.000000 USDC | 0.006484 USDC | 0.859554 USDC (0.7908 €) | — | 4.76 | 0.090 (n=24) | REJECTED | reliability_not_demonstrated |
| 52837704 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.753626 WETH | 0.000361 WETH | 0.000000 WETH | 0.000003 WETH | 0.000358 WETH (0.7900 €) | — | 4.75 | 0.090 (n=24) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52839614 | USDC→[aerodrome_slipstream]→USDbC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 265.497558 USDC | 0.865712 USDC | 0.000000 USDC | 0.009435 USDC | 0.856277 USDC (0.7878 €) | — | 32.25 | 0.001 (n=8) | REJECTED | reliability_not_demonstrated |
| 52839614 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→USDbC→[uniswap_v3]→WETH | 0.110229 WETH | 0.000359 WETH | 0.000000 WETH | 0.000004 WETH | 0.000355 WETH (0.7862 €) | — | 32.24 | 0.001 (n=8) | REJECTED | reliability_not_demonstrated |
| 52839614 | USDC→[aerodrome_slipstream]→USDbC→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 259.687658 USDC | 0.823189 USDC | 0.000000 USDC | 0.009435 USDC | 0.813754 USDC (0.7487 €) | — | 31.34 | 0.001 (n=7) | REJECTED | reliability_not_demonstrated |
| 52839614 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→USDbC→[uniswap_v3]→WETH | 0.107888 WETH | 0.000342 WETH | 0.000000 WETH | 0.000004 WETH | 0.000338 WETH (0.7473 €) | — | 31.31 | 0.001 (n=7) | REJECTED | reliability_not_demonstrated |
| 52839614 | USDC→[aerodrome_slipstream]→USDbC→[uniswap_v3]→WETH→[sushiswap_v3]→USDC | 220.265262 USDC | 0.707567 USDC | 0.000000 USDC | 0.009435 USDC | 0.698132 USDC (0.6423 €) | — | 31.70 | 0.001 (n=7) | REJECTED | reliability_not_demonstrated |
| 52839614 | WETH→[sushiswap_v3]→USDC→[aerodrome_slipstream]→USDbC→[uniswap_v3]→WETH | 0.091535 WETH | 0.000294 WETH | 0.000000 WETH | 0.000004 WETH | 0.000290 WETH (0.6417 €) | — | 31.69 | 0.001 (n=7) | REJECTED | reliability_not_demonstrated |
| 52837704 | USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 1,463.962719 USDC | 0.563106 USDC | 0.000000 USDC | 0.008307 USDC | 0.554799 USDC (0.5104 €) | — | 3.79 | 0.145 (n=70) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 52837704 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH | 0.611402 WETH | 0.000235 WETH | 0.000000 WETH | 0.000003 WETH | 0.000231 WETH (0.5098 €) | — | 3.78 | 0.145 (n=70) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 52836654 | USDC→[aerodrome]→AERO→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 795.067478 USDC | 0.558489 USDC | 0.000000 USDC | 0.007237 USDC | 0.551252 USDC (0.5072 €) | — | 6.93 | 0.009 (n=33) | REJECTED | p_lower_below_threshold(0.01<0.75) |
| 52836654 | WETH→[pancakeswap_v3]→USDC→[aerodrome]→AERO→[pancakeswap_v3]→WETH | 0.332070 WETH | 0.000233 WETH | 0.000000 WETH | 0.000003 WETH | 0.000230 WETH (0.5068 €) | 0.000230 WETH | 6.93 | 0.009 (n=33) | REJECTED | p_lower_below_threshold(0.01<0.75) |
| 52837704 | USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 1,331.486427 USDC | 0.526924 USDC | 0.000000 USDC | 0.008307 USDC | 0.518617 USDC (0.4771 €) | — | 3.90 | 0.115 (n=117) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52837704 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.554679 WETH | 0.000220 WETH | 0.000000 WETH | 0.000003 WETH | 0.000216 WETH (0.4765 €) | — | 3.90 | 0.115 (n=117) | REJECTED | p_lower_below_threshold(0.12<0.75) |

## Fiabilité et décision
- Observations ghost : 1370 ; taux observé 0.103 ; borne inférieure crédible (0.9) 0.093 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 9.3% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
