# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-31T13:35:46+00:00 ; durée 82.94 min ; blocs 53329707 → 53332197 (2484 vus)

## Connexion
- Requêtes RPC : 29423 ; erreurs : 0 ; latence p50/p95 : 206.2/1,011.7 ms
- Rafraîchissements d'état : 2484 ; âge des données au dernier bloc : 5.45 s ; changements de frais LP observés (pools à frais dynamiques) : 2709
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 21412 ; cycles déclenchés par événement : 2539 ; avance médiane sur le rafraîchissement multicall : 435 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,246.02 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 500 pools, 290 jetons, 18658 routes
- Par DEX : uniswap_v3 137, aerodrome_slipstream 113, aerodrome 207, pancakeswap_v3 29, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 178 (rejetés 2) → 583 jetons ; pools candidats 3735 (énumérés 318, par paires 0), mesurés 503, sous le plancher de 10000.0 $ : 3 → gardés 500 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2242.796031, 'cbBTC': 77486.299825, 'AERO': 0.625959}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 150,646,986 | 2,246.021536 | 53332197 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,029,198 | 0.029039 | 53332197 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,287,025 | 0.000013 | 53332197 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,032,341 | 0.029054 | 53332197 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 7,950,930 | 2,245.914837 | 53332197 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,745,688 | 99.714636 | 53332197 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,683,791 | 0.001617 | 53332197 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 5,876,523 | 1.582416 | 53332197 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,299,194 | 0.029050 | 53332197 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/USDC | 150 | 4,113,432 | 2,246.298372 | 53332197 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,066,994 | 1.000001 | 53332197 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,061,614 | 2,246.479733 | 53332197 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | WETH/KTA | 3000 | 3,532,133 | 37,842.595855 | 53332197 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,683,387 | 0.029043 | 53332197 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2808 | 2,353,015 | 99.736107 | 53332197 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | WETH/FAI | 10000 | 2,064,358 | 1,200,126.211824 | 53332197 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 400 | 1,975,653 | 0.000013 | 53332197 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,754,619 | 0.000000 | 53332197 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,723,809 | 0.017502 | 53332197 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,683,142 | 422.654505 | 53332197 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,641,335 | 0.000013 | 53332197 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v2 | WETH/USDC | 3000 | 1,592,768 | 2,249.361088 | 53332197 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,584,455 | 0.000013 | 53332197 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,542,969 | 1.498817 | 53332197 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome | WETH/USDC | 3000 | 1,471,825 | 2,252.451953 | 53332197 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,456,813 | 0.826387 | 53332197 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,413,843 | 3,554.564956 | 53332197 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,355,598 | 2,245.908249 | 53332197 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,345,140 | 0.005286 | 53332197 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/cbBTC | 332 | 1,313,810 | 0.000013 | 53332197 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,303,497 | 14,563.296139 | 53332197 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | USDC/SEND | 3000 | 1,174,511 | 70.441448 | 53332197 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,116,157 | 35,641,633.243540 | 53332197 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,057,276 | 518,686.203692 | 53332197 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,026,958 | 0.000000 | 53332197 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,020,800 | 21,692,159.024843 | 53332197 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome | WETH/EDEL | 7000 | 1,015,668 | 74,685.417243 | 53332197 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome_slipstream | USDC/VELVET | 100 | 989,050 | 19.560630 | 53332197 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/VVV | 10000 | 968,499 | 99.433912 | 53332197 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome | USDC/NOCK | 3000 | 961,248 | 67.751426 | 53332197 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | USDC/VVV | 3000 | 960,309 | 0.044387 | 53332197 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | WETH/WELL | 10000 | 932,902 | 1,211,895.789509 | 53332197 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/MORPHO | 3000 | 920,948 | 1,022.966849 | 53332197 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/USDC | 10000 | 920,718 | 2,235.963257 | 53332197 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome | WETH/AERO | 10000 | 869,018 | 3,537.395732 | 53332197 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | uXRP/WETH | 3000 | 862,102 | 0.000552 | 53332197 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 845,157 | 19.185360 | 53332197 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 827,522 | 0.061653 | 53332197 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 760,606 | 0.802842 | 53332197 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| aerodrome | VIRTUAL/WETH | 10000 | 726,594 | 0.000258 | 53332197 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 724,747 | 4,537,594.315788 | 53332197 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 712,320 | 0.580109 | 53332197 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 687,285 | 0.000008 | 53332197 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v2 | WETH/NPC | 3000 | 669,425 | 141,964.912393 | 53332197 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome | WETH/msETH (stable) | 500 | 661,045 | 2.334833 | 53332197 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | WETH/BRETT | 2153 | 655,721 | 521,674.366303 | 53332197 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | TIG/USDC | 10000 | 628,169 | 0.499036 | 53332197 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 615,061 | 0.093663 | 53332197 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| aerodrome | WETH/bsdETH | 100 | 603,375 | 0.916727 | 53332197 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome_slipstream | WETH/MORPHO | 2733 | 554,928 | 1,022.521864 | 53332197 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |

## Recherche d'opportunités
- Cycles : 5022 ; routes examinées : 93700476 ; candidats optimisés : 266667 ; net attendu > 0 : 219 ; dernier cycle 57.0 ms
- Rejets (moteur) : {'spread_below_threshold': 92633677, 'liquidity_below_min': 784603, 'negative_expected_net': 266448, 'unquotable': 10026, 'borrow_bound_too_small': 5017, 'cycle_budget_exhausted': 486}
- Enregistrements de la session : 266667 ; net attendu > 0 : 219 ; simulés (eth_call de la vraie tx) : 3 (ok 1, échec 2) ; étiquettes ghost N+1 : 1/1 positives
- Décisions : {'REJECTED': 266667} ; motifs de rejet : {'below_safety_margin': 216, 'negative_expected_net': 266448, 'p_lower_below_threshold': 215, 'reliability_not_demonstrated': 4, 'simulation_failed': 2}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53330420 | USDC→[aerodrome_slipstream]→EURC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 96.114789 USDC | 0.022344 USDC | 0.000000 USDC | 0.006747 USDC | 0.015597 USDC (0.0143 €) | — | 1.62 | 0.144 (n=649) | REJECTED | below_safety_margin(15597<19222), p_lower_below_threshold(0.14<0.75) |
| 53330420 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→EURC→[pancakeswap_v3]→WETH | 0.042866 WETH | 0.000010 WETH | 0.000000 WETH | 0.000003 WETH | 0.000007 WETH (0.0143 €) | — | 1.61 | 0.144 (n=649) | REJECTED | below_safety_margin(6920372804848<8573129929888), p_lower_below_threshold(0.14<0.75) |
| 53330420 | USDC→[aerodrome_slipstream]→EURC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 85.064882 USDC | 0.019170 USDC | 0.000000 USDC | 0.006747 USDC | 0.012423 USDC (0.0114 €) | — | 1.46 | 0.144 (n=649) | REJECTED | below_safety_margin(12423<17012), p_lower_below_threshold(0.14<0.75) |
| 53330420 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→EURC→[pancakeswap_v3]→WETH | 0.037894 WETH | 0.000009 WETH | 0.000000 WETH | 0.000003 WETH | 0.000006 WETH (0.0114 €) | — | 1.45 | 0.144 (n=649) | REJECTED | below_safety_margin(5511295611875<7578819259550), p_lower_below_threshold(0.14<0.75) |
| 53331459 | USDC→[aerodrome]→PLAY→[pancakeswap_v3]→USDC | 12.916938 USDC | 0.016923 USDC | 0.000000 USDC | 0.004745 USDC | 0.012178 USDC (0.0112 €) | — | 9.43 | 0.023 (n=13) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53331459 | USDC→[aerodrome]→PLAY→[pancakeswap_v3]→USDC | 12.916938 USDC | 0.016923 USDC | 0.000000 USDC | 0.004745 USDC | 0.012178 USDC (0.0112 €) | — | 9.43 | 0.023 (n=13) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53331460 | USDC→[aerodrome]→PLAY→[pancakeswap_v3]→USDC | 12.916938 USDC | 0.016923 USDC | 0.000000 USDC | 0.004745 USDC | 0.012178 USDC (0.0112 €) | 0.012178 USDC | 9.43 | 0.059 (n=14) | REJECTED | reliability_not_demonstrated |
| 53330420 | USDC→[aerodrome_slipstream]→EURC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 78.732838 USDC | 0.018346 USDC | 0.000000 USDC | 0.006747 USDC | 0.011599 USDC (0.0107 €) | — | 1.47 | 0.144 (n=649) | REJECTED | below_safety_margin(11599<15746), p_lower_below_threshold(0.14<0.75) |
| 53330420 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→EURC→[pancakeswap_v3]→WETH | 0.035084 WETH | 0.000008 WETH | 0.000000 WETH | 0.000003 WETH | 0.000005 WETH (0.0106 €) | — | 1.47 | 0.144 (n=649) | REJECTED | below_safety_margin(5145676401010<7016707605742), p_lower_below_threshold(0.14<0.75) |
| 53330420 | USDC→[aerodrome_slipstream]→EURC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 71.111596 USDC | 0.015950 USDC | 0.000000 USDC | 0.006747 USDC | 0.009203 USDC (0.0085 €) | — | 1.29 | 0.144 (n=649) | REJECTED | below_safety_margin(9203<14222), p_lower_below_threshold(0.14<0.75) |
| 53330420 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→EURC→[pancakeswap_v3]→WETH | 0.031721 WETH | 0.000007 WETH | 0.000000 WETH | 0.000003 WETH | 0.000004 WETH (0.0084 €) | — | 1.29 | 0.144 (n=649) | REJECTED | below_safety_margin(4081185674771<6344275233055), p_lower_below_threshold(0.14<0.75) |
| 53330420 | USDC→[aerodrome_slipstream]→EURC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 77.074542 USDC | 0.014449 USDC | 0.000000 USDC | 0.006747 USDC | 0.007702 USDC (0.0071 €) | — | 1.00 | 0.144 (n=649) | REJECTED | below_safety_margin(7702<15414), p_lower_below_threshold(0.14<0.75) |
| 53330420 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→EURC→[pancakeswap_v3]→WETH | 0.034384 WETH | 0.000006 WETH | 0.000000 WETH | 0.000003 WETH | 0.000003 WETH (0.0071 €) | — | 0.99 | 0.144 (n=649) | REJECTED | below_safety_margin(3414487672077<6876703763002), p_lower_below_threshold(0.14<0.75) |
| 53330420 | USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 88.715814 USDC | 0.012685 USDC | 0.000000 USDC | 0.006747 USDC | 0.005938 USDC (0.0055 €) | — | 0.67 | 0.144 (n=649) | REJECTED | below_safety_margin(5938<17743), p_lower_below_threshold(0.14<0.75) |
| 53330420 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH | 0.039511 WETH | 0.000006 WETH | 0.000000 WETH | 0.000003 WETH | 0.000003 WETH (0.0054 €) | — | 0.67 | 0.144 (n=649) | REJECTED | below_safety_margin(2630117628282<7902261269992), p_lower_below_threshold(0.14<0.75) |
| 53330420 | USDC→[aerodrome_slipstream]→EURC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 67.569346 USDC | 0.012173 USDC | 0.000000 USDC | 0.006747 USDC | 0.005426 USDC (0.0050 €) | — | 0.80 | 0.144 (n=649) | REJECTED | below_safety_margin(5426<13513), p_lower_below_threshold(0.14<0.75) |
| 53330420 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→EURC→[pancakeswap_v3]→WETH | 0.030341 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0050 €) | — | 0.79 | 0.144 (n=649) | REJECTED | below_safety_margin(2403251936887<6068294482378), p_lower_below_threshold(0.14<0.75) |
| 53331459 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 19.056863 USDC | 0.008539 USDC | 0.000000 USDC | 0.005055 USDC | 0.003484 USDC (0.0032 €) | — | 1.83 | 0.039 (n=152) | REJECTED | below_safety_margin(3484<3811), p_lower_below_threshold(0.04<0.75) |
| 53331459 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 19.056863 USDC | 0.008539 USDC | 0.000000 USDC | 0.005055 USDC | 0.003484 USDC (0.0032 €) | — | 1.83 | 0.039 (n=152) | REJECTED | below_safety_margin(3484<3811), p_lower_below_threshold(0.04<0.75) |
| 53331460 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 19.056863 USDC | 0.008539 USDC | 0.000000 USDC | 0.005055 USDC | 0.003484 USDC (0.0032 €) | — | 1.83 | 0.039 (n=152) | REJECTED | below_safety_margin(3484<3811), p_lower_below_threshold(0.04<0.75) |
| 53330420 | USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 66.525761 USDC | 0.009534 USDC | 0.000000 USDC | 0.006747 USDC | 0.002787 USDC (0.0026 €) | — | 0.42 | 0.189 (n=283) | REJECTED | below_safety_margin(2787<13305), p_lower_below_threshold(0.19<0.75) |
| 53330420 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH | 0.029816 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0025 €) | — | 0.41 | 0.189 (n=283) | REJECTED | below_safety_margin(1231115487267<5963247133341), p_lower_below_threshold(0.19<0.75) |
| 53331936 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 17.954644 USDC | 0.007560 USDC | 0.000000 USDC | 0.005053 USDC | 0.002507 USDC (0.0023 €) | — | 1.40 | 0.039 (n=152) | REJECTED | below_safety_margin(2507<3590), p_lower_below_threshold(0.04<0.75) |
| 53331936 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 17.954644 USDC | 0.007560 USDC | 0.000000 USDC | 0.005053 USDC | 0.002507 USDC (0.0023 €) | — | 1.40 | 0.039 (n=152) | REJECTED | below_safety_margin(2507<3590), p_lower_below_threshold(0.04<0.75) |
| 53330420 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 35.611467 USDC | 0.006812 USDC | 0.000000 USDC | 0.005042 USDC | 0.001770 USDC (0.0016 €) | — | 0.50 | 0.039 (n=152) | REJECTED | below_safety_margin(1770<7122), p_lower_below_threshold(0.04<0.75) |

## Fiabilité et décision
- Observations ghost : 3946 ; taux observé 0.129 ; borne inférieure crédible (0.9) 0.123 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 12.3% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
