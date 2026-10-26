# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-26T13:40:40+00:00 ; durée 303.16 min ; blocs 53107248 → 53116341 (8795 vus)

## Connexion
- Requêtes RPC : 103223 ; erreurs : 85 ; latence p50/p95 : 399.1/1,626.0 ms
- Rafraîchissements d'état : 8795 ; âge des données au dernier bloc : 6.36 s ; changements de frais LP observés (pools à frais dynamiques) : 16284
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 20005 ; cycles déclenchés par événement : 1392 ; avance médiane sur le rafraîchissement multicall : 466 ms
- Gaz : base fee 0.006088 gwei ; prix ETH (pool le plus profond) : 2,310.42 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 527 pools, 302 jetons, 19574 routes
- Par DEX : uniswap_v3 142, aerodrome 213, aerodrome_slipstream 127, pancakeswap_v3 30, uniswap_v2 12, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 188 (rejetés 2) → 593 jetons ; pools candidats 3779 (énumérés 339, par paires 0), mesurés 529, sous le plancher de 10000.0 $ : 2 → gardés 527 (max 1500) ; prix des hubs : {'USDC': 1.0, 'DAI': 1.0, 'USDbC': 1.0, 'WETH': 2317.899718, 'cbBTC': 80102.759686, 'AERO': 0.672129}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 157,485,670 | 2,310.423899 | 53116342 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,667,805 | 0.028970 | 53116342 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,127,479 | 0.028978 | 53116342 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,455,947 | 0.000013 | 53116342 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome | WETH/VVV | 3000 | 8,794,529 | 93.376077 | 53116342 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/USDC | 500 | 8,286,335 | 2,310.450398 | 53116342 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | USDC/AERO | 3000 | 7,147,754 | 1.488014 | 53116342 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,974,887 | 0.001656 | 53116342 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | WETH/USDC | 713 | 5,369,611 | 2,309.571627 | 53116342 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,335,419 | 0.028974 | 53116342 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,441,949 | 2,309.553942 | 53116342 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,197,138 | 0.999621 | 53116342 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,787,495 | 34,830.967179 | 53116342 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/USDC | 3000 | 3,738,665 | 2,310.204989 | 53116342 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 3,199,381 | 0.028968 | 53116342 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2883 | 2,487,629 | 93.366236 | 53116342 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | USDC/cbBTC | 532 | 2,470,347 | 0.000013 | 53116342 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,198,263 | 404.001463 | 53116342 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | WETH/FAI | 10000 | 2,114,664 | 1,210,234.968788 | 53116342 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,883,174 | 0.000013 | 53116342 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,880,163 | 0.000000 | 53116342 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,816,826 | 0.018456 | 53116342 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,709,360 | 0.000013 | 53116342 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | USDC/cbBTC | 348 | 1,693,712 | 0.000013 | 53116342 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | VIRTUAL/WETH | 10000 | 1,547,821 | 0.000265 | 53116342 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,499,718 | 0.005856 | 53116342 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,457,945 | 0.826460 | 53116342 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,453,220 | 1.698035 | 53116342 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | WETH/AERO | 3000 | 1,417,273 | 3,432.999148 | 53116342 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,365,195 | 13,957.847124 | 53116342 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/AERO | 10000 | 1,229,952 | 3,440.523125 | 53116342 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,227,592 | 0.000266 | 53116342 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | USDC/SEND | 3000 | 1,221,567 | 65.118993 | 53116342 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,208,800 | 2,310.295083 | 53116342 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | DRB/WETH | 10000 | 1,163,703 | 0.000000 | 53116342 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | WETH/WELL | 10000 | 1,132,355 | 1,092,272.815641 | 53116342 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/doginme | 10000 | 1,125,131 | 37,839,432.755685 | 53116342 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,101,708 | 499,334.501245 | 53116342 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,065,140 | 20,057,394.338751 | 53116342 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome | WETH/EDEL | 7000 | 1,064,544 | 72,184.113152 | 53116342 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | USDC/NOCK | 3000 | 1,055,325 | 56.240311 | 53116342 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,030,099 | 17.436232 | 53116342 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | USDC/VVV | 3000 | 969,978 | 0.040331 | 53116342 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/USDC | 10000 | 920,965 | 2,312.267761 | 53116342 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome | WETH/msETH (stable) | 500 | 903,300 | 2.308512 | 53116342 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | uXRP/WETH | 3000 | 888,430 | 0.000554 | 53116342 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | USDC/SAPIEN | 4595 | 879,457 | 17.955801 | 53116342 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 877,456 | 17.063383 | 53116342 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| uniswap_v3 | WETH/MORPHO | 3000 | 877,171 | 1,142.044301 | 53116342 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/VVV | 10000 | 865,076 | 94.031548 | 53116342 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v2 | WETH/USDC | 3000 | 843,068 | 2,309.828642 | 53116342 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 795,431 | 0.000008 | 53116342 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| pancakeswap_v3 | QUID/USDC | 100 | 792,616 | 0.056297 | 53116342 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 782,270 | 0.803142 | 53116342 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 741,814 | 0.617394 | 53116342 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 727,753 | 4,758,065.395551 | 53116342 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v2 | WETH/NPC | 3000 | 701,195 | 136,653.871746 | 53116342 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| uniswap_v3 | TIG/USDC | 10000 | 699,763 | 0.615992 | 53116342 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | WETH/BRETT | 2171 | 688,317 | 495,465.743454 | 53116342 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 678,415 | 0.110017 | 53116342 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |

## Recherche d'opportunités
- Cycles : 10186 ; routes examinées : 199380764 ; candidats optimisés : 583773 ; net attendu > 0 : 327 ; dernier cycle 355.8 ms
- Rejets (moteur) : {'spread_below_threshold': 196105149, 'liquidity_below_min': 2475795, 'negative_expected_net': 583446, 'unquotable': 204798, 'borrow_bound_too_small': 10174, 'cycle_budget_exhausted': 1075}
- Enregistrements de la session : 583773 ; net attendu > 0 : 327 ; simulés (eth_call de la vraie tx) : 15 (ok 11, échec 4) ; étiquettes ghost N+1 : 0/12 positives
- Décisions : {'REJECTED': 583773} ; motifs de rejet : {'below_safety_margin': 234, 'negative_expected_net': 583446, 'p_lower_below_threshold': 301, 'price_impact': 1, 'reliability_not_demonstrated': 26, 'simulation_failed': 4, 'stale_data': 14}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53116285 | WETH→[uniswap_v3]→wstETH→[aerodrome_slipstream]→AERO→[pancakeswap_v3]→WETH | 0.145963 WETH | 0.000374 WETH | 0.000000 WETH | 0.000004 WETH | 0.000370 WETH (0.7870 €) | 0.000370 WETH | 25.38 | 0.000 (n=22) | REJECTED | reliability_not_demonstrated |
| 53116285 | WETH→[aerodrome_slipstream]→wstETH→[aerodrome_slipstream]→AERO→[pancakeswap_v3]→WETH | 0.137659 WETH | 0.000351 WETH | 0.000000 WETH | 0.000004 WETH | 0.000347 WETH (0.7379 €) | 0.000347 WETH | 25.23 | 0.000 (n=22) | REJECTED | reliability_not_demonstrated |
| 53116285 | USDC→[uniswap_v3]→cbBTC→[uniswap_v3]→AERO→[uniswap_v3]→USDC | 238.211126 USDC | 0.451470 USDC | 0.000000 USDC | 0.008291 USDC | 0.443179 USDC (0.4077 €) | — | 18.60 | 0.000 (n=50) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53116285 | cbBTC→[uniswap_v3]→AERO→[uniswap_v3]→USDC→[uniswap_v3]→cbBTC | 0.002951 cbBTC | 0.000006 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000006 cbBTC (0.4063 €) | — | 18.77 | 0.000 (n=50) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53116285 | USDC→[aerodrome_slipstream]→cbBTC→[uniswap_v3]→AERO→[uniswap_v3]→USDC | 246.127642 USDC | 0.444785 USDC | 0.000000 USDC | 0.008291 USDC | 0.436494 USDC (0.4016 €) | — | 17.73 | 0.000 (n=50) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53116285 | cbBTC→[uniswap_v3]→AERO→[uniswap_v3]→USDC→[aerodrome_slipstream]→cbBTC | 0.002938 cbBTC | 0.000006 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000005 cbBTC (0.4004 €) | — | 18.59 | 0.000 (n=50) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53116285 | USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→AERO→[uniswap_v3]→USDC | 238.193084 USDC | 0.442249 USDC | 0.000000 USDC | 0.008291 USDC | 0.433958 USDC (0.3992 €) | — | 18.22 | 0.000 (n=50) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53116285 | USDC→[uniswap_v3]→cbBTC→[uniswap_v3]→AERO→[uniswap_v3]→USDC | 245.086905 USDC | 0.441624 USDC | 0.000000 USDC | 0.008291 USDC | 0.433333 USDC (0.3987 €) | — | 17.68 | 0.000 (n=50) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53116285 | cbBTC→[uniswap_v3]→AERO→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.002894 cbBTC | 0.000006 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000005 cbBTC (0.3975 €) | — | 18.73 | 0.000 (n=50) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53116285 | cbBTC→[uniswap_v3]→AERO→[uniswap_v3]→USDC→[uniswap_v3]→cbBTC | 0.002951 cbBTC | 0.000006 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000005 cbBTC (0.3975 €) | — | 18.37 | 0.000 (n=50) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53116285 | USDC→[aerodrome_slipstream]→cbBTC→[uniswap_v3]→AERO→[uniswap_v3]→USDC | 227.845023 USDC | 0.408657 USDC | 0.000000 USDC | 0.008291 USDC | 0.400366 USDC (0.3683 €) | — | 17.57 | 0.000 (n=50) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53116285 | cbBTC→[uniswap_v3]→AERO→[uniswap_v3]→USDC→[aerodrome_slipstream]→cbBTC | 0.002749 cbBTC | 0.000005 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000005 cbBTC (0.3667 €) | — | 18.19 | 0.000 (n=50) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53116285 | USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→AERO→[uniswap_v3]→USDC | 213.999081 USDC | 0.404490 USDC | 0.000000 USDC | 0.008707 USDC | 0.395783 USDC (0.3641 €) | — | 18.49 | 0.000 (n=50) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53116285 | cbBTC→[uniswap_v3]→AERO→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.002618 cbBTC | 0.000005 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000005 cbBTC (0.3630 €) | — | 18.91 | 0.000 (n=50) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53116285 | WETH→[aerodrome]→wstETH→[aerodrome_slipstream]→AERO→[pancakeswap_v3]→WETH | 0.064503 WETH | 0.000132 WETH | 0.000000 WETH | 0.000003 WETH | 0.000129 WETH (0.2737 €) | 0.000129 WETH | 19.97 | 0.039 (n=21) | REJECTED | reliability_not_demonstrated |
| 53116285 | WETH→[uniswap_v3]→wstETH→[aerodrome]→AERO→[pancakeswap_v3]→WETH | 0.053301 WETH | 0.000123 WETH | 0.000000 WETH | 0.000003 WETH | 0.000120 WETH (0.2544 €) | — | 22.47 | 0.001 (n=10) | REJECTED | reliability_not_demonstrated |
| 53116285 | WETH→[aerodrome_slipstream]→wstETH→[aerodrome]→AERO→[pancakeswap_v3]→WETH | 0.051721 WETH | 0.000117 WETH | 0.000000 WETH | 0.000003 WETH | 0.000114 WETH (0.2420 €) | — | 22.02 | 0.001 (n=10) | REJECTED | reliability_not_demonstrated |
| 53116285 | WETH→[pancakeswap_v3]→cbBTC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH | 0.082709 WETH | 0.000112 WETH | 0.000000 WETH | 0.000004 WETH | 0.000108 WETH (0.2304 €) | — | 13.12 | 0.000 (n=50) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53116285 | cbBTC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.002424 cbBTC | 0.000003 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000003 cbBTC (0.2303 €) | — | 12.95 | 0.000 (n=50) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53116285 | WETH→[aerodrome_slipstream]→cbBTC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH | 0.073288 WETH | 0.000096 WETH | 0.000000 WETH | 0.000004 WETH | 0.000092 WETH (0.1960 €) | — | 12.59 | 0.000 (n=50) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53116285 | cbBTC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→cbBTC | 0.002115 cbBTC | 0.000003 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000003 cbBTC (0.1958 €) | — | 12.63 | 0.000 (n=50) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53116285 | cbBTC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.002045 cbBTC | 0.000003 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1767 €) | — | 11.79 | 0.000 (n=50) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53116285 | WETH→[pancakeswap_v3]→cbBTC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH | 0.073175 WETH | 0.000087 WETH | 0.000000 WETH | 0.000004 WETH | 0.000083 WETH (0.1767 €) | — | 11.36 | 0.000 (n=50) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53116285 | WETH→[uniswap_v3]→cbBTC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH | 0.070000 WETH | 0.000082 WETH | 0.000000 WETH | 0.000004 WETH | 0.000078 WETH (0.1667 €) | — | 11.21 | 0.000 (n=50) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53116285 | cbBTC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH→[uniswap_v3]→cbBTC | 0.001989 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1665 €) | — | 11.41 | 0.000 (n=50) | REJECTED | p_lower_below_threshold(0.00<0.75) |

## Fiabilité et décision
- Observations ghost : 2619 ; taux observé 0.094 ; borne inférieure crédible (0.9) 0.087 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 8.7% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
