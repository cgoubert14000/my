# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-10T14:51:47+00:00 ; durée 49.07 min ; blocs 55644907 → 55659616 (2395 vus)

## Connexion
- Requêtes RPC : 34214 ; erreurs : 10 ; latence p50/p95 : 231.9/1,254.0 ms
- Rafraîchissements d'état : 2395 ; âge des données au dernier bloc : 8.21 s ; changements de frais LP observés (pools à frais dynamiques) : 2590
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 2340 ; cycles déclenchés par événement : 505 ; avance médiane sur le rafraîchissement multicall : 535 ms
- Gaz : base fee 0.005022 gwei ; prix ETH (pool le plus profond) : 2,073.45 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 461 pools, 270 jetons, 16362 routes
- Par DEX : uniswap_v3 132, aerodrome_slipstream 99, aerodrome 190, pancakeswap_v3 26, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 164 (rejetés 2) → 569 jetons ; pools candidats 3648 (énumérés 286, par paires 0), mesurés 463, sous le plancher de 10000.0 $ : 2 → gardés 461 (max 1500) ; prix des hubs : {'USDC': 1.0, 'USDbC': 1.0, 'DAI': 1.0, 'WETH': 2067.744894, 'cbBTC': 73787.664735, 'AERO': 0.555242}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 135,901,484 | 2,073.448739 | 55659639 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,260,237 | 0.027998 | 55659639 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,379,533 | 0.000014 | 55659639 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 8,618,500 | 0.028005 | 55659639 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 7,337,361 | 2,071.456132 | 55659639 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 6,894,855 | 105.591731 | 55659639 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| aerodrome | USDC/AERO | 3000 | 4,365,077 | 1.789733 | 55659639 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,321,324 | 0.028002 | 55659639 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 3,937,709 | 2,072.241533 | 55659639 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,896,988 | 0.999802 | 55659639 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,060,605 | 42,952.367153 | 55659639 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 150 | 2,954,021 | 2,072.182315 | 55659639 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,289,614 | 0.028020 | 55659639 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 1,982,260 | 1,109,075.760713 | 55659639 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,687,566 | 0.000014 | 55659639 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | USDC/cbBTC | 568 | 1,661,649 | 0.000014 | 55659639 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | XDP/USDC | 100 | 1,614,505 | 0.016279 | 55659639 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,549,468 | 0.006689 | 55659639 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,517,481 | 0.000000 | 55659639 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,499,792 | 0.000013 | 55659639 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,461,050 | 0.821956 | 55659639 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,454,704 | 1.378588 | 55659639 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,437,930 | 414.776207 | 55659639 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v2 | WETH/USDC | 3000 | 1,276,710 | 2,073.753830 | 55659639 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| uniswap_v3 | WETH/AERO | 3000 | 1,268,556 | 3,713.166910 | 55659639 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,241,948 | 14,831.964804 | 55659639 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/USDC | 3000 | 1,205,630 | 2,072.953420 | 55659639 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome | USDC/SEND | 3000 | 1,106,702 | 79.337354 | 55659639 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,049,249 | 2,071.439836 | 55659639 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | WETH/doginme | 10000 | 1,036,086 | 35,265,552.209358 | 55659639 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome_slipstream | USDC/VELVET | 100 | 959,249 | 21.440070 | 55659639 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/BRETT | 10000 | 950,007 | 558,916.958532 | 55659639 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | WETH/VVV | 10000 | 927,374 | 104.859028 | 55659639 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome_slipstream | USDC/cbBTC | 350 | 920,423 | 0.000014 | 55659639 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 918,877 | 0.001483 | 55659639 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| uniswap_v3 | WETH/TOSHI | 10000 | 918,650 | 22,771,584.884619 | 55659639 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | USDC/VVV | 3000 | 900,497 | 0.051003 | 55659639 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/MORPHO | 3000 | 894,133 | 1,022.268720 | 55659639 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/USDC | 10000 | 879,162 | 2,071.230075 | 55659639 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | DRB/WETH | 10000 | 868,849 | 0.000000 | 55659639 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | USDC/NOCK | 3000 | 788,410 | 75.670823 | 55659639 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | USDC/SAPIEN | 4510 | 777,407 | 21.780293 | 55659639 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome | WETH/EDEL | 7000 | 772,085 | 109,950.922805 | 55659639 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| pancakeswap_v3 | QUID/USDC | 100 | 760,065 | 0.051529 | 55659639 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/AERO | 10000 | 727,736 | 3,710.753909 | 55659639 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | WETH/wstETH | 3000 | 701,896 | 0.803151 | 55659639 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 655,573 | 0.538128 | 55659639 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 648,050 | 4,846,485.887071 | 55659639 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 642,408 | 0.518639 | 55659639 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 608,234 | 0.000008 | 55659639 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v2 | WETH/NPC | 3000 | 586,499 | 158,195.973403 | 55659639 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome | VIRTUAL/WETH | 10000 | 583,789 | 0.000257 | 55659639 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/BRETT | 2096 | 582,958 | 554,721.779581 | 55659639 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | FLOCK/USDC | 3000 | 566,186 | 0.038394 | 55659639 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome_slipstream | WETH/MORPHO | 2718 | 504,680 | 1,022.001633 | 55659639 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| pancakeswap_v3 | ELSA/USDC | 100 | 485,044 | 0.070813 | 55659639 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| aerodrome | WETH/DRV | 3000 | 484,448 | 6,717.814059 | 55659639 | `0xaC4e562d7C6108f971321F14238E24AE2cC398ac` |
| aerodrome_slipstream | USDC/USDT | 8 | 455,525 | 1.001153 | 55659639 | `0xa41Bc0AFfbA7Fd420d186b84899d7ab2aC57fcD1` |
| uniswap_v3 | WETH/UNI | 10000 | 453,954 | 296.329143 | 55659639 | `0xAb365f161Dd501473a1ff0D2ef0dCE94E7398839` |
| uniswap_v3 | WETH/uSOL | 3000 | 445,108 | 24.759492 | 55659639 | `0xab04A352D4EC8d0F1812A4E5EBe7807Fa67acD48` |

## Recherche d'opportunités
- Cycles : 2899 ; routes examinées : 47433438 ; candidats optimisés : 204211 ; net attendu > 0 : 1265 ; dernier cycle 377.5 ms
- Rejets (moteur) : {'spread_below_threshold': 46485744, 'liquidity_below_min': 726261, 'negative_expected_net': 202946, 'pool_quarantined': 11826, 'borrow_bound_too_small': 4957, 'cycle_budget_exhausted': 439}
- Enregistrements de la session : 204211 ; net attendu > 0 : 1265 ; simulés (eth_call de la vraie tx) : 62 (ok 44, échec 18) ; étiquettes ghost N+1 : 26/50 positives
- Décisions : {'REJECTED': 204211} ; motifs de rejet : {'below_safety_margin': 1072, 'negative_expected_net': 202946, 'p_lower_below_threshold': 1234, 'reliability_not_demonstrated': 31, 'sim_below_estimate': 4, 'simulated_net_nonpositive': 1, 'simulation_failed': 18, 'stale_data': 200}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 55656217 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 496.019379 USDC | 0.073011 USDC | 0.000000 USDC | 0.005127 USDC | 0.067884 USDC (0.0625 €) | — | 1.37 | 0.086 (n=340) | REJECTED | below_safety_margin(67884<99203), p_lower_below_threshold(0.09<0.75) |
| 55656217 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.238660 WETH | 0.000035 WETH | 0.000000 WETH | 0.000002 WETH | 0.000033 WETH (0.0624 €) | — | 1.37 | 0.086 (n=340) | REJECTED | below_safety_margin(32640227257654<47731912546365), p_lower_below_threshold(0.09<0.75) |
| 55647094 | cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH→[uniswap_v3]→cbBTC | 0.004596 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0468 €) | — | 1.50 | 0.316 (n=517) | REJECTED | below_safety_margin(69<91), p_lower_below_threshold(0.32<0.75) |
| 55647094 | WETH→[uniswap_v3]→cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.174281 WETH | 0.000028 WETH | 0.000000 WETH | 0.000003 WETH | 0.000025 WETH (0.0466 €) | — | 1.41 | 0.316 (n=517) | REJECTED | below_safety_margin(24518343617352<34856237954381), p_lower_below_threshold(0.32<0.75) |
| 55647094 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 364.443705 USDC | 0.056893 USDC | 0.000000 USDC | 0.006281 USDC | 0.050612 USDC (0.0466 €) | — | 1.39 | 0.316 (n=517) | REJECTED | below_safety_margin(50612<72888), p_lower_below_threshold(0.32<0.75) |
| 55654854 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WBTC→[uniswap_v3]→cbBTC | 0.003711 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0394 €) | — | 1.56 | 0.230 (n=1426) | REJECTED | below_safety_margin(58<74), p_lower_below_threshold(0.23<0.75) |
| 55647094 | cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.003909 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0394 €) | — | 1.48 | 0.227 (n=1406) | REJECTED | below_safety_margin(58<78), p_lower_below_threshold(0.23<0.75) |
| 55647094 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.150305 WETH | 0.000024 WETH | 0.000000 WETH | 0.000003 WETH | 0.000021 WETH (0.0393 €) | — | 1.37 | 0.227 (n=1406) | REJECTED | below_safety_margin(20664748044216<30061088872016), p_lower_below_threshold(0.23<0.75) |
| 55647094 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 297.718576 USDC | 0.048873 USDC | 0.000000 USDC | 0.006281 USDC | 0.042592 USDC (0.0392 €) | — | 1.43 | 0.227 (n=1406) | REJECTED | below_safety_margin(42592<59543), p_lower_below_threshold(0.23<0.75) |
| 55654854 | USDC→[uniswap_v3]→WBTC→[uniswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 310.056130 USDC | 0.049631 USDC | 0.000000 USDC | 0.007342 USDC | 0.042289 USDC (0.0389 €) | — | 1.36 | 0.230 (n=1426) | REJECTED | below_safety_margin(42289<62011), p_lower_below_threshold(0.23<0.75) |
| 55645931 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.006254 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0387 €) | — | 0.91 | 0.059 (n=36) | REJECTED | below_safety_margin(57<125), p_lower_below_threshold(0.06<0.75) |
| 55645931 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.223435 WETH | 0.000023 WETH | 0.000000 WETH | 0.000003 WETH | 0.000020 WETH (0.0384 €) | — | 0.90 | 0.059 (n=36) | REJECTED | below_safety_margin(20184448102296<44686993205901), p_lower_below_threshold(0.06<0.75) |
| 55645931 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 462.507606 USDC | 0.047993 USDC | 0.000000 USDC | 0.006274 USDC | 0.041719 USDC (0.0384 €) | — | 0.90 | 0.059 (n=36) | REJECTED | below_safety_margin(41719<92501), p_lower_below_threshold(0.06<0.75) |
| 55658963 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.006197 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0361 €) | — | 0.86 | 0.077 (n=37) | REJECTED | below_safety_margin(53<123), p_lower_below_threshold(0.08<0.75) |
| 55658964 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.006197 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0361 €) | — | 0.86 | 0.077 (n=37) | REJECTED | below_safety_margin(53<123), p_lower_below_threshold(0.08<0.75) |
| 55658963 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.258626 WETH | 0.000022 WETH | 0.000000 WETH | 0.000003 WETH | 0.000019 WETH (0.0357 €) | — | 0.72 | 0.077 (n=37) | REJECTED | below_safety_margin(18702234726837<51725228019350), p_lower_below_threshold(0.08<0.75) |
| 55658964 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.258626 WETH | 0.000022 WETH | 0.000000 WETH | 0.000003 WETH | 0.000019 WETH (0.0357 €) | — | 0.72 | 0.077 (n=37) | REJECTED | below_safety_margin(18700189286237<51725228019350), p_lower_below_threshold(0.08<0.75) |
| 55658963 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 488.588780 USDC | 0.045411 USDC | 0.000000 USDC | 0.006657 USDC | 0.038754 USDC (0.0357 €) | — | 0.79 | 0.077 (n=37) | REJECTED | below_safety_margin(38754<97717), p_lower_below_threshold(0.08<0.75) |
| 55658964 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 488.588780 USDC | 0.045411 USDC | 0.000000 USDC | 0.006661 USDC | 0.038750 USDC (0.0357 €) | — | 0.79 | 0.077 (n=37) | REJECTED | below_safety_margin(38750<97717), p_lower_below_threshold(0.08<0.75) |
| 55647094 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.099025 WETH | 0.000020 WETH | 0.000000 WETH | 0.000003 WETH | 0.000017 WETH (0.0314 €) | — | 1.67 | 0.227 (n=1406) | REJECTED | below_safety_margin(16512542878146<19804904995583), p_lower_below_threshold(0.23<0.75) |
| 55647094 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 200.308158 USDC | 0.040373 USDC | 0.000000 USDC | 0.006281 USDC | 0.034092 USDC (0.0314 €) | — | 1.70 | 0.227 (n=1406) | REJECTED | below_safety_margin(34092<40061), p_lower_below_threshold(0.23<0.75) |
| 55647094 | cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.002455 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0312 €) | — | 1.87 | 0.227 (n=1406) | REJECTED | below_safety_margin(46<49), p_lower_below_threshold(0.23<0.75) |
| 55654408 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→cbBTC | 0.004688 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0298 €) | — | 0.94 | 0.227 (n=1416) | REJECTED | below_safety_margin(44<93), p_lower_below_threshold(0.23<0.75) |
| 55654408 | USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 411.088953 USDC | 0.038588 USDC | 0.000000 USDC | 0.006379 USDC | 0.032209 USDC (0.0296 €) | — | 0.78 | 0.227 (n=1416) | REJECTED | below_safety_margin(32209<82217), p_lower_below_threshold(0.23<0.75) |
| 55654408 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.176169 WETH | 0.000019 WETH | 0.000000 WETH | 0.000003 WETH | 0.000015 WETH (0.0293 €) | — | 0.88 | 0.227 (n=1416) | REJECTED | below_safety_margin(15419260660434<35233718328412), p_lower_below_threshold(0.23<0.75) |

## Fiabilité et décision
- Observations ghost : 7555 ; taux observé 0.195 ; borne inférieure crédible (0.9) 0.189 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 18.9% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ✅ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
