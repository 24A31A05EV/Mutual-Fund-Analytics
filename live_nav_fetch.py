import requests
import pandas as pd
import os

os.makedirs("data/raw", exist_ok=True)

schemes = {
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_Large_Cap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

for name, code in schemes.items():
    url = f"https://api.mfapi.in/mf/{code}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        print(f"\n{name}")
        print("Scheme:", data["meta"]["scheme_name"])

        df = pd.DataFrame(data["data"])

        file_path = f"data/raw/{name}.csv"
        df.to_csv(file_path, index=False)

        print(f"Saved: {file_path}")

    else:
        print(f"Failed to fetch {name}")