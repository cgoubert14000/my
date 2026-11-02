# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-02T20:39:21+00:00 ; durée 18.3 min ; blocs 53430755 → 53431307 (550 vus)

## Connexion
- Requêtes RPC : 6481 ; erreurs : 0 ; latence p50/p95 : 126.2/897.9 ms
- Rafraîchissements d'état : 551 ; âge des données au dernier bloc : 0.43 s ; changements de frais LP observés (pools à frais dynamiques) : 1036
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 7020 ; cycles déclenchés par événement : 554 ; avance médiane sur le rafraîchissement multicall : 366 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,249.92 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 490 pools, 284 jetons, 18378 routes
- Par DEX : uniswap_v3 136, aerodrome_slipstream 107, aerodrome 202, pancakeswap_v3 30, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 174 (rejetés 2) → 579 jetons ; pools candidats 3753 (énumérés 307, par paires 0), mesurés 493, sous le plancher de 10000.0 $ : 3 → gardés 490 (max 1500) ; prix des hubs : {'USDC': 1.0, 'DAI': 1.0, 'USDbC': 1.0, 'WETH': 2249.230736, 'cbBTC': 77054.558403, 'AERO': 0.602518}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 149,925,727 | 2,249.919841 | 53431307 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,163,477 | 0.029238 | 53431307 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,083,461 | 0.029260 | 53431307 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,008,472 | 0.000013 | 53431307 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 7,841,231 | 2,244.217700 | 53431307 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,524,325 | 105.489557 | 53431307 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,516,473 | 0.001552 | 53431307 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 5,346,378 | 1.668235 | 53431307 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,760,559 | 0.029233 | 53431307 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,056,434 | 2,244.838905 | 53431307 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,048,479 | 0.999897 | 53431307 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome_slipstream | WETH/USDC | 150 | 3,916,641 | 2,244.922952 | 53431307 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome | WETH/KTA | 3000 | 3,490,940 | 38,874.527591 | 53431307 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,630,703 | 0.029262 | 53431307 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2709 | 2,265,292 | 105.515012 | 53431307 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | WETH/FAI | 10000 | 2,146,950 | 1,113,421.448962 | 53431307 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 424 | 2,040,295 | 0.000013 | 53431307 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | XDP/USDC | 100 | 1,729,146 | 0.017633 | 53431307 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,657,788 | 0.000000 | 53431307 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,606,530 | 0.000013 | 53431307 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,565,730 | 0.000013 | 53431307 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,545,941 | 1.450900 | 53431307 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,524,868 | 445.583177 | 53431307 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v2 | WETH/USDC | 3000 | 1,495,854 | 2,249.896485 | 53431307 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,453,431 | 0.822643 | 53431307 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,382,811 | 3,744.101037 | 53431307 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | WETH/USDC | 3000 | 1,348,366 | 2,250.033681 | 53431307 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,304,173 | 2,244.362739 | 53431307 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,291,960 | 0.005025 | 53431307 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,271,814 | 15,228.277853 | 53431307 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome_slipstream | USDC/cbBTC | 336 | 1,259,800 | 0.000013 | 53431307 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/SEND | 3000 | 1,168,739 | 71.138543 | 53431307 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,092,512 | 38,343,352.381818 | 53431307 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,047,418 | 536,313.754105 | 53431307 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,001,417 | 22,715,602.023203 | 53431307 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | DRB/WETH | 10000 | 997,948 | 0.000000 | 53431307 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome_slipstream | USDC/VELVET | 100 | 973,608 | 20.492094 | 53431307 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | WETH/EDEL | 7000 | 962,301 | 83,393.955848 | 53431307 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/USDC | 10000 | 921,182 | 2,257.234891 | 53431307 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome | WETH/WELL | 10000 | 917,896 | 1,253,370.638723 | 53431307 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/MORPHO | 3000 | 909,157 | 1,041.447442 | 53431307 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/VVV | 10000 | 902,332 | 105.982345 | 53431307 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome | USDC/NOCK | 3000 | 885,149 | 79.903221 | 53431307 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | uXRP/WETH | 3000 | 860,491 | 0.000553 | 53431307 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| uniswap_v3 | USDC/VVV | 3000 | 859,052 | 0.046997 | 53431307 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | WETH/AERO | 10000 | 822,136 | 3,718.658167 | 53431307 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | USDC/SAPIEN | 4590 | 812,723 | 20.362414 | 53431307 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 797,771 | 0.057040 | 53431307 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 763,794 | 0.798908 | 53431307 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 724,137 | 0.575454 | 53431307 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| aerodrome | VIRTUAL/WETH | 10000 | 716,856 | 0.000258 | 53431307 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 690,548 | 5,019,057.821558 | 53431307 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v2 | WETH/NPC | 3000 | 667,666 | 143,341.627726 | 53431307 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| uniswap_v3 | TIG/USDC | 10000 | 667,227 | 0.564616 | 53431307 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 662,418 | 0.000008 | 53431307 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | WETH/msETH (stable) | 500 | 651,950 | 2.338865 | 53431307 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | WETH/BRETT | 2111 | 645,357 | 538,768.681356 | 53431307 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome | WETH/bsdETH | 100 | 604,201 | 0.915187 | 53431307 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 585,084 | 0.086738 | 53431307 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| uniswap_v3 | FLOCK/USDC | 3000 | 554,901 | 0.037608 | 53431307 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |

## Recherche d'opportunités
- Cycles : 1104 ; routes examinées : 20289312 ; candidats optimisés : 64733 ; net attendu > 0 : 62 ; dernier cycle 77.6 ms
- Rejets (moteur) : {'spread_below_threshold': 19952530, 'liquidity_below_min': 268700, 'negative_expected_net': 64671, 'unquotable': 2206, 'borrow_bound_too_small': 1103}
- Enregistrements de la session : 64730 ; net attendu > 0 : 62 ; simulés (eth_call de la vraie tx) : 6 (ok 0, échec 6) ; étiquettes ghost N+1 : 1/5 positives
- Décisions : {'REJECTED': 64730} ; motifs de rejet : {'below_safety_margin': 10, 'negative_expected_net': 64668, 'p_lower_below_threshold': 60, 'reliability_not_demonstrated': 2, 'simulation_failed': 6}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
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
| 53430895 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.001369 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0347 €) | — | 3.58 | 0.159 (n=596) | REJECTED | p_lower_below_threshold(0.16<0.75) |
| 53430895 | WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.047365 WETH | 0.000020 WETH | 0.000000 WETH | 0.000003 WETH | 0.000017 WETH (0.0342 €) | — | 3.49 | 0.159 (n=596) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.16<0.75) |
| 53430896 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→USDC | 80.519604 USDC | 0.036060 USDC | 0.000000 USDC | 0.006785 USDC | 0.029275 USDC (0.0269 €) | — | 3.64 | 0.287 (n=313) | REJECTED | p_lower_below_threshold(0.29<0.75) |
| 53430896 | cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.000964 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0269 €) | — | 3.94 | 0.287 (n=313) | REJECTED | p_lower_below_threshold(0.29<0.75) |
| 53430896 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.000942 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0262 €) | — | 3.93 | 0.159 (n=596) | REJECTED | p_lower_below_threshold(0.16<0.75) |
| 53430896 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 76.206627 USDC | 0.035083 USDC | 0.000000 USDC | 0.006785 USDC | 0.028298 USDC (0.0260 €) | — | 3.71 | 0.159 (n=596) | REJECTED | p_lower_below_threshold(0.16<0.75) |
| 53430895 | USDC→[uniswap_v3]→AERO→[aerodrome]→VIRTUAL→[pancakeswap_v3]→USDC | 21.503308 USDC | 0.031161 USDC | 0.000000 USDC | 0.006474 USDC | 0.024687 USDC (0.0227 €) | — | 11.48 | 0.137 (n=38) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 53430896 | USDC→[uniswap_v3]→AERO→[aerodrome]→VIRTUAL→[pancakeswap_v3]→USDC | 21.503308 USDC | 0.031161 USDC | 0.000000 USDC | 0.006474 USDC | 0.024687 USDC (0.0227 €) | — | 11.48 | 0.137 (n=38) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 53430895 | cbBTC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.000880 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0198 €) | — | 3.18 | 0.159 (n=596) | REJECTED | p_lower_below_threshold(0.16<0.75) |
| 53430895 | WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→WETH | 0.031999 WETH | 0.000012 WETH | 0.000000 WETH | 0.000003 WETH | 0.000009 WETH (0.0196 €) | — | 2.96 | 0.187 (n=833) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.19<0.75) |
| 53430895 | USDC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 50.572883 USDC | 0.023821 USDC | 0.000000 USDC | 0.006785 USDC | 0.017036 USDC (0.0157 €) | — | 3.37 | 0.159 (n=596) | REJECTED | p_lower_below_threshold(0.16<0.75) |
| 53430896 | USDC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 50.572883 USDC | 0.023821 USDC | 0.000000 USDC | 0.006785 USDC | 0.017036 USDC (0.0157 €) | — | 3.37 | 0.159 (n=596) | REJECTED | p_lower_below_threshold(0.16<0.75) |
| 53430895 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH | 0.022496 WETH | 0.000011 WETH | 0.000000 WETH | 0.000003 WETH | 0.000008 WETH (0.0156 €) | — | 3.36 | 0.159 (n=596) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.16<0.75) |
| 53430896 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH | 0.022496 WETH | 0.000011 WETH | 0.000000 WETH | 0.000003 WETH | 0.000008 WETH (0.0156 €) | — | 3.36 | 0.159 (n=596) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.16<0.75) |
| 53430895 | USDC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 40.563624 USDC | 0.023732 USDC | 0.000000 USDC | 0.006785 USDC | 0.016947 USDC (0.0156 €) | — | 4.18 | 0.159 (n=596) | REJECTED | p_lower_below_threshold(0.16<0.75) |

## Fiabilité et décision
- Observations ghost : 4764 ; taux observé 0.171 ; borne inférieure crédible (0.9) 0.164 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 16.4% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
