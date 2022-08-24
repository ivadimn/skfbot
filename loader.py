from telebot import TeleBot
from config_data import config
from utils.functions import load_currency_list

bot = TeleBot(config.BOT_TOKEN)
curr_list = load_currency_list()

