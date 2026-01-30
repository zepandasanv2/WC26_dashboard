from pathlib import Path
import pandas as pd

def load_data():
    """Charge les données des matchs et des joueurs depuis les fichiers CSV."""
    project_root = Path(__file__).parent.parent
    matchs_path = project_root / "data" / "matchs.csv"
    joueurs_path = project_root / "data" / "joueurs.csv"

    matchs = pd.read_csv(matchs_path)
    joueurs = pd.read_csv(joueurs_path)

    return matchs, joueurs

if __name__ == "__main__":
    matchs, joueurs = load_data()
    print("=== Données chargées avec succès ===")
    print("Matchs :", matchs.shape)
    print("Joueurs :", joueurs.shape)
