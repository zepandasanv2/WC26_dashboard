# World Cup 2026 Dashboard

Ce projet consiste à créer un dashboard interactif pour suivre en temps réel les performances, statistiques et données clés de la Coupe du Monde 2026, qui se déroulera aux États-Unis, Canada et Mexique du 11 juin au 19 juillet 2026. Cette édition sera historique avec 48 équipes (contre 32 auparavant) et un format inédit.

---

## Fonctionnalités
- Visualisation des statistiques : Top buteurs, buts par équipe, cartes jaunes.
- Données structurées : Matchs, joueurs, stades.
- Notifications Discord : Alertes pour les actions importantes (ex : commits, déploiements).

---

## Installation

### Prérequis
- Python 3.11+
- Un environnement virtuel (recommandé)

### Étapes
1. Cloner le dépôt :
```bash
   git clone <URL_DU_DÉPÔT>
   cd WC26_Dashboard
```
2. Créer et activer un environnement virtuel :
```bash
   python -m venv venv
   source venv/bin/activate  # Linux
```

3. Installer les dépendances :
```bash
   pip install -r requirements.txt
```
---
## Lancer le Dashboard
```bash
python scripts/dashboard.py
```
Ouvre http://127.0.0.1:8050 dans ton navigateur.

---

## Notifications Discord

### Configuration
1. Créer un webhook Discord :
   - Va dans les paramètres de ton serveur Discord > Intégrations > Webhooks > Nouveau Webhook.
   - Copie l’URL du webhook.

2. Ajouter l’URL du webhook :
   - Dans ton dépôt GitHub, va dans Settings > Secrets > Actions.
   - Ajoute un nouveau secret nommé DISCORD_WEBHOOK_URL avec l’URL copiée.

3. Le workflow YML (déjà configuré) utilisera ce secret pour envoyer des notifications automatiques lors des actions GitHub (ex : push, pull request).

---

## Structure du Projet
```
WC26_Dashboard/
│
├── data/                  # Données CSV (matchs, joueurs, stades)
│   ├── matchs.csv
│   └── joueurs.csv
│
├── scripts/               # Scripts Python
│   ├── app.py             # Chargement des données
│   └── dashboard.py       # Dashboard interactif
│
├── .ipynb_checkpoints
|   └── exploration_cdm2026-checkpoint.ipynb
|
├── .github/workflows/     # Workflows GitHub Actions (inclut le YML pour Discord)
│
├── requirements.txt       # Dépendances Python
├── README.md               # Ce fichier
└── .gitignore
```
---

## Prochaines Étapes
- Déployer le dashboard en ligne (ex : Render, Heroku).
- Intégrer des données réelles via une API (ex : API Football Data).
- Ajouter des filtres interactifs (ex : sélectionner une équipe).

---

## Contribuerdd
Les contributions sont les bienvenues ! Ouvre une issue ou une pull request pour proposer des améliorations.

---

## Licence
Ce projet est sous licence MIT.
