# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-23T19:50:13+00:00 ; durée 73.77 min ; blocs 52995614 → 52997830 (2047 vus)

## Connexion
- Requêtes RPC : 25389 ; erreurs : 105 ; latence p50/p95 : 437.6/1,538.9 ms
- Rafraîchissements d'état : 2047 ; âge des données au dernier bloc : 3.89 s ; changements de frais LP observés (pools à frais dynamiques) : 4005
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 22324 ; cycles déclenchés par événement : 1235 ; avance médiane sur le rafraîchissement multicall : 829 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,398.20 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 546 pools, 317 jetons, 19488 routes
- Par DEX : uniswap_v3 138, aerodrome 222, aerodrome_slipstream 137, pancakeswap_v3 32, uniswap_v2 13, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 200 (rejetés 2) → 605 jetons ; pools candidats 3880 (énumérés 359, par paires 0), mesurés 548, sous le plancher de 10000.0 $ : 2 → gardés 546 (max 1500) ; prix des hubs : {'USDC': 1.0, 'DAI': 1.0, 'USDbC': 1.0, 'WETH': 2404.297357, 'AERO': 0.765849, 'cbBTC': 81434.30056}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 157,213,853 | 2,398.202455 | 52997831 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,563,951 | 0.029483 | 52997831 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 12,612,998 | 95.017698 | 52997831 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| aerodrome | USDC/AERO | 3000 | 10,452,019 | 1.340215 | 52997831 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,266,389 | 0.029437 | 52997831 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,768,335 | 0.000012 | 52997831 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 8,833,607 | 0.029452 | 52997831 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/USDC | 500 | 8,679,176 | 2,394.327001 | 52997831 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,136,236 | 0.001666 | 52997831 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 332 | 6,343,529 | 0.000012 | 52997831 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 535 | 5,476,414 | 2,394.766158 | 52997831 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,443,141 | 0.029475 | 52997831 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | USDC/cbBTC | 424 | 4,919,510 | 0.000012 | 52997831 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,552,295 | 2,394.710601 | 52997831 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,280,915 | 0.999604 | 52997831 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/USDC | 3000 | 4,234,339 | 2,399.612143 | 52997831 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome | WETH/KTA | 3000 | 3,991,578 | 34,203.454040 | 52997831 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | VIRTUAL/WETH | 10000 | 3,403,453 | 0.000275 | 52997831 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/USDT | 406 | 2,805,540 | 2,398.385168 | 52997831 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome_slipstream | WETH/VVV | 2754 | 2,531,964 | 95.036216 | 52997831 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,301,865 | 397.255585 | 52997831 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | WETH/FAI | 10000 | 2,204,099 | 1,200,269.042327 | 52997831 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome | WETH/AERO | 10000 | 2,040,608 | 3,183.987534 | 52997831 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,942,574 | 0.000000 | 52997831 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,927,936 | 0.000012 | 52997831 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v3 | XDP/USDC | 100 | 1,765,305 | 0.017895 | 52997831 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,744,068 | 0.000012 | 52997831 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,555,812 | 1.605727 | 52997831 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | WETH/AERO | 3000 | 1,513,959 | 3,207.362290 | 52997831 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,459,629 | 0.824389 | 52997831 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,409,932 | 13,462.220178 | 52997831 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,386,937 | 0.005075 | 52997831 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,296,845 | 0.000273 | 52997831 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,292,799 | 2,394.701776 | 52997831 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | DRB/WETH | 10000 | 1,263,705 | 0.000000 | 52997831 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | WETH/msETH (stable) | 500 | 1,255,333 | 2.309353 | 52997831 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome | USDC/SEND | 3000 | 1,228,362 | 64.400566 | 52997831 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,189,139 | 35,655,996.601722 | 52997831 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,166,361 | 482,299.940575 | 52997831 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | WETH/WELL | 10000 | 1,166,150 | 1,114,950.650117 | 52997831 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome | USDC/NOCK | 3000 | 1,141,776 | 48.058962 | 52997831 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,141,299 | 16.319618 | 52997831 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | WETH/EDEL | 7000 | 1,079,288 | 75,703.052717 | 52997831 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,073,484 | 21,000,503.766767 | 52997831 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | USDC/VVV | 3000 | 1,071,216 | 0.039688 | 52997831 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,050,424 | 16.535269 | 52997831 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 992,282 | 23.118403 | 52997831 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| uniswap_v3 | WETH/MORPHO | 3000 | 952,249 | 1,061.383682 | 52997831 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/USDC | 10000 | 939,281 | 2,390.810444 | 52997831 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | uXRP/WETH | 3000 | 911,159 | 0.000541 | 52997831 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 899,622 | 0.000009 | 52997831 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | USDC/SAPIEN | 4555 | 895,448 | 17.393566 | 52997831 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v2 | WETH/USDC | 3000 | 858,902 | 2,391.494699 | 52997831 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome | weETH_04c0/WETH | 500 | 829,123 | 1.105789 | 52997831 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| pancakeswap_v3 | QUID/USDC | 100 | 824,694 | 0.061235 | 52997831 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 811,948 | 0.803225 | 52997831 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 778,866 | 0.653090 | 52997831 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 774,562 | 4,523,444.142552 | 52997831 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v2 | WETH/NPC | 3000 | 731,970 | 134,996.936494 | 52997831 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| uniswap_v3 | TIG/USDC | 10000 | 731,829 | 0.671366 | 52997831 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |

## Recherche d'opportunités
- Cycles : 3281 ; routes examinées : 63940128 ; candidats optimisés : 356596 ; net attendu > 0 : 36 ; dernier cycle 193.8 ms
- Rejets (moteur) : {'spread_below_threshold': 62686340, 'liquidity_below_min': 893038, 'negative_expected_net': 356560, 'borrow_bound_too_small': 3281, 'cycle_budget_exhausted': 873}
- Enregistrements de la session : 356596 ; net attendu > 0 : 36 ; simulés (eth_call de la vraie tx) : 5 (ok 2, échec 3) ; étiquettes ghost N+1 : 1/3 positives
- Décisions : {'REJECTED': 356596} ; motifs de rejet : {'below_safety_margin': 31, 'negative_expected_net': 356560, 'p_lower_below_threshold': 35, 'reliability_not_demonstrated': 1, 'simulation_failed': 3}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52997059 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 67.235756 USDC | 0.069204 USDC | 0.000000 USDC | 0.005568 USDC | 0.063636 USDC (0.0585 €) | — | 9.46 | 0.000 (n=48) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 52997045 | WETH→[pancakeswap_v3]→AERO→[aerodrome]→BRETT→[aerodrome_slipstream]→WETH | 0.011664 WETH | 0.000026 WETH | 0.000000 WETH | 0.000003 WETH | 0.000024 WETH (0.0519 €) | 0.000024 WETH | 20.17 | 0.001 (n=10) | REJECTED | reliability_not_demonstrated |
| 52997044 | WETH→[pancakeswap_v3]→AERO→[aerodrome]→BRETT→[aerodrome_slipstream]→WETH | 0.005039 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0045 €) | — | 4.06 | 0.008 (n=35) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.01<0.75) |
| 52997045 | WETH→[pancakeswap_v3]→AERO→[aerodrome]→BRETT→[aerodrome_slipstream]→WETH | 0.005039 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0045 €) | — | 4.06 | 0.008 (n=35) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.01<0.75) |
| 52997045 | WETH→[uniswap_v3]→AERO→[aerodrome]→BRETT→[aerodrome_slipstream]→WETH | 0.005007 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0042 €) | 0.000002 WETH | 3.77 | 0.032 (n=135) | REJECTED | p_lower_below_threshold(0.03<0.75) |
| 52997806 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.004248 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0017 €) | — | 1.82 | 0.121 (n=244) | REJECTED | below_safety_margin(772022710410<849587718125), p_lower_below_threshold(0.12<0.75) |
| 52997807 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.004248 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0017 €) | — | 1.82 | 0.121 (n=244) | REJECTED | below_safety_margin(772022710410<849587718125), p_lower_below_threshold(0.12<0.75) |
| 52997806 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 10.069049 USDC | 0.009059 USDC | 0.000000 USDC | 0.007224 USDC | 0.001835 USDC (0.0017 €) | — | 1.82 | 0.121 (n=244) | REJECTED | below_safety_margin(1835<2013), p_lower_below_threshold(0.12<0.75) |
| 52997807 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 10.069049 USDC | 0.009059 USDC | 0.000000 USDC | 0.007224 USDC | 0.001835 USDC (0.0017 €) | — | 1.82 | 0.121 (n=244) | REJECTED | below_safety_margin(1835<2013), p_lower_below_threshold(0.12<0.75) |
| 52997059 | WETH→[aerodrome_slipstream]→BRETT→[aerodrome]→AERO→[pancakeswap_v3]→WETH | 0.004358 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0015 €) | — | 1.55 | 0.170 (n=31) | REJECTED | below_safety_margin(677611574278<871697844290), p_lower_below_threshold(0.17<0.75) |
| 52997060 | WETH→[aerodrome_slipstream]→BRETT→[aerodrome]→AERO→[pancakeswap_v3]→WETH | 0.004358 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0015 €) | — | 1.55 | 0.170 (n=31) | REJECTED | below_safety_margin(677611574278<871697844290), p_lower_below_threshold(0.17<0.75) |
| 52997530 | cbBTC→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→VIRTUAL→[aerodrome]→cbBTC | 0.000343 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0007 €) | — | 0.29 | 0.118 (n=93) | REJECTED | below_safety_margin(1<6), p_lower_below_threshold(0.12<0.75) |
| 52997530 | cbBTC→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→VIRTUAL→[aerodrome]→cbBTC | 0.000343 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0007 €) | — | 0.29 | 0.118 (n=93) | REJECTED | below_safety_margin(1<6), p_lower_below_threshold(0.12<0.75) |
| 52996140 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.003969 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0007 €) | — | 0.75 | 0.121 (n=244) | REJECTED | below_safety_margin(299216607808<793839115648), p_lower_below_threshold(0.12<0.75) |
| 52996140 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 9.463325 USDC | 0.007965 USDC | 0.000000 USDC | 0.007255 USDC | 0.000710 USDC (0.0007 €) | — | 0.75 | 0.121 (n=244) | REJECTED | below_safety_margin(710<1892), p_lower_below_threshold(0.12<0.75) |
| 52997740 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.003700 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0006 €) | — | 0.74 | 0.241 (n=120) | REJECTED | below_safety_margin(275356814631<740028045821), p_lower_below_threshold(0.24<0.75) |
| 52997738 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.003673 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0006 €) | — | 0.75 | 0.241 (n=120) | REJECTED | below_safety_margin(274297160110<734549483230), p_lower_below_threshold(0.24<0.75) |
| 52997740 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.003673 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0006 €) | — | 0.75 | 0.241 (n=120) | REJECTED | below_safety_margin(274297160110<734549483230), p_lower_below_threshold(0.24<0.75) |
| 52997740 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 8.735298 USDC | 0.007874 USDC | 0.000000 USDC | 0.007227 USDC | 0.000647 USDC (0.0006 €) | — | 0.74 | 0.241 (n=120) | REJECTED | below_safety_margin(647<1747), p_lower_below_threshold(0.24<0.75) |
| 52997738 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 8.735298 USDC | 0.007874 USDC | 0.000000 USDC | 0.007230 USDC | 0.000644 USDC (0.0006 €) | — | 0.74 | 0.241 (n=120) | REJECTED | below_safety_margin(644<1747), p_lower_below_threshold(0.24<0.75) |
| 52997740 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 8.735298 USDC | 0.007874 USDC | 0.000000 USDC | 0.007230 USDC | 0.000644 USDC (0.0006 €) | — | 0.74 | 0.241 (n=120) | REJECTED | below_safety_margin(644<1747), p_lower_below_threshold(0.24<0.75) |
| 52997530 | WETH→[aerodrome_slipstream]→VIRTUAL→[aerodrome]→cbBTC→[aerodrome_slipstream]→WETH | 0.011847 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0005 €) | — | 0.20 | 0.118 (n=93) | REJECTED | below_safety_margin(241932805615<2369422373442), p_lower_below_threshold(0.12<0.75) |
| 52997530 | WETH→[aerodrome_slipstream]→VIRTUAL→[aerodrome]→cbBTC→[aerodrome_slipstream]→WETH | 0.011847 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0005 €) | — | 0.20 | 0.118 (n=93) | REJECTED | below_safety_margin(241932805615<2369422373442), p_lower_below_threshold(0.12<0.75) |
| 52997806 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.003893 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0005 €) | — | 0.54 | 0.241 (n=120) | REJECTED | below_safety_margin(209635518993<778619698688), p_lower_below_threshold(0.24<0.75) |
| 52997807 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.003893 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0005 €) | — | 0.54 | 0.241 (n=120) | REJECTED | below_safety_margin(209635518993<778619698688), p_lower_below_threshold(0.24<0.75) |

## Fiabilité et décision
- Observations ghost : 2052 ; taux observé 0.096 ; borne inférieure crédible (0.9) 0.088 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 8.8% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
