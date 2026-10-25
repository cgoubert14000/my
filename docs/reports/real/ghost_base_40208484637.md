# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-25T16:51:41+00:00 ; durée 61.48 min ; blocs 53077030 → 53078876 (1845 vus)

## Connexion
- Requêtes RPC : 23376 ; erreurs : 0 ; latence p50/p95 : 104.1/561.4 ms
- Rafraîchissements d'état : 1845 ; âge des données au dernier bloc : 2.69 s ; changements de frais LP observés (pools à frais dynamiques) : 2261
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 19945 ; cycles déclenchés par événement : 3041 ; avance médiane sur le rafraîchissement multicall : 241 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,340.84 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 531 pools, 306 jetons, 19476 routes
- Par DEX : uniswap_v3 142, aerodrome 215, aerodrome_slipstream 127, pancakeswap_v3 31, uniswap_v2 13, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 191 (rejetés 2) → 596 jetons ; pools candidats 3792 (énumérés 341, par paires 0), mesurés 533, sous le plancher de 10000.0 $ : 2 → gardés 531 (max 1500) ; prix des hubs : {'USDC': 1.0, 'USDbC': 1.0, 'DAI': 1.0, 'WETH': 2340.831442, 'cbBTC': 80585.156098, 'AERO': 0.694811}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 158,525,067 | 2,340.837522 | 53078875 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 17,490,297 | 0.029090 | 53078875 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,234,818 | 0.029036 | 53078875 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,569,127 | 0.000012 | 53078875 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome | WETH/VVV | 3000 | 8,902,790 | 93.735554 | 53078875 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/USDC | 500 | 8,439,027 | 2,343.116924 | 53078876 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | USDC/AERO | 3000 | 7,591,645 | 1.442813 | 53078875 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,011,503 | 0.001644 | 53078875 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | WETH/USDC | 624 | 5,492,274 | 2,343.937466 | 53078876 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,362,050 | 0.029100 | 53078875 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,437,396 | 2,344.110059 | 53078876 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,230,473 | 1.000001 | 53078875 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,825,182 | 35,052.963329 | 53078875 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/USDC | 3000 | 3,784,731 | 2,342.710295 | 53078875 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 3,228,987 | 0.029050 | 53078875 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | USDC/cbBTC | 436 | 2,789,294 | 0.000012 | 53078875 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome_slipstream | WETH/VVV | 2760 | 2,519,626 | 93.770327 | 53078875 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,219,262 | 410.364225 | 53078875 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | WETH/FAI | 10000 | 2,123,620 | 1,231,850.150958 | 53078875 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,905,407 | 0.000012 | 53078875 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,895,661 | 0.000000 | 53078875 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,779,790 | 0.017853 | 53078875 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,727,634 | 0.000012 | 53078875 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | USDC/cbBTC | 336 | 1,719,108 | 0.000012 | 53078875 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | VIRTUAL/WETH | 10000 | 1,569,826 | 0.000264 | 53078875 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,470,515 | 1.673913 | 53078875 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,458,631 | 0.826105 | 53078875 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,447,087 | 3,380.320528 | 53078875 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,424,581 | 0.005483 | 53078875 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,371,041 | 14,101.074902 | 53078875 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,285,856 | 2,343.174157 | 53078875 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | WETH/AERO | 10000 | 1,265,942 | 3,377.387910 | 53078875 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,242,574 | 0.000266 | 53078875 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | USDC/SEND | 3000 | 1,221,986 | 65.074320 | 53078875 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,166,161 | 35,443,569.697102 | 53078875 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | DRB/WETH | 10000 | 1,143,826 | 0.000000 | 53078875 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | WETH/WELL | 10000 | 1,127,563 | 1,130,768.148677 | 53078875 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,124,538 | 496,604.656724 | 53078875 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | USDC/NOCK | 3000 | 1,090,198 | 52.699716 | 53078875 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,042,538 | 16.875784 | 53078875 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | WETH/EDEL | 7000 | 1,033,336 | 78,641.973877 | 53078875 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,023,806 | 21,896,670.763972 | 53078875 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | USDC/VVV | 3000 | 973,155 | 0.040022 | 53078875 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/USDC | 10000 | 925,690 | 2,339.197561 | 53078875 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome | WETH/msETH (stable) | 500 | 918,089 | 2.310010 | 53078875 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | uXRP/WETH | 3000 | 897,827 | 0.000551 | 53078875 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| uniswap_v3 | WETH/MORPHO | 3000 | 894,836 | 1,122.241994 | 53078875 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 885,972 | 17.181327 | 53078875 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 878,931 | 17.965371 | 53078875 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v3 | WETH/VVV | 10000 | 875,458 | 93.571370 | 53078875 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v2 | WETH/USDC | 3000 | 848,506 | 2,341.766577 | 53078875 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | AERO/cbBTC | 2700 | 811,521 | 0.000009 | 53078875 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | WETH/wstETH | 3000 | 792,573 | 0.803130 | 53078875 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| pancakeswap_v3 | QUID/USDC | 100 | 789,612 | 0.055855 | 53078875 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | weETH_04c0/WETH | 500 | 782,572 | 1.105853 | 53078875 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 745,721 | 0.622584 | 53078875 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 740,976 | 4,710,909.432847 | 53078875 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 732,281 | 0.671774 | 53078875 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/NPC | 3000 | 711,806 | 136,092.169099 | 53078875 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 699,595 | 495,504.237541 | 53078875 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |

## Recherche d'opportunités
- Cycles : 4885 ; routes examinées : 95140260 ; candidats optimisés : 235666 ; net attendu > 0 : 408 ; dernier cycle 80.2 ms
- Rejets (moteur) : {'spread_below_threshold': 92958365, 'liquidity_below_min': 1576760, 'pool_quarantined': 266940, 'negative_expected_net': 235258, 'unquotable': 97644, 'borrow_bound_too_small': 4885}
- Enregistrements de la session : 235666 ; net attendu > 0 : 408 ; simulés (eth_call de la vraie tx) : 59 (ok 18, échec 41) ; étiquettes ghost N+1 : 0/47 positives
- Décisions : {'REJECTED': 235666} ; motifs de rejet : {'below_safety_margin': 116, 'negative_expected_net': 235258, 'p_lower_below_threshold': 293, 'price_impact': 4, 'reliability_not_demonstrated': 115, 'simulation_failed': 41}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53077286 | WETH→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.794869 WETH | 0.000746 WETH | 0.000000 WETH | 0.000003 WETH | 0.000743 WETH (1.5998 €) | — | 9.35 | 0.000 (n=46) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 53077286 | cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.023019 cbBTC | 0.000022 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000022 cbBTC (1.5995 €) | — | 9.38 | 0.000 (n=46) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53077845 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→cbBTC | 0.001782 cbBTC | 0.000016 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000016 cbBTC (1.1949 €) | — | 90.63 | 0.000 (n=17) | REJECTED | reliability_not_demonstrated |
| 53077845 | WETH→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.062522 WETH | 0.000557 WETH | 0.000000 WETH | 0.000003 WETH | 0.000554 WETH (1.1936 €) | — | 88.65 | 0.000 (n=17) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53077845 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→cbBTC | 0.001795 cbBTC | 0.000016 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000016 cbBTC (1.1934 €) | — | 89.86 | 0.000 (n=17) | REJECTED | reliability_not_demonstrated |
| 53077845 | WETH→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.062522 WETH | 0.000557 WETH | 0.000000 WETH | 0.000003 WETH | 0.000554 WETH (1.1921 €) | — | 88.54 | 0.000 (n=17) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53077845 | cbBTC→[uniswap_v3]→WETH→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→cbBTC | 0.001797 cbBTC | 0.000016 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000016 cbBTC (1.1838 €) | — | 89.04 | 0.000 (n=24) | REJECTED | reliability_not_demonstrated |
| 53077845 | WETH→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→cbBTC→[uniswap_v3]→WETH | 0.062522 WETH | 0.000552 WETH | 0.000000 WETH | 0.000003 WETH | 0.000549 WETH (1.1824 €) | — | 87.82 | 0.000 (n=24) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53077845 | cbBTC→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→cbBTC | 0.001734 cbBTC | 0.000016 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000016 cbBTC (1.1579 €) | — | 90.25 | 0.000 (n=24) | REJECTED | reliability_not_demonstrated |
| 53077845 | WETH→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→WETH | 0.059759 WETH | 0.000540 WETH | 0.000000 WETH | 0.000003 WETH | 0.000537 WETH (1.1565 €) | — | 89.86 | 0.000 (n=24) | REJECTED | reliability_not_demonstrated |
| 53077845 | cbBTC→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→cbBTC | 0.001515 cbBTC | 0.000016 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000016 cbBTC (1.1512 €) | — | 102.71 | 0.000 (n=24) | REJECTED | reliability_not_demonstrated |
| 53077845 | WETH→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→WETH | 0.052188 WETH | 0.000537 WETH | 0.000000 WETH | 0.000003 WETH | 0.000534 WETH (1.1510 €) | — | 102.41 | 0.000 (n=24) | REJECTED | reliability_not_demonstrated |
| 53077845 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→cbBTC | 0.001494 cbBTC | 0.000016 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000015 cbBTC (1.1409 €) | — | 103.20 | 0.000 (n=17) | REJECTED | reliability_not_demonstrated |
| 53077845 | WETH→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.051488 WETH | 0.000533 WETH | 0.000000 WETH | 0.000003 WETH | 0.000530 WETH (1.1407 €) | — | 102.88 | 0.000 (n=17) | REJECTED | reliability_not_demonstrated |
| 53077845 | cbBTC→[uniswap_v3]→WETH→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→cbBTC | 0.001418 cbBTC | 0.000015 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000015 cbBTC (1.1261 €) | — | 107.34 | 0.000 (n=24) | REJECTED | reliability_not_demonstrated |
| 53077845 | WETH→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→cbBTC→[uniswap_v3]→WETH | 0.048731 WETH | 0.000526 WETH | 0.000000 WETH | 0.000003 WETH | 0.000523 WETH (1.1252 €) | — | 107.22 | 0.000 (n=24) | REJECTED | reliability_not_demonstrated |
| 53077286 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→cbBTC | 0.014726 cbBTC | 0.000015 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000015 cbBTC (1.0960 €) | — | 10.05 | 0.000 (n=46) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53077286 | WETH→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.500915 WETH | 0.000512 WETH | 0.000000 WETH | 0.000003 WETH | 0.000509 WETH (1.0958 €) | — | 10.16 | 0.000 (n=46) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 53078369 | USDC→[pancakeswap_v3]→ICNT→[uniswap_v3]→USDC | 273.199639 USDC | 1.151136 USDC | 0.000000 USDC | 0.005257 USDC | 1.145879 USDC (1.0542 €) | — | 41.94 | 0.001 (n=11) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53077845 | USDC→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→USDC | 120.391629 USDC | 1.150851 USDC | 0.000000 USDC | 0.007035 USDC | 1.143816 USDC (1.0523 €) | — | 95.01 | 0.000 (n=24) | REJECTED | reliability_not_demonstrated |
| 53077845 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→USDC | 120.344519 USDC | 1.150785 USDC | 0.000000 USDC | 0.007035 USDC | 1.143750 USDC (1.0523 €) | — | 95.04 | 0.000 (n=17) | REJECTED | reliability_not_demonstrated |
| 53077845 | WETH→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→WETH | 0.051376 WETH | 0.000491 WETH | 0.000000 WETH | 0.000003 WETH | 0.000488 WETH (1.0504 €) | — | 94.94 | 0.000 (n=24) | REJECTED | reliability_not_demonstrated |
| 53077845 | WETH→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.051329 WETH | 0.000491 WETH | 0.000000 WETH | 0.000003 WETH | 0.000488 WETH (1.0504 €) | — | 95.02 | 0.000 (n=17) | REJECTED | reliability_not_demonstrated |
| 53077845 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→USDC | 117.111566 USDC | 1.144335 USDC | 0.000000 USDC | 0.007035 USDC | 1.137300 USDC (1.0463 €) | — | 97.11 | 0.000 (n=24) | REJECTED | reliability_not_demonstrated |
| 53077845 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→USDC | 119.793976 USDC | 1.144514 USDC | 0.000000 USDC | 0.007390 USDC | 1.137124 USDC (1.0462 €) | — | 94.92 | 0.000 (n=24) | REJECTED | reliability_not_demonstrated |

## Fiabilité et décision
- Observations ghost : 2501 ; taux observé 0.091 ; borne inférieure crédible (0.9) 0.084 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 8.4% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
