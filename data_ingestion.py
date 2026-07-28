import pandas as pd
import os

folder = "data/raw"

csv_files = sorted([f for f in os.listdir(folder) if f.endswith(".csv")])

print(f"\nFound {len(csv_files)} CSV files.\n")

for file in csv_files:

    print("=" * 80)
    print(f"FILE: {file}")

    path = os.path.join(folder, file)

    try:
        df = pd.read_csv(path)

        print("\nShape:")
        print(df.shape)

        print("\nColumns:")
        print(df.columns.tolist())

        print("\nData Types:")
        print(df.dtypes)

        print("\nFirst 5 Rows:")
        print(df.head())

        print("\nMissing Values:")
        print(df.isnull().sum())

        print("\nDuplicate Rows:")
        print(df.duplicated().sum())

    except Exception as e:
        print("Error reading file:", e)

    print("=" * 80)