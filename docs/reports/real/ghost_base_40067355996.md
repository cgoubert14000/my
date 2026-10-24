# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-24T08:25:48+00:00 ; durée 157.51 min ; blocs 53015772 → 53020497 (4724 vus)

## Connexion
- Requêtes RPC : 58332 ; erreurs : 8 ; latence p50/p95 : 133.3/577.3 ms
- Rafraîchissements d'état : 4724 ; âge des données au dernier bloc : 2.72 s ; changements de frais LP observés (pools à frais dynamiques) : 4485
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 50950 ; cycles déclenchés par événement : 4974 ; avance médiane sur le rafraîchissement multicall : 288 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,374.99 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 540 pools, 312 jetons, 19252 routes
- Par DEX : uniswap_v3 140, aerodrome 217, aerodrome_slipstream 135, pancakeswap_v3 31, uniswap_v2 13, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 196 (rejetés 2) → 601 jetons ; pools candidats 3859 (énumérés 351, par paires 0), mesurés 542, sous le plancher de 10000.0 $ : 2 → gardés 540 (max 1500) ; prix des hubs : {'USDC': 1.0, 'USDbC': 1.0, 'DAI': 1.0, 'WETH': 2380.141625, 'AERO': 0.727873, 'cbBTC': 80675.114522}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 156,014,051 | 2,374.986079 | 53020498 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 17,045,202 | 0.029388 | 53020498 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 12,325,393 | 97.410374 | 53020498 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,186,808 | 0.029387 | 53020498 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| aerodrome | USDC/AERO | 3000 | 9,679,251 | 1.390158 | 53020498 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,554,402 | 0.000012 | 53020498 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 8,625,167 | 2,370.653878 | 53020498 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 8,540,732 | 0.029401 | 53020498 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,057,476 | 0.001651 | 53020498 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 334 | 6,310,309 | 0.000012 | 53020498 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 150 | 5,487,726 | 2,371.137992 | 53020498 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,438,961 | 0.029379 | 53020498 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | USDC/cbBTC | 412 | 4,870,577 | 0.000012 | 53020498 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,502,447 | 2,371.457053 | 53020498 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,253,761 | 0.999263 | 53020498 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/USDC | 3000 | 4,096,487 | 2,364.296943 | 53020498 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome | WETH/KTA | 3000 | 3,959,310 | 34,073.608935 | 53020498 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | VIRTUAL/WETH | 10000 | 3,322,628 | 0.000270 | 53020498 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/USDT | 403 | 2,790,978 | 2,375.679118 | 53020498 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome_slipstream | WETH/VVV | 2700 | 2,521,514 | 97.442061 | 53020498 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,260,698 | 406.566925 | 53020498 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | WETH/FAI | 10000 | 2,127,597 | 1,263,317.112174 | 53020498 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome | WETH/AERO | 10000 | 1,990,436 | 3,273.820455 | 53020498 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,931,373 | 0.000000 | 53020498 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,913,536 | 0.000012 | 53020498 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,741,010 | 0.000012 | 53020498 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | XDP/USDC | 100 | 1,740,024 | 0.017647 | 53020498 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,549,717 | 1.610679 | 53020498 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | WETH/AERO | 3000 | 1,483,976 | 3,296.084953 | 53020498 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,459,823 | 0.824842 | 53020498 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,387,269 | 13,846.954346 | 53020498 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,381,708 | 0.005137 | 53020498 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,328,018 | 2,371.257558 | 53020498 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,273,594 | 0.000268 | 53020498 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | WETH/msETH (stable) | 500 | 1,237,892 | 2.305750 | 53020498 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome | USDC/SEND | 3000 | 1,225,295 | 64.723347 | 53020498 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | DRB/WETH | 10000 | 1,202,668 | 0.000000 | 53020498 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/doginme | 10000 | 1,182,948 | 35,408,980.771479 | 53020498 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | WETH/WELL | 10000 | 1,152,301 | 1,119,131.144339 | 53020498 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome | USDC/NOCK | 3000 | 1,140,011 | 48.194613 | 53020498 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,138,187 | 492,454.570560 | 53020498 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,108,378 | 16.722695 | 53020498 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | WETH/EDEL | 7000 | 1,082,225 | 73,823.526979 | 53020498 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,050,449 | 21,442,258.356506 | 53020498 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | USDC/VVV | 3000 | 1,039,721 | 0.041096 | 53020498 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,035,896 | 17.168668 | 53020498 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 969,622 | 23.275906 | 53020498 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| uniswap_v3 | WETH/MORPHO | 3000 | 934,977 | 1,078.952860 | 53020498 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | uXRP/WETH | 3000 | 900,169 | 0.000539 | 53020498 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 882,732 | 17.820350 | 53020498 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 867,867 | 0.000009 | 53020498 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| pancakeswap_v3 | QUID/USDC | 100 | 854,658 | 0.066175 | 53020498 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| uniswap_v2 | WETH/USDC | 3000 | 854,608 | 2,375.358015 | 53020498 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome | weETH_04c0/WETH | 500 | 817,398 | 1.105904 | 53020498 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome | WETH/wstETH | 3000 | 804,195 | 0.803010 | 53020498 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | WETH/USDC | 10000 | 789,229 | 2,373.719186 | 53020498 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/VVV | 10000 | 778,935 | 96.731427 | 53020498 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 764,830 | 0.634913 | 53020498 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 758,642 | 4,624,753.613571 | 53020498 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 730,003 | 0.668128 | 53020498 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |

## Recherche d'opportunités
- Cycles : 9697 ; routes examinées : 186686644 ; candidats optimisés : 661051 ; net attendu > 0 : 57 ; dernier cycle 171.1 ms
- Rejets (moteur) : {'spread_below_threshold': 183422302, 'liquidity_below_min': 2593535, 'negative_expected_net': 660994, 'borrow_bound_too_small': 9696, 'cycle_budget_exhausted': 60}
- Enregistrements de la session : 661051 ; net attendu > 0 : 57 ; simulés (eth_call de la vraie tx) : 11 (ok 6, échec 5) ; étiquettes ghost N+1 : 0/7 positives
- Décisions : {'REJECTED': 661051} ; motifs de rejet : {'below_safety_margin': 28, 'negative_expected_net': 660994, 'p_lower_below_threshold': 19, 'reliability_not_demonstrated': 38, 'simulation_failed': 5}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53019828 | USDC→[uniswap_v3]→ZORA→[aerodrome_slipstream]→USDC | 433.202296 USDC | 2.497024 USDC | 0.000000 USDC | 0.005697 USDC | 2.491327 USDC (2.2920 €) | — | 57.51 | 0.006 (n=1) | REJECTED | reliability_not_demonstrated |
| 53019828 | WETH→[uniswap_v3]→ZORA→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.035915 WETH | 0.000213 WETH | 0.000000 WETH | 0.000003 WETH | 0.000209 WETH (0.4580 €) | — | 58.32 | 0.001 (n=10) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53019828 | WETH→[uniswap_v3]→ZORA→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→WETH | 0.035861 WETH | 0.000212 WETH | 0.000000 WETH | 0.000003 WETH | 0.000209 WETH (0.4569 €) | — | 58.27 | 0.001 (n=10) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53019828 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→ZORA→[aerodrome_slipstream]→USDC | 84.993781 USDC | 0.504007 USDC | 0.000000 USDC | 0.007503 USDC | 0.496504 USDC (0.4568 €) | — | 58.42 | 0.001 (n=10) | REJECTED | reliability_not_demonstrated |
| 53019828 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→ZORA→[aerodrome_slipstream]→USDC | 84.883041 USDC | 0.502795 USDC | 0.000000 USDC | 0.007503 USDC | 0.495292 USDC (0.4557 €) | — | 58.35 | 0.001 (n=10) | REJECTED | reliability_not_demonstrated |
| 53019828 | WETH→[uniswap_v3]→ZORA→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.035568 WETH | 0.000210 WETH | 0.000000 WETH | 0.000003 WETH | 0.000207 WETH (0.4524 €) | — | 58.16 | 0.001 (n=10) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53019828 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→ZORA→[aerodrome_slipstream]→USDC | 84.325109 USDC | 0.497921 USDC | 0.000000 USDC | 0.007503 USDC | 0.490418 USDC (0.4512 €) | — | 58.16 | 0.001 (n=10) | REJECTED | reliability_not_demonstrated |
| 53019828 | WETH→[uniswap_v3]→ZORA→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.033945 WETH | 0.000190 WETH | 0.000000 WETH | 0.000003 WETH | 0.000187 WETH (0.4096 €) | — | 55.18 | 0.001 (n=10) | REJECTED | reliability_not_demonstrated |
| 53019828 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→ZORA→[aerodrome_slipstream]→USDC | 80.399853 USDC | 0.451418 USDC | 0.000000 USDC | 0.007142 USDC | 0.444276 USDC (0.4087 €) | — | 55.26 | 0.001 (n=10) | REJECTED | reliability_not_demonstrated |
| 53019828 | WETH→[uniswap_v3]→ZORA→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.033821 WETH | 0.000189 WETH | 0.000000 WETH | 0.000003 WETH | 0.000186 WETH (0.4067 €) | — | 54.99 | 0.001 (n=10) | REJECTED | reliability_not_demonstrated |
| 53019828 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→ZORA→[aerodrome_slipstream]→USDC | 80.207722 USDC | 0.448293 USDC | 0.000000 USDC | 0.007142 USDC | 0.441151 USDC (0.4059 €) | — | 55.00 | 0.001 (n=10) | REJECTED | reliability_not_demonstrated |
| 53019828 | WETH→[uniswap_v3]→ZORA→[aerodrome_slipstream]→USDC→[sushiswap_v3]→WETH | 0.032461 WETH | 0.000180 WETH | 0.000000 WETH | 0.000003 WETH | 0.000177 WETH (0.3872 €) | — | 54.54 | 0.001 (n=10) | REJECTED | reliability_not_demonstrated |
| 53019828 | USDC→[sushiswap_v3]→WETH→[uniswap_v3]→ZORA→[aerodrome_slipstream]→USDC | 76.947843 USDC | 0.427298 USDC | 0.000000 USDC | 0.007142 USDC | 0.420156 USDC (0.3865 €) | — | 54.60 | 0.001 (n=10) | REJECTED | reliability_not_demonstrated |
| 53019828 | WETH→[uniswap_v3]→ZORA→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→WETH | 0.029495 WETH | 0.000171 WETH | 0.000000 WETH | 0.000003 WETH | 0.000168 WETH (0.3668 €) | — | 56.86 | 0.001 (n=10) | REJECTED | reliability_not_demonstrated |
| 53019828 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→ZORA→[aerodrome_slipstream]→USDC | 69.941036 USDC | 0.405553 USDC | 0.000000 USDC | 0.007142 USDC | 0.398411 USDC (0.3665 €) | — | 56.96 | 0.001 (n=10) | REJECTED | reliability_not_demonstrated |
| 53019828 | USDC→[aerodrome]→WETH→[uniswap_v3]→ZORA→[aerodrome_slipstream]→USDC | 59.066632 USDC | 0.244343 USDC | 0.000000 USDC | 0.006814 USDC | 0.237529 USDC (0.2185 €) | — | 40.21 | 0.003 (n=93) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53019828 | WETH→[uniswap_v3]→ZORA→[aerodrome_slipstream]→USDC→[aerodrome]→WETH | 0.024837 WETH | 0.000103 WETH | 0.000000 WETH | 0.000003 WETH | 0.000100 WETH (0.2183 €) | — | 40.20 | 0.003 (n=93) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53019828 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→ZORA→[aerodrome_slipstream]→USDC | 44.184247 USDC | 0.135897 USDC | 0.000000 USDC | 0.007142 USDC | 0.128755 USDC (0.1185 €) | — | 29.14 | 0.001 (n=10) | REJECTED | reliability_not_demonstrated |
| 53019828 | WETH→[uniswap_v3]→ZORA→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.018574 WETH | 0.000057 WETH | 0.000000 WETH | 0.000003 WETH | 0.000054 WETH (0.1181 €) | — | 29.07 | 0.001 (n=10) | REJECTED | reliability_not_demonstrated |
| 53019828 | USDC→[uniswap_v2]→WETH→[uniswap_v3]→ZORA→[aerodrome_slipstream]→USDC | 42.080379 USDC | 0.127250 USDC | 0.000000 USDC | 0.006404 USDC | 0.120846 USDC (0.1112 €) | — | 28.72 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 53019828 | WETH→[uniswap_v3]→ZORA→[aerodrome_slipstream]→USDC→[uniswap_v2]→WETH | 0.017676 WETH | 0.000053 WETH | 0.000000 WETH | 0.000003 WETH | 0.000051 WETH (0.1108 €) | — | 28.66 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 53019008 | WETH→[pancakeswap_v3]→USDC→[aerodrome]→WETH | 0.141970 WETH | 0.000025 WETH | 0.000000 WETH | 0.000002 WETH | 0.000023 WETH (0.0496 €) | — | 1.59 | 0.001 (n=7) | REJECTED | below_safety_margin(22640535312575<28393906814056), reliability_not_demonstrated |
| 53019008 | USDC→[aerodrome]→WETH→[pancakeswap_v3]→USDC | 337.717587 USDC | 0.059181 USDC | 0.000000 USDC | 0.005380 USDC | 0.053801 USDC (0.0495 €) | — | 1.59 | 0.001 (n=7) | REJECTED | below_safety_margin(53801<67543), reliability_not_demonstrated |
| 53019008 | WETH→[aerodrome_slipstream]→USDC→[aerodrome]→WETH | 0.136296 WETH | 0.000022 WETH | 0.000000 WETH | 0.000002 WETH | 0.000020 WETH (0.0446 €) | — | 1.49 | 0.136 (n=11) | REJECTED | below_safety_margin(20361812975464<27259269285167), reliability_not_demonstrated |
| 53019008 | USDC→[aerodrome]→WETH→[aerodrome_slipstream]→USDC | 323.142646 USDC | 0.053403 USDC | 0.000000 USDC | 0.005019 USDC | 0.048384 USDC (0.0445 €) | — | 1.50 | 0.136 (n=11) | REJECTED | below_safety_margin(48384<64628), reliability_not_demonstrated |

## Fiabilité et décision
- Observations ghost : 2100 ; taux observé 0.098 ; borne inférieure crédible (0.9) 0.090 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 9.0% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
