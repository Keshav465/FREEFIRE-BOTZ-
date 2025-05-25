import os
from dotenv import load_dotenv
from telegram.ext import ApplicationBuilder
git add src/bot
git commit -m "Add bot module"
# Absolute import (if bot is in the same directory as main.py)
from bot.handlers import like_handler

def start_bot():
    load_dotenv()
    token = os.getenv("BOT_TOKEN")

    app = ApplicationBuilder().token(token).build()

    # Register command handlers
    app.add_handler(like_handler)

    print("✅ Bot started...")
    app.run_polling()
