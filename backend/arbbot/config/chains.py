"""Chain registry: tokens, DEX factories, flash-loan providers, infra contracts.

IMPORTANT — mainnet addresses below come from public documentation as of the author's knowledge and are
flagged `verified=False` until `arbbot verify-chain` has probed them on a live RPC (code present + ABI probe).
The engine refuses to leave read-only mode on a chain whose config has not been verified.
"""
from __future__ import annotations

import json
import pathlib
from dataclasses import dataclass, field

from ..core.types import DexKind, FlashSource, Token


@dataclass(frozen=True)
class DexConfig:
    id: str
    kind: DexKind
    factory: str
    fee_ppm: int = 3000  # default LP fee for V2-style factories (V3 fee tiers are per pool)
    fee_tiers: tuple[int, ...] = ()  # V3: tiers to scan
    solidly_fee_from_factory: bool = False  # Aerodrome: getFee(pool, stable)
    dynamic_fee: bool = False  # pool.fee() can change between blocks (Slipstream fee modules) → re-read every refresh
    enabled: bool = True
    notes: str = ""


@dataclass(frozen=True)
class FlashProviderConfig:
    source: FlashSource
    address: str
    fee_bps: float  # expected fee (verified live where the protocol exposes it)
    notes: str = ""


@dataclass
class ChainConfig:
    id: str
    chain_id: int
    name: str
    native_symbol: str
    wrapped_native: str
    tokens: dict[str, Token]
    dexes: list[DexConfig]
    flash_providers: list[FlashProviderConfig]
    multicall3: str = "0xcA11bde05977b3631167028862bE2a173976CA11"
    block_time_s: float = 2.0
    l1_fee_model: str = "none"  # "opstack" | "arbitrum" | "none"
    opstack_gas_oracle: str = "0x420000000000000000000000000000000000000F"
    executor: str = ""
    verified: bool = False
    explorer_tx: str = ""
    extra: dict = field(default_factory=dict)
    # tokens the route finder is allowed to borrow (must have deep flash liquidity)
    borrowable: tuple[str, ...] = ("WETH", "USDC")
    # explicit pools (devnet) – mainnet pools are discovered from factories
    static_pools: list[dict] = field(default_factory=list)

    def token(self, symbol: str) -> Token:
        return self.tokens[symbol]

    def token_by_address(self, address: str) -> Token | None:
        a = address.lower()
        for t in self.tokens.values():
            if t.address.lower() == a:
                return t
        return None


def _t(address: str, symbol: str, decimals: int) -> Token:
    return Token(address, symbol, decimals)


BASE = ChainConfig(
    id="base",
    chain_id=8453,
    name="Base",
    native_symbol="ETH",
    wrapped_native="0x4200000000000000000000000000000000000006",
    tokens={
        "WETH": _t("0x4200000000000000000000000000000000000006", "WETH", 18),
        "USDC": _t("0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913", "USDC", 6),
        "USDbC": _t("0xd9aAEc86B65D86f6A7B5B1b0c42FFA531710b6CA", "USDbC", 6),
        "DAI": _t("0x50c5725949A6F0c72E6C4a641F24049A917DB0Cb", "DAI", 18),
        "cbETH": _t("0x2Ae3F1Ec7F1F5012CFEab0185bfc7aa3cf0DEc22", "cbETH", 18),
        "cbBTC": _t("0xcbB7C0000aB88B473b1f5aFd9ef808440eed33Bf", "cbBTC", 8),
        "AERO": _t("0x940181a94A35A4569E4529A3CDfB74e38FD98631", "AERO", 18),
    },
    dexes=[
        DexConfig("uniswap_v3", DexKind.UNIV3, "0x33128a8fC17869897dcE68Ed026d694621f6FDfD", fee_tiers=(100, 500, 3000, 10000)),
        DexConfig("uniswap_v2", DexKind.UNIV2, "0x8909Dc15e40173Ff4699343b6eB8132c65e18eC6", fee_ppm=3000),
        DexConfig("sushiswap_v2", DexKind.UNIV2, "0x71524B4f93c58fcbF659783284E38825f0622859", fee_ppm=3000),
        DexConfig("sushiswap_v3", DexKind.UNIV3, "0xc35DADB65012eC5796536bD9864eD8773aBc74C4", fee_tiers=(100, 500, 3000, 10000)),
        DexConfig("pancakeswap_v3", DexKind.PANCAKE_V3, "0x0BFbCF9fa4f9C56B0F40a671Ad40E0805A091865", fee_tiers=(100, 500, 2500, 10000)),
        DexConfig("pancakeswap_v2", DexKind.UNIV2, "0x02a84c1b3BBD7401a5f7fa98a384EBC70bB5749E", fee_ppm=2500),
        DexConfig("baseswap_v2", DexKind.UNIV2, "0xFDa619b6d20975be80A10332cD39b9a4b0FAa8BB", fee_ppm=2500, enabled=False,
                  notes="address NOT confirmed from an official repository/package → disabled until verified by the operator"),
        DexConfig("aerodrome", DexKind.SOLIDLY, "0x420DD381b31aEf6683db6B902084cB0FFECe40Da", solidly_fee_from_factory=True),
        DexConfig(
            "aerodrome_slipstream", DexKind.UNIV3, "0x5e7BB104d84c7CB9B682AaC2F3d509f5F406809A", fee_tiers=(),
            dynamic_fee=True,
            notes="CL pools keyed by tickSpacing (1,50,100,200,2000); fee read from pool.fee() — dynamic (fee module), re-read every block",
        ),
    ],
    flash_providers=[
        FlashProviderConfig(FlashSource.MORPHO, "0xBBBBBbbBBb9cC5e90e3b3Af64bdAF62C37EEFFCb", 0.0, "0 fee; capacity = token balance of Morpho"),
        FlashProviderConfig(FlashSource.BALANCER_V2, "0xBA12222222228d8Ba445958a75a0704d566BF2C8", 0.0, "0 fee; V2 TVL collapsed after Nov-2025 exploit → check capacity live"),
        FlashProviderConfig(FlashSource.AAVE_V3, "0xA238Dd80C259a72e81d7e4664a9801593F98d1c5", 5.0, "FLASHLOAN_PREMIUM_TOTAL read live"),
    ],
    block_time_s=2.0,
    l1_fee_model="opstack",
    explorer_tx="https://basescan.org/tx/",
    borrowable=("WETH", "USDC"),
)

ARBITRUM = ChainConfig(
    id="arbitrum",
    chain_id=42161,
    name="Arbitrum One",
    native_symbol="ETH",
    wrapped_native="0x82aF49447D8a07e3bd95BD0d56f35241523fBab1",
    tokens={
        "WETH": _t("0x82aF49447D8a07e3bd95BD0d56f35241523fBab1", "WETH", 18),
        "USDC": _t("0xaf88d065e77c8cC2239327C5EDb3A432268e5831", "USDC", 6),
        "USDCe": _t("0xFF970A61A04b1cA14834A43f5dE4533eBDDB5CC8", "USDC.e", 6),  # bridged USDC; no longer listed by Aave → symbol/decimals checked live
        "USDT": _t("0xFd086bC7CD5C481DCC9C85ebE478A1C0b69FCbb9", "USDT", 6),
        "DAI": _t("0xDA10009cBd5D07dd0CeCc66161FC93D7c9000da1", "DAI", 18),
        "WBTC": _t("0x2f2a2543B76A4166549F7aaB2e75Bef0aefC5B0f", "WBTC", 8),
        "ARB": _t("0x912CE59144191C1204E64559FE8253a0e49E6548", "ARB", 18),
    },
    dexes=[
        DexConfig("uniswap_v3", DexKind.UNIV3, "0x1F98431c8aD98523631AE4a59f267346ea31F984", fee_tiers=(100, 500, 3000, 10000)),
        DexConfig("uniswap_v2", DexKind.UNIV2, "0xf1D7CC64Fb4452F05c498126312eBE29f30Fbcf9", fee_ppm=3000),
        DexConfig("sushiswap_v2", DexKind.UNIV2, "0xc35DADB65012eC5796536bD9864eD8773aBc74C4", fee_ppm=3000),
        DexConfig("sushiswap_v3", DexKind.UNIV3, "0x1af415a1EbA07a4986a52B6f2e7dE7003D82231e", fee_tiers=(100, 500, 3000, 10000)),
        DexConfig("pancakeswap_v3", DexKind.PANCAKE_V3, "0x0BFbCF9fa4f9C56B0F40a671Ad40E0805A091865", fee_tiers=(100, 500, 2500, 10000)),
        DexConfig(
            "camelot_v2", DexKind.UNIV2, "0x6EcCab422D763aC031210895C81787E87B43A652", fee_ppm=3000, enabled=False,
            notes="Camelot pairs have directional dynamic fees (token0FeePercent/token1FeePercent) → needs a dedicated adapter",
        ),
    ],
    flash_providers=[
        FlashProviderConfig(FlashSource.MORPHO, "0x6c247b1F6182318877311737BaC0844bAa518F5e", 0.0, "0 fee; source @morpho-org/morpho-ts addresses (ArbitrumMainnet.blue)"),
        FlashProviderConfig(FlashSource.BALANCER_V2, "0xBA12222222228d8Ba445958a75a0704d566BF2C8", 0.0, "0 fee; check capacity live"),
        FlashProviderConfig(FlashSource.AAVE_V3, "0x794a61358D6845594F94dc1DB02A252b5b4814aD", 5.0, "FLASHLOAN_PREMIUM_TOTAL read live"),
    ],
    block_time_s=0.25,
    l1_fee_model="arbitrum",
    explorer_tx="https://arbiscan.io/tx/",
    borrowable=("WETH", "USDC"),
)


# Provenance of every mainnet address above (checked 2026-10-13 from official repositories / packages — the sandbox used
# to build this project had no RPC access, so on-chain presence is confirmed by `arbbot verify-chain` on the operator's
# machine). Keys are lower-case addresses.
ADDRESS_SOURCES: dict[str, str] = {
    # Base
    "0x4200000000000000000000000000000000000006": "OP-stack WETH predeploy; bgd-labs/aave-address-book AaveV3Base WETH_UNDERLYING",
    "0x833589fcd6edb6e08f4c7c32d4f71b54bda02913": "bgd-labs/aave-address-book AaveV3Base USDC_UNDERLYING (Circle native USDC)",
    "0xd9aaec86b65d86f6a7b5b1b0c42ffa531710b6ca": "bgd-labs/aave-address-book AaveV3Base USDbC_UNDERLYING; sushi npm tokens/base/USDbC",
    "0x50c5725949a6f0c72e6c4a641f24049a917db0cb": "sushi npm package evm/config/tokens/DAI (BASE)",
    "0x2ae3f1ec7f1f5012cfeab0185bfc7aa3cf0dec22": "bgd-labs/aave-address-book AaveV3Base cbETH_UNDERLYING",
    "0xcbb7c0000ab88b473b1f5afd9ef808440eed33bf": "bgd-labs/aave-address-book AaveV3Base cbBTC_UNDERLYING",
    "0x940181a94a35a4569e4529a3cdfb74e38fd98631": "sushi npm package evm/config/tokens/AERO (BASE)",
    "0x33128a8fc17869897dce68ed026d694621f6fdfd": "@uniswap/sdk-core 7.19 BASE_ADDRESSES.v3CoreFactoryAddress",
    "0x8909dc15e40173ff4699343b6eb8132c65e18ec6": "@uniswap/sdk-core 7.19 V2_FACTORY_ADDRESSES[BASE]",
    "0x71524b4f93c58fcbf659783284e38825f0622859": "sushi npm package evm/config/features/sushiswap-v2 (BASE factory)",
    "0xc35dadb65012ec5796536bd9864ed8773abc74c4": "sushi npm package: SushiSwap V3 factory on BASE / V2 factory on ARBITRUM",
    "0x0bfbcf9fa4f9c56b0f40a671ad40e0805a091865": "@pancakeswap/v3-sdk FACTORY_ADDRESSES (BASE, ARBITRUM_ONE)",
    "0x02a84c1b3bbd7401a5f7fa98a384ebc70bb5749e": "@pancakeswap/v2-sdk FACTORY_ADDRESS_MAP (BASE, ARBITRUM_ONE)",
    "0xfda619b6d20975be80a10332cd39b9a4b0faa8bb": "BaseSwap docs only — NOT confirmed from an official repository (disabled)",
    "0x420dd381b31aef6683db6b902084cb0ffece40da": "aerodrome-finance/contracts README (PoolFactory)",
    "0x5e7bb104d84c7cb9b682aac2f3d509f5f406809a": "aerodrome-finance/slipstream README (CL PoolFactory, Base)",
    "0xbbbbbbbbbb9cc5e90e3b3af64bdaf62c37eeffcb": "@morpho-org/morpho-ts addresses (BaseMainnet.blue / EthMainnet.blue)",
    "0xba12222222228d8ba445958a75a0704d566bf2c8": "balancer/balancer-deployments addresses/base.json 20210418-vault",
    "0xa238dd80c259a72e81d7e4664a9801593f98d1c5": "bgd-labs/aave-address-book AaveV3Base.POOL",
    "0x420000000000000000000000000000000000000f": "OP-stack GasPriceOracle predeploy",
    "0xca11bde05977b3631167028862be2a173976ca11": "mds1/multicall Multicall3 (same address on all chains)",
    # Arbitrum
    "0x82af49447d8a07e3bd95bd0d56f35241523fbab1": "bgd-labs/aave-address-book AaveV3Arbitrum WETH_UNDERLYING",
    "0xaf88d065e77c8cc2239327c5edb3a432268e5831": "bgd-labs/aave-address-book AaveV3Arbitrum USDCn_UNDERLYING (native USDC)",
    "0xff970a61a04b1ca14834a43f5de4533ebddb5cc8": "bridged USDC.e — not in current Aave address book; verified live only",
    "0xfd086bc7cd5c481dcc9c85ebe478a1c0b69fcbb9": "bgd-labs/aave-address-book AaveV3Arbitrum USDT_UNDERLYING",
    "0xda10009cbd5d07dd0cecc66161fc93d7c9000da1": "bgd-labs/aave-address-book AaveV3Arbitrum DAI_UNDERLYING",
    "0x2f2a2543b76a4166549f7aab2e75bef0aefc5b0f": "bgd-labs/aave-address-book AaveV3Arbitrum WBTC_UNDERLYING",
    "0x912ce59144191c1204e64559fe8253a0e49e6548": "bgd-labs/aave-address-book AaveV3Arbitrum ARB_UNDERLYING",
    "0x1f98431c8ad98523631ae4a59f267346ea31f984": "@uniswap/sdk-core DEFAULT_ADDRESSES.v3CoreFactoryAddress (Arbitrum One)",
    "0xf1d7cc64fb4452f05c498126312ebe29f30fbcf9": "@uniswap/sdk-core 7.19 V2_FACTORY_ADDRESSES[ARBITRUM_ONE]",
    "0x1af415a1eba07a4986a52b6f2e7de7003d82231e": "sushi npm package evm/config/features/sushiswap-v3 (ARBITRUM factory)",
    "0x6c247b1f6182318877311737bac0844baa518f5e": "@morpho-org/morpho-ts addresses (ArbitrumMainnet.blue)",
    "0x794a61358d6845594f94dc1db02a252b5b4814ad": "bgd-labs/aave-address-book AaveV3Arbitrum.POOL",
    "0x6eccab422d763ac031210895c81787e87b43a652": "Camelot docs — disabled (dynamic directional fees need a dedicated adapter)",
}


def address_source(address: str) -> str:
    return ADDRESS_SOURCES.get(address.lower(), "UNKNOWN SOURCE — verify manually before use")


def load_local(deployments_path: pathlib.Path) -> ChainConfig:
    d = json.loads(pathlib.Path(deployments_path).read_text())
    tokens = {k: Token(v["address"], v["symbol"], v["decimals"]) for k, v in d["tokens"].items()}
    dex_ids = sorted({p["dex"] for p in d["pools"]})
    kinds = {p["dex"]: DexKind[p["kind"]] for p in d["pools"]}
    def _factory(did: str) -> str:
        if kinds[did] == DexKind.UNIV2:
            return d["v2_factories"].get(did, "") or ""
        if kinds[did] in (DexKind.UNIV3, DexKind.PANCAKE_V3):
            return d.get("v3_factory", "") or ""
        return d.get("solidly_factory", "") or ""  # devnet Solidly pools are deployed without a factory

    dexes = [DexConfig(did, kinds[did], _factory(did)) for did in dex_ids]
    providers = [
        FlashProviderConfig(FlashSource[k], v, {"BALANCER_V2": 0.0, "AAVE_V3": 5.0, "MORPHO": 0.0}[k])
        for k, v in d["flash_providers"].items()
    ]
    return ChainConfig(
        id="local",
        chain_id=d["chain_id"],
        name="Local devnet (anvil)",
        native_symbol="ETH",
        wrapped_native=d["native_wrapped"],
        tokens=tokens,
        dexes=dexes,
        flash_providers=providers,
        multicall3=d.get("multicall3", "0xcA11bde05977b3631167028862bE2a173976CA11"),
        block_time_s=2.0,
        l1_fee_model="none",
        executor=d["executor"],
        verified=True,  # devnet addresses are generated locally
        extra={"accounts": d["accounts"], "prices_usd": d["prices_usd"], "v3_helper": d.get("v3_helper")},
        borrowable=("WETH", "USDC", "DAI"),
        static_pools=d["pools"],
    )


def get_chain(chain: str, devnet_path: pathlib.Path | None = None) -> ChainConfig:
    if chain == "base":
        return BASE
    if chain == "arbitrum":
        return ARBITRUM
    if chain == "local":
        if devnet_path is None or not pathlib.Path(devnet_path).exists():
            raise FileNotFoundError("devnet/deployments.local.json not found — run `python devnet/deploy_devnet.py`")
        return load_local(devnet_path)
    raise KeyError(chain)
