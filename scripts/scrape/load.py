from pathlib import Path
import requests

def load_html(url,target_name):
    project_root = Path(__file__).parent
    print(project_root)
    path_html = project_root / "html" / target_name
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url, headers=headers)

    # Sauvegarder le HTML dans un fichier
    with open(path_html, "w", encoding="utf-8") as file:
        file.write(response.text)
    print(f"HTML sauvegardé dans {path_html} !")

# Exécuter la fonction
url = "https://fr.wikipedia.org/wiki/Coupe_du_monde_de_football_2026"
load_html(url,"wikipedia.html")


    

