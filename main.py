import logging
import os
from dotenv import load_dotenv
import speedtest-cli
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    MessageHandler, filters
)


from handlers.talk import (
    start,
    search_help,
    report,
    hours,
    net, bolsa_valores,


)

load_dotenv()

TOKEN = os.getenv("TELEGRAM_TOKEN_API")

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)


async def acoes(update: Update, context: ContextTypes.DEFAULT_TYPE):

    texto = update.message.text

    if texto == "💰 Cotação":
        await bolsa_valores(update, context)

    elif texto == "🕐 Tempo":
        await hours(update, context)

    elif texto == "❓ Ajuda":
        await search_help(update, context)

    elif texto == "📡 Net":
        await net(update, context)

    elif texto == "🚨 Reportar":
        await report(update, context)




app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help",search_help))
app.add_handler(CommandHandler("report",report))
app.add_handler(CommandHandler("hours",hours))
app.add_handler(CommandHandler("net",net))
app.add_handler(CommandHandler("bolsa", bolsa_valores))
app.add_handler(CommandHandler("acoes", acoes))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, acoes))




app.run_polling()
