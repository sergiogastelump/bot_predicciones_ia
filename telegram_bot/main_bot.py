import os
from flask import Flask, request
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from dotenv import load_dotenv
from services.ia_service import predecir_partido

# Cargar variables
load_dotenv()
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
PORT = int(os.environ.get("PORT", 10000))

if not TELEGRAM_TOKEN:
    raise ValueError("❌ No se encontró TELEGRAM_TOKEN")

# Flask (para Render)
app = Flask(__name__)

# Telegram bot
application = Application.builder().token(TELEGRAM_TOKEN).build()

# ---------- Comandos ----------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 Bienvenido al Bot de Predicciones Deportivas con IA!\n"
        "Comandos:\n"
        "/predecir America vs Chivas"
    )

async def predecir(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Esperamos formato: /predecir equipo1 vs equipo2
    if len(context.args) < 3:
        await update.message.reply_text("❌ Formato incorrecto. Usa: /predecir Equipo1 vs Equipo2")
        return

    equipo_local = context.args[0]
    equipo_visitante = context.args[2]
    pred = predecir_partido(equipo_local, equipo_visitante)

    await update.message.reply_text(
        f"🔮 Predicción:\n{pred['resultado']}\n"
        f"Probabilidad de acierto: {pred['probabilidad']}%"
    )

# Registrar comandos
application.add_handler(CommandHandler("start", start))
application.add_handler(CommandHandler("predecir", predecir))

# ---------- Rutas Flask ----------
@app.route("/", methods=["GET"])
def home():
    return "✅ Servidor Flask activo y webhook operativo.", 200

@app.route("/webhook", methods=["POST"])
def webhook():
    """
    Telegram envía aquí los mensajes.
    """
    update = Update.de_json(request.get_json(force=True), application.bot)
    application.update_queue.put_nowait(update)
    return "✅ Webhook recibido", 200

# ---------- Main ----------
if __name__ == "__main__":
    print(f"🚀 Servidor corriendo en puerto {PORT}")
    app.run(host="0.0.0.0", port=PORT)
