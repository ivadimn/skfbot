from telebot.handler_backends import State, StatesGroup


class CurrencyState(StatesGroup):
    normal = State()
    many_currencies = State()
