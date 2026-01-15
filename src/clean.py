import pandas as pd
import sys

# Read raw data
df = pd.read_csv("data/raw/data.csv")

# Clean data: Drop rows with missing values
df_clean = df.dropna()

# Save processed data
df_clean.to_csv("data/processed/clean_data.csv", index=False)
print("Data cleaned and saved.")
