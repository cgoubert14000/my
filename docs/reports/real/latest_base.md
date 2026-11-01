# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-01T12:23:02+00:00 ; durée 107.08 min ; blocs 53370003 → 53373216 (3198 vus)

## Connexion
- Requêtes RPC : 36950 ; erreurs : 3 ; latence p50/p95 : 86.5/663.3 ms
- Rafraîchissements d'état : 3199 ; âge des données au dernier bloc : 2.01 s ; changements de frais LP observés (pools à frais dynamiques) : 2232
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 8497 ; cycles déclenchés par événement : 1301 ; avance médiane sur le rafraîchissement multicall : 267 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,260.19 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 501 pools, 289 jetons, 18668 routes
- Par DEX : uniswap_v3 139, aerodrome_slipstream 112, aerodrome 207, pancakeswap_v3 29, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 178 (rejetés 2) → 583 jetons ; pools candidats 3735 (énumérés 317, par paires 0), mesurés 504, sous le plancher de 10000.0 $ : 3 → gardés 501 (max 1500) ; prix des hubs : {'USDC': 1.0, 'USDbC': 1.0, 'DAI': 1.0, 'WETH': 2268.223075, 'cbBTC': 77979.526152, 'AERO': 0.640175}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 150,629,915 | 2,260.185373 | 53373216 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,138,157 | 0.029046 | 53373216 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,278,146 | 0.000013 | 53373216 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,116,606 | 0.029102 | 53373216 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 7,878,895 | 2,256.956333 | 53373216 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,876,461 | 97.383964 | 53373216 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,669,192 | 0.001590 | 53373216 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 5,690,008 | 1.569797 | 53373216 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,178,657 | 0.029036 | 53373216 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,097,184 | 0.998845 | 53373216 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome_slipstream | WETH/USDC | 150 | 4,059,624 | 2,256.569837 | 53373216 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/USDC | 100 | 3,841,187 | 2,256.525007 | 53373216 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | WETH/KTA | 3000 | 3,557,617 | 37,774.338019 | 53373216 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2510 | 2,697,473 | 0.029088 | 53373216 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2739 | 2,413,628 | 97.428587 | 53373216 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | USDC/cbBTC | 400 | 2,188,139 | 0.000013 | 53373216 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome | WETH/FAI | 10000 | 2,079,741 | 1,197,399.229010 | 53373216 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,758,341 | 0.000000 | 53373216 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,724,095 | 0.017517 | 53373216 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,655,828 | 0.000013 | 53373216 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,585,728 | 0.000013 | 53373216 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,553,850 | 424.565593 | 53373216 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,537,008 | 1.499750 | 53373216 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v2 | WETH/USDC | 3000 | 1,505,919 | 2,260.252920 | 53373216 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,457,455 | 0.825724 | 53373216 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,427,951 | 3,542.223524 | 53373216 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | WETH/USDC | 3000 | 1,407,325 | 2,262.082581 | 53373216 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,346,343 | 2,257.070974 | 53373216 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,323,190 | 0.005168 | 53373216 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,309,372 | 14,590.941534 | 53373216 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome_slipstream | USDC/cbBTC | 334 | 1,307,450 | 0.000013 | 53373216 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/SEND | 3000 | 1,169,853 | 71.003503 | 53373216 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,116,572 | 36,244,784.972170 | 53373216 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,072,325 | 508,523.449741 | 53373216 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,060,722 | 0.000000 | 53373216 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,020,635 | 21,951,530.215130 | 53373216 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | WETH/VVV | 10000 | 996,697 | 96.699319 | 53373216 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome_slipstream | USDC/VELVET | 100 | 994,570 | 19.247973 | 53373216 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | USDC/VVV | 3000 | 983,862 | 0.043167 | 53373216 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | WETH/EDEL | 7000 | 978,144 | 81,505.075938 | 53373216 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | USDC/NOCK | 3000 | 959,379 | 68.016292 | 53373216 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome | WETH/WELL | 10000 | 957,266 | 1,162,935.806093 | 53373216 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/MORPHO | 3000 | 945,119 | 985.892459 | 53373216 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/USDC | 10000 | 922,587 | 2,252.785569 | 53373216 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome | WETH/AERO | 10000 | 870,374 | 3,523.410425 | 53373216 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | uXRP/WETH | 3000 | 861,900 | 0.000548 | 53373216 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 841,880 | 19.303648 | 53373216 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 821,550 | 0.060720 | 53373216 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 765,861 | 0.801881 | 53373216 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| aerodrome | VIRTUAL/WETH | 10000 | 734,029 | 0.000260 | 53373216 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 722,043 | 0.591796 | 53373216 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 715,532 | 4,714,619.366329 | 53373216 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 691,616 | 0.000008 | 53373216 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v2 | WETH/NPC | 3000 | 684,609 | 137,474.633134 | 53373216 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 666,565 | 511,999.882027 | 53373216 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | TIG/USDC | 10000 | 664,726 | 0.555641 | 53373216 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome | WETH/msETH (stable) | 500 | 658,546 | 2.339369 | 53373216 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 614,828 | 0.093577 | 53373216 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| aerodrome | WETH/bsdETH | 100 | 606,554 | 0.916406 | 53373216 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome_slipstream | WETH/MORPHO | 2715 | 555,112 | 985.794542 | 53373216 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |

## Recherche d'opportunités
- Cycles : 4499 ; routes examinées : 83987332 ; candidats optimisés : 274257 ; net attendu > 0 : 431 ; dernier cycle 113.4 ms
- Rejets (moteur) : {'spread_below_threshold': 82864941, 'liquidity_below_min': 824202, 'negative_expected_net': 273826, 'borrow_bound_too_small': 14441, 'unquotable': 8992, 'cycle_budget_exhausted': 499}
- Enregistrements de la session : 274257 ; net attendu > 0 : 431 ; simulés (eth_call de la vraie tx) : 32 (ok 26, échec 6) ; étiquettes ghost N+1 : 0/30 positives
- Décisions : {'REJECTED': 274257} ; motifs de rejet : {'below_safety_margin': 257, 'negative_expected_net': 273826, 'p_lower_below_threshold': 411, 'price_impact': 2, 'reliability_not_demonstrated': 20, 'simulation_failed': 6}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53372995 | WETH→[pancakeswap_v3]→EURC→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→WETH | 0.063961 WETH | 0.000071 WETH | 0.000000 WETH | 0.000003 WETH | 0.000068 WETH (0.1421 €) | 0.000068 WETH | 10.66 | 0.067 (n=100) | REJECTED | p_lower_below_threshold(0.07<0.75) |
| 53372995 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→EURC→[aerodrome_slipstream]→USDC | 144.244787 USDC | 0.161319 USDC | 0.000000 USDC | 0.007152 USDC | 0.154167 USDC (0.1418 €) | — | 10.69 | 0.067 (n=100) | REJECTED | p_lower_below_threshold(0.07<0.75) |
| 53372995 | WETH→[pancakeswap_v3]→EURC→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→WETH | 0.060768 WETH | 0.000066 WETH | 0.000000 WETH | 0.000003 WETH | 0.000063 WETH (0.1321 €) | 0.000063 WETH | 10.43 | 0.067 (n=100) | REJECTED | p_lower_below_threshold(0.07<0.75) |
| 53372995 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→EURC→[aerodrome_slipstream]→USDC | 137.149811 USDC | 0.150131 USDC | 0.000000 USDC | 0.006808 USDC | 0.143323 USDC (0.1319 €) | — | 10.45 | 0.067 (n=100) | REJECTED | p_lower_below_threshold(0.07<0.75) |
| 53372995 | WETH→[pancakeswap_v3]→EURC→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.056907 WETH | 0.000058 WETH | 0.000000 WETH | 0.000003 WETH | 0.000055 WETH (0.1142 €) | 0.000055 WETH | 9.63 | 0.067 (n=100) | REJECTED | p_lower_below_threshold(0.07<0.75) |
| 53372995 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→EURC→[uniswap_v3]→USDC | 128.528221 USDC | 0.130743 USDC | 0.000000 USDC | 0.006808 USDC | 0.123935 USDC (0.1140 €) | — | 9.64 | 0.067 (n=100) | REJECTED | p_lower_below_threshold(0.07<0.75) |
| 53372995 | WETH→[pancakeswap_v3]→EURC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.097161 WETH | 0.000052 WETH | 0.000000 WETH | 0.000003 WETH | 0.000049 WETH (0.1011 €) | — | 4.99 | 0.119 (n=518) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 53372995 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→EURC→[aerodrome_slipstream]→USDC | 219.786778 USDC | 0.116865 USDC | 0.000000 USDC | 0.007152 USDC | 0.109713 USDC (0.1009 €) | — | 4.99 | 0.119 (n=518) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 53372995 | WETH→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→WETH | 0.056567 WETH | 0.000050 WETH | 0.000000 WETH | 0.000003 WETH | 0.000047 WETH (0.0979 €) | — | 8.30 | 0.017 (n=85) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 53372995 | USDC→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→USDC | 127.696615 USDC | 0.113043 USDC | 0.000000 USDC | 0.006808 USDC | 0.106235 USDC (0.0977 €) | — | 8.32 | 0.017 (n=85) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 53372995 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 127.383188 USDC | 0.100457 USDC | 0.000000 USDC | 0.006808 USDC | 0.093649 USDC (0.0862 €) | — | 7.35 | 0.119 (n=518) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 53372995 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.058317 WETH | 0.000044 WETH | 0.000000 WETH | 0.000003 WETH | 0.000041 WETH (0.0861 €) | — | 7.08 | 0.119 (n=518) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 53372995 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC | 0.001493 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0861 €) | — | 8.04 | 0.067 (n=100) | REJECTED | p_lower_below_threshold(0.07<0.75) |
| 53372995 | WETH→[pancakeswap_v3]→EURC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.084181 WETH | 0.000043 WETH | 0.000000 WETH | 0.000003 WETH | 0.000040 WETH (0.0833 €) | — | 4.75 | 0.119 (n=518) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 53372995 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→EURC→[aerodrome_slipstream]→USDC | 190.237370 USDC | 0.097168 USDC | 0.000000 USDC | 0.006808 USDC | 0.090360 USDC (0.0831 €) | — | 4.75 | 0.119 (n=518) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 53372995 | WETH→[pancakeswap_v3]→EURC→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.083330 WETH | 0.000043 WETH | 0.000000 WETH | 0.000003 WETH | 0.000040 WETH (0.0828 €) | — | 4.77 | 0.119 (n=518) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 53372995 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→EURC→[aerodrome_slipstream]→USDC | 188.773124 USDC | 0.096988 USDC | 0.000000 USDC | 0.007152 USDC | 0.089836 USDC (0.0826 €) | — | 4.76 | 0.119 (n=518) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 53370189 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH | 0.053476 WETH | 0.000040 WETH | 0.000000 WETH | 0.000003 WETH | 0.000037 WETH (0.0779 €) | — | 6.98 | 0.119 (n=515) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.12<0.75) |
| 53370189 | USDC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 120.929741 USDC | 0.091510 USDC | 0.000000 USDC | 0.006816 USDC | 0.084694 USDC (0.0779 €) | — | 7.00 | 0.119 (n=515) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 53370189 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH | 0.052830 WETH | 0.000039 WETH | 0.000000 WETH | 0.000003 WETH | 0.000036 WETH (0.0750 €) | — | 6.81 | 0.119 (n=515) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.12<0.75) |
| 53370189 | USDC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 119.611763 USDC | 0.088379 USDC | 0.000000 USDC | 0.006816 USDC | 0.081563 USDC (0.0750 €) | — | 6.82 | 0.119 (n=515) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 53370189 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH | 0.050680 WETH | 0.000037 WETH | 0.000000 WETH | 0.000003 WETH | 0.000034 WETH (0.0716 €) | — | 6.77 | 0.119 (n=515) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.12<0.75) |
| 53370189 | USDC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 114.787888 USDC | 0.084935 USDC | 0.000000 USDC | 0.007160 USDC | 0.077775 USDC (0.0716 €) | — | 6.78 | 0.119 (n=515) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 53372995 | WETH→[pancakeswap_v3]→EURC→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.072827 WETH | 0.000036 WETH | 0.000000 WETH | 0.000003 WETH | 0.000033 WETH (0.0687 €) | — | 4.52 | 0.119 (n=518) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 53372995 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→EURC→[aerodrome_slipstream]→USDC | 164.507147 USDC | 0.081315 USDC | 0.000000 USDC | 0.006808 USDC | 0.074507 USDC (0.0685 €) | — | 4.53 | 0.119 (n=518) | REJECTED | p_lower_below_threshold(0.12<0.75) |

## Fiabilité et décision
- Observations ghost : 4085 ; taux observé 0.129 ; borne inférieure crédible (0.9) 0.122 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 12.2% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ✅ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
