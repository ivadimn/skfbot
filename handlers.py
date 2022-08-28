from telebot.types import Message
from loader import bot, cache
from config_data.resources import commands, Msgs
from extensions.currency import Currency
from extensions.functions import parse_data, get_curr_list
from extensions.errors import DataError, NotCurrencyError, AmbiguousCurrencyError
from extensions.currency_state import CurrencyState
from extensions.user_data import UserData


@bot.message_handler(commands=["start", "reset"])
def start(message: Message) -> None:
    welcome_msg = Msgs.WELCOME
    bot.set_state(message.chat.id, CurrencyState.normal)
    bot.reply_to(message, welcome_msg.format(message.from_user.first_name, message.from_user.last_name))


@bot.message_handler(commands=["help"])
def helps(message: Message) -> None:
    help_msg = Msgs.COMMAND_LIST.\
        format("\n".join(["{0} - {1}".format(key, value) for key, value in commands.items()]))
    bot.send_message(message.chat.id, help_msg)

@bot.message_handler(commands=["values"])
def values(message: Message) -> None:
    msg = Msgs.CURRENCY_LIST.format("\n".join(get_curr_list()))
    bot.send_message(message.chat.id, msg)


@bot.message_handler(state=CurrencyState.normal)
def convert(message: Message) -> None:
    data = message.text
    user_data = cache.get(message.chat.id)
    try:
        base, quote, amount = parse_data(data)
        if not user_data:
            user_data = UserData(message.chat.id, base, quote, amount)
            cache[message.chat.id] = user_data
        user_data.get_codes()
        send_result(user_data)
    except DataError as e:
        bot.reply_to(message, e.msg)
    except NotCurrencyError as e:
        bot.reply_to(message, e.msg)
    except AmbiguousCurrencyError as e:
        bot.set_state(message.chat.id, CurrencyState.select_index)
        bot.send_message(message.chat.id, e.msg)


@bot.message_handler(state=CurrencyState.select_index)
def select_index(message: Message) -> None:
    user_data: UserData = cache.get(message.chat.id)
    try:
        if user_data.base_code == "":
            user_data.base_code, user_data.base = select_code(user_data, message.text)
            user_data.get_codes()
        else:
            user_data.quote_code, user_data.quote = select_code(user_data, message.text)
        send_result(user_data)
    except ValueError:
        msg = "{0}\n{1}".format(Msgs.ERROR_INDEX.format(message.text), Msgs.REPEAT)
        bot.send_message(user_data.user_id, msg)
    except AmbiguousCurrencyError as e:
        bot.send_message(message.chat.id, e.msg)


def select_code(user_data: UserData, data: str) -> tuple:
    index = int(data) - 1
    currs = user_data.curr_list
    if 0 <= index < len(currs):
        return currs[index][0], currs[index][1]
    else:
        raise ValueError()


def send_result(user_data: UserData) -> None:
    price = Currency.try_from_cache(user_data.base_code, user_data.quote_code, user_data.amount)
    if price == 0:
        price = Currency.get_price(user_data.base_code, user_data.quote_code, user_data.amount)
    cache.pop(user_data.user_id)
    bot.set_state(user_data.user_id, CurrencyState.normal)
    bot.send_message(user_data.user_id,
                     Msgs.RESULT.format(user_data.amount,
                                        user_data.base, price, user_data.quote))
