# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-18T18:50:48+00:00 ; durée 255.33 min ; blocs 52772387 → 52780045 (7532 vus)

## Connexion
- Requêtes RPC : 89405 ; erreurs : 5 ; latence p50/p95 : 387.2/1,795.8 ms
- Rafraîchissements d'état : 7532 ; âge des données au dernier bloc : 3.5 s ; changements de frais LP observés (pools à frais dynamiques) : 15427
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 4312 ; cycles déclenchés par événement : 200 ; avance médiane sur le rafraîchissement multicall : 636 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,365.75 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 574 pools, 327 jetons, 21464 routes
- Par DEX : uniswap_v3 136, aerodrome 233 (quarantaine 1), aerodrome_slipstream 155, pancakeswap_v3 32, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 206 (rejetés 2) → 611 jetons ; pools candidats 3914 (énumérés 390, par paires 0), mesurés 576, sous le plancher de 10000.0 $ : 2 → gardés 574 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2372.774214, 'AERO': 0.799025, 'cbBTC': 81081.426767}
- Pools en quarantaine : 1 — aerodrome:fBOMB/AERO@0xbBf71A: simulation failed ×5 (model/chain mismatch) — until block 52780169

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 144,638,936 | 2,365.746029 | 52780045 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 40,925,624 | 1.264390 | 52780045 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 18,472,341 | 0.029186 | 52780045 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 500 | 17,888,653 | 0.029142 | 52780045 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 16,336,167 | 108.334537 | 52780045 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,254,819 | 0.029199 | 52780045 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,733,700 | 0.000012 | 52780045 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 8,241,191 | 2,362.529846 | 52780045 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome_slipstream | USDC/cbBTC | 436 | 7,936,568 | 0.000012 | 52780045 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome_slipstream | USDC/cbBTC | 338 | 7,862,288 | 0.000012 | 52780045 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 624 | 7,240,508 | 2,363.271638 | 52780045 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,073,229 | 0.001644 | 52780045 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | WETH/USDC | 3000 | 5,424,201 | 2,365.973666 | 52780045 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,179,497 | 0.029143 | 52780045 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/superOETHb | 400 | 5,137,385 | 1.000854 | 52780045 | `0x6446021F4E396dA3df4235C62537431372195D38` |
| aerodrome | fBOMB/AERO | 10000 | 4,947,484 | 0.025885 | 52780045 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,728,823 | 0.802398 | 52780045 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,532,690 | 0.000271 | 52780045 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/USDT | 412 | 4,452,657 | 2,366.395252 | 52780045 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,412,822 | 2,363.399632 | 52780045 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,323,195 | 0.998103 | 52780045 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,997,920 | 33,211.740788 | 52780045 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | USDC/AERO | 10000 | 3,403,760 | 1.252452 | 52780045 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome | WETH/AERO | 10000 | 3,224,738 | 2,953.585814 | 52780045 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,850,981 | 1.141830 | 52780045 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,834,800 | 0.000012 | 52780045 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 2,665,501 | 0.000010 | 52780045 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/VVV | 2727 | 2,497,856 | 108.312199 | 52780045 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,232,966 | 412.928921 | 52780045 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | WETH/FAI | 10000 | 2,157,322 | 1,220,768.381336 | 52780045 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,065,779 | 1.233151 | 52780045 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,036,703 | 1.372655 | 52780045 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,978,388 | 0.000000 | 52780045 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome_slipstream | EURC/USDC | 70 | 1,959,032 | 1.122865 | 52780045 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,805,531 | 15.846235 | 52780045 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | fBOMB/USDC | 10000 | 1,792,251 | 0.021114 | 52780045 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,763,050 | 0.000012 | 52780045 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | XDP/USDC | 100 | 1,756,489 | 0.018439 | 52780045 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,751,618 | 14,157.910565 | 52780045 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | weETH_04c0/WETH | 500 | 1,710,660 | 1.105523 | 52780045 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome | WETH/msETH (stable) | 500 | 1,639,947 | 2.303680 | 52780045 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 1,628,936 | 1,029.688703 | 52780045 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| uniswap_v3 | WETH/AERO | 3000 | 1,460,742 | 2,979.516677 | 52780045 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,456,228 | 0.826424 | 52780045 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,435,324 | 0.916353 | 52780045 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,318,938 | 0.435316 | 52780045 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,283,637 | 0.000000 | 52780045 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,270,453 | 0.000270 | 52780045 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,267,236 | 0.004566 | 52780045 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome | WETH/cbBTC | 3000 | 1,252,583 | 0.029203 | 52780045 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| aerodrome | USDC/SEND | 3000 | 1,233,378 | 63.877921 | 52780045 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,225,870 | 23.237335 | 52780045 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,199,548 | 2,362.524931 | 52780045 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome_slipstream | WETH/msETH | 500 | 1,195,846 | 1.130988 | 52780045 | `0x74F72788F4814D7fF3C49B44684aa98Eee140C0E` |
| uniswap_v3 | WETH/doginme | 10000 | 1,184,574 | 34,669,034.800324 | 52780045 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | WETH/WELL | 10000 | 1,140,063 | 1,167,492.014199 | 52780045 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,109,532 | 531,931.778434 | 52780045 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome_slipstream | msUSD/USDC | 500 | 1,087,582 | 0.885208 | 52780045 | `0x7501bc8Bb51616F79bfA524E464fb7B41f0B10fB` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,084,869 | 15.238654 | 52780045 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | USDC/NOCK | 3000 | 1,079,036 | 54.117965 | 52780045 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |

## Recherche d'opportunités
- Cycles : 7731 ; routes examinées : 165938184 ; candidats optimisés : 927854 ; net attendu > 0 : 417 ; dernier cycle 511.4 ms
- Rejets (moteur) : {'spread_below_threshold': 162799891, 'liquidity_below_min': 1559517, 'negative_expected_net': 927437, 'pool_quarantined': 639106, 'borrow_bound_too_small': 7720, 'cycle_budget_exhausted': 4096}
- Enregistrements de la session : 927854 ; net attendu > 0 : 417 ; simulés (eth_call de la vraie tx) : 119 (ok 7, échec 112) ; étiquettes ghost N+1 : 0/61 positives
- Décisions : {'REJECTED': 927854} ; motifs de rejet : {'below_safety_margin': 271, 'negative_expected_net': 927437, 'p_lower_below_threshold': 385, 'price_impact': 290, 'reliability_not_demonstrated': 32, 'simulation_failed': 112, 'stale_data': 20}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52772457 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→AERO→[pancakeswap_v3]→WETH | 0.157042 WETH | 0.000051 WETH | 0.000000 WETH | 0.000003 WETH | 0.000048 WETH (0.1050 €) | — | 3.06 | 0.128 (n=86) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.13<0.75) |
| 52772457 | cbBTC→[aerodrome_slipstream]→AERO→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.004218 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.1044 €) | — | 3.32 | 0.128 (n=86) | REJECTED | p_lower_below_threshold(0.13<0.75) |
| 52772400 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 459.130293 USDC | 0.098558 USDC | 0.000000 USDC | 0.005706 USDC | 0.092852 USDC (0.0854 €) | — | 2.02 | 0.020 (n=40) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.02<0.75) |
| 52772400 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.193596 WETH | 0.000042 WETH | 0.000000 WETH | 0.000002 WETH | 0.000039 WETH (0.0854 €) | — | 2.02 | 0.020 (n=40) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.02<0.75) |
| 52772457 | cbBTC→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→USDC→[uniswap_v3]→cbBTC | 0.003328 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0678 €) | — | 2.73 | 0.311 (n=62) | REJECTED | p_lower_below_threshold(0.31<0.75) |
| 52772457 | USDC→[uniswap_v3]→cbBTC→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→USDC | 278.506660 USDC | 0.080302 USDC | 0.000000 USDC | 0.007158 USDC | 0.073144 USDC (0.0673 €) | — | 2.63 | 0.311 (n=62) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.31<0.75) |
| 52772457 | cbBTC→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→cbBTC | 0.003359 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0663 €) | — | 2.65 | 0.311 (n=62) | REJECTED | p_lower_below_threshold(0.31<0.75) |
| 52772457 | USDC→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→USDC | 272.352625 USDC | 0.078563 USDC | 0.000000 USDC | 0.007158 USDC | 0.071405 USDC (0.0657 €) | — | 2.62 | 0.311 (n=62) | REJECTED | p_lower_below_threshold(0.31<0.75) |
| 52772457 | cbBTC→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→cbBTC | 0.003111 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0589 €) | — | 2.54 | 0.311 (n=62) | REJECTED | stale_data(4022ms>4000.0), p_lower_below_threshold(0.31<0.75) |
| 52772457 | USDC→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→USDC | 272.370781 USDC | 0.070961 USDC | 0.000000 USDC | 0.007158 USDC | 0.063803 USDC (0.0587 €) | — | 2.34 | 0.311 (n=62) | REJECTED | stale_data(4015ms>4000.0), p_lower_below_threshold(0.31<0.75) |
| 52772457 | cbBTC→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.003110 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0581 €) | — | 2.51 | 0.124 (n=109) | REJECTED | stale_data(4009ms>4000.0), p_lower_below_threshold(0.12<0.75) |
| 52772457 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→USDC | 257.401804 USDC | 0.070287 USDC | 0.000000 USDC | 0.007158 USDC | 0.063129 USDC (0.0581 €) | — | 2.45 | 0.124 (n=109) | REJECTED | stale_data(4002ms>4000.0), p_lower_below_threshold(0.12<0.75) |
| 52772457 | WETH→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→AERO→[pancakeswap_v3]→WETH | 0.075109 WETH | 0.000028 WETH | 0.000000 WETH | 0.000003 WETH | 0.000025 WETH (0.0538 €) | — | 3.28 | 0.128 (n=86) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.13<0.75) |
| 52772457 | cbBTC→[aerodrome_slipstream]→AERO→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→cbBTC | 0.002046 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0537 €) | — | 3.52 | 0.128 (n=86) | REJECTED | p_lower_below_threshold(0.13<0.75) |
| 52772457 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→USDC | 162.197416 USDC | 0.048555 USDC | 0.000000 USDC | 0.007158 USDC | 0.041397 USDC (0.0381 €) | — | 2.55 | 0.124 (n=109) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52772457 | cbBTC→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.001939 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0380 €) | — | 2.63 | 0.124 (n=109) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52775705 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome_slipstream]→WETH | 0.040270 WETH | 0.000013 WETH | 0.000000 WETH | 0.000003 WETH | 0.000010 WETH (0.0227 €) | 0.000010 WETH | 2.59 | 0.124 (n=109) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52775705 | USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 94.879841 USDC | 0.031796 USDC | 0.000000 USDC | 0.007129 USDC | 0.024667 USDC (0.0227 €) | — | 2.60 | 0.124 (n=109) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52772457 | USDC→[uniswap_v3]→cbBTC→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC | 110.178546 USDC | 0.031856 USDC | 0.000000 USDC | 0.007518 USDC | 0.024338 USDC (0.0224 €) | — | 2.21 | 0.311 (n=62) | REJECTED | p_lower_below_threshold(0.31<0.75) |
| 52772457 | cbBTC→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC→[uniswap_v3]→cbBTC | 0.001399 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0224 €) | — | 2.14 | 0.311 (n=62) | REJECTED | p_lower_below_threshold(0.31<0.75) |
| 52772400 | WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.109119 WETH | 0.000013 WETH | 0.000000 WETH | 0.000003 WETH | 0.000010 WETH (0.0222 €) | — | 0.93 | 0.311 (n=62) | REJECTED | below_safety_margin(10168213104552<21823795850761), p_lower_below_threshold(0.31<0.75) |
| 52772400 | WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.109119 WETH | 0.000013 WETH | 0.000000 WETH | 0.000003 WETH | 0.000010 WETH (0.0222 €) | — | 0.93 | 0.311 (n=62) | REJECTED | below_safety_margin(10168213104552<21823795850761), p_lower_below_threshold(0.31<0.75) |
| 52772400 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC | 259.011558 USDC | 0.031638 USDC | 0.000000 USDC | 0.007512 USDC | 0.024126 USDC (0.0222 €) | — | 0.93 | 0.311 (n=62) | REJECTED | below_safety_margin(24126<51802), p_lower_below_threshold(0.31<0.75) |
| 52772400 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC | 259.011558 USDC | 0.031638 USDC | 0.000000 USDC | 0.007512 USDC | 0.024126 USDC (0.0222 €) | — | 0.93 | 0.311 (n=62) | REJECTED | below_safety_margin(24126<51802), p_lower_below_threshold(0.31<0.75) |
| 52772400 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 238.249470 USDC | 0.031017 USDC | 0.000000 USDC | 0.007512 USDC | 0.023505 USDC (0.0216 €) | — | 0.99 | 0.124 (n=109) | REJECTED | below_safety_margin(23505<47649), p_lower_below_threshold(0.12<0.75) |

## Fiabilité et décision
- Observations ghost : 1026 ; taux observé 0.110 ; borne inférieure crédible (0.9) 0.098 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 9.8% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
