# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-11T23:27:32+00:00 ; durée 320.5 min ; blocs 56150210 → 56246268 (14625 vus)

## Connexion
- Requêtes RPC : 191648 ; erreurs : 270 ; latence p50/p95 : 147.3/1,561.1 ms
- Rafraîchissements d'état : 14625 ; âge des données au dernier bloc : 8.29 s ; changements de frais LP observés (pools à frais dynamiques) : 11653
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 15662 ; cycles déclenchés par événement : 5408 ; avance médiane sur le rafraîchissement multicall : 641 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,042.24 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 462 pools, 267 jetons, 16678 routes
- Par DEX : uniswap_v3 134, aerodrome_slipstream 100, aerodrome 187, pancakeswap_v3 27, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 161 (rejetés 2) → 566 jetons ; pools candidats 3639 (énumérés 284, par paires 0), mesurés 464, sous le plancher de 10000.0 $ : 2 → gardés 462 (max 1500) ; prix des hubs : {'USDC': 1.0, 'DAI': 1.0, 'USDbC': 1.0, 'WETH': 2091.017157, 'cbBTC': 74374.029387, 'AERO': 0.55788}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 133,890,871 | 2,042.240028 | 56246293 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,363,026 | 0.027744 | 56246293 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 8,557,624 | 0.027789 | 56246293 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 8,508,241 | 0.000014 | 56246293 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 7,048,498 | 2,044.039786 | 56246293 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 6,801,640 | 105.040166 | 56246293 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,570,519 | 0.027746 | 56246293 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 4,217,712 | 1.870158 | 56246293 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,001,162 | 2,043.154035 | 56246293 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,878,555 | 0.998583 | 56246293 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,016,275 | 42,902.499047 | 56246293 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 146 | 2,880,111 | 2,043.050896 | 56246293 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,193,611 | 0.027775 | 56246293 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 1,940,261 | 1,123,024.323907 | 56246293 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 508 | 1,641,848 | 0.000014 | 56246293 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | XDP/USDC | 100 | 1,612,262 | 0.016238 | 56246293 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,604,119 | 0.000014 | 56246293 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,558,028 | 0.000000 | 56246293 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,528,527 | 0.000014 | 56246293 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,512,325 | 0.006605 | 56246293 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,461,473 | 0.830438 | 56246293 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,437,836 | 1.406597 | 56246293 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,397,904 | 430.537119 | 56246293 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v2 | WETH/USDC | 3000 | 1,267,228 | 2,042.024806 | 56246293 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| uniswap_v3 | WETH/AERO | 3000 | 1,247,073 | 3,814.375114 | 56246293 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,210,099 | 15,500.096054 | 56246293 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/USDC | 3000 | 1,153,585 | 2,042.955468 | 56246293 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,122,335 | 2,043.680205 | 56246293 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,060,556 | 86.391696 | 56246293 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,036,202 | 33,570,438.445626 | 56246293 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/VVV | 10000 | 1,009,186 | 104.315321 | 56246293 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome_slipstream | USDC/VELVET | 100 | 957,758 | 21.543831 | 56246293 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/BRETT | 10000 | 930,597 | 567,228.892490 | 56246293 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 909,899 | 0.001472 | 56246293 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 354 | 900,782 | 0.000014 | 56246293 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | WETH/TOSHI | 10000 | 894,946 | 23,195,871.080466 | 56246293 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | USDC/VVV | 3000 | 890,077 | 0.051527 | 56246293 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/USDC | 10000 | 876,445 | 2,054.858045 | 56246293 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 869,295 | 1,032.124716 | 56246293 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | DRB/WETH | 10000 | 851,856 | 0.000000 | 56246293 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | USDC/NOCK | 3000 | 777,417 | 77.826021 | 56246293 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| pancakeswap_v3 | QUID/USDC | 100 | 762,952 | 0.051930 | 56246293 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/EDEL | 7000 | 744,094 | 114,842.897497 | 56246293 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 743,196 | 23.200594 | 56246293 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome | WETH/AERO | 10000 | 699,904 | 3,786.866427 | 56246293 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | WETH/wstETH | 3000 | 691,913 | 0.801801 | 56246293 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 663,745 | 0.522742 | 56246293 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 646,831 | 4,726,297.490340 | 56246293 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 620,722 | 0.484715 | 56246293 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/NPC | 3000 | 596,925 | 148,331.451562 | 56246293 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | AERO/cbBTC | 1025 | 580,860 | 0.000007 | 56246293 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | VIRTUAL/WETH | 10000 | 572,624 | 0.000257 | 56246293 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/BRETT | 2114 | 569,892 | 570,645.776044 | 56246293 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | FLOCK/USDC | 3000 | 553,213 | 0.037028 | 56246293 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome_slipstream | WETH/MORPHO | 2739 | 485,127 | 1,032.331528 | 56246293 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| pancakeswap_v3 | ELSA/USDC | 100 | 461,619 | 0.066377 | 56246293 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| aerodrome_slipstream | USDC/USDT | 8 | 453,831 | 1.000956 | 56246293 | `0xa41Bc0AFfbA7Fd420d186b84899d7ab2aC57fcD1` |
| uniswap_v3 | USDC/MORPHO | 10000 | 449,855 | 0.502364 | 56246293 | `0x2043B296fFC6b2d3bf4A3F3167d2Afb3B0FBdbEE` |
| aerodrome | cbBTC/EDGE | 7000 | 439,809 | 901,686.368204 | 56246293 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| uniswap_v3 | WETH/uSOL | 3000 | 438,292 | 24.783986 | 56246293 | `0xab04A352D4EC8d0F1812A4E5EBe7807Fa67acD48` |

## Recherche d'opportunités
- Cycles : 20032 ; routes examinées : 334093696 ; candidats optimisés : 1669751 ; net attendu > 0 : 2081 ; dernier cycle 266.4 ms
- Rejets (moteur) : {'spread_below_threshold': 326656103, 'liquidity_below_min': 5719858, 'negative_expected_net': 1667670, 'borrow_bound_too_small': 38661, 'cycle_budget_exhausted': 9262, 'unquotable': 61}
- Enregistrements de la session : 1669751 ; net attendu > 0 : 2081 ; simulés (eth_call de la vraie tx) : 79 (ok 51, échec 28) ; étiquettes ghost N+1 : 18/69 positives
- Décisions : {'REJECTED': 1669751} ; motifs de rejet : {'below_safety_margin': 1802, 'negative_expected_net': 1667670, 'p_lower_below_threshold': 2040, 'price_impact': 6, 'reliability_not_demonstrated': 41, 'sim_below_estimate': 6, 'simulated_net_nonpositive': 2, 'simulation_failed': 28, 'stale_data': 467}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 56234265 | WETH→[pancakeswap_v3]→AAVE→[uniswap_v3]→WETH | 0.144994 WETH | 0.000244 WETH | 0.000000 WETH | 0.000002 WETH | 0.000241 WETH (0.4571 €) | — | 16.63 | 0.007 (n=114) | REJECTED | stale_data(5203ms>4000.0), simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.01<0.75) |
| 56234265 | WETH→[pancakeswap_v3]→AAVE→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.102478 WETH | 0.000199 WETH | 0.000000 WETH | 0.000003 WETH | 0.000196 WETH (0.3710 €) | — | 19.10 | 0.144 (n=237) | REJECTED | stale_data(5094ms>4000.0), simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.14<0.75) |
| 56234265 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→AAVE→[uniswap_v3]→USDC | 210.605820 USDC | 0.409443 USDC | 0.000000 USDC | 0.006845 USDC | 0.402598 USDC (0.3704 €) | — | 19.12 | 0.144 (n=237) | REJECTED | stale_data(5102ms>4000.0), p_lower_below_threshold(0.14<0.75) |
| 56234265 | WETH→[pancakeswap_v3]→AAVE→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.098810 WETH | 0.000188 WETH | 0.000000 WETH | 0.000003 WETH | 0.000185 WETH (0.3502 €) | — | 18.70 | 0.144 (n=237) | REJECTED | stale_data(5109ms>4000.0), simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.14<0.75) |
| 56234265 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→AAVE→[uniswap_v3]→USDC | 203.054716 USDC | 0.386967 USDC | 0.000000 USDC | 0.006845 USDC | 0.380122 USDC (0.3497 €) | — | 18.72 | 0.144 (n=237) | REJECTED | stale_data(5117ms>4000.0), p_lower_below_threshold(0.14<0.75) |
| 56234265 | WETH→[pancakeswap_v3]→AAVE→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.096276 WETH | 0.000182 WETH | 0.000000 WETH | 0.000003 WETH | 0.000178 WETH (0.3382 €) | — | 18.53 | 0.144 (n=237) | REJECTED | stale_data(5125ms>4000.0), p_lower_below_threshold(0.14<0.75) |
| 56234265 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→AAVE→[uniswap_v3]→USDC | 197.933923 USDC | 0.374016 USDC | 0.000000 USDC | 0.006845 USDC | 0.367171 USDC (0.3378 €) | — | 18.55 | 0.144 (n=237) | REJECTED | stale_data(5132ms>4000.0), p_lower_below_threshold(0.14<0.75) |
| 56234265 | WETH→[pancakeswap_v3]→AAVE→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.095388 WETH | 0.000174 WETH | 0.000000 WETH | 0.000003 WETH | 0.000171 WETH (0.3237 €) | — | 17.90 | 0.144 (n=237) | REJECTED | stale_data(5157ms>4000.0), p_lower_below_threshold(0.14<0.75) |
| 56234265 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→AAVE→[uniswap_v3]→USDC | 195.999591 USDC | 0.358302 USDC | 0.000000 USDC | 0.006845 USDC | 0.351457 USDC (0.3233 €) | — | 17.93 | 0.144 (n=237) | REJECTED | stale_data(5165ms>4000.0), p_lower_below_threshold(0.14<0.75) |
| 56234265 | WETH→[pancakeswap_v3]→AAVE→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.088769 WETH | 0.000149 WETH | 0.000000 WETH | 0.000003 WETH | 0.000146 WETH (0.2764 €) | — | 16.43 | 0.144 (n=237) | REJECTED | stale_data(5190ms>4000.0), p_lower_below_threshold(0.14<0.75) |
| 56234265 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→AAVE→[uniswap_v3]→USDC | 182.693531 USDC | 0.306984 USDC | 0.000000 USDC | 0.006845 USDC | 0.300139 USDC (0.2761 €) | — | 16.43 | 0.144 (n=237) | REJECTED | stale_data(5198ms>4000.0), p_lower_below_threshold(0.14<0.75) |
| 56245013 | WETH→[uniswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 1.420281 WETH | 0.000118 WETH | 0.000000 WETH | 0.000003 WETH | 0.000116 WETH (0.2172 €) | — | 0.81 | 0.104 (n=362) | REJECTED | below_safety_margin(115619679037555<284056186247201), p_lower_below_threshold(0.10<0.75) |
| 56245013 | cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→cbBTC | 0.036096 cbBTC | 0.000003 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000003 cbBTC (0.2166 €) | — | 0.89 | 0.104 (n=362) | REJECTED | below_safety_margin(320<721), p_lower_below_threshold(0.10<0.75) |
| 56178863 | cbBTC→[aerodrome_slipstream]→AERO→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.002971 cbBTC | 0.000003 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1669 €) | — | 8.21 | 0.144 (n=236) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 56178863 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→AERO→[pancakeswap_v3]→WETH | 0.106755 WETH | 0.000090 WETH | 0.000000 WETH | 0.000003 WETH | 0.000087 WETH (0.1668 €) | 0.000081 WETH | 8.18 | 0.144 (n=236) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 56234265 | USDC→[sushiswap_v3]→WETH→[pancakeswap_v3]→AAVE→[uniswap_v3]→USDC | 103.752296 USDC | 0.182597 USDC | 0.000000 USDC | 0.006845 USDC | 0.175752 USDC (0.1617 €) | — | 16.94 | 0.144 (n=237) | REJECTED | stale_data(5182ms>4000.0), p_lower_below_threshold(0.14<0.75) |
| 56234265 | WETH→[pancakeswap_v3]→AAVE→[uniswap_v3]→USDC→[sushiswap_v3]→WETH | 0.050415 WETH | 0.000089 WETH | 0.000000 WETH | 0.000003 WETH | 0.000085 WETH (0.1616 €) | — | 16.91 | 0.144 (n=237) | REJECTED | stale_data(5174ms>4000.0), p_lower_below_threshold(0.14<0.75) |
| 56197526 | WETH→[aerodrome]→RISE→[uniswap_v2]→WETH | 0.028799 WETH | 0.000086 WETH | 0.000000 WETH | 0.000002 WETH | 0.000084 WETH (0.1611 €) | — | 29.26 | 0.006 (n=1) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 56197527 | WETH→[aerodrome]→RISE→[uniswap_v2]→WETH | 0.028799 WETH | 0.000086 WETH | 0.000000 WETH | 0.000002 WETH | 0.000084 WETH (0.1611 €) | — | 29.26 | 0.006 (n=1) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 56178863 | cbBTC→[aerodrome_slipstream]→AERO→[pancakeswap_v3]→WETH→[uniswap_v3]→cbBTC | 0.002669 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1313 €) | — | 7.19 | 0.202 (n=1227) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 56178863 | WETH→[uniswap_v3]→cbBTC→[aerodrome_slipstream]→AERO→[pancakeswap_v3]→WETH | 0.092146 WETH | 0.000071 WETH | 0.000000 WETH | 0.000003 WETH | 0.000068 WETH (0.1308 €) | 0.000063 WETH | 7.43 | 0.202 (n=1227) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 56178863 | cbBTC→[aerodrome_slipstream]→AERO→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.002515 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1272 €) | — | 7.39 | 0.202 (n=1227) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 56178863 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→AERO→[pancakeswap_v3]→WETH | 0.092157 WETH | 0.000069 WETH | 0.000000 WETH | 0.000003 WETH | 0.000066 WETH (0.1270 €) | 0.000061 WETH | 7.21 | 0.202 (n=1227) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 56234050 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.251484 WETH | 0.000054 WETH | 0.000000 WETH | 0.000002 WETH | 0.000052 WETH (0.0986 €) | — | 2.07 | 0.104 (n=360) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.10<0.75) |
| 56234050 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 515.793110 USDC | 0.111924 USDC | 0.000000 USDC | 0.004960 USDC | 0.106964 USDC (0.0984 €) | — | 2.07 | 0.104 (n=360) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.10<0.75) |

## Fiabilité et décision
- Observations ghost : 8233 ; taux observé 0.217 ; borne inférieure crédible (0.9) 0.211 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 21.1% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ✅ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
