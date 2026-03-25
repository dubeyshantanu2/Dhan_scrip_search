import pandas as pd
import zipfile
import io

def search_scrip(query: str, zip_path: str = "api-scrip-master-detailed.csv.zip") -> pd.DataFrame:
    """
    Search the scrip master CSV for a keyword and return all matching rows.

    Args:
        query     : Search term (e.g. "NIFTY", "BANKNIFTY", "RELIANCE")
        zip_path  : Path to the zip file containing the CSV

    Returns:
        DataFrame with matching rows, showing key columns
    """
    # Read CSV from inside the zip
    with zipfile.ZipFile(zip_path, 'r') as z:
        csv_filename = [f for f in z.namelist() if f.endswith('.csv')][0]
        with z.open(csv_filename) as f:
            df = pd.read_csv(f, low_memory=False)

    # Strip whitespace from column names
    df.columns = df.columns.str.strip()

    # Search across key text columns (case-insensitive)
    search_cols = ["UNDERLYING_SYMBOL", "SYMBOL_NAME", "DISPLAY_NAME"]
    mask = df[search_cols].apply(
        lambda col: col.astype(str).str.contains(query, case=False, na=False)
    ).any(axis=1)

    results = df[mask].copy()

    if results.empty:
        print(f"No results found for '{query}'")
        return results

    # Return key columns
    key_cols = [
        "EXCH_ID", "SEGMENT", "SECURITY_ID", "UNDERLYING_SECURITY_ID",
        "UNDERLYING_SYMBOL", "SYMBOL_NAME", "DISPLAY_NAME",
        "INSTRUMENT_TYPE", "SERIES", "LOT_SIZE",
        "SM_EXPIRY_DATE", "STRIKE_PRICE", "OPTION_TYPE"
    ]
    # Only keep columns that exist
    key_cols = [c for c in key_cols if c in results.columns]

    print(f"Found {len(results)} result(s) for '{query}'")
    return results[key_cols].reset_index(drop=True)


# ── Example usage ──────────────────────────────────────────────────────────────
if __name__ == "__main__":
    results = search_scrip("GOLDPETAL")
    print(results.to_string(index=False))
