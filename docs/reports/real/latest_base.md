# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-21T10:47:05+00:00 ; durée 21.37 min ; blocs 52894493 → 52895138 (497 vus)

## Connexion
- Requêtes RPC : 7186 ; erreurs : 0 ; latence p50/p95 : 275.4/868.0 ms
- Rafraîchissements d'état : 498 ; âge des données au dernier bloc : 1.95 s ; changements de frais LP observés (pools à frais dynamiques) : 1115
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 5484 ; cycles déclenchés par événement : 328 ; avance médiane sur le rafraîchissement multicall : 537 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,451.18 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 578 pools, 326 jetons, 21598 routes
- Par DEX : uniswap_v3 138, aerodrome 235, aerodrome_slipstream 155, pancakeswap_v3 32, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 206 (rejetés 2) → 611 jetons ; pools candidats 3912 (énumérés 393, par paires 0), mesurés 581, sous le plancher de 10000.0 $ : 3 → gardés 578 (max 1500) ; prix des hubs : {'USDC': 1.0, 'DAI': 1.0, 'USDbC': 1.0, 'WETH': 2451.17881, 'AERO': 0.838921, 'cbBTC': 83216.410353}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 149,230,114 | 2,451.179009 | 52895138 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 38,396,605 | 1.186148 | 52895138 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| aerodrome | WETH/VVV | 3000 | 18,041,157 | 95.073445 | 52895138 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,523,293 | 0.029440 | 52895138 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 14,663,398 | 0.029458 | 52895138 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,434,914 | 0.029472 | 52895138 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,965,464 | 0.000012 | 52895138 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome_slipstream | USDC/cbBTC | 496 | 9,721,582 | 0.000012 | 52895138 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | WETH/USDC | 500 | 8,784,839 | 2,455.326384 | 52895138 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/USDC | 3000 | 8,462,866 | 2,451.099026 | 52895138 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | USDC/cbBTC | 346 | 7,426,593 | 0.000012 | 52895138 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,308,897 | 0.001669 | 52895138 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | WETH/USDC | 669 | 7,068,433 | 2,454.763799 | 52895138 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,615,344 | 0.029450 | 52895138 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | fBOMB/AERO | 10000 | 5,217,625 | 0.024844 | 52895138 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome_slipstream | WETH/USDT | 436 | 5,114,823 | 2,458.118740 | 52895138 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,728,334 | 0.000279 | 52895138 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,724,209 | 0.802395 | 52895138 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,437,584 | 2,454.438506 | 52895138 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,419,370 | 0.998741 | 52895138 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 4,048,371 | 34,771.083097 | 52895138 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | USDC/AERO | 10000 | 3,949,818 | 1.183610 | 52895138 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome | WETH/AERO | 10000 | 3,343,962 | 2,898.787807 | 52895138 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,806,025 | 397.833710 | 52895138 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | WETH/VVV | 2739 | 2,761,985 | 94.956544 | 52895138 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,536,520 | 1.142088 | 52895138 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| aerodrome_slipstream | AERO/cbBTC | 2700 | 2,354,810 | 0.000010 | 52895138 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,277,898 | 0.000012 | 52895138 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | WETH/FAI | 10000 | 2,245,393 | 1,209,742.010817 | 52895138 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 2,078,634 | 0.000012 | 52895138 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,027,072 | 1.383640 | 52895138 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,954,238 | 0.000000 | 52895138 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome | weETH_04c0/WETH | 500 | 1,909,603 | 1.105697 | 52895138 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| uniswap_v3 | XDP/USDC | 100 | 1,809,892 | 0.019180 | 52895138 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,720,159 | 0.916061 | 52895138 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| aerodrome | fBOMB/USDC | 10000 | 1,713,897 | 0.021420 | 52895138 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,710,848 | 1.490009 | 52895138 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome | WETH/msETH (stable) | 500 | 1,692,065 | 2.310993 | 52895138 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | WETH/AERO | 3000 | 1,675,906 | 2,910.063881 | 52895138 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,664,783 | 13,526.556742 | 52895138 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,567,129 | 15.817293 | 52895138 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,458,172 | 0.826524 | 52895138 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | EURC/USDC | 70 | 1,399,472 | 1.122693 | 52895138 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,351,128 | 0.004793 | 52895138 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,336,216 | 0.000280 | 52895138 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| uniswap_v3 | DRB/WETH | 10000 | 1,325,134 | 0.000000 | 52895138 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | WETH/cbBTC | 3000 | 1,314,480 | 0.029472 | 52895138 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,288,823 | 2,455.317663 | 52895138 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,234,154 | 63.797536 | 52895138 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,226,666 | 34,790,527.077835 | 52895138 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,216,762 | 23.076897 | 52895138 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| aerodrome | WETH/EDEL | 7000 | 1,201,549 | 71,237.085568 | 52895138 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | WETH/WELL | 10000 | 1,198,773 | 1,133,547.877610 | 52895138 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome | USDC/NOCK | 3000 | 1,182,452 | 45.064899 | 52895138 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,181,613 | 483,701.112498 | 52895138 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,181,344 | 0.436589 | 52895138 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,160,044 | 1.106158 | 52895138 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |
| aerodrome_slipstream | msUSD/USDC | 500 | 1,158,653 | 0.886246 | 52895138 | `0x7501bc8Bb51616F79bfA524E464fb7B41f0B10fB` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,115,967 | 20,374,625.032721 | 52895138 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | WETH/msETH | 500 | 1,067,139 | 1.132372 | 52895138 | `0x74F72788F4814D7fF3C49B44684aa98Eee140C0E` |

## Recherche d'opportunités
- Cycles : 825 ; routes examinées : 17818350 ; candidats optimisés : 77961 ; net attendu > 0 : 57 ; dernier cycle 152.6 ms
- Rejets (moteur) : {'spread_below_threshold': 17548680, 'liquidity_below_min': 145666, 'negative_expected_net': 77904, 'pool_quarantined': 44720, 'borrow_bound_too_small': 818, 'cycle_budget_exhausted': 505}
- Enregistrements de la session : 77961 ; net attendu > 0 : 57 ; simulés (eth_call de la vraie tx) : 5 (ok 0, échec 5) ; étiquettes ghost N+1 : 0/1 positives
- Décisions : {'REJECTED': 77961} ; motifs de rejet : {'below_safety_margin': 52, 'negative_expected_net': 77904, 'p_lower_below_threshold': 57, 'price_impact': 53, 'simulation_failed': 5, 'stale_data': 11}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52895105 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 27.179587 USDC | 0.010654 USDC | 0.000000 USDC | 0.005503 USDC | 0.005151 USDC (0.0047 €) | — | 1.90 | 0.024 (n=60) | REJECTED | below_safety_margin(5151<5435), p_lower_below_threshold(0.02<0.75) |
| 52895106 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 27.179587 USDC | 0.010654 USDC | 0.000000 USDC | 0.005503 USDC | 0.005151 USDC (0.0047 €) | — | 1.90 | 0.024 (n=60) | REJECTED | below_safety_margin(5151<5435), p_lower_below_threshold(0.02<0.75) |
| 52895106 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 27.179587 USDC | 0.010654 USDC | 0.000000 USDC | 0.005503 USDC | 0.005151 USDC (0.0047 €) | — | 1.90 | 0.024 (n=60) | REJECTED | below_safety_margin(5151<5435), p_lower_below_threshold(0.02<0.75) |
| 52895107 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 27.179587 USDC | 0.010654 USDC | 0.000000 USDC | 0.005503 USDC | 0.005151 USDC (0.0047 €) | — | 1.90 | 0.024 (n=60) | REJECTED | below_safety_margin(5151<5435), p_lower_below_threshold(0.02<0.75) |
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
| 52894619 | USDC→[aerodrome_slipstream]→AERO→[aerodrome]→fBOMB→[aerodrome]→USDC | 0.999999 USDC | 0.006831 USDC | 0.000000 USDC | 0.006689 USDC | 0.000142 USDC (0.0001 €) | — | 1.42 | 0.101 (n=83) | REJECTED | below_safety_margin(142<199), price_impact(205bps>150.0), p_lower_below_threshold(0.10<0.75) |
| 52894622 | USDC→[aerodrome_slipstream]→AERO→[aerodrome]→fBOMB→[aerodrome]→USDC | 0.999999 USDC | 0.006831 USDC | 0.000000 USDC | 0.006689 USDC | 0.000142 USDC (0.0001 €) | — | 1.42 | 0.101 (n=83) | REJECTED | below_safety_margin(142<199), stale_data(6974ms>4000.0), price_impact(205bps>150.0), p_lower_below_threshold(0.10<0.75) |
| 52894613 | WETH→[pancakeswap_v3]→AERO→[aerodrome]→fBOMB→[aerodrome]→WETH | 0.000408 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0001 €) | — | 1.07 | 0.048 (n=44) | REJECTED | below_safety_margin(43806040744<81593394651), price_impact(205bps>150.0), p_lower_below_threshold(0.05<0.75) |
| 52894618 | WETH→[pancakeswap_v3]→AERO→[aerodrome]→fBOMB→[aerodrome]→WETH | 0.000408 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0001 €) | — | 1.07 | 0.048 (n=44) | REJECTED | below_safety_margin(43806040744<81593394651), price_impact(205bps>150.0), p_lower_below_threshold(0.05<0.75) |

## Fiabilité et décision
- Observations ghost : 1654 ; taux observé 0.101 ; borne inférieure crédible (0.9) 0.092 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 9.2% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
