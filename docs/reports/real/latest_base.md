# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-21T10:56:16+00:00 ; durée 30.56 min ; blocs 52894493 → 52895414 (771 vus)

## Connexion
- Requêtes RPC : 10654 ; erreurs : 3 ; latence p50/p95 : 194.8/791.3 ms
- Rafraîchissements d'état : 772 ; âge des données au dernier bloc : 0.99 s ; changements de frais LP observés (pools à frais dynamiques) : 1723
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 6071 ; cycles déclenchés par événement : 364 ; avance médiane sur le rafraîchissement multicall : 537 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,451.18 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 578 pools, 326 jetons, 21598 routes
- Par DEX : uniswap_v3 138, aerodrome 235, aerodrome_slipstream 155, pancakeswap_v3 32, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 206 (rejetés 2) → 611 jetons ; pools candidats 3912 (énumérés 393, par paires 0), mesurés 581, sous le plancher de 10000.0 $ : 3 → gardés 578 (max 1500) ; prix des hubs : {'USDC': 1.0, 'DAI': 1.0, 'USDbC': 1.0, 'WETH': 2451.17881, 'AERO': 0.838921, 'cbBTC': 83216.410353}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 149,230,900 | 2,451.177548 | 52895414 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 38,417,738 | 1.184844 | 52895414 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| aerodrome | WETH/VVV | 3000 | 18,043,557 | 95.048036 | 52895414 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,521,267 | 0.029453 | 52895414 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 14,561,050 | 0.029458 | 52895414 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,433,409 | 0.029472 | 52895414 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,963,911 | 0.000012 | 52895414 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 8,784,834 | 2,455.139194 | 52895414 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/USDC | 3000 | 8,462,864 | 2,451.219379 | 52895414 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | USDC/cbBTC | 400 | 7,642,401 | 0.000012 | 52895414 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome_slipstream | WETH/USDC | 549 | 7,442,195 | 2,455.309044 | 52895414 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | USDC/cbBTC | 332 | 7,400,460 | 0.000012 | 52895414 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,307,326 | 0.001669 | 52895414 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,614,655 | 0.029460 | 52895414 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | fBOMB/AERO | 10000 | 5,220,472 | 0.024844 | 52895414 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome_slipstream | WETH/USDT | 409 | 5,084,739 | 2,457.866279 | 52895414 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,728,331 | 0.000279 | 52895414 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,724,206 | 0.802395 | 52895414 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,437,597 | 2,455.468078 | 52895414 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,417,414 | 0.998741 | 52895414 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 4,048,398 | 34,770.582805 | 52895414 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | USDC/AERO | 10000 | 3,950,507 | 1.183610 | 52895414 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome | WETH/AERO | 10000 | 3,345,799 | 2,898.787807 | 52895414 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | WETH/VVV | 2700 | 2,762,270 | 94.956544 | 52895414 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 2,714,674 | 0.000010 | 52895414 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,671,181 | 397.951794 | 52895414 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,536,519 | 1.142088 | 52895414 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,277,467 | 0.000012 | 52895414 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | WETH/FAI | 10000 | 2,245,392 | 1,209,742.010817 | 52895414 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 2,078,128 | 0.000012 | 52895414 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,027,072 | 1.383640 | 52895414 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,954,237 | 0.000000 | 52895414 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome | weETH_04c0/WETH | 500 | 1,909,602 | 1.105697 | 52895414 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome_slipstream | WETH/MORPHO | 2721 | 1,881,037 | 1,043.778014 | 52895414 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| uniswap_v3 | XDP/USDC | 100 | 1,809,221 | 0.019166 | 52895414 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,720,158 | 0.916061 | 52895414 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| aerodrome | fBOMB/USDC | 10000 | 1,713,901 | 0.021420 | 52895414 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,710,848 | 1.490009 | 52895414 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome | WETH/msETH (stable) | 500 | 1,692,064 | 2.310993 | 52895414 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | WETH/AERO | 3000 | 1,676,519 | 2,907.250002 | 52895414 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,663,126 | 13,526.481710 | 52895414 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,619,308 | 15.876995 | 52895414 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,458,172 | 0.826524 | 52895414 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | EURC/USDC | 76 | 1,399,702 | 1.122974 | 52895414 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,351,127 | 0.004793 | 52895414 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,336,215 | 0.000280 | 52895414 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| uniswap_v3 | DRB/WETH | 10000 | 1,325,133 | 0.000000 | 52895414 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | WETH/cbBTC | 3000 | 1,314,189 | 0.029472 | 52895414 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,288,801 | 2,455.176048 | 52895414 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,234,154 | 63.797535 | 52895414 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,226,665 | 34,790,527.077835 | 52895414 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,216,761 | 23.076897 | 52895414 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| aerodrome | WETH/EDEL | 7000 | 1,202,068 | 71,175.592639 | 52895414 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | WETH/WELL | 10000 | 1,198,772 | 1,133,547.877610 | 52895414 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome | USDC/NOCK | 3000 | 1,182,452 | 45.064898 | 52895414 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,181,611 | 483,702.994218 | 52895414 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,181,344 | 0.436589 | 52895414 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,160,044 | 1.106158 | 52895414 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |
| aerodrome_slipstream | msUSD/USDC | 500 | 1,158,653 | 0.886246 | 52895414 | `0x7501bc8Bb51616F79bfA524E464fb7B41f0B10fB` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,115,966 | 20,374,625.032721 | 52895414 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |

## Recherche d'opportunités
- Cycles : 1135 ; routes examinées : 24513730 ; candidats optimisés : 121251 ; net attendu > 0 : 61 ; dernier cycle 407.5 ms
- Rejets (moteur) : {'spread_below_threshold': 24149549, 'liquidity_below_min': 196437, 'negative_expected_net': 121190, 'pool_quarantined': 44720, 'borrow_bound_too_small': 1127, 'cycle_budget_exhausted': 505}
- Enregistrements de la session : 121248 ; net attendu > 0 : 61 ; simulés (eth_call de la vraie tx) : 5 (ok 0, échec 5) ; étiquettes ghost N+1 : 0/1 positives
- Décisions : {'REJECTED': 121248} ; motifs de rejet : {'below_safety_margin': 56, 'negative_expected_net': 121187, 'p_lower_below_threshold': 61, 'price_impact': 53, 'simulation_failed': 5, 'stale_data': 11}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52895105 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 27.179587 USDC | 0.010654 USDC | 0.000000 USDC | 0.005503 USDC | 0.005151 USDC (0.0047 €) | — | 1.90 | 0.024 (n=60) | REJECTED | below_safety_margin(5151<5435), p_lower_below_threshold(0.02<0.75) |
| 52895106 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 27.179587 USDC | 0.010654 USDC | 0.000000 USDC | 0.005503 USDC | 0.005151 USDC (0.0047 €) | — | 1.90 | 0.024 (n=60) | REJECTED | below_safety_margin(5151<5435), p_lower_below_threshold(0.02<0.75) |
| 52895106 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 27.179587 USDC | 0.010654 USDC | 0.000000 USDC | 0.005503 USDC | 0.005151 USDC (0.0047 €) | — | 1.90 | 0.024 (n=60) | REJECTED | below_safety_margin(5151<5435), p_lower_below_threshold(0.02<0.75) |
| 52895107 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 27.179587 USDC | 0.010654 USDC | 0.000000 USDC | 0.005503 USDC | 0.005151 USDC (0.0047 €) | — | 1.90 | 0.024 (n=60) | REJECTED | below_safety_margin(5151<5435), p_lower_below_threshold(0.02<0.75) |
| 52895221 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 9.789597 USDC | 0.008380 USDC | 0.000000 USDC | 0.007393 USDC | 0.000987 USDC (0.0009 €) | — | 1.01 | 0.287 (n=92) | REJECTED | below_safety_margin(987<1957), p_lower_below_threshold(0.29<0.75) |
| 52895221 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.004027 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0009 €) | — | 0.98 | 0.287 (n=92) | REJECTED | below_safety_margin(394716231352<805466920311), p_lower_below_threshold(0.29<0.75) |
| 52895221 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 9.518309 USDC | 0.007948 USDC | 0.000000 USDC | 0.007393 USDC | 0.000555 USDC (0.0005 €) | — | 0.58 | 0.119 (n=194) | REJECTED | below_safety_margin(555<1903), p_lower_below_threshold(0.12<0.75) |
| 52895221 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.003892 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0005 €) | — | 0.56 | 0.119 (n=194) | REJECTED | below_safety_margin(219342448525<778414563277), p_lower_below_threshold(0.12<0.75) |
| 52894627 | USDC→[aerodrome_slipstream]→AERO→[aerodrome]→fBOMB→[aerodrome]→USDC | 0.999999 USDC | 0.007019 USDC | 0.000000 USDC | 0.006689 USDC | 0.000330 USDC (0.0003 €) | — | 3.30 | 0.037 (n=117) | REJECTED | price_impact(205bps>150.0), simulation_failed:revert 0xa932492f, p_lower_below_threshold(0.04<0.75) |
| 52894628 | USDC→[aerodrome_slipstream]→AERO→[aerodrome]→fBOMB→[aerodrome]→USDC | 0.999999 USDC | 0.007019 USDC | 0.000000 USDC | 0.006689 USDC | 0.000330 USDC (0.0003 €) | — | 3.30 | 0.037 (n=117) | REJECTED | price_impact(205bps>150.0), simulation_failed:revert 0xa932492f, p_lower_below_threshold(0.04<0.75) |
| 52894629 | USDC→[aerodrome_slipstream]→AERO→[aerodrome]→fBOMB→[aerodrome]→USDC | 0.999999 USDC | 0.007019 USDC | 0.000000 USDC | 0.006689 USDC | 0.000330 USDC (0.0003 €) | — | 3.30 | 0.037 (n=117) | REJECTED | price_impact(205bps>150.0), simulation_failed:revert 0xa932492f, p_lower_below_threshold(0.04<0.75) |
| 52894631 | USDC→[aerodrome_slipstream]→AERO→[aerodrome]→fBOMB→[aerodrome]→USDC | 0.999999 USDC | 0.007019 USDC | 0.000000 USDC | 0.006689 USDC | 0.000330 USDC (0.0003 €) | — | 3.30 | 0.037 (n=117) | REJECTED | price_impact(205bps>150.0), simulation_failed:revert 0xa932492f, p_lower_below_threshold(0.04<0.75) |
| 52894623 | USDC→[aerodrome_slipstream]→AERO→[aerodrome]→fBOMB→[aerodrome]→USDC | 0.999999 USDC | 0.007015 USDC | 0.000000 USDC | 0.006689 USDC | 0.000326 USDC (0.0003 €) | — | 3.26 | 0.037 (n=116) | REJECTED | price_impact(205bps>150.0), simulation_failed:revert 0xa932492f, p_lower_below_threshold(0.04<0.75) |
| 52894618 | USDC→[uniswap_v3]→AERO→[aerodrome]→fBOMB→[aerodrome]→USDC | 0.999999 USDC | 0.006841 USDC | 0.000000 USDC | 0.006689 USDC | 0.000152 USDC (0.0001 €) | — | 1.52 | 0.101 (n=83) | REJECTED | below_safety_margin(152<199), price_impact(205bps>150.0), p_lower_below_threshold(0.10<0.75) |
| 52894619 | USDC→[uniswap_v3]→AERO→[aerodrome]→fBOMB→[aerodrome]→USDC | 0.999999 USDC | 0.006841 USDC | 0.000000 USDC | 0.006689 USDC | 0.000152 USDC (0.0001 €) | — | 1.52 | 0.101 (n=83) | REJECTED | below_safety_margin(152<199), price_impact(205bps>150.0), p_lower_below_threshold(0.10<0.75) |
| 52894622 | USDC→[uniswap_v3]→AERO→[aerodrome]→fBOMB→[aerodrome]→USDC | 0.999999 USDC | 0.006841 USDC | 0.000000 USDC | 0.006689 USDC | 0.000152 USDC (0.0001 €) | — | 1.52 | 0.101 (n=83) | REJECTED | below_safety_margin(152<199), stale_data(6973ms>4000.0), price_impact(205bps>150.0), p_lower_below_threshold(0.10<0.75) |
| 52894623 | USDC→[uniswap_v3]→AERO→[aerodrome]→fBOMB→[aerodrome]→USDC | 0.999999 USDC | 0.006841 USDC | 0.000000 USDC | 0.006689 USDC | 0.000152 USDC (0.0001 €) | — | 1.52 | 0.101 (n=83) | REJECTED | below_safety_margin(152<199), price_impact(205bps>150.0), p_lower_below_threshold(0.10<0.75) |
| 52894627 | USDC→[uniswap_v3]→AERO→[aerodrome]→fBOMB→[aerodrome]→USDC | 0.999999 USDC | 0.006841 USDC | 0.000000 USDC | 0.006689 USDC | 0.000152 USDC (0.0001 €) | — | 1.52 | 0.101 (n=83) | REJECTED | below_safety_margin(152<199), price_impact(205bps>150.0), p_lower_below_threshold(0.10<0.75) |
| 52894628 | USDC→[uniswap_v3]→AERO→[aerodrome]→fBOMB→[aerodrome]→USDC | 0.999999 USDC | 0.006841 USDC | 0.000000 USDC | 0.006689 USDC | 0.000152 USDC (0.0001 €) | — | 1.52 | 0.101 (n=83) | REJECTED | below_safety_margin(152<199), price_impact(205bps>150.0), p_lower_below_threshold(0.10<0.75) |
| 52894629 | USDC→[uniswap_v3]→AERO→[aerodrome]→fBOMB→[aerodrome]→USDC | 0.999999 USDC | 0.006841 USDC | 0.000000 USDC | 0.006689 USDC | 0.000152 USDC (0.0001 €) | — | 1.52 | 0.101 (n=83) | REJECTED | below_safety_margin(152<199), price_impact(205bps>150.0), p_lower_below_threshold(0.10<0.75) |
| 52894631 | USDC→[uniswap_v3]→AERO→[aerodrome]→fBOMB→[aerodrome]→USDC | 0.999999 USDC | 0.006841 USDC | 0.000000 USDC | 0.006689 USDC | 0.000152 USDC (0.0001 €) | — | 1.52 | 0.101 (n=83) | REJECTED | below_safety_margin(152<199), price_impact(205bps>150.0), p_lower_below_threshold(0.10<0.75) |
| 52894611 | USDC→[aerodrome_slipstream]→AERO→[aerodrome]→fBOMB→[aerodrome]→USDC | 0.999999 USDC | 0.006831 USDC | 0.000000 USDC | 0.006689 USDC | 0.000142 USDC (0.0001 €) | — | 1.42 | 0.101 (n=83) | REJECTED | below_safety_margin(142<199), stale_data(8966ms>4000.0), price_impact(205bps>150.0), p_lower_below_threshold(0.10<0.75) |
| 52894612 | USDC→[aerodrome_slipstream]→AERO→[aerodrome]→fBOMB→[aerodrome]→USDC | 0.999999 USDC | 0.006831 USDC | 0.000000 USDC | 0.006689 USDC | 0.000142 USDC (0.0001 €) | — | 1.42 | 0.101 (n=83) | REJECTED | below_safety_margin(142<199), price_impact(205bps>150.0), p_lower_below_threshold(0.10<0.75) |
| 52894613 | USDC→[aerodrome_slipstream]→AERO→[aerodrome]→fBOMB→[aerodrome]→USDC | 0.999999 USDC | 0.006831 USDC | 0.000000 USDC | 0.006689 USDC | 0.000142 USDC (0.0001 €) | — | 1.42 | 0.101 (n=83) | REJECTED | below_safety_margin(142<199), price_impact(205bps>150.0), p_lower_below_threshold(0.10<0.75) |
| 52894618 | USDC→[aerodrome_slipstream]→AERO→[aerodrome]→fBOMB→[aerodrome]→USDC | 0.999999 USDC | 0.006831 USDC | 0.000000 USDC | 0.006689 USDC | 0.000142 USDC (0.0001 €) | — | 1.42 | 0.101 (n=83) | REJECTED | below_safety_margin(142<199), price_impact(205bps>150.0), p_lower_below_threshold(0.10<0.75) |

## Fiabilité et décision
- Observations ghost : 1654 ; taux observé 0.101 ; borne inférieure crédible (0.9) 0.092 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 9.2% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
