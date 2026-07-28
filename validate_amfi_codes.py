import pandas as pd

fund_master = pd.read_csv("data/raw/01_fund_master.csv")
nav_history = pd.read_csv("data/raw/02_nav_history.csv")

print("=" * 60)
print("AMFI CODE VALIDATION")
print("=" * 60)

master_codes = set(fund_master["amfi_code"])
nav_codes = set(nav_history["amfi_code"])

missing_codes = master_codes - nav_codes

print(f"Fund Master Codes : {len(master_codes)}")
print(f"NAV History Codes : {len(nav_codes)}")

if len(missing_codes) == 0:
    print("\n✅ SUCCESS")
    print("Every AMFI code exists in nav_history.")
else:
    print("\n❌ Missing Codes")
    print(missing_codes)