# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-09T10:35:16+00:00 ; durée 36.66 min ; blocs 55139673 → 55150668 (1262 vus)

## Connexion
- Requêtes RPC : 19890 ; erreurs : 5 ; latence p50/p95 : 398.0/1,591.6 ms
- Rafraîchissements d'état : 1262 ; âge des données au dernier bloc : 6.41 s ; changements de frais LP observés (pools à frais dynamiques) : 1107
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 2243 ; cycles déclenchés par événement : 676 ; avance médiane sur le rafraîchissement multicall : 563 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,103.78 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 465 pools, 272 jetons, 17388 routes
- Par DEX : uniswap_v3 131, aerodrome_slipstream 99, aerodrome 193, pancakeswap_v3 28, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 167 (rejetés 2) → 572 jetons ; pools candidats 3672 (énumérés 289, par paires 0), mesurés 467, sous le plancher de 10000.0 $ : 2 → gardés 465 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDbC': 1.0, 'USDC': 1.0, 'WETH': 2109.380964, 'cbBTC': 74235.499826, 'AERO': 0.565393}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 137,485,205 | 2,103.780306 | 55150668 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,330,501 | 0.028386 | 55150668 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,234,730 | 0.000013 | 55150668 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 8,648,716 | 0.028398 | 55150668 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 7,372,221 | 2,102.481431 | 55150668 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,056,826 | 103.770845 | 55150668 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,208,484 | 0.001519 | 55150668 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,597,931 | 0.028390 | 55150668 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 4,552,688 | 1.772989 | 55150668 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/USDC | 100 | 3,937,741 | 2,102.936013 | 55150668 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,903,479 | 0.998733 | 55150668 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,082,143 | 43,602.393602 | 55150668 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 150 | 2,999,729 | 2,103.047628 | 55150668 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,338,824 | 0.028389 | 55150668 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 1,977,319 | 1,147,475.453732 | 55150668 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 520 | 1,699,371 | 0.000013 | 55150668 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,641,868 | 0.000013 | 55150668 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,602,995 | 0.006865 | 55150668 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v3 | XDP/USDC | 100 | 1,570,986 | 0.015585 | 55150668 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,544,649 | 0.000000 | 55150668 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,476,122 | 1.418208 | 55150668 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,453,452 | 0.821691 | 55150668 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,445,076 | 428.581001 | 55150668 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,437,366 | 0.000013 | 55150668 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v3 | WETH/AERO | 3000 | 1,302,847 | 3,732.438077 | 55150668 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v2 | WETH/USDC | 3000 | 1,285,840 | 2,102.829268 | 55150668 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,232,391 | 15,118.571287 | 55150668 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/USDC | 3000 | 1,215,696 | 2,104.778109 | 55150668 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome | USDC/SEND | 3000 | 1,120,185 | 77.439002 | 55150668 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,091,189 | 2,102.922141 | 55150668 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | WETH/doginme | 10000 | 1,035,888 | 36,726,664.920069 | 55150668 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/VVV | 10000 | 1,004,713 | 104.501447 | 55150668 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome_slipstream | USDC/VELVET | 100 | 960,789 | 21.334096 | 55150668 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/BRETT | 10000 | 951,080 | 581,301.114147 | 55150668 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome_slipstream | USDC/cbBTC | 354 | 920,053 | 0.000014 | 55150668 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | WETH/TOSHI | 10000 | 914,969 | 23,484,902.655903 | 55150668 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome | USDC/NOCK | 3000 | 909,888 | 75.688905 | 55150668 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/USDC | 10000 | 907,813 | 2,104.880343 | 55150668 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 897,527 | 1,034.165893 | 55150668 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | DRB/WETH | 10000 | 895,895 | 0.000000 | 55150668 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | USDC/VVV | 3000 | 838,196 | 0.049262 | 55150668 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | WETH/EDEL | 7000 | 815,424 | 101,479.006437 | 55150668 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome_slipstream | USDC/SAPIEN | 4505 | 763,872 | 22.312858 | 55150668 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 761,734 | 0.051753 | 55150668 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/AERO | 10000 | 736,686 | 3,721.601102 | 55150668 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | WETH/wstETH | 3000 | 712,112 | 0.803267 | 55150668 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 693,675 | 0.536417 | 55150668 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 646,637 | 5,010,207.279324 | 55150668 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 641,730 | 0.521652 | 55150668 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 615,249 | 0.000008 | 55150668 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v2 | WETH/NPC | 3000 | 612,535 | 149,222.050958 | 55150668 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome | VIRTUAL/WETH | 10000 | 588,015 | 0.000253 | 55150668 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 579,392 | 576,712.111747 | 55150668 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | FLOCK/USDC | 3000 | 567,693 | 0.038557 | 55150668 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome | WETH/msETH (stable) | 500 | 528,231 | 2.378996 | 55150668 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 509,917 | 1,033.778607 | 55150668 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome | cbBTC/EDGE | 7000 | 505,434 | 914,156.513345 | 55150668 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| uniswap_v3 | USDC/USDT | 100 | 497,519 | 1.001238 | 55150668 | `0xD56da2B74bA826f19015E6B7Dd9Dae1903E85DA1` |
| pancakeswap_v3 | ELSA/USDC | 100 | 484,776 | 0.070436 | 55150668 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| aerodrome | WETH/DRV | 3000 | 476,586 | 7,145.846751 | 55150668 | `0xaC4e562d7C6108f971321F14238E24AE2cC398ac` |

## Recherche d'opportunités
- Cycles : 1937 ; routes examinées : 33680556 ; candidats optimisés : 158945 ; net attendu > 0 : 198 ; dernier cycle 460.6 ms
- Rejets (moteur) : {'spread_below_threshold': 32970817, 'liquidity_below_min': 546632, 'negative_expected_net': 158747, 'borrow_bound_too_small': 3873, 'cycle_budget_exhausted': 289}
- Enregistrements de la session : 158945 ; net attendu > 0 : 198 ; simulés (eth_call de la vraie tx) : 6 (ok 6, échec 0) ; étiquettes ghost N+1 : 6/6 positives
- Décisions : {'REJECTED': 158945} ; motifs de rejet : {'below_safety_margin': 187, 'negative_expected_net': 158747, 'p_lower_below_threshold': 186, 'reliability_not_demonstrated': 12, 'sim_below_estimate': 2, 'stale_data': 55}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 55149091 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 596.907834 USDC | 0.096224 USDC | 0.000000 USDC | 0.004729 USDC | 0.091495 USDC (0.0842 €) | — | 1.53 | 0.059 (n=301) | REJECTED | below_safety_margin(91495<119381), p_lower_below_threshold(0.06<0.75) |
| 55149092 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 596.907834 USDC | 0.096224 USDC | 0.000000 USDC | 0.004729 USDC | 0.091495 USDC (0.0842 €) | — | 1.53 | 0.059 (n=301) | REJECTED | below_safety_margin(91495<119381), p_lower_below_threshold(0.06<0.75) |
| 55149091 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.284633 WETH | 0.000046 WETH | 0.000000 WETH | 0.000002 WETH | 0.000043 WETH (0.0841 €) | — | 1.53 | 0.059 (n=301) | REJECTED | below_safety_margin(43444993489647<56926665444047), p_lower_below_threshold(0.06<0.75) |
| 55149092 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.284633 WETH | 0.000046 WETH | 0.000000 WETH | 0.000002 WETH | 0.000043 WETH (0.0841 €) | — | 1.53 | 0.059 (n=301) | REJECTED | below_safety_margin(43444993489647<56926665444047), p_lower_below_threshold(0.06<0.75) |
| 55148022 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 333.059552 USDC | 0.030009 USDC | 0.000000 USDC | 0.005131 USDC | 0.024878 USDC (0.0229 €) | — | 0.75 | 0.059 (n=301) | REJECTED | below_safety_margin(24878<66611), p_lower_below_threshold(0.06<0.75) |
| 55148022 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.158471 WETH | 0.000014 WETH | 0.000000 WETH | 0.000002 WETH | 0.000012 WETH (0.0228 €) | — | 0.74 | 0.059 (n=301) | REJECTED | below_safety_margin(11805362372769<31694116956527), p_lower_below_threshold(0.06<0.75) |
| 55141691 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.100895 WETH | 0.000011 WETH | 0.000000 WETH | 0.000002 WETH | 0.000009 WETH (0.0172 €) | — | 0.88 | 0.059 (n=301) | REJECTED | below_safety_margin(8887739178696<20178939300070), p_lower_below_threshold(0.06<0.75) |
| 55141692 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.100895 WETH | 0.000011 WETH | 0.000000 WETH | 0.000002 WETH | 0.000009 WETH (0.0172 €) | — | 0.88 | 0.059 (n=301) | REJECTED | below_safety_margin(8887739178696<20178939300070), p_lower_below_threshold(0.06<0.75) |
| 55141691 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 210.005583 USDC | 0.023725 USDC | 0.000000 USDC | 0.005060 USDC | 0.018665 USDC (0.0172 €) | — | 0.89 | 0.059 (n=301) | REJECTED | below_safety_margin(18665<42001), p_lower_below_threshold(0.06<0.75) |
| 55141692 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 210.005583 USDC | 0.023725 USDC | 0.000000 USDC | 0.005060 USDC | 0.018665 USDC (0.0172 €) | — | 0.89 | 0.059 (n=301) | REJECTED | below_safety_margin(18665<42001), p_lower_below_threshold(0.06<0.75) |
| 55149091 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 187.328801 USDC | 0.022829 USDC | 0.000000 USDC | 0.004729 USDC | 0.018100 USDC (0.0167 €) | — | 0.97 | 0.048 (n=90) | REJECTED | below_safety_margin(18100<37465), p_lower_below_threshold(0.05<0.75) |
| 55149092 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 187.328801 USDC | 0.022829 USDC | 0.000000 USDC | 0.004729 USDC | 0.018100 USDC (0.0167 €) | — | 0.97 | 0.048 (n=90) | REJECTED | below_safety_margin(18100<37465), p_lower_below_threshold(0.05<0.75) |
| 55149091 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.088955 WETH | 0.000011 WETH | 0.000000 WETH | 0.000002 WETH | 0.000009 WETH (0.0166 €) | — | 0.97 | 0.048 (n=90) | REJECTED | below_safety_margin(8590809096937<17791066151819), p_lower_below_threshold(0.05<0.75) |
| 55149092 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.088955 WETH | 0.000011 WETH | 0.000000 WETH | 0.000002 WETH | 0.000009 WETH (0.0166 €) | — | 0.97 | 0.048 (n=90) | REJECTED | below_safety_margin(8590809096937<17791066151819), p_lower_below_threshold(0.05<0.75) |
| 55143237 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.121072 WETH | 0.000010 WETH | 0.000000 WETH | 0.000002 WETH | 0.000007 WETH (0.0142 €) | — | 0.61 | 0.059 (n=301) | REJECTED | below_safety_margin(7336549129306<24214447333590), p_lower_below_threshold(0.06<0.75) |
| 55143238 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.121072 WETH | 0.000010 WETH | 0.000000 WETH | 0.000002 WETH | 0.000007 WETH (0.0142 €) | — | 0.61 | 0.059 (n=301) | REJECTED | below_safety_margin(7336549129306<24214447333590), p_lower_below_threshold(0.06<0.75) |
| 55143237 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 252.743506 USDC | 0.020164 USDC | 0.000000 USDC | 0.004739 USDC | 0.015425 USDC (0.0142 €) | — | 0.61 | 0.059 (n=301) | REJECTED | below_safety_margin(15425<50548), p_lower_below_threshold(0.06<0.75) |
| 55143238 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 252.743506 USDC | 0.020164 USDC | 0.000000 USDC | 0.004739 USDC | 0.015425 USDC (0.0142 €) | — | 0.61 | 0.059 (n=301) | REJECTED | below_safety_margin(15425<50548), p_lower_below_threshold(0.06<0.75) |
| 55148407 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.087893 WETH | 0.000008 WETH | 0.000000 WETH | 0.000002 WETH | 0.000006 WETH (0.0114 €) | — | 0.67 | 0.059 (n=301) | REJECTED | below_safety_margin(5871668414220<17578525234328), stale_data(4515ms>4000.0), p_lower_below_threshold(0.06<0.75) |
| 55148407 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 182.894792 USDC | 0.017081 USDC | 0.000000 USDC | 0.004729 USDC | 0.012352 USDC (0.0114 €) | — | 0.68 | 0.059 (n=301) | REJECTED | below_safety_margin(12352<36578), stale_data(4520ms>4000.0), p_lower_below_threshold(0.06<0.75) |
| 55150197 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.105293 WETH | 0.000007 WETH | 0.000000 WETH | 0.000002 WETH | 0.000005 WETH (0.0097 €) | — | 0.48 | 0.059 (n=301) | REJECTED | below_safety_margin(5001774652257<21058563495875), p_lower_below_threshold(0.06<0.75) |
| 55150197 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 219.239084 USDC | 0.015237 USDC | 0.000000 USDC | 0.004729 USDC | 0.010508 USDC (0.0097 €) | — | 0.48 | 0.059 (n=301) | REJECTED | below_safety_margin(10508<43847), p_lower_below_threshold(0.06<0.75) |
| 55143643 | WETH→[pancakeswap_v3]→EURC→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.025556 WETH | 0.000007 WETH | 0.000000 WETH | 0.000003 WETH | 0.000004 WETH (0.0081 €) | — | 1.64 | 0.203 (n=1237) | REJECTED | below_safety_margin(4185936773466<5111264866502), stale_data(4666ms>4000.0), p_lower_below_threshold(0.20<0.75) |
| 55143643 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→EURC→[aerodrome_slipstream]→USDC | 53.713136 USDC | 0.015201 USDC | 0.000000 USDC | 0.006437 USDC | 0.008764 USDC (0.0081 €) | — | 1.63 | 0.203 (n=1237) | REJECTED | below_safety_margin(8764<10742), stale_data(4672ms>4000.0), p_lower_below_threshold(0.20<0.75) |
| 55149548 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.076503 WETH | 0.000006 WETH | 0.000000 WETH | 0.000002 WETH | 0.000004 WETH (0.0077 €) | — | 0.52 | 0.059 (n=301) | REJECTED | below_safety_margin(3990471695977<15300675652132), p_lower_below_threshold(0.06<0.75) |

## Fiabilité et décision
- Observations ghost : 6746 ; taux observé 0.178 ; borne inférieure crédible (0.9) 0.172 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 17.2% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
