# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-10T15:16:29+00:00 ; durée 73.76 min ; blocs 55644907 → 55667026 (3704 vus)

## Connexion
- Requêtes RPC : 51446 ; erreurs : 20 ; latence p50/p95 : 250.6/1,408.3 ms
- Rafraîchissements d'état : 3704 ; âge des données au dernier bloc : 6.89 s ; changements de frais LP observés (pools à frais dynamiques) : 4321
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 2340 ; cycles déclenchés par événement : 505 ; avance médiane sur le rafraîchissement multicall : 535 ms
- Gaz : base fee 0.005003 gwei ; prix ETH (pool le plus profond) : 2,075.18 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 461 pools, 270 jetons, 16362 routes
- Par DEX : uniswap_v3 132, aerodrome_slipstream 99, aerodrome 190, pancakeswap_v3 26, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 164 (rejetés 2) → 569 jetons ; pools candidats 3648 (énumérés 286, par paires 0), mesurés 463, sous le plancher de 10000.0 $ : 2 → gardés 461 (max 1500) ; prix des hubs : {'USDC': 1.0, 'USDbC': 1.0, 'DAI': 1.0, 'WETH': 2067.744894, 'cbBTC': 73787.664735, 'AERO': 0.555242}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 109,380,026 | 2,075.183541 | 55667026 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,275,275 | 0.027884 | 55667026 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,420,441 | 0.000013 | 55667026 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 8,633,631 | 0.027941 | 55667026 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 7,342,781 | 2,070.209530 | 55667026 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 6,981,858 | 103.148899 | 55667026 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| aerodrome | USDC/AERO | 3000 | 4,378,617 | 1.778677 | 55667026 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,337,465 | 0.027883 | 55667026 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 3,940,726 | 2,069.993375 | 55667026 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,916,243 | 0.999802 | 55667026 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,063,166 | 42,952.367153 | 55667026 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 150 | 2,956,219 | 2,070.039539 | 55667026 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2595 | 2,292,923 | 0.027932 | 55667026 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 1,981,597 | 1,111,676.761782 | 55667026 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,693,992 | 0.000013 | 55667026 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | USDC/cbBTC | 600 | 1,667,742 | 0.000013 | 55667026 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | XDP/USDC | 100 | 1,619,911 | 0.016360 | 55667026 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,550,763 | 0.006689 | 55667026 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,518,831 | 0.000000 | 55667026 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,504,690 | 0.000013 | 55667026 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,461,050 | 0.821956 | 55667026 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,454,698 | 1.378597 | 55667026 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,437,229 | 412.518102 | 55667026 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v2 | WETH/USDC | 3000 | 1,277,204 | 2,075.152244 | 55667026 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| uniswap_v3 | WETH/AERO | 3000 | 1,273,681 | 3,691.616944 | 55667026 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,248,824 | 14,767.619490 | 55667026 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/USDC | 3000 | 1,206,134 | 2,075.189224 | 55667026 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome | USDC/SEND | 3000 | 1,106,632 | 79.347328 | 55667026 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,052,320 | 2,069.917634 | 55667026 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | WETH/doginme | 10000 | 1,036,951 | 35,265,552.209358 | 55667026 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome_slipstream | USDC/VELVET | 100 | 961,922 | 21.257914 | 55667026 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/BRETT | 10000 | 953,382 | 554,544.354099 | 55667026 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | WETH/VVV | 10000 | 941,500 | 103.652186 | 55667026 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome_slipstream | USDC/cbBTC | 390 | 924,647 | 0.000013 | 55667026 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 924,092 | 0.001485 | 55667026 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| uniswap_v3 | WETH/TOSHI | 10000 | 920,774 | 22,715,021.049960 | 55667026 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | USDC/VVV | 3000 | 918,610 | 0.049842 | 55667026 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/MORPHO | 3000 | 896,502 | 1,018.555383 | 55667026 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/USDC | 10000 | 879,476 | 2,073.739809 | 55667026 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | DRB/WETH | 10000 | 870,610 | 0.000000 | 55667026 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | USDC/NOCK | 3000 | 791,407 | 75.098733 | 55667026 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | USDC/SAPIEN | 4575 | 781,135 | 21.634916 | 55667026 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome | WETH/EDEL | 7000 | 771,257 | 110,371.857315 | 55667026 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| pancakeswap_v3 | QUID/USDC | 100 | 762,433 | 0.051862 | 55667026 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/AERO | 10000 | 730,302 | 3,710.753909 | 55667026 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | WETH/wstETH | 3000 | 702,492 | 0.803132 | 55667026 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 659,149 | 0.542007 | 55667026 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 648,866 | 4,842,399.299035 | 55667026 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 642,408 | 0.518639 | 55667026 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 611,752 | 0.000008 | 55667026 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v2 | WETH/NPC | 3000 | 588,898 | 157,173.998306 | 55667026 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome | VIRTUAL/WETH | 10000 | 585,939 | 0.000259 | 55667026 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/BRETT | 2099 | 585,843 | 550,760.975550 | 55667026 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | FLOCK/USDC | 3000 | 568,024 | 0.038585 | 55667026 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome_slipstream | WETH/MORPHO | 2712 | 506,123 | 1,018.236722 | 55667026 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| pancakeswap_v3 | ELSA/USDC | 100 | 487,069 | 0.071158 | 55667026 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| aerodrome | WETH/DRV | 3000 | 485,517 | 6,699.461394 | 55667026 | `0xaC4e562d7C6108f971321F14238E24AE2cC398ac` |
| aerodrome_slipstream | USDC/USDT | 11 | 455,530 | 1.001128 | 55667026 | `0xa41Bc0AFfbA7Fd420d186b84899d7ab2aC57fcD1` |
| uniswap_v3 | WETH/UNI | 10000 | 454,283 | 295.265436 | 55667026 | `0xAb365f161Dd501473a1ff0D2ef0dCE94E7398839` |
| uniswap_v3 | USDC/MORPHO | 10000 | 446,075 | 0.491422 | 55667026 | `0x2043B296fFC6b2d3bf4A3F3167d2Afb3B0FBdbEE` |

## Recherche d'opportunités
- Cycles : 4208 ; routes examinées : 68851296 ; candidats optimisés : 315178 ; net attendu > 0 : 1911 ; dernier cycle 293.4 ms
- Rejets (moteur) : {'spread_below_threshold': 67443469, 'liquidity_below_min': 1072312, 'negative_expected_net': 313267, 'pool_quarantined': 11826, 'borrow_bound_too_small': 7008, 'cycle_budget_exhausted': 1361}
- Enregistrements de la session : 315178 ; net attendu > 0 : 1911 ; simulés (eth_call de la vraie tx) : 96 (ok 78, échec 18) ; étiquettes ghost N+1 : 45/79 positives
- Décisions : {'REJECTED': 315178} ; motifs de rejet : {'below_safety_margin': 1622, 'negative_expected_net': 313267, 'p_lower_below_threshold': 1842, 'reliability_not_demonstrated': 69, 'sim_below_estimate': 6, 'simulated_net_nonpositive': 2, 'simulation_failed': 18, 'stale_data': 241}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 55656217 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 496.019379 USDC | 0.073011 USDC | 0.000000 USDC | 0.005127 USDC | 0.067884 USDC (0.0625 €) | — | 1.37 | 0.086 (n=340) | REJECTED | below_safety_margin(67884<99203), p_lower_below_threshold(0.09<0.75) |
| 55656217 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.238660 WETH | 0.000035 WETH | 0.000000 WETH | 0.000002 WETH | 0.000033 WETH (0.0624 €) | — | 1.37 | 0.086 (n=340) | REJECTED | below_safety_margin(32640227257654<47731912546365), p_lower_below_threshold(0.09<0.75) |
| 55647094 | cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH→[uniswap_v3]→cbBTC | 0.004596 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0468 €) | — | 1.50 | 0.316 (n=517) | REJECTED | below_safety_margin(69<91), p_lower_below_threshold(0.32<0.75) |
| 55647094 | WETH→[uniswap_v3]→cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.174281 WETH | 0.000028 WETH | 0.000000 WETH | 0.000003 WETH | 0.000025 WETH (0.0466 €) | — | 1.41 | 0.316 (n=517) | REJECTED | below_safety_margin(24518343617352<34856237954381), p_lower_below_threshold(0.32<0.75) |
| 55647094 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 364.443705 USDC | 0.056893 USDC | 0.000000 USDC | 0.006281 USDC | 0.050612 USDC (0.0466 €) | — | 1.39 | 0.316 (n=517) | REJECTED | below_safety_margin(50612<72888), p_lower_below_threshold(0.32<0.75) |
| 55662322 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 571.454285 USDC | 0.056084 USDC | 0.000000 USDC | 0.006843 USDC | 0.049241 USDC (0.0453 €) | — | 0.86 | 0.077 (n=37) | REJECTED | below_safety_margin(49241<114290), p_lower_below_threshold(0.08<0.75) |
| 55662322 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.277744 WETH | 0.000027 WETH | 0.000000 WETH | 0.000003 WETH | 0.000024 WETH (0.0452 €) | — | 0.85 | 0.077 (n=37) | REJECTED | below_safety_margin(23600759272259<55548795018163), p_lower_below_threshold(0.08<0.75) |
| 55662322 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.007166 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0451 €) | — | 0.92 | 0.077 (n=37) | REJECTED | below_safety_margin(66<143), p_lower_below_threshold(0.08<0.75) |
| 55662693 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 573.889526 USDC | 0.050417 USDC | 0.000000 USDC | 0.006981 USDC | 0.043436 USDC (0.0400 €) | — | 0.76 | 0.077 (n=37) | REJECTED | below_safety_margin(43436<114777), p_lower_below_threshold(0.08<0.75) |
| 55662693 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.263762 WETH | 0.000024 WETH | 0.000000 WETH | 0.000003 WETH | 0.000021 WETH (0.0398 €) | — | 0.79 | 0.077 (n=37) | REJECTED | below_safety_margin(20752435210641<52752498179559), p_lower_below_threshold(0.08<0.75) |
| 55662693 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.007845 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0397 €) | — | 0.74 | 0.077 (n=37) | REJECTED | below_safety_margin(58<156), p_lower_below_threshold(0.08<0.75) |
| 55654854 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WBTC→[uniswap_v3]→cbBTC | 0.003711 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0394 €) | — | 1.56 | 0.230 (n=1426) | REJECTED | below_safety_margin(58<74), p_lower_below_threshold(0.23<0.75) |
| 55647094 | cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.003909 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0394 €) | — | 1.48 | 0.227 (n=1406) | REJECTED | below_safety_margin(58<78), p_lower_below_threshold(0.23<0.75) |
| 55647094 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.150305 WETH | 0.000024 WETH | 0.000000 WETH | 0.000003 WETH | 0.000021 WETH (0.0393 €) | — | 1.37 | 0.227 (n=1406) | REJECTED | below_safety_margin(20664748044216<30061088872016), p_lower_below_threshold(0.23<0.75) |
| 55647094 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 297.718576 USDC | 0.048873 USDC | 0.000000 USDC | 0.006281 USDC | 0.042592 USDC (0.0392 €) | — | 1.43 | 0.227 (n=1406) | REJECTED | below_safety_margin(42592<59543), p_lower_below_threshold(0.23<0.75) |
| 55654854 | USDC→[uniswap_v3]→WBTC→[uniswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 310.056130 USDC | 0.049631 USDC | 0.000000 USDC | 0.007342 USDC | 0.042289 USDC (0.0389 €) | — | 1.36 | 0.230 (n=1426) | REJECTED | below_safety_margin(42289<62011), p_lower_below_threshold(0.23<0.75) |
| 55645931 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.006254 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0387 €) | — | 0.91 | 0.059 (n=36) | REJECTED | below_safety_margin(57<125), p_lower_below_threshold(0.06<0.75) |
| 55645931 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.223435 WETH | 0.000023 WETH | 0.000000 WETH | 0.000003 WETH | 0.000020 WETH (0.0384 €) | — | 0.90 | 0.059 (n=36) | REJECTED | below_safety_margin(20184448102296<44686993205901), p_lower_below_threshold(0.06<0.75) |
| 55645931 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 462.507606 USDC | 0.047993 USDC | 0.000000 USDC | 0.006274 USDC | 0.041719 USDC (0.0384 €) | — | 0.90 | 0.059 (n=36) | REJECTED | below_safety_margin(41719<92501), p_lower_below_threshold(0.06<0.75) |
| 55660693 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC | 99.668852 USDC | 0.047703 USDC | 0.000000 USDC | 0.006657 USDC | 0.041046 USDC (0.0378 €) | — | 4.12 | 0.184 (n=1110) | REJECTED | p_lower_below_threshold(0.18<0.75) |
| 55660693 | cbBTC→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.001207 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0375 €) | — | 4.56 | 0.184 (n=1110) | REJECTED | p_lower_below_threshold(0.18<0.75) |
| 55658963 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.006197 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0361 €) | — | 0.86 | 0.077 (n=37) | REJECTED | below_safety_margin(53<123), p_lower_below_threshold(0.08<0.75) |
| 55658964 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.006197 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0361 €) | — | 0.86 | 0.077 (n=37) | REJECTED | below_safety_margin(53<123), p_lower_below_threshold(0.08<0.75) |
| 55658963 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.258626 WETH | 0.000022 WETH | 0.000000 WETH | 0.000003 WETH | 0.000019 WETH (0.0357 €) | — | 0.72 | 0.077 (n=37) | REJECTED | below_safety_margin(18702234726837<51725228019350), p_lower_below_threshold(0.08<0.75) |
| 55658964 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.258626 WETH | 0.000022 WETH | 0.000000 WETH | 0.000003 WETH | 0.000019 WETH (0.0357 €) | — | 0.72 | 0.077 (n=37) | REJECTED | below_safety_margin(18700189286237<51725228019350), p_lower_below_threshold(0.08<0.75) |

## Fiabilité et décision
- Observations ghost : 7584 ; taux observé 0.197 ; borne inférieure crédible (0.9) 0.191 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 19.1% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ✅ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
