# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-31T14:03:37+00:00 ; durée 110.8 min ; blocs 53329707 → 53333032 (3265 vus)

## Connexion
- Requêtes RPC : 38639 ; erreurs : 25 ; latence p50/p95 : 240.0/1,186.2 ms
- Rafraîchissements d'état : 3265 ; âge des données au dernier bloc : 4.22 s ; changements de frais LP observés (pools à frais dynamiques) : 3305
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 28448 ; cycles déclenchés par événement : 3335 ; avance médiane sur le rafraîchissement multicall : 456 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,246.02 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 500 pools, 290 jetons, 18658 routes
- Par DEX : uniswap_v3 137, aerodrome_slipstream 113, aerodrome 207, pancakeswap_v3 29, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 178 (rejetés 2) → 583 jetons ; pools candidats 3735 (énumérés 318, par paires 0), mesurés 503, sous le plancher de 10000.0 $ : 3 → gardés 500 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2242.796031, 'cbBTC': 77486.299825, 'AERO': 0.625959}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 150,622,636 | 2,246.021119 | 53333033 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,027,170 | 0.029053 | 53333033 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,283,573 | 0.000013 | 53333033 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,030,608 | 0.029054 | 53333033 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 7,854,915 | 2,248.303784 | 53333033 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,746,072 | 99.704381 | 53333033 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,674,978 | 0.001614 | 53333033 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 5,872,898 | 1.583527 | 53333033 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,289,292 | 0.029057 | 53333033 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/USDC | 150 | 4,113,331 | 2,248.830312 | 53333033 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,082,617 | 2,248.955682 | 53333033 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,064,969 | 1.000001 | 53333033 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,532,134 | 37,842.552964 | 53333033 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,683,080 | 0.029043 | 53333033 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2721 | 2,353,204 | 99.738999 | 53333033 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | WETH/FAI | 10000 | 2,064,358 | 1,200,126.211824 | 53333033 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 424 | 1,970,064 | 0.000013 | 53333033 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,754,611 | 0.000000 | 53333033 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,731,665 | 0.017631 | 53333033 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,683,057 | 422.777679 | 53333033 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,638,270 | 0.000013 | 53333033 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v2 | WETH/USDC | 3000 | 1,592,773 | 2,254.156626 | 53333033 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,583,894 | 0.000013 | 53333033 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,542,969 | 1.498817 | 53333033 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome | WETH/USDC | 3000 | 1,471,826 | 2,254.552605 | 53333033 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,457,690 | 0.825481 | 53333033 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,413,294 | 3,561.803500 | 53333033 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,352,334 | 2,248.521242 | 53333033 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,345,140 | 0.005286 | 53333033 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/cbBTC | 336 | 1,313,333 | 0.000013 | 53333033 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,303,039 | 14,544.882696 | 53333033 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | USDC/SEND | 3000 | 1,174,511 | 70.441448 | 53333033 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,114,315 | 35,805,160.659331 | 53333033 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,057,273 | 518,688.615453 | 53333033 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,027,723 | 0.000000 | 53333033 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,023,287 | 21,605,572.925706 | 53333033 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome | WETH/EDEL | 7000 | 1,015,561 | 74,701.082453 | 53333033 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome_slipstream | USDC/VELVET | 100 | 989,206 | 19.551653 | 53333033 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/VVV | 10000 | 976,701 | 99.433918 | 53333033 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | USDC/VVV | 3000 | 960,410 | 0.044354 | 53333033 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | USDC/NOCK | 3000 | 959,415 | 68.010694 | 53333033 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome | WETH/WELL | 10000 | 932,803 | 1,212,150.254289 | 53333033 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/MORPHO | 3000 | 922,511 | 1,018.743335 | 53333033 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/USDC | 10000 | 921,116 | 2,235.963257 | 53333033 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome | WETH/AERO | 10000 | 868,714 | 3,537.395732 | 53333033 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | uXRP/WETH | 3000 | 862,101 | 0.000552 | 53333033 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 845,157 | 19.185360 | 53333033 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 827,605 | 0.061666 | 53333033 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 760,606 | 0.802842 | 53333033 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| aerodrome | VIRTUAL/WETH | 10000 | 726,594 | 0.000258 | 53333033 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 724,826 | 4,536,615.535034 | 53333033 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 712,978 | 0.582131 | 53333033 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 686,872 | 0.000008 | 53333033 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v2 | WETH/NPC | 3000 | 671,084 | 141,265.079805 | 53333033 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome | WETH/msETH (stable) | 500 | 661,033 | 2.334833 | 53333033 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 655,718 | 521,740.894848 | 53333033 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | TIG/USDC | 10000 | 628,169 | 0.499036 | 53333033 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 615,309 | 0.093721 | 53333033 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| aerodrome | WETH/bsdETH | 100 | 603,375 | 0.916727 | 53333033 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome_slipstream | WETH/MORPHO | 2706 | 555,491 | 1,018.619872 | 53333033 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |

## Recherche d'opportunités
- Cycles : 6599 ; routes examinées : 123124142 ; candidats optimisés : 345251 ; net attendu > 0 : 230 ; dernier cycle 57.5 ms
- Rejets (moteur) : {'spread_below_threshold': 121717516, 'liquidity_below_min': 1040661, 'negative_expected_net': 345021, 'unquotable': 13164, 'borrow_bound_too_small': 6589, 'cycle_budget_exhausted': 961}
- Enregistrements de la session : 345251 ; net attendu > 0 : 230 ; simulés (eth_call de la vraie tx) : 8 (ok 5, échec 3) ; étiquettes ghost N+1 : 1/4 positives
- Décisions : {'REJECTED': 345251} ; motifs de rejet : {'below_safety_margin': 222, 'negative_expected_net': 345021, 'p_lower_below_threshold': 224, 'reliability_not_demonstrated': 6, 'simulation_failed': 3}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53332585 | USDC→[pancakeswap_v3]→ICNT→[uniswap_v3]→USDC | 48.587111 USDC | 0.035885 USDC | 0.000000 USDC | 0.005052 USDC | 0.030833 USDC (0.0284 €) | — | 6.35 | 0.019 (n=182) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.02<0.75) |
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
| 53332513 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 23.677312 USDC | 0.012953 USDC | 0.000000 USDC | 0.005053 USDC | 0.007900 USDC (0.0073 €) | 0.007900 USDC | 3.34 | 0.020 (n=181) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 53332513 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 23.677312 USDC | 0.012953 USDC | 0.000000 USDC | 0.005053 USDC | 0.007900 USDC (0.0073 €) | 0.007900 USDC | 3.34 | 0.020 (n=181) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 53330420 | USDC→[aerodrome_slipstream]→EURC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 77.074542 USDC | 0.014449 USDC | 0.000000 USDC | 0.006747 USDC | 0.007702 USDC (0.0071 €) | — | 1.00 | 0.144 (n=649) | REJECTED | below_safety_margin(7702<15414), p_lower_below_threshold(0.14<0.75) |
| 53330420 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→EURC→[pancakeswap_v3]→WETH | 0.034384 WETH | 0.000006 WETH | 0.000000 WETH | 0.000003 WETH | 0.000003 WETH (0.0071 €) | — | 0.99 | 0.144 (n=649) | REJECTED | below_safety_margin(3414487672077<6876703763002), p_lower_below_threshold(0.14<0.75) |
| 53330420 | USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 88.715814 USDC | 0.012685 USDC | 0.000000 USDC | 0.006747 USDC | 0.005938 USDC (0.0055 €) | — | 0.67 | 0.144 (n=649) | REJECTED | below_safety_margin(5938<17743), p_lower_below_threshold(0.14<0.75) |
| 53330420 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH | 0.039511 WETH | 0.000006 WETH | 0.000000 WETH | 0.000003 WETH | 0.000003 WETH (0.0054 €) | — | 0.67 | 0.144 (n=649) | REJECTED | below_safety_margin(2630117628282<7902261269992), p_lower_below_threshold(0.14<0.75) |
| 53330420 | USDC→[aerodrome_slipstream]→EURC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 67.569346 USDC | 0.012173 USDC | 0.000000 USDC | 0.006747 USDC | 0.005426 USDC (0.0050 €) | — | 0.80 | 0.144 (n=649) | REJECTED | below_safety_margin(5426<13513), p_lower_below_threshold(0.14<0.75) |
| 53330420 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→EURC→[pancakeswap_v3]→WETH | 0.030341 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0050 €) | — | 0.79 | 0.144 (n=649) | REJECTED | below_safety_margin(2403251936887<6068294482378), p_lower_below_threshold(0.14<0.75) |
| 53332545 | USDC→[pancakeswap_v3]→PLAY→[aerodrome]→USDC | 9.754361 USDC | 0.009656 USDC | 0.000000 USDC | 0.004742 USDC | 0.004914 USDC (0.0045 €) | 0.004914 USDC | 5.04 | 0.052 (n=28) | REJECTED | reliability_not_demonstrated |
| 53332545 | USDC→[pancakeswap_v3]→PLAY→[aerodrome]→USDC | 9.754361 USDC | 0.009656 USDC | 0.000000 USDC | 0.004742 USDC | 0.004914 USDC (0.0045 €) | 0.004914 USDC | 5.04 | 0.052 (n=28) | REJECTED | reliability_not_demonstrated |
| 53332338 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 160.416740 USDC | 0.010689 USDC | 0.000000 USDC | 0.006763 USDC | 0.003926 USDC (0.0036 €) | — | 0.24 | 0.144 (n=649) | REJECTED | below_safety_margin(3926<32083), p_lower_below_threshold(0.14<0.75) |
| 53332338 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.001675 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0036 €) | — | 0.30 | 0.144 (n=649) | REJECTED | below_safety_margin(5<33), p_lower_below_threshold(0.14<0.75) |
| 53331459 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 19.056863 USDC | 0.008539 USDC | 0.000000 USDC | 0.005055 USDC | 0.003484 USDC (0.0032 €) | — | 1.83 | 0.039 (n=152) | REJECTED | below_safety_margin(3484<3811), p_lower_below_threshold(0.04<0.75) |

## Fiabilité et décision
- Observations ghost : 3949 ; taux observé 0.129 ; borne inférieure crédible (0.9) 0.123 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 12.3% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
