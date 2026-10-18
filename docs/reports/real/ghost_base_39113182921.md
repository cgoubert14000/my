# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-18T13:42:06+00:00 ; durée 283.89 min ; blocs 52762270 → 52770783 (8350 vus)

## Connexion
- Requêtes RPC : 114659 ; erreurs : 0 ; latence p50/p95 : 273.4/905.8 ms
- Rafraîchissements d'état : 8351 ; âge des données au dernier bloc : 1.67 s ; changements de frais LP observés (pools à frais dynamiques) : 15175
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 131310 ; cycles déclenchés par événement : 11581 ; avance médiane sur le rafraîchissement multicall : 379 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,387.65 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 578 pools, 328 jetons, 21580 routes
- Par DEX : uniswap_v3 136, aerodrome 235 (quarantaine 2), aerodrome_slipstream 157, pancakeswap_v3 32, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 207 (rejetés 2) → 612 jetons ; pools candidats 3915 (énumérés 394, par paires 0), mesurés 580, sous le plancher de 10000.0 $ : 2 → gardés 578 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'DAI': 1.0, 'USDC': 1.0, 'WETH': 2410.986474, 'AERO': 0.834015, 'cbBTC': 81629.281689}
- Pools en quarantaine : 2 — aerodrome:fBOMB/AERO@0xbBf71A: simulation failed ×5 (model/chain mismatch) — until block 52770809; aerodrome:fBOMB/USDC@0xFf8e0b: simulation failed ×5 (model/chain mismatch) — until block 52770809

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 145,452,431 | 2,387.646168 | 52770783 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 41,462,766 | 1.234596 | 52770783 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 500 | 18,047,144 | 0.029400 | 52770783 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 16,526,818 | 108.085842 | 52770783 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| aerodrome_slipstream | WETH/cbBTC | 2510 | 16,109,314 | 0.029387 | 52770783 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,318,807 | 0.029399 | 52770783 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,744,379 | 0.000012 | 52770783 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 8,985,122 | 2,392.429863 | 52770783 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome_slipstream | USDC/cbBTC | 472 | 8,233,748 | 0.000012 | 52770783 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome_slipstream | USDC/cbBTC | 346 | 7,843,772 | 0.000012 | 52770783 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,085,906 | 0.001648 | 52770783 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | WETH/USDC | 788 | 7,035,298 | 2,392.992649 | 52770783 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome | WETH/USDC | 3000 | 5,460,708 | 2,387.622207 | 52770783 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,272,371 | 0.029402 | 52770783 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/superOETHb | 400 | 5,184,942 | 1.000855 | 52770783 | `0x6446021F4E396dA3df4235C62537431372195D38` |
| aerodrome | fBOMB/AERO | 10000 | 5,029,063 | 0.025720 | 52770783 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,772,599 | 0.802398 | 52770783 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,584,711 | 0.000272 | 52770783 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,409,841 | 0.998809 | 52770783 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,395,999 | 2,392.772340 | 52770783 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | WETH/KTA | 3000 | 4,020,032 | 33,458.346263 | 52770783 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | USDC/AERO | 10000 | 3,624,868 | 1.227494 | 52770783 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome_slipstream | WETH/USDT | 445 | 3,559,913 | 2,396.054536 | 52770783 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome | WETH/AERO | 10000 | 3,282,681 | 2,937.827667 | 52770783 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,877,334 | 1.141820 | 52770783 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,830,340 | 0.000012 | 52770783 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/VVV | 2802 | 2,523,538 | 108.112644 | 52770783 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 2,468,281 | 0.000010 | 52770783 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,260,743 | 409.470540 | 52770783 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | WETH/FAI | 10000 | 2,229,286 | 1,164,488.939756 | 52770783 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,106,813 | 1.199655 | 52770783 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,035,564 | 1.373959 | 52770783 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| aerodrome_slipstream | EURC/USDC | 73 | 1,959,575 | 1.123337 | 52770783 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,844,820 | 0.000000 | 52770783 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome | fBOMB/USDC | 10000 | 1,800,258 | 0.021398 | 52770783 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| uniswap_v3 | XDP/USDC | 100 | 1,776,878 | 0.018840 | 52770783 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,775,615 | 15.765635 | 52770783 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,763,248 | 0.000012 | 52770783 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,733,492 | 13,931.893815 | 52770783 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | weETH_04c0/WETH | 500 | 1,726,490 | 1.105521 | 52770783 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome | WETH/msETH (stable) | 500 | 1,654,631 | 2.304383 | 52770783 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | WETH/AERO | 3000 | 1,487,973 | 2,956.438321 | 52770783 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,456,394 | 0.826238 | 52770783 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,318,449 | 0.435380 | 52770783 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,310,271 | 0.000000 | 52770783 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,285,026 | 0.000270 | 52770783 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,270,473 | 0.004595 | 52770783 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome | WETH/cbBTC | 3000 | 1,245,944 | 0.029402 | 52770783 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| aerodrome | USDC/SEND | 3000 | 1,233,250 | 63.891160 | 52770783 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,225,840 | 23.333268 | 52770783 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| aerodrome_slipstream | WETH/msETH | 500 | 1,200,615 | 1.131038 | 52770783 | `0x74F72788F4814D7fF3C49B44684aa98Eee140C0E` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,197,413 | 2,392.492701 | 52770783 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | WETH/doginme | 10000 | 1,186,991 | 35,292,776.914954 | 52770783 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | WETH/WELL | 10000 | 1,151,391 | 1,165,957.462515 | 52770783 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,119,822 | 520,265.007663 | 52770783 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome_slipstream | msUSD/USDC | 500 | 1,105,224 | 0.885256 | 52770783 | `0x7501bc8Bb51616F79bfA524E464fb7B41f0B10fB` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,093,085 | 14.960563 | 52770783 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | USDC/NOCK | 3000 | 1,070,661 | 54.967930 | 52770783 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,047,962 | 1.105821 | 52770783 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |
| aerodrome | WETH/EDEL | 7000 | 1,042,336 | 90,372.184556 | 52770783 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |

## Recherche d'opportunités
- Cycles : 19931 ; routes examinées : 430110980 ; candidats optimisés : 2208407 ; net attendu > 0 : 1079 ; dernier cycle 80.7 ms
- Rejets (moteur) : {'spread_below_threshold': 424440172, 'liquidity_below_min': 3215288, 'negative_expected_net': 2207328, 'pool_quarantined': 212942, 'borrow_bound_too_small': 19924, 'cycle_budget_exhausted': 14247}
- Enregistrements de la session : 2208407 ; net attendu > 0 : 1079 ; simulés (eth_call de la vraie tx) : 103 (ok 25, échec 78) ; étiquettes ghost N+1 : 0/77 positives
- Décisions : {'REJECTED': 2208407} ; motifs de rejet : {'below_safety_margin': 843, 'negative_expected_net': 2207328, 'p_lower_below_threshold': 825, 'price_impact': 6, 'reliability_not_demonstrated': 254, 'simulation_failed': 78, 'stale_data': 2}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52763312 | WETH→[uniswap_v3]→TEVA→[aerodrome]→WETH | 0.045860 WETH | 0.000451 WETH | 0.000000 WETH | 0.000002 WETH | 0.000449 WETH (0.9969 €) | — | 97.84 | — (n=0) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52763336 | WETH→[uniswap_v3]→TEVA→[aerodrome]→WETH | 0.044695 WETH | 0.000379 WETH | 0.000000 WETH | 0.000002 WETH | 0.000377 WETH (0.8390 €) | — | 84.36 | 0.006 (n=1) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52765230 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→USDC | 331.897771 USDC | 0.790288 USDC | 0.000000 USDC | 0.007637 USDC | 0.782651 USDC (0.7200 €) | — | 23.58 | 0.002 (n=4) | REJECTED | reliability_not_demonstrated |
| 52765230 | WETH→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.137210 WETH | 0.000326 WETH | 0.000000 WETH | 0.000003 WETH | 0.000323 WETH (0.7192 €) | — | 23.55 | 0.002 (n=4) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52765230 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→USDC | 334.557229 USDC | 0.776637 USDC | 0.000000 USDC | 0.007637 USDC | 0.769000 USDC (0.7075 €) | — | 22.99 | 0.002 (n=5) | REJECTED | reliability_not_demonstrated |
| 52765230 | WETH→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.138268 WETH | 0.000321 WETH | 0.000000 WETH | 0.000003 WETH | 0.000317 WETH (0.7067 €) | — | 22.96 | 0.002 (n=5) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52770431 | WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 1.536170 WETH | 0.000301 WETH | 0.000000 WETH | 0.000003 WETH | 0.000297 WETH (0.6567 €) | — | 1.94 | 0.131 (n=103) | REJECTED | below_safety_margin(297431252520989<307233958732228), p_lower_below_threshold(0.13<0.75) |
| 52770431 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC | 3,679.785940 USDC | 0.720256 USDC | 0.000000 USDC | 0.008309 USDC | 0.711947 USDC (0.6550 €) | — | 1.93 | 0.131 (n=103) | REJECTED | below_safety_margin(711947<735957), p_lower_below_threshold(0.13<0.75) |
| 52769416 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.560034 WETH | 0.000286 WETH | 0.000000 WETH | 0.000002 WETH | 0.000284 WETH (0.6307 €) | — | 5.06 | 0.000 (n=67) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 52769416 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 1,349.869585 USDC | 0.690241 USDC | 0.000000 USDC | 0.005796 USDC | 0.684445 USDC (0.6297 €) | — | 5.07 | 0.000 (n=67) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 52762636 | WETH→[aerodrome_slipstream]→KTA→[aerodrome]→WETH | 0.107115 WETH | 0.000278 WETH | 0.000000 WETH | 0.000002 WETH | 0.000276 WETH (0.6125 €) | — | 25.74 | 0.002 (n=4) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52769416 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.015054 cbBTC | 0.000008 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000008 cbBTC (0.6051 €) | — | 5.33 | 0.136 (n=81) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 52769416 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.528671 WETH | 0.000275 WETH | 0.000000 WETH | 0.000003 WETH | 0.000272 WETH (0.6048 €) | — | 5.14 | 0.136 (n=81) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.14<0.75) |
| 52769416 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 1,272.043171 USDC | 0.663285 USDC | 0.000000 USDC | 0.007266 USDC | 0.656019 USDC (0.6035 €) | — | 5.16 | 0.136 (n=81) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 52770431 | WETH→[aerodrome_slipstream]→USDT→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 1.411056 WETH | 0.000275 WETH | 0.000000 WETH | 0.000003 WETH | 0.000272 WETH (0.6003 €) | — | 1.93 | 0.131 (n=103) | REJECTED | below_safety_margin(271850490476985<282211220469743), p_lower_below_threshold(0.13<0.75) |
| 52770431 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDT→[uniswap_v3]→USDC | 3,371.626297 USDC | 0.659006 USDC | 0.000000 USDC | 0.008309 USDC | 0.650697 USDC (0.5986 €) | — | 1.93 | 0.131 (n=103) | REJECTED | below_safety_margin(650697<674325), p_lower_below_threshold(0.13<0.75) |
| 52765230 | USDC→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→USDC | 294.578188 USDC | 0.599486 USDC | 0.000000 USDC | 0.007637 USDC | 0.591849 USDC (0.5445 €) | — | 20.09 | 0.002 (n=4) | REJECTED | reliability_not_demonstrated |
| 52765230 | WETH→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→WETH | 0.121496 WETH | 0.000247 WETH | 0.000000 WETH | 0.000003 WETH | 0.000244 WETH (0.5436 €) | — | 20.10 | 0.002 (n=4) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52765230 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→USDC | 287.191677 USDC | 0.570485 USDC | 0.000000 USDC | 0.007637 USDC | 0.562848 USDC (0.5178 €) | — | 19.60 | 0.001 (n=14) | REJECTED | reliability_not_demonstrated |
| 52765230 | WETH→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.118596 WETH | 0.000235 WETH | 0.000000 WETH | 0.000003 WETH | 0.000232 WETH (0.5169 €) | — | 19.58 | 0.001 (n=14) | REJECTED | reliability_not_demonstrated |
| 52765230 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→USDC | 279.567138 USDC | 0.544737 USDC | 0.000000 USDC | 0.007637 USDC | 0.537100 USDC (0.4941 €) | — | 19.21 | 0.001 (n=14) | REJECTED | reliability_not_demonstrated |
| 52765230 | WETH→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.115494 WETH | 0.000225 WETH | 0.000000 WETH | 0.000003 WETH | 0.000222 WETH (0.4932 €) | — | 19.19 | 0.001 (n=14) | REJECTED | reliability_not_demonstrated |
| 52770431 | WETH→[aerodrome_slipstream]→USDT→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 1.012027 WETH | 0.000202 WETH | 0.000000 WETH | 0.000003 WETH | 0.000198 WETH (0.4383 €) | — | 1.96 | 0.131 (n=103) | REJECTED | below_safety_margin(198490182309506<202405437407813), p_lower_below_threshold(0.13<0.75) |
| 52770431 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDT→[pancakeswap_v3]→USDC | 2,420.659123 USDC | 0.483370 USDC | 0.000000 USDC | 0.008309 USDC | 0.475061 USDC (0.4371 €) | — | 1.96 | 0.131 (n=103) | REJECTED | below_safety_margin(475061<484131), p_lower_below_threshold(0.13<0.75) |
| 52765230 | USDC→[sushiswap_v3]→WETH→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→USDC | 211.066296 USDC | 0.415657 USDC | 0.000000 USDC | 0.008004 USDC | 0.407653 USDC (0.3750 €) | — | 19.31 | 0.001 (n=14) | REJECTED | reliability_not_demonstrated |

## Fiabilité et décision
- Observations ghost : 940 ; taux observé 0.120 ; borne inférieure crédible (0.9) 0.107 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 10.7% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
