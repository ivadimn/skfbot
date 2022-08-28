from telebot import TeleBot
from telebot.types import BotCommand
from config_data.config import COMMANDS
from config_data.resources import Msgs
from loader import curr_list
from extensions.errors import DataError, NotCurrencyError


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
    if curr_list.get(lst[0]) is None:
        raise NotCurrencyError(Msgs.ERROR_CURRENCY_NOT_FOUND.format(lst[0]))
    if curr_list.get(lst[1]) is None:
        raise NotCurrencyError(Msgs.ERROR_CURRENCY_NOT_FOUND.format(lst[1]))
    if lst[0] == lst[1] and len(curr_list.get(lst[0])) == 1:
        raise DataError(Msgs.ERROR_SAME_CURRENCY)
    return lst[0].lower(), lst[1].lower(), int(lst[2])


def get_curr_list() -> list:
    lst = []
    for key, vals in curr_list.items():
        if len(vals) == 1:
            lst.append("{0} - {1}".format(key, vals[0][0]))
        else:
            lst.append("{0}:".format(key))
            for val in vals:
                lst.append("    {0} - {1}".format(val[0], val[1]))
    return lst
