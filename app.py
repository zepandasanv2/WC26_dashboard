import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)

def get_connection():
    return sqlite3.connect("db/wc26.db")


@app.route("/")
def home():
    return "API WC26 OK"