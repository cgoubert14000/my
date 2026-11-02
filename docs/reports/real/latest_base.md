# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-02T23:54:40+00:00 ; durée 213.61 min ; blocs 53430755 → 53437164 (6399 vus)

## Connexion
- Requêtes RPC : 76618 ; erreurs : 30 ; latence p50/p95 : 129.1/731.8 ms
- Rafraîchissements d'état : 6400 ; âge des données au dernier bloc : 0.86 s ; changements de frais LP observés (pools à frais dynamiques) : 6483
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 54814 ; cycles déclenchés par événement : 6757 ; avance médiane sur le rafraîchissement multicall : 241 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,251.09 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 490 pools, 284 jetons, 18378 routes
- Par DEX : uniswap_v3 136, aerodrome_slipstream 107, aerodrome 202, pancakeswap_v3 30, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 174 (rejetés 2) → 579 jetons ; pools candidats 3753 (énumérés 307, par paires 0), mesurés 493, sous le plancher de 10000.0 $ : 3 → gardés 490 (max 1500) ; prix des hubs : {'USDC': 1.0, 'DAI': 1.0, 'USDbC': 1.0, 'WETH': 2249.230736, 'cbBTC': 77054.558403, 'AERO': 0.602518}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 150,011,151 | 2,251.087091 | 53437164 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,159,987 | 0.029327 | 53437164 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,076,523 | 0.029314 | 53437164 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 8,978,738 | 0.000013 | 53437164 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 7,842,899 | 2,249.323467 | 53437164 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,524,532 | 105.593221 | 53437164 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,529,065 | 0.001566 | 53437164 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 5,353,147 | 1.661704 | 53437164 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,759,043 | 0.029338 | 53437164 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,073,048 | 2,250.354099 | 53437164 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,038,208 | 0.999897 | 53437164 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome_slipstream | WETH/USDC | 150 | 3,905,428 | 2,250.143135 | 53437164 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome | WETH/KTA | 3000 | 3,493,793 | 38,851.346168 | 53437164 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,702,575 | 0.029328 | 53437164 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 2,138,109 | 1,123,812.880448 | 53437164 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 424 | 2,029,320 | 0.000013 | 53437164 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome_slipstream | WETH/VVV | 2700 | 1,975,089 | 105.598026 | 53437164 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| uniswap_v3 | XDP/USDC | 100 | 1,736,492 | 0.017755 | 53437164 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,665,585 | 0.000000 | 53437164 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,603,972 | 0.000013 | 53437164 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,545,941 | 1.450900 | 53437164 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,532,324 | 0.000013 | 53437164 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,526,410 | 444.889706 | 53437164 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v2 | WETH/USDC | 3000 | 1,496,246 | 2,252.942914 | 53437164 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,453,608 | 0.822379 | 53437164 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,386,554 | 3,739.096250 | 53437164 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | WETH/USDC | 3000 | 1,348,717 | 2,255.404636 | 53437164 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,305,539 | 2,250.178296 | 53437164 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,289,168 | 0.005008 | 53437164 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,271,213 | 15,160.246340 | 53437164 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome_slipstream | USDC/cbBTC | 336 | 1,256,900 | 0.000013 | 53437164 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/SEND | 3000 | 1,168,739 | 71.138543 | 53437164 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,098,978 | 37,712,955.632377 | 53437164 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,048,916 | 535,171.277917 | 53437164 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,004,455 | 22,651,286.634694 | 53437164 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | DRB/WETH | 10000 | 1,003,659 | 0.000000 | 53437164 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome_slipstream | USDC/VELVET | 100 | 984,011 | 19.856390 | 53437164 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | WETH/EDEL | 7000 | 954,018 | 84,938.680374 | 53437164 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/USDC | 10000 | 921,361 | 2,257.234891 | 53437164 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome | WETH/WELL | 10000 | 911,879 | 1,271,284.356318 | 53437164 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/MORPHO | 3000 | 910,566 | 1,039.895456 | 53437164 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/VVV | 10000 | 900,448 | 105.982299 | 53437164 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | uXRP/WETH | 3000 | 863,664 | 0.000551 | 53437164 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| uniswap_v3 | USDC/VVV | 3000 | 856,311 | 0.046948 | 53437164 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | USDC/NOCK | 3000 | 855,997 | 85.438449 | 53437164 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome | WETH/AERO | 10000 | 823,956 | 3,725.146765 | 53437164 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 813,546 | 20.333020 | 53437164 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 798,603 | 0.057165 | 53437164 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 764,190 | 0.798908 | 53437164 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 723,954 | 0.578785 | 53437164 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| aerodrome | VIRTUAL/WETH | 10000 | 716,396 | 0.000258 | 53437164 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 695,681 | 4,950,544.972612 | 53437164 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v2 | WETH/NPC | 3000 | 661,703 | 146,093.510555 | 53437164 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| uniswap_v3 | TIG/USDC | 10000 | 656,055 | 0.546614 | 53437164 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 655,044 | 0.000008 | 53437164 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | WETH/msETH (stable) | 500 | 652,297 | 2.338821 | 53437164 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 646,436 | 538,305.089750 | 53437164 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome | WETH/bsdETH | 100 | 604,494 | 0.915248 | 53437164 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 588,831 | 0.087565 | 53437164 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| uniswap_v3 | FLOCK/USDC | 3000 | 555,657 | 0.037685 | 53437164 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |

## Recherche d'opportunités
- Cycles : 13156 ; routes examinées : 241780968 ; candidats optimisés : 649215 ; net attendu > 0 : 305 ; dernier cycle 70.4 ms
- Rejets (moteur) : {'spread_below_threshold': 238251880, 'liquidity_below_min': 2812149, 'negative_expected_net': 648910, 'unquotable': 54438, 'borrow_bound_too_small': 13153, 'cycle_budget_exhausted': 93}
- Enregistrements de la session : 649215 ; net attendu > 0 : 305 ; simulés (eth_call de la vraie tx) : 16 (ok 3, échec 13) ; étiquettes ghost N+1 : 1/13 positives
- Décisions : {'REJECTED': 649215} ; motifs de rejet : {'below_safety_margin': 242, 'negative_expected_net': 648910, 'p_lower_below_threshold': 287, 'price_impact': 2, 'reliability_not_demonstrated': 18, 'simulation_failed': 13}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53436806 | WETH→[aerodrome_slipstream]→BRETT→[uniswap_v3]→WETH | 0.144162 WETH | 0.006601 WETH | 0.000000 WETH | 0.000003 WETH | 0.006599 WETH (13.6660 €) | — | 457.73 | 0.001 (n=6) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53436806 | WETH→[aerodrome_slipstream]→BRETT→[uniswap_v3]→WETH | 0.099313 WETH | 0.004085 WETH | 0.000000 WETH | 0.000002 WETH | 0.004082 WETH (8.4546 €) | — | 411.06 | 0.001 (n=6) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53430895 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→USDC | 245.658989 USDC | 0.352776 USDC | 0.000000 USDC | 0.006785 USDC | 0.345991 USDC (0.3183 €) | — | 14.08 | 0.031 (n=91) | REJECTED | p_lower_below_threshold(0.03<0.75) |
| 53430895 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 244.076529 USDC | 0.352155 USDC | 0.000000 USDC | 0.006785 USDC | 0.345370 USDC (0.3177 €) | — | 14.15 | 0.098 (n=111) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53430895 | cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.003068 cbBTC | 0.000005 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000004 cbBTC (0.3177 €) | — | 14.64 | 0.031 (n=91) | REJECTED | p_lower_below_threshold(0.03<0.75) |
| 53430895 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.003053 cbBTC | 0.000005 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000004 cbBTC (0.3170 €) | — | 14.68 | 0.098 (n=111) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53430895 | cbBTC→[uniswap_v3]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.002998 cbBTC | 0.000004 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000004 cbBTC (0.2781 €) | — | 13.11 | 0.031 (n=91) | REJECTED | p_lower_below_threshold(0.03<0.75) |
| 53430895 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[uniswap_v3]→USDC | 227.538095 USDC | 0.308718 USDC | 0.000000 USDC | 0.006785 USDC | 0.301933 USDC (0.2778 €) | — | 13.27 | 0.031 (n=91) | REJECTED | p_lower_below_threshold(0.03<0.75) |
| 53430895 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→USDC | 227.538095 USDC | 0.307229 USDC | 0.000000 USDC | 0.006785 USDC | 0.300444 USDC (0.2764 €) | — | 13.20 | 0.031 (n=91) | REJECTED | p_lower_below_threshold(0.03<0.75) |
| 53430895 | cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.002834 cbBTC | 0.000004 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000004 cbBTC (0.2760 €) | — | 13.76 | 0.031 (n=91) | REJECTED | p_lower_below_threshold(0.03<0.75) |
| 53430895 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.002309 cbBTC | 0.000003 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000003 cbBTC (0.2059 €) | — | 12.60 | 0.098 (n=111) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53430895 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 189.086221 USDC | 0.230454 USDC | 0.000000 USDC | 0.006785 USDC | 0.223669 USDC (0.2058 €) | — | 11.83 | 0.098 (n=111) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53434127 | USDC→[pancakeswap_v3]→PLAY→[aerodrome_slipstream]→USDC | 44.863801 USDC | 0.050318 USDC | 0.000000 USDC | 0.005060 USDC | 0.045258 USDC (0.0416 €) | — | 10.09 | 0.000 (n=71) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 53430895 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.001369 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0347 €) | — | 3.58 | 0.159 (n=596) | REJECTED | p_lower_below_threshold(0.16<0.75) |
| 53430895 | WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.047365 WETH | 0.000020 WETH | 0.000000 WETH | 0.000003 WETH | 0.000017 WETH (0.0342 €) | — | 3.49 | 0.159 (n=596) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.16<0.75) |
| 53430896 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→USDC | 80.519604 USDC | 0.036060 USDC | 0.000000 USDC | 0.006785 USDC | 0.029275 USDC (0.0269 €) | — | 3.64 | 0.287 (n=313) | REJECTED | p_lower_below_threshold(0.29<0.75) |
| 53430896 | cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.000964 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0269 €) | — | 3.94 | 0.287 (n=313) | REJECTED | p_lower_below_threshold(0.29<0.75) |
| 53430896 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.000942 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0262 €) | — | 3.93 | 0.159 (n=596) | REJECTED | p_lower_below_threshold(0.16<0.75) |
| 53430896 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 76.206627 USDC | 0.035083 USDC | 0.000000 USDC | 0.006785 USDC | 0.028298 USDC (0.0260 €) | — | 3.71 | 0.159 (n=596) | REJECTED | p_lower_below_threshold(0.16<0.75) |
| 53430895 | USDC→[uniswap_v3]→AERO→[aerodrome]→VIRTUAL→[pancakeswap_v3]→USDC | 21.503308 USDC | 0.031161 USDC | 0.000000 USDC | 0.006474 USDC | 0.024687 USDC (0.0227 €) | — | 11.48 | 0.137 (n=38) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 53430896 | USDC→[uniswap_v3]→AERO→[aerodrome]→VIRTUAL→[pancakeswap_v3]→USDC | 21.503308 USDC | 0.031161 USDC | 0.000000 USDC | 0.006474 USDC | 0.024687 USDC (0.0227 €) | — | 11.48 | 0.137 (n=38) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 53435612 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.227863 WETH | 0.000014 WETH | 0.000000 WETH | 0.000003 WETH | 0.000011 WETH (0.0227 €) | — | 0.48 | 0.041 (n=20) | REJECTED | below_safety_margin(10946418868377<45572591252304), reliability_not_demonstrated |
| 53435612 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.005866 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0226 €) | — | 0.55 | 0.041 (n=20) | REJECTED | below_safety_margin(32<117), reliability_not_demonstrated |
| 53435612 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 566.380001 USDC | 0.031746 USDC | 0.000000 USDC | 0.007446 USDC | 0.024300 USDC (0.0224 €) | — | 0.43 | 0.041 (n=20) | REJECTED | below_safety_margin(24300<113276), reliability_not_demonstrated |
| 53436806 | WETH→[pancakeswap_v3]→BRETT→[uniswap_v3]→WETH | 0.000444 WETH | 0.000013 WETH | 0.000000 WETH | 0.000002 WETH | 0.000011 WETH (0.0223 €) | — | 242.74 | 0.006 (n=1) | REJECTED | price_impact(398bps>150.0), simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |

## Fiabilité et décision
- Observations ghost : 4772 ; taux observé 0.171 ; borne inférieure crédible (0.9) 0.164 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 16.4% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
