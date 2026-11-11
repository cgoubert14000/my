# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-11T08:59:52+00:00 ; durée 127.27 min ; blocs 55947872 → 55986007 (6201 vus)

## Connexion
- Requêtes RPC : 79523 ; erreurs : 0 ; latence p50/p95 : 144.9/1,546.6 ms
- Rafraîchissements d'état : 6201 ; âge des données au dernier bloc : 8.94 s ; changements de frais LP observés (pools à frais dynamiques) : 3164
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 5338 ; cycles déclenchés par événement : 2136 ; avance médiane sur le rafraîchissement multicall : 409 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,060.73 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 460 pools, 267 jetons, 16590 routes
- Par DEX : uniswap_v3 134, aerodrome_slipstream 98, aerodrome 187, pancakeswap_v3 27, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 161 (rejetés 2) → 566 jetons ; pools candidats 3638 (énumérés 282, par paires 0), mesurés 462, sous le plancher de 10000.0 $ : 2 → gardés 460 (max 1500) ; prix des hubs : {'USDC': 1.0, 'USDbC': 1.0, 'DAI': 1.0, 'WETH': 2057.512263, 'cbBTC': 73519.133148, 'AERO': 0.539928}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 134,266,409 | 2,060.725983 | 55986033 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,491,631 | 0.027925 | 55986033 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 8,591,193 | 0.027971 | 55986033 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 8,344,150 | 0.000014 | 55986033 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 7,086,062 | 2,056.271169 | 55986033 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 6,736,535 | 109.027570 | 55986033 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,343,037 | 0.027922 | 55986033 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 4,269,038 | 1.841864 | 55986033 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,087,706 | 2,056.513227 | 55986033 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,877,618 | 1.000003 | 55986033 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,059,153 | 42,466.855796 | 55986033 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 150 | 2,928,134 | 2,056.816210 | 55986033 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,215,984 | 0.027958 | 55986033 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 1,958,314 | 1,122,462.090019 | 55986033 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,683,774 | 0.000014 | 55986033 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | USDC/cbBTC | 412 | 1,651,145 | 0.000014 | 55986033 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | XDP/USDC | 100 | 1,606,821 | 0.016160 | 55986033 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,555,538 | 0.000000 | 55986033 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,510,611 | 0.006498 | 55986033 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,462,932 | 0.824397 | 55986033 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,458,001 | 1.373191 | 55986033 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,441,431 | 0.000014 | 55986033 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,420,567 | 419.945612 | 55986033 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v2 | WETH/USDC | 3000 | 1,272,857 | 2,061.193099 | 55986033 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| uniswap_v3 | WETH/AERO | 3000 | 1,266,142 | 3,790.150750 | 55986033 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,229,956 | 15,012.916707 | 55986033 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/USDC | 3000 | 1,158,794 | 2,062.389132 | 55986033 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome | USDC/SEND | 3000 | 1,060,987 | 86.321491 | 55986033 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,047,498 | 33,221,424.263322 | 55986033 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,015,746 | 2,056.698369 | 55986033 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome_slipstream | USDC/VELVET | 100 | 963,622 | 21.143971 | 55986033 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/BRETT | 10000 | 944,297 | 558,012.356380 | 55986033 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | WETH/VVV | 10000 | 932,572 | 108.480188 | 55986033 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome_slipstream | USDC/cbBTC | 332 | 912,797 | 0.000014 | 55986033 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 912,688 | 0.001474 | 55986033 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| uniswap_v3 | WETH/TOSHI | 10000 | 906,075 | 23,078,466.085712 | 55986033 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | WETH/MORPHO | 3000 | 882,429 | 1,023.344580 | 55986033 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/USDC | 10000 | 879,558 | 2,050.503253 | 55986033 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | DRB/WETH | 10000 | 878,171 | 0.000000 | 55986033 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | USDC/VVV | 3000 | 875,717 | 0.053005 | 55986033 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | USDC/NOCK | 3000 | 772,254 | 78.869999 | 55986033 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| pancakeswap_v3 | QUID/USDC | 100 | 768,444 | 0.052709 | 55986033 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 757,418 | 22.595558 | 55986033 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome | WETH/EDEL | 7000 | 747,492 | 115,870.226425 | 55986033 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | WETH/AERO | 10000 | 709,002 | 3,790.378227 | 55986033 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | WETH/wstETH | 3000 | 697,682 | 0.802938 | 55986033 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 675,586 | 4,407,432.512026 | 55986033 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 673,257 | 0.530584 | 55986033 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v3 | TIG/USDC | 10000 | 626,865 | 0.494663 | 55986033 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/NPC | 3000 | 594,078 | 152,397.166271 | 55986033 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 586,269 | 0.000007 | 55986033 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | VIRTUAL/WETH | 10000 | 581,630 | 0.000259 | 55986033 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/BRETT | 2120 | 579,936 | 559,334.345975 | 55986033 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | FLOCK/USDC | 3000 | 566,712 | 0.038430 | 55986033 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome_slipstream | WETH/MORPHO | 2727 | 493,401 | 1,023.707173 | 55986033 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| uniswap_v3 | USDC/MORPHO | 10000 | 462,740 | 0.496647 | 55986033 | `0x2043B296fFC6b2d3bf4A3F3167d2Afb3B0FBdbEE` |
| aerodrome_slipstream | USDC/USDT | 8 | 455,102 | 1.001020 | 55986033 | `0xa41Bc0AFfbA7Fd420d186b84899d7ab2aC57fcD1` |
| pancakeswap_v3 | ELSA/USDC | 100 | 453,153 | 0.064840 | 55986033 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| uniswap_v3 | WETH/uSOL | 3000 | 440,543 | 24.974962 | 55986033 | `0xab04A352D4EC8d0F1812A4E5EBe7807Fa67acD48` |
| aerodrome | cbBTC/EDGE | 7000 | 439,954 | 902,062.594339 | 55986033 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |

## Recherche d'opportunités
- Cycles : 8336 ; routes examinées : 138294240 ; candidats optimisés : 618414 ; net attendu > 0 : 451 ; dernier cycle 152.7 ms
- Rejets (moteur) : {'spread_below_threshold': 135167298, 'liquidity_below_min': 2490639, 'negative_expected_net': 617963, 'borrow_bound_too_small': 16141, 'cycle_budget_exhausted': 1748}
- Enregistrements de la session : 618414 ; net attendu > 0 : 451 ; simulés (eth_call de la vraie tx) : 18 (ok 10, échec 8) ; étiquettes ghost N+1 : 4/17 positives
- Décisions : {'REJECTED': 618414} ; motifs de rejet : {'below_safety_margin': 375, 'negative_expected_net': 617963, 'p_lower_below_threshold': 429, 'reliability_not_demonstrated': 22, 'simulation_failed': 8, 'stale_data': 18}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 55983017 | cbBTC→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC | 0.020036 cbBTC | 0.000007 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000007 cbBTC (0.4822 €) | — | 3.54 | 0.201 (n=1182) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 55983017 | WETH→[pancakeswap_v3]→cbBTC→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.719100 WETH | 0.000257 WETH | 0.000000 WETH | 0.000003 WETH | 0.000254 WETH (0.4818 €) | 0.000254 WETH | 3.53 | 0.201 (n=1182) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 55983017 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC→[uniswap_v3]→USDC | 1,549.178979 USDC | 0.528634 USDC | 0.000000 USDC | 0.006198 USDC | 0.522436 USDC (0.4806 €) | — | 3.37 | 0.201 (n=1182) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 55983017 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC | 0.015524 cbBTC | 0.000006 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000006 cbBTC (0.3790 €) | — | 3.59 | 0.201 (n=1182) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 55983017 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.581928 WETH | 0.000203 WETH | 0.000000 WETH | 0.000003 WETH | 0.000200 WETH (0.3789 €) | 0.000200 WETH | 3.43 | 0.201 (n=1182) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 55983017 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 1,207.822455 USDC | 0.417107 USDC | 0.000000 USDC | 0.006511 USDC | 0.410596 USDC (0.3777 €) | — | 3.40 | 0.201 (n=1182) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 55983017 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→WETH | 0.480295 WETH | 0.000183 WETH | 0.000000 WETH | 0.000003 WETH | 0.000180 WETH (0.3420 €) | 0.000180 WETH | 3.76 | 0.201 (n=1182) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 55983017 | cbBTC→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC | 0.013069 cbBTC | 0.000005 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000005 cbBTC (0.3416 €) | — | 3.85 | 0.201 (n=1182) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 55983017 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 973.694435 USDC | 0.376714 USDC | 0.000000 USDC | 0.006198 USDC | 0.370516 USDC (0.3409 €) | — | 3.81 | 0.201 (n=1182) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 55983017 | cbBTC→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC | 0.012868 cbBTC | 0.000005 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000005 cbBTC (0.3321 €) | — | 3.80 | 0.201 (n=1182) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 55983017 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→WETH | 0.461055 WETH | 0.000178 WETH | 0.000000 WETH | 0.000003 WETH | 0.000175 WETH (0.3319 €) | — | 3.80 | 0.201 (n=1182) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 55983017 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 952.619448 USDC | 0.365900 USDC | 0.000000 USDC | 0.006198 USDC | 0.359702 USDC (0.3309 €) | — | 3.78 | 0.201 (n=1182) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 55983017 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.570121 WETH | 0.000159 WETH | 0.000000 WETH | 0.000002 WETH | 0.000157 WETH (0.2981 €) | — | 2.76 | 0.081 (n=113) | REJECTED | p_lower_below_threshold(0.08<0.75) |
| 55983017 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 1,171.290177 USDC | 0.327917 USDC | 0.000000 USDC | 0.004631 USDC | 0.323286 USDC (0.2974 €) | — | 2.76 | 0.081 (n=113) | REJECTED | p_lower_below_threshold(0.08<0.75) |
| 55951267 | USDC→[pancakeswap_v3]→ICNT→[uniswap_v3]→USDC | 145.747655 USDC | 0.253186 USDC | 0.000000 USDC | 0.004616 USDC | 0.248570 USDC (0.2287 €) | — | 17.05 | 0.007 (n=113) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.01<0.75) |
| 55983017 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.485054 WETH | 0.000120 WETH | 0.000000 WETH | 0.000002 WETH | 0.000118 WETH (0.2229 €) | — | 2.42 | 0.100 (n=358) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 55983017 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 996.350752 USDC | 0.246700 USDC | 0.000000 USDC | 0.004944 USDC | 0.241756 USDC (0.2224 €) | — | 2.43 | 0.100 (n=358) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 55983017 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.354556 WETH | 0.000099 WETH | 0.000000 WETH | 0.000002 WETH | 0.000097 WETH (0.1840 €) | — | 2.74 | 0.100 (n=358) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 55983017 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 728.408585 USDC | 0.204441 USDC | 0.000000 USDC | 0.004944 USDC | 0.199497 USDC (0.1835 €) | — | 2.74 | 0.100 (n=358) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 55983017 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.232428 WETH | 0.000065 WETH | 0.000000 WETH | 0.000002 WETH | 0.000062 WETH (0.1181 €) | — | 2.68 | 0.081 (n=113) | REJECTED | p_lower_below_threshold(0.08<0.75) |
| 55983017 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 478.665558 USDC | 0.132987 USDC | 0.000000 USDC | 0.004944 USDC | 0.128043 USDC (0.1178 €) | — | 2.67 | 0.081 (n=113) | REJECTED | p_lower_below_threshold(0.08<0.75) |
| 55983017 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.128144 WETH | 0.000053 WETH | 0.000000 WETH | 0.000003 WETH | 0.000050 WETH (0.0946 €) | — | 3.90 | 0.201 (n=1182) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 55983017 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 275.188494 USDC | 0.108833 USDC | 0.000000 USDC | 0.006198 USDC | 0.102635 USDC (0.0944 €) | — | 3.73 | 0.201 (n=1182) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 55983017 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC | 0.003544 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0944 €) | — | 3.92 | 0.201 (n=1182) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 55983017 | WETH→[pancakeswap_v3]→cbBTC→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.226693 WETH | 0.000033 WETH | 0.000000 WETH | 0.000003 WETH | 0.000030 WETH (0.0572 €) | — | 1.33 | 0.262 (n=1558) | REJECTED | below_safety_margin(30150216924327<45338533255198), p_lower_below_threshold(0.26<0.75) |

## Fiabilité et décision
- Observations ghost : 8005 ; taux observé 0.211 ; borne inférieure crédible (0.9) 0.205 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 20.5% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
