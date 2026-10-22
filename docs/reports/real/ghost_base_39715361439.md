# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-22T03:34:47+00:00 ; durée 18.45 min ; blocs 52924813 → 52925369 (536 vus)

## Connexion
- Requêtes RPC : 6850 ; erreurs : 0 ; latence p50/p95 : 399.7/1,141.3 ms
- Rafraîchissements d'état : 536 ; âge des données au dernier bloc : 3.3 s ; changements de frais LP observés (pools à frais dynamiques) : 923
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 10258 ; cycles déclenchés par événement : 463 ; avance médiane sur le rafraîchissement multicall : 1,029 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,439.85 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 566 pools, 325 jetons, 21116 routes
- Par DEX : uniswap_v3 137, aerodrome 233, aerodrome_slipstream 146, pancakeswap_v3 32, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 205 (rejetés 2) → 610 jetons ; pools candidats 3904 (énumérés 382, par paires 0), mesurés 569, sous le plancher de 10000.0 $ : 3 → gardés 566 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDbC': 1.0, 'USDC': 1.0, 'WETH': 2442.747144, 'AERO': 0.821241, 'cbBTC': 82764.497741}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 156,529,813 | 2,439.583741 | 52925369 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 25,489,641 | 1.220646 | 52925368 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| aerodrome | WETH/VVV | 3000 | 16,635,689 | 89.700556 | 52925369 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,401,163 | 0.029448 | 52925368 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,411,486 | 0.029404 | 52925368 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 9,792,469 | 0.029398 | 52925368 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,472,910 | 0.000012 | 52925369 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 8,746,481 | 2,433.476161 | 52925369 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/USDC | 3000 | 7,394,830 | 2,439.495597 | 52925369 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,258,163 | 0.001661 | 52925368 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 340 | 7,100,631 | 0.000012 | 52925369 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 654 | 6,586,776 | 2,432.787739 | 52925369 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | USDC/cbBTC | 448 | 5,994,185 | 0.000012 | 52925368 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,535,476 | 0.029446 | 52925369 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,601,871 | 2,432.420555 | 52925369 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,359,771 | 0.999956 | 52925368 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,080,154 | 0.000278 | 52925368 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome | WETH/KTA | 3000 | 4,041,777 | 34,561.335980 | 52925368 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDT | 418 | 2,898,414 | 2,436.812411 | 52925369 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome_slipstream | WETH/VVV | 2727 | 2,817,410 | 89.722659 | 52925368 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | WETH/AERO | 10000 | 2,507,295 | 2,976.966827 | 52925368 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,346,713 | 394.680083 | 52925369 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,259,796 | 0.000012 | 52925369 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | WETH/FAI | 10000 | 2,247,556 | 1,195,533.776576 | 52925368 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 2,091,594 | 0.000012 | 52925369 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,934,734 | 0.000000 | 52925368 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,794,148 | 0.018510 | 52925368 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome | weETH_04c0/WETH | 500 | 1,763,458 | 1.105712 | 52925368 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,703,434 | 1.495412 | 52925368 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | WETH/AERO | 3000 | 1,655,381 | 2,972.645850 | 52925368 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | WETH/msETH (stable) | 500 | 1,625,596 | 2.329429 | 52925368 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome | fBOMB/AERO | 10000 | 1,573,818 | 0.023325 | 52925368 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| uniswap_v2 | WETH/USDC | 3000 | 1,544,379 | 2,439.759598 | 52925369 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,457,057 | 0.826101 | 52925368 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,438,130 | 13,393.005455 | 52925368 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome_slipstream | WETH/wstETH | 90 | 1,379,756 | 0.802239 | 52925368 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| uniswap_v3 | DRB/WETH | 10000 | 1,374,027 | 0.000000 | 52925368 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,361,109 | 0.004862 | 52925368 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome | USDC/alUSDb (stable) | 500 | 1,349,463 | 1.422897 | 52925368 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,327,539 | 0.000276 | 52925368 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,297,423 | 16.215515 | 52925368 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,291,049 | 2,433.390089 | 52925369 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 1,281,813 | 0.000010 | 52925368 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | USDC/SEND | 3000 | 1,231,841 | 64.037314 | 52925368 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome | WETH/WELL | 10000 | 1,217,852 | 1,081,669.486840 | 52925368 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/doginme | 10000 | 1,213,205 | 35,458,267.717002 | 52925368 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | USDC/NOCK | 3000 | 1,191,303 | 44.398055 | 52925368 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,177,054 | 492,403.031955 | 52925368 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,173,246 | 23.134704 | 52925368 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| aerodrome | fBOMB/USDC | 10000 | 1,153,953 | 0.019354 | 52925368 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| aerodrome | WETH/EDEL | 7000 | 1,151,947 | 71,954.539414 | 52925368 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,086,842 | 21,166,261.097057 | 52925368 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | EURC/USDC | 70 | 1,074,296 | 1.125182 | 52925368 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| aerodrome | WETH/cbBTC | 3000 | 1,073,951 | 0.029409 | 52925368 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,068,799 | 0.915940 | 52925368 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,049,228 | 16.631443 | 52925369 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome_slipstream | USDC/AERO | 10000 | 997,711 | 1.212915 | 52925368 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| uniswap_v3 | USDC/VVV | 3000 | 997,085 | 0.036860 | 52925368 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/MORPHO | 3000 | 970,746 | 1,060.176172 | 52925368 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome_slipstream | USDC/USDT | 8 | 953,068 | 1.001384 | 52925369 | `0xa41Bc0AFfbA7Fd420d186b84899d7ab2aC57fcD1` |

## Recherche d'opportunités
- Cycles : 998 ; routes examinées : 21073768 ; candidats optimisés : 199929 ; net attendu > 0 : 139 ; dernier cycle 189.1 ms
- Rejets (moteur) : {'spread_below_threshold': 20616518, 'liquidity_below_min': 255273, 'negative_expected_net': 199790, 'cycle_budget_exhausted': 1050, 'borrow_bound_too_small': 998}
- Enregistrements de la session : 199929 ; net attendu > 0 : 139 ; simulés (eth_call de la vraie tx) : 1 (ok 0, échec 1) ; étiquettes ghost N+1 : 0/1 positives
- Décisions : {'REJECTED': 199929} ; motifs de rejet : {'below_safety_margin': 138, 'negative_expected_net': 199790, 'p_lower_below_threshold': 139, 'simulation_failed': 1}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52925059 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 34.487994 USDC | 0.017827 USDC | 0.000000 USDC | 0.005511 USDC | 0.012316 USDC (0.0113 €) | — | 3.57 | 0.003 (n=101) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 52924919 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.004174 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0017 €) | — | 1.76 | 0.258 (n=102) | REJECTED | below_safety_margin(734612464081<834874892483), p_lower_below_threshold(0.26<0.75) |
| 52924920 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.004174 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0017 €) | — | 1.76 | 0.258 (n=102) | REJECTED | below_safety_margin(734612464081<834874892483), p_lower_below_threshold(0.26<0.75) |
| 52924920 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.004174 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0017 €) | — | 1.76 | 0.258 (n=102) | REJECTED | below_safety_margin(734612464081<834874892483), p_lower_below_threshold(0.26<0.75) |
| 52924917 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.004174 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0016 €) | — | 1.76 | 0.258 (n=102) | REJECTED | below_safety_margin(733298530263<834874892483), p_lower_below_threshold(0.26<0.75) |
| 52924918 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.004174 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0016 €) | — | 1.76 | 0.258 (n=102) | REJECTED | below_safety_margin(733298530263<834874892483), p_lower_below_threshold(0.26<0.75) |
| 52924918 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.004174 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0016 €) | — | 1.75 | 0.258 (n=102) | REJECTED | below_safety_margin(731900614252<834874892483), p_lower_below_threshold(0.26<0.75) |
| 52924919 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.004174 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0016 €) | — | 1.75 | 0.258 (n=102) | REJECTED | below_safety_margin(731900614252<834874892483), p_lower_below_threshold(0.26<0.75) |
| 52924919 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 10.058377 USDC | 0.009160 USDC | 0.000000 USDC | 0.007391 USDC | 0.001769 USDC (0.0016 €) | — | 1.76 | 0.258 (n=102) | REJECTED | below_safety_margin(1769<2011), p_lower_below_threshold(0.26<0.75) |
| 52924920 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 10.058377 USDC | 0.009160 USDC | 0.000000 USDC | 0.007391 USDC | 0.001769 USDC (0.0016 €) | — | 1.76 | 0.258 (n=102) | REJECTED | below_safety_margin(1769<2011), p_lower_below_threshold(0.26<0.75) |
| 52924920 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 10.058377 USDC | 0.009160 USDC | 0.000000 USDC | 0.007391 USDC | 0.001769 USDC (0.0016 €) | — | 1.76 | 0.258 (n=102) | REJECTED | below_safety_margin(1769<2011), p_lower_below_threshold(0.26<0.75) |
| 52924917 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 10.058377 USDC | 0.009160 USDC | 0.000000 USDC | 0.007394 USDC | 0.001766 USDC (0.0016 €) | — | 1.76 | 0.258 (n=102) | REJECTED | below_safety_margin(1766<2011), p_lower_below_threshold(0.26<0.75) |
| 52924918 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 10.058377 USDC | 0.009160 USDC | 0.000000 USDC | 0.007394 USDC | 0.001766 USDC (0.0016 €) | — | 1.76 | 0.258 (n=102) | REJECTED | below_safety_margin(1766<2011), p_lower_below_threshold(0.26<0.75) |
| 52924918 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 10.058377 USDC | 0.009160 USDC | 0.000000 USDC | 0.007397 USDC | 0.001763 USDC (0.0016 €) | — | 1.75 | 0.258 (n=102) | REJECTED | below_safety_margin(1763<2011), p_lower_below_threshold(0.26<0.75) |
| 52924919 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 10.058377 USDC | 0.009160 USDC | 0.000000 USDC | 0.007397 USDC | 0.001763 USDC (0.0016 €) | — | 1.75 | 0.258 (n=102) | REJECTED | below_safety_margin(1763<2011), p_lower_below_threshold(0.26<0.75) |
| 52924930 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.004171 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0016 €) | — | 1.66 | 0.258 (n=102) | REJECTED | below_safety_margin(691761966427<834163431152), p_lower_below_threshold(0.26<0.75) |
| 52924930 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.004171 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0016 €) | — | 1.66 | 0.258 (n=102) | REJECTED | below_safety_margin(691761966427<834163431152), p_lower_below_threshold(0.26<0.75) |
| 52924928 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.004171 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0016 €) | — | 1.66 | 0.258 (n=102) | REJECTED | below_safety_margin(690546095607<834163431152), p_lower_below_threshold(0.26<0.75) |
| 52924928 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.004171 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0016 €) | — | 1.66 | 0.258 (n=102) | REJECTED | below_safety_margin(690546095607<834163431152), p_lower_below_threshold(0.26<0.75) |
| 52924929 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.004171 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0016 €) | — | 1.66 | 0.258 (n=102) | REJECTED | below_safety_margin(690546095607<834163431152), p_lower_below_threshold(0.26<0.75) |
| 52924929 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.004171 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0016 €) | — | 1.66 | 0.258 (n=102) | REJECTED | below_safety_margin(690546095607<834163431152), p_lower_below_threshold(0.26<0.75) |
| 52924931 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.004171 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0015 €) | — | 1.65 | 0.258 (n=102) | REJECTED | below_safety_margin(688238509523<834163431152), p_lower_below_threshold(0.26<0.75) |
| 52924931 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.004171 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0015 €) | — | 1.65 | 0.258 (n=102) | REJECTED | below_safety_margin(688238509523<834163431152), p_lower_below_threshold(0.26<0.75) |
| 52924932 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.004171 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0015 €) | — | 1.65 | 0.258 (n=102) | REJECTED | below_safety_margin(688238509523<834163431152), p_lower_below_threshold(0.26<0.75) |
| 52924930 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 10.027234 USDC | 0.009050 USDC | 0.000000 USDC | 0.007385 USDC | 0.001665 USDC (0.0015 €) | — | 1.66 | 0.258 (n=102) | REJECTED | below_safety_margin(1665<2005), p_lower_below_threshold(0.26<0.75) |

## Fiabilité et décision
- Observations ghost : 1799 ; taux observé 0.097 ; borne inférieure crédible (0.9) 0.088 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 8.8% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
