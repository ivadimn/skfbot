from telebot.custom_filters import StateFilter
from loader import bot
import handlers
from utils.functions import set_commands
from api.currency import Currency
from utils.functions import parse_data
from errors.errors import DataError, NotCurrencyError, AmbiguousCurrencyError


def w_bot():
    while True:
        data = input("Введите валюты: ")
        data = data.strip()
        if data == "end":
            break
        try:
            base, quote, amount = parse_data(data)
            vfrom = get_code(base)
            print(vfrom)
            vto = get_code(quote)
            print(vfrom, vto, amount)
            price = Currency.get_price("EUR", "RUB", 100)
            print("Для покупки {0} {1} потребуется {2} {3}".format(amount, base, price, quote))
        except DataError as e:
            print(e.msg)
            print("Повторите попытку..")
            continue
        except NotCurrencyError as e:
            print(e.msg)
            print("Уточните валюту!!")
            continue
        except AmbiguousCurrencyError as e:
            print("Много валют!")
            print(e.msg)
            n = input("Введите номер нужной валюты: ")
            print(n)
            break


if __name__ == "__main__":
    bot.add_custom_filter(StateFilter(bot))
    set_commands(bot)
    bot.infinity_polling()
    print("Bot closed")



