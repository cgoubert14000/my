# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-18T19:54:45+00:00 ; durée 319.27 min ; blocs 52772387 → 52781963 (9363 vus)

## Connexion
- Requêtes RPC : 110168 ; erreurs : 5 ; latence p50/p95 : 297.7/1,779.8 ms
- Rafraîchissements d'état : 9364 ; âge des données au dernier bloc : 1.85 s ; changements de frais LP observés (pools à frais dynamiques) : 21590
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 4312 ; cycles déclenchés par événement : 200 ; avance médiane sur le rafraîchissement multicall : 636 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,338.09 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 574 pools, 327 jetons, 21464 routes
- Par DEX : uniswap_v3 136, aerodrome 233 (quarantaine 2), aerodrome_slipstream 155, pancakeswap_v3 32, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 206 (rejetés 2) → 611 jetons ; pools candidats 3914 (énumérés 390, par paires 0), mesurés 576, sous le plancher de 10000.0 $ : 2 → gardés 574 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2372.774214, 'AERO': 0.799025, 'cbBTC': 81081.426767}
- Pools en quarantaine : 2 — aerodrome:fBOMB/AERO@0xbBf71A: simulation failed ×5 (model/chain mismatch) — until block 52782013; aerodrome:fBOMB/USDC@0xFf8e0b: simulation failed ×5 (model/chain mismatch) — until block 52781980

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 144,071,593 | 2,338.086373 | 52781963 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 40,541,995 | 1.289018 | 52781963 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 500 | 17,694,499 | 0.028908 | 52781963 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 16,041,508 | 109.739189 | 52781963 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| aerodrome_slipstream | WETH/cbBTC | 2505 | 11,791,065 | 0.028905 | 52781963 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,121,526 | 0.028915 | 52781963 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,717,345 | 0.000012 | 52781963 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 8,179,888 | 2,336.206776 | 52781963 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome_slipstream | USDC/cbBTC | 334 | 7,814,009 | 0.000012 | 52781963 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | USDC/cbBTC | 412 | 7,034,836 | 0.000012 | 52781963 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,016,015 | 0.001629 | 52781963 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | WETH/USDC | 150 | 6,819,994 | 2,336.893336 | 52781963 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome | WETH/USDC | 3000 | 5,392,320 | 2,338.437733 | 52781963 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | USDC/AERO | 10000 | 5,326,056 | 1.287392 | 52781963 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,126,508 | 0.028911 | 52781963 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/superOETHb | 400 | 5,077,320 | 1.000854 | 52781963 | `0x6446021F4E396dA3df4235C62537431372195D38` |
| aerodrome | fBOMB/AERO | 10000 | 4,858,537 | 0.026109 | 52781963 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,673,535 | 0.802398 | 52781963 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,466,683 | 0.000269 | 52781963 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,358,089 | 2,337.087551 | 52781963 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,306,023 | 0.998069 | 52781963 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,954,457 | 33,156.661001 | 52781963 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/AERO | 10000 | 3,175,014 | 3,003.190229 | 52781963 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | WETH/USDT | 436 | 3,005,142 | 2,340.152446 | 52781963 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,828,313 | 0.000012 | 52781963 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,817,652 | 1.141832 | 52781963 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| aerodrome_slipstream | AERO/cbBTC | 2700 | 2,480,394 | 0.000010 | 52781963 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,465,844 | 415.935623 | 52781963 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | WETH/VVV | 2721 | 2,433,184 | 109.713931 | 52781963 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 2,402,555 | 1,027.129176 | 52781963 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome | WETH/FAI | 10000 | 2,144,689 | 1,206,478.919535 | 52781963 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,065,785 | 1.233147 | 52781963 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,036,703 | 1.372655 | 52781963 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,944,885 | 0.000000 | 52781963 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome_slipstream | EURC/USDC | 70 | 1,933,281 | 1.122455 | 52781963 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,870,754 | 15.909684 | 52781963 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | fBOMB/USDC | 10000 | 1,777,246 | 0.020721 | 52781963 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,759,055 | 0.000012 | 52781963 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | XDP/USDC | 100 | 1,730,486 | 0.017980 | 52781963 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome | weETH_04c0/WETH | 500 | 1,690,691 | 1.105523 | 52781963 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,656,063 | 14,384.140067 | 52781963 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/msETH (stable) | 500 | 1,621,251 | 2.301885 | 52781963 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,455,921 | 0.826769 | 52781963 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,434,286 | 3,019.204742 | 52781963 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,418,543 | 0.916353 | 52781963 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,317,780 | 0.434746 | 52781963 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,285,947 | 0.000000 | 52781963 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,251,967 | 0.000268 | 52781963 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | WETH/cbBTC | 3000 | 1,242,929 | 0.028920 | 52781963 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,233,297 | 0.004546 | 52781963 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome | USDC/SEND | 3000 | 1,233,273 | 63.888794 | 52781963 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome_slipstream | WETH/msETH | 500 | 1,228,567 | 1.130602 | 52781963 | `0x74F72788F4814D7fF3C49B44684aa98Eee140C0E` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,217,123 | 23.234008 | 52781963 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,184,489 | 2,336.375379 | 52781963 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | WETH/doginme | 10000 | 1,177,261 | 34,107,681.991808 | 52781963 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | WETH/WELL | 10000 | 1,124,014 | 1,173,149.213795 | 52781963 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,095,045 | 532,458.626616 | 52781963 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,073,993 | 15.642194 | 52781963 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | USDC/NOCK | 3000 | 1,067,694 | 55.276609 | 52781963 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | msUSD/USDC | 503 | 1,027,495 | 0.884748 | 52781963 | `0x7501bc8Bb51616F79bfA524E464fb7B41f0B10fB` |

## Recherche d'opportunités
- Cycles : 9563 ; routes examinées : 205260232 ; candidats optimisés : 1177896 ; net attendu > 0 : 626 ; dernier cycle 357.8 ms
- Rejets (moteur) : {'spread_below_threshold': 201179995, 'liquidity_below_min': 2009408, 'negative_expected_net': 1177270, 'pool_quarantined': 858006, 'cycle_budget_exhausted': 25378, 'borrow_bound_too_small': 9549}
- Enregistrements de la session : 1177896 ; net attendu > 0 : 626 ; simulés (eth_call de la vraie tx) : 170 (ok 22, échec 148) ; étiquettes ghost N+1 : 8/101 positives
- Décisions : {'REJECTED': 1177896} ; motifs de rejet : {'below_safety_margin': 384, 'negative_expected_net': 1177270, 'p_lower_below_threshold': 547, 'price_impact': 331, 'reliability_not_demonstrated': 79, 'sim_below_estimate': 3, 'simulated_net_nonpositive': 2, 'simulation_failed': 148, 'stale_data': 20}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52781506 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→uSOL→[aerodrome_slipstream]→cbBTC | 0.003356 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1117 €) | — | 4.47 | 0.128 (n=92) | REJECTED | p_lower_below_threshold(0.13<0.75) |
| 52781506 | WETH→[aerodrome_slipstream]→uSOL→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.125384 WETH | 0.000055 WETH | 0.000000 WETH | 0.000003 WETH | 0.000052 WETH (0.1117 €) | 0.000052 WETH | 4.13 | 0.128 (n=92) | REJECTED | p_lower_below_threshold(0.13<0.75) |
| 52772457 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→AERO→[pancakeswap_v3]→WETH | 0.157042 WETH | 0.000051 WETH | 0.000000 WETH | 0.000003 WETH | 0.000048 WETH (0.1050 €) | — | 3.06 | 0.128 (n=86) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.13<0.75) |
| 52772457 | cbBTC→[aerodrome_slipstream]→AERO→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.004218 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.1044 €) | — | 3.32 | 0.128 (n=86) | REJECTED | p_lower_below_threshold(0.13<0.75) |
| 52781506 | cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→uSOL→[aerodrome_slipstream]→cbBTC | 0.002976 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0976 €) | — | 4.40 | 0.128 (n=92) | REJECTED | p_lower_below_threshold(0.13<0.75) |
| 52781506 | WETH→[uniswap_v3]→uSOL→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.106404 WETH | 0.000048 WETH | 0.000000 WETH | 0.000003 WETH | 0.000045 WETH (0.0975 €) | 0.000045 WETH | 4.25 | 0.128 (n=92) | REJECTED | p_lower_below_threshold(0.13<0.75) |
| 52772400 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 459.130293 USDC | 0.098558 USDC | 0.000000 USDC | 0.005706 USDC | 0.092852 USDC (0.0854 €) | — | 2.02 | 0.020 (n=40) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.02<0.75) |
| 52772400 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.193596 WETH | 0.000042 WETH | 0.000000 WETH | 0.000002 WETH | 0.000039 WETH (0.0854 €) | — | 2.02 | 0.020 (n=40) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.02<0.75) |
| 52772457 | cbBTC→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→USDC→[uniswap_v3]→cbBTC | 0.003328 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0678 €) | — | 2.73 | 0.311 (n=62) | REJECTED | p_lower_below_threshold(0.31<0.75) |
| 52772457 | USDC→[uniswap_v3]→cbBTC→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→USDC | 278.506660 USDC | 0.080302 USDC | 0.000000 USDC | 0.007158 USDC | 0.073144 USDC (0.0673 €) | — | 2.63 | 0.311 (n=62) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.31<0.75) |
| 52772457 | cbBTC→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→cbBTC | 0.003359 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0663 €) | — | 2.65 | 0.311 (n=62) | REJECTED | p_lower_below_threshold(0.31<0.75) |
| 52772457 | USDC→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→USDC | 272.352625 USDC | 0.078563 USDC | 0.000000 USDC | 0.007158 USDC | 0.071405 USDC (0.0657 €) | — | 2.62 | 0.311 (n=62) | REJECTED | p_lower_below_threshold(0.31<0.75) |
| 52772457 | cbBTC→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→cbBTC | 0.003111 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0589 €) | — | 2.54 | 0.311 (n=62) | REJECTED | stale_data(4022ms>4000.0), p_lower_below_threshold(0.31<0.75) |
| 52772457 | USDC→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→USDC | 272.370781 USDC | 0.070961 USDC | 0.000000 USDC | 0.007158 USDC | 0.063803 USDC (0.0587 €) | — | 2.34 | 0.311 (n=62) | REJECTED | stale_data(4015ms>4000.0), p_lower_below_threshold(0.31<0.75) |
| 52772457 | cbBTC→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.003110 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0581 €) | — | 2.51 | 0.124 (n=109) | REJECTED | stale_data(4009ms>4000.0), p_lower_below_threshold(0.12<0.75) |
| 52772457 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→USDC | 257.401804 USDC | 0.070287 USDC | 0.000000 USDC | 0.007158 USDC | 0.063129 USDC (0.0581 €) | — | 2.45 | 0.124 (n=109) | REJECTED | stale_data(4002ms>4000.0), p_lower_below_threshold(0.12<0.75) |
| 52781506 | WETH→[aerodrome_slipstream]→oUSDT→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.062179 WETH | 0.000029 WETH | 0.000000 WETH | 0.000003 WETH | 0.000025 WETH (0.0547 €) | 0.000025 WETH | 4.08 | 0.128 (n=92) | REJECTED | p_lower_below_threshold(0.13<0.75) |
| 52781506 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→oUSDT→[aerodrome_slipstream]→cbBTC | 0.001648 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0544 €) | — | 4.43 | 0.128 (n=92) | REJECTED | p_lower_below_threshold(0.13<0.75) |
| 52772457 | WETH→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→AERO→[pancakeswap_v3]→WETH | 0.075109 WETH | 0.000028 WETH | 0.000000 WETH | 0.000003 WETH | 0.000025 WETH (0.0538 €) | — | 3.28 | 0.128 (n=86) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.13<0.75) |
| 52772457 | cbBTC→[aerodrome_slipstream]→AERO→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→cbBTC | 0.002046 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0537 €) | — | 3.52 | 0.128 (n=86) | REJECTED | p_lower_below_threshold(0.13<0.75) |
| 52781506 | WETH→[aerodrome_slipstream]→uSOL→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→WETH | 0.064907 WETH | 0.000025 WETH | 0.000000 WETH | 0.000003 WETH | 0.000022 WETH (0.0466 €) | — | 3.33 | 0.177 (n=53) | REJECTED | p_lower_below_threshold(0.18<0.75) |
| 52781506 | cbBTC→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→uSOL→[aerodrome_slipstream]→cbBTC | 0.001685 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0462 €) | — | 3.68 | 0.177 (n=53) | REJECTED | p_lower_below_threshold(0.18<0.75) |
| 52781506 | WETH→[uniswap_v3]→uSOL→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→WETH | 0.060965 WETH | 0.000023 WETH | 0.000000 WETH | 0.000003 WETH | 0.000020 WETH (0.0434 €) | — | 3.30 | 0.177 (n=53) | REJECTED | p_lower_below_threshold(0.18<0.75) |
| 52781506 | cbBTC→[aerodrome_slipstream]→WETH→[uniswap_v3]→uSOL→[aerodrome_slipstream]→cbBTC | 0.001582 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0432 €) | — | 3.67 | 0.177 (n=53) | REJECTED | p_lower_below_threshold(0.18<0.75) |
| 52781699 | WETH→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.377937 WETH | 0.000022 WETH | 0.000000 WETH | 0.000003 WETH | 0.000019 WETH (0.0418 €) | — | 0.51 | 0.019 (n=43) | REJECTED | below_safety_margin(19454906321013<75587332978084), p_lower_below_threshold(0.02<0.75) |

## Fiabilité et décision
- Observations ghost : 1066 ; taux observé 0.114 ; borne inférieure crédible (0.9) 0.102 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 10.2% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
