# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-12T10:37:08+00:00 ; durée 315.83 min ; blocs 56352481 → 56447160 (13749 vus)

## Connexion
- Requêtes RPC : 188608 ; erreurs : 40 ; latence p50/p95 : 511.1/2,048.9 ms
- Rafraîchissements d'état : 13749 ; âge des données au dernier bloc : 13.02 s ; changements de frais LP observés (pools à frais dynamiques) : 6563
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 1475 ; cycles déclenchés par événement : 699 ; avance médiane sur le rafraîchissement multicall : 504 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,045.27 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 457 pools, 265 jetons, 15538 routes
- Par DEX : uniswap_v3 133, aerodrome_slipstream 98, aerodrome 186, pancakeswap_v3 27, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 1
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 159 (rejetés 2) → 564 jetons ; pools candidats 3626 (énumérés 282, par paires 0), mesurés 459, sous le plancher de 10000.0 $ : 2 → gardés 457 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDC': 1.0, 'USDbC': 1.0, 'WETH': 2045.219297, 'cbBTC': 73500.635487, 'AERO': 0.536237}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 133,797,874 | 2,045.271976 | 56447199 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,404,795 | 0.027874 | 56447199 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 8,673,759 | 0.027806 | 56447199 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 8,390,893 | 0.000014 | 56447199 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 7,070,036 | 2,049.456275 | 56447199 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 6,863,303 | 103.467723 | 56447199 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,250,306 | 0.027884 | 56447199 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 4,193,029 | 1.891304 | 56447199 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,188,941 | 2,050.267919 | 56447199 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,865,688 | 0.998657 | 56447199 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,040,652 | 42,342.817258 | 56447199 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 193 | 2,862,102 | 2,049.972157 | 56447199 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,194,136 | 0.027823 | 56447199 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 1,939,017 | 1,127,807.662643 | 56447199 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | XDP/USDC | 100 | 1,652,793 | 0.016863 | 56447199 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | USDC/cbBTC | 460 | 1,641,380 | 0.000014 | 56447199 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,586,847 | 0.000014 | 56447199 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,556,918 | 0.000000 | 56447199 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,525,033 | 0.000014 | 56447199 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,509,851 | 0.006578 | 56447199 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,461,872 | 0.830193 | 56447199 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,397,950 | 432.298824 | 56447199 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v2 | WETH/USDC | 3000 | 1,268,195 | 2,045.414517 | 56447199 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| uniswap_v3 | WETH/AERO | 3000 | 1,238,812 | 3,869.954851 | 56447199 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,206,594 | 15,508.237634 | 56447199 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/USDC | 3000 | 1,153,645 | 2,049.979661 | 56447199 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,124,694 | 2,049.455235 | 56447199 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,061,555 | 86.229165 | 56447199 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,046,779 | 1.389936 | 56447199 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | WETH/doginme | 10000 | 1,034,835 | 33,847,318.837345 | 56447199 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/VVV | 10000 | 1,018,786 | 104.215889 | 56447199 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome_slipstream | USDC/VELVET | 100 | 960,240 | 21.373282 | 56447199 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/BRETT | 10000 | 934,416 | 562,919.352532 | 56447199 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 910,567 | 0.001483 | 56447199 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| uniswap_v3 | USDC/VVV | 3000 | 903,556 | 0.050554 | 56447199 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/TOSHI | 10000 | 893,989 | 23,297,416.943306 | 56447199 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/cbBTC | 338 | 884,450 | 0.000014 | 56447199 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | WETH/USDC | 10000 | 876,485 | 2,054.853960 | 56447199 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 875,110 | 1,024.963856 | 56447199 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | DRB/WETH | 10000 | 859,147 | 0.000000 | 56447199 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | USDC/NOCK | 3000 | 776,029 | 78.104581 | 56447199 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 745,630 | 23.096993 | 56447199 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 745,611 | 0.049526 | 56447199 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/EDEL | 7000 | 738,745 | 116,846.318063 | 56447199 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | WETH/AERO | 10000 | 696,493 | 3,849.674049 | 56447199 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | WETH/wstETH | 3000 | 692,940 | 0.801801 | 56447199 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 664,239 | 0.524505 | 56447199 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 641,466 | 4,820,291.029909 | 56447199 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 616,133 | 0.477761 | 56447199 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/NPC | 3000 | 584,799 | 155,065.788556 | 56447199 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome | VIRTUAL/WETH | 10000 | 573,303 | 0.000257 | 56447199 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/BRETT | 2150 | 573,048 | 563,075.892379 | 56447199 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome_slipstream | AERO/cbBTC | 1025 | 566,458 | 0.000007 | 56447199 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v3 | FLOCK/USDC | 3000 | 559,883 | 0.037708 | 56447199 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 487,260 | 1,024.531802 | 56447199 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| pancakeswap_v3 | ELSA/USDC | 100 | 464,503 | 0.066878 | 56447199 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| aerodrome_slipstream | USDC/USDT | 8 | 453,315 | 1.000978 | 56447199 | `0xa41Bc0AFfbA7Fd420d186b84899d7ab2aC57fcD1` |
| uniswap_v3 | USDC/MORPHO | 10000 | 446,323 | 0.501968 | 56447199 | `0x2043B296fFC6b2d3bf4A3F3167d2Afb3B0FBdbEE` |
| uniswap_v3 | WETH/uSOL | 3000 | 438,836 | 24.793014 | 56447199 | `0xab04A352D4EC8d0F1812A4E5EBe7807Fa67acD48` |
| uniswap_v3 | WETH/UNI | 10000 | 432,669 | 332.166569 | 56447199 | `0xAb365f161Dd501473a1ff0D2ef0dCE94E7398839` |

## Recherche d'opportunités
- Cycles : 14447 ; routes examinées : 224477486 ; candidats optimisés : 1045210 ; net attendu > 0 : 233 ; dernier cycle 501.6 ms
- Rejets (moteur) : {'spread_below_threshold': 220749937, 'liquidity_below_min': 2666588, 'negative_expected_net': 1044977, 'borrow_bound_too_small': 14431, 'cycle_budget_exhausted': 1320}
- Enregistrements de la session : 1045210 ; net attendu > 0 : 233 ; simulés (eth_call de la vraie tx) : 30 (ok 30, échec 0) ; étiquettes ghost N+1 : 9/23 positives
- Décisions : {'REJECTED': 1045210} ; motifs de rejet : {'below_safety_margin': 165, 'negative_expected_net': 1044977, 'p_lower_below_threshold': 227, 'price_impact': 1, 'reliability_not_demonstrated': 6, 'sim_below_estimate': 7, 'simulated_net_nonpositive': 3, 'stale_data': 50}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 56441903 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC | 93.766930 USDC | 0.051965 USDC | 0.000000 USDC | 0.006150 USDC | 0.045815 USDC (0.0421 €) | 0.045815 USDC | 4.89 | 0.203 (n=1239) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 56441903 | cbBTC→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.001260 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0419 €) | — | 4.92 | 0.203 (n=1239) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 56441903 | cbBTC→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.001136 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0378 €) | — | 4.93 | 0.203 (n=1239) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 56441903 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC | 82.774819 USDC | 0.047391 USDC | 0.000000 USDC | 0.006460 USDC | 0.040931 USDC (0.0377 €) | 0.040931 USDC | 4.94 | 0.203 (n=1239) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 56441903 | cbBTC→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC→[uniswap_v3]→cbBTC | 0.001129 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0358 €) | — | 4.70 | 0.310 (n=571) | REJECTED | p_lower_below_threshold(0.31<0.75) |
| 56441903 | USDC→[uniswap_v3]→cbBTC→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC | 95.843428 USDC | 0.044961 USDC | 0.000000 USDC | 0.006150 USDC | 0.038811 USDC (0.0357 €) | 0.038811 USDC | 4.05 | 0.310 (n=571) | REJECTED | p_lower_below_threshold(0.31<0.75) |
| 56435379 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 145.668574 USDC | 0.042573 USDC | 0.000000 USDC | 0.004602 USDC | 0.037971 USDC (0.0349 €) | — | 2.61 | 0.055 (n=15) | REJECTED | reliability_not_demonstrated |
| 56435379 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.001768 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0344 €) | — | 2.88 | 0.055 (n=15) | REJECTED | reliability_not_demonstrated |
| 56441903 | USDC→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC | 65.899605 USDC | 0.042286 USDC | 0.000000 USDC | 0.006150 USDC | 0.036136 USDC (0.0332 €) | — | 5.48 | 0.310 (n=571) | REJECTED | p_lower_below_threshold(0.31<0.75) |
| 56441903 | cbBTC→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC→[aerodrome_slipstream]→cbBTC | 0.000815 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0331 €) | — | 6.01 | 0.310 (n=571) | REJECTED | p_lower_below_threshold(0.31<0.75) |
| 56435379 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 145.668574 USDC | 0.042118 USDC | 0.000000 USDC | 0.006159 USDC | 0.035959 USDC (0.0331 €) | — | 2.47 | 0.164 (n=42) | REJECTED | p_lower_below_threshold(0.16<0.75) |
| 56435379 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.001782 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0331 €) | — | 2.75 | 0.164 (n=42) | REJECTED | p_lower_below_threshold(0.16<0.75) |
| 56435379 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.070385 WETH | 0.000021 WETH | 0.000000 WETH | 0.000003 WETH | 0.000018 WETH (0.0329 €) | 0.000018 WETH | 2.49 | 0.164 (n=42) | REJECTED | p_lower_below_threshold(0.16<0.75) |
| 56441903 | cbBTC→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC→[aerodrome_slipstream]→cbBTC | 0.001126 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0324 €) | — | 4.26 | 0.310 (n=571) | REJECTED | p_lower_below_threshold(0.31<0.75) |
| 56441903 | USDC→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC | 85.080002 USDC | 0.041351 USDC | 0.000000 USDC | 0.006150 USDC | 0.035201 USDC (0.0324 €) | — | 4.14 | 0.310 (n=571) | REJECTED | p_lower_below_threshold(0.31<0.75) |
| 56435379 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.001574 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0250 €) | — | 2.35 | 0.268 (n=1587) | REJECTED | p_lower_below_threshold(0.27<0.75) |
| 56435379 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 130.024493 USDC | 0.032955 USDC | 0.000000 USDC | 0.006159 USDC | 0.026796 USDC (0.0247 €) | — | 2.06 | 0.268 (n=1587) | REJECTED | p_lower_below_threshold(0.27<0.75) |
| 56435379 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.063653 WETH | 0.000016 WETH | 0.000000 WETH | 0.000003 WETH | 0.000013 WETH (0.0246 €) | 0.000013 WETH | 2.06 | 0.268 (n=1587) | REJECTED | p_lower_below_threshold(0.27<0.75) |
| 56388390 | USDC→[uniswap_v3]→TIG→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 35.218273 USDC | 0.032458 USDC | 0.000000 USDC | 0.006143 USDC | 0.026315 USDC (0.0242 €) | — | 7.47 | 0.308 (n=567) | REJECTED | p_lower_below_threshold(0.31<0.75) |
| 56388390 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→TIG→[aerodrome_slipstream]→WETH | 0.017342 WETH | 0.000016 WETH | 0.000000 WETH | 0.000003 WETH | 0.000013 WETH (0.0242 €) | 0.000013 WETH | 7.41 | 0.308 (n=567) | REJECTED | p_lower_below_threshold(0.31<0.75) |
| 56388390 | USDC→[uniswap_v3]→TIG→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 35.404259 USDC | 0.032255 USDC | 0.000000 USDC | 0.006143 USDC | 0.026112 USDC (0.0240 €) | — | 7.38 | 0.203 (n=1238) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 56388390 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→TIG→[aerodrome_slipstream]→WETH | 0.017304 WETH | 0.000016 WETH | 0.000000 WETH | 0.000003 WETH | 0.000013 WETH (0.0240 €) | 0.000013 WETH | 7.37 | 0.203 (n=1238) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 56388390 | USDC→[uniswap_v3]→TIG→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→USDC | 34.633173 USDC | 0.031152 USDC | 0.000000 USDC | 0.006143 USDC | 0.025009 USDC (0.0230 €) | — | 7.22 | 0.308 (n=567) | REJECTED | p_lower_below_threshold(0.31<0.75) |
| 56388390 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→TIG→[aerodrome_slipstream]→WETH | 0.017066 WETH | 0.000015 WETH | 0.000000 WETH | 0.000003 WETH | 0.000012 WETH (0.0230 €) | 0.000012 WETH | 7.16 | 0.308 (n=567) | REJECTED | p_lower_below_threshold(0.31<0.75) |
| 56435379 | cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.001368 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0209 €) | — | 2.27 | 0.268 (n=1587) | REJECTED | p_lower_below_threshold(0.27<0.75) |

## Fiabilité et décision
- Observations ghost : 8263 ; taux observé 0.218 ; borne inférieure crédible (0.9) 0.212 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 21.2% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ✅ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
