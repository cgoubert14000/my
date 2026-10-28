# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-28T06:32:00+00:00 ; durée 61.28 min ; blocs 53188044 → 53189885 (1826 vus)

## Connexion
- Requêtes RPC : 21832 ; erreurs : 20 ; latence p50/p95 : 211.8/1,177.4 ms
- Rafraîchissements d'état : 1827 ; âge des données au dernier bloc : 1.43 s ; changements de frais LP observés (pools à frais dynamiques) : 1306
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 12330 ; cycles déclenchés par événement : 2102 ; avance médiane sur le rafraîchissement multicall : 477 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,355.90 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 521 pools, 302 jetons, 18962 routes
- Par DEX : uniswap_v3 147, aerodrome_slipstream 121, aerodrome 210, pancakeswap_v3 28, uniswap_v2 12, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 184 (rejetés 2) → 589 jetons ; pools candidats 3762 (énumérés 330, par paires 0), mesurés 523, sous le plancher de 10000.0 $ : 2 → gardés 521 (max 1500) ; prix des hubs : {'USDC': 1.0, 'USDbC': 1.0, 'DAI': 1.0, 'WETH': 2356.459313, 'cbBTC': 80857.377983, 'AERO': 0.694089}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 158,168,162 | 2,355.903181 | 53189885 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,700,129 | 0.029092 | 53189885 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,647,196 | 0.000012 | 53189885 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,494,785 | 0.029105 | 53189885 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 8,431,484 | 2,351.195612 | 53189885 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 8,374,031 | 96.096956 | 53189885 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,065,730 | 0.001648 | 53189885 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 6,867,590 | 1.441952 | 53189885 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,745,840 | 0.029082 | 53189885 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/USDC | 150 | 5,047,557 | 2,350.660880 | 53189885 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,483,818 | 2,350.579758 | 53189885 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,263,884 | 0.998870 | 53189885 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,768,824 | 36,575.451931 | 53189885 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,964,187 | 0.029116 | 53189885 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2724 | 2,530,782 | 96.077370 | 53189885 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | USDC/cbBTC | 412 | 2,458,453 | 0.000012 | 53189885 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome | WETH/FAI | 10000 | 2,150,540 | 1,216,715.810354 | 53189885 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome | WETH/USDC | 3000 | 1,922,703 | 2,357.245771 | 53189885 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| uniswap_v3 | XDP/USDC | 100 | 1,842,517 | 0.019032 | 53189885 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,829,460 | 0.000000 | 53189885 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,799,310 | 395.499893 | 53189885 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | USDC/cbBTC | 334 | 1,700,255 | 0.000012 | 53189885 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,693,383 | 0.000012 | 53189885 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,692,743 | 0.000012 | 53189885 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,517,260 | 0.005798 | 53189885 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,474,280 | 1.658893 | 53189885 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,462,208 | 0.826416 | 53189885 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,454,945 | 3,393.525972 | 53189885 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,399,991 | 13,592.804557 | 53189885 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,259,754 | 0.000268 | 53189885 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,242,487 | 2,351.317421 | 53189885 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | WETH/AERO | 10000 | 1,201,628 | 3,369.352247 | 53189885 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | USDC/SEND | 3000 | 1,194,235 | 68.133836 | 53189885 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome | VIRTUAL/WETH | 10000 | 1,190,781 | 0.000267 | 53189885 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome | WETH/WELL | 10000 | 1,167,846 | 1,067,137.705684 | 53189885 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/doginme | 10000 | 1,165,636 | 36,230,754.358062 | 53189885 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | DRB/WETH | 10000 | 1,140,730 | 0.000000 | 53189885 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,129,835 | 498,236.291064 | 53189885 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | WETH/EDEL | 7000 | 1,083,564 | 72,227.288837 | 53189885 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,063,529 | 21,141,464.036905 | 53189885 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome | USDC/NOCK | 3000 | 1,058,058 | 55.918159 | 53189885 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,047,445 | 16.667144 | 53189885 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | USDC/VVV | 3000 | 1,002,209 | 0.040839 | 53189885 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/VVV | 10000 | 1,000,474 | 95.958399 | 53189885 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/USDC | 10000 | 945,543 | 2,342.370626 | 53189885 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 933,126 | 1,062.909743 | 53189885 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | uXRP/WETH | 3000 | 910,564 | 0.000560 | 53189885 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome | WETH/msETH (stable) | 500 | 889,599 | 2.313211 | 53189885 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | USDC/SAPIEN | 4515 | 883,054 | 17.846161 | 53189885 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 852,018 | 17.446284 | 53189885 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| uniswap_v2 | WETH/USDC | 3000 | 850,845 | 2,357.180367 | 53189885 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| pancakeswap_v3 | QUID/USDC | 100 | 808,645 | 0.058727 | 53189885 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 797,649 | 0.803180 | 53189885 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 755,711 | 0.000009 | 53189885 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 755,447 | 0.630601 | 53189885 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 753,066 | 4,620,519.673883 | 53189885 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v2 | WETH/NPC | 3000 | 713,944 | 137,102.136989 | 53189885 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 701,848 | 501,369.566106 | 53189885 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | TIG/USDC | 10000 | 681,427 | 0.584770 | 53189885 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 671,628 | 0.108091 | 53189885 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |

## Recherche d'opportunités
- Cycles : 3928 ; routes examinées : 74482736 ; candidats optimisés : 222703 ; net attendu > 0 : 58 ; dernier cycle 283.5 ms
- Rejets (moteur) : {'spread_below_threshold': 73422248, 'liquidity_below_min': 778709, 'negative_expected_net': 222645, 'borrow_bound_too_small': 58875, 'cycle_budget_exhausted': 144}
- Enregistrements de la session : 222703 ; net attendu > 0 : 58 ; simulés (eth_call de la vraie tx) : 11 (ok 0, échec 11) ; étiquettes ghost N+1 : 0/11 positives
- Décisions : {'REJECTED': 222703} ; motifs de rejet : {'below_safety_margin': 12, 'negative_expected_net': 222645, 'p_lower_below_threshold': 40, 'price_impact': 2, 'reliability_not_demonstrated': 18, 'simulation_failed': 11}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53188413 | USDC→[aerodrome]→OWB→[uniswap_v3]→USDC | 139.105675 USDC | 6.970905 USDC | 0.000000 USDC | 0.004965 USDC | 6.965940 USDC (6.4087 €) | — | 500.77 | 0.001 (n=13) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53188189 | WETH→[aerodrome_slipstream]→TIG→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→WETH | 0.003143 WETH | 0.000056 WETH | 0.000000 WETH | 0.000003 WETH | 0.000053 WETH (0.1141 €) | — | 167.43 | 0.000 (n=32) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 53188189 | USDC→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→TIG→[aerodrome_slipstream]→USDC | 7.383964 USDC | 0.131180 USDC | 0.000000 USDC | 0.007438 USDC | 0.123742 USDC (0.1138 €) | — | 167.58 | 0.000 (n=32) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53188189 | WETH→[aerodrome_slipstream]→TIG→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.003145 WETH | 0.000055 WETH | 0.000000 WETH | 0.000003 WETH | 0.000052 WETH (0.1135 €) | — | 166.40 | 0.000 (n=23) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53188189 | WETH→[aerodrome_slipstream]→TIG→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.003145 WETH | 0.000055 WETH | 0.000000 WETH | 0.000003 WETH | 0.000052 WETH (0.1134 €) | — | 166.34 | 0.000 (n=32) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 53188189 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→TIG→[aerodrome_slipstream]→USDC | 7.386026 USDC | 0.130499 USDC | 0.000000 USDC | 0.007438 USDC | 0.123061 USDC (0.1132 €) | — | 166.61 | 0.000 (n=23) | REJECTED | reliability_not_demonstrated |
| 53188189 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→TIG→[aerodrome_slipstream]→USDC | 7.386509 USDC | 0.130461 USDC | 0.000000 USDC | 0.007438 USDC | 0.123023 USDC (0.1132 €) | — | 166.55 | 0.000 (n=32) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53188189 | WETH→[aerodrome_slipstream]→TIG→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→WETH | 0.003142 WETH | 0.000055 WETH | 0.000000 WETH | 0.000003 WETH | 0.000052 WETH (0.1128 €) | — | 165.64 | 0.000 (n=32) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53188189 | USDC→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→TIG→[aerodrome_slipstream]→USDC | 7.384617 USDC | 0.129822 USDC | 0.000000 USDC | 0.007438 USDC | 0.122384 USDC (0.1126 €) | — | 165.73 | 0.000 (n=32) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53188189 | WETH→[aerodrome_slipstream]→TIG→[aerodrome_slipstream]→USDC→[sushiswap_v3]→WETH | 0.003131 WETH | 0.000054 WETH | 0.000000 WETH | 0.000003 WETH | 0.000050 WETH (0.1092 €) | — | 160.87 | 0.000 (n=32) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53188189 | USDC→[sushiswap_v3]→WETH→[aerodrome_slipstream]→TIG→[aerodrome_slipstream]→USDC | 7.357162 USDC | 0.126296 USDC | 0.000000 USDC | 0.007796 USDC | 0.118500 USDC (0.1090 €) | — | 161.07 | 0.000 (n=32) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53188189 | WETH→[aerodrome_slipstream]→TIG→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.003122 WETH | 0.000053 WETH | 0.000000 WETH | 0.000003 WETH | 0.000050 WETH (0.1081 €) | — | 159.73 | 0.000 (n=23) | REJECTED | reliability_not_demonstrated |
| 53188189 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→TIG→[aerodrome_slipstream]→USDC | 7.346989 USDC | 0.124810 USDC | 0.000000 USDC | 0.007438 USDC | 0.117372 USDC (0.1080 €) | — | 159.76 | 0.000 (n=23) | REJECTED | reliability_not_demonstrated |
| 53188189 | WETH→[aerodrome_slipstream]→TIG→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.003122 WETH | 0.000053 WETH | 0.000000 WETH | 0.000003 WETH | 0.000050 WETH (0.1080 €) | — | 159.50 | 0.000 (n=32) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53188189 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→TIG→[aerodrome_slipstream]→USDC | 7.347537 USDC | 0.124642 USDC | 0.000000 USDC | 0.007438 USDC | 0.117204 USDC (0.1078 €) | — | 159.51 | 0.000 (n=32) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53188189 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→TIG→[aerodrome_slipstream]→USDC | 6.829681 USDC | 0.093763 USDC | 0.000000 USDC | 0.007438 USDC | 0.086325 USDC (0.0794 €) | — | 126.40 | 0.000 (n=32) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53188189 | USDC→[uniswap_v2]→WETH→[aerodrome_slipstream]→TIG→[aerodrome_slipstream]→USDC | 6.818773 USDC | 0.093010 USDC | 0.000000 USDC | 0.006707 USDC | 0.086303 USDC (0.0794 €) | — | 126.57 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 53188189 | WETH→[aerodrome_slipstream]→TIG→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.002890 WETH | 0.000040 WETH | 0.000000 WETH | 0.000003 WETH | 0.000037 WETH (0.0792 €) | — | 126.36 | 0.000 (n=32) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53188189 | WETH→[aerodrome_slipstream]→TIG→[aerodrome_slipstream]→USDC→[uniswap_v2]→WETH | 0.002885 WETH | 0.000039 WETH | 0.000000 WETH | 0.000003 WETH | 0.000037 WETH (0.0791 €) | — | 126.54 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 53188189 | USDC→[aerodrome]→WETH→[aerodrome_slipstream]→TIG→[aerodrome_slipstream]→USDC | 6.829772 USDC | 0.089096 USDC | 0.000000 USDC | 0.007113 USDC | 0.081983 USDC (0.0754 €) | — | 120.04 | 0.001 (n=10) | REJECTED | reliability_not_demonstrated |
| 53188189 | WETH→[aerodrome_slipstream]→TIG→[aerodrome_slipstream]→USDC→[aerodrome]→WETH | 0.002888 WETH | 0.000038 WETH | 0.000000 WETH | 0.000003 WETH | 0.000035 WETH (0.0751 €) | — | 120.00 | 0.001 (n=10) | REJECTED | reliability_not_demonstrated |
| 53189786 | WETH→[uniswap_v3]→TEVA→[aerodrome]→WETH | 0.012898 WETH | 0.000035 WETH | 0.000000 WETH | 0.000002 WETH | 0.000033 WETH (0.0713 €) | — | 25.51 | 0.000 (n=25) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53188413 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.140556 WETH | 0.000020 WETH | 0.000000 WETH | 0.000002 WETH | 0.000017 WETH (0.0371 €) | — | 1.22 | 0.020 (n=107) | REJECTED | below_safety_margin(17111321660092<28111151584822), p_lower_below_threshold(0.02<0.75) |
| 53188413 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 330.221781 USDC | 0.045863 USDC | 0.000000 USDC | 0.005648 USDC | 0.040215 USDC (0.0370 €) | — | 1.22 | 0.020 (n=107) | REJECTED | below_safety_margin(40215<66044), p_lower_below_threshold(0.02<0.75) |
| 53188189 | USDC→[uniswap_v3]→TIG→[aerodrome_slipstream]→USDC | 2.566552 USDC | 0.024875 USDC | 0.000000 USDC | 0.005291 USDC | 0.019584 USDC (0.0180 €) | — | 76.30 | 0.003 (n=2) | REJECTED | reliability_not_demonstrated |

## Fiabilité et décision
- Observations ghost : 2903 ; taux observé 0.091 ; borne inférieure crédible (0.9) 0.085 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 8.5% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
