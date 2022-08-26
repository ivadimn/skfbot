from telebot.types import Message
from loader import bot, redis
from config_data.resources import commands, Msgs
from api.currency import Currency
from utils.functions import parse_data
from errors.errors import DataError, NotCurrencyError, AmbiguousCurrencyError
from states.currency_state import CurrencyState
from extensions import UserData


@bot.message_handler(commands=["start", "reset"])
def start(message: Message) -> None:
    welcome_msg = Msgs.WELCOME
    print(message.chat.id)
    print(message.from_user.id)
    bot.set_state(message.chat.id, CurrencyState.normal)
    bot.reply_to(message, welcome_msg.format(message.from_user.first_name, message.from_user.last_name))


@bot.message_handler(commands=["help"])
def helps(message: Message) -> None:
    help_msg = Msgs.COMMAND_LIST.\
        format("\n".join(["{0} - {1}".format(key, value) for key, value in commands.items()]))
    bot.send_message(message.chat.id, help_msg)


@bot.message_handler(state=CurrencyState.normal)
def convert(message: Message) -> None:
    data = message.text
    user_data = redis.get(message.chat.id)
    try:
        base, quote, amount = parse_data(data)
        if not user_data:
            user_data = UserData(message.chat.id, base, quote, amount)
            redis[message.chat.id] = user_data
        user_data.get_codes()
        send_result(user_data)
    except DataError as e:
        bot.reply_to(message, e.msg)
    except NotCurrencyError as e:
        bot.reply_to(message, e.msg)
    except AmbiguousCurrencyError as e:
        if user_data.base_code == "":
            bot.set_state(message.chat.id, CurrencyState.select_base)
        else:
            bot.set_state(message.chat.id, CurrencyState.select_quote)
        bot.send_message(message.chat.id, e.msg)


@bot.message_handler(state=CurrencyState.select_base)
def index_base(message: Message) -> None:
    user_data: UserData = redis.get(message.chat.id)
    try:
        user_data.base_code = select_code(user_data, message.text)
        user_data.get_codes()
        send_result(user_data)
    except ValueError:
        msg = "{0}\n{1}".format(Msgs.ERROR_INDEX.format(message.text), Msgs.REPEAT)
        bot.send_message(user_data.user_id, msg)
    except AmbiguousCurrencyError as e:
        bot.set_state(message.chat.id, CurrencyState.select_quote)
        bot.send_message(message.chat.id, e.msg)


@bot.message_handler(state=CurrencyState.select_quote)
def index_quote(message: Message) -> None:
    user_data: UserData = redis.get(message.chat.id)
    try:
        user_data.quote_code = select_code(user_data, message.text)
        send_result(user_data)
    except ValueError:
        msg = "{0}\n{1}".format(Msgs.ERROR_INDEX.format(message.text), Msgs.REPEAT)
        bot.send_message(user_data.user_id, msg)


def select_code(user_data: UserData, data: str) -> str:
    index = int(data) - 1
    currs = user_data.curr_list
    if 0 <= index < len(currs):
        return currs[index][0]
    else:
        raise ValueError()


def send_result(user_data: UserData) -> None:
    price = Currency.get_price(user_data.base_code, user_data.quote_code, user_data.amount)
    redis.pop(user_data.user_id)
    print(price)
    bot.set_state(user_data.user_id, CurrencyState.normal)
    bot.send_message(user_data.user_id,
                     Msgs.RESULT.format(user_data.amount,
                                        user_data.base, price, user_data.quote))
