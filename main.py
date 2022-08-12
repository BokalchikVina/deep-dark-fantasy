import telebot

from data import BotDB

con = BotDB("database.db")
bot = telebot.TeleBot('5226303098:AAG-Cje17TQmI9xdxV3rfia0SmJJVjzLAPg')

@bot.message_handlers(commands = ["start"])

def start():
