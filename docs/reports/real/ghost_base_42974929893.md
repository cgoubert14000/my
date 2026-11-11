# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-11T07:35:26+00:00 ; durée 42.85 min ; blocs 55947872 → 55960707 (1951 vus)

## Connexion
- Requêtes RPC : 25995 ; erreurs : 0 ; latence p50/p95 : 179.4/1,796.3 ms
- Rafraîchissements d'état : 1951 ; âge des données au dernier bloc : 7.43 s ; changements de frais LP observés (pools à frais dynamiques) : 1100
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 1692 ; cycles déclenchés par événement : 616 ; avance médiane sur le rafraîchissement multicall : 251 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,059.66 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 460 pools, 267 jetons, 16590 routes
- Par DEX : uniswap_v3 134, aerodrome_slipstream 98, aerodrome 187, pancakeswap_v3 27, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 161 (rejetés 2) → 566 jetons ; pools candidats 3638 (énumérés 282, par paires 0), mesurés 462, sous le plancher de 10000.0 $ : 2 → gardés 460 (max 1500) ; prix des hubs : {'USDC': 1.0, 'USDbC': 1.0, 'DAI': 1.0, 'WETH': 2057.512263, 'cbBTC': 73519.133148, 'AERO': 0.539928}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 134,208,815 | 2,059.664291 | 55960737 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,416,822 | 0.027924 | 55960737 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 8,595,521 | 0.027977 | 55960737 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 8,340,715 | 0.000014 | 55960737 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 7,081,208 | 2,060.735400 | 55960737 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 6,764,952 | 108.002140 | 55960737 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,361,287 | 0.027913 | 55960737 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 4,263,420 | 1.846721 | 55960737 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,875,679 | 1.000003 | 55960737 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| pancakeswap_v3 | WETH/USDC | 100 | 3,788,756 | 2,059.923498 | 55960737 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | WETH/KTA | 3000 | 3,062,109 | 42,341.239494 | 55960737 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 150 | 2,926,885 | 2,060.123323 | 55960737 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,214,844 | 0.027976 | 55960737 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 1,958,310 | 1,121,311.176185 | 55960737 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,683,074 | 0.000014 | 55960737 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | USDC/cbBTC | 400 | 1,620,011 | 0.000014 | 55960737 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | XDP/USDC | 100 | 1,607,650 | 0.016173 | 55960737 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,554,505 | 0.000000 | 55960737 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,517,772 | 0.006572 | 55960737 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,462,240 | 0.824485 | 55960737 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,458,001 | 1.373191 | 55960737 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,440,979 | 0.000014 | 55960737 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,421,693 | 417.989901 | 55960737 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v2 | WETH/USDC | 3000 | 1,272,527 | 2,059.505447 | 55960737 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| uniswap_v3 | WETH/AERO | 3000 | 1,263,716 | 3,807.830192 | 55960737 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,231,819 | 14,959.977045 | 55960737 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/USDC | 3000 | 1,158,496 | 2,060.661242 | 55960737 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome | USDC/SEND | 3000 | 1,060,990 | 86.321079 | 55960737 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,048,665 | 33,199,659.082426 | 55960737 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,015,397 | 2,060.529326 | 55960737 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome_slipstream | USDC/VELVET | 100 | 960,354 | 21.364791 | 55960737 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/BRETT | 10000 | 943,818 | 557,999.178955 | 55960737 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | WETH/VVV | 10000 | 938,743 | 107.688152 | 55960737 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome_slipstream | USDC/cbBTC | 332 | 912,338 | 0.000014 | 55960737 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 911,110 | 0.001470 | 55960737 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| uniswap_v3 | WETH/TOSHI | 10000 | 903,982 | 23,147,877.094335 | 55960737 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | WETH/MORPHO | 3000 | 880,429 | 1,026.548782 | 55960737 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/USDC | 10000 | 879,442 | 2,050.503253 | 55960737 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | DRB/WETH | 10000 | 879,252 | 0.000000 | 55960737 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | USDC/VVV | 3000 | 870,279 | 0.052370 | 55960737 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| pancakeswap_v3 | QUID/USDC | 100 | 765,467 | 0.052288 | 55960737 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | USDC/NOCK | 3000 | 761,774 | 81.054974 | 55960737 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 755,723 | 22.665932 | 55960737 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome | WETH/EDEL | 7000 | 747,290 | 115,813.602681 | 55960737 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | WETH/AERO | 10000 | 707,888 | 3,790.378227 | 55960737 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | WETH/wstETH | 3000 | 697,323 | 0.802938 | 55960737 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 673,287 | 0.529133 | 55960737 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 664,882 | 4,544,844.608281 | 55960737 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 626,917 | 0.494749 | 55960737 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/NPC | 3000 | 593,816 | 152,374.438906 | 55960737 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 585,105 | 0.000007 | 55960737 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | VIRTUAL/WETH | 10000 | 581,496 | 0.000259 | 55960737 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/BRETT | 2096 | 579,644 | 561,620.164114 | 55960737 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | FLOCK/USDC | 3000 | 557,826 | 0.037512 | 55960737 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 492,219 | 1,025.988838 | 55960737 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| uniswap_v3 | USDC/MORPHO | 10000 | 461,533 | 0.496647 | 55960737 | `0x2043B296fFC6b2d3bf4A3F3167d2Afb3B0FBdbEE` |
| pancakeswap_v3 | ELSA/USDC | 100 | 458,715 | 0.065794 | 55960737 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| aerodrome_slipstream | USDC/USDT | 8 | 455,067 | 1.000992 | 55960737 | `0xa41Bc0AFfbA7Fd420d186b84899d7ab2aC57fcD1` |
| aerodrome | cbBTC/EDGE | 7000 | 448,014 | 870,182.366484 | 55960737 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| uniswap_v3 | WETH/uSOL | 3000 | 439,643 | 25.056759 | 55960737 | `0xab04A352D4EC8d0F1812A4E5EBe7807Fa67acD48` |

## Recherche d'opportunités
- Cycles : 2566 ; routes examinées : 42569940 ; candidats optimisés : 222517 ; net attendu > 0 : 165 ; dernier cycle 417.8 ms
- Rejets (moteur) : {'spread_below_threshold': 41463381, 'liquidity_below_min': 878820, 'negative_expected_net': 222352, 'borrow_bound_too_small': 4621, 'cycle_budget_exhausted': 601}
- Enregistrements de la session : 222517 ; net attendu > 0 : 165 ; simulés (eth_call de la vraie tx) : 2 (ok 1, échec 1) ; étiquettes ghost N+1 : 1/2 positives
- Décisions : {'REJECTED': 222517} ; motifs de rejet : {'below_safety_margin': 163, 'negative_expected_net': 222352, 'p_lower_below_threshold': 147, 'reliability_not_demonstrated': 18, 'simulation_failed': 1, 'stale_data': 16}

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
- Observations ghost : 7990 ; taux observé 0.211 ; borne inférieure crédible (0.9) 0.205 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 20.5% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
