# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-10T16:18:58+00:00 ; durée 136.25 min ; blocs 55644907 → 55685764 (6596 vus)

## Connexion
- Requêtes RPC : 92036 ; erreurs : 220 ; latence p50/p95 : 280.9/1,335.2 ms
- Rafraîchissements d'état : 6596 ; âge des données au dernier bloc : 4.86 s ; changements de frais LP observés (pools à frais dynamiques) : 8656
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 5086 ; cycles déclenchés par événement : 932 ; avance médiane sur le rafraîchissement multicall : 569 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,030.89 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 461 pools, 270 jetons, 16362 routes
- Par DEX : uniswap_v3 132, aerodrome_slipstream 99, aerodrome 190, pancakeswap_v3 26, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 164 (rejetés 2) → 569 jetons ; pools candidats 3648 (énumérés 286, par paires 0), mesurés 463, sous le plancher de 10000.0 $ : 2 → gardés 461 (max 1500) ; prix des hubs : {'USDC': 1.0, 'USDbC': 1.0, 'DAI': 1.0, 'WETH': 2067.744894, 'cbBTC': 73787.664735, 'AERO': 0.555242}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 133,047,285 | 2,030.893231 | 55685764 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,234,157 | 0.027704 | 55685764 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 8,997,756 | 0.000014 | 55685764 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 8,466,604 | 0.027646 | 55685764 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 7,112,523 | 2,033.962646 | 55685764 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 6,773,577 | 104.961882 | 55685764 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| aerodrome | USDC/AERO | 3000 | 4,317,120 | 1.829712 | 55685764 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,272,158 | 0.027694 | 55685764 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,857,487 | 0.999802 | 55685764 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| pancakeswap_v3 | WETH/USDC | 100 | 3,821,404 | 2,033.651030 | 55685764 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | WETH/KTA | 3000 | 2,994,313 | 43,052.148358 | 55685764 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 150 | 2,900,997 | 2,033.622341 | 55685764 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2505 | 2,240,447 | 0.027661 | 55685764 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 1,938,271 | 1,112,861.197332 | 55685764 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,671,734 | 0.000014 | 55685764 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | USDC/cbBTC | 600 | 1,649,268 | 0.000014 | 55685764 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | XDP/USDC | 100 | 1,621,456 | 0.016383 | 55685764 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,534,673 | 0.006781 | 55685764 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,490,421 | 0.000000 | 55685764 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,489,863 | 0.000014 | 55685764 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,462,743 | 0.822038 | 55685764 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,454,698 | 1.378597 | 55685764 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,406,501 | 412.650125 | 55685764 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v2 | WETH/USDC | 3000 | 1,263,539 | 2,030.093810 | 55685764 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| uniswap_v3 | WETH/AERO | 3000 | 1,241,501 | 3,712.786651 | 55685764 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,226,587 | 14,914.930916 | 55685764 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/USDC | 3000 | 1,193,194 | 2,030.372116 | 55685764 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome | USDC/SEND | 3000 | 1,106,361 | 79.386245 | 55685764 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,044,611 | 2,033.947359 | 55685764 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | WETH/doginme | 10000 | 1,017,167 | 34,863,423.994171 | 55685764 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome_slipstream | USDC/VELVET | 100 | 956,569 | 21.625864 | 55685764 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/BRETT | 10000 | 933,053 | 554,512.257641 | 55685764 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | WETH/VVV | 10000 | 912,352 | 105.108034 | 55685764 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome_slipstream | USDC/cbBTC | 358 | 911,705 | 0.000014 | 55685764 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 904,844 | 0.001468 | 55685764 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| uniswap_v3 | WETH/TOSHI | 10000 | 903,958 | 22,595,229.025818 | 55685764 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | USDC/VVV | 3000 | 882,784 | 0.051546 | 55685764 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/MORPHO | 3000 | 879,843 | 1,012.620796 | 55685764 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/USDC | 10000 | 871,112 | 2,025.243169 | 55685764 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | DRB/WETH | 10000 | 853,954 | 0.000000 | 55685764 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | USDC/NOCK | 3000 | 796,206 | 74.196198 | 55685764 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 766,942 | 22.200321 | 55685764 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 761,252 | 0.051696 | 55685764 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/EDEL | 7000 | 754,028 | 110,597.047500 | 55685764 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | WETH/AERO | 10000 | 712,313 | 3,710.753909 | 55685764 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | WETH/wstETH | 3000 | 687,504 | 0.803119 | 55685764 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 647,424 | 0.529066 | 55685764 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v3 | TIG/USDC | 10000 | 640,018 | 0.514947 | 55685764 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 636,765 | 4,815,945.727971 | 55685764 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 590,288 | 0.000007 | 55685764 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | VIRTUAL/WETH | 10000 | 573,503 | 0.000259 | 55685764 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/BRETT | 2120 | 573,361 | 553,964.974740 | 55685764 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v2 | WETH/NPC | 3000 | 573,168 | 158,920.032327 | 55685764 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| uniswap_v3 | FLOCK/USDC | 3000 | 558,372 | 0.037579 | 55685764 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome_slipstream | WETH/MORPHO | 2709 | 496,842 | 1,012.457659 | 55685764 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| pancakeswap_v3 | ELSA/USDC | 100 | 484,314 | 0.070627 | 55685764 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| aerodrome | WETH/DRV | 3000 | 477,073 | 6,645.688897 | 55685764 | `0xaC4e562d7C6108f971321F14238E24AE2cC398ac` |
| aerodrome_slipstream | USDC/USDT | 8 | 455,456 | 1.001343 | 55685764 | `0xa41Bc0AFfbA7Fd420d186b84899d7ab2aC57fcD1` |
| uniswap_v3 | WETH/UNI | 10000 | 445,147 | 295.265436 | 55685764 | `0xAb365f161Dd501473a1ff0D2ef0dCE94E7398839` |
| uniswap_v3 | USDC/MORPHO | 10000 | 441,288 | 0.500303 | 55685764 | `0x2043B296fFC6b2d3bf4A3F3167d2Afb3B0FBdbEE` |

## Recherche d'opportunités
- Cycles : 7527 ; routes examinées : 123156774 ; candidats optimisés : 685122 ; net attendu > 0 : 4915 ; dernier cycle 239.4 ms
- Rejets (moteur) : {'spread_below_threshold': 120432903, 'liquidity_below_min': 1989704, 'negative_expected_net': 680207, 'pool_quarantined': 25258, 'borrow_bound_too_small': 13546, 'cycle_budget_exhausted': 10241}
- Enregistrements de la session : 685122 ; net attendu > 0 : 4915 ; simulés (eth_call de la vraie tx) : 250 (ok 184, échec 66) ; étiquettes ghost N+1 : 112/208 positives
- Décisions : {'REJECTED': 685122} ; motifs de rejet : {'below_safety_margin': 3996, 'negative_expected_net': 680207, 'p_lower_below_threshold': 4760, 'reliability_not_demonstrated': 155, 'sim_below_estimate': 32, 'simulated_net_nonpositive': 22, 'simulation_failed': 66, 'stale_data': 523}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 55670011 | WETH→[aerodrome_slipstream]→USDC→[aerodrome]→AUKI→[pancakeswap_v3]→WETH | 0.066963 WETH | 0.000440 WETH | 0.000000 WETH | 0.000003 WETH | 0.000438 WETH (0.8349 €) | — | 65.34 | 0.001 (n=10) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 55670011 | USDC→[aerodrome]→AUKI→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 138.463970 USDC | 0.912685 USDC | 0.000000 USDC | 0.006029 USDC | 0.906656 USDC (0.8341 €) | — | 65.48 | 0.001 (n=10) | REJECTED | reliability_not_demonstrated |
| 55670011 | WETH→[pancakeswap_v3]→USDC→[aerodrome]→AUKI→[pancakeswap_v3]→WETH | 0.066851 WETH | 0.000438 WETH | 0.000000 WETH | 0.000003 WETH | 0.000435 WETH (0.8303 €) | — | 65.10 | 0.001 (n=8) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 55670011 | USDC→[aerodrome]→AUKI→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 138.459955 USDC | 0.907719 USDC | 0.000000 USDC | 0.006029 USDC | 0.901690 USDC (0.8296 €) | — | 65.12 | 0.001 (n=8) | REJECTED | reliability_not_demonstrated |
| 55670011 | WETH→[uniswap_v3]→USDC→[aerodrome]→AUKI→[pancakeswap_v3]→WETH | 0.066134 WETH | 0.000434 WETH | 0.000000 WETH | 0.000003 WETH | 0.000432 WETH (0.8233 €) | — | 65.25 | 0.001 (n=10) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 55670011 | USDC→[aerodrome]→AUKI→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 136.946975 USDC | 0.899995 USDC | 0.000000 USDC | 0.006029 USDC | 0.893966 USDC (0.8224 €) | — | 65.28 | 0.001 (n=10) | REJECTED | reliability_not_demonstrated |
| 55670011 | WETH→[uniswap_v3]→USDC→[aerodrome]→AUKI→[pancakeswap_v3]→WETH | 0.064805 WETH | 0.000411 WETH | 0.000000 WETH | 0.000003 WETH | 0.000408 WETH (0.7789 €) | — | 62.99 | 0.001 (n=10) | REJECTED | reliability_not_demonstrated |
| 55670011 | USDC→[aerodrome]→AUKI→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 134.087851 USDC | 0.851510 USDC | 0.000000 USDC | 0.006029 USDC | 0.845481 USDC (0.7778 €) | — | 63.05 | 0.001 (n=10) | REJECTED | reliability_not_demonstrated |
| 55670011 | WETH→[pancakeswap_v3]→USDC→[aerodrome]→AUKI→[pancakeswap_v3]→WETH | 0.064117 WETH | 0.000405 WETH | 0.000000 WETH | 0.000003 WETH | 0.000402 WETH (0.7671 €) | — | 62.71 | 0.001 (n=8) | REJECTED | reliability_not_demonstrated |
| 55670011 | USDC→[aerodrome]→AUKI→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 132.821327 USDC | 0.838622 USDC | 0.000000 USDC | 0.006029 USDC | 0.832593 USDC (0.7660 €) | — | 62.69 | 0.001 (n=8) | REJECTED | reliability_not_demonstrated |
| 55670011 | WETH→[uniswap_v3]→AUKI→[pancakeswap_v3]→WETH | 0.071959 WETH | 0.000375 WETH | 0.000000 WETH | 0.000002 WETH | 0.000373 WETH (0.7119 €) | — | 51.85 | 0.002 (n=4) | REJECTED | reliability_not_demonstrated |
| 55670011 | WETH→[sushiswap_v3]→USDC→[aerodrome]→AUKI→[pancakeswap_v3]→WETH | 0.055050 WETH | 0.000345 WETH | 0.000000 WETH | 0.000003 WETH | 0.000342 WETH (0.6532 €) | — | 62.19 | 0.001 (n=10) | REJECTED | reliability_not_demonstrated |
| 55670011 | USDC→[aerodrome]→AUKI→[pancakeswap_v3]→WETH→[sushiswap_v3]→USDC | 113.877973 USDC | 0.714076 USDC | 0.000000 USDC | 0.006344 USDC | 0.707732 USDC (0.6511 €) | — | 62.15 | 0.001 (n=10) | REJECTED | reliability_not_demonstrated |
| 55670011 | WETH→[uniswap_v3]→USDC→[aerodrome]→AUKI→[pancakeswap_v3]→WETH | 0.056208 WETH | 0.000309 WETH | 0.000000 WETH | 0.000003 WETH | 0.000306 WETH (0.5834 €) | — | 54.40 | 0.001 (n=10) | REJECTED | reliability_not_demonstrated |
| 55670011 | USDC→[aerodrome]→AUKI→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 116.152836 USDC | 0.638193 USDC | 0.000000 USDC | 0.006029 USDC | 0.632164 USDC (0.5816 €) | — | 54.43 | 0.001 (n=10) | REJECTED | reliability_not_demonstrated |
| 55670011 | WETH→[uniswap_v2]→USDC→[aerodrome]→AUKI→[pancakeswap_v3]→WETH | 0.055179 WETH | 0.000307 WETH | 0.000000 WETH | 0.000003 WETH | 0.000305 WETH (0.5811 €) | — | 55.20 | 0.002 (n=3) | REJECTED | reliability_not_demonstrated |
| 55670011 | USDC→[aerodrome]→AUKI→[pancakeswap_v3]→WETH→[uniswap_v2]→USDC | 114.010951 USDC | 0.634991 USDC | 0.000000 USDC | 0.005385 USDC | 0.629606 USDC (0.5792 €) | — | 55.22 | 0.002 (n=3) | REJECTED | reliability_not_demonstrated |
| 55670011 | WETH→[aerodrome]→USDC→[aerodrome]→AUKI→[pancakeswap_v3]→WETH | 0.051894 WETH | 0.000272 WETH | 0.000000 WETH | 0.000003 WETH | 0.000269 WETH (0.5136 €) | — | 51.87 | 0.001 (n=8) | REJECTED | reliability_not_demonstrated |
| 55670011 | USDC→[aerodrome]→AUKI→[pancakeswap_v3]→WETH→[aerodrome]→USDC | 107.024642 USDC | 0.561837 USDC | 0.000000 USDC | 0.005743 USDC | 0.556094 USDC (0.5116 €) | — | 51.96 | 0.001 (n=8) | REJECTED | reliability_not_demonstrated |
| 55670011 | WETH→[aerodrome_slipstream]→USDC→[aerodrome]→AUKI→[pancakeswap_v3]→WETH | 0.045931 WETH | 0.000268 WETH | 0.000000 WETH | 0.000004 WETH | 0.000264 WETH (0.5046 €) | — | 57.58 | 0.001 (n=10) | REJECTED | reliability_not_demonstrated |
| 55670011 | USDC→[aerodrome]→AUKI→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 94.751963 USDC | 0.553346 USDC | 0.000000 USDC | 0.007603 USDC | 0.545743 USDC (0.5021 €) | — | 57.60 | 0.001 (n=10) | REJECTED | reliability_not_demonstrated |
| 55673391 | WETH→[uniswap_v3]→USDT→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.166322 WETH | 0.000083 WETH | 0.000000 WETH | 0.000003 WETH | 0.000079 WETH (0.1490 €) | 0.000093 WETH | 4.78 | 0.294 (n=497) | REJECTED | p_lower_below_threshold(0.29<0.75) |
| 55673391 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→USDT→[uniswap_v3]→USDC | 338.063724 USDC | 0.168254 USDC | 0.000000 USDC | 0.006565 USDC | 0.161689 USDC (0.1488 €) | — | 4.78 | 0.294 (n=497) | REJECTED | p_lower_below_threshold(0.29<0.75) |
| 55673391 | WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.164272 WETH | 0.000081 WETH | 0.000000 WETH | 0.000003 WETH | 0.000078 WETH (0.1464 €) | 0.000091 WETH | 4.75 | 0.294 (n=497) | REJECTED | p_lower_below_threshold(0.29<0.75) |
| 55673391 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC | 333.379060 USDC | 0.165370 USDC | 0.000000 USDC | 0.006565 USDC | 0.158805 USDC (0.1461 €) | — | 4.76 | 0.294 (n=497) | REJECTED | p_lower_below_threshold(0.29<0.75) |

## Fiabilité et décision
- Observations ghost : 7713 ; taux observé 0.202 ; borne inférieure crédible (0.9) 0.196 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 19.6% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ✅ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
