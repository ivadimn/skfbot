from telebot import TeleBot
from telebot.types import BotCommand
from config_data.config import COMMANDS


def set_commands(bot: TeleBot):
    bot.set_my_commands(
        [BotCommand(*command) for command in COMMANDS]
    )