import os
from dotenv import find_dotenv, load_dotenv

if not find_dotenv():
    exit("Environment variables not loaded, file .env not found")
else:
    load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
API_KEY = os.getenv("API_KEY")
PRICE_URL = os.getenv("PRICE_URL")
LIST_URL = os.getenv("LIST_URL")
COMMANDS = (
    ('start', "Запустить бот"),
    ('values', "Показать полный список валют"),
    ('help', "Помощь")
)

