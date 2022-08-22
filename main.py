from loader import bot
import handlers
from utils.functions import set_commands


if __name__ == "__main__":
    set_commands(bot)
    bot.infinity_polling()
    print("Bot closed")