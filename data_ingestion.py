import pandas as pd
import os

folder = "data/raw"

csv_files = [file for file in os.listdir(folder) if file.endswith(".csv")]

print(f"\nFound {len(csv_files)} CSV files.\n")

for file in csv_files:

    print("=" * 70)
    print(f"File: {file}")

    path = os.path.join(folder, file)

    df = pd.read_csv(path)
    df["date"] = pd.to_datetime(df["date"], format="%d-%m-%Y")
     print(df.dtypes)
    print(df.dtypes)
print(df.head())
df["date"] = pd.to_datetime(df["date"])

    print("\nShape:")
    print(df.shape)

    print("\nData Types:")
    print(df.dtypes)

    print("\nFirst 5 Rows:")
    print(df.head())

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nDuplicate Rows:")
    print(df.duplicated().sum())

    print("=" * 70)