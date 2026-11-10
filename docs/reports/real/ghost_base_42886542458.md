# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-10T23:14:33+00:00 ; durée 214.26 min ; blocs 55746173 → 55810426 (3039 vus)

## Connexion
- Requêtes RPC : 104196 ; erreurs : 100 ; latence p50/p95 : 331.3/1,429.5 ms
- Rafraîchissements d'état : 3039 ; âge des données au dernier bloc : 9.08 s ; changements de frais LP observés (pools à frais dynamiques) : 4818
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 11569 ; cycles déclenchés par événement : 3135 ; avance médiane sur le rafraîchissement multicall : 642 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,046.90 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 461 pools, 269 jetons, 15520 routes
- Par DEX : uniswap_v3 132, aerodrome_slipstream 98, aerodrome 190, pancakeswap_v3 28, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 1
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 163 (rejetés 2) → 568 jetons ; pools candidats 3640 (énumérés 285, par paires 0), mesurés 463, sous le plancher de 10000.0 $ : 2 → gardés 461 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'DAI': 1.0, 'USDC': 1.0, 'WETH': 2041.615001, 'cbBTC': 73281.760168, 'AERO': 0.54062}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 133,521,309 | 2,046.896144 | 55810454 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,360,546 | 0.027796 | 55810454 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 8,532,777 | 0.027851 | 55810454 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 8,318,233 | 0.000014 | 55810454 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 7,034,018 | 2,045.653761 | 55810454 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 6,791,220 | 105.849895 | 55810454 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,314,965 | 0.027805 | 55810454 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 4,299,456 | 1.843179 | 55810454 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,873,919 | 0.999938 | 55810454 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| pancakeswap_v3 | WETH/USDC | 100 | 3,866,686 | 2,046.407995 | 55810454 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | WETH/KTA | 3000 | 3,046,723 | 42,241.364698 | 55810454 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 150 | 2,916,469 | 2,046.475162 | 55810454 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,267,088 | 0.027812 | 55810454 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 1,945,575 | 1,121,998.074522 | 55810454 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,681,125 | 0.000014 | 55810454 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | XDP/USDC | 100 | 1,620,853 | 0.016373 | 55810454 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | USDC/cbBTC | 460 | 1,618,231 | 0.000014 | 55810454 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,546,854 | 0.000000 | 55810454 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,528,602 | 0.006680 | 55810454 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,462,489 | 0.823771 | 55810454 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,434,937 | 1.411479 | 55810454 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,424,470 | 0.000014 | 55810454 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,414,731 | 415.883772 | 55810454 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v2 | WETH/USDC | 3000 | 1,268,545 | 2,047.482287 | 55810454 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| uniswap_v3 | WETH/AERO | 3000 | 1,261,658 | 3,765.273009 | 55810454 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,229,974 | 14,959.197917 | 55810454 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/USDC | 3000 | 1,155,510 | 2,048.278391 | 55810454 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome | USDC/SEND | 3000 | 1,064,057 | 85.824177 | 55810454 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,050,893 | 2,045.785196 | 55810454 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | WETH/doginme | 10000 | 1,040,500 | 33,451,923.663241 | 55810454 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome_slipstream | USDC/VELVET | 100 | 956,415 | 21.636819 | 55810454 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/VVV | 10000 | 944,701 | 106.489601 | 55810454 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/BRETT | 10000 | 938,960 | 556,999.330809 | 55810454 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome_slipstream | USDC/cbBTC | 346 | 916,056 | 0.000014 | 55810454 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 910,349 | 0.001472 | 55810454 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| uniswap_v3 | WETH/TOSHI | 10000 | 905,104 | 22,857,397.181832 | 55810454 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | WETH/MORPHO | 3000 | 882,131 | 1,013.002707 | 55810454 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | USDC/VVV | 3000 | 879,798 | 0.051777 | 55810454 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/USDC | 10000 | 877,795 | 2,042.470303 | 55810454 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | DRB/WETH | 10000 | 862,530 | 0.000000 | 55810454 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | USDC/NOCK | 3000 | 776,835 | 77.942652 | 55810454 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 761,916 | 22.407583 | 55810454 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 760,601 | 0.051604 | 55810454 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/EDEL | 7000 | 748,044 | 114,151.571124 | 55810454 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | WETH/AERO | 10000 | 706,367 | 3,770.863155 | 55810454 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | WETH/wstETH | 3000 | 692,942 | 0.803072 | 55810454 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 653,836 | 0.526776 | 55810454 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 642,866 | 4,799,962.784482 | 55810454 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 627,981 | 0.496414 | 55810454 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/NPC | 3000 | 593,695 | 150,564.948649 | 55810454 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 586,908 | 0.000007 | 55810454 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | VIRTUAL/WETH | 10000 | 577,892 | 0.000259 | 55810454 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/BRETT | 2114 | 576,563 | 558,031.541973 | 55810454 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | FLOCK/USDC | 3000 | 556,207 | 0.037352 | 55810454 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome_slipstream | WETH/MORPHO | 2703 | 492,980 | 1,012.916963 | 55810454 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome | WETH/DRV | 3000 | 483,173 | 6,581.475062 | 55810454 | `0xaC4e562d7C6108f971321F14238E24AE2cC398ac` |
| pancakeswap_v3 | ELSA/USDC | 100 | 477,824 | 0.069391 | 55810454 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| uniswap_v3 | USDC/MORPHO | 10000 | 463,860 | 0.495049 | 55810454 | `0x2043B296fFC6b2d3bf4A3F3167d2Afb3B0FBdbEE` |
| aerodrome_slipstream | USDC/USDT | 8 | 455,045 | 1.001130 | 55810454 | `0xa41Bc0AFfbA7Fd420d186b84899d7ab2aC57fcD1` |
| uniswap_v3 | WETH/UNI | 10000 | 440,663 | 306.226543 | 55810454 | `0xAb365f161Dd501473a1ff0D2ef0dCE94E7398839` |

## Recherche d'opportunités
- Cycles : 6173 ; routes examinées : 95804960 ; candidats optimisés : 584569 ; net attendu > 0 : 1630 ; dernier cycle 463.1 ms
- Rejets (moteur) : {'spread_below_threshold': 93842109, 'liquidity_below_min': 1364525, 'negative_expected_net': 582939, 'borrow_bound_too_small': 10617, 'cycle_budget_exhausted': 1772, 'unquotable': 1368}
- Enregistrements de la session : 584569 ; net attendu > 0 : 1630 ; simulés (eth_call de la vraie tx) : 51 (ok 17, échec 34) ; étiquettes ghost N+1 : 20/50 positives
- Décisions : {'REJECTED': 584569} ; motifs de rejet : {'below_safety_margin': 1148, 'negative_expected_net': 582939, 'p_lower_below_threshold': 1610, 'price_impact': 14, 'reliability_not_demonstrated': 20, 'sim_below_estimate': 3, 'simulated_net_nonpositive': 2, 'simulation_failed': 34, 'stale_data': 816}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 55755672 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 1,575.554409 USDC | 0.620325 USDC | 0.000000 USDC | 0.004902 USDC | 0.615423 USDC (0.5662 €) | — | 3.91 | 0.079 (n=117) | REJECTED | p_lower_below_threshold(0.08<0.75) |
| 55755672 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.770860 WETH | 0.000303 WETH | 0.000000 WETH | 0.000002 WETH | 0.000301 WETH (0.5655 €) | — | 3.91 | 0.079 (n=117) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.08<0.75) |
| 55755672 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 1,399.868878 USDC | 0.581906 USDC | 0.000000 USDC | 0.004902 USDC | 0.577004 USDC (0.5308 €) | — | 4.12 | 0.073 (n=488) | REJECTED | p_lower_below_threshold(0.07<0.75) |
| 55755672 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.684636 WETH | 0.000285 WETH | 0.000000 WETH | 0.000002 WETH | 0.000282 WETH (0.5302 €) | — | 4.12 | 0.073 (n=488) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.07<0.75) |
| 55755672 | USDC→[uniswap_v3]→cbBTC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 1,557.503328 USDC | 0.531965 USDC | 0.000000 USDC | 0.006145 USDC | 0.525820 USDC (0.4838 €) | — | 3.38 | 0.309 (n=525) | REJECTED | stale_data(7512ms>4000.0), p_lower_below_threshold(0.31<0.75) |
| 55755672 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→cbBTC→[uniswap_v3]→WETH | 0.749527 WETH | 0.000260 WETH | 0.000000 WETH | 0.000003 WETH | 0.000257 WETH (0.4835 €) | — | 3.43 | 0.309 (n=525) | REJECTED | stale_data(7508ms>4000.0), simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.31<0.75) |
| 55755672 | cbBTC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→cbBTC | 0.020044 cbBTC | 0.000007 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000007 cbBTC (0.4832 €) | — | 3.57 | 0.309 (n=525) | REJECTED | stale_data(7504ms>4000.0), p_lower_below_threshold(0.31<0.75) |
| 55755672 | USDC→[uniswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 1,482.582053 USDC | 0.526246 USDC | 0.000000 USDC | 0.006145 USDC | 0.520101 USDC (0.4785 €) | — | 3.51 | 0.200 (n=1167) | REJECTED | stale_data(7489ms>4000.0), p_lower_below_threshold(0.20<0.75) |
| 55755672 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→cbBTC | 0.019681 cbBTC | 0.000007 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000007 cbBTC (0.4785 €) | — | 3.60 | 0.200 (n=1167) | REJECTED | stale_data(7480ms>4000.0), p_lower_below_threshold(0.20<0.75) |
| 55755672 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.703492 WETH | 0.000257 WETH | 0.000000 WETH | 0.000003 WETH | 0.000254 WETH (0.4780 €) | — | 3.62 | 0.200 (n=1167) | REJECTED | stale_data(7484ms>4000.0), p_lower_below_threshold(0.20<0.75) |
| 55750635 | WETH→[uniswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.522401 WETH | 0.000228 WETH | 0.000000 WETH | 0.000003 WETH | 0.000225 WETH (0.4229 €) | — | 4.31 | 0.201 (n=1164) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.20<0.75) |
| 55750635 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 1,094.278628 USDC | 0.465851 USDC | 0.000000 USDC | 0.006771 USDC | 0.459080 USDC (0.4224 €) | — | 4.20 | 0.201 (n=1164) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 55750635 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→cbBTC | 0.014660 cbBTC | 0.000006 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000006 cbBTC (0.4219 €) | — | 4.26 | 0.201 (n=1164) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 55750635 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 1,054.214208 USDC | 0.454811 USDC | 0.000000 USDC | 0.006461 USDC | 0.448350 USDC (0.4125 €) | — | 4.25 | 0.201 (n=1164) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 55750635 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC | 0.014214 cbBTC | 0.000006 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000006 cbBTC (0.4125 €) | — | 4.30 | 0.201 (n=1164) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 55750635 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.516486 WETH | 0.000223 WETH | 0.000000 WETH | 0.000003 WETH | 0.000220 WETH (0.4124 €) | — | 4.25 | 0.201 (n=1164) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.20<0.75) |
| 55755672 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 1,051.324572 USDC | 0.441903 USDC | 0.000000 USDC | 0.004902 USDC | 0.437001 USDC (0.4020 €) | — | 4.16 | 0.073 (n=488) | REJECTED | stale_data(7323ms>4000.0), p_lower_below_threshold(0.07<0.75) |
| 55755672 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.514637 WETH | 0.000216 WETH | 0.000000 WETH | 0.000002 WETH | 0.000214 WETH (0.4015 €) | — | 4.15 | 0.073 (n=488) | REJECTED | stale_data(7319ms>4000.0), p_lower_below_threshold(0.07<0.75) |
| 55750635 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.595022 WETH | 0.000215 WETH | 0.000000 WETH | 0.000002 WETH | 0.000213 WETH (0.3998 €) | — | 3.58 | 0.079 (n=116) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.08<0.75) |
| 55750635 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 1,211.693254 USDC | 0.439042 USDC | 0.000000 USDC | 0.004597 USDC | 0.434445 USDC (0.3997 €) | — | 3.59 | 0.079 (n=116) | REJECTED | p_lower_below_threshold(0.08<0.75) |
| 55755672 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 1,063.940446 USDC | 0.392701 USDC | 0.000000 USDC | 0.006765 USDC | 0.385936 USDC (0.3551 €) | — | 3.63 | 0.200 (n=1167) | REJECTED | stale_data(7434ms>4000.0), p_lower_below_threshold(0.20<0.75) |
| 55755672 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.513233 WETH | 0.000192 WETH | 0.000000 WETH | 0.000003 WETH | 0.000189 WETH (0.3547 €) | — | 3.68 | 0.200 (n=1167) | REJECTED | stale_data(7429ms>4000.0), p_lower_below_threshold(0.20<0.75) |
| 55755672 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.013585 cbBTC | 0.000005 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000005 cbBTC (0.3543 €) | — | 3.86 | 0.200 (n=1167) | REJECTED | stale_data(7424ms>4000.0), p_lower_below_threshold(0.20<0.75) |
| 55755672 | USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 1,080.506623 USDC | 0.389527 USDC | 0.000000 USDC | 0.006765 USDC | 0.382762 USDC (0.3521 €) | — | 3.54 | 0.200 (n=1167) | REJECTED | stale_data(7475ms>4000.0), p_lower_below_threshold(0.20<0.75) |
| 55755672 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH | 0.516213 WETH | 0.000191 WETH | 0.000000 WETH | 0.000003 WETH | 0.000187 WETH (0.3517 €) | — | 3.63 | 0.200 (n=1167) | REJECTED | stale_data(7470ms>4000.0), p_lower_below_threshold(0.20<0.75) |

## Fiabilité et décision
- Observations ghost : 7906 ; taux observé 0.209 ; borne inférieure crédible (0.9) 0.203 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 20.3% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
