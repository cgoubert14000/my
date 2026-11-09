# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-09T10:04:40+00:00 ; durée 6.06 min ; blocs 55139673 → 55141460 (267 vus)

## Connexion
- Requêtes RPC : 3752 ; erreurs : 0 ; latence p50/p95 : 408.2/1,684.4 ms
- Rafraîchissements d'état : 267 ; âge des données au dernier bloc : 13.42 s ; changements de frais LP observés (pools à frais dynamiques) : 163
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 303 ; cycles déclenchés par événement : 123 ; avance médiane sur le rafraîchissement multicall : 538 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,108.90 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 465 pools, 272 jetons, 17388 routes
- Par DEX : uniswap_v3 131, aerodrome_slipstream 99, aerodrome 193, pancakeswap_v3 28, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 167 (rejetés 2) → 572 jetons ; pools candidats 3672 (énumérés 289, par paires 0), mesurés 467, sous le plancher de 10000.0 $ : 2 → gardés 465 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDbC': 1.0, 'USDC': 1.0, 'WETH': 2109.380964, 'cbBTC': 74235.499826, 'AERO': 0.565393}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 138,255,571 | 2,108.036109 | 55141501 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,371,918 | 0.028385 | 55141501 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,249,816 | 0.000013 | 55141501 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 8,636,422 | 0.028432 | 55141501 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 7,397,195 | 2,101.807775 | 55141501 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,050,014 | 104.477682 | 55141501 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,231,189 | 0.001523 | 55141501 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,609,028 | 0.028376 | 55141501 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 4,559,371 | 1.770562 | 55141501 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,912,755 | 0.998733 | 55141501 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| pancakeswap_v3 | WETH/USDC | 100 | 3,861,866 | 2,102.130563 | 55141501 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | WETH/KTA | 3000 | 3,126,860 | 42,570.754849 | 55141501 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 150 | 3,006,010 | 2,102.120742 | 55141501 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,344,703 | 0.028442 | 55141501 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 1,982,133 | 1,147,475.453732 | 55141501 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 556 | 1,702,370 | 0.000013 | 55141501 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,644,999 | 0.000014 | 55141501 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,619,803 | 0.006933 | 55141501 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v3 | XDP/USDC | 100 | 1,570,567 | 0.015579 | 55141501 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,548,411 | 0.000000 | 55141501 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,476,122 | 1.418208 | 55141501 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,453,452 | 0.821691 | 55141501 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,447,964 | 429.214495 | 55141501 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,442,437 | 0.000013 | 55141501 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v3 | WETH/AERO | 3000 | 1,305,157 | 3,736.805221 | 55141501 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v2 | WETH/USDC | 3000 | 1,287,402 | 2,107.944054 | 55141501 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,234,550 | 15,119.273852 | 55141501 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/USDC | 3000 | 1,217,175 | 2,107.455358 | 55141501 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome | USDC/SEND | 3000 | 1,120,185 | 77.439002 | 55141501 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,093,259 | 2,102.809167 | 55141501 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | WETH/doginme | 10000 | 1,037,119 | 36,865,069.416824 | 55141501 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/VVV | 10000 | 1,004,639 | 104.886900 | 55141501 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome_slipstream | USDC/VELVET | 100 | 957,207 | 21.580649 | 55141501 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/BRETT | 10000 | 953,396 | 581,300.568066 | 55141501 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome_slipstream | USDC/cbBTC | 356 | 922,061 | 0.000013 | 55141501 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | WETH/TOSHI | 10000 | 915,298 | 23,566,542.905991 | 55141501 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome | USDC/NOCK | 3000 | 909,697 | 75.720707 | 55141501 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/USDC | 10000 | 908,805 | 2,104.880343 | 55141501 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 899,298 | 1,034.988630 | 55141501 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | DRB/WETH | 10000 | 898,144 | 0.000000 | 55141501 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | USDC/VVV | 3000 | 835,233 | 0.049670 | 55141501 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | WETH/EDEL | 7000 | 816,828 | 101,623.549494 | 55141501 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| pancakeswap_v3 | QUID/USDC | 100 | 763,890 | 0.052057 | 55141501 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome_slipstream | USDC/SAPIEN | 4525 | 760,324 | 22.457856 | 55141501 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome | WETH/AERO | 10000 | 738,088 | 3,721.601102 | 55141501 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | WETH/wstETH | 3000 | 713,843 | 0.803274 | 55141501 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 693,148 | 0.535277 | 55141501 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 647,724 | 5,017,721.904717 | 55141501 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 641,730 | 0.521652 | 55141501 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 616,303 | 0.000008 | 55141501 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v2 | WETH/NPC | 3000 | 614,027 | 149,222.050958 | 55141501 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome | VIRTUAL/WETH | 10000 | 588,489 | 0.000252 | 55141501 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/BRETT | 2123 | 580,803 | 576,707.132069 | 55141501 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | FLOCK/USDC | 3000 | 567,815 | 0.038570 | 55141501 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome | WETH/msETH (stable) | 500 | 529,517 | 2.378996 | 55141501 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 510,934 | 1,034.701624 | 55141501 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome | cbBTC/EDGE | 7000 | 506,114 | 913,662.011814 | 55141501 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| uniswap_v3 | USDC/USDT | 100 | 497,519 | 1.001238 | 55141501 | `0xD56da2B74bA826f19015E6B7Dd9Dae1903E85DA1` |
| pancakeswap_v3 | ELSA/USDC | 100 | 487,282 | 0.070897 | 55141501 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| aerodrome | WETH/DRV | 3000 | 478,190 | 7,132.606507 | 55141501 | `0xaC4e562d7C6108f971321F14238E24AE2cC398ac` |

## Recherche d'opportunités
- Cycles : 389 ; routes examinées : 6763932 ; candidats optimisés : 20780 ; net attendu > 0 : 20 ; dernier cycle 385.4 ms
- Rejets (moteur) : {'spread_below_threshold': 6680483, 'liquidity_below_min': 61891, 'negative_expected_net': 20760, 'borrow_bound_too_small': 778}
- Enregistrements de la session : 20780 ; net attendu > 0 : 20 ; simulés (eth_call de la vraie tx) : 0 (ok 0, échec 0) ; étiquettes ghost N+1 : 0/0 positives
- Décisions : {'REJECTED': 20780} ; motifs de rejet : {'below_safety_margin': 20, 'negative_expected_net': 20760, 'p_lower_below_threshold': 8, 'reliability_not_demonstrated': 12}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 55141426 | WETH→[uniswap_v2]→USDC→[pancakeswap_v3]→WETH | 0.036577 WETH | 0.000005 WETH | 0.000000 WETH | 0.000002 WETH | 0.000003 WETH (0.0052 €) | — | 0.74 | — (n=0) | REJECTED | below_safety_margin(2689045639212<7315474365551), reliability_not_demonstrated |
| 55141427 | WETH→[uniswap_v2]→USDC→[pancakeswap_v3]→WETH | 0.036577 WETH | 0.000005 WETH | 0.000000 WETH | 0.000002 WETH | 0.000003 WETH (0.0052 €) | — | 0.74 | — (n=0) | REJECTED | below_safety_margin(2689045639212<7315474365551), reliability_not_demonstrated |
| 55141426 | USDC→[pancakeswap_v3]→WETH→[uniswap_v2]→USDC | 76.357676 USDC | 0.009732 USDC | 0.000000 USDC | 0.004090 USDC | 0.005642 USDC (0.0052 €) | — | 0.74 | — (n=0) | REJECTED | below_safety_margin(5642<15271), reliability_not_demonstrated |
| 55141427 | USDC→[pancakeswap_v3]→WETH→[uniswap_v2]→USDC | 76.357676 USDC | 0.009732 USDC | 0.000000 USDC | 0.004090 USDC | 0.005642 USDC (0.0052 €) | — | 0.74 | — (n=0) | REJECTED | below_safety_margin(5642<15271), reliability_not_demonstrated |
| 55141426 | WETH→[uniswap_v2]→USDC→[aerodrome_slipstream]→WETH | 0.027051 WETH | 0.000003 WETH | 0.000000 WETH | 0.000002 WETH | 0.000001 WETH (0.0017 €) | — | 0.32 | 0.001 (n=7) | REJECTED | below_safety_margin(862811617866<5410138084453), reliability_not_demonstrated |
| 55141427 | WETH→[uniswap_v2]→USDC→[aerodrome_slipstream]→WETH | 0.027051 WETH | 0.000003 WETH | 0.000000 WETH | 0.000002 WETH | 0.000001 WETH (0.0017 €) | — | 0.32 | 0.001 (n=7) | REJECTED | below_safety_margin(862811617866<5410138084453), reliability_not_demonstrated |
| 55141426 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v2]→USDC | 56.675339 USDC | 0.005892 USDC | 0.000000 USDC | 0.004090 USDC | 0.001802 USDC (0.0017 €) | — | 0.32 | 0.001 (n=7) | REJECTED | below_safety_margin(1802<11335), reliability_not_demonstrated |
| 55141427 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v2]→USDC | 56.675339 USDC | 0.005892 USDC | 0.000000 USDC | 0.004090 USDC | 0.001802 USDC (0.0017 €) | — | 0.32 | 0.001 (n=7) | REJECTED | below_safety_margin(1802<11335), reliability_not_demonstrated |
| 55141426 | WETH→[uniswap_v2]→USDC→[uniswap_v3]→WETH | 0.024947 WETH | 0.000003 WETH | 0.000000 WETH | 0.000002 WETH | 0.000001 WETH (0.0014 €) | — | 0.28 | 0.001 (n=7) | REJECTED | below_safety_margin(697995164636<4989377215058), reliability_not_demonstrated |
| 55141427 | WETH→[uniswap_v2]→USDC→[uniswap_v3]→WETH | 0.024947 WETH | 0.000003 WETH | 0.000000 WETH | 0.000002 WETH | 0.000001 WETH (0.0014 €) | — | 0.28 | 0.001 (n=7) | REJECTED | below_safety_margin(697995164636<4989377215058), reliability_not_demonstrated |
| 55141426 | USDC→[uniswap_v3]→WETH→[uniswap_v2]→USDC | 52.435656 USDC | 0.005546 USDC | 0.000000 USDC | 0.004090 USDC | 0.001456 USDC (0.0013 €) | — | 0.28 | 0.001 (n=7) | REJECTED | below_safety_margin(1456<10487), reliability_not_demonstrated |
| 55141427 | USDC→[uniswap_v3]→WETH→[uniswap_v2]→USDC | 52.435656 USDC | 0.005546 USDC | 0.000000 USDC | 0.004090 USDC | 0.001456 USDC (0.0013 €) | — | 0.28 | 0.001 (n=7) | REJECTED | below_safety_margin(1456<10487), reliability_not_demonstrated |
| 55141426 | WETH→[pancakeswap_v3]→EURC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.018024 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0006 €) | — | 0.17 | 0.203 (n=1237) | REJECTED | below_safety_margin(315146978592<3604852191832), p_lower_below_threshold(0.20<0.75) |
| 55141427 | WETH→[pancakeswap_v3]→EURC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.018024 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0006 €) | — | 0.17 | 0.203 (n=1237) | REJECTED | below_safety_margin(315146978592<3604852191832), p_lower_below_threshold(0.20<0.75) |
| 55141426 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→EURC→[aerodrome_slipstream]→USDC | 37.707448 USDC | 0.006995 USDC | 0.000000 USDC | 0.006350 USDC | 0.000645 USDC (0.0006 €) | — | 0.17 | 0.203 (n=1237) | REJECTED | below_safety_margin(645<7541), p_lower_below_threshold(0.20<0.75) |
| 55141427 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→EURC→[aerodrome_slipstream]→USDC | 37.707448 USDC | 0.006995 USDC | 0.000000 USDC | 0.006350 USDC | 0.000645 USDC (0.0006 €) | — | 0.17 | 0.203 (n=1237) | REJECTED | below_safety_margin(645<7541), p_lower_below_threshold(0.20<0.75) |
| 55141426 | WETH→[pancakeswap_v3]→EURC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.018077 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0005 €) | — | 0.16 | 0.203 (n=1237) | REJECTED | below_safety_margin(280719098793<3615369370916), p_lower_below_threshold(0.20<0.75) |
| 55141427 | WETH→[pancakeswap_v3]→EURC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.018077 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0005 €) | — | 0.16 | 0.203 (n=1237) | REJECTED | below_safety_margin(280719098793<3615369370916), p_lower_below_threshold(0.20<0.75) |
| 55141426 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→EURC→[aerodrome_slipstream]→USDC | 37.184513 USDC | 0.006921 USDC | 0.000000 USDC | 0.006350 USDC | 0.000571 USDC (0.0005 €) | — | 0.15 | 0.203 (n=1237) | REJECTED | below_safety_margin(571<7436), p_lower_below_threshold(0.20<0.75) |
| 55141427 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→EURC→[aerodrome_slipstream]→USDC | 37.184513 USDC | 0.006921 USDC | 0.000000 USDC | 0.006350 USDC | 0.000571 USDC (0.0005 €) | — | 0.15 | 0.203 (n=1237) | REJECTED | below_safety_margin(571<7436), p_lower_below_threshold(0.20<0.75) |

## Fiabilité et décision
- Observations ghost : 6740 ; taux observé 0.177 ; borne inférieure crédible (0.9) 0.171 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 17.1% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
