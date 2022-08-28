from telebot.custom_filters import StateFilter
from loader import bot
from extensions.functions import set_commands
import handlers


if __name__ == "__main__":
    bot.add_custom_filter(StateFilter(bot))
    set_commands(bot)
    bot.infinity_polling()
    print("Bot closed")



