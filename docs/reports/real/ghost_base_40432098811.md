# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-27T04:38:57+00:00 ; durée 191.18 min ; blocs 53137556 → 53143292 (5656 vus)

## Connexion
- Requêtes RPC : 70223 ; erreurs : 28 ; latence p50/p95 : 337.1/1,134.5 ms
- Rafraîchissements d'état : 5656 ; âge des données au dernier bloc : 3.3 s ; changements de frais LP observés (pools à frais dynamiques) : 7943
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 64678 ; cycles déclenchés par événement : 6288 ; avance médiane sur le rafraîchissement multicall : 883 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,313.13 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 530 pools, 305 jetons, 19446 routes
- Par DEX : uniswap_v3 143, aerodrome 212, aerodrome_slipstream 130, pancakeswap_v3 29, uniswap_v2 13, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 189 (rejetés 2) → 594 jetons ; pools candidats 3790 (énumérés 341, par paires 0), mesurés 533, sous le plancher de 10000.0 $ : 3 → gardés 530 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2322.398057, 'cbBTC': 80000.770706, 'AERO': 0.673032}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 155,961,577 | 2,313.131390 | 53143292 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,050,291 | 0.029011 | 53143292 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,080,810 | 0.028948 | 53143292 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,484,338 | 0.000013 | 53143292 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome | WETH/VVV | 3000 | 8,611,395 | 93.006342 | 53143292 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/USDC | 500 | 8,311,942 | 2,308.547597 | 53143292 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | USDC/AERO | 3000 | 6,999,119 | 1.491894 | 53143292 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,942,670 | 0.001642 | 53143292 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,348,572 | 0.029004 | 53143292 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/USDC | 150 | 5,233,026 | 2,308.032218 | 53143292 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,538,834 | 2,308.268042 | 53143292 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,199,691 | 0.998750 | 53143292 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,718,165 | 36,226.781852 | 53143292 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/USDC | 3000 | 3,357,233 | 2,310.185495 | 53143292 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 3,173,719 | 0.028966 | 53143292 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2700 | 2,494,699 | 93.056308 | 53143292 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | USDC/cbBTC | 448 | 2,438,304 | 0.000013 | 53143292 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome | WETH/FAI | 10000 | 2,110,766 | 1,217,557.512867 | 53143292 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | XDP/USDC | 100 | 1,839,243 | 0.018859 | 53143292 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,826,656 | 0.000000 | 53143292 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,753,408 | 405.417585 | 53143292 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,687,194 | 0.000013 | 53143292 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | USDC/cbBTC | 338 | 1,685,024 | 0.000013 | 53143292 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,661,447 | 0.000013 | 53143292 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | VIRTUAL/WETH | 10000 | 1,548,833 | 0.000266 | 53143292 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,498,841 | 0.005842 | 53143292 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,460,927 | 0.826515 | 53143292 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,453,150 | 1.698035 | 53143292 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | WETH/AERO | 3000 | 1,424,002 | 3,446.918837 | 53143292 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,363,941 | 13,980.023284 | 53143292 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,246,722 | 2,308.421870 | 53143292 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,232,328 | 0.000265 | 53143292 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | USDC/SEND | 3000 | 1,217,284 | 65.578051 | 53143292 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome | WETH/AERO | 10000 | 1,201,514 | 3,447.248911 | 53143292 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | DRB/WETH | 10000 | 1,140,270 | 0.000000 | 53143292 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | WETH/WELL | 10000 | 1,134,340 | 1,091,005.379706 | 53143292 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/doginme | 10000 | 1,133,068 | 37,251,512.319145 | 53143292 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,101,122 | 501,575.907361 | 53143292 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | WETH/EDEL | 7000 | 1,068,608 | 71,799.426826 | 53143292 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,053,533 | 20,515,189.927461 | 53143292 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome | USDC/NOCK | 3000 | 1,039,999 | 57.876948 | 53143292 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,035,437 | 17.192824 | 53143292 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | USDC/VVV | 3000 | 1,009,474 | 0.040286 | 53143292 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/USDC | 10000 | 950,565 | 2,317.651257 | 53143292 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 916,181 | 1,080.435952 | 53143292 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome | WETH/msETH (stable) | 500 | 904,191 | 2.309154 | 53143292 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | uXRP/WETH | 3000 | 892,245 | 0.000558 | 53143292 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 874,732 | 18.117460 | 53143292 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v3 | WETH/VVV | 10000 | 872,728 | 92.537139 | 53143292 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 846,191 | 17.403379 | 53143292 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| uniswap_v2 | WETH/USDC | 3000 | 843,616 | 2,312.853048 | 53143292 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| pancakeswap_v3 | QUID/USDC | 100 | 800,355 | 0.057461 | 53143292 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 792,658 | 0.000008 | 53143292 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | WETH/wstETH | 3000 | 783,168 | 0.803179 | 53143292 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 739,967 | 0.612032 | 53143292 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 737,621 | 4,642,934.525623 | 53143292 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v2 | WETH/NPC | 3000 | 697,726 | 138,328.796552 | 53143292 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| uniswap_v3 | TIG/USDC | 10000 | 696,438 | 0.610143 | 53143292 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | WETH/BRETT | 2105 | 687,488 | 503,028.499843 | 53143292 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 670,489 | 0.107884 | 53143292 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |

## Recherche d'opportunités
- Cycles : 11943 ; routes examinées : 232243578 ; candidats optimisés : 590056 ; net attendu > 0 : 416 ; dernier cycle 201.2 ms
- Rejets (moteur) : {'spread_below_threshold': 228416302, 'liquidity_below_min': 2965702, 'negative_expected_net': 589640, 'unquotable': 255868, 'borrow_bound_too_small': 11931, 'pool_quarantined': 2872, 'cycle_budget_exhausted': 847}
- Enregistrements de la session : 590056 ; net attendu > 0 : 416 ; simulés (eth_call de la vraie tx) : 28 (ok 3, échec 25) ; étiquettes ghost N+1 : 0/25 positives
- Décisions : {'REJECTED': 590056} ; motifs de rejet : {'below_safety_margin': 185, 'negative_expected_net': 589640, 'p_lower_below_threshold': 313, 'price_impact': 3, 'reliability_not_demonstrated': 103, 'simulation_failed': 25, 'stale_data': 12}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
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
| 53143242 | USDC→[uniswap_v3]→WETH→[uniswap_v2]→wIRON→[aerodrome]→USDC | 139.394615 USDC | 1.588233 USDC | 0.000000 USDC | 0.005912 USDC | 1.582321 USDC (1.4557 €) | — | 113.51 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 53143242 | WETH→[uniswap_v2]→wIRON→[aerodrome]→USDC→[sushiswap_v3]→WETH | 0.057983 WETH | 0.000659 WETH | 0.000000 WETH | 0.000003 WETH | 0.000656 WETH (1.3959 €) | — | 113.13 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 53143242 | USDC→[sushiswap_v3]→WETH→[uniswap_v2]→wIRON→[aerodrome]→USDC | 134.048255 USDC | 1.522689 USDC | 0.000000 USDC | 0.006264 USDC | 1.516425 USDC (1.3951 €) | — | 113.13 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 53141762 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→VIRTUAL→[uniswap_v3]→WETH | 0.254689 WETH | 0.000469 WETH | 0.000000 WETH | 0.000003 WETH | 0.000466 WETH (0.9919 €) | — | 18.30 | 0.000 (n=56) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 53141762 | USDC→[pancakeswap_v3]→VIRTUAL→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 588.515929 USDC | 1.085236 USDC | 0.000000 USDC | 0.007301 USDC | 1.077935 USDC (0.9917 €) | — | 18.32 | 0.000 (n=56) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53141762 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→VIRTUAL→[uniswap_v3]→WETH | 0.251010 WETH | 0.000454 WETH | 0.000000 WETH | 0.000003 WETH | 0.000451 WETH (0.9597 €) | — | 17.97 | 0.000 (n=56) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 53141762 | USDC→[pancakeswap_v3]→VIRTUAL→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 579.907895 USDC | 1.050146 USDC | 0.000000 USDC | 0.007301 USDC | 1.042845 USDC (0.9594 €) | — | 17.98 | 0.000 (n=56) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53143242 | USDC→[aerodrome]→WETH→[uniswap_v2]→wIRON→[aerodrome]→USDC | 97.606291 USDC | 1.046190 USDC | 0.000000 USDC | 0.005593 USDC | 1.040597 USDC (0.9573 €) | — | 106.61 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 53143242 | WETH→[uniswap_v2]→wIRON→[aerodrome]→USDC→[aerodrome]→WETH | 0.042113 WETH | 0.000451 WETH | 0.000000 WETH | 0.000002 WETH | 0.000449 WETH (0.9554 €) | — | 106.61 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 53141762 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→VIRTUAL→[uniswap_v3]→WETH | 0.246294 WETH | 0.000441 WETH | 0.000000 WETH | 0.000003 WETH | 0.000438 WETH (0.9326 €) | — | 17.79 | 0.000 (n=56) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 53141762 | USDC→[pancakeswap_v3]→VIRTUAL→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 569.107879 USDC | 1.020630 USDC | 0.000000 USDC | 0.007301 USDC | 1.013329 USDC (0.9323 €) | — | 17.81 | 0.000 (n=56) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53141762 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→VIRTUAL→[uniswap_v3]→WETH | 0.247176 WETH | 0.000440 WETH | 0.000000 WETH | 0.000003 WETH | 0.000437 WETH (0.9298 €) | — | 17.68 | 0.000 (n=56) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53141762 | USDC→[pancakeswap_v3]→VIRTUAL→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 570.980057 USDC | 1.017620 USDC | 0.000000 USDC | 0.007301 USDC | 1.010319 USDC (0.9295 €) | — | 17.69 | 0.000 (n=56) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53141762 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome_slipstream]→WETH | 0.242493 WETH | 0.000429 WETH | 0.000000 WETH | 0.000003 WETH | 0.000426 WETH (0.9069 €) | — | 17.57 | 0.000 (n=56) | REJECTED | p_lower_below_threshold(0.00<0.75) |

## Fiabilité et décision
- Observations ghost : 2800 ; taux observé 0.091 ; borne inférieure crédible (0.9) 0.084 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 8.4% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
