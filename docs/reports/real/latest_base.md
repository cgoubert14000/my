# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-04T11:49:02+00:00 ; durée 6.09 min ; blocs 53501612 → 53501797 (183 vus)

## Connexion
- Requêtes RPC : 2240 ; erreurs : 0 ; latence p50/p95 : 164.2/1,034.9 ms
- Rafraîchissements d'état : 183 ; âge des données au dernier bloc : 2.56 s ; changements de frais LP observés (pools à frais dynamiques) : 222
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 2482 ; cycles déclenchés par événement : 294 ; avance médiane sur le rafraîchissement multicall : 545 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,329.10 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 495 pools, 284 jetons, 19384 routes
- Par DEX : uniswap_v3 142, aerodrome_slipstream 106, aerodrome 204, pancakeswap_v3 29, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 174 (rejetés 2) → 579 jetons ; pools candidats 3706 (énumérés 308, par paires 0), mesurés 498, sous le plancher de 10000.0 $ : 3 → gardés 495 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDC': 1.0, 'USDbC': 1.0, 'WETH': 2327.57512, 'cbBTC': 78571.031441, 'AERO': 0.644724}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 152,385,666 | 2,329.102401 | 53501797 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,981,860 | 0.029691 | 53501797 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,366,783 | 0.029623 | 53501797 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,173,960 | 0.000013 | 53501797 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 8,150,827 | 2,331.464048 | 53501797 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 8,112,478 | 96.494897 | 53501797 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,666,276 | 0.001563 | 53501797 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 5,418,750 | 1.551052 | 53501797 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,912,822 | 0.029681 | 53501797 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,223,799 | 2,330.757639 | 53501797 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,126,909 | 0.999894 | 53501797 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome_slipstream | WETH/USDC | 150 | 3,901,117 | 2,330.766357 | 53501797 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome | WETH/KTA | 3000 | 3,517,037 | 41,042.973959 | 53501797 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2515 | 2,682,988 | 0.029639 | 53501797 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2733 | 2,228,832 | 96.522191 | 53501797 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | WETH/FAI | 10000 | 2,183,731 | 1,153,315.868669 | 53501797 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 484 | 1,826,479 | 0.000013 | 53501797 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | XDP/USDC | 100 | 1,744,823 | 0.017928 | 53501797 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,671,875 | 0.000000 | 53501797 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,649,724 | 0.006488 | 53501797 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,631,589 | 0.000013 | 53501797 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,591,309 | 434.342320 | 53501797 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,554,531 | 0.000013 | 53501797 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,552,810 | 1.433011 | 53501797 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | WETH/AERO | 3000 | 1,457,347 | 3,617.163449 | 53501797 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,454,103 | 0.819242 | 53501797 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,381,133 | 2,331.212806 | 53501797 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | WETH/USDC | 3000 | 1,352,574 | 2,331.798254 | 53501797 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| uniswap_v2 | WETH/USDC | 3000 | 1,351,973 | 2,329.838422 | 53501797 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,320,137 | 14,620.579281 | 53501797 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | USDC/SEND | 3000 | 1,158,306 | 72.425825 | 53501797 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,142,559 | 37,192,037.297593 | 53501797 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,071,826 | 551,635.897113 | 53501797 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,069,596 | 0.000000 | 53501797 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,046,387 | 22,207,069.108539 | 53501797 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | WETH/VVV | 10000 | 1,031,362 | 96.789805 | 53501797 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | USDC/VVV | 3000 | 997,101 | 0.041405 | 53501797 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome_slipstream | USDC/VELVET | 100 | 996,200 | 19.159480 | 53501797 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/MORPHO | 3000 | 978,625 | 1,040.967326 | 53501797 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome_slipstream | USDC/cbBTC | 336 | 950,032 | 0.000013 | 53501797 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | WETH/WELL | 10000 | 944,477 | 1,268,565.070221 | 53501797 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome | USDC/NOCK | 3000 | 935,617 | 71.516051 | 53501797 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/USDC | 10000 | 934,443 | 2,312.902102 | 53501797 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome | WETH/EDEL | 7000 | 933,755 | 94,915.168446 | 53501797 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | uXRP/WETH | 3000 | 893,702 | 0.000551 | 53501797 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome | WETH/AERO | 10000 | 861,344 | 3,632.791343 | 53501797 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 828,673 | 19.799017 | 53501797 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 797,719 | 0.057025 | 53501797 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 790,560 | 0.799140 | 53501797 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 740,977 | 0.593926 | 53501797 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| aerodrome | VIRTUAL/WETH | 10000 | 735,833 | 0.000254 | 53501797 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 718,771 | 4,965,945.251736 | 53501797 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v2 | WETH/NPC | 3000 | 688,731 | 144,424.914996 | 53501797 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 684,585 | 0.000008 | 53501797 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 658,403 | 550,428.918626 | 53501797 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | TIG/USDC | 10000 | 656,250 | 0.541523 | 53501797 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome | WETH/msETH (stable) | 500 | 648,118 | 2.483100 | 53501797 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome | WETH/bsdETH | 100 | 625,928 | 0.913833 | 53501797 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 612,346 | 0.092860 | 53501797 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| uniswap_v3 | FLOCK/USDC | 3000 | 573,719 | 0.039477 | 53501797 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |

## Recherche d'opportunités
- Cycles : 476 ; routes examinées : 9226784 ; candidats optimisés : 55173 ; net attendu > 0 : 52 ; dernier cycle 177.9 ms
- Rejets (moteur) : {'spread_below_threshold': 9033157, 'liquidity_below_min': 137950, 'negative_expected_net': 55121, 'borrow_bound_too_small': 476, 'cycle_budget_exhausted': 28}
- Enregistrements de la session : 55173 ; net attendu > 0 : 52 ; simulés (eth_call de la vraie tx) : 1 (ok 0, échec 1) ; étiquettes ghost N+1 : 0/1 positives
- Décisions : {'REJECTED': 55173} ; motifs de rejet : {'below_safety_margin': 51, 'negative_expected_net': 55121, 'p_lower_below_threshold': 52, 'simulation_failed': 1, 'stale_data': 8}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53501641 | USDC→[pancakeswap_v3]→ICNT→[uniswap_v3]→USDC | 95.999795 USDC | 0.132980 USDC | 0.000000 USDC | 0.005238 USDC | 0.127742 USDC (0.1175 €) | — | 13.31 | 0.000 (n=80) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 53501630 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 70.325640 USDC | 0.019659 USDC | 0.000000 USDC | 0.007008 USDC | 0.012651 USDC (0.0116 €) | — | 1.80 | 0.183 (n=886) | REJECTED | below_safety_margin(12651<14065), p_lower_below_threshold(0.18<0.75) |
| 53501630 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.000877 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0115 €) | — | 1.82 | 0.183 (n=886) | REJECTED | below_safety_margin(16<17), p_lower_below_threshold(0.18<0.75) |
| 53501630 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.000877 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0115 €) | — | 1.82 | 0.183 (n=886) | REJECTED | below_safety_margin(16<17), p_lower_below_threshold(0.18<0.75) |
| 53501630 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 70.230403 USDC | 0.019055 USDC | 0.000000 USDC | 0.007008 USDC | 0.012047 USDC (0.0111 €) | — | 1.72 | 0.183 (n=886) | REJECTED | below_safety_margin(12047<14046), p_lower_below_threshold(0.18<0.75) |
| 53501712 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 64.828500 USDC | 0.012769 USDC | 0.000000 USDC | 0.007006 USDC | 0.005763 USDC (0.0053 €) | — | 0.89 | 0.253 (n=354) | REJECTED | below_safety_margin(5763<12965), p_lower_below_threshold(0.25<0.75) |
| 53501713 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 64.828500 USDC | 0.012769 USDC | 0.000000 USDC | 0.007006 USDC | 0.005763 USDC (0.0053 €) | — | 0.89 | 0.253 (n=354) | REJECTED | below_safety_margin(5763<12965), stale_data(4454ms>4000.0), p_lower_below_threshold(0.25<0.75) |
| 53501712 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→WETH | 0.027761 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0053 €) | — | 0.89 | 0.253 (n=354) | REJECTED | below_safety_margin(2459639547889<5552107171970), p_lower_below_threshold(0.25<0.75) |
| 53501713 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→WETH | 0.027761 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0053 €) | — | 0.89 | 0.253 (n=354) | REJECTED | below_safety_margin(2459639547889<5552107171970), stale_data(4447ms>4000.0), p_lower_below_threshold(0.25<0.75) |
| 53501712 | USDC→[uniswap_v3]→AERO→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 66.611364 USDC | 0.011491 USDC | 0.000000 USDC | 0.007006 USDC | 0.004485 USDC (0.0041 €) | — | 0.67 | 0.253 (n=354) | REJECTED | below_safety_margin(4485<13322), p_lower_below_threshold(0.25<0.75) |
| 53501713 | USDC→[uniswap_v3]→AERO→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 66.611364 USDC | 0.011491 USDC | 0.000000 USDC | 0.007006 USDC | 0.004485 USDC (0.0041 €) | — | 0.67 | 0.253 (n=354) | REJECTED | below_safety_margin(4485<13322), stale_data(4480ms>4000.0), p_lower_below_threshold(0.25<0.75) |
| 53501712 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→AERO→[uniswap_v3]→WETH | 0.028393 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0041 €) | — | 0.67 | 0.253 (n=354) | REJECTED | below_safety_margin(1911815854876<5678546110651), p_lower_below_threshold(0.25<0.75) |
| 53501713 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→AERO→[uniswap_v3]→WETH | 0.028393 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0041 €) | — | 0.67 | 0.253 (n=354) | REJECTED | below_safety_margin(1911815854876<5678546110651), stale_data(4487ms>4000.0), p_lower_below_threshold(0.25<0.75) |
| 53501712 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 57.967857 USDC | 0.009361 USDC | 0.000000 USDC | 0.007006 USDC | 0.002355 USDC (0.0022 €) | — | 0.41 | 0.183 (n=886) | REJECTED | below_safety_margin(2355<11593), p_lower_below_threshold(0.18<0.75) |
| 53501713 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 57.967857 USDC | 0.009361 USDC | 0.000000 USDC | 0.007006 USDC | 0.002355 USDC (0.0022 €) | — | 0.41 | 0.183 (n=886) | REJECTED | below_safety_margin(2355<11593), stale_data(4540ms>4000.0), p_lower_below_threshold(0.18<0.75) |
| 53501712 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→WETH | 0.025180 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0021 €) | — | 0.40 | 0.183 (n=886) | REJECTED | below_safety_margin(999862019545<5035991096384), p_lower_below_threshold(0.18<0.75) |
| 53501713 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→WETH | 0.025180 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0021 €) | — | 0.40 | 0.183 (n=886) | REJECTED | below_safety_margin(999862019545<5035991096384), stale_data(4534ms>4000.0), p_lower_below_threshold(0.18<0.75) |
| 53501629 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.000479 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0014 €) | — | 0.42 | 0.183 (n=886) | REJECTED | below_safety_margin(2<9), p_lower_below_threshold(0.18<0.75) |
| 53501629 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.000479 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0014 €) | — | 0.42 | 0.183 (n=886) | REJECTED | below_safety_margin(2<9), p_lower_below_threshold(0.18<0.75) |
| 53501629 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 51.463073 USDC | 0.008134 USDC | 0.000000 USDC | 0.007008 USDC | 0.001126 USDC (0.0010 €) | — | 0.22 | 0.183 (n=886) | REJECTED | below_safety_margin(1126<10292), p_lower_below_threshold(0.18<0.75) |
| 53501629 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 51.463073 USDC | 0.008134 USDC | 0.000000 USDC | 0.007008 USDC | 0.001126 USDC (0.0010 €) | — | 0.22 | 0.183 (n=886) | REJECTED | below_safety_margin(1126<10292), p_lower_below_threshold(0.18<0.75) |
| 53501712 | USDC→[uniswap_v3]→AERO→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 58.853661 USDC | 0.008032 USDC | 0.000000 USDC | 0.007006 USDC | 0.001026 USDC (0.0009 €) | — | 0.17 | 0.183 (n=886) | REJECTED | below_safety_margin(1026<11770), p_lower_below_threshold(0.18<0.75) |
| 53501713 | USDC→[uniswap_v3]→AERO→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 58.853661 USDC | 0.008032 USDC | 0.000000 USDC | 0.007006 USDC | 0.001026 USDC (0.0009 €) | — | 0.17 | 0.183 (n=886) | REJECTED | below_safety_margin(1026<11770), stale_data(4586ms>4000.0), p_lower_below_threshold(0.18<0.75) |
| 53501712 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→AERO→[uniswap_v3]→WETH | 0.025700 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0009 €) | — | 0.17 | 0.183 (n=886) | REJECTED | below_safety_margin(430356725621<5140023951194), p_lower_below_threshold(0.18<0.75) |
| 53501713 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→AERO→[uniswap_v3]→WETH | 0.025700 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0009 €) | — | 0.17 | 0.183 (n=886) | REJECTED | below_safety_margin(430356725621<5140023951194), stale_data(4594ms>4000.0), p_lower_below_threshold(0.18<0.75) |

## Fiabilité et décision
- Observations ghost : 5073 ; taux observé 0.168 ; borne inférieure crédible (0.9) 0.161 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 16.1% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
