# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-03T02:13:29+00:00 ; durée 15.2 min ; blocs 53440871 → 53441330 (454 vus)

## Connexion
- Requêtes RPC : 5461 ; erreurs : 0 ; latence p50/p95 : 243.8/1,421.0 ms
- Rafraîchissements d'état : 455 ; âge des données au dernier bloc : 1.68 s ; changements de frais LP observés (pools à frais dynamiques) : 619
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 5244 ; cycles déclenchés par événement : 702 ; avance médiane sur le rafraîchissement multicall : 581 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,253.97 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 490 pools, 285 jetons, 18224 routes
- Par DEX : uniswap_v3 136, aerodrome_slipstream 108, aerodrome 202, pancakeswap_v3 29, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 174 (rejetés 2) → 579 jetons ; pools candidats 3753 (énumérés 308, par paires 0), mesurés 493, sous le plancher de 10000.0 $ : 3 → gardés 490 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDC': 1.0, 'USDbC': 1.0, 'WETH': 2253.967555, 'cbBTC': 77042.637438, 'AERO': 0.602257}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 149,985,825 | 2,253.967541 | 53441330 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,174,051 | 0.029278 | 53441330 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,093,404 | 0.029314 | 53441330 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 8,973,888 | 0.000013 | 53441330 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 7,851,864 | 2,251.007984 | 53441330 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,575,565 | 104.442142 | 53441330 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,544,449 | 0.001564 | 53441330 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 5,345,692 | 1.666343 | 53441330 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,768,087 | 0.029281 | 53441330 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,074,367 | 2,251.626251 | 53441330 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,050,218 | 0.999897 | 53441330 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome_slipstream | WETH/USDC | 150 | 3,908,260 | 2,251.529899 | 53441330 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome | WETH/KTA | 3000 | 3,490,301 | 39,028.825618 | 53441330 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,695,367 | 0.029323 | 53441330 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 2,145,726 | 1,118,706.121332 | 53441330 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 424 | 2,033,737 | 0.000013 | 53441330 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome_slipstream | WETH/VVV | 2724 | 1,991,115 | 104.477050 | 53441330 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| uniswap_v3 | XDP/USDC | 100 | 1,763,338 | 0.018258 | 53441330 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,667,086 | 0.000000 | 53441330 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,607,564 | 0.000013 | 53441330 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,555,241 | 1.436173 | 53441330 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,542,441 | 0.000013 | 53441330 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,529,238 | 444.077418 | 53441330 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v2 | WETH/USDC | 3000 | 1,497,203 | 2,254.145201 | 53441330 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,453,608 | 0.822379 | 53441330 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,381,254 | 3,754.408383 | 53441330 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | WETH/USDC | 3000 | 1,349,579 | 2,256.891614 | 53441330 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,309,564 | 2,251.022988 | 53441330 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,288,705 | 0.004998 | 53441330 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,275,083 | 15,146.201165 | 53441330 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome_slipstream | USDC/cbBTC | 334 | 1,259,844 | 0.000013 | 53441330 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/SEND | 3000 | 1,168,739 | 71.138543 | 53441330 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,100,440 | 37,707,062.323865 | 53441330 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,045,288 | 542,381.855563 | 53441330 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,006,515 | 0.000000 | 53441330 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,001,419 | 22,629,385.868386 | 53441330 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/VELVET | 100 | 980,344 | 20.076183 | 53441330 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | WETH/EDEL | 7000 | 955,662 | 84,860.616311 | 53441330 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/USDC | 10000 | 922,809 | 2,257.234891 | 53441330 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome | WETH/WELL | 10000 | 913,175 | 1,270,925.743179 | 53441330 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/VVV | 10000 | 912,105 | 104.430898 | 53441330 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 911,865 | 1,040.916537 | 53441330 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome | USDC/NOCK | 3000 | 878,912 | 81.041304 | 53441330 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | uXRP/WETH | 3000 | 863,066 | 0.000550 | 53441330 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| uniswap_v3 | USDC/VVV | 3000 | 861,585 | 0.046426 | 53441330 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | WETH/AERO | 10000 | 823,340 | 3,725.146765 | 53441330 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 813,546 | 20.333020 | 53441330 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 791,292 | 0.056065 | 53441330 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 765,149 | 0.798949 | 53441330 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 723,826 | 0.578389 | 53441330 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| aerodrome | VIRTUAL/WETH | 10000 | 717,313 | 0.000258 | 53441330 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 700,604 | 4,893,819.869498 | 53441330 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v2 | WETH/NPC | 3000 | 663,573 | 145,643.676101 | 53441330 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| uniswap_v3 | TIG/USDC | 10000 | 660,062 | 0.547852 | 53441330 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome | WETH/msETH (stable) | 500 | 653,132 | 2.338821 | 53441330 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 651,357 | 0.000008 | 53441330 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 642,741 | 546,222.238572 | 53441330 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome | WETH/bsdETH | 100 | 605,400 | 0.914848 | 53441330 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 589,085 | 0.087621 | 53441330 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| uniswap_v3 | FLOCK/USDC | 3000 | 547,496 | 0.036840 | 53441330 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |

## Recherche d'opportunités
- Cycles : 1156 ; routes examinées : 21066944 ; candidats optimisés : 53154 ; net attendu > 0 : 26 ; dernier cycle 96.8 ms
- Rejets (moteur) : {'spread_below_threshold': 20794472, 'liquidity_below_min': 215813, 'negative_expected_net': 53128, 'unquotable': 2310, 'borrow_bound_too_small': 1155}
- Enregistrements de la session : 53151 ; net attendu > 0 : 26 ; simulés (eth_call de la vraie tx) : 2 (ok 0, échec 2) ; étiquettes ghost N+1 : 0/2 positives
- Décisions : {'REJECTED': 53151} ; motifs de rejet : {'below_safety_margin': 24, 'negative_expected_net': 53125, 'p_lower_below_threshold': 26, 'simulation_failed': 2}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53440959 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH | 0.017415 WETH | 0.000006 WETH | 0.000000 WETH | 0.000003 WETH | 0.000003 WETH (0.0070 €) | — | 1.93 | 0.186 (n=834) | REJECTED | below_safety_margin(3356158371189<3482936178209), p_lower_below_threshold(0.19<0.75) |
| 53440959 | USDC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 39.182298 USDC | 0.014335 USDC | 0.000000 USDC | 0.006772 USDC | 0.007563 USDC (0.0070 €) | — | 1.93 | 0.186 (n=834) | REJECTED | below_safety_margin(7563<7836), p_lower_below_threshold(0.19<0.75) |
| 53441325 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome_slipstream]→WETH | 0.012374 WETH | 0.000006 WETH | 0.000000 WETH | 0.000003 WETH | 0.000003 WETH (0.0054 €) | — | 2.09 | 0.186 (n=834) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.19<0.75) |
| 53441325 | USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 27.567782 USDC | 0.012595 USDC | 0.000000 USDC | 0.006772 USDC | 0.005823 USDC (0.0054 €) | — | 2.11 | 0.186 (n=834) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.19<0.75) |
| 53440959 | WETH→[aerodrome]→USDC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH | 0.015013 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0049 €) | — | 1.58 | 0.341 (n=102) | REJECTED | below_safety_margin(2378556590281<3002541347852), p_lower_below_threshold(0.34<0.75) |
| 53440959 | USDC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH→[aerodrome]→USDC | 33.611932 USDC | 0.011820 USDC | 0.000000 USDC | 0.006461 USDC | 0.005359 USDC (0.0049 €) | — | 1.59 | 0.341 (n=102) | REJECTED | below_safety_margin(5359<6722), p_lower_below_threshold(0.34<0.75) |
| 53440959 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH | 0.016276 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0048 €) | — | 1.43 | 0.186 (n=834) | REJECTED | below_safety_margin(2326850086013<3255257008595), p_lower_below_threshold(0.19<0.75) |
| 53440959 | USDC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 36.369124 USDC | 0.012014 USDC | 0.000000 USDC | 0.006772 USDC | 0.005242 USDC (0.0048 €) | — | 1.44 | 0.186 (n=834) | REJECTED | below_safety_margin(5242<7273), p_lower_below_threshold(0.19<0.75) |
| 53440959 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH | 0.012861 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0047 €) | — | 1.77 | 0.186 (n=834) | REJECTED | below_safety_margin(2282266051116<2572254458402), p_lower_below_threshold(0.19<0.75) |
| 53440959 | USDC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 29.037583 USDC | 0.011913 USDC | 0.000000 USDC | 0.006772 USDC | 0.005141 USDC (0.0047 €) | — | 1.77 | 0.186 (n=834) | REJECTED | below_safety_margin(5141<5807), p_lower_below_threshold(0.19<0.75) |
| 53440959 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH | 0.015046 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0032 €) | — | 1.01 | 0.186 (n=834) | REJECTED | below_safety_margin(1519358717496<3009187477175), p_lower_below_threshold(0.19<0.75) |
| 53440959 | USDC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 33.611932 USDC | 0.010195 USDC | 0.000000 USDC | 0.006772 USDC | 0.003423 USDC (0.0031 €) | — | 1.02 | 0.186 (n=834) | REJECTED | below_safety_margin(3423<6722), p_lower_below_threshold(0.19<0.75) |
| 53441325 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome_slipstream]→WETH | 0.010948 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0029 €) | — | 1.30 | 0.186 (n=834) | REJECTED | below_safety_margin(1421367305877<2189624815075), p_lower_below_threshold(0.19<0.75) |
| 53441325 | USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 24.427692 USDC | 0.009963 USDC | 0.000000 USDC | 0.006772 USDC | 0.003191 USDC (0.0029 €) | — | 1.31 | 0.186 (n=834) | REJECTED | below_safety_margin(3191<4885), p_lower_below_threshold(0.19<0.75) |
| 53440959 | WETH→[sushiswap_v3]→USDC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH | 0.011765 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0019 €) | — | 0.76 | 0.186 (n=834) | REJECTED | below_safety_margin(898832265433<2353096804546), p_lower_below_threshold(0.19<0.75) |
| 53440959 | USDC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH→[sushiswap_v3]→USDC | 26.373695 USDC | 0.008795 USDC | 0.000000 USDC | 0.006772 USDC | 0.002023 USDC (0.0019 €) | — | 0.77 | 0.186 (n=834) | REJECTED | below_safety_margin(2023<5274), p_lower_below_threshold(0.19<0.75) |
| 53441128 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 21.567849 USDC | 0.007041 USDC | 0.000000 USDC | 0.005061 USDC | 0.001980 USDC (0.0018 €) | — | 0.92 | 0.037 (n=181) | REJECTED | below_safety_margin(1980<4313), p_lower_below_threshold(0.04<0.75) |
| 53440959 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH | 0.013791 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0017 €) | — | 0.60 | 0.186 (n=834) | REJECTED | below_safety_margin(824837138189<2758227567666), p_lower_below_threshold(0.19<0.75) |
| 53440959 | USDC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 30.851438 USDC | 0.008629 USDC | 0.000000 USDC | 0.006772 USDC | 0.001857 USDC (0.0017 €) | — | 0.60 | 0.186 (n=834) | REJECTED | below_safety_margin(1857<6170), p_lower_below_threshold(0.19<0.75) |
| 53441325 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome_slipstream]→WETH | 0.008571 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0011 €) | — | 0.62 | 0.186 (n=834) | REJECTED | below_safety_margin(531732741927<1714281848466), p_lower_below_threshold(0.19<0.75) |
| 53441325 | USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→USDC | 19.155679 USDC | 0.007959 USDC | 0.000000 USDC | 0.006772 USDC | 0.001187 USDC (0.0011 €) | — | 0.62 | 0.186 (n=834) | REJECTED | below_safety_margin(1187<3831), p_lower_below_threshold(0.19<0.75) |
| 53441250 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 19.749151 USDC | 0.005882 USDC | 0.000000 USDC | 0.005059 USDC | 0.000823 USDC (0.0008 €) | — | 0.42 | 0.037 (n=181) | REJECTED | below_safety_margin(823<3949), p_lower_below_threshold(0.04<0.75) |
| 53441228 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.057749 WETH | 0.000003 WETH | 0.000000 WETH | 0.000002 WETH | 0.000000 WETH (0.0006 €) | — | 0.05 | 0.037 (n=181) | REJECTED | below_safety_margin(275823193612<11549841382431), p_lower_below_threshold(0.04<0.75) |
| 53441228 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 127.728926 USDC | 0.006012 USDC | 0.000000 USDC | 0.005402 USDC | 0.000610 USDC (0.0006 €) | — | 0.05 | 0.037 (n=181) | REJECTED | below_safety_margin(610<25545), p_lower_below_threshold(0.04<0.75) |
| 53441325 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→VIRTUAL→[uniswap_v3]→WETH | 0.018785 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0002 €) | — | 0.06 | 0.186 (n=834) | REJECTED | below_safety_margin(104695905022<3756987818337), p_lower_below_threshold(0.19<0.75) |

## Fiabilité et décision
- Observations ghost : 4779 ; taux observé 0.171 ; borne inférieure crédible (0.9) 0.164 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 16.4% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
