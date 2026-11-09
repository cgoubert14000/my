# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-09T06:42:56+00:00 ; durée 141.68 min ; blocs 55038467 → 55080912 (5199 vus)

## Connexion
- Requêtes RPC : 75631 ; erreurs : 0 ; latence p50/p95 : 553.6/2,159.6 ms
- Rafraîchissements d'état : 5199 ; âge des données au dernier bloc : 14.13 s ; changements de frais LP observés (pools à frais dynamiques) : 3637
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 7838 ; cycles déclenchés par événement : 2438 ; avance médiane sur le rafraîchissement multicall : 755 ms
- Gaz : base fee 0.005344 gwei ; prix ETH (pool le plus profond) : 2,112.40 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 467 pools, 272 jetons, 17562 routes
- Par DEX : uniswap_v3 134, aerodrome_slipstream 97, aerodrome 194, pancakeswap_v3 28, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 166 (rejetés 2) → 571 jetons ; pools candidats 3664 (énumérés 288, par paires 0), mesurés 469, sous le plancher de 10000.0 $ : 2 → gardés 467 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'DAI': 1.0, 'USDC': 1.0, 'WETH': 2141.212816, 'cbBTC': 74926.035696, 'AERO': 0.58265}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 138,304,022 | 2,112.262440 | 55080948 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,283,822 | 0.028451 | 55080948 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 8,840,812 | 0.000014 | 55080948 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 8,718,887 | 0.028521 | 55080948 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 7,421,940 | 2,106.405632 | 55080948 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,082,347 | 103.940262 | 55080948 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,219,865 | 0.001519 | 55080948 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,575,126 | 0.028451 | 55080948 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 4,571,181 | 1.761727 | 55080948 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,910,491 | 0.998733 | 55080948 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| pancakeswap_v3 | WETH/USDC | 100 | 3,896,473 | 2,107.022168 | 55080948 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | WETH/KTA | 3000 | 3,120,495 | 42,886.456474 | 55080948 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 150 | 3,016,441 | 2,106.978858 | 55080948 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2585 | 2,345,848 | 0.028513 | 55080948 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 1,975,232 | 1,159,342.676479 | 55080948 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 508 | 1,701,627 | 0.000013 | 55080948 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,591,854 | 0.000014 | 55080948 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,580,017 | 0.006634 | 55080948 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v3 | XDP/USDC | 100 | 1,555,778 | 0.015375 | 55080948 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,543,982 | 0.000000 | 55080948 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,474,099 | 1.421539 | 55080948 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,452,662 | 0.824262 | 55080948 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,447,122 | 432.435375 | 55080948 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,404,160 | 0.000013 | 55080948 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v3 | WETH/AERO | 3000 | 1,309,976 | 3,718.461265 | 55080948 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v2 | WETH/USDC | 3000 | 1,288,420 | 2,112.662370 | 55080948 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,230,925 | 15,170.389174 | 55080948 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/USDC | 3000 | 1,218,183 | 2,111.434228 | 55080948 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome | USDC/SEND | 3000 | 1,120,777 | 77.357246 | 55080948 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,087,046 | 2,106.864036 | 55080948 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | WETH/doginme | 10000 | 1,038,710 | 36,878,976.881950 | 55080948 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/VVV | 10000 | 1,008,387 | 104.274421 | 55080948 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/BRETT | 10000 | 950,780 | 588,968.824557 | 55080948 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome_slipstream | USDC/VELVET | 100 | 948,268 | 22.196497 | 55080948 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/TOSHI | 10000 | 925,053 | 23,211,976.018977 | 55080948 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/cbBTC | 352 | 921,424 | 0.000014 | 55080948 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/NOCK | 3000 | 913,216 | 75.138200 | 55080948 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/USDC | 10000 | 909,062 | 2,093.804189 | 55080948 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | DRB/WETH | 10000 | 900,080 | 0.000000 | 55080948 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/MORPHO | 3000 | 896,793 | 1,044.191181 | 55080948 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | USDC/VVV | 3000 | 839,459 | 0.049274 | 55080948 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | WETH/EDEL | 7000 | 820,663 | 101,010.041414 | 55080948 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| pancakeswap_v3 | QUID/USDC | 100 | 779,353 | 0.054275 | 55080948 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome_slipstream | USDC/SAPIEN | 4535 | 747,195 | 23.005396 | 55080948 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome | WETH/AERO | 10000 | 741,227 | 3,701.404575 | 55080948 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | WETH/wstETH | 3000 | 716,050 | 0.800980 | 55080948 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 693,117 | 0.531397 | 55080948 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 646,310 | 5,056,331.240227 | 55080948 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 643,591 | 0.524564 | 55080948 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 618,173 | 0.000008 | 55080948 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v2 | WETH/NPC | 3000 | 615,739 | 148,874.888380 | 55080948 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome | VIRTUAL/WETH | 10000 | 588,606 | 0.000251 | 55080948 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/BRETT | 2120 | 577,769 | 591,583.032322 | 55080948 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | FLOCK/USDC | 3000 | 563,803 | 0.038154 | 55080948 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome | WETH/msETH (stable) | 500 | 542,958 | 2.338654 | 55080948 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | WETH/MORPHO | 2724 | 508,650 | 1,044.573436 | 55080948 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome | cbBTC/EDGE | 7000 | 500,897 | 927,786.431744 | 55080948 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| uniswap_v3 | USDC/USDT | 100 | 497,532 | 1.001258 | 55080948 | `0xD56da2B74bA826f19015E6B7Dd9Dae1903E85DA1` |
| pancakeswap_v3 | ELSA/USDC | 100 | 491,648 | 0.071754 | 55080948 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| uniswap_v3 | WETH/USDC | 100 | 482,296 | 2,106.761254 | 55080948 | `0xb4CB800910B228ED3d0834cF79D697127BBB00e5` |

## Recherche d'opportunités
- Cycles : 7636 ; routes examinées : 134103432 ; candidats optimisés : 452068 ; net attendu > 0 : 639 ; dernier cycle 757.4 ms
- Rejets (moteur) : {'spread_below_threshold': 131804312, 'liquidity_below_min': 1838884, 'negative_expected_net': 451429, 'borrow_bound_too_small': 7633, 'cycle_budget_exhausted': 535}
- Enregistrements de la session : 452068 ; net attendu > 0 : 639 ; simulés (eth_call de la vraie tx) : 32 (ok 23, échec 9) ; étiquettes ghost N+1 : 4/28 positives
- Décisions : {'REJECTED': 452068} ; motifs de rejet : {'below_safety_margin': 575, 'negative_expected_net': 451429, 'p_lower_below_threshold': 578, 'reliability_not_demonstrated': 61, 'simulation_failed': 9, 'stale_data': 86}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 55045434 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.355434 WETH | 0.000047 WETH | 0.000000 WETH | 0.000003 WETH | 0.000044 WETH (0.0857 €) | — | 1.22 | 0.048 (n=30) | REJECTED | below_safety_margin(43516011434452<71086872293656), p_lower_below_threshold(0.05<0.75) |
| 55045434 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.355434 WETH | 0.000047 WETH | 0.000000 WETH | 0.000003 WETH | 0.000044 WETH (0.0857 €) | — | 1.22 | 0.048 (n=30) | REJECTED | below_safety_margin(43516011434452<71086872293656), p_lower_below_threshold(0.05<0.75) |
| 55045434 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 732.198649 USDC | 0.099587 USDC | 0.000000 USDC | 0.006433 USDC | 0.093154 USDC (0.0857 €) | — | 1.27 | 0.048 (n=30) | REJECTED | below_safety_margin(93154<146439), p_lower_below_threshold(0.05<0.75) |
| 55045434 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 732.198649 USDC | 0.099587 USDC | 0.000000 USDC | 0.006433 USDC | 0.093154 USDC (0.0857 €) | — | 1.27 | 0.048 (n=30) | REJECTED | below_safety_margin(93154<146439), p_lower_below_threshold(0.05<0.75) |
| 55045434 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.009259 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0855 €) | — | 1.34 | 0.048 (n=30) | REJECTED | below_safety_margin(124<185), p_lower_below_threshold(0.05<0.75) |
| 55045434 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.009259 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0855 €) | — | 1.34 | 0.048 (n=30) | REJECTED | below_safety_margin(124<185), p_lower_below_threshold(0.05<0.75) |
| 55073953 | USDC→[pancakeswap_v3]→ICNT→[uniswap_v3]→USDC | 88.285333 USDC | 0.083463 USDC | 0.000000 USDC | 0.004818 USDC | 0.078645 USDC (0.0724 €) | — | 8.91 | 0.007 (n=109) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.01<0.75) |
| 55045434 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.006493 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0690 €) | — | 1.54 | 0.204 (n=1207) | REJECTED | below_safety_margin(100<129), p_lower_below_threshold(0.20<0.75) |
| 55045434 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.006493 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0690 €) | — | 1.54 | 0.204 (n=1207) | REJECTED | below_safety_margin(100<129), p_lower_below_threshold(0.20<0.75) |
| 55045434 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 501.136491 USDC | 0.080969 USDC | 0.000000 USDC | 0.006433 USDC | 0.074536 USDC (0.0686 €) | — | 1.49 | 0.204 (n=1207) | REJECTED | below_safety_margin(74536<100227), p_lower_below_threshold(0.20<0.75) |
| 55045434 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 501.136491 USDC | 0.080969 USDC | 0.000000 USDC | 0.006433 USDC | 0.074536 USDC (0.0686 €) | — | 1.49 | 0.204 (n=1207) | REJECTED | below_safety_margin(74536<100227), p_lower_below_threshold(0.20<0.75) |
| 55045434 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.226863 WETH | 0.000038 WETH | 0.000000 WETH | 0.000003 WETH | 0.000035 WETH (0.0684 €) | — | 1.53 | 0.204 (n=1207) | REJECTED | below_safety_margin(34746748358204<45372651029136), p_lower_below_threshold(0.20<0.75) |
| 55045434 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.226863 WETH | 0.000038 WETH | 0.000000 WETH | 0.000003 WETH | 0.000035 WETH (0.0684 €) | — | 1.53 | 0.204 (n=1207) | REJECTED | below_safety_margin(34746748358204<45372651029136), p_lower_below_threshold(0.20<0.75) |
| 55072334 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.135415 WETH | 0.000024 WETH | 0.000000 WETH | 0.000003 WETH | 0.000021 WETH (0.0408 €) | — | 1.54 | 0.203 (n=1210) | REJECTED | below_safety_margin(20787072282793<27082935218889), p_lower_below_threshold(0.20<0.75) |
| 55072334 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.135415 WETH | 0.000024 WETH | 0.000000 WETH | 0.000003 WETH | 0.000021 WETH (0.0408 €) | — | 1.54 | 0.203 (n=1210) | REJECTED | below_safety_margin(20787072282793<27082935218889), p_lower_below_threshold(0.20<0.75) |
| 55072334 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.003743 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0405 €) | — | 1.58 | 0.203 (n=1210) | REJECTED | below_safety_margin(59<74), p_lower_below_threshold(0.20<0.75) |
| 55072334 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.003743 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0405 €) | — | 1.58 | 0.203 (n=1210) | REJECTED | below_safety_margin(59<74), p_lower_below_threshold(0.20<0.75) |
| 55072334 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 272.073666 USDC | 0.050502 USDC | 0.000000 USDC | 0.006728 USDC | 0.043774 USDC (0.0403 €) | — | 1.61 | 0.203 (n=1210) | REJECTED | below_safety_margin(43774<54414), p_lower_below_threshold(0.20<0.75) |
| 55072334 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 272.073666 USDC | 0.050502 USDC | 0.000000 USDC | 0.006728 USDC | 0.043774 USDC (0.0403 €) | — | 1.61 | 0.203 (n=1210) | REJECTED | below_safety_margin(43774<54414), p_lower_below_threshold(0.20<0.75) |
| 55045434 | cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.003032 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0331 €) | — | 1.58 | 0.204 (n=1207) | REJECTED | below_safety_margin(48<60), p_lower_below_threshold(0.20<0.75) |
| 55045434 | cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.003032 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0331 €) | — | 1.58 | 0.204 (n=1207) | REJECTED | below_safety_margin(48<60), p_lower_below_threshold(0.20<0.75) |
| 55045434 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 206.733463 USDC | 0.042103 USDC | 0.000000 USDC | 0.006433 USDC | 0.035670 USDC (0.0328 €) | — | 1.73 | 0.204 (n=1207) | REJECTED | below_safety_margin(35670<41346), p_lower_below_threshold(0.20<0.75) |
| 55045434 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 206.733463 USDC | 0.042103 USDC | 0.000000 USDC | 0.006433 USDC | 0.035670 USDC (0.0328 €) | — | 1.73 | 0.204 (n=1207) | REJECTED | below_safety_margin(35670<41346), p_lower_below_threshold(0.20<0.75) |
| 55045434 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.111121 WETH | 0.000020 WETH | 0.000000 WETH | 0.000003 WETH | 0.000017 WETH (0.0327 €) | — | 1.50 | 0.204 (n=1207) | REJECTED | below_safety_margin(16614882044691<22224232427663), p_lower_below_threshold(0.20<0.75) |
| 55045434 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.111121 WETH | 0.000020 WETH | 0.000000 WETH | 0.000003 WETH | 0.000017 WETH (0.0327 €) | — | 1.50 | 0.204 (n=1207) | REJECTED | below_safety_margin(16614882044691<22224232427663), p_lower_below_threshold(0.20<0.75) |

## Fiabilité et décision
- Observations ghost : 6678 ; taux observé 0.175 ; borne inférieure crédible (0.9) 0.169 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 16.9% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ✅ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
