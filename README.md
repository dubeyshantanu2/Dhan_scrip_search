# Dhan Scrip Search

A lightweight Python utility to search [Dhan's](https://dhan.co/) scrip master CSV for stocks, derivatives, and commodities across BSE, NSE, and MCX.

## Overview

Dhan publishes a detailed scrip master file containing **~279,000 instruments** spanning:

| Exchange | Segments |
|----------|----------|
| **NSE**  | Cash (C), Derivatives (D), Index (I) |
| **BSE**  | Cash (C), Equity Derivatives (E) |
| **MCX**  | Commodity Derivatives (M) |

This tool loads the compressed CSV and performs fast, case-insensitive keyword searches across `UNDERLYING_SYMBOL`, `SYMBOL_NAME`, and `DISPLAY_NAME`.

## Prerequisites

- Python 3.8+
- [pandas](https://pandas.pydata.org/)

## Installation

```bash
git clone https://github.com/dubeyshantanu2/Dhan_scrip_search.git
cd Dhan_scrip_search
pip install pandas
```

## Usage

### As a script

```bash
python search_scrip.py
```

By default it searches for `"GOLDPETAL"`. Edit the `__main__` block in `search_scrip.py` to change the query.

### As a module

```python
from search_scrip import search_scrip

# Search for NIFTY options
results = search_scrip("NIFTY")
print(results.head())

# Search for a specific stock
results = search_scrip("RELIANCE")
print(results.to_string(index=False))
```

### Function Signature

```python
search_scrip(query: str, zip_path: str = "api-scrip-master-detailed.csv.zip") -> pd.DataFrame
```

| Parameter  | Type  | Default | Description |
|------------|-------|---------|-------------|
| `query`    | `str` | —       | Search term (e.g. `"NIFTY"`, `"BANKNIFTY"`, `"RELIANCE"`) |
| `zip_path` | `str` | `"api-scrip-master-detailed.csv.zip"` | Path to the zip file containing the scrip master CSV |

**Returns:** A `DataFrame` with matching rows containing the key columns listed below.

## Output Columns

| Column | Description |
|--------|-------------|
| `EXCH_ID` | Exchange — `NSE`, `BSE`, or `MCX` |
| `SEGMENT` | Market segment (`C` = Cash, `D` = Derivatives, `E` = Equity Derivatives, `M` = MCX, `I` = Index) |
| `SECURITY_ID` | Dhan's unique security identifier |
| `UNDERLYING_SECURITY_ID` | Security ID of the underlying instrument |
| `UNDERLYING_SYMBOL` | Underlying trading symbol |
| `SYMBOL_NAME` | Full symbol name |
| `DISPLAY_NAME` | Human-readable display name |
| `INSTRUMENT_TYPE` | Type of instrument |
| `SERIES` | Trading series (e.g. `EQ`, `BE`) |
| `LOT_SIZE` | Contract lot size |
| `SM_EXPIRY_DATE` | Expiry date (for derivatives) |
| `STRIKE_PRICE` | Strike price (for options) |
| `OPTION_TYPE` | `CE` (Call) or `PE` (Put) |

## Data Source

The scrip master CSV is sourced from [Dhan's API documentation](https://dhanhq.co/docs/v2/).  
The included zip file (`api-scrip-master-detailed.csv.zip`) is a snapshot; download the latest version from Dhan for up-to-date instrument data.

## License

This project is provided as-is for educational and personal use.
