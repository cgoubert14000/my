# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-01T06:32:55+00:00 ; durée 92.39 min ; blocs 53359939 → 53362712 (2767 vus)

## Connexion
- Requêtes RPC : 32474 ; erreurs : 0 ; latence p50/p95 : 63.9/919.8 ms
- Rafraîchissements d'état : 2768 ; âge des données au dernier bloc : 1.43 s ; changements de frais LP observés (pools à frais dynamiques) : 1888
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 5585 ; cycles déclenchés par événement : 1058 ; avance médiane sur le rafraîchissement multicall : 398 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,265.71 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 502 pools, 289 jetons, 18760 routes
- Par DEX : uniswap_v3 139, aerodrome_slipstream 114, aerodrome 206, pancakeswap_v3 29, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 178 (rejetés 2) → 583 jetons ; pools candidats 3742 (énumérés 318, par paires 0), mesurés 505, sous le plancher de 10000.0 $ : 3 → gardés 502 (max 1500) ; prix des hubs : {'USDC': 1.0, 'USDbC': 1.0, 'DAI': 1.0, 'WETH': 2265.714788, 'cbBTC': 77709.69565, 'AERO': 0.641921}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 150,871,424 | 2,265.709679 | 53362712 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,148,272 | 0.029131 | 53362712 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,340,963 | 0.000013 | 53362712 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,107,810 | 0.029145 | 53362712 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| aerodrome | WETH/VVV | 3000 | 7,924,524 | 96.731392 | 53362712 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/USDC | 500 | 7,894,040 | 2,267.644552 | 53362712 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,695,943 | 0.001605 | 53362712 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 5,764,037 | 1.550153 | 53362712 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,160,603 | 0.029120 | 53362712 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,095,227 | 0.998845 | 53362712 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome_slipstream | WETH/USDC | 150 | 4,068,606 | 2,267.113357 | 53362712 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/USDC | 100 | 3,987,082 | 2,266.948778 | 53362712 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | WETH/KTA | 3000 | 3,561,521 | 37,876.046274 | 53362712 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,702,312 | 0.029157 | 53362712 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2709 | 2,427,257 | 96.767354 | 53362712 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | USDC/cbBTC | 400 | 2,187,750 | 0.000013 | 53362712 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome | WETH/FAI | 10000 | 2,083,152 | 1,199,321.852139 | 53362712 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,764,287 | 0.000000 | 53362712 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,710,846 | 0.017303 | 53362712 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,678,739 | 0.000013 | 53362712 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,586,376 | 0.000013 | 53362712 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,561,631 | 420.763478 | 53362712 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,537,008 | 1.499750 | 53362712 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v2 | WETH/USDC | 3000 | 1,507,909 | 2,268.617342 | 53362712 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,457,455 | 0.825724 | 53362712 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,439,449 | 3,515.863927 | 53362712 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | WETH/USDC | 3000 | 1,412,136 | 2,273.776252 | 53362712 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,349,501 | 2,267.754672 | 53362712 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,324,579 | 0.005159 | 53362712 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,315,173 | 14,458.494474 | 53362712 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome_slipstream | USDC/cbBTC | 332 | 1,308,533 | 0.000013 | 53362712 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/SEND | 3000 | 1,170,289 | 70.950596 | 53362712 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,142,558 | 34,082,960.896487 | 53362712 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,075,033 | 508,418.248226 | 53362712 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,067,292 | 0.000000 | 53362712 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,032,958 | 21,602,651.733132 | 53362712 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome | WETH/EDEL | 7000 | 1,003,474 | 77,821.018976 | 53362712 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/VVV | 10000 | 1,002,494 | 96.055338 | 53362712 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome_slipstream | USDC/VELVET | 100 | 999,272 | 18.988612 | 53362712 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | USDC/VVV | 3000 | 990,332 | 0.042679 | 53362712 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | USDC/NOCK | 3000 | 974,542 | 65.916065 | 53362712 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome | WETH/WELL | 10000 | 962,632 | 1,158,223.277826 | 53362712 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/MORPHO | 3000 | 948,671 | 978.350801 | 53362712 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/USDC | 10000 | 927,752 | 2,249.741211 | 53362712 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome | WETH/AERO | 10000 | 881,178 | 3,504.632835 | 53362712 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | uXRP/WETH | 3000 | 867,606 | 0.000549 | 53362712 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 838,953 | 19.406084 | 53362712 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 821,565 | 0.060723 | 53362712 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 767,167 | 0.803065 | 53362712 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| aerodrome | VIRTUAL/WETH | 10000 | 737,673 | 0.000261 | 53362712 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 725,872 | 0.595697 | 53362712 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 715,057 | 4,743,861.262014 | 53362712 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 696,500 | 0.000008 | 53362712 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v2 | WETH/NPC | 3000 | 676,359 | 141,528.663406 | 53362712 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | WETH/BRETT | 2102 | 668,249 | 505,960.389852 | 53362712 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome | WETH/msETH (stable) | 500 | 660,282 | 2.338701 | 53362712 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | TIG/USDC | 10000 | 658,547 | 0.545923 | 53362712 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 614,508 | 0.093509 | 53362712 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| aerodrome | WETH/bsdETH | 100 | 608,113 | 0.916175 | 53362712 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome_slipstream | WETH/MORPHO | 2703 | 556,508 | 978.556794 | 53362712 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |

## Recherche d'opportunités
- Cycles : 3825 ; routes examinées : 71757000 ; candidats optimisés : 292679 ; net attendu > 0 : 67 ; dernier cycle 309.7 ms
- Rejets (moteur) : {'spread_below_threshold': 70306408, 'liquidity_below_min': 1146438, 'negative_expected_net': 292612, 'unquotable': 7650, 'borrow_bound_too_small': 3825}
- Enregistrements de la session : 292679 ; net attendu > 0 : 67 ; simulés (eth_call de la vraie tx) : 0 (ok 0, échec 0) ; étiquettes ghost N+1 : 0/0 positives
- Décisions : {'REJECTED': 292679} ; motifs de rejet : {'below_safety_margin': 67, 'negative_expected_net': 292612, 'p_lower_below_threshold': 67}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53360865 | WETH→[uniswap_v3]→AAVE→[pancakeswap_v3]→WETH | 0.023511 WETH | 0.000007 WETH | 0.000000 WETH | 0.000002 WETH | 0.000004 WETH (0.0093 €) | — | 1.90 | 0.043 (n=154) | REJECTED | below_safety_margin(4456871587155<4702111714852), p_lower_below_threshold(0.04<0.75) |
| 53360511 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.000556 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0021 €) | — | 0.54 | 0.140 (n=666) | REJECTED | below_safety_margin(3<11), p_lower_below_threshold(0.14<0.75) |
| 53360511 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.000556 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0021 €) | — | 0.54 | 0.140 (n=666) | REJECTED | below_safety_margin(3<11), p_lower_below_threshold(0.14<0.75) |
| 53360511 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 46.386008 USDC | 0.008923 USDC | 0.000000 USDC | 0.006808 USDC | 0.002115 USDC (0.0019 €) | — | 0.46 | 0.140 (n=666) | REJECTED | below_safety_margin(2115<9277), p_lower_below_threshold(0.14<0.75) |
| 53360511 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 46.386008 USDC | 0.008923 USDC | 0.000000 USDC | 0.006808 USDC | 0.002115 USDC (0.0019 €) | — | 0.46 | 0.140 (n=666) | REJECTED | below_safety_margin(2115<9277), p_lower_below_threshold(0.14<0.75) |
| 53361161 | WETH→[pancakeswap_v3]→EURC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.026592 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0014 €) | — | 0.26 | 0.140 (n=666) | REJECTED | below_safety_margin(693398805761<5318334343811), p_lower_below_threshold(0.14<0.75) |
| 53361161 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→EURC→[aerodrome_slipstream]→USDC | 60.106831 USDC | 0.008712 USDC | 0.000000 USDC | 0.007152 USDC | 0.001560 USDC (0.0014 €) | — | 0.26 | 0.140 (n=666) | REJECTED | below_safety_margin(1560<12021), p_lower_below_threshold(0.14<0.75) |
| 53361925 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→EURC→[aerodrome_slipstream]→cbBTC | 0.000273 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0014 €) | — | 0.73 | 0.140 (n=666) | REJECTED | below_safety_margin(2<5), p_lower_below_threshold(0.14<0.75) |
| 53361925 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→EURC→[aerodrome_slipstream]→cbBTC | 0.000273 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0014 €) | — | 0.73 | 0.140 (n=666) | REJECTED | below_safety_margin(2<5), p_lower_below_threshold(0.14<0.75) |
| 53361925 | USDC→[aerodrome_slipstream]→EURC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 21.651624 USDC | 0.002658 USDC | 0.000000 USDC | 0.001141 USDC | 0.001517 USDC (0.0014 €) | — | 0.70 | 0.140 (n=666) | REJECTED | below_safety_margin(1517<4330), p_lower_below_threshold(0.14<0.75) |
| 53360014 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.004348 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0013 €) | — | 1.45 | 0.189 (n=283) | REJECTED | below_safety_margin(629547186721<869576446142), p_lower_below_threshold(0.19<0.75) |
| 53360014 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.004348 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0013 €) | — | 1.45 | 0.189 (n=283) | REJECTED | below_safety_margin(629547186721<869576446142), p_lower_below_threshold(0.19<0.75) |
| 53360014 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 9.906459 USDC | 0.008234 USDC | 0.000000 USDC | 0.006808 USDC | 0.001426 USDC (0.0013 €) | — | 1.44 | 0.189 (n=283) | REJECTED | below_safety_margin(1426<1981), p_lower_below_threshold(0.19<0.75) |
| 53360014 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 9.906459 USDC | 0.008234 USDC | 0.000000 USDC | 0.006808 USDC | 0.001426 USDC (0.0013 €) | — | 1.44 | 0.189 (n=283) | REJECTED | below_safety_margin(1426<1981), p_lower_below_threshold(0.19<0.75) |
| 53361925 | USDC→[aerodrome_slipstream]→EURC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 21.351346 USDC | 0.002442 USDC | 0.000000 USDC | 0.001141 USDC | 0.001301 USDC (0.0012 €) | — | 0.61 | 0.140 (n=666) | REJECTED | below_safety_margin(1301<4270), p_lower_below_threshold(0.14<0.75) |
| 53361140 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.004282 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0007 €) | — | 0.80 | 0.189 (n=283) | REJECTED | below_safety_margin(343341129493<856390021177), p_lower_below_threshold(0.19<0.75) |
| 53361141 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.004282 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0007 €) | — | 0.80 | 0.189 (n=283) | REJECTED | below_safety_margin(343341129493<856390021177), p_lower_below_threshold(0.19<0.75) |
| 53361142 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.004282 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0007 €) | — | 0.80 | 0.189 (n=283) | REJECTED | below_safety_margin(343341129493<856390021177), p_lower_below_threshold(0.19<0.75) |
| 53361143 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.004282 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0007 €) | — | 0.80 | 0.189 (n=283) | REJECTED | below_safety_margin(343192112381<856390021177), p_lower_below_threshold(0.19<0.75) |
| 53361144 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.004282 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0007 €) | — | 0.80 | 0.189 (n=283) | REJECTED | below_safety_margin(343192112381<856390021177), p_lower_below_threshold(0.19<0.75) |
| 53361140 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 9.633559 USDC | 0.007578 USDC | 0.000000 USDC | 0.006808 USDC | 0.000770 USDC (0.0007 €) | — | 0.80 | 0.189 (n=283) | REJECTED | below_safety_margin(770<1926), p_lower_below_threshold(0.19<0.75) |
| 53361141 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 9.633559 USDC | 0.007578 USDC | 0.000000 USDC | 0.006808 USDC | 0.000770 USDC (0.0007 €) | — | 0.80 | 0.189 (n=283) | REJECTED | below_safety_margin(770<1926), p_lower_below_threshold(0.19<0.75) |
| 53361142 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 9.633559 USDC | 0.007578 USDC | 0.000000 USDC | 0.006808 USDC | 0.000770 USDC (0.0007 €) | — | 0.80 | 0.189 (n=283) | REJECTED | below_safety_margin(770<1926), p_lower_below_threshold(0.19<0.75) |
| 53361143 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 9.633559 USDC | 0.007578 USDC | 0.000000 USDC | 0.006808 USDC | 0.000770 USDC (0.0007 €) | — | 0.80 | 0.189 (n=283) | REJECTED | below_safety_margin(770<1926), p_lower_below_threshold(0.19<0.75) |
| 53361144 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 9.633559 USDC | 0.007578 USDC | 0.000000 USDC | 0.006808 USDC | 0.000770 USDC (0.0007 €) | — | 0.80 | 0.189 (n=283) | REJECTED | below_safety_margin(770<1926), p_lower_below_threshold(0.19<0.75) |

## Fiabilité et décision
- Observations ghost : 4038 ; taux observé 0.129 ; borne inférieure crédible (0.9) 0.122 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 12.2% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
