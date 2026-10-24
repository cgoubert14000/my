# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-24T07:48:18+00:00 ; durée 120.02 min ; blocs 53015772 → 53019373 (3600 vus)

## Connexion
- Requêtes RPC : 44488 ; erreurs : 3 ; latence p50/p95 : 145.2/643.4 ms
- Rafraîchissements d'état : 3600 ; âge des données au dernier bloc : 2.48 s ; changements de frais LP observés (pools à frais dynamiques) : 3123
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 32321 ; cycles déclenchés par événement : 3717 ; avance médiane sur le rafraîchissement multicall : 348 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,379.18 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 540 pools, 312 jetons, 19252 routes
- Par DEX : uniswap_v3 140, aerodrome 217, aerodrome_slipstream 135, pancakeswap_v3 31, uniswap_v2 13, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 196 (rejetés 2) → 601 jetons ; pools candidats 3859 (énumérés 351, par paires 0), mesurés 542, sous le plancher de 10000.0 $ : 2 → gardés 540 (max 1500) ; prix des hubs : {'USDC': 1.0, 'USDbC': 1.0, 'DAI': 1.0, 'WETH': 2380.141625, 'AERO': 0.727873, 'cbBTC': 80675.114522}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 156,177,528 | 2,379.177911 | 53019373 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 17,086,926 | 0.029442 | 53019373 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 12,385,909 | 96.801642 | 53019373 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,197,604 | 0.029387 | 53019373 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| aerodrome | USDC/AERO | 3000 | 9,713,415 | 1.382566 | 53019373 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,554,024 | 0.000012 | 53019373 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 8,636,215 | 2,376.448621 | 53019373 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 8,548,146 | 0.029400 | 53019373 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,055,502 | 0.001650 | 53019373 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 330 | 6,310,117 | 0.000012 | 53019373 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 150 | 5,504,995 | 2,375.965504 | 53019373 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,452,979 | 0.029431 | 53019373 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | USDC/cbBTC | 400 | 4,870,332 | 0.000012 | 53019373 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,561,868 | 2,376.164390 | 53019373 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,253,485 | 0.999263 | 53019373 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/USDC | 3000 | 4,100,130 | 2,371.274062 | 53019373 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome | WETH/KTA | 3000 | 3,966,338 | 34,072.930118 | 53019373 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | VIRTUAL/WETH | 10000 | 3,330,276 | 0.000270 | 53019373 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/USDT | 403 | 2,793,155 | 2,380.962414 | 53019373 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome_slipstream | WETH/VVV | 2700 | 2,533,628 | 96.828750 | 53019373 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,263,255 | 407.265680 | 53019373 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | WETH/FAI | 10000 | 2,131,353 | 1,263,317.112174 | 53019373 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome | WETH/AERO | 10000 | 1,997,662 | 3,273.527761 | 53019373 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,934,360 | 0.000000 | 53019373 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,913,476 | 0.000012 | 53019373 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v3 | XDP/USDC | 100 | 1,742,258 | 0.017684 | 53019373 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,740,929 | 0.000012 | 53019373 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,549,717 | 1.610679 | 53019373 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | WETH/AERO | 3000 | 1,489,362 | 3,285.648912 | 53019373 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,459,688 | 0.824979 | 53019373 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,387,226 | 13,824.239047 | 53019373 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,384,147 | 0.005137 | 53019373 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,331,053 | 2,376.405845 | 53019373 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,276,524 | 0.000268 | 53019373 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | WETH/msETH (stable) | 500 | 1,242,429 | 2.308508 | 53019373 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome | USDC/SEND | 3000 | 1,225,295 | 64.723347 | 53019373 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | DRB/WETH | 10000 | 1,204,476 | 0.000000 | 53019373 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/doginme | 10000 | 1,184,733 | 35,426,944.939198 | 53019373 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | WETH/WELL | 10000 | 1,154,348 | 1,119,106.419977 | 53019373 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,140,551 | 492,039.665164 | 53019373 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | USDC/NOCK | 3000 | 1,134,136 | 48.695204 | 53019373 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,112,060 | 16.689655 | 53019373 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | WETH/EDEL | 7000 | 1,084,010 | 73,840.444209 | 53019373 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,052,303 | 21,442,258.356506 | 53019373 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | USDC/VVV | 3000 | 1,044,751 | 0.040738 | 53019373 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,037,040 | 17.117202 | 53019373 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 971,333 | 23.275941 | 53019373 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| uniswap_v3 | WETH/MORPHO | 3000 | 938,672 | 1,075.742960 | 53019373 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | uXRP/WETH | 3000 | 903,934 | 0.000541 | 53019373 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| pancakeswap_v3 | QUID/USDC | 100 | 892,464 | 0.072813 | 53019373 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 882,708 | 17.821156 | 53019373 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 870,205 | 0.000009 | 53019373 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v2 | WETH/USDC | 3000 | 855,361 | 2,379.598689 | 53019373 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome | weETH_04c0/WETH | 500 | 818,841 | 1.105904 | 53019373 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome | WETH/wstETH | 3000 | 805,614 | 0.803010 | 53019373 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | WETH/USDC | 10000 | 789,653 | 2,373.719186 | 53019373 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/VVV | 10000 | 782,611 | 96.498774 | 53019373 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 766,372 | 0.637278 | 53019373 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 760,075 | 4,623,605.368989 | 53019373 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v2 | WETH/NPC | 3000 | 730,650 | 133,369.876928 | 53019373 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |

## Recherche d'opportunités
- Cycles : 7316 ; routes examinées : 140847632 ; candidats optimisés : 488354 ; net attendu > 0 : 35 ; dernier cycle 94.4 ms
- Rejets (moteur) : {'spread_below_threshold': 138323547, 'liquidity_below_min': 2028356, 'negative_expected_net': 488319, 'borrow_bound_too_small': 7315, 'cycle_budget_exhausted': 60}
- Enregistrements de la session : 488354 ; net attendu > 0 : 35 ; simulés (eth_call de la vraie tx) : 8 (ok 6, échec 2) ; étiquettes ghost N+1 : 0/4 positives
- Décisions : {'REJECTED': 488354} ; motifs de rejet : {'below_safety_margin': 27, 'negative_expected_net': 488319, 'p_lower_below_threshold': 16, 'reliability_not_demonstrated': 19, 'simulation_failed': 2}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53019008 | WETH→[pancakeswap_v3]→USDC→[aerodrome]→WETH | 0.141970 WETH | 0.000025 WETH | 0.000000 WETH | 0.000002 WETH | 0.000023 WETH (0.0496 €) | — | 1.59 | 0.001 (n=7) | REJECTED | below_safety_margin(22640535312575<28393906814056), reliability_not_demonstrated |
| 53019008 | USDC→[aerodrome]→WETH→[pancakeswap_v3]→USDC | 337.717587 USDC | 0.059181 USDC | 0.000000 USDC | 0.005380 USDC | 0.053801 USDC (0.0495 €) | — | 1.59 | 0.001 (n=7) | REJECTED | below_safety_margin(53801<67543), reliability_not_demonstrated |
| 53019008 | WETH→[aerodrome_slipstream]→USDC→[aerodrome]→WETH | 0.136296 WETH | 0.000022 WETH | 0.000000 WETH | 0.000002 WETH | 0.000020 WETH (0.0446 €) | — | 1.49 | 0.136 (n=11) | REJECTED | below_safety_margin(20361812975464<27259269285167), reliability_not_demonstrated |
| 53019008 | USDC→[aerodrome]→WETH→[aerodrome_slipstream]→USDC | 323.142646 USDC | 0.053403 USDC | 0.000000 USDC | 0.005019 USDC | 0.048384 USDC (0.0445 €) | — | 1.50 | 0.136 (n=11) | REJECTED | below_safety_margin(48384<64628), reliability_not_demonstrated |
| 53019008 | WETH→[uniswap_v3]→USDC→[aerodrome]→WETH | 0.095044 WETH | 0.000017 WETH | 0.000000 WETH | 0.000002 WETH | 0.000015 WETH (0.0335 €) | — | 1.61 | 0.136 (n=11) | REJECTED | below_safety_margin(15307063055705<19008839397401), reliability_not_demonstrated |
| 53019008 | USDC→[aerodrome]→WETH→[uniswap_v3]→USDC | 224.652872 USDC | 0.041386 USDC | 0.000000 USDC | 0.005019 USDC | 0.036367 USDC (0.0335 €) | — | 1.62 | 0.136 (n=11) | REJECTED | below_safety_margin(36367<44930), reliability_not_demonstrated |
| 53019008 | USDC→[aerodrome]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 225.886738 USDC | 0.026678 USDC | 0.000000 USDC | 0.006827 USDC | 0.019851 USDC (0.0183 €) | — | 0.88 | 0.063 (n=45) | REJECTED | below_safety_margin(19851<45177), p_lower_below_threshold(0.06<0.75) |
| 53019008 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[aerodrome]→WETH | 0.101473 WETH | 0.000011 WETH | 0.000000 WETH | 0.000003 WETH | 0.000008 WETH (0.0179 €) | — | 0.81 | 0.063 (n=45) | REJECTED | below_safety_margin(8196313070011<20294581494877), p_lower_below_threshold(0.06<0.75) |
| 53019008 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome]→WETH→[pancakeswap_v3]→cbBTC | 0.002508 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0178 €) | — | 0.96 | 0.063 (n=45) | REJECTED | below_safety_margin(24<50), p_lower_below_threshold(0.06<0.75) |
| 53019008 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome]→WETH→[pancakeswap_v3]→cbBTC | 0.002333 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0164 €) | — | 0.94 | 0.063 (n=45) | REJECTED | below_safety_margin(22<46), p_lower_below_threshold(0.06<0.75) |
| 53019008 | USDC→[aerodrome]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 181.759599 USDC | 0.024323 USDC | 0.000000 USDC | 0.006827 USDC | 0.017496 USDC (0.0161 €) | — | 0.96 | 0.063 (n=45) | REJECTED | below_safety_margin(17496<36351), p_lower_below_threshold(0.06<0.75) |
| 53019008 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[aerodrome]→WETH | 0.070752 WETH | 0.000010 WETH | 0.000000 WETH | 0.000003 WETH | 0.000007 WETH (0.0160 €) | — | 1.03 | 0.063 (n=45) | REJECTED | below_safety_margin(7315168126583<14150443254096), p_lower_below_threshold(0.06<0.75) |
| 53015828 | USDC→[pancakeswap_v3]→PLAY→[aerodrome_slipstream]→USDC | 30.757704 USDC | 0.021524 USDC | 0.000000 USDC | 0.005347 USDC | 0.016177 USDC (0.0149 €) | — | 5.26 | 0.003 (n=111) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 53015828 | USDC→[pancakeswap_v3]→PLAY→[aerodrome]→USDC | 13.708061 USDC | 0.018663 USDC | 0.000000 USDC | 0.005018 USDC | 0.013645 USDC (0.0126 €) | — | 9.95 | 0.001 (n=10) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53018116 | USDC→[pancakeswap_v3]→PLAY→[aerodrome]→USDC | 10.213386 USDC | 0.010336 USDC | 0.000000 USDC | 0.005014 USDC | 0.005322 USDC (0.0049 €) | 0.005322 USDC | 5.21 | 0.025 (n=12) | REJECTED | reliability_not_demonstrated |
| 53018116 | USDC→[pancakeswap_v3]→PLAY→[aerodrome]→USDC | 10.213386 USDC | 0.010336 USDC | 0.000000 USDC | 0.005014 USDC | 0.005322 USDC (0.0049 €) | 0.005322 USDC | 5.21 | 0.025 (n=12) | REJECTED | reliability_not_demonstrated |
| 53018111 | USDC→[pancakeswap_v3]→PLAY→[aerodrome_slipstream]→USDC | 20.381325 USDC | 0.009483 USDC | 0.000000 USDC | 0.005342 USDC | 0.004141 USDC (0.0038 €) | 0.004141 USDC | 2.03 | 0.019 (n=77) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 53018111 | USDC→[pancakeswap_v3]→PLAY→[aerodrome_slipstream]→USDC | 20.381325 USDC | 0.009483 USDC | 0.000000 USDC | 0.005342 USDC | 0.004141 USDC (0.0038 €) | 0.004141 USDC | 2.03 | 0.019 (n=77) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 53019008 | USDC→[aerodrome]→WETH→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 80.151250 USDC | 0.010911 USDC | 0.000000 USDC | 0.006827 USDC | 0.004084 USDC (0.0038 €) | — | 0.51 | 0.170 (n=31) | REJECTED | below_safety_margin(4084<16030), p_lower_below_threshold(0.17<0.75) |
| 53019008 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome]→WETH→[aerodrome_slipstream]→cbBTC | 0.000942 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0037 €) | — | 0.53 | 0.170 (n=31) | REJECTED | below_safety_margin(5<18), p_lower_below_threshold(0.17<0.75) |
| 53019008 | WETH→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC→[aerodrome]→WETH | 0.033063 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0036 €) | — | 0.50 | 0.170 (n=31) | REJECTED | below_safety_margin(1664914471968<6612619923972), p_lower_below_threshold(0.17<0.75) |
| 53018111 | USDC→[pancakeswap_v3]→PLAY→[aerodrome]→USDC | 9.361975 USDC | 0.008739 USDC | 0.000000 USDC | 0.005014 USDC | 0.003725 USDC (0.0034 €) | 0.003725 USDC | 3.98 | 0.027 (n=11) | REJECTED | reliability_not_demonstrated |
| 53018111 | USDC→[pancakeswap_v3]→PLAY→[aerodrome]→USDC | 9.361975 USDC | 0.008739 USDC | 0.000000 USDC | 0.005014 USDC | 0.003725 USDC (0.0034 €) | 0.003725 USDC | 3.98 | 0.027 (n=11) | REJECTED | reliability_not_demonstrated |
| 53019008 | WETH→[uniswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[aerodrome]→WETH | 0.050807 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0030 €) | — | 0.27 | 0.170 (n=31) | REJECTED | below_safety_margin(1379670709875<10161408018155), p_lower_below_threshold(0.17<0.75) |
| 53019008 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome]→WETH→[uniswap_v3]→cbBTC | 0.001724 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0030 €) | — | 0.23 | 0.170 (n=31) | REJECTED | below_safety_margin(4<34), p_lower_below_threshold(0.17<0.75) |

## Fiabilité et décision
- Observations ghost : 2097 ; taux observé 0.098 ; borne inférieure crédible (0.9) 0.090 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 9.0% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
