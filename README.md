#  Ratez Bot — Currency Converter Telegram Bot

Ratez Bot is a Telegram bot written in Python that allows users to convert currencies
using real-time exchange rates via an external API.

The bot supports:
- Step-by-step conversion using `/convert`
- Quick conversions like `100 USD to EUR`
- Popular currencies via a custom keyboard

---

##  Project Structure

The project follows a modular structure with clear separation of responsibilities:

``` 
bot/
├── config/ # Configuration (token, constants)
├── handlers/ # Command, message, and conversation handlers
├── services/ # External services (exchange rate API)
├── utils/ # Utilities (keyboards, logging)
└── main.py # Application entry point
``` 

---

##  How to Run

1. Create and activate a virtual environment
2. Install dependencies:
```bash
   pip install -r requirements.txt
```
3. Set the bot tokenin a .env file
``` python
BOT_TOKEN=your_token_here
``` 
4. Run the bot
```
python bot/main.py
``` 

## CI & Code Quality
The project uses GitHub Actions with a flake8 linter to automatically check
code quality on every push and pull request.

## Technologies Used
Python 3.11

python-telegram-bot

requests

GitHub Actions (CI)

flake8 (linting)

## Notes
The .venv directory and environment variables are excluded from version control
The bot token is never stored in the repository

- [README на Русский](README.ru.md)

