# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-31T01:25:41+00:00 ; durée 27.67 min ; blocs 53309463 → 53310295 (775 vus)

## Connexion
- Requêtes RPC : 9484 ; erreurs : 0 ; latence p50/p95 : 366.0/1,309.4 ms
- Rafraîchissements d'état : 775 ; âge des données au dernier bloc : 6.33 s ; changements de frais LP observés (pools à frais dynamiques) : 1066
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 11266 ; cycles déclenchés par événement : 700 ; avance médiane sur le rafraîchissement multicall : 1,163 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,242.90 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 506 pools, 291 jetons, 18872 routes
- Par DEX : uniswap_v3 137, aerodrome_slipstream 117, aerodrome 207, pancakeswap_v3 30, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 179 (rejetés 2) → 584 jetons ; pools candidats 3782 (énumérés 322, par paires 0), mesurés 509, sous le plancher de 10000.0 $ : 3 → gardés 506 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'DAI': 1.0, 'USDC': 1.0, 'WETH': 2241.465194, 'cbBTC': 77391.917525, 'AERO': 0.626719}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 150,416,179 | 2,242.898387 | 53310293 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,992,283 | 0.028990 | 53310293 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,255,528 | 0.000013 | 53310295 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,026,605 | 0.029063 | 53310293 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 8,195,374 | 2,242.884133 | 53310295 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,751,283 | 99.293930 | 53310295 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,714,090 | 0.001630 | 53310293 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 5,925,424 | 1.585747 | 53310293 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,569,265 | 0.028994 | 53310293 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/USDC | 639 | 4,143,812 | 2,242.114997 | 53310295 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,069,243 | 1.000000 | 53310293 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,051,694 | 2,241.985183 | 53310295 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | WETH/KTA | 3000 | 3,544,472 | 37,475.281767 | 53310293 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2510 | 2,751,700 | 0.029049 | 53310293 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2709 | 2,348,869 | 99.349043 | 53310293 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | WETH/FAI | 10000 | 2,056,168 | 1,206,344.208581 | 53310293 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 484 | 1,989,489 | 0.000013 | 53310295 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,767,178 | 0.000000 | 53310293 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,730,124 | 0.017584 | 53310293 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,686,610 | 418.395064 | 53310293 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,617,986 | 0.000013 | 53310295 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,569,739 | 0.000013 | 53310293 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | WETH/USDC | 3000 | 1,523,832 | 2,248.807280 | 53310295 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,520,145 | 1.536599 | 53310293 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,457,570 | 0.825600 | 53310293 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | USDC/cbBTC | 346 | 1,427,978 | 0.000013 | 53310295 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | WETH/AERO | 3000 | 1,426,077 | 3,561.554894 | 53310293 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,313,751 | 2,242.882426 | 53310295 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,310,279 | 0.005131 | 53310293 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,308,414 | 14,431.113043 | 53310293 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | USDC/SEND | 3000 | 1,176,817 | 70.165644 | 53310293 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,114,636 | 35,605,065.258765 | 53310293 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,059,662 | 513,477.219299 | 53310293 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,038,021 | 21,020,489.174102 | 53310293 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome | WETH/EDEL | 7000 | 1,024,810 | 73,154.893477 | 53310294 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | DRB/WETH | 10000 | 1,016,330 | 0.000000 | 53310293 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v2 | WETH/USDC | 3000 | 1,009,778 | 2,242.367982 | 53310293 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,004,406 | 18.712950 | 53310293 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/VVV | 10000 | 975,136 | 99.068168 | 53310293 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome | USDC/NOCK | 3000 | 973,713 | 66.027555 | 53310293 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | USDC/VVV | 3000 | 957,626 | 0.044258 | 53310293 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | WETH/WELL | 10000 | 927,885 | 1,221,631.480308 | 53310293 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/USDC | 10000 | 920,540 | 2,235.963227 | 53310293 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 896,168 | 1,072.311325 | 53310293 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome | WETH/AERO | 10000 | 868,540 | 3,580.729527 | 53310293 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | uXRP/WETH | 3000 | 865,158 | 0.000557 | 53310293 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | USDC/SAPIEN | 4505 | 849,387 | 19.033920 | 53310293 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 844,575 | 0.064433 | 53310293 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 759,222 | 0.803531 | 53310293 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| aerodrome | VIRTUAL/WETH | 10000 | 739,622 | 0.000266 | 53310293 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 728,826 | 0.595793 | 53310293 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 728,466 | 4,478,645.879136 | 53310293 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 686,322 | 0.000008 | 53310293 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | WETH/msETH (stable) | 500 | 680,685 | 2.331396 | 53310293 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v2 | WETH/NPC | 3000 | 662,991 | 144,320.750576 | 53310293 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | WETH/BRETT | 2096 | 658,243 | 511,169.611316 | 53310293 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | TIG/USDC | 10000 | 633,929 | 0.507882 | 53310293 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 622,011 | 0.095317 | 53310293 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| aerodrome | WETH/bsdETH | 100 | 603,164 | 0.914818 | 53310293 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome_slipstream | WETH/MORPHO | 2709 | 542,900 | 1,072.120571 | 53310293 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |

## Recherche d'opportunités
- Cycles : 1474 ; routes examinées : 27817328 ; candidats optimisés : 203501 ; net attendu > 0 : 44 ; dernier cycle 494.5 ms
- Rejets (moteur) : {'spread_below_threshold': 27318985, 'liquidity_below_min': 290148, 'negative_expected_net': 203457, 'unquotable': 2948, 'borrow_bound_too_small': 1474, 'cycle_budget_exhausted': 272}
- Enregistrements de la session : 203501 ; net attendu > 0 : 44 ; simulés (eth_call de la vraie tx) : 6 (ok 2, échec 4) ; étiquettes ghost N+1 : 0/4 positives
- Décisions : {'REJECTED': 203501} ; motifs de rejet : {'below_safety_margin': 38, 'negative_expected_net': 203457, 'p_lower_below_threshold': 43, 'reliability_not_demonstrated': 1, 'simulation_failed': 4, 'stale_data': 1}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53309650 | cbBTC→[uniswap_v3]→AERO→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.000493 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0050 €) | — | 1.42 | 0.144 (n=648) | REJECTED | below_safety_margin(7<9), p_lower_below_threshold(0.14<0.75) |
| 53309651 | cbBTC→[uniswap_v3]→AERO→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.000493 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0050 €) | — | 1.42 | 0.144 (n=648) | REJECTED | below_safety_margin(7<9), p_lower_below_threshold(0.14<0.75) |
| 53309650 | WETH→[uniswap_v3]→wstETH→[aerodrome]→AERO→[pancakeswap_v3]→WETH | 0.008857 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0047 €) | 0.000002 WETH | 2.58 | 0.285 (n=80) | REJECTED | p_lower_below_threshold(0.28<0.75) |
| 53309651 | WETH→[uniswap_v3]→wstETH→[aerodrome]→AERO→[pancakeswap_v3]→WETH | 0.008857 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0047 €) | — | 2.58 | 0.285 (n=80) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.28<0.75) |
| 53309650 | USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→AERO→[uniswap_v3]→USDC | 30.718101 USDC | 0.011829 USDC | 0.000000 USDC | 0.006741 USDC | 0.005088 USDC (0.0047 €) | — | 1.66 | 0.144 (n=648) | REJECTED | below_safety_margin(5088<6143), p_lower_below_threshold(0.14<0.75) |
| 53309651 | USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→AERO→[uniswap_v3]→USDC | 30.718101 USDC | 0.011829 USDC | 0.000000 USDC | 0.006741 USDC | 0.005088 USDC (0.0047 €) | — | 1.66 | 0.144 (n=648) | REJECTED | below_safety_margin(5088<6143), p_lower_below_threshold(0.14<0.75) |
| 53309650 | WETH→[aerodrome_slipstream]→wstETH→[aerodrome]→AERO→[pancakeswap_v3]→WETH | 0.008258 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0044 €) | 0.000002 WETH | 2.58 | 0.285 (n=80) | REJECTED | p_lower_below_threshold(0.28<0.75) |
| 53309651 | WETH→[aerodrome_slipstream]→wstETH→[aerodrome]→AERO→[pancakeswap_v3]→WETH | 0.008258 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0044 €) | — | 2.58 | 0.285 (n=80) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.28<0.75) |
| 53310270 | USDC→[pancakeswap_v3]→PLAY→[aerodrome_slipstream]→USDC | 20.246524 USDC | 0.009596 USDC | 0.000000 USDC | 0.005038 USDC | 0.004558 USDC (0.0042 €) | — | 2.25 | 0.039 (n=151) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.04<0.75) |
| 53310033 | USDC→[aerodrome]→PLAY→[pancakeswap_v3]→USDC | 9.072945 USDC | 0.008244 USDC | 0.000000 USDC | 0.004727 USDC | 0.003517 USDC (0.0032 €) | — | 3.88 | 0.036 (n=23) | REJECTED | stale_data(4113ms>4000.0), simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53309666 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 123.408566 USDC | 0.009862 USDC | 0.000000 USDC | 0.007081 USDC | 0.002781 USDC (0.0026 €) | — | 0.23 | 0.144 (n=648) | REJECTED | below_safety_margin(2781<24681), p_lower_below_threshold(0.14<0.75) |
| 53309667 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 123.408566 USDC | 0.009862 USDC | 0.000000 USDC | 0.007081 USDC | 0.002781 USDC (0.0026 €) | — | 0.23 | 0.144 (n=648) | REJECTED | below_safety_margin(2781<24681), p_lower_below_threshold(0.14<0.75) |
| 53309666 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.054424 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0024 €) | — | 0.21 | 0.144 (n=648) | REJECTED | below_safety_margin(1167298084836<10884700978695), p_lower_below_threshold(0.14<0.75) |
| 53309667 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.054424 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0024 €) | — | 0.21 | 0.144 (n=648) | REJECTED | below_safety_margin(1167298084836<10884700978695), p_lower_below_threshold(0.14<0.75) |
| 53309666 | cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.001583 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0021 €) | — | 0.19 | 0.144 (n=648) | REJECTED | below_safety_margin(3<31), p_lower_below_threshold(0.14<0.75) |
| 53309667 | cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.001583 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0021 €) | — | 0.19 | 0.144 (n=648) | REJECTED | below_safety_margin(3<31), p_lower_below_threshold(0.14<0.75) |
| 53309666 | cbBTC→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.000801 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0014 €) | — | 0.25 | 0.144 (n=648) | REJECTED | below_safety_margin(2<16), p_lower_below_threshold(0.14<0.75) |
| 53309667 | cbBTC→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.000801 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0014 €) | — | 0.25 | 0.144 (n=648) | REJECTED | below_safety_margin(2<16), p_lower_below_threshold(0.14<0.75) |
| 53309650 | WETH→[aerodrome]→wstETH→[aerodrome]→AERO→[pancakeswap_v3]→WETH | 0.006969 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0014 €) | — | 0.99 | 0.119 (n=64) | REJECTED | below_safety_margin(688741858136<1393804240133), p_lower_below_threshold(0.12<0.75) |
| 53309651 | WETH→[aerodrome]→wstETH→[aerodrome]→AERO→[pancakeswap_v3]→WETH | 0.006969 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0014 €) | — | 0.99 | 0.119 (n=64) | REJECTED | below_safety_margin(688741858136<1393804240133), p_lower_below_threshold(0.12<0.75) |
| 53309666 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 63.193900 USDC | 0.008613 USDC | 0.000000 USDC | 0.007081 USDC | 0.001532 USDC (0.0014 €) | — | 0.24 | 0.144 (n=648) | REJECTED | below_safety_margin(1532<12638), p_lower_below_threshold(0.14<0.75) |
| 53309667 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 63.193900 USDC | 0.008613 USDC | 0.000000 USDC | 0.007081 USDC | 0.001532 USDC (0.0014 €) | — | 0.24 | 0.144 (n=648) | REJECTED | below_safety_margin(1532<12638), p_lower_below_threshold(0.14<0.75) |
| 53309666 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→WETH | 0.027876 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0013 €) | — | 0.23 | 0.144 (n=648) | REJECTED | below_safety_margin(627272668257<5575176226241), p_lower_below_threshold(0.14<0.75) |
| 53309667 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→WETH | 0.027876 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0013 €) | — | 0.23 | 0.144 (n=648) | REJECTED | below_safety_margin(627272668257<5575176226241), p_lower_below_threshold(0.14<0.75) |
| 53309666 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 31.995096 USDC | 0.006118 USDC | 0.000000 USDC | 0.005037 USDC | 0.001081 USDC (0.0010 €) | — | 0.34 | 0.007 (n=40) | REJECTED | below_safety_margin(1081<6399), p_lower_below_threshold(0.01<0.75) |

## Fiabilité et décision
- Observations ghost : 3902 ; taux observé 0.129 ; borne inférieure crédible (0.9) 0.122 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 12.2% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
