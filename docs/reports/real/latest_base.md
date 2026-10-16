# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-16T13:26:20+00:00 ; durée 93.11 min ; blocs 52681120 → 52683912 (2661 vus)

## Connexion
- Requêtes RPC : 36527 ; erreurs : 45 ; latence p50/p95 : 104.3/1,278.5 ms
- Rafraîchissements d'état : 2661 ; âge des données au dernier bloc : 5.1 s ; changements de frais LP observés (pools à frais dynamiques) : 6122
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 51857 ; cycles déclenchés par événement : 2454 ; avance médiane sur le rafraîchissement multicall : 1,230 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,463.54 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 575 pools, 328 jetons, 21482 routes
- Par DEX : uniswap_v3 136, aerodrome 236 (quarantaine 3), aerodrome_slipstream 153 (quarantaine 1), pancakeswap_v3 32, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 209 (rejetés 2) → 614 jetons ; pools candidats 3925 (énumérés 391, par paires 0), mesurés 577, sous le plancher de 10000.0 $ : 2 → gardés 575 (max 1500) ; prix des hubs : {'USDC': 1.0, 'DAI': 1.0, 'USDbC': 1.0, 'WETH': 2482.328501, 'AERO': 0.918334, 'cbBTC': 82582.444221}
- Pools en quarantaine : 4 — aerodrome:fBOMB/AERO@0xbBf71A: simulation failed ×5 (model/chain mismatch) — until block 52684202; aerodrome:fBOMB/USDC@0xFf8e0b: simulation failed ×5 (model/chain mismatch) — until block 52684202; aerodrome:VIRTUAL/cbBTC@0xb909F5: simulation failed ×5 (model/chain mismatch) — until block 52683920; aerodrome_slipstream:VIRTUAL/WETH@0x3f0296: simulation failed ×5 (model/chain mismatch) — until block 52683920

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 147,780,834 | 2,463.537735 | 52683912 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 46,846,418 | 1.097795 | 52683912 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 500 | 18,596,986 | 0.030047 | 52683912 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 16,981,381 | 0.030036 | 52683912 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/VVV | 3000 | 16,575,491 | 101.253407 | 52683912 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,556,353 | 0.030047 | 52683912 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,743,982 | 0.000012 | 52683912 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 9,182,578 | 2,461.580655 | 52683912 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome_slipstream | WETH/USDC | 579 | 8,402,112 | 2,462.034650 | 52683912 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | USDC/cbBTC | 336 | 7,853,101 | 0.000012 | 52683912 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | USDC/cbBTC | 424 | 7,514,884 | 0.000012 | 52683912 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,223,575 | 0.001681 | 52683912 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/AERO | 10000 | 5,574,350 | 1.089888 | 52683912 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome | WETH/USDC | 3000 | 5,471,000 | 2,463.970721 | 52683912 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome | fBOMB/AERO | 10000 | 5,461,322 | 0.024817 | 52683912 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,428,089 | 0.030045 | 52683912 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/superOETHb | 400 | 5,264,153 | 1.000855 | 52683912 | `0x6446021F4E396dA3df4235C62537431372195D38` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,924,110 | 0.802398 | 52683912 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,790,418 | 0.000280 | 52683912 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,355,392 | 0.998889 | 52683912 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,347,628 | 2,462.054480 | 52683912 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | WETH/KTA | 3000 | 4,082,121 | 34,543.797025 | 52683912 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/AERO | 10000 | 3,558,876 | 2,682.609994 | 52683912 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | cbETH/WETH | 60 | 3,058,159 | 1.141839 | 52683912 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,849,312 | 0.000012 | 52683912 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/VVV | 2721 | 2,679,047 | 101.225547 | 52683912 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,613,170 | 402.246391 | 52683912 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | AERO/cbBTC | 2700 | 2,565,604 | 0.000011 | 52683912 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | WETH/FAI | 10000 | 2,312,209 | 1,152,367.436387 | 52683912 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | WETH/USDT | 406 | 2,237,078 | 2,464.466541 | 52683912 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| uniswap_v3 | BNKR/WETH | 10000 | 2,122,300 | 0.000000 | 52683912 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,111,807 | 1.195904 | 52683912 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,007,128 | 1.405359 | 52683912 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| aerodrome | fBOMB/USDC | 10000 | 1,860,489 | 0.023202 | 52683912 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,855,206 | 15.271909 | 52683912 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,794,514 | 13,377.470327 | 52683912 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | XDP/USDC | 100 | 1,779,577 | 0.018858 | 52683912 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,769,458 | 0.000012 | 52683912 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | WETH/msETH (stable) | 500 | 1,701,822 | 2.310554 | 52683912 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | WETH/AERO | 3000 | 1,577,633 | 2,702.261902 | 52683912 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,531,304 | 0.916551 | 52683912 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| aerodrome | weETH_04c0/WETH | 500 | 1,523,231 | 1.105492 | 52683912 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome_slipstream | WETH/AERO | 3032 | 1,495,495 | 2,701.427700 | 52683912 | `0x82321f3BEB69f503380D6B233857d5C43562e2D0` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,456,109 | 0.825834 | 52683912 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | DRB/WETH | 10000 | 1,383,034 | 0.000000 | 52683912 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,373,357 | 0.004813 | 52683912 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | EURC/USDC | 73 | 1,346,916 | 1.124193 | 52683912 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,344,830 | 0.000278 | 52683912 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,324,107 | 0.436784 | 52683912 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,256,731 | 23.453028 | 52683912 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| aerodrome | USDC/SEND | 3000 | 1,249,107 | 62.279234 | 52683912 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,224,364 | 35,313,335.067008 | 52683912 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,222,504 | 1.105605 | 52683912 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |
| aerodrome | WETH/cbBTC | 3000 | 1,219,995 | 0.030036 | 52683912 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,217,476 | 2,461.601529 | 52683912 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | WETH/WELL | 10000 | 1,214,688 | 1,115,434.792630 | 52683912 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome_slipstream | WETH/MORPHO | 2706 | 1,204,350 | 1,008.551455 | 52683912 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome_slipstream | msUSD/USDC | 500 | 1,181,351 | 0.886320 | 52683912 | `0x7501bc8Bb51616F79bfA524E464fb7B41f0B10fB` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,166,800 | 506,756.054763 | 52683912 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | USDC/NOCK | 3000 | 1,146,318 | 47.960755 | 52683912 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |

## Recherche d'opportunités
- Cycles : 5114 ; routes examinées : 109858948 ; candidats optimisés : 739907 ; net attendu > 0 : 839 ; dernier cycle 518.5 ms
- Rejets (moteur) : {'spread_below_threshold': 107128911, 'liquidity_below_min': 1136816, 'pool_quarantined': 846284, 'negative_expected_net': 739068, 'borrow_bound_too_small': 5103, 'cycle_budget_exhausted': 1927}
- Enregistrements de la session : 739907 ; net attendu > 0 : 839 ; simulés (eth_call de la vraie tx) : 83 (ok 18, échec 65) ; étiquettes ghost N+1 : 6/41 positives
- Décisions : {'REJECTED': 739907} ; motifs de rejet : {'below_safety_margin': 418, 'negative_expected_net': 739068, 'p_lower_below_threshold': 631, 'price_impact': 408, 'reliability_not_demonstrated': 208, 'simulation_failed': 65, 'stale_data': 8}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52683619 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→VIRTUAL→[aerodrome]→cbBTC | 0.005432 cbBTC | 0.000010 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000010 cbBTC (0.7377 €) | — | 18.00 | 0.002 (n=4) | REJECTED | reliability_not_demonstrated |
| 52683619 | WETH→[aerodrome_slipstream]→VIRTUAL→[aerodrome]→cbBTC→[pancakeswap_v3]→WETH | 0.184099 WETH | 0.000328 WETH | 0.000000 WETH | 0.000003 WETH | 0.000325 WETH (0.7375 €) | — | 17.68 | 0.002 (n=4) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52683619 | cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome]→cbBTC | 0.004389 cbBTC | 0.000009 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000009 cbBTC (0.6683 €) | — | 20.18 | 0.002 (n=3) | REJECTED | reliability_not_demonstrated |
| 52683620 | cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome]→cbBTC | 0.004389 cbBTC | 0.000009 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000009 cbBTC (0.6683 €) | — | 20.18 | 0.002 (n=3) | REJECTED | reliability_not_demonstrated |
| 52683619 | USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome]→cbBTC→[aerodrome_slipstream]→USDC | 368.787596 USDC | 0.732861 USDC | 0.000000 USDC | 0.007083 USDC | 0.725778 USDC (0.6677 €) | — | 19.68 | 0.002 (n=4) | REJECTED | reliability_not_demonstrated |
| 52683620 | USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome]→cbBTC→[aerodrome_slipstream]→USDC | 368.787596 USDC | 0.732861 USDC | 0.000000 USDC | 0.007083 USDC | 0.725778 USDC (0.6677 €) | — | 19.68 | 0.002 (n=4) | REJECTED | reliability_not_demonstrated |
| 52683619 | cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome]→cbBTC | 0.004423 cbBTC | 0.000009 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000009 cbBTC (0.6661 €) | — | 19.96 | 0.002 (n=4) | REJECTED | reliability_not_demonstrated |
| 52683620 | cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome]→cbBTC | 0.004423 cbBTC | 0.000009 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000009 cbBTC (0.6661 €) | — | 19.96 | 0.002 (n=4) | REJECTED | reliability_not_demonstrated |
| 52683619 | USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome]→cbBTC→[aerodrome_slipstream]→USDC | 372.440191 USDC | 0.729818 USDC | 0.000000 USDC | 0.007083 USDC | 0.722735 USDC (0.6649 €) | — | 19.41 | 0.002 (n=4) | REJECTED | reliability_not_demonstrated |
| 52683620 | USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome]→cbBTC→[aerodrome_slipstream]→USDC | 372.440191 USDC | 0.729818 USDC | 0.000000 USDC | 0.007083 USDC | 0.722735 USDC (0.6649 €) | — | 19.41 | 0.002 (n=4) | REJECTED | reliability_not_demonstrated |
| 52683619 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome]→cbBTC | 0.004388 cbBTC | 0.000009 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000009 cbBTC (0.6645 €) | — | 20.08 | 0.036 (n=23) | REJECTED | reliability_not_demonstrated |
| 52683620 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome]→cbBTC | 0.004388 cbBTC | 0.000009 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000009 cbBTC (0.6645 €) | — | 20.08 | 0.036 (n=23) | REJECTED | reliability_not_demonstrated |
| 52683619 | USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome]→cbBTC→[pancakeswap_v3]→USDC | 373.580952 USDC | 0.728182 USDC | 0.000000 USDC | 0.007083 USDC | 0.721099 USDC (0.6634 €) | — | 19.30 | 0.001 (n=10) | REJECTED | reliability_not_demonstrated |
| 52683620 | USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome]→cbBTC→[pancakeswap_v3]→USDC | 373.580952 USDC | 0.728182 USDC | 0.000000 USDC | 0.007083 USDC | 0.721099 USDC (0.6634 €) | — | 19.30 | 0.001 (n=10) | REJECTED | reliability_not_demonstrated |
| 52683619 | cbBTC→[uniswap_v3]→USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome]→cbBTC | 0.004258 cbBTC | 0.000008 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000008 cbBTC (0.6223 €) | — | 19.38 | 0.002 (n=4) | REJECTED | reliability_not_demonstrated |
| 52683620 | cbBTC→[uniswap_v3]→USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome]→cbBTC | 0.004258 cbBTC | 0.000008 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000008 cbBTC (0.6223 €) | — | 19.38 | 0.002 (n=4) | REJECTED | reliability_not_demonstrated |
| 52683619 | USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome]→cbBTC→[uniswap_v3]→USDC | 356.229227 USDC | 0.682506 USDC | 0.000000 USDC | 0.007083 USDC | 0.675423 USDC (0.6214 €) | — | 18.96 | 0.002 (n=4) | REJECTED | reliability_not_demonstrated |
| 52683620 | USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome]→cbBTC→[uniswap_v3]→USDC | 356.229227 USDC | 0.682506 USDC | 0.000000 USDC | 0.007083 USDC | 0.675423 USDC (0.6214 €) | — | 18.96 | 0.002 (n=4) | REJECTED | reliability_not_demonstrated |
| 52683620 | WETH→[aerodrome_slipstream]→VIRTUAL→[aerodrome]→cbBTC→[pancakeswap_v3]→WETH | 0.162066 WETH | 0.000260 WETH | 0.000000 WETH | 0.000003 WETH | 0.000257 WETH (0.5831 €) | — | 15.87 | 0.002 (n=4) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52683620 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→VIRTUAL→[aerodrome]→cbBTC | 0.004828 cbBTC | 0.000008 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000008 cbBTC (0.5831 €) | — | 16.01 | 0.002 (n=4) | REJECTED | reliability_not_demonstrated |
| 52683619 | cbBTC→[uniswap_v3]→WETH→[aerodrome_slipstream]→VIRTUAL→[aerodrome]→cbBTC | 0.004932 cbBTC | 0.000008 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000008 cbBTC (0.5823 €) | — | 15.65 | 0.008 (n=39) | REJECTED | p_lower_below_threshold(0.01<0.75) |
| 52683619 | WETH→[aerodrome_slipstream]→VIRTUAL→[aerodrome]→cbBTC→[uniswap_v3]→WETH | 0.162065 WETH | 0.000260 WETH | 0.000000 WETH | 0.000003 WETH | 0.000257 WETH (0.5817 €) | — | 15.84 | 0.008 (n=39) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.01<0.75) |
| 52683619 | cbBTC→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→VIRTUAL→[aerodrome]→cbBTC | 0.004147 cbBTC | 0.000007 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000007 cbBTC (0.5371 €) | — | 17.17 | 0.008 (n=39) | REJECTED | p_lower_below_threshold(0.01<0.75) |
| 52683619 | WETH→[aerodrome_slipstream]→VIRTUAL→[aerodrome]→cbBTC→[aerodrome_slipstream]→WETH | 0.142392 WETH | 0.000240 WETH | 0.000000 WETH | 0.000003 WETH | 0.000237 WETH (0.5370 €) | — | 16.64 | 0.008 (n=39) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.01<0.75) |
| 52683619 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome]→cbBTC | 0.003608 cbBTC | 0.000007 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000007 cbBTC (0.5273 €) | — | 19.37 | 0.001 (n=10) | REJECTED | reliability_not_demonstrated |

## Fiabilité et décision
- Observations ghost : 554 ; taux observé 0.121 ; borne inférieure crédible (0.9) 0.104 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 10.4% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
