import os
import json
import pandas as pd
from datetime import datetime

# init var
RAW_DIR = "data/raw"
PROCESSED_DIR = "data/processed"

# Retrieve today date  
today = datetime.now().strftime("%Y%m%d")
ingestion_date = datetime.now().strftime("%Y-%m-%d")

input_file = os.path.join(RAW_DIR, f"baseWC_{today}.json")


output_file = os.path.join(PROCESSED_DIR, "matches.csv")

# create folder if not exist
os.makedirs(PROCESSED_DIR, exist_ok=True)

#read json
with open(input_file, "r", encoding="utf-8") as f:
    source = json.load(f)

# retrieve matches
matches = source.get("matches", [])

# Data transformation
rows = []
for match in matches:
    row = {
        "date": match.get("date"),
        "time": match.get("time"),
        "team1": match.get("team1"),
        "team2": match.get("team2"),
        "group": match.get("group"),
        "ground": match.get("ground"),
        "round": match.get("round"),
        "ingestion_date": ingestion_date
        
    }
    rows.append(row)

# df creation
df = pd.DataFrame(rows)

# to csv
df.to_csv(output_file, index=False, encoding="utf-8")

print(f"[SUCCESS] Transformed data saved to {output_file}")

