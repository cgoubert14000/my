# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-12T11:38:39+00:00 ; durée 39.94 min ; blocs 56453704 → 56465681 (2030 vus)

## Connexion
- Requêtes RPC : 27191 ; erreurs : 0 ; latence p50/p95 : 388.0/1,412.0 ms
- Rafraîchissements d'état : 2030 ; âge des données au dernier bloc : 6.76 s ; changements de frais LP observés (pools à frais dynamiques) : 1167
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 638 ; cycles déclenchés par événement : 242 ; avance médiane sur le rafraîchissement multicall : 491 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,030.87 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 456 pools, 265 jetons, 15214 routes
- Par DEX : uniswap_v3 134, aerodrome_slipstream 98, aerodrome 186, pancakeswap_v3 25, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 1
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 159 (rejetés 2) → 564 jetons ; pools candidats 3626 (énumérés 282, par paires 0), mesurés 458, sous le plancher de 10000.0 $ : 2 → gardés 456 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2045.271447, 'cbBTC': 73394.102525, 'AERO': 0.529681}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 133,120,168 | 2,030.868324 | 56465681 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,310,731 | 0.027777 | 56465681 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 8,619,050 | 0.027806 | 56465681 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 8,372,247 | 0.000014 | 56465681 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 7,028,682 | 2,026.962634 | 56465681 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 6,795,900 | 104.049185 | 56465681 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,222,759 | 0.027786 | 56465681 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 4,180,940 | 1.902257 | 56465681 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,162,765 | 2,027.488418 | 56465681 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,851,700 | 0.998657 | 56465681 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,019,176 | 42,344.562426 | 56465681 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 169 | 2,834,623 | 2,027.305321 | 56465681 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2505 | 2,179,716 | 0.027819 | 56465681 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 1,925,361 | 1,127,807.662643 | 56465681 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | XDP/USDC | 100 | 1,652,948 | 0.016864 | 56465681 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | USDC/cbBTC | 568 | 1,637,098 | 0.000014 | 56465681 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,582,749 | 0.000014 | 56465681 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,545,681 | 0.000000 | 56465681 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,517,107 | 0.000014 | 56465681 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,502,074 | 0.006593 | 56465681 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,462,089 | 0.829972 | 56465681 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,387,962 | 432.451691 | 56465681 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v2 | WETH/USDC | 3000 | 1,263,729 | 2,031.021026 | 56465681 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| uniswap_v3 | WETH/AERO | 3000 | 1,231,186 | 3,854.141022 | 56465681 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,200,217 | 15,547.764549 | 56465681 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/USDC | 3000 | 1,149,575 | 2,031.233285 | 56465681 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,118,919 | 2,026.697191 | 56465681 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,061,623 | 86.218152 | 56465681 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,046,779 | 1.389936 | 56465681 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | WETH/doginme | 10000 | 1,027,547 | 33,847,318.837345 | 56465681 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/VVV | 10000 | 1,008,470 | 104.215602 | 56465681 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome_slipstream | USDC/VELVET | 100 | 954,235 | 21.791087 | 56465681 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/BRETT | 10000 | 927,830 | 562,928.380412 | 56465681 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 906,010 | 0.001479 | 56465681 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| uniswap_v3 | USDC/VVV | 3000 | 894,323 | 0.051159 | 56465681 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome_slipstream | USDC/cbBTC | 356 | 892,338 | 0.000014 | 56465681 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | WETH/TOSHI | 10000 | 888,176 | 23,276,199.996804 | 56465681 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | WETH/USDC | 10000 | 873,814 | 2,045.150933 | 56465681 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 869,873 | 1,022.953583 | 56465681 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | DRB/WETH | 10000 | 854,476 | 0.000000 | 56465681 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | USDC/NOCK | 3000 | 773,394 | 78.637659 | 56465681 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| pancakeswap_v3 | QUID/USDC | 100 | 745,225 | 0.049474 | 56465681 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome_slipstream | USDC/SAPIEN | 4555 | 744,239 | 23.156927 | 56465681 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome | WETH/EDEL | 7000 | 734,593 | 116,512.360305 | 56465681 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | WETH/AERO | 10000 | 692,034 | 3,849.674049 | 56465681 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | WETH/wstETH | 3000 | 688,060 | 0.801801 | 56465681 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 659,629 | 0.520257 | 56465681 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 637,241 | 4,815,930.290155 | 56465681 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 616,256 | 0.477929 | 56465681 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/NPC | 3000 | 581,348 | 154,710.658792 | 56465681 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome | VIRTUAL/WETH | 10000 | 569,266 | 0.000257 | 56465681 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/BRETT | 2099 | 569,014 | 565,576.055003 | 56465681 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome_slipstream | AERO/cbBTC | 1025 | 563,490 | 0.000007 | 56465681 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v3 | FLOCK/USDC | 3000 | 554,337 | 0.037161 | 56465681 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome_slipstream | WETH/MORPHO | 2703 | 484,388 | 1,022.061107 | 56465681 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| pancakeswap_v3 | ELSA/USDC | 100 | 458,386 | 0.065760 | 56465681 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| aerodrome_slipstream | USDC/USDT | 8 | 453,298 | 1.001040 | 56465681 | `0xa41Bc0AFfbA7Fd420d186b84899d7ab2aC57fcD1` |
| uniswap_v3 | USDC/MORPHO | 10000 | 444,677 | 0.501968 | 56465681 | `0x2043B296fFC6b2d3bf4A3F3167d2Afb3B0FBdbEE` |
| uniswap_v3 | WETH/uSOL | 3000 | 435,912 | 24.794769 | 56465681 | `0xab04A352D4EC8d0F1812A4E5EBe7807Fa67acD48` |
| aerodrome | cbBTC/EDGE | 7000 | 430,713 | 929,980.086525 | 56465681 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |

## Recherche d'opportunités
- Cycles : 2271 ; routes examinées : 34550994 ; candidats optimisés : 186976 ; net attendu > 0 : 184 ; dernier cycle 419.8 ms
- Rejets (moteur) : {'spread_below_threshold': 33935221, 'liquidity_below_min': 425678, 'negative_expected_net': 186792, 'borrow_bound_too_small': 2271, 'cycle_budget_exhausted': 848}
- Enregistrements de la session : 186976 ; net attendu > 0 : 184 ; simulés (eth_call de la vraie tx) : 15 (ok 12, échec 3) ; étiquettes ghost N+1 : 12/12 positives
- Décisions : {'REJECTED': 186976} ; motifs de rejet : {'below_safety_margin': 114, 'negative_expected_net': 186792, 'p_lower_below_threshold': 174, 'reliability_not_demonstrated': 10, 'sim_below_estimate': 6, 'simulated_net_nonpositive': 5, 'simulation_failed': 3, 'stale_data': 8}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 56463349 | WETH→[pancakeswap_v3]→EURC→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.050848 WETH | 0.000029 WETH | 0.000000 WETH | 0.000003 WETH | 0.000026 WETH (0.0486 €) | — | 5.09 | 0.203 (n=1243) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.20<0.75) |
| 56463349 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→EURC→[aerodrome_slipstream]→USDC | 103.311208 USDC | 0.058790 USDC | 0.000000 USDC | 0.006190 USDC | 0.052600 USDC (0.0484 €) | — | 5.09 | 0.203 (n=1243) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 56463349 | WETH→[pancakeswap_v3]→EURC→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.043081 WETH | 0.000024 WETH | 0.000000 WETH | 0.000003 WETH | 0.000021 WETH (0.0402 €) | — | 4.97 | 0.203 (n=1243) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.20<0.75) |
| 56463349 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→EURC→[aerodrome_slipstream]→USDC | 87.411861 USDC | 0.049699 USDC | 0.000000 USDC | 0.006190 USDC | 0.043509 USDC (0.0400 €) | — | 4.98 | 0.203 (n=1243) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 56463349 | WETH→[aerodrome_slipstream]→AAVE→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.028294 WETH | 0.000019 WETH | 0.000000 WETH | 0.000003 WETH | 0.000016 WETH (0.0304 €) | — | 5.73 | 0.311 (n=577) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.31<0.75) |
| 56463349 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→AAVE→[uniswap_v3]→USDC | 57.177531 USDC | 0.039098 USDC | 0.000000 USDC | 0.006190 USDC | 0.032908 USDC (0.0303 €) | — | 5.76 | 0.311 (n=577) | REJECTED | p_lower_below_threshold(0.31<0.75) |
| 56460049 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 503.872102 USDC | 0.036307 USDC | 0.000000 USDC | 0.006149 USDC | 0.030158 USDC (0.0277 €) | — | 0.60 | 0.160 (n=43) | REJECTED | below_safety_margin(30158<100774), p_lower_below_threshold(0.16<0.75) |
| 56460049 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.005935 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0277 €) | — | 0.69 | 0.160 (n=43) | REJECTED | below_safety_margin(41<118), p_lower_below_threshold(0.16<0.75) |
| 56460049 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.245576 WETH | 0.000018 WETH | 0.000000 WETH | 0.000003 WETH | 0.000015 WETH (0.0275 €) | — | 0.60 | 0.160 (n=43) | REJECTED | below_safety_margin(14617304400314<49115134048151), p_lower_below_threshold(0.16<0.75) |
| 56463349 | WETH→[pancakeswap_v3]→EURC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.038174 WETH | 0.000017 WETH | 0.000000 WETH | 0.000003 WETH | 0.000014 WETH (0.0254 €) | — | 3.55 | 0.203 (n=1243) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 56463349 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→EURC→[aerodrome_slipstream]→USDC | 77.549336 USDC | 0.033710 USDC | 0.000000 USDC | 0.006190 USDC | 0.027520 USDC (0.0253 €) | — | 3.55 | 0.203 (n=1243) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 56463349 | WETH→[pancakeswap_v3]→EURC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.032432 WETH | 0.000014 WETH | 0.000000 WETH | 0.000003 WETH | 0.000011 WETH (0.0207 €) | — | 3.40 | 0.203 (n=1243) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 56463349 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→EURC→[aerodrome_slipstream]→USDC | 65.695777 USDC | 0.028612 USDC | 0.000000 USDC | 0.006190 USDC | 0.022422 USDC (0.0206 €) | — | 3.41 | 0.203 (n=1243) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 56463349 | WETH→[pancakeswap_v3]→EURC→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→WETH | 0.032937 WETH | 0.000013 WETH | 0.000000 WETH | 0.000003 WETH | 0.000010 WETH (0.0181 €) | — | 2.93 | 0.269 (n=1594) | REJECTED | p_lower_below_threshold(0.27<0.75) |
| 56463349 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→EURC→[aerodrome_slipstream]→USDC | 67.203615 USDC | 0.025802 USDC | 0.000000 USDC | 0.006190 USDC | 0.019612 USDC (0.0180 €) | — | 2.92 | 0.269 (n=1594) | REJECTED | p_lower_below_threshold(0.27<0.75) |
| 56463349 | WETH→[aerodrome_slipstream]→AAVE→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.022517 WETH | 0.000012 WETH | 0.000000 WETH | 0.000003 WETH | 0.000009 WETH (0.0174 €) | — | 4.12 | 0.203 (n=1243) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 56463349 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→AAVE→[uniswap_v3]→USDC | 45.477976 USDC | 0.025052 USDC | 0.000000 USDC | 0.006190 USDC | 0.018862 USDC (0.0174 €) | — | 4.15 | 0.203 (n=1243) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 56463349 | WETH→[pancakeswap_v3]→EURC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.032924 WETH | 0.000012 WETH | 0.000000 WETH | 0.000003 WETH | 0.000009 WETH (0.0170 €) | — | 2.75 | 0.269 (n=1594) | REJECTED | p_lower_below_threshold(0.27<0.75) |
| 56463349 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→EURC→[aerodrome_slipstream]→USDC | 67.037385 USDC | 0.024566 USDC | 0.000000 USDC | 0.006190 USDC | 0.018376 USDC (0.0169 €) | — | 2.74 | 0.269 (n=1594) | REJECTED | p_lower_below_threshold(0.27<0.75) |
| 56463349 | WETH→[pancakeswap_v3]→EURC→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→WETH | 0.028058 WETH | 0.000011 WETH | 0.000000 WETH | 0.000003 WETH | 0.000008 WETH (0.0146 €) | — | 2.77 | 0.269 (n=1594) | REJECTED | p_lower_below_threshold(0.27<0.75) |
| 56463349 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→EURC→[aerodrome_slipstream]→USDC | 57.115439 USDC | 0.021980 USDC | 0.000000 USDC | 0.006190 USDC | 0.015790 USDC (0.0145 €) | — | 2.76 | 0.269 (n=1594) | REJECTED | p_lower_below_threshold(0.27<0.75) |
| 56463349 | WETH→[pancakeswap_v3]→EURC→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.029276 WETH | 0.000010 WETH | 0.000000 WETH | 0.000003 WETH | 0.000007 WETH (0.0136 €) | — | 2.48 | 0.269 (n=1594) | REJECTED | p_lower_below_threshold(0.27<0.75) |
| 56463349 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→EURC→[uniswap_v3]→USDC | 59.269275 USDC | 0.020924 USDC | 0.000000 USDC | 0.006190 USDC | 0.014734 USDC (0.0136 €) | — | 2.49 | 0.269 (n=1594) | REJECTED | p_lower_below_threshold(0.27<0.75) |
| 56463349 | WETH→[pancakeswap_v3]→EURC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.027890 WETH | 0.000010 WETH | 0.000000 WETH | 0.000003 WETH | 0.000007 WETH (0.0135 €) | — | 2.58 | 0.269 (n=1594) | REJECTED | p_lower_below_threshold(0.27<0.75) |
| 56463349 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→EURC→[aerodrome_slipstream]→USDC | 56.201653 USDC | 0.020806 USDC | 0.000000 USDC | 0.006190 USDC | 0.014616 USDC (0.0134 €) | — | 2.60 | 0.269 (n=1594) | REJECTED | p_lower_below_threshold(0.27<0.75) |

## Fiabilité et décision
- Observations ghost : 8279 ; taux observé 0.219 ; borne inférieure crédible (0.9) 0.213 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 21.3% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
