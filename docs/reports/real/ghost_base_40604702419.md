# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-28T03:29:49+00:00 ; durée 215.95 min ; blocs 53177940 → 53184419 (6454 vus)

## Connexion
- Requêtes RPC : 74111 ; erreurs : 70 ; latence p50/p95 : 73.2/979.8 ms
- Rafraîchissements d'état : 6455 ; âge des données au dernier bloc : 1.23 s ; changements de frais LP observés (pools à frais dynamiques) : 6992
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 9885 ; cycles déclenchés par événement : 1231 ; avance médiane sur le rafraîchissement multicall : 399 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,358.78 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 524 pools, 303 jetons, 19128 routes
- Par DEX : uniswap_v3 147, aerodrome 211, aerodrome_slipstream 123, pancakeswap_v3 28, uniswap_v2 12, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 185 (rejetés 2) → 590 jetons ; pools candidats 3771 (énumérés 333, par paires 0), mesurés 526, sous le plancher de 10000.0 $ : 2 → gardés 524 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2351.399953, 'cbBTC': 80864.599929, 'AERO': 0.698092}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 158,249,740 | 2,358.777627 | 53184419 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,694,253 | 0.029131 | 53184419 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,646,391 | 0.000012 | 53184419 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,502,162 | 0.029105 | 53184419 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| aerodrome | WETH/VVV | 3000 | 8,520,335 | 93.051737 | 53184419 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/USDC | 500 | 8,438,989 | 2,359.291796 | 53184419 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,055,643 | 0.001644 | 53184419 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 6,950,193 | 1.425396 | 53184419 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,748,892 | 0.029141 | 53184419 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/USDC | 624 | 5,075,406 | 2,359.343339 | 53184419 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,480,137 | 2,359.237010 | 53184419 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,263,505 | 0.998869 | 53184419 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,778,725 | 36,472.866645 | 53184419 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,968,564 | 0.029118 | 53184419 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2748 | 2,565,316 | 93.070256 | 53184419 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | USDC/cbBTC | 460 | 2,450,759 | 0.000012 | 53184419 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome | WETH/USDC | 3000 | 2,371,239 | 2,361.114720 | 53184419 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome | WETH/FAI | 10000 | 2,153,693 | 1,216,117.694104 | 53184419 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | XDP/USDC | 100 | 1,844,461 | 0.018981 | 53184419 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,834,282 | 0.000000 | 53184419 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,798,602 | 397.856452 | 53184419 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | USDC/cbBTC | 344 | 1,700,136 | 0.000012 | 53184419 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,693,299 | 0.000012 | 53184419 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,688,576 | 0.000012 | 53184419 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,530,979 | 0.005853 | 53184419 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,474,280 | 1.658893 | 53184419 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | WETH/AERO | 3000 | 1,464,762 | 3,359.631315 | 53184419 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,461,656 | 0.826410 | 53184419 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,397,634 | 13,666.962829 | 53184419 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,262,751 | 0.000269 | 53184419 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,246,360 | 2,358.976853 | 53184419 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | WETH/AERO | 10000 | 1,211,413 | 3,357.634058 | 53184419 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | USDC/SEND | 3000 | 1,194,235 | 68.133836 | 53184419 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome | VIRTUAL/WETH | 10000 | 1,193,694 | 0.000267 | 53184419 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | WETH/doginme | 10000 | 1,169,358 | 36,016,354.554572 | 53184419 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | WETH/WELL | 10000 | 1,169,334 | 1,067,021.369279 | 53184419 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | DRB/WETH | 10000 | 1,133,650 | 0.000000 | 53184419 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,131,220 | 498,236.826218 | 53184419 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | WETH/EDEL | 7000 | 1,084,882 | 72,227.811135 | 53184419 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | USDC/NOCK | 3000 | 1,056,663 | 56.065854 | 53184419 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,056,338 | 21,125,285.664000 | 53184419 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,051,753 | 16.484868 | 53184419 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | USDC/VVV | 3000 | 1,023,434 | 0.039441 | 53184419 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/VVV | 10000 | 1,015,878 | 92.395325 | 53184419 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/USDC | 10000 | 946,011 | 2,342.370703 | 53184419 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 933,706 | 1,062.737859 | 53184419 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | uXRP/WETH | 3000 | 914,630 | 0.000564 | 53184419 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome | WETH/msETH (stable) | 500 | 890,684 | 2.313211 | 53184419 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 884,121 | 17.810644 | 53184419 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 852,733 | 17.456523 | 53184419 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| uniswap_v2 | WETH/USDC | 3000 | 851,355 | 2,358.975062 | 53184419 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome | WETH/wstETH | 3000 | 798,622 | 0.803180 | 53184419 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| pancakeswap_v3 | QUID/USDC | 100 | 795,082 | 0.056662 | 53184419 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome_slipstream | AERO/cbBTC | 2700 | 760,009 | 0.000009 | 53184419 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 757,221 | 0.633831 | 53184419 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 756,146 | 4,594,072.812787 | 53184419 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v2 | WETH/NPC | 3000 | 714,585 | 137,188.831576 | 53184419 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 702,707 | 500,413.240395 | 53184419 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | TIG/USDC | 10000 | 685,255 | 0.591081 | 53184419 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 674,309 | 0.108796 | 53184419 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |

## Recherche d'opportunités
- Cycles : 7685 ; routes examinées : 146998680 ; candidats optimisés : 381360 ; net attendu > 0 : 112 ; dernier cycle 95.6 ms
- Rejets (moteur) : {'spread_below_threshold': 144528924, 'liquidity_below_min': 1930991, 'negative_expected_net': 381248, 'borrow_bound_too_small': 156883, 'cycle_budget_exhausted': 370, 'unquotable': 152}
- Enregistrements de la session : 381360 ; net attendu > 0 : 112 ; simulés (eth_call de la vraie tx) : 10 (ok 10, échec 0) ; étiquettes ghost N+1 : 4/10 positives
- Décisions : {'REJECTED': 381360} ; motifs de rejet : {'below_safety_margin': 84, 'negative_expected_net': 381248, 'p_lower_below_threshold': 93, 'reliability_not_demonstrated': 19}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53182278 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.007259 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0699 €) | — | 1.29 | 0.003 (n=2) | REJECTED | below_safety_margin(94<145), reliability_not_demonstrated |
| 53182278 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.250456 WETH | 0.000034 WETH | 0.000000 WETH | 0.000002 WETH | 0.000032 WETH (0.0693 €) | — | 1.28 | 0.003 (n=2) | REJECTED | below_safety_margin(31960218814645<50091270569155), reliability_not_demonstrated |
| 53182278 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 1,017.145501 USDC | 0.059728 USDC | 0.000000 USDC | 0.005654 USDC | 0.054074 USDC (0.0497 €) | — | 0.53 | 0.020 (n=106) | REJECTED | below_safety_margin(54074<203429), p_lower_below_threshold(0.02<0.75) |
| 53182278 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.430558 WETH | 0.000025 WETH | 0.000000 WETH | 0.000002 WETH | 0.000023 WETH (0.0497 €) | — | 0.53 | 0.020 (n=106) | REJECTED | below_safety_margin(22887495811158<86111678777983), p_lower_below_threshold(0.02<0.75) |
| 53182278 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 379.948769 USDC | 0.054366 USDC | 0.000000 USDC | 0.005296 USDC | 0.049070 USDC (0.0451 €) | — | 1.29 | 0.013 (n=22) | REJECTED | below_safety_margin(49070<75989), reliability_not_demonstrated |
| 53182278 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.161137 WETH | 0.000023 WETH | 0.000000 WETH | 0.000002 WETH | 0.000021 WETH (0.0451 €) | — | 1.29 | 0.013 (n=22) | REJECTED | below_safety_margin(20768798052170<32227400529091), reliability_not_demonstrated |
| 53182278 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.004453 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0417 €) | — | 1.26 | 0.126 (n=394) | REJECTED | below_safety_margin(56<89), p_lower_below_threshold(0.13<0.75) |
| 53182278 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 372.148176 USDC | 0.052030 USDC | 0.000000 USDC | 0.007088 USDC | 0.044942 USDC (0.0413 €) | — | 1.21 | 0.126 (n=394) | REJECTED | below_safety_margin(44942<74429), p_lower_below_threshold(0.13<0.75) |
| 53182278 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.142651 WETH | 0.000022 WETH | 0.000000 WETH | 0.000003 WETH | 0.000019 WETH (0.0411 €) | — | 1.33 | 0.126 (n=394) | REJECTED | below_safety_margin(18937297064803<28530173520111), p_lower_below_threshold(0.13<0.75) |
| 53182278 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→cbBTC | 0.002225 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0320 €) | — | 1.93 | 0.020 (n=106) | REJECTED | below_safety_margin(43<44), p_lower_below_threshold(0.02<0.75) |
| 53182278 | WETH→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.065000 WETH | 0.000017 WETH | 0.000000 WETH | 0.000002 WETH | 0.000015 WETH (0.0319 €) | 0.000015 WETH | 2.26 | 0.020 (n=106) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 53182278 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 607.506229 USDC | 0.039539 USDC | 0.000000 USDC | 0.007088 USDC | 0.032451 USDC (0.0299 €) | — | 0.53 | 0.001 (n=7) | REJECTED | below_safety_margin(32451<121501), reliability_not_demonstrated |
| 53182278 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.257216 WETH | 0.000017 WETH | 0.000000 WETH | 0.000003 WETH | 0.000014 WETH (0.0298 €) | — | 0.53 | 0.001 (n=7) | REJECTED | below_safety_margin(13718299728617<51443120143865), reliability_not_demonstrated |
| 53182278 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.007284 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0298 €) | — | 0.55 | 0.001 (n=7) | REJECTED | below_safety_margin(40<145), reliability_not_demonstrated |
| 53179140 | USDC→[aerodrome_slipstream]→EURC→[aerodrome_slipstream]→USDC | 566.811391 USDC | 0.037549 USDC | 0.000000 USDC | 0.005280 USDC | 0.032269 USDC (0.0297 €) | — | 0.57 | 0.013 (n=22) | REJECTED | below_safety_margin(32269<113362), reliability_not_demonstrated |
| 53182278 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→cbBTC | 0.001848 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0290 €) | — | 2.11 | 0.126 (n=394) | REJECTED | p_lower_below_threshold(0.13<0.75) |
| 53182278 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 153.026518 USDC | 0.038441 USDC | 0.000000 USDC | 0.007088 USDC | 0.031353 USDC (0.0288 €) | — | 2.05 | 0.126 (n=394) | REJECTED | p_lower_below_threshold(0.13<0.75) |
| 53182278 | WETH→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.065000 WETH | 0.000016 WETH | 0.000000 WETH | 0.000003 WETH | 0.000013 WETH (0.0288 €) | 0.000013 WETH | 2.05 | 0.126 (n=394) | REJECTED | p_lower_below_threshold(0.13<0.75) |
| 53182278 | USDC→[aerodrome_slipstream]→EURC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 87.730947 USDC | 0.031397 USDC | 0.000000 USDC | 0.007088 USDC | 0.024309 USDC (0.0224 €) | — | 2.77 | 0.126 (n=394) | REJECTED | p_lower_below_threshold(0.13<0.75) |
| 53182278 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→EURC→[pancakeswap_v3]→WETH | 0.037179 WETH | 0.000013 WETH | 0.000000 WETH | 0.000003 WETH | 0.000010 WETH (0.0223 €) | 0.000010 WETH | 2.77 | 0.126 (n=394) | REJECTED | p_lower_below_threshold(0.13<0.75) |
| 53182278 | USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 135.376426 USDC | 0.029034 USDC | 0.000000 USDC | 0.007088 USDC | 0.021946 USDC (0.0202 €) | — | 1.62 | 0.172 (n=198) | REJECTED | below_safety_margin(21946<27075), p_lower_below_threshold(0.17<0.75) |
| 53182278 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH | 0.057742 WETH | 0.000012 WETH | 0.000000 WETH | 0.000003 WETH | 0.000009 WETH (0.0201 €) | — | 1.61 | 0.172 (n=198) | REJECTED | below_safety_margin(9285396234323<11548447037638), p_lower_below_threshold(0.17<0.75) |
| 53182279 | USDC→[aerodrome_slipstream]→EURC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 83.993839 USDC | 0.029027 USDC | 0.000000 USDC | 0.007157 USDC | 0.021870 USDC (0.0201 €) | — | 2.60 | 0.125 (n=396) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 53182279 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→EURC→[pancakeswap_v3]→WETH | 0.035617 WETH | 0.000012 WETH | 0.000000 WETH | 0.000003 WETH | 0.000009 WETH (0.0200 €) | 0.000009 WETH | 2.59 | 0.125 (n=396) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 53182279 | USDC→[aerodrome_slipstream]→USD→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 39.254957 USDC | 0.028780 USDC | 0.000000 USDC | 0.007157 USDC | 0.021623 USDC (0.0199 €) | — | 5.51 | 0.094 (n=311) | REJECTED | p_lower_below_threshold(0.09<0.75) |

## Fiabilité et décision
- Observations ghost : 2888 ; taux observé 0.092 ; borne inférieure crédible (0.9) 0.085 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 8.5% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
