# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-30T19:26:08+00:00 ; durée 6.08 min ; blocs 53299323 → 53299510 (181 vus)

## Connexion
- Requêtes RPC : 2134 ; erreurs : 0 ; latence p50/p95 : 224.2/1,489.6 ms
- Rafraîchissements d'état : 182 ; âge des données au dernier bloc : 0.99 s ; changements de frais LP observés (pools à frais dynamiques) : 376
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 3701 ; cycles déclenchés par événement : 177 ; avance médiane sur le rafraîchissement multicall : 710 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,225.35 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 497 pools, 288 jetons, 18532 routes
- Par DEX : uniswap_v3 136, aerodrome_slipstream 112, aerodrome 205, pancakeswap_v3 29, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 178 (rejetés 2) → 583 jetons ; pools candidats 3774 (énumérés 315, par paires 0), mesurés 500, sous le plancher de 10000.0 $ : 3 → gardés 497 (max 1500) ; prix des hubs : {'USDC': 1.0, 'USDbC': 1.0, 'DAI': 1.0, 'WETH': 2226.87299, 'cbBTC': 76304.747909, 'AERO': 0.609807}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 149,690,594 | 2,225.349424 | 53299510 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,816,197 | 0.029138 | 53299510 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,622,158 | 0.000013 | 53299510 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 8,941,616 | 0.029112 | 53299510 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 8,131,629 | 2,229.836456 | 53299510 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,604,197 | 101.583663 | 53299510 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,589,339 | 0.001612 | 53299510 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 5,830,167 | 1.639921 | 53299510 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,511,149 | 0.029137 | 53299510 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/USDC | 862 | 4,130,282 | 2,229.330008 | 53299510 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,034,419 | 2,229.112338 | 53299510 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,020,333 | 0.998958 | 53299510 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,518,399 | 37,439.924413 | 53299510 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,728,022 | 0.029126 | 53299510 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2700 | 2,290,627 | 101.585356 | 53299510 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | WETH/FAI | 10000 | 2,040,080 | 1,206,344.208581 | 53299510 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 600 | 1,901,411 | 0.000013 | 53299510 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,750,551 | 0.000000 | 53299510 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,715,904 | 0.017352 | 53299510 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,666,244 | 423.573625 | 53299510 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,617,090 | 0.000013 | 53299510 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,532,984 | 0.000013 | 53299510 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | WETH/USDC | 3000 | 1,518,418 | 2,226.850923 | 53299510 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,512,933 | 1.548785 | 53299510 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,454,686 | 0.825659 | 53299510 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | USDC/cbBTC | 374 | 1,451,990 | 0.000013 | 53299510 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | WETH/AERO | 3000 | 1,385,964 | 3,645.177987 | 53299510 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,306,642 | 2,229.863657 | 53299510 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,287,637 | 14,527.551479 | 53299510 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,263,866 | 0.004960 | 53299510 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome | USDC/SEND | 3000 | 1,176,193 | 70.240036 | 53299510 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,094,726 | 36,605,298.548697 | 53299510 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,048,477 | 517,397.137309 | 53299510 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,029,960 | 21,015,971.546121 | 53299510 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | DRB/WETH | 10000 | 1,013,203 | 0.000000 | 53299510 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | WETH/EDEL | 7000 | 1,008,037 | 74,430.949000 | 53299510 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v2 | WETH/USDC | 3000 | 1,005,812 | 2,225.721010 | 53299510 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | USDC/VELVET | 100 | 988,358 | 19.600552 | 53299510 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | USDC/NOCK | 3000 | 981,375 | 65.000545 | 53299510 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/VVV | 10000 | 953,354 | 101.211383 | 53299510 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | USDC/VVV | 3000 | 934,494 | 0.045579 | 53299510 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/USDC | 10000 | 917,910 | 2,235.963227 | 53299510 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome | WETH/WELL | 10000 | 917,062 | 1,231,142.580594 | 53299510 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/MORPHO | 3000 | 880,285 | 1,088.079959 | 53299510 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | uXRP/WETH | 3000 | 854,926 | 0.000552 | 53299510 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome | WETH/AERO | 10000 | 850,729 | 3,618.825714 | 53299510 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 830,122 | 19.709429 | 53299510 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 813,407 | 0.059430 | 53299510 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 753,242 | 0.803616 | 53299510 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| aerodrome | VIRTUAL/WETH | 10000 | 731,857 | 0.000264 | 53299510 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 720,984 | 4,500,524.323568 | 53299510 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 719,917 | 0.587134 | 53299510 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| aerodrome | WETH/msETH (stable) | 500 | 675,591 | 2.330205 | 53299510 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 668,886 | 0.000008 | 53299510 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 650,474 | 521,500.601896 | 53299510 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v2 | WETH/NPC | 3000 | 647,852 | 148,768.098255 | 53299510 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| uniswap_v3 | TIG/USDC | 10000 | 629,569 | 0.501272 | 53299510 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 599,391 | 0.090086 | 53299510 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| aerodrome | WETH/bsdETH | 100 | 598,350 | 0.915108 | 53299510 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 533,854 | 1,087.668974 | 53299510 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |

## Recherche d'opportunités
- Cycles : 357 ; routes examinées : 6615924 ; candidats optimisés : 29003 ; net attendu > 0 : 64 ; dernier cycle 241.3 ms
- Rejets (moteur) : {'spread_below_threshold': 6495410, 'liquidity_below_min': 88010, 'negative_expected_net': 28939, 'unquotable': 3144, 'borrow_bound_too_small': 357}
- Enregistrements de la session : 29003 ; net attendu > 0 : 64 ; simulés (eth_call de la vraie tx) : 2 (ok 0, échec 2) ; étiquettes ghost N+1 : 0/0 positives
- Décisions : {'REJECTED': 29003} ; motifs de rejet : {'below_safety_margin': 62, 'negative_expected_net': 28939, 'p_lower_below_threshold': 63, 'reliability_not_demonstrated': 1, 'simulation_failed': 2}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53299393 | WETH→[uniswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.130434 WETH | 0.000007 WETH | 0.000000 WETH | 0.000003 WETH | 0.000004 WETH (0.0082 €) | — | 0.31 | 0.145 (n=645) | REJECTED | below_safety_margin(3985072136953<26086734346216), p_lower_below_threshold(0.14<0.75) |
| 53299394 | WETH→[uniswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.130434 WETH | 0.000007 WETH | 0.000000 WETH | 0.000003 WETH | 0.000004 WETH (0.0082 €) | — | 0.31 | 0.145 (n=645) | REJECTED | below_safety_margin(3985072136953<26086734346216), p_lower_below_threshold(0.14<0.75) |
| 53299393 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→cbBTC | 0.003172 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0077 €) | — | 0.35 | 0.145 (n=645) | REJECTED | below_safety_margin(11<63), p_lower_below_threshold(0.14<0.75) |
| 53299394 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→cbBTC | 0.003172 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0077 €) | — | 0.35 | 0.145 (n=645) | REJECTED | below_safety_margin(11<63), p_lower_below_threshold(0.14<0.75) |
| 53299393 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 356.710534 USDC | 0.015540 USDC | 0.000000 USDC | 0.007302 USDC | 0.008238 USDC (0.0076 €) | — | 0.23 | 0.145 (n=645) | REJECTED | below_safety_margin(8238<71342), p_lower_below_threshold(0.14<0.75) |
| 53299394 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 356.710534 USDC | 0.015540 USDC | 0.000000 USDC | 0.007302 USDC | 0.008238 USDC (0.0076 €) | — | 0.23 | 0.145 (n=645) | REJECTED | below_safety_margin(8238<71342), p_lower_below_threshold(0.14<0.75) |
| 53299509 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 23.309646 USDC | 0.013088 USDC | 0.000000 USDC | 0.005032 USDC | 0.008056 USDC (0.0074 €) | — | 3.46 | 0.020 (n=178) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.02<0.75) |
| 53299393 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→cbBTC | 0.002865 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0035 €) | — | 0.17 | 0.145 (n=645) | REJECTED | below_safety_margin(5<57), p_lower_below_threshold(0.14<0.75) |
| 53299394 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→cbBTC | 0.002865 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0035 €) | — | 0.17 | 0.145 (n=645) | REJECTED | below_safety_margin(5<57), p_lower_below_threshold(0.14<0.75) |
| 53299393 | WETH→[uniswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.109133 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0034 €) | — | 0.15 | 0.145 (n=645) | REJECTED | below_safety_margin(1668059738194<21826669199352), p_lower_below_threshold(0.14<0.75) |
| 53299394 | WETH→[uniswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.109133 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0034 €) | — | 0.15 | 0.145 (n=645) | REJECTED | below_safety_margin(1668059738194<21826669199352), p_lower_below_threshold(0.14<0.75) |
| 53299393 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 242.621949 USDC | 0.010968 USDC | 0.000000 USDC | 0.007302 USDC | 0.003666 USDC (0.0034 €) | — | 0.15 | 0.145 (n=645) | REJECTED | below_safety_margin(3666<48524), p_lower_below_threshold(0.14<0.75) |
| 53299394 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 242.621949 USDC | 0.010968 USDC | 0.000000 USDC | 0.007302 USDC | 0.003666 USDC (0.0034 €) | — | 0.15 | 0.145 (n=645) | REJECTED | below_safety_margin(3666<48524), p_lower_below_threshold(0.14<0.75) |
| 53299509 | USDC→[aerodrome]→PLAY→[pancakeswap_v3]→USDC | 8.317621 USDC | 0.007214 USDC | 0.000000 USDC | 0.004725 USDC | 0.002489 USDC (0.0023 €) | — | 2.99 | 0.001 (n=14) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53299431 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→cbBTC | 0.000768 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0021 €) | — | 0.39 | 0.145 (n=645) | REJECTED | below_safety_margin(3<15), p_lower_below_threshold(0.14<0.75) |
| 53299431 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 58.663934 USDC | 0.008494 USDC | 0.000000 USDC | 0.006721 USDC | 0.001773 USDC (0.0016 €) | — | 0.30 | 0.145 (n=645) | REJECTED | below_safety_margin(1773<11732), p_lower_below_threshold(0.14<0.75) |
| 53299458 | USDC→[aerodrome_slipstream]→EURC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 43.101009 USDC | 0.008465 USDC | 0.000000 USDC | 0.006720 USDC | 0.001745 USDC (0.0016 €) | — | 0.40 | 0.145 (n=645) | REJECTED | below_safety_margin(1745<8620), p_lower_below_threshold(0.14<0.75) |
| 53299458 | USDC→[aerodrome_slipstream]→EURC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 43.101009 USDC | 0.008465 USDC | 0.000000 USDC | 0.006720 USDC | 0.001745 USDC (0.0016 €) | — | 0.40 | 0.145 (n=645) | REJECTED | below_safety_margin(1745<8620), p_lower_below_threshold(0.14<0.75) |
| 53299458 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→EURC→[pancakeswap_v3]→WETH | 0.019273 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0016 €) | — | 0.40 | 0.145 (n=645) | REJECTED | below_safety_margin(779239374449<3854663451690), p_lower_below_threshold(0.14<0.75) |
| 53299458 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→EURC→[pancakeswap_v3]→WETH | 0.019273 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0016 €) | — | 0.40 | 0.145 (n=645) | REJECTED | below_safety_margin(779239374449<3854663451690), p_lower_below_threshold(0.14<0.75) |
| 53299458 | USDC→[aerodrome_slipstream]→EURC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 43.155175 USDC | 0.008706 USDC | 0.000000 USDC | 0.007057 USDC | 0.001649 USDC (0.0015 €) | — | 0.38 | 0.145 (n=645) | REJECTED | below_safety_margin(1649<8631), p_lower_below_threshold(0.14<0.75) |
| 53299458 | USDC→[aerodrome_slipstream]→EURC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 43.155175 USDC | 0.008706 USDC | 0.000000 USDC | 0.007057 USDC | 0.001649 USDC (0.0015 €) | — | 0.38 | 0.145 (n=645) | REJECTED | below_safety_margin(1649<8631), p_lower_below_threshold(0.14<0.75) |
| 53299458 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→EURC→[pancakeswap_v3]→WETH | 0.019545 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0015 €) | — | 0.38 | 0.145 (n=645) | REJECTED | below_safety_margin(735679209190<3909002868701), p_lower_below_threshold(0.14<0.75) |
| 53299458 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→EURC→[pancakeswap_v3]→WETH | 0.019545 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0015 €) | — | 0.38 | 0.145 (n=645) | REJECTED | below_safety_margin(735679209190<3909002868701), p_lower_below_threshold(0.14<0.75) |
| 53299431 | WETH→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.025589 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0015 €) | — | 0.29 | 0.145 (n=645) | REJECTED | below_safety_margin(734361799575<5117747030405), p_lower_below_threshold(0.14<0.75) |

## Fiabilité et décision
- Observations ghost : 3872 ; taux observé 0.130 ; borne inférieure crédible (0.9) 0.123 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 12.3% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
