# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-11T10:06:43+00:00 ; durée 194.13 min ; blocs 55947872 → 56006050 (9287 vus)

## Connexion
- Requêtes RPC : 120330 ; erreurs : 55 ; latence p50/p95 : 146.8/1,557.2 ms
- Rafraîchissements d'état : 9287 ; âge des données au dernier bloc : 8.85 s ; changements de frais LP observés (pools à frais dynamiques) : 4822
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 8119 ; cycles déclenchés par événement : 3263 ; avance médiane sur le rafraîchissement multicall : 539 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,052.04 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 460 pools, 267 jetons, 16590 routes
- Par DEX : uniswap_v3 134, aerodrome_slipstream 98, aerodrome 187, pancakeswap_v3 27, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 161 (rejetés 2) → 566 jetons ; pools candidats 3638 (énumérés 282, par paires 0), mesurés 462, sous le plancher de 10000.0 $ : 2 → gardés 460 (max 1500) ; prix des hubs : {'USDC': 1.0, 'USDbC': 1.0, 'DAI': 1.0, 'WETH': 2057.512263, 'cbBTC': 73519.133148, 'AERO': 0.539928}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 133,789,909 | 2,052.040179 | 56006076 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,431,439 | 0.027873 | 56006076 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 8,557,132 | 0.027925 | 56006076 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 8,399,954 | 0.000014 | 56006076 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 7,070,501 | 2,053.687775 | 56006076 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 6,728,841 | 108.357801 | 56006076 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,318,513 | 0.027866 | 56006076 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 4,279,236 | 1.833095 | 56006076 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,046,224 | 2,054.147997 | 56006076 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,868,451 | 1.000003 | 56006076 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,047,912 | 42,420.789008 | 56006076 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 150 | 2,918,769 | 2,054.146634 | 56006076 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,207,251 | 0.027908 | 56006076 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 1,950,060 | 1,122,462.090019 | 56006076 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 400 | 1,648,265 | 0.000014 | 56006076 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | XDP/USDC | 100 | 1,607,436 | 0.016170 | 56006076 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,583,775 | 0.000014 | 56006076 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,548,980 | 0.000000 | 56006076 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,500,506 | 0.006478 | 56006076 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,464,066 | 0.825656 | 56006076 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,458,001 | 1.373191 | 56006076 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,439,287 | 0.000014 | 56006076 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,415,036 | 419.485026 | 56006076 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v2 | WETH/USDC | 3000 | 1,270,176 | 2,052.242242 | 56006076 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| uniswap_v3 | WETH/AERO | 3000 | 1,268,050 | 3,767.799051 | 56006076 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,226,655 | 15,067.753075 | 56006076 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/USDC | 3000 | 1,156,350 | 2,054.089314 | 56006076 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,106,928 | 2,053.842618 | 56006076 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,060,987 | 86.321491 | 56006076 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,043,083 | 33,221,424.263322 | 56006076 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome_slipstream | USDC/VELVET | 100 | 963,879 | 21.126812 | 56006076 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/BRETT | 10000 | 940,316 | 558,014.182091 | 56006076 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | WETH/VVV | 10000 | 932,835 | 108.480071 | 56006076 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 913,168 | 0.001482 | 56006076 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 334 | 910,795 | 0.000014 | 56006076 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | WETH/TOSHI | 10000 | 902,131 | 23,083,911.649235 | 56006076 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | WETH/MORPHO | 3000 | 879,186 | 1,022.315208 | 56006076 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/USDC | 10000 | 877,935 | 2,050.503253 | 56006076 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | USDC/VVV | 3000 | 877,254 | 0.052763 | 56006076 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | DRB/WETH | 10000 | 873,836 | 0.000000 | 56006076 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | USDC/NOCK | 3000 | 768,668 | 79.607657 | 56006076 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| pancakeswap_v3 | QUID/USDC | 100 | 759,814 | 0.051490 | 56006076 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 756,880 | 22.617986 | 56006076 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome | WETH/EDEL | 7000 | 747,166 | 114,995.820387 | 56006076 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | WETH/AERO | 10000 | 708,754 | 3,790.378227 | 56006076 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | WETH/wstETH | 3000 | 694,741 | 0.802938 | 56006076 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 670,847 | 0.530721 | 56006076 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 668,462 | 4,464,543.047012 | 56006076 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 626,299 | 0.493795 | 56006076 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/NPC | 3000 | 591,807 | 152,277.330486 | 56006076 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 587,766 | 0.000007 | 56006076 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | VIRTUAL/WETH | 10000 | 579,178 | 0.000259 | 56006076 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 577,494 | 558,504.717450 | 56006076 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | FLOCK/USDC | 3000 | 559,197 | 0.037650 | 56006076 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome_slipstream | WETH/MORPHO | 2727 | 491,618 | 1,022.048830 | 56006076 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| uniswap_v3 | USDC/MORPHO | 10000 | 461,674 | 0.496647 | 56006076 | `0x2043B296fFC6b2d3bf4A3F3167d2Afb3B0FBdbEE` |
| aerodrome_slipstream | USDC/USDT | 8 | 454,296 | 1.000960 | 56006076 | `0xa41Bc0AFfbA7Fd420d186b84899d7ab2aC57fcD1` |
| pancakeswap_v3 | ELSA/USDC | 100 | 453,861 | 0.064967 | 56006076 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| uniswap_v3 | WETH/uSOL | 3000 | 440,013 | 24.828549 | 56006076 | `0xab04A352D4EC8d0F1812A4E5EBe7807Fa67acD48` |
| aerodrome | cbBTC/EDGE | 7000 | 437,393 | 909,264.096662 | 56006076 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |

## Recherche d'opportunités
- Cycles : 12549 ; routes examinées : 208187910 ; candidats optimisés : 961772 ; net attendu > 0 : 860 ; dernier cycle 324.2 ms
- Rejets (moteur) : {'spread_below_threshold': 203451921, 'liquidity_below_min': 3747293, 'negative_expected_net': 960912, 'borrow_bound_too_small': 24565, 'cycle_budget_exhausted': 2359}
- Enregistrements de la session : 961772 ; net attendu > 0 : 860 ; simulés (eth_call de la vraie tx) : 25 (ok 13, échec 12) ; étiquettes ghost N+1 : 5/22 positives
- Décisions : {'REJECTED': 961772} ; motifs de rejet : {'below_safety_margin': 769, 'negative_expected_net': 960912, 'p_lower_below_threshold': 836, 'reliability_not_demonstrated': 24, 'simulation_failed': 12, 'stale_data': 147}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 56001114 | USDC→[aerodrome]→OWB→[uniswap_v3]→USDC | 137.998270 USDC | 4.819843 USDC | 0.000000 USDC | 0.004326 USDC | 4.815517 USDC (4.4303 €) | — | 348.95 | 0.000 (n=21) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
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

## Fiabilité et décision
- Observations ghost : 8010 ; taux observé 0.211 ; borne inférieure crédible (0.9) 0.205 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 20.5% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
