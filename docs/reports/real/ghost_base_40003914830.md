# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-23T22:27:17+00:00 ; durée 230.82 min ; blocs 52995614 → 53002540 (6504 vus)

## Connexion
- Requêtes RPC : 79491 ; erreurs : 118 ; latence p50/p95 : 303.3/2,019.0 ms
- Rafraîchissements d'état : 6504 ; âge des données au dernier bloc : 2.74 s ; changements de frais LP observés (pools à frais dynamiques) : 9873
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 55309 ; cycles déclenchés par événement : 3954 ; avance médiane sur le rafraîchissement multicall : 897 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,397.96 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 546 pools, 317 jetons, 19488 routes
- Par DEX : uniswap_v3 138, aerodrome 222, aerodrome_slipstream 137, pancakeswap_v3 32, uniswap_v2 13, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 200 (rejetés 2) → 605 jetons ; pools candidats 3880 (énumérés 359, par paires 0), mesurés 548, sous le plancher de 10000.0 $ : 2 → gardés 546 (max 1500) ; prix des hubs : {'USDC': 1.0, 'DAI': 1.0, 'USDbC': 1.0, 'WETH': 2404.297357, 'AERO': 0.765849, 'cbBTC': 81434.30056}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 157,190,109 | 2,397.962333 | 53002541 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,573,394 | 0.029467 | 53002541 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 12,566,345 | 95.685172 | 53002541 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,264,197 | 0.029437 | 53002541 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| aerodrome | USDC/AERO | 3000 | 10,111,643 | 1.346378 | 53002541 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,771,215 | 0.000012 | 53002541 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 8,827,578 | 0.029452 | 53002541 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/USDC | 500 | 8,673,417 | 2,393.758456 | 53002541 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,135,062 | 0.001664 | 53002541 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 332 | 6,328,372 | 0.000012 | 53002541 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 150 | 5,564,649 | 2,393.625648 | 53002541 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,443,237 | 0.029462 | 53002541 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | USDC/cbBTC | 412 | 4,897,924 | 0.000012 | 53002541 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,543,369 | 2,393.737624 | 53002541 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,283,094 | 0.999388 | 53002541 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/USDC | 3000 | 4,223,300 | 2,399.570199 | 53002541 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome | WETH/KTA | 3000 | 3,982,743 | 34,344.540367 | 53002541 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | VIRTUAL/WETH | 10000 | 3,394,938 | 0.000274 | 53002541 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/USDT | 412 | 2,805,805 | 2,397.518049 | 53002541 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome_slipstream | WETH/VVV | 2733 | 2,524,305 | 95.710544 | 53002541 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,292,783 | 401.262517 | 53002541 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | WETH/FAI | 10000 | 2,183,289 | 1,223,014.013660 | 53002541 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome | WETH/AERO | 10000 | 2,035,811 | 3,218.162269 | 53002541 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,946,038 | 0.000000 | 53002541 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,928,285 | 0.000012 | 53002541 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v3 | XDP/USDC | 100 | 1,757,505 | 0.017750 | 53002541 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,744,689 | 0.000012 | 53002541 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,555,812 | 1.605727 | 53002541 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | WETH/AERO | 3000 | 1,512,685 | 3,221.354094 | 53002541 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,460,251 | 0.824389 | 53002541 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,405,107 | 13,607.824947 | 53002541 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,385,508 | 0.005034 | 53002541 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,296,073 | 0.000272 | 53002541 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,291,381 | 2,393.662463 | 53002541 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | DRB/WETH | 10000 | 1,262,217 | 0.000000 | 53002541 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | WETH/msETH (stable) | 500 | 1,255,208 | 2.309353 | 53002541 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome | USDC/SEND | 3000 | 1,227,434 | 64.498001 | 53002541 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,192,649 | 35,609,935.701366 | 53002541 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | WETH/WELL | 10000 | 1,169,166 | 1,108,212.811609 | 53002541 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,157,270 | 483,252.813396 | 53002541 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,141,604 | 16.326240 | 53002541 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | USDC/NOCK | 3000 | 1,134,579 | 48.670656 | 53002541 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome | WETH/EDEL | 7000 | 1,083,341 | 75,122.598796 | 53002541 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | USDC/VVV | 3000 | 1,068,416 | 0.039984 | 53002541 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,060,789 | 21,434,164.100116 | 53002541 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,041,119 | 16.935740 | 53002541 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 988,209 | 23.136213 | 53002541 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| uniswap_v3 | WETH/MORPHO | 3000 | 954,819 | 1,059.039280 | 53002541 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/USDC | 10000 | 939,243 | 2,390.810721 | 53002541 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | uXRP/WETH | 3000 | 913,783 | 0.000544 | 53002541 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 889,604 | 17.585645 | 53002541 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 883,852 | 0.000009 | 53002541 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v2 | WETH/USDC | 3000 | 858,862 | 2,390.805658 | 53002541 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| pancakeswap_v3 | QUID/USDC | 100 | 832,948 | 0.062600 | 53002541 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | weETH_04c0/WETH | 500 | 829,040 | 1.105789 | 53002541 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome | WETH/wstETH | 3000 | 811,866 | 0.803225 | 53002541 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | WETH/VVV | 10000 | 786,436 | 95.252668 | 53002541 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 778,007 | 0.653121 | 53002541 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 769,466 | 4,582,735.770558 | 53002541 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v2 | WETH/NPC | 3000 | 738,096 | 132,761.043236 | 53002541 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |

## Recherche d'opportunités
- Cycles : 10457 ; routes examinées : 203786016 ; candidats optimisés : 868064 ; net attendu > 0 : 159 ; dernier cycle 286.8 ms
- Rejets (moteur) : {'spread_below_threshold': 199779980, 'liquidity_below_min': 3126499, 'negative_expected_net': 867905, 'borrow_bound_too_small': 10456, 'cycle_budget_exhausted': 1017}
- Enregistrements de la session : 868064 ; net attendu > 0 : 159 ; simulés (eth_call de la vraie tx) : 5 (ok 2, échec 3) ; étiquettes ghost N+1 : 1/3 positives
- Décisions : {'REJECTED': 868064} ; motifs de rejet : {'below_safety_margin': 154, 'negative_expected_net': 867905, 'p_lower_below_threshold': 148, 'reliability_not_demonstrated': 11, 'simulation_failed': 3, 'stale_data': 14}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52997859 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.013052 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.1048 €) | — | 1.07 | 0.001 (n=7) | REJECTED | below_safety_margin(140<261), reliability_not_demonstrated |
| 52997859 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.013052 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.1048 €) | — | 1.07 | 0.001 (n=7) | REJECTED | below_safety_margin(140<261), reliability_not_demonstrated |
| 52997859 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.469736 WETH | 0.000051 WETH | 0.000000 WETH | 0.000003 WETH | 0.000047 WETH (0.1044 €) | — | 1.01 | 0.001 (n=7) | REJECTED | below_safety_margin(47310295624478<93947291756440), reliability_not_demonstrated |
| 52997859 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.469736 WETH | 0.000051 WETH | 0.000000 WETH | 0.000003 WETH | 0.000047 WETH (0.1044 €) | — | 1.01 | 0.001 (n=7) | REJECTED | below_safety_margin(47310295624478<93947291756440), reliability_not_demonstrated |
| 52997859 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 1,085.695509 USDC | 0.121282 USDC | 0.000000 USDC | 0.007951 USDC | 0.113331 USDC (0.1043 €) | — | 1.04 | 0.001 (n=7) | REJECTED | below_safety_margin(113331<217139), reliability_not_demonstrated |
| 52997859 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 1,085.695509 USDC | 0.121282 USDC | 0.000000 USDC | 0.007951 USDC | 0.113331 USDC (0.1043 €) | — | 1.04 | 0.001 (n=7) | REJECTED | below_safety_margin(113331<217139), reliability_not_demonstrated |
| 52997059 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 67.235756 USDC | 0.069204 USDC | 0.000000 USDC | 0.005568 USDC | 0.063636 USDC (0.0585 €) | — | 9.46 | 0.000 (n=48) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 52997045 | WETH→[pancakeswap_v3]→AERO→[aerodrome]→BRETT→[aerodrome_slipstream]→WETH | 0.011664 WETH | 0.000026 WETH | 0.000000 WETH | 0.000003 WETH | 0.000024 WETH (0.0519 €) | 0.000024 WETH | 20.17 | 0.001 (n=10) | REJECTED | reliability_not_demonstrated |
| 52997859 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.002747 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0120 €) | — | 0.58 | 0.121 (n=244) | REJECTED | below_safety_margin(16<54), p_lower_below_threshold(0.12<0.75) |
| 52997859 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.002747 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0120 €) | — | 0.58 | 0.121 (n=244) | REJECTED | below_safety_margin(16<54), p_lower_below_threshold(0.12<0.75) |
| 52997859 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.105070 WETH | 0.000008 WETH | 0.000000 WETH | 0.000003 WETH | 0.000005 WETH (0.0117 €) | — | 0.51 | 0.121 (n=244) | REJECTED | below_safety_margin(5310924181147<21013959391428), p_lower_below_threshold(0.12<0.75) |
| 52997859 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.105070 WETH | 0.000008 WETH | 0.000000 WETH | 0.000003 WETH | 0.000005 WETH (0.0117 €) | — | 0.51 | 0.121 (n=244) | REJECTED | below_safety_margin(5310924181147<21013959391428), p_lower_below_threshold(0.12<0.75) |
| 52997859 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 248.141202 USDC | 0.019649 USDC | 0.000000 USDC | 0.007223 USDC | 0.012426 USDC (0.0114 €) | — | 0.50 | 0.121 (n=244) | REJECTED | below_safety_margin(12426<49628), p_lower_below_threshold(0.12<0.75) |
| 52997859 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 248.141202 USDC | 0.019649 USDC | 0.000000 USDC | 0.007223 USDC | 0.012426 USDC (0.0114 €) | — | 0.50 | 0.121 (n=244) | REJECTED | below_safety_margin(12426<49628), p_lower_below_threshold(0.12<0.75) |
| 52997859 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→cbBTC | 0.001447 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0067 €) | — | 0.62 | 0.121 (n=244) | REJECTED | below_safety_margin(9<28), p_lower_below_threshold(0.12<0.75) |
| 52997859 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→cbBTC | 0.001447 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0067 €) | — | 0.62 | 0.121 (n=244) | REJECTED | below_safety_margin(9<28), p_lower_below_threshold(0.12<0.75) |
| 52997859 | WETH→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.047148 WETH | 0.000006 WETH | 0.000000 WETH | 0.000003 WETH | 0.000003 WETH (0.0066 €) | — | 0.63 | 0.121 (n=244) | REJECTED | below_safety_margin(2991842465210<9429652084597), p_lower_below_threshold(0.12<0.75) |
| 52997859 | WETH→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.047148 WETH | 0.000006 WETH | 0.000000 WETH | 0.000003 WETH | 0.000003 WETH (0.0066 €) | — | 0.63 | 0.121 (n=244) | REJECTED | below_safety_margin(2991842465210<9429652084597), p_lower_below_threshold(0.12<0.75) |
| 52997859 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 97.411872 USDC | 0.014255 USDC | 0.000000 USDC | 0.007223 USDC | 0.007032 USDC (0.0065 €) | — | 0.72 | 0.121 (n=244) | REJECTED | below_safety_margin(7032<19482), p_lower_below_threshold(0.12<0.75) |
| 52997859 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 97.411872 USDC | 0.014255 USDC | 0.000000 USDC | 0.007223 USDC | 0.007032 USDC (0.0065 €) | — | 0.72 | 0.121 (n=244) | REJECTED | below_safety_margin(7032<19482), p_lower_below_threshold(0.12<0.75) |
| 52997044 | WETH→[pancakeswap_v3]→AERO→[aerodrome]→BRETT→[aerodrome_slipstream]→WETH | 0.005039 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0045 €) | — | 4.06 | 0.008 (n=35) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.01<0.75) |
| 52997045 | WETH→[pancakeswap_v3]→AERO→[aerodrome]→BRETT→[aerodrome_slipstream]→WETH | 0.005039 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0045 €) | — | 4.06 | 0.008 (n=35) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.01<0.75) |
| 52997045 | WETH→[uniswap_v3]→AERO→[aerodrome]→BRETT→[aerodrome_slipstream]→WETH | 0.005007 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0042 €) | 0.000002 WETH | 3.77 | 0.032 (n=135) | REJECTED | p_lower_below_threshold(0.03<0.75) |
| 52999365 | USDC→[pancakeswap_v3]→ICNT→[uniswap_v3]→USDC | 24.635146 USDC | 0.009445 USDC | 0.000000 USDC | 0.005390 USDC | 0.004055 USDC (0.0037 €) | — | 1.65 | 0.020 (n=71) | REJECTED | below_safety_margin(4055<4927), p_lower_below_threshold(0.02<0.75) |
| 52999366 | USDC→[pancakeswap_v3]→ICNT→[uniswap_v3]→USDC | 24.635146 USDC | 0.009445 USDC | 0.000000 USDC | 0.005390 USDC | 0.004055 USDC (0.0037 €) | — | 1.65 | 0.020 (n=71) | REJECTED | below_safety_margin(4055<4927), p_lower_below_threshold(0.02<0.75) |

## Fiabilité et décision
- Observations ghost : 2052 ; taux observé 0.096 ; borne inférieure crédible (0.9) 0.088 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 8.8% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
