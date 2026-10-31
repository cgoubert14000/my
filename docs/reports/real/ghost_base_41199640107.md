# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-31T12:43:22+00:00 ; durée 30.54 min ; blocs 53329707 → 53330626 (915 vus)

## Connexion
- Requêtes RPC : 10751 ; erreurs : 0 ; latence p50/p95 : 220.2/1,103.8 ms
- Rafraîchissements d'état : 915 ; âge des données au dernier bloc : 2.31 s ; changements de frais LP observés (pools à frais dynamiques) : 1142
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 8532 ; cycles déclenchés par événement : 900 ; avance médiane sur le rafraîchissement multicall : 530 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,246.02 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 500 pools, 290 jetons, 18658 routes
- Par DEX : uniswap_v3 137, aerodrome_slipstream 113, aerodrome 207, pancakeswap_v3 29, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 178 (rejetés 2) → 583 jetons ; pools candidats 3735 (énumérés 318, par paires 0), mesurés 503, sous le plancher de 10000.0 $ : 3 → gardés 500 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2242.796031, 'cbBTC': 77486.299825, 'AERO': 0.625959}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 150,420,876 | 2,246.019825 | 53330626 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,028,004 | 0.029036 | 53330626 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,289,261 | 0.000013 | 53330626 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,032,886 | 0.029054 | 53330626 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 7,869,747 | 2,250.524128 | 53330626 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,783,422 | 98.749931 | 53330626 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,689,066 | 0.001618 | 53330626 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 5,907,345 | 1.565946 | 53330626 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,299,285 | 0.029048 | 53330626 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/USDC | 150 | 4,114,321 | 2,251.085143 | 53330626 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,094,133 | 2,251.165432 | 53330626 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,067,448 | 1.000001 | 53330626 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,534,770 | 37,786.100701 | 53330626 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,684,590 | 0.029040 | 53330626 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2838 | 2,365,119 | 98.660398 | 53330626 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | WETH/FAI | 10000 | 2,061,203 | 1,203,801.785954 | 53330626 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 424 | 1,977,040 | 0.000013 | 53330626 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,755,488 | 0.000000 | 53330626 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,728,792 | 0.017585 | 53330626 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,684,352 | 421.823808 | 53330626 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,641,471 | 0.000013 | 53330626 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v2 | WETH/USDC | 3000 | 1,592,766 | 2,248.708557 | 53330626 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,584,552 | 0.000013 | 53330626 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,542,998 | 1.498770 | 53330626 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome | WETH/USDC | 3000 | 1,524,726 | 2,252.618350 | 53330626 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,456,812 | 0.826388 | 53330626 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,427,893 | 3,527.496257 | 53330626 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | USDC/cbBTC | 334 | 1,414,444 | 0.000013 | 53330626 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,355,604 | 2,251.620831 | 53330626 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,352,315 | 0.005320 | 53330626 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,304,711 | 14,556.225879 | 53330626 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | USDC/SEND | 3000 | 1,174,512 | 70.441448 | 53330626 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,114,691 | 35,766,913.327811 | 53330626 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,060,021 | 514,970.993525 | 53330626 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,030,458 | 21,341,044.339289 | 53330626 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | DRB/WETH | 10000 | 1,026,868 | 0.000000 | 53330626 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | WETH/EDEL | 7000 | 1,015,191 | 74,755.434002 | 53330626 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome_slipstream | USDC/VELVET | 100 | 993,355 | 19.315590 | 53330626 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/VVV | 10000 | 973,592 | 99.433409 | 53330626 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | USDC/VVV | 3000 | 966,831 | 0.043827 | 53330626 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | USDC/NOCK | 3000 | 957,415 | 68.295026 | 53330626 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome | WETH/WELL | 10000 | 932,354 | 1,213,318.600796 | 53330626 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/USDC | 10000 | 920,718 | 2,235.963257 | 53330626 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 918,580 | 1,027.931274 | 53330626 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome | WETH/AERO | 10000 | 873,577 | 3,537.395732 | 53330626 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | uXRP/WETH | 3000 | 862,101 | 0.000552 | 53330626 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 848,211 | 19.078075 | 53330626 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 828,069 | 0.061741 | 53330626 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 760,605 | 0.802842 | 53330626 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| aerodrome | VIRTUAL/WETH | 10000 | 725,889 | 0.000257 | 53330626 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 724,455 | 4,541,231.784388 | 53330626 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 711,220 | 0.581031 | 53330626 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| aerodrome_slipstream | AERO/cbBTC | 2700 | 691,351 | 0.000008 | 53330626 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v2 | WETH/NPC | 3000 | 668,221 | 142,476.187763 | 53330626 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome | WETH/msETH (stable) | 500 | 661,061 | 2.334749 | 53330626 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | WETH/BRETT | 2096 | 658,181 | 517,009.049095 | 53330626 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | TIG/USDC | 10000 | 628,169 | 0.499036 | 53330626 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 616,388 | 0.093975 | 53330626 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| aerodrome | WETH/bsdETH | 100 | 603,406 | 0.916631 | 53330626 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome_slipstream | WETH/MORPHO | 2703 | 554,016 | 1,028.150886 | 53330626 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |

## Recherche d'opportunités
- Cycles : 1814 ; routes examinées : 33845612 ; candidats optimisés : 121592 ; net attendu > 0 : 210 ; dernier cycle 334.2 ms
- Rejets (moteur) : {'spread_below_threshold': 33430837, 'liquidity_below_min': 287679, 'negative_expected_net': 121382, 'unquotable': 3626, 'borrow_bound_too_small': 1814}
- Enregistrements de la session : 121589 ; net attendu > 0 : 210 ; simulés (eth_call de la vraie tx) : 0 (ok 0, échec 0) ; étiquettes ghost N+1 : 0/0 positives
- Décisions : {'REJECTED': 121589} ; motifs de rejet : {'below_safety_margin': 210, 'negative_expected_net': 121379, 'p_lower_below_threshold': 210}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53330420 | USDC→[aerodrome_slipstream]→EURC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 96.114789 USDC | 0.022344 USDC | 0.000000 USDC | 0.006747 USDC | 0.015597 USDC (0.0143 €) | — | 1.62 | 0.144 (n=649) | REJECTED | below_safety_margin(15597<19222), p_lower_below_threshold(0.14<0.75) |
| 53330420 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→EURC→[pancakeswap_v3]→WETH | 0.042866 WETH | 0.000010 WETH | 0.000000 WETH | 0.000003 WETH | 0.000007 WETH (0.0143 €) | — | 1.61 | 0.144 (n=649) | REJECTED | below_safety_margin(6920372804848<8573129929888), p_lower_below_threshold(0.14<0.75) |
| 53330420 | USDC→[aerodrome_slipstream]→EURC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 85.064882 USDC | 0.019170 USDC | 0.000000 USDC | 0.006747 USDC | 0.012423 USDC (0.0114 €) | — | 1.46 | 0.144 (n=649) | REJECTED | below_safety_margin(12423<17012), p_lower_below_threshold(0.14<0.75) |
| 53330420 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→EURC→[pancakeswap_v3]→WETH | 0.037894 WETH | 0.000009 WETH | 0.000000 WETH | 0.000003 WETH | 0.000006 WETH (0.0114 €) | — | 1.45 | 0.144 (n=649) | REJECTED | below_safety_margin(5511295611875<7578819259550), p_lower_below_threshold(0.14<0.75) |
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
| 53330420 | USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 66.525761 USDC | 0.009534 USDC | 0.000000 USDC | 0.006747 USDC | 0.002787 USDC (0.0026 €) | — | 0.42 | 0.189 (n=283) | REJECTED | below_safety_margin(2787<13305), p_lower_below_threshold(0.19<0.75) |
| 53330420 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH | 0.029816 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0025 €) | — | 0.41 | 0.189 (n=283) | REJECTED | below_safety_margin(1231115487267<5963247133341), p_lower_below_threshold(0.19<0.75) |
| 53330420 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 35.611467 USDC | 0.006812 USDC | 0.000000 USDC | 0.005042 USDC | 0.001770 USDC (0.0016 €) | — | 0.50 | 0.039 (n=152) | REJECTED | below_safety_margin(1770<7122), p_lower_below_threshold(0.04<0.75) |
| 53330420 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.015971 WETH | 0.000003 WETH | 0.000000 WETH | 0.000002 WETH | 0.000001 WETH (0.0016 €) | — | 0.49 | 0.039 (n=152) | REJECTED | below_safety_margin(780611979415<3194297808516), p_lower_below_threshold(0.04<0.75) |
| 53330418 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 9.820239 USDC | 0.008054 USDC | 0.000000 USDC | 0.006740 USDC | 0.001314 USDC (0.0012 €) | — | 1.34 | 0.144 (n=649) | REJECTED | below_safety_margin(1314<1964), p_lower_below_threshold(0.14<0.75) |
| 53330419 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 9.820239 USDC | 0.008054 USDC | 0.000000 USDC | 0.006740 USDC | 0.001314 USDC (0.0012 €) | — | 1.34 | 0.144 (n=649) | REJECTED | below_safety_margin(1314<1964), p_lower_below_threshold(0.14<0.75) |
| 53330419 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 9.820239 USDC | 0.008054 USDC | 0.000000 USDC | 0.006740 USDC | 0.001314 USDC (0.0012 €) | — | 1.34 | 0.144 (n=649) | REJECTED | below_safety_margin(1314<1964), p_lower_below_threshold(0.14<0.75) |
| 53330418 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.004407 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0012 €) | — | 1.31 | 0.144 (n=649) | REJECTED | below_safety_margin(576407007921<881309199431), p_lower_below_threshold(0.14<0.75) |
| 53330419 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.004407 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0012 €) | — | 1.31 | 0.144 (n=649) | REJECTED | below_safety_margin(576407007921<881309199431), p_lower_below_threshold(0.14<0.75) |
| 53330419 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.004407 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0012 €) | — | 1.31 | 0.144 (n=649) | REJECTED | below_safety_margin(576407007921<881309199431), p_lower_below_threshold(0.14<0.75) |
| 53330402 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 9.281529 USDC | 0.007703 USDC | 0.000000 USDC | 0.006739 USDC | 0.000964 USDC (0.0009 €) | — | 1.04 | 0.189 (n=283) | REJECTED | below_safety_margin(964<1856), p_lower_below_threshold(0.19<0.75) |

## Fiabilité et décision
- Observations ghost : 3945 ; taux observé 0.129 ; borne inférieure crédible (0.9) 0.123 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 12.3% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
