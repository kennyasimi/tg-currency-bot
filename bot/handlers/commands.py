from telegram import Update
from telegram.ext import ContextTypes


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    welcome_text = """
🏦 *Welcome to Ratez Bot!* 💱

Use /convert to start converting currencies!
    """
    await update.message.reply_text(welcome_text, parse_mode='Markdown')


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_text = """
💱 *Ratez Bot Help Center* 🌍
Use /convert or type '100 USD to EUR'
    """
    await update.message.reply_text(help_text, parse_mode='Markdown')
