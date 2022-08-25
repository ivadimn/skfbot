import json
from telebot import TeleBot
from config_data import config


def load_currency_list() -> dict:
    with open("curr_list.json", "r") as f:
        currs = json.load(f)
    return currs


bot = TeleBot(config.BOT_TOKEN)
curr_list = load_currency_list()

