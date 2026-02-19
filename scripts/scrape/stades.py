from pathlib import Path
from bs4 import BeautifulSoup
import pandas as pd

def stadium_extract():
    project_root = Path(__file__)
    source_path = project_root.parent / "html" / "wikipedia.html"
    with open(source_path , "r", encoding="utf-8") as file:
        html_content = file.read()
    
    soup = BeautifulSoup(html_content, 'html.parser')
    
    tables = soup.find_all("table")

    print("Nombre de tableaux :", len(tables))
    

    print(tables[4])
stadium_extract()