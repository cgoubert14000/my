# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-20T00:22:56+00:00 ; durée 85.33 min ; blocs 59693368 → 59718981 (4187 vus)

## Connexion
- Requêtes RPC : 51942 ; erreurs : 0 ; latence p50/p95 : 442.0/1,366.0 ms
- Rafraîchissements d'état : 4187 ; âge des données au dernier bloc : 5.45 s ; changements de frais LP observés (pools à frais dynamiques) : 2916
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 6357 ; cycles déclenchés par événement : 2077 ; avance médiane sur le rafraîchissement multicall : 336 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 1,756.46 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 425 pools, 247 jetons, 12948 routes
- Par DEX : uniswap_v3 129, aerodrome 171, aerodrome_slipstream 86, pancakeswap_v3 26, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 1
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 145 (rejetés 2) → 550 jetons ; pools candidats 3571 (énumérés 255, par paires 0), mesurés 427, sous le plancher de 10000.0 $ : 2 → gardés 425 (max 1500) ; prix des hubs : {'USDC': 1.0, 'DAI': 1.0, 'USDbC': 1.0, 'WETH': 1759.475588, 'cbBTC': 62145.383052, 'AERO': 0.418705}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 85,497,462 | 1,756.460373 | 59718981 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/USDC | 500 | 25,571,739 | 1,759.357089 | 59718981 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| uniswap_v3 | WETH/cbBTC | 500 | 21,231,900 | 0.028315 | 59718981 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 7,696,197 | 0.028313 | 59718981 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| aerodrome | WETH/VVV | 3000 | 6,670,023 | 80.530101 | 59718981 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | USDC/cbBTC | 500 | 6,075,184 | 0.000016 | 59718981 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,160,357 | 0.028308 | 59718981 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 3,573,579 | 2.410320 | 59718981 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/USDC | 100 | 3,276,752 | 1,759.873723 | 59718981 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,267,025 | 0.998616 | 59718981 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 2,732,600 | 38,666.141864 | 59718981 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 107 | 2,302,605 | 1,759.842392 | 59718981 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,064,539 | 0.000016 | 59718981 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 1,713,034 | 0.028309 | 59718981 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 1,650,695 | 1,147,728.379701 | 59718981 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,458,205 | 0.844466 | 59718981 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | USDC/cbBTC | 484 | 1,385,940 | 0.000016 | 59718981 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,328,867 | 0.000000 | 59718981 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,265,917 | 0.006529 | 59718981 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,245,519 | 0.000016 | 59718981 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,125,124 | 13.878905 | 59718981 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | USDC/SEND | 3000 | 1,060,065 | 86.471751 | 59718981 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,048,870 | 447.228596 | 59718981 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | WETH/USDC | 3000 | 1,020,763 | 1,755.602311 | 59718981 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| uniswap_v3 | WETH/VVV | 10000 | 1,018,555 | 79.963855 | 59718981 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,013,401 | 15,789.710812 | 59718981 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v2 | WETH/USDC | 3000 | 986,416 | 1,756.334006 | 59718981 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| uniswap_v3 | WETH/AERO | 3000 | 985,864 | 4,235.292775 | 59718981 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v3 | WETH/doginme | 10000 | 926,220 | 30,646,273.347966 | 59718981 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | USDC/VVV | 3000 | 910,896 | 0.045782 | 59718981 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | USDC/NOCK | 3000 | 846,808 | 59.664398 | 59718981 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/BRETT | 10000 | 821,889 | 523,883.700955 | 59718981 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | DRB/WETH | 10000 | 806,769 | 0.000000 | 59718981 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/TOSHI | 10000 | 793,166 | 22,197,854.584471 | 59718981 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 785,169 | 0.001543 | 59718981 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| uniswap_v3 | WETH/MORPHO | 3000 | 741,138 | 1,072.441650 | 59718981 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | XDP/USDC | 100 | 729,875 | 0.014923 | 59718981 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | WETH/USDC | 500 | 727,079 | 1,759.360277 | 59718981 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| pancakeswap_v3 | QUID/USDC | 100 | 724,295 | 0.046626 | 59718981 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome_slipstream | USDC/SAPIEN | 4605 | 709,916 | 24.827276 | 59718981 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v3 | WETH/USDC | 10000 | 696,007 | 1,752.211334 | 59718981 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/USDC | 100 | 601,285 | 1,759.833165 | 59718981 | `0xb4CB800910B228ED3d0834cF79D697127BBB00e5` |
| aerodrome | WETH/wstETH | 3000 | 596,192 | 0.798842 | 59718981 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | TIG/USDC | 10000 | 589,415 | 0.436590 | 59718981 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 554,775 | 4,769,188.903836 | 59718981 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome | WETH/AERO | 10000 | 540,134 | 4,203.495683 | 59718981 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | WETH/BRETT | 3706 | 511,999 | 523,541.884031 | 59718981 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome | USDC/MAI (stable) | 3000 | 509,125 | 1.386503 | 59718981 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | FLOCK/USDC | 3000 | 500,611 | 0.031881 | 59718981 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| uniswap_v2 | WETH/NPC | 3000 | 479,083 | 170,944.269832 | 59718981 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | USDC/USDT | 11 | 464,508 | 1.001324 | 59718981 | `0xa41Bc0AFfbA7Fd420d186b84899d7ab2aC57fcD1` |
| aerodrome_slipstream | AERO/cbBTC | 1025 | 440,186 | 0.000007 | 59718981 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| pancakeswap_v3 | ELSA/USDC | 100 | 408,146 | 0.056950 | 59718981 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| aerodrome_slipstream | WETH/MORPHO | 3034 | 403,659 | 1,072.508406 | 59718981 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| uniswap_v3 | WETH/UNI | 10000 | 386,224 | 355.155789 | 59718981 | `0xAb365f161Dd501473a1ff0D2ef0dCE94E7398839` |
| uniswap_v3 | WETH/uSOL | 3000 | 385,394 | 23.917382 | 59718981 | `0xab04A352D4EC8d0F1812A4E5EBe7807Fa67acD48` |
| aerodrome | cbBTC/EDGE | 7000 | 382,076 | 849,085.087211 | 59718981 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| aerodrome | AWE/USDC | 3000 | 369,801 | 0.056864 | 59718981 | `0xcb7f520d18141E36956fE0b3A6Bc3D4F11245521` |
| aerodrome | VIRTUAL/WETH | 10000 | 368,590 | 0.000239 | 59718981 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/VVV | 2730 | 368,097 | 80.544506 | 59718981 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |

## Recherche d'opportunités
- Cycles : 6263 ; routes examinées : 81093324 ; candidats optimisés : 108322 ; net attendu > 0 : 39 ; dernier cycle 305.1 ms
- Rejets (moteur) : {'spread_below_threshold': 79551758, 'liquidity_below_min': 940835, 'negative_expected_net': 108283, 'borrow_bound_too_small': 6531, 'cycle_budget_exhausted': 144}
- Enregistrements de la session : 21913 ; net attendu > 0 : 39 ; simulés (eth_call de la vraie tx) : 0 (ok 0, échec 0) ; étiquettes ghost N+1 : 0/0 positives
- Décisions : {'REJECTED': 21913} ; motifs de rejet : {'below_safety_margin': 39, 'negative_expected_net': 21874, 'p_lower_below_threshold': 39, 'price_impact': 36}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 59697177 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.001883 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0006 €) | — | 0.05 | 0.175 (n=44) | REJECTED | below_safety_margin(1<37), p_lower_below_threshold(0.18<0.75) |
| 59697177 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 123.681033 USDC | 0.005743 USDC | 0.000000 USDC | 0.005361 USDC | 0.000382 USDC (0.0004 €) | — | 0.03 | 0.175 (n=44) | REJECTED | below_safety_margin(382<24736), p_lower_below_threshold(0.18<0.75) |
| 59697177 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.066562 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0001 €) | — | 0.01 | 0.175 (n=44) | REJECTED | below_safety_margin(60322543631<13312314161262), p_lower_below_threshold(0.18<0.75) |
| 59703714 | USDC→[pancakeswap_v3]→WETH→[aerodrome]→fBOMB→[aerodrome]→USDC | 0.999999 USDC | 0.004894 USDC | 0.000000 USDC | 0.004801 USDC | 0.000093 USDC (0.0001 €) | — | 0.93 | 0.221 (n=90) | REJECTED | below_safety_margin(93<199), price_impact(201bps>150.0), p_lower_below_threshold(0.22<0.75) |
| 59703714 | USDC→[pancakeswap_v3]→WETH→[aerodrome]→fBOMB→[aerodrome]→USDC | 0.999999 USDC | 0.004894 USDC | 0.000000 USDC | 0.004801 USDC | 0.000093 USDC (0.0001 €) | — | 0.93 | 0.221 (n=90) | REJECTED | below_safety_margin(93<199), price_impact(201bps>150.0), p_lower_below_threshold(0.22<0.75) |
| 59703715 | USDC→[pancakeswap_v3]→WETH→[aerodrome]→fBOMB→[aerodrome]→USDC | 0.999999 USDC | 0.004894 USDC | 0.000000 USDC | 0.004801 USDC | 0.000093 USDC (0.0001 €) | — | 0.93 | 0.221 (n=90) | REJECTED | below_safety_margin(93<199), price_impact(201bps>150.0), p_lower_below_threshold(0.22<0.75) |
| 59703693 | USDC→[pancakeswap_v3]→WETH→[aerodrome]→fBOMB→[aerodrome]→USDC | 0.999999 USDC | 0.004894 USDC | 0.000000 USDC | 0.004802 USDC | 0.000092 USDC (0.0001 €) | — | 0.92 | 0.221 (n=90) | REJECTED | below_safety_margin(92<199), price_impact(201bps>150.0), p_lower_below_threshold(0.22<0.75) |
| 59703693 | USDC→[pancakeswap_v3]→WETH→[aerodrome]→fBOMB→[aerodrome]→USDC | 0.999999 USDC | 0.004894 USDC | 0.000000 USDC | 0.004802 USDC | 0.000092 USDC (0.0001 €) | — | 0.92 | 0.221 (n=90) | REJECTED | below_safety_margin(92<199), price_impact(201bps>150.0), p_lower_below_threshold(0.22<0.75) |
| 59703693 | WETH→[aerodrome]→fBOMB→[aerodrome]→USDC→[pancakeswap_v3]→WETH | 0.000570 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0001 €) | — | 0.91 | 0.221 (n=90) | REJECTED | below_safety_margin(51999092606<114099750249), price_impact(201bps>150.0), p_lower_below_threshold(0.22<0.75) |
| 59703693 | WETH→[aerodrome]→fBOMB→[aerodrome]→USDC→[pancakeswap_v3]→WETH | 0.000570 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0001 €) | — | 0.91 | 0.221 (n=90) | REJECTED | below_safety_margin(51999092606<114099750249), price_impact(201bps>150.0), p_lower_below_threshold(0.22<0.75) |
| 59703716 | USDC→[pancakeswap_v3]→WETH→[aerodrome]→fBOMB→[aerodrome]→USDC | 0.999999 USDC | 0.004894 USDC | 0.000000 USDC | 0.004803 USDC | 0.000091 USDC (0.0001 €) | — | 0.91 | 0.221 (n=90) | REJECTED | below_safety_margin(91<199), price_impact(201bps>150.0), p_lower_below_threshold(0.22<0.75) |
| 59703716 | USDC→[pancakeswap_v3]→WETH→[aerodrome]→fBOMB→[aerodrome]→USDC | 0.999999 USDC | 0.004894 USDC | 0.000000 USDC | 0.004803 USDC | 0.000091 USDC (0.0001 €) | — | 0.91 | 0.221 (n=90) | REJECTED | below_safety_margin(91<199), price_impact(201bps>150.0), p_lower_below_threshold(0.22<0.75) |
| 59703714 | WETH→[aerodrome]→fBOMB→[aerodrome]→USDC→[pancakeswap_v3]→WETH | 0.000571 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0001 €) | — | 0.91 | 0.221 (n=90) | REJECTED | below_safety_margin(51804931332<114112452851), price_impact(201bps>150.0), p_lower_below_threshold(0.22<0.75) |
| 59703714 | WETH→[aerodrome]→fBOMB→[aerodrome]→USDC→[pancakeswap_v3]→WETH | 0.000571 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0001 €) | — | 0.91 | 0.221 (n=90) | REJECTED | below_safety_margin(51804931332<114112452851), price_impact(201bps>150.0), p_lower_below_threshold(0.22<0.75) |
| 59703715 | WETH→[aerodrome]→fBOMB→[aerodrome]→USDC→[pancakeswap_v3]→WETH | 0.000571 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0001 €) | — | 0.91 | 0.221 (n=90) | REJECTED | below_safety_margin(51804931332<114112452851), price_impact(201bps>150.0), p_lower_below_threshold(0.22<0.75) |
| 59703717 | USDC→[pancakeswap_v3]→WETH→[aerodrome]→fBOMB→[aerodrome]→USDC | 0.999999 USDC | 0.004893 USDC | 0.000000 USDC | 0.004803 USDC | 0.000090 USDC (0.0001 €) | — | 0.90 | 0.221 (n=90) | REJECTED | below_safety_margin(90<199), price_impact(201bps>150.0), p_lower_below_threshold(0.22<0.75) |
| 59703718 | USDC→[pancakeswap_v3]→WETH→[aerodrome]→fBOMB→[aerodrome]→USDC | 0.999999 USDC | 0.004893 USDC | 0.000000 USDC | 0.004803 USDC | 0.000090 USDC (0.0001 €) | — | 0.90 | 0.221 (n=90) | REJECTED | below_safety_margin(90<199), price_impact(201bps>150.0), p_lower_below_threshold(0.22<0.75) |
| 59703716 | WETH→[aerodrome]→fBOMB→[aerodrome]→USDC→[pancakeswap_v3]→WETH | 0.000571 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0001 €) | — | 0.90 | 0.221 (n=90) | REJECTED | below_safety_margin(51131761727<114112452851), price_impact(201bps>150.0), p_lower_below_threshold(0.22<0.75) |
| 59703716 | WETH→[aerodrome]→fBOMB→[aerodrome]→USDC→[pancakeswap_v3]→WETH | 0.000571 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0001 €) | — | 0.90 | 0.221 (n=90) | REJECTED | below_safety_margin(51131761727<114112452851), price_impact(201bps>150.0), p_lower_below_threshold(0.22<0.75) |
| 59703717 | WETH→[aerodrome]→fBOMB→[aerodrome]→USDC→[pancakeswap_v3]→WETH | 0.000571 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0001 €) | — | 0.89 | 0.221 (n=90) | REJECTED | below_safety_margin(50947096168<114112452851), price_impact(201bps>150.0), p_lower_below_threshold(0.22<0.75) |
| 59703718 | WETH→[aerodrome]→fBOMB→[aerodrome]→USDC→[pancakeswap_v3]→WETH | 0.000571 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0001 €) | — | 0.89 | 0.221 (n=90) | REJECTED | below_safety_margin(50947096168<114112452851), price_impact(201bps>150.0), p_lower_below_threshold(0.22<0.75) |
| 59703714 | USDC→[uniswap_v3]→WETH→[aerodrome]→fBOMB→[aerodrome]→USDC | 0.999999 USDC | 0.004888 USDC | 0.000000 USDC | 0.004801 USDC | 0.000087 USDC (0.0001 €) | — | 0.87 | 0.281 (n=245) | REJECTED | below_safety_margin(87<199), price_impact(201bps>150.0), p_lower_below_threshold(0.28<0.75) |
| 59703714 | USDC→[uniswap_v3]→WETH→[aerodrome]→fBOMB→[aerodrome]→USDC | 0.999999 USDC | 0.004888 USDC | 0.000000 USDC | 0.004801 USDC | 0.000087 USDC (0.0001 €) | — | 0.87 | 0.281 (n=245) | REJECTED | below_safety_margin(87<199), price_impact(201bps>150.0), p_lower_below_threshold(0.28<0.75) |
| 59703715 | USDC→[uniswap_v3]→WETH→[aerodrome]→fBOMB→[aerodrome]→USDC | 0.999999 USDC | 0.004888 USDC | 0.000000 USDC | 0.004801 USDC | 0.000087 USDC (0.0001 €) | — | 0.87 | 0.281 (n=245) | REJECTED | below_safety_margin(87<199), price_impact(201bps>150.0), p_lower_below_threshold(0.28<0.75) |
| 59703693 | USDC→[uniswap_v3]→WETH→[aerodrome]→fBOMB→[aerodrome]→USDC | 0.999999 USDC | 0.004888 USDC | 0.000000 USDC | 0.004802 USDC | 0.000086 USDC (0.0001 €) | — | 0.86 | 0.281 (n=245) | REJECTED | below_safety_margin(86<199), price_impact(201bps>150.0), p_lower_below_threshold(0.28<0.75) |

## Fiabilité et décision
- Observations ghost : 8582 ; taux observé 0.227 ; borne inférieure crédible (0.9) 0.222 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 22.2% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
