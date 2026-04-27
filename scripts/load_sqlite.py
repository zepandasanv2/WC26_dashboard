import sqlite3
import pandas as pd
import os

DB_DIR = "db"
DB_FILE = os.path.join(DB_DIR, "wc26.db")

CSV_FILE = "data/processed/matches.csv"