# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-29T11:09:53+00:00 ; durée 95.2 min ; blocs 53238564 → 53241421 (2855 vus)

## Connexion
- Requêtes RPC : 34450 ; erreurs : 25 ; latence p50/p95 : 112.1/847.2 ms
- Rafraîchissements d'état : 2856 ; âge des données au dernier bloc : 1.56 s ; changements de frais LP observés (pools à frais dynamiques) : 2878
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 18056 ; cycles déclenchés par événement : 2439 ; avance médiane sur le rafraîchissement multicall : 272 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,321.54 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 513 pools, 295 jetons, 18990 routes
- Par DEX : uniswap_v3 144, aerodrome_slipstream 118, aerodrome 209, pancakeswap_v3 28, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 181 (rejetés 2) → 586 jetons ; pools candidats 3754 (énumérés 326, par paires 0), mesurés 515, sous le plancher de 10000.0 $ : 2 → gardés 513 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'DAI': 1.0, 'USDC': 1.0, 'WETH': 2317.952116, 'cbBTC': 80065.266817, 'AERO': 0.676266}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 157,140,338 | 2,321.542811 | 53241421 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,395,272 | 0.028993 | 53241421 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,700,183 | 0.000012 | 53241421 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,381,901 | 0.028932 | 53241421 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 8,268,607 | 2,324.407578 | 53241421 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 8,141,851 | 98.533709 | 53241421 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,965,466 | 0.001638 | 53241421 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 6,626,771 | 1.459638 | 53241421 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,758,878 | 0.029000 | 53241421 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/USDC | 150 | 4,766,783 | 2,325.008997 | 53241421 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,397,719 | 2,324.862086 | 53241421 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,216,056 | 0.998880 | 53241421 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,634,176 | 38,191.794258 | 53241421 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,911,246 | 0.028948 | 53241421 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2748 | 2,471,540 | 98.587836 | 53241421 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | USDC/cbBTC | 436 | 2,337,005 | 0.000012 | 53241421 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome | WETH/FAI | 10000 | 2,120,936 | 1,214,695.556270 | 53241421 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | XDP/USDC | 100 | 1,835,522 | 0.019015 | 53241421 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome | WETH/USDC | 3000 | 1,816,343 | 2,322.437269 | 53241421 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,769,157 | 401.855255 | 53241421 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,759,028 | 0.000000 | 53241421 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,709,653 | 0.000012 | 53241421 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,697,694 | 0.000012 | 53241421 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | USDC/cbBTC | 330 | 1,601,367 | 0.000012 | 53241421 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,514,127 | 1.588199 | 53241421 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,460,116 | 0.827421 | 53241421 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,437,852 | 3,399.313201 | 53241421 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,410,332 | 0.005409 | 53241421 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,374,701 | 13,857.651548 | 53241421 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,266,304 | 2,324.314057 | 53241421 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,229,044 | 0.000263 | 53241421 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | USDC/SEND | 3000 | 1,189,801 | 68.642527 | 53241421 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,143,800 | 36,689,161.244872 | 53241421 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | WETH/WELL | 10000 | 1,139,060 | 1,088,550.659539 | 53241421 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome | VIRTUAL/WETH | 10000 | 1,136,594 | 0.000263 | 53241421 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,099,370 | 509,179.099119 | 53241421 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,077,428 | 0.000000 | 53241421 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | WETH/AERO | 10000 | 1,054,024 | 3,422.772172 | 53241421 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,053,794 | 21,679,979.074370 | 53241421 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome | WETH/EDEL | 7000 | 1,047,288 | 75,019.709682 | 53241421 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,047,059 | 16.685094 | 53241421 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v2 | WETH/USDC | 3000 | 1,026,014 | 2,321.817125 | 53241421 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome | USDC/NOCK | 3000 | 1,012,586 | 61.053992 | 53241421 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | USDC/VVV | 3000 | 988,749 | 0.042418 | 53241421 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/VVV | 10000 | 987,102 | 98.043733 | 53241421 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/USDC | 10000 | 935,837 | 2,314.580420 | 53241421 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 915,733 | 1,066.372889 | 53241421 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | uXRP/WETH | 3000 | 892,324 | 0.000554 | 53241421 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 866,636 | 18.407866 | 53241421 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 863,781 | 0.067690 | 53241421 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/msETH (stable) | 500 | 858,153 | 2.329231 | 53241421 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 838,082 | 17.517829 | 53241421 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | WETH/wstETH | 3000 | 785,706 | 0.803812 | 53241421 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 743,829 | 0.000009 | 53241421 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 742,043 | 4,621,763.171336 | 53241421 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 740,522 | 0.611008 | 53241421 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/NPC | 3000 | 695,006 | 140,537.914498 | 53241421 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 683,975 | 509,258.851011 | 53241421 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | TIG/USDC | 10000 | 650,369 | 0.534022 | 53241421 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 631,703 | 0.097911 | 53241421 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |

## Recherche d'opportunités
- Cycles : 5294 ; routes examinées : 100533060 ; candidats optimisés : 308714 ; net attendu > 0 : 127 ; dernier cycle 120.3 ms
- Rejets (moteur) : {'spread_below_threshold': 99064407, 'liquidity_below_min': 1144057, 'negative_expected_net': 308587, 'unquotable': 10588, 'borrow_bound_too_small': 5294}
- Enregistrements de la session : 308714 ; net attendu > 0 : 127 ; simulés (eth_call de la vraie tx) : 13 (ok 10, échec 3) ; étiquettes ghost N+1 : 1/10 positives
- Décisions : {'REJECTED': 308714} ; motifs de rejet : {'below_safety_margin': 79, 'negative_expected_net': 308587, 'p_lower_below_threshold': 113, 'reliability_not_demonstrated': 14, 'simulation_failed': 3}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53240395 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→AERO→[uniswap_v3]→USDC | 158.328234 USDC | 0.095113 USDC | 0.000000 USDC | 0.006969 USDC | 0.088144 USDC (0.0811 €) | — | 5.57 | 0.098 (n=336) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53240395 | WETH→[uniswap_v3]→AERO→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.068238 WETH | 0.000041 WETH | 0.000000 WETH | 0.000003 WETH | 0.000038 WETH (0.0809 €) | 0.000038 WETH | 5.56 | 0.098 (n=336) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53240395 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC | 142.168352 USDC | 0.084555 USDC | 0.000000 USDC | 0.006969 USDC | 0.077586 USDC (0.0714 €) | — | 5.46 | 0.098 (n=336) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53240395 | WETH→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.061509 WETH | 0.000036 WETH | 0.000000 WETH | 0.000003 WETH | 0.000033 WETH (0.0712 €) | 0.000033 WETH | 5.43 | 0.098 (n=336) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53240395 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→AERO→[uniswap_v3]→USDC | 141.519830 USDC | 0.082593 USDC | 0.000000 USDC | 0.007321 USDC | 0.075272 USDC (0.0693 €) | — | 5.32 | 0.138 (n=187) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 53240395 | WETH→[uniswap_v3]→AERO→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.061011 WETH | 0.000036 WETH | 0.000000 WETH | 0.000003 WETH | 0.000032 WETH (0.0691 €) | 0.000032 WETH | 5.31 | 0.138 (n=187) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 53240395 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC | 128.279120 USDC | 0.073907 USDC | 0.000000 USDC | 0.007321 USDC | 0.066586 USDC (0.0613 €) | — | 5.19 | 0.138 (n=187) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 53240395 | WETH→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.055286 WETH | 0.000032 WETH | 0.000000 WETH | 0.000003 WETH | 0.000029 WETH (0.0611 €) | — | 5.18 | 0.138 (n=187) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 53240395 | cbBTC→[uniswap_v3]→AERO→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.000805 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0339 €) | — | 5.71 | 0.098 (n=336) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53240395 | USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→AERO→[uniswap_v3]→USDC | 69.245283 USDC | 0.043678 USDC | 0.000000 USDC | 0.006969 USDC | 0.036709 USDC (0.0338 €) | — | 5.30 | 0.098 (n=336) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53240395 | USDC→[aerodrome]→WETH→[uniswap_v3]→AERO→[uniswap_v3]→USDC | 76.318974 USDC | 0.028564 USDC | 0.000000 USDC | 0.006649 USDC | 0.021915 USDC (0.0202 €) | — | 2.87 | 0.146 (n=123) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 53240395 | WETH→[uniswap_v3]→AERO→[uniswap_v3]→USDC→[aerodrome]→WETH | 0.032910 WETH | 0.000012 WETH | 0.000000 WETH | 0.000003 WETH | 0.000009 WETH (0.0201 €) | — | 2.86 | 0.146 (n=123) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 53240395 | cbBTC→[uniswap_v3]→AERO→[uniswap_v3]→USDC→[aerodrome_slipstream]→cbBTC | 0.000635 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0192 €) | — | 4.09 | 0.138 (n=187) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 53240395 | USDC→[aerodrome_slipstream]→cbBTC→[uniswap_v3]→AERO→[uniswap_v3]→USDC | 54.505100 USDC | 0.027629 USDC | 0.000000 USDC | 0.006969 USDC | 0.020660 USDC (0.0190 €) | — | 3.79 | 0.138 (n=187) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 53241042 | USDC→[pancakeswap_v3]→PLAY→[aerodrome_slipstream]→USDC | 32.615491 USDC | 0.025442 USDC | 0.000000 USDC | 0.005217 USDC | 0.020225 USDC (0.0186 €) | — | 6.20 | 0.009 (n=157) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.01<0.75) |
| 53238757 | USDC→[pancakeswap_v3]→ICNT→[uniswap_v3]→USDC | 40.763407 USDC | 0.024719 USDC | 0.000000 USDC | 0.005204 USDC | 0.019515 USDC (0.0180 €) | — | 4.79 | 0.009 (n=156) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.01<0.75) |
| 53240395 | USDC→[sushiswap_v3]→WETH→[uniswap_v3]→AERO→[uniswap_v3]→USDC | 64.935458 USDC | 0.026060 USDC | 0.000000 USDC | 0.006969 USDC | 0.019091 USDC (0.0176 €) | — | 2.94 | 0.165 (n=223) | REJECTED | p_lower_below_threshold(0.17<0.75) |
| 53240395 | WETH→[uniswap_v3]→AERO→[uniswap_v3]→USDC→[sushiswap_v3]→WETH | 0.027978 WETH | 0.000011 WETH | 0.000000 WETH | 0.000003 WETH | 0.000008 WETH (0.0175 €) | — | 2.93 | 0.165 (n=223) | REJECTED | p_lower_below_threshold(0.17<0.75) |
| 53240395 | USDC→[aerodrome]→WETH→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC | 69.621607 USDC | 0.025564 USDC | 0.000000 USDC | 0.006649 USDC | 0.018915 USDC (0.0174 €) | — | 2.72 | 0.146 (n=123) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 53240395 | WETH→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC→[aerodrome]→WETH | 0.030043 WETH | 0.000011 WETH | 0.000000 WETH | 0.000003 WETH | 0.000008 WETH (0.0173 €) | — | 2.71 | 0.146 (n=123) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 53240395 | cbBTC→[uniswap_v3]→AERO→[uniswap_v3]→USDC→[aerodrome_slipstream]→cbBTC | 0.000562 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0169 €) | — | 4.09 | 0.138 (n=187) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 53240395 | USDC→[aerodrome_slipstream]→cbBTC→[uniswap_v3]→AERO→[uniswap_v3]→USDC | 47.319372 USDC | 0.025295 USDC | 0.000000 USDC | 0.006969 USDC | 0.018326 USDC (0.0169 €) | — | 3.87 | 0.138 (n=187) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 53240395 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→AERO→[uniswap_v3]→USDC | 38.752986 USDC | 0.025221 USDC | 0.000000 USDC | 0.007321 USDC | 0.017900 USDC (0.0165 €) | — | 4.62 | 0.138 (n=187) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 53240395 | WETH→[uniswap_v3]→AERO→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.016710 WETH | 0.000011 WETH | 0.000000 WETH | 0.000003 WETH | 0.000008 WETH (0.0164 €) | — | 4.60 | 0.138 (n=187) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 53240395 | cbBTC→[uniswap_v3]→AERO→[uniswap_v3]→USDC→[uniswap_v3]→cbBTC | 0.000559 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0162 €) | — | 3.94 | 0.138 (n=187) | REJECTED | p_lower_below_threshold(0.14<0.75) |

## Fiabilité et décision
- Observations ghost : 3111 ; taux observé 0.100 ; borne inférieure crédible (0.9) 0.093 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 9.3% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
