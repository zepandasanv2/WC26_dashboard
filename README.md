# World Cup 2026 Data Project

[![Daily ETL Pipeline](https://github.com/zepandasanv2/WC26_dashboard/actions/workflows/etl.yml/badge.svg)](https://github.com/zepandasanv2/WC26_dashboard/actions/workflows/etl.yml)

## Overview

This project is a data-driven application focused on the FIFA World Cup 2026.
It provides a complete pipeline from raw data ingestion to an interactive web interface.

The goal is to explore match data by team through a custom API and a lightweight frontend.

## Architecture 

```txt
JSON → Makefile → transform → CSV → SQLite → Flask API → Frontend
```

## Project Structure 
```txt
WC26_Data_Project/ 
├── data/ 
|   ├── raw/ # JSON files 
│   └── processed/ # matches.csv 
├── db/ 
│   └── wc26.db 
├── frontend/ 
│   ├── index.html 
│   └── app.js 
├── scripts 
    ├──transform.py # Data transformation script └── load_sqlite.py # Load CSV into SQLite 
├── app.py # Flask API 
├── Makefile # Data pipeline automation 
├── requirements.txt 
└── README.md
```

## Data Pipeline
The data pipeline is automated using a Makefile.

### Steps:
1. Data Ingestion
    - Fetch raw data (JSON)
2. Transformation
   - transform.py converts JSON into structured match data
3. Output
   - Generates:
   ```
   data/processed/matches.csv
   ```

### Run the pipeline
```bash
make pipeline
```
---

## Automation (GitHub Actions) 
The data pipeline is automated using a GitHub Actions workflow.

### Daily Execution

A scheduled workflow runs every day to:

- Execute the Makefile
- Fetch fresh data (JSON)
- Transform it into matches.csv

This ensures that the dataset stays up-to-date without manual intervention.

### Workflow Features
- Automated execution (cron job)
- Data refresh pipeline
- Integration with Makefile commands

### Notes 
- The pipeline currently handles ingestion and transformation
- Future improvements will include SQL integration within the pipeline

---
This setup demonstrates a real-world data engineering workflow with automation.

## Database Setup
Load the processed CSV into SQLite:
```bash
python load_sqlite.py
```

This creates:
```txt
db/wc26.db
```
With the table:
```txt
team_matches
```

## API Usage 
### Start the Flask API:
```bash
python app.py
```
Base URL: http://127.0.0.1:5000
### Endpoints 
- Get all teams
```txt
GET /teams
```
- Get matches for a team
```txt
GET /matches?team=TeamName
```txt
Example:
```txt
/matches?team=France
```

## Frontend
Run a local server:
```bash
cd frontend
python -m http.server
```
Open: http://localhost:8000

## Features 
- Team selection (dropdown)
- Dynamic API calls
- Match display:
   * Opponent
   * Date
   * Time
   * Stadium
   * Round

## Key concepts 
- Data pipeline automation with Makefile
- Data transformation (JSON → CSV)
- Database modeling with SQLite
- REST API design with Flask
- Frontend data rendering (JavaScript) 

## Future Improvements
- Stadium map visualization (Leaflet)
- UI improvements (Bootstrap)
- Advanced filtering
- Add SQL layer in Makefile pipeline
- Deployment

## Notifications Discord
(to translate in english)
### Configuration
1. Créer un webhook Discord :
   - Va dans les paramètres de ton serveur Discord > Intégrations > Webhooks > Nouveau Webhook.
   - Copie l’URL du webhook.

2. Ajouter l’URL du webhook :
   - Dans ton dépôt GitHub, va dans Settings > Secrets > Actions.
   - Ajoute un nouveau secret nommé DISCORD_WEBHOOK_URL avec l’URL copiée.

3. Le workflow YML (déjà configuré) utilisera ce secret pour envoyer des notifications automatiques lors des actions GitHub (ex : push, pull request).

## Contribuerer
(to translate in english)
Les contributions sont les bienvenues ! Ouvre une issue ou une pull request pour proposer des améliorations.

## Author
Ze Panda San 

## Licence
(to translate in english)
Ce projet est sous licence MIT.
