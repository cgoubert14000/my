# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-08T11:24:22+00:00 ; durée 330.21 min ; blocs 54634334 → 54733358 (14103 vus)

## Connexion
- Requêtes RPC : 184130 ; erreurs : 40 ; latence p50/p95 : 216.3/1,494.4 ms
- Rafraîchissements d'état : 14103 ; âge des données au dernier bloc : 8.43 s ; changements de frais LP observés (pools à frais dynamiques) : 3939
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 12397 ; cycles déclenchés par événement : 4635 ; avance médiane sur le rafraîchissement multicall : 392 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,233.79 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 470 pools, 276 jetons, 17708 routes
- Par DEX : uniswap_v3 135, aerodrome_slipstream 96, aerodrome 197, pancakeswap_v3 28, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 168 (rejetés 2) → 573 jetons ; pools candidats 3668 (énumérés 291, par paires 0), mesurés 473, sous le plancher de 10000.0 $ : 3 → gardés 470 (max 1500) ; prix des hubs : {'USDC': 1.0, 'USDbC': 1.0, 'DAI': 1.0, 'WETH': 2231.640985, 'cbBTC': 75743.146723, 'AERO': 0.606566}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 145,737,169 | 2,233.787325 | 54733386 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,859,228 | 0.029487 | 54733386 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,227,019 | 0.000013 | 54733386 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,152,797 | 0.029508 | 54733386 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 8,097,660 | 2,239.444609 | 54733386 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,411,869 | 106.124563 | 54733386 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,400,550 | 0.001545 | 54733386 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,159,090 | 0.029489 | 54733386 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 4,825,281 | 1.663248 | 54733386 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,178,735 | 2,239.137462 | 54733386 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,986,636 | 0.999609 | 54733386 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,280,824 | 43,384.320439 | 54733386 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 150 | 3,180,483 | 2,239.042728 | 54733386 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,547,155 | 0.029492 | 54733386 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 2,095,362 | 1,152,023.747540 | 54733386 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 484 | 1,737,714 | 0.000013 | 54733386 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,649,925 | 0.006522 | 54733386 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,649,348 | 0.000013 | 54733386 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,617,394 | 0.000000 | 54733386 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,569,331 | 0.015550 | 54733386 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,515,558 | 445.895581 | 54733386 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,508,336 | 0.000013 | 54733386 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,469,419 | 1.434827 | 54733386 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,458,312 | 0.821536 | 54733386 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,386,028 | 3,723.317307 | 54733386 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v2 | WETH/USDC | 3000 | 1,324,604 | 2,240.305944 | 54733386 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome | WETH/USDC | 3000 | 1,295,518 | 2,241.154742 | 54733386 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,258,394 | 15,110.740214 | 54733386 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,187,675 | 2,239.284550 | 54733386 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,123,360 | 77.001845 | 54733386 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,096,065 | 37,131,013.184037 | 54733386 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/VVV | 10000 | 1,056,876 | 106.719446 | 54733386 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,006,197 | 587,576.124167 | 54733386 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | WETH/TOSHI | 10000 | 980,477 | 23,108,518.016850 | 54733386 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/VELVET | 100 | 970,450 | 20.694920 | 54733386 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | DRB/WETH | 10000 | 963,396 | 0.000000 | 54733386 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/USDC | 10000 | 935,960 | 2,228.787480 | 54733386 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 929,345 | 1,072.413291 | 54733386 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome_slipstream | USDC/cbBTC | 342 | 925,310 | 0.000013 | 54733386 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/NOCK | 3000 | 923,857 | 73.417334 | 54733386 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome | WETH/EDEL | 7000 | 859,929 | 102,872.739971 | 54733386 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | USDC/VVV | 3000 | 832,489 | 0.047386 | 54733386 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | WETH/AERO | 10000 | 785,803 | 3,702.121411 | 54733386 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| pancakeswap_v3 | QUID/USDC | 100 | 784,282 | 0.054997 | 54733386 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome_slipstream | USDC/SAPIEN | 4540 | 777,443 | 21.759593 | 54733386 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome | WETH/wstETH | 3000 | 757,753 | 0.799805 | 54733386 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 713,987 | 0.562447 | 54733386 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| aerodrome | VIRTUAL/WETH | 10000 | 682,127 | 0.000253 | 54733386 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 680,589 | 5,098,978.431118 | 54733386 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 669,109 | 0.565420 | 54733386 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 654,077 | 0.000008 | 54733386 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v2 | WETH/NPC | 3000 | 638,532 | 154,751.954482 | 54733386 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | WETH/BRETT | 2135 | 611,617 | 588,556.312735 | 54733386 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | FLOCK/USDC | 3000 | 581,207 | 0.040001 | 54733386 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome | WETH/msETH (stable) | 500 | 554,297 | 2.471794 | 54733386 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| pancakeswap_v3 | ELSA/USDC | 100 | 522,789 | 0.078040 | 54733386 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| aerodrome | cbBTC/EDGE | 7000 | 521,196 | 900,163.032322 | 54733386 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| aerodrome_slipstream | WETH/MORPHO | 2736 | 520,110 | 1,072.230395 | 54733386 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome | WETH/DRV | 3000 | 515,742 | 6,879.468905 | 54733386 | `0xaC4e562d7C6108f971321F14238E24AE2cC398ac` |
| uniswap_v3 | WETH/USDC | 100 | 514,573 | 2,239.238220 | 54733386 | `0xb4CB800910B228ED3d0834cF79D697127BBB00e5` |

## Recherche d'opportunités
- Cycles : 18737 ; routes examinées : 331794796 ; candidats optimisés : 973700 ; net attendu > 0 : 531 ; dernier cycle 91.3 ms
- Rejets (moteur) : {'spread_below_threshold': 325454836, 'liquidity_below_min': 5360211, 'negative_expected_net': 973169, 'cycle_budget_exhausted': 4585, 'pool_quarantined': 1464}
- Enregistrements de la session : 973700 ; net attendu > 0 : 531 ; simulés (eth_call de la vraie tx) : 61 (ok 10, échec 51) ; étiquettes ghost N+1 : 7/49 positives
- Décisions : {'REJECTED': 973700} ; motifs de rejet : {'below_safety_margin': 315, 'negative_expected_net': 973169, 'p_lower_below_threshold': 482, 'reliability_not_demonstrated': 49, 'sim_below_estimate': 3, 'simulated_net_nonpositive': 3, 'simulation_failed': 51, 'stale_data': 26}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 54674540 | cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.258357 cbBTC | 0.003545 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.003545 cbBTC (246.9441 €) | — | 137.23 | 0.000 (n=38) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 54674540 | WETH→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 8.757750 WETH | 0.120183 WETH | 0.000000 WETH | 0.000004 WETH | 0.120179 WETH (246.8911 €) | — | 137.23 | 0.000 (n=38) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 54674540 | cbBTC→[uniswap_v3]→WETH→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.250913 cbBTC | 0.003403 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.003403 cbBTC (237.0499 €) | — | 135.64 | 0.000 (n=41) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 54674540 | WETH→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[uniswap_v3]→WETH | 8.501926 WETH | 0.115323 WETH | 0.000000 WETH | 0.000003 WETH | 0.115319 WETH (236.9079 €) | — | 135.64 | 0.000 (n=41) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 54674540 | USDC→[aerodrome]→AERO→[aerodrome_slipstream]→cbBTC→[uniswap_v3]→USDC | 14,744.145025 USDC | 209.965882 USDC | 0.000000 USDC | 0.006401 USDC | 209.959481 USDC (193.1627 €) | — | 142.40 | 0.000 (n=25) | REJECTED | reliability_not_demonstrated |
| 54674540 | cbBTC→[uniswap_v3]→USDC→[aerodrome]→AERO→[aerodrome_slipstream]→cbBTC | 0.194538 cbBTC | 0.002770 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.002770 cbBTC (192.9592 €) | — | 142.40 | 0.000 (n=25) | REJECTED | reliability_not_demonstrated |
| 54674540 | USDC→[aerodrome]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 14,615.810069 USDC | 202.947744 USDC | 0.000000 USDC | 0.009113 USDC | 202.938631 USDC (186.7035 €) | — | 138.85 | 0.001 (n=9) | REJECTED | reliability_not_demonstrated |
| 54674540 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome]→AERO→[aerodrome_slipstream]→cbBTC | 0.193050 cbBTC | 0.002681 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.002680 cbBTC (186.7009 €) | — | 138.85 | 0.001 (n=9) | REJECTED | reliability_not_demonstrated |
| 54674540 | cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.194147 cbBTC | 0.002650 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.002650 cbBTC (184.5855 €) | — | 136.50 | 0.000 (n=38) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 54674540 | cbBTC→[aerodrome_slipstream]→WETH→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.193291 cbBTC | 0.002637 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.002636 cbBTC (183.6341 €) | — | 136.40 | 0.000 (n=41) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 54674540 | WETH→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 6.547674 WETH | 0.089378 WETH | 0.000000 WETH | 0.000003 WETH | 0.089375 WETH (183.6079 €) | — | 136.50 | 0.000 (n=38) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 54674540 | WETH→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→WETH | 6.528980 WETH | 0.089057 WETH | 0.000000 WETH | 0.000003 WETH | 0.089053 WETH (182.9477 €) | — | 136.40 | 0.000 (n=41) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 54674540 | cbBTC→[uniswap_v3]→WETH→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.190960 cbBTC | 0.002504 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.002504 cbBTC (174.4211 €) | — | 131.14 | 0.000 (n=41) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 54674540 | WETH→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[uniswap_v3]→WETH | 6.450344 WETH | 0.084590 WETH | 0.000000 WETH | 0.000003 WETH | 0.084587 WETH (173.7713 €) | — | 131.13 | 0.000 (n=41) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 54674540 | cbBTC→[aerodrome_slipstream]→USDC→[aerodrome]→AERO→[aerodrome_slipstream]→cbBTC | 0.168622 cbBTC | 0.002394 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.002394 cbBTC (166.7468 €) | — | 141.97 | 0.000 (n=25) | REJECTED | reliability_not_demonstrated |
| 54674540 | USDC→[aerodrome]→AERO→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→USDC | 12,734.511732 USDC | 180.801836 USDC | 0.000000 USDC | 0.006740 USDC | 180.795096 USDC (166.3315 €) | — | 141.97 | 0.000 (n=25) | REJECTED | reliability_not_demonstrated |
| 54674540 | cbBTC→[aerodrome_slipstream]→USDC→[aerodrome]→AERO→[aerodrome_slipstream]→cbBTC | 0.165211 cbBTC | 0.002328 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.002328 cbBTC (162.1741 €) | — | 140.93 | 0.000 (n=25) | REJECTED | reliability_not_demonstrated |
| 54674540 | USDC→[aerodrome]→AERO→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→USDC | 12,470.780262 USDC | 175.761213 USDC | 0.000000 USDC | 0.006401 USDC | 175.754812 USDC (161.6944 €) | — | 140.93 | 0.000 (n=25) | REJECTED | reliability_not_demonstrated |
| 54674540 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→cbBTC | 0.142341 cbBTC | 0.002043 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.002043 cbBTC (142.2702 €) | — | 143.50 | 0.000 (n=38) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 54674540 | WETH→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 4.825624 WETH | 0.069249 WETH | 0.000000 WETH | 0.000003 WETH | 0.069246 WETH (142.2560 €) | — | 143.50 | 0.000 (n=38) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 54674540 | cbBTC→[uniswap_v3]→WETH→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→cbBTC | 0.137790 cbBTC | 0.001956 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.001955 cbBTC (136.2021 €) | — | 141.92 | 0.000 (n=41) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 54674540 | WETH→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→cbBTC→[uniswap_v3]→WETH | 4.669078 WETH | 0.066265 WETH | 0.000000 WETH | 0.000003 WETH | 0.066262 WETH (136.1265 €) | — | 141.92 | 0.000 (n=41) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 54674540 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→cbBTC | 0.115926 cbBTC | 0.001655 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.001655 cbBTC (115.2826 €) | — | 142.77 | 0.000 (n=38) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 54674540 | WETH→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 3.915496 WETH | 0.055905 WETH | 0.000000 WETH | 0.000003 WETH | 0.055902 WETH (114.8428 €) | — | 142.77 | 0.000 (n=38) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 54674540 | cbBTC→[uniswap_v3]→USDC→[aerodrome]→AERO→[aerodrome_slipstream]→cbBTC | 0.135127 cbBTC | 0.001645 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.001645 cbBTC (114.5959 €) | — | 121.76 | 0.000 (n=25) | REJECTED | reliability_not_demonstrated |

## Fiabilité et décision
- Observations ghost : 6188 ; taux observé 0.161 ; borne inférieure crédible (0.9) 0.155 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 15.5% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
