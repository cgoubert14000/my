# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-25T19:54:40+00:00 ; durée 244.47 min ; blocs 53077030 → 53084364 (7328 vus)

## Connexion
- Requêtes RPC : 91529 ; erreurs : 5 ; latence p50/p95 : 63.5/533.8 ms
- Rafraîchissements d'état : 7329 ; âge des données au dernier bloc : 1.03 s ; changements de frais LP observés (pools à frais dynamiques) : 8316
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 31716 ; cycles déclenchés par événement : 4541 ; avance médiane sur le rafraîchissement multicall : 257 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,354.46 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 531 pools, 306 jetons, 19476 routes
- Par DEX : uniswap_v3 142, aerodrome 215, aerodrome_slipstream 127, pancakeswap_v3 31, uniswap_v2 13, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 191 (rejetés 2) → 596 jetons ; pools candidats 3792 (énumérés 341, par paires 0), mesurés 533, sous le plancher de 10000.0 $ : 2 → gardés 531 (max 1500) ; prix des hubs : {'USDC': 1.0, 'USDbC': 1.0, 'DAI': 1.0, 'WETH': 2340.831442, 'cbBTC': 80585.156098, 'AERO': 0.694811}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 159,098,411 | 2,354.460752 | 53084364 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 17,581,579 | 0.029185 | 53084364 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,284,574 | 0.029142 | 53084364 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,615,081 | 0.000012 | 53084364 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome | WETH/VVV | 3000 | 9,079,255 | 91.179367 | 53084364 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/USDC | 500 | 8,468,373 | 2,349.006215 | 53084364 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | USDC/AERO | 3000 | 7,518,645 | 1.454365 | 53084364 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,043,354 | 0.001650 | 53084364 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | WETH/USDC | 150 | 5,526,578 | 2,348.198021 | 53084364 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,389,023 | 0.029178 | 53084364 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,528,025 | 2,348.066549 | 53084364 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,241,260 | 1.000001 | 53084364 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,850,959 | 34,989.001278 | 53084364 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/USDC | 3000 | 3,795,450 | 2,354.536463 | 53084364 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 3,242,850 | 0.029155 | 53084364 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | USDC/cbBTC | 400 | 2,789,615 | 0.000012 | 53084364 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome_slipstream | WETH/VVV | 2730 | 2,552,355 | 91.204417 | 53084364 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,234,311 | 409.337060 | 53084364 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | WETH/FAI | 10000 | 2,136,748 | 1,230,964.316803 | 53084364 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,908,438 | 0.000000 | 53084364 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,905,043 | 0.000012 | 53084364 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v3 | XDP/USDC | 100 | 1,791,833 | 0.018066 | 53084364 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,730,678 | 0.000012 | 53084364 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | USDC/cbBTC | 332 | 1,722,367 | 0.000012 | 53084364 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | VIRTUAL/WETH | 10000 | 1,580,533 | 0.000265 | 53084364 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,458,369 | 0.826377 | 53084364 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,453,220 | 1.698035 | 53084364 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | WETH/AERO | 3000 | 1,443,871 | 3,415.724935 | 53084364 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,440,122 | 0.005516 | 53084364 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,377,674 | 14,020.604884 | 53084364 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,296,682 | 2,349.006215 | 53084364 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | WETH/AERO | 10000 | 1,264,565 | 3,391.486403 | 53084364 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,251,054 | 0.000266 | 53084364 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | USDC/SEND | 3000 | 1,221,956 | 65.077583 | 53084364 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,172,910 | 35,446,952.567842 | 53084364 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | DRB/WETH | 10000 | 1,152,437 | 0.000000 | 53084364 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | WETH/WELL | 10000 | 1,144,593 | 1,110,180.922641 | 53084364 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,131,502 | 496,100.713712 | 53084364 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | USDC/NOCK | 3000 | 1,095,534 | 52.187600 | 53084364 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome | WETH/EDEL | 7000 | 1,066,617 | 74,670.829454 | 53084364 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,039,714 | 16.999993 | 53084364 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,027,954 | 21,964,749.071839 | 53084364 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | USDC/VVV | 3000 | 985,211 | 0.038831 | 53084364 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/USDC | 10000 | 927,918 | 2,339.197561 | 53084364 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome | WETH/msETH (stable) | 500 | 923,106 | 2.311225 | 53084364 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | uXRP/WETH | 3000 | 903,019 | 0.000551 | 53084364 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| uniswap_v3 | WETH/MORPHO | 3000 | 901,381 | 1,121.486236 | 53084364 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 895,844 | 17.078101 | 53084364 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| uniswap_v3 | WETH/VVV | 10000 | 889,252 | 91.446039 | 53084364 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 877,860 | 18.001308 | 53084364 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v2 | WETH/USDC | 3000 | 850,976 | 2,353.809064 | 53084364 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 809,504 | 0.000009 | 53084364 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | WETH/wstETH | 3000 | 797,186 | 0.803130 | 53084364 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| aerodrome | weETH_04c0/WETH | 500 | 787,127 | 1.105853 | 53084364 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| pancakeswap_v3 | QUID/USDC | 100 | 786,987 | 0.055465 | 53084364 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 749,861 | 0.626032 | 53084364 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 741,114 | 4,764,216.110846 | 53084364 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v2 | WETH/NPC | 3000 | 719,066 | 134,918.465013 | 53084364 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| uniswap_v3 | TIG/USDC | 10000 | 718,684 | 0.648287 | 53084364 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | WETH/BRETT | 2096 | 704,053 | 497,190.268977 | 53084364 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |

## Recherche d'opportunités
- Cycles : 11869 ; routes examinées : 231160644 ; candidats optimisés : 602964 ; net attendu > 0 : 1540 ; dernier cycle 204.9 ms
- Rejets (moteur) : {'spread_below_threshold': 225714510, 'liquidity_below_min': 3543298, 'pool_quarantined': 1046120, 'negative_expected_net': 601424, 'unquotable': 240778, 'borrow_bound_too_small': 11865, 'cycle_budget_exhausted': 1109}
- Enregistrements de la session : 602964 ; net attendu > 0 : 1540 ; simulés (eth_call de la vraie tx) : 100 (ok 26, échec 74) ; étiquettes ghost N+1 : 3/84 positives
- Décisions : {'REJECTED': 602964} ; motifs de rejet : {'below_safety_margin': 587, 'negative_expected_net': 601424, 'p_lower_below_threshold': 1372, 'price_impact': 4, 'reliability_not_demonstrated': 168, 'sim_below_estimate': 2, 'simulated_net_nonpositive': 1, 'simulation_failed': 74}

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
- Observations ghost : 2538 ; taux observé 0.091 ; borne inférieure crédible (0.9) 0.084 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 8.4% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
