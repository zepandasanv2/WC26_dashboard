import sqlite3
import pandas as pd
import os

DB_DIR = "db"
DB_FILE = os.path.join(DB_DIR, "wc26.db")
CSV_FILE = "data/processed/matches.csv"

os.makedirs(DB_DIR, exist_ok=True)
conn = sqlite3.connect(DB_FILE)
df = pd.read_csv(CSV_FILE)

df_team1 = df.rename(columns={
    "team1": "team",
    "team2": "opponent"
})

df_team2 = df.rename(columns={
    "team2": "team",
    "team1": "opponent"
})

df_final = pd.concat([df_team1, df_team2], ignore_index=True)