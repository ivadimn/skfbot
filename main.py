from loader import bot
import handlers
from utils.functions import set_commands
from api.currency import Currency

'//*[@id="equities_table"]/tbody'

if __name__ == "__main__":
    #set_commands(bot)
    #bot.infinity_polling()
    #print("Bot closed")
    curr = Currency.get_list()
    index = 1
    for name, descr in curr.items():
        print(index, name, descr)
        index += 1
