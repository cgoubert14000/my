# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-28T13:30:21+00:00 ; durée 142.34 min ; blocs 53198162 → 53202433 (4216 vus)

## Connexion
- Requêtes RPC : 50216 ; erreurs : 18 ; latence p50/p95 : 245.0/1,033.2 ms
- Rafraîchissements d'état : 4216 ; âge des données au dernier bloc : 3.03 s ; changements de frais LP observés (pools à frais dynamiques) : 5932
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 47226 ; cycles déclenchés par événement : 3988 ; avance médiane sur le rafraîchissement multicall : 556 ms
- Gaz : base fee 0.005205 gwei ; prix ETH (pool le plus profond) : 2,340.48 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 525 pools, 303 jetons, 18974 routes
- Par DEX : uniswap_v3 148, aerodrome_slipstream 121, aerodrome 211, pancakeswap_v3 29, uniswap_v2 12, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 186 (rejetés 2) → 591 jetons ; pools candidats 3816 (énumérés 332, par paires 0), mesurés 527, sous le plancher de 10000.0 $ : 2 → gardés 525 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2367.672797, 'cbBTC': 81332.776577, 'AERO': 0.700175}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 157,562,367 | 2,340.475655 | 53202433 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,569,613 | 0.028984 | 53202433 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,858,020 | 0.000012 | 53202433 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,447,756 | 0.029033 | 53202433 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 8,446,177 | 2,334.620480 | 53202433 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 8,292,971 | 96.616895 | 53202433 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| aerodrome | USDC/AERO | 3000 | 7,195,612 | 1.434128 | 53202433 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,032,364 | 0.001642 | 53202433 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,702,039 | 0.028983 | 53202433 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/USDC | 624 | 4,943,682 | 2,334.193623 | 53202433 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,464,700 | 2,333.770952 | 53202433 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,251,738 | 0.998872 | 53202433 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,744,721 | 36,564.168751 | 53202433 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,945,059 | 0.029016 | 53202433 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2790 | 2,529,479 | 96.632995 | 53202433 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | USDC/cbBTC | 448 | 2,390,356 | 0.000012 | 53202433 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome | WETH/FAI | 10000 | 2,135,780 | 1,217,487.019299 | 53202433 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome | WETH/USDC | 3000 | 1,857,622 | 2,340.596055 | 53202433 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| uniswap_v3 | XDP/USDC | 100 | 1,830,151 | 0.018814 | 53202433 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,792,551 | 0.000000 | 53202433 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,780,286 | 401.560529 | 53202433 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,719,876 | 0.000012 | 53202433 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,681,228 | 0.000012 | 53202433 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | USDC/cbBTC | 336 | 1,666,533 | 0.000012 | 53202433 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,499,832 | 0.005763 | 53202433 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,476,274 | 1.655260 | 53202433 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,461,407 | 0.826871 | 53202433 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,456,377 | 3,348.326461 | 53202433 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,386,164 | 13,853.744736 | 53202433 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,245,537 | 0.000266 | 53202433 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,237,795 | 2,334.383821 | 53202433 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | WETH/AERO | 10000 | 1,200,467 | 3,355.251498 | 53202433 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | USDC/SEND | 3000 | 1,193,895 | 68.172568 | 53202433 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome | VIRTUAL/WETH | 10000 | 1,177,174 | 0.000267 | 53202433 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome | WETH/WELL | 10000 | 1,160,110 | 1,067,272.336197 | 53202433 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/doginme | 10000 | 1,158,806 | 36,147,549.764297 | 53202433 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,123,848 | 504,711.810233 | 53202433 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,116,676 | 0.000000 | 53202433 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,082,647 | 20,964,586.632119 | 53202433 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome | WETH/EDEL | 7000 | 1,077,681 | 72,057.326818 | 53202433 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,046,022 | 16.728527 | 53202433 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | USDC/NOCK | 3000 | 1,031,541 | 58.830069 | 53202433 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/VVV | 10000 | 998,418 | 96.692371 | 53202433 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | USDC/VVV | 3000 | 994,957 | 0.041395 | 53202433 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/USDC | 10000 | 938,804 | 2,356.990184 | 53202433 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 924,032 | 1,069.968532 | 53202433 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | uXRP/WETH | 3000 | 904,934 | 0.000560 | 53202433 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome | WETH/msETH (stable) | 500 | 879,259 | 2.330915 | 53202433 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 875,025 | 18.116124 | 53202433 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v2 | WETH/USDC | 3000 | 848,037 | 2,340.352258 | 53202433 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 837,307 | 17.652068 | 53202433 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| pancakeswap_v3 | QUID/USDC | 100 | 809,124 | 0.058799 | 53202433 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 792,528 | 0.802973 | 53202433 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 755,978 | 0.000009 | 53202433 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 748,657 | 4,614,211.631613 | 53202433 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 746,689 | 0.620072 | 53202433 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/NPC | 3000 | 714,668 | 135,061.432130 | 53202433 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 692,602 | 503,802.405653 | 53202433 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 667,705 | 0.107064 | 53202433 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| uniswap_v3 | TIG/USDC | 10000 | 661,262 | 0.551795 | 53202433 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |

## Recherche d'opportunités
- Cycles : 8203 ; routes examinées : 155643722 ; candidats optimisés : 596494 ; net attendu > 0 : 253 ; dernier cycle 393.0 ms
- Rejets (moteur) : {'spread_below_threshold': 152581135, 'liquidity_below_min': 2457133, 'negative_expected_net': 596241, 'borrow_bound_too_small': 8200, 'cycle_budget_exhausted': 760}
- Enregistrements de la session : 596494 ; net attendu > 0 : 253 ; simulés (eth_call de la vraie tx) : 26 (ok 7, échec 19) ; étiquettes ghost N+1 : 2/20 positives
- Décisions : {'REJECTED': 596494} ; motifs de rejet : {'below_safety_margin': 158, 'negative_expected_net': 596241, 'p_lower_below_threshold': 226, 'reliability_not_demonstrated': 27, 'simulation_failed': 19, 'stale_data': 10}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53201125 | WETH→[uniswap_v3]→VIRTUAL→[aerodrome_slipstream]→WETH | 0.119406 WETH | 0.000131 WETH | 0.000000 WETH | 0.000002 WETH | 0.000129 WETH (0.2770 €) | — | 10.77 | 0.001 (n=8) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53201125 | WETH→[uniswap_v3]→VIRTUAL→[aerodrome_slipstream]→WETH | 0.258628 WETH | 0.000112 WETH | 0.000000 WETH | 0.000002 WETH | 0.000110 WETH (0.2367 €) | — | 4.25 | 0.060 (n=47) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.06<0.75) |
| 53201125 | WETH→[uniswap_v3]→VIRTUAL→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.110339 WETH | 0.000084 WETH | 0.000000 WETH | 0.000003 WETH | 0.000081 WETH (0.1746 €) | — | 7.35 | 0.099 (n=315) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.10<0.75) |
| 53201125 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→VIRTUAL→[pancakeswap_v3]→USDC | 258.127392 USDC | 0.196931 USDC | 0.000000 USDC | 0.007404 USDC | 0.189527 USDC (0.1744 €) | — | 7.34 | 0.099 (n=315) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53201125 | WETH→[uniswap_v3]→VIRTUAL→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.109907 WETH | 0.000083 WETH | 0.000000 WETH | 0.000003 WETH | 0.000080 WETH (0.1714 €) | — | 7.24 | 0.099 (n=315) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53201125 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→VIRTUAL→[pancakeswap_v3]→USDC | 256.703526 USDC | 0.193098 USDC | 0.000000 USDC | 0.007049 USDC | 0.186049 USDC (0.1712 €) | — | 7.25 | 0.099 (n=315) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53199512 | USDC→[pancakeswap_v3]→ICNT→[uniswap_v3]→USDC | 111.039812 USDC | 0.179775 USDC | 0.000000 USDC | 0.005316 USDC | 0.174459 USDC (0.1605 €) | — | 15.71 | 0.000 (n=58) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 53201125 | WETH→[uniswap_v3]→VIRTUAL→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.097638 WETH | 0.000073 WETH | 0.000000 WETH | 0.000003 WETH | 0.000070 WETH (0.1512 €) | — | 7.19 | 0.099 (n=315) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53201125 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→VIRTUAL→[pancakeswap_v3]→USDC | 227.296210 USDC | 0.171241 USDC | 0.000000 USDC | 0.007049 USDC | 0.164192 USDC (0.1511 €) | — | 7.22 | 0.099 (n=315) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53201125 | WETH→[uniswap_v3]→VIRTUAL→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.069705 WETH | 0.000033 WETH | 0.000000 WETH | 0.000003 WETH | 0.000030 WETH (0.0651 €) | — | 4.34 | 0.099 (n=315) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53201125 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→VIRTUAL→[pancakeswap_v3]→USDC | 162.629429 USDC | 0.077751 USDC | 0.000000 USDC | 0.007049 USDC | 0.070702 USDC (0.0650 €) | — | 4.35 | 0.099 (n=315) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53201125 | WETH→[uniswap_v3]→VIRTUAL→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.068593 WETH | 0.000033 WETH | 0.000000 WETH | 0.000003 WETH | 0.000030 WETH (0.0645 €) | — | 4.36 | 0.099 (n=315) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53201125 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→VIRTUAL→[pancakeswap_v3]→USDC | 160.380959 USDC | 0.077078 USDC | 0.000000 USDC | 0.007049 USDC | 0.070029 USDC (0.0644 €) | — | 4.37 | 0.099 (n=315) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53199823 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.491950 WETH | 0.000031 WETH | 0.000000 WETH | 0.000002 WETH | 0.000029 WETH (0.0629 €) | — | 0.59 | 0.026 (n=110) | REJECTED | below_safety_margin(28936252376355<98390013216214), p_lower_below_threshold(0.03<0.75) |
| 53199823 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 1,159.092536 USDC | 0.073774 USDC | 0.000000 USDC | 0.005687 USDC | 0.068087 USDC (0.0626 €) | — | 0.59 | 0.026 (n=110) | REJECTED | below_safety_margin(68087<231818), p_lower_below_threshold(0.03<0.75) |
| 53200783 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.420802 WETH | 0.000028 WETH | 0.000000 WETH | 0.000002 WETH | 0.000026 WETH (0.0550 €) | — | 0.61 | 0.026 (n=110) | REJECTED | below_safety_margin(25560129801433<84160438354009), p_lower_below_threshold(0.03<0.75) |
| 53200783 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 979.926626 USDC | 0.065225 USDC | 0.000000 USDC | 0.005548 USDC | 0.059677 USDC (0.0549 €) | — | 0.61 | 0.026 (n=110) | REJECTED | below_safety_margin(59677<195985), p_lower_below_threshold(0.03<0.75) |
| 53198655 | cbBTC→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→cbBTC | 0.000372 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0547 €) | — | 19.62 | 0.000 (n=65) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53198655 | WETH→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→WETH | 0.013055 WETH | 0.000028 WETH | 0.000000 WETH | 0.000003 WETH | 0.000025 WETH (0.0542 €) | — | 19.08 | 0.000 (n=65) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 53198655 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→cbBTC | 0.000537 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0532 €) | — | 13.23 | 0.000 (n=65) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53198655 | USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 48.139367 USDC | 0.064903 USDC | 0.000000 USDC | 0.007118 USDC | 0.057785 USDC (0.0532 €) | — | 12.00 | 0.000 (n=65) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53198655 | WETH→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.013055 WETH | 0.000027 WETH | 0.000000 WETH | 0.000003 WETH | 0.000024 WETH (0.0517 €) | — | 18.22 | 0.000 (n=65) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 53198655 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→cbBTC | 0.000346 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0517 €) | — | 19.92 | 0.000 (n=65) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53198655 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→cbBTC | 0.000374 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0517 €) | — | 18.44 | 0.000 (n=65) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53198655 | WETH→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.012296 WETH | 0.000027 WETH | 0.000000 WETH | 0.000003 WETH | 0.000023 WETH (0.0511 €) | — | 19.11 | 0.000 (n=65) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |

## Fiabilité et décision
- Observations ghost : 2952 ; taux observé 0.094 ; borne inférieure crédible (0.9) 0.087 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 8.7% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
