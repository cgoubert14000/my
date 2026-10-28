# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-28T18:04:59+00:00 ; durée 79.42 min ; blocs 53208289 → 53210674 (2238 vus)

## Connexion
- Requêtes RPC : 25795 ; erreurs : 120 ; latence p50/p95 : 311.5/1,502.2 ms
- Rafraîchissements d'état : 2238 ; âge des données au dernier bloc : 2.43 s ; changements de frais LP observés (pools à frais dynamiques) : 3807
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 16555 ; cycles déclenchés par événement : 927 ; avance médiane sur le rafraîchissement multicall : 609 ms
- Gaz : base fee 0.006154 gwei ; prix ETH (pool le plus profond) : 2,347.03 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 517 pools, 298 jetons, 19028 routes
- Par DEX : uniswap_v3 144, aerodrome_slipstream 121 (quarantaine 2), aerodrome 210, pancakeswap_v3 28, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 183 (rejetés 2) → 588 jetons ; pools candidats 3758 (énumérés 330, par paires 0), mesurés 519, sous le plancher de 10000.0 $ : 2 → gardés 517 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDC': 1.0, 'USDbC': 1.0, 'WETH': 2331.23448, 'cbBTC': 80382.611332, 'AERO': 0.701638}
- Pools en quarantaine : 2 — aerodrome_slipstream:WETH/USD@0x4D6997: simulation failed ×5 (model/chain mismatch) — until block 53210828; aerodrome_slipstream:USDC/USD@0x0c1A09: simulation failed ×5 (model/chain mismatch) — until block 53210828

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 157,906,411 | 2,347.029066 | 53210674 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,549,357 | 0.029015 | 53210674 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,882,229 | 0.000012 | 53210674 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,471,449 | 0.028977 | 53210674 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 8,517,359 | 2,346.775159 | 53210674 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 8,284,239 | 97.372385 | 53210674 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,053,634 | 0.001646 | 53210674 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 6,797,621 | 1.422187 | 53210674 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,820,279 | 0.029007 | 53210674 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/USDC | 564 | 4,946,731 | 2,345.979718 | 53210674 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,431,380 | 2,345.744070 | 53210674 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,259,758 | 0.998804 | 53210674 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,691,971 | 37,827.433912 | 53210674 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2510 | 2,942,056 | 0.028990 | 53210674 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2829 | 2,528,121 | 97.355603 | 53210674 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | WETH/FAI | 10000 | 2,144,700 | 1,214,151.729099 | 53210674 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 448 | 2,122,966 | 0.000012 | 53210674 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome | WETH/USDC | 3000 | 1,860,221 | 2,346.648257 | 53210674 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| uniswap_v3 | XDP/USDC | 100 | 1,822,933 | 0.018680 | 53210674 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,786,036 | 401.049082 | 53210674 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,781,813 | 0.000000 | 53210674 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,721,877 | 0.000012 | 53210674 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,695,498 | 0.000012 | 53210674 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | USDC/cbBTC | 334 | 1,669,303 | 0.000012 | 53210674 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,514,132 | 1.588195 | 53210674 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,494,271 | 0.005718 | 53210674 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v3 | WETH/AERO | 3000 | 1,465,052 | 3,342.254560 | 53210674 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,460,758 | 0.826986 | 53210674 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,389,881 | 13,832.186639 | 53210674 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,248,501 | 2,346.669809 | 53210674 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,247,669 | 0.000265 | 53210674 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | USDC/SEND | 3000 | 1,193,805 | 68.182945 | 53210674 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome | VIRTUAL/WETH | 10000 | 1,162,036 | 0.000266 | 53210674 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | WETH/doginme | 10000 | 1,157,802 | 36,550,416.191071 | 53210674 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | WETH/WELL | 10000 | 1,156,425 | 1,080,107.736919 | 53210674 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | DRB/WETH | 10000 | 1,121,857 | 0.000000 | 53210674 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,115,715 | 503,817.642035 | 53210674 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,087,140 | 21,137,337.930642 | 53210674 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome | WETH/AERO | 10000 | 1,080,892 | 3,335.376067 | 53210674 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | WETH/EDEL | 7000 | 1,079,548 | 72,211.066348 | 53210674 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,053,778 | 16.401291 | 53210674 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v2 | WETH/USDC | 3000 | 1,031,560 | 2,346.325203 | 53210674 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome | USDC/NOCK | 3000 | 1,007,659 | 61.652288 | 53210674 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/VVV | 10000 | 999,918 | 97.473185 | 53210674 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | USDC/VVV | 3000 | 999,285 | 0.041394 | 53210674 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/USDC | 10000 | 939,903 | 2,344.326232 | 53210674 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 930,123 | 1,062.078577 | 53210674 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | uXRP/WETH | 3000 | 906,650 | 0.000559 | 53210674 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome | WETH/msETH (stable) | 500 | 881,775 | 2.330700 | 53210674 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | USDC/SAPIEN | 4580 | 873,173 | 18.179395 | 53210674 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 842,382 | 17.611431 | 53210674 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| pancakeswap_v3 | QUID/USDC | 100 | 805,042 | 0.058170 | 53210674 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 794,747 | 0.802973 | 53210674 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 760,098 | 0.000009 | 53210674 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 749,237 | 4,632,969.863717 | 53210674 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 747,130 | 0.623602 | 53210674 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/NPC | 3000 | 708,715 | 138,118.152167 | 53210674 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | WETH/BRETT | 2225 | 695,232 | 499,599.785671 | 53210674 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 669,010 | 0.107390 | 53210674 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| uniswap_v3 | TIG/USDC | 10000 | 664,074 | 0.555984 | 53210674 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |

## Recherche d'opportunités
- Cycles : 3164 ; routes examinées : 60204592 ; candidats optimisés : 214235 ; net attendu > 0 : 351 ; dernier cycle 221.3 ms
- Rejets (moteur) : {'spread_below_threshold': 59170718, 'liquidity_below_min': 801987, 'negative_expected_net': 213884, 'pool_quarantined': 13888, 'borrow_bound_too_small': 3159, 'cycle_budget_exhausted': 605}
- Enregistrements de la session : 214235 ; net attendu > 0 : 351 ; simulés (eth_call de la vraie tx) : 20 (ok 2, échec 18) ; étiquettes ghost N+1 : 3/20 positives
- Décisions : {'REJECTED': 214235} ; motifs de rejet : {'below_safety_margin': 309, 'negative_expected_net': 213884, 'p_lower_below_threshold': 313, 'reliability_not_demonstrated': 38, 'simulation_failed': 18, 'stale_data': 70}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53210529 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.011595 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0870 €) | — | 1.01 | 0.001 (n=7) | REJECTED | below_safety_margin(117<231), reliability_not_demonstrated |
| 53210529 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.406438 WETH | 0.000043 WETH | 0.000000 WETH | 0.000003 WETH | 0.000040 WETH (0.0865 €) | — | 0.99 | 0.001 (n=7) | REJECTED | below_safety_margin(40092328619319<81287613159080), reliability_not_demonstrated |
| 53210529 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 951.804771 USDC | 0.101824 USDC | 0.000000 USDC | 0.007951 USDC | 0.093873 USDC (0.0864 €) | — | 0.99 | 0.001 (n=7) | REJECTED | below_safety_margin(93873<190360), reliability_not_demonstrated |
| 53210528 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USD→[aerodrome_slipstream]→USDC | 53.324969 USDC | 0.056221 USDC | 0.000000 USDC | 0.007778 USDC | 0.048443 USDC (0.0446 €) | — | 9.08 | 0.000 (n=67) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53210528 | WETH→[aerodrome_slipstream]→USD→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.022710 WETH | 0.000024 WETH | 0.000000 WETH | 0.000003 WETH | 0.000021 WETH (0.0445 €) | — | 9.09 | 0.000 (n=67) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 53210530 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→EURC→[aerodrome_slipstream]→cbBTC | 0.001950 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0439 €) | — | 3.03 | 0.097 (n=322) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53210530 | USDC→[aerodrome_slipstream]→EURC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 168.509941 USDC | 0.055314 USDC | 0.000000 USDC | 0.007750 USDC | 0.047564 USDC (0.0438 €) | — | 2.82 | 0.121 (n=415) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 53210296 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 637.241527 USDC | 0.047417 USDC | 0.000000 USDC | 0.007408 USDC | 0.040009 USDC (0.0368 €) | — | 0.63 | 0.001 (n=7) | REJECTED | below_safety_margin(40009<127448), reliability_not_demonstrated |
| 53210297 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 637.241527 USDC | 0.047417 USDC | 0.000000 USDC | 0.007408 USDC | 0.040009 USDC (0.0368 €) | — | 0.63 | 0.001 (n=7) | REJECTED | below_safety_margin(40009<127448), reliability_not_demonstrated |
| 53210296 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.298264 WETH | 0.000020 WETH | 0.000000 WETH | 0.000003 WETH | 0.000017 WETH (0.0365 €) | — | 0.57 | 0.001 (n=7) | REJECTED | below_safety_margin(16960518600437<59652855271606), reliability_not_demonstrated |
| 53210297 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.298264 WETH | 0.000020 WETH | 0.000000 WETH | 0.000003 WETH | 0.000017 WETH (0.0365 €) | — | 0.57 | 0.001 (n=7) | REJECTED | below_safety_margin(16960518600437<59652855271606), reliability_not_demonstrated |
| 53210296 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.007632 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0363 €) | — | 0.64 | 0.001 (n=7) | REJECTED | below_safety_margin(49<152), reliability_not_demonstrated |
| 53210297 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.007632 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0363 €) | — | 0.64 | 0.001 (n=7) | REJECTED | below_safety_margin(49<152), reliability_not_demonstrated |
| 53210529 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.123863 WETH | 0.000019 WETH | 0.000000 WETH | 0.000004 WETH | 0.000015 WETH (0.0328 €) | — | 1.23 | 0.122 (n=414) | REJECTED | below_safety_margin(15195834036142<24772636913697), p_lower_below_threshold(0.12<0.75) |
| 53210529 | cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.003561 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0327 €) | — | 1.24 | 0.122 (n=414) | REJECTED | below_safety_margin(44<71), p_lower_below_threshold(0.12<0.75) |
| 53210529 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 296.604790 USDC | 0.043803 USDC | 0.000000 USDC | 0.008332 USDC | 0.035471 USDC (0.0326 €) | — | 1.20 | 0.122 (n=414) | REJECTED | below_safety_margin(35471<59320), p_lower_below_threshold(0.12<0.75) |
| 53210528 | USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 157.905563 USDC | 0.040586 USDC | 0.000000 USDC | 0.007419 USDC | 0.033167 USDC (0.0305 €) | — | 2.10 | 0.122 (n=413) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 53210528 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH | 0.067230 WETH | 0.000017 WETH | 0.000000 WETH | 0.000003 WETH | 0.000014 WETH (0.0305 €) | — | 2.10 | 0.122 (n=413) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.12<0.75) |
| 53210528 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC | 81.194873 USDC | 0.040054 USDC | 0.000000 USDC | 0.007419 USDC | 0.032635 USDC (0.0300 €) | — | 4.02 | 0.098 (n=318) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53210528 | WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.034808 WETH | 0.000017 WETH | 0.000000 WETH | 0.000003 WETH | 0.000014 WETH (0.0300 €) | — | 4.00 | 0.098 (n=318) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.10<0.75) |
| 53210528 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USD→[aerodrome_slipstream]→USDC | 44.249790 USDC | 0.039056 USDC | 0.000000 USDC | 0.007423 USDC | 0.031633 USDC (0.0291 €) | — | 7.15 | 0.124 (n=172) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 53210528 | WETH→[aerodrome_slipstream]→USD→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.018782 WETH | 0.000017 WETH | 0.000000 WETH | 0.000003 WETH | 0.000013 WETH (0.0290 €) | — | 7.17 | 0.124 (n=172) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.12<0.75) |
| 53210530 | USDC→[aerodrome_slipstream]→EURC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 137.192537 USDC | 0.039250 USDC | 0.000000 USDC | 0.007750 USDC | 0.031500 USDC (0.0290 €) | — | 2.30 | 0.121 (n=415) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 53210530 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→EURC→[aerodrome_slipstream]→cbBTC | 0.001440 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0282 €) | — | 2.64 | 0.121 (n=415) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 53210530 | USDC→[aerodrome_slipstream]→EURC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 93.256330 USDC | 0.035850 USDC | 0.000000 USDC | 0.007750 USDC | 0.028100 USDC (0.0259 €) | — | 3.01 | 0.097 (n=322) | REJECTED | p_lower_below_threshold(0.10<0.75) |

## Fiabilité et décision
- Observations ghost : 2985 ; taux observé 0.094 ; borne inférieure crédible (0.9) 0.087 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 8.7% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
