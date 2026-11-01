# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-01T01:18:35+00:00 ; durée 113.83 min ; blocs 53349866 → 53353282 (3413 vus)

## Connexion
- Requêtes RPC : 41449 ; erreurs : 0 ; latence p50/p95 : 70.5/1,048.8 ms
- Rafraîchissements d'état : 3414 ; âge des données au dernier bloc : 1.54 s ; changements de frais LP observés (pools à frais dynamiques) : 2534
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 24795 ; cycles déclenchés par événement : 3172 ; avance médiane sur le rafraîchissement multicall : 373 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,256.94 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 503 pools, 291 jetons, 18668 routes
- Par DEX : uniswap_v3 140, aerodrome_slipstream 114, aerodrome 206, pancakeswap_v3 29, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 178 (rejetés 2) → 583 jetons ; pools candidats 3742 (énumérés 319, par paires 0), mesurés 506, sous le plancher de 10000.0 $ : 3 → gardés 503 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'DAI': 1.0, 'USDC': 1.0, 'WETH': 2257.094934, 'cbBTC': 77437.995276, 'AERO': 0.643751}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 150,517,608 | 2,256.940608 | 53353282 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,077,382 | 0.029155 | 53353282 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,299,897 | 0.000013 | 53353282 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,063,704 | 0.029089 | 53353282 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| aerodrome | WETH/VVV | 3000 | 7,933,773 | 95.770152 | 53353282 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/USDC | 500 | 7,870,283 | 2,264.022544 | 53353282 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,676,589 | 0.001610 | 53353282 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 5,761,267 | 1.551640 | 53353282 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,254,847 | 0.029163 | 53353282 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,075,942 | 0.998852 | 53353282 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome_slipstream | WETH/USDC | 150 | 4,057,675 | 2,263.268588 | 53353282 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/USDC | 100 | 3,930,608 | 2,263.117361 | 53353282 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | WETH/KTA | 3000 | 3,548,023 | 37,869.935864 | 53353282 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,691,278 | 0.029101 | 53353282 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2715 | 2,428,677 | 95.805642 | 53353282 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | WETH/FAI | 10000 | 2,073,787 | 1,200,829.160231 | 53353282 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 400 | 1,960,627 | 0.000013 | 53353282 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,757,724 | 0.000000 | 53353282 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,713,572 | 0.017338 | 53353282 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,673,855 | 0.000013 | 53353282 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v2 | WETH/USDC | 3000 | 1,596,670 | 2,257.557374 | 53353282 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,581,963 | 0.000013 | 53353282 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,551,415 | 424.670009 | 53353282 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,546,920 | 1.490152 | 53353282 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,457,383 | 0.825799 | 53353282 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,435,787 | 3,508.072589 | 53353282 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | WETH/USDC | 3000 | 1,409,400 | 2,263.616117 | 53353282 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,347,829 | 2,262.574012 | 53353282 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,324,237 | 0.005182 | 53353282 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,304,385 | 14,577.348753 | 53353282 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome_slipstream | USDC/cbBTC | 330 | 1,304,112 | 0.000013 | 53353282 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/SEND | 3000 | 1,174,072 | 70.494059 | 53353282 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,147,437 | 33,384,154.930702 | 53353282 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,065,366 | 515,624.675384 | 53353282 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,047,880 | 0.000000 | 53353282 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,028,963 | 21,602,616.147259 | 53353282 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | WETH/VVV | 10000 | 1,004,663 | 96.085154 | 53353282 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome | WETH/EDEL | 7000 | 1,002,275 | 77,404.486579 | 53353282 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | USDC/VVV | 3000 | 992,119 | 0.042352 | 53353282 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome_slipstream | USDC/VELVET | 100 | 990,527 | 19.476151 | 53353282 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | USDC/NOCK | 3000 | 976,049 | 65.712700 | 53353282 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome | WETH/WELL | 10000 | 961,627 | 1,151,679.900833 | 53353282 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/MORPHO | 3000 | 948,661 | 957.223590 | 53353282 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/USDC | 10000 | 924,195 | 2,242.032039 | 53353282 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome | WETH/AERO | 10000 | 879,205 | 3,494.893415 | 53353282 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | uXRP/WETH | 3000 | 865,255 | 0.000551 | 53353282 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 840,428 | 19.353497 | 53353282 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 827,802 | 0.061717 | 53353282 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 764,198 | 0.803065 | 53353282 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| aerodrome | VIRTUAL/WETH | 10000 | 734,831 | 0.000261 | 53353282 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 723,684 | 0.591178 | 53353282 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 720,737 | 4,633,070.561598 | 53353282 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 694,494 | 0.000008 | 53353282 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v2 | WETH/NPC | 3000 | 673,739 | 141,527.765601 | 53353282 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | WETH/BRETT | 2093 | 660,674 | 520,434.149330 | 53353282 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome | WETH/msETH (stable) | 500 | 658,135 | 2.336543 | 53353282 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | TIG/USDC | 10000 | 657,127 | 0.543723 | 53353282 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 614,729 | 0.093567 | 53353282 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| aerodrome | WETH/bsdETH | 100 | 605,732 | 0.916259 | 53353282 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome_slipstream | WETH/MORPHO | 2715 | 557,472 | 958.195924 | 53353282 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |

## Recherche d'opportunités
- Cycles : 6585 ; routes examinées : 122928780 ; candidats optimisés : 320925 ; net attendu > 0 : 149 ; dernier cycle 582.1 ms
- Rejets (moteur) : {'spread_below_threshold': 121028136, 'liquidity_below_min': 1552613, 'negative_expected_net': 320776, 'unquotable': 20392, 'borrow_bound_too_small': 6583, 'cycle_budget_exhausted': 131}
- Enregistrements de la session : 320925 ; net attendu > 0 : 149 ; simulés (eth_call de la vraie tx) : 0 (ok 0, échec 0) ; étiquettes ghost N+1 : 0/0 positives
- Décisions : {'REJECTED': 320925} ; motifs de rejet : {'below_safety_margin': 149, 'negative_expected_net': 320776, 'p_lower_below_threshold': 149}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53353236 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC | 59.968082 USDC | 0.011786 USDC | 0.000000 USDC | 0.006780 USDC | 0.005006 USDC (0.0046 €) | — | 0.83 | 0.141 (n=665) | REJECTED | below_safety_margin(5006<11993), p_lower_below_threshold(0.14<0.75) |
| 53353237 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC | 59.968082 USDC | 0.011786 USDC | 0.000000 USDC | 0.006780 USDC | 0.005006 USDC (0.0046 €) | — | 0.83 | 0.141 (n=665) | REJECTED | below_safety_margin(5006<11993), p_lower_below_threshold(0.14<0.75) |
| 53353237 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC | 59.968082 USDC | 0.011786 USDC | 0.000000 USDC | 0.006780 USDC | 0.005006 USDC (0.0046 €) | — | 0.83 | 0.141 (n=665) | REJECTED | below_safety_margin(5006<11993), p_lower_below_threshold(0.14<0.75) |
| 53353236 | cbBTC→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.000683 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0043 €) | — | 0.88 | 0.141 (n=665) | REJECTED | below_safety_margin(6<13), p_lower_below_threshold(0.14<0.75) |
| 53353237 | cbBTC→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.000683 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0043 €) | — | 0.88 | 0.141 (n=665) | REJECTED | below_safety_margin(6<13), p_lower_below_threshold(0.14<0.75) |
| 53353237 | cbBTC→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.000683 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0043 €) | — | 0.88 | 0.141 (n=665) | REJECTED | below_safety_margin(6<13), p_lower_below_threshold(0.14<0.75) |
| 53351894 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH | 0.034024 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0025 €) | — | 0.35 | 0.141 (n=665) | REJECTED | below_safety_margin(1189291991563<6804899194948), p_lower_below_threshold(0.14<0.75) |
| 53351894 | USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 76.025549 USDC | 0.009461 USDC | 0.000000 USDC | 0.006780 USDC | 0.002681 USDC (0.0025 €) | — | 0.35 | 0.141 (n=665) | REJECTED | below_safety_margin(2681<15205), p_lower_below_threshold(0.14<0.75) |
| 53353222 | cbBTC→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.000502 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0021 €) | — | 0.60 | 0.141 (n=665) | REJECTED | below_safety_margin(3<10), p_lower_below_threshold(0.14<0.75) |
| 53353222 | cbBTC→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.000502 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0021 €) | — | 0.60 | 0.141 (n=665) | REJECTED | below_safety_margin(3<10), p_lower_below_threshold(0.14<0.75) |
| 53353236 | cbBTC→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.000476 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0021 €) | — | 0.63 | 0.141 (n=665) | REJECTED | below_safety_margin(3<9), p_lower_below_threshold(0.14<0.75) |
| 53353237 | cbBTC→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.000476 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0021 €) | — | 0.63 | 0.141 (n=665) | REJECTED | below_safety_margin(3<9), p_lower_below_threshold(0.14<0.75) |
| 53353237 | cbBTC→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.000476 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0021 €) | — | 0.63 | 0.141 (n=665) | REJECTED | below_safety_margin(3<9), p_lower_below_threshold(0.14<0.75) |
| 53353222 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC | 50.489162 USDC | 0.009020 USDC | 0.000000 USDC | 0.006780 USDC | 0.002240 USDC (0.0021 €) | — | 0.44 | 0.141 (n=665) | REJECTED | below_safety_margin(2240<10097), p_lower_below_threshold(0.14<0.75) |
| 53353222 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC | 50.489162 USDC | 0.009020 USDC | 0.000000 USDC | 0.006780 USDC | 0.002240 USDC (0.0021 €) | — | 0.44 | 0.141 (n=665) | REJECTED | below_safety_margin(2240<10097), p_lower_below_threshold(0.14<0.75) |
| 53353236 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC | 39.138039 USDC | 0.008719 USDC | 0.000000 USDC | 0.006780 USDC | 0.001939 USDC (0.0018 €) | — | 0.50 | 0.141 (n=665) | REJECTED | below_safety_margin(1939<7827), p_lower_below_threshold(0.14<0.75) |
| 53353237 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC | 39.138039 USDC | 0.008719 USDC | 0.000000 USDC | 0.006780 USDC | 0.001939 USDC (0.0018 €) | — | 0.50 | 0.141 (n=665) | REJECTED | below_safety_margin(1939<7827), p_lower_below_threshold(0.14<0.75) |
| 53353237 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC | 39.138039 USDC | 0.008719 USDC | 0.000000 USDC | 0.006780 USDC | 0.001939 USDC (0.0018 €) | — | 0.50 | 0.141 (n=665) | REJECTED | below_safety_margin(1939<7827), p_lower_below_threshold(0.14<0.75) |
| 53351333 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.004491 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0013 €) | — | 1.39 | 0.141 (n=665) | REJECTED | below_safety_margin(624610008058<898222925891), p_lower_below_threshold(0.14<0.75) |
| 53351333 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.004491 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0013 €) | — | 1.39 | 0.141 (n=665) | REJECTED | below_safety_margin(624610008058<898222925891), p_lower_below_threshold(0.14<0.75) |
| 53351334 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.004491 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0013 €) | — | 1.39 | 0.141 (n=665) | REJECTED | below_safety_margin(624610008058<898222925891), p_lower_below_threshold(0.14<0.75) |
| 53351334 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.004491 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0013 €) | — | 1.39 | 0.141 (n=665) | REJECTED | below_safety_margin(624610008058<898222925891), p_lower_below_threshold(0.14<0.75) |
| 53351333 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 10.078098 USDC | 0.008175 USDC | 0.000000 USDC | 0.006780 USDC | 0.001395 USDC (0.0013 €) | — | 1.38 | 0.141 (n=665) | REJECTED | below_safety_margin(1395<2015), p_lower_below_threshold(0.14<0.75) |
| 53351333 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 10.078098 USDC | 0.008175 USDC | 0.000000 USDC | 0.006780 USDC | 0.001395 USDC (0.0013 €) | — | 1.38 | 0.141 (n=665) | REJECTED | below_safety_margin(1395<2015), p_lower_below_threshold(0.14<0.75) |
| 53351334 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 10.078098 USDC | 0.008175 USDC | 0.000000 USDC | 0.006780 USDC | 0.001395 USDC (0.0013 €) | — | 1.38 | 0.141 (n=665) | REJECTED | below_safety_margin(1395<2015), p_lower_below_threshold(0.14<0.75) |

## Fiabilité et décision
- Observations ghost : 4032 ; taux observé 0.128 ; borne inférieure crédible (0.9) 0.122 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 12.2% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
