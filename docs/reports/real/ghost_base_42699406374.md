# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-09T21:28:02+00:00 ; durée 15.29 min ; blocs 55341906 → 55346504 (766 vus)

## Connexion
- Requêtes RPC : 10843 ; erreurs : 0 ; latence p50/p95 : 313.6/1,132.4 ms
- Rafraîchissements d'état : 766 ; âge des données au dernier bloc : 5.76 s ; changements de frais LP observés (pools à frais dynamiques) : 349
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 598 ; cycles déclenchés par événement : 282 ; avance médiane sur le rafraîchissement multicall : 431 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,127.77 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 468 pools, 272 jetons, 17716 routes
- Par DEX : uniswap_v3 134, aerodrome_slipstream 99, aerodrome 193, pancakeswap_v3 28, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 166 (rejetés 2) → 571 jetons ; pools candidats 3654 (énumérés 289, par paires 0), mesurés 471, sous le plancher de 10000.0 $ : 3 → gardés 468 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDbC': 1.0, 'USDC': 1.0, 'WETH': 2127.766856, 'cbBTC': 74794.411024, 'AERO': 0.572023}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 139,785,720 | 2,127.766944 | 55346504 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,655,722 | 0.028444 | 55346504 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,333,073 | 0.000013 | 55346504 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 8,787,243 | 0.028437 | 55346504 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 7,480,549 | 2,127.218225 | 55346504 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,341,101 | 98.091350 | 55346504 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,932,934 | 0.028438 | 55346504 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 4,579,267 | 1.747594 | 55346504 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,009,910 | 2,127.379823 | 55346504 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,891,095 | 1.000033 | 55346504 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,106,959 | 43,892.698508 | 55346504 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 549 | 3,028,177 | 2,127.361775 | 55346504 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,348,591 | 0.028441 | 55346504 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 2,031,757 | 1,111,732.813378 | 55346504 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,705,643 | 0.000013 | 55346504 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | USDC/cbBTC | 412 | 1,691,656 | 0.000013 | 55346504 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | XDP/USDC | 100 | 1,581,283 | 0.015759 | 55346504 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,563,388 | 0.006562 | 55346504 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,562,523 | 0.000000 | 55346504 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,493,197 | 0.000013 | 55346504 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,481,281 | 1.407587 | 55346504 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,465,442 | 424.798157 | 55346504 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,456,949 | 0.821811 | 55346504 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,320,505 | 3,723.831035 | 55346504 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v2 | WETH/USDC | 3000 | 1,293,210 | 2,130.627821 | 55346504 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,249,959 | 14,915.862630 | 55346504 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/USDC | 3000 | 1,221,417 | 2,132.279011 | 55346504 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome | USDC/SEND | 3000 | 1,107,263 | 79.257048 | 55346504 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,102,799 | 2,127.322666 | 55346504 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | WETH/doginme | 10000 | 1,050,306 | 36,312,398.434913 | 55346504 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/VVV | 10000 | 985,749 | 98.507483 | 55346504 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/BRETT | 10000 | 970,755 | 565,879.607607 | 55346504 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | USDC/VVV | 3000 | 965,264 | 0.046076 | 55346504 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome_slipstream | USDC/VELVET | 100 | 961,876 | 21.260693 | 55346504 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 936,946 | 0.001511 | 55346504 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| uniswap_v3 | WETH/TOSHI | 10000 | 936,790 | 23,213,728.096903 | 55346504 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/cbBTC | 332 | 928,280 | 0.000013 | 55346504 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/NOCK | 3000 | 919,209 | 74.161721 | 55346504 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/MORPHO | 3000 | 909,788 | 1,032.741252 | 55346504 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/USDC | 10000 | 887,623 | 2,127.924155 | 55346504 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | DRB/WETH | 10000 | 887,391 | 0.000000 | 55346504 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | WETH/EDEL | 7000 | 816,888 | 103,434.488382 | 55346504 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome_slipstream | USDC/SAPIEN | 4505 | 773,679 | 21.924424 | 55346504 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 771,091 | 0.053079 | 55346504 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/AERO | 10000 | 746,241 | 3,694.644594 | 55346504 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | WETH/wstETH | 3000 | 722,419 | 0.798411 | 55346504 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 672,289 | 0.550997 | 55346504 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 664,806 | 4,849,152.505807 | 55346504 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 647,922 | 0.527215 | 55346504 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 622,517 | 0.000008 | 55346504 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v2 | WETH/NPC | 3000 | 616,166 | 150,883.061464 | 55346504 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome | VIRTUAL/WETH | 10000 | 601,085 | 0.000258 | 55346504 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/BRETT | 2102 | 594,336 | 570,037.890210 | 55346504 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | FLOCK/USDC | 3000 | 573,759 | 0.039184 | 55346504 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 514,843 | 1,033.238520 | 55346504 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome | WETH/msETH (stable) | 500 | 498,158 | 2.400596 | 55346504 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | USDC/USDT | 100 | 497,035 | 1.001011 | 55346504 | `0xD56da2B74bA826f19015E6B7Dd9Dae1903E85DA1` |
| aerodrome | WETH/DRV | 3000 | 491,698 | 6,867.322545 | 55346504 | `0xaC4e562d7C6108f971321F14238E24AE2cC398ac` |
| pancakeswap_v3 | ELSA/USDC | 100 | 472,057 | 0.068041 | 55346504 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| uniswap_v3 | WETH/uSOL | 3000 | 469,859 | 24.688056 | 55346504 | `0xab04A352D4EC8d0F1812A4E5EBe7807Fa67acD48` |

## Recherche d'opportunités
- Cycles : 1047 ; routes examinées : 18548652 ; candidats optimisés : 55623 ; net attendu > 0 : 55 ; dernier cycle 48.5 ms
- Rejets (moteur) : {'spread_below_threshold': 18297055, 'liquidity_below_min': 193736, 'negative_expected_net': 55568, 'borrow_bound_too_small': 2092, 'cycle_budget_exhausted': 146}
- Enregistrements de la session : 55623 ; net attendu > 0 : 55 ; simulés (eth_call de la vraie tx) : 6 (ok 0, échec 6) ; étiquettes ghost N+1 : 0/6 positives
- Décisions : {'REJECTED': 55623} ; motifs de rejet : {'below_safety_margin': 24, 'negative_expected_net': 55568, 'p_lower_below_threshold': 55, 'simulation_failed': 6, 'stale_data': 25}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 55346177 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.418819 WETH | 0.000076 WETH | 0.000000 WETH | 0.000002 WETH | 0.000074 WETH (0.1445 €) | — | 1.76 | 0.069 (n=319) | REJECTED | below_safety_margin(73797417742801<83763779130135), stale_data(4362ms>4000.0), p_lower_below_threshold(0.07<0.75) |
| 55346177 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 889.698067 USDC | 0.162109 USDC | 0.000000 USDC | 0.005113 USDC | 0.156996 USDC (0.1444 €) | — | 1.76 | 0.069 (n=319) | REJECTED | below_safety_margin(156996<177939), stale_data(4365ms>4000.0), p_lower_below_threshold(0.07<0.75) |
| 55346177 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→USDC | 171.149913 USDC | 0.154905 USDC | 0.000000 USDC | 0.006410 USDC | 0.148495 USDC (0.1366 €) | — | 8.68 | 0.058 (n=130) | REJECTED | stale_data(4301ms>4000.0), p_lower_below_threshold(0.06<0.75) |
| 55346177 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→WETH | 0.080469 WETH | 0.000073 WETH | 0.000000 WETH | 0.000003 WETH | 0.000070 WETH (0.1366 €) | — | 8.67 | 0.058 (n=130) | REJECTED | stale_data(4298ms>4000.0), simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.06<0.75) |
| 55346177 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→WETH | 0.058706 WETH | 0.000039 WETH | 0.000000 WETH | 0.000003 WETH | 0.000036 WETH (0.0700 €) | — | 6.09 | 0.175 (n=1020) | REJECTED | stale_data(4320ms>4000.0), simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.17<0.75) |
| 55346177 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 124.183498 USDC | 0.082422 USDC | 0.000000 USDC | 0.006410 USDC | 0.076012 USDC (0.0699 €) | — | 6.12 | 0.175 (n=1020) | REJECTED | stale_data(4323ms>4000.0), p_lower_below_threshold(0.17<0.75) |
| 55346177 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→WETH | 0.055815 WETH | 0.000036 WETH | 0.000000 WETH | 0.000003 WETH | 0.000033 WETH (0.0655 €) | — | 5.99 | 0.299 (n=457) | REJECTED | stale_data(4327ms>4000.0), simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.30<0.75) |
| 55346177 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 118.767460 USDC | 0.077568 USDC | 0.000000 USDC | 0.006410 USDC | 0.071158 USDC (0.0655 €) | — | 5.99 | 0.299 (n=457) | REJECTED | stale_data(4331ms>4000.0), p_lower_below_threshold(0.30<0.75) |
| 55346177 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→WETH | 0.057629 WETH | 0.000036 WETH | 0.000000 WETH | 0.000003 WETH | 0.000033 WETH (0.0654 €) | — | 5.80 | 0.299 (n=457) | REJECTED | stale_data(4335ms>4000.0), p_lower_below_threshold(0.30<0.75) |
| 55346177 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 122.199762 USDC | 0.077442 USDC | 0.000000 USDC | 0.006410 USDC | 0.071032 USDC (0.0653 €) | — | 5.81 | 0.299 (n=457) | REJECTED | stale_data(4339ms>4000.0), p_lower_below_threshold(0.30<0.75) |
| 55346177 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→WETH | 0.056329 WETH | 0.000035 WETH | 0.000000 WETH | 0.000003 WETH | 0.000032 WETH (0.0628 €) | — | 5.70 | 0.175 (n=1020) | REJECTED | stale_data(4342ms>4000.0), p_lower_below_threshold(0.17<0.75) |
| 55346177 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 119.813820 USDC | 0.074644 USDC | 0.000000 USDC | 0.006410 USDC | 0.068234 USDC (0.0628 €) | — | 5.70 | 0.175 (n=1020) | REJECTED | stale_data(4346ms>4000.0), p_lower_below_threshold(0.17<0.75) |
| 55346177 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 545.677081 USDC | 0.064486 USDC | 0.000000 USDC | 0.006410 USDC | 0.058076 USDC (0.0534 €) | — | 1.06 | 0.218 (n=1313) | REJECTED | below_safety_margin(58076<109135), stale_data(4379ms>4000.0), p_lower_below_threshold(0.22<0.75) |
| 55346177 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.256091 WETH | 0.000030 WETH | 0.000000 WETH | 0.000003 WETH | 0.000027 WETH (0.0534 €) | — | 1.06 | 0.218 (n=1313) | REJECTED | below_safety_margin(27260334202825<51218160628537), stale_data(4375ms>4000.0), p_lower_below_threshold(0.22<0.75) |
| 55346177 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.006526 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0530 €) | — | 1.18 | 0.218 (n=1313) | REJECTED | below_safety_margin(77<130), stale_data(4382ms>4000.0), p_lower_below_threshold(0.22<0.75) |
| 55344828 | cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.001219 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0434 €) | — | 5.17 | 0.299 (n=457) | REJECTED | p_lower_below_threshold(0.30<0.75) |
| 55344828 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→USDC | 111.664293 USDC | 0.053403 USDC | 0.000000 USDC | 0.006409 USDC | 0.046994 USDC (0.0432 €) | — | 4.21 | 0.299 (n=457) | REJECTED | p_lower_below_threshold(0.30<0.75) |
| 55346177 | WETH→[sushiswap_v3]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→WETH | 0.034021 WETH | 0.000024 WETH | 0.000000 WETH | 0.000003 WETH | 0.000021 WETH (0.0412 €) | — | 6.19 | 0.299 (n=457) | REJECTED | stale_data(4313ms>4000.0), p_lower_below_threshold(0.30<0.75) |
| 55346177 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→WETH→[sushiswap_v3]→USDC | 72.279855 USDC | 0.051160 USDC | 0.000000 USDC | 0.006410 USDC | 0.044750 USDC (0.0412 €) | — | 6.19 | 0.299 (n=457) | REJECTED | stale_data(4316ms>4000.0), p_lower_below_threshold(0.30<0.75) |
| 55346177 | WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→WETH | 0.044047 WETH | 0.000023 WETH | 0.000000 WETH | 0.000002 WETH | 0.000020 WETH (0.0401 €) | — | 4.65 | 0.049 (n=433) | REJECTED | stale_data(4349ms>4000.0), p_lower_below_threshold(0.05<0.75) |
| 55346177 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 308.421295 USDC | 0.047286 USDC | 0.000000 USDC | 0.005436 USDC | 0.041850 USDC (0.0385 €) | — | 1.36 | 0.044 (n=99) | REJECTED | below_safety_margin(41850<61684), stale_data(4371ms>4000.0), p_lower_below_threshold(0.04<0.75) |
| 55346177 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.145424 WETH | 0.000022 WETH | 0.000000 WETH | 0.000003 WETH | 0.000020 WETH (0.0385 €) | — | 1.35 | 0.044 (n=99) | REJECTED | below_safety_margin(19668293763758<29084736237497), stale_data(4368ms>4000.0), p_lower_below_threshold(0.04<0.75) |
| 55344828 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 96.328338 USDC | 0.043854 USDC | 0.000000 USDC | 0.006409 USDC | 0.037445 USDC (0.0344 €) | — | 3.89 | 0.175 (n=1020) | REJECTED | p_lower_below_threshold(0.17<0.75) |
| 55344828 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.001147 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0344 €) | — | 4.36 | 0.175 (n=1020) | REJECTED | p_lower_below_threshold(0.17<0.75) |
| 55344828 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→USDC | 95.355451 USDC | 0.042345 USDC | 0.000000 USDC | 0.006409 USDC | 0.035936 USDC (0.0331 €) | — | 3.77 | 0.299 (n=457) | REJECTED | p_lower_below_threshold(0.30<0.75) |

## Fiabilité et décision
- Observations ghost : 7107 ; taux observé 0.184 ; borne inférieure crédible (0.9) 0.178 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 17.8% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
