from telegram import Update
from telegram.ext import ContextTypes
from bot.utils.logger import logger
from bot.services.exchange_service import ExchangeService

def handle_response(text: str) -> str:
    processed_text = text.lower().strip()

    if processed_text in ['hello', 'hi', 'hey', 'hola', 'greetings']:
        return "Hey there!  Use /convert to start currency conversion! 💱"

    elif processed_text in ['how are you', 'how are you doing', "how's it going"]:
        return "I'm great! Ready to help with currency conversions. Use /convert to start! 🌍"

    elif processed_text in ['thanks', 'thank you', 'ty', 'thankyou']:
        return "You're welcome! 😊"

    elif processed_text in ['bye', 'goodbye', 'see you']:
        return "Goodbye! 👋 Use /convert anytime for currency conversions!"

    elif processed_text in ['/help', 'help', 'commands', 'what can you do']:
        return """💱 *Available Commands:*
/convert - Start interactive currency conversion
/help - Show this help message

💡 *Quick Conversion:*
Type '100 USD to EUR'
"""

    elif ' to ' in processed_text:
        try:
            parts = text.split(' to ')
            if len(parts) == 2:
                amount_part = parts[0].strip()
                to_currency = parts[1].strip().upper()

                amount_parts = amount_part.split(' ')
                if len(amount_parts) == 2:
                    amount = float(amount_parts[0])
                    from_currency = amount_parts[1].upper()

                    exchange_service = ExchangeService()

                    from_with_emoji = from_currency
                    to_with_emoji = to_currency

                    rate, error = exchange_service.get_exchange_rate(from_with_emoji, to_with_emoji)

                    if not error and rate:
                        converted = amount * rate
                        return f"""💱 *Quick Conversion Result:*

💰 *{amount} {from_currency} = {converted:.2f} {to_currency}*

📊 Exchange Rate: 1 {from_currency} = {rate:.4f} {to_currency}"""
                    else:
                        return f"❌ Could not convert {from_currency} to {to_currency}."

        except ValueError:
            return "❌ Invalid format! Please use: '100 USD to EUR'"
        except Exception as e:
            logger.error(f"Quick conversion error: {e}")
            return "❌ Error processing your request."

    elif 'rate' in processed_text or 'exchange' in processed_text:
        return "💱 Use /convert or type '100 USD to EUR'"

    else:
        return """💱 *I'm Ratez Bot - Your Currency Exchange Assistant!*

Use /convert for step-by-step conversion or '100 USD to EUR'
"""

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text: str = update.message.text
    response: str = handle_response(text)
    await update.message.reply_text(response, parse_mode='Markdown')
