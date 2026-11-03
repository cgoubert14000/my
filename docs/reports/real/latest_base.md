# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-03T18:32:21+00:00 ; durée 320.73 min ; blocs 53461072 → 53470692 (9493 vus)

## Connexion
- Requêtes RPC : 110453 ; erreurs : 338 ; latence p50/p95 : 123.8/1,524.2 ms
- Rafraîchissements d'état : 9493 ; âge des données au dernier bloc : 2.48 s ; changements de frais LP observés (pools à frais dynamiques) : 14921
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 88509 ; cycles déclenchés par événement : 7959 ; avance médiane sur le rafraîchissement multicall : 478 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,294.11 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 492 pools, 286 jetons, 19214 routes
- Par DEX : uniswap_v3 138, aerodrome_slipstream 108, aerodrome 204, pancakeswap_v3 28, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 174 (rejetés 2) → 579 jetons ; pools candidats 3706 (énumérés 309, par paires 0), mesurés 495, sous le plancher de 10000.0 $ : 3 → gardés 492 (max 1500) ; prix des hubs : {'USDC': 1.0, 'DAI': 1.0, 'USDbC': 1.0, 'WETH': 2276.593928, 'cbBTC': 77247.513172, 'AERO': 0.617437}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 151,695,066 | 2,294.108297 | 53470692 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,418,679 | 0.029569 | 53470692 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,208,110 | 0.029576 | 53470692 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,024,526 | 0.000013 | 53470692 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 8,057,829 | 2,296.276111 | 53470692 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,753,898 | 103.212375 | 53470692 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,617,192 | 0.001575 | 53470692 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 5,413,213 | 1.578549 | 53470692 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,841,797 | 0.029566 | 53470692 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,168,333 | 2,297.193720 | 53470692 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,082,283 | 0.999841 | 53470692 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome_slipstream | WETH/USDC | 150 | 3,921,180 | 2,296.971534 | 53470692 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome | WETH/KTA | 3000 | 3,423,480 | 42,025.045472 | 53470692 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,714,559 | 0.029581 | 53470692 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 2,180,258 | 1,122,487.229038 | 53470692 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | WETH/VVV | 2751 | 2,111,022 | 103.181826 | 53470692 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | USDC/cbBTC | 496 | 1,813,713 | 0.000013 | 53470692 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | XDP/USDC | 100 | 1,738,362 | 0.017806 | 53470692 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,688,362 | 0.000000 | 53470692 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,640,962 | 0.000013 | 53470692 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,559,193 | 441.744604 | 53470692 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,554,793 | 1.429892 | 53470692 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,553,529 | 0.000013 | 53470692 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v2 | WETH/USDC | 3000 | 1,510,504 | 2,292.979898 | 53470692 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,454,614 | 0.821402 | 53470692 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,430,401 | 3,618.389134 | 53470692 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | WETH/USDC | 3000 | 1,345,738 | 2,290.331489 | 53470692 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,340,866 | 2,296.273710 | 53470692 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,319,679 | 0.005059 | 53470692 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,293,768 | 14,932.934310 | 53470692 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome_slipstream | USDC/cbBTC | 348 | 1,194,844 | 0.000013 | 53470692 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/SEND | 3000 | 1,158,695 | 72.377202 | 53470692 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,129,053 | 36,845,770.635172 | 53470692 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,062,973 | 543,726.044137 | 53470692 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,037,306 | 21,972,681.122588 | 53470692 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | DRB/WETH | 10000 | 1,029,606 | 0.000000 | 53470692 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome_slipstream | USDC/VELVET | 100 | 994,685 | 19.243040 | 53470692 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/MORPHO | 3000 | 963,293 | 1,034.965458 | 53470692 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome | WETH/EDEL | 7000 | 956,570 | 87,743.331997 | 53470692 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | USDC/NOCK | 3000 | 947,313 | 69.760873 | 53470692 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/VVV | 10000 | 946,634 | 103.520872 | 53470692 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome | WETH/WELL | 10000 | 937,115 | 1,250,187.168811 | 53470692 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/USDC | 10000 | 929,961 | 2,282.122456 | 53470692 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | USDC/VVV | 3000 | 890,242 | 0.044921 | 53470692 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | uXRP/WETH | 3000 | 883,118 | 0.000556 | 53470692 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome | WETH/AERO | 10000 | 849,456 | 3,646.232124 | 53470692 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 821,696 | 20.040775 | 53470692 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 798,112 | 0.057087 | 53470692 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 778,682 | 0.799140 | 53470692 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 737,754 | 0.590265 | 53470692 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| aerodrome | VIRTUAL/WETH | 10000 | 729,000 | 0.000257 | 53470692 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 717,746 | 4,831,190.551050 | 53470692 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 675,188 | 0.000008 | 53470692 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v2 | WETH/NPC | 3000 | 669,454 | 148,256.334907 | 53470692 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| uniswap_v3 | TIG/USDC | 10000 | 664,892 | 0.555399 | 53470692 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome | WETH/msETH (stable) | 500 | 663,947 | 2.343097 | 53470692 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | WETH/BRETT | 2096 | 653,385 | 547,973.665264 | 53470692 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome | WETH/bsdETH | 100 | 616,226 | 0.914716 | 53470692 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 584,980 | 0.086672 | 53470692 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| uniswap_v3 | FLOCK/USDC | 3000 | 567,188 | 0.038833 | 53470692 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |

## Recherche d'opportunités
- Cycles : 17451 ; routes examinées : 335303514 ; candidats optimisés : 900475 ; net attendu > 0 : 1201 ; dernier cycle 552.0 ms
- Rejets (moteur) : {'spread_below_threshold': 328787829, 'liquidity_below_min': 5417894, 'negative_expected_net': 899274, 'pool_quarantined': 128124, 'unquotable': 47206, 'borrow_bound_too_small': 17441, 'cycle_budget_exhausted': 4545}
- Enregistrements de la session : 900475 ; net attendu > 0 : 1201 ; simulés (eth_call de la vraie tx) : 82 (ok 15, échec 67) ; étiquettes ghost N+1 : 6/70 positives
- Décisions : {'REJECTED': 900475} ; motifs de rejet : {'below_safety_margin': 774, 'negative_expected_net': 899274, 'p_lower_below_threshold': 1079, 'price_impact': 45, 'reliability_not_demonstrated': 122, 'sim_below_estimate': 2, 'simulated_net_nonpositive': 2, 'simulation_failed': 67}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53470131 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→cbBTC | 0.045605 cbBTC | 0.000167 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000167 cbBTC (11.8974 €) | — | 36.57 | 0.000 (n=35) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53470131 | WETH→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 1.551306 WETH | 0.005640 WETH | 0.000000 WETH | 0.000003 WETH | 0.005637 WETH (11.8966 €) | — | 36.33 | 0.000 (n=35) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 53470131 | cbBTC→[uniswap_v3]→WETH→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→cbBTC | 0.042710 cbBTC | 0.000145 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000145 cbBTC (10.3599 €) | — | 34.00 | 0.000 (n=50) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53470131 | WETH→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→cbBTC→[uniswap_v3]→WETH | 1.443159 WETH | 0.004909 WETH | 0.000000 WETH | 0.000003 WETH | 0.004906 WETH (10.3543 €) | — | 33.99 | 0.000 (n=50) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 53470131 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→cbBTC | 0.038276 cbBTC | 0.000131 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000131 cbBTC (9.3590 €) | — | 34.27 | 0.000 (n=35) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53470131 | WETH→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 1.305186 WETH | 0.004432 WETH | 0.000000 WETH | 0.000003 WETH | 0.004429 WETH (9.3480 €) | — | 33.93 | 0.000 (n=35) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 53470131 | WETH→[aerodrome]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.688309 WETH | 0.003913 WETH | 0.000000 WETH | 0.000003 WETH | 0.003910 WETH (8.2525 €) | — | 56.81 | 0.001 (n=8) | REJECTED | reliability_not_demonstrated |
| 53470131 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome]→AERO→[aerodrome_slipstream]→cbBTC | 0.020358 cbBTC | 0.000116 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000116 cbBTC (8.2524 €) | — | 56.82 | 0.001 (n=8) | REJECTED | reliability_not_demonstrated |
| 53470131 | cbBTC→[uniswap_v3]→WETH→[aerodrome]→AERO→[aerodrome_slipstream]→cbBTC | 0.018456 cbBTC | 0.000103 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000103 cbBTC (7.3335 €) | — | 55.69 | 0.000 (n=23) | REJECTED | reliability_not_demonstrated |
| 53470131 | WETH→[aerodrome]→AERO→[aerodrome_slipstream]→cbBTC→[uniswap_v3]→WETH | 0.623565 WETH | 0.003476 WETH | 0.000000 WETH | 0.000003 WETH | 0.003473 WETH (7.3295 €) | — | 55.69 | 0.000 (n=23) | REJECTED | reliability_not_demonstrated |
| 53470131 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome]→AERO→[aerodrome_slipstream]→cbBTC | 0.017697 cbBTC | 0.000099 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000099 cbBTC (7.0460 €) | — | 55.81 | 0.001 (n=8) | REJECTED | reliability_not_demonstrated |
| 53470131 | WETH→[aerodrome]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.597924 WETH | 0.003339 WETH | 0.000000 WETH | 0.000003 WETH | 0.003336 WETH (7.0403 €) | — | 55.79 | 0.001 (n=8) | REJECTED | reliability_not_demonstrated |
| 53470131 | cbBTC→[aerodrome_slipstream]→WETH→[aerodrome]→AERO→[aerodrome_slipstream]→cbBTC | 0.013614 cbBTC | 0.000075 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000075 cbBTC (5.3644 €) | — | 55.23 | 0.000 (n=23) | REJECTED | reliability_not_demonstrated |
| 53470131 | WETH→[aerodrome]→AERO→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→WETH | 0.458737 WETH | 0.002536 WETH | 0.000000 WETH | 0.000003 WETH | 0.002533 WETH (5.3457 €) | — | 55.21 | 0.000 (n=23) | REJECTED | reliability_not_demonstrated |
| 53470131 | cbBTC→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→cbBTC | 0.029521 cbBTC | 0.000072 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000072 cbBTC (5.1247 €) | — | 24.33 | 0.000 (n=50) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53470131 | WETH→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→WETH | 1.002774 WETH | 0.002425 WETH | 0.000000 WETH | 0.000003 WETH | 0.002422 WETH (5.1114 €) | — | 24.15 | 0.000 (n=50) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53470131 | cbBTC→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→cbBTC | 0.019448 cbBTC | 0.000070 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000070 cbBTC (4.9963 €) | — | 36.01 | 0.000 (n=50) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53470131 | WETH→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→WETH | 0.662202 WETH | 0.002360 WETH | 0.000000 WETH | 0.000003 WETH | 0.002357 WETH (4.9752 €) | — | 35.60 | 0.000 (n=50) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53470131 | cbBTC→[uniswap_v3]→WETH→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→cbBTC | 0.028229 cbBTC | 0.000064 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000063 cbBTC (4.5275 €) | — | 22.48 | 0.000 (n=50) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53470131 | WETH→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→cbBTC→[uniswap_v3]→WETH | 0.958322 WETH | 0.002142 WETH | 0.000000 WETH | 0.000003 WETH | 0.002139 WETH (4.5142 €) | — | 22.32 | 0.000 (n=50) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53470131 | USDC→[pancakeswap_v3]→WETH→[aerodrome]→AERO→[uniswap_v3]→USDC | 760.847852 USDC | 4.785194 USDC | 0.000000 USDC | 0.007630 USDC | 4.777564 USDC (4.3954 €) | — | 62.79 | 0.001 (n=8) | REJECTED | reliability_not_demonstrated |
| 53470131 | WETH→[aerodrome]→AERO→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.331204 WETH | 0.002083 WETH | 0.000000 WETH | 0.000003 WETH | 0.002080 WETH (4.3894 €) | — | 62.79 | 0.001 (n=8) | REJECTED | reliability_not_demonstrated |
| 53470131 | USDC→[aerodrome_slipstream]→WETH→[aerodrome]→AERO→[uniswap_v3]→USDC | 751.697280 USDC | 4.665187 USDC | 0.000000 USDC | 0.007281 USDC | 4.657906 USDC (4.2853 €) | — | 61.97 | 0.000 (n=23) | REJECTED | reliability_not_demonstrated |
| 53470131 | WETH→[aerodrome]→AERO→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.327175 WETH | 0.002031 WETH | 0.000000 WETH | 0.000003 WETH | 0.002027 WETH (4.2789 €) | — | 61.97 | 0.000 (n=23) | REJECTED | reliability_not_demonstrated |
| 53470131 | USDC→[uniswap_v3]→WETH→[aerodrome]→AERO→[uniswap_v3]→USDC | 728.794035 USDC | 4.545056 USDC | 0.000000 USDC | 0.008326 USDC | 4.536730 USDC (4.1738 €) | — | 62.25 | 0.000 (n=23) | REJECTED | reliability_not_demonstrated |

## Fiabilité et décision
- Observations ghost : 4905 ; taux observé 0.169 ; borne inférieure crédible (0.9) 0.162 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 16.2% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
