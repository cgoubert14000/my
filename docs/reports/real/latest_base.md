# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-04T01:30:53+00:00 ; durée 61.35 min ; blocs 53481408 → 53483251 (1778 vus)

## Connexion
- Requêtes RPC : 20393 ; erreurs : 70 ; latence p50/p95 : 281.0/1,076.0 ms
- Rafraîchissements d'état : 1778 ; âge des données au dernier bloc : 4.98 s ; changements de frais LP observés (pools à frais dynamiques) : 4264
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 19021 ; cycles déclenchés par événement : 1415 ; avance médiane sur le rafraîchissement multicall : 559 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,263.48 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 490 pools, 282 jetons, 19430 routes
- Par DEX : uniswap_v3 139, aerodrome_slipstream 105, aerodrome 203, pancakeswap_v3 29, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 172 (rejetés 2) → 577 jetons ; pools candidats 3703 (énumérés 305, par paires 0), mesurés 493, sous le plancher de 10000.0 $ : 3 → gardés 490 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2264.542979, 'cbBTC': 77119.048638, 'AERO': 0.629628}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 149,875,121 | 2,263.479576 | 53483250 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,602,989 | 0.029412 | 53483250 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,110,877 | 0.029422 | 53483250 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,035,007 | 0.000013 | 53483250 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 7,989,192 | 2,260.971571 | 53483250 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,673,336 | 101.863567 | 53483250 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,538,340 | 0.001563 | 53483250 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 5,383,762 | 1.592842 | 53483250 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,783,627 | 0.029402 | 53483250 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,154,913 | 2,261.876412 | 53483250 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,048,550 | 0.999909 | 53483250 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome_slipstream | WETH/USDC | 698 | 3,841,378 | 2,261.743953 | 53483250 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome | WETH/KTA | 3000 | 3,406,289 | 41,324.348970 | 53483250 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,659,294 | 0.029409 | 53483250 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 2,138,785 | 1,135,502.765144 | 53483250 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | WETH/VVV | 2715 | 2,103,897 | 101.816132 | 53483250 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | USDC/cbBTC | 472 | 1,803,961 | 0.000013 | 53483250 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | XDP/USDC | 100 | 1,725,219 | 0.017560 | 53483250 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,661,171 | 0.000000 | 53483250 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,645,330 | 0.006667 | 53483251 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,609,628 | 0.000013 | 53483250 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,554,793 | 1.429892 | 53483250 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,539,873 | 440.415944 | 53483250 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,537,258 | 0.000013 | 53483250 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v2 | WETH/USDC | 3000 | 1,500,474 | 2,263.713142 | 53483250 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,454,326 | 0.820467 | 53483250 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,413,782 | 3,604.705937 | 53483250 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,342,908 | 2,260.954521 | 53483250 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | WETH/USDC | 3000 | 1,334,196 | 2,266.252254 | 53483250 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,282,112 | 14,969.979919 | 53483250 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | USDC/SEND | 3000 | 1,158,466 | 72.405863 | 53483250 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,112,506 | 36,969,258.567437 | 53483250 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | DRB/WETH | 10000 | 1,048,630 | 0.000000 | 53483250 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,043,310 | 550,478.359200 | 53483250 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,023,533 | 21,970,183.467339 | 53483250 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/VELVET | 100 | 994,412 | 19.258555 | 53483250 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/VVV | 10000 | 952,903 | 101.306061 | 53483250 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome | WETH/EDEL | 7000 | 952,644 | 86,121.555971 | 53483250 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/MORPHO | 3000 | 942,997 | 1,054.045010 | 53483250 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome_slipstream | USDC/cbBTC | 342 | 935,815 | 0.000013 | 53483250 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/NOCK | 3000 | 930,258 | 72.342493 | 53483250 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/USDC | 10000 | 925,193 | 2,279.510176 | 53483250 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome | WETH/WELL | 10000 | 916,640 | 1,271,961.163077 | 53483250 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | USDC/VVV | 3000 | 877,793 | 0.044967 | 53483250 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | uXRP/WETH | 3000 | 859,779 | 0.000549 | 53483250 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome | WETH/AERO | 10000 | 839,350 | 3,611.587591 | 53483250 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 815,788 | 20.258147 | 53483250 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 786,239 | 0.055313 | 53483250 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 768,286 | 0.799140 | 53483250 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 731,028 | 0.580136 | 53483250 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| aerodrome | VIRTUAL/WETH | 10000 | 719,204 | 0.000257 | 53483250 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 703,725 | 4,891,834.984874 | 53483250 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 667,928 | 0.000008 | 53483250 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v2 | WETH/NPC | 3000 | 661,985 | 147,616.193389 | 53483250 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome | WETH/msETH (stable) | 500 | 651,112 | 2.364339 | 53483250 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | TIG/USDC | 10000 | 649,140 | 0.530504 | 53483250 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | WETH/BRETT | 2108 | 640,515 | 552,549.257297 | 53483250 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome | WETH/bsdETH | 100 | 608,227 | 0.914029 | 53483250 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 585,174 | 0.086739 | 53483250 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| uniswap_v3 | FLOCK/USDC | 3000 | 558,512 | 0.037919 | 53483250 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |

## Recherche d'opportunités
- Cycles : 3192 ; routes examinées : 62020560 ; candidats optimisés : 199334 ; net attendu > 0 : 425 ; dernier cycle 117.0 ms
- Rejets (moteur) : {'spread_below_threshold': 61060823, 'liquidity_below_min': 756350, 'negative_expected_net': 198909, 'borrow_bound_too_small': 3176, 'cycle_budget_exhausted': 877}
- Enregistrements de la session : 199334 ; net attendu > 0 : 425 ; simulés (eth_call de la vraie tx) : 22 (ok 5, échec 17) ; étiquettes ghost N+1 : 3/17 positives
- Décisions : {'REJECTED': 199334} ; motifs de rejet : {'below_safety_margin': 361, 'negative_expected_net': 198909, 'p_lower_below_threshold': 410, 'reliability_not_demonstrated': 15, 'sim_below_estimate': 3, 'simulated_net_nonpositive': 1, 'simulation_failed': 17, 'stale_data': 5}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53482801 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.395100 WETH | 0.000029 WETH | 0.000000 WETH | 0.000002 WETH | 0.000027 WETH (0.0564 €) | — | 0.69 | 0.034 (n=197) | REJECTED | below_safety_margin(27080914046156<79019907377896), p_lower_below_threshold(0.03<0.75) |
| 53482801 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.395100 WETH | 0.000029 WETH | 0.000000 WETH | 0.000002 WETH | 0.000027 WETH (0.0564 €) | — | 0.69 | 0.034 (n=197) | REJECTED | below_safety_margin(27080914046156<79019907377896), p_lower_below_threshold(0.03<0.75) |
| 53482801 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 892.938370 USDC | 0.066697 USDC | 0.000000 USDC | 0.005424 USDC | 0.061273 USDC (0.0564 €) | — | 0.69 | 0.034 (n=197) | REJECTED | below_safety_margin(61273<178587), p_lower_below_threshold(0.03<0.75) |
| 53482801 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 892.938370 USDC | 0.066697 USDC | 0.000000 USDC | 0.005424 USDC | 0.061273 USDC (0.0564 €) | — | 0.69 | 0.034 (n=197) | REJECTED | below_safety_margin(61273<178587), p_lower_below_threshold(0.03<0.75) |
| 53482442 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.280734 WETH | 0.000015 WETH | 0.000000 WETH | 0.000002 WETH | 0.000013 WETH (0.0265 €) | — | 0.45 | 0.034 (n=197) | REJECTED | below_safety_margin(12707668661965<56146702894766), p_lower_below_threshold(0.03<0.75) |
| 53482444 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.280734 WETH | 0.000015 WETH | 0.000000 WETH | 0.000002 WETH | 0.000013 WETH (0.0265 €) | — | 0.45 | 0.034 (n=197) | REJECTED | below_safety_margin(12707668661965<56146702894766), p_lower_below_threshold(0.03<0.75) |
| 53482442 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 634.696703 USDC | 0.033856 USDC | 0.000000 USDC | 0.005093 USDC | 0.028763 USDC (0.0265 €) | — | 0.45 | 0.034 (n=197) | REJECTED | below_safety_margin(28763<126939), p_lower_below_threshold(0.03<0.75) |
| 53482444 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 634.696703 USDC | 0.033856 USDC | 0.000000 USDC | 0.005093 USDC | 0.028763 USDC (0.0265 €) | — | 0.45 | 0.034 (n=197) | REJECTED | below_safety_margin(28763<126939), p_lower_below_threshold(0.03<0.75) |
| 53482562 | cbBTC→[aerodrome_slipstream]→AERO→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.001146 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0234 €) | — | 2.88 | 0.184 (n=854) | REJECTED | p_lower_below_threshold(0.18<0.75) |
| 53482562 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→AERO→[pancakeswap_v3]→WETH | 0.046156 WETH | 0.000014 WETH | 0.000000 WETH | 0.000003 WETH | 0.000011 WETH (0.0232 €) | — | 2.41 | 0.184 (n=854) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.18<0.75) |
| 53483010 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC | 78.940251 USDC | 0.031684 USDC | 0.000000 USDC | 0.006803 USDC | 0.024881 USDC (0.0229 €) | — | 3.15 | 0.157 (n=612) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.16<0.75) |
| 53483010 | cbBTC→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.001195 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0226 €) | — | 2.68 | 0.183 (n=859) | REJECTED | p_lower_below_threshold(0.18<0.75) |
| 53483010 | cbBTC→[aerodrome_slipstream]→AERO→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→cbBTC | 0.001035 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0226 €) | — | 3.09 | 0.157 (n=612) | REJECTED | p_lower_below_threshold(0.16<0.75) |
| 53483010 | WETH→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→AERO→[pancakeswap_v3]→WETH | 0.036690 WETH | 0.000014 WETH | 0.000000 WETH | 0.000003 WETH | 0.000011 WETH (0.0226 €) | — | 2.95 | 0.183 (n=859) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.18<0.75) |
| 53482501 | WETH→[aerodrome]→USDC→[uniswap_v3]→WETH | 0.055511 WETH | 0.000013 WETH | 0.000000 WETH | 0.000002 WETH | 0.000011 WETH (0.0220 €) | — | 1.90 | 0.216 (n=21) | REJECTED | below_safety_margin(10537187774160<11102245886394), reliability_not_demonstrated |
| 53482501 | USDC→[uniswap_v3]→WETH→[aerodrome]→USDC | 124.584664 USDC | 0.028930 USDC | 0.000000 USDC | 0.005153 USDC | 0.023777 USDC (0.0219 €) | — | 1.91 | 0.216 (n=21) | REJECTED | below_safety_margin(23777<24916), reliability_not_demonstrated |
| 53483010 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→AERO→[pancakeswap_v3]→WETH | 0.043454 WETH | 0.000013 WETH | 0.000000 WETH | 0.000003 WETH | 0.000010 WETH (0.0212 €) | — | 2.35 | 0.183 (n=859) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.18<0.75) |
| 53483010 | cbBTC→[aerodrome_slipstream]→AERO→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.001233 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0212 €) | — | 2.43 | 0.183 (n=859) | REJECTED | p_lower_below_threshold(0.18<0.75) |
| 53482453 | WETH→[sushiswap_v3]→USDC→[uniswap_v3]→WETH | 0.049638 WETH | 0.000012 WETH | 0.000000 WETH | 0.000002 WETH | 0.000010 WETH (0.0200 €) | — | 1.93 | 0.024 (n=59) | REJECTED | below_safety_margin(9588157494987<9927694244160), p_lower_below_threshold(0.02<0.75) |
| 53482454 | WETH→[sushiswap_v3]→USDC→[uniswap_v3]→WETH | 0.049638 WETH | 0.000012 WETH | 0.000000 WETH | 0.000002 WETH | 0.000010 WETH (0.0200 €) | — | 1.93 | 0.024 (n=59) | REJECTED | below_safety_margin(9588157494987<9927694244160), p_lower_below_threshold(0.02<0.75) |
| 53482453 | USDC→[uniswap_v3]→WETH→[sushiswap_v3]→USDC | 112.308995 USDC | 0.026773 USDC | 0.000000 USDC | 0.005093 USDC | 0.021680 USDC (0.0199 €) | — | 1.93 | 0.024 (n=59) | REJECTED | below_safety_margin(21680<22461), p_lower_below_threshold(0.02<0.75) |
| 53482454 | USDC→[uniswap_v3]→WETH→[sushiswap_v3]→USDC | 112.308995 USDC | 0.026773 USDC | 0.000000 USDC | 0.005093 USDC | 0.021680 USDC (0.0199 €) | — | 1.93 | 0.024 (n=59) | REJECTED | below_safety_margin(21680<22461), p_lower_below_threshold(0.02<0.75) |
| 53483010 | USDC→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC | 70.715179 USDC | 0.027900 USDC | 0.000000 USDC | 0.006803 USDC | 0.021097 USDC (0.0194 €) | — | 2.98 | 0.258 (n=347) | REJECTED | p_lower_below_threshold(0.26<0.75) |
| 53482562 | cbBTC→[aerodrome_slipstream]→AERO→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→cbBTC | 0.000905 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0191 €) | — | 2.98 | 0.184 (n=854) | REJECTED | p_lower_below_threshold(0.18<0.75) |
| 53483010 | cbBTC→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC→[aerodrome_slipstream]→cbBTC | 0.000820 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0191 €) | — | 3.29 | 0.293 (n=319) | REJECTED | p_lower_below_threshold(0.29<0.75) |

## Fiabilité et décision
- Observations ghost : 4957 ; taux observé 0.168 ; borne inférieure crédible (0.9) 0.162 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 16.2% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
