import pandas as pd

df = pd.read_csv("data/processed/01_fund_master.csv")

print("=" * 60)
print("BUSINESS INSIGHTS")
print("=" * 60)

# 1. Total schemes
print(f"\nTotal Schemes: {len(df)}")

# 2. Total fund houses
print(f"Total Fund Houses: {df['fund_house'].nunique()}")

# 3. Most common category
print("\nMost Common Category:")
print(df["category"].value_counts().head(1))

# 4. Most common risk category
print("\nMost Common Risk Category:")
print(df["risk_category"].value_counts().head(1))

# 5. Average expense ratio
print(f"\nAverage Expense Ratio: {df['expense_ratio_pct'].mean():.2f}%")

# 6. Top 5 Fund Houses
print("\nTop 5 Fund Houses:")
print(df["fund_house"].value_counts().head())