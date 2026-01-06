import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
BOT_USERNAME = "@Ratez_Bot"  # can hardcode username
