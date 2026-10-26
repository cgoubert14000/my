# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-26T14:19:15+00:00 ; durée 6.13 min ; blocs 53117317 → 53117503 (184 vus)

## Connexion
- Requêtes RPC : 2359 ; erreurs : 5 ; latence p50/p95 : 69.9/1,015.1 ms
- Rafraîchissements d'état : 185 ; âge des données au dernier bloc : 2.02 s ; changements de frais LP observés (pools à frais dynamiques) : 510
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 2717 ; cycles déclenchés par événement : 144 ; avance médiane sur le rafraîchissement multicall : 346 ms
- Gaz : base fee 0.005018 gwei ; prix ETH (pool le plus profond) : 2,310.34 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 529 pools, 304 jetons, 19426 routes
- Par DEX : uniswap_v3 143, aerodrome 213, aerodrome_slipstream 128, pancakeswap_v3 29, uniswap_v2 13, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 189 (rejetés 2) → 594 jetons ; pools candidats 3787 (énumérés 341, par paires 0), mesurés 532, sous le plancher de 10000.0 $ : 3 → gardés 529 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2307.602823, 'cbBTC': 79842.460004, 'AERO': 0.67568}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 157,472,724 | 2,310.339616 | 53117503 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,675,718 | 0.028965 | 53117503 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,127,741 | 0.028964 | 53117503 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,451,453 | 0.000013 | 53117503 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome | WETH/VVV | 3000 | 8,778,473 | 93.816843 | 53117503 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/USDC | 500 | 8,285,206 | 2,316.082899 | 53117503 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | USDC/AERO | 3000 | 7,183,836 | 1.473040 | 53117503 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,977,850 | 0.001657 | 53117503 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,335,167 | 0.028976 | 53117503 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/USDC | 150 | 5,333,809 | 2,316.667618 | 53117503 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,446,526 | 2,316.900600 | 53117503 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,197,821 | 0.999584 | 53117503 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,788,561 | 34,808.843801 | 53117503 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/USDC | 3000 | 3,738,597 | 2,310.099826 | 53117503 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 3,191,051 | 0.028949 | 53117503 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2700 | 2,483,024 | 93.869842 | 53117503 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | USDC/cbBTC | 484 | 2,469,524 | 0.000013 | 53117503 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,194,326 | 406.022559 | 53117503 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | WETH/FAI | 10000 | 2,114,587 | 1,210,234.968788 | 53117503 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,884,345 | 0.000013 | 53117503 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,880,106 | 0.000000 | 53117503 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,815,831 | 0.018440 | 53117503 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,709,632 | 0.000013 | 53117503 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | USDC/cbBTC | 346 | 1,693,960 | 0.000013 | 53117503 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | VIRTUAL/WETH | 10000 | 1,547,764 | 0.000265 | 53117503 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,502,164 | 0.005868 | 53117503 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,457,958 | 0.826447 | 53117503 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,453,150 | 1.698035 | 53117503 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | WETH/AERO | 3000 | 1,425,275 | 3,411.265570 | 53117503 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,362,666 | 14,019.659505 | 53117503 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,227,549 | 0.000267 | 53117503 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | WETH/AERO | 10000 | 1,222,614 | 3,435.976752 | 53117503 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | USDC/SEND | 3000 | 1,221,560 | 65.119740 | 53117503 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,203,137 | 2,316.020719 | 53117503 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | DRB/WETH | 10000 | 1,164,298 | 0.000000 | 53117503 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | WETH/WELL | 10000 | 1,132,313 | 1,092,273.529269 | 53117503 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/doginme | 10000 | 1,128,015 | 37,542,283.331259 | 53117503 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,101,674 | 499,327.370307 | 53117503 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,065,093 | 20,057,418.320076 | 53117503 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome | WETH/EDEL | 7000 | 1,064,832 | 72,139.825087 | 53117503 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | USDC/NOCK | 3000 | 1,052,550 | 56.537257 | 53117503 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,028,040 | 17.532114 | 53117503 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | USDC/VVV | 3000 | 966,808 | 0.040546 | 53117503 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/USDC | 10000 | 920,957 | 2,311.179744 | 53117503 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome | WETH/msETH (stable) | 500 | 903,266 | 2.308515 | 53117503 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | uXRP/WETH | 3000 | 888,398 | 0.000554 | 53117503 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 877,478 | 18.022108 | 53117503 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 876,383 | 17.063383 | 53117503 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| uniswap_v3 | WETH/MORPHO | 3000 | 876,336 | 1,142.047805 | 53117503 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/VVV | 10000 | 862,113 | 93.744740 | 53117503 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v2 | WETH/USDC | 3000 | 843,058 | 2,309.951415 | 53117503 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 799,822 | 0.000009 | 53117503 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| pancakeswap_v3 | QUID/USDC | 100 | 793,880 | 0.056487 | 53117503 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 782,241 | 0.803142 | 53117503 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 741,875 | 0.614846 | 53117503 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 728,619 | 4,746,432.668466 | 53117503 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v2 | WETH/NPC | 3000 | 698,920 | 137,535.922570 | 53117503 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| uniswap_v3 | TIG/USDC | 10000 | 697,844 | 0.612711 | 53117503 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | WETH/BRETT | 2096 | 688,296 | 496,755.006257 | 53117503 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 677,830 | 0.109857 | 53117503 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |

## Recherche d'opportunités
- Cycles : 328 ; routes examinées : 6371728 ; candidats optimisés : 18794 ; net attendu > 0 : 22 ; dernier cycle 325.8 ms
- Rejets (moteur) : {'spread_below_threshold': 6256258, 'liquidity_below_min': 89788, 'negative_expected_net': 18772, 'unquotable': 6560, 'borrow_bound_too_small': 328}
- Enregistrements de la session : 18794 ; net attendu > 0 : 22 ; simulés (eth_call de la vraie tx) : 2 (ok 0, échec 2) ; étiquettes ghost N+1 : 0/2 positives
- Décisions : {'REJECTED': 18794} ; motifs de rejet : {'below_safety_margin': 20, 'negative_expected_net': 18772, 'p_lower_below_threshold': 20, 'price_impact': 2, 'reliability_not_demonstrated': 2, 'simulation_failed': 2}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53117403 | USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 89.830787 USDC | 0.012120 USDC | 0.000000 USDC | 0.007015 USDC | 0.005105 USDC (0.0047 €) | — | 0.57 | 0.138 (n=346) | REJECTED | below_safety_margin(5105<17966), p_lower_below_threshold(0.14<0.75) |
| 53117403 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH | 0.039270 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0047 €) | — | 0.56 | 0.138 (n=346) | REJECTED | below_safety_margin(2198463905465<7853900261473), p_lower_below_threshold(0.14<0.75) |
| 53117481 | cbBTC→[aerodrome]→fBOMB→[aerodrome]→AERO→[aerodrome_slipstream]→cbBTC | 0.000013 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0029 €) | — | 31.90 | 0.003 (n=100) | REJECTED | price_impact(211bps>150.0), simulation_failed:revert 0xa932492f, p_lower_below_threshold(0.00<0.75) |
| 53117403 | USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 67.580373 USDC | 0.008721 USDC | 0.000000 USDC | 0.007368 USDC | 0.001353 USDC (0.0012 €) | — | 0.20 | 0.182 (n=178) | REJECTED | below_safety_margin(1353<13516), p_lower_below_threshold(0.18<0.75) |
| 53117403 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH | 0.029466 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0012 €) | — | 0.20 | 0.182 (n=178) | REJECTED | below_safety_margin(576308896429<5893138790441), p_lower_below_threshold(0.18<0.75) |
| 53117403 | USDC→[uniswap_v3]→USDT→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 73.573943 USDC | 0.008045 USDC | 0.000000 USDC | 0.007015 USDC | 0.001030 USDC (0.0009 €) | — | 0.14 | 0.138 (n=346) | REJECTED | below_safety_margin(1030<14714), p_lower_below_threshold(0.14<0.75) |
| 53117403 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→USDT→[aerodrome_slipstream]→WETH | 0.031822 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0009 €) | — | 0.14 | 0.138 (n=346) | REJECTED | below_safety_margin(437117131220<6364327788925), p_lower_below_threshold(0.14<0.75) |
| 53117403 | USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 64.443418 USDC | 0.007922 USDC | 0.000000 USDC | 0.007015 USDC | 0.000907 USDC (0.0008 €) | — | 0.14 | 0.182 (n=178) | REJECTED | below_safety_margin(907<12888), p_lower_below_threshold(0.18<0.75) |
| 53117403 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH | 0.028077 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0008 €) | — | 0.14 | 0.182 (n=178) | REJECTED | below_safety_margin(384214202984<5615438695793), p_lower_below_threshold(0.18<0.75) |
| 53117499 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 9.602124 USDC | 0.008167 USDC | 0.000000 USDC | 0.007332 USDC | 0.000835 USDC (0.0008 €) | — | 0.87 | 0.182 (n=178) | REJECTED | below_safety_margin(835<1920), p_lower_below_threshold(0.18<0.75) |
| 53117499 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.004159 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0007 €) | — | 0.85 | 0.182 (n=178) | REJECTED | below_safety_margin(352004278260<831802436256), p_lower_below_threshold(0.18<0.75) |
| 53117499 | USDC→[uniswap_v2]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 8.982079 USDC | 0.006991 USDC | 0.000000 USDC | 0.006264 USDC | 0.000727 USDC (0.0007 €) | — | 0.81 | — (n=0) | REJECTED | below_safety_margin(727<1796), reliability_not_demonstrated |
| 53117499 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[uniswap_v2]→WETH | 0.003921 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0007 €) | — | 0.78 | — (n=0) | REJECTED | below_safety_margin(306473078907<784196332544), reliability_not_demonstrated |
| 53117481 | WETH→[aerodrome]→fBOMB→[aerodrome]→AERO→[pancakeswap_v3]→WETH | 0.000433 WETH | 0.000001 WETH | 0.000000 WETH | 0.000000 WETH | 0.000000 WETH (0.0003 €) | — | 3.17 | 0.025 (n=58) | REJECTED | price_impact(205bps>150.0), simulation_failed:revert 0xa932492f, p_lower_below_threshold(0.02<0.75) |
| 53117491 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 9.266312 USDC | 0.007168 USDC | 0.000000 USDC | 0.006976 USDC | 0.000192 USDC (0.0002 €) | — | 0.21 | 0.138 (n=346) | REJECTED | below_safety_margin(192<1853), p_lower_below_threshold(0.14<0.75) |
| 53117492 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 9.266312 USDC | 0.007168 USDC | 0.000000 USDC | 0.006976 USDC | 0.000192 USDC (0.0002 €) | — | 0.21 | 0.138 (n=346) | REJECTED | below_safety_margin(192<1853), p_lower_below_threshold(0.14<0.75) |
| 53117491 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.004046 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0002 €) | — | 0.19 | 0.138 (n=346) | REJECTED | below_safety_margin(75755115801<809201255986), p_lower_below_threshold(0.14<0.75) |
| 53117492 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.004046 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0002 €) | — | 0.19 | 0.138 (n=346) | REJECTED | below_safety_margin(75755115801<809201255986), p_lower_below_threshold(0.14<0.75) |
| 53117491 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 9.113881 USDC | 0.007015 USDC | 0.000000 USDC | 0.006976 USDC | 0.000039 USDC (0.0000 €) | — | 0.04 | 0.182 (n=178) | REJECTED | below_safety_margin(39<1822), p_lower_below_threshold(0.18<0.75) |
| 53117492 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 9.113881 USDC | 0.007015 USDC | 0.000000 USDC | 0.006976 USDC | 0.000039 USDC (0.0000 €) | — | 0.04 | 0.182 (n=178) | REJECTED | below_safety_margin(39<1822), p_lower_below_threshold(0.18<0.75) |
| 53117491 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.004010 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0000 €) | — | 0.02 | 0.182 (n=178) | REJECTED | below_safety_margin(9642293109<802070766819), p_lower_below_threshold(0.18<0.75) |
| 53117492 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.004010 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0000 €) | — | 0.02 | 0.182 (n=178) | REJECTED | below_safety_margin(9642293109<802070766819), p_lower_below_threshold(0.18<0.75) |

## Fiabilité et décision
- Observations ghost : 2626 ; taux observé 0.095 ; borne inférieure crédible (0.9) 0.088 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 8.8% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
