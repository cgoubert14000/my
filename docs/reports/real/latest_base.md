# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-19T19:17:27+00:00 ; durée 119.3 min ; blocs 59591500 → 59627313 (4895 vus)

## Connexion
- Requêtes RPC : 57112 ; erreurs : 385 ; latence p50/p95 : 347.7/1,668.4 ms
- Rafraîchissements d'état : 4895 ; âge des données au dernier bloc : 8.59 s ; changements de frais LP observés (pools à frais dynamiques) : 5510
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 9399 ; cycles déclenchés par événement : 2547 ; avance médiane sur le rafraîchissement multicall : 263 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 1,775.22 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 428 pools, 248 jetons, 13064 routes
- Par DEX : uniswap_v3 129, aerodrome 172, aerodrome_slipstream 87, pancakeswap_v3 27, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 1
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 146 (rejetés 2) → 551 jetons ; pools candidats 3579 (énumérés 257, par paires 0), mesurés 430, sous le plancher de 10000.0 $ : 2 → gardés 428 (max 1500) ; prix des hubs : {'USDC': 1.0, 'DAI': 1.0, 'USDbC': 1.0, 'WETH': 1755.680432, 'cbBTC': 62293.409251, 'AERO': 0.417081}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 86,268,406 | 1,775.223509 | 59627338 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/USDC | 500 | 25,676,999 | 1,773.862007 | 59627338 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| uniswap_v3 | WETH/cbBTC | 500 | 21,377,842 | 0.028322 | 59627338 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 7,772,381 | 0.028253 | 59627338 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| aerodrome | WETH/VVV | 3000 | 6,819,364 | 78.696255 | 59627338 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | USDC/cbBTC | 500 | 5,956,649 | 0.000016 | 59627338 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,202,813 | 0.028321 | 59627338 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 3,605,935 | 2.367660 | 59627338 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,296,559 | 1.000000 | 59627338 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| pancakeswap_v3 | WETH/USDC | 100 | 3,292,800 | 1,773.190059 | 59627338 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | WETH/KTA | 3000 | 2,770,405 | 38,426.030612 | 59627338 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 138 | 2,325,407 | 1,773.064514 | 59627338 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,085,616 | 0.000016 | 59627338 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/cbBTC | 2545 | 1,731,471 | 0.028269 | 59627338 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 1,668,716 | 1,147,195.575609 | 59627338 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,457,928 | 0.844466 | 59627338 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | USDC/cbBTC | 460 | 1,446,921 | 0.000016 | 59627338 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,329,964 | 0.000000 | 59627338 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,269,535 | 0.006529 | 59627338 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,257,603 | 0.000016 | 59627338 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,142,513 | 13.362977 | 59627338 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | USDC/SEND | 3000 | 1,060,088 | 86.467991 | 59627338 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,059,886 | 447.441839 | 59627338 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | WETH/VVV | 10000 | 1,032,059 | 78.586106 | 59627338 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome | WETH/USDC | 3000 | 1,026,555 | 1,776.508554 | 59627338 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,023,829 | 15,832.645623 | 59627338 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | WETH/AERO | 3000 | 1,001,576 | 4,198.367739 | 59627338 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v2 | WETH/USDC | 3000 | 991,625 | 1,776.174418 | 59627338 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| uniswap_v3 | WETH/doginme | 10000 | 959,219 | 28,661,611.128378 | 59627338 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | USDC/VVV | 3000 | 930,706 | 0.044386 | 59627338 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | USDC/NOCK | 3000 | 861,506 | 57.645878 | 59627338 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/BRETT | 10000 | 830,665 | 523,890.949446 | 59627338 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | DRB/WETH | 10000 | 822,979 | 0.000000 | 59627338 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/TOSHI | 10000 | 805,625 | 22,203,974.752029 | 59627338 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 793,094 | 0.001542 | 59627338 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| uniswap_v3 | WETH/MORPHO | 3000 | 742,122 | 1,084.902335 | 59627338 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| pancakeswap_v3 | WETH/USDC | 500 | 736,192 | 1,773.895941 | 59627338 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | XDP/USDC | 100 | 730,747 | 0.014864 | 59627338 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | QUID/USDC | 100 | 722,299 | 0.046367 | 59627338 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome_slipstream | USDC/SAPIEN | 4610 | 716,926 | 24.470007 | 59627338 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v3 | WETH/USDC | 10000 | 697,904 | 1,771.711737 | 59627338 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/USDC | 100 | 603,261 | 1,772.989705 | 59627338 | `0xb4CB800910B228ED3d0834cF79D697127BBB00e5` |
| aerodrome | WETH/wstETH | 3000 | 602,560 | 0.798842 | 59627338 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | TIG/USDC | 10000 | 592,964 | 0.441730 | 59627338 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 559,437 | 4,790,469.487725 | 59627338 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome | WETH/AERO | 10000 | 547,879 | 4,190.759325 | 59627338 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | WETH/BRETT | 3706 | 517,430 | 525,348.699776 | 59627338 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome | USDC/MAI (stable) | 3000 | 509,175 | 1.386543 | 59627338 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | FLOCK/USDC | 3000 | 500,754 | 0.031899 | 59627338 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| uniswap_v2 | WETH/NPC | 3000 | 487,826 | 168,388.250376 | 59627338 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | USDC/USDT | 11 | 461,327 | 1.001432 | 59627338 | `0xa41Bc0AFfbA7Fd420d186b84899d7ab2aC57fcD1` |
| aerodrome_slipstream | AERO/cbBTC | 1025 | 447,121 | 0.000007 | 59627338 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | VIRTUAL/WETH | 10000 | 432,101 | 0.000239 | 59627338 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| pancakeswap_v3 | ELSA/USDC | 100 | 408,421 | 0.056999 | 59627338 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| aerodrome_slipstream | WETH/MORPHO | 3040 | 403,904 | 1,085.200454 | 59627338 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| uniswap_v3 | WETH/UNI | 10000 | 388,337 | 357.692790 | 59627338 | `0xAb365f161Dd501473a1ff0D2ef0dCE94E7398839` |
| uniswap_v3 | WETH/uSOL | 3000 | 388,200 | 24.104714 | 59627338 | `0xab04A352D4EC8d0F1812A4E5EBe7807Fa67acD48` |
| aerodrome | cbBTC/EDGE | 7000 | 387,051 | 847,206.835530 | 59627338 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| aerodrome_slipstream | WETH/VVV | 2718 | 374,162 | 78.739646 | 59627338 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | AWE/USDC | 3000 | 372,198 | 0.057604 | 59627338 | `0xcb7f520d18141E36956fE0b3A6Bc3D4F11245521` |

## Recherche d'opportunités
- Cycles : 7441 ; routes examinées : 97209224 ; candidats optimisés : 134540 ; net attendu > 0 : 51 ; dernier cycle 298.1 ms
- Rejets (moteur) : {'spread_below_threshold': 95264558, 'liquidity_below_min': 1234356, 'negative_expected_net': 134489, 'borrow_bound_too_small': 9820, 'cycle_budget_exhausted': 3021}
- Enregistrements de la session : 69631 ; net attendu > 0 : 51 ; simulés (eth_call de la vraie tx) : 0 (ok 0, échec 0) ; étiquettes ghost N+1 : 0/0 positives
- Décisions : {'REJECTED': 69631} ; motifs de rejet : {'below_safety_margin': 51, 'negative_expected_net': 69580, 'p_lower_below_threshold': 51, 'stale_data': 29}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 59591958 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.126331 WETH | 0.000013 WETH | 0.000000 WETH | 0.000002 WETH | 0.000011 WETH (0.0177 €) | — | 0.87 | 0.109 (n=377) | REJECTED | below_safety_margin(10948928198956<25266204118772), p_lower_below_threshold(0.11<0.75) |
| 59591958 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.126331 WETH | 0.000013 WETH | 0.000000 WETH | 0.000002 WETH | 0.000011 WETH (0.0177 €) | — | 0.87 | 0.109 (n=377) | REJECTED | below_safety_margin(10948928198956<25266204118772), p_lower_below_threshold(0.11<0.75) |
| 59591958 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 218.769810 USDC | 0.023215 USDC | 0.000000 USDC | 0.004050 USDC | 0.019165 USDC (0.0176 €) | — | 0.88 | 0.109 (n=377) | REJECTED | below_safety_margin(19165<43753), p_lower_below_threshold(0.11<0.75) |
| 59591958 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 218.769810 USDC | 0.023215 USDC | 0.000000 USDC | 0.004050 USDC | 0.019165 USDC (0.0176 €) | — | 0.88 | 0.109 (n=377) | REJECTED | below_safety_margin(19165<43753), p_lower_below_threshold(0.11<0.75) |
| 59591958 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 47.588538 USDC | 0.009311 USDC | 0.000000 USDC | 0.005408 USDC | 0.003903 USDC (0.0036 €) | — | 0.82 | 0.272 (n=1639) | REJECTED | below_safety_margin(3903<9517), p_lower_below_threshold(0.27<0.75) |
| 59591958 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 47.588538 USDC | 0.009311 USDC | 0.000000 USDC | 0.005408 USDC | 0.003903 USDC (0.0036 €) | — | 0.82 | 0.272 (n=1639) | REJECTED | below_safety_margin(3903<9517), p_lower_below_threshold(0.27<0.75) |
| 59591958 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.026982 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0035 €) | — | 0.80 | 0.272 (n=1639) | REJECTED | below_safety_margin(2148914236807<5396318220261), p_lower_below_threshold(0.27<0.75) |
| 59591958 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.026982 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0035 €) | — | 0.80 | 0.272 (n=1639) | REJECTED | below_safety_margin(2148914236807<5396318220261), p_lower_below_threshold(0.27<0.75) |
| 59591958 | cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.000624 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0034 €) | — | 0.96 | 0.272 (n=1639) | REJECTED | below_safety_margin(6<12), p_lower_below_threshold(0.27<0.75) |
| 59591958 | cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.000624 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0034 €) | — | 0.96 | 0.272 (n=1639) | REJECTED | below_safety_margin(6<12), p_lower_below_threshold(0.27<0.75) |
| 59592754 | USDC→[aerodrome]→WETH→[uniswap_v3]→USDC | 52.540659 USDC | 0.006096 USDC | 0.000000 USDC | 0.003827 USDC | 0.002269 USDC (0.0021 €) | — | 0.43 | 0.253 (n=31) | REJECTED | below_safety_margin(2269<10508), stale_data(33749ms>4000.0), p_lower_below_threshold(0.25<0.75) |
| 59592754 | WETH→[uniswap_v3]→USDC→[aerodrome]→WETH | 0.030242 WETH | 0.000003 WETH | 0.000000 WETH | 0.000002 WETH | 0.000001 WETH (0.0021 €) | — | 0.42 | 0.253 (n=31) | REJECTED | below_safety_margin(1280472426852<6048444384827), stale_data(33746ms>4000.0), p_lower_below_threshold(0.25<0.75) |
| 59592754 | USDC→[uniswap_v3]→SLC→[aerodrome]→WETH→[uniswap_v3]→USDC | 15.016684 USDC | 0.006500 USDC | 0.000000 USDC | 0.005190 USDC | 0.001310 USDC (0.0012 €) | — | 0.87 | 0.276 (n=243) | REJECTED | below_safety_margin(1310<3003), stale_data(33446ms>4000.0), p_lower_below_threshold(0.28<0.75) |
| 59592754 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→SLC→[aerodrome]→WETH | 0.008724 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0012 €) | — | 0.84 | 0.276 (n=243) | REJECTED | below_safety_margin(734416735291<1744840239615), stale_data(33442ms>4000.0), p_lower_below_threshold(0.28<0.75) |
| 59593875 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 7.721666 USDC | 0.006654 USDC | 0.000000 USDC | 0.005601 USDC | 0.001053 USDC (0.0010 €) | — | 1.36 | 0.353 (n=641) | REJECTED | below_safety_margin(1053<1544), p_lower_below_threshold(0.35<0.75) |
| 59593876 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 7.811663 USDC | 0.006644 USDC | 0.000000 USDC | 0.005602 USDC | 0.001042 USDC (0.0010 €) | — | 1.33 | 0.353 (n=641) | REJECTED | below_safety_margin(1042<1562), p_lower_below_threshold(0.35<0.75) |
| 59593877 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 7.710664 USDC | 0.006638 USDC | 0.000000 USDC | 0.005603 USDC | 0.001035 USDC (0.0010 €) | — | 1.34 | 0.353 (n=641) | REJECTED | below_safety_margin(1035<1542), p_lower_below_threshold(0.35<0.75) |
| 59593875 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.004412 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0010 €) | — | 1.32 | 0.353 (n=641) | REJECTED | below_safety_margin(584482381186<882329081164), p_lower_below_threshold(0.35<0.75) |
| 59593876 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.004392 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0009 €) | — | 1.32 | 0.353 (n=641) | REJECTED | below_safety_margin(578113540988<878312182130), p_lower_below_threshold(0.35<0.75) |
| 59593877 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.004392 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0009 €) | — | 1.31 | 0.353 (n=641) | REJECTED | below_safety_margin(574567064919<878312352930), p_lower_below_threshold(0.35<0.75) |
| 59592754 | USDC→[pancakeswap_v3]→USDT→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 16.253466 USDC | 0.006388 USDC | 0.000000 USDC | 0.005433 USDC | 0.000955 USDC (0.0009 €) | — | 0.59 | 0.272 (n=1639) | REJECTED | below_safety_margin(955<3250), stale_data(33469ms>4000.0), p_lower_below_threshold(0.27<0.75) |
| 59592754 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→USDT→[aerodrome_slipstream]→WETH | 0.009233 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0009 €) | — | 0.58 | 0.272 (n=1639) | REJECTED | below_safety_margin(532603464847<1846647301195), stale_data(33462ms>4000.0), p_lower_below_threshold(0.27<0.75) |
| 59593875 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 7.531660 USDC | 0.006373 USDC | 0.000000 USDC | 0.005601 USDC | 0.000772 USDC (0.0007 €) | — | 1.03 | 0.272 (n=1639) | REJECTED | below_safety_margin(772<1506), p_lower_below_threshold(0.27<0.75) |
| 59593876 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 7.531660 USDC | 0.006373 USDC | 0.000000 USDC | 0.005602 USDC | 0.000771 USDC (0.0007 €) | — | 1.02 | 0.272 (n=1639) | REJECTED | below_safety_margin(771<1506), p_lower_below_threshold(0.27<0.75) |
| 59593877 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 7.531660 USDC | 0.006372 USDC | 0.000000 USDC | 0.005603 USDC | 0.000769 USDC (0.0007 €) | — | 1.02 | 0.272 (n=1639) | REJECTED | below_safety_margin(769<1506), p_lower_below_threshold(0.27<0.75) |

## Fiabilité et décision
- Observations ghost : 8576 ; taux observé 0.227 ; borne inférieure crédible (0.9) 0.221 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 22.1% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
