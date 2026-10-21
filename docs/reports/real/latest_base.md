# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-21T10:41:01+00:00 ; durée 15.3 min ; blocs 52894493 → 52894956 (316 vus)

## Connexion
- Requêtes RPC : 4730 ; erreurs : 0 ; latence p50/p95 : 291.4/1,075.6 ms
- Rafraîchissements d'état : 316 ; âge des données au dernier bloc : 2.31 s ; changements de frais LP observés (pools à frais dynamiques) : 767
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 3517 ; cycles déclenchés par événement : 205 ; avance médiane sur le rafraîchissement multicall : 712 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,451.18 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 578 pools, 326 jetons, 21598 routes
- Par DEX : uniswap_v3 138, aerodrome 235, aerodrome_slipstream 155, pancakeswap_v3 32, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 206 (rejetés 2) → 611 jetons ; pools candidats 3912 (énumérés 393, par paires 0), mesurés 581, sous le plancher de 10000.0 $ : 3 → gardés 578 (max 1500) ; prix des hubs : {'USDC': 1.0, 'DAI': 1.0, 'USDbC': 1.0, 'WETH': 2451.17881, 'AERO': 0.838921, 'cbBTC': 83216.410353}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 149,230,526 | 2,451.179010 | 52894956 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 38,327,414 | 1.190435 | 52894956 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| aerodrome | WETH/VVV | 3000 | 18,026,815 | 95.138071 | 52894956 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,525,102 | 0.029428 | 52894956 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 13,229,322 | 0.029458 | 52894956 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,430,887 | 0.029472 | 52894956 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| aerodrome_slipstream | USDC/cbBTC | 412 | 10,418,392 | 0.000012 | 52894956 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,966,859 | 0.000012 | 52894956 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 8,784,776 | 2,449.540398 | 52894956 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/USDC | 3000 | 8,462,866 | 2,451.053453 | 52894956 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | USDC/cbBTC | 334 | 8,187,098 | 0.000012 | 52894956 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,311,090 | 0.001668 | 52894956 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | WETH/USDC | 549 | 7,194,633 | 2,450.010410 | 52894956 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,615,994 | 0.029433 | 52894956 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | fBOMB/AERO | 10000 | 5,208,332 | 0.024844 | 52894956 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,728,334 | 0.000279 | 52894956 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,724,761 | 0.802395 | 52894956 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,447,385 | 2,450.162452 | 52894956 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,421,175 | 0.998741 | 52894956 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 4,048,216 | 34,773.752269 | 52894956 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | USDC/AERO | 10000 | 3,947,563 | 1.183610 | 52894956 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome | WETH/AERO | 10000 | 3,337,950 | 2,898.786498 | 52894956 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | WETH/USDT | 409 | 3,149,920 | 2,452.413247 | 52894956 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome_slipstream | WETH/VVV | 2712 | 2,761,222 | 95.108489 | 52894956 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,536,520 | 1.142088 | 52894956 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,347,411 | 398.073560 | 52894956 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,274,592 | 0.000012 | 52894956 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | WETH/FAI | 10000 | 2,245,393 | 1,209,742.010817 | 52894956 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | AERO/cbBTC | 2700 | 2,212,195 | 0.000010 | 52894956 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 2,079,099 | 0.000012 | 52894956 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,027,072 | 1.383640 | 52894956 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,954,238 | 0.000000 | 52894956 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome | weETH_04c0/WETH | 500 | 1,909,603 | 1.105697 | 52894956 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,820,098 | 13,531.257619 | 52894956 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | XDP/USDC | 100 | 1,808,251 | 0.019148 | 52894956 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 1,794,653 | 1,049.739233 | 52894956 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,720,159 | 0.916061 | 52894956 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| aerodrome | fBOMB/USDC | 10000 | 1,713,872 | 0.021420 | 52894956 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,710,848 | 1.490009 | 52894956 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome | WETH/msETH (stable) | 500 | 1,692,065 | 2.310993 | 52894956 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | WETH/AERO | 3000 | 1,673,899 | 2,915.458350 | 52894956 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,559,112 | 15.817293 | 52894956 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,458,172 | 0.826524 | 52894956 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | EURC/USDC | 73 | 1,399,460 | 1.122678 | 52894956 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,351,128 | 0.004793 | 52894956 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,336,213 | 0.000280 | 52894956 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| uniswap_v3 | DRB/WETH | 10000 | 1,325,133 | 0.000000 | 52894956 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | WETH/cbBTC | 3000 | 1,314,749 | 0.029472 | 52894956 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,288,805 | 2,449.528581 | 52894956 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,234,154 | 63.797536 | 52894956 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,226,666 | 34,790,527.077835 | 52894956 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,216,762 | 23.076903 | 52894956 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| aerodrome | WETH/EDEL | 7000 | 1,203,328 | 71,026.639926 | 52894956 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | WETH/WELL | 10000 | 1,198,773 | 1,133,547.877610 | 52894956 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome | USDC/NOCK | 3000 | 1,185,227 | 44.854075 | 52894956 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,181,613 | 483,701.112498 | 52894956 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,181,344 | 0.436589 | 52894956 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,160,044 | 1.106158 | 52894956 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |
| aerodrome_slipstream | msUSD/USDC | 500 | 1,158,653 | 0.886246 | 52894956 | `0x7501bc8Bb51616F79bfA524E464fb7B41f0B10fB` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,115,967 | 20,374,625.032721 | 52894956 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |

## Recherche d'opportunités
- Cycles : 520 ; routes examinées : 11230960 ; candidats optimisés : 40057 ; net attendu > 0 : 53 ; dernier cycle 87.5 ms
- Rejets (moteur) : {'spread_below_threshold': 11058022, 'liquidity_below_min': 87072, 'pool_quarantined': 44720, 'negative_expected_net': 40004, 'borrow_bound_too_small': 512, 'cycle_budget_exhausted': 505}
- Enregistrements de la session : 40054 ; net attendu > 0 : 53 ; simulés (eth_call de la vraie tx) : 5 (ok 0, échec 5) ; étiquettes ghost N+1 : 0/1 positives
- Décisions : {'REJECTED': 40054} ; motifs de rejet : {'below_safety_margin': 48, 'negative_expected_net': 40001, 'p_lower_below_threshold': 53, 'price_impact': 53, 'simulation_failed': 5, 'stale_data': 11}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
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
| 52894619 | WETH→[pancakeswap_v3]→AERO→[aerodrome]→fBOMB→[aerodrome]→WETH | 0.000408 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0001 €) | — | 1.07 | 0.048 (n=44) | REJECTED | below_safety_margin(43806040744<81593394651), price_impact(205bps>150.0), p_lower_below_threshold(0.05<0.75) |
| 52894611 | WETH→[pancakeswap_v3]→AERO→[aerodrome]→fBOMB→[aerodrome]→WETH | 0.000408 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0001 €) | — | 1.07 | 0.048 (n=44) | REJECTED | below_safety_margin(43798635962<81593394651), stale_data(8967ms>4000.0), price_impact(205bps>150.0), p_lower_below_threshold(0.05<0.75) |
| 52894612 | WETH→[pancakeswap_v3]→AERO→[aerodrome]→fBOMB→[aerodrome]→WETH | 0.000408 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0001 €) | — | 1.07 | 0.048 (n=44) | REJECTED | below_safety_margin(43798635962<81593394651), price_impact(205bps>150.0), p_lower_below_threshold(0.05<0.75) |
| 52894627 | WETH→[pancakeswap_v3]→AERO→[aerodrome]→fBOMB→[aerodrome]→WETH | 0.000408 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0001 €) | — | 1.07 | 0.048 (n=44) | REJECTED | below_safety_margin(43753278796<81593394651), price_impact(205bps>150.0), p_lower_below_threshold(0.05<0.75) |

## Fiabilité et décision
- Observations ghost : 1654 ; taux observé 0.101 ; borne inférieure crédible (0.9) 0.092 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 9.2% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
