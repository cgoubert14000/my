# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-27T12:45:18+00:00 ; durée 3.04 min ; blocs 53157790 → 53157884 (90 vus)

## Connexion
- Requêtes RPC : 1106 ; erreurs : 0 ; latence p50/p95 : 240.0/1,590.0 ms
- Rafraîchissements d'état : 90 ; âge des données au dernier bloc : 3.1 s ; changements de frais LP observés (pools à frais dynamiques) : 207
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 1384 ; cycles déclenchés par événement : 95 ; avance médiane sur le rafraîchissement multicall : 495 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,325.14 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 524 pools, 301 jetons, 19174 routes
- Par DEX : uniswap_v3 145, aerodrome 212, aerodrome_slipstream 123, pancakeswap_v3 28, uniswap_v2 13, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 188 (rejetés 2) → 593 jetons ; pools candidats 3787 (énumérés 335, par paires 0), mesurés 527, sous le plancher de 10000.0 $ : 3 → gardés 524 (max 1500) ; prix des hubs : {'USDC': 1.0, 'USDbC': 1.0, 'DAI': 1.0, 'WETH': 2324.722428, 'cbBTC': 80182.929325, 'AERO': 0.68845}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 156,498,435 | 2,325.142131 | 53157885 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,208,808 | 0.029052 | 53157885 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,120,957 | 0.028983 | 53157885 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,529,299 | 0.000012 | 53157885 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome | WETH/VVV | 3000 | 8,582,952 | 90.699563 | 53157885 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/USDC | 500 | 8,348,041 | 2,330.436924 | 53157885 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | USDC/AERO | 3000 | 7,008,776 | 1.452067 | 53157885 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,967,943 | 0.001641 | 53157885 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,363,988 | 0.029055 | 53157885 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/USDC | 150 | 5,232,555 | 2,330.906509 | 53157885 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,464,184 | 2,330.794487 | 53157885 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,215,664 | 0.998745 | 53157885 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,684,676 | 37,272.351590 | 53157885 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2510 | 3,175,215 | 0.028996 | 53157885 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2703 | 2,550,347 | 90.608222 | 53157885 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | WETH/USDC | 3000 | 2,356,722 | 2,325.444849 | 53157885 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | USDC/cbBTC | 472 | 2,222,756 | 0.000012 | 53157885 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome | WETH/FAI | 10000 | 2,121,181 | 1,218,183.889145 | 53157885 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,838,194 | 0.000000 | 53157885 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,835,099 | 0.018799 | 53157885 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,765,565 | 403.320771 | 53157885 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,692,173 | 0.000012 | 53157885 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | USDC/cbBTC | 338 | 1,688,969 | 0.000012 | 53157885 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,664,518 | 0.000012 | 53157885 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,508,218 | 0.005849 | 53157885 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,460,781 | 0.826827 | 53157885 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,453,150 | 1.698035 | 53157885 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | WETH/AERO | 3000 | 1,437,721 | 3,385.910463 | 53157885 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,372,709 | 13,897.054489 | 53157885 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,237,550 | 0.000266 | 53157885 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,230,455 | 2,330.396599 | 53157885 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,213,284 | 66.011115 | 53157885 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome | WETH/AERO | 10000 | 1,203,886 | 3,409.123374 | 53157885 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | VIRTUAL/WETH | 10000 | 1,171,086 | 0.000266 | 53157885 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome | WETH/WELL | 10000 | 1,151,101 | 1,069,914.247915 | 53157885 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | DRB/WETH | 10000 | 1,143,290 | 0.000000 | 53157885 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/doginme | 10000 | 1,139,742 | 37,177,108.460802 | 53157885 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,102,014 | 507,870.201558 | 53157885 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | WETH/EDEL | 7000 | 1,072,742 | 71,787.380027 | 53157885 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,044,931 | 21,163,489.858524 | 53157885 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,029,399 | 17.469940 | 53157885 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | USDC/VVV | 3000 | 1,028,634 | 0.038971 | 53157885 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | USDC/NOCK | 3000 | 1,021,452 | 59.997914 | 53157885 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/USDC | 10000 | 940,294 | 2,317.653415 | 53157885 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 911,875 | 1,066.820147 | 53157885 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome | WETH/msETH (stable) | 500 | 908,804 | 2.309463 | 53157885 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | uXRP/WETH | 3000 | 899,095 | 0.000560 | 53157885 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| uniswap_v3 | WETH/VVV | 10000 | 895,587 | 90.798647 | 53157885 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 871,815 | 18.217445 | 53157885 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v2 | WETH/USDC | 3000 | 845,835 | 2,325.050327 | 53157885 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 834,362 | 17.615855 | 53157885 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome_slipstream | AERO/cbBTC | 2700 | 804,405 | 0.000009 | 53157885 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| pancakeswap_v3 | QUID/USDC | 100 | 798,574 | 0.057190 | 53157885 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 787,234 | 0.803179 | 53157885 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 744,406 | 4,605,529.853202 | 53157885 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 742,676 | 0.618937 | 53157885 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/NPC | 3000 | 700,304 | 138,745.151447 | 53157885 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| uniswap_v3 | TIG/USDC | 10000 | 689,371 | 0.598064 | 53157885 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | WETH/BRETT | 2114 | 686,626 | 503,772.948014 | 53157885 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 672,195 | 0.108284 | 53157885 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |

## Recherche d'opportunités
- Cycles : 184 ; routes examinées : 3528016 ; candidats optimisés : 14453 ; net attendu > 0 : 20 ; dernier cycle 229.9 ms
- Rejets (moteur) : {'spread_below_threshold': 3480049, 'liquidity_below_min': 33128, 'negative_expected_net': 14433, 'borrow_bound_too_small': 386}
- Enregistrements de la session : 14453 ; net attendu > 0 : 20 ; simulés (eth_call de la vraie tx) : 0 (ok 0, échec 0) ; étiquettes ghost N+1 : 0/0 positives
- Décisions : {'REJECTED': 14453} ; motifs de rejet : {'below_safety_margin': 20, 'negative_expected_net': 14433, 'p_lower_below_threshold': 16, 'reliability_not_demonstrated': 4}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53157877 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 576.906943 USDC | 0.092155 USDC | 0.000000 USDC | 0.005585 USDC | 0.086570 USDC (0.0796 €) | — | 1.50 | 0.020 (n=105) | REJECTED | below_safety_margin(86570<115381), p_lower_below_threshold(0.02<0.75) |
| 53157877 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.247311 WETH | 0.000040 WETH | 0.000000 WETH | 0.000002 WETH | 0.000037 WETH (0.0794 €) | — | 1.50 | 0.020 (n=105) | REJECTED | below_safety_margin(37128881072348<49462128105230), p_lower_below_threshold(0.02<0.75) |
| 53157877 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 481.024479 USDC | 0.060505 USDC | 0.000000 USDC | 0.005232 USDC | 0.055273 USDC (0.0509 €) | — | 1.15 | 0.013 (n=22) | REJECTED | below_safety_margin(55273<96204), reliability_not_demonstrated |
| 53157877 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.206988 WETH | 0.000026 WETH | 0.000000 WETH | 0.000002 WETH | 0.000024 WETH (0.0507 €) | — | 1.15 | 0.013 (n=22) | REJECTED | below_safety_margin(23702945929398<41397618782382), reliability_not_demonstrated |
| 53157877 | cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.002884 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0140 €) | — | 0.66 | 0.129 (n=383) | REJECTED | below_safety_margin(19<57), p_lower_below_threshold(0.13<0.75) |
| 53157877 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 309.748452 USDC | 0.021832 USDC | 0.000000 USDC | 0.007001 USDC | 0.014831 USDC (0.0136 €) | — | 0.48 | 0.129 (n=383) | REJECTED | below_safety_margin(14831<61949), p_lower_below_threshold(0.13<0.75) |
| 53157877 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.133027 WETH | 0.000009 WETH | 0.000000 WETH | 0.000003 WETH | 0.000006 WETH (0.0136 €) | — | 0.48 | 0.129 (n=383) | REJECTED | below_safety_margin(6341750328914<26605403660291), p_lower_below_threshold(0.13<0.75) |
| 53157877 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 122.129349 USDC | 0.019850 USDC | 0.000000 USDC | 0.007001 USDC | 0.012849 USDC (0.0118 €) | — | 1.05 | 0.129 (n=383) | REJECTED | below_safety_margin(12849<24425), p_lower_below_threshold(0.13<0.75) |
| 53157877 | cbBTC→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.001325 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0118 €) | — | 1.21 | 0.129 (n=383) | REJECTED | below_safety_margin(16<26), p_lower_below_threshold(0.13<0.75) |
| 53157877 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→WETH | 0.055052 WETH | 0.000008 WETH | 0.000000 WETH | 0.000003 WETH | 0.000005 WETH (0.0113 €) | — | 0.96 | 0.129 (n=383) | REJECTED | below_safety_margin(5289966400506<11010498029567), p_lower_below_threshold(0.13<0.75) |
| 53157877 | USDC→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 103.513536 USDC | 0.014741 USDC | 0.000000 USDC | 0.007001 USDC | 0.007740 USDC (0.0071 €) | — | 0.75 | 0.167 (n=193) | REJECTED | below_safety_margin(7740<20702), p_lower_below_threshold(0.17<0.75) |
| 53157877 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→WETH | 0.043047 WETH | 0.000006 WETH | 0.000000 WETH | 0.000003 WETH | 0.000003 WETH (0.0069 €) | — | 0.75 | 0.167 (n=193) | REJECTED | below_safety_margin(3208459958558<8609318170970), p_lower_below_threshold(0.17<0.75) |
| 53157877 | cbBTC→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→cbBTC | 0.001105 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0066 €) | — | 0.81 | 0.167 (n=193) | REJECTED | below_safety_margin(9<22), p_lower_below_threshold(0.17<0.75) |
| 53157877 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 172.409956 USDC | 0.009997 USDC | 0.000000 USDC | 0.005232 USDC | 0.004765 USDC (0.0044 €) | — | 0.28 | 0.020 (n=105) | REJECTED | below_safety_margin(4765<34481), p_lower_below_threshold(0.02<0.75) |
| 53157877 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.074502 WETH | 0.000004 WETH | 0.000000 WETH | 0.000002 WETH | 0.000002 WETH (0.0044 €) | — | 0.27 | 0.020 (n=105) | REJECTED | below_safety_margin(2037081082119<14900439279245), p_lower_below_threshold(0.02<0.75) |
| 53157877 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 187.242944 USDC | 0.009304 USDC | 0.000000 USDC | 0.005232 USDC | 0.004072 USDC (0.0037 €) | — | 0.22 | 0.013 (n=22) | REJECTED | below_safety_margin(4072<37448), reliability_not_demonstrated |
| 53157877 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.081347 WETH | 0.000004 WETH | 0.000000 WETH | 0.000002 WETH | 0.000002 WETH (0.0037 €) | — | 0.21 | 0.013 (n=22) | REJECTED | below_safety_margin(1740386227825<16269483736123), reliability_not_demonstrated |
| 53157877 | cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→cbBTC | 0.002884 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0037 €) | — | 0.17 | 0.129 (n=383) | REJECTED | below_safety_margin(5<57), p_lower_below_threshold(0.13<0.75) |
| 53157877 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.077223 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0034 €) | — | 0.21 | 0.129 (n=383) | REJECTED | below_safety_margin(1605051696591<15444603430564), p_lower_below_threshold(0.13<0.75) |
| 53157877 | USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 223.085361 USDC | 0.010678 USDC | 0.000000 USDC | 0.007001 USDC | 0.003677 USDC (0.0034 €) | — | 0.16 | 0.129 (n=383) | REJECTED | below_safety_margin(3677<44617), p_lower_below_threshold(0.13<0.75) |

## Fiabilité et décision
- Observations ghost : 2832 ; taux observé 0.090 ; borne inférieure crédible (0.9) 0.083 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 8.3% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
