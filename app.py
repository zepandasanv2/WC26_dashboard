import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)

def get_connection():
    return sqlite3.connect("db/wc26.db")


@app.route("/")
def home():
    return "API WC26 OK"

@app.route("/teams")
def get_teams():
    con = get_connection()
    cursor = con.cursor()

    cursor.execute("""
        SELECT DISTINCT team 
        FROM team_matches
        ORDER BY team
    """)

    teams = [row[0] for row in cursor.fetchall()]

    con.close()

    return jsonify(teams)

if __name__ == "__main__":
    app.run(debug=True)