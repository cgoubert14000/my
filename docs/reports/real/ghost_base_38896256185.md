# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-16T15:02:38+00:00 ; durée 189.41 min ; blocs 52681120 → 52686798 (5413 vus)

## Connexion
- Requêtes RPC : 74794 ; erreurs : 105 ; latence p50/p95 : 224.3/1,830.5 ms
- Rafraîchissements d'état : 5413 ; âge des données au dernier bloc : 2.73 s ; changements de frais LP observés (pools à frais dynamiques) : 15015
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 127807 ; cycles déclenchés par événement : 5010 ; avance médiane sur le rafraîchissement multicall : 1,380 ms
- Gaz : base fee 0.005501 gwei ; prix ETH (pool le plus profond) : 2,456.50 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 575 pools, 328 jetons, 21482 routes
- Par DEX : uniswap_v3 136, aerodrome 236 (quarantaine 2), aerodrome_slipstream 153, pancakeswap_v3 32, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 209 (rejetés 2) → 614 jetons ; pools candidats 3925 (énumérés 391, par paires 0), mesurés 577, sous le plancher de 10000.0 $ : 2 → gardés 575 (max 1500) ; prix des hubs : {'USDC': 1.0, 'DAI': 1.0, 'USDbC': 1.0, 'WETH': 2482.328501, 'AERO': 0.918334, 'cbBTC': 82582.444221}
- Pools en quarantaine : 2 — aerodrome:fBOMB/AERO@0xbBf71A: simulation failed ×5 (model/chain mismatch) — until block 52686851; aerodrome:fBOMB/USDC@0xFf8e0b: simulation failed ×5 (model/chain mismatch) — until block 52686851

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 147,578,203 | 2,456.496974 | 52686798 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 46,484,477 | 1.114926 | 52686798 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 500 | 18,572,257 | 0.029973 | 52686798 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 16,399,115 | 102.852760 | 52686798 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 11,713,985 | 0.030032 | 52686798 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,534,869 | 0.030046 | 52686798 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,765,653 | 0.000012 | 52686798 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 9,158,815 | 2,450.244661 | 52686798 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome_slipstream | USDC/cbBTC | 360 | 7,851,823 | 0.000012 | 52686798 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,222,911 | 0.001680 | 52686798 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | WETH/USDC | 952 | 6,996,322 | 2,450.732899 | 52686798 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | USDC/cbBTC | 568 | 6,579,705 | 0.000012 | 52686798 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome | WETH/USDC | 3000 | 5,463,457 | 2,456.439934 | 52686798 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome | fBOMB/AERO | 10000 | 5,437,586 | 0.024927 | 52686798 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,407,199 | 0.029972 | 52686798 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/superOETHb | 400 | 5,249,108 | 1.000855 | 52686798 | `0x6446021F4E396dA3df4235C62537431372195D38` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,910,038 | 0.802398 | 52686798 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,769,995 | 0.000279 | 52686798 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,426,784 | 2,450.294157 | 52686798 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,353,276 | 0.998890 | 52686798 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 4,065,081 | 34,635.183790 | 52686798 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/AERO | 10000 | 3,526,233 | 2,714.803201 | 52686798 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | cbETH/WETH | 60 | 3,049,273 | 1.141867 | 52686798 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,845,657 | 0.000012 | 52686798 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/VVV | 2775 | 2,652,077 | 102.886622 | 52686798 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | WETH/MORPHO | 2736 | 2,553,311 | 1,023.554481 | 52686798 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 2,543,688 | 0.000011 | 52686798 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,342,636 | 400.430411 | 52686798 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | WETH/FAI | 10000 | 2,304,327 | 1,153,641.231085 | 52686798 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | BNKR/WETH | 10000 | 2,116,210 | 0.000000 | 52686798 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,111,807 | 1.195904 | 52686798 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | WETH/USDT | 496 | 2,086,890 | 2,453.386818 | 52686798 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 2,068,119 | 15.369658 | 52686798 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,009,165 | 1.405359 | 52686798 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| aerodrome | fBOMB/USDC | 10000 | 1,851,448 | 0.022997 | 52686798 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| aerodrome_slipstream | USDC/AERO | 10000 | 1,823,616 | 1.107197 | 52686798 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| uniswap_v3 | XDP/USDC | 100 | 1,769,918 | 0.018668 | 52686798 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,768,904 | 0.000012 | 52686798 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | WETH/msETH (stable) | 500 | 1,697,677 | 2.309096 | 52686798 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | WETH/AERO | 3000 | 1,568,630 | 2,734.023394 | 52686798 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | WETH/AERO | 3048 | 1,540,563 | 2,733.735929 | 52686798 | `0x82321f3BEB69f503380D6B233857d5C43562e2D0` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,526,927 | 0.916551 | 52686798 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| aerodrome | weETH_04c0/WETH | 500 | 1,518,878 | 1.105492 | 52686798 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome_slipstream | EURC/USDC | 76 | 1,497,469 | 1.125141 | 52686798 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,458,432 | 0.823795 | 52686798 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,420,526 | 13,347.642339 | 52686798 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | DRB/WETH | 10000 | 1,379,095 | 0.000000 | 52686798 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,362,128 | 0.004793 | 52686798 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,339,138 | 0.000278 | 52686798 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,322,993 | 0.436008 | 52686798 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,259,047 | 23.386722 | 52686798 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| aerodrome | USDC/SEND | 3000 | 1,249,107 | 62.279233 | 52686798 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,219,288 | 35,449,290.457953 | 52686798 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,219,010 | 1.105605 | 52686798 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |
| aerodrome | WETH/cbBTC | 3000 | 1,218,012 | 0.030036 | 52686798 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,216,236 | 2,450.241484 | 52686798 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | WETH/WELL | 10000 | 1,210,661 | 1,116,458.246832 | 52686798 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,163,137 | 506,670.436529 | 52686798 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | USDC/NOCK | 3000 | 1,153,857 | 47.336138 | 52686798 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome | WETH/EDEL | 7000 | 1,144,566 | 80,228.024391 | 52686798 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |

## Recherche d'opportunités
- Cycles : 10422 ; routes examinées : 223885404 ; candidats optimisés : 1413824 ; net attendu > 0 : 1161 ; dernier cycle 232.7 ms
- Rejets (moteur) : {'spread_below_threshold': 219080528, 'liquidity_below_min': 2193370, 'negative_expected_net': 1412663, 'pool_quarantined': 1158532, 'unquotable': 26066, 'borrow_bound_too_small': 10407, 'cycle_budget_exhausted': 2677}
- Enregistrements de la session : 1413824 ; net attendu > 0 : 1161 ; simulés (eth_call de la vraie tx) : 121 (ok 30, échec 91) ; étiquettes ghost N+1 : 12/63 positives
- Décisions : {'REJECTED': 1413824} ; motifs de rejet : {'below_safety_margin': 683, 'negative_expected_net': 1412663, 'p_lower_below_threshold': 908, 'price_impact': 475, 'reliability_not_demonstrated': 253, 'sim_below_estimate': 4, 'simulated_net_nonpositive': 3, 'simulation_failed': 91, 'stale_data': 8}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52683619 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→VIRTUAL→[aerodrome]→cbBTC | 0.005432 cbBTC | 0.000010 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000010 cbBTC (0.7377 €) | — | 18.00 | 0.002 (n=4) | REJECTED | reliability_not_demonstrated |
| 52683619 | WETH→[aerodrome_slipstream]→VIRTUAL→[aerodrome]→cbBTC→[pancakeswap_v3]→WETH | 0.184099 WETH | 0.000328 WETH | 0.000000 WETH | 0.000003 WETH | 0.000325 WETH (0.7375 €) | — | 17.68 | 0.002 (n=4) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52683619 | cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome]→cbBTC | 0.004389 cbBTC | 0.000009 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000009 cbBTC (0.6683 €) | — | 20.18 | 0.002 (n=3) | REJECTED | reliability_not_demonstrated |
| 52683620 | cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome]→cbBTC | 0.004389 cbBTC | 0.000009 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000009 cbBTC (0.6683 €) | — | 20.18 | 0.002 (n=3) | REJECTED | reliability_not_demonstrated |
| 52683619 | USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome]→cbBTC→[aerodrome_slipstream]→USDC | 368.787596 USDC | 0.732861 USDC | 0.000000 USDC | 0.007083 USDC | 0.725778 USDC (0.6677 €) | — | 19.68 | 0.002 (n=4) | REJECTED | reliability_not_demonstrated |
| 52683620 | USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome]→cbBTC→[aerodrome_slipstream]→USDC | 368.787596 USDC | 0.732861 USDC | 0.000000 USDC | 0.007083 USDC | 0.725778 USDC (0.6677 €) | — | 19.68 | 0.002 (n=4) | REJECTED | reliability_not_demonstrated |
| 52683619 | cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome]→cbBTC | 0.004423 cbBTC | 0.000009 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000009 cbBTC (0.6661 €) | — | 19.96 | 0.002 (n=4) | REJECTED | reliability_not_demonstrated |
| 52683620 | cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome]→cbBTC | 0.004423 cbBTC | 0.000009 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000009 cbBTC (0.6661 €) | — | 19.96 | 0.002 (n=4) | REJECTED | reliability_not_demonstrated |
| 52683619 | USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome]→cbBTC→[aerodrome_slipstream]→USDC | 372.440191 USDC | 0.729818 USDC | 0.000000 USDC | 0.007083 USDC | 0.722735 USDC (0.6649 €) | — | 19.41 | 0.002 (n=4) | REJECTED | reliability_not_demonstrated |
| 52683620 | USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome]→cbBTC→[aerodrome_slipstream]→USDC | 372.440191 USDC | 0.729818 USDC | 0.000000 USDC | 0.007083 USDC | 0.722735 USDC (0.6649 €) | — | 19.41 | 0.002 (n=4) | REJECTED | reliability_not_demonstrated |
| 52683619 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome]→cbBTC | 0.004388 cbBTC | 0.000009 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000009 cbBTC (0.6645 €) | — | 20.08 | 0.036 (n=23) | REJECTED | reliability_not_demonstrated |
| 52683620 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome]→cbBTC | 0.004388 cbBTC | 0.000009 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000009 cbBTC (0.6645 €) | — | 20.08 | 0.036 (n=23) | REJECTED | reliability_not_demonstrated |
| 52683619 | USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome]→cbBTC→[pancakeswap_v3]→USDC | 373.580952 USDC | 0.728182 USDC | 0.000000 USDC | 0.007083 USDC | 0.721099 USDC (0.6634 €) | — | 19.30 | 0.001 (n=10) | REJECTED | reliability_not_demonstrated |
| 52683620 | USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome]→cbBTC→[pancakeswap_v3]→USDC | 373.580952 USDC | 0.728182 USDC | 0.000000 USDC | 0.007083 USDC | 0.721099 USDC (0.6634 €) | — | 19.30 | 0.001 (n=10) | REJECTED | reliability_not_demonstrated |
| 52683619 | cbBTC→[uniswap_v3]→USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome]→cbBTC | 0.004258 cbBTC | 0.000008 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000008 cbBTC (0.6223 €) | — | 19.38 | 0.002 (n=4) | REJECTED | reliability_not_demonstrated |
| 52683620 | cbBTC→[uniswap_v3]→USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome]→cbBTC | 0.004258 cbBTC | 0.000008 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000008 cbBTC (0.6223 €) | — | 19.38 | 0.002 (n=4) | REJECTED | reliability_not_demonstrated |
| 52683619 | USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome]→cbBTC→[uniswap_v3]→USDC | 356.229227 USDC | 0.682506 USDC | 0.000000 USDC | 0.007083 USDC | 0.675423 USDC (0.6214 €) | — | 18.96 | 0.002 (n=4) | REJECTED | reliability_not_demonstrated |
| 52683620 | USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome]→cbBTC→[uniswap_v3]→USDC | 356.229227 USDC | 0.682506 USDC | 0.000000 USDC | 0.007083 USDC | 0.675423 USDC (0.6214 €) | — | 18.96 | 0.002 (n=4) | REJECTED | reliability_not_demonstrated |
| 52683620 | WETH→[aerodrome_slipstream]→VIRTUAL→[aerodrome]→cbBTC→[pancakeswap_v3]→WETH | 0.162066 WETH | 0.000260 WETH | 0.000000 WETH | 0.000003 WETH | 0.000257 WETH (0.5831 €) | — | 15.87 | 0.002 (n=4) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52683620 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→VIRTUAL→[aerodrome]→cbBTC | 0.004828 cbBTC | 0.000008 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000008 cbBTC (0.5831 €) | — | 16.01 | 0.002 (n=4) | REJECTED | reliability_not_demonstrated |
| 52683619 | cbBTC→[uniswap_v3]→WETH→[aerodrome_slipstream]→VIRTUAL→[aerodrome]→cbBTC | 0.004932 cbBTC | 0.000008 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000008 cbBTC (0.5823 €) | — | 15.65 | 0.008 (n=39) | REJECTED | p_lower_below_threshold(0.01<0.75) |
| 52683619 | WETH→[aerodrome_slipstream]→VIRTUAL→[aerodrome]→cbBTC→[uniswap_v3]→WETH | 0.162065 WETH | 0.000260 WETH | 0.000000 WETH | 0.000003 WETH | 0.000257 WETH (0.5817 €) | — | 15.84 | 0.008 (n=39) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.01<0.75) |
| 52683619 | cbBTC→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→VIRTUAL→[aerodrome]→cbBTC | 0.004147 cbBTC | 0.000007 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000007 cbBTC (0.5371 €) | — | 17.17 | 0.008 (n=39) | REJECTED | p_lower_below_threshold(0.01<0.75) |
| 52683619 | WETH→[aerodrome_slipstream]→VIRTUAL→[aerodrome]→cbBTC→[aerodrome_slipstream]→WETH | 0.142392 WETH | 0.000240 WETH | 0.000000 WETH | 0.000003 WETH | 0.000237 WETH (0.5370 €) | — | 16.64 | 0.008 (n=39) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.01<0.75) |
| 52683619 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome]→cbBTC | 0.003608 cbBTC | 0.000007 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000007 cbBTC (0.5273 €) | — | 19.37 | 0.001 (n=10) | REJECTED | reliability_not_demonstrated |

## Fiabilité et décision
- Observations ghost : 576 ; taux observé 0.127 ; borne inférieure crédible (0.9) 0.110 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 11.0% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
