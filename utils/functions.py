from telebot import TeleBot
from telebot.types import BotCommand
from config_data.config import COMMANDS
from config_data.resources import Msgs
from loader import curr_list
from errors.errors import DataError, NotCurrencyError, AmbiguousCurrencyError


def set_commands(bot: TeleBot):
    bot.set_my_commands(
        [BotCommand(*command) for command in COMMANDS]
    )


def parse_data(data: str) -> tuple:
    lst = data.split(" ")
    if len(lst) != 3:
        raise DataError(Msgs.ERROR_DATA)
    if not lst[2].isdigit():
        raise DataError(Msgs.ERROR_AMOUNT)
    return lst[0].lower(), lst[1].lower(), int(lst[2])



