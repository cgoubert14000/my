# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-01T00:32:22+00:00 ; durée 67.61 min ; blocs 53349866 → 53351895 (2027 vus)

## Connexion
- Requêtes RPC : 24538 ; erreurs : 0 ; latence p50/p95 : 68.3/925.0 ms
- Rafraîchissements d'état : 2027 ; âge des données au dernier bloc : 3.84 s ; changements de frais LP observés (pools à frais dynamiques) : 1484
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 14497 ; cycles déclenchés par événement : 1840 ; avance médiane sur le rafraîchissement multicall : 404 ms
- Gaz : base fee 0.005001 gwei ; prix ETH (pool le plus profond) : 2,256.86 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 503 pools, 291 jetons, 18668 routes
- Par DEX : uniswap_v3 140, aerodrome_slipstream 114, aerodrome 206, pancakeswap_v3 29, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 178 (rejetés 2) → 583 jetons ; pools candidats 3742 (énumérés 319, par paires 0), mesurés 506, sous le plancher de 10000.0 $ : 3 → gardés 503 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'DAI': 1.0, 'USDC': 1.0, 'WETH': 2257.094934, 'cbBTC': 77437.995276, 'AERO': 0.643751}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 150,527,939 | 2,256.859206 | 53351896 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,097,156 | 0.029091 | 53351896 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,320,014 | 0.000013 | 53351896 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,071,239 | 0.029089 | 53351896 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| aerodrome | WETH/VVV | 3000 | 7,927,840 | 95.906630 | 53351896 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/USDC | 500 | 7,869,886 | 2,255.839709 | 53351896 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,686,537 | 0.001609 | 53351896 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 5,774,581 | 1.544493 | 53351896 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,258,570 | 0.029098 | 53351896 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,084,771 | 0.998852 | 53351896 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome_slipstream | WETH/USDC | 150 | 4,057,492 | 2,256.491464 | 53351896 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/USDC | 100 | 3,923,250 | 2,256.725973 | 53351896 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | WETH/KTA | 3000 | 3,548,200 | 37,863.422163 | 53351896 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,692,575 | 0.029101 | 53351896 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2700 | 2,426,958 | 95.909801 | 53351896 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | WETH/FAI | 10000 | 2,073,712 | 1,200,829.160231 | 53351896 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 448 | 1,963,395 | 0.000013 | 53351896 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,757,691 | 0.000000 | 53351896 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,710,133 | 0.017283 | 53351896 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,676,275 | 0.000013 | 53351896 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v2 | WETH/USDC | 3000 | 1,596,641 | 2,257.330357 | 53351896 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,583,992 | 0.000013 | 53351896 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,551,297 | 424.725857 | 53351896 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,546,920 | 1.490152 | 53351896 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,457,383 | 0.825799 | 53351896 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,439,462 | 3,481.384448 | 53351896 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | WETH/USDC | 3000 | 1,409,373 | 2,259.553240 | 53351896 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,346,985 | 2,255.794464 | 53351896 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,324,189 | 0.005182 | 53351896 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/cbBTC | 338 | 1,306,172 | 0.000013 | 53351896 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,305,938 | 14,588.573974 | 53351896 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | USDC/SEND | 3000 | 1,174,224 | 70.475891 | 53351896 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,169,591 | 31,611,899.096659 | 53351896 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,065,411 | 515,513.256143 | 53351896 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,046,302 | 0.000000 | 53351896 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,028,926 | 21,602,616.147259 | 53351896 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome | WETH/EDEL | 7000 | 1,005,350 | 76,946.552554 | 53351896 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/VVV | 10000 | 1,001,697 | 96.085144 | 53351896 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | USDC/VVV | 3000 | 991,132 | 0.042573 | 53351896 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome_slipstream | USDC/VELVET | 100 | 989,743 | 19.521052 | 53351896 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | USDC/NOCK | 3000 | 977,142 | 65.565745 | 53351896 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome | WETH/WELL | 10000 | 953,583 | 1,171,106.372869 | 53351896 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/MORPHO | 3000 | 950,554 | 947.054368 | 53351896 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/USDC | 10000 | 924,184 | 2,242.032039 | 53351896 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome | WETH/AERO | 10000 | 881,222 | 3,494.893415 | 53351896 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | uXRP/WETH | 3000 | 864,865 | 0.000550 | 53351896 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 840,428 | 19.353497 | 53351896 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 833,067 | 0.062565 | 53351896 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 764,170 | 0.803065 | 53351896 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| aerodrome | VIRTUAL/WETH | 10000 | 734,804 | 0.000261 | 53351896 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 723,724 | 0.590446 | 53351896 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 722,400 | 4,611,407.396929 | 53351896 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 696,860 | 0.000008 | 53351896 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v2 | WETH/NPC | 3000 | 672,975 | 141,838.129506 | 53351896 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 660,722 | 519,377.465504 | 53351896 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome | WETH/msETH (stable) | 500 | 658,111 | 2.336543 | 53351896 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | TIG/USDC | 10000 | 656,919 | 0.543398 | 53351896 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 614,553 | 0.093526 | 53351896 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| aerodrome | WETH/bsdETH | 100 | 605,721 | 0.916224 | 53351896 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome_slipstream | WETH/MORPHO | 2814 | 558,161 | 947.251967 | 53351896 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |

## Recherche d'opportunités
- Cycles : 3866 ; routes examinées : 72170488 ; candidats optimisés : 182802 ; net attendu > 0 : 126 ; dernier cycle 212.7 ms
- Rejets (moteur) : {'spread_below_threshold': 71162015, 'liquidity_below_min': 813991, 'negative_expected_net': 182676, 'unquotable': 7728, 'borrow_bound_too_small': 3865, 'cycle_budget_exhausted': 87}
- Enregistrements de la session : 182802 ; net attendu > 0 : 126 ; simulés (eth_call de la vraie tx) : 0 (ok 0, échec 0) ; étiquettes ghost N+1 : 0/0 positives
- Décisions : {'REJECTED': 182802} ; motifs de rejet : {'below_safety_margin': 126, 'negative_expected_net': 182676, 'p_lower_below_threshold': 126}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53351894 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH | 0.034024 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0025 €) | — | 0.35 | 0.141 (n=665) | REJECTED | below_safety_margin(1189291991563<6804899194948), p_lower_below_threshold(0.14<0.75) |
| 53351894 | USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 76.025549 USDC | 0.009461 USDC | 0.000000 USDC | 0.006780 USDC | 0.002681 USDC (0.0025 €) | — | 0.35 | 0.141 (n=665) | REJECTED | below_safety_margin(2681<15205), p_lower_below_threshold(0.14<0.75) |
| 53351333 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.004491 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0013 €) | — | 1.39 | 0.141 (n=665) | REJECTED | below_safety_margin(624610008058<898222925891), p_lower_below_threshold(0.14<0.75) |
| 53351333 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.004491 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0013 €) | — | 1.39 | 0.141 (n=665) | REJECTED | below_safety_margin(624610008058<898222925891), p_lower_below_threshold(0.14<0.75) |
| 53351334 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.004491 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0013 €) | — | 1.39 | 0.141 (n=665) | REJECTED | below_safety_margin(624610008058<898222925891), p_lower_below_threshold(0.14<0.75) |
| 53351334 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.004491 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0013 €) | — | 1.39 | 0.141 (n=665) | REJECTED | below_safety_margin(624610008058<898222925891), p_lower_below_threshold(0.14<0.75) |
| 53351333 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 10.078098 USDC | 0.008175 USDC | 0.000000 USDC | 0.006780 USDC | 0.001395 USDC (0.0013 €) | — | 1.38 | 0.141 (n=665) | REJECTED | below_safety_margin(1395<2015), p_lower_below_threshold(0.14<0.75) |
| 53351333 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 10.078098 USDC | 0.008175 USDC | 0.000000 USDC | 0.006780 USDC | 0.001395 USDC (0.0013 €) | — | 1.38 | 0.141 (n=665) | REJECTED | below_safety_margin(1395<2015), p_lower_below_threshold(0.14<0.75) |
| 53351334 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 10.078098 USDC | 0.008175 USDC | 0.000000 USDC | 0.006780 USDC | 0.001395 USDC (0.0013 €) | — | 1.38 | 0.141 (n=665) | REJECTED | below_safety_margin(1395<2015), p_lower_below_threshold(0.14<0.75) |
| 53351334 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 10.078098 USDC | 0.008175 USDC | 0.000000 USDC | 0.006780 USDC | 0.001395 USDC (0.0013 €) | — | 1.38 | 0.141 (n=665) | REJECTED | below_safety_margin(1395<2015), p_lower_below_threshold(0.14<0.75) |
| 53351332 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.004404 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0011 €) | — | 1.18 | 0.141 (n=665) | REJECTED | below_safety_margin(518674208369<880757238037), p_lower_below_threshold(0.14<0.75) |
| 53351332 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.004404 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0011 €) | — | 1.18 | 0.141 (n=665) | REJECTED | below_safety_margin(518674208369<880757238037), p_lower_below_threshold(0.14<0.75) |
| 53351332 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 9.904114 USDC | 0.007936 USDC | 0.000000 USDC | 0.006780 USDC | 0.001156 USDC (0.0011 €) | — | 1.17 | 0.141 (n=665) | REJECTED | below_safety_margin(1156<1980), p_lower_below_threshold(0.14<0.75) |
| 53351332 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 9.904114 USDC | 0.007936 USDC | 0.000000 USDC | 0.006780 USDC | 0.001156 USDC (0.0011 €) | — | 1.17 | 0.141 (n=665) | REJECTED | below_safety_margin(1156<1980), p_lower_below_threshold(0.14<0.75) |
| 53351331 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.004395 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0010 €) | — | 1.07 | 0.141 (n=665) | REJECTED | below_safety_margin(470285925278<879045341954), p_lower_below_threshold(0.14<0.75) |
| 53351331 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.004395 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0010 €) | — | 1.07 | 0.141 (n=665) | REJECTED | below_safety_margin(470285925278<879045341954), p_lower_below_threshold(0.14<0.75) |
| 53351331 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 9.873328 USDC | 0.007827 USDC | 0.000000 USDC | 0.006780 USDC | 0.001047 USDC (0.0010 €) | — | 1.06 | 0.141 (n=665) | REJECTED | below_safety_margin(1047<1974), p_lower_below_threshold(0.14<0.75) |
| 53351331 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 9.873328 USDC | 0.007827 USDC | 0.000000 USDC | 0.006780 USDC | 0.001047 USDC (0.0010 €) | — | 1.06 | 0.141 (n=665) | REJECTED | below_safety_margin(1047<1974), p_lower_below_threshold(0.14<0.75) |
| 53351329 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.004395 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0008 €) | — | 0.93 | 0.141 (n=665) | REJECTED | below_safety_margin(407491031286<879045341954), p_lower_below_threshold(0.14<0.75) |
| 53351329 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.004395 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0008 €) | — | 0.93 | 0.141 (n=665) | REJECTED | below_safety_margin(407491031286<879045341954), p_lower_below_threshold(0.14<0.75) |
| 53351330 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.004395 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0008 €) | — | 0.93 | 0.141 (n=665) | REJECTED | below_safety_margin(407491031286<879045341954), p_lower_below_threshold(0.14<0.75) |
| 53351330 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.004395 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0008 €) | — | 0.93 | 0.141 (n=665) | REJECTED | below_safety_margin(407491031286<879045341954), p_lower_below_threshold(0.14<0.75) |
| 53351326 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.004395 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0008 €) | — | 0.93 | 0.141 (n=665) | REJECTED | below_safety_margin(407491031286<879045341954), p_lower_below_threshold(0.14<0.75) |
| 53351327 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.004395 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0008 €) | — | 0.93 | 0.141 (n=665) | REJECTED | below_safety_margin(407491031286<879045341954), p_lower_below_threshold(0.14<0.75) |
| 53351327 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.004395 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0008 €) | — | 0.93 | 0.141 (n=665) | REJECTED | below_safety_margin(407491031286<879045341954), p_lower_below_threshold(0.14<0.75) |

## Fiabilité et décision
- Observations ghost : 4032 ; taux observé 0.128 ; borne inférieure crédible (0.9) 0.122 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 12.2% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
