# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-05T21:51:17+00:00 ; durée 27.31 min ; blocs 53617273 → 53625406 (793 vus)

## Connexion
- Requêtes RPC : 13680 ; erreurs : 0 ; latence p50/p95 : 769.9/2,192.1 ms
- Rafraîchissements d'état : 793 ; âge des données au dernier bloc : 20.56 s ; changements de frais LP observés (pools à frais dynamiques) : 1140
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 1686 ; cycles déclenchés par événement : 411 ; avance médiane sur le rafraîchissement multicall : 792 ms
- Gaz : base fee 0.005001 gwei ; prix ETH (pool le plus profond) : 2,231.75 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 482 pools, 280 jetons, 18100 routes
- Par DEX : uniswap_v3 136, aerodrome_slipstream 101, aerodrome 201, pancakeswap_v3 30, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 173 (rejetés 2) → 578 jetons ; pools candidats 3707 (énumérés 302, par paires 0), mesurés 487, sous le plancher de 10000.0 $ : 5 → gardés 482 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2231.121633, 'cbBTC': 75799.40241, 'AERO': 0.604242}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 145,851,090 | 2,231.753989 | 53625460 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,517,451 | 0.029428 | 53625460 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,219,984 | 0.000013 | 53625460 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,044,589 | 0.029389 | 53625460 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 7,948,148 | 2,229.848115 | 53625460 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,487,317 | 103.890086 | 53625460 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,422,362 | 0.001553 | 53625460 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 5,110,744 | 1.650587 | 53625460 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,649,778 | 0.029416 | 53625460 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,091,450 | 2,229.255673 | 53625460 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,995,521 | 0.998651 | 53625460 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,348,025 | 41,584.396381 | 53625460 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 150 | 3,227,510 | 2,229.196605 | 53625460 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2505 | 2,557,688 | 0.029382 | 53625460 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 2,079,510 | 1,167,526.188748 | 53625460 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,930,934 | 0.008036 | 53625460 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/cbBTC | 472 | 1,743,351 | 0.000013 | 53625460 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,638,641 | 0.000000 | 53625460 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,636,803 | 0.016438 | 53625460 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,624,551 | 0.000013 | 53625460 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,529,107 | 1.457700 | 53625460 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,524,325 | 0.000013 | 53625460 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,514,661 | 444.761366 | 53625460 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,459,636 | 0.816622 | 53625460 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,382,343 | 3,686.877491 | 53625460 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v2 | WETH/USDC | 3000 | 1,323,741 | 2,224.865766 | 53625460 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome | WETH/USDC | 3000 | 1,322,408 | 2,232.911841 | 53625460 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,259,232 | 15,125.315456 | 53625460 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,162,360 | 2,229.471561 | 53625460 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,123,791 | 76.942850 | 53625460 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,093,602 | 37,279,855.731115 | 53625460 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/VVV | 10000 | 1,066,865 | 104.138057 | 53625460 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,019,639 | 567,090.345640 | 53625460 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,007,081 | 0.000000 | 53625460 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/TOSHI | 10000 | 993,825 | 22,568,727.559837 | 53625460 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/VELVET | 100 | 960,365 | 21.360593 | 53625460 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | USDC/NOCK | 3000 | 952,300 | 69.141322 | 53625460 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/USDC | 10000 | 934,368 | 2,239.022789 | 53625460 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 929,141 | 1,072.522749 | 53625460 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome_slipstream | USDC/cbBTC | 346 | 923,726 | 0.000013 | 53625460 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | WETH/EDEL | 7000 | 880,044 | 98,074.897076 | 53625460 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | USDC/VVV | 3000 | 863,018 | 0.046616 | 53625460 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | uXRP/WETH | 3000 | 848,417 | 0.000544 | 53625460 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome | WETH/AERO | 10000 | 798,075 | 3,701.209517 | 53625460 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 786,979 | 21.377928 | 53625460 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 785,897 | 0.055245 | 53625460 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 757,253 | 0.799698 | 53625460 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 714,375 | 0.566046 | 53625460 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 688,173 | 4,976,126.884257 | 53625460 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome | VIRTUAL/WETH | 10000 | 681,648 | 0.000253 | 53625460 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v2 | WETH/NPC | 3000 | 665,068 | 142,310.342286 | 53625460 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 654,397 | 0.000008 | 53625460 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v3 | TIG/USDC | 10000 | 651,741 | 0.533927 | 53625460 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | WETH/BRETT | 2108 | 622,259 | 567,704.309941 | 53625460 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome | WETH/bsdETH | 100 | 599,069 | 0.913935 | 53625460 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome | WETH/msETH (stable) | 500 | 596,055 | 2.475447 | 53625460 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| pancakeswap_v3 | ELSA/USDC | 100 | 549,188 | 0.084427 | 53625460 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| uniswap_v3 | FLOCK/USDC | 3000 | 548,146 | 0.036784 | 53625460 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome | cbBTC/EDGE | 7000 | 547,806 | 809,786.405212 | 53625460 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 520,336 | 1,072.209068 | 53625460 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |

## Recherche d'opportunités
- Cycles : 1203 ; routes examinées : 21774300 ; candidats optimisés : 70529 ; net attendu > 0 : 26 ; dernier cycle 621.5 ms
- Rejets (moteur) : {'spread_below_threshold': 21317440, 'liquidity_below_min': 384648, 'negative_expected_net': 70503, 'borrow_bound_too_small': 1198, 'cycle_budget_exhausted': 485}
- Enregistrements de la session : 70529 ; net attendu > 0 : 26 ; simulés (eth_call de la vraie tx) : 2 (ok 2, échec 0) ; étiquettes ghost N+1 : 0/2 positives
- Décisions : {'REJECTED': 70529} ; motifs de rejet : {'below_safety_margin': 24, 'negative_expected_net': 70503, 'p_lower_below_threshold': 22, 'reliability_not_demonstrated': 4, 'stale_data': 14}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53617917 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.338587 WETH | 0.000069 WETH | 0.000000 WETH | 0.000003 WETH | 0.000066 WETH (0.1350 €) | — | 1.95 | 0.046 (n=233) | REJECTED | below_safety_margin(66042364924503<67717351541604), stale_data(6295ms>4000.0), p_lower_below_threshold(0.05<0.75) |
| 53617917 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 748.880467 USDC | 0.152184 USDC | 0.000000 USDC | 0.005683 USDC | 0.146501 USDC (0.1348 €) | — | 1.96 | 0.046 (n=233) | REJECTED | below_safety_margin(146501<149776), stale_data(6303ms>4000.0), p_lower_below_threshold(0.05<0.75) |
| 53617917 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.152255 WETH | 0.000047 WETH | 0.000000 WETH | 0.000003 WETH | 0.000044 WETH (0.0908 €) | 0.000044 WETH | 2.92 | 0.057 (n=76) | REJECTED | stale_data(6191ms>4000.0), p_lower_below_threshold(0.06<0.75) |
| 53617917 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 336.649658 USDC | 0.104612 USDC | 0.000000 USDC | 0.006041 USDC | 0.098571 USDC (0.0907 €) | 0.098571 USDC | 2.93 | 0.057 (n=76) | REJECTED | stale_data(6198ms>4000.0), p_lower_below_threshold(0.06<0.75) |
| 53618187 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 333.527485 USDC | 0.029762 USDC | 0.000000 USDC | 0.005283 USDC | 0.024479 USDC (0.0225 €) | — | 0.73 | 0.046 (n=233) | REJECTED | below_safety_margin(24479<66705), p_lower_below_threshold(0.05<0.75) |
| 53618187 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.149601 WETH | 0.000013 WETH | 0.000000 WETH | 0.000002 WETH | 0.000011 WETH (0.0225 €) | — | 0.74 | 0.046 (n=233) | REJECTED | below_safety_margin(11000756189724<29920206520439), p_lower_below_threshold(0.05<0.75) |
| 53617917 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.064521 WETH | 0.000010 WETH | 0.000000 WETH | 0.000003 WETH | 0.000006 WETH (0.0130 €) | — | 0.99 | 0.168 (n=1020) | REJECTED | below_safety_margin(6373757605358<12904292848390), stale_data(6350ms>4000.0), p_lower_below_threshold(0.17<0.75) |
| 53617917 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 142.645611 USDC | 0.021504 USDC | 0.000000 USDC | 0.007481 USDC | 0.014023 USDC (0.0129 €) | — | 0.98 | 0.168 (n=1020) | REJECTED | below_safety_margin(14023<28529), stale_data(6368ms>4000.0), p_lower_below_threshold(0.17<0.75) |
| 53617917 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.001637 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0126 €) | — | 1.10 | 0.168 (n=1020) | REJECTED | below_safety_margin(18<32), stale_data(6359ms>4000.0), p_lower_below_threshold(0.17<0.75) |
| 53617917 | WETH→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.043508 WETH | 0.000009 WETH | 0.000000 WETH | 0.000004 WETH | 0.000005 WETH (0.0111 €) | — | 1.24 | 0.168 (n=1020) | REJECTED | below_safety_margin(5405219764860<8701692752134), stale_data(6259ms>4000.0), p_lower_below_threshold(0.17<0.75) |
| 53617917 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 101.697045 USDC | 0.019489 USDC | 0.000000 USDC | 0.007838 USDC | 0.011651 USDC (0.0107 €) | — | 1.15 | 0.168 (n=1020) | REJECTED | below_safety_margin(11651<20339), stale_data(6272ms>4000.0), p_lower_below_threshold(0.17<0.75) |
| 53617917 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→cbBTC | 0.001342 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0105 €) | — | 1.12 | 0.168 (n=1020) | REJECTED | below_safety_margin(15<26), stale_data(6266ms>4000.0), p_lower_below_threshold(0.17<0.75) |
| 53618187 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 119.327532 USDC | 0.010669 USDC | 0.000000 USDC | 0.005283 USDC | 0.005386 USDC (0.0050 €) | — | 0.45 | 0.056 (n=78) | REJECTED | below_safety_margin(5386<23865), p_lower_below_threshold(0.06<0.75) |
| 53618187 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.053492 WETH | 0.000005 WETH | 0.000000 WETH | 0.000002 WETH | 0.000002 WETH (0.0049 €) | — | 0.45 | 0.056 (n=78) | REJECTED | below_safety_margin(2417942222935<10698479847029), p_lower_below_threshold(0.06<0.75) |
| 53617832 | WETH→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.037291 WETH | 0.000004 WETH | 0.000000 WETH | 0.000002 WETH | 0.000002 WETH (0.0040 €) | — | 0.52 | 0.046 (n=233) | REJECTED | below_safety_margin(1947299737005<7458278034233), p_lower_below_threshold(0.05<0.75) |
| 53617832 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→cbBTC | 0.000869 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0035 €) | — | 0.58 | 0.046 (n=233) | REJECTED | below_safety_margin(5<17), p_lower_below_threshold(0.05<0.75) |
| 53621020 | USDC→[uniswap_v2]→WETH→[pancakeswap_v3]→USDC | 54.368735 USDC | 0.004787 USDC | 0.000000 USDC | 0.004348 USDC | 0.000439 USDC (0.0004 €) | — | 0.08 | — (n=0) | REJECTED | below_safety_margin(439<10873), reliability_not_demonstrated |
| 53621020 | USDC→[uniswap_v2]→WETH→[pancakeswap_v3]→USDC | 54.368735 USDC | 0.004787 USDC | 0.000000 USDC | 0.004348 USDC | 0.000439 USDC (0.0004 €) | — | 0.08 | — (n=0) | REJECTED | below_safety_margin(439<10873), reliability_not_demonstrated |
| 53621020 | WETH→[pancakeswap_v3]→USDC→[uniswap_v2]→WETH | 0.024491 WETH | 0.000002 WETH | 0.000000 WETH | 0.000002 WETH | 0.000000 WETH (0.0004 €) | — | 0.08 | — (n=0) | REJECTED | below_safety_margin(190635465258<4898151165640), reliability_not_demonstrated |
| 53621020 | WETH→[pancakeswap_v3]→USDC→[uniswap_v2]→WETH | 0.024491 WETH | 0.000002 WETH | 0.000000 WETH | 0.000002 WETH | 0.000000 WETH (0.0004 €) | — | 0.08 | — (n=0) | REJECTED | below_safety_margin(190635465258<4898151165640), reliability_not_demonstrated |
| 53617917 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.003879 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0004 €) | — | 0.45 | 0.233 (n=399) | REJECTED | below_safety_margin(174659769374<775794202179), stale_data(5978ms>4000.0), p_lower_below_threshold(0.23<0.75) |
| 53617917 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 8.515443 USDC | 0.007495 USDC | 0.000000 USDC | 0.007123 USDC | 0.000372 USDC (0.0003 €) | — | 0.44 | 0.233 (n=399) | REJECTED | below_safety_margin(372<1703), stale_data(5983ms>4000.0), p_lower_below_threshold(0.23<0.75) |
| 53617963 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.003814 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0001 €) | — | 0.09 | 0.233 (n=399) | REJECTED | below_safety_margin(35601225363<762875311339), p_lower_below_threshold(0.23<0.75) |
| 53618004 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.003815 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0001 €) | — | 0.08 | 0.233 (n=399) | REJECTED | below_safety_margin(30905249228<763050444299), stale_data(5308ms>4000.0), p_lower_below_threshold(0.23<0.75) |
| 53617963 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 8.307546 USDC | 0.007189 USDC | 0.000000 USDC | 0.007125 USDC | 0.000064 USDC (0.0001 €) | — | 0.08 | 0.233 (n=399) | REJECTED | below_safety_margin(64<1661), p_lower_below_threshold(0.23<0.75) |

## Fiabilité et décision
- Observations ghost : 5773 ; taux observé 0.158 ; borne inférieure crédible (0.9) 0.152 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 15.2% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
