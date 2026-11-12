# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-12T16:38:09+00:00 ; durée 3.0 min ; blocs 56554640 → 56555507 (144 vus)

## Connexion
- Requêtes RPC : 1978 ; erreurs : 0 ; latence p50/p95 : 278.4/1,614.7 ms
- Rafraîchissements d'état : 144 ; âge des données au dernier bloc : 11.96 s ; changements de frais LP observés (pools à frais dynamiques) : 115
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 301 ; cycles déclenchés par événement : 82 ; avance médiane sur le rafraîchissement multicall : 431 ms
- Gaz : base fee 0.005090 gwei ; prix ETH (pool le plus profond) : 2,007.07 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 454 pools, 266 jetons, 14202 routes
- Par DEX : uniswap_v3 133, aerodrome_slipstream 96, aerodrome 187, pancakeswap_v3 25, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 1
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 160 (rejetés 2) → 565 jetons ; pools candidats 3627 (énumérés 281, par paires 0), mesurés 456, sous le plancher de 10000.0 $ : 2 → gardés 454 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'DAI': 1.0, 'USDC': 1.0, 'WETH': 2012.424484, 'cbBTC': 71768.389273, 'AERO': 0.523178}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 132,470,954 | 2,006.860949 | 56555542 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,251,515 | 0.027951 | 56555542 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 8,691,507 | 0.000014 | 56555542 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 8,514,829 | 0.028017 | 56555542 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 6,964,311 | 2,001.986342 | 56555542 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 6,678,328 | 105.234611 | 56555542 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,189,277 | 0.027947 | 56555542 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 4,156,200 | 1.915123 | 56555542 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,063,801 | 2,001.138300 | 56555542 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,783,452 | 0.998590 | 56555542 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 2,977,337 | 42,528.478465 | 56555542 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 417 | 2,804,118 | 2,001.347984 | 56555542 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2560 | 2,150,707 | 0.028010 | 56555542 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 1,875,457 | 1,160,931.772445 | 56555542 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | XDP/USDC | 100 | 1,652,462 | 0.016865 | 56555542 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | USDC/cbBTC | 544 | 1,608,372 | 0.000014 | 56555542 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,575,288 | 0.000014 | 56555542 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,526,918 | 0.000000 | 56555542 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,501,869 | 0.006656 | 56555542 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,474,571 | 0.000014 | 56555542 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,463,486 | 0.831291 | 56555542 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,374,920 | 429.069744 | 56555542 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v2 | WETH/USDC | 3000 | 1,256,348 | 2,007.411467 | 56555542 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| uniswap_v3 | WETH/AERO | 3000 | 1,222,279 | 3,843.833263 | 56555542 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,186,185 | 15,299.364682 | 56555542 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/USDC | 3000 | 1,141,940 | 2,006.476874 | 56555542 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,088,633 | 2,001.477467 | 56555542 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,061,177 | 86.290648 | 56555542 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,047,058 | 1.389298 | 56555542 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | WETH/doginme | 10000 | 1,012,489 | 34,293,975.350421 | 56555542 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/VVV | 10000 | 978,277 | 105.928308 | 56555542 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome_slipstream | USDC/VELVET | 100 | 969,284 | 20.772484 | 56555542 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/BRETT | 10000 | 914,856 | 566,667.795336 | 56555542 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 891,735 | 0.001486 | 56555542 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| uniswap_v3 | WETH/TOSHI | 10000 | 878,899 | 23,229,511.263151 | 56555542 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | USDC/VVV | 3000 | 877,429 | 0.052376 | 56555542 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome_slipstream | USDC/cbBTC | 354 | 871,261 | 0.000014 | 56555542 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | WETH/USDC | 10000 | 868,113 | 2,005.358242 | 56555542 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 866,403 | 1,006.382970 | 56555542 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | DRB/WETH | 10000 | 830,985 | 0.000000 | 56555542 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | USDC/NOCK | 3000 | 766,504 | 80.057857 | 56555542 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| pancakeswap_v3 | QUID/USDC | 100 | 743,500 | 0.049239 | 56555542 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome_slipstream | USDC/SAPIEN | 4525 | 739,327 | 23.380906 | 56555542 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome | WETH/AERO | 10000 | 685,458 | 3,870.915778 | 56555542 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | WETH/wstETH | 3000 | 679,997 | 0.801801 | 56555542 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 649,980 | 0.514109 | 56555542 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 629,726 | 4,816,909.901838 | 56555542 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome | WETH/EDEL | 7000 | 599,074 | 171,109.496002 | 56555542 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | TIG/USDC | 10000 | 592,649 | 0.443073 | 56555542 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/NPC | 3000 | 576,633 | 153,577.891344 | 56555542 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome | VIRTUAL/WETH | 10000 | 560,810 | 0.000255 | 56555542 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/BRETT | 2102 | 560,466 | 564,609.443280 | 56555542 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome_slipstream | AERO/cbBTC | 1025 | 557,956 | 0.000007 | 56555542 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v3 | FLOCK/USDC | 3000 | 554,744 | 0.037361 | 56555542 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome_slipstream | WETH/MORPHO | 2706 | 483,383 | 1,006.600432 | 56555542 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| pancakeswap_v3 | ELSA/USDC | 100 | 456,006 | 0.065323 | 56555542 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| aerodrome_slipstream | USDC/USDT | 8 | 450,227 | 1.001066 | 56555542 | `0xa41Bc0AFfbA7Fd420d186b84899d7ab2aC57fcD1` |
| uniswap_v3 | USDC/MORPHO | 10000 | 446,572 | 0.502823 | 56555542 | `0x2043B296fFC6b2d3bf4A3F3167d2Afb3B0FBdbEE` |
| uniswap_v3 | WETH/uSOL | 3000 | 428,442 | 24.789313 | 56555542 | `0xab04A352D4EC8d0F1812A4E5EBe7807Fa67acD48` |
| uniswap_v3 | WETH/UNI | 10000 | 423,098 | 333.493261 | 56555542 | `0xAb365f161Dd501473a1ff0D2ef0dCE94E7398839` |

## Recherche d'opportunités
- Cycles : 225 ; routes examinées : 3195450 ; candidats optimisés : 14445 ; net attendu > 0 : 21 ; dernier cycle 939.4 ms
- Rejets (moteur) : {'spread_below_threshold': 3115646, 'liquidity_below_min': 65341, 'negative_expected_net': 14424, 'cycle_budget_exhausted': 18}
- Enregistrements de la session : 14445 ; net attendu > 0 : 21 ; simulés (eth_call de la vraie tx) : 0 (ok 0, échec 0) ; étiquettes ghost N+1 : 0/0 positives
- Décisions : {'REJECTED': 14445} ; motifs de rejet : {'below_safety_margin': 21, 'negative_expected_net': 14424, 'p_lower_below_threshold': 17, 'reliability_not_demonstrated': 4, 'stale_data': 9}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 56555438 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.001695 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0033 €) | — | 0.29 | 0.268 (n=1617) | REJECTED | below_safety_margin(5<33), p_lower_below_threshold(0.27<0.75) |
| 56555438 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.001695 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0033 €) | — | 0.29 | 0.268 (n=1617) | REJECTED | below_safety_margin(5<33), p_lower_below_threshold(0.27<0.75) |
| 56555438 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.052888 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0029 €) | — | 0.30 | 0.268 (n=1617) | REJECTED | below_safety_margin(1573120128124<10577649162355), p_lower_below_threshold(0.27<0.75) |
| 56555438 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.052888 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0029 €) | — | 0.30 | 0.268 (n=1617) | REJECTED | below_safety_margin(1573120128124<10577649162355), p_lower_below_threshold(0.27<0.75) |
| 56555438 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 121.694191 USDC | 0.009251 USDC | 0.000000 USDC | 0.006165 USDC | 0.003086 USDC (0.0028 €) | — | 0.25 | 0.268 (n=1617) | REJECTED | below_safety_margin(3086<24338), p_lower_below_threshold(0.27<0.75) |
| 56555438 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 121.694191 USDC | 0.009251 USDC | 0.000000 USDC | 0.006165 USDC | 0.003086 USDC (0.0028 €) | — | 0.25 | 0.268 (n=1617) | REJECTED | below_safety_margin(3086<24338), p_lower_below_threshold(0.27<0.75) |
| 56555351 | WETH→[uniswap_v2]→USDC→[pancakeswap_v3]→WETH | 0.029980 WETH | 0.000003 WETH | 0.000000 WETH | 0.000002 WETH | 0.000001 WETH (0.0019 €) | — | 0.34 | — (n=0) | REJECTED | below_safety_margin(1009039948270<5995965538256), stale_data(4350ms>4000.0), reliability_not_demonstrated |
| 56555352 | WETH→[uniswap_v2]→USDC→[pancakeswap_v3]→WETH | 0.029980 WETH | 0.000003 WETH | 0.000000 WETH | 0.000002 WETH | 0.000001 WETH (0.0019 €) | — | 0.34 | — (n=0) | REJECTED | below_safety_margin(1009039948270<5995965538256), stale_data(5564ms>4000.0), reliability_not_demonstrated |
| 56555351 | USDC→[pancakeswap_v3]→WETH→[uniswap_v2]→USDC | 60.497904 USDC | 0.006006 USDC | 0.000000 USDC | 0.003993 USDC | 0.002013 USDC (0.0019 €) | — | 0.33 | — (n=0) | REJECTED | below_safety_margin(2013<12099), stale_data(4355ms>4000.0), reliability_not_demonstrated |
| 56555352 | USDC→[pancakeswap_v3]→WETH→[uniswap_v2]→USDC | 60.497904 USDC | 0.006006 USDC | 0.000000 USDC | 0.003993 USDC | 0.002013 USDC (0.0019 €) | — | 0.33 | — (n=0) | REJECTED | below_safety_margin(2013<12099), stale_data(5569ms>4000.0), reliability_not_demonstrated |
| 56555351 | WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.038308 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0017 €) | — | 0.24 | 0.268 (n=1617) | REJECTED | below_safety_margin(937665082948<7661616714633), stale_data(4345ms>4000.0), p_lower_below_threshold(0.27<0.75) |
| 56555352 | WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.038308 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0017 €) | — | 0.24 | 0.268 (n=1617) | REJECTED | below_safety_margin(937665082948<7661616714633), stale_data(5559ms>4000.0), p_lower_below_threshold(0.27<0.75) |
| 56555351 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC | 75.696681 USDC | 0.008032 USDC | 0.000000 USDC | 0.006170 USDC | 0.001862 USDC (0.0017 €) | — | 0.25 | 0.268 (n=1617) | REJECTED | below_safety_margin(1862<15139), stale_data(4339ms>4000.0), p_lower_below_threshold(0.27<0.75) |
| 56555352 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC | 75.696681 USDC | 0.008032 USDC | 0.000000 USDC | 0.006170 USDC | 0.001862 USDC (0.0017 €) | — | 0.25 | 0.268 (n=1617) | REJECTED | below_safety_margin(1862<15139), stale_data(5553ms>4000.0), p_lower_below_threshold(0.27<0.75) |
| 56555352 | WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.036867 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0012 €) | — | 0.17 | 0.268 (n=1617) | REJECTED | below_safety_margin(645142552920<7373465584304), p_lower_below_threshold(0.27<0.75) |
| 56555353 | WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.036867 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0012 €) | — | 0.17 | 0.268 (n=1617) | REJECTED | below_safety_margin(645142552920<7373465584304), p_lower_below_threshold(0.27<0.75) |
| 56555352 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC | 72.754847 USDC | 0.007446 USDC | 0.000000 USDC | 0.006172 USDC | 0.001274 USDC (0.0012 €) | — | 0.18 | 0.268 (n=1617) | REJECTED | below_safety_margin(1274<14550), p_lower_below_threshold(0.27<0.75) |
| 56555353 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC | 72.754847 USDC | 0.007446 USDC | 0.000000 USDC | 0.006172 USDC | 0.001274 USDC (0.0012 €) | — | 0.18 | 0.268 (n=1617) | REJECTED | below_safety_margin(1274<14550), p_lower_below_threshold(0.27<0.75) |
| 56555351 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 32.961821 USDC | 0.006289 USDC | 0.000000 USDC | 0.006170 USDC | 0.000119 USDC (0.0001 €) | — | 0.04 | 0.160 (n=43) | REJECTED | below_safety_margin(119<6592), p_lower_below_threshold(0.16<0.75) |
| 56555352 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 32.961821 USDC | 0.006289 USDC | 0.000000 USDC | 0.006170 USDC | 0.000119 USDC (0.0001 €) | — | 0.04 | 0.160 (n=43) | REJECTED | below_safety_margin(119<6592), stale_data(5215ms>4000.0), p_lower_below_threshold(0.16<0.75) |
| 56555507 | WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.010845 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0000 €) | — | 0.00 | 0.268 (n=1617) | REJECTED | below_safety_margin(1936938193<2169073438088), p_lower_below_threshold(0.27<0.75) |

## Fiabilité et décision
- Observations ghost : 8415 ; taux observé 0.222 ; borne inférieure crédible (0.9) 0.216 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 21.6% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
