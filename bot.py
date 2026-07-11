from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)
from dotenv import load_dotenv
import os

from keyboards import main_menu

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "🤖 *Astra Bots*\n\n"
        "به مرکز ربات‌های Astra خوش آمدید.\n\n"
        "یکی از ربات‌های زیر را انتخاب کنید 👇"
    )

    await update.message.reply_text(
        text,
        reply_markup=main_menu(),
        parse_mode="Markdown",
    )


async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    text = (
        "⭐ *درباره Astra*\n\n"
        "Astra مجموعه‌ای از ربات‌های هوشمند است.\n\n"
        "🌍 Astra Time\n"
        "🌐 Astra Translate\n"
        "🤖 Astra AI\n\n"
        "به زودی ربات‌های بیشتری اضافه خواهند شد."
    )

    await query.edit_message_text(
        text=text,
        parse_mode="Markdown",
        reply_markup=main_menu(),
    )


def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(about, pattern="about"))

    print("✅ Astra Bots is running...")
    app.run_polling()


if __name__ == "__main__":
    main()
