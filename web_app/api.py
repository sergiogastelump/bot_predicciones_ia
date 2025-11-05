from flask import Flask, render_template
import os
import pandas as pd
from data.db_manager import DB_PATH, inicializar_db

app = Flask(__name__)

@app.route("/")
def index():
    try:
        if not os.path.exists(DB_PATH):
            inicializar_db()
        conn_str = f"sqlite:///{DB_PATH}"
        # si falla con pandas-read-sql en flask, puedes quitar esta parte
        return "✅ Web app activa. Aquí irán las tablas."
    except Exception as e:
        return f"⚠️ Error al cargar datos: {e}"

if __name__ == "__main__":
    app.run(debug=True)
