import pandas as pd
from sqlalchemy import create_engine
import os

# Create SQLite database
engine = create_engine("sqlite:///mutual_fund.db")

processed_folder = "data/processed"

# Load every cleaned CSV into SQLite
for file in os.listdir(processed_folder):
    if file.endswith(".csv"):
        table_name = file.replace(".csv", "")
        file_path = os.path.join(processed_folder, file)

        df = pd.read_csv(file_path)

        df.to_sql(
            table_name,
            engine,
            if_exists="replace",
            index=False
        )

        print(f"Table '{table_name}' created successfully.")

print("\nAll tables imported into mutual_fund.db")