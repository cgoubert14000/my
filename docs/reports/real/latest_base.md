# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-04T11:12:30+00:00 ; durée 305.4 min ; blocs 53491535 → 53500698 (9116 vus)

## Connexion
- Requêtes RPC : 103095 ; erreurs : 0 ; latence p50/p95 : 237.0/1,062.4 ms
- Rafraîchissements d'état : 9116 ; âge des données au dernier bloc : 3.51 s ; changements de frais LP observés (pools à frais dynamiques) : 13239
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 2397 ; cycles déclenchés par événement : 309 ; avance médiane sur le rafraîchissement multicall : 626 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,324.25 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 494 pools, 284 jetons, 19492 routes
- Par DEX : uniswap_v3 141, aerodrome_slipstream 106, aerodrome 204, pancakeswap_v3 29, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 173 (rejetés 2) → 578 jetons ; pools candidats 3704 (énumérés 307, par paires 0), mesurés 497, sous le plancher de 10000.0 $ : 3 → gardés 494 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDC': 1.0, 'USDbC': 1.0, 'WETH': 2296.568203, 'cbBTC': 77781.37292, 'AERO': 0.62987}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 152,419,105 | 2,324.253274 | 53500698 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,935,387 | 0.029652 | 53500698 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,345,409 | 0.029594 | 53500698 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,170,798 | 0.000013 | 53500698 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 8,147,912 | 2,328.961807 | 53500698 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 8,067,961 | 97.156888 | 53500698 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,652,424 | 0.001559 | 53500698 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 5,415,941 | 1.552662 | 53500698 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,905,450 | 0.029664 | 53500698 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,223,304 | 2,329.920911 | 53500698 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,123,759 | 0.999894 | 53500698 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome_slipstream | WETH/USDC | 150 | 3,895,398 | 2,329.888176 | 53500698 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome | WETH/KTA | 3000 | 3,514,977 | 40,920.174749 | 53500698 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,678,581 | 0.029610 | 53500698 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2709 | 2,217,038 | 97.135831 | 53500698 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | WETH/FAI | 10000 | 2,179,184 | 1,153,315.868669 | 53500698 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 460 | 1,825,579 | 0.000013 | 53500698 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | XDP/USDC | 100 | 1,746,883 | 0.017962 | 53500698 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,695,040 | 0.000000 | 53500698 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,632,886 | 0.006424 | 53500698 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,630,384 | 0.000013 | 53500698 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,588,542 | 433.835526 | 53500698 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,553,942 | 0.000013 | 53500698 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,552,810 | 1.433011 | 53500698 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | WETH/AERO | 3000 | 1,455,250 | 3,609.634954 | 53500698 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,454,396 | 0.818931 | 53500698 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,379,392 | 2,329.017976 | 53500698 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | WETH/USDC | 3000 | 1,351,166 | 2,328.746137 | 53500698 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| uniswap_v2 | WETH/USDC | 3000 | 1,350,562 | 2,324.502174 | 53500698 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,319,038 | 14,658.110207 | 53500698 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | USDC/SEND | 3000 | 1,158,306 | 72.425825 | 53500698 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,140,193 | 37,190,801.109527 | 53500698 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,069,602 | 551,624.988487 | 53500698 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,064,412 | 0.000000 | 53500698 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,044,403 | 22,204,813.882201 | 53500698 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | WETH/VVV | 10000 | 1,026,552 | 96.478842 | 53500698 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome_slipstream | USDC/VELVET | 100 | 998,763 | 19.018582 | 53500698 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | USDC/VVV | 3000 | 991,630 | 0.041757 | 53500698 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/MORPHO | 3000 | 977,279 | 1,040.289948 | 53500698 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome_slipstream | USDC/cbBTC | 340 | 949,491 | 0.000013 | 53500698 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | WETH/WELL | 10000 | 942,653 | 1,268,183.094439 | 53500698 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome | USDC/NOCK | 3000 | 935,617 | 71.516051 | 53500698 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/USDC | 10000 | 933,905 | 2,307.778444 | 53500698 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome | WETH/EDEL | 7000 | 928,523 | 95,588.597076 | 53500698 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | uXRP/WETH | 3000 | 891,856 | 0.000551 | 53500698 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome | WETH/AERO | 10000 | 860,002 | 3,632.791343 | 53500698 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 828,671 | 19.799067 | 53500698 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 797,987 | 0.057065 | 53500698 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 788,914 | 0.799140 | 53500698 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 739,885 | 0.591747 | 53500698 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| aerodrome | VIRTUAL/WETH | 10000 | 734,301 | 0.000254 | 53500698 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 716,875 | 4,971,471.496958 | 53500698 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v2 | WETH/NPC | 3000 | 687,948 | 144,151.493942 | 53500698 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 683,945 | 0.000008 | 53500698 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 657,039 | 550,428.918626 | 53500698 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | TIG/USDC | 10000 | 653,910 | 0.537869 | 53500698 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome | WETH/msETH (stable) | 500 | 647,951 | 2.476435 | 53500698 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome | WETH/bsdETH | 100 | 624,625 | 0.913833 | 53500698 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 610,507 | 0.092434 | 53500698 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| uniswap_v3 | FLOCK/USDC | 3000 | 574,205 | 0.039521 | 53500698 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |

## Recherche d'opportunités
- Cycles : 9424 ; routes examinées : 183692608 ; candidats optimisés : 597577 ; net attendu > 0 : 552 ; dernier cycle 522.1 ms
- Rejets (moteur) : {'spread_below_threshold': 180173868, 'liquidity_below_min': 2909519, 'negative_expected_net': 597025, 'borrow_bound_too_small': 9407, 'cycle_budget_exhausted': 2100}
- Enregistrements de la session : 597575 ; net attendu > 0 : 552 ; simulés (eth_call de la vraie tx) : 27 (ok 25, échec 2) ; étiquettes ghost N+1 : 0/26 positives
- Décisions : {'REJECTED': 597575} ; motifs de rejet : {'below_safety_margin': 424, 'negative_expected_net': 597023, 'p_lower_below_threshold': 539, 'reliability_not_demonstrated': 13, 'simulation_failed': 2, 'stale_data': 6}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53498561 | USDC→[pancakeswap_v3]→ICNT→[uniswap_v3]→USDC | 74.951959 USDC | 0.080508 USDC | 0.000000 USDC | 0.005210 USDC | 0.075298 USDC (0.0693 €) | — | 10.05 | 0.000 (n=79) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 53494541 | USDC→[aerodrome_slipstream]→cbBTC→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 396.927215 USDC | 0.070121 USDC | 0.000000 USDC | 0.007272 USDC | 0.062849 USDC (0.0578 €) | — | 1.58 | 0.256 (n=350) | REJECTED | below_safety_margin(62849<79385), p_lower_below_threshold(0.26<0.75) |
| 53494541 | cbBTC→[uniswap_v3]→WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→cbBTC | 0.004907 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0574 €) | — | 1.63 | 0.256 (n=350) | REJECTED | below_safety_margin(80<98), p_lower_below_threshold(0.26<0.75) |
| 53494541 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→cbBTC→[uniswap_v3]→WETH | 0.171917 WETH | 0.000030 WETH | 0.000000 WETH | 0.000003 WETH | 0.000027 WETH (0.0574 €) | — | 1.58 | 0.256 (n=350) | REJECTED | below_safety_margin(27092060689453<34383492694631), p_lower_below_threshold(0.26<0.75) |
| 53494541 | cbBTC→[uniswap_v3]→WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.002332 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0431 €) | — | 2.57 | 0.183 (n=877) | REJECTED | p_lower_below_threshold(0.18<0.75) |
| 53494541 | USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 192.043443 USDC | 0.053695 USDC | 0.000000 USDC | 0.006922 USDC | 0.046773 USDC (0.0430 €) | — | 2.44 | 0.183 (n=877) | REJECTED | p_lower_below_threshold(0.18<0.75) |
| 53494541 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH | 0.091948 WETH | 0.000023 WETH | 0.000000 WETH | 0.000003 WETH | 0.000020 WETH (0.0429 €) | 0.000020 WETH | 2.20 | 0.183 (n=877) | REJECTED | p_lower_below_threshold(0.18<0.75) |
| 53494541 | cbBTC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.001113 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0416 €) | — | 5.21 | 0.161 (n=630) | REJECTED | p_lower_below_threshold(0.16<0.75) |
| 53494541 | USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 99.787582 USDC | 0.051811 USDC | 0.000000 USDC | 0.006922 USDC | 0.044889 USDC (0.0413 €) | — | 4.50 | 0.161 (n=630) | REJECTED | p_lower_below_threshold(0.16<0.75) |
| 53494541 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH | 0.044572 WETH | 0.000022 WETH | 0.000000 WETH | 0.000003 WETH | 0.000019 WETH (0.0409 €) | 0.000019 WETH | 4.34 | 0.161 (n=630) | REJECTED | p_lower_below_threshold(0.16<0.75) |
| 53494541 | USDC→[aerodrome_slipstream]→EURC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 78.349042 USDC | 0.044388 USDC | 0.000000 USDC | 0.006922 USDC | 0.037466 USDC (0.0345 €) | — | 4.78 | 0.161 (n=630) | REJECTED | p_lower_below_threshold(0.16<0.75) |
| 53494541 | WETH→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→EURC→[pancakeswap_v3]→WETH | 0.034068 WETH | 0.000019 WETH | 0.000000 WETH | 0.000003 WETH | 0.000016 WETH (0.0344 €) | 0.000016 WETH | 4.77 | 0.161 (n=630) | REJECTED | p_lower_below_threshold(0.16<0.75) |
| 53494541 | USDC→[uniswap_v3]→EURC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 76.885486 USDC | 0.043631 USDC | 0.000000 USDC | 0.006922 USDC | 0.036709 USDC (0.0338 €) | — | 4.77 | 0.161 (n=630) | REJECTED | p_lower_below_threshold(0.16<0.75) |
| 53494541 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→EURC→[pancakeswap_v3]→WETH | 0.033473 WETH | 0.000019 WETH | 0.000000 WETH | 0.000003 WETH | 0.000016 WETH (0.0337 €) | — | 4.75 | 0.161 (n=630) | REJECTED | p_lower_below_threshold(0.16<0.75) |
| 53494541 | USDC→[aerodrome_slipstream]→EURC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 77.394326 USDC | 0.043498 USDC | 0.000000 USDC | 0.006922 USDC | 0.036576 USDC (0.0336 €) | — | 4.73 | 0.161 (n=630) | REJECTED | p_lower_below_threshold(0.16<0.75) |
| 53494541 | WETH→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→EURC→[pancakeswap_v3]→WETH | 0.033685 WETH | 0.000019 WETH | 0.000000 WETH | 0.000003 WETH | 0.000016 WETH (0.0336 €) | — | 4.71 | 0.161 (n=630) | REJECTED | p_lower_below_threshold(0.16<0.75) |
| 53494541 | cbBTC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→cbBTC | 0.001088 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0330 €) | — | 4.23 | 0.290 (n=322) | REJECTED | p_lower_below_threshold(0.29<0.75) |
| 53494541 | USDC→[aerodrome_slipstream]→cbBTC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 85.932718 USDC | 0.042640 USDC | 0.000000 USDC | 0.006922 USDC | 0.035718 USDC (0.0329 €) | — | 4.16 | 0.290 (n=322) | REJECTED | p_lower_below_threshold(0.29<0.75) |
| 53494541 | WETH→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→cbBTC→[uniswap_v3]→WETH | 0.044571 WETH | 0.000018 WETH | 0.000000 WETH | 0.000003 WETH | 0.000015 WETH (0.0324 €) | — | 3.43 | 0.290 (n=322) | REJECTED | p_lower_below_threshold(0.29<0.75) |
| 53494541 | USDC→[uniswap_v3]→cbBTC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 84.290656 USDC | 0.038155 USDC | 0.000000 USDC | 0.006922 USDC | 0.031233 USDC (0.0287 €) | — | 3.71 | 0.290 (n=322) | REJECTED | p_lower_below_threshold(0.29<0.75) |
| 53494541 | cbBTC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→cbBTC | 0.001088 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0287 €) | — | 3.68 | 0.290 (n=322) | REJECTED | p_lower_below_threshold(0.29<0.75) |
| 53494541 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→cbBTC→[uniswap_v3]→WETH | 0.039648 WETH | 0.000016 WETH | 0.000000 WETH | 0.000003 WETH | 0.000013 WETH (0.0284 €) | — | 3.39 | 0.290 (n=322) | REJECTED | p_lower_below_threshold(0.29<0.75) |
| 53494541 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.001088 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0273 €) | — | 3.49 | 0.161 (n=630) | REJECTED | p_lower_below_threshold(0.16<0.75) |
| 53494541 | cbBTC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.001078 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0273 €) | — | 3.53 | 0.161 (n=630) | REJECTED | p_lower_below_threshold(0.16<0.75) |
| 53494541 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 82.621603 USDC | 0.036138 USDC | 0.000000 USDC | 0.006922 USDC | 0.029216 USDC (0.0269 €) | — | 3.54 | 0.161 (n=630) | REJECTED | p_lower_below_threshold(0.16<0.75) |

## Fiabilité et décision
- Observations ghost : 5069 ; taux observé 0.168 ; borne inférieure crédible (0.9) 0.161 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 16.1% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ✅ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
