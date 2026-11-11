# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-11T19:36:37+00:00 ; durée 89.57 min ; blocs 56150210 → 56177047 (4877 vus)

## Connexion
- Requêtes RPC : 59716 ; erreurs : 30 ; latence p50/p95 : 154.2/1,554.2 ms
- Rafraîchissements d'état : 4877 ; âge des données au dernier bloc : 9.64 s ; changements de frais LP observés (pools à frais dynamiques) : 3541
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 3620 ; cycles déclenchés par événement : 1182 ; avance médiane sur le rafraîchissement multicall : 359 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,077.56 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 462 pools, 267 jetons, 16678 routes
- Par DEX : uniswap_v3 134, aerodrome_slipstream 100, aerodrome 187, pancakeswap_v3 27, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 161 (rejetés 2) → 566 jetons ; pools candidats 3639 (énumérés 284, par paires 0), mesurés 464, sous le plancher de 10000.0 $ : 2 → gardés 462 (max 1500) ; prix des hubs : {'USDC': 1.0, 'DAI': 1.0, 'USDbC': 1.0, 'WETH': 2091.017157, 'cbBTC': 74374.029387, 'AERO': 0.55788}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 135,323,900 | 2,077.564448 | 56177071 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,576,261 | 0.027972 | 56177071 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 8,667,004 | 0.028003 | 56177071 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 8,547,713 | 0.000013 | 56177071 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 7,151,252 | 2,079.090613 | 56177071 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 6,997,836 | 102.694875 | 56177071 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,637,133 | 0.027962 | 56177071 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 4,287,955 | 1.811573 | 56177071 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,082,849 | 2,079.892825 | 56177071 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,913,589 | 0.998575 | 56177071 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,063,501 | 43,041.171578 | 56177071 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 131 | 2,925,529 | 2,079.675100 | 56177071 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,228,529 | 0.027989 | 56177071 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 1,975,296 | 1,121,348.046698 | 56177071 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 436 | 1,655,052 | 0.000013 | 56177071 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | XDP/USDC | 100 | 1,623,190 | 0.016405 | 56177071 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,611,471 | 0.000013 | 56177071 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,570,274 | 0.000000 | 56177071 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,537,286 | 0.000013 | 56177071 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,507,036 | 0.006412 | 56177071 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,464,343 | 0.830233 | 56177071 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,437,836 | 1.406597 | 56177071 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,428,235 | 424.124902 | 56177071 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | WETH/AERO | 3000 | 1,280,183 | 3,763.734815 | 56177071 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v2 | WETH/USDC | 3000 | 1,278,120 | 2,076.939921 | 56177071 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,233,591 | 15,126.816066 | 56177071 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/USDC | 3000 | 1,163,519 | 2,080.047097 | 56177071 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,135,976 | 2,078.999800 | 56177071 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,060,556 | 86.391696 | 56177071 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,050,813 | 33,778,785.269459 | 56177071 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/VVV | 10000 | 1,041,552 | 101.980193 | 56177071 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome_slipstream | USDC/VELVET | 100 | 963,654 | 21.142097 | 56177071 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/BRETT | 10000 | 951,483 | 558,929.094844 | 56177071 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 924,657 | 0.001493 | 56177071 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| uniswap_v3 | USDC/VVV | 3000 | 918,683 | 0.049430 | 56177071 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome_slipstream | USDC/cbBTC | 340 | 918,559 | 0.000013 | 56177071 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | WETH/TOSHI | 10000 | 913,766 | 23,053,289.280513 | 56177071 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | WETH/MORPHO | 3000 | 887,967 | 1,024.206559 | 56177071 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/USDC | 10000 | 882,801 | 2,080.323257 | 56177071 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | DRB/WETH | 10000 | 867,038 | 0.000000 | 56177071 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | USDC/NOCK | 3000 | 776,481 | 78.013640 | 56177071 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| pancakeswap_v3 | QUID/USDC | 100 | 768,085 | 0.052657 | 56177071 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome_slipstream | USDC/SAPIEN | 4520 | 752,384 | 22.807618 | 56177071 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome | WETH/EDEL | 7000 | 739,131 | 120,451.487952 | 56177071 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | WETH/AERO | 10000 | 717,350 | 3,736.460573 | 56177071 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | WETH/wstETH | 3000 | 703,881 | 0.801801 | 56177071 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 679,148 | 0.536278 | 56177071 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 666,973 | 4,599,757.694679 | 56177071 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 623,858 | 0.490058 | 56177071 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/NPC | 3000 | 608,925 | 147,500.193009 | 56177071 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | AERO/cbBTC | 1025 | 594,730 | 0.000007 | 56177071 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | VIRTUAL/WETH | 10000 | 586,902 | 0.000259 | 56177071 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/BRETT | 2096 | 584,213 | 563,990.597969 | 56177071 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | FLOCK/USDC | 3000 | 566,202 | 0.038371 | 56177071 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome_slipstream | WETH/MORPHO | 2706 | 497,533 | 1,024.549056 | 56177071 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| pancakeswap_v3 | ELSA/USDC | 100 | 464,651 | 0.066921 | 56177071 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| uniswap_v3 | USDC/MORPHO | 10000 | 457,810 | 0.490200 | 56177071 | `0x2043B296fFC6b2d3bf4A3F3167d2Afb3B0FBdbEE` |
| aerodrome_slipstream | USDC/USDT | 8 | 454,441 | 1.000670 | 56177071 | `0xa41Bc0AFfbA7Fd420d186b84899d7ab2aC57fcD1` |
| uniswap_v3 | WETH/uSOL | 3000 | 447,359 | 24.625098 | 56177071 | `0xab04A352D4EC8d0F1812A4E5EBe7807Fa67acD48` |
| aerodrome | cbBTC/EDGE | 7000 | 441,892 | 908,282.838332 | 56177071 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |

## Recherche d'opportunités
- Cycles : 6058 ; routes examinées : 101035324 ; candidats optimisés : 394284 ; net attendu > 0 : 308 ; dernier cycle 271.9 ms
- Rejets (moteur) : {'spread_below_threshold': 99311988, 'liquidity_below_min': 1315142, 'negative_expected_net': 393976, 'borrow_bound_too_small': 11154, 'cycle_budget_exhausted': 2723, 'unquotable': 33}
- Enregistrements de la session : 394284 ; net attendu > 0 : 308 ; simulés (eth_call de la vraie tx) : 31 (ok 26, échec 5) ; étiquettes ghost N+1 : 5/27 positives
- Décisions : {'REJECTED': 394284} ; motifs de rejet : {'below_safety_margin': 200, 'negative_expected_net': 393976, 'p_lower_below_threshold': 302, 'reliability_not_demonstrated': 6, 'sim_below_estimate': 1, 'simulated_net_nonpositive': 1, 'simulation_failed': 5, 'stale_data': 62}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 56174132 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→cbBTC | 0.010681 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0437 €) | — | 0.60 | 0.265 (n=1578) | REJECTED | below_safety_margin(64<213), p_lower_below_threshold(0.27<0.75) |
| 56174132 | USDC→[uniswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 794.809726 USDC | 0.053596 USDC | 0.000000 USDC | 0.006384 USDC | 0.047212 USDC (0.0434 €) | — | 0.59 | 0.265 (n=1578) | REJECTED | below_safety_margin(47212<158961), p_lower_below_threshold(0.27<0.75) |
| 56167293 | WETH→[uniswap_v3]→VIRTUAL→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.056066 WETH | 0.000026 WETH | 0.000000 WETH | 0.000003 WETH | 0.000023 WETH (0.0433 €) | 0.000023 WETH | 4.03 | 0.203 (n=1224) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 56174132 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.392586 WETH | 0.000026 WETH | 0.000000 WETH | 0.000003 WETH | 0.000023 WETH (0.0433 €) | — | 0.58 | 0.265 (n=1578) | REJECTED | below_safety_margin(22654727219442<78517201570312), p_lower_below_threshold(0.27<0.75) |
| 56167293 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→VIRTUAL→[pancakeswap_v3]→USDC | 116.074313 USDC | 0.053249 USDC | 0.000000 USDC | 0.006285 USDC | 0.046964 USDC (0.0432 €) | — | 4.05 | 0.203 (n=1224) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 56167293 | WETH→[uniswap_v3]→VIRTUAL→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.050025 WETH | 0.000022 WETH | 0.000000 WETH | 0.000003 WETH | 0.000019 WETH (0.0364 €) | 0.000019 WETH | 3.79 | 0.203 (n=1224) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 56167293 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→VIRTUAL→[pancakeswap_v3]→USDC | 103.494507 USDC | 0.045704 USDC | 0.000000 USDC | 0.006285 USDC | 0.039419 USDC (0.0363 €) | — | 3.81 | 0.203 (n=1224) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 56167293 | WETH→[uniswap_v3]→VIRTUAL→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.050944 WETH | 0.000022 WETH | 0.000000 WETH | 0.000003 WETH | 0.000019 WETH (0.0359 €) | 0.000019 WETH | 3.68 | 0.203 (n=1224) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 56167293 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→VIRTUAL→[pancakeswap_v3]→USDC | 105.432893 USDC | 0.045228 USDC | 0.000000 USDC | 0.006285 USDC | 0.038943 USDC (0.0358 €) | — | 3.69 | 0.203 (n=1224) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 56162083 | WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→WETH | 0.028201 WETH | 0.000013 WETH | 0.000000 WETH | 0.000003 WETH | 0.000010 WETH (0.0199 €) | 0.000010 WETH | 3.66 | 0.310 (n=558) | REJECTED | stale_data(4023ms>4000.0), p_lower_below_threshold(0.31<0.75) |
| 56162083 | USDC→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC | 58.652831 USDC | 0.027823 USDC | 0.000000 USDC | 0.006310 USDC | 0.021513 USDC (0.0198 €) | — | 3.67 | 0.310 (n=558) | REJECTED | stale_data(4029ms>4000.0), p_lower_below_threshold(0.31<0.75) |
| 56162083 | WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.028201 WETH | 0.000013 WETH | 0.000000 WETH | 0.000003 WETH | 0.000010 WETH (0.0196 €) | 0.000010 WETH | 3.61 | 0.203 (n=1219) | REJECTED | stale_data(4049ms>4000.0), p_lower_below_threshold(0.20<0.75) |
| 56162083 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC | 58.654926 USDC | 0.027537 USDC | 0.000000 USDC | 0.006310 USDC | 0.021227 USDC (0.0195 €) | — | 3.62 | 0.203 (n=1219) | REJECTED | stale_data(4056ms>4000.0), p_lower_below_threshold(0.20<0.75) |
| 56162083 | WETH→[aerodrome_slipstream]→USDT→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.027967 WETH | 0.000013 WETH | 0.000000 WETH | 0.000003 WETH | 0.000010 WETH (0.0194 €) | 0.000010 WETH | 3.61 | 0.203 (n=1219) | REJECTED | stale_data(4042ms>4000.0), p_lower_below_threshold(0.20<0.75) |
| 56162083 | USDC→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→USDT→[pancakeswap_v3]→USDC | 58.148032 USDC | 0.027330 USDC | 0.000000 USDC | 0.006310 USDC | 0.021020 USDC (0.0193 €) | — | 3.61 | 0.203 (n=1219) | REJECTED | stale_data(4036ms>4000.0), p_lower_below_threshold(0.20<0.75) |
| 56162083 | WETH→[aerodrome_slipstream]→USDT→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.027967 WETH | 0.000013 WETH | 0.000000 WETH | 0.000003 WETH | 0.000010 WETH (0.0191 €) | — | 3.56 | 0.203 (n=1219) | REJECTED | stale_data(4069ms>4000.0), p_lower_below_threshold(0.20<0.75) |
| 56162083 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDT→[pancakeswap_v3]→USDC | 58.127932 USDC | 0.027042 USDC | 0.000000 USDC | 0.006310 USDC | 0.020732 USDC (0.0191 €) | — | 3.57 | 0.203 (n=1219) | REJECTED | stale_data(4062ms>4000.0), p_lower_below_threshold(0.20<0.75) |
| 56162083 | WETH→[aerodrome_slipstream]→USDT→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.027417 WETH | 0.000013 WETH | 0.000000 WETH | 0.000003 WETH | 0.000010 WETH (0.0184 €) | — | 3.49 | 0.310 (n=558) | REJECTED | stale_data(4076ms>4000.0), p_lower_below_threshold(0.31<0.75) |
| 56162083 | USDC→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→USDT→[uniswap_v3]→USDC | 56.734038 USDC | 0.026258 USDC | 0.000000 USDC | 0.006310 USDC | 0.019948 USDC (0.0184 €) | — | 3.52 | 0.310 (n=558) | REJECTED | stale_data(4082ms>4000.0), p_lower_below_threshold(0.31<0.75) |
| 56162083 | WETH→[aerodrome_slipstream]→USDT→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.027425 WETH | 0.000012 WETH | 0.000000 WETH | 0.000003 WETH | 0.000009 WETH (0.0182 €) | — | 3.44 | 0.203 (n=1219) | REJECTED | stale_data(4089ms>4000.0), p_lower_below_threshold(0.20<0.75) |
| 56162083 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDT→[uniswap_v3]→USDC | 57.188759 USDC | 0.025969 USDC | 0.000000 USDC | 0.006310 USDC | 0.019659 USDC (0.0181 €) | — | 3.44 | 0.203 (n=1219) | REJECTED | stale_data(4096ms>4000.0), p_lower_below_threshold(0.20<0.75) |
| 56167293 | WETH→[aerodrome_slipstream]→VIRTUAL→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.038899 WETH | 0.000012 WETH | 0.000000 WETH | 0.000003 WETH | 0.000009 WETH (0.0180 €) | — | 2.42 | 0.265 (n=1578) | REJECTED | p_lower_below_threshold(0.27<0.75) |
| 56167293 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→VIRTUAL→[pancakeswap_v3]→USDC | 80.942844 USDC | 0.025820 USDC | 0.000000 USDC | 0.006285 USDC | 0.019535 USDC (0.0180 €) | — | 2.41 | 0.265 (n=1578) | REJECTED | p_lower_below_threshold(0.27<0.75) |
| 56167293 | WETH→[aerodrome_slipstream]→VIRTUAL→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.034289 WETH | 0.000010 WETH | 0.000000 WETH | 0.000003 WETH | 0.000007 WETH (0.0139 €) | — | 2.12 | 0.265 (n=1578) | REJECTED | p_lower_below_threshold(0.27<0.75) |
| 56167293 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→VIRTUAL→[pancakeswap_v3]→USDC | 70.696270 USDC | 0.021384 USDC | 0.000000 USDC | 0.006285 USDC | 0.015099 USDC (0.0139 €) | — | 2.14 | 0.265 (n=1578) | REJECTED | p_lower_below_threshold(0.27<0.75) |

## Fiabilité et décision
- Observations ghost : 8191 ; taux observé 0.216 ; borne inférieure crédible (0.9) 0.211 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 21.1% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ✅ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
