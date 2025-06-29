"""
population_viz.py
Visualise World Bank total‑population data:
  • Bar chart of top‑N populous countries for a chosen year
  • Histogram of population distribution across all countries
Author: <your‑name>
"""

import io
import zipfile
import requests
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# --------------------------- CONFIG ------------------------------------------------
YEAR      = 2022       # change this to any year available in the dataset (1960‑2023)
TOP_N     = 10         # number of countries to show in the bar chart
SAVE_DIR  = "."        # folder where PNGs will be saved
# -----------------------------------------------------------------------------------

def download_worldbank_population_zip() -> bytes:
    """
    Fetches the zipped CSV bundle for indicator SP.POP.TOTL via the World Bank API.
    Returns the raw bytes of the ZIP file.
    """
    url = "https://api.worldbank.org/v2/en/indicator/SP.POP.TOTL?downloadformat=csv"
    resp = requests.get(url, timeout=120)
    resp.raise_for_status()
    return resp.content   # binary ZIP bytes

def extract_population_csv(zip_bytes: bytes) -> pd.DataFrame:
    """
    Opens the ZIP file in‑memory, finds the main data CSV, and loads it into a DataFrame.
    """
    with zipfile.ZipFile(io.BytesIO(zip_bytes)) as zf:
        # The data file name starts with "API_SP.POP.TOTL" and ends with ".csv"
        data_file = [f for f in zf.namelist() if f.startswith("API_SP.POP.TOTL") and f.endswith(".csv")][0]
        # First 4 rows are header notes → skip them
        df = pd.read_csv(zf.open(data_file), skiprows=4)
    return df

def clean_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """
    Keep real countries (ISO‑3 codes) and drop aggregates like 'World'.
    A real country row always has a 3‑char Country Code and an income level in the 'IncomeGroup' column.
    """
    # If 'Country Code' length == 3 → likely a country (aggregates like '1W', '8S' are shorter)
    # Use str.len() for safety
    mask = df["Country Code"].str.len() == 3
    df_countries = df[mask].copy()
    return df_countries

def prepare_top_n(df: pd.DataFrame, year: int, top_n: int) -> pd.DataFrame:
    """
    For the requested year, drop NaNs and return the top‑N countries by population.
    """
    col = str(year)
    if col not in df.columns:
        raise ValueError(f"Year {year} not found in the dataset.")
    temp = df[["Country Name", col]].dropna()
    temp = temp.sort_values(by=col, ascending=False).head(top_n)
    return temp

def plot_bar_chart(df_top: pd.DataFrame, year: int, path: str):
    plt.figure(figsize=(10, 6))
    plt.bar(df_top["Country Name"], df_top[str(year)])
    plt.xticks(rotation=45, ha="right")
    plt.title(f"Top {len(df_top)} Countries by Population ({year:,})")
    plt.ylabel("Population")
    plt.tight_layout()
    plt.savefig(path, dpi=300)
    plt.show()

def plot_histogram(df_all: pd.DataFrame, year: int, path: str):
    plt.figure(figsize=(10, 6))
    plt.hist(df_all[str(year)].dropna(), bins=20, edgecolor="black")
    plt.title(f"Distribution of Country Populations ({year:,})")
    plt.xlabel("Population")
    plt.ylabel("Number of Countries")
    plt.tight_layout()
    plt.savefig(path, dpi=300)
    plt.show()

def main():
    print("🔄 Downloading World Bank population data …")
    zip_bytes = download_worldbank_population_zip()
    df_raw    = extract_population_csv(zip_bytes)
    df_clean  = clean_dataframe(df_raw)

    # Create the bar chart
    df_top = prepare_top_n(df_clean, YEAR, TOP_N)
    bar_path = f"{SAVE_DIR}/top{TOP_N}_population_{YEAR}.png"
    hist_path = f"{SAVE_DIR}/population_histogram_{YEAR}.png"

    print(f"📊 Plotting bar chart for top‑{TOP_N} countries ({YEAR}) …")
    plot_bar_chart(df_top, YEAR, bar_path)
    print(f"✅ Saved: {bar_path}")

    # Create the histogram
    print("📊 Plotting histogram for all countries …")
    plot_histogram(df_clean, YEAR, hist_path)
    print(f"✅ Saved: {hist_path}")

    print("\n🎉 Finished! Charts saved in:", SAVE_DIR)

if __name__ == "__main__":
    t0 = datetime.now()
    try:
        main()
    except Exception as e:
        print("❌ Error:", e)
    finally:
        print(f"⏱  Runtime: {(datetime.now() - t0).seconds} seconds")