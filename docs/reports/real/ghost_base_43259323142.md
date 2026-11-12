# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-12T17:45:43+00:00 ; durée 70.58 min ; blocs 56554640 → 56575786 (4309 vus)

## Connexion
- Requêtes RPC : 48972 ; erreurs : 36 ; latence p50/p95 : 184.1/1,685.9 ms
- Rafraîchissements d'état : 4309 ; âge des données au dernier bloc : 9.0 s ; changements de frais LP observés (pools à frais dynamiques) : 2542
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 1271 ; cycles déclenchés par événement : 354 ; avance médiane sur le rafraîchissement multicall : 593 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,007.82 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 454 pools, 266 jetons, 14202 routes
- Par DEX : uniswap_v3 133, aerodrome_slipstream 96, aerodrome 187, pancakeswap_v3 25, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 1
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 160 (rejetés 2) → 565 jetons ; pools candidats 3627 (énumérés 281, par paires 0), mesurés 456, sous le plancher de 10000.0 $ : 2 → gardés 454 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'DAI': 1.0, 'USDC': 1.0, 'WETH': 2012.424484, 'cbBTC': 71768.389273, 'AERO': 0.523178}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 132,557,347 | 2,007.824649 | 56575810 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,282,942 | 0.028014 | 56575810 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 8,565,317 | 0.000014 | 56575810 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 8,510,243 | 0.028017 | 56575810 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 6,848,285 | 2,009.520248 | 56575810 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 6,638,718 | 106.573997 | 56575810 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,189,287 | 0.028026 | 56575810 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 4,160,428 | 1.910739 | 56575810 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,074,512 | 2,009.800985 | 56575810 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,776,443 | 0.998584 | 56575810 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 2,978,315 | 42,532.539357 | 56575810 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 107 | 2,806,009 | 2,009.608392 | 56575810 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,150,751 | 0.028010 | 56575810 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 1,874,794 | 1,162,627.550588 | 56575810 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | XDP/USDC | 100 | 1,646,863 | 0.016775 | 56575810 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | USDC/cbBTC | 460 | 1,605,884 | 0.000014 | 56575810 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,566,886 | 0.000014 | 56575810 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,519,739 | 0.000000 | 56575810 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,489,591 | 0.006616 | 56575810 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,474,657 | 0.000014 | 56575810 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,464,579 | 0.831291 | 56575810 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,373,554 | 431.098219 | 56575810 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v2 | WETH/USDC | 3000 | 1,256,588 | 2,007.760818 | 56575810 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| uniswap_v3 | WETH/AERO | 3000 | 1,224,084 | 3,837.769249 | 56575810 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,182,675 | 15,377.573328 | 56575810 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/USDC | 3000 | 1,142,154 | 2,007.836581 | 56575810 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,095,494 | 2,009.466669 | 56575810 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,061,177 | 86.290648 | 56575810 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,047,058 | 1.389298 | 56575810 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | WETH/doginme | 10000 | 1,012,028 | 34,378,325.114166 | 56575810 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/VVV | 10000 | 978,103 | 105.928959 | 56575810 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome_slipstream | USDC/VELVET | 100 | 971,231 | 20.647334 | 56575810 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/BRETT | 10000 | 925,266 | 560,053.914628 | 56575810 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 889,963 | 0.001485 | 56575810 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| uniswap_v3 | WETH/TOSHI | 10000 | 879,229 | 23,229,511.263151 | 56575810 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/cbBTC | 344 | 869,715 | 0.000014 | 56575810 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | USDC/VVV | 3000 | 868,290 | 0.053053 | 56575810 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/USDC | 10000 | 868,250 | 2,005.358242 | 56575810 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 866,534 | 1,006.940756 | 56575810 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | DRB/WETH | 10000 | 824,754 | 0.000000 | 56575810 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | USDC/NOCK | 3000 | 770,515 | 79.226527 | 56575810 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| pancakeswap_v3 | QUID/USDC | 100 | 744,206 | 0.049335 | 56575810 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 735,994 | 23.521096 | 56575810 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome | WETH/AERO | 10000 | 686,290 | 3,863.882062 | 56575810 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | WETH/wstETH | 3000 | 680,253 | 0.801801 | 56575810 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| aerodrome | WETH/EDEL | 7000 | 656,135 | 142,732.274139 | 56575810 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 652,324 | 0.513115 | 56575810 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 629,963 | 4,816,907.713210 | 56575810 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 595,428 | 0.447045 | 56575810 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/NPC | 3000 | 578,529 | 152,704.694286 | 56575810 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | WETH/BRETT | 2093 | 564,136 | 561,914.637132 | 56575810 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome | VIRTUAL/WETH | 10000 | 561,021 | 0.000255 | 56575810 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | AERO/cbBTC | 1025 | 557,090 | 0.000007 | 56575810 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v3 | FLOCK/USDC | 3000 | 554,110 | 0.037323 | 56575810 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 483,589 | 1,006.612486 | 56575810 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| pancakeswap_v3 | ELSA/USDC | 100 | 454,325 | 0.065019 | 56575810 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| aerodrome_slipstream | USDC/USDT | 8 | 450,251 | 1.000954 | 56575810 | `0xa41Bc0AFfbA7Fd420d186b84899d7ab2aC57fcD1` |
| uniswap_v3 | USDC/MORPHO | 10000 | 446,514 | 0.502823 | 56575810 | `0x2043B296fFC6b2d3bf4A3F3167d2Afb3B0FBdbEE` |
| uniswap_v3 | WETH/uSOL | 3000 | 428,770 | 24.791120 | 56575810 | `0xab04A352D4EC8d0F1812A4E5EBe7807Fa67acD48` |
| uniswap_v3 | WETH/UNI | 10000 | 422,907 | 333.493261 | 56575810 | `0xAb365f161Dd501473a1ff0D2ef0dCE94E7398839` |

## Recherche d'opportunités
- Cycles : 4662 ; routes examinées : 66209724 ; candidats optimisés : 279117 ; net attendu > 0 : 332 ; dernier cycle 503.2 ms
- Rejets (moteur) : {'spread_below_threshold': 64925684, 'liquidity_below_min': 1003339, 'negative_expected_net': 278785, 'cycle_budget_exhausted': 1584}
- Enregistrements de la session : 279117 ; net attendu > 0 : 332 ; simulés (eth_call de la vraie tx) : 30 (ok 29, échec 1) ; étiquettes ghost N+1 : 10/27 positives
- Décisions : {'REJECTED': 279117} ; motifs de rejet : {'below_safety_margin': 247, 'negative_expected_net': 278785, 'p_lower_below_threshold': 309, 'reliability_not_demonstrated': 23, 'simulation_failed': 1, 'stale_data': 28}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 56564036 | WETH→[aerodrome]→NPC→[uniswap_v2]→WETH | 0.011966 WETH | 0.000080 WETH | 0.000000 WETH | 0.000002 WETH | 0.000079 WETH (0.1449 €) | 0.000079 WETH | 65.72 | 0.006 (n=1) | REJECTED | reliability_not_demonstrated |
| 56572083 | cbBTC→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC | 0.003555 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0290 €) | — | 1.24 | 0.269 (n=1619) | REJECTED | below_safety_margin(44<71), p_lower_below_threshold(0.27<0.75) |
| 56572084 | cbBTC→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC | 0.003555 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0290 €) | — | 1.24 | 0.269 (n=1619) | REJECTED | below_safety_margin(44<71), p_lower_below_threshold(0.27<0.75) |
| 56572083 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 286.012905 USDC | 0.037587 USDC | 0.000000 USDC | 0.006085 USDC | 0.031502 USDC (0.0290 €) | — | 1.10 | 0.269 (n=1619) | REJECTED | below_safety_margin(31502<57202), p_lower_below_threshold(0.27<0.75) |
| 56572084 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 286.012905 USDC | 0.037587 USDC | 0.000000 USDC | 0.006093 USDC | 0.031494 USDC (0.0290 €) | — | 1.10 | 0.269 (n=1619) | REJECTED | below_safety_margin(31494<57202), p_lower_below_threshold(0.27<0.75) |
| 56572083 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→WETH | 0.142147 WETH | 0.000019 WETH | 0.000000 WETH | 0.000003 WETH | 0.000016 WETH (0.0289 €) | — | 1.10 | 0.269 (n=1619) | REJECTED | below_safety_margin(15671788024706<28429305439186), p_lower_below_threshold(0.27<0.75) |
| 56572084 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→WETH | 0.142147 WETH | 0.000019 WETH | 0.000000 WETH | 0.000003 WETH | 0.000016 WETH (0.0289 €) | — | 1.10 | 0.269 (n=1619) | REJECTED | below_safety_margin(15667763521501<28429305439186), p_lower_below_threshold(0.27<0.75) |
| 56572083 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 263.216814 USDC | 0.030932 USDC | 0.000000 USDC | 0.006085 USDC | 0.024847 USDC (0.0229 €) | — | 0.94 | 0.269 (n=1619) | REJECTED | below_safety_margin(24847<52643), p_lower_below_threshold(0.27<0.75) |
| 56572084 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 263.216814 USDC | 0.030932 USDC | 0.000000 USDC | 0.006093 USDC | 0.024839 USDC (0.0229 €) | — | 0.94 | 0.269 (n=1619) | REJECTED | below_safety_margin(24839<52643), p_lower_below_threshold(0.27<0.75) |
| 56572083 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.135721 WETH | 0.000015 WETH | 0.000000 WETH | 0.000003 WETH | 0.000012 WETH (0.0227 €) | — | 0.90 | 0.269 (n=1619) | REJECTED | below_safety_margin(12266523743846<27144165951627), p_lower_below_threshold(0.27<0.75) |
| 56572084 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.135721 WETH | 0.000015 WETH | 0.000000 WETH | 0.000003 WETH | 0.000012 WETH (0.0227 €) | — | 0.90 | 0.269 (n=1619) | REJECTED | below_safety_margin(12262499240641<27144165951627), p_lower_below_threshold(0.27<0.75) |
| 56572083 | cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.003312 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0224 €) | — | 1.03 | 0.269 (n=1619) | REJECTED | below_safety_margin(34<66), p_lower_below_threshold(0.27<0.75) |
| 56572084 | cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.003312 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0224 €) | — | 1.03 | 0.269 (n=1619) | REJECTED | below_safety_margin(34<66), p_lower_below_threshold(0.27<0.75) |
| 56572083 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 257.865069 USDC | 0.025905 USDC | 0.000000 USDC | 0.006085 USDC | 0.019820 USDC (0.0182 €) | — | 0.77 | 0.269 (n=1619) | REJECTED | below_safety_margin(19820<51573), p_lower_below_threshold(0.27<0.75) |
| 56572083 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC | 0.003227 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0178 €) | — | 0.84 | 0.269 (n=1619) | REJECTED | below_safety_margin(27<64), p_lower_below_threshold(0.27<0.75) |
| 56572083 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.109410 WETH | 0.000012 WETH | 0.000000 WETH | 0.000003 WETH | 0.000009 WETH (0.0174 €) | — | 0.86 | 0.269 (n=1619) | REJECTED | below_safety_margin(9426049907506<21881947331944), p_lower_below_threshold(0.27<0.75) |
| 56572083 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC→[uniswap_v3]→USDC | 262.706789 USDC | 0.022710 USDC | 0.000000 USDC | 0.006085 USDC | 0.016625 USDC (0.0153 €) | — | 0.63 | 0.269 (n=1619) | REJECTED | below_safety_margin(16625<52541), p_lower_below_threshold(0.27<0.75) |
| 56572084 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC→[uniswap_v3]→USDC | 262.706789 USDC | 0.022710 USDC | 0.000000 USDC | 0.006093 USDC | 0.016617 USDC (0.0153 €) | — | 0.63 | 0.269 (n=1619) | REJECTED | below_safety_margin(16617<52541), p_lower_below_threshold(0.27<0.75) |
| 56572083 | WETH→[pancakeswap_v3]→cbBTC→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.131213 WETH | 0.000011 WETH | 0.000000 WETH | 0.000003 WETH | 0.000008 WETH (0.0152 €) | — | 0.63 | 0.269 (n=1619) | REJECTED | below_safety_margin(8223550163283<26242563422196), p_lower_below_threshold(0.27<0.75) |
| 56572084 | WETH→[pancakeswap_v3]→cbBTC→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.131213 WETH | 0.000011 WETH | 0.000000 WETH | 0.000003 WETH | 0.000008 WETH (0.0152 €) | — | 0.63 | 0.269 (n=1619) | REJECTED | below_safety_margin(8219525660078<26242563422196), p_lower_below_threshold(0.27<0.75) |
| 56572083 | cbBTC→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC | 0.003505 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0152 €) | — | 0.66 | 0.269 (n=1619) | REJECTED | below_safety_margin(23<70), p_lower_below_threshold(0.27<0.75) |
| 56572084 | cbBTC→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC | 0.003505 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0152 €) | — | 0.66 | 0.269 (n=1619) | REJECTED | below_safety_margin(23<70), p_lower_below_threshold(0.27<0.75) |
| 56572083 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 272.987293 USDC | 0.019262 USDC | 0.000000 USDC | 0.006085 USDC | 0.013177 USDC (0.0121 €) | — | 0.48 | 0.269 (n=1619) | REJECTED | below_safety_margin(13177<54597), p_lower_below_threshold(0.27<0.75) |
| 56571777 | USDC→[aerodrome]→VIRTUAL→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 25.522497 USDC | 0.018791 USDC | 0.000000 USDC | 0.005811 USDC | 0.012980 USDC (0.0119 €) | — | 5.09 | 0.186 (n=328) | REJECTED | p_lower_below_threshold(0.19<0.75) |
| 56571777 | WETH→[uniswap_v3]→USDC→[aerodrome]→VIRTUAL→[aerodrome_slipstream]→WETH | 0.012768 WETH | 0.000009 WETH | 0.000000 WETH | 0.000003 WETH | 0.000006 WETH (0.0119 €) | 0.000006 WETH | 5.05 | 0.186 (n=328) | REJECTED | p_lower_below_threshold(0.19<0.75) |

## Fiabilité et décision
- Observations ghost : 8442 ; taux observé 0.222 ; borne inférieure crédible (0.9) 0.217 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 21.7% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ✅ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
