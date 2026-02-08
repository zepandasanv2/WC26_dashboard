from pathlib import Path
import pandas as pd

def clean_stades():
    
    project_root = Path(__file__).parent.parent.parent.parent
    path_host_cities = project_root / "data" / "raw" / "level1" / "host_cities.csv"
    path_stades = project_root / "data" / "raw" / "level2" / "stades.csv"
    #print("Path : ", path_host_cities)
    
    df = pd.read_csv(path_host_cities)  

    df.drop(['id', 'region_cluster', 'airport_code'], axis=1, inplace=True)

    
    df.rename(columns={
        "venue_name": "nom",
        "city_name": "ville",
        "country": "pays",
    }, inplace=True)
    

    df.insert(0, "stade_id", range(1, len(df) + 1))

    

    """
    stades_officiels = [
        "Estadio Azteca", "MetLife Stadium", "Stade Olympique", "Stade BC Place",
        "SoFi Stadium", "AT&T Stadium", "NRG Stadium", "Arrowhead Stadium",
        "Mercedes-Benz Stadium", "Gillette Stadium", "Levi's Stadium", "Lumen Field",
        "Lincoln Financial Field", "Estadio Akron", "Estadio BBVA"
    ]
    df = df[df["nom"].isin(stades_officiels)]
    """
    
    df.to_csv(path_stades, index=False)
    print(f'Fichier stades.csv créé avec succès dans {path_stades}  !')
    

if __name__ == "__main__":
    clean_stades()
