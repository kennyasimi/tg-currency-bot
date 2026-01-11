


from bot.handlers.commands import start_command, help_command
from bot.handlers.messages import handle_message
from bot.handlers.conversation import (
    AMOUNT, FROM_CURRENCY, TO_CURRENCY,
    convert_command, handle_amount,
    handle_from_currency, handle_to_currency,
    cancel_command
)
from bot.config import TOKEN, BOT_USERNAME



from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters, ConversationHandler

# Setup logging
from bot.utils.logger import logger


# ERROR HANDLER
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.error(f"Update {update} caused error {context.error}")


# MAIN -where our program starts and where the event loop is started
if __name__ == '__main__':
    print('🚀 Starting Ratez Bot...')
    print(f'🤖 Bot Username: {BOT_USERNAME}')

    app = Application.builder().token(TOKEN).build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('convert', convert_command)],
        states={
            AMOUNT: [MessageHandler(filters.TEXT & ~filters.COMMAND, handle_amount)],
            FROM_CURRENCY: [MessageHandler(filters.TEXT & ~filters.COMMAND, handle_from_currency)],
            TO_CURRENCY: [MessageHandler(filters.TEXT & ~filters.COMMAND, handle_to_currency)],
        },
        fallbacks=[CommandHandler('cancel', cancel_command)]
    )

    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(conv_handler)
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.add_error_handler(error)

    print('🔄 Polling for updates...')
    app.run_polling()
