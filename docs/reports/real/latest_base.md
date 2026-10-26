# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-26T13:37:31+00:00 ; durée 300.0 min ; blocs 53107248 → 53116248 (8708 vus)

## Connexion
- Requêtes RPC : 102209 ; erreurs : 85 ; latence p50/p95 : 397.3/1,522.3 ms
- Rafraîchissements d'état : 8708 ; âge des données au dernier bloc : 2.7 s ; changements de frais LP observés (pools à frais dynamiques) : 15870
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 20005 ; cycles déclenchés par événement : 1392 ; avance médiane sur le rafraîchissement multicall : 466 ms
- Gaz : base fee 0.005797 gwei ; prix ETH (pool le plus profond) : 2,302.94 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 527 pools, 302 jetons, 19574 routes
- Par DEX : uniswap_v3 142, aerodrome 213, aerodrome_slipstream 127, pancakeswap_v3 30, uniswap_v2 12, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 188 (rejetés 2) → 593 jetons ; pools candidats 3779 (énumérés 339, par paires 0), mesurés 529, sous le plancher de 10000.0 $ : 2 → gardés 527 (max 1500) ; prix des hubs : {'USDC': 1.0, 'DAI': 1.0, 'USDbC': 1.0, 'WETH': 2317.899718, 'cbBTC': 80102.759686, 'AERO': 0.672129}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 157,072,514 | 2,302.941708 | 53116248 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,612,597 | 0.028983 | 53116248 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,093,376 | 0.028978 | 53116248 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,437,616 | 0.000013 | 53116248 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome | WETH/VVV | 3000 | 8,732,316 | 94.099046 | 53116248 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/USDC | 500 | 8,264,671 | 2,306.539546 | 53116248 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | USDC/AERO | 3000 | 7,125,680 | 1.497254 | 53116248 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,945,740 | 0.001655 | 53116248 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | WETH/USDC | 654 | 5,355,768 | 2,307.210661 | 53116248 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,317,611 | 0.028990 | 53116248 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,430,303 | 2,307.272987 | 53116248 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,181,694 | 0.999621 | 53116248 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,775,120 | 34,832.986301 | 53116248 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/USDC | 3000 | 3,732,607 | 2,302.615203 | 53116248 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 3,188,693 | 0.028968 | 53116248 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2724 | 2,471,594 | 94.065648 | 53116248 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | USDC/cbBTC | 520 | 2,464,404 | 0.000013 | 53116248 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,188,279 | 405.484749 | 53116248 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | WETH/FAI | 10000 | 2,107,816 | 1,210,234.968788 | 53116248 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,879,480 | 0.000013 | 53116248 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,874,074 | 0.000000 | 53116248 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,817,382 | 0.018468 | 53116248 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,705,133 | 0.000013 | 53116248 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | USDC/cbBTC | 344 | 1,689,912 | 0.000013 | 53116248 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | VIRTUAL/WETH | 10000 | 1,542,808 | 0.000265 | 53116248 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,494,861 | 0.005856 | 53116248 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,457,945 | 0.826460 | 53116248 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,453,220 | 1.698035 | 53116248 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | WETH/AERO | 3000 | 1,410,282 | 3,449.597123 | 53116248 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,358,460 | 14,000.834914 | 53116248 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/AERO | 10000 | 1,224,171 | 3,471.670851 | 53116248 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,223,610 | 0.000266 | 53116248 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | USDC/SEND | 3000 | 1,221,567 | 65.118993 | 53116248 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,205,781 | 2,306.569654 | 53116248 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | DRB/WETH | 10000 | 1,159,936 | 0.000000 | 53116248 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | WETH/WELL | 10000 | 1,128,688 | 1,092,272.815641 | 53116248 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/doginme | 10000 | 1,121,488 | 37,839,432.755685 | 53116248 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,097,952 | 499,567.247558 | 53116248 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,061,690 | 20,057,394.338751 | 53116248 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome | WETH/EDEL | 7000 | 1,061,138 | 72,178.446302 | 53116248 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | USDC/NOCK | 3000 | 1,055,325 | 56.240311 | 53116248 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,029,710 | 17.454284 | 53116248 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | USDC/VVV | 3000 | 963,090 | 0.040795 | 53116248 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/USDC | 10000 | 919,657 | 2,312.267761 | 53116248 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome | WETH/msETH (stable) | 500 | 900,381 | 2.308489 | 53116248 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | uXRP/WETH | 3000 | 885,553 | 0.000554 | 53116248 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 878,129 | 17.999757 | 53116248 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v3 | WETH/MORPHO | 3000 | 874,277 | 1,142.125047 | 53116248 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 872,279 | 17.113287 | 53116248 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| uniswap_v3 | WETH/VVV | 10000 | 859,569 | 94.282730 | 53116248 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v2 | WETH/USDC | 3000 | 841,699 | 2,302.985098 | 53116248 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| pancakeswap_v3 | QUID/USDC | 100 | 792,616 | 0.056297 | 53116248 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 791,361 | 0.000008 | 53116248 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | WETH/wstETH | 3000 | 779,736 | 0.803142 | 53116248 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 739,936 | 0.613346 | 53116248 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 725,857 | 4,752,019.898270 | 53116248 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 699,763 | 0.615992 | 53116248 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/NPC | 3000 | 699,704 | 136,348.951855 | 53116248 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | WETH/BRETT | 2099 | 685,914 | 497,209.375308 | 53116248 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 676,091 | 0.109404 | 53116248 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |

## Recherche d'opportunités
- Cycles : 10099 ; routes examinées : 197677826 ; candidats optimisés : 577743 ; net attendu > 0 : 245 ; dernier cycle 345.0 ms
- Rejets (moteur) : {'spread_below_threshold': 194436354, 'liquidity_below_min': 2449518, 'negative_expected_net': 577498, 'unquotable': 203058, 'borrow_bound_too_small': 10087, 'cycle_budget_exhausted': 1066}
- Enregistrements de la session : 577743 ; net attendu > 0 : 245 ; simulés (eth_call de la vraie tx) : 12 (ok 8, échec 4) ; étiquettes ghost N+1 : 0/9 positives
- Décisions : {'REJECTED': 577743} ; motifs de rejet : {'below_safety_margin': 228, 'negative_expected_net': 577498, 'p_lower_below_threshold': 228, 'price_impact': 1, 'reliability_not_demonstrated': 17, 'simulation_failed': 4, 'stale_data': 14}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53113838 | USDC→[pancakeswap_v3]→PLAY→[aerodrome_slipstream]→USDC | 57.394422 USDC | 0.073073 USDC | 0.000000 USDC | 0.005230 USDC | 0.067843 USDC (0.0624 €) | — | 11.82 | 0.000 (n=51) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 53113383 | USDC→[pancakeswap_v3]→PLAY→[aerodrome_slipstream]→USDC | 35.563030 USDC | 0.027254 USDC | 0.000000 USDC | 0.005232 USDC | 0.022022 USDC (0.0203 €) | 0.022022 USDC | 6.19 | 0.002 (n=134) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53113383 | USDC→[pancakeswap_v3]→PLAY→[aerodrome_slipstream]→USDC | 35.563030 USDC | 0.027254 USDC | 0.000000 USDC | 0.005232 USDC | 0.022022 USDC (0.0203 €) | 0.022022 USDC | 6.19 | 0.002 (n=134) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53114154 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 24.066900 USDC | 0.012841 USDC | 0.000000 USDC | 0.005232 USDC | 0.007609 USDC (0.0070 €) | — | 3.16 | 0.002 (n=135) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 53113418 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.184010 WETH | 0.000005 WETH | 0.000000 WETH | 0.000002 WETH | 0.000002 WETH (0.0054 €) | — | 0.14 | 0.022 (n=95) | REJECTED | below_safety_margin(2497999458590<36802053422786), p_lower_below_threshold(0.02<0.75) |
| 53113419 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.184010 WETH | 0.000005 WETH | 0.000000 WETH | 0.000002 WETH | 0.000002 WETH (0.0054 €) | — | 0.14 | 0.022 (n=95) | REJECTED | below_safety_margin(2497999458590<36802053422786), p_lower_below_threshold(0.02<0.75) |
| 53113418 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 430.913300 USDC | 0.011045 USDC | 0.000000 USDC | 0.005230 USDC | 0.005815 USDC (0.0053 €) | — | 0.13 | 0.022 (n=95) | REJECTED | below_safety_margin(5815<86182), p_lower_below_threshold(0.02<0.75) |
| 53113419 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 430.913300 USDC | 0.011045 USDC | 0.000000 USDC | 0.005230 USDC | 0.005815 USDC (0.0053 €) | — | 0.13 | 0.022 (n=95) | REJECTED | below_safety_margin(5815<86182), p_lower_below_threshold(0.02<0.75) |
| 53116184 | cbBTC→[uniswap_v3]→WBTC→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.000479 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0051 €) | — | 1.46 | 0.133 (n=344) | REJECTED | below_safety_margin(7<9), p_lower_below_threshold(0.13<0.75) |
| 53116179 | WETH→[uniswap_v3]→NOCK→[aerodrome]→USDC→[uniswap_v3]→WETH | 0.010103 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0050 €) | 0.000002 WETH | 2.35 | 0.122 (n=104) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 53116179 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→NOCK→[aerodrome]→USDC | 22.966195 USDC | 0.012129 USDC | 0.000000 USDC | 0.006690 USDC | 0.005439 USDC (0.0050 €) | — | 2.37 | 0.122 (n=104) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 53116184 | USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WBTC→[uniswap_v3]→USDC | 38.609722 USDC | 0.012085 USDC | 0.000000 USDC | 0.007070 USDC | 0.005015 USDC (0.0046 €) | — | 1.30 | 0.133 (n=344) | REJECTED | below_safety_margin(5015<7721), p_lower_below_threshold(0.13<0.75) |
| 53116179 | WETH→[uniswap_v3]→NOCK→[aerodrome]→USDC→[pancakeswap_v3]→WETH | 0.009907 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0046 €) | 0.000002 WETH | 2.18 | 0.189 (n=41) | REJECTED | p_lower_below_threshold(0.19<0.75) |
| 53116179 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→NOCK→[aerodrome]→USDC | 22.702595 USDC | 0.011632 USDC | 0.000000 USDC | 0.006690 USDC | 0.004942 USDC (0.0045 €) | — | 2.18 | 0.189 (n=41) | REJECTED | p_lower_below_threshold(0.19<0.75) |
| 53107366 | USDC→[sushiswap_v3]→WETH→[pancakeswap_v3]→USDC | 63.193801 USDC | 0.009983 USDC | 0.000000 USDC | 0.005224 USDC | 0.004759 USDC (0.0044 €) | — | 0.75 | 0.022 (n=95) | REJECTED | below_safety_margin(4759<12638), p_lower_below_threshold(0.02<0.75) |
| 53107366 | WETH→[pancakeswap_v3]→USDC→[sushiswap_v3]→WETH | 0.027089 WETH | 0.000004 WETH | 0.000000 WETH | 0.000002 WETH | 0.000002 WETH (0.0044 €) | — | 0.75 | 0.022 (n=95) | REJECTED | below_safety_margin(2036524520673<5417835819103), p_lower_below_threshold(0.02<0.75) |
| 53113890 | WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.016247 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0043 €) | — | 1.22 | 0.133 (n=344) | REJECTED | below_safety_margin(1986842600651<3249449387170), p_lower_below_threshold(0.13<0.75) |
| 53113890 | WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.016247 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0043 €) | — | 1.22 | 0.133 (n=344) | REJECTED | below_safety_margin(1986842600651<3249449387170), p_lower_below_threshold(0.13<0.75) |
| 53113890 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC | 37.532616 USDC | 0.011977 USDC | 0.000000 USDC | 0.007355 USDC | 0.004622 USDC (0.0043 €) | — | 1.23 | 0.133 (n=344) | REJECTED | below_safety_margin(4622<7506), p_lower_below_threshold(0.13<0.75) |
| 53113890 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC | 37.532616 USDC | 0.011977 USDC | 0.000000 USDC | 0.007355 USDC | 0.004622 USDC (0.0043 €) | — | 1.23 | 0.133 (n=344) | REJECTED | below_safety_margin(4622<7506), p_lower_below_threshold(0.13<0.75) |
| 53116179 | WETH→[aerodrome_slipstream]→LCAP→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.023467 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0040 €) | — | 0.80 | 0.182 (n=178) | REJECTED | below_safety_margin(1873846782189<4693422209124), p_lower_below_threshold(0.18<0.75) |
| 53116179 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→LCAP→[aerodrome_slipstream]→USDC | 53.530972 USDC | 0.011653 USDC | 0.000000 USDC | 0.007361 USDC | 0.004292 USDC (0.0039 €) | — | 0.80 | 0.182 (n=178) | REJECTED | below_safety_margin(4292<10706), p_lower_below_threshold(0.18<0.75) |
| 53116179 | WETH→[aerodrome_slipstream]→LCAP→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.024309 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0039 €) | — | 0.76 | 0.133 (n=344) | REJECTED | below_safety_margin(1843081014552<4861829199513), p_lower_below_threshold(0.13<0.75) |
| 53116179 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→LCAP→[aerodrome_slipstream]→USDC | 55.597179 USDC | 0.011231 USDC | 0.000000 USDC | 0.007010 USDC | 0.004221 USDC (0.0039 €) | — | 0.76 | 0.133 (n=344) | REJECTED | below_safety_margin(4221<11119), p_lower_below_threshold(0.13<0.75) |
| 53116179 | cbBTC→[aerodrome_slipstream]→tBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.000467 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0037 €) | — | 1.07 | 0.133 (n=344) | REJECTED | below_safety_margin(5<9), p_lower_below_threshold(0.13<0.75) |

## Fiabilité et décision
- Observations ghost : 2616 ; taux observé 0.094 ; borne inférieure crédible (0.9) 0.087 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 8.7% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
