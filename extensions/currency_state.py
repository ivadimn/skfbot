from telebot.handler_backends import State, StatesGroup


class CurrencyState(StatesGroup):
    normal = State()
    select_base = State()
    select_quote = State()
    select_index = State()
