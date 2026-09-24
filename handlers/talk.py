from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)
from datetime import datetime, date, time, timedelta
import httpx


from servico.control import valuate_connection
from servico.currency import buscar_cotacoes_brl
from handlers.botoes import comandos_rapidos




async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Olá! Eu sou um bot. 👋",
        reply_markup=comandos_rapidos
    )

async def search_help(update: Update,context: ContextTypes.DEFAULT_TYPE):

    await  update.message.reply_text(
        "Sim, como poderia te ajudar ?",
        reply_markup=comandos_rapidos
    )

async def report(update: Update,context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Qual bug do telegram voce gostaria de reportar?",
    reply_markup=comandos_rapidos)


async def hours(update: Update,context):
    inicio = datetime.now()
    await update.message.reply_text(f"Agora e exatamente {inicio} tenha um bom dia",
    reply_markup=comandos_rapidos)


async def net(update: Update,context):
    download, upload = valuate_connection()
    await update.message.reply_text(f'resultado da conexao e: {download:.2f}Mbps de download e {upload:.2f}Mbps upload',
    reply_markup=comandos_rapidos)


async def bolsa_valores(update: Update, context):

    async with httpx.AsyncClient() as client:

        cotacoes = await buscar_cotacoes_brl(client)

    mensagem = (
        "📊 *Cotações*\n\n"
        f"🇺🇸 USD: R$ {cotacoes['usd']:.2f}\n"
        f"🇨🇦 CAD: R$ {cotacoes['cad']:.2f}\n"
        f"🇬🇧 GBP: R$ {cotacoes['gbp']:.2f}\n"
        f"🇪🇺 EUR: R$ {cotacoes['eur']:.2f}\n\n"
        "💰 *Conversão de 100 unidades:*\n\n"
        f"🇺🇸 100 USD: R$ {cotacoes['usd'] * 100:.2f}\n"
        f"🇨🇦 100 CAD: R$ {cotacoes['cad'] * 100:.2f}\n"
        f"🇬🇧 100 GBP: R$ {cotacoes['gbp'] * 100:.2f}\n"
        f"🇪🇺 100 EUR: R$ {cotacoes['eur'] * 100:.2f}"
    )

    await update.message.reply_text(
        mensagem,
        parse_mode="Markdown",
        reply_markup=comandos_rapidos,

    )


