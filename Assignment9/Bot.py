
import telebot

bot = telebot.TeleBot("5845886395:AAGUb5qTTb4eftdwRyT4XyPBYlKWBg93XUY", parse_mode=None)

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Welcome")

@bot.message_handler(commands=['help'])
def send_welcome(message):
	bot.reply_to(message, "")

# @bot.message_handler(func=lambda m: True)
# def echo_all(message):
# 	# bot.reply_to(message, " ")
# 	bot.send_message(massage.chat_id, " ")

bot.infinity_polling()
