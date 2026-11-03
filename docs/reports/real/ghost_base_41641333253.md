# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-03T13:33:02+00:00 ; durée 21.41 min ; blocs 53461072 → 53461716 (633 vus)

## Connexion
- Requêtes RPC : 7452 ; erreurs : 0 ; latence p50/p95 : 237.5/1,250.7 ms
- Rafraîchissements d'état : 633 ; âge des données au dernier bloc : 2.54 s ; changements de frais LP observés (pools à frais dynamiques) : 1333
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 8895 ; cycles déclenchés par événement : 517 ; avance médiane sur le rafraîchissement multicall : 1,561 ms
- Gaz : base fee 0.005524 gwei ; prix ETH (pool le plus profond) : 2,297.08 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 492 pools, 286 jetons, 19214 routes
- Par DEX : uniswap_v3 138, aerodrome_slipstream 108, aerodrome 204 (quarantaine 1), pancakeswap_v3 28, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 174 (rejetés 2) → 579 jetons ; pools candidats 3706 (énumérés 309, par paires 0), mesurés 495, sous le plancher de 10000.0 $ : 3 → gardés 492 (max 1500) ; prix des hubs : {'USDC': 1.0, 'DAI': 1.0, 'USDbC': 1.0, 'WETH': 2276.593928, 'cbBTC': 77247.513172, 'AERO': 0.617437}
- Pools en quarantaine : 1 — aerodrome:fBOMB/AERO@0xbBf71A: simulation failed ×5 (model/chain mismatch) — until block 53461859

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 151,751,306 | 2,297.081017 | 53461716 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,536,137 | 0.029613 | 53461716 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,210,896 | 0.029543 | 53461716 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,018,267 | 0.000013 | 53461716 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 7,963,721 | 2,299.893183 | 53461716 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,748,143 | 103.697424 | 53461716 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,611,632 | 0.001573 | 53461716 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 5,436,448 | 1.576436 | 53461716 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,825,695 | 0.029610 | 53461716 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,196,487 | 2,300.354903 | 53461716 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,081,736 | 0.999818 | 53461716 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome_slipstream | WETH/USDC | 1399 | 3,926,759 | 2,299.797036 | 53461716 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome | WETH/KTA | 3000 | 3,526,209 | 39,714.819856 | 53461716 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2650 | 2,722,658 | 0.029556 | 53461716 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 2,177,156 | 1,128,607.075173 | 53461716 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | WETH/VVV | 2793 | 2,107,242 | 103.676449 | 53461716 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | USDC/cbBTC | 600 | 1,814,373 | 0.000013 | 53461716 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | XDP/USDC | 100 | 1,740,414 | 0.017839 | 53461716 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,683,415 | 0.000000 | 53461716 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,640,110 | 0.000013 | 53461716 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,560,653 | 442.193925 | 53461716 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,555,667 | 0.000013 | 53461716 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,546,556 | 1.442896 | 53461716 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v2 | WETH/USDC | 3000 | 1,511,426 | 2,296.808045 | 53461716 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,454,645 | 0.821370 | 53461716 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,438,514 | 3,623.241956 | 53461716 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | WETH/USDC | 3000 | 1,346,609 | 2,299.511424 | 53461716 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,326,018 | 2,299.842158 | 53461716 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,324,671 | 0.005074 | 53461716 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,293,708 | 14,964.339508 | 53461716 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome_slipstream | USDC/cbBTC | 386 | 1,237,870 | 0.000013 | 53461716 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/SEND | 3000 | 1,164,332 | 71.678033 | 53461716 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,129,531 | 36,906,634.524476 | 53461716 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,065,117 | 542,613.811813 | 53461716 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,042,740 | 21,820,916.175696 | 53461716 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | DRB/WETH | 10000 | 1,023,587 | 0.000000 | 53461716 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,004,514 | 18.708430 | 53461716 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | WETH/EDEL | 7000 | 965,488 | 86,353.263316 | 53461716 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/VVV | 10000 | 942,673 | 104.432053 | 53461716 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome | WETH/WELL | 10000 | 937,379 | 1,252,721.609265 | 53461716 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/USDC | 10000 | 930,668 | 2,280.553383 | 53461716 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 924,074 | 1,083.090634 | 53461716 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome | USDC/NOCK | 3000 | 911,952 | 75.275626 | 53461716 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | uXRP/WETH | 3000 | 886,226 | 0.000557 | 53461716 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| uniswap_v3 | USDC/VVV | 3000 | 885,346 | 0.045160 | 53461716 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | WETH/AERO | 10000 | 853,931 | 3,649.702832 | 53461716 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | USDC/SAPIEN | 4570 | 822,116 | 20.024535 | 53461716 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 795,060 | 0.056628 | 53461716 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 779,698 | 0.799125 | 53461716 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 732,227 | 0.590999 | 53461716 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| aerodrome | VIRTUAL/WETH | 10000 | 729,310 | 0.000257 | 53461716 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 720,866 | 4,801,658.325979 | 53461716 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 675,488 | 0.000008 | 53461716 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v2 | WETH/NPC | 3000 | 672,098 | 147,467.920574 | 53461716 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome | WETH/msETH (stable) | 500 | 664,807 | 2.343097 | 53461716 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | TIG/USDC | 10000 | 655,889 | 0.541238 | 53461716 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | WETH/BRETT | 2132 | 654,910 | 541,683.834039 | 53461716 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome | WETH/bsdETH | 100 | 617,058 | 0.914615 | 53461716 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 593,678 | 0.088624 | 53461716 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| uniswap_v3 | FLOCK/USDC | 3000 | 569,486 | 0.039074 | 53461716 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |

## Recherche d'opportunités
- Cycles : 1149 ; routes examinées : 22076886 ; candidats optimisés : 76533 ; net attendu > 0 : 180 ; dernier cycle 385.0 ms
- Rejets (moteur) : {'spread_below_threshold': 21664447, 'liquidity_below_min': 323314, 'negative_expected_net': 76353, 'pool_quarantined': 5304, 'cycle_budget_exhausted': 3547, 'unquotable': 2592, 'borrow_bound_too_small': 1149}
- Enregistrements de la session : 76533 ; net attendu > 0 : 180 ; simulés (eth_call de la vraie tx) : 16 (ok 5, échec 11) ; étiquettes ghost N+1 : 6/14 positives
- Décisions : {'REJECTED': 76533} ; motifs de rejet : {'below_safety_margin': 129, 'negative_expected_net': 76353, 'p_lower_below_threshold': 177, 'price_impact': 5, 'reliability_not_demonstrated': 3, 'sim_below_estimate': 2, 'simulated_net_nonpositive': 2, 'simulation_failed': 11}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53461592 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 863.053285 USDC | 0.058737 USDC | 0.000000 USDC | 0.005490 USDC | 0.053247 USDC (0.0490 €) | — | 0.62 | 0.035 (n=191) | REJECTED | below_safety_margin(53247<172610), p_lower_below_threshold(0.03<0.75) |
| 53461593 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 863.053285 USDC | 0.058737 USDC | 0.000000 USDC | 0.005490 USDC | 0.053247 USDC (0.0490 €) | — | 0.62 | 0.035 (n=191) | REJECTED | below_safety_margin(53247<172610), p_lower_below_threshold(0.03<0.75) |
| 53461592 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.378818 WETH | 0.000026 WETH | 0.000000 WETH | 0.000002 WETH | 0.000023 WETH (0.0488 €) | — | 0.62 | 0.035 (n=191) | REJECTED | below_safety_margin(23308414488570<75763685316246), p_lower_below_threshold(0.03<0.75) |
| 53461593 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.378818 WETH | 0.000026 WETH | 0.000000 WETH | 0.000002 WETH | 0.000023 WETH (0.0488 €) | — | 0.62 | 0.035 (n=191) | REJECTED | below_safety_margin(23308414488570<75763685316246), p_lower_below_threshold(0.03<0.75) |
| 53461592 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 264.521146 USDC | 0.024946 USDC | 0.000000 USDC | 0.005143 USDC | 0.019803 USDC (0.0182 €) | — | 0.75 | 0.025 (n=58) | REJECTED | below_safety_margin(19803<52904), p_lower_below_threshold(0.02<0.75) |
| 53461593 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 264.521146 USDC | 0.024946 USDC | 0.000000 USDC | 0.005143 USDC | 0.019803 USDC (0.0182 €) | — | 0.75 | 0.025 (n=58) | REJECTED | below_safety_margin(19803<52904), p_lower_below_threshold(0.02<0.75) |
| 53461684 | USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 128.825056 USDC | 0.026942 USDC | 0.000000 USDC | 0.007180 USDC | 0.019762 USDC (0.0182 €) | — | 1.53 | 0.187 (n=842) | REJECTED | below_safety_margin(19762<25765), p_lower_below_threshold(0.19<0.75) |
| 53461592 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.115652 WETH | 0.000011 WETH | 0.000000 WETH | 0.000002 WETH | 0.000009 WETH (0.0181 €) | — | 0.75 | 0.025 (n=58) | REJECTED | below_safety_margin(8664892176091<23130374141157), p_lower_below_threshold(0.02<0.75) |
| 53461593 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.115652 WETH | 0.000011 WETH | 0.000000 WETH | 0.000002 WETH | 0.000009 WETH (0.0181 €) | — | 0.75 | 0.025 (n=58) | REJECTED | below_safety_margin(8664892176091<23130374141157), p_lower_below_threshold(0.02<0.75) |
| 53461684 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH | 0.055825 WETH | 0.000012 WETH | 0.000000 WETH | 0.000003 WETH | 0.000009 WETH (0.0181 €) | — | 1.54 | 0.187 (n=842) | REJECTED | below_safety_margin(8594955756307<11165092531733), p_lower_below_threshold(0.19<0.75) |
| 53461684 | USDC→[uniswap_v3]→cbXRP→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 70.259060 USDC | 0.019981 USDC | 0.000000 USDC | 0.007180 USDC | 0.012801 USDC (0.0118 €) | — | 1.82 | 0.187 (n=842) | REJECTED | below_safety_margin(12801<14051), p_lower_below_threshold(0.19<0.75) |
| 53461684 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→cbXRP→[pancakeswap_v3]→WETH | 0.030395 WETH | 0.000009 WETH | 0.000000 WETH | 0.000003 WETH | 0.000006 WETH (0.0117 €) | — | 1.83 | 0.187 (n=842) | REJECTED | below_safety_margin(5564789926199<6079029873533), p_lower_below_threshold(0.19<0.75) |
| 53461686 | USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 15.321295 USDC | 0.019772 USDC | 0.000000 USDC | 0.007286 USDC | 0.012486 USDC (0.0115 €) | — | 8.15 | 0.097 (n=112) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53461686 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→WETH | 0.006666 WETH | 0.000009 WETH | 0.000000 WETH | 0.000003 WETH | 0.000005 WETH (0.0114 €) | -0.000003 WETH | 8.13 | 0.097 (n=112) | REJECTED | sim_below_estimate(281542287601<8593574021975), simulated_net_nonpositive, p_lower_below_threshold(0.10<0.75) |
| 53461200 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.115048 WETH | 0.000008 WETH | 0.000000 WETH | 0.000003 WETH | 0.000005 WETH (0.0108 €) | — | 0.45 | 0.187 (n=842) | REJECTED | below_safety_margin(5146246836645<23009588869935), p_lower_below_threshold(0.19<0.75) |
| 53461200 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.002834 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0107 €) | — | 0.53 | 0.187 (n=842) | REJECTED | below_safety_margin(15<56), p_lower_below_threshold(0.19<0.75) |
| 53461200 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 259.955727 USDC | 0.018769 USDC | 0.000000 USDC | 0.007203 USDC | 0.011566 USDC (0.0106 €) | — | 0.44 | 0.187 (n=842) | REJECTED | below_safety_margin(11566<51991), p_lower_below_threshold(0.19<0.75) |
| 53461516 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 53.941949 USDC | 0.016424 USDC | 0.000000 USDC | 0.005130 USDC | 0.011294 USDC (0.0104 €) | — | 2.09 | 0.026 (n=56) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.03<0.75) |
| 53461516 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.023898 WETH | 0.000007 WETH | 0.000000 WETH | 0.000002 WETH | 0.000005 WETH (0.0104 €) | — | 2.07 | 0.026 (n=56) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.03<0.75) |
| 53461686 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 14.408330 USDC | 0.017230 USDC | 0.000000 USDC | 0.007286 USDC | 0.009944 USDC (0.0091 €) | — | 6.90 | 0.159 (n=602) | REJECTED | p_lower_below_threshold(0.16<0.75) |
| 53461686 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.006304 WETH | 0.000007 WETH | 0.000000 WETH | 0.000003 WETH | 0.000004 WETH (0.0091 €) | — | 6.84 | 0.159 (n=602) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.16<0.75) |
| 53461654 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→AERO→[pancakeswap_v3]→WETH | 0.032017 WETH | 0.000007 WETH | 0.000000 WETH | 0.000003 WETH | 0.000004 WETH (0.0087 €) | — | 1.30 | 0.187 (n=842) | REJECTED | below_safety_margin(4160219936828<6403486750321), p_lower_below_threshold(0.19<0.75) |
| 53461516 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 51.910745 USDC | 0.014555 USDC | 0.000000 USDC | 0.005130 USDC | 0.009425 USDC (0.0087 €) | — | 1.82 | 0.026 (n=56) | REJECTED | below_safety_margin(9425<10382), p_lower_below_threshold(0.03<0.75) |
| 53461516 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.022968 WETH | 0.000006 WETH | 0.000000 WETH | 0.000002 WETH | 0.000004 WETH (0.0087 €) | — | 1.80 | 0.026 (n=56) | REJECTED | below_safety_margin(4134729814390<4593529188301), p_lower_below_threshold(0.03<0.75) |
| 53461516 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.023676 WETH | 0.000007 WETH | 0.000000 WETH | 0.000003 WETH | 0.000004 WETH (0.0081 €) | — | 1.63 | 0.187 (n=842) | REJECTED | below_safety_margin(3856343035207<4735199363378), p_lower_below_threshold(0.19<0.75) |

## Fiabilité et décision
- Observations ghost : 4849 ; taux observé 0.171 ; borne inférieure crédible (0.9) 0.164 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 16.4% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
