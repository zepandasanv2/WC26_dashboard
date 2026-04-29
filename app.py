import sqlite3
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

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

@app.route("/matches")
def get_matches():
    team = request.args.get("team")

    if not team:
        return jsonify({
            "error": "team parameter required",
            "example": "/matches?team=France"
    }), 400

    con = get_connection()
    cursor = con.cursor()

    cursor.execute("""
        SELECT date, time, opponent, round, ground
        FROM team_matches
        WHERE team = ?
    """, (team,))

    rows = cursor.fetchall()
    con.close()

    matches = [
        {
            "date": row[0],
            "time": row[1],
            "opponent": row[2],
            "round": row[3],
            "ground": row[4]
        }
        for row in rows
    ]

    return jsonify(matches)

if __name__ == "__main__":
    app.run(debug=True)