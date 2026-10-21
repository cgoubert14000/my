# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-21T11:20:47+00:00 ; durée 55.06 min ; blocs 52894493 → 52896145 (1453 vus)

## Connexion
- Requêtes RPC : 19718 ; erreurs : 55 ; latence p50/p95 : 952.8/2,905.8 ms
- Rafraîchissements d'état : 1453 ; âge des données au dernier bloc : 14.49 s ; changements de frais LP observés (pools à frais dynamiques) : 3250
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 9790 ; cycles déclenchés par événement : 581 ; avance médiane sur le rafraîchissement multicall : 935 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,454.56 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 578 pools, 326 jetons, 21598 routes
- Par DEX : uniswap_v3 138, aerodrome 235 (quarantaine 2), aerodrome_slipstream 155, pancakeswap_v3 32, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 206 (rejetés 2) → 611 jetons ; pools candidats 3912 (énumérés 393, par paires 0), mesurés 581, sous le plancher de 10000.0 $ : 3 → gardés 578 (max 1500) ; prix des hubs : {'USDC': 1.0, 'DAI': 1.0, 'USDbC': 1.0, 'WETH': 2451.17881, 'AERO': 0.838921, 'cbBTC': 83216.410353}
- Pools en quarantaine : 2 — aerodrome:fBOMB/USDC@0xFf8e0b: simulation failed ×5 (model/chain mismatch) — until block 52896291; aerodrome:fBOMB/USDbC@0xC39566: simulation failed ×5 (model/chain mismatch) — until block 52896291

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 149,388,822 | 2,454.563832 | 52896144 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 38,445,888 | 1.183110 | 52896144 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| aerodrome | WETH/VVV | 3000 | 18,061,253 | 95.124156 | 52896144 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,462,833 | 0.029525 | 52896144 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,440,755 | 0.029473 | 52896144 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| aerodrome_slipstream | WETH/cbBTC | 2505 | 10,373,095 | 0.029466 | 52896144 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,451,984 | 0.000012 | 52896144 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome_slipstream | USDC/cbBTC | 424 | 8,844,335 | 0.000012 | 52896144 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | WETH/USDC | 500 | 8,791,708 | 2,460.875846 | 52896144 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/USDC | 3000 | 8,468,748 | 2,454.423354 | 52896144 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | WETH/USDC | 535 | 7,933,147 | 2,460.727198 | 52896144 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | USDC/cbBTC | 332 | 7,422,674 | 0.000012 | 52896144 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,304,655 | 0.001672 | 52896144 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,618,126 | 0.029527 | 52896144 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | fBOMB/AERO | 10000 | 5,166,826 | 0.024844 | 52896144 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,736,787 | 0.000279 | 52896144 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,730,732 | 0.802395 | 52896144 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,529,449 | 2,460.520770 | 52896144 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,412,699 | 0.998741 | 52896144 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 4,054,166 | 34,767.574109 | 52896144 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDT | 406 | 3,851,157 | 2,463.773815 | 52896144 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome_slipstream | USDC/AERO | 10000 | 3,747,511 | 1.183610 | 52896144 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome | WETH/AERO | 10000 | 3,350,562 | 2,898.942477 | 52896144 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | WETH/MORPHO | 2703 | 2,800,989 | 1,035.710035 | 52896144 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome_slipstream | WETH/VVV | 2703 | 2,765,267 | 95.158830 | 52896144 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,747,999 | 398.121242 | 52896144 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,540,023 | 1.142088 | 52896144 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 2,321,629 | 0.000010 | 52896144 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,270,512 | 0.000012 | 52896144 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | WETH/FAI | 10000 | 2,247,871 | 1,209,742.010817 | 52896144 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 2,076,914 | 0.000012 | 52896144 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,027,072 | 1.383640 | 52896144 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,956,937 | 0.000000 | 52896144 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome | weETH_04c0/WETH | 500 | 1,912,240 | 1.105697 | 52896144 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| uniswap_v3 | XDP/USDC | 100 | 1,804,709 | 0.019178 | 52896144 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,722,535 | 0.916061 | 52896144 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,710,848 | 1.490009 | 52896144 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome | WETH/msETH (stable) | 500 | 1,694,401 | 2.310993 | 52896144 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,692,743 | 15.819999 | 52896144 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| uniswap_v3 | WETH/AERO | 3000 | 1,678,907 | 2,909.831630 | 52896144 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,675,454 | 13,503.978007 | 52896144 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | fBOMB/USDC | 10000 | 1,479,630 | 0.020657 | 52896144 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,458,172 | 0.826524 | 52896144 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | EURC/USDC | 70 | 1,429,304 | 1.122934 | 52896144 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,352,672 | 0.004792 | 52896144 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,338,603 | 0.000280 | 52896144 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| uniswap_v3 | DRB/WETH | 10000 | 1,326,964 | 0.000000 | 52896144 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | WETH/cbBTC | 3000 | 1,314,394 | 0.029472 | 52896144 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,279,420 | 2,460.534198 | 52896144 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,234,154 | 63.797535 | 52896144 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,228,340 | 34,792,196.491151 | 52896144 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,218,442 | 23.076897 | 52896144 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| aerodrome | WETH/EDEL | 7000 | 1,201,911 | 71,390.965744 | 52896144 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | WETH/WELL | 10000 | 1,200,428 | 1,133,547.877610 | 52896144 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,183,244 | 483,701.488787 | 52896144 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | USDC/NOCK | 3000 | 1,182,792 | 45.038972 | 52896144 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,181,344 | 0.436589 | 52896144 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,161,646 | 1.106158 | 52896144 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |
| aerodrome_slipstream | msUSD/USDC | 500 | 1,158,653 | 0.886246 | 52896144 | `0x7501bc8Bb51616F79bfA524E464fb7B41f0B10fB` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,117,508 | 20,374,625.032721 | 52896144 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |

## Recherche d'opportunités
- Cycles : 2033 ; routes examinées : 43908734 ; candidats optimisés : 290973 ; net attendu > 0 : 174 ; dernier cycle 225.0 ms
- Rejets (moteur) : {'spread_below_threshold': 43184787, 'liquidity_below_min': 360448, 'negative_expected_net': 290799, 'pool_quarantined': 69440, 'borrow_bound_too_small': 2024, 'cycle_budget_exhausted': 1062}
- Enregistrements de la session : 290973 ; net attendu > 0 : 174 ; simulés (eth_call de la vraie tx) : 25 (ok 13, échec 12) ; étiquettes ghost N+1 : 0/16 positives
- Décisions : {'REJECTED': 290973} ; motifs de rejet : {'below_safety_margin': 132, 'negative_expected_net': 290799, 'p_lower_below_threshold': 109, 'price_impact': 62, 'reliability_not_demonstrated': 65, 'simulation_failed': 12, 'stale_data': 11}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52895732 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 27.839630 USDC | 0.068292 USDC | 0.000000 USDC | 0.015234 USDC | 0.053058 USDC (0.0488 €) | — | 19.06 | 0.000 (n=25) | REJECTED | reliability_not_demonstrated |
| 52895732 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.011374 WETH | 0.000028 WETH | 0.000000 WETH | 0.000006 WETH | 0.000022 WETH (0.0487 €) | 0.000022 WETH | 18.96 | 0.000 (n=25) | REJECTED | reliability_not_demonstrated |
| 52895732 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 27.539992 USDC | 0.066544 USDC | 0.000000 USDC | 0.015234 USDC | 0.051310 USDC (0.0472 €) | — | 18.63 | 0.000 (n=25) | REJECTED | reliability_not_demonstrated |
| 52895732 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.011221 WETH | 0.000027 WETH | 0.000000 WETH | 0.000006 WETH | 0.000021 WETH (0.0471 €) | 0.000021 WETH | 18.59 | 0.000 (n=25) | REJECTED | reliability_not_demonstrated |
| 52895732 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 27.419986 USDC | 0.066108 USDC | 0.000000 USDC | 0.015234 USDC | 0.050874 USDC (0.0468 €) | — | 18.55 | 0.000 (n=25) | REJECTED | reliability_not_demonstrated |
| 52895732 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.011190 WETH | 0.000027 WETH | 0.000000 WETH | 0.000006 WETH | 0.000021 WETH (0.0467 €) | 0.000021 WETH | 18.48 | 0.000 (n=25) | REJECTED | reliability_not_demonstrated |
| 52895732 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 27.299978 USDC | 0.065066 USDC | 0.000000 USDC | 0.015234 USDC | 0.049832 USDC (0.0458 €) | — | 18.25 | 0.000 (n=25) | REJECTED | reliability_not_demonstrated |
| 52895732 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.011101 WETH | 0.000026 WETH | 0.000000 WETH | 0.000006 WETH | 0.000020 WETH (0.0457 €) | — | 18.25 | 0.000 (n=25) | REJECTED | reliability_not_demonstrated |
| 52895732 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[sushiswap_v3]→USDC | 26.661639 USDC | 0.064178 USDC | 0.000000 USDC | 0.015234 USDC | 0.048944 USDC (0.0450 €) | — | 18.36 | 0.000 (n=25) | REJECTED | reliability_not_demonstrated |
| 52895732 | WETH→[sushiswap_v3]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.010882 WETH | 0.000026 WETH | 0.000000 WETH | 0.000006 WETH | 0.000020 WETH (0.0449 €) | — | 18.29 | 0.000 (n=25) | REJECTED | reliability_not_demonstrated |
| 52895732 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 24.964327 USDC | 0.054526 USDC | 0.000000 USDC | 0.015234 USDC | 0.039292 USDC (0.0361 €) | — | 15.74 | 0.000 (n=25) | REJECTED | reliability_not_demonstrated |
| 52895732 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.010207 WETH | 0.000022 WETH | 0.000000 WETH | 0.000006 WETH | 0.000016 WETH (0.0361 €) | — | 15.65 | 0.000 (n=25) | REJECTED | reliability_not_demonstrated |
| 52895732 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 22.008324 USDC | 0.053146 USDC | 0.000000 USDC | 0.015234 USDC | 0.037912 USDC (0.0349 €) | — | 17.23 | 0.000 (n=25) | REJECTED | reliability_not_demonstrated |
| 52895732 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.009021 WETH | 0.000022 WETH | 0.000000 WETH | 0.000006 WETH | 0.000015 WETH (0.0348 €) | — | 17.10 | 0.000 (n=25) | REJECTED | reliability_not_demonstrated |
| 52895745 | USDC→[pancakeswap_v3]→WETH→[uniswap_v2]→wIRON→[aerodrome]→USDC | 22.743455 USDC | 0.029660 USDC | 0.000000 USDC | 0.013170 USDC | 0.016490 USDC (0.0152 €) | — | 7.25 | 0.516 (n=5) | REJECTED | reliability_not_demonstrated |
| 52895745 | WETH→[uniswap_v2]→wIRON→[aerodrome]→USDC→[pancakeswap_v3]→WETH | 0.009288 WETH | 0.000012 WETH | 0.000000 WETH | 0.000005 WETH | 0.000007 WETH (0.0151 €) | 0.000007 WETH | 7.21 | 0.516 (n=5) | REJECTED | reliability_not_demonstrated |
| 52895745 | USDC→[uniswap_v3]→WETH→[uniswap_v2]→wIRON→[aerodrome]→USDC | 22.745063 USDC | 0.029596 USDC | 0.000000 USDC | 0.013170 USDC | 0.016426 USDC (0.0151 €) | — | 7.22 | 0.192 (n=8) | REJECTED | reliability_not_demonstrated |
| 52895745 | WETH→[uniswap_v2]→wIRON→[aerodrome]→USDC→[uniswap_v3]→WETH | 0.009288 WETH | 0.000012 WETH | 0.000000 WETH | 0.000005 WETH | 0.000007 WETH (0.0151 €) | 0.000007 WETH | 7.19 | 0.192 (n=8) | REJECTED | reliability_not_demonstrated |
| 52895850 | USDC→[uniswap_v3]→WETH→[uniswap_v2]→wIRON→[aerodrome]→USDC | 20.693037 USDC | 0.024568 USDC | 0.000000 USDC | 0.012044 USDC | 0.012524 USDC (0.0115 €) | 0.012524 USDC | 6.05 | 0.124 (n=12) | REJECTED | reliability_not_demonstrated |
| 52895850 | WETH→[uniswap_v2]→wIRON→[aerodrome]→USDC→[uniswap_v3]→WETH | 0.008400 WETH | 0.000010 WETH | 0.000000 WETH | 0.000005 WETH | 0.000005 WETH (0.0115 €) | 0.000005 WETH | 6.05 | 0.124 (n=12) | REJECTED | reliability_not_demonstrated |
| 52895850 | USDC→[pancakeswap_v3]→WETH→[uniswap_v2]→wIRON→[aerodrome]→USDC | 19.446366 USDC | 0.021635 USDC | 0.000000 USDC | 0.012044 USDC | 0.009591 USDC (0.0088 €) | — | 4.93 | 0.408 (n=6) | REJECTED | reliability_not_demonstrated |
| 52895850 | WETH→[uniswap_v2]→wIRON→[aerodrome]→USDC→[pancakeswap_v3]→WETH | 0.007880 WETH | 0.000009 WETH | 0.000000 WETH | 0.000005 WETH | 0.000004 WETH (0.0088 €) | 0.000004 WETH | 4.93 | 0.408 (n=6) | REJECTED | reliability_not_demonstrated |
| 52895745 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v2]→wIRON→[aerodrome]→USDC | 18.174814 USDC | 0.019107 USDC | 0.000000 USDC | 0.013170 USDC | 0.005937 USDC (0.0055 €) | — | 3.27 | 0.192 (n=8) | REJECTED | reliability_not_demonstrated |
| 52895745 | WETH→[uniswap_v2]→wIRON→[aerodrome]→USDC→[aerodrome_slipstream]→WETH | 0.007440 WETH | 0.000008 WETH | 0.000000 WETH | 0.000005 WETH | 0.000002 WETH (0.0054 €) | 0.000002 WETH | 3.23 | 0.192 (n=8) | REJECTED | reliability_not_demonstrated |
| 52895815 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v2]→wIRON→[aerodrome]→USDC | 15.079347 USDC | 0.017980 USDC | 0.000000 USDC | 0.012470 USDC | 0.005510 USDC (0.0051 €) | 0.005510 USDC | 3.65 | 0.151 (n=10) | REJECTED | reliability_not_demonstrated |

## Fiabilité et décision
- Observations ghost : 1669 ; taux observé 0.100 ; borne inférieure crédible (0.9) 0.091 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 9.1% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
