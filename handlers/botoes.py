from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ContextTypes


botoes = [
    ["💰 Cotação"],
    ["🕐 Tempo"],
    ["❓ Ajuda"],
    ["📡 Net"],
    ["🚨 Reportar"],
]

comandos_rapidos = ReplyKeyboardMarkup(
    botoes,
    resize_keyboard=True,
)


async def mostrar_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Escolha uma opção:",
        reply_markup=comandos_rapidos,
    )
