# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-06T14:20:15+00:00 ; durée 9.16 min ; blocs 53919422 → 53922150 (342 vus)

## Connexion
- Requêtes RPC : 5328 ; erreurs : 0 ; latence p50/p95 : 341.8/1,695.4 ms
- Rafraîchissements d'état : 342 ; âge des données au dernier bloc : 9.84 s ; changements de frais LP observés (pools à frais dynamiques) : 301
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 420 ; cycles déclenchés par événement : 185 ; avance médiane sur le rafraîchissement multicall : 655 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,229.60 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 484 pools, 280 jetons, 17898 routes
- Par DEX : uniswap_v3 137, aerodrome_slipstream 103, aerodrome 200, pancakeswap_v3 29, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 172 (rejetés 2) → 577 jetons ; pools candidats 3743 (énumérés 302, par paires 0), mesurés 487, sous le plancher de 10000.0 $ : 3 → gardés 484 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2229.592504, 'cbBTC': 75521.601442, 'AERO': 0.600396}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 145,569,183 | 2,229.600992 | 53922179 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,669,262 | 0.029516 | 53922179 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,331,962 | 0.000013 | 53922179 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,119,370 | 0.029445 | 53922179 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 7,974,610 | 2,231.572029 | 53922179 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,343,700 | 107.719324 | 53922179 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,413,537 | 0.001560 | 53922179 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 4,870,112 | 1.665567 | 53922179 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,715,630 | 0.029524 | 53922179 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,147,475 | 2,232.260212 | 53922179 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,981,483 | 0.998492 | 53922179 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,294,594 | 42,861.321518 | 53922179 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 150 | 3,196,349 | 2,232.076866 | 53922179 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,549,022 | 0.029463 | 53922179 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 2,074,761 | 1,170,614.944842 | 53922179 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,817,877 | 0.007459 | 53922179 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/cbBTC | 508 | 1,732,003 | 0.000013 | 53922179 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,653,491 | 0.000013 | 53922179 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | XDP/USDC | 100 | 1,641,717 | 0.016514 | 53922179 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,635,478 | 0.000000 | 53922179 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,537,161 | 1.444757 | 53922179 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,526,314 | 0.000013 | 53922179 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,524,273 | 434.466283 | 53922179 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,462,125 | 0.818407 | 53922179 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,375,851 | 3,709.908769 | 53922179 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v2 | WETH/USDC | 3000 | 1,323,194 | 2,230.133697 | 53922179 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome | WETH/USDC | 3000 | 1,321,368 | 2,231.648469 | 53922179 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,268,982 | 14,722.347964 | 53922179 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,168,891 | 2,231.524729 | 53922179 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,123,886 | 76.929838 | 53922179 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,091,895 | 37,253,287.307397 | 53922179 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/VVV | 10000 | 1,042,638 | 107.061342 | 53922179 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,021,135 | 559,380.608527 | 53922179 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,019,347 | 0.000000 | 53922179 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/TOSHI | 10000 | 996,538 | 22,433,261.257503 | 53922179 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/VELVET | 100 | 984,870 | 19.806046 | 53922179 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/USDC | 10000 | 934,523 | 2,225.576719 | 53922179 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 933,059 | 1,068.711881 | 53922179 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome_slipstream | USDC/cbBTC | 350 | 921,565 | 0.000013 | 53922179 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/NOCK | 3000 | 901,293 | 77.139275 | 53922179 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome | WETH/EDEL | 7000 | 857,772 | 103,064.195038 | 53922179 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | uXRP/WETH | 3000 | 836,677 | 0.000530 | 53922179 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 812,204 | 20.439281 | 53922179 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v3 | USDC/VVV | 3000 | 804,536 | 0.048336 | 53922179 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | WETH/AERO | 10000 | 794,099 | 3,681.640183 | 53922179 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| pancakeswap_v3 | QUID/USDC | 100 | 791,771 | 0.056111 | 53922179 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 756,384 | 0.799699 | 53922179 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 724,241 | 0.578440 | 53922179 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 693,560 | 4,890,076.632358 | 53922179 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome | VIRTUAL/WETH | 10000 | 687,111 | 0.000257 | 53922179 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v2 | WETH/NPC | 3000 | 658,583 | 144,876.664384 | 53922179 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| uniswap_v3 | TIG/USDC | 10000 | 656,769 | 0.541771 | 53922179 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 650,419 | 0.000008 | 53922179 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 626,268 | 558,094.906167 | 53922179 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome | WETH/bsdETH | 100 | 597,816 | 0.913997 | 53922179 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome | WETH/msETH (stable) | 500 | 586,004 | 2.472301 | 53922179 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | FLOCK/USDC | 3000 | 559,712 | 0.037965 | 53922179 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome | cbBTC/EDGE | 7000 | 530,272 | 864,591.008798 | 53922179 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| pancakeswap_v3 | ELSA/USDC | 100 | 527,235 | 0.079153 | 53922179 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| aerodrome_slipstream | WETH/MORPHO | 2703 | 521,878 | 1,068.977260 | 53922179 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |

## Recherche d'opportunités
- Cycles : 526 ; routes examinées : 9414348 ; candidats optimisés : 45383 ; net attendu > 0 : 40 ; dernier cycle 449.3 ms
- Rejets (moteur) : {'spread_below_threshold': 9229854, 'liquidity_below_min': 138585, 'negative_expected_net': 45343, 'borrow_bound_too_small': 526}
- Enregistrements de la session : 45383 ; net attendu > 0 : 40 ; simulés (eth_call de la vraie tx) : 0 (ok 0, échec 0) ; étiquettes ghost N+1 : 0/0 positives
- Décisions : {'REJECTED': 45383} ; motifs de rejet : {'below_safety_margin': 40, 'negative_expected_net': 45343, 'p_lower_below_threshold': 40, 'stale_data': 6}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53921994 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 164.696992 USDC | 0.011222 USDC | 0.000000 USDC | 0.005035 USDC | 0.006187 USDC (0.0057 €) | — | 0.38 | 0.048 (n=242) | REJECTED | below_safety_margin(6187<32939), p_lower_below_threshold(0.05<0.75) |
| 53921994 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 164.696992 USDC | 0.011222 USDC | 0.000000 USDC | 0.005035 USDC | 0.006187 USDC (0.0057 €) | — | 0.38 | 0.048 (n=242) | REJECTED | below_safety_margin(6187<32939), p_lower_below_threshold(0.05<0.75) |
| 53921994 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.074266 WETH | 0.000005 WETH | 0.000000 WETH | 0.000002 WETH | 0.000003 WETH (0.0057 €) | — | 0.37 | 0.048 (n=242) | REJECTED | below_safety_margin(2772403998773<14853259609927), p_lower_below_threshold(0.05<0.75) |
| 53921994 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.074266 WETH | 0.000005 WETH | 0.000000 WETH | 0.000002 WETH | 0.000003 WETH (0.0057 €) | — | 0.37 | 0.048 (n=242) | REJECTED | below_safety_margin(2772403998773<14853259609927), p_lower_below_threshold(0.05<0.75) |
| 53921457 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.003957 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0009 €) | — | 1.12 | 0.236 (n=403) | REJECTED | below_safety_margin(443263711727<791322113294), stale_data(4292ms>4000.0), p_lower_below_threshold(0.24<0.75) |
| 53921458 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.003957 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0009 €) | — | 1.12 | 0.236 (n=403) | REJECTED | below_safety_margin(443263711727<791322113294), p_lower_below_threshold(0.24<0.75) |
| 53921459 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.003957 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0009 €) | — | 1.12 | 0.236 (n=403) | REJECTED | below_safety_margin(443263711727<791322113294), p_lower_below_threshold(0.24<0.75) |
| 53921460 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.003957 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0009 €) | — | 1.12 | 0.236 (n=403) | REJECTED | below_safety_margin(443263711727<791322113294), p_lower_below_threshold(0.24<0.75) |
| 53921457 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 8.757646 USDC | 0.007695 USDC | 0.000000 USDC | 0.006713 USDC | 0.000982 USDC (0.0009 €) | — | 1.12 | 0.236 (n=403) | REJECTED | below_safety_margin(982<1751), stale_data(4286ms>4000.0), p_lower_below_threshold(0.24<0.75) |
| 53921458 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 8.757646 USDC | 0.007695 USDC | 0.000000 USDC | 0.006713 USDC | 0.000982 USDC (0.0009 €) | — | 1.12 | 0.236 (n=403) | REJECTED | below_safety_margin(982<1751), p_lower_below_threshold(0.24<0.75) |
| 53921459 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 8.757646 USDC | 0.007695 USDC | 0.000000 USDC | 0.006713 USDC | 0.000982 USDC (0.0009 €) | — | 1.12 | 0.236 (n=403) | REJECTED | below_safety_margin(982<1751), p_lower_below_threshold(0.24<0.75) |
| 53921460 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 8.757646 USDC | 0.007695 USDC | 0.000000 USDC | 0.006713 USDC | 0.000982 USDC (0.0009 €) | — | 1.12 | 0.236 (n=403) | REJECTED | below_safety_margin(982<1751), p_lower_below_threshold(0.24<0.75) |
| 53921461 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.003907 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0007 €) | — | 0.93 | 0.236 (n=403) | REJECTED | below_safety_margin(363201102442<781464568239), p_lower_below_threshold(0.24<0.75) |
| 53921461 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.003907 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0007 €) | — | 0.93 | 0.236 (n=403) | REJECTED | below_safety_margin(363201102442<781464568239), p_lower_below_threshold(0.24<0.75) |
| 53921461 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 8.658627 USDC | 0.007516 USDC | 0.000000 USDC | 0.006713 USDC | 0.000803 USDC (0.0007 €) | — | 0.93 | 0.236 (n=403) | REJECTED | below_safety_margin(803<1731), p_lower_below_threshold(0.24<0.75) |
| 53921461 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 8.658627 USDC | 0.007516 USDC | 0.000000 USDC | 0.006713 USDC | 0.000803 USDC (0.0007 €) | — | 0.93 | 0.236 (n=403) | REJECTED | below_safety_margin(803<1731), p_lower_below_threshold(0.24<0.75) |
| 53921461 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.003853 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0005 €) | — | 0.58 | 0.169 (n=1026) | REJECTED | below_safety_margin(222154739456<770633643229), p_lower_below_threshold(0.17<0.75) |
| 53921461 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.003853 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0005 €) | — | 0.58 | 0.169 (n=1026) | REJECTED | below_safety_margin(222154739456<770633643229), p_lower_below_threshold(0.17<0.75) |
| 53921457 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.003853 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0005 €) | — | 0.58 | 0.169 (n=1026) | REJECTED | below_safety_margin(221905907847<770633643229), stale_data(4303ms>4000.0), p_lower_below_threshold(0.17<0.75) |
| 53921458 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.003853 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0005 €) | — | 0.58 | 0.169 (n=1026) | REJECTED | below_safety_margin(221905907847<770633643229), p_lower_below_threshold(0.17<0.75) |
| 53921459 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.003853 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0005 €) | — | 0.58 | 0.169 (n=1026) | REJECTED | below_safety_margin(221905907847<770633643229), p_lower_below_threshold(0.17<0.75) |
| 53921460 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.003853 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0005 €) | — | 0.58 | 0.169 (n=1026) | REJECTED | below_safety_margin(221905907847<770633643229), p_lower_below_threshold(0.17<0.75) |
| 53921457 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 8.542968 USDC | 0.007202 USDC | 0.000000 USDC | 0.006713 USDC | 0.000489 USDC (0.0004 €) | — | 0.57 | 0.169 (n=1026) | REJECTED | below_safety_margin(489<1708), stale_data(4297ms>4000.0), p_lower_below_threshold(0.17<0.75) |
| 53921458 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 8.542968 USDC | 0.007202 USDC | 0.000000 USDC | 0.006713 USDC | 0.000489 USDC (0.0004 €) | — | 0.57 | 0.169 (n=1026) | REJECTED | below_safety_margin(489<1708), p_lower_below_threshold(0.17<0.75) |
| 53921459 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 8.542968 USDC | 0.007202 USDC | 0.000000 USDC | 0.006713 USDC | 0.000489 USDC (0.0004 €) | — | 0.57 | 0.169 (n=1026) | REJECTED | below_safety_margin(489<1708), p_lower_below_threshold(0.17<0.75) |

## Fiabilité et décision
- Observations ghost : 5846 ; taux observé 0.159 ; borne inférieure crédible (0.9) 0.153 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 15.3% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
