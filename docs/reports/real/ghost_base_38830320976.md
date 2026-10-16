# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-16T02:47:28+00:00 ; durée 126.27 min ; blocs 52660958 → 52664748 (3291 vus)

## Connexion
- Requêtes RPC : 38329 ; erreurs : 48 ; latence p50/p95 : 491.3/2,341.4 ms
- Rafraîchissements d'état : 3292 ; âge des données au dernier bloc : 1.41 s ; changements de frais LP observés (pools à frais dynamiques) : 8231
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 0 ; cycles déclenchés par événement : 0 ; avance médiane sur le rafraîchissement multicall : — ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,436.46 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 573 pools, 327 jetons, 21346 routes
- Par DEX : uniswap_v3 134, aerodrome 235, aerodrome_slipstream 155, pancakeswap_v3 31, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 208 (rejetés 2) → 613 jetons ; pools candidats 3922 (énumérés 392, par paires 0), mesurés 575, sous le plancher de 10000.0 $ : 2 → gardés 573 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2444.060646, 'AERO': 0.934005, 'cbBTC': 82314.094538}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 146,235,886 | 2,436.455531 | 52664748 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 47,114,080 | 1.073554 | 52664748 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 500 | 18,434,068 | 0.029734 | 52664748 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 16,680,102 | 97.727609 | 52664748 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 12,872,968 | 0.029674 | 52664748 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,539,608 | 0.029682 | 52664748 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,735,884 | 0.000012 | 52664748 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 9,114,276 | 2,440.470443 | 52664748 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome_slipstream | USDC/cbBTC | 340 | 8,066,210 | 0.000012 | 52664748 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,211,539 | 0.001677 | 52664748 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | WETH/USDC | 639 | 7,025,880 | 2,439.905330 | 52664748 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | USDC/cbBTC | 448 | 7,005,862 | 0.000012 | 52664748 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome_slipstream | USDC/AERO | 10000 | 6,631,178 | 1.081192 | 52664748 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome | fBOMB/AERO | 10000 | 5,511,246 | 0.024735 | 52664748 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome | WETH/USDC | 3000 | 5,433,372 | 2,438.468313 | 52664748 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,387,952 | 0.029741 | 52664748 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/superOETHb | 400 | 5,206,283 | 1.000855 | 52664748 | `0x6446021F4E396dA3df4235C62537431372195D38` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,870,241 | 0.802398 | 52664748 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,724,838 | 0.000278 | 52664748 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,426,980 | 2,439.492456 | 52664748 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,351,120 | 0.998877 | 52664748 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 4,017,243 | 34,888.648105 | 52664748 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/AERO | 10000 | 3,578,043 | 2,626.106593 | 52664748 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | WETH/USDT | 415 | 3,047,712 | 2,443.835808 | 52664748 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,874,710 | 401.205430 | 52664748 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,849,145 | 1.141809 | 52664748 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,842,416 | 0.000012 | 52664748 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/VVV | 2754 | 2,672,620 | 97.741167 | 52664748 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | AERO/cbBTC | 2700 | 2,464,596 | 0.000011 | 52664748 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | WETH/FAI | 10000 | 2,278,359 | 1,160,911.454912 | 52664748 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | WETH/MORPHO | 2703 | 2,256,689 | 1,008.685807 | 52664748 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,111,736 | 1.195936 | 52664748 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | BNKR/WETH | 10000 | 2,095,998 | 0.000000 | 52664748 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,008,461 | 1.403757 | 52664748 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,938,262 | 15.358129 | 52664748 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | fBOMB/USDC | 10000 | 1,836,845 | 0.023058 | 52664748 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| uniswap_v3 | XDP/USDC | 100 | 1,790,193 | 0.019008 | 52664748 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,776,239 | 0.000012 | 52664748 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | WETH/msETH (stable) | 500 | 1,681,678 | 2.309604 | 52664748 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,643,516 | 13,501.315653 | 52664748 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | WETH/AERO | 3000 | 1,575,511 | 2,621.945896 | 52664748 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,514,469 | 0.916551 | 52664748 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| aerodrome | weETH_04c0/WETH | 500 | 1,506,476 | 1.105492 | 52664748 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome_slipstream | WETH/AERO | 3008 | 1,475,905 | 2,622.149035 | 52664748 | `0x82321f3BEB69f503380D6B233857d5C43562e2D0` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,456,377 | 0.830051 | 52664748 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,363,490 | 0.004827 | 52664748 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v3 | DRB/WETH | 10000 | 1,359,457 | 0.000000 | 52664748 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome_slipstream | EURC/USDC | 73 | 1,349,950 | 1.121527 | 52664748 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,342,661 | 23.248217 | 52664748 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,324,276 | 0.000280 | 52664748 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | USDC/SEND | 3000 | 1,248,987 | 62.291240 | 52664748 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome | WETH/cbBTC | 3000 | 1,212,917 | 0.029673 | 52664748 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| uniswap_v3 | WETH/doginme | 10000 | 1,208,695 | 35,361,261.668762 | 52664748 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,208,578 | 1.105591 | 52664748 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,199,234 | 2,440.194252 | 52664748 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | WETH/WELL | 10000 | 1,186,409 | 1,143,664.079159 | 52664748 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome_slipstream | msUSD/USDC | 500 | 1,169,612 | 0.885950 | 52664748 | `0x7501bc8Bb51616F79bfA524E464fb7B41f0B10fB` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,168,705 | 496,823.388703 | 52664748 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,164,607 | 0.436271 | 52664748 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,131,309 | 13.720903 | 52664748 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |

## Recherche d'opportunités
- Cycles : 3291 ; routes examinées : 70249686 ; candidats optimisés : 491899 ; net attendu > 0 : 297 ; dernier cycle 509.4 ms
- Rejets (moteur) : {'spread_below_threshold': 69090051, 'liquidity_below_min': 650278, 'negative_expected_net': 491602, 'cycle_budget_exhausted': 14167, 'borrow_bound_too_small': 3291}
- Enregistrements de la session : 491899 ; net attendu > 0 : 297 ; simulés (eth_call de la vraie tx) : 9 (ok 6, échec 3) ; étiquettes ghost N+1 : 0/9 positives
- Décisions : {'REJECTED': 491899} ; motifs de rejet : {'below_safety_margin': 259, 'negative_expected_net': 491602, 'p_lower_below_threshold': 261, 'price_impact': 14, 'reliability_not_demonstrated': 36, 'simulation_failed': 3, 'stale_data': 38}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52662051 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.010627 WETH | 0.000026 WETH | 0.000000 WETH | 0.000003 WETH | 0.000023 WETH (0.0515 €) | 0.000023 WETH | 21.55 | 0.003 (n=2) | REJECTED | reliability_not_demonstrated |
| 52662051 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 25.934333 USDC | 0.063303 USDC | 0.000000 USDC | 0.007345 USDC | 0.055958 USDC (0.0515 €) | — | 21.58 | 0.003 (n=2) | REJECTED | reliability_not_demonstrated |
| 52662051 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 25.934333 USDC | 0.059170 USDC | 0.000000 USDC | 0.007345 USDC | 0.051825 USDC (0.0477 €) | — | 19.98 | 0.002 (n=3) | REJECTED | reliability_not_demonstrated |
| 52662051 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.010624 WETH | 0.000024 WETH | 0.000000 WETH | 0.000003 WETH | 0.000021 WETH (0.0477 €) | 0.000021 WETH | 19.97 | 0.002 (n=3) | REJECTED | reliability_not_demonstrated |
| 52662051 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.010605 WETH | 0.000024 WETH | 0.000000 WETH | 0.000003 WETH | 0.000021 WETH (0.0472 €) | 0.000021 WETH | 19.82 | 0.001 (n=7) | REJECTED | reliability_not_demonstrated |
| 52662051 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 25.934333 USDC | 0.058702 USDC | 0.000000 USDC | 0.007345 USDC | 0.051357 USDC (0.0472 €) | — | 19.80 | 0.001 (n=7) | REJECTED | reliability_not_demonstrated |
| 52662051 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.009873 WETH | 0.000021 WETH | 0.000000 WETH | 0.000003 WETH | 0.000018 WETH (0.0398 €) | — | 17.95 | 0.001 (n=7) | REJECTED | reliability_not_demonstrated |
| 52662051 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 23.994295 USDC | 0.050627 USDC | 0.000000 USDC | 0.007345 USDC | 0.043282 USDC (0.0398 €) | — | 18.04 | 0.001 (n=7) | REJECTED | reliability_not_demonstrated |
| 52662051 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.009804 WETH | 0.000020 WETH | 0.000000 WETH | 0.000003 WETH | 0.000017 WETH (0.0392 €) | — | 17.80 | 0.002 (n=3) | REJECTED | reliability_not_demonstrated |
| 52662051 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 23.848658 USDC | 0.049957 USDC | 0.000000 USDC | 0.007345 USDC | 0.042612 USDC (0.0392 €) | — | 17.87 | 0.002 (n=3) | REJECTED | reliability_not_demonstrated |
| 52662051 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.009411 WETH | 0.000019 WETH | 0.000000 WETH | 0.000003 WETH | 0.000016 WETH (0.0357 €) | — | 16.90 | 0.002 (n=3) | REJECTED | reliability_not_demonstrated |
| 52662051 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 22.901658 USDC | 0.046164 USDC | 0.000000 USDC | 0.007345 USDC | 0.038819 USDC (0.0357 €) | — | 16.95 | 0.002 (n=3) | REJECTED | reliability_not_demonstrated |
| 52662051 | WETH→[sushiswap_v3]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.009123 WETH | 0.000018 WETH | 0.000000 WETH | 0.000003 WETH | 0.000015 WETH (0.0341 €) | — | 16.63 | 0.002 (n=3) | REJECTED | reliability_not_demonstrated |
| 52662051 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[sushiswap_v3]→USDC | 22.150661 USDC | 0.044370 USDC | 0.000000 USDC | 0.007345 USDC | 0.037025 USDC (0.0341 €) | — | 16.72 | 0.002 (n=3) | REJECTED | reliability_not_demonstrated |
| 52662051 | WETH→[uniswap_v2]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.007075 WETH | 0.000011 WETH | 0.000000 WETH | 0.000003 WETH | 0.000008 WETH (0.0184 €) | — | 11.58 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52662051 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[uniswap_v2]→USDC | 17.138973 USDC | 0.026553 USDC | 0.000000 USDC | 0.006586 USDC | 0.019967 USDC (0.0184 €) | — | 11.65 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52662051 | WETH→[aerodrome]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.003384 WETH | 0.000006 WETH | 0.000000 WETH | 0.000003 WETH | 0.000003 WETH (0.0069 €) | — | 9.01 | 0.016 (n=18) | REJECTED | reliability_not_demonstrated |
| 52662051 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[aerodrome]→USDC | 8.269195 USDC | 0.014409 USDC | 0.000000 USDC | 0.007008 USDC | 0.007401 USDC (0.0068 €) | — | 8.95 | 0.016 (n=18) | REJECTED | reliability_not_demonstrated |
| 52662016 | WETH→[aerodrome_slipstream]→VIRTUAL→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.028765 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0042 €) | — | 0.65 | 0.077 (n=47) | REJECTED | below_safety_margin(1858338591797<5752973554803), p_lower_below_threshold(0.08<0.75) |
| 52662017 | WETH→[aerodrome_slipstream]→VIRTUAL→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.028765 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0042 €) | — | 0.65 | 0.077 (n=47) | REJECTED | below_safety_margin(1858338591797<5752973554803), p_lower_below_threshold(0.08<0.75) |
| 52662016 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→VIRTUAL→[pancakeswap_v3]→USDC | 71.018303 USDC | 0.011885 USDC | 0.000000 USDC | 0.007346 USDC | 0.004539 USDC (0.0042 €) | — | 0.64 | 0.077 (n=47) | REJECTED | below_safety_margin(4539<14203), p_lower_below_threshold(0.08<0.75) |
| 52662017 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→VIRTUAL→[pancakeswap_v3]→USDC | 71.018303 USDC | 0.011885 USDC | 0.000000 USDC | 0.007346 USDC | 0.004539 USDC (0.0042 €) | — | 0.64 | 0.077 (n=47) | REJECTED | below_safety_margin(4539<14203), p_lower_below_threshold(0.08<0.75) |
| 52663899 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 11.339197 USDC | 0.011188 USDC | 0.000000 USDC | 0.007326 USDC | 0.003862 USDC (0.0036 €) | 0.003862 USDC | 3.41 | 0.131 (n=52) | REJECTED | p_lower_below_threshold(0.13<0.75) |
| 52663899 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.004647 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0035 €) | 0.000002 WETH | 3.41 | 0.131 (n=52) | REJECTED | p_lower_below_threshold(0.13<0.75) |
| 52662016 | WETH→[aerodrome_slipstream]→VIRTUAL→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.027847 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0026 €) | — | 0.42 | 0.077 (n=47) | REJECTED | below_safety_margin(1176806255801<5569339749629), p_lower_below_threshold(0.08<0.75) |

## Fiabilité et décision
- Observations ghost : 428 ; taux observé 0.136 ; borne inférieure crédible (0.9) 0.116 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 11.6% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
