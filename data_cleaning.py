import pandas as pd
import os

# Create processed folder if it doesn't exist
os.makedirs("data/processed", exist_ok=True)

# Files to clean
files = [
    "01_fund_master.csv",
    "02_nav_history.csv",
    "03_aum_by_fund_house.csv",
    "04_monthly_sip_inflows.csv",
    "05_category_inflows.csv",
    "06_industry_folio_count.csv",
    "07_scheme_performance.csv",
    "08_investor_transactions.csv",
    "09_portfolio_holdings.csv",
    "10_benchmark_indices.csv"
]

for file in files:
    path = os.path.join("data", "raw", file)

    if os.path.exists(path):
        print("=" * 60)
        print(f"Cleaning: {file}")

        df = pd.read_csv(path)

        # Remove duplicate rows
        df = df.drop_duplicates()

        # Remove leading/trailing spaces from column names
        df.columns = df.columns.str.strip()

        # Fill missing values
        for col in df.columns:
            if df[col].dtype == "object":
                df[col] = df[col].fillna("Unknown")
            else:
                df[col] = df[col].fillna(0)

        output_path = os.path.join("data", "processed", file)
        df.to_csv(output_path, index=False)

        print(f"Saved cleaned file -> {output_path}")
        print(f"Rows: {df.shape[0]} | Columns: {df.shape[1]}")
    else:
        print(f"{file} not found.")