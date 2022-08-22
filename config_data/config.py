import os
from dotenv import find_dotenv, load_dotenv

if not find_dotenv():
    exit("Environment variables not loaded, file .env not found")
else:
    load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
COMMANDS = (
    ('start', "Start bot"),
    ('values', "Show full list currency"),
    ('help', "Show help")
)

