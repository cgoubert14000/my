# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-30T13:44:56+00:00 ; durée 3.01 min ; blocs 53289181 → 53289274 (91 vus)

## Connexion
- Requêtes RPC : 1107 ; erreurs : 0 ; latence p50/p95 : 70.4/957.7 ms
- Rafraîchissements d'état : 92 ; âge des données au dernier bloc : 0.9 s ; changements de frais LP observés (pools à frais dynamiques) : 263
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 2033 ; cycles déclenchés par événement : 123 ; avance médiane sur le rafraîchissement multicall : 238 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,224.45 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 498 pools, 287 jetons, 18738 routes
- Par DEX : uniswap_v3 137, aerodrome_slipstream 113, aerodrome 206, pancakeswap_v3 28, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 177 (rejetés 2) → 582 jetons ; pools candidats 3726 (énumérés 317, par paires 0), mesurés 501, sous le plancher de 10000.0 $ : 3 → gardés 498 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDC': 1.0, 'USDbC': 1.0, 'WETH': 2224.464255, 'cbBTC': 77004.393698, 'AERO': 0.620215}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 149,610,838 | 2,224.445496 | 53289274 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,064,675 | 0.028876 | 53289274 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,562,515 | 0.000013 | 53289274 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 8,996,963 | 0.028860 | 53289274 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 8,092,877 | 2,220.167555 | 53289274 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,733,642 | 100.128137 | 53289274 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,653,859 | 0.001615 | 53289274 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 6,050,134 | 1.616507 | 53289274 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,524,703 | 0.028885 | 53289274 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/USDC | 150 | 4,184,517 | 2,220.901801 | 53289274 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,052,363 | 0.999935 | 53289274 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,030,704 | 2,220.823866 | 53289274 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | WETH/KTA | 3000 | 3,543,610 | 36,879.105369 | 53289274 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,750,538 | 0.028852 | 53289274 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2700 | 2,311,319 | 100.105879 | 53289274 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | WETH/FAI | 10000 | 2,035,256 | 1,211,085.087564 | 53289274 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 592 | 1,914,962 | 0.000013 | 53289274 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | XDP/USDC | 100 | 1,780,087 | 0.018459 | 53289274 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,698,436 | 0.000000 | 53289274 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,674,224 | 417.145139 | 53289274 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,659,721 | 0.000013 | 53289274 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,566,284 | 0.000013 | 53289274 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | WETH/USDC | 3000 | 1,531,357 | 2,224.414203 | 53289274 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,463,389 | 1.643209 | 53289274 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | USDC/cbBTC | 360 | 1,461,634 | 0.000013 | 53289274 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,454,887 | 0.824971 | 53289274 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,396,751 | 3,589.558744 | 53289274 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,310,296 | 2,220.058086 | 53289274 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,302,050 | 14,437.913699 | 53289274 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,272,148 | 0.005028 | 53289274 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome | USDC/SEND | 3000 | 1,178,067 | 70.016773 | 53289274 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,097,693 | 36,265,727.250085 | 53289274 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,051,423 | 512,819.849502 | 53289274 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,027,636 | 21,083,127.034335 | 53289274 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome | WETH/EDEL | 7000 | 1,007,324 | 74,482.747035 | 53289274 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v2 | WETH/USDC | 3000 | 1,005,538 | 2,223.921161 | 53289274 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| uniswap_v3 | DRB/WETH | 10000 | 998,405 | 0.000000 | 53289274 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome_slipstream | USDC/VELVET | 100 | 993,096 | 19.329925 | 53289274 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | USDC/NOCK | 3000 | 968,598 | 66.726688 | 53289274 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/VVV | 10000 | 957,888 | 99.903217 | 53289274 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | USDC/VVV | 3000 | 954,480 | 0.045058 | 53289274 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | WETH/WELL | 10000 | 924,941 | 1,209,274.366068 | 53289274 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/USDC | 10000 | 917,355 | 2,231.397776 | 53289274 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 874,160 | 1,085.469537 | 53289274 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome | WETH/AERO | 10000 | 859,918 | 3,587.716388 | 53289274 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | uXRP/WETH | 3000 | 857,019 | 0.000556 | 53289274 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | USDC/SAPIEN | 4615 | 832,304 | 19.628289 | 53289274 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 812,208 | 0.059244 | 53289274 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 784,397 | 17.950100 | 53289274 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | WETH/wstETH | 3000 | 752,936 | 0.803616 | 53289274 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| aerodrome | VIRTUAL/WETH | 10000 | 726,045 | 0.000260 | 53289274 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 710,494 | 0.579740 | 53289274 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 708,075 | 4,661,925.388116 | 53289274 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 689,208 | 0.000008 | 53289274 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | WETH/msETH (stable) | 500 | 677,738 | 2.330067 | 53289274 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 653,217 | 515,184.867605 | 53289274 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v2 | WETH/NPC | 3000 | 651,199 | 147,091.457185 | 53289274 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| uniswap_v3 | TIG/USDC | 10000 | 640,152 | 0.517611 | 53289274 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 605,692 | 0.091551 | 53289274 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| aerodrome | WETH/bsdETH | 100 | 598,217 | 0.914771 | 53289274 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |

## Recherche d'opportunités
- Cycles : 214 ; routes examinées : 4009932 ; candidats optimisés : 20675 ; net attendu > 0 : 60 ; dernier cycle 162.3 ms
- Rejets (moteur) : {'spread_below_threshold': 3906961, 'liquidity_below_min': 79766, 'negative_expected_net': 20615, 'unquotable': 2316, 'borrow_bound_too_small': 214}
- Enregistrements de la session : 20675 ; net attendu > 0 : 60 ; simulés (eth_call de la vraie tx) : 0 (ok 0, échec 0) ; étiquettes ghost N+1 : 0/0 positives
- Décisions : {'REJECTED': 20675} ; motifs de rejet : {'below_safety_margin': 60, 'negative_expected_net': 20615, 'p_lower_below_threshold': 48, 'reliability_not_demonstrated': 12}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53289230 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.001653 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0113 €) | — | 0.97 | 0.137 (n=587) | REJECTED | below_safety_margin(16<33), p_lower_below_threshold(0.14<0.75) |
| 53289230 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.061630 WETH | 0.000008 WETH | 0.000000 WETH | 0.000003 WETH | 0.000005 WETH (0.0110 €) | — | 0.87 | 0.137 (n=587) | REJECTED | below_safety_margin(5358809215971<12326015959908), p_lower_below_threshold(0.14<0.75) |
| 53289230 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 130.045512 USDC | 0.018722 USDC | 0.000000 USDC | 0.006805 USDC | 0.011917 USDC (0.0110 €) | — | 0.92 | 0.137 (n=587) | REJECTED | below_safety_margin(11917<26009), p_lower_below_threshold(0.14<0.75) |
| 53289230 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.158629 WETH | 0.000008 WETH | 0.000000 WETH | 0.000003 WETH | 0.000005 WETH (0.0101 €) | — | 0.31 | 0.001 (n=14) | REJECTED | below_safety_margin(4949302033562<31725899691134), reliability_not_demonstrated |
| 53289230 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.158629 WETH | 0.000008 WETH | 0.000000 WETH | 0.000003 WETH | 0.000005 WETH (0.0101 €) | — | 0.31 | 0.001 (n=14) | REJECTED | below_safety_margin(4949302033562<31725899691134), reliability_not_demonstrated |
| 53289230 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 330.685080 USDC | 0.018098 USDC | 0.000000 USDC | 0.007143 USDC | 0.010955 USDC (0.0101 €) | — | 0.33 | 0.001 (n=14) | REJECTED | below_safety_margin(10955<66137), reliability_not_demonstrated |
| 53289230 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 330.685080 USDC | 0.018098 USDC | 0.000000 USDC | 0.007143 USDC | 0.010955 USDC (0.0101 €) | — | 0.33 | 0.001 (n=14) | REJECTED | below_safety_margin(10955<66137), reliability_not_demonstrated |
| 53289230 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.002340 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0099 €) | — | 0.60 | 0.001 (n=14) | REJECTED | below_safety_margin(14<46), reliability_not_demonstrated |
| 53289230 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.004065 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0099 €) | — | 0.34 | 0.001 (n=14) | REJECTED | below_safety_margin(14<81), reliability_not_demonstrated |
| 53289230 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.002340 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0099 €) | — | 0.60 | 0.001 (n=14) | REJECTED | below_safety_margin(14<46), reliability_not_demonstrated |
| 53289230 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.004065 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0099 €) | — | 0.34 | 0.001 (n=14) | REJECTED | below_safety_margin(14<81), reliability_not_demonstrated |
| 53289230 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 322.350762 USDC | 0.017286 USDC | 0.000000 USDC | 0.007143 USDC | 0.010143 USDC (0.0093 €) | — | 0.31 | 0.137 (n=587) | REJECTED | below_safety_margin(10143<64470), p_lower_below_threshold(0.14<0.75) |
| 53289230 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 322.350762 USDC | 0.017286 USDC | 0.000000 USDC | 0.007143 USDC | 0.010143 USDC (0.0093 €) | — | 0.31 | 0.137 (n=587) | REJECTED | below_safety_margin(10143<64470), p_lower_below_threshold(0.14<0.75) |
| 53289230 | WETH→[uniswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.161303 WETH | 0.000008 WETH | 0.000000 WETH | 0.000003 WETH | 0.000005 WETH (0.0093 €) | — | 0.28 | 0.137 (n=587) | REJECTED | below_safety_margin(4551016518510<32260648189832), p_lower_below_threshold(0.14<0.75) |
| 53289230 | WETH→[uniswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.161303 WETH | 0.000008 WETH | 0.000000 WETH | 0.000003 WETH | 0.000005 WETH (0.0093 €) | — | 0.28 | 0.137 (n=587) | REJECTED | below_safety_margin(4551016518510<32260648189832), p_lower_below_threshold(0.14<0.75) |
| 53289230 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 206.925658 USDC | 0.017250 USDC | 0.000000 USDC | 0.007143 USDC | 0.010107 USDC (0.0093 €) | — | 0.49 | 0.001 (n=14) | REJECTED | below_safety_margin(10107<41385), reliability_not_demonstrated |
| 53289230 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 206.925658 USDC | 0.017250 USDC | 0.000000 USDC | 0.007143 USDC | 0.010107 USDC (0.0093 €) | — | 0.49 | 0.001 (n=14) | REJECTED | below_safety_margin(10107<41385), reliability_not_demonstrated |
| 53289230 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→cbBTC | 0.004060 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0092 €) | — | 0.32 | 0.137 (n=587) | REJECTED | below_safety_margin(13<81), p_lower_below_threshold(0.14<0.75) |
| 53289230 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→cbBTC | 0.004060 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0092 €) | — | 0.32 | 0.137 (n=587) | REJECTED | below_safety_margin(13<81), p_lower_below_threshold(0.14<0.75) |
| 53289230 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.091505 WETH | 0.000008 WETH | 0.000000 WETH | 0.000003 WETH | 0.000004 WETH (0.0089 €) | — | 0.48 | 0.001 (n=14) | REJECTED | below_safety_margin(4366705491212<18301012521479), reliability_not_demonstrated |
| 53289230 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.091505 WETH | 0.000008 WETH | 0.000000 WETH | 0.000003 WETH | 0.000004 WETH (0.0089 €) | — | 0.48 | 0.001 (n=14) | REJECTED | below_safety_margin(4366705491212<18301012521479), reliability_not_demonstrated |
| 53289230 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.001566 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0078 €) | — | 0.70 | 0.137 (n=587) | REJECTED | below_safety_margin(11<31), p_lower_below_threshold(0.14<0.75) |
| 53289230 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.072386 WETH | 0.000007 WETH | 0.000000 WETH | 0.000003 WETH | 0.000004 WETH (0.0073 €) | — | 0.49 | 0.137 (n=587) | REJECTED | below_safety_margin(3582490520149<14477132614050), p_lower_below_threshold(0.14<0.75) |
| 53289230 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 160.835990 USDC | 0.014696 USDC | 0.000000 USDC | 0.006805 USDC | 0.007891 USDC (0.0073 €) | — | 0.49 | 0.137 (n=587) | REJECTED | below_safety_margin(7891<32167), p_lower_below_threshold(0.14<0.75) |
| 53289230 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH→[uniswap_v3]→cbBTC | 0.001481 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0071 €) | — | 0.68 | 0.137 (n=587) | REJECTED | below_safety_margin(10<29), p_lower_below_threshold(0.14<0.75) |

## Fiabilité et décision
- Observations ghost : 3650 ; taux observé 0.116 ; borne inférieure crédible (0.9) 0.110 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 11.0% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
