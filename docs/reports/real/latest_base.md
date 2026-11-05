# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-05T15:26:56+00:00 ; durée 318.46 min ; blocs 53541978 → 53551528 (9437 vus)

## Connexion
- Requêtes RPC : 110999 ; erreurs : 13 ; latence p50/p95 : 128.4/1,699.4 ms
- Rafraîchissements d'état : 9437 ; âge des données au dernier bloc : 5.17 s ; changements de frais LP observés (pools à frais dynamiques) : 17706
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 100913 ; cycles déclenchés par événement : 8247 ; avance médiane sur le rafraîchissement multicall : 1,023 ms
- Gaz : base fee 0.014815 gwei ; prix ETH (pool le plus profond) : 2,294.85 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 498 pools, 288 jetons, 19416 routes
- Par DEX : uniswap_v3 142 (quarantaine 1), aerodrome_slipstream 107, aerodrome 205, pancakeswap_v3 29, uniswap_v2 12, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 175 (rejetés 2) → 580 jetons ; pools candidats 3707 (énumérés 310, par paires 0), mesurés 501, sous le plancher de 10000.0 $ : 3 → gardés 498 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDC': 1.0, 'USDbC': 1.0, 'WETH': 2417.172064, 'cbBTC': 80337.642272, 'AERO': 0.664358}
- Pools en quarantaine : 1 — uniswap_v3:VIRTUAL/WETH@0x9c087E: simulation failed ×5 (model/chain mismatch) — until block 53551571

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 150,586,744 | 2,294.851684 | 53551528 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,698,669 | 0.029991 | 53551528 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,206,508 | 0.029915 | 53551528 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,027,448 | 0.000013 | 53551528 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 8,023,746 | 2,287.697456 | 53551528 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,431,113 | 111.515504 | 53551528 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,476,917 | 0.001553 | 53551528 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 5,116,034 | 1.686540 | 53551528 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,095,734 | 0.030002 | 53551528 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,147,050 | 2,288.655807 | 53551528 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,030,029 | 0.998760 | 53551528 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,414,661 | 42,269.694854 | 53551528 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 150 | 3,330,101 | 2,288.580530 | 53551528 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2600 | 2,610,752 | 0.029925 | 53551528 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 2,144,939 | 1,160,500.715180 | 53551528 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 600 | 1,774,921 | 0.000013 | 53551528 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,773,049 | 0.006923 | 53551528 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,675,469 | 0.000000 | 53551528 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,652,595 | 0.016549 | 53551528 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,634,954 | 0.000013 | 53551528 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,549,151 | 1.432376 | 53551528 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,546,359 | 454.893107 | 53551528 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,521,338 | 0.000013 | 53551528 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,460,233 | 0.816887 | 53551528 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,376,320 | 3,858.232111 | 53551528 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | WETH/USDC | 3000 | 1,342,646 | 2,291.009756 | 53551528 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| uniswap_v2 | WETH/USDC | 3000 | 1,342,241 | 2,290.299998 | 53551528 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,268,441 | 15,154.586276 | 53551528 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,199,484 | 2,289.016181 | 53551528 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,151,099 | 73.335477 | 53551528 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,120,347 | 37,667,688.172912 | 53551528 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | DRB/WETH | 10000 | 1,047,682 | 0.000000 | 53551528 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/VVV | 10000 | 1,037,655 | 110.939509 | 53551528 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,036,460 | 582,765.542821 | 53551528 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,010,387 | 23,003,409.905224 | 53551528 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome | USDC/NOCK | 3000 | 985,983 | 64.497688 | 53551528 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | USDC/VELVET | 100 | 960,034 | 21.386094 | 53551528 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/USDC | 10000 | 944,837 | 2,310.951117 | 53551528 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 940,821 | 1,081.527434 | 53551528 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome_slipstream | USDC/cbBTC | 502 | 930,005 | 0.000013 | 53551528 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | WETH/EDEL | 7000 | 902,750 | 98,575.803498 | 53551528 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | uXRP/WETH | 3000 | 874,011 | 0.000546 | 53551528 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| uniswap_v3 | USDC/VVV | 3000 | 849,546 | 0.048688 | 53551528 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | WETH/AERO | 10000 | 800,615 | 3,830.039282 | 53551528 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| pancakeswap_v3 | QUID/USDC | 100 | 798,747 | 0.057164 | 53551528 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome_slipstream | USDC/SAPIEN | 5120 | 788,258 | 21.322337 | 53551528 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome | WETH/wstETH | 3000 | 779,046 | 0.798912 | 53551528 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 709,833 | 0.556257 | 53551528 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 702,538 | 5,048,261.982758 | 53551528 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome | VIRTUAL/WETH | 10000 | 690,122 | 0.000245 | 53551528 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v2 | WETH/NPC | 3000 | 687,959 | 140,600.605119 | 53551528 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| uniswap_v3 | TIG/USDC | 10000 | 656,438 | 0.546002 | 53551528 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 647,121 | 0.000008 | 53551528 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/BRETT | 2381 | 630,658 | 586,856.933434 | 53551528 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome | WETH/bsdETH | 100 | 615,909 | 0.914226 | 53551528 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome | WETH/msETH (stable) | 500 | 612,198 | 2.479668 | 53551528 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 575,209 | 0.084415 | 53551528 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| aerodrome | cbBTC/EDGE | 7000 | 552,710 | 814,379.753072 | 53551528 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| uniswap_v3 | FLOCK/USDC | 3000 | 547,511 | 0.036729 | 53551528 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome | WETH/DRV | 3000 | 536,723 | 6,704.166688 | 53551528 | `0xaC4e562d7C6108f971321F14238E24AE2cC398ac` |

## Recherche d'opportunités
- Cycles : 17683 ; routes examinées : 343333128 ; candidats optimisés : 1092882 ; net attendu > 0 : 3963 ; dernier cycle 723.9 ms
- Rejets (moteur) : {'spread_below_threshold': 337162791, 'liquidity_below_min': 4930946, 'negative_expected_net': 1088919, 'pool_quarantined': 105838, 'cycle_budget_exhausted': 23021, 'borrow_bound_too_small': 17650}
- Enregistrements de la session : 1092882 ; net attendu > 0 : 3963 ; simulés (eth_call de la vraie tx) : 204 (ok 112, échec 92) ; étiquettes ghost N+1 : 27/182 positives
- Décisions : {'REJECTED': 1092882} ; motifs de rejet : {'below_safety_margin': 2620, 'negative_expected_net': 1088919, 'p_lower_below_threshold': 3574, 'price_impact': 2, 'reliability_not_demonstrated': 389, 'sim_below_estimate': 3, 'simulated_net_nonpositive': 3, 'simulation_failed': 92, 'stale_data': 103}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53551457 | cbBTC→[uniswap_v3]→WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.067214 cbBTC | 0.000031 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000030 cbBTC (2.1464 €) | — | 4.50 | 0.149 (n=734) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 53551457 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH | 2.271732 WETH | 0.001023 WETH | 0.000000 WETH | 0.000010 WETH | 0.001013 WETH (2.1457 €) | — | 4.46 | 0.149 (n=734) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.15<0.75) |
| 53551457 | USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 5,287.120562 USDC | 2.348990 USDC | 0.000000 USDC | 0.024154 USDC | 2.324836 USDC (2.1388 €) | — | 4.40 | 0.149 (n=734) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 53551389 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→cbBTC | 0.036868 cbBTC | 0.000025 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000024 cbBTC (1.7452 €) | — | 6.64 | 0.150 (n=729) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 53551389 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 1.259493 WETH | 0.000831 WETH | 0.000000 WETH | 0.000010 WETH | 0.000821 WETH (1.7449 €) | — | 6.52 | 0.150 (n=729) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.15<0.75) |
| 53551389 | USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 2,893.570456 USDC | 1.915127 USDC | 0.000000 USDC | 0.023090 USDC | 1.892037 USDC (1.7407 €) | — | 6.54 | 0.150 (n=729) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 53551457 | cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.056038 cbBTC | 0.000024 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000024 cbBTC (1.6665 €) | — | 4.20 | 0.149 (n=734) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 53551457 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 1.916264 WETH | 0.000797 WETH | 0.000000 WETH | 0.000011 WETH | 0.000786 WETH (1.6653 €) | — | 4.10 | 0.149 (n=734) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.15<0.75) |
| 53551457 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 4,467.068868 USDC | 1.828955 USDC | 0.000000 USDC | 0.025072 USDC | 1.803883 USDC (1.6596 €) | — | 4.04 | 0.149 (n=734) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 53551500 | cbBTC→[uniswap_v3]→WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.053273 cbBTC | 0.000020 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000020 cbBTC (1.4001 €) | — | 3.72 | 0.148 (n=740) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 53551500 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH | 1.758302 WETH | 0.000672 WETH | 0.000000 WETH | 0.000010 WETH | 0.000662 WETH (1.3994 €) | — | 3.76 | 0.148 (n=740) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.15<0.75) |
| 53551500 | USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 4,077.606564 USDC | 1.540325 USDC | 0.000000 USDC | 0.023831 USDC | 1.516494 USDC (1.3952 €) | — | 3.72 | 0.148 (n=740) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 53551500 | cbBTC→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.040791 cbBTC | 0.000017 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000016 cbBTC (1.1488 €) | — | 3.99 | 0.148 (n=740) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 53551500 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→WETH | 1.367396 WETH | 0.000553 WETH | 0.000000 WETH | 0.000010 WETH | 0.000543 WETH (1.1477 €) | — | 3.97 | 0.148 (n=740) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.15<0.75) |
| 53551500 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 3,193.322284 USDC | 1.266652 USDC | 0.000000 USDC | 0.022878 USDC | 1.243774 USDC (1.1443 €) | — | 3.89 | 0.148 (n=740) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 53551500 | cbBTC→[uniswap_v3]→WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.044634 cbBTC | 0.000015 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000015 cbBTC (1.0612 €) | — | 3.37 | 0.148 (n=740) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 53551500 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH | 1.487634 WETH | 0.000512 WETH | 0.000000 WETH | 0.000010 WETH | 0.000502 WETH (1.0608 €) | — | 3.37 | 0.148 (n=740) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.15<0.75) |
| 53551500 | USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 3,440.816518 USDC | 1.173274 USDC | 0.000000 USDC | 0.023831 USDC | 1.149443 USDC (1.0575 €) | — | 3.34 | 0.148 (n=740) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 53551466 | cbBTC→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.024732 cbBTC | 0.000014 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000014 cbBTC (0.9799 €) | — | 5.60 | 0.149 (n=736) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 53551466 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→WETH | 0.845902 WETH | 0.000472 WETH | 0.000000 WETH | 0.000010 WETH | 0.000462 WETH (0.9791 €) | — | 5.47 | 0.149 (n=736) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.15<0.75) |
| 53551466 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 1,943.801599 USDC | 1.082644 USDC | 0.000000 USDC | 0.022689 USDC | 1.059955 USDC (0.9752 €) | — | 5.45 | 0.149 (n=736) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 53545322 | USDC→[pancakeswap_v3]→ICNT→[uniswap_v3]→USDC | 275.403994 USDC | 1.039397 USDC | 0.000000 USDC | 0.005442 USDC | 1.033955 USDC (0.9512 €) | — | 37.54 | 0.000 (n=17) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53551457 | cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.027512 cbBTC | 0.000013 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000013 cbBTC (0.8974 €) | — | 4.60 | 0.149 (n=734) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 53551457 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.946398 WETH | 0.000433 WETH | 0.000000 WETH | 0.000010 WETH | 0.000423 WETH (0.8966 €) | — | 4.47 | 0.149 (n=734) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.15<0.75) |
| 53551457 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 2,194.993294 USDC | 0.993294 USDC | 0.000000 USDC | 0.022317 USDC | 0.970977 USDC (0.8933 €) | — | 4.42 | 0.149 (n=734) | REJECTED | p_lower_below_threshold(0.15<0.75) |

## Fiabilité et décision
- Observations ghost : 5649 ; taux observé 0.157 ; borne inférieure crédible (0.9) 0.151 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 15.1% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ✅ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
