# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-04T13:03:01+00:00 ; durée 80.09 min ; blocs 53501612 → 53504016 (2402 vus)

## Connexion
- Requêtes RPC : 28901 ; erreurs : 3 ; latence p50/p95 : 70.8/1,010.1 ms
- Rafraîchissements d'état : 2403 ; âge des données au dernier bloc : 1.31 s ; changements de frais LP observés (pools à frais dynamiques) : 3916
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 2870 ; cycles déclenchés par événement : 336 ; avance médiane sur le rafraîchissement multicall : 348 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,314.76 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 495 pools, 284 jetons, 19384 routes
- Par DEX : uniswap_v3 142, aerodrome_slipstream 106, aerodrome 204, pancakeswap_v3 29, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 174 (rejetés 2) → 579 jetons ; pools candidats 3706 (énumérés 308, par paires 0), mesurés 498, sous le plancher de 10000.0 $ : 3 → gardés 495 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDC': 1.0, 'USDbC': 1.0, 'WETH': 2327.57512, 'cbBTC': 78571.031441, 'AERO': 0.644724}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 152,066,686 | 2,314.756655 | 53504016 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,931,197 | 0.029562 | 53504016 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,360,178 | 0.029623 | 53504016 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,195,871 | 0.000013 | 53504016 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 8,085,262 | 2,317.202376 | 53504016 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,970,947 | 98.720498 | 53504016 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,621,996 | 0.001548 | 53504016 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 5,355,674 | 1.575768 | 53504016 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,892,191 | 0.029563 | 53504016 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,234,681 | 2,316.908087 | 53504016 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,119,502 | 0.999894 | 53504016 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome_slipstream | WETH/USDC | 788 | 3,884,038 | 2,316.754820 | 53504016 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome | WETH/KTA | 3000 | 3,504,215 | 40,836.155022 | 53504016 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2525 | 2,670,439 | 0.029622 | 53504016 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2709 | 2,191,710 | 98.700520 | 53504016 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | WETH/FAI | 10000 | 2,170,280 | 1,153,315.868669 | 53504016 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 600 | 1,819,904 | 0.000013 | 53504016 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | XDP/USDC | 100 | 1,743,328 | 0.017902 | 53504016 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,662,447 | 0.000000 | 53504016 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,630,018 | 0.006443 | 53504016 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,629,093 | 0.000013 | 53504016 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,578,905 | 436.767185 | 53504016 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,553,144 | 0.000013 | 53504016 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,540,593 | 1.452399 | 53504016 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,453,540 | 0.818214 | 53504016 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,440,273 | 3,645.091088 | 53504016 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,374,894 | 2,317.175554 | 53504016 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | WETH/USDC | 3000 | 1,348,402 | 2,315.724903 | 53504016 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| uniswap_v2 | WETH/USDC | 3000 | 1,347,809 | 2,314.876819 | 53504016 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,312,290 | 14,760.309740 | 53504016 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | USDC/SEND | 3000 | 1,158,306 | 72.425825 | 53504016 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,136,210 | 37,123,742.323280 | 53504016 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,065,235 | 551,620.067121 | 53504016 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,063,349 | 0.000000 | 53504016 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,039,903 | 22,246,651.370919 | 53504016 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | WETH/VVV | 10000 | 1,014,382 | 98.026036 | 53504016 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome_slipstream | USDC/VELVET | 100 | 995,085 | 19.221488 | 53504016 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | USDC/VVV | 3000 | 981,437 | 0.042601 | 53504016 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/MORPHO | 3000 | 972,824 | 1,040.839758 | 53504016 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome_slipstream | USDC/cbBTC | 378 | 948,797 | 0.000013 | 53504016 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | WETH/WELL | 10000 | 938,655 | 1,268,577.703025 | 53504016 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome | USDC/NOCK | 3000 | 938,394 | 71.093390 | 53504016 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/USDC | 10000 | 932,687 | 2,312.902102 | 53504016 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome | WETH/EDEL | 7000 | 930,957 | 94,313.901975 | 53504016 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | uXRP/WETH | 3000 | 885,260 | 0.000549 | 53504016 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome | WETH/AERO | 10000 | 851,706 | 3,632.791343 | 53504016 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 825,234 | 19.923515 | 53504016 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 795,638 | 0.056711 | 53504016 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 785,691 | 0.799140 | 53504016 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 737,634 | 0.585972 | 53504016 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| aerodrome | VIRTUAL/WETH | 10000 | 731,264 | 0.000254 | 53504016 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 710,130 | 5,025,226.815022 | 53504016 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v2 | WETH/NPC | 3000 | 685,107 | 144,165.698100 | 53504016 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 678,283 | 0.000008 | 53504016 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v3 | TIG/USDC | 10000 | 656,984 | 0.542670 | 53504016 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 654,366 | 554,817.040215 | 53504016 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome | WETH/msETH (stable) | 500 | 644,102 | 2.483231 | 53504016 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome | WETH/bsdETH | 100 | 622,059 | 0.913872 | 53504016 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 601,042 | 0.090252 | 53504016 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| uniswap_v3 | FLOCK/USDC | 3000 | 570,888 | 0.039176 | 53504016 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |

## Recherche d'opportunités
- Cycles : 2738 ; routes examinées : 53073392 ; candidats optimisés : 185017 ; net attendu > 0 : 160 ; dernier cycle 289.7 ms
- Rejets (moteur) : {'spread_below_threshold': 52077733, 'liquidity_below_min': 807783, 'negative_expected_net': 184857, 'borrow_bound_too_small': 2737, 'cycle_budget_exhausted': 122}
- Enregistrements de la session : 185017 ; net attendu > 0 : 160 ; simulés (eth_call de la vraie tx) : 14 (ok 10, échec 4) ; étiquettes ghost N+1 : 1/14 positives
- Décisions : {'REJECTED': 185017} ; motifs de rejet : {'below_safety_margin': 71, 'negative_expected_net': 184857, 'p_lower_below_threshold': 151, 'reliability_not_demonstrated': 9, 'simulation_failed': 4, 'stale_data': 8}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53501798 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→AERO→[aerodrome]→USDC | 2,034.593747 USDC | 3.018894 USDC | 0.000000 USDC | 0.007392 USDC | 3.011502 USDC (2.7706 €) | — | 14.80 | 0.130 (n=40) | REJECTED | p_lower_below_threshold(0.13<0.75) |
| 53501798 | cbBTC→[aerodrome_slipstream]→AERO→[aerodrome]→USDC→[pancakeswap_v3]→cbBTC | 0.025981 cbBTC | 0.000038 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000038 cbBTC (2.7669 €) | — | 14.76 | 0.130 (n=40) | REJECTED | p_lower_below_threshold(0.13<0.75) |
| 53501798 | USDC→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→AERO→[aerodrome]→USDC | 1,767.921875 USDC | 2.407901 USDC | 0.000000 USDC | 0.006685 USDC | 2.401216 USDC (2.2091 €) | — | 13.58 | 0.067 (n=175) | REJECTED | p_lower_below_threshold(0.07<0.75) |
| 53501798 | cbBTC→[aerodrome_slipstream]→AERO→[aerodrome]→USDC→[aerodrome_slipstream]→cbBTC | 0.022432 cbBTC | 0.000031 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000031 cbBTC (2.2055 €) | — | 13.62 | 0.067 (n=175) | REJECTED | p_lower_below_threshold(0.07<0.75) |
| 53501798 | USDC→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→AERO→[aerodrome]→USDC | 1,514.082298 USDC | 1.845325 USDC | 0.000000 USDC | 0.006685 USDC | 1.838640 USDC (1.6915 €) | — | 12.14 | 0.067 (n=175) | REJECTED | p_lower_below_threshold(0.07<0.75) |
| 53501798 | cbBTC→[aerodrome_slipstream]→AERO→[aerodrome]→USDC→[aerodrome_slipstream]→cbBTC | 0.019018 cbBTC | 0.000023 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000023 cbBTC (1.6880 €) | — | 12.30 | 0.067 (n=175) | REJECTED | p_lower_below_threshold(0.07<0.75) |
| 53501798 | USDC→[uniswap_v3]→cbBTC→[aerodrome_slipstream]→AERO→[aerodrome]→USDC | 1,642.926197 USDC | 1.835277 USDC | 0.000000 USDC | 0.006685 USDC | 1.828592 USDC (1.6823 €) | — | 11.13 | 0.067 (n=175) | REJECTED | p_lower_below_threshold(0.07<0.75) |
| 53501798 | cbBTC→[aerodrome_slipstream]→AERO→[aerodrome]→USDC→[uniswap_v3]→cbBTC | 0.020773 cbBTC | 0.000023 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000023 cbBTC (1.6793 €) | — | 11.20 | 0.067 (n=175) | REJECTED | p_lower_below_threshold(0.07<0.75) |
| 53501798 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→WETH | 0.510340 WETH | 0.000611 WETH | 0.000000 WETH | 0.000003 WETH | 0.000608 WETH (1.3035 €) | — | 11.92 | 0.097 (n=121) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.10<0.75) |
| 53501798 | cbBTC→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC | 0.015101 cbBTC | 0.000018 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000018 cbBTC (1.3034 €) | — | 11.96 | 0.097 (n=121) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53501798 | cbBTC→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→WETH→[uniswap_v3]→cbBTC | 0.014794 cbBTC | 0.000017 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000017 cbBTC (1.2536 €) | — | 11.74 | 0.030 (n=93) | REJECTED | p_lower_below_threshold(0.03<0.75) |
| 53501798 | WETH→[uniswap_v3]→cbBTC→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→WETH | 0.496341 WETH | 0.000588 WETH | 0.000000 WETH | 0.000003 WETH | 0.000585 WETH (1.2535 €) | — | 11.79 | 0.030 (n=93) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.03<0.75) |
| 53501798 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→WETH | 0.433638 WETH | 0.000494 WETH | 0.000000 WETH | 0.000003 WETH | 0.000491 WETH (1.0518 €) | — | 11.32 | 0.097 (n=121) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.10<0.75) |
| 53501798 | cbBTC→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC | 0.012582 cbBTC | 0.000015 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000015 cbBTC (1.0508 €) | — | 11.57 | 0.097 (n=121) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53501798 | USDC→[uniswap_v3]→cbBTC→[aerodrome_slipstream]→AERO→[aerodrome]→USDC | 1,121.920580 USDC | 0.911875 USDC | 0.000000 USDC | 0.006685 USDC | 0.905190 USDC (0.8328 €) | — | 8.07 | 0.067 (n=175) | REJECTED | p_lower_below_threshold(0.07<0.75) |
| 53501798 | cbBTC→[aerodrome_slipstream]→AERO→[aerodrome]→USDC→[uniswap_v3]→cbBTC | 0.013997 cbBTC | 0.000012 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000012 cbBTC (0.8307 €) | — | 8.22 | 0.067 (n=175) | REJECTED | p_lower_below_threshold(0.07<0.75) |
| 53501798 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→AERO→[aerodrome]→USDC | 612.183435 USDC | 0.652754 USDC | 0.000000 USDC | 0.007039 USDC | 0.645715 USDC (0.5941 €) | — | 10.55 | 0.130 (n=40) | REJECTED | p_lower_below_threshold(0.13<0.75) |
| 53501798 | cbBTC→[aerodrome_slipstream]→AERO→[aerodrome]→USDC→[pancakeswap_v3]→cbBTC | 0.007516 cbBTC | 0.000008 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000008 cbBTC (0.5918 €) | — | 10.91 | 0.130 (n=40) | REJECTED | p_lower_below_threshold(0.13<0.75) |
| 53501798 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→AERO→[pancakeswap_v3]→WETH | 0.151314 WETH | 0.000272 WETH | 0.000000 WETH | 0.000003 WETH | 0.000269 WETH (0.5771 €) | — | 17.80 | 0.097 (n=121) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53501798 | cbBTC→[aerodrome_slipstream]→AERO→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.004491 cbBTC | 0.000008 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000008 cbBTC (0.5766 €) | — | 17.79 | 0.097 (n=121) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53501798 | WETH→[uniswap_v3]→cbBTC→[aerodrome_slipstream]→AERO→[pancakeswap_v3]→WETH | 0.150937 WETH | 0.000264 WETH | 0.000000 WETH | 0.000003 WETH | 0.000261 WETH (0.5597 €) | — | 17.31 | 0.097 (n=121) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53501798 | cbBTC→[aerodrome_slipstream]→AERO→[pancakeswap_v3]→WETH→[uniswap_v3]→cbBTC | 0.004491 cbBTC | 0.000008 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000008 cbBTC (0.5593 €) | — | 17.26 | 0.097 (n=121) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53501798 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→AERO→[pancakeswap_v3]→WETH | 0.143622 WETH | 0.000248 WETH | 0.000000 WETH | 0.000003 WETH | 0.000245 WETH (0.5246 €) | — | 17.05 | 0.097 (n=121) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53501798 | cbBTC→[aerodrome_slipstream]→AERO→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.004153 cbBTC | 0.000007 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000007 cbBTC (0.5239 €) | — | 17.48 | 0.097 (n=121) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53501798 | WETH→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→WETH | 0.204064 WETH | 0.000229 WETH | 0.000000 WETH | 0.000003 WETH | 0.000226 WETH (0.4849 €) | — | 11.09 | 0.030 (n=93) | REJECTED | p_lower_below_threshold(0.03<0.75) |

## Fiabilité et décision
- Observations ghost : 5086 ; taux observé 0.168 ; borne inférieure crédible (0.9) 0.161 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 16.1% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
