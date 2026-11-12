# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-12T20:00:51+00:00 ; durée 205.71 min ; blocs 56554640 → 56616313 (11093 vus)

## Connexion
- Requêtes RPC : 133853 ; erreurs : 168 ; latence p50/p95 : 238.3/1,734.1 ms
- Rafraîchissements d'état : 11093 ; âge des données au dernier bloc : 5.61 s ; changements de frais LP observés (pools à frais dynamiques) : 6457
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 6177 ; cycles déclenchés par événement : 1945 ; avance médiane sur le rafraîchissement multicall : 621 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,011.70 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 454 pools, 266 jetons, 14202 routes
- Par DEX : uniswap_v3 133, aerodrome_slipstream 96, aerodrome 187, pancakeswap_v3 25, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 1
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 160 (rejetés 2) → 565 jetons ; pools candidats 3627 (énumérés 281, par paires 0), mesurés 456, sous le plancher de 10000.0 $ : 2 → gardés 454 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'DAI': 1.0, 'USDC': 1.0, 'WETH': 2012.424484, 'cbBTC': 71768.389273, 'AERO': 0.523178}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 132,562,615 | 2,011.701044 | 56616313 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,302,922 | 0.028140 | 56616313 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 8,527,194 | 0.000014 | 56616313 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 8,521,440 | 0.028069 | 56616313 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 6,853,249 | 2,015.944430 | 56616313 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 6,679,475 | 105.684548 | 56616313 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,192,984 | 0.028150 | 56616313 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 4,167,905 | 1.902462 | 56616313 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,081,552 | 2,015.804710 | 56616313 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,765,382 | 0.998728 | 56616313 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 2,984,361 | 42,523.469462 | 56616313 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 107 | 2,810,351 | 2,015.815291 | 56616313 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2530 | 2,152,652 | 0.028093 | 56616313 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 1,878,110 | 1,163,003.281972 | 56616313 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | XDP/USDC | 100 | 1,647,524 | 0.016785 | 56616313 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | USDC/cbBTC | 400 | 1,601,296 | 0.000014 | 56616313 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,568,910 | 0.000014 | 56616313 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,503,439 | 0.000000 | 56616313 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,471,796 | 0.000014 | 56616313 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,470,917 | 0.006498 | 56616313 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,464,198 | 0.831231 | 56616313 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,379,510 | 427.587739 | 56616313 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v2 | WETH/USDC | 3000 | 1,257,809 | 2,011.811067 | 56616313 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| uniswap_v3 | WETH/AERO | 3000 | 1,228,371 | 3,837.837231 | 56616313 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,186,327 | 15,206.057854 | 56616313 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/USDC | 3000 | 1,143,113 | 2,014.913619 | 56616313 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,098,344 | 2,016.560068 | 56616313 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,060,906 | 86.334668 | 56616313 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,047,056 | 1.389303 | 56616313 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | WETH/doginme | 10000 | 1,012,282 | 34,549,076.362434 | 56616313 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/VVV | 10000 | 986,950 | 106.187487 | 56616313 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome_slipstream | USDC/VELVET | 100 | 978,376 | 20.200213 | 56616313 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/BRETT | 10000 | 920,654 | 560,074.360983 | 56616313 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 889,768 | 0.001492 | 56616313 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| uniswap_v3 | WETH/TOSHI | 10000 | 881,812 | 23,226,178.240886 | 56616313 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | USDC/VVV | 3000 | 876,184 | 0.052517 | 56616313 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/MORPHO | 3000 | 869,467 | 1,004.409589 | 56616313 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/USDC | 10000 | 868,952 | 2,005.358242 | 56616313 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome_slipstream | USDC/cbBTC | 330 | 867,617 | 0.000014 | 56616313 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | DRB/WETH | 10000 | 812,248 | 0.000000 | 56616313 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | USDC/NOCK | 3000 | 770,380 | 79.254131 | 56616313 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| pancakeswap_v3 | QUID/USDC | 100 | 744,932 | 0.049433 | 56616313 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome_slipstream | USDC/SAPIEN | 4505 | 739,469 | 23.369127 | 56616313 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome | WETH/AERO | 10000 | 688,287 | 3,863.882062 | 56616313 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | WETH/wstETH | 3000 | 681,567 | 0.801801 | 56616313 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| aerodrome | WETH/EDEL | 7000 | 675,799 | 135,067.252305 | 56616313 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 662,474 | 0.527169 | 56616313 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 630,587 | 4,826,077.693844 | 56616313 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 599,250 | 0.452559 | 56616313 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/NPC | 3000 | 579,979 | 152,534.204355 | 56616313 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome | VIRTUAL/WETH | 10000 | 566,641 | 0.000260 | 56616313 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/BRETT | 2096 | 565,219 | 559,033.713705 | 56616313 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome_slipstream | AERO/cbBTC | 1025 | 558,290 | 0.000007 | 56616313 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v3 | FLOCK/USDC | 3000 | 554,826 | 0.037397 | 56616313 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 484,415 | 1,004.133428 | 56616313 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| pancakeswap_v3 | ELSA/USDC | 100 | 457,875 | 0.065659 | 56616313 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| aerodrome_slipstream | USDC/USDT | 11 | 449,571 | 1.000903 | 56616313 | `0xa41Bc0AFfbA7Fd420d186b84899d7ab2aC57fcD1` |
| uniswap_v3 | USDC/MORPHO | 10000 | 447,971 | 0.502250 | 56616313 | `0x2043B296fFC6b2d3bf4A3F3167d2Afb3B0FBdbEE` |
| uniswap_v3 | WETH/UNI | 10000 | 434,893 | 333.133889 | 56616313 | `0xAb365f161Dd501473a1ff0D2ef0dCE94E7398839` |
| uniswap_v3 | WETH/uSOL | 3000 | 428,866 | 24.860791 | 56616313 | `0xab04A352D4EC8d0F1812A4E5EBe7807Fa67acD48` |

## Recherche d'opportunités
- Cycles : 13037 ; routes examinées : 185151474 ; candidats optimisés : 872994 ; net attendu > 0 : 830 ; dernier cycle 435.6 ms
- Rejets (moteur) : {'spread_below_threshold': 181400547, 'liquidity_below_min': 2872097, 'negative_expected_net': 872164, 'cycle_budget_exhausted': 3992, 'borrow_bound_too_small': 1844}
- Enregistrements de la session : 872994 ; net attendu > 0 : 830 ; simulés (eth_call de la vraie tx) : 51 (ok 46, échec 5) ; étiquettes ghost N+1 : 19/46 positives
- Décisions : {'REJECTED': 872994} ; motifs de rejet : {'below_safety_margin': 667, 'negative_expected_net': 872164, 'p_lower_below_threshold': 798, 'reliability_not_demonstrated': 32, 'sim_below_estimate': 1, 'simulated_net_nonpositive': 1, 'simulation_failed': 5, 'stale_data': 154}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 56564036 | WETH→[aerodrome]→NPC→[uniswap_v2]→WETH | 0.011966 WETH | 0.000080 WETH | 0.000000 WETH | 0.000002 WETH | 0.000079 WETH (0.1449 €) | 0.000079 WETH | 65.72 | 0.006 (n=1) | REJECTED | reliability_not_demonstrated |
| 56598010 | WETH→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH | 0.934169 WETH | 0.000028 WETH | 0.000000 WETH | 0.000002 WETH | 0.000026 WETH (0.0475 €) | — | 0.27 | 0.104 (n=371) | REJECTED | below_safety_margin(25652669957624<186833754396777), p_lower_below_threshold(0.10<0.75) |
| 56598011 | WETH→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH | 0.934169 WETH | 0.000028 WETH | 0.000000 WETH | 0.000002 WETH | 0.000026 WETH (0.0475 €) | — | 0.27 | 0.104 (n=371) | REJECTED | below_safety_margin(25652669957624<186833754396777), stale_data(4336ms>4000.0), p_lower_below_threshold(0.10<0.75) |
| 56598010 | cbBTC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.023133 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0475 €) | — | 0.31 | 0.104 (n=371) | REJECTED | below_safety_margin(72<462), p_lower_below_threshold(0.10<0.75) |
| 56598011 | cbBTC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.023133 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0475 €) | — | 0.31 | 0.104 (n=371) | REJECTED | below_safety_margin(72<462), stale_data(4342ms>4000.0), p_lower_below_threshold(0.10<0.75) |
| 56598985 | USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WBTC→[uniswap_v3]→USDC | 307.406334 USDC | 0.056015 USDC | 0.000000 USDC | 0.006064 USDC | 0.049951 USDC (0.0460 €) | — | 1.62 | 0.269 (n=1619) | REJECTED | below_safety_margin(49951<61481), stale_data(4133ms>4000.0), p_lower_below_threshold(0.27<0.75) |
| 56598985 | cbBTC→[uniswap_v3]→WBTC→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.003777 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0455 €) | — | 1.83 | 0.269 (n=1619) | REJECTED | below_safety_margin(69<75), stale_data(4139ms>4000.0), p_lower_below_threshold(0.27<0.75) |
| 56598986 | cbBTC→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.006612 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0369 €) | — | 0.85 | 0.104 (n=371) | REJECTED | below_safety_margin(56<132), p_lower_below_threshold(0.10<0.75) |
| 56598986 | USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→USDC | 464.648392 USDC | 0.044332 USDC | 0.000000 USDC | 0.004531 USDC | 0.039801 USDC (0.0366 €) | — | 0.86 | 0.104 (n=371) | REJECTED | below_safety_margin(39801<92929), p_lower_below_threshold(0.10<0.75) |
| 56572083 | cbBTC→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC | 0.003555 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0290 €) | — | 1.24 | 0.269 (n=1619) | REJECTED | below_safety_margin(44<71), p_lower_below_threshold(0.27<0.75) |
| 56572084 | cbBTC→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC | 0.003555 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0290 €) | — | 1.24 | 0.269 (n=1619) | REJECTED | below_safety_margin(44<71), p_lower_below_threshold(0.27<0.75) |
| 56572083 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 286.012905 USDC | 0.037587 USDC | 0.000000 USDC | 0.006085 USDC | 0.031502 USDC (0.0290 €) | — | 1.10 | 0.269 (n=1619) | REJECTED | below_safety_margin(31502<57202), p_lower_below_threshold(0.27<0.75) |
| 56572084 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 286.012905 USDC | 0.037587 USDC | 0.000000 USDC | 0.006093 USDC | 0.031494 USDC (0.0290 €) | — | 1.10 | 0.269 (n=1619) | REJECTED | below_safety_margin(31494<57202), p_lower_below_threshold(0.27<0.75) |
| 56572083 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→WETH | 0.142147 WETH | 0.000019 WETH | 0.000000 WETH | 0.000003 WETH | 0.000016 WETH (0.0289 €) | — | 1.10 | 0.269 (n=1619) | REJECTED | below_safety_margin(15671788024706<28429305439186), p_lower_below_threshold(0.27<0.75) |
| 56572084 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→WETH | 0.142147 WETH | 0.000019 WETH | 0.000000 WETH | 0.000003 WETH | 0.000016 WETH (0.0289 €) | — | 1.10 | 0.269 (n=1619) | REJECTED | below_safety_margin(15667763521501<28429305439186), p_lower_below_threshold(0.27<0.75) |
| 56572083 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 263.216814 USDC | 0.030932 USDC | 0.000000 USDC | 0.006085 USDC | 0.024847 USDC (0.0229 €) | — | 0.94 | 0.269 (n=1619) | REJECTED | below_safety_margin(24847<52643), p_lower_below_threshold(0.27<0.75) |
| 56572084 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 263.216814 USDC | 0.030932 USDC | 0.000000 USDC | 0.006093 USDC | 0.024839 USDC (0.0229 €) | — | 0.94 | 0.269 (n=1619) | REJECTED | below_safety_margin(24839<52643), p_lower_below_threshold(0.27<0.75) |
| 56577361 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 255.397168 USDC | 0.029406 USDC | 0.000000 USDC | 0.004579 USDC | 0.024827 USDC (0.0228 €) | — | 0.97 | 0.104 (n=371) | REJECTED | below_safety_margin(24827<51079), p_lower_below_threshold(0.10<0.75) |
| 56577361 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.127197 WETH | 0.000015 WETH | 0.000000 WETH | 0.000002 WETH | 0.000012 WETH (0.0228 €) | — | 0.97 | 0.104 (n=371) | REJECTED | below_safety_margin(12313661343728<25439386269510), p_lower_below_threshold(0.10<0.75) |
| 56572083 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.135721 WETH | 0.000015 WETH | 0.000000 WETH | 0.000003 WETH | 0.000012 WETH (0.0227 €) | — | 0.90 | 0.269 (n=1619) | REJECTED | below_safety_margin(12266523743846<27144165951627), p_lower_below_threshold(0.27<0.75) |
| 56572084 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.135721 WETH | 0.000015 WETH | 0.000000 WETH | 0.000003 WETH | 0.000012 WETH (0.0227 €) | — | 0.90 | 0.269 (n=1619) | REJECTED | below_safety_margin(12262499240641<27144165951627), p_lower_below_threshold(0.27<0.75) |
| 56572083 | cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.003312 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0224 €) | — | 1.03 | 0.269 (n=1619) | REJECTED | below_safety_margin(34<66), p_lower_below_threshold(0.27<0.75) |
| 56572084 | cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.003312 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0224 €) | — | 1.03 | 0.269 (n=1619) | REJECTED | below_safety_margin(34<66), p_lower_below_threshold(0.27<0.75) |
| 56591784 | USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 257.968799 USDC | 0.025649 USDC | 0.000000 USDC | 0.004553 USDC | 0.021096 USDC (0.0194 €) | — | 0.82 | 0.104 (n=371) | REJECTED | below_safety_margin(21096<51593), p_lower_below_threshold(0.10<0.75) |
| 56591784 | USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 257.968799 USDC | 0.025649 USDC | 0.000000 USDC | 0.004553 USDC | 0.021096 USDC (0.0194 €) | — | 0.82 | 0.104 (n=371) | REJECTED | below_safety_margin(21096<51593), stale_data(4299ms>4000.0), p_lower_below_threshold(0.10<0.75) |

## Fiabilité et décision
- Observations ghost : 8461 ; taux observé 0.223 ; borne inférieure crédible (0.9) 0.217 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 21.7% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ✅ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
