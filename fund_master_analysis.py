import pandas as pd

# Load fund master
df = pd.read_csv("data/raw/01_fund_master.csv")

print("=" * 60)
print("FUND MASTER INFORMATION")
print("=" * 60)

print("\nTotal Schemes:", len(df))
print("Total Fund Houses:", df["fund_house"].nunique())
print("Total Categories:", df["category"].nunique())
print("Total Sub Categories:", df["sub_category"].nunique())
print("Total Risk Categories:", df["risk_category"].nunique())

print("\nUnique Fund Houses")
print(df["fund_house"].unique())

print("\nUnique Categories")
print(df["category"].unique())

print("\nUnique Sub Categories")
print(df["sub_category"].unique())

print("\nUnique Risk Categories")
print(df["risk_category"].unique())