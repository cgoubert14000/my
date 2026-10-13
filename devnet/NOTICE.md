# Third-party artifacts

`devnet/artifacts/*.json` are extracted (by `extract_artifacts.py`) from the official npm packages:

| Package | Version | License |
|---|---|---|
| @uniswap/v2-core | 1.0.1 | GPL-3.0 |
| @uniswap/v2-periphery | 1.1.0-beta.0 | GPL-3.0 |
| @uniswap/v3-core | 1.0.1 | BUSL-1.1 → GPL-2.0-or-later (change date 2023-04-01) |
| @uniswap/v3-periphery | 1.4.4 | GPL-2.0-or-later |

They are used **only** for local testing (Foundry tests and the anvil devnet). They are not modified.
