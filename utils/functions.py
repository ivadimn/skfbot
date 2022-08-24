from telebot import TeleBot
from telebot.types import BotCommand
import json
from config_data.config import COMMANDS
from loader import curr_list


def set_commands(bot: TeleBot):
    bot.set_my_commands(
        [BotCommand(*command) for command in COMMANDS]
    )


def load_currency_list() -> dict:
    with open("curr_list.json", "r") as f:
        currs = json.load(f)
    return currs


def parse_data(data: str) -> tuple:
    lst = data.split(" ")
    if len(lst) != 3:
        print("Error data!!")
        return ()
    if not lst[2].isdigit():
        print("Error data!!")
        return ()
    return lst[0].lower(), lst[1].lower(), lst[2]


def get_code(name: str) -> str:
    curr = curr_list.get(name)
    if not curr:
        return ""
    if len(curr) > 1:
        return "Error"
    return curr.keys[0]
