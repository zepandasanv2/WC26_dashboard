from pathlib import Path
import pandas as pd
import dash
from dash import dcc, html
import plotly.express as px

# Charger les données
def load_data():
    project_root = Path(__file__).parent.parent
    matchs_path = project_root / "data" / "matchs.csv"
    joueurs_path = project_root / "data" / "joueurs.csv"
    matchs = pd.read_csv(matchs_path)
    joueurs = pd.read_csv(joueurs_path)
    return matchs, joueurs

matchs, joueurs = load_data()

# Calculer les buts par équipe
buts_par_equipe = joueurs.groupby("equipe")["buts"].sum().reset_index()

# Initialiser l'application Dash
app = dash.Dash(__name__)

# Layout du dashboard
app.layout = html.Div([
    html.H1("Dashboard CDM 2026", style={"textAlign": "center", "color": "#1E90FF"}),
    dcc.Graph(
        id="top-buteurs",
        figure=px.bar(
            joueurs.sort_values("buts", ascending=False).head(5),
            x="nom",
            y="buts",
            title="Top 5 des buteurs",
            labels={"nom": "Joueur", "buts": "Nombre de buts"},
            color="equipe"
        ),
        style={"margin": "20px"}
    ),
    dcc.Graph(  # <-- Virgule ajoutée ici
        id="buts-par-equipe",
        figure=px.bar(
            buts_par_equipe,
            x="equipe",
            y="buts",
            title="Nombre de buts par équipe",
            labels={"equipe": "Équipe", "buts": "Nombre de buts"}
        ),
        style={"margin": "20px"}
    ),  
    dcc.Graph(
    id="cartons-jaunes",
    figure=px.histogram(
        joueurs,
        x="cartons_jaunes",
        title="Répartition des cartons jaunes",
        labels={"cartons_jaunes": "Nombre de cartons jaunes", "count": "Nombre de joueurs"},
        nbins=3,  # Force à avoir 3 bins (pour 0, 0.5, et 1)
        range_x=[-0.5, 1.5]  # Ajuste l'axe X pour centrer les valeurs
    ),
    style={"margin": "20px"}
)

], style={"backgroundColor": "#f9f9f9", "padding": "20px"})

# Lancer le serveur
if __name__ == "__main__":
    app.run(debug=True)
