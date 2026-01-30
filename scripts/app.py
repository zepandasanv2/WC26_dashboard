from pathlib import Path
import pandas as pd

# Pour taper les fichiers peut importe où on se situe
project_root = Path(__file__).parent.parent

matchs_path = project_root / "data" / "matchs.csv"
joueurs_path = project_root / "data" / "joueurs.csv"

matchs = pd.read_csv(matchs_path)
joueurs = pd.read_csv(joueurs_path)

# Table print
print("=== Matchs ===")
print(matchs.head())
print("\n=== Joueurs ===")
print(joueurs.head())