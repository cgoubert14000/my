# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-31T02:05:52+00:00 ; durée 67.85 min ; blocs 53309463 → 53311500 (1962 vus)

## Connexion
- Requêtes RPC : 23541 ; erreurs : 0 ; latence p50/p95 : 266.5/1,234.8 ms
- Rafraîchissements d'état : 1962 ; âge des données au dernier bloc : 3.74 s ; changements de frais LP observés (pools à frais dynamiques) : 2721
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 23326 ; cycles déclenchés par événement : 1864 ; avance médiane sur le rafraîchissement multicall : 704 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,242.90 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 506 pools, 291 jetons, 18872 routes
- Par DEX : uniswap_v3 137, aerodrome_slipstream 117, aerodrome 207, pancakeswap_v3 30, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 179 (rejetés 2) → 584 jetons ; pools candidats 3782 (énumérés 322, par paires 0), mesurés 509, sous le plancher de 10000.0 $ : 3 → gardés 506 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'DAI': 1.0, 'USDC': 1.0, 'WETH': 2241.465194, 'cbBTC': 77391.917525, 'AERO': 0.626719}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 150,422,727 | 2,242.900251 | 53311500 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,999,631 | 0.029007 | 53311500 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,252,705 | 0.000013 | 53311500 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,024,321 | 0.029063 | 53311500 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 8,195,504 | 2,241.069183 | 53311500 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,748,142 | 99.374381 | 53311500 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,708,638 | 0.001630 | 53311500 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 5,916,730 | 1.590411 | 53311500 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,577,578 | 0.029007 | 53311500 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/USDC | 150 | 4,143,778 | 2,241.770569 | 53311500 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,101,338 | 2,242.096020 | 53311500 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,066,175 | 1.000001 | 53311500 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,544,882 | 37,466.656309 | 53311500 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,751,313 | 0.029049 | 53311500 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2769 | 2,347,837 | 99.398402 | 53311500 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | WETH/FAI | 10000 | 2,056,170 | 1,206,344.208581 | 53311500 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 412 | 1,988,640 | 0.000013 | 53311500 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,767,140 | 0.000000 | 53311500 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,721,353 | 0.017443 | 53311500 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,684,086 | 420.244644 | 53311500 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,617,192 | 0.000013 | 53311500 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,584,187 | 0.000013 | 53311500 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | WETH/USDC | 3000 | 1,523,832 | 2,246.656400 | 53311500 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,520,145 | 1.536599 | 53311500 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,457,570 | 0.825600 | 53311500 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | USDC/cbBTC | 332 | 1,426,924 | 0.000013 | 53311500 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | WETH/AERO | 3000 | 1,423,807 | 3,563.255222 | 53311500 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,320,884 | 0.005181 | 53311500 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,305,611 | 14,445.527455 | 53311500 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,281,363 | 2,240.970984 | 53311500 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,176,817 | 70.165644 | 53311500 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,114,637 | 35,605,065.258765 | 53311500 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,059,924 | 513,128.942924 | 53311500 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,038,022 | 21,020,489.174102 | 53311500 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome | WETH/EDEL | 7000 | 1,025,738 | 73,022.709974 | 53311500 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | DRB/WETH | 10000 | 1,015,351 | 0.000000 | 53311500 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v2 | WETH/USDC | 3000 | 1,009,836 | 2,246.459548 | 53311500 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,002,122 | 18.834600 | 53311500 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | USDC/NOCK | 3000 | 974,707 | 65.892845 | 53311500 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/VVV | 10000 | 974,678 | 99.067896 | 53311500 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | USDC/VVV | 3000 | 957,096 | 0.044364 | 53311500 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | WETH/WELL | 10000 | 927,815 | 1,221,816.941141 | 53311500 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/USDC | 10000 | 920,414 | 2,235.963227 | 53311500 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 899,039 | 1,065.067782 | 53311500 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome | WETH/AERO | 10000 | 867,265 | 3,547.698845 | 53311500 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | uXRP/WETH | 3000 | 865,158 | 0.000557 | 53311500 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| pancakeswap_v3 | QUID/USDC | 100 | 848,443 | 0.064673 | 53311500 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome_slipstream | USDC/SAPIEN | 4570 | 848,201 | 19.075463 | 53311500 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome | WETH/wstETH | 3000 | 759,223 | 0.803531 | 53311500 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| aerodrome | VIRTUAL/WETH | 10000 | 739,623 | 0.000266 | 53311500 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 728,496 | 0.594257 | 53311500 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 728,442 | 4,478,950.712775 | 53311500 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 685,077 | 0.000008 | 53311500 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | WETH/msETH (stable) | 500 | 668,737 | 2.331523 | 53311500 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v2 | WETH/NPC | 3000 | 662,991 | 144,320.750576 | 53311500 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | WETH/BRETT | 2153 | 658,481 | 515,384.033972 | 53311500 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | TIG/USDC | 10000 | 633,929 | 0.507882 | 53311500 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 616,755 | 0.094072 | 53311500 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| aerodrome | WETH/bsdETH | 100 | 603,165 | 0.914818 | 53311500 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 544,936 | 1,064.789739 | 53311500 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |

## Recherche d'opportunités
- Cycles : 3825 ; routes examinées : 72185400 ; candidats optimisés : 389953 ; net attendu > 0 : 90 ; dernier cycle 243.2 ms
- Rejets (moteur) : {'spread_below_threshold': 70589821, 'liquidity_below_min': 1121230, 'negative_expected_net': 389863, 'pool_quarantined': 72346, 'unquotable': 7642, 'borrow_bound_too_small': 3822, 'cycle_budget_exhausted': 586}
- Enregistrements de la session : 389953 ; net attendu > 0 : 90 ; simulés (eth_call de la vraie tx) : 11 (ok 2, échec 9) ; étiquettes ghost N+1 : 0/5 positives
- Décisions : {'REJECTED': 389953} ; motifs de rejet : {'below_safety_margin': 79, 'negative_expected_net': 389863, 'p_lower_below_threshold': 81, 'price_impact': 5, 'reliability_not_demonstrated': 9, 'simulation_failed': 9, 'stale_data': 1}

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
| 53310557 | WETH→[uniswap_v3]→wstETH→[aerodrome_slipstream]→AERO→[pancakeswap_v3]→WETH | 0.011785 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0035 €) | — | 1.45 | 0.144 (n=648) | REJECTED | below_safety_margin(1705078259542<2356904996928), p_lower_below_threshold(0.14<0.75) |
| 53310557 | WETH→[uniswap_v3]→wstETH→[aerodrome_slipstream]→AERO→[pancakeswap_v3]→WETH | 0.011785 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0035 €) | — | 1.45 | 0.144 (n=648) | REJECTED | below_safety_margin(1705078259542<2356904996928), p_lower_below_threshold(0.14<0.75) |
| 53310558 | WETH→[uniswap_v3]→wstETH→[aerodrome_slipstream]→AERO→[pancakeswap_v3]→WETH | 0.011785 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0035 €) | — | 1.45 | 0.144 (n=648) | REJECTED | below_safety_margin(1705078259542<2356904996928), p_lower_below_threshold(0.14<0.75) |
| 53310033 | USDC→[aerodrome]→PLAY→[pancakeswap_v3]→USDC | 9.072945 USDC | 0.008244 USDC | 0.000000 USDC | 0.004727 USDC | 0.003517 USDC (0.0032 €) | — | 3.88 | 0.036 (n=23) | REJECTED | stale_data(4113ms>4000.0), simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53310623 | USDC→[aerodrome_slipstream]→cbBTC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 272.238999 USDC | 0.009873 USDC | 0.000000 USDC | 0.006746 USDC | 0.003127 USDC (0.0029 €) | — | 0.11 | 0.144 (n=648) | REJECTED | below_safety_margin(3127<54447), p_lower_below_threshold(0.14<0.75) |
| 53310623 | cbBTC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→cbBTC | 0.002768 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0028 €) | — | 0.14 | 0.144 (n=648) | REJECTED | below_safety_margin(4<55), p_lower_below_threshold(0.14<0.75) |
| 53310623 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→cbBTC→[uniswap_v3]→WETH | 0.118416 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0028 €) | — | 0.11 | 0.144 (n=648) | REJECTED | below_safety_margin(1343220230457<23683187834112), p_lower_below_threshold(0.14<0.75) |
| 53309666 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 123.408566 USDC | 0.009862 USDC | 0.000000 USDC | 0.007081 USDC | 0.002781 USDC (0.0026 €) | — | 0.23 | 0.144 (n=648) | REJECTED | below_safety_margin(2781<24681), p_lower_below_threshold(0.14<0.75) |
| 53309667 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 123.408566 USDC | 0.009862 USDC | 0.000000 USDC | 0.007081 USDC | 0.002781 USDC (0.0026 €) | — | 0.23 | 0.144 (n=648) | REJECTED | below_safety_margin(2781<24681), p_lower_below_threshold(0.14<0.75) |
| 53309666 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.054424 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0024 €) | — | 0.21 | 0.144 (n=648) | REJECTED | below_safety_margin(1167298084836<10884700978695), p_lower_below_threshold(0.14<0.75) |
| 53309667 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.054424 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0024 €) | — | 0.21 | 0.144 (n=648) | REJECTED | below_safety_margin(1167298084836<10884700978695), p_lower_below_threshold(0.14<0.75) |
| 53309666 | cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.001583 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0021 €) | — | 0.19 | 0.144 (n=648) | REJECTED | below_safety_margin(3<31), p_lower_below_threshold(0.14<0.75) |
| 53309667 | cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.001583 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0021 €) | — | 0.19 | 0.144 (n=648) | REJECTED | below_safety_margin(3<31), p_lower_below_threshold(0.14<0.75) |
| 53310557 | WETH→[aerodrome_slipstream]→wstETH→[aerodrome_slipstream]→AERO→[pancakeswap_v3]→WETH | 0.009824 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0021 €) | — | 1.05 | 0.144 (n=648) | REJECTED | below_safety_margin(1029366967275<1964817391652), p_lower_below_threshold(0.14<0.75) |
| 53310557 | WETH→[aerodrome_slipstream]→wstETH→[aerodrome_slipstream]→AERO→[pancakeswap_v3]→WETH | 0.009824 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0021 €) | — | 1.05 | 0.144 (n=648) | REJECTED | below_safety_margin(1029366967275<1964817391652), p_lower_below_threshold(0.14<0.75) |
| 53310558 | WETH→[aerodrome_slipstream]→wstETH→[aerodrome_slipstream]→AERO→[pancakeswap_v3]→WETH | 0.009824 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0021 €) | — | 1.05 | 0.144 (n=648) | REJECTED | below_safety_margin(1029366967275<1964817391652), p_lower_below_threshold(0.14<0.75) |

## Fiabilité et décision
- Observations ghost : 3903 ; taux observé 0.129 ; borne inférieure crédible (0.9) 0.122 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 12.2% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
