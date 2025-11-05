import sqlite3
import pandas as pd
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "bot_predicciones.db")

def inicializar_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS partidos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        deporte TEXT,
        liga TEXT,
        equipo_local TEXT,
        equipo_visitante TEXT,
        fecha TEXT,
        prob_local REAL,
        prob_empate REAL,
        prob_visitante REAL
    )''')
    conn.commit()
    conn.close()

def obtener_partidos(limit=10):
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query(f"SELECT * FROM partidos LIMIT {limit}", conn)
    conn.close()
    return df
