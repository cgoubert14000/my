# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-27T04:42:03+00:00 ; durée 194.29 min ; blocs 53137556 → 53143384 (5748 vus)

## Connexion
- Requêtes RPC : 71354 ; erreurs : 28 ; latence p50/p95 : 292.0/1,107.5 ms
- Rafraîchissements d'état : 5748 ; âge des données au dernier bloc : 3.5 s ; changements de frais LP observés (pools à frais dynamiques) : 8017
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 65563 ; cycles déclenchés par événement : 6402 ; avance médiane sur le rafraîchissement multicall : 721 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,313.12 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 530 pools, 305 jetons, 19446 routes
- Par DEX : uniswap_v3 143, aerodrome 212 (quarantaine 1), aerodrome_slipstream 130, pancakeswap_v3 29, uniswap_v2 13 (quarantaine 1), sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 189 (rejetés 2) → 594 jetons ; pools candidats 3790 (énumérés 341, par paires 0), mesurés 533, sous le plancher de 10000.0 $ : 3 → gardés 530 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2322.398057, 'cbBTC': 80000.770706, 'AERO': 0.673032}
- Pools en quarantaine : 2 — aerodrome:wIRON/USDC@0x9941df: simulation failed ×5 (model/chain mismatch) — until block 53143651; uniswap_v2:wIRON/WETH@0x378C0D: simulation failed ×5 (model/chain mismatch) — until block 53143651

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 155,960,831 | 2,313.115530 | 53143384 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,050,500 | 0.029008 | 53143384 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,081,051 | 0.028948 | 53143384 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,484,847 | 0.000013 | 53143384 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome | WETH/VVV | 3000 | 8,611,140 | 93.010567 | 53143384 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/USDC | 500 | 8,311,916 | 2,307.358513 | 53143384 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | USDC/AERO | 3000 | 6,999,119 | 1.491894 | 53143384 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,943,171 | 0.001641 | 53143384 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,348,670 | 0.028996 | 53143384 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/USDC | 150 | 5,229,115 | 2,306.453155 | 53143384 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,536,891 | 2,306.361051 | 53143385 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,200,114 | 0.998750 | 53143384 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,718,151 | 36,226.562000 | 53143384 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/USDC | 3000 | 3,357,221 | 2,310.133301 | 53143384 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 3,173,777 | 0.028966 | 53143384 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2700 | 2,494,636 | 93.056308 | 53143384 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | USDC/cbBTC | 448 | 2,438,467 | 0.000013 | 53143384 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome | WETH/FAI | 10000 | 2,110,752 | 1,217,557.512867 | 53143384 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | XDP/USDC | 100 | 1,834,574 | 0.018770 | 53143384 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,826,643 | 0.000000 | 53143384 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,753,404 | 405.411626 | 53143384 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,687,311 | 0.000013 | 53143384 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | USDC/cbBTC | 336 | 1,685,129 | 0.000013 | 53143384 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,661,540 | 0.000013 | 53143384 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | VIRTUAL/WETH | 10000 | 1,548,822 | 0.000266 | 53143384 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,498,831 | 0.005842 | 53143384 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,460,927 | 0.826515 | 53143384 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,453,150 | 1.698035 | 53143384 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | WETH/AERO | 3000 | 1,423,998 | 3,446.918837 | 53143384 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,364,029 | 13,980.023284 | 53143384 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,246,719 | 2,307.155537 | 53143384 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,232,320 | 0.000265 | 53143384 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | USDC/SEND | 3000 | 1,217,284 | 65.578051 | 53143384 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome | WETH/AERO | 10000 | 1,201,510 | 3,447.248911 | 53143384 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | DRB/WETH | 10000 | 1,140,264 | 0.000000 | 53143384 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | WETH/WELL | 10000 | 1,134,332 | 1,091,005.379706 | 53143384 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/doginme | 10000 | 1,133,060 | 37,251,512.319145 | 53143384 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,101,114 | 501,575.907361 | 53143384 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | WETH/EDEL | 7000 | 1,068,633 | 71,795.152582 | 53143384 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,053,526 | 20,515,189.927461 | 53143384 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome | USDC/NOCK | 3000 | 1,039,999 | 57.876948 | 53143384 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,033,935 | 17.260914 | 53143384 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | USDC/VVV | 3000 | 1,009,446 | 0.040331 | 53143384 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/USDC | 10000 | 950,562 | 2,317.651257 | 53143384 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 916,175 | 1,080.435946 | 53143384 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome | WETH/msETH (stable) | 500 | 904,185 | 2.309154 | 53143384 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | uXRP/WETH | 3000 | 892,239 | 0.000558 | 53143384 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 874,732 | 18.117460 | 53143384 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v3 | WETH/VVV | 10000 | 872,708 | 92.537139 | 53143384 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 845,961 | 17.408407 | 53143384 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| uniswap_v2 | WETH/USDC | 3000 | 843,613 | 2,312.830001 | 53143384 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| pancakeswap_v3 | QUID/USDC | 100 | 800,201 | 0.057438 | 53143384 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 792,695 | 0.000008 | 53143384 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | WETH/wstETH | 3000 | 783,163 | 0.803179 | 53143384 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 739,964 | 0.612032 | 53143384 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 737,616 | 4,642,934.525623 | 53143384 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v2 | WETH/NPC | 3000 | 697,722 | 138,328.796552 | 53143384 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| uniswap_v3 | TIG/USDC | 10000 | 696,438 | 0.610143 | 53143384 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | WETH/BRETT | 2108 | 687,483 | 503,066.400259 | 53143384 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 670,489 | 0.107884 | 53143384 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |

## Recherche d'opportunités
- Cycles : 12149 ; routes examinées : 236249454 ; candidats optimisés : 604019 ; net attendu > 0 : 432 ; dernier cycle 537.6 ms
- Rejets (moteur) : {'spread_below_threshold': 232349683, 'liquidity_below_min': 3015194, 'negative_expected_net': 603587, 'unquotable': 260378, 'borrow_bound_too_small': 12136, 'pool_quarantined': 7072, 'cycle_budget_exhausted': 847}
- Enregistrements de la session : 604017 ; net attendu > 0 : 432 ; simulés (eth_call de la vraie tx) : 31 (ok 3, échec 28) ; étiquettes ghost N+1 : 0/28 positives
- Décisions : {'REJECTED': 604017} ; motifs de rejet : {'below_safety_margin': 187, 'negative_expected_net': 603585, 'p_lower_below_threshold': 315, 'price_impact': 3, 'reliability_not_demonstrated': 117, 'simulation_failed': 28, 'stale_data': 12}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53143351 | WETH→[uniswap_v3]→USDC→[aerodrome]→wIRON→[uniswap_v2]→WETH | 0.054583 WETH | 0.000952 WETH | 0.000000 WETH | 0.000003 WETH | 0.000950 WETH (2.0209 €) | — | 173.98 | 0.003 (n=2) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53143351 | WETH→[pancakeswap_v3]→USDC→[aerodrome]→wIRON→[uniswap_v2]→WETH | 0.054910 WETH | 0.000951 WETH | 0.000000 WETH | 0.000003 WETH | 0.000948 WETH (2.0177 €) | — | 172.67 | 0.006 (n=1) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53143351 | USDC→[aerodrome]→wIRON→[uniswap_v2]→WETH→[uniswap_v3]→USDC | 125.935794 USDC | 2.196972 USDC | 0.000000 USDC | 0.005914 USDC | 2.191058 USDC (2.0158 €) | — | 173.98 | 0.003 (n=2) | REJECTED | reliability_not_demonstrated |
| 53143351 | USDC→[aerodrome]→wIRON→[uniswap_v2]→WETH→[pancakeswap_v3]→USDC | 126.695173 USDC | 2.193525 USDC | 0.000000 USDC | 0.005914 USDC | 2.187611 USDC (2.0126 €) | — | 172.67 | 0.006 (n=1) | REJECTED | reliability_not_demonstrated |
| 53143351 | WETH→[aerodrome_slipstream]→USDC→[aerodrome]→wIRON→[uniswap_v2]→WETH | 0.054616 WETH | 0.000943 WETH | 0.000000 WETH | 0.000003 WETH | 0.000940 WETH (2.0009 €) | — | 172.16 | 0.003 (n=2) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53143351 | USDC→[aerodrome]→wIRON→[uniswap_v2]→WETH→[aerodrome_slipstream]→USDC | 126.003261 USDC | 2.175157 USDC | 0.000000 USDC | 0.005914 USDC | 2.169243 USDC (1.9957 €) | — | 172.16 | 0.003 (n=2) | REJECTED | reliability_not_demonstrated |
| 53143351 | WETH→[pancakeswap_v3]→USDC→[aerodrome]→wIRON→[uniswap_v2]→WETH | 0.052424 WETH | 0.000919 WETH | 0.000000 WETH | 0.000003 WETH | 0.000916 WETH (1.9497 €) | — | 174.76 | 0.006 (n=1) | REJECTED | reliability_not_demonstrated |
| 53143351 | USDC→[aerodrome]→wIRON→[uniswap_v2]→WETH→[pancakeswap_v3]→USDC | 120.934634 USDC | 2.119371 USDC | 0.000000 USDC | 0.005914 USDC | 2.113457 USDC (1.9444 €) | — | 174.76 | 0.006 (n=1) | REJECTED | reliability_not_demonstrated |
| 53143351 | WETH→[uniswap_v3]→USDC→[aerodrome]→wIRON→[uniswap_v2]→WETH | 0.052451 WETH | 0.000916 WETH | 0.000000 WETH | 0.000003 WETH | 0.000913 WETH (1.9428 €) | — | 174.06 | 0.003 (n=2) | REJECTED | reliability_not_demonstrated |
| 53143351 | USDC→[aerodrome]→wIRON→[uniswap_v2]→WETH→[uniswap_v3]→USDC | 120.990801 USDC | 2.111837 USDC | 0.000000 USDC | 0.005914 USDC | 2.105923 USDC (1.9374 €) | — | 174.06 | 0.003 (n=2) | REJECTED | reliability_not_demonstrated |
| 53143351 | WETH→[sushiswap_v3]→USDC→[aerodrome]→wIRON→[uniswap_v2]→WETH | 0.050692 WETH | 0.000890 WETH | 0.000000 WETH | 0.000003 WETH | 0.000888 WETH (1.8887 €) | — | 175.08 | 0.003 (n=2) | REJECTED | reliability_not_demonstrated |
| 53143351 | USDC→[aerodrome]→wIRON→[uniswap_v2]→WETH→[sushiswap_v3]→USDC | 116.842036 USDC | 2.051957 USDC | 0.000000 USDC | 0.006265 USDC | 2.045692 USDC (1.8820 €) | — | 175.08 | 0.003 (n=2) | REJECTED | reliability_not_demonstrated |
| 53143351 | WETH→[aerodrome_slipstream]→USDC→[aerodrome]→wIRON→[uniswap_v2]→WETH | 0.051526 WETH | 0.000883 WETH | 0.000000 WETH | 0.000003 WETH | 0.000880 WETH (1.8737 €) | — | 170.88 | 0.003 (n=2) | REJECTED | reliability_not_demonstrated |
| 53143351 | USDC→[aerodrome]→wIRON→[uniswap_v2]→WETH→[aerodrome_slipstream]→USDC | 118.668551 USDC | 2.033663 USDC | 0.000000 USDC | 0.005914 USDC | 2.027749 USDC (1.8655 €) | — | 170.88 | 0.003 (n=2) | REJECTED | reliability_not_demonstrated |
| 53143242 | WETH→[uniswap_v2]→wIRON→[aerodrome]→USDC→[aerodrome_slipstream]→WETH | 0.062844 WETH | 0.000743 WETH | 0.000000 WETH | 0.000003 WETH | 0.000741 WETH (1.5767 €) | — | 117.90 | — (n=0) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53143242 | WETH→[uniswap_v2]→wIRON→[aerodrome]→USDC→[uniswap_v3]→WETH | 0.062754 WETH | 0.000742 WETH | 0.000000 WETH | 0.000003 WETH | 0.000740 WETH (1.5746 €) | — | 117.91 | — (n=0) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53143242 | WETH→[uniswap_v2]→wIRON→[aerodrome]→USDC→[pancakeswap_v3]→WETH | 0.063188 WETH | 0.000742 WETH | 0.000000 WETH | 0.000003 WETH | 0.000740 WETH (1.5741 €) | — | 117.06 | — (n=0) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53143242 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v2]→wIRON→[aerodrome]→USDC | 145.055042 USDC | 1.716050 USDC | 0.000000 USDC | 0.005912 USDC | 1.710138 USDC (1.5733 €) | — | 117.90 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 53143242 | USDC→[uniswap_v3]→WETH→[uniswap_v2]→wIRON→[aerodrome]→USDC | 144.861660 USDC | 1.713938 USDC | 0.000000 USDC | 0.005912 USDC | 1.708026 USDC (1.5714 €) | — | 117.91 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 53143242 | USDC→[pancakeswap_v3]→WETH→[uniswap_v2]→wIRON→[aerodrome]→USDC | 145.855037 USDC | 1.713297 USDC | 0.000000 USDC | 0.005912 USDC | 1.707385 USDC (1.5708 €) | — | 117.06 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 53143242 | WETH→[uniswap_v2]→wIRON→[aerodrome]→USDC→[pancakeswap_v3]→WETH | 0.060312 WETH | 0.000692 WETH | 0.000000 WETH | 0.000003 WETH | 0.000689 WETH (1.4665 €) | — | 114.26 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 53143242 | USDC→[pancakeswap_v3]→WETH→[uniswap_v2]→wIRON→[aerodrome]→USDC | 139.311377 USDC | 1.597670 USDC | 0.000000 USDC | 0.005912 USDC | 1.591758 USDC (1.4644 €) | — | 114.26 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 53143242 | WETH→[uniswap_v2]→wIRON→[aerodrome]→USDC→[aerodrome_slipstream]→WETH | 0.058628 WETH | 0.000691 WETH | 0.000000 WETH | 0.000003 WETH | 0.000688 WETH (1.4643 €) | — | 117.37 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 53143242 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v2]→wIRON→[aerodrome]→USDC | 135.528430 USDC | 1.596572 USDC | 0.000000 USDC | 0.005912 USDC | 1.590660 USDC (1.4634 €) | — | 117.37 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 53143242 | WETH→[uniswap_v2]→wIRON→[aerodrome]→USDC→[uniswap_v3]→WETH | 0.060344 WETH | 0.000688 WETH | 0.000000 WETH | 0.000003 WETH | 0.000685 WETH (1.4577 €) | — | 113.51 | — (n=0) | REJECTED | reliability_not_demonstrated |

## Fiabilité et décision
- Observations ghost : 2803 ; taux observé 0.091 ; borne inférieure crédible (0.9) 0.084 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 8.4% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
