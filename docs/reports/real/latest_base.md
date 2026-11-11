# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-11T17:29:56+00:00 ; durée 299.2 min ; blocs 56049289 → 56139006 (7911 vus)

## Connexion
- Requêtes RPC : 124428 ; erreurs : 460 ; latence p50/p95 : 445.7/1,848.8 ms
- Rafraîchissements d'état : 7911 ; âge des données au dernier bloc : 11.62 s ; changements de frais LP observés (pools à frais dynamiques) : 9406
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 6839 ; cycles déclenchés par événement : 1496 ; avance médiane sur le rafraîchissement multicall : 969 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,095.67 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 460 pools, 267 jetons, 15580 routes
- Par DEX : uniswap_v3 134, aerodrome_slipstream 99, aerodrome 187, pancakeswap_v3 27, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 1
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 161 (rejetés 2) → 566 jetons ; pools candidats 3638 (énumérés 283, par paires 0), mesurés 462, sous le plancher de 10000.0 $ : 2 → gardés 460 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2055.911323, 'cbBTC': 73875.741474, 'AERO': 0.535737}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 135,854,809 | 2,095.668086 | 56139040 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,696,236 | 0.028099 | 56139040 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 8,731,522 | 0.028050 | 56139040 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 8,521,030 | 0.000013 | 56139040 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 7,201,109 | 2,090.032086 | 56139040 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,094,643 | 101.660657 | 56139040 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,677,892 | 0.028093 | 56139040 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 4,343,898 | 1.768759 | 56139040 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,109,769 | 2,090.274004 | 56139040 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,929,829 | 0.998575 | 56139040 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,089,683 | 43,055.478922 | 56139040 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 224 | 2,968,322 | 2,090.589041 | 56139040 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2510 | 2,251,385 | 0.028063 | 56139040 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 1,992,509 | 1,121,348.046698 | 56139040 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 532 | 1,659,980 | 0.000013 | 56139040 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | XDP/USDC | 100 | 1,623,095 | 0.016403 | 56139040 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,619,086 | 0.000013 | 56139040 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,579,490 | 0.000000 | 56139040 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,541,128 | 0.000013 | 56139040 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,522,170 | 0.006449 | 56139040 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,465,229 | 0.828374 | 56139040 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,445,417 | 419.322684 | 56139040 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,438,232 | 1.405931 | 56139040 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | WETH/AERO | 3000 | 1,303,374 | 3,704.406674 | 56139040 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v2 | WETH/USDC | 3000 | 1,283,657 | 2,093.874584 | 56139040 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,247,402 | 14,924.002518 | 56139040 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/USDC | 3000 | 1,168,577 | 2,095.744460 | 56139040 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,143,038 | 2,090.029085 | 56139040 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,060,753 | 86.359612 | 56139040 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,060,166 | 33,760,442.851361 | 56139040 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/VVV | 10000 | 1,056,959 | 101.857345 | 56139040 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome_slipstream | USDC/VELVET | 100 | 976,387 | 20.321954 | 56139040 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/BRETT | 10000 | 962,202 | 554,843.191422 | 56139040 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | USDC/VVV | 3000 | 931,992 | 0.048650 | 56139040 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 931,223 | 0.001502 | 56139040 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 356 | 921,973 | 0.000013 | 56139040 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | WETH/TOSHI | 10000 | 921,729 | 23,053,289.280513 | 56139040 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | WETH/MORPHO | 3000 | 898,627 | 1,017.427940 | 56139040 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/USDC | 10000 | 885,963 | 2,080.323257 | 56139040 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | DRB/WETH | 10000 | 870,937 | 0.000000 | 56139040 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | USDC/NOCK | 3000 | 779,011 | 77.507684 | 56139040 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| pancakeswap_v3 | QUID/USDC | 100 | 768,459 | 0.052710 | 56139040 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 759,542 | 22.508590 | 56139040 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome | WETH/EDEL | 7000 | 748,325 | 119,566.622541 | 56139040 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | WETH/AERO | 10000 | 729,135 | 3,732.302618 | 56139040 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | WETH/wstETH | 3000 | 709,512 | 0.802938 | 56139040 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 684,169 | 0.544243 | 56139040 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 667,919 | 4,665,730.940469 | 56139040 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 621,892 | 0.487134 | 56139040 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/NPC | 3000 | 617,300 | 146,029.586973 | 56139040 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | AERO/cbBTC | 1025 | 604,661 | 0.000008 | 56139040 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | VIRTUAL/WETH | 10000 | 592,017 | 0.000259 | 56139040 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 591,547 | 556,047.595305 | 56139040 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | FLOCK/USDC | 3000 | 568,280 | 0.038577 | 56139040 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome_slipstream | WETH/MORPHO | 2721 | 503,676 | 1,017.830656 | 56139040 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| pancakeswap_v3 | ELSA/USDC | 100 | 472,942 | 0.068331 | 56139040 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| uniswap_v3 | USDC/MORPHO | 10000 | 462,704 | 0.490200 | 56139040 | `0x2043B296fFC6b2d3bf4A3F3167d2Afb3B0FBdbEE` |
| aerodrome_slipstream | USDC/USDT | 17 | 454,468 | 1.000498 | 56139040 | `0xa41Bc0AFfbA7Fd420d186b84899d7ab2aC57fcD1` |
| uniswap_v3 | WETH/uSOL | 3000 | 451,257 | 24.625100 | 56139040 | `0xab04A352D4EC8d0F1812A4E5EBe7807Fa67acD48` |
| uniswap_v3 | WETH/UNI | 10000 | 444,739 | 317.476230 | 56139040 | `0xAb365f161Dd501473a1ff0D2ef0dCE94E7398839` |

## Recherche d'opportunités
- Cycles : 9406 ; routes examinées : 146545480 ; candidats optimisés : 908362 ; net attendu > 0 : 3151 ; dernier cycle 403.2 ms
- Rejets (moteur) : {'spread_below_threshold': 143148035, 'liquidity_below_min': 2446811, 'negative_expected_net': 905211, 'borrow_bound_too_small': 12679, 'pool_quarantined': 12556, 'cycle_budget_exhausted': 10984, 'unquotable': 6053}
- Enregistrements de la session : 908362 ; net attendu > 0 : 3151 ; simulés (eth_call de la vraie tx) : 126 (ok 80, échec 46) ; étiquettes ghost N+1 : 58/107 positives
- Décisions : {'REJECTED': 908362} ; motifs de rejet : {'below_safety_margin': 1899, 'negative_expected_net': 905211, 'p_lower_below_threshold': 2830, 'price_impact': 31, 'reliability_not_demonstrated': 321, 'sim_below_estimate': 15, 'simulated_net_nonpositive': 7, 'simulation_failed': 46, 'stale_data': 1419}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 56136932 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→VIRTUAL→[uniswap_v3]→USDC | 4,566.905637 USDC | 25.187569 USDC | 0.000000 USDC | 0.007645 USDC | 25.179924 USDC (23.1655 €) | — | 55.14 | 0.000 (n=40) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 56136932 | WETH→[aerodrome_slipstream]→VIRTUAL→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 2.180370 WETH | 0.012024 WETH | 0.000000 WETH | 0.000004 WETH | 0.012020 WETH (23.1264 €) | — | 55.13 | 0.000 (n=40) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 56136932 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→VIRTUAL→[uniswap_v3]→USDC | 4,587.264902 USDC | 24.901791 USDC | 0.000000 USDC | 0.006689 USDC | 24.895102 USDC (22.9035 €) | — | 54.27 | 0.000 (n=43) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 56136932 | WETH→[aerodrome_slipstream]→VIRTUAL→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 2.189839 WETH | 0.011888 WETH | 0.000000 WETH | 0.000003 WETH | 0.011885 WETH (22.8658 €) | — | 54.27 | 0.000 (n=43) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 56136932 | USDC→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→VIRTUAL→[uniswap_v3]→USDC | 4,076.572142 USDC | 22.121164 USDC | 0.000000 USDC | 0.006689 USDC | 22.114475 USDC (20.3453 €) | — | 54.25 | 0.000 (n=43) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 56136932 | WETH→[aerodrome_slipstream]→VIRTUAL→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 1.944047 WETH | 0.010548 WETH | 0.000000 WETH | 0.000003 WETH | 0.010545 WETH (20.2881 €) | — | 54.24 | 0.000 (n=43) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 56136932 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→VIRTUAL→[uniswap_v3]→USDC | 4,050.839651 USDC | 21.544834 USDC | 0.000000 USDC | 0.007007 USDC | 21.537827 USDC (19.8148 €) | — | 53.17 | 0.000 (n=40) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 56136932 | WETH→[aerodrome_slipstream]→VIRTUAL→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 1.931519 WETH | 0.010273 WETH | 0.000000 WETH | 0.000003 WETH | 0.010269 WETH (19.7579 €) | — | 53.17 | 0.000 (n=40) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 56136932 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→VIRTUAL→[uniswap_v3]→USDC | 3,314.799081 USDC | 17.973162 USDC | 0.000000 USDC | 0.007326 USDC | 17.965836 USDC (16.5286 €) | — | 54.20 | 0.000 (n=43) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 56136932 | WETH→[aerodrome_slipstream]→VIRTUAL→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 1.578441 WETH | 0.008555 WETH | 0.000000 WETH | 0.000004 WETH | 0.008552 WETH (16.4533 €) | — | 54.18 | 0.000 (n=43) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 56136931 | cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→VIRTUAL→[aerodrome]→cbBTC | 0.011108 cbBTC | 0.000214 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000214 cbBTC (14.6746 €) | — | 192.82 | 0.001 (n=12) | REJECTED | stale_data(5046ms>4000.0), reliability_not_demonstrated |
| 56136931 | WETH→[uniswap_v3]→VIRTUAL→[aerodrome]→cbBTC→[pancakeswap_v3]→WETH | 0.395469 WETH | 0.007629 WETH | 0.000000 WETH | 0.000003 WETH | 0.007626 WETH (14.6716 €) | 0.007626 WETH | 192.83 | 0.001 (n=12) | REJECTED | stale_data(5040ms>4000.0), reliability_not_demonstrated |
| 56136931 | cbBTC→[uniswap_v3]→WETH→[uniswap_v3]→VIRTUAL→[aerodrome]→cbBTC | 0.010727 cbBTC | 0.000208 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000208 cbBTC (14.2300 €) | — | 193.61 | 0.000 (n=28) | REJECTED | stale_data(5126ms>4000.0), reliability_not_demonstrated |
| 56136931 | WETH→[uniswap_v3]→VIRTUAL→[aerodrome]→cbBTC→[uniswap_v3]→WETH | 0.381901 WETH | 0.007396 WETH | 0.000000 WETH | 0.000003 WETH | 0.007393 WETH (14.2241 €) | 0.007393 WETH | 193.59 | 0.000 (n=28) | REJECTED | stale_data(5121ms>4000.0), reliability_not_demonstrated |
| 56136931 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→VIRTUAL→[aerodrome]→cbBTC | 0.010872 cbBTC | 0.000203 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000203 cbBTC (13.8874 €) | — | 186.44 | 0.001 (n=12) | REJECTED | stale_data(5209ms>4000.0), reliability_not_demonstrated |
| 56136931 | WETH→[aerodrome_slipstream]→VIRTUAL→[aerodrome]→cbBTC→[pancakeswap_v3]→WETH | 0.387145 WETH | 0.007220 WETH | 0.000000 WETH | 0.000003 WETH | 0.007217 WETH (13.8850 €) | 0.007217 WETH | 186.41 | 0.001 (n=12) | REJECTED | stale_data(5203ms>4000.0), reliability_not_demonstrated |
| 56136931 | cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→VIRTUAL→[aerodrome]→cbBTC | 0.010316 cbBTC | 0.000202 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000201 cbBTC (13.8059 €) | — | 195.34 | 0.001 (n=12) | REJECTED | stale_data(5068ms>4000.0), reliability_not_demonstrated |
| 56136931 | WETH→[uniswap_v3]→VIRTUAL→[aerodrome]→cbBTC→[pancakeswap_v3]→WETH | 0.366808 WETH | 0.007168 WETH | 0.000000 WETH | 0.000003 WETH | 0.007165 WETH (13.7849 €) | — | 195.33 | 0.001 (n=12) | REJECTED | stale_data(5073ms>4000.0), reliability_not_demonstrated |
| 56136931 | cbBTC→[uniswap_v3]→WETH→[aerodrome_slipstream]→VIRTUAL→[aerodrome]→cbBTC | 0.010499 cbBTC | 0.000197 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000197 cbBTC (13.4640 €) | — | 187.18 | 0.000 (n=28) | REJECTED | stale_data(5282ms>4000.0), reliability_not_demonstrated |
| 56136931 | WETH→[aerodrome_slipstream]→VIRTUAL→[aerodrome]→cbBTC→[uniswap_v3]→WETH | 0.373657 WETH | 0.006997 WETH | 0.000000 WETH | 0.000003 WETH | 0.006994 WETH (13.4563 €) | — | 187.18 | 0.000 (n=28) | REJECTED | stale_data(5277ms>4000.0), reliability_not_demonstrated |
| 56136931 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→VIRTUAL→[aerodrome]→cbBTC | 0.010096 cbBTC | 0.000191 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000191 cbBTC (13.0693 €) | — | 188.93 | 0.001 (n=12) | REJECTED | stale_data(5251ms>4000.0), reliability_not_demonstrated |
| 56136931 | WETH→[aerodrome_slipstream]→VIRTUAL→[aerodrome]→cbBTC→[pancakeswap_v3]→WETH | 0.359017 WETH | 0.006786 WETH | 0.000000 WETH | 0.000003 WETH | 0.006783 WETH (13.0499 €) | — | 188.93 | 0.001 (n=12) | REJECTED | stale_data(5246ms>4000.0), reliability_not_demonstrated |
| 56136931 | cbBTC→[aerodrome_slipstream]→WETH→[uniswap_v3]→VIRTUAL→[aerodrome]→cbBTC | 0.008693 cbBTC | 0.000187 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000187 cbBTC (12.7973 €) | — | 214.86 | 0.000 (n=28) | REJECTED | stale_data(5094ms>4000.0), reliability_not_demonstrated |
| 56136931 | WETH→[uniswap_v3]→VIRTUAL→[aerodrome]→cbBTC→[aerodrome_slipstream]→WETH | 0.309419 WETH | 0.006651 WETH | 0.000000 WETH | 0.000003 WETH | 0.006648 WETH (12.7899 €) | — | 214.84 | 0.000 (n=28) | REJECTED | stale_data(5089ms>4000.0), reliability_not_demonstrated |
| 56136931 | cbBTC→[uniswap_v3]→WETH→[uniswap_v3]→VIRTUAL→[aerodrome]→cbBTC | 0.008266 cbBTC | 0.000181 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000181 cbBTC (12.3821 €) | — | 218.63 | 0.000 (n=28) | REJECTED | stale_data(5099ms>4000.0), reliability_not_demonstrated |

## Fiabilité et décision
- Observations ghost : 8164 ; taux observé 0.216 ; borne inférieure crédible (0.9) 0.211 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 21.1% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ✅ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
