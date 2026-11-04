# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-04T13:49:14+00:00 ; durée 126.29 min ; blocs 53501612 → 53505402 (3783 vus)

## Connexion
- Requêtes RPC : 45369 ; erreurs : 25 ; latence p50/p95 : 130.7/891.4 ms
- Rafraîchissements d'état : 3783 ; âge des données au dernier bloc : 2.51 s ; changements de frais LP observés (pools à frais dynamiques) : 5844
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 13226 ; cycles déclenchés par événement : 1590 ; avance médiane sur le rafraîchissement multicall : 365 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,314.76 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 495 pools, 284 jetons, 19384 routes
- Par DEX : uniswap_v3 142, aerodrome_slipstream 106, aerodrome 204, pancakeswap_v3 29, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 174 (rejetés 2) → 579 jetons ; pools candidats 3706 (énumérés 308, par paires 0), mesurés 498, sous le plancher de 10000.0 $ : 3 → gardés 495 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDC': 1.0, 'USDbC': 1.0, 'WETH': 2327.57512, 'cbBTC': 78571.031441, 'AERO': 0.644724}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 152,230,513 | 2,314.757208 | 53505402 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,917,584 | 0.029596 | 53505402 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,355,287 | 0.029623 | 53505402 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,192,349 | 0.000013 | 53505402 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 8,087,920 | 2,316.997363 | 53505402 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,921,372 | 99.960072 | 53505402 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,621,766 | 0.001552 | 53505402 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 5,367,135 | 1.569054 | 53505402 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,891,409 | 0.029588 | 53505402 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,224,769 | 2,316.726673 | 53505402 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,116,484 | 0.999253 | 53505402 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome_slipstream | WETH/USDC | 150 | 3,862,823 | 2,316.631753 | 53505402 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome | WETH/KTA | 3000 | 3,504,394 | 40,829.165881 | 53505402 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,668,333 | 0.029563 | 53505402 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2703 | 2,179,912 | 99.979448 | 53505402 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | WETH/FAI | 10000 | 2,170,281 | 1,153,315.868669 | 53505402 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 424 | 1,818,558 | 0.000013 | 53505402 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | XDP/USDC | 100 | 1,742,935 | 0.017894 | 53505402 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,662,877 | 0.000000 | 53505402 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,635,158 | 0.006466 | 53505402 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,624,366 | 0.000013 | 53505402 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,576,544 | 438.953734 | 53505402 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,549,821 | 0.000013 | 53505402 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,535,342 | 1.457360 | 53505402 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,453,555 | 0.818198 | 53505402 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,444,342 | 3,636.309763 | 53505402 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,374,994 | 2,316.964067 | 53505402 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | WETH/USDC | 3000 | 1,348,402 | 2,315.597722 | 53505402 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| uniswap_v2 | WETH/USDC | 3000 | 1,347,812 | 2,315.722985 | 53505402 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,308,638 | 14,830.582459 | 53505402 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | USDC/SEND | 3000 | 1,158,110 | 72.450319 | 53505402 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,136,210 | 37,123,742.323280 | 53505402 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | DRB/WETH | 10000 | 1,065,304 | 0.000000 | 53505402 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,064,986 | 551,991.240135 | 53505402 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,039,872 | 22,247,827.318813 | 53505402 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | WETH/VVV | 10000 | 1,008,074 | 99.268538 | 53505402 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome_slipstream | USDC/VELVET | 100 | 995,176 | 19.216389 | 53505402 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | USDC/VVV | 3000 | 972,535 | 0.043137 | 53505402 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/MORPHO | 3000 | 965,862 | 1,052.862117 | 53505402 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome | USDC/NOCK | 3000 | 953,861 | 68.806560 | 53505402 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | USDC/cbBTC | 334 | 947,986 | 0.000013 | 53505402 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | WETH/WELL | 10000 | 939,272 | 1,266,912.604368 | 53505402 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome | WETH/EDEL | 7000 | 933,718 | 93,757.063492 | 53505402 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/USDC | 10000 | 932,687 | 2,312.902102 | 53505402 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | uXRP/WETH | 3000 | 885,082 | 0.000548 | 53505402 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome | WETH/AERO | 10000 | 853,512 | 3,632.791343 | 53505402 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 824,885 | 19.936200 | 53505402 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 795,507 | 0.056691 | 53505402 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 785,691 | 0.799140 | 53505402 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 737,761 | 0.585237 | 53505402 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| aerodrome | VIRTUAL/WETH | 10000 | 731,265 | 0.000254 | 53505402 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 711,959 | 4,999,479.742471 | 53505402 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v2 | WETH/NPC | 3000 | 685,326 | 144,073.905303 | 53505402 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 679,518 | 0.000008 | 53505402 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v3 | TIG/USDC | 10000 | 658,789 | 0.545495 | 53505402 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 654,137 | 555,935.499385 | 53505402 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome | WETH/msETH (stable) | 500 | 644,020 | 2.483701 | 53505402 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome | WETH/bsdETH | 100 | 621,891 | 0.914366 | 53505402 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 602,700 | 0.090630 | 53505402 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| uniswap_v3 | FLOCK/USDC | 3000 | 572,485 | 0.039344 | 53505402 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |

## Recherche d'opportunités
- Cycles : 5372 ; routes examinées : 104130848 ; candidats optimisés : 346303 ; net attendu > 0 : 229 ; dernier cycle 118.9 ms
- Rejets (moteur) : {'spread_below_threshold': 102203390, 'liquidity_below_min': 1575610, 'negative_expected_net': 346074, 'borrow_bound_too_small': 5370, 'cycle_budget_exhausted': 175}
- Enregistrements de la session : 346303 ; net attendu > 0 : 229 ; simulés (eth_call de la vraie tx) : 19 (ok 11, échec 8) ; étiquettes ghost N+1 : 2/19 positives
- Décisions : {'REJECTED': 346303} ; motifs de rejet : {'below_safety_margin': 88, 'negative_expected_net': 346074, 'p_lower_below_threshold': 219, 'reliability_not_demonstrated': 10, 'simulation_failed': 8, 'stale_data': 8}

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
- Observations ghost : 5091 ; taux observé 0.168 ; borne inférieure crédible (0.9) 0.161 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 16.1% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
