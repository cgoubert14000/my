# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-23T14:00:42+00:00 ; durée 61.25 min ; blocs 52985506 → 52987345 (1780 vus)

## Connexion
- Requêtes RPC : 21946 ; erreurs : 3 ; latence p50/p95 : 311.0/1,383.6 ms
- Rafraîchissements d'état : 1780 ; âge des données au dernier bloc : 2.99 s ; changements de frais LP observés (pools à frais dynamiques) : 4496
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 32846 ; cycles déclenchés par événement : 1878 ; avance médiane sur le rafraîchissement multicall : 1,199 ms
- Gaz : base fee 0.015605 gwei ; prix ETH (pool le plus profond) : 2,407.49 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 544 pools, 316 jetons, 19376 routes
- Par DEX : uniswap_v3 137, aerodrome 221, aerodrome_slipstream 137, pancakeswap_v3 32, uniswap_v2 13, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 200 (rejetés 2) → 605 jetons ; pools candidats 3880 (énumérés 358, par paires 0), mesurés 546, sous le plancher de 10000.0 $ : 2 → gardés 544 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDC': 1.0, 'USDbC': 1.0, 'WETH': 2396.209038, 'AERO': 0.783075, 'cbBTC': 81657.338706}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 157,244,678 | 2,407.486382 | 52987346 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,539,750 | 0.029439 | 52987346 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 12,933,755 | 91.857137 | 52987346 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| aerodrome | USDC/AERO | 3000 | 10,693,702 | 1.323648 | 52987346 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,375,569 | 0.029405 | 52987346 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,880,177 | 0.000012 | 52987346 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 8,928,967 | 0.029396 | 52987346 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/USDC | 500 | 8,709,264 | 2,411.218968 | 52987346 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,189,901 | 0.001674 | 52987346 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 344 | 6,358,247 | 0.000012 | 52987346 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 564 | 5,567,414 | 2,410.513070 | 52987346 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,467,579 | 0.029442 | 52987346 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | USDC/cbBTC | 484 | 5,099,888 | 0.000012 | 52987346 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,558,711 | 2,410.443190 | 52987346 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,303,876 | 0.999613 | 52987346 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/USDC | 3000 | 4,290,225 | 2,408.358358 | 52987346 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome | WETH/KTA | 3000 | 4,014,035 | 34,084.188801 | 52987346 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | VIRTUAL/WETH | 10000 | 3,417,422 | 0.000275 | 52987346 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/USDT | 412 | 2,907,500 | 2,415.124360 | 52987346 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome_slipstream | WETH/VVV | 2703 | 2,570,623 | 91.854236 | 52987346 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,320,095 | 392.062623 | 52987346 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | WETH/FAI | 10000 | 2,225,887 | 1,186,015.808845 | 52987346 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome | WETH/AERO | 10000 | 2,078,704 | 3,173.245570 | 52987346 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,997,793 | 0.000000 | 52987346 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,924,125 | 0.000012 | 52987346 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v3 | XDP/USDC | 100 | 1,760,538 | 0.017709 | 52987346 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,755,127 | 0.000012 | 52987346 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | WETH/AERO | 3000 | 1,586,513 | 3,194.351568 | 52987346 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,556,034 | 1.605482 | 52987346 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,458,140 | 0.823916 | 52987346 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,423,363 | 13,319.328940 | 52987346 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,389,807 | 0.005029 | 52987346 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome | WETH/msETH (stable) | 500 | 1,303,469 | 2.317628 | 52987346 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,301,787 | 0.000276 | 52987346 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,287,271 | 2,411.326310 | 52987346 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | DRB/WETH | 10000 | 1,268,260 | 0.000000 | 52987346 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | USDC/SEND | 3000 | 1,228,398 | 64.396809 | 52987346 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,186,646 | 36,379,202.579772 | 52987346 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,171,197 | 16.283376 | 52987346 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | WETH/WELL | 10000 | 1,166,279 | 1,123,351.691850 | 52987346 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,161,839 | 483,175.493584 | 52987346 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | USDC/NOCK | 3000 | 1,139,475 | 48.253232 | 52987346 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome | WETH/EDEL | 7000 | 1,096,498 | 74,220.206578 | 52987346 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | USDC/VVV | 3000 | 1,092,579 | 0.038088 | 52987346 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,080,532 | 20,901,603.416754 | 52987346 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,054,178 | 16.377988 | 52987346 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,014,228 | 23.075735 | 52987346 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| uniswap_v3 | WETH/MORPHO | 3000 | 961,965 | 1,054.443016 | 52987346 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/USDC | 10000 | 940,386 | 2,390.809061 | 52987346 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | uXRP/WETH | 3000 | 918,593 | 0.000546 | 52987346 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 915,718 | 0.000009 | 52987346 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 888,797 | 17.601678 | 52987346 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v2 | WETH/USDC | 3000 | 860,521 | 2,406.783631 | 52987346 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome | weETH_04c0/WETH | 500 | 839,381 | 1.105789 | 52987346 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome | WETH/wstETH | 3000 | 815,608 | 0.803225 | 52987346 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| pancakeswap_v3 | QUID/USDC | 100 | 804,144 | 0.058073 | 52987346 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 780,652 | 0.665211 | 52987346 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 780,561 | 4,488,634.474834 | 52987346 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v2 | WETH/NPC | 3000 | 737,498 | 134,019.952199 | 52987346 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| uniswap_v3 | TIG/USDC | 10000 | 732,979 | 0.673394 | 52987346 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |

## Recherche d'opportunités
- Cycles : 3657 ; routes examinées : 70858032 ; candidats optimisés : 329699 ; net attendu > 0 : 105 ; dernier cycle 938.2 ms
- Rejets (moteur) : {'spread_below_threshold': 69636617, 'liquidity_below_min': 886472, 'negative_expected_net': 329594, 'borrow_bound_too_small': 3657, 'cycle_budget_exhausted': 1587}
- Enregistrements de la session : 329699 ; net attendu > 0 : 105 ; simulés (eth_call de la vraie tx) : 8 (ok 0, échec 8) ; étiquettes ghost N+1 : 3/8 positives
- Décisions : {'REJECTED': 329699} ; motifs de rejet : {'below_safety_margin': 53, 'negative_expected_net': 329594, 'p_lower_below_threshold': 97, 'price_impact': 1, 'reliability_not_demonstrated': 8, 'simulation_failed': 8}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52986138 | WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→WETH | 0.047521 WETH | 0.000034 WETH | 0.000000 WETH | 0.000002 WETH | 0.000032 WETH (0.0703 €) | — | 6.71 | 0.067 (n=32) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.07<0.75) |
| 52986138 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC | 109.931222 USDC | 0.076766 USDC | 0.000000 USDC | 0.007947 USDC | 0.068819 USDC (0.0633 €) | — | 6.26 | 0.105 (n=204) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 52986138 | WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.045801 WETH | 0.000032 WETH | 0.000000 WETH | 0.000003 WETH | 0.000029 WETH (0.0633 €) | — | 6.26 | 0.105 (n=204) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.10<0.75) |
| 52986138 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC | 107.309726 USDC | 0.075479 USDC | 0.000000 USDC | 0.007947 USDC | 0.067532 USDC (0.0621 €) | — | 6.29 | 0.131 (n=103) | REJECTED | p_lower_below_threshold(0.13<0.75) |
| 52986138 | WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.044833 WETH | 0.000031 WETH | 0.000000 WETH | 0.000003 WETH | 0.000028 WETH (0.0621 €) | — | 6.28 | 0.131 (n=103) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.13<0.75) |
| 52986138 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC | 106.461541 USDC | 0.071195 USDC | 0.000000 USDC | 0.007583 USDC | 0.063612 USDC (0.0585 €) | — | 5.98 | 0.131 (n=103) | REJECTED | p_lower_below_threshold(0.13<0.75) |
| 52986138 | WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.044559 WETH | 0.000030 WETH | 0.000000 WETH | 0.000003 WETH | 0.000027 WETH (0.0585 €) | — | 5.95 | 0.131 (n=103) | REJECTED | p_lower_below_threshold(0.13<0.75) |
| 52986138 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC | 106.438680 USDC | 0.071096 USDC | 0.000000 USDC | 0.007583 USDC | 0.063513 USDC (0.0584 €) | — | 5.97 | 0.105 (n=204) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 52986138 | WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.044374 WETH | 0.000030 WETH | 0.000000 WETH | 0.000003 WETH | 0.000026 WETH (0.0584 €) | — | 5.97 | 0.105 (n=204) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 52986006 | WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→wstETH→[uniswap_v3]→WETH | 0.046809 WETH | 0.000029 WETH | 0.000000 WETH | 0.000003 WETH | 0.000026 WETH (0.0569 €) | — | 5.51 | 0.097 (n=202) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.10<0.75) |
| 52986138 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDT→[uniswap_v3]→USDC | 103.097243 USDC | 0.067436 USDC | 0.000000 USDC | 0.007947 USDC | 0.059489 USDC (0.0547 €) | — | 5.77 | 0.105 (n=204) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 52986138 | WETH→[uniswap_v3]→USDT→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.043104 WETH | 0.000028 WETH | 0.000000 WETH | 0.000003 WETH | 0.000025 WETH (0.0547 €) | — | 5.75 | 0.105 (n=204) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 52986138 | USDC→[sushiswap_v3]→WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC | 88.191515 USDC | 0.066371 USDC | 0.000000 USDC | 0.007947 USDC | 0.058424 USDC (0.0538 €) | — | 6.62 | 0.131 (n=103) | REJECTED | p_lower_below_threshold(0.13<0.75) |
| 52986138 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→USDT→[uniswap_v3]→USDC | 100.572079 USDC | 0.066352 USDC | 0.000000 USDC | 0.007947 USDC | 0.058405 USDC (0.0537 €) | — | 5.81 | 0.131 (n=103) | REJECTED | p_lower_below_threshold(0.13<0.75) |
| 52986138 | WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC→[sushiswap_v3]→WETH | 0.036750 WETH | 0.000028 WETH | 0.000000 WETH | 0.000003 WETH | 0.000024 WETH (0.0537 €) | — | 6.63 | 0.131 (n=103) | REJECTED | p_lower_below_threshold(0.13<0.75) |
| 52986138 | WETH→[uniswap_v3]→USDT→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.042043 WETH | 0.000028 WETH | 0.000000 WETH | 0.000003 WETH | 0.000024 WETH (0.0537 €) | — | 5.79 | 0.131 (n=103) | REJECTED | p_lower_below_threshold(0.13<0.75) |
| 52986006 | WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→wstETH→[aerodrome_slipstream]→WETH | 0.045023 WETH | 0.000027 WETH | 0.000000 WETH | 0.000003 WETH | 0.000024 WETH (0.0521 €) | — | 5.25 | 0.097 (n=202) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.10<0.75) |
| 52986138 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→USDT→[uniswap_v3]→USDC | 99.849880 USDC | 0.062150 USDC | 0.000000 USDC | 0.007583 USDC | 0.054567 USDC (0.0502 €) | — | 5.46 | 0.131 (n=103) | REJECTED | p_lower_below_threshold(0.13<0.75) |
| 52986138 | WETH→[uniswap_v3]→USDT→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.041660 WETH | 0.000026 WETH | 0.000000 WETH | 0.000003 WETH | 0.000023 WETH (0.0501 €) | — | 5.46 | 0.131 (n=103) | REJECTED | p_lower_below_threshold(0.13<0.75) |
| 52986138 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDT→[uniswap_v3]→USDC | 99.168224 USDC | 0.062066 USDC | 0.000000 USDC | 0.007583 USDC | 0.054483 USDC (0.0501 €) | — | 5.49 | 0.105 (n=204) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 52986138 | WETH→[uniswap_v3]→USDT→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.041660 WETH | 0.000026 WETH | 0.000000 WETH | 0.000003 WETH | 0.000023 WETH (0.0501 €) | — | 5.45 | 0.105 (n=204) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 52986138 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDT→[pancakeswap_v3]→USDC | 97.643360 USDC | 0.059929 USDC | 0.000000 USDC | 0.007947 USDC | 0.051982 USDC (0.0478 €) | — | 5.32 | 0.105 (n=204) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 52986138 | WETH→[uniswap_v3]→USDT→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.040666 WETH | 0.000025 WETH | 0.000000 WETH | 0.000003 WETH | 0.000022 WETH (0.0478 €) | — | 5.33 | 0.105 (n=204) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 52986138 | USDC→[sushiswap_v3]→WETH→[uniswap_v3]→USDT→[uniswap_v3]→USDC | 82.828475 USDC | 0.058870 USDC | 0.000000 USDC | 0.007583 USDC | 0.051287 USDC (0.0472 €) | — | 6.19 | 0.131 (n=103) | REJECTED | p_lower_below_threshold(0.13<0.75) |
| 52986138 | WETH→[uniswap_v3]→USDT→[uniswap_v3]→USDC→[sushiswap_v3]→WETH | 0.034693 WETH | 0.000025 WETH | 0.000000 WETH | 0.000003 WETH | 0.000021 WETH (0.0471 €) | — | 6.16 | 0.131 (n=103) | REJECTED | p_lower_below_threshold(0.13<0.75) |

## Fiabilité et décision
- Observations ghost : 1992 ; taux observé 0.097 ; borne inférieure crédible (0.9) 0.089 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 8.9% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
