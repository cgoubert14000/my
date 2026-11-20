# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-20T14:03:29+00:00 ; durée 228.54 min ; blocs 59896587 → 59965137 (22008 vus)

## Connexion
- Requêtes RPC : 203002 ; erreurs : 0 ; latence p50/p95 : 110.2/915.9 ms
- Rafraîchissements d'état : 22008 ; âge des données au dernier bloc : 5.86 s ; changements de frais LP observés (pools à frais dynamiques) : 12140
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 37320 ; cycles déclenchés par événement : 7675 ; avance médiane sur le rafraîchissement multicall : 146 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 1,750.78 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 423 pools, 248 jetons, 12740 routes
- Par DEX : uniswap_v3 127, aerodrome_slipstream 86, aerodrome 171, pancakeswap_v3 26, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 1
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 146 (rejetés 2) → 551 jetons ; pools candidats 3579 (énumérés 255, par paires 0), mesurés 425, sous le plancher de 10000.0 $ : 2 → gardés 423 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDbC': 1.0, 'USDC': 1.0, 'WETH': 1747.036684, 'cbBTC': 61757.075443, 'AERO': 0.420112}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 77,300,525 | 1,750.780969 | 59965136 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 21,201,257 | 0.028328 | 59965136 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/USDC | 500 | 11,282,435 | 1,751.054821 | 59965136 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| uniswap_v3 | WETH/cbBTC | 3000 | 7,662,949 | 0.028289 | 59965136 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| aerodrome | WETH/VVV | 3000 | 6,482,938 | 84.694473 | 59965137 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | USDC/cbBTC | 500 | 6,011,824 | 0.000016 | 59965136 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,153,976 | 0.028318 | 59965136 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 3,545,661 | 2.447870 | 59965136 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/USDC | 100 | 3,397,393 | 1,750.828407 | 59965136 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,254,833 | 0.998711 | 59965136 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 2,694,324 | 39,515.737471 | 59965136 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 138 | 2,292,419 | 1,750.925042 | 59965136 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,912,468 | 0.000016 | 59965136 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 1,707,578 | 0.028297 | 59965136 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 1,648,824 | 1,142,907.098486 | 59965136 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,451,340 | 0.843780 | 59965136 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | USDC/cbBTC | 460 | 1,380,968 | 0.000016 | 59965136 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,324,502 | 0.000000 | 59965136 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,240,227 | 0.000016 | 59965136 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,224,331 | 0.006355 | 59965136 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,078,176 | 15.470228 | 59965136 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | USDC/SEND | 3000 | 1,059,687 | 86.533479 | 59965136 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,038,119 | 461.720647 | 59965136 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 995,469 | 16,291.302184 | 59965136 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v2 | WETH/USDC | 3000 | 992,513 | 1,752.439358 | 59965136 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| uniswap_v3 | WETH/AERO | 3000 | 974,272 | 4,285.239984 | 59965136 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v3 | WETH/VVV | 10000 | 971,803 | 84.712348 | 59965136 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/doginme | 10000 | 904,637 | 32,469,155.503356 | 59965136 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | USDC/VVV | 3000 | 902,533 | 0.048421 | 59965136 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | WETH/USDC | 3000 | 897,013 | 1,751.479191 | 59965137 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| uniswap_v3 | WETH/BRETT | 10000 | 815,597 | 530,504.437748 | 59965136 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | WETH/TOSHI | 10000 | 782,126 | 22,533,368.835447 | 59965136 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome | USDC/NOCK | 3000 | 779,713 | 70.374628 | 59965136 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | DRB/WETH | 10000 | 774,238 | 0.000000 | 59965136 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 774,117 | 0.001511 | 59965136 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| uniswap_v3 | XDP/USDC | 100 | 743,443 | 0.015460 | 59965136 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | WETH/USDC | 500 | 725,292 | 1,751.054478 | 59965136 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| pancakeswap_v3 | QUID/USDC | 100 | 722,698 | 0.046418 | 59965136 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| uniswap_v3 | WETH/MORPHO | 3000 | 715,646 | 1,113.050902 | 59965136 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome_slipstream | USDC/SAPIEN | 4520 | 712,652 | 24.766936 | 59965136 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v3 | WETH/USDC | 10000 | 695,089 | 1,743.566465 | 59965136 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/USDC | 100 | 612,140 | 1,750.868573 | 59965136 | `0xb4CB800910B228ED3d0834cF79D697127BBB00e5` |
| aerodrome | WETH/wstETH | 3000 | 594,414 | 0.798440 | 59965136 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | TIG/USDC | 10000 | 584,162 | 0.429119 | 59965136 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 556,620 | 4,707,926.067481 | 59965136 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome | WETH/AERO | 10000 | 535,114 | 4,262.695313 | 59965136 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | USDC/MAI (stable) | 3000 | 508,939 | 1.386531 | 59965136 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | WETH/BRETT | 3754 | 507,114 | 535,380.533144 | 59965136 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | FLOCK/USDC | 3000 | 494,115 | 0.031259 | 59965136 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| uniswap_v2 | WETH/NPC | 3000 | 458,021 | 185,945.670021 | 59965136 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | USDC/USDT | 8 | 456,507 | 1.001565 | 59965137 | `0xa41Bc0AFfbA7Fd420d186b84899d7ab2aC57fcD1` |
| pancakeswap_v3 | ELSA/USDC | 100 | 444,859 | 0.063190 | 59965136 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| aerodrome_slipstream | AERO/cbBTC | 1025 | 435,112 | 0.000007 | 59965136 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/MORPHO | 3034 | 387,708 | 1,112.719496 | 59965136 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| uniswap_v3 | WETH/uSOL | 3000 | 384,306 | 23.823406 | 59965136 | `0xab04A352D4EC8d0F1812A4E5EBe7807Fa67acD48` |
| aerodrome | cbBTC/EDGE | 7000 | 377,544 | 859,434.269057 | 59965136 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| uniswap_v3 | WETH/UNI | 10000 | 374,215 | 367.139832 | 59965136 | `0xAb365f161Dd501473a1ff0D2ef0dCE94E7398839` |
| aerodrome | AWE/USDC | 3000 | 367,032 | 0.056016 | 59965136 | `0xcb7f520d18141E36956fE0b3A6Bc3D4F11245521` |
| aerodrome | VIRTUAL/WETH | 10000 | 358,937 | 0.000230 | 59965136 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/VVV | 2715 | 357,435 | 84.726334 | 59965136 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |

## Recherche d'opportunités
- Cycles : 29682 ; routes examinées : 378148680 ; candidats optimisés : 441824 ; net attendu > 0 : 366 ; dernier cycle 1458.6 ms
- Rejets (moteur) : {'spread_below_threshold': 371042919, 'liquidity_below_min': 4154994, 'negative_expected_net': 441458, 'cycle_budget_exhausted': 44080, 'borrow_bound_too_small': 42720, 'pool_quarantined': 28688, 'no_price_reference': 245}
- Enregistrements de la session : 230776 ; net attendu > 0 : 366 ; simulés (eth_call de la vraie tx) : 42 (ok 6, échec 36) ; étiquettes ghost N+1 : 11/29 positives
- Décisions : {'REJECTED': 230776} ; motifs de rejet : {'below_safety_margin': 300, 'negative_expected_net': 230410, 'p_lower_below_threshold': 364, 'price_impact': 21, 'reliability_not_demonstrated': 2, 'simulation_failed': 36, 'stale_data': 27}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 59931575 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 686.457140 USDC | 0.119872 USDC | 0.000000 USDC | 0.004198 USDC | 0.115674 USDC (0.1064 €) | — | 1.69 | 0.111 (n=380) | REJECTED | below_safety_margin(115674<137291), p_lower_below_threshold(0.11<0.75) |
| 59931589 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 686.457140 USDC | 0.119872 USDC | 0.000000 USDC | 0.004198 USDC | 0.115674 USDC (0.1064 €) | — | 1.69 | 0.111 (n=380) | REJECTED | below_safety_margin(115674<137291), p_lower_below_threshold(0.11<0.75) |
| 59931575 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.397053 WETH | 0.000069 WETH | 0.000000 WETH | 0.000002 WETH | 0.000067 WETH (0.1063 €) | — | 1.68 | 0.111 (n=380) | REJECTED | below_safety_margin(66717612332529<79410520469949), p_lower_below_threshold(0.11<0.75) |
| 59931589 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.397053 WETH | 0.000069 WETH | 0.000000 WETH | 0.000002 WETH | 0.000067 WETH (0.1063 €) | — | 1.68 | 0.111 (n=380) | REJECTED | below_safety_margin(66717612332529<79410520469949), p_lower_below_threshold(0.11<0.75) |
| 59931575 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 283.558757 USDC | 0.042818 USDC | 0.000000 USDC | 0.003935 USDC | 0.038883 USDC (0.0358 €) | — | 1.37 | 0.098 (n=128) | REJECTED | below_safety_margin(38883<56711), p_lower_below_threshold(0.10<0.75) |
| 59931589 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 283.558757 USDC | 0.042818 USDC | 0.000000 USDC | 0.003935 USDC | 0.038883 USDC (0.0358 €) | — | 1.37 | 0.098 (n=128) | REJECTED | below_safety_margin(38883<56711), p_lower_below_threshold(0.10<0.75) |
| 59931575 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.163619 WETH | 0.000025 WETH | 0.000000 WETH | 0.000002 WETH | 0.000022 WETH (0.0357 €) | — | 1.37 | 0.098 (n=128) | REJECTED | below_safety_margin(22426759358077<32723734311580), p_lower_below_threshold(0.10<0.75) |
| 59931589 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.163619 WETH | 0.000025 WETH | 0.000000 WETH | 0.000002 WETH | 0.000022 WETH (0.0357 €) | — | 1.37 | 0.098 (n=128) | REJECTED | below_safety_margin(22426759358077<32723734311580), p_lower_below_threshold(0.10<0.75) |
| 59945018 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 404.546288 USDC | 0.038086 USDC | 0.000000 USDC | 0.003925 USDC | 0.034161 USDC (0.0314 €) | — | 0.84 | 0.110 (n=381) | REJECTED | below_safety_margin(34161<80909), p_lower_below_threshold(0.11<0.75) |
| 59945031 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 404.546288 USDC | 0.038086 USDC | 0.000000 USDC | 0.003925 USDC | 0.034161 USDC (0.0314 €) | — | 0.84 | 0.110 (n=381) | REJECTED | below_safety_margin(34161<80909), p_lower_below_threshold(0.11<0.75) |
| 59945018 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.232696 WETH | 0.000022 WETH | 0.000000 WETH | 0.000002 WETH | 0.000020 WETH (0.0314 €) | — | 0.84 | 0.110 (n=381) | REJECTED | below_safety_margin(19605436234526<46539270151610), p_lower_below_threshold(0.11<0.75) |
| 59945031 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.232696 WETH | 0.000022 WETH | 0.000000 WETH | 0.000002 WETH | 0.000020 WETH (0.0314 €) | — | 0.84 | 0.110 (n=381) | REJECTED | below_safety_margin(19605436234526<46539270151610), p_lower_below_threshold(0.11<0.75) |
| 59947219 | WETH→[uniswap_v3]→USDC→[aerodrome]→AERO→[pancakeswap_v3]→WETH | 0.041179 WETH | 0.000019 WETH | 0.000000 WETH | 0.000003 WETH | 0.000016 WETH (0.0250 €) | — | 3.80 | 0.307 (n=237) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.31<0.75) |
| 59947219 | USDC→[aerodrome]→AERO→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 71.380814 USDC | 0.032213 USDC | 0.000000 USDC | 0.005040 USDC | 0.027173 USDC (0.0250 €) | — | 3.81 | 0.307 (n=237) | REJECTED | p_lower_below_threshold(0.31<0.75) |
| 59947219 | WETH→[pancakeswap_v3]→USDC→[aerodrome]→AERO→[pancakeswap_v3]→WETH | 0.041160 WETH | 0.000018 WETH | 0.000000 WETH | 0.000003 WETH | 0.000015 WETH (0.0246 €) | — | 3.74 | 0.206 (n=140) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.21<0.75) |
| 59947219 | USDC→[aerodrome]→AERO→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 70.877588 USDC | 0.031808 USDC | 0.000000 USDC | 0.005040 USDC | 0.026768 USDC (0.0246 €) | — | 3.78 | 0.206 (n=140) | REJECTED | p_lower_below_threshold(0.21<0.75) |
| 59931546 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 316.509578 USDC | 0.026700 USDC | 0.000000 USDC | 0.004195 USDC | 0.022505 USDC (0.0207 €) | — | 0.71 | 0.111 (n=380) | REJECTED | below_safety_margin(22505<63301), p_lower_below_threshold(0.11<0.75) |
| 59931553 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 316.509578 USDC | 0.026700 USDC | 0.000000 USDC | 0.004195 USDC | 0.022505 USDC (0.0207 €) | — | 0.71 | 0.111 (n=380) | REJECTED | below_safety_margin(22505<63301), p_lower_below_threshold(0.11<0.75) |
| 59931546 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.183276 WETH | 0.000015 WETH | 0.000000 WETH | 0.000002 WETH | 0.000013 WETH (0.0207 €) | — | 0.71 | 0.111 (n=380) | REJECTED | below_safety_margin(12977313126533<36655103564637), p_lower_below_threshold(0.11<0.75) |
| 59931553 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.183276 WETH | 0.000015 WETH | 0.000000 WETH | 0.000002 WETH | 0.000013 WETH (0.0207 €) | — | 0.71 | 0.111 (n=380) | REJECTED | below_safety_margin(12977313126533<36655103564637), p_lower_below_threshold(0.11<0.75) |
| 59947219 | WETH→[aerodrome_slipstream]→USDC→[aerodrome]→AERO→[pancakeswap_v3]→WETH | 0.035564 WETH | 0.000014 WETH | 0.000000 WETH | 0.000003 WETH | 0.000011 WETH (0.0183 €) | — | 3.22 | 0.307 (n=237) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.31<0.75) |
| 59947219 | USDC→[aerodrome]→AERO→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 61.695896 USDC | 0.024937 USDC | 0.000000 USDC | 0.005040 USDC | 0.019897 USDC (0.0183 €) | — | 3.23 | 0.307 (n=237) | REJECTED | p_lower_below_threshold(0.31<0.75) |
| 59947198 | WETH→[uniswap_v3]→USDC→[aerodrome]→AERO→[pancakeswap_v3]→WETH | 0.032069 WETH | 0.000011 WETH | 0.000000 WETH | 0.000003 WETH | 0.000008 WETH (0.0133 €) | — | 2.59 | 0.358 (n=157) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.36<0.75) |
| 59947198 | USDC→[aerodrome]→AERO→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 55.535902 USDC | 0.019463 USDC | 0.000000 USDC | 0.005040 USDC | 0.014423 USDC (0.0133 €) | — | 2.60 | 0.358 (n=157) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.36<0.75) |
| 59947198 | WETH→[pancakeswap_v3]→USDC→[aerodrome]→AERO→[pancakeswap_v3]→WETH | 0.031929 WETH | 0.000011 WETH | 0.000000 WETH | 0.000003 WETH | 0.000008 WETH (0.0130 €) | — | 2.54 | 0.219 (n=91) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.22<0.75) |

## Fiabilité et décision
- Observations ghost : 8619 ; taux observé 0.228 ; borne inférieure crédible (0.9) 0.223 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 22.3% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
