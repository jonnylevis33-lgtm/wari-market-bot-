import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Activer les logs pour voir les erreurs sur Render
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

TOKEN = os.getenv("TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Salut ! \n\n"
        "Je suis le bot Wari Market ✅\n"
        "Tape /help pour voir ce que je peux faire"
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Commandes disponibles:\n"
        "/start - Lancer le bot\n"
        "/help - Aide"
    )

def main():
    if not TOKEN:
        logger.error("ERREUR: La variable TOKEN n'est pas définie")
        return
    
    logger.info("Démarrage du bot...")
    app = Application.builder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    
    logger.info("Bot en ligne")
    app.run_polling()

if __name__ == "__main__":
    main()
