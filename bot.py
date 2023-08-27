import os

from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

from check import check

load_dotenv()

PORT = os.getenv("PORT")
TOKEN = os.getenv("TOKEN")


async def check_perforce(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'🟨 Checking Perforce on {PORT} 🟨')
    if check(PORT):
        await update.message.reply_text(f'🟩 Perforce {PORT} is up 🟩')
    else:
        await update.message.reply_text(f'🟥 Perforce {PORT} is down 🟥')


def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("check", check_perforce))
    print("Bot started")
    app.run_polling()


if __name__ == '__main__':
    main()
