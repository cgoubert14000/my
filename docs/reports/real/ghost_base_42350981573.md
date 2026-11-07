# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-07T10:06:01+00:00 ; durée 157.5 min ; blocs 54230643 → 54277867 (7363 vus)

## Connexion
- Requêtes RPC : 97829 ; erreurs : 200 ; latence p50/p95 : 317.1/1,798.3 ms
- Rafraîchissements d'état : 7363 ; âge des données au dernier bloc : 9.35 s ; changements de frais LP observés (pools à frais dynamiques) : 2647
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 4588 ; cycles déclenchés par événement : 2012 ; avance médiane sur le rafraîchissement multicall : 437 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,242.46 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 476 pools, 279 jetons, 17784 routes
- Par DEX : uniswap_v3 135, aerodrome_slipstream 99, aerodrome 198, pancakeswap_v3 29, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 170 (rejetés 2) → 575 jetons ; pools candidats 3720 (énumérés 295, par paires 0), mesurés 479, sous le plancher de 10000.0 $ : 3 → gardés 476 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2241.234025, 'cbBTC': 75952.6335, 'AERO': 0.608777}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 146,022,165 | 2,242.462387 | 54277898 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,810,866 | 0.029529 | 54277898 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,328,684 | 0.000013 | 54277898 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,192,570 | 0.029513 | 54277898 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 8,023,933 | 2,244.078920 | 54277898 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,354,397 | 108.648921 | 54277898 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,428,201 | 0.001551 | 54277898 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 4,852,404 | 1.666694 | 54277898 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,772,437 | 0.029540 | 54277898 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,180,076 | 2,245.008720 | 54277898 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,002,494 | 0.998507 | 54277898 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,320,535 | 42,682.443204 | 54277898 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 150 | 3,204,351 | 2,244.927029 | 54277898 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,559,282 | 0.029528 | 54277898 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 2,099,210 | 1,156,736.421986 | 54277898 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 400 | 1,742,913 | 0.000013 | 54277898 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,669,795 | 0.000000 | 54277898 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,667,428 | 0.006590 | 54277898 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,637,014 | 0.000013 | 54277898 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | XDP/USDC | 100 | 1,608,618 | 0.016014 | 54277898 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,531,389 | 436.318072 | 54277898 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,509,892 | 0.000013 | 54277898 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,481,364 | 1.493437 | 54277898 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,460,301 | 0.819432 | 54277898 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,380,099 | 3,738.938508 | 54277898 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v2 | WETH/USDC | 3000 | 1,327,090 | 2,246.385783 | 54277898 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome | WETH/USDC | 3000 | 1,325,479 | 2,247.428848 | 54277898 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,273,988 | 14,734.211319 | 54277898 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,198,430 | 2,244.148879 | 54277898 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,123,702 | 76.955062 | 54277898 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,110,703 | 36,090,744.436654 | 54277898 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/VVV | 10000 | 1,040,876 | 107.865732 | 54277898 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,026,663 | 559,738.741503 | 54277898 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,004,143 | 0.000000 | 54277898 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/TOSHI | 10000 | 999,203 | 22,522,526.287595 | 54277898 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/VELVET | 100 | 980,602 | 20.061540 | 54277898 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/MORPHO | 3000 | 942,703 | 1,058.426615 | 54277898 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/USDC | 10000 | 938,064 | 2,228.788739 | 54277898 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome_slipstream | USDC/cbBTC | 334 | 927,171 | 0.000013 | 54277898 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/NOCK | 3000 | 915,513 | 74.761656 | 54277898 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome | WETH/EDEL | 7000 | 883,670 | 98,235.520835 | 54277898 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | USDC/VVV | 3000 | 804,209 | 0.048435 | 54277898 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 797,734 | 20.977026 | 54277898 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome | WETH/AERO | 10000 | 796,096 | 3,711.695747 | 54277898 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| pancakeswap_v3 | QUID/USDC | 100 | 790,384 | 0.055902 | 54277898 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 760,747 | 0.799699 | 54277898 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 721,205 | 0.566867 | 54277898 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 696,179 | 4,910,167.640250 | 54277898 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome | VIRTUAL/WETH | 10000 | 685,710 | 0.000253 | 54277898 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | TIG/USDC | 10000 | 675,403 | 0.571190 | 54277898 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/NPC | 3000 | 660,293 | 145,802.261424 | 54277898 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 652,080 | 0.000008 | 54277898 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 629,723 | 564,917.383337 | 54277898 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome | WETH/msETH (stable) | 500 | 589,135 | 2.473837 | 54277898 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | FLOCK/USDC | 3000 | 578,433 | 0.039872 | 54277898 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| pancakeswap_v3 | ELSA/USDC | 100 | 530,722 | 0.079808 | 54277898 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 529,623 | 1,058.722291 | 54277898 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome | cbBTC/EDGE | 7000 | 517,935 | 915,795.565206 | 54277898 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| aerodrome | WETH/DRV | 3000 | 514,032 | 6,979.214575 | 54277898 | `0xaC4e562d7C6108f971321F14238E24AE2cC398ac` |
| uniswap_v3 | WETH/USDC | 100 | 511,754 | 2,244.880695 | 54277898 | `0xb4CB800910B228ED3d0834cF79D697127BBB00e5` |

## Recherche d'opportunités
- Cycles : 9374 ; routes examinées : 166707216 ; candidats optimisés : 411887 ; net attendu > 0 : 39 ; dernier cycle 322.9 ms
- Rejets (moteur) : {'spread_below_threshold': 164457773, 'liquidity_below_min': 1827689, 'negative_expected_net': 411848, 'borrow_bound_too_small': 9367, 'cycle_budget_exhausted': 500}
- Enregistrements de la session : 411887 ; net attendu > 0 : 39 ; simulés (eth_call de la vraie tx) : 12 (ok 9, échec 3) ; étiquettes ghost N+1 : 1/10 positives
- Décisions : {'REJECTED': 411887} ; motifs de rejet : {'below_safety_margin': 27, 'negative_expected_net': 411848, 'p_lower_below_threshold': 39, 'simulation_failed': 3, 'stale_data': 20}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 54246318 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 27.735293 USDC | 0.020597 USDC | 0.000000 USDC | 0.005033 USDC | 0.015564 USDC (0.0143 €) | 0.015564 USDC | 5.61 | 0.025 (n=329) | REJECTED | p_lower_below_threshold(0.03<0.75) |
| 54266291 | USDC→[pancakeswap_v3]→PLAY→[aerodrome_slipstream]→USDC | 24.463190 USDC | 0.016058 USDC | 0.000000 USDC | 0.005035 USDC | 0.011023 USDC (0.0101 €) | — | 4.51 | 0.025 (n=331) | REJECTED | stale_data(4867ms>4000.0), simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.03<0.75) |
| 54231076 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 23.543309 USDC | 0.014681 USDC | 0.000000 USDC | 0.005032 USDC | 0.009649 USDC (0.0089 €) | 0.009649 USDC | 4.10 | 0.025 (n=328) | REJECTED | p_lower_below_threshold(0.03<0.75) |
| 54231076 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 23.543309 USDC | 0.014681 USDC | 0.000000 USDC | 0.005032 USDC | 0.009649 USDC (0.0089 €) | — | 4.10 | 0.025 (n=328) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.03<0.75) |
| 54274531 | USDC→[uniswap_v3]→AERO→[aerodrome]→USDbC→[aerodrome_slipstream]→USDC | 32.331815 USDC | 0.015477 USDC | 0.000000 USDC | 0.006429 USDC | 0.009048 USDC (0.0083 €) | 0.009048 USDC | 2.80 | 0.212 (n=192) | REJECTED | p_lower_below_threshold(0.21<0.75) |
| 54270937 | WETH→[pancakeswap_v3]→AERO→[aerodrome]→wstETH→[uniswap_v3]→WETH | 0.009427 WETH | 0.000007 WETH | 0.000000 WETH | 0.000003 WETH | 0.000004 WETH (0.0077 €) | 0.000004 WETH | 3.94 | 0.279 (n=167) | REJECTED | p_lower_below_threshold(0.28<0.75) |
| 54270937 | WETH→[pancakeswap_v3]→AERO→[aerodrome]→wstETH→[aerodrome_slipstream]→WETH | 0.008987 WETH | 0.000006 WETH | 0.000000 WETH | 0.000003 WETH | 0.000003 WETH (0.0065 €) | 0.000003 WETH | 3.49 | 0.279 (n=167) | REJECTED | p_lower_below_threshold(0.28<0.75) |
| 54249134 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 20.515326 USDC | 0.011356 USDC | 0.000000 USDC | 0.005036 USDC | 0.006320 USDC (0.0058 €) | 0.006320 USDC | 3.08 | 0.025 (n=330) | REJECTED | p_lower_below_threshold(0.03<0.75) |
| 54249134 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 20.515326 USDC | 0.011356 USDC | 0.000000 USDC | 0.005036 USDC | 0.006320 USDC (0.0058 €) | — | 3.08 | 0.025 (n=330) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.03<0.75) |
| 54269847 | USDC→[pancakeswap_v3]→PLAY→[aerodrome_slipstream]→USDC | 19.552131 USDC | 0.010320 USDC | 0.000000 USDC | 0.005035 USDC | 0.005285 USDC (0.0049 €) | 0.005285 USDC | 2.70 | 0.046 (n=255) | REJECTED | p_lower_below_threshold(0.05<0.75) |
| 54254635 | USDC→[pancakeswap_v3]→ICNT→[uniswap_v3]→USDC | 27.523699 USDC | 0.009237 USDC | 0.000000 USDC | 0.005033 USDC | 0.004204 USDC (0.0039 €) | — | 1.53 | 0.046 (n=255) | REJECTED | below_safety_margin(4204<5504), stale_data(4982ms>4000.0), p_lower_below_threshold(0.05<0.75) |
| 54238043 | USDC→[pancakeswap_v3]→PLAY→[aerodrome_slipstream]→USDC | 18.092171 USDC | 0.008744 USDC | 0.000000 USDC | 0.005033 USDC | 0.003711 USDC (0.0034 €) | 0.003711 USDC | 2.05 | 0.046 (n=254) | REJECTED | p_lower_below_threshold(0.05<0.75) |
| 54274087 | WETH→[uniswap_v3]→DEGEN→[uniswap_v3]→WETH | 0.009075 WETH | 0.000004 WETH | 0.000000 WETH | 0.000002 WETH | 0.000001 WETH (0.0028 €) | — | 1.50 | 0.052 (n=83) | REJECTED | below_safety_margin(1357835475336<1815075662829), p_lower_below_threshold(0.05<0.75) |
| 54252757 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.000528 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0028 €) | — | 0.76 | 0.175 (n=1034) | REJECTED | below_safety_margin(4<10), stale_data(6553ms>4000.0), p_lower_below_threshold(0.18<0.75) |
| 54252757 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.000528 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0028 €) | — | 0.76 | 0.175 (n=1034) | REJECTED | below_safety_margin(4<10), stale_data(6790ms>4000.0), p_lower_below_threshold(0.18<0.75) |
| 54270937 | WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→wstETH→[uniswap_v3]→WETH | 0.006156 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0027 €) | 0.000001 WETH | 2.12 | 0.175 (n=1034) | REJECTED | p_lower_below_threshold(0.18<0.75) |
| 54252757 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.000442 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0021 €) | — | 0.68 | 0.175 (n=1034) | REJECTED | below_safety_margin(3<8), stale_data(6568ms>4000.0), p_lower_below_threshold(0.18<0.75) |
| 54252757 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.000442 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0021 €) | — | 0.68 | 0.175 (n=1034) | REJECTED | below_safety_margin(3<8), stale_data(6805ms>4000.0), p_lower_below_threshold(0.18<0.75) |
| 54270937 | WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→wstETH→[aerodrome_slipstream]→WETH | 0.005877 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0019 €) | — | 1.58 | 0.175 (n=1034) | REJECTED | below_safety_margin(931202191178<1175405286242), p_lower_below_threshold(0.18<0.75) |
| 54252757 | WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.020143 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0019 €) | — | 0.45 | 0.175 (n=1034) | REJECTED | below_safety_margin(900288630420<4028669010413), stale_data(6577ms>4000.0), p_lower_below_threshold(0.18<0.75) |
| 54252757 | WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.020143 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0019 €) | — | 0.45 | 0.175 (n=1034) | REJECTED | below_safety_margin(900288630420<4028669010413), stale_data(6813ms>4000.0), p_lower_below_threshold(0.18<0.75) |
| 54252757 | WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.022942 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0017 €) | — | 0.37 | 0.175 (n=1034) | REJECTED | below_safety_margin(845892239498<4588410158020), stale_data(6561ms>4000.0), p_lower_below_threshold(0.18<0.75) |
| 54252757 | WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.022942 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0017 €) | — | 0.37 | 0.175 (n=1034) | REJECTED | below_safety_margin(845892239498<4588410158020), stale_data(6798ms>4000.0), p_lower_below_threshold(0.18<0.75) |
| 54252757 | cbBTC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.000348 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0014 €) | — | 0.57 | 0.175 (n=1034) | REJECTED | below_safety_margin(2<6), stale_data(6539ms>4000.0), p_lower_below_threshold(0.18<0.75) |
| 54252757 | cbBTC→[uniswap_v3]→WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.000526 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0014 €) | — | 0.38 | 0.175 (n=1034) | REJECTED | below_safety_margin(2<10), stale_data(6593ms>4000.0), p_lower_below_threshold(0.18<0.75) |

## Fiabilité et décision
- Observations ghost : 5965 ; taux observé 0.160 ; borne inférieure crédible (0.9) 0.154 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 15.4% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
