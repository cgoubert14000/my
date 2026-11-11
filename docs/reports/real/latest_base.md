# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-11T07:57:15+00:00 ; durée 64.66 min ; blocs 55947872 → 55967210 (3054 vus)

## Connexion
- Requêtes RPC : 39801 ; erreurs : 0 ; latence p50/p95 : 278.1/1,607.9 ms
- Rafraîchissements d'état : 3054 ; âge des données au dernier bloc : 14.87 s ; changements de frais LP observés (pools à frais dynamiques) : 1449
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 2597 ; cycles déclenchés par événement : 944 ; avance médiane sur le rafraîchissement multicall : 251 ms
- Gaz : base fee 0.005053 gwei ; prix ETH (pool le plus profond) : 2,061.10 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 460 pools, 267 jetons, 16590 routes
- Par DEX : uniswap_v3 134, aerodrome_slipstream 98, aerodrome 187, pancakeswap_v3 27, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 161 (rejetés 2) → 566 jetons ; pools candidats 3638 (énumérés 282, par paires 0), mesurés 462, sous le plancher de 10000.0 $ : 2 → gardés 460 (max 1500) ; prix des hubs : {'USDC': 1.0, 'USDbC': 1.0, 'DAI': 1.0, 'WETH': 2057.512263, 'cbBTC': 73519.133148, 'AERO': 0.539928}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 134,276,685 | 2,061.815218 | 55967240 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,426,443 | 0.027927 | 55967240 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 8,604,056 | 0.027977 | 55967240 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 8,343,974 | 0.000014 | 55967240 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 7,085,282 | 2,066.819547 | 55967240 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 6,757,150 | 108.402230 | 55967240 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,364,251 | 0.027930 | 55967240 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 4,269,787 | 1.841218 | 55967240 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,088,194 | 2,067.414204 | 55967240 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,877,958 | 1.000003 | 55967240 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,063,281 | 42,367.677117 | 55967240 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 150 | 2,928,588 | 2,067.532778 | 55967240 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,216,348 | 0.027976 | 55967240 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 1,959,671 | 1,121,311.176185 | 55967240 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,683,864 | 0.000014 | 55967240 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | USDC/cbBTC | 600 | 1,620,724 | 0.000014 | 55967240 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | XDP/USDC | 100 | 1,609,655 | 0.016203 | 55967240 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,555,585 | 0.000000 | 55967240 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,514,445 | 0.006549 | 55967240 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,462,240 | 0.824485 | 55967240 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,458,001 | 1.373191 | 55967240 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,441,483 | 0.000014 | 55967240 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,421,994 | 418.710982 | 55967240 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v2 | WETH/USDC | 3000 | 1,272,970 | 2,061.633382 | 55967240 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| uniswap_v3 | WETH/AERO | 3000 | 1,266,448 | 3,805.108111 | 55967240 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,231,682 | 14,971.521927 | 55967240 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/USDC | 3000 | 1,158,898 | 2,062.965600 | 55967240 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome | USDC/SEND | 3000 | 1,060,990 | 86.321079 | 55967240 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,046,899 | 33,221,424.263322 | 55967240 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,015,928 | 2,066.743069 | 55967240 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome_slipstream | USDC/VELVET | 100 | 960,036 | 21.386504 | 55967240 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/BRETT | 10000 | 944,473 | 558,001.026164 | 55967240 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | WETH/VVV | 10000 | 936,994 | 107.689035 | 55967240 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome_slipstream | USDC/cbBTC | 364 | 912,857 | 0.000014 | 55967240 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 912,087 | 0.001471 | 55967240 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| uniswap_v3 | WETH/TOSHI | 10000 | 904,610 | 23,147,877.094335 | 55967240 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | WETH/MORPHO | 3000 | 881,041 | 1,026.548782 | 55967240 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | DRB/WETH | 10000 | 879,863 | 0.000000 | 55967240 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/USDC | 10000 | 879,709 | 2,050.503253 | 55967240 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | USDC/VVV | 3000 | 868,062 | 0.052465 | 55967240 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| pancakeswap_v3 | QUID/USDC | 100 | 780,252 | 0.054411 | 55967240 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | USDC/NOCK | 3000 | 766,999 | 79.954543 | 55967240 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 755,723 | 22.665932 | 55967240 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome | WETH/EDEL | 7000 | 748,983 | 115,451.047321 | 55967240 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | WETH/AERO | 10000 | 709,190 | 3,790.378227 | 55967240 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | WETH/wstETH | 3000 | 697,807 | 0.802938 | 55967240 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 673,359 | 0.529027 | 55967240 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 662,394 | 4,585,479.099506 | 55967240 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 626,951 | 0.494797 | 55967240 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/NPC | 3000 | 594,226 | 152,375.842124 | 55967240 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 586,410 | 0.000007 | 55967240 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | VIRTUAL/WETH | 10000 | 581,734 | 0.000259 | 55967240 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 580,045 | 561,507.721304 | 55967240 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | FLOCK/USDC | 3000 | 558,584 | 0.037590 | 55967240 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 492,561 | 1,025.988839 | 55967240 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| uniswap_v3 | USDC/MORPHO | 10000 | 461,763 | 0.496647 | 55967240 | `0x2043B296fFC6b2d3bf4A3F3167d2Afb3B0FBdbEE` |
| pancakeswap_v3 | ELSA/USDC | 100 | 458,105 | 0.065736 | 55967240 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| aerodrome_slipstream | USDC/USDT | 8 | 455,002 | 1.000986 | 55967240 | `0xa41Bc0AFfbA7Fd420d186b84899d7ab2aC57fcD1` |
| aerodrome | cbBTC/EDGE | 7000 | 453,573 | 850,435.536677 | 55967240 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| uniswap_v3 | WETH/uSOL | 3000 | 439,973 | 25.056759 | 55967240 | `0xab04A352D4EC8d0F1812A4E5EBe7807Fa67acD48` |

## Recherche d'opportunités
- Cycles : 3996 ; routes examinées : 66293640 ; candidats optimisés : 329092 ; net attendu > 0 : 247 ; dernier cycle 579.9 ms
- Rejets (moteur) : {'spread_below_threshold': 64516445, 'liquidity_below_min': 1439745, 'negative_expected_net': 328845, 'borrow_bound_too_small': 7476, 'cycle_budget_exhausted': 882}
- Enregistrements de la session : 329092 ; net attendu > 0 : 247 ; simulés (eth_call de la vraie tx) : 8 (ok 4, échec 4) ; étiquettes ghost N+1 : 4/8 positives
- Décisions : {'REJECTED': 329092} ; motifs de rejet : {'below_safety_margin': 231, 'negative_expected_net': 328845, 'p_lower_below_threshold': 227, 'reliability_not_demonstrated': 20, 'simulation_failed': 4, 'stale_data': 18}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 55951267 | USDC→[pancakeswap_v3]→ICNT→[uniswap_v3]→USDC | 145.747655 USDC | 0.253186 USDC | 0.000000 USDC | 0.004616 USDC | 0.248570 USDC (0.2287 €) | — | 17.05 | 0.007 (n=113) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.01<0.75) |
| 55958191 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 397.168686 USDC | 0.066484 USDC | 0.000000 USDC | 0.004937 USDC | 0.061547 USDC (0.0566 €) | — | 1.55 | 0.100 (n=357) | REJECTED | below_safety_margin(61547<79433), p_lower_below_threshold(0.10<0.75) |
| 55958191 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 397.168686 USDC | 0.066484 USDC | 0.000000 USDC | 0.004937 USDC | 0.061547 USDC (0.0566 €) | — | 1.55 | 0.100 (n=357) | REJECTED | below_safety_margin(61547<79433), p_lower_below_threshold(0.10<0.75) |
| 55958191 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.193167 WETH | 0.000032 WETH | 0.000000 WETH | 0.000002 WETH | 0.000030 WETH (0.0566 €) | — | 1.55 | 0.100 (n=357) | REJECTED | below_safety_margin(29863080145926<38633455242635), p_lower_below_threshold(0.10<0.75) |
| 55958191 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.193167 WETH | 0.000032 WETH | 0.000000 WETH | 0.000002 WETH | 0.000030 WETH (0.0566 €) | — | 1.55 | 0.100 (n=357) | REJECTED | below_safety_margin(29863080145926<38633455242635), p_lower_below_threshold(0.10<0.75) |
| 55958191 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 333.104978 USDC | 0.060400 USDC | 0.000000 USDC | 0.004625 USDC | 0.055775 USDC (0.0513 €) | — | 1.67 | 0.100 (n=357) | REJECTED | below_safety_margin(55775<66620), p_lower_below_threshold(0.10<0.75) |
| 55958191 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 333.104978 USDC | 0.060400 USDC | 0.000000 USDC | 0.004625 USDC | 0.055775 USDC (0.0513 €) | — | 1.67 | 0.100 (n=357) | REJECTED | below_safety_margin(55775<66620), p_lower_below_threshold(0.10<0.75) |
| 55958191 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.161735 WETH | 0.000029 WETH | 0.000000 WETH | 0.000002 WETH | 0.000027 WETH (0.0513 €) | — | 1.67 | 0.100 (n=357) | REJECTED | below_safety_margin(27064313873970<32347007069318), p_lower_below_threshold(0.10<0.75) |
| 55958191 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.161735 WETH | 0.000029 WETH | 0.000000 WETH | 0.000002 WETH | 0.000027 WETH (0.0513 €) | — | 1.67 | 0.100 (n=357) | REJECTED | below_safety_margin(27064313873970<32347007069318), p_lower_below_threshold(0.10<0.75) |
| 55958191 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 325.719934 USDC | 0.053642 USDC | 0.000000 USDC | 0.006189 USDC | 0.047453 USDC (0.0437 €) | — | 1.46 | 0.261 (n=1552) | REJECTED | below_safety_margin(47453<65143), p_lower_below_threshold(0.26<0.75) |
| 55958191 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 325.719934 USDC | 0.053642 USDC | 0.000000 USDC | 0.006189 USDC | 0.047453 USDC (0.0437 €) | — | 1.46 | 0.261 (n=1552) | REJECTED | below_safety_margin(47453<65143), p_lower_below_threshold(0.26<0.75) |
| 55958191 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.157454 WETH | 0.000026 WETH | 0.000000 WETH | 0.000003 WETH | 0.000023 WETH (0.0436 €) | — | 1.46 | 0.261 (n=1552) | REJECTED | below_safety_margin(23027714929936<31490849162554), p_lower_below_threshold(0.26<0.75) |
| 55958191 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.157454 WETH | 0.000026 WETH | 0.000000 WETH | 0.000003 WETH | 0.000023 WETH (0.0436 €) | — | 1.46 | 0.261 (n=1552) | REJECTED | below_safety_margin(23027714929936<31490849162554), p_lower_below_threshold(0.26<0.75) |
| 55958191 | cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.003887 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0434 €) | — | 1.65 | 0.261 (n=1552) | REJECTED | below_safety_margin(64<77), p_lower_below_threshold(0.26<0.75) |
| 55958191 | cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.003887 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0434 €) | — | 1.65 | 0.261 (n=1552) | REJECTED | below_safety_margin(64<77), p_lower_below_threshold(0.26<0.75) |
| 55958191 | cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH→[uniswap_v3]→cbBTC | 0.003026 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0210 €) | — | 1.02 | 0.328 (n=569) | REJECTED | below_safety_margin(31<60), p_lower_below_threshold(0.33<0.75) |
| 55958191 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.003256 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0210 €) | — | 0.95 | 0.261 (n=1552) | REJECTED | below_safety_margin(31<65), p_lower_below_threshold(0.26<0.75) |
| 55958191 | cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH→[uniswap_v3]→cbBTC | 0.003026 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0210 €) | — | 1.02 | 0.328 (n=569) | REJECTED | below_safety_margin(31<60), p_lower_below_threshold(0.33<0.75) |
| 55958191 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.003256 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0210 €) | — | 0.95 | 0.261 (n=1552) | REJECTED | below_safety_margin(31<65), p_lower_below_threshold(0.26<0.75) |
| 55958191 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.120949 WETH | 0.000014 WETH | 0.000000 WETH | 0.000003 WETH | 0.000011 WETH (0.0209 €) | — | 0.91 | 0.261 (n=1552) | REJECTED | below_safety_margin(11023887007981<24189800046033), p_lower_below_threshold(0.26<0.75) |
| 55958191 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.120949 WETH | 0.000014 WETH | 0.000000 WETH | 0.000003 WETH | 0.000011 WETH (0.0209 €) | — | 0.91 | 0.261 (n=1552) | REJECTED | below_safety_margin(11023887007981<24189800046033), p_lower_below_threshold(0.26<0.75) |
| 55958191 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 247.801984 USDC | 0.028864 USDC | 0.000000 USDC | 0.006189 USDC | 0.022675 USDC (0.0209 €) | — | 0.92 | 0.261 (n=1552) | REJECTED | below_safety_margin(22675<49560), p_lower_below_threshold(0.26<0.75) |
| 55958191 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 247.801984 USDC | 0.028864 USDC | 0.000000 USDC | 0.006189 USDC | 0.022675 USDC (0.0209 €) | — | 0.92 | 0.261 (n=1552) | REJECTED | below_safety_margin(22675<49560), p_lower_below_threshold(0.26<0.75) |
| 55958191 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 253.210547 USDC | 0.028851 USDC | 0.000000 USDC | 0.006189 USDC | 0.022662 USDC (0.0208 €) | — | 0.89 | 0.328 (n=569) | REJECTED | below_safety_margin(22662<50642), p_lower_below_threshold(0.33<0.75) |
| 55958191 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 253.210547 USDC | 0.028851 USDC | 0.000000 USDC | 0.006189 USDC | 0.022662 USDC (0.0208 €) | — | 0.89 | 0.328 (n=569) | REJECTED | below_safety_margin(22662<50642), p_lower_below_threshold(0.33<0.75) |

## Fiabilité et décision
- Observations ghost : 7996 ; taux observé 0.211 ; borne inférieure crédible (0.9) 0.206 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 20.6% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
