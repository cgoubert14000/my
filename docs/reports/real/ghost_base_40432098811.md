# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-27T02:35:09+00:00 ; durée 67.38 min ; blocs 53137556 → 53139579 (1967 vus)

## Connexion
- Requêtes RPC : 24436 ; erreurs : 1 ; latence p50/p95 : 303.7/1,339.4 ms
- Rafraîchissements d'état : 1967 ; âge des données au dernier bloc : 2.61 s ; changements de frais LP observés (pools à frais dynamiques) : 3578
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 26343 ; cycles déclenchés par événement : 1678 ; avance médiane sur le rafraîchissement multicall : 648 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,320.08 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 530 pools, 305 jetons, 19446 routes
- Par DEX : uniswap_v3 143, aerodrome 212, aerodrome_slipstream 130, pancakeswap_v3 29, uniswap_v2 13, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 189 (rejetés 2) → 594 jetons ; pools candidats 3790 (énumérés 341, par paires 0), mesurés 533, sous le plancher de 10000.0 $ : 3 → gardés 530 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2322.398057, 'cbBTC': 80000.770706, 'AERO': 0.673032}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 156,230,247 | 2,320.078429 | 53139579 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,095,417 | 0.028990 | 53139579 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,116,810 | 0.028948 | 53139579 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,497,364 | 0.000013 | 53139579 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome | WETH/VVV | 3000 | 8,643,259 | 92.877230 | 53139579 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/USDC | 500 | 8,336,013 | 2,314.235810 | 53139579 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | USDC/AERO | 3000 | 7,006,739 | 1.488898 | 53139579 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,968,523 | 0.001642 | 53139579 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,376,792 | 0.028992 | 53139579 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/USDC | 150 | 5,249,912 | 2,313.351090 | 53139579 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,548,118 | 2,313.184192 | 53139579 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,212,098 | 0.999452 | 53139579 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,773,922 | 35,375.780357 | 53139579 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/USDC | 3000 | 3,362,270 | 2,320.511634 | 53139579 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 3,184,444 | 0.028965 | 53139579 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2715 | 2,503,870 | 92.884290 | 53139579 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | USDC/cbBTC | 460 | 2,449,592 | 0.000013 | 53139579 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome | WETH/FAI | 10000 | 2,118,129 | 1,216,380.983500 | 53139579 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,832,982 | 0.000000 | 53139579 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,831,369 | 0.018712 | 53139579 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,758,931 | 405.209070 | 53139579 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | USDC/cbBTC | 342 | 1,688,747 | 0.000013 | 53139579 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,677,644 | 0.000013 | 53139579 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,664,722 | 0.000012 | 53139579 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | VIRTUAL/WETH | 10000 | 1,553,506 | 0.000266 | 53139579 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,506,160 | 0.005855 | 53139579 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,460,925 | 0.826518 | 53139579 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,453,150 | 1.698035 | 53139579 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | WETH/AERO | 3000 | 1,426,073 | 3,446.232497 | 53139579 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,368,897 | 13,975.389622 | 53139579 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,241,478 | 2,314.351302 | 53139579 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,236,020 | 0.000266 | 53139579 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | USDC/SEND | 3000 | 1,217,284 | 65.578051 | 53139579 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome | WETH/AERO | 10000 | 1,204,634 | 3,444.389703 | 53139579 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | DRB/WETH | 10000 | 1,145,935 | 0.000000 | 53139579 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/doginme | 10000 | 1,141,236 | 36,778,162.730985 | 53139579 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | WETH/WELL | 10000 | 1,137,752 | 1,090,994.671468 | 53139579 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,107,177 | 498,191.124905 | 53139579 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | WETH/EDEL | 7000 | 1,070,556 | 71,968.785905 | 53139579 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,067,312 | 20,147,287.445614 | 53139579 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome | USDC/NOCK | 3000 | 1,038,699 | 58.021930 | 53139579 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,029,535 | 17.463078 | 53139579 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | USDC/VVV | 3000 | 1,012,183 | 0.040129 | 53139579 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/USDC | 10000 | 951,827 | 2,317.651257 | 53139579 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 920,720 | 1,077.844036 | 53139579 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome | WETH/msETH (stable) | 500 | 906,907 | 2.309154 | 53139579 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | uXRP/WETH | 3000 | 894,924 | 0.000558 | 53139579 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | USDC/SAPIEN | 4565 | 876,809 | 18.047549 | 53139579 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v3 | WETH/VVV | 10000 | 871,731 | 92.391180 | 53139579 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 853,002 | 17.317761 | 53139579 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| uniswap_v2 | WETH/USDC | 3000 | 844,879 | 2,320.434974 | 53139579 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| pancakeswap_v3 | QUID/USDC | 100 | 798,052 | 0.057113 | 53139579 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 794,844 | 0.000008 | 53139579 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | WETH/wstETH | 3000 | 785,520 | 0.803179 | 53139579 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 741,716 | 0.614929 | 53139579 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 738,646 | 4,657,877.831546 | 53139579 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 699,989 | 0.616103 | 53139579 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/NPC | 3000 | 699,733 | 138,363.900067 | 53139579 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 691,995 | 502,216.041796 | 53139579 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 671,881 | 0.108254 | 53139579 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |

## Recherche d'opportunités
- Cycles : 3644 ; routes examinées : 70861224 ; candidats optimisés : 189836 ; net attendu > 0 : 43 ; dernier cycle 450.1 ms
- Rejets (moteur) : {'spread_below_threshold': 69580816, 'liquidity_below_min': 1013288, 'negative_expected_net': 189793, 'unquotable': 73510, 'borrow_bound_too_small': 3642, 'cycle_budget_exhausted': 132}
- Enregistrements de la session : 189836 ; net attendu > 0 : 43 ; simulés (eth_call de la vraie tx) : 7 (ok 3, échec 4) ; étiquettes ghost N+1 : 0/4 positives
- Décisions : {'REJECTED': 189836} ; motifs de rejet : {'below_safety_margin': 14, 'negative_expected_net': 189793, 'p_lower_below_threshold': 37, 'reliability_not_demonstrated': 6, 'simulation_failed': 4}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53139048 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.433874 WETH | 0.000025 WETH | 0.000000 WETH | 0.000002 WETH | 0.000023 WETH (0.0485 €) | — | 0.52 | 0.021 (n=102) | REJECTED | below_safety_margin(22684599651538<86774773737856), p_lower_below_threshold(0.02<0.75) |
| 53139049 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.433874 WETH | 0.000025 WETH | 0.000000 WETH | 0.000002 WETH | 0.000023 WETH (0.0485 €) | — | 0.52 | 0.021 (n=102) | REJECTED | below_safety_margin(22684599651538<86774773737856), p_lower_below_threshold(0.02<0.75) |
| 53139048 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 1,005.832273 USDC | 0.058181 USDC | 0.000000 USDC | 0.005566 USDC | 0.052615 USDC (0.0484 €) | — | 0.52 | 0.021 (n=102) | REJECTED | below_safety_margin(52615<201166), p_lower_below_threshold(0.02<0.75) |
| 53139049 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 1,005.832273 USDC | 0.058181 USDC | 0.000000 USDC | 0.005566 USDC | 0.052615 USDC (0.0484 €) | — | 0.52 | 0.021 (n=102) | REJECTED | below_safety_margin(52615<201166), p_lower_below_threshold(0.02<0.75) |
| 53138225 | WETH→[sushiswap_v3]→USDC→[uniswap_v3]→TOSHI→[aerodrome_slipstream]→WETH | 0.015175 WETH | 0.000024 WETH | 0.000000 WETH | 0.000003 WETH | 0.000021 WETH (0.0441 €) | 0.000021 WETH | 13.59 | 0.000 (n=58) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53138225 | WETH→[sushiswap_v3]→USDC→[uniswap_v3]→TOSHI→[aerodrome_slipstream]→WETH | 0.015175 WETH | 0.000024 WETH | 0.000000 WETH | 0.000003 WETH | 0.000021 WETH (0.0441 €) | — | 13.59 | 0.000 (n=58) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 53138225 | USDC→[uniswap_v3]→TOSHI→[aerodrome_slipstream]→WETH→[sushiswap_v3]→USDC | 35.137177 USDC | 0.055236 USDC | 0.000000 USDC | 0.007338 USDC | 0.047898 USDC (0.0441 €) | — | 13.63 | 0.000 (n=58) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53138225 | USDC→[uniswap_v3]→TOSHI→[aerodrome_slipstream]→WETH→[sushiswap_v3]→USDC | 35.137177 USDC | 0.055236 USDC | 0.000000 USDC | 0.007338 USDC | 0.047898 USDC (0.0441 €) | — | 13.63 | 0.000 (n=58) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53138225 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→TOSHI→[aerodrome_slipstream]→WETH | 0.015350 WETH | 0.000023 WETH | 0.000000 WETH | 0.000003 WETH | 0.000020 WETH (0.0433 €) | 0.000020 WETH | 13.19 | 0.000 (n=58) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53138225 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→TOSHI→[aerodrome_slipstream]→WETH | 0.015350 WETH | 0.000023 WETH | 0.000000 WETH | 0.000003 WETH | 0.000020 WETH (0.0433 €) | — | 13.19 | 0.000 (n=58) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 53138225 | USDC→[uniswap_v3]→TOSHI→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 35.470699 USDC | 0.054007 USDC | 0.000000 USDC | 0.006985 USDC | 0.047022 USDC (0.0433 €) | — | 13.26 | 0.000 (n=58) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53138225 | USDC→[uniswap_v3]→TOSHI→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 35.470699 USDC | 0.054007 USDC | 0.000000 USDC | 0.006985 USDC | 0.047022 USDC (0.0433 €) | — | 13.26 | 0.000 (n=58) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53138225 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→TOSHI→[aerodrome_slipstream]→WETH | 0.014411 WETH | 0.000023 WETH | 0.000000 WETH | 0.000003 WETH | 0.000020 WETH (0.0418 €) | 0.000020 WETH | 13.58 | 0.000 (n=58) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53138225 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→TOSHI→[aerodrome_slipstream]→WETH | 0.014411 WETH | 0.000023 WETH | 0.000000 WETH | 0.000003 WETH | 0.000020 WETH (0.0418 €) | — | 13.58 | 0.000 (n=58) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 53138225 | USDC→[uniswap_v3]→TOSHI→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→USDC | 33.276894 USDC | 0.052434 USDC | 0.000000 USDC | 0.006985 USDC | 0.045449 USDC (0.0418 €) | — | 13.66 | 0.000 (n=58) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53138225 | USDC→[uniswap_v3]→TOSHI→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→USDC | 33.276894 USDC | 0.052434 USDC | 0.000000 USDC | 0.006985 USDC | 0.045449 USDC (0.0418 €) | — | 13.66 | 0.000 (n=58) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53138225 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→TOSHI→[aerodrome_slipstream]→WETH | 0.015201 WETH | 0.000023 WETH | 0.000000 WETH | 0.000003 WETH | 0.000020 WETH (0.0418 €) | — | 12.86 | 0.000 (n=58) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53138225 | USDC→[uniswap_v3]→TOSHI→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 35.137177 USDC | 0.052383 USDC | 0.000000 USDC | 0.006985 USDC | 0.045398 USDC (0.0418 €) | — | 12.92 | 0.000 (n=58) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53138225 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→TOSHI→[aerodrome_slipstream]→WETH | 0.015225 WETH | 0.000023 WETH | 0.000000 WETH | 0.000003 WETH | 0.000020 WETH (0.0417 €) | — | 12.82 | 0.000 (n=58) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53138225 | USDC→[uniswap_v3]→TOSHI→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 35.090479 USDC | 0.052318 USDC | 0.000000 USDC | 0.006985 USDC | 0.045333 USDC (0.0417 €) | — | 12.92 | 0.000 (n=58) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53138225 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→TOSHI→[aerodrome_slipstream]→WETH | 0.015161 WETH | 0.000022 WETH | 0.000000 WETH | 0.000003 WETH | 0.000019 WETH (0.0416 €) | — | 12.84 | 0.000 (n=56) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53138225 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→TOSHI→[aerodrome_slipstream]→WETH | 0.015161 WETH | 0.000022 WETH | 0.000000 WETH | 0.000003 WETH | 0.000019 WETH (0.0416 €) | — | 12.84 | 0.000 (n=56) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53138225 | USDC→[uniswap_v3]→TOSHI→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 35.098791 USDC | 0.052179 USDC | 0.000000 USDC | 0.006985 USDC | 0.045194 USDC (0.0416 €) | — | 12.88 | 0.000 (n=56) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53138225 | USDC→[uniswap_v3]→TOSHI→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 35.098791 USDC | 0.052179 USDC | 0.000000 USDC | 0.006985 USDC | 0.045194 USDC (0.0416 €) | — | 12.88 | 0.000 (n=56) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53138225 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→TOSHI→[aerodrome_slipstream]→WETH | 0.014645 WETH | 0.000021 WETH | 0.000000 WETH | 0.000003 WETH | 0.000018 WETH (0.0387 €) | — | 12.37 | 0.000 (n=56) | REJECTED | p_lower_below_threshold(0.00<0.75) |

## Fiabilité et décision
- Observations ghost : 2779 ; taux observé 0.092 ; borne inférieure crédible (0.9) 0.085 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 8.5% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
