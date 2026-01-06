from telegram import ReplyKeyboardMarkup

POPULAR_CURRENCIES = [
    ["USD 🇺🇸", "EUR 🇪🇺", "GBP 🇬🇧"],
    ["INR 🇮🇳", "JPY 🇯🇵", "CAD 🇨🇦"],
    ["AUD 🇦🇺", "CHF 🇨🇭", "CNY 🇨🇳"],
    ["RUB 🇷🇺", "🔙 Cancel"]
]

def get_currency_keyboard():
    return ReplyKeyboardMarkup(POPULAR_CURRENCIES, resize_keyboard=True, one_time_keyboard=False)
