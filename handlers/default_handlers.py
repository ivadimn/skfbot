from telebot.types import Message
from loader import bot, curr_list
from config_data.resources import commands, Msgs
from api.currency import Currency
from utils.functions import parse_data, get_code
from errors.errors import DataError, NotCurrencyError, AmbiguousCurrencyError
from states.currency_state import CurrencyState


@bot.message_handler(commands=["start", "reset"])
def start(message: Message) -> None:
    welcome_msg = Msgs.WELCOME
    bot.reply_to(message, welcome_msg.format(message.from_user.first_name, message.from_user.last_name))


@bot.message_handler(commands=["help"])
def helps(message: Message) -> None:
    help_msg = Msgs.COMMAND_LIST.\
        format("\n".join(["{0} - {1}".format(key, value) for key, value in commands.items()]))
    bot.send_message(message.chat.id, help_msg)


@bot.message_handler(content_types=["text"])
def convert(message: Message) -> None:
    data = message.text
    try:
        base, quote, amount = parse_data(data)
        vfrom = get_code(base)
        vto = get_code(quote)
        price = Currency.get_price(vfrom, vto, 100)
        bot.reply_to(message, Msgs.RESULT.format(amount, base, price, quote))
    except DataError as e:
        bot.reply_to(message, e.msg)
    except NotCurrencyError as e:
        bot.reply_to(message, e.msg)

@bot.message_handler(states=CurrencyState.many_currencies)
def index(message: Message) -> None:
    pass



