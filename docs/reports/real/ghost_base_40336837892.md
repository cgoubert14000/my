# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-26T14:49:56+00:00 ; durée 36.82 min ; blocs 53117317 → 53118424 (1095 vus)

## Connexion
- Requêtes RPC : 13478 ; erreurs : 55 ; latence p50/p95 : 80.1/1,003.7 ms
- Rafraîchissements d'état : 1096 ; âge des données au dernier bloc : 2.77 s ; changements de frais LP observés (pools à frais dynamiques) : 3372
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 10338 ; cycles déclenchés par événement : 623 ; avance médiane sur le rafraîchissement multicall : 1,454 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,315.05 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 529 pools, 304 jetons, 19426 routes
- Par DEX : uniswap_v3 143, aerodrome 213, aerodrome_slipstream 128, pancakeswap_v3 29, uniswap_v2 13, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 189 (rejetés 2) → 594 jetons ; pools candidats 3787 (énumérés 341, par paires 0), mesurés 532, sous le plancher de 10000.0 $ : 3 → gardés 529 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2307.602823, 'cbBTC': 79842.460004, 'AERO': 0.67568}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 157,768,598 | 2,315.122626 | 53118424 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,705,949 | 0.028970 | 53118423 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,147,839 | 0.028964 | 53118423 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,455,918 | 0.000012 | 53118423 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome | WETH/VVV | 3000 | 8,843,795 | 92.721254 | 53118423 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/USDC | 500 | 8,313,967 | 2,320.915140 | 53118424 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | USDC/AERO | 3000 | 7,161,922 | 1.451816 | 53118423 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,994,650 | 0.001658 | 53118423 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,345,929 | 0.028965 | 53118423 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/USDC | 818 | 5,331,620 | 2,321.688220 | 53118424 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,454,598 | 2,321.886846 | 53118424 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,205,593 | 0.999582 | 53118423 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,793,369 | 34,862.475723 | 53118423 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/USDC | 3000 | 3,360,920 | 2,315.036687 | 53118423 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 3,195,863 | 0.028949 | 53118423 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2811 | 2,500,180 | 92.723641 | 53118423 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | USDC/cbBTC | 600 | 2,472,527 | 0.000012 | 53118423 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,200,360 | 405.229039 | 53118423 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | WETH/FAI | 10000 | 2,118,901 | 1,210,234.968788 | 53118423 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,885,988 | 0.000013 | 53118423 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,880,207 | 0.000000 | 53118423 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,816,066 | 0.018444 | 53118423 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,711,773 | 0.000012 | 53118423 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | USDC/cbBTC | 376 | 1,695,886 | 0.000012 | 53118423 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | VIRTUAL/WETH | 10000 | 1,550,336 | 0.000265 | 53118423 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,511,878 | 0.005899 | 53118423 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,460,402 | 0.825253 | 53118423 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,453,150 | 1.698035 | 53118423 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | WETH/AERO | 3000 | 1,445,339 | 3,367.854284 | 53118423 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,366,337 | 13,986.901184 | 53118423 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,230,307 | 0.000267 | 53118423 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | USDC/SEND | 3000 | 1,221,560 | 65.119739 | 53118423 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome | WETH/AERO | 10000 | 1,219,776 | 3,391.667395 | 53118423 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,209,054 | 2,320.947015 | 53118424 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | DRB/WETH | 10000 | 1,165,855 | 0.000000 | 53118423 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | WETH/WELL | 10000 | 1,134,265 | 1,092,963.116433 | 53118423 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/doginme | 10000 | 1,129,947 | 37,579,806.280132 | 53118423 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,104,416 | 498,719.396387 | 53118423 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,066,412 | 20,085,608.129299 | 53118423 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome | WETH/EDEL | 7000 | 1,064,749 | 72,445.739323 | 53118423 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | USDC/NOCK | 3000 | 1,055,881 | 56.181041 | 53118423 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,029,964 | 17.439235 | 53118424 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | USDC/VVV | 3000 | 975,566 | 0.039959 | 53118423 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/USDC | 10000 | 931,685 | 2,311.179728 | 53118423 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome | WETH/msETH (stable) | 500 | 905,109 | 2.308515 | 53118423 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | uXRP/WETH | 3000 | 892,163 | 0.000557 | 53118423 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| uniswap_v3 | WETH/MORPHO | 3000 | 881,548 | 1,137.061738 | 53118423 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 880,310 | 17.018075 | 53118423 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome_slipstream | USDC/SAPIEN | 4560 | 878,976 | 17.972393 | 53118423 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v3 | WETH/VVV | 10000 | 869,230 | 93.363735 | 53118423 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v2 | WETH/USDC | 3000 | 843,922 | 2,314.798006 | 53118423 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 806,024 | 0.000009 | 53118423 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| pancakeswap_v3 | QUID/USDC | 100 | 799,107 | 0.057274 | 53118423 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 783,837 | 0.803142 | 53118423 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 743,324 | 0.619644 | 53118424 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 730,455 | 4,741,912.428264 | 53118423 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v2 | WETH/NPC | 3000 | 698,792 | 138,149.730166 | 53118423 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| uniswap_v3 | TIG/USDC | 10000 | 698,257 | 0.613395 | 53118423 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | WETH/BRETT | 2135 | 690,145 | 494,765.702946 | 53118423 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 681,322 | 0.110779 | 53118423 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |

## Recherche d'opportunités
- Cycles : 1718 ; routes examinées : 33373868 ; candidats optimisés : 96802 ; net attendu > 0 : 245 ; dernier cycle 212.8 ms
- Rejets (moteur) : {'spread_below_threshold': 32777145, 'liquidity_below_min': 464643, 'negative_expected_net': 96557, 'unquotable': 33560, 'borrow_bound_too_small': 1718}
- Enregistrements de la session : 96802 ; net attendu > 0 : 245 ; simulés (eth_call de la vraie tx) : 12 (ok 3, échec 9) ; étiquettes ghost N+1 : 0/12 positives
- Décisions : {'REJECTED': 96802} ; motifs de rejet : {'below_safety_margin': 210, 'negative_expected_net': 96557, 'p_lower_below_threshold': 214, 'price_impact': 4, 'reliability_not_demonstrated': 31, 'simulation_failed': 9}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53117984 | USDC→[pancakeswap_v3]→PLAY→[aerodrome_slipstream]→USDC | 86.226081 USDC | 0.161516 USDC | 0.000000 USDC | 0.005222 USDC | 0.156294 USDC (0.1438 €) | — | 18.13 | 0.000 (n=52) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 53118377 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 1,240.658245 USDC | 0.099339 USDC | 0.000000 USDC | 0.005572 USDC | 0.093767 USDC (0.0863 €) | — | 0.76 | 0.022 (n=95) | REJECTED | below_safety_margin(93767<248131), p_lower_below_threshold(0.02<0.75) |
| 53118377 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.537206 WETH | 0.000043 WETH | 0.000000 WETH | 0.000002 WETH | 0.000040 WETH (0.0860 €) | — | 0.75 | 0.022 (n=95) | REJECTED | below_safety_margin(40441239565660<107441233745586), p_lower_below_threshold(0.02<0.75) |
| 53118362 | USDC→[pancakeswap_v3]→PLAY→[aerodrome_slipstream]→USDC | 65.570830 USDC | 0.094423 USDC | 0.000000 USDC | 0.005574 USDC | 0.088849 USDC (0.0817 €) | — | 13.55 | 0.000 (n=53) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 53117512 | USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 166.418370 USDC | 0.044255 USDC | 0.000000 USDC | 0.001203 USDC | 0.043052 USDC (0.0396 €) | — | 2.59 | 0.138 (n=346) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 53117512 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH | 0.071718 WETH | 0.000019 WETH | 0.000000 WETH | 0.000001 WETH | 0.000019 WETH (0.0395 €) | 0.000019 WETH | 2.59 | 0.138 (n=346) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 53117512 | USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 493.169353 USDC | 0.029918 USDC | 0.000000 USDC | 0.001203 USDC | 0.028715 USDC (0.0264 €) | — | 0.58 | 0.138 (n=346) | REJECTED | below_safety_margin(28715<98633), p_lower_below_threshold(0.14<0.75) |
| 53117512 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH | 0.214196 WETH | 0.000013 WETH | 0.000000 WETH | 0.000001 WETH | 0.000012 WETH (0.0261 €) | — | 0.57 | 0.138 (n=346) | REJECTED | below_safety_margin(12232716902053<42839285508129), p_lower_below_threshold(0.14<0.75) |
| 53117512 | cbBTC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.005431 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0257 €) | — | 0.64 | 0.138 (n=346) | REJECTED | below_safety_margin(35<108), p_lower_below_threshold(0.14<0.75) |
| 53118377 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 249.559710 USDC | 0.027838 USDC | 0.000000 USDC | 0.005572 USDC | 0.022266 USDC (0.0205 €) | — | 0.89 | 0.022 (n=95) | REJECTED | below_safety_margin(22266<49911), p_lower_below_threshold(0.02<0.75) |
| 53118377 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.108302 WETH | 0.000012 WETH | 0.000000 WETH | 0.000002 WETH | 0.000010 WETH (0.0204 €) | — | 0.89 | 0.022 (n=95) | REJECTED | below_safety_margin(9599547141433<21660368315119), p_lower_below_threshold(0.02<0.75) |
| 53118363 | cbBTC→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC→[aerodrome_slipstream]→cbBTC | 0.000958 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0176 €) | — | 2.51 | 0.182 (n=178) | REJECTED | p_lower_below_threshold(0.18<0.75) |
| 53117512 | USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 101.471583 USDC | 0.020275 USDC | 0.000000 USDC | 0.001203 USDC | 0.019072 USDC (0.0175 €) | — | 1.88 | 0.182 (n=178) | REJECTED | below_safety_margin(19072<20294), p_lower_below_threshold(0.18<0.75) |
| 53117512 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH | 0.043976 WETH | 0.000009 WETH | 0.000000 WETH | 0.000001 WETH | 0.000008 WETH (0.0175 €) | — | 1.87 | 0.182 (n=178) | REJECTED | below_safety_margin(8216505034538<8795280748470), p_lower_below_threshold(0.18<0.75) |
| 53118363 | USDC→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC | 87.316834 USDC | 0.025736 USDC | 0.000000 USDC | 0.006986 USDC | 0.018750 USDC (0.0173 €) | — | 2.15 | 0.182 (n=178) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.18<0.75) |
| 53118363 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC | 87.324553 USDC | 0.025215 USDC | 0.000000 USDC | 0.006986 USDC | 0.018229 USDC (0.0168 €) | — | 2.09 | 0.137 (n=347) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.14<0.75) |
| 53118363 | cbBTC→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.000820 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0161 €) | — | 2.68 | 0.137 (n=347) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 53118363 | USDC→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC | 79.855970 USDC | 0.023991 USDC | 0.000000 USDC | 0.006986 USDC | 0.017005 USDC (0.0156 €) | — | 2.13 | 0.182 (n=178) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.18<0.75) |
| 53118363 | cbBTC→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC→[aerodrome_slipstream]→cbBTC | 0.000908 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0154 €) | — | 2.31 | 0.182 (n=178) | REJECTED | p_lower_below_threshold(0.18<0.75) |
| 53118363 | USDC→[uniswap_v3]→cbBTC→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC | 87.309904 USDC | 0.023069 USDC | 0.000000 USDC | 0.006986 USDC | 0.016083 USDC (0.0148 €) | — | 1.84 | 0.182 (n=178) | REJECTED | below_safety_margin(16083<17461), p_lower_below_threshold(0.18<0.75) |
| 53118363 | cbBTC→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC→[uniswap_v3]→cbBTC | 0.000845 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0147 €) | — | 2.37 | 0.182 (n=178) | REJECTED | p_lower_below_threshold(0.18<0.75) |
| 53118377 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 223.650595 USDC | 0.020890 USDC | 0.000000 USDC | 0.005221 USDC | 0.015669 USDC (0.0144 €) | — | 0.70 | 0.018 (n=16) | REJECTED | below_safety_margin(15669<44730), reliability_not_demonstrated |
| 53118377 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.096231 WETH | 0.000009 WETH | 0.000000 WETH | 0.000002 WETH | 0.000007 WETH (0.0144 €) | — | 0.70 | 0.018 (n=16) | REJECTED | below_safety_margin(6754177209929<19246129910878), reliability_not_demonstrated |
| 53117541 | USDC→[aerodrome_slipstream]→USDT→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 127.494300 USDC | 0.022226 USDC | 0.000000 USDC | 0.007010 USDC | 0.015216 USDC (0.0140 €) | — | 1.19 | 0.182 (n=178) | REJECTED | below_safety_margin(15216<25498), p_lower_below_threshold(0.18<0.75) |
| 53117541 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→USDT→[uniswap_v3]→WETH | 0.054928 WETH | 0.000010 WETH | 0.000000 WETH | 0.000003 WETH | 0.000007 WETH (0.0139 €) | — | 1.19 | 0.182 (n=178) | REJECTED | below_safety_margin(6541833503514<10985597991880), p_lower_below_threshold(0.18<0.75) |

## Fiabilité et décision
- Observations ghost : 2636 ; taux observé 0.094 ; borne inférieure crédible (0.9) 0.087 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 8.7% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
