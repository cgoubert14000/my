# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-02T19:37:38+00:00 ; durée 293.45 min ; blocs 53420649 → 53429447 (8584 vus)

## Connexion
- Requêtes RPC : 102569 ; erreurs : 35 ; latence p50/p95 : 109.9/1,257.9 ms
- Rafraîchissements d'état : 8584 ; âge des données au dernier bloc : 4.46 s ; changements de frais LP observés (pools à frais dynamiques) : 14422
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 121835 ; cycles déclenchés par événement : 10578 ; avance médiane sur le rafraîchissement multicall : 495 ms
- Gaz : base fee 0.005031 gwei ; prix ETH (pool le plus profond) : 2,247.41 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 494 pools, 286 jetons, 18656 routes
- Par DEX : uniswap_v3 138, aerodrome_slipstream 108, aerodrome 204, pancakeswap_v3 30, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 174 (rejetés 2) → 579 jetons ; pools candidats 3706 (énumérés 310, par paires 0), mesurés 497, sous le plancher de 10000.0 $ : 3 → gardés 494 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDbC': 1.0, 'USDC': 1.0, 'WETH': 2287.70349, 'cbBTC': 77760.832568, 'AERO': 0.623017}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 149,081,117 | 2,247.409945 | 53429447 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,142,318 | 0.029224 | 53429447 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,075,151 | 0.029295 | 53429447 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 8,995,824 | 0.000013 | 53429447 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 7,834,037 | 2,241.249481 | 53429447 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,506,602 | 105.751930 | 53429447 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,514,901 | 0.001554 | 53429447 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 5,372,913 | 1.663287 | 53429447 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,753,508 | 0.029213 | 53429447 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,053,341 | 2,241.452296 | 53429447 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,045,682 | 0.999919 | 53429447 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome_slipstream | WETH/USDC | 967 | 3,922,633 | 2,241.126049 | 53429447 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome | WETH/KTA | 3000 | 3,490,006 | 38,808.615216 | 53429447 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,628,048 | 0.029279 | 53429447 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2736 | 2,259,140 | 105.778204 | 53429447 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | WETH/FAI | 10000 | 2,120,144 | 1,139,208.448561 | 53429447 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 600 | 2,073,842 | 0.000013 | 53429447 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | XDP/USDC | 100 | 1,727,956 | 0.017613 | 53429447 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,651,592 | 0.000000 | 53429447 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,605,696 | 0.000013 | 53429447 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,565,074 | 0.000013 | 53429447 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,545,941 | 1.450900 | 53429447 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,523,923 | 444.856787 | 53429447 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v2 | WETH/USDC | 3000 | 1,495,008 | 2,247.638960 | 53429447 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,453,431 | 0.822643 | 53429447 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,384,783 | 3,731.845318 | 53429447 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | WETH/USDC | 3000 | 1,347,614 | 2,246.690278 | 53429447 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,307,117 | 2,241.935508 | 53429447 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,292,296 | 0.005033 | 53429447 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,271,638 | 15,197.750126 | 53429447 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome_slipstream | USDC/cbBTC | 368 | 1,259,123 | 0.000013 | 53429447 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/SEND | 3000 | 1,168,903 | 71.118536 | 53429447 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,090,723 | 38,405,256.857330 | 53429447 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,046,238 | 536,330.968886 | 53429447 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,005,164 | 22,794,286.692245 | 53429447 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | DRB/WETH | 10000 | 996,540 | 0.000000 | 53429447 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome_slipstream | USDC/VELVET | 100 | 976,704 | 20.298839 | 53429447 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | WETH/EDEL | 7000 | 961,140 | 83,409.150663 | 53429447 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/USDC | 10000 | 920,756 | 2,263.329115 | 53429447 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome | WETH/WELL | 10000 | 919,219 | 1,246,977.893805 | 53429447 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/MORPHO | 3000 | 908,460 | 1,040.608900 | 53429447 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome | USDC/NOCK | 3000 | 906,340 | 76.210474 | 53429447 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/VVV | 10000 | 899,645 | 105.988971 | 53429447 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | uXRP/WETH | 3000 | 860,297 | 0.000549 | 53429447 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| uniswap_v3 | USDC/VVV | 3000 | 856,855 | 0.047170 | 53429447 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | WETH/AERO | 10000 | 822,898 | 3,704.508938 | 53429447 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | USDC/SAPIEN | 4590 | 817,524 | 20.185434 | 53429447 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 795,730 | 0.056732 | 53429447 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 762,964 | 0.798863 | 53429447 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| aerodrome | VIRTUAL/WETH | 10000 | 716,077 | 0.000258 | 53429447 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 702,337 | 0.576225 | 53429447 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 693,941 | 4,958,854.792230 | 53429447 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 668,209 | 0.566210 | 53429447 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/NPC | 3000 | 667,152 | 143,241.585712 | 53429447 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 663,537 | 0.000008 | 53429447 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | WETH/msETH (stable) | 500 | 650,752 | 2.341382 | 53429447 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 644,620 | 538,476.714406 | 53429447 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome | WETH/bsdETH | 100 | 603,547 | 0.915126 | 53429447 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 586,360 | 0.087028 | 53429447 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| uniswap_v3 | FLOCK/USDC | 3000 | 553,112 | 0.037425 | 53429447 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |

## Recherche d'opportunités
- Cycles : 19161 ; routes examinées : 357467616 ; candidats optimisés : 1465779 ; net attendu > 0 : 2504 ; dernier cycle 782.2 ms
- Rejets (moteur) : {'spread_below_threshold': 349786325, 'liquidity_below_min': 5295037, 'negative_expected_net': 1463275, 'pool_quarantined': 787186, 'unquotable': 111242, 'borrow_bound_too_small': 19155, 'cycle_budget_exhausted': 2892}
- Enregistrements de la session : 1465779 ; net attendu > 0 : 2504 ; simulés (eth_call de la vraie tx) : 149 (ok 60, échec 89) ; étiquettes ghost N+1 : 24/113 positives
- Décisions : {'REJECTED': 1465779} ; motifs de rejet : {'below_safety_margin': 2027, 'negative_expected_net': 1463275, 'p_lower_below_threshold': 2249, 'price_impact': 398, 'reliability_not_demonstrated': 255, 'sim_below_estimate': 11, 'simulated_net_nonpositive': 7, 'simulation_failed': 89, 'stale_data': 69}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53428636 | USDC→[pancakeswap_v3]→ICNT→[uniswap_v3]→USDC | 180.311935 USDC | 0.507995 USDC | 0.000000 USDC | 0.007121 USDC | 0.500874 USDC (0.4608 €) | — | 27.78 | 0.000 (n=16) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53428032 | WETH→[pancakeswap_v3]→AUKI→[uniswap_v3]→WETH | 0.062194 WETH | 0.000140 WETH | 0.000000 WETH | 0.000002 WETH | 0.000138 WETH (0.2856 €) | — | 22.15 | 0.001 (n=15) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53421255 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.022920 cbBTC | 0.000003 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000003 cbBTC (0.2227 €) | — | 1.36 | 0.015 (n=19) | REJECTED | below_safety_margin(311<458), reliability_not_demonstrated |
| 53421255 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.806328 WETH | 0.000109 WETH | 0.000000 WETH | 0.000003 WETH | 0.000106 WETH (0.2224 €) | — | 1.31 | 0.015 (n=19) | REJECTED | below_safety_margin(105730486160810<161265691126913), reliability_not_demonstrated |
| 53421255 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 1,798.869495 USDC | 0.248913 USDC | 0.000000 USDC | 0.007636 USDC | 0.241277 USDC (0.2220 €) | — | 1.34 | 0.015 (n=19) | REJECTED | below_safety_margin(241277<359773), reliability_not_demonstrated |
| 53427335 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.693160 WETH | 0.000108 WETH | 0.000000 WETH | 0.000003 WETH | 0.000105 WETH (0.2182 €) | — | 1.51 | 0.187 (n=831) | REJECTED | below_safety_margin(105006854700363<138632093252889), p_lower_below_threshold(0.19<0.75) |
| 53427335 | cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.021185 cbBTC | 0.000003 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000003 cbBTC (0.2180 €) | — | 1.45 | 0.187 (n=831) | REJECTED | below_safety_margin(307<423), p_lower_below_threshold(0.19<0.75) |
| 53427335 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 1,552.652163 USDC | 0.243304 USDC | 0.000000 USDC | 0.007148 USDC | 0.236156 USDC (0.2173 €) | — | 1.52 | 0.187 (n=831) | REJECTED | below_safety_margin(236156<310530), p_lower_below_threshold(0.19<0.75) |
| 53423107 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 1,463.190229 USDC | 0.236997 USDC | 0.000000 USDC | 0.007581 USDC | 0.229416 USDC (0.2111 €) | — | 1.57 | 0.015 (n=19) | REJECTED | below_safety_margin(229416<292638), reliability_not_demonstrated |
| 53423107 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.018050 cbBTC | 0.000003 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000003 cbBTC (0.2108 €) | — | 1.64 | 0.015 (n=19) | REJECTED | below_safety_margin(296<360), reliability_not_demonstrated |
| 53423107 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.623407 WETH | 0.000104 WETH | 0.000000 WETH | 0.000003 WETH | 0.000101 WETH (0.2108 €) | — | 1.62 | 0.015 (n=19) | REJECTED | below_safety_margin(100913025911152<124681318574639), reliability_not_demonstrated |
| 53427335 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.017689 cbBTC | 0.000003 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000003 cbBTC (0.1903 €) | — | 1.52 | 0.041 (n=20) | REJECTED | below_safety_margin(268<353), reliability_not_demonstrated |
| 53427335 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.604517 WETH | 0.000095 WETH | 0.000000 WETH | 0.000003 WETH | 0.000092 WETH (0.1902 €) | — | 1.51 | 0.041 (n=20) | REJECTED | below_safety_margin(91526851909524<120903357080830), reliability_not_demonstrated |
| 53427335 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 1,406.773967 USDC | 0.213214 USDC | 0.000000 USDC | 0.007148 USDC | 0.206066 USDC (0.1896 €) | — | 1.46 | 0.041 (n=20) | REJECTED | below_safety_margin(206066<281354), reliability_not_demonstrated |
| 53420906 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→cbBTC | 0.015164 cbBTC | 0.000003 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000003 cbBTC (0.1868 €) | — | 1.72 | 0.039 (n=170) | REJECTED | below_safety_margin(261<303), p_lower_below_threshold(0.04<0.75) |
| 53420906 | USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 1,239.328545 USDC | 0.207693 USDC | 0.000000 USDC | 0.005181 USDC | 0.202512 USDC (0.1863 €) | — | 1.63 | 0.039 (n=170) | REJECTED | below_safety_margin(202512<247865), p_lower_below_threshold(0.04<0.75) |
| 53423107 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.558889 WETH | 0.000083 WETH | 0.000000 WETH | 0.000003 WETH | 0.000080 WETH (0.1670 €) | — | 1.43 | 0.186 (n=817) | REJECTED | below_safety_margin(79963547611790<111777767764553), p_lower_below_threshold(0.19<0.75) |
| 53423107 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.016032 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1667 €) | — | 1.46 | 0.186 (n=817) | REJECTED | below_safety_margin(234<320), p_lower_below_threshold(0.19<0.75) |
| 53423107 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 1,242.865749 USDC | 0.188376 USDC | 0.000000 USDC | 0.007237 USDC | 0.181139 USDC (0.1666 €) | — | 1.46 | 0.186 (n=817) | REJECTED | below_safety_margin(181139<248573), p_lower_below_threshold(0.19<0.75) |
| 53426301 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 1,333.888851 USDC | 0.154265 USDC | 0.000000 USDC | 0.005441 USDC | 0.148824 USDC (0.1369 €) | — | 1.12 | 0.037 (n=178) | REJECTED | below_safety_margin(148824<266777), p_lower_below_threshold(0.04<0.75) |
| 53426302 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 1,333.888851 USDC | 0.154265 USDC | 0.000000 USDC | 0.005441 USDC | 0.148824 USDC (0.1369 €) | — | 1.12 | 0.037 (n=178) | REJECTED | below_safety_margin(148824<266777), p_lower_below_threshold(0.04<0.75) |
| 53426301 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.592483 WETH | 0.000069 WETH | 0.000000 WETH | 0.000002 WETH | 0.000066 WETH (0.1368 €) | — | 1.12 | 0.037 (n=178) | REJECTED | below_safety_margin(66099892856396<118496688310974), p_lower_below_threshold(0.04<0.75) |
| 53426302 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.592483 WETH | 0.000069 WETH | 0.000000 WETH | 0.000002 WETH | 0.000066 WETH (0.1368 €) | — | 1.12 | 0.037 (n=178) | REJECTED | below_safety_margin(66099892856396<118496688310974), p_lower_below_threshold(0.04<0.75) |
| 53423107 | USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→USDC | 1,399.750949 USDC | 0.143343 USDC | 0.000000 USDC | 0.005499 USDC | 0.137844 USDC (0.1268 €) | — | 0.98 | 0.038 (n=176) | REJECTED | below_safety_margin(137844<279950), p_lower_below_threshold(0.04<0.75) |
| 53423107 | cbBTC→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.016285 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1261 €) | — | 1.09 | 0.038 (n=176) | REJECTED | below_safety_margin(177<325), p_lower_below_threshold(0.04<0.75) |

## Fiabilité et décision
- Observations ghost : 4754 ; taux observé 0.171 ; borne inférieure crédible (0.9) 0.164 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 16.4% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
