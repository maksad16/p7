import pandas as pd
import os

# Ensure directory exists
os.makedirs("data/raw", exist_ok=True)

# Simulate fetching raw data
data = {
    "id": [1, 2, 3, 4],
    "name": ["Sahil", "Bob", "Charlie", None],
    "age": [25, 30, 35, None]
}

df = pd.DataFrame(data)
df.to_csv("data/raw/data.csv", index=False)
print("Raw data ingested.")
