# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-10T19:58:38+00:00 ; durée 18.33 min ; blocs 55746173 → 55751705 (311 vus)

## Connexion
- Requêtes RPC : 8566 ; erreurs : 0 ; latence p50/p95 : 581.4/1,602.9 ms
- Rafraîchissements d'état : 312 ; âge des données au dernier bloc : 7.0 s ; changements de frais LP observés (pools à frais dynamiques) : 489
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 4202 ; cycles déclenchés par événement : 1262 ; avance médiane sur le rafraîchissement multicall : 591 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,041.62 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 461 pools, 269 jetons, 15520 routes
- Par DEX : uniswap_v3 132, aerodrome_slipstream 98, aerodrome 190, pancakeswap_v3 28, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 1
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 163 (rejetés 2) → 568 jetons ; pools candidats 3640 (énumérés 285, par paires 0), mesurés 463, sous le plancher de 10000.0 $ : 2 → gardés 461 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'DAI': 1.0, 'USDC': 1.0, 'WETH': 2041.615001, 'cbBTC': 73281.760168, 'AERO': 0.54062}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 133,123,247 | 2,041.615032 | 55751673 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,215,859 | 0.027833 | 55751673 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 8,523,009 | 0.027774 | 55751673 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 8,286,348 | 0.000014 | 55751704 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 7,075,045 | 2,042.672654 | 55751673 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 6,750,691 | 106.793398 | 55751673 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| aerodrome | USDC/AERO | 3000 | 4,302,578 | 1.842095 | 55751673 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,294,804 | 0.027838 | 55751700 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,858,651 | 0.999947 | 55751673 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| pancakeswap_v3 | WETH/USDC | 100 | 3,854,140 | 2,043.764682 | 55751677 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | WETH/KTA | 3000 | 3,000,502 | 43,328.623020 | 55751673 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 150 | 2,914,467 | 2,043.764541 | 55751683 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,250,727 | 0.027787 | 55751673 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 1,940,733 | 1,121,791.087457 | 55751673 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,673,187 | 0.000014 | 55751705 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | USDC/cbBTC | 508 | 1,617,217 | 0.000014 | 55751678 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | XDP/USDC | 100 | 1,609,354 | 0.016201 | 55751704 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,544,987 | 0.000000 | 55751673 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,524,209 | 0.006677 | 55751673 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,463,342 | 0.823606 | 55751673 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,434,937 | 1.411479 | 55751673 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,408,933 | 418.108514 | 55751673 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,408,276 | 0.000014 | 55751673 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v2 | WETH/USDC | 3000 | 1,266,896 | 2,042.852672 | 55751673 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| uniswap_v3 | WETH/AERO | 3000 | 1,260,912 | 3,767.604267 | 55751673 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,223,001 | 15,034.481941 | 55751673 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/USDC | 3000 | 1,154,019 | 2,045.547747 | 55751673 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome | USDC/SEND | 3000 | 1,064,190 | 85.802599 | 55751673 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,048,736 | 2,042.608674 | 55751673 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | WETH/doginme | 10000 | 1,024,202 | 34,812,490.424314 | 55751673 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome_slipstream | USDC/VELVET | 100 | 956,152 | 21.655152 | 55751683 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/BRETT | 10000 | 937,373 | 555,558.745889 | 55751673 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome_slipstream | USDC/cbBTC | 352 | 912,598 | 0.000014 | 55751704 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | WETH/VVV | 10000 | 910,014 | 106.527491 | 55751673 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 908,519 | 0.001478 | 55751673 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| uniswap_v3 | WETH/TOSHI | 10000 | 904,250 | 22,857,397.181832 | 55751673 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | WETH/MORPHO | 3000 | 881,268 | 1,004.230901 | 55751673 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/USDC | 10000 | 876,712 | 2,026.985532 | 55751673 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | USDC/VVV | 3000 | 871,646 | 0.052255 | 55751673 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | DRB/WETH | 10000 | 863,594 | 0.000000 | 55751673 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | USDC/NOCK | 3000 | 771,403 | 79.044204 | 55751673 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 761,241 | 22.434834 | 55751673 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 759,107 | 0.051395 | 55751673 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/EDEL | 7000 | 748,511 | 113,421.506950 | 55751673 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | WETH/AERO | 10000 | 711,787 | 3,770.863155 | 55751673 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | WETH/wstETH | 3000 | 691,148 | 0.803085 | 55751673 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 650,383 | 0.525728 | 55751673 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 643,129 | 4,771,278.746561 | 55751673 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 627,294 | 0.495441 | 55751673 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 586,379 | 0.000007 | 55751673 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | VIRTUAL/WETH | 10000 | 576,531 | 0.000259 | 55751673 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/BRETT | 2099 | 575,844 | 558,102.218823 | 55751673 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v2 | WETH/NPC | 3000 | 569,486 | 162,758.481862 | 55751673 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| uniswap_v3 | FLOCK/USDC | 3000 | 554,157 | 0.037143 | 55751673 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 495,747 | 1,004.514167 | 55751673 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome | WETH/DRV | 3000 | 480,065 | 6,632.603514 | 55751673 | `0xaC4e562d7C6108f971321F14238E24AE2cC398ac` |
| pancakeswap_v3 | ELSA/USDC | 100 | 475,226 | 0.068906 | 55751673 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| uniswap_v3 | USDC/MORPHO | 10000 | 465,899 | 0.495575 | 55751673 | `0x2043B296fFC6b2d3bf4A3F3167d2Afb3B0FBdbEE` |
| aerodrome_slipstream | USDC/USDT | 8 | 455,023 | 1.001121 | 55751686 | `0xa41Bc0AFfbA7Fd420d186b84899d7ab2aC57fcD1` |
| uniswap_v3 | WETH/UNI | 10000 | 442,585 | 303.301208 | 55751673 | `0xAb365f161Dd501473a1ff0D2ef0dCE94E7398839` |

## Recherche d'opportunités
- Cycles : 1573 ; routes examinées : 24412960 ; candidats optimisés : 155237 ; net attendu > 0 : 595 ; dernier cycle 191.3 ms
- Rejets (moteur) : {'spread_below_threshold': 23874933, 'liquidity_below_min': 379591, 'negative_expected_net': 154642, 'borrow_bound_too_small': 3146, 'cycle_budget_exhausted': 53}
- Enregistrements de la session : 155237 ; net attendu > 0 : 595 ; simulés (eth_call de la vraie tx) : 11 (ok 0, échec 11) ; étiquettes ghost N+1 : 2/11 positives
- Décisions : {'REJECTED': 155237} ; motifs de rejet : {'below_safety_margin': 435, 'negative_expected_net': 154642, 'p_lower_below_threshold': 591, 'reliability_not_demonstrated': 4, 'simulation_failed': 11, 'stale_data': 255}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 55750635 | WETH→[uniswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.522401 WETH | 0.000228 WETH | 0.000000 WETH | 0.000003 WETH | 0.000225 WETH (0.4229 €) | — | 4.31 | 0.201 (n=1164) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.20<0.75) |
| 55750635 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 1,094.278628 USDC | 0.465851 USDC | 0.000000 USDC | 0.006771 USDC | 0.459080 USDC (0.4224 €) | — | 4.20 | 0.201 (n=1164) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 55750635 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→cbBTC | 0.014660 cbBTC | 0.000006 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000006 cbBTC (0.4219 €) | — | 4.26 | 0.201 (n=1164) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 55750635 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 1,054.214208 USDC | 0.454811 USDC | 0.000000 USDC | 0.006461 USDC | 0.448350 USDC (0.4125 €) | — | 4.25 | 0.201 (n=1164) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 55750635 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC | 0.014214 cbBTC | 0.000006 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000006 cbBTC (0.4125 €) | — | 4.30 | 0.201 (n=1164) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 55750635 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.516486 WETH | 0.000223 WETH | 0.000000 WETH | 0.000003 WETH | 0.000220 WETH (0.4124 €) | — | 4.25 | 0.201 (n=1164) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.20<0.75) |
| 55750635 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.595022 WETH | 0.000215 WETH | 0.000000 WETH | 0.000002 WETH | 0.000213 WETH (0.3998 €) | — | 3.58 | 0.079 (n=116) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.08<0.75) |
| 55750635 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 1,211.693254 USDC | 0.439042 USDC | 0.000000 USDC | 0.004597 USDC | 0.434445 USDC (0.3997 €) | — | 3.59 | 0.079 (n=116) | REJECTED | p_lower_below_threshold(0.08<0.75) |
| 55750635 | WETH→[uniswap_v3]→cbBTC→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.583894 WETH | 0.000188 WETH | 0.000000 WETH | 0.000003 WETH | 0.000185 WETH (0.3479 €) | — | 3.17 | 0.309 (n=525) | REJECTED | p_lower_below_threshold(0.31<0.75) |
| 55750635 | cbBTC→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→cbBTC | 0.015456 cbBTC | 0.000005 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000005 cbBTC (0.3477 €) | — | 3.33 | 0.309 (n=525) | REJECTED | p_lower_below_threshold(0.31<0.75) |
| 55750635 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→cbBTC→[uniswap_v3]→USDC | 1,148.391068 USDC | 0.383913 USDC | 0.000000 USDC | 0.006151 USDC | 0.377762 USDC (0.3475 €) | — | 3.29 | 0.309 (n=525) | REJECTED | p_lower_below_threshold(0.31<0.75) |
| 55750635 | WETH→[pancakeswap_v3]→cbBTC→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.557229 WETH | 0.000181 WETH | 0.000000 WETH | 0.000003 WETH | 0.000178 WETH (0.3351 €) | — | 3.20 | 0.201 (n=1164) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 55750635 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC→[uniswap_v3]→USDC | 1,104.801737 USDC | 0.370365 USDC | 0.000000 USDC | 0.006151 USDC | 0.364214 USDC (0.3351 €) | — | 3.30 | 0.201 (n=1164) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 55750635 | cbBTC→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC | 0.014907 cbBTC | 0.000005 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000005 cbBTC (0.3348 €) | — | 3.33 | 0.201 (n=1164) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 55750635 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.505567 WETH | 0.000180 WETH | 0.000000 WETH | 0.000002 WETH | 0.000178 WETH (0.3341 €) | — | 3.52 | 0.073 (n=488) | REJECTED | p_lower_below_threshold(0.07<0.75) |
| 55750635 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 1,031.863129 USDC | 0.367990 USDC | 0.000000 USDC | 0.004907 USDC | 0.363083 USDC (0.3340 €) | — | 3.52 | 0.073 (n=488) | REJECTED | p_lower_below_threshold(0.07<0.75) |
| 55750635 | WETH→[uniswap_v3]→cbBTC→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→WETH | 0.403221 WETH | 0.000157 WETH | 0.000000 WETH | 0.000003 WETH | 0.000154 WETH (0.2886 €) | — | 3.81 | 0.309 (n=525) | REJECTED | p_lower_below_threshold(0.31<0.75) |
| 55750635 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 818.748652 USDC | 0.319566 USDC | 0.000000 USDC | 0.006151 USDC | 0.313415 USDC (0.2883 €) | — | 3.83 | 0.309 (n=525) | REJECTED | p_lower_below_threshold(0.31<0.75) |
| 55750635 | cbBTC→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→cbBTC | 0.011099 cbBTC | 0.000004 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000004 cbBTC (0.2883 €) | — | 3.85 | 0.309 (n=525) | REJECTED | p_lower_below_threshold(0.31<0.75) |
| 55750635 | cbBTC→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC | 0.010604 cbBTC | 0.000004 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000004 cbBTC (0.2835 €) | — | 3.96 | 0.201 (n=1164) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 55750635 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→WETH | 0.402288 WETH | 0.000154 WETH | 0.000000 WETH | 0.000003 WETH | 0.000151 WETH (0.2835 €) | — | 3.75 | 0.201 (n=1164) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 55750635 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 817.228476 USDC | 0.314150 USDC | 0.000000 USDC | 0.006151 USDC | 0.307999 USDC (0.2834 €) | — | 3.77 | 0.201 (n=1164) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 55750635 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.375220 WETH | 0.000129 WETH | 0.000000 WETH | 0.000002 WETH | 0.000127 WETH (0.2380 €) | — | 3.38 | 0.073 (n=488) | REJECTED | p_lower_below_threshold(0.07<0.75) |
| 55750635 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 764.992790 USDC | 0.263211 USDC | 0.000000 USDC | 0.004597 USDC | 0.258614 USDC (0.2379 €) | — | 3.38 | 0.073 (n=488) | REJECTED | p_lower_below_threshold(0.07<0.75) |
| 55750458 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC→[uniswap_v3]→USDC | 942.459273 USDC | 0.264349 USDC | 0.000000 USDC | 0.006154 USDC | 0.258195 USDC (0.2375 €) | — | 2.74 | 0.253 (n=1516) | REJECTED | p_lower_below_threshold(0.25<0.75) |

## Fiabilité et décision
- Observations ghost : 7867 ; taux observé 0.208 ; borne inférieure crédible (0.9) 0.202 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 20.2% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
