# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-09T21:40:16+00:00 ; durée 27.53 min ; blocs 55341906 → 55350163 (1422 vus)

## Connexion
- Requêtes RPC : 19573 ; erreurs : 0 ; latence p50/p95 : 329.7/1,145.1 ms
- Rafraîchissements d'état : 1422 ; âge des données au dernier bloc : 7.67 s ; changements de frais LP observés (pools à frais dynamiques) : 757
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 644 ; cycles déclenchés par événement : 303 ; avance médiane sur le rafraîchissement multicall : 435 ms
- Gaz : base fee 0.005007 gwei ; prix ETH (pool le plus profond) : 2,127.82 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 468 pools, 272 jetons, 17716 routes
- Par DEX : uniswap_v3 134, aerodrome_slipstream 99, aerodrome 193, pancakeswap_v3 28, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 166 (rejetés 2) → 571 jetons ; pools candidats 3654 (énumérés 289, par paires 0), mesurés 471, sous le plancher de 10000.0 $ : 3 → gardés 468 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDbC': 1.0, 'USDC': 1.0, 'WETH': 2127.766856, 'cbBTC': 74794.411024, 'AERO': 0.572023}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 140,085,584 | 2,127.817782 | 55350188 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,657,088 | 0.028432 | 55350188 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,340,354 | 0.000013 | 55350188 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 8,788,444 | 0.028437 | 55350188 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 7,480,759 | 2,126.199877 | 55350188 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,369,235 | 97.348445 | 55350188 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,933,505 | 0.028417 | 55350188 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 4,583,024 | 1.745643 | 55350188 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,010,034 | 2,125.358903 | 55350188 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,892,871 | 1.000033 | 55350188 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,107,033 | 43,892.698508 | 55350188 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 150 | 3,028,251 | 2,125.039302 | 55350188 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,348,830 | 0.028441 | 55350188 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 2,031,806 | 1,111,732.813378 | 55350188 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,706,231 | 0.000013 | 55350188 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | USDC/cbBTC | 508 | 1,692,223 | 0.000013 | 55350188 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | XDP/USDC | 100 | 1,585,692 | 0.015822 | 55350188 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,562,560 | 0.000000 | 55350188 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,562,172 | 0.006556 | 55350188 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,493,529 | 0.000013 | 55350188 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,468,082 | 1.429325 | 55350188 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,465,427 | 424.849054 | 55350188 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,456,949 | 0.821811 | 55350188 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,321,852 | 3,721.575721 | 55350188 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v2 | WETH/USDC | 3000 | 1,293,226 | 2,130.628750 | 55350188 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,250,232 | 14,915.862630 | 55350188 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/USDC | 3000 | 1,221,432 | 2,131.819056 | 55350188 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome | USDC/SEND | 3000 | 1,107,263 | 79.257048 | 55350188 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,102,713 | 2,126.049889 | 55350188 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | WETH/doginme | 10000 | 1,050,331 | 36,312,398.434913 | 55350188 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/VVV | 10000 | 988,957 | 98.035330 | 55350188 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/BRETT | 10000 | 970,780 | 565,875.845450 | 55350188 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | USDC/VVV | 3000 | 970,354 | 0.045783 | 55350188 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome_slipstream | USDC/VELVET | 100 | 963,913 | 21.131344 | 55350188 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 937,130 | 0.001511 | 55350188 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| uniswap_v3 | WETH/TOSHI | 10000 | 936,812 | 23,213,728.096903 | 55350188 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/cbBTC | 348 | 928,665 | 0.000013 | 55350188 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/NOCK | 3000 | 919,209 | 74.161721 | 55350188 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/MORPHO | 3000 | 909,613 | 1,033.156372 | 55350188 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | DRB/WETH | 10000 | 896,274 | 0.000000 | 55350188 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/USDC | 10000 | 887,632 | 2,127.924155 | 55350188 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome | WETH/EDEL | 7000 | 816,915 | 103,432.507369 | 55350188 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 773,679 | 21.924424 | 55350188 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 770,598 | 0.053008 | 55350188 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/AERO | 10000 | 746,861 | 3,694.644594 | 55350188 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | WETH/wstETH | 3000 | 722,381 | 0.798531 | 55350188 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 672,303 | 0.551144 | 55350188 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 664,879 | 4,848,319.861784 | 55350188 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 647,922 | 0.527215 | 55350188 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 623,294 | 0.000008 | 55350188 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v2 | WETH/NPC | 3000 | 615,932 | 151,004.757884 | 55350188 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome | VIRTUAL/WETH | 10000 | 601,100 | 0.000258 | 55350188 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 594,354 | 569,172.811967 | 55350188 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | FLOCK/USDC | 3000 | 574,352 | 0.039247 | 55350188 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 514,730 | 1,033.427173 | 55350188 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome | WETH/msETH (stable) | 500 | 498,170 | 2.400596 | 55350188 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | USDC/USDT | 100 | 497,035 | 1.001011 | 55350188 | `0xD56da2B74bA826f19015E6B7Dd9Dae1903E85DA1` |
| aerodrome | WETH/DRV | 3000 | 491,304 | 6,878.663669 | 55350188 | `0xaC4e562d7C6108f971321F14238E24AE2cC398ac` |
| pancakeswap_v3 | ELSA/USDC | 100 | 470,887 | 0.067824 | 55350188 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| uniswap_v3 | WETH/uSOL | 3000 | 469,711 | 24.705405 | 55350188 | `0xab04A352D4EC8d0F1812A4E5EBe7807Fa67acD48` |

## Recherche d'opportunités
- Cycles : 1724 ; routes examinées : 30542384 ; candidats optimisés : 97773 ; net attendu > 0 : 257 ; dernier cycle 415.6 ms
- Rejets (moteur) : {'spread_below_threshold': 30106278, 'liquidity_below_min': 334731, 'negative_expected_net': 97516, 'borrow_bound_too_small': 3446, 'cycle_budget_exhausted': 156}
- Enregistrements de la session : 97773 ; net attendu > 0 : 257 ; simulés (eth_call de la vraie tx) : 17 (ok 11, échec 6) ; étiquettes ghost N+1 : 8/16 positives
- Décisions : {'REJECTED': 97773} ; motifs de rejet : {'below_safety_margin': 172, 'negative_expected_net': 97516, 'p_lower_below_threshold': 249, 'reliability_not_demonstrated': 8, 'sim_below_estimate': 3, 'simulation_failed': 6, 'stale_data': 25}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 55346177 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.418819 WETH | 0.000076 WETH | 0.000000 WETH | 0.000002 WETH | 0.000074 WETH (0.1445 €) | — | 1.76 | 0.069 (n=319) | REJECTED | below_safety_margin(73797417742801<83763779130135), stale_data(4362ms>4000.0), p_lower_below_threshold(0.07<0.75) |
| 55346177 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 889.698067 USDC | 0.162109 USDC | 0.000000 USDC | 0.005113 USDC | 0.156996 USDC (0.1444 €) | — | 1.76 | 0.069 (n=319) | REJECTED | below_safety_margin(156996<177939), stale_data(4365ms>4000.0), p_lower_below_threshold(0.07<0.75) |
| 55346177 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→USDC | 171.149913 USDC | 0.154905 USDC | 0.000000 USDC | 0.006410 USDC | 0.148495 USDC (0.1366 €) | — | 8.68 | 0.058 (n=130) | REJECTED | stale_data(4301ms>4000.0), p_lower_below_threshold(0.06<0.75) |
| 55346177 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→WETH | 0.080469 WETH | 0.000073 WETH | 0.000000 WETH | 0.000003 WETH | 0.000070 WETH (0.1366 €) | — | 8.67 | 0.058 (n=130) | REJECTED | stale_data(4298ms>4000.0), simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.06<0.75) |
| 55348722 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 654.268100 USDC | 0.087616 USDC | 0.000000 USDC | 0.004787 USDC | 0.082829 USDC (0.0762 €) | — | 1.27 | 0.069 (n=319) | REJECTED | below_safety_margin(82829<130853), p_lower_below_threshold(0.07<0.75) |
| 55348722 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.307237 WETH | 0.000041 WETH | 0.000000 WETH | 0.000002 WETH | 0.000039 WETH (0.0761 €) | — | 1.26 | 0.069 (n=319) | REJECTED | below_safety_margin(38858560354535<61447332248618), p_lower_below_threshold(0.07<0.75) |
| 55346177 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→WETH | 0.058706 WETH | 0.000039 WETH | 0.000000 WETH | 0.000003 WETH | 0.000036 WETH (0.0700 €) | — | 6.09 | 0.175 (n=1020) | REJECTED | stale_data(4320ms>4000.0), simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.17<0.75) |
| 55346177 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 124.183498 USDC | 0.082422 USDC | 0.000000 USDC | 0.006410 USDC | 0.076012 USDC (0.0699 €) | — | 6.12 | 0.175 (n=1020) | REJECTED | stale_data(4323ms>4000.0), p_lower_below_threshold(0.17<0.75) |
| 55346177 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→WETH | 0.055815 WETH | 0.000036 WETH | 0.000000 WETH | 0.000003 WETH | 0.000033 WETH (0.0655 €) | — | 5.99 | 0.299 (n=457) | REJECTED | stale_data(4327ms>4000.0), simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.30<0.75) |
| 55346177 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 118.767460 USDC | 0.077568 USDC | 0.000000 USDC | 0.006410 USDC | 0.071158 USDC (0.0655 €) | — | 5.99 | 0.299 (n=457) | REJECTED | stale_data(4331ms>4000.0), p_lower_below_threshold(0.30<0.75) |
| 55346177 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→WETH | 0.057629 WETH | 0.000036 WETH | 0.000000 WETH | 0.000003 WETH | 0.000033 WETH (0.0654 €) | — | 5.80 | 0.299 (n=457) | REJECTED | stale_data(4335ms>4000.0), p_lower_below_threshold(0.30<0.75) |
| 55346177 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 122.199762 USDC | 0.077442 USDC | 0.000000 USDC | 0.006410 USDC | 0.071032 USDC (0.0653 €) | — | 5.81 | 0.299 (n=457) | REJECTED | stale_data(4339ms>4000.0), p_lower_below_threshold(0.30<0.75) |
| 55346971 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.200028 WETH | 0.000036 WETH | 0.000000 WETH | 0.000003 WETH | 0.000033 WETH (0.0644 €) | — | 1.64 | 0.218 (n=1313) | REJECTED | below_safety_margin(32875270927406<40005625865923), p_lower_below_threshold(0.22<0.75) |
| 55346971 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 429.397370 USDC | 0.076430 USDC | 0.000000 USDC | 0.006796 USDC | 0.069634 USDC (0.0641 €) | — | 1.62 | 0.218 (n=1313) | REJECTED | below_safety_margin(69634<85879), p_lower_below_threshold(0.22<0.75) |
| 55346971 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.005627 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0640 €) | — | 1.65 | 0.218 (n=1313) | REJECTED | below_safety_margin(93<112), p_lower_below_threshold(0.22<0.75) |
| 55346971 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 428.715723 USDC | 0.073952 USDC | 0.000000 USDC | 0.005161 USDC | 0.068791 USDC (0.0633 €) | — | 1.60 | 0.069 (n=319) | REJECTED | below_safety_margin(68791<85743), p_lower_below_threshold(0.07<0.75) |
| 55346971 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.201306 WETH | 0.000035 WETH | 0.000000 WETH | 0.000002 WETH | 0.000032 WETH (0.0632 €) | — | 1.60 | 0.069 (n=319) | REJECTED | below_safety_margin(32270852989532<40261142645193), p_lower_below_threshold(0.07<0.75) |
| 55346177 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→WETH | 0.056329 WETH | 0.000035 WETH | 0.000000 WETH | 0.000003 WETH | 0.000032 WETH (0.0628 €) | — | 5.70 | 0.175 (n=1020) | REJECTED | stale_data(4342ms>4000.0), p_lower_below_threshold(0.17<0.75) |
| 55346177 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 119.813820 USDC | 0.074644 USDC | 0.000000 USDC | 0.006410 USDC | 0.068234 USDC (0.0628 €) | — | 5.70 | 0.175 (n=1020) | REJECTED | stale_data(4346ms>4000.0), p_lower_below_threshold(0.17<0.75) |
| 55346177 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 545.677081 USDC | 0.064486 USDC | 0.000000 USDC | 0.006410 USDC | 0.058076 USDC (0.0534 €) | — | 1.06 | 0.218 (n=1313) | REJECTED | below_safety_margin(58076<109135), stale_data(4379ms>4000.0), p_lower_below_threshold(0.22<0.75) |
| 55346177 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.256091 WETH | 0.000030 WETH | 0.000000 WETH | 0.000003 WETH | 0.000027 WETH (0.0534 €) | — | 1.06 | 0.218 (n=1313) | REJECTED | below_safety_margin(27260334202825<51218160628537), stale_data(4375ms>4000.0), p_lower_below_threshold(0.22<0.75) |
| 55346177 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.006526 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0530 €) | — | 1.18 | 0.218 (n=1313) | REJECTED | below_safety_margin(77<130), stale_data(4382ms>4000.0), p_lower_below_threshold(0.22<0.75) |
| 55349322 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→AERO→[aerodrome]→USDC | 284.086347 USDC | 0.062357 USDC | 0.000000 USDC | 0.006108 USDC | 0.056249 USDC (0.0517 €) | — | 1.98 | 0.329 (n=128) | REJECTED | below_safety_margin(56249<56817), p_lower_below_threshold(0.33<0.75) |
| 55349300 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→AERO→[aerodrome]→USDC | 284.086347 USDC | 0.062357 USDC | 0.000000 USDC | 0.006112 USDC | 0.056245 USDC (0.0517 €) | — | 1.98 | 0.329 (n=128) | REJECTED | below_safety_margin(56245<56817), p_lower_below_threshold(0.33<0.75) |
| 55349322 | WETH→[uniswap_v3]→AERO→[aerodrome]→USDC→[pancakeswap_v3]→WETH | 0.133613 WETH | 0.000029 WETH | 0.000000 WETH | 0.000003 WETH | 0.000026 WETH (0.0517 €) | — | 1.98 | 0.329 (n=128) | REJECTED | below_safety_margin(26418724161174<26722571878096), p_lower_below_threshold(0.33<0.75) |

## Fiabilité et décision
- Observations ghost : 7117 ; taux observé 0.185 ; borne inférieure crédible (0.9) 0.179 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 17.9% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
