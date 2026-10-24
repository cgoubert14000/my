# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-24T17:32:15+00:00 ; durée 18.34 min ; blocs 53036340 → 53036893 (534 vus)

## Connexion
- Requêtes RPC : 6677 ; erreurs : 0 ; latence p50/p95 : 203.4/949.1 ms
- Rafraîchissements d'état : 535 ; âge des données au dernier bloc : 1.63 s ; changements de frais LP observés (pools à frais dynamiques) : 688
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 6286 ; cycles déclenchés par événement : 866 ; avance médiane sur le rafraîchissement multicall : 449 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,312.73 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 530 pools, 306 jetons, 19348 routes
- Par DEX : uniswap_v3 139, aerodrome 216, aerodrome_slipstream 130, pancakeswap_v3 30, uniswap_v2 12, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 193 (rejetés 2) → 598 jetons ; pools candidats 3808 (énumérés 345, par paires 0), mesurés 532, sous le plancher de 10000.0 $ : 2 → gardés 530 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDbC': 1.0, 'USDC': 1.0, 'WETH': 2311.365621, 'cbBTC': 80049.166907, 'AERO': 0.688082}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 152,917,421 | 2,312.731277 | 53036893 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 17,076,715 | 0.028897 | 53036893 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 11,951,152 | 97.275385 | 53036893 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,078,096 | 0.028893 | 53036893 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,526,428 | 0.000012 | 53036893 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome | USDC/AERO | 3000 | 8,731,991 | 1.446627 | 53036893 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/USDC | 500 | 8,366,238 | 2,313.496069 | 53036893 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 7,597,624 | 0.028886 | 53036893 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,954,394 | 0.001635 | 53036893 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 340 | 6,282,876 | 0.000012 | 53036893 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 743 | 5,388,077 | 2,313.239753 | 53036893 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,356,322 | 0.028888 | 53036893 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | USDC/cbBTC | 448 | 4,497,613 | 0.000012 | 53036893 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,415,110 | 2,313.429730 | 53036893 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,211,290 | 0.999835 | 53036893 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,815,649 | 34,787.800316 | 53036893 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/USDC | 3000 | 3,777,224 | 2,313.709383 | 53036893 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | WETH/USDT | 439 | 2,742,617 | 2,323.302614 | 53036893 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome_slipstream | WETH/VVV | 2703 | 2,457,757 | 97.305493 | 53036893 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,192,062 | 410.465796 | 53036893 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | WETH/FAI | 10000 | 2,088,636 | 1,243,064.919347 | 53036893 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,896,278 | 0.000013 | 53036893 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,880,274 | 0.000000 | 53036893 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,782,594 | 0.017922 | 53036893 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,731,006 | 0.000012 | 53036893 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | VIRTUAL/WETH | 10000 | 1,561,818 | 0.000264 | 53036893 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,489,913 | 1.675240 | 53036893 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,457,852 | 0.826899 | 53036893 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,437,070 | 3,351.563883 | 53036893 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,384,186 | 0.005315 | 53036893 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,359,946 | 14,206.291356 | 53036893 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/AERO | 10000 | 1,272,211 | 3,341.127574 | 53036893 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,240,927 | 2,313.496090 | 53036893 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,227,318 | 0.000266 | 53036893 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | USDC/SEND | 3000 | 1,224,787 | 64.777090 | 53036893 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | DRB/WETH | 10000 | 1,156,884 | 0.000000 | 53036893 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/doginme | 10000 | 1,151,402 | 35,511,971.060590 | 53036893 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | USDC/NOCK | 3000 | 1,121,809 | 49.771304 | 53036893 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome | WETH/WELL | 10000 | 1,118,801 | 1,122,207.256227 | 53036893 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,101,314 | 501,073.386748 | 53036893 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | WETH/EDEL | 7000 | 1,035,023 | 76,534.736351 | 53036893 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,019,114 | 17.956452 | 53036893 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,012,473 | 21,823,007.868303 | 53036893 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 943,226 | 17.067591 | 53036893 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 940,928 | 23.203225 | 53036893 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| uniswap_v3 | USDC/VVV | 3000 | 940,153 | 0.042094 | 53036893 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/MORPHO | 3000 | 920,698 | 1,090.536732 | 53036893 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome | WETH/msETH (stable) | 500 | 912,037 | 2.306099 | 53036893 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | uXRP/WETH | 3000 | 884,191 | 0.000548 | 53036893 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 878,740 | 17.963727 | 53036893 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v3 | WETH/VVV | 10000 | 856,909 | 97.275921 | 53036893 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v2 | WETH/USDC | 3000 | 843,331 | 2,312.995769 | 53036893 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| pancakeswap_v3 | QUID/USDC | 100 | 825,953 | 0.061464 | 53036893 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 818,433 | 0.000009 | 53036893 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | weETH_04c0/WETH | 500 | 790,866 | 1.105883 | 53036893 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome | WETH/wstETH | 3000 | 783,072 | 0.803098 | 53036893 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | WETH/USDC | 10000 | 780,027 | 2,304.780586 | 53036893 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 739,899 | 0.615522 | 53036893 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 737,364 | 4,642,831.775011 | 53036893 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 731,296 | 0.670007 | 53036893 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |

## Recherche d'opportunités
- Cycles : 1400 ; routes examinées : 27087200 ; candidats optimisés : 115765 ; net attendu > 0 : 84 ; dernier cycle 261.8 ms
- Rejets (moteur) : {'spread_below_threshold': 26531992, 'liquidity_below_min': 311584, 'pool_quarantined': 124092, 'negative_expected_net': 115681, 'unquotable': 1989, 'borrow_bound_too_small': 1396, 'cycle_budget_exhausted': 382}
- Enregistrements de la session : 115765 ; net attendu > 0 : 84 ; simulés (eth_call de la vraie tx) : 11 (ok 0, échec 11) ; étiquettes ghost N+1 : 0/9 positives
- Décisions : {'REJECTED': 115765} ; motifs de rejet : {'below_safety_margin': 54, 'negative_expected_net': 115681, 'p_lower_below_threshold': 78, 'price_impact': 22, 'reliability_not_demonstrated': 6, 'simulation_failed': 11, 'stale_data': 10}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53036844 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→USDC | 155.743154 USDC | 0.092802 USDC | 0.000000 USDC | 0.006953 USDC | 0.085849 USDC (0.0790 €) | — | 5.51 | 0.142 (n=126) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.14<0.75) |
| 53036844 | cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.001790 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0788 €) | — | 5.98 | 0.142 (n=126) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 53036844 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→USDC | 164.697571 USDC | 0.091762 USDC | 0.000000 USDC | 0.006953 USDC | 0.084809 USDC (0.0780 €) | — | 5.15 | 0.142 (n=126) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 53036844 | cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.001783 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0780 €) | — | 5.94 | 0.142 (n=126) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 53036844 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.001756 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0714 €) | — | 5.53 | 0.092 (n=241) | REJECTED | p_lower_below_threshold(0.09<0.75) |
| 53036844 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 159.239477 USDC | 0.084053 USDC | 0.000000 USDC | 0.006953 USDC | 0.077100 USDC (0.0709 €) | — | 4.84 | 0.092 (n=241) | REJECTED | p_lower_below_threshold(0.09<0.75) |
| 53036844 | cbBTC→[uniswap_v3]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.001752 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0648 €) | — | 5.02 | 0.142 (n=126) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 53036844 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[uniswap_v3]→USDC | 142.420043 USDC | 0.077132 USDC | 0.000000 USDC | 0.006953 USDC | 0.070179 USDC (0.0646 €) | — | 4.93 | 0.142 (n=126) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 53036844 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.001263 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0442 €) | — | 4.75 | 0.092 (n=241) | REJECTED | p_lower_below_threshold(0.09<0.75) |
| 53036844 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 108.025334 USDC | 0.054777 USDC | 0.000000 USDC | 0.006953 USDC | 0.047824 USDC (0.0440 €) | — | 4.43 | 0.092 (n=241) | REJECTED | p_lower_below_threshold(0.09<0.75) |
| 53036844 | WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.037003 WETH | 0.000018 WETH | 0.000000 WETH | 0.000003 WETH | 0.000015 WETH (0.0319 €) | — | 4.06 | 0.092 (n=241) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.09<0.75) |
| 53036844 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.000957 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0316 €) | — | 4.49 | 0.092 (n=241) | REJECTED | p_lower_below_threshold(0.09<0.75) |
| 53036452 | USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 157.266489 USDC | 0.039250 USDC | 0.000000 USDC | 0.007304 USDC | 0.031946 USDC (0.0294 €) | — | 2.03 | 0.141 (n=287) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.14<0.75) |
| 53036452 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH | 0.067789 WETH | 0.000017 WETH | 0.000000 WETH | 0.000003 WETH | 0.000014 WETH (0.0293 €) | — | 2.03 | 0.141 (n=287) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.14<0.75) |
| 53036452 | USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→USDC | 155.337195 USDC | 0.038281 USDC | 0.000000 USDC | 0.007304 USDC | 0.030977 USDC (0.0285 €) | — | 1.99 | 0.216 (n=138) | REJECTED | below_safety_margin(30977<31067), p_lower_below_threshold(0.22<0.75) |
| 53036452 | WETH→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH | 0.067251 WETH | 0.000017 WETH | 0.000000 WETH | 0.000003 WETH | 0.000013 WETH (0.0284 €) | — | 1.99 | 0.216 (n=138) | REJECTED | below_safety_margin(13361933332999<13450236810884), p_lower_below_threshold(0.22<0.75) |
| 53036844 | WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→WETH | 0.028671 WETH | 0.000015 WETH | 0.000000 WETH | 0.000003 WETH | 0.000012 WETH (0.0253 €) | — | 4.14 | 0.092 (n=241) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.09<0.75) |
| 53036844 | cbBTC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.000808 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0250 €) | — | 4.21 | 0.092 (n=241) | REJECTED | p_lower_below_threshold(0.09<0.75) |
| 53036452 | USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 98.178490 USDC | 0.020082 USDC | 0.000000 USDC | 0.007304 USDC | 0.012778 USDC (0.0118 €) | — | 1.30 | 0.216 (n=138) | REJECTED | below_safety_margin(12778<19635), p_lower_below_threshold(0.22<0.75) |
| 53036452 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH | 0.042683 WETH | 0.000009 WETH | 0.000000 WETH | 0.000003 WETH | 0.000006 WETH (0.0117 €) | — | 1.29 | 0.216 (n=138) | REJECTED | below_safety_margin(5508761511665<8536688905492), p_lower_below_threshold(0.22<0.75) |
| 53036452 | USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 406.450587 USDC | 0.017180 USDC | 0.000000 USDC | 0.006953 USDC | 0.010227 USDC (0.0094 €) | — | 0.25 | 0.141 (n=287) | REJECTED | below_safety_margin(10227<81290), p_lower_below_threshold(0.14<0.75) |
| 53036452 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH | 0.176843 WETH | 0.000007 WETH | 0.000000 WETH | 0.000003 WETH | 0.000004 WETH (0.0094 €) | — | 0.25 | 0.141 (n=287) | REJECTED | below_safety_margin(4406808339041<35368634157539), p_lower_below_threshold(0.14<0.75) |
| 53036452 | USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→USDC | 445.063356 USDC | 0.016775 USDC | 0.000000 USDC | 0.006953 USDC | 0.009822 USDC (0.0090 €) | — | 0.22 | 0.216 (n=138) | REJECTED | below_safety_margin(9822<89012), p_lower_below_threshold(0.22<0.75) |
| 53036452 | WETH→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH | 0.192325 WETH | 0.000007 WETH | 0.000000 WETH | 0.000003 WETH | 0.000004 WETH (0.0090 €) | — | 0.22 | 0.216 (n=138) | REJECTED | below_safety_margin(4231852543830<38465047282999), p_lower_below_threshold(0.22<0.75) |
| 53036452 | USDC→[aerodrome_slipstream]→EURC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 56.340295 USDC | 0.013169 USDC | 0.000000 USDC | 0.006953 USDC | 0.006216 USDC (0.0057 €) | — | 1.10 | 0.141 (n=287) | REJECTED | below_safety_margin(6216<11268), p_lower_below_threshold(0.14<0.75) |

## Fiabilité et décision
- Observations ghost : 2264 ; taux observé 0.098 ; borne inférieure crédible (0.9) 0.090 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 9.0% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
