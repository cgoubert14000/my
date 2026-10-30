# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-30T19:38:21+00:00 ; durée 18.3 min ; blocs 53299323 → 53299876 (546 vus)

## Connexion
- Requêtes RPC : 6358 ; erreurs : 0 ; latence p50/p95 : 398.7/1,519.2 ms
- Rafraîchissements d'état : 547 ; âge des données au dernier bloc : 1.72 s ; changements de frais LP observés (pools à frais dynamiques) : 977
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 9394 ; cycles déclenchés par événement : 523 ; avance médiane sur le rafraîchissement multicall : 830 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,225.35 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 497 pools, 288 jetons, 18532 routes
- Par DEX : uniswap_v3 136, aerodrome_slipstream 112, aerodrome 205, pancakeswap_v3 29, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 178 (rejetés 2) → 583 jetons ; pools candidats 3774 (énumérés 315, par paires 0), mesurés 500, sous le plancher de 10000.0 $ : 3 → gardés 497 (max 1500) ; prix des hubs : {'USDC': 1.0, 'USDbC': 1.0, 'DAI': 1.0, 'WETH': 2226.87299, 'cbBTC': 76304.747909, 'AERO': 0.609807}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 149,690,268 | 2,225.349302 | 53299876 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,812,825 | 0.029130 | 53299876 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,625,753 | 0.000013 | 53299876 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 8,942,578 | 0.029112 | 53299876 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 8,130,846 | 2,227.866366 | 53299876 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,604,618 | 101.572392 | 53299876 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,590,181 | 0.001611 | 53299876 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 5,834,806 | 1.637314 | 53299876 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,511,749 | 0.029127 | 53299876 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/USDC | 698 | 4,117,728 | 2,227.239803 | 53299876 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,034,453 | 2,227.114865 | 53299876 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,021,416 | 0.998958 | 53299876 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,510,921 | 37,599.578114 | 53299876 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,728,208 | 0.029126 | 53299876 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2712 | 2,290,733 | 101.631738 | 53299876 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | WETH/FAI | 10000 | 2,040,080 | 1,206,344.208581 | 53299876 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 556 | 1,901,783 | 0.000013 | 53299876 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,750,772 | 0.000000 | 53299876 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,715,449 | 0.017344 | 53299876 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,666,792 | 423.172056 | 53299876 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,617,649 | 0.000013 | 53299876 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,533,252 | 0.000013 | 53299876 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | WETH/USDC | 3000 | 1,518,418 | 2,228.912074 | 53299876 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,512,933 | 1.548785 | 53299876 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,454,686 | 0.825659 | 53299876 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | USDC/cbBTC | 362 | 1,452,304 | 0.000013 | 53299876 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | WETH/AERO | 3000 | 1,387,284 | 3,645.179264 | 53299876 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,306,576 | 2,227.828264 | 53299876 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,288,346 | 14,527.551479 | 53299876 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,263,866 | 0.004960 | 53299876 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome | USDC/SEND | 3000 | 1,176,193 | 70.240036 | 53299876 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,094,726 | 36,605,298.548697 | 53299876 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,048,476 | 517,398.175090 | 53299876 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,029,960 | 21,015,971.546121 | 53299876 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | DRB/WETH | 10000 | 1,013,202 | 0.000000 | 53299876 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | WETH/EDEL | 7000 | 1,008,020 | 74,433.570233 | 53299876 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v2 | WETH/USDC | 3000 | 1,005,812 | 2,225.721574 | 53299876 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | USDC/VELVET | 100 | 988,705 | 19.580523 | 53299876 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | USDC/NOCK | 3000 | 972,154 | 66.239399 | 53299876 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/VVV | 10000 | 953,422 | 101.211377 | 53299876 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | USDC/VVV | 3000 | 934,577 | 0.045623 | 53299876 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/USDC | 10000 | 917,910 | 2,235.963227 | 53299876 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome | WETH/WELL | 10000 | 917,065 | 1,231,134.743514 | 53299876 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/MORPHO | 3000 | 880,285 | 1,088.079959 | 53299876 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | uXRP/WETH | 3000 | 855,287 | 0.000553 | 53299876 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome | WETH/AERO | 10000 | 851,403 | 3,618.825714 | 53299876 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 830,122 | 19.709429 | 53299876 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 813,353 | 0.059422 | 53299876 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 753,242 | 0.803616 | 53299876 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| aerodrome | VIRTUAL/WETH | 10000 | 730,821 | 0.000264 | 53299876 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 721,197 | 4,497,867.658229 | 53299876 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 719,916 | 0.587134 | 53299876 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| aerodrome | WETH/msETH (stable) | 500 | 675,591 | 2.330205 | 53299876 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 669,606 | 0.000008 | 53299876 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 650,473 | 521,500.601896 | 53299876 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v2 | WETH/NPC | 3000 | 647,762 | 148,809.295257 | 53299876 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| uniswap_v3 | TIG/USDC | 10000 | 629,569 | 0.501272 | 53299876 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 599,578 | 0.090128 | 53299876 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| aerodrome | WETH/bsdETH | 100 | 598,350 | 0.915108 | 53299876 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome_slipstream | WETH/MORPHO | 2703 | 533,425 | 1,087.736379 | 53299876 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |

## Recherche d'opportunités
- Cycles : 1069 ; routes examinées : 19810708 ; candidats optimisés : 80519 ; net attendu > 0 : 109 ; dernier cycle 307.8 ms
- Rejets (moteur) : {'spread_below_threshold': 19487805, 'liquidity_below_min': 233814, 'negative_expected_net': 80410, 'unquotable': 7416, 'borrow_bound_too_small': 1068}
- Enregistrements de la session : 80519 ; net attendu > 0 : 109 ; simulés (eth_call de la vraie tx) : 2 (ok 0, échec 2) ; étiquettes ghost N+1 : 0/2 positives
- Décisions : {'REJECTED': 80519} ; motifs de rejet : {'below_safety_margin': 107, 'negative_expected_net': 80410, 'p_lower_below_threshold': 94, 'reliability_not_demonstrated': 15, 'simulation_failed': 2}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53299663 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 852.704355 USDC | 0.105755 USDC | 0.000000 USDC | 0.007061 USDC | 0.098694 USDC (0.0908 €) | — | 1.16 | 0.001 (n=15) | REJECTED | below_safety_margin(98694<170540), reliability_not_demonstrated |
| 53299663 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.378616 WETH | 0.000047 WETH | 0.000000 WETH | 0.000003 WETH | 0.000044 WETH (0.0907 €) | — | 1.17 | 0.001 (n=15) | REJECTED | below_safety_margin(44325697852444<75723270317330), reliability_not_demonstrated |
| 53299663 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.011165 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0906 €) | — | 1.16 | 0.001 (n=15) | REJECTED | below_safety_margin(129<223), reliability_not_demonstrated |
| 53299663 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC | 0.009073 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0653 €) | — | 1.03 | 0.145 (n=645) | REJECTED | below_safety_margin(93<181), p_lower_below_threshold(0.14<0.75) |
| 53299663 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 763.278000 USDC | 0.077483 USDC | 0.000000 USDC | 0.006723 USDC | 0.070760 USDC (0.0651 €) | — | 0.93 | 0.145 (n=645) | REJECTED | below_safety_margin(70760<152655), p_lower_below_threshold(0.14<0.75) |
| 53299663 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.342793 WETH | 0.000035 WETH | 0.000000 WETH | 0.000003 WETH | 0.000032 WETH (0.0651 €) | — | 0.93 | 0.145 (n=645) | REJECTED | below_safety_margin(31776587749514<68558667203723), p_lower_below_threshold(0.14<0.75) |
| 53299663 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 166.887928 USDC | 0.019728 USDC | 0.000000 USDC | 0.006723 USDC | 0.013005 USDC (0.0120 €) | — | 0.78 | 0.145 (n=645) | REJECTED | below_safety_margin(13005<33377), p_lower_below_threshold(0.14<0.75) |
| 53299663 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.001844 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0119 €) | — | 0.92 | 0.145 (n=645) | REJECTED | below_safety_margin(17<36), p_lower_below_threshold(0.14<0.75) |
| 53299663 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.081701 WETH | 0.000009 WETH | 0.000000 WETH | 0.000003 WETH | 0.000006 WETH (0.0117 €) | — | 0.70 | 0.145 (n=645) | REJECTED | below_safety_margin(5702577909032<16340267270861), p_lower_below_threshold(0.14<0.75) |
| 53299393 | WETH→[uniswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.130434 WETH | 0.000007 WETH | 0.000000 WETH | 0.000003 WETH | 0.000004 WETH (0.0082 €) | — | 0.31 | 0.145 (n=645) | REJECTED | below_safety_margin(3985072136953<26086734346216), p_lower_below_threshold(0.14<0.75) |
| 53299394 | WETH→[uniswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.130434 WETH | 0.000007 WETH | 0.000000 WETH | 0.000003 WETH | 0.000004 WETH (0.0082 €) | — | 0.31 | 0.145 (n=645) | REJECTED | below_safety_margin(3985072136953<26086734346216), p_lower_below_threshold(0.14<0.75) |
| 53299393 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→cbBTC | 0.003172 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0077 €) | — | 0.35 | 0.145 (n=645) | REJECTED | below_safety_margin(11<63), p_lower_below_threshold(0.14<0.75) |
| 53299394 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→cbBTC | 0.003172 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0077 €) | — | 0.35 | 0.145 (n=645) | REJECTED | below_safety_margin(11<63), p_lower_below_threshold(0.14<0.75) |
| 53299393 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 356.710534 USDC | 0.015540 USDC | 0.000000 USDC | 0.007302 USDC | 0.008238 USDC (0.0076 €) | — | 0.23 | 0.145 (n=645) | REJECTED | below_safety_margin(8238<71342), p_lower_below_threshold(0.14<0.75) |
| 53299394 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 356.710534 USDC | 0.015540 USDC | 0.000000 USDC | 0.007302 USDC | 0.008238 USDC (0.0076 €) | — | 0.23 | 0.145 (n=645) | REJECTED | below_safety_margin(8238<71342), p_lower_below_threshold(0.14<0.75) |
| 53299509 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 23.309646 USDC | 0.013088 USDC | 0.000000 USDC | 0.005032 USDC | 0.008056 USDC (0.0074 €) | — | 3.46 | 0.020 (n=178) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.02<0.75) |
| 53299663 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 83.628692 USDC | 0.012884 USDC | 0.000000 USDC | 0.006723 USDC | 0.006161 USDC (0.0057 €) | — | 0.74 | 0.145 (n=645) | REJECTED | below_safety_margin(6161<16725), p_lower_below_threshold(0.14<0.75) |
| 53299663 | WETH→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.044019 WETH | 0.000006 WETH | 0.000000 WETH | 0.000003 WETH | 0.000003 WETH (0.0056 €) | — | 0.63 | 0.145 (n=645) | REJECTED | below_safety_margin(2755927718276<8803759509460), p_lower_below_threshold(0.14<0.75) |
| 53299663 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→cbBTC | 0.001284 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0056 €) | — | 0.62 | 0.145 (n=645) | REJECTED | below_safety_margin(8<25), p_lower_below_threshold(0.14<0.75) |
| 53299744 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.002880 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0042 €) | — | 0.21 | 0.001 (n=15) | REJECTED | below_safety_margin(6<57), reliability_not_demonstrated |
| 53299744 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 228.350280 USDC | 0.011131 USDC | 0.000000 USDC | 0.006718 USDC | 0.004413 USDC (0.0041 €) | — | 0.19 | 0.001 (n=15) | REJECTED | below_safety_margin(4413<45670), reliability_not_demonstrated |
| 53299744 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.105217 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0038 €) | — | 0.18 | 0.001 (n=15) | REJECTED | below_safety_margin(1875265269468<21043418541340), reliability_not_demonstrated |
| 53299393 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→cbBTC | 0.002865 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0035 €) | — | 0.17 | 0.145 (n=645) | REJECTED | below_safety_margin(5<57), p_lower_below_threshold(0.14<0.75) |
| 53299394 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→cbBTC | 0.002865 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0035 €) | — | 0.17 | 0.145 (n=645) | REJECTED | below_safety_margin(5<57), p_lower_below_threshold(0.14<0.75) |
| 53299744 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC | 0.002880 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0035 €) | — | 0.17 | 0.145 (n=645) | REJECTED | below_safety_margin(5<57), p_lower_below_threshold(0.14<0.75) |

## Fiabilité et décision
- Observations ghost : 3874 ; taux observé 0.130 ; borne inférieure crédible (0.9) 0.123 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 12.3% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
