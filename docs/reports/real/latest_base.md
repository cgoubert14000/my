# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-10T23:05:06+00:00 ; durée 204.8 min ; blocs 55746173 → 55807588 (2615 vus)

## Connexion
- Requêtes RPC : 98411 ; erreurs : 95 ; latence p50/p95 : 407.0/1,394.3 ms
- Rafraîchissements d'état : 2615 ; âge des données au dernier bloc : 4.91 s ; changements de frais LP observés (pools à frais dynamiques) : 4628
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 11569 ; cycles déclenchés par événement : 3135 ; avance médiane sur le rafraîchissement multicall : 642 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,048.71 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 461 pools, 269 jetons, 15520 routes
- Par DEX : uniswap_v3 132, aerodrome_slipstream 98, aerodrome 190, pancakeswap_v3 28, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 1
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 163 (rejetés 2) → 568 jetons ; pools candidats 3640 (énumérés 285, par paires 0), mesurés 463, sous le plancher de 10000.0 $ : 2 → gardés 461 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'DAI': 1.0, 'USDC': 1.0, 'WETH': 2041.615001, 'cbBTC': 73281.760168, 'AERO': 0.54062}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 133,610,675 | 2,048.711978 | 55807611 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,374,439 | 0.027789 | 55807611 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 8,540,794 | 0.027851 | 55807611 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 8,334,329 | 0.000014 | 55807611 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 7,039,505 | 2,043.437591 | 55807611 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 6,800,880 | 105.737028 | 55807611 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,317,938 | 0.027781 | 55807611 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 4,302,540 | 1.840537 | 55807611 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,878,258 | 0.999938 | 55807611 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| pancakeswap_v3 | WETH/USDC | 100 | 3,870,187 | 2,043.074730 | 55807611 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | WETH/KTA | 3000 | 3,049,424 | 42,241.363265 | 55807611 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 150 | 2,918,726 | 2,043.305217 | 55807611 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,269,173 | 0.027812 | 55807611 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 1,947,300 | 1,121,998.074522 | 55807611 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,682,585 | 0.000014 | 55807611 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | USDC/cbBTC | 472 | 1,619,577 | 0.000014 | 55807611 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | XDP/USDC | 100 | 1,617,613 | 0.016324 | 55807611 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,548,235 | 0.000000 | 55807611 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,529,949 | 0.006680 | 55807611 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,462,489 | 0.823771 | 55807611 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,434,937 | 1.411479 | 55807611 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,425,492 | 0.000014 | 55807611 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,416,923 | 414.887241 | 55807611 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v2 | WETH/USDC | 3000 | 1,269,107 | 2,048.336734 | 55807611 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| uniswap_v3 | WETH/AERO | 3000 | 1,263,208 | 3,765.272819 | 55807611 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,232,498 | 14,920.490649 | 55807611 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/USDC | 3000 | 1,156,023 | 2,049.032186 | 55807611 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome | USDC/SEND | 3000 | 1,064,057 | 85.824177 | 55807611 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,051,638 | 2,043.465233 | 55807611 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | WETH/doginme | 10000 | 1,038,676 | 33,463,807.671865 | 55807611 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome_slipstream | USDC/VELVET | 100 | 956,750 | 21.613406 | 55807611 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/VVV | 10000 | 946,223 | 106.489567 | 55807611 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/BRETT | 10000 | 939,795 | 556,995.335345 | 55807611 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome_slipstream | USDC/cbBTC | 344 | 917,024 | 0.000014 | 55807611 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 911,664 | 0.001473 | 55807611 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| uniswap_v3 | WETH/TOSHI | 10000 | 905,907 | 22,857,397.181832 | 55807611 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | WETH/MORPHO | 3000 | 882,913 | 1,013.002685 | 55807611 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | USDC/VVV | 3000 | 881,235 | 0.051702 | 55807611 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/USDC | 10000 | 878,153 | 2,042.470303 | 55807611 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | DRB/WETH | 10000 | 863,295 | 0.000000 | 55807611 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | USDC/NOCK | 3000 | 778,148 | 77.679855 | 55807611 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | USDC/SAPIEN | 4535 | 761,916 | 22.407583 | 55807611 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 760,643 | 0.051610 | 55807611 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/EDEL | 7000 | 748,707 | 114,151.549109 | 55807611 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | WETH/AERO | 10000 | 707,187 | 3,770.863155 | 55807611 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | WETH/wstETH | 3000 | 693,556 | 0.803072 | 55807611 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 654,324 | 0.527674 | 55807611 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 643,436 | 4,799,962.784482 | 55807611 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 629,331 | 0.498463 | 55807611 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/NPC | 3000 | 595,991 | 149,670.409190 | 55807611 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 587,692 | 0.000007 | 55807611 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | VIRTUAL/WETH | 10000 | 578,404 | 0.000259 | 55807611 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/BRETT | 2093 | 577,075 | 557,337.649624 | 55807611 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | FLOCK/USDC | 3000 | 556,697 | 0.037402 | 55807611 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 493,416 | 1,012.802133 | 55807611 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome | WETH/DRV | 3000 | 483,331 | 6,588.844626 | 55807611 | `0xaC4e562d7C6108f971321F14238E24AE2cC398ac` |
| pancakeswap_v3 | ELSA/USDC | 100 | 479,403 | 0.069689 | 55807611 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| uniswap_v3 | USDC/MORPHO | 10000 | 464,153 | 0.495049 | 55807611 | `0x2043B296fFC6b2d3bf4A3F3167d2Afb3B0FBdbEE` |
| aerodrome_slipstream | USDC/USDT | 8 | 455,045 | 1.001143 | 55807611 | `0xa41Bc0AFfbA7Fd420d186b84899d7ab2aC57fcD1` |
| uniswap_v3 | WETH/UNI | 10000 | 442,214 | 305.355956 | 55807611 | `0xAb365f161Dd501473a1ff0D2ef0dCE94E7398839` |

## Recherche d'opportunités
- Cycles : 5748 ; routes examinées : 89208960 ; candidats optimisés : 542422 ; net attendu > 0 : 1626 ; dernier cycle 352.9 ms
- Rejets (moteur) : {'spread_below_threshold': 87369743, 'liquidity_below_min': 1283717, 'negative_expected_net': 540796, 'borrow_bound_too_small': 9938, 'cycle_budget_exhausted': 1772, 'unquotable': 1368}
- Enregistrements de la session : 542422 ; net attendu > 0 : 1626 ; simulés (eth_call de la vraie tx) : 51 (ok 17, échec 34) ; étiquettes ghost N+1 : 20/50 positives
- Décisions : {'REJECTED': 542422} ; motifs de rejet : {'below_safety_margin': 1144, 'negative_expected_net': 540796, 'p_lower_below_threshold': 1606, 'price_impact': 14, 'reliability_not_demonstrated': 20, 'sim_below_estimate': 3, 'simulated_net_nonpositive': 2, 'simulation_failed': 34, 'stale_data': 816}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 55755672 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 1,575.554409 USDC | 0.620325 USDC | 0.000000 USDC | 0.004902 USDC | 0.615423 USDC (0.5662 €) | — | 3.91 | 0.079 (n=117) | REJECTED | p_lower_below_threshold(0.08<0.75) |
| 55755672 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.770860 WETH | 0.000303 WETH | 0.000000 WETH | 0.000002 WETH | 0.000301 WETH (0.5655 €) | — | 3.91 | 0.079 (n=117) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.08<0.75) |
| 55755672 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 1,399.868878 USDC | 0.581906 USDC | 0.000000 USDC | 0.004902 USDC | 0.577004 USDC (0.5308 €) | — | 4.12 | 0.073 (n=488) | REJECTED | p_lower_below_threshold(0.07<0.75) |
| 55755672 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.684636 WETH | 0.000285 WETH | 0.000000 WETH | 0.000002 WETH | 0.000282 WETH (0.5302 €) | — | 4.12 | 0.073 (n=488) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.07<0.75) |
| 55755672 | USDC→[uniswap_v3]→cbBTC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 1,557.503328 USDC | 0.531965 USDC | 0.000000 USDC | 0.006145 USDC | 0.525820 USDC (0.4838 €) | — | 3.38 | 0.309 (n=525) | REJECTED | stale_data(7512ms>4000.0), p_lower_below_threshold(0.31<0.75) |
| 55755672 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→cbBTC→[uniswap_v3]→WETH | 0.749527 WETH | 0.000260 WETH | 0.000000 WETH | 0.000003 WETH | 0.000257 WETH (0.4835 €) | — | 3.43 | 0.309 (n=525) | REJECTED | stale_data(7508ms>4000.0), simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.31<0.75) |
| 55755672 | cbBTC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→cbBTC | 0.020044 cbBTC | 0.000007 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000007 cbBTC (0.4832 €) | — | 3.57 | 0.309 (n=525) | REJECTED | stale_data(7504ms>4000.0), p_lower_below_threshold(0.31<0.75) |
| 55755672 | USDC→[uniswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 1,482.582053 USDC | 0.526246 USDC | 0.000000 USDC | 0.006145 USDC | 0.520101 USDC (0.4785 €) | — | 3.51 | 0.200 (n=1167) | REJECTED | stale_data(7489ms>4000.0), p_lower_below_threshold(0.20<0.75) |
| 55755672 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→cbBTC | 0.019681 cbBTC | 0.000007 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000007 cbBTC (0.4785 €) | — | 3.60 | 0.200 (n=1167) | REJECTED | stale_data(7480ms>4000.0), p_lower_below_threshold(0.20<0.75) |
| 55755672 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.703492 WETH | 0.000257 WETH | 0.000000 WETH | 0.000003 WETH | 0.000254 WETH (0.4780 €) | — | 3.62 | 0.200 (n=1167) | REJECTED | stale_data(7484ms>4000.0), p_lower_below_threshold(0.20<0.75) |
| 55750635 | WETH→[uniswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.522401 WETH | 0.000228 WETH | 0.000000 WETH | 0.000003 WETH | 0.000225 WETH (0.4229 €) | — | 4.31 | 0.201 (n=1164) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.20<0.75) |
| 55750635 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 1,094.278628 USDC | 0.465851 USDC | 0.000000 USDC | 0.006771 USDC | 0.459080 USDC (0.4224 €) | — | 4.20 | 0.201 (n=1164) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 55750635 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→cbBTC | 0.014660 cbBTC | 0.000006 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000006 cbBTC (0.4219 €) | — | 4.26 | 0.201 (n=1164) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 55750635 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 1,054.214208 USDC | 0.454811 USDC | 0.000000 USDC | 0.006461 USDC | 0.448350 USDC (0.4125 €) | — | 4.25 | 0.201 (n=1164) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 55750635 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC | 0.014214 cbBTC | 0.000006 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000006 cbBTC (0.4125 €) | — | 4.30 | 0.201 (n=1164) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 55750635 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.516486 WETH | 0.000223 WETH | 0.000000 WETH | 0.000003 WETH | 0.000220 WETH (0.4124 €) | — | 4.25 | 0.201 (n=1164) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.20<0.75) |
| 55755672 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 1,051.324572 USDC | 0.441903 USDC | 0.000000 USDC | 0.004902 USDC | 0.437001 USDC (0.4020 €) | — | 4.16 | 0.073 (n=488) | REJECTED | stale_data(7323ms>4000.0), p_lower_below_threshold(0.07<0.75) |
| 55755672 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.514637 WETH | 0.000216 WETH | 0.000000 WETH | 0.000002 WETH | 0.000214 WETH (0.4015 €) | — | 4.15 | 0.073 (n=488) | REJECTED | stale_data(7319ms>4000.0), p_lower_below_threshold(0.07<0.75) |
| 55750635 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.595022 WETH | 0.000215 WETH | 0.000000 WETH | 0.000002 WETH | 0.000213 WETH (0.3998 €) | — | 3.58 | 0.079 (n=116) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.08<0.75) |
| 55750635 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 1,211.693254 USDC | 0.439042 USDC | 0.000000 USDC | 0.004597 USDC | 0.434445 USDC (0.3997 €) | — | 3.59 | 0.079 (n=116) | REJECTED | p_lower_below_threshold(0.08<0.75) |
| 55755672 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 1,063.940446 USDC | 0.392701 USDC | 0.000000 USDC | 0.006765 USDC | 0.385936 USDC (0.3551 €) | — | 3.63 | 0.200 (n=1167) | REJECTED | stale_data(7434ms>4000.0), p_lower_below_threshold(0.20<0.75) |
| 55755672 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.513233 WETH | 0.000192 WETH | 0.000000 WETH | 0.000003 WETH | 0.000189 WETH (0.3547 €) | — | 3.68 | 0.200 (n=1167) | REJECTED | stale_data(7429ms>4000.0), p_lower_below_threshold(0.20<0.75) |
| 55755672 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.013585 cbBTC | 0.000005 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000005 cbBTC (0.3543 €) | — | 3.86 | 0.200 (n=1167) | REJECTED | stale_data(7424ms>4000.0), p_lower_below_threshold(0.20<0.75) |
| 55755672 | USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 1,080.506623 USDC | 0.389527 USDC | 0.000000 USDC | 0.006765 USDC | 0.382762 USDC (0.3521 €) | — | 3.54 | 0.200 (n=1167) | REJECTED | stale_data(7475ms>4000.0), p_lower_below_threshold(0.20<0.75) |
| 55755672 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH | 0.516213 WETH | 0.000191 WETH | 0.000000 WETH | 0.000003 WETH | 0.000187 WETH (0.3517 €) | — | 3.63 | 0.200 (n=1167) | REJECTED | stale_data(7470ms>4000.0), p_lower_below_threshold(0.20<0.75) |

## Fiabilité et décision
- Observations ghost : 7906 ; taux observé 0.209 ; borne inférieure crédible (0.9) 0.203 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 20.3% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
