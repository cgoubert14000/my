# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-26T11:39:12+00:00 ; durée 181.69 min ; blocs 53107248 → 53112697 (5258 vus)

## Connexion
- Requêtes RPC : 61567 ; erreurs : 0 ; latence p50/p95 : 440.9/2,626.3 ms
- Rafraîchissements d'état : 5258 ; âge des données au dernier bloc : 8.75 s ; changements de frais LP observés (pools à frais dynamiques) : 8882
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 524 ; cycles déclenchés par événement : 28 ; avance médiane sur le rafraîchissement multicall : 1,135 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,328.37 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 527 pools, 302 jetons, 19574 routes
- Par DEX : uniswap_v3 142, aerodrome 213, aerodrome_slipstream 127, pancakeswap_v3 30, uniswap_v2 12, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 188 (rejetés 2) → 593 jetons ; pools candidats 3779 (énumérés 339, par paires 0), mesurés 529, sous le plancher de 10000.0 $ : 2 → gardés 527 (max 1500) ; prix des hubs : {'USDC': 1.0, 'DAI': 1.0, 'USDbC': 1.0, 'WETH': 2317.899718, 'cbBTC': 80102.759686, 'AERO': 0.672129}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 158,284,446 | 2,328.370971 | 53112698 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 17,506,875 | 0.029002 | 53112698 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,202,992 | 0.028978 | 53112698 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,487,289 | 0.000012 | 53112698 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome | WETH/VVV | 3000 | 8,775,452 | 95.347701 | 53112698 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/USDC | 500 | 8,332,892 | 2,327.618132 | 53112698 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | USDC/AERO | 3000 | 7,095,129 | 1.513241 | 53112698 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,007,875 | 0.001650 | 53112698 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | WETH/USDC | 150 | 5,404,233 | 2,328.501615 | 53112698 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,376,884 | 0.029008 | 53112698 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,475,765 | 2,328.548410 | 53112698 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,226,306 | 0.998980 | 53112698 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,815,256 | 34,861.286787 | 53112698 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/USDC | 3000 | 3,763,584 | 2,328.161155 | 53112698 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 3,224,943 | 0.028970 | 53112698 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | USDC/cbBTC | 436 | 2,484,348 | 0.000012 | 53112698 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome_slipstream | WETH/VVV | 2712 | 2,484,204 | 95.385473 | 53112698 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,203,679 | 409.871464 | 53112698 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | WETH/FAI | 10000 | 2,131,090 | 1,210,234.968788 | 53112698 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,895,390 | 0.000000 | 53112698 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,889,334 | 0.000012 | 53112698 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v3 | XDP/USDC | 100 | 1,821,430 | 0.018541 | 53112698 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,716,636 | 0.000012 | 53112698 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | USDC/cbBTC | 338 | 1,700,354 | 0.000012 | 53112698 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | VIRTUAL/WETH | 10000 | 1,559,843 | 0.000265 | 53112698 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,458,546 | 0.825837 | 53112698 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,453,220 | 1.698035 | 53112698 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,448,303 | 0.005563 | 53112698 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v3 | WETH/AERO | 3000 | 1,407,723 | 3,523.505958 | 53112698 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,367,110 | 14,149.217976 | 53112698 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,237,113 | 0.000265 | 53112698 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,226,269 | 2,327.628725 | 53112698 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | WETH/AERO | 10000 | 1,225,626 | 3,498.670300 | 53112698 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | USDC/SEND | 3000 | 1,220,638 | 65.218151 | 53112698 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | DRB/WETH | 10000 | 1,164,589 | 0.000000 | 53112698 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | WETH/WELL | 10000 | 1,133,783 | 1,106,515.029542 | 53112698 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/doginme | 10000 | 1,133,756 | 37,860,745.964831 | 53112698 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,109,890 | 499,794.956696 | 53112698 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | WETH/EDEL | 7000 | 1,066,092 | 73,097.141160 | 53112698 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,053,433 | 20,722,960.720777 | 53112698 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome | USDC/NOCK | 3000 | 1,050,781 | 56.727708 | 53112698 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,031,283 | 17.381325 | 53112698 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | USDC/VVV | 3000 | 961,563 | 0.041042 | 53112698 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/USDC | 10000 | 924,032 | 2,312.265191 | 53112698 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome | WETH/msETH (stable) | 500 | 909,595 | 2.311243 | 53112698 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | uXRP/WETH | 3000 | 892,261 | 0.000551 | 53112698 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 879,411 | 17.185816 | 53112698 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| uniswap_v3 | WETH/MORPHO | 3000 | 875,542 | 1,154.573026 | 53112698 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 872,367 | 18.191425 | 53112698 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v3 | WETH/VVV | 10000 | 865,910 | 94.690956 | 53112698 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v2 | WETH/USDC | 3000 | 846,326 | 2,328.185157 | 53112698 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| pancakeswap_v3 | QUID/USDC | 100 | 791,660 | 0.056155 | 53112698 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 789,846 | 0.000008 | 53112698 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | WETH/wstETH | 3000 | 788,346 | 0.803142 | 53112698 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| aerodrome | weETH_04c0/WETH | 500 | 778,435 | 1.105941 | 53112698 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 746,017 | 0.615580 | 53112698 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 732,386 | 4,771,289.564501 | 53112698 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 709,557 | 0.632525 | 53112698 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/NPC | 3000 | 703,557 | 137,852.005385 | 53112698 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | WETH/BRETT | 2141 | 693,318 | 502,507.517266 | 53112698 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |

## Recherche d'opportunités
- Cycles : 5285 ; routes examinées : 103448590 ; candidats optimisés : 304617 ; net attendu > 0 : 89 ; dernier cycle 338.2 ms
- Rejets (moteur) : {'spread_below_threshold': 101757793, 'liquidity_below_min': 1273505, 'negative_expected_net': 304528, 'unquotable': 106938, 'borrow_bound_too_small': 5281, 'cycle_budget_exhausted': 456}
- Enregistrements de la session : 304617 ; net attendu > 0 : 89 ; simulés (eth_call de la vraie tx) : 1 (ok 1, échec 0) ; étiquettes ghost N+1 : 0/1 positives
- Décisions : {'REJECTED': 304617} ; motifs de rejet : {'below_safety_margin': 88, 'negative_expected_net': 304528, 'p_lower_below_threshold': 83, 'price_impact': 1, 'reliability_not_demonstrated': 6, 'stale_data': 12}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53107366 | USDC→[sushiswap_v3]→WETH→[pancakeswap_v3]→USDC | 63.193801 USDC | 0.009983 USDC | 0.000000 USDC | 0.005224 USDC | 0.004759 USDC (0.0044 €) | — | 0.75 | 0.022 (n=95) | REJECTED | below_safety_margin(4759<12638), p_lower_below_threshold(0.02<0.75) |
| 53107366 | WETH→[pancakeswap_v3]→USDC→[sushiswap_v3]→WETH | 0.027089 WETH | 0.000004 WETH | 0.000000 WETH | 0.000002 WETH | 0.000002 WETH (0.0044 €) | — | 0.75 | 0.022 (n=95) | REJECTED | below_safety_margin(2036524520673<5417835819103), p_lower_below_threshold(0.02<0.75) |
| 53108445 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 19.494862 USDC | 0.008361 USDC | 0.000000 USDC | 0.005220 USDC | 0.003141 USDC (0.0029 €) | — | 1.61 | 0.022 (n=95) | REJECTED | below_safety_margin(3141<3898), p_lower_below_threshold(0.02<0.75) |
| 53108189 | WETH→[aerodrome]→doginme→[uniswap_v3]→WETH | 0.000430 WETH | 0.000003 WETH | 0.000000 WETH | 0.000002 WETH | 0.000001 WETH (0.0028 €) | 0.000001 WETH | 30.08 | 0.000 (n=22) | REJECTED | price_impact(200bps>150.0), reliability_not_demonstrated |
| 53111495 | WETH→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.030554 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0025 €) | — | 0.39 | 0.184 (n=176) | REJECTED | below_safety_margin(1188648585199<6110749115033), p_lower_below_threshold(0.18<0.75) |
| 53111495 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→USDC | 71.077813 USDC | 0.009753 USDC | 0.000000 USDC | 0.006997 USDC | 0.002756 USDC (0.0025 €) | — | 0.39 | 0.184 (n=176) | REJECTED | below_safety_margin(2756<14215), p_lower_below_threshold(0.18<0.75) |
| 53108357 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.004713 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0015 €) | — | 1.52 | 0.133 (n=344) | REJECTED | below_safety_margin(716090095945<942632439736), p_lower_below_threshold(0.13<0.75) |
| 53108357 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 10.864719 USDC | 0.008636 USDC | 0.000000 USDC | 0.006986 USDC | 0.001650 USDC (0.0015 €) | — | 1.52 | 0.133 (n=344) | REJECTED | below_safety_margin(1650<2172), p_lower_below_threshold(0.13<0.75) |
| 53107366 | USDC→[aerodrome]→wIRON→[uniswap_v2]→WETH→[pancakeswap_v3]→USDC | 11.240663 USDC | 0.007586 USDC | 0.000000 USDC | 0.005948 USDC | 0.001638 USDC (0.0015 €) | — | 1.46 | 0.128 (n=17) | REJECTED | below_safety_margin(1638<2248), reliability_not_demonstrated |
| 53107366 | WETH→[pancakeswap_v3]→USDC→[aerodrome]→wIRON→[uniswap_v2]→WETH | 0.004869 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0015 €) | — | 1.43 | 0.128 (n=17) | REJECTED | below_safety_margin(695529570407<973860427537), reliability_not_demonstrated |
| 53108466 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→tBTC→[pancakeswap_v3]→cbBTC | 0.000380 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0015 €) | — | 0.53 | 0.133 (n=344) | REJECTED | below_safety_margin(2<7), p_lower_below_threshold(0.13<0.75) |
| 53110434 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.004567 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0014 €) | — | 1.41 | 0.184 (n=176) | REJECTED | below_safety_margin(642255198934<913433673864), p_lower_below_threshold(0.18<0.75) |
| 53110434 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 10.577855 USDC | 0.008490 USDC | 0.000000 USDC | 0.006998 USDC | 0.001492 USDC (0.0014 €) | — | 1.41 | 0.184 (n=176) | REJECTED | below_safety_margin(1492<2115), p_lower_below_threshold(0.18<0.75) |
| 53109323 | USDC→[uniswap_v2]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 9.943159 USDC | 0.007743 USDC | 0.000000 USDC | 0.006271 USDC | 0.001472 USDC (0.0014 €) | — | 1.48 | — (n=0) | REJECTED | below_safety_margin(1472<1988), reliability_not_demonstrated |
| 53109323 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[uniswap_v2]→WETH | 0.004291 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0013 €) | — | 1.45 | — (n=0) | REJECTED | below_safety_margin(623353371290<858295434485), reliability_not_demonstrated |
| 53108466 | USDC→[aerodrome_slipstream]→tBTC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 29.230978 USDC | 0.008269 USDC | 0.000000 USDC | 0.006987 USDC | 0.001282 USDC (0.0012 €) | — | 0.44 | 0.133 (n=344) | REJECTED | below_safety_margin(1282<5846), p_lower_below_threshold(0.13<0.75) |
| 53109419 | USDC→[aerodrome]→PLAY→[pancakeswap_v3]→USDC | 8.034931 USDC | 0.006178 USDC | 0.000000 USDC | 0.004906 USDC | 0.001272 USDC (0.0012 €) | — | 1.58 | 0.001 (n=12) | REJECTED | below_safety_margin(1272<1606), reliability_not_demonstrated |
| 53107313 | USDC→[aerodrome_slipstream]→tBTC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 30.930355 USDC | 0.007910 USDC | 0.000000 USDC | 0.006981 USDC | 0.000929 USDC (0.0009 €) | — | 0.30 | 0.133 (n=344) | REJECTED | below_safety_margin(929<6186), p_lower_below_threshold(0.13<0.75) |
| 53111436 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.004352 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0008 €) | — | 0.86 | 0.133 (n=344) | REJECTED | below_safety_margin(373308134208<870372426836), p_lower_below_threshold(0.13<0.75) |
| 53111436 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 10.035532 USDC | 0.007863 USDC | 0.000000 USDC | 0.006997 USDC | 0.000866 USDC (0.0008 €) | — | 0.86 | 0.133 (n=344) | REJECTED | below_safety_margin(866<2007), p_lower_below_threshold(0.13<0.75) |
| 53108466 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→tBTC→[aerodrome_slipstream]→cbBTC | 0.000378 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0007 €) | — | 0.26 | 0.133 (n=344) | REJECTED | below_safety_margin(1<7), p_lower_below_threshold(0.13<0.75) |
| 53107313 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→tBTC→[pancakeswap_v3]→cbBTC | 0.000380 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0007 €) | — | 0.26 | 0.133 (n=344) | REJECTED | below_safety_margin(1<7), p_lower_below_threshold(0.13<0.75) |
| 53107313 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→tBTC→[aerodrome_slipstream]→cbBTC | 0.000379 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0007 €) | — | 0.26 | 0.133 (n=344) | REJECTED | below_safety_margin(1<7), p_lower_below_threshold(0.13<0.75) |
| 53108466 | USDC→[aerodrome_slipstream]→tBTC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 30.430720 USDC | 0.007783 USDC | 0.000000 USDC | 0.006987 USDC | 0.000796 USDC (0.0007 €) | — | 0.26 | 0.133 (n=344) | REJECTED | below_safety_margin(796<6086), p_lower_below_threshold(0.13<0.75) |
| 53107313 | USDC→[aerodrome_slipstream]→tBTC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 30.898475 USDC | 0.007709 USDC | 0.000000 USDC | 0.006981 USDC | 0.000728 USDC (0.0007 €) | — | 0.24 | 0.133 (n=344) | REJECTED | below_safety_margin(728<6179), p_lower_below_threshold(0.13<0.75) |

## Fiabilité et décision
- Observations ghost : 2608 ; taux observé 0.095 ; borne inférieure crédible (0.9) 0.088 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 8.8% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
