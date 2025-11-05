from flask import Flask, render_template
import pandas as pd
from data.db_manager import DB_PATH

app = Flask(__name__)

@app.route("/")
def index():
    try:
        df = pd.read_sql_query("SELECT * FROM partidos LIMIT 10;", f"sqlite:///{DB_PATH}")
        return render_template("index.html", registros=df.to_dict(orient="records"))
    except Exception as e:
        return f"⚠️ Error al cargar datos: {e}"

if __name__ == "__main__":
    app.run(debug=True)
