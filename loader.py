import json
from telebot import TeleBot
from telebot.storage import StateMemoryStorage
from config_data import config


def load_currency_list() -> dict:
    with open("curr_list.json", "r") as f:
        currs = json.load(f)
    return currs


storage = StateMemoryStorage()
bot = TeleBot(config.BOT_TOKEN, state_storage=storage)
curr_list = load_currency_list()
redis = dict()

