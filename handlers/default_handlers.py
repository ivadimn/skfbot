from telebot.types import Message
from loader import bot
from config_data.resources import commands, res


@bot.message_handler(commands=["start", "reset"])
def start(message: Message) -> None:
    locale = "ru" if message.from_user.language_code.lower() == "ru" else "en"
    welcome_msg = res[locale]["msgs"]["WELCOME"]
    bot.reply_to(message, welcome_msg.format(message.from_user.first_name, message.from_user.last_name))


@bot.message_handler(commands=["help"])
def help(message: Message) -> None:
    locale = "ru" if message.from_user.language_code.lower() == "ru" else "en"
    help_msg = res[locale]["msgs"]["COMMANDS_LIST"].format("\n".join(commands))
    bot.send_message(message.chat.id, help_msg)