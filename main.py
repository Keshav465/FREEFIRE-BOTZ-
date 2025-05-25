import os
from dotenv import load_dotenv
from telegram.ext import ApplicationBuilder
from bot.handlers import like_handler

def start_bot():
    load_dotenv()
    token = os.getenv("BOT_TOKEN")

    app = ApplicationBuilder().token(token).build()

    # Register command handlers
    app.add_handler(like_handler)

    print("✅ Bot started...")
    app.run_polling()
