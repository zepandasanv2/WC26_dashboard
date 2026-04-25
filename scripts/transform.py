import os
import json
import pandas as pd
from datetime import datetime

# init var
RAW_DIR = "data/raw"
PROCESSED_DIR = "data/processed"

# Retrieve today date  
today = datetime.now().strftime("%Y%m%d")


input_file = os.path.join(RAW_DIR, f"baseWC_{today}.json")


output_file = os.path.join(PROCESSED_DIR, "matches.csv")

# create folder if not exist
os.makedirs(PROCESSED_DIR, exist_ok=True)