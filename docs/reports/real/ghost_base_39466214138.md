# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-20T22:17:35+00:00 ; durée 283.64 min ; blocs 52864139 → 52872645 (7598 vus)

## Connexion
- Requêtes RPC : 105612 ; erreurs : 263 ; latence p50/p95 : 561.6/1,792.8 ms
- Rafraîchissements d'état : 7598 ; âge des données au dernier bloc : 5.28 s ; changements de frais LP observés (pools à frais dynamiques) : 16298
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 131949 ; cycles déclenchés par événement : 6298 ; avance médiane sur le rafraîchissement multicall : 1,354 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,454.54 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 577 pools, 327 jetons, 22534 routes
- Par DEX : uniswap_v3 136, aerodrome 236 (quarantaine 2), aerodrome_slipstream 158, pancakeswap_v3 30, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 207 (rejetés 2) → 612 jetons ; pools candidats 3877 (énumérés 395, par paires 0), mesurés 579, sous le plancher de 10000.0 $ : 2 → gardés 577 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDbC': 1.0, 'USDC': 1.0, 'WETH': 2447.454075, 'AERO': 0.860145, 'cbBTC': 82683.957961}
- Pools en quarantaine : 2 — aerodrome:fBOMB/AERO@0xbBf71A: simulation failed ×5 (model/chain mismatch) — until block 52872766; aerodrome:fBOMB/cbBTC@0x3d36Cf: simulation failed ×5 (model/chain mismatch) — until block 52872766

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 148,620,946 | 2,454.540569 | 52872646 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 40,925,613 | 1.122803 | 52872646 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 18,778,361 | 0.029592 | 52872646 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/VVV | 3000 | 17,995,354 | 95.983700 | 52872646 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,441,473 | 0.029631 | 52872646 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,575,076 | 0.029573 | 52872646 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,934,160 | 0.000012 | 52872646 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 8,622,904 | 2,460.446366 | 52872646 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome_slipstream | WETH/USDC | 594 | 8,503,949 | 2,461.214778 | 52872646 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | USDC/cbBTC | 436 | 8,431,120 | 0.000012 | 52872646 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome | WETH/USDC | 3000 | 8,395,271 | 2,454.664836 | 52872646 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | USDC/cbBTC | 336 | 8,173,417 | 0.000012 | 52872646 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,308,125 | 0.001681 | 52872646 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,451,098 | 0.029633 | 52872646 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | fBOMB/AERO | 10000 | 5,348,611 | 0.024511 | 52872646 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,739,340 | 0.000275 | 52872646 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,731,258 | 0.802394 | 52872646 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,452,690 | 2,461.426037 | 52872646 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,402,940 | 0.998740 | 52872646 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome_slipstream | WETH/USDT | 406 | 4,237,766 | 2,463.565092 | 52872646 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome | WETH/KTA | 3000 | 4,059,576 | 34,673.917032 | 52872646 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | USDC/AERO | 10000 | 3,603,552 | 1.130606 | 52872646 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome | WETH/AERO | 10000 | 3,441,100 | 2,777.848002 | 52872646 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,875,019 | 0.000012 | 52872646 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/VVV | 2700 | 2,751,824 | 95.986683 | 52872646 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | WETH/MORPHO | 2703 | 2,674,252 | 1,018.049225 | 52872646 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,542,749 | 1.142084 | 52872646 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,472,357 | 401.414110 | 52872646 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | AERO/cbBTC | 2700 | 2,383,112 | 0.000011 | 52872646 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | WETH/FAI | 10000 | 2,249,203 | 1,208,956.300568 | 52872646 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,058,907 | 1.238865 | 52872646 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,027,920 | 1.383226 | 52872646 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,962,427 | 0.000000 | 52872646 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome | weETH_04c0/WETH | 500 | 1,921,358 | 1.105602 | 52872646 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| uniswap_v3 | XDP/USDC | 100 | 1,816,656 | 0.019372 | 52872646 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,777,118 | 0.000012 | 52872646 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,768,994 | 13,544.095535 | 52872646 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,716,489 | 15.864263 | 52872646 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | fBOMB/USDC | 10000 | 1,711,029 | 0.021273 | 52872646 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| uniswap_v3 | WETH/AERO | 3000 | 1,699,067 | 2,762.770139 | 52872646 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | WETH/msETH (stable) | 500 | 1,693,634 | 2.311422 | 52872646 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,573,912 | 0.916062 | 52872646 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,456,349 | 0.826533 | 52872646 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | EURC/USDC | 70 | 1,391,301 | 1.123475 | 52872646 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,355,530 | 0.004804 | 52872646 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v3 | DRB/WETH | 10000 | 1,348,593 | 0.000000 | 52872646 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,328,805 | 0.000277 | 52872646 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | WETH/cbBTC | 3000 | 1,312,889 | 0.029584 | 52872646 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,274,151 | 2,460.445846 | 52872646 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,235,999 | 63.607139 | 52872646 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,226,201 | 23.060385 | 52872646 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| aerodrome | WETH/EDEL | 7000 | 1,225,694 | 68,752.670077 | 52872646 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/doginme | 10000 | 1,218,880 | 35,654,187.998682 | 52872646 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,180,957 | 0.436848 | 52872646 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,173,736 | 494,185.481434 | 52872646 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | WETH/WELL | 10000 | 1,168,675 | 1,196,019.729567 | 52872646 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,146,247 | 1.106158 | 52872646 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |
| aerodrome | USDC/NOCK | 3000 | 1,136,552 | 48.778264 | 52872646 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | msUSD/USDC | 503 | 1,127,882 | 0.886359 | 52872646 | `0x7501bc8Bb51616F79bfA524E464fb7B41f0B10fB` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,108,956 | 20,633,128.396423 | 52872646 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |

## Recherche d'opportunités
- Cycles : 13895 ; routes examinées : 313109930 ; candidats optimisés : 1515810 ; net attendu > 0 : 168 ; dernier cycle 548.4 ms
- Rejets (moteur) : {'spread_below_threshold': 309265226, 'liquidity_below_min': 2132682, 'negative_expected_net': 1515642, 'pool_quarantined': 178752, 'borrow_bound_too_small': 13872, 'cycle_budget_exhausted': 3588}
- Enregistrements de la session : 1515810 ; net attendu > 0 : 168 ; simulés (eth_call de la vraie tx) : 31 (ok 7, échec 24) ; étiquettes ghost N+1 : 4/17 positives
- Décisions : {'REJECTED': 1515810} ; motifs de rejet : {'below_safety_margin': 69, 'negative_expected_net': 1515642, 'p_lower_below_threshold': 127, 'price_impact': 10, 'reliability_not_demonstrated': 41, 'sim_below_estimate': 1, 'simulation_failed': 24, 'stale_data': 5}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52864215 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→ZORA→[aerodrome_slipstream]→WETH | 0.107790 WETH | 0.000142 WETH | 0.000000 WETH | 0.000003 WETH | 0.000139 WETH (0.3137 €) | — | 12.93 | 0.000 (n=23) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52864215 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→ZORA→[aerodrome_slipstream]→WETH | 0.107651 WETH | 0.000142 WETH | 0.000000 WETH | 0.000003 WETH | 0.000139 WETH (0.3131 €) | — | 12.92 | 0.000 (n=24) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52864215 | USDC→[uniswap_v3]→ZORA→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 263.009308 USDC | 0.347768 USDC | 0.000000 USDC | 0.007447 USDC | 0.340321 USDC (0.3131 €) | — | 12.94 | 0.000 (n=23) | REJECTED | reliability_not_demonstrated |
| 52864215 | USDC→[uniswap_v3]→ZORA→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 262.890606 USDC | 0.347145 USDC | 0.000000 USDC | 0.007447 USDC | 0.339698 USDC (0.3125 €) | — | 12.92 | 0.000 (n=24) | REJECTED | reliability_not_demonstrated |
| 52864215 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→ZORA→[aerodrome_slipstream]→WETH | 0.104793 WETH | 0.000140 WETH | 0.000000 WETH | 0.000003 WETH | 0.000137 WETH (0.3090 €) | — | 13.10 | 0.000 (n=23) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52864215 | USDC→[uniswap_v3]→ZORA→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 255.494914 USDC | 0.342672 USDC | 0.000000 USDC | 0.007447 USDC | 0.335225 USDC (0.3084 €) | — | 13.12 | 0.000 (n=23) | REJECTED | reliability_not_demonstrated |
| 52864215 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→ZORA→[aerodrome_slipstream]→WETH | 0.105902 WETH | 0.000139 WETH | 0.000000 WETH | 0.000003 WETH | 0.000136 WETH (0.3058 €) | — | 12.82 | 0.000 (n=24) | REJECTED | reliability_not_demonstrated |
| 52864215 | USDC→[uniswap_v3]→ZORA→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 258.491603 USDC | 0.339173 USDC | 0.000000 USDC | 0.007447 USDC | 0.331726 USDC (0.3052 €) | — | 12.83 | 0.000 (n=24) | REJECTED | reliability_not_demonstrated |
| 52864215 | USDC→[uniswap_v3]→ZORA→[aerodrome_slipstream]→USDC | 223.523660 USDC | 0.301346 USDC | 0.000000 USDC | 0.005571 USDC | 0.295775 USDC (0.2721 €) | — | 13.23 | 0.002 (n=4) | REJECTED | reliability_not_demonstrated |
| 52864215 | WETH→[sushiswap_v3]→USDC→[uniswap_v3]→ZORA→[aerodrome_slipstream]→WETH | 0.075471 WETH | 0.000103 WETH | 0.000000 WETH | 0.000003 WETH | 0.000100 WETH (0.2250 €) | — | 13.24 | 0.000 (n=23) | REJECTED | reliability_not_demonstrated |
| 52864215 | USDC→[uniswap_v3]→ZORA→[aerodrome_slipstream]→WETH→[sushiswap_v3]→USDC | 183.847545 USDC | 0.251751 USDC | 0.000000 USDC | 0.007818 USDC | 0.243933 USDC (0.2244 €) | — | 13.27 | 0.000 (n=23) | REJECTED | reliability_not_demonstrated |
| 52864215 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→ZORA→[aerodrome_slipstream]→WETH | 0.085936 WETH | 0.000090 WETH | 0.000000 WETH | 0.000003 WETH | 0.000087 WETH (0.1959 €) | — | 10.12 | 0.000 (n=23) | REJECTED | reliability_not_demonstrated |
| 52864215 | USDC→[uniswap_v3]→ZORA→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→USDC | 209.235903 USDC | 0.219816 USDC | 0.000000 USDC | 0.007447 USDC | 0.212369 USDC (0.1954 €) | — | 10.15 | 0.000 (n=23) | REJECTED | reliability_not_demonstrated |
| 52872012 | USDC→[aerodrome]→VIRTUAL→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 92.683541 USDC | 0.134522 USDC | 0.000000 USDC | 0.007042 USDC | 0.127480 USDC (0.1173 €) | — | 13.75 | 0.027 (n=11) | REJECTED | reliability_not_demonstrated |
| 52872012 | WETH→[pancakeswap_v3]→USDC→[aerodrome]→VIRTUAL→[aerodrome_slipstream]→WETH | 0.037868 WETH | 0.000055 WETH | 0.000000 WETH | 0.000003 WETH | 0.000052 WETH (0.1170 €) | 0.000052 WETH | 13.71 | 0.027 (n=11) | REJECTED | reliability_not_demonstrated |
| 52872012 | USDC→[aerodrome]→VIRTUAL→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 90.453283 USDC | 0.129444 USDC | 0.000000 USDC | 0.007042 USDC | 0.122402 USDC (0.1126 €) | — | 13.53 | 0.014 (n=105) | REJECTED | p_lower_below_threshold(0.01<0.75) |
| 52872012 | WETH→[uniswap_v3]→USDC→[aerodrome]→VIRTUAL→[aerodrome_slipstream]→WETH | 0.036841 WETH | 0.000053 WETH | 0.000000 WETH | 0.000003 WETH | 0.000050 WETH (0.1124 €) | 0.000050 WETH | 13.53 | 0.014 (n=105) | REJECTED | p_lower_below_threshold(0.01<0.75) |
| 52872012 | USDC→[aerodrome]→VIRTUAL→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 90.441307 USDC | 0.128716 USDC | 0.000000 USDC | 0.007042 USDC | 0.121674 USDC (0.1119 €) | — | 13.45 | 0.027 (n=11) | REJECTED | reliability_not_demonstrated |
| 52872012 | WETH→[pancakeswap_v3]→USDC→[aerodrome]→VIRTUAL→[aerodrome_slipstream]→WETH | 0.036887 WETH | 0.000052 WETH | 0.000000 WETH | 0.000003 WETH | 0.000050 WETH (0.1117 €) | 0.000050 WETH | 13.43 | 0.027 (n=11) | REJECTED | reliability_not_demonstrated |
| 52872012 | USDC→[aerodrome]→VIRTUAL→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 90.545957 USDC | 0.128106 USDC | 0.000000 USDC | 0.007042 USDC | 0.121064 USDC (0.1114 €) | — | 13.37 | 0.014 (n=105) | REJECTED | p_lower_below_threshold(0.01<0.75) |
| 52872012 | WETH→[uniswap_v3]→USDC→[aerodrome]→VIRTUAL→[aerodrome_slipstream]→WETH | 0.036888 WETH | 0.000052 WETH | 0.000000 WETH | 0.000003 WETH | 0.000049 WETH (0.1111 €) | — | 13.36 | 0.014 (n=105) | REJECTED | p_lower_below_threshold(0.01<0.75) |
| 52864215 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→ZORA→[aerodrome_slipstream]→WETH | 0.063447 WETH | 0.000049 WETH | 0.000000 WETH | 0.000003 WETH | 0.000046 WETH (0.1038 €) | — | 7.26 | 0.146 (n=81) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 52864215 | USDC→[uniswap_v3]→ZORA→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 154.894625 USDC | 0.119867 USDC | 0.000000 USDC | 0.007447 USDC | 0.112420 USDC (0.1034 €) | — | 7.26 | 0.146 (n=81) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 52872012 | USDC→[aerodrome]→VIRTUAL→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 81.373521 USDC | 0.102254 USDC | 0.000000 USDC | 0.007042 USDC | 0.095212 USDC (0.0876 €) | — | 11.70 | 0.027 (n=11) | REJECTED | reliability_not_demonstrated |
| 52872012 | WETH→[pancakeswap_v3]→USDC→[aerodrome]→VIRTUAL→[aerodrome_slipstream]→WETH | 0.033270 WETH | 0.000042 WETH | 0.000000 WETH | 0.000003 WETH | 0.000039 WETH (0.0874 €) | — | 11.65 | 0.027 (n=11) | REJECTED | reliability_not_demonstrated |

## Fiabilité et décision
- Observations ghost : 1562 ; taux observé 0.104 ; borne inférieure crédible (0.9) 0.094 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 9.4% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
