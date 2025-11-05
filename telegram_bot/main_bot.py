import os
from flask import Flask, request
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from dotenv import load_dotenv
from services.ia_service import predecir_partido

load_dotenv()
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
PORT = int(os.environ.get("PORT", 10000))

app = Flask(__name__)
application = Application.builder().token(TELEGRAM_TOKEN).build()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 Bienvenido al Bot de Predicciones Deportivas con IA!\n"
        "Usa /predecir equipo1 vs equipo2 para obtener una predicción."
    )

async def predecir(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) < 3:
        await update.message.reply_text("❌ Formato incorrecto. Ejemplo: /predecir America vs Chivas")
        return
    equipo_local, equipo_visitante = context.args[0], context.args[2]
    resultado = predecir_partido(equipo_local, equipo_visitante)
    await update.message.reply_text(
        f"🔮 Predicción: {resultado['resultado']}\n"
        f"Probabilidad de acierto: {resultado['probabilidad']}%"
    )

application.add_handler(CommandHandler("start", start))
application.add_handler(CommandHandler("predecir", predecir))

@app.route("/", methods=["GET"])
def home():
    return "✅ Servidor Flask activo y webhook operativo.", 200

@app.route("/webhook", methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(force=True), application.bot)
    application.update_queue.put_nowait(update)
    return "✅ Webhook recibido correctamente", 200

if __name__ == "__main__":
    print(f"🚀 Servidor corriendo en puerto {PORT}")
    app.run(host="0.0.0.0", port=PORT)
