import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_stades_wikipedia():
    # URL de la page Wikipedia sur les stades de la CDM 2026
    url = "https://fr.wikipedia.org/wiki/Coupe_du_monde_de_football_de_2026#Stades"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Trouver la table des stades
    tables = soup.find_all('table', {'class': 'wikitable'})
    stades_table = tables[0]  # La première table contient les stades

    # Extraire les données
    stades = []
    for row in stades_table.find_all('tr')[1:]:  # Ignorer l'en-tête
        cols = row.find_all('td')
        if len(cols) >= 4:  # Vérifier qu'il y a assez de colonnes
            nom = cols[0].text.strip()
            ville = cols[1].text.strip()
            pays = cols[2].text.strip()
            capacite = cols[3].text.strip().replace('\xa0', '')  # Supprimer les espaces insécables

            stades.append({
                "nom": nom,
                "ville": ville,
                "pays": pays,
                "capacite": capacite
            })

    # Sauvegarder dans un CSV
    pd.DataFrame(stades).to_csv("data/raw/stades_scraped.csv", index=False)
    print("Stades scrapés et sauvegardés !")

# Exécuter la fonction
scrape_stades_wikipedia()