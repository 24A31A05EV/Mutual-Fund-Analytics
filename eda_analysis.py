import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset
df = pd.read_csv("data/processed/01_fund_master.csv")

print("=" * 60)
print("DATASET OVERVIEW")
print("=" * 60)

print("\nShape:")
print(df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nSummary Statistics:")
print(df.describe())

# -----------------------------
# Business Question 1
# Schemes per Fund House
# -----------------------------
fund_house_count = df["fund_house"].value_counts()

print("\nSchemes by Fund House:")
print(fund_house_count)

plt.figure(figsize=(10,5))
fund_house_count.plot(kind="bar")
plt.title("Number of Schemes by Fund House")
plt.xlabel("Fund House")
plt.ylabel("Number of Schemes")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# -----------------------------
# Business Question 2
# Category Distribution
# -----------------------------
category_count = df["category"].value_counts()

print("\nCategory Distribution:")
print(category_count)

plt.figure(figsize=(6,6))
category_count.plot(kind="pie", autopct="%1.1f%%")
plt.ylabel("")
plt.title("Scheme Category Distribution")
plt.tight_layout()
plt.show()

# -----------------------------
# Business Question 3
# Risk Category
# -----------------------------
risk_count = df["risk_category"].value_counts()

print("\nRisk Category Distribution:")
print(risk_count)

plt.figure(figsize=(8,5))
risk_count.plot(kind="bar")
plt.title("Risk Category Distribution")
plt.xlabel("Risk Category")
plt.ylabel("Number of Schemes")
plt.xticks(rotation=30)
plt.tight_layout()
plt.show()
# ---------------------------------
# Average Expense Ratio by Category
# ---------------------------------

expense = df.groupby("category")["expense_ratio_pct"].mean().sort_values()

print("\nAverage Expense Ratio by Category")
print(expense)

plt.figure(figsize=(6,4))
expense.plot(kind="bar")
plt.title("Average Expense Ratio by Category")
plt.xlabel("Category")
plt.ylabel("Expense Ratio (%)")
plt.tight_layout()
plt.show()
# ---------------------------------
# Top Fund Managers
# ---------------------------------

managers = df["fund_manager"].value_counts().head(10)

print("\nTop Fund Managers")
print(managers)

plt.figure(figsize=(10,5))
managers.plot(kind="bar")
plt.title("Top Fund Managers")
plt.xlabel("Fund Manager")
plt.ylabel("Number of Schemes")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
# ---------------------------------
# Risk Category Distribution
# ---------------------------------

risk = df["risk_category"].value_counts()

plt.figure(figsize=(6,6))
risk.plot(kind="pie", autopct="%1.1f%%")
plt.title("Risk Category Distribution")
plt.ylabel("")
plt.tight_layout()
plt.show()