# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-29T21:25:23+00:00 ; durée 33.79 min ; blocs 53258868 → 53259886 (851 vus)

## Connexion
- Requêtes RPC : 10561 ; erreurs : 0 ; latence p50/p95 : 248.7/1,152.6 ms
- Rafraîchissements d'état : 851 ; âge des données au dernier bloc : 2.52 s ; changements de frais LP observés (pools à frais dynamiques) : 3982
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 38585 ; cycles déclenchés par événement : 746 ; avance médiane sur le rafraîchissement multicall : 672 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,282.95 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 499 pools, 290 jetons, 18414 routes
- Par DEX : uniswap_v3 138, aerodrome_slipstream 113, aerodrome 207, pancakeswap_v3 27, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 178 (rejetés 2) → 583 jetons ; pools candidats 3735 (énumérés 319, par paires 0), mesurés 502, sous le plancher de 10000.0 $ : 3 → gardés 499 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDC': 1.0, 'USDbC': 1.0, 'WETH': 2268.963647, 'cbBTC': 79202.631326, 'AERO': 0.656707}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 155,714,281 | 2,282.954321 | 53259886 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,174,781 | 0.028778 | 53259886 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,649,424 | 0.000013 | 53259886 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,267,456 | 0.028733 | 53259886 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 8,174,437 | 2,284.187152 | 53259886 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 8,061,408 | 97.178561 | 53259886 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,830,695 | 0.001605 | 53259886 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 6,249,183 | 1.525801 | 53259886 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,690,442 | 0.028762 | 53259886 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/USDC | 624 | 4,364,582 | 2,284.578001 | 53259886 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,336,564 | 2,283.676934 | 53259886 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,178,742 | 0.998745 | 53259886 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,590,461 | 37,837.525686 | 53259886 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2540 | 2,839,492 | 0.028745 | 53259886 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2793 | 2,390,917 | 97.105044 | 53259886 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | WETH/FAI | 10000 | 2,092,358 | 1,206,956.533351 | 53259886 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 424 | 2,088,358 | 0.000013 | 53259886 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | XDP/USDC | 100 | 1,770,403 | 0.018278 | 53259886 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,734,316 | 0.000000 | 53259886 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,725,050 | 411.879444 | 53259886 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | WETH/USDC | 3000 | 1,715,043 | 2,282.362725 | 53259886 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,699,591 | 0.000013 | 53259886 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,691,904 | 0.000013 | 53259886 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | USDC/cbBTC | 330 | 1,591,587 | 0.000013 | 53259886 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,514,127 | 1.588199 | 53259886 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,455,073 | 0.826447 | 53259886 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,393,145 | 3,479.786310 | 53259886 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,371,427 | 0.005335 | 53259886 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,345,433 | 14,294.086951 | 53259886 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,242,339 | 2,284.221083 | 53259886 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,188,281 | 0.000254 | 53259886 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | USDC/SEND | 3000 | 1,180,099 | 69.775852 | 53259886 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,121,341 | 37,069,483.623453 | 53259886 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | WETH/WELL | 10000 | 1,109,394 | 1,109,715.612087 | 53259886 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,071,189 | 522,365.092383 | 53259886 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | WETH/EDEL | 7000 | 1,055,852 | 71,406.623831 | 53259886 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,036,031 | 21,682,267.847916 | 53259886 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | DRB/WETH | 10000 | 1,030,928 | 0.000000 | 53259886 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,027,271 | 17.573006 | 53259886 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | USDC/VVV | 3000 | 1,026,879 | 0.042484 | 53259886 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v2 | WETH/USDC | 3000 | 1,017,574 | 2,282.247573 | 53259886 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome | VIRTUAL/WETH | 10000 | 997,688 | 0.000254 | 53259886 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome | USDC/NOCK | 3000 | 983,092 | 64.772886 | 53259886 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome | WETH/AERO | 10000 | 982,747 | 3,460.203192 | 53259886 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | WETH/VVV | 10000 | 981,647 | 97.831212 | 53259886 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/USDC | 10000 | 928,311 | 2,271.410543 | 53259886 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 909,462 | 1,044.468878 | 53259886 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | uXRP/WETH | 3000 | 872,968 | 0.000548 | 53259886 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 854,110 | 18.851750 | 53259886 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 829,430 | 0.061972 | 53259886 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 814,097 | 17.754162 | 53259886 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | WETH/wstETH | 3000 | 772,741 | 0.803616 | 53259886 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 732,322 | 4,589,554.467248 | 53259886 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 722,254 | 0.000008 | 53259886 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 710,638 | 0.579321 | 53259886 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| aerodrome | WETH/msETH (stable) | 500 | 694,892 | 2.333420 | 53259886 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v2 | WETH/NPC | 3000 | 668,254 | 147,020.689822 | 53259886 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | WETH/BRETT | 2132 | 663,767 | 520,037.994261 | 53259886 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | TIG/USDC | 10000 | 639,098 | 0.516287 | 53259886 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 628,779 | 0.097086 | 53259886 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |

## Recherche d'opportunités
- Cycles : 1596 ; routes examinées : 29388744 ; candidats optimisés : 219596 ; net attendu > 0 : 148 ; dernier cycle 155.7 ms
- Rejets (moteur) : {'spread_below_threshold': 28507501, 'liquidity_below_min': 651245, 'negative_expected_net': 219448, 'cycle_budget_exhausted': 8809, 'borrow_bound_too_small': 1593}
- Enregistrements de la session : 219596 ; net attendu > 0 : 148 ; simulés (eth_call de la vraie tx) : 12 (ok 6, échec 6) ; étiquettes ghost N+1 : 0/12 positives
- Décisions : {'REJECTED': 219596} ; motifs de rejet : {'below_safety_margin': 104, 'negative_expected_net': 219448, 'p_lower_below_threshold': 116, 'reliability_not_demonstrated': 32, 'simulation_failed': 6}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53258958 | USDC→[aerodrome_slipstream]→WETH→[aerodrome]→SPARKLET→[aerodrome]→USDC | 53.672656 USDC | 0.609516 USDC | 0.000000 USDC | 0.094098 USDC | 0.515418 USDC (0.4742 €) | — | 96.03 | 0.001 (n=12) | REJECTED | reliability_not_demonstrated |
| 53258958 | WETH→[aerodrome]→SPARKLET→[aerodrome]→USDC→[aerodrome_slipstream]→WETH | 0.023643 WETH | 0.000268 WETH | 0.000000 WETH | 0.000042 WETH | 0.000227 WETH (0.4727 €) | — | 95.98 | 0.001 (n=12) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53258958 | USDC→[pancakeswap_v3]→WETH→[aerodrome]→SPARKLET→[aerodrome]→USDC | 53.992478 USDC | 0.607074 USDC | 0.000000 USDC | 0.094098 USDC | 0.512976 USDC (0.4719 €) | — | 95.01 | 0.002 (n=4) | REJECTED | reliability_not_demonstrated |
| 53258958 | WETH→[aerodrome]→SPARKLET→[aerodrome]→USDC→[pancakeswap_v3]→WETH | 0.023782 WETH | 0.000267 WETH | 0.000000 WETH | 0.000042 WETH | 0.000226 WETH (0.4704 €) | — | 94.96 | 0.002 (n=4) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53258958 | USDC→[uniswap_v3]→WETH→[aerodrome]→SPARKLET→[aerodrome]→USDC | 53.850836 USDC | 0.603667 USDC | 0.000000 USDC | 0.098825 USDC | 0.504842 USDC (0.4645 €) | — | 93.75 | 0.001 (n=12) | REJECTED | reliability_not_demonstrated |
| 53258958 | WETH→[aerodrome]→SPARKLET→[aerodrome]→USDC→[uniswap_v3]→WETH | 0.023718 WETH | 0.000266 WETH | 0.000000 WETH | 0.000044 WETH | 0.000222 WETH (0.4629 €) | — | 93.70 | 0.001 (n=12) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53258958 | USDC→[pancakeswap_v3]→WETH→[aerodrome]→SPARKLET→[aerodrome]→USDC | 51.505228 USDC | 0.596764 USDC | 0.000000 USDC | 0.094098 USDC | 0.502666 USDC (0.4625 €) | — | 97.60 | 0.002 (n=4) | REJECTED | reliability_not_demonstrated |
| 53258958 | WETH→[aerodrome]→SPARKLET→[aerodrome]→USDC→[pancakeswap_v3]→WETH | 0.022685 WETH | 0.000263 WETH | 0.000000 WETH | 0.000042 WETH | 0.000221 WETH (0.4609 €) | — | 97.54 | 0.002 (n=4) | REJECTED | reliability_not_demonstrated |
| 53258958 | USDC→[uniswap_v3]→WETH→[aerodrome]→SPARKLET→[aerodrome]→USDC | 51.572167 USDC | 0.588705 USDC | 0.000000 USDC | 0.094098 USDC | 0.494607 USDC (0.4550 €) | — | 95.91 | 0.001 (n=12) | REJECTED | reliability_not_demonstrated |
| 53258958 | WETH→[aerodrome]→SPARKLET→[aerodrome]→USDC→[uniswap_v3]→WETH | 0.022711 WETH | 0.000259 WETH | 0.000000 WETH | 0.000042 WETH | 0.000218 WETH (0.4534 €) | — | 95.85 | 0.001 (n=12) | REJECTED | reliability_not_demonstrated |
| 53258958 | USDC→[sushiswap_v3]→WETH→[aerodrome]→SPARKLET→[aerodrome]→USDC | 50.823742 USDC | 0.577408 USDC | 0.000000 USDC | 0.094098 USDC | 0.483310 USDC (0.4446 €) | — | 95.10 | 0.001 (n=12) | REJECTED | reliability_not_demonstrated |
| 53258958 | WETH→[aerodrome]→SPARKLET→[aerodrome]→USDC→[sushiswap_v3]→WETH | 0.022374 WETH | 0.000254 WETH | 0.000000 WETH | 0.000042 WETH | 0.000213 WETH (0.4429 €) | — | 95.03 | 0.001 (n=12) | REJECTED | reliability_not_demonstrated |
| 53258958 | USDC→[aerodrome_slipstream]→WETH→[aerodrome]→SPARKLET→[aerodrome]→USDC | 52.465127 USDC | 0.575243 USDC | 0.000000 USDC | 0.094098 USDC | 0.481145 USDC (0.4427 €) | — | 91.71 | 0.001 (n=12) | REJECTED | reliability_not_demonstrated |
| 53258958 | WETH→[aerodrome]→SPARKLET→[aerodrome]→USDC→[aerodrome_slipstream]→WETH | 0.023090 WETH | 0.000253 WETH | 0.000000 WETH | 0.000042 WETH | 0.000212 WETH (0.4408 €) | — | 91.64 | 0.001 (n=12) | REJECTED | reliability_not_demonstrated |
| 53258958 | USDC→[uniswap_v2]→WETH→[aerodrome]→SPARKLET→[aerodrome]→USDC | 35.907335 USDC | 0.511105 USDC | 0.000000 USDC | 0.084430 USDC | 0.426675 USDC (0.3925 €) | — | 118.83 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 53258958 | WETH→[aerodrome]→SPARKLET→[aerodrome]→USDC→[uniswap_v2]→WETH | 0.015813 WETH | 0.000225 WETH | 0.000000 WETH | 0.000037 WETH | 0.000188 WETH (0.3912 €) | — | 118.76 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 53258958 | USDC→[aerodrome]→WETH→[aerodrome]→SPARKLET→[aerodrome]→USDC | 36.083880 USDC | 0.509169 USDC | 0.000000 USDC | 0.089801 USDC | 0.419368 USDC (0.3858 €) | — | 116.22 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 53258958 | WETH→[aerodrome]→SPARKLET→[aerodrome]→USDC→[aerodrome]→WETH | 0.015891 WETH | 0.000224 WETH | 0.000000 WETH | 0.000040 WETH | 0.000185 WETH (0.3844 €) | — | 116.15 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 53258958 | USDC→[uniswap_v3]→WETH→[aerodrome]→SPARKLET→[aerodrome]→USDC | 36.346156 USDC | 0.504189 USDC | 0.000000 USDC | 0.094098 USDC | 0.410091 USDC (0.3773 €) | — | 112.83 | 0.001 (n=12) | REJECTED | reliability_not_demonstrated |
| 53258958 | WETH→[aerodrome]→SPARKLET→[aerodrome]→USDC→[uniswap_v3]→WETH | 0.016005 WETH | 0.000222 WETH | 0.000000 WETH | 0.000042 WETH | 0.000180 WETH (0.3759 €) | — | 112.75 | 0.001 (n=12) | REJECTED | reliability_not_demonstrated |
| 53259511 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 1,280.711812 USDC | 0.357319 USDC | 0.000000 USDC | 0.036862 USDC | 0.320457 USDC (0.2948 €) | 0.320457 USDC | 2.50 | 0.001 (n=9) | REJECTED | reliability_not_demonstrated |
| 53259511 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.015637 cbBTC | 0.000005 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000004 cbBTC (0.2943 €) | 0.000004 cbBTC | 2.59 | 0.001 (n=9) | REJECTED | reliability_not_demonstrated |
| 53259511 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.552494 WETH | 0.000158 WETH | 0.000000 WETH | 0.000016 WETH | 0.000142 WETH (0.2943 €) | 0.000142 WETH | 2.57 | 0.001 (n=9) | REJECTED | reliability_not_demonstrated |
| 53259635 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 1,012.715722 USDC | 0.262482 USDC | 0.000000 USDC | 0.044762 USDC | 0.217720 USDC (0.2003 €) | — | 2.15 | 0.003 (n=2) | REJECTED | reliability_not_demonstrated |
| 53259635 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.445023 WETH | 0.000115 WETH | 0.000000 WETH | 0.000020 WETH | 0.000096 WETH (0.1996 €) | — | 2.15 | 0.003 (n=2) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |

## Fiabilité et décision
- Observations ghost : 3264 ; taux observé 0.106 ; borne inférieure crédible (0.9) 0.100 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 10.0% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
