from telebot import TeleBot
from telebot.types import BotCommand
import json
from config_data.config import COMMANDS


def set_commands(bot: TeleBot):
    bot.set_my_commands(
        [BotCommand(*command) for command in COMMANDS]
    )


def load_currency_list() -> dict:
    with open("curr_list.json", "r") as f:
        currs = json.load(f)
    return currs
