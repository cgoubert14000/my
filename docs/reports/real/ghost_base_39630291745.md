# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-21T18:19:15+00:00 ; durée 135.89 min ; blocs 52904622 → 52908701 (3977 vus)

## Connexion
- Requêtes RPC : 52694 ; erreurs : 8 ; latence p50/p95 : 381.1/854.3 ms
- Rafraîchissements d'état : 3977 ; âge des données au dernier bloc : 2.29 s ; changements de frais LP observés (pools à frais dynamiques) : 8215
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 44757 ; cycles déclenchés par événement : 2376 ; avance médiane sur le rafraîchissement multicall : 510 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,510.77 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 578 pools, 327 jetons, 21568 routes
- Par DEX : uniswap_v3 138, aerodrome 236, aerodrome_slipstream 156, pancakeswap_v3 31, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 207 (rejetés 2) → 612 jetons ; pools candidats 3876 (énumérés 394, par paires 0), mesurés 580, sous le plancher de 10000.0 $ : 2 → gardés 578 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2506.228815, 'AERO': 0.862155, 'cbBTC': 84485.636227}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 157,843,839 | 2,510.772486 | 52908701 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 38,113,095 | 1.158389 | 52908701 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 18,965,991 | 0.029674 | 52908701 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/VVV | 3000 | 18,122,106 | 92.653093 | 52908701 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,808,041 | 0.029715 | 52908701 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,668,680 | 0.029664 | 52908701 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,924,723 | 0.000012 | 52908701 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 8,909,353 | 2,516.781193 | 52908701 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome_slipstream | USDC/cbBTC | 436 | 8,551,956 | 0.000012 | 52908701 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome | WETH/USDC | 3000 | 8,473,029 | 2,510.578992 | 52908701 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | WETH/USDC | 564 | 7,615,237 | 2,516.057637 | 52908701 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | USDC/cbBTC | 336 | 7,439,620 | 0.000012 | 52908701 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,436,430 | 0.001678 | 52908701 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,704,611 | 0.029715 | 52908701 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | fBOMB/AERO | 10000 | 4,994,387 | 0.023059 | 52908701 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,613,390 | 2,515.967036 | 52908701 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | USDC/AERO | 10000 | 4,460,672 | 1.159829 | 52908701 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,285,958 | 1.000106 | 52908701 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,284,579 | 0.000278 | 52908701 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/USDT | 415 | 4,189,273 | 2,519.168755 | 52908701 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome | WETH/KTA | 3000 | 4,126,879 | 35,105.838001 | 52908701 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/wstETH | 90 | 3,516,512 | 0.802373 | 52908701 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome | WETH/AERO | 10000 | 3,424,712 | 2,901.426295 | 52908701 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | WETH/VVV | 2709 | 2,853,131 | 92.684180 | 52908701 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,800,439 | 386.222707 | 52908701 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | WETH/FAI | 10000 | 2,312,046 | 1,196,489.382095 | 52908701 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 2,302,132 | 0.915907 | 52908701 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,279,225 | 0.000012 | 52908701 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 2,165,889 | 0.000010 | 52908701 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 2,094,517 | 0.000012 | 52908701 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,027,089 | 1.383628 | 52908701 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| aerodrome_slipstream | WETH/MORPHO | 2715 | 2,009,604 | 1,051.000843 | 52908701 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,979,158 | 0.000000 | 52908701 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome | weETH_04c0/WETH | 500 | 1,956,043 | 1.105712 | 52908701 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome_slipstream | cbETH/WETH | 60 | 1,858,948 | 1.142097 | 52908701 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| uniswap_v3 | XDP/USDC | 100 | 1,814,920 | 0.019036 | 52908701 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,788,578 | 13,014.082749 | 52908701 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,738,789 | 15.839328 | 52908701 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | WETH/msETH (stable) | 500 | 1,729,826 | 2.312215 | 52908701 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | WETH/AERO | 3000 | 1,716,744 | 2,912.866440 | 52908701 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,708,216 | 1.493868 | 52908701 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,456,992 | 0.826661 | 52908701 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | EURC/USDC | 70 | 1,428,674 | 1.123843 | 52908701 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| aerodrome | fBOMB/USDC | 10000 | 1,418,599 | 0.019848 | 52908701 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,412,782 | 0.004846 | 52908701 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v3 | DRB/WETH | 10000 | 1,387,100 | 0.000000 | 52908701 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,366,680 | 0.000279 | 52908701 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | WETH/cbBTC | 3000 | 1,340,197 | 0.029680 | 52908701 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,305,451 | 2,516.153692 | 52908701 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,288,124 | 23.143008 | 52908701 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| aerodrome | WETH/WELL | 10000 | 1,283,255 | 1,037,892.303680 | 52908701 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/doginme | 10000 | 1,248,717 | 35,399,426.800340 | 52908701 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | USDC/SEND | 3000 | 1,232,141 | 64.006086 | 52908701 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome | WETH/EDEL | 7000 | 1,222,867 | 72,167.311263 | 52908701 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | USDC/NOCK | 3000 | 1,221,797 | 42.209359 | 52908701 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,218,511 | 484,632.650414 | 52908701 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,188,248 | 1.106158 | 52908701 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |
| aerodrome_slipstream | msUSD/USDC | 500 | 1,187,941 | 0.886486 | 52908701 | `0x7501bc8Bb51616F79bfA524E464fb7B41f0B10fB` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,176,191 | 0.436959 | 52908701 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,125,541 | 20,934,775.309326 | 52908701 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |

## Recherche d'opportunités
- Cycles : 6352 ; routes examinées : 136999936 ; candidats optimisés : 675815 ; net attendu > 0 : 147 ; dernier cycle 454.8 ms
- Rejets (moteur) : {'spread_below_threshold': 135147385, 'liquidity_below_min': 1168800, 'negative_expected_net': 675668, 'borrow_bound_too_small': 6340, 'cycle_budget_exhausted': 1421}
- Enregistrements de la session : 675815 ; net attendu > 0 : 147 ; simulés (eth_call de la vraie tx) : 8 (ok 1, échec 7) ; étiquettes ghost N+1 : 0/8 positives
- Décisions : {'REJECTED': 675815} ; motifs de rejet : {'below_safety_margin': 93, 'negative_expected_net': 675668, 'p_lower_below_threshold': 92, 'reliability_not_demonstrated': 55, 'simulation_failed': 7, 'stale_data': 9}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52904867 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH | 5.290395 WETH | 0.004687 WETH | 0.000000 WETH | 0.000003 WETH | 0.004684 WETH (10.8029 €) | — | 8.85 | 0.000 (n=26) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52904867 | USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 13,257.243552 USDC | 11.747487 USDC | 0.000000 USDC | 0.007596 USDC | 11.739891 USDC (10.8007 €) | — | 8.86 | 0.000 (n=26) | REJECTED | reliability_not_demonstrated |
| 52904867 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH | 4.690550 WETH | 0.004357 WETH | 0.000000 WETH | 0.000004 WETH | 0.004353 WETH (10.0396 €) | — | 9.28 | 0.000 (n=27) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52904867 | USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 11,757.060894 USDC | 10.919145 USDC | 0.000000 USDC | 0.010260 USDC | 10.908885 USDC (10.0362 €) | — | 9.28 | 0.000 (n=27) | REJECTED | reliability_not_demonstrated |
| 52904867 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→USDT→[aerodrome_slipstream]→WETH | 4.523217 WETH | 0.003930 WETH | 0.000000 WETH | 0.000003 WETH | 0.003927 WETH (9.0578 €) | — | 8.68 | 0.000 (n=26) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52904867 | USDC→[uniswap_v3]→USDT→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 11,336.129402 USDC | 9.852500 USDC | 0.000000 USDC | 0.008357 USDC | 9.844143 USDC (9.0566 €) | — | 8.68 | 0.000 (n=26) | REJECTED | reliability_not_demonstrated |
| 52904867 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→USDT→[aerodrome_slipstream]→WETH | 4.094311 WETH | 0.003734 WETH | 0.000000 WETH | 0.000004 WETH | 0.003730 WETH (8.6031 €) | — | 9.11 | 0.000 (n=27) | REJECTED | reliability_not_demonstrated |
| 52904867 | USDC→[uniswap_v3]→USDT→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 10,260.868308 USDC | 9.359500 USDC | 0.000000 USDC | 0.010640 USDC | 9.348860 USDC (8.6010 €) | — | 9.11 | 0.000 (n=27) | REJECTED | reliability_not_demonstrated |
| 52904867 | WETH→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH | 4.773284 WETH | 0.003527 WETH | 0.000000 WETH | 0.000003 WETH | 0.003524 WETH (8.1278 €) | — | 7.38 | 0.138 (n=86) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 52904867 | USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→USDC | 11,963.205563 USDC | 8.839237 USDC | 0.000000 USDC | 0.007596 USDC | 8.831641 USDC (8.1251 €) | — | 7.38 | 0.138 (n=86) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 52904867 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→USDT→[aerodrome_slipstream]→WETH | 4.026460 WETH | 0.002904 WETH | 0.000000 WETH | 0.000003 WETH | 0.002900 WETH (6.6900 €) | — | 7.20 | 0.138 (n=86) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 52904867 | USDC→[uniswap_v3]→USDT→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→USDC | 10,092.039463 USDC | 7.278144 USDC | 0.000000 USDC | 0.008357 USDC | 7.269787 USDC (6.6882 €) | — | 7.20 | 0.138 (n=86) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 52904867 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH | 2.498645 WETH | 0.002198 WETH | 0.000000 WETH | 0.000003 WETH | 0.002195 WETH (5.0618 €) | — | 8.78 | 0.000 (n=27) | REJECTED | reliability_not_demonstrated |
| 52904867 | USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 6,257.474670 USDC | 5.505138 USDC | 0.000000 USDC | 0.007976 USDC | 5.497162 USDC (5.0574 €) | — | 8.78 | 0.000 (n=27) | REJECTED | reliability_not_demonstrated |
| 52904867 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→USDT→[aerodrome_slipstream]→WETH | 2.295257 WETH | 0.001970 WETH | 0.000000 WETH | 0.000003 WETH | 0.001967 WETH (4.5360 €) | — | 8.57 | 0.000 (n=27) | REJECTED | reliability_not_demonstrated |
| 52904867 | USDC→[uniswap_v3]→USDT→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 5,748.469875 USDC | 4.935009 USDC | 0.000000 USDC | 0.008357 USDC | 4.926652 USDC (4.5325 €) | — | 8.57 | 0.000 (n=27) | REJECTED | reliability_not_demonstrated |
| 52904867 | USDC→[pancakeswap_v3]→USDT→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 3,663.050751 USDC | 4.493251 USDC | 0.000000 USDC | 0.010640 USDC | 4.482611 USDC (4.1240 €) | — | 12.24 | 0.000 (n=27) | REJECTED | reliability_not_demonstrated |
| 52904867 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→USDT→[aerodrome_slipstream]→WETH | 1.460331 WETH | 0.001792 WETH | 0.000000 WETH | 0.000004 WETH | 0.001787 WETH (4.1229 €) | — | 12.24 | 0.000 (n=27) | REJECTED | reliability_not_demonstrated |
| 52904867 | USDC→[pancakeswap_v3]→USDT→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 3,663.050751 USDC | 4.329451 USDC | 0.000000 USDC | 0.009879 USDC | 4.319572 USDC (3.9740 €) | — | 11.79 | 0.000 (n=27) | REJECTED | reliability_not_demonstrated |
| 52904867 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→USDT→[aerodrome_slipstream]→WETH | 1.459881 WETH | 0.001726 WETH | 0.000000 WETH | 0.000004 WETH | 0.001722 WETH (3.9721 €) | — | 11.80 | 0.000 (n=27) | REJECTED | reliability_not_demonstrated |
| 52904867 | USDC→[pancakeswap_v3]→USDT→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→USDC | 3,663.050751 USDC | 3.318625 USDC | 0.000000 USDC | 0.009879 USDC | 3.308746 USDC (3.0440 €) | — | 9.03 | 0.000 (n=27) | REJECTED | reliability_not_demonstrated |
| 52904867 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→USDT→[aerodrome_slipstream]→WETH | 1.460239 WETH | 0.001323 WETH | 0.000000 WETH | 0.000004 WETH | 0.001320 WETH (3.0435 €) | — | 9.04 | 0.000 (n=27) | REJECTED | reliability_not_demonstrated |
| 52904867 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→USDT→[aerodrome_slipstream]→WETH | 1.459884 WETH | 0.001316 WETH | 0.000000 WETH | 0.000004 WETH | 0.001312 WETH (3.0265 €) | — | 8.99 | 0.000 (n=27) | REJECTED | reliability_not_demonstrated |
| 52904867 | USDC→[pancakeswap_v3]→USDT→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 3,663.050751 USDC | 3.298919 USDC | 0.000000 USDC | 0.010260 USDC | 3.288659 USDC (3.0256 €) | — | 8.98 | 0.000 (n=27) | REJECTED | reliability_not_demonstrated |
| 52904867 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH | 1.246273 WETH | 0.001113 WETH | 0.000000 WETH | 0.000004 WETH | 0.001109 WETH (2.5578 €) | — | 8.90 | 0.000 (n=26) | REJECTED | reliability_not_demonstrated |

## Fiabilité et décision
- Observations ghost : 1717 ; taux observé 0.100 ; borne inférieure crédible (0.9) 0.091 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 9.1% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
