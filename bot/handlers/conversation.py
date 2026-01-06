from telegram import  Update
from telegram.ext import ContextTypes, ConversationHandler
from bot.services.exchange_service import ExchangeService
from bot.utils.keyboards import get_currency_keyboard
from telegram import ReplyKeyboardRemove


AMOUNT, FROM_CURRENCY, TO_CURRENCY = range(3)

async def convert_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "💱 Enter amount:",
        parse_mode='Markdown',
        reply_markup=ReplyKeyboardRemove()
    )
    return AMOUNT

async def handle_amount(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        amount = float(update.message.text)
        if amount <= 0:
            await update.message.reply_text("❌ Enter positive number:")
            return AMOUNT

        context.user_data['amount'] = amount
        await update.message.reply_text(
            f"💰 Amount: {amount}\nSelect source currency:",
            parse_mode='Markdown',
            reply_markup=get_currency_keyboard()
        )
        return FROM_CURRENCY

    except ValueError:
        await update.message.reply_text("❌ Invalid number:")
        return AMOUNT

async def handle_from_currency(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.text == "🔙 Cancel":
        await update.message.reply_text("❌ Cancelled.", reply_markup=ReplyKeyboardRemove())
        return ConversationHandler.END

    context.user_data['from_currency'] = update.message.text
    await update.message.reply_text(
        f"Now select target currency:",
        parse_mode='Markdown',
        reply_markup=get_currency_keyboard()
    )
    return TO_CURRENCY

async def handle_to_currency(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.text == "🔙 Cancel":
        await update.message.reply_text("❌ Cancelled.", reply_markup=ReplyKeyboardRemove())
        return ConversationHandler.END

    exchange_service = ExchangeService()
    await update.message.reply_chat_action(action="typing")

    rate, error = exchange_service.get_exchange_rate(
        context.user_data['from_currency'],
        update.message.text
    )

    if error:
        await update.message.reply_text("❌ Error. Try again.", reply_markup=ReplyKeyboardRemove())
    else:
        amount = context.user_data['amount']
        converted_amount = amount * rate
        from_code = context.user_data['from_currency'].split(' ')[0]
        to_code = update.message.text.split(' ')[0]

        result_text = f"""
💱 *Conversion Complete!* ✅
💰 *{amount} {from_code} = {converted_amount:.2f} {to_code}*
📊 *Rate:* {rate:.4f}
        """
        await update.message.reply_text(result_text, parse_mode='Markdown', reply_markup=ReplyKeyboardRemove())

    return ConversationHandler.END

async def cancel_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("❌ Cancelled.", reply_markup=ReplyKeyboardRemove())
    return ConversationHandler.END