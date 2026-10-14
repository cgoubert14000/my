# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-14T08:59:35+00:00 ; durée 309.51 min ; blocs 52580225 → 52589507 (9075 vus)

## Connexion
- Requêtes RPC : 119456 ; erreurs : 13 ; latence p50/p95 : 212.0/1,185.7 ms
- Rafraîchissements d'état : 9075 ; âge des données au dernier bloc : 2.89 s ; changements de frais LP observés (pools à frais dynamiques) : 14101
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 261404 ; cycles déclenchés par événement : 8419 ; avance médiane sur le rafraîchissement multicall : 608 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,509.01 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 582 pools, 328 jetons, 21942 routes
- Par DEX : uniswap_v3 141, aerodrome 236, aerodrome_slipstream 156, pancakeswap_v3 32, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 208 (rejetés 2) → 613 jetons ; pools candidats 3923 (énumérés 393, par paires 0), mesurés 584, sous le plancher de 10000.0 $ : 2 → gardés 582 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDbC': 1.0, 'USDC': 1.0, 'WETH': 2513.126375, 'AERO': 0.908483, 'cbBTC': 83773.517368}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 150,016,996 | 2,509.012261 | 52589508 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 41,987,773 | 1.106926 | 52589508 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 500 | 18,360,060 | 0.030046 | 52589508 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 16,344,763 | 108.210420 | 52589508 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 15,489,324 | 0.030049 | 52589508 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,725,242 | 0.030064 | 52589508 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| aerodrome_slipstream | WETH/USDC | 654 | 9,420,053 | 2,504.287704 | 52589508 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| uniswap_v3 | WETH/USDC | 500 | 9,414,929 | 2,505.132882 | 52589508 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,312,964 | 0.000012 | 52589508 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome | WETH/USDC | 3000 | 9,124,669 | 2,509.369598 | 52589508 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | USDC/cbBTC | 336 | 8,238,727 | 0.000012 | 52589508 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,343,758 | 0.001675 | 52589508 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 424 | 6,922,943 | 0.000012 | 52589508 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome_slipstream | USDC/AERO | 10000 | 6,451,484 | 1.099888 | 52589508 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,578,858 | 0.030035 | 52589508 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/superOETHb | 400 | 5,541,606 | 1.000859 | 52589508 | `0x6446021F4E396dA3df4235C62537431372195D38` |
| aerodrome | fBOMB/AERO | 10000 | 5,449,389 | 0.026735 | 52589508 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,789,783 | 0.000281 | 52589508 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,737,412 | 0.802386 | 52589508 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,519,494 | 2,504.150990 | 52589508 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,419,646 | 0.999381 | 52589508 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 4,116,842 | 35,228.601718 | 52589508 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/AERO | 10000 | 3,724,880 | 2,772.876123 | 52589508 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | cbETH/WETH | 60 | 3,035,592 | 1.141618 | 52589508 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,868,578 | 0.000012 | 52589508 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,805,014 | 404.771623 | 52589508 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | WETH/VVV | 2742 | 2,635,414 | 108.242191 | 52589508 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 2,587,465 | 0.000011 | 52589508 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | WETH/FAI | 10000 | 2,456,403 | 1,059,089.868450 | 52589508 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | WETH/USDT | 421 | 2,444,444 | 2,507.507467 | 52589508 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 2,174,209 | 1,069.053324 | 52589508 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,116,960 | 1.189905 | 52589508 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | BNKR/WETH | 10000 | 2,112,313 | 0.000000 | 52589508 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome | fBOMB/USDbC | 10000 | 2,040,125 | 0.024088 | 52589508 | `0xC395664B295ed5bf1D249Ae8be9740655AA174ef` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,973,862 | 15.659057 | 52589508 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,949,201 | 0.916707 | 52589508 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| aerodrome | USDC/alUSDb (stable) | 500 | 1,859,284 | 1.372626 | 52589508 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| uniswap_v3 | XDP/USDC | 100 | 1,817,501 | 0.019731 | 52589508 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,708,110 | 0.000012 | 52589508 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | WETH/msETH (stable) | 500 | 1,681,909 | 2.306591 | 52589508 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,676,216 | 13,469.471789 | 52589508 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | WETH/AERO | 3000 | 1,570,456 | 2,773.758228 | 52589508 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | weETH_04c0/WETH | 500 | 1,551,246 | 1.105776 | 52589508 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,460,783 | 0.831749 | 52589508 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | DRB/WETH | 10000 | 1,460,313 | 0.000000 | 52589508 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,406,854 | 0.000279 | 52589508 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,398,396 | 0.004863 | 52589508 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | WETH/AERO | 3000 | 1,393,902 | 2,771.280205 | 52589508 | `0x82321f3BEB69f503380D6B233857d5C43562e2D0` |
| aerodrome_slipstream | EURC/USDC | 70 | 1,368,948 | 1.119665 | 52589508 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| aerodrome_slipstream | WETH/msETH | 500 | 1,365,494 | 1.131481 | 52589508 | `0x74F72788F4814D7fF3C49B44684aa98Eee140C0E` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,308,890 | 23.420291 | 52589508 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,268,054 | 2,505.135021 | 52589508 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome_slipstream | msUSD/USDC | 500 | 1,258,403 | 0.886407 | 52589508 | `0x7501bc8Bb51616F79bfA524E464fb7B41f0B10fB` |
| uniswap_v3 | WETH/doginme | 10000 | 1,257,057 | 34,607,063.116792 | 52589508 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | USDC/SEND | 3000 | 1,247,679 | 62.421881 | 52589508 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,242,887 | 1.105594 | 52589508 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |
| aerodrome | WETH/EDEL | 7000 | 1,219,472 | 72,906.123027 | 52589508 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,209,089 | 483,539.485072 | 52589508 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | WETH/WELL | 10000 | 1,192,255 | 1,200,896.863660 | 52589508 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,167,820 | 0.436887 | 52589508 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |

## Recherche d'opportunités
- Cycles : 17493 ; routes examinées : 383831406 ; candidats optimisés : 1198183 ; net attendu > 0 : 141 ; dernier cycle 63.8 ms
- Rejets (moteur) : {'spread_below_threshold': 379227858, 'liquidity_below_min': 2907847, 'negative_expected_net': 1198042, 'borrow_bound_too_small': 437275, 'unquotable': 34982, 'pool_quarantined': 20268, 'cycle_budget_exhausted': 4989, 'no_price_reference': 4}
- Enregistrements de la session : 1198183 ; net attendu > 0 : 141 ; simulés (eth_call de la vraie tx) : 21 (ok 7, échec 14) ; étiquettes ghost N+1 : 3/12 positives
- Décisions : {'REJECTED': 1198183} ; motifs de rejet : {'below_safety_margin': 75, 'negative_expected_net': 1198042, 'price_impact': 2, 'reliability_not_demonstrated': 141, 'simulation_failed': 14}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52582097 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome]→EXTRA→[aerodrome]→cbBTC | 0.001083 cbBTC | 0.000021 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000021 cbBTC (1.5788 €) | — | 189.30 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52582097 | WETH→[aerodrome]→EXTRA→[aerodrome]→cbBTC→[pancakeswap_v3]→WETH | 0.036031 WETH | 0.000685 WETH | 0.000000 WETH | 0.000003 WETH | 0.000682 WETH (1.5769 €) | — | 189.31 | — (n=0) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52582097 | WETH→[aerodrome]→EXTRA→[aerodrome]→cbBTC→[aerodrome_slipstream]→WETH | 0.035764 WETH | 0.000681 WETH | 0.000000 WETH | 0.000003 WETH | 0.000678 WETH (1.5685 €) | — | 189.70 | — (n=0) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52582097 | cbBTC→[aerodrome_slipstream]→WETH→[aerodrome]→EXTRA→[aerodrome]→cbBTC | 0.001072 cbBTC | 0.000020 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000020 cbBTC (1.5673 €) | — | 189.91 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52582097 | cbBTC→[uniswap_v3]→WETH→[aerodrome]→EXTRA→[aerodrome]→cbBTC | 0.001036 cbBTC | 0.000020 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000020 cbBTC (1.5072 €) | — | 189.05 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52582097 | WETH→[aerodrome]→EXTRA→[aerodrome]→cbBTC→[uniswap_v3]→WETH | 0.034445 WETH | 0.000654 WETH | 0.000000 WETH | 0.000003 WETH | 0.000651 WETH (1.5057 €) | — | 189.08 | — (n=0) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52582097 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome]→EXTRA→[aerodrome]→cbBTC | 0.001034 cbBTC | 0.000020 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000020 cbBTC (1.5034 €) | — | 188.86 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52582097 | WETH→[aerodrome]→EXTRA→[aerodrome]→cbBTC→[pancakeswap_v3]→WETH | 0.034381 WETH | 0.000652 WETH | 0.000000 WETH | 0.000003 WETH | 0.000649 WETH (1.5015 €) | — | 188.91 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52582097 | cbBTC→[aerodrome_slipstream]→WETH→[aerodrome]→EXTRA→[aerodrome]→cbBTC | 0.000791 cbBTC | 0.000014 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000014 cbBTC (1.0992 €) | — | 180.50 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52582097 | WETH→[aerodrome]→EXTRA→[aerodrome]→cbBTC→[aerodrome_slipstream]→WETH | 0.026275 WETH | 0.000477 WETH | 0.000000 WETH | 0.000003 WETH | 0.000474 WETH (1.0957 €) | — | 180.38 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52582097 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome]→EXTRA→[aerodrome]→cbBTC | 0.000783 cbBTC | 0.000014 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000014 cbBTC (1.0885 €) | — | 180.56 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52582097 | WETH→[aerodrome]→EXTRA→[aerodrome]→cbBTC→[pancakeswap_v3]→WETH | 0.026052 WETH | 0.000473 WETH | 0.000000 WETH | 0.000003 WETH | 0.000470 WETH (1.0863 €) | — | 180.36 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52582097 | cbBTC→[uniswap_v3]→WETH→[aerodrome]→EXTRA→[aerodrome]→cbBTC | 0.000729 cbBTC | 0.000013 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000013 cbBTC (0.9868 €) | — | 175.75 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52582097 | WETH→[aerodrome]→EXTRA→[aerodrome]→cbBTC→[uniswap_v3]→WETH | 0.024214 WETH | 0.000428 WETH | 0.000000 WETH | 0.000003 WETH | 0.000425 WETH (0.9834 €) | — | 175.67 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52582097 | cbBTC→[aerodrome]→WETH→[aerodrome]→EXTRA→[aerodrome]→cbBTC | 0.000720 cbBTC | 0.000013 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000013 cbBTC (0.9753 €) | — | 176.04 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52582097 | WETH→[aerodrome]→EXTRA→[aerodrome]→cbBTC→[aerodrome]→WETH | 0.023838 WETH | 0.000422 WETH | 0.000000 WETH | 0.000003 WETH | 0.000419 WETH (0.9694 €) | — | 175.89 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52581009 | WETH→[aerodrome]→EXTRA→[aerodrome]→cbBTC→[pancakeswap_v3]→WETH | 0.013241 WETH | 0.000047 WETH | 0.000000 WETH | 0.000003 WETH | 0.000045 WETH (0.1032 €) | — | 33.70 | — (n=0) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52581010 | WETH→[aerodrome]→EXTRA→[aerodrome]→cbBTC→[pancakeswap_v3]→WETH | 0.013241 WETH | 0.000047 WETH | 0.000000 WETH | 0.000003 WETH | 0.000045 WETH (0.1032 €) | — | 33.70 | — (n=0) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52581009 | cbBTC→[aerodrome_slipstream]→WETH→[aerodrome]→EXTRA→[aerodrome]→cbBTC | 0.000403 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.1025 €) | — | 33.01 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52581009 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome]→EXTRA→[aerodrome]→cbBTC | 0.000379 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.1025 €) | — | 35.12 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52581010 | cbBTC→[aerodrome_slipstream]→WETH→[aerodrome]→EXTRA→[aerodrome]→cbBTC | 0.000403 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.1025 €) | — | 33.01 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52581010 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome]→EXTRA→[aerodrome]→cbBTC | 0.000379 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.1025 €) | — | 35.12 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52581009 | WETH→[aerodrome]→EXTRA→[aerodrome]→cbBTC→[aerodrome_slipstream]→WETH | 0.014644 WETH | 0.000047 WETH | 0.000000 WETH | 0.000003 WETH | 0.000044 WETH (0.1020 €) | — | 30.13 | — (n=0) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52581010 | WETH→[aerodrome]→EXTRA→[aerodrome]→cbBTC→[aerodrome_slipstream]→WETH | 0.014644 WETH | 0.000047 WETH | 0.000000 WETH | 0.000003 WETH | 0.000044 WETH (0.1020 €) | — | 30.13 | — (n=0) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52581009 | WETH→[aerodrome]→EXTRA→[aerodrome]→cbBTC→[pancakeswap_v3]→WETH | 0.013241 WETH | 0.000039 WETH | 0.000000 WETH | 0.000003 WETH | 0.000036 WETH (0.0830 €) | — | 27.11 | — (n=0) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |

## Fiabilité et décision
- Observations ghost : 21 ; taux observé 0.143 ; borne inférieure crédible (0.9) 0.069 ; seuil 0.75 → **FIABILITÉ NON DÉMONTRÉE — DONNÉES INSUFFISANTES**
- Statut de maturité : **APPRENTISSAGE** — FIABILITÉ NON DÉMONTRÉE — DONNÉES INSUFFISANTES
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ❌ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
