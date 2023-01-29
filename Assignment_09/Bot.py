
import random
import math
import telebot
from telebot import types
from khayyam import JalaliDatetime
import gtts
import qrcode

bot = telebot.TeleBot("5845886395:AAGUb5qTTb4eftdwRyT4XyPBYlKWBg93XUY", parse_mode=None)

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.send_message(message.chat.id, message.from_user.first_name + " dear! Hi!")

@bot.message_handler(commands=['game'])
def send_game(message):
	markup = types.ReplyKeyboardMarkup(row_width=1)
	key = types.KeyboardButton('new game')
	markup.add(key)	
	computer_choice = random.randint(0,100)
	bot.send_message(message.chat.id, "Enter your guess (0-100): " ,reply_markup=markup)
	@bot.message_handler(func=lambda m: True)
	def echo_all(message):
		if int(message.text) < computer_choice:
			bot.send_message(message.chat.id, "go up 🔼" , reply_markup=markup)
		elif int(message.text) > computer_choice:
			bot.send_message(message.chat.id, " go down 🔽" , reply_markup=markup)
		elif int(message.text)==computer_choice:
			bot.send_message(message.chat.id, "you win! 🏆" , reply_markup=markup)

@bot.message_handler(commands=['age'])
def send_age(message):
	bot.send_message(message.chat.id, " Enter your birthday (example: 1401/1/1): ")		
	@bot.message_handler(func=lambda m: True)
	def echo_all(message):
		list_age = message.text.split("/")
		sum_of_days = int(JalaliDatetime.now()) - int(JalaliDatetime(list_age[0], list_age[1], list_age[2]))
		year_age = sum_of_days.days // 365
		month_age = (sum_of_days.days - (year_age * 365)) // 30
		day_age = k % 30	
		bot.send_message(message.chat.id, str(year_age)+ " year, "+ str(month_age)+ " month, "+ str(day_age)+ " day")

@bot.message_handler(commands=['voice'])
def send_voice(message):
	state="voice"
	bot.send_message(message.chat.id, "Enter your english text: ")
	@bot.message_handler(func=lambda m: True)
	def echo_all(message):
		voi = gtts.gTTS(user_text , lang = "ar", slow = False)
		voi.save("voice.mp3")
		voice = open("voice.mp3", "rb")
		bot.send_voice(message.chat.id, voice)

@bot.message_handler(commands=['max'])
def send_max(message):
	bot.send_message(message.chat.id, " Enter your numbers (example: 32 125 8 ...): ")		
	@bot.message_handler(func=lambda m: True)
	def echo_all(message):
		list_num = message.text.split(" ")
		max_num = max(list_num)
		bot.send_message(message.chat.id, max_num)

@bot.message_handler(commands=['argmax'])
def send_max(message):
	bot.send_message(message.chat.id, " Enter your numbers (example: 32 125 8 ...): ")		
	@bot.message_handler(func=lambda m: True)
	def echo_all(message):
		list_num = message.text.split(" ")
		max_num = max(int(list_num))
		for i in range(len(list_num)):
			if list_num[i] == max_num:
				bot.send_message(message.chat.id, i)

@bot.message_handler(commands=['qrcode'])
def send_qrcode(message):
	bot.send_message(message.chat.id, "Enter your text: ")
	@bot.message_handler(func=lambda m: True)
	def echo_all(message):
		img = qrcode.make(message.text)
		img.save("qrcode.png")
		photo = open("qrcode.png", "rb")
		bot.send_photo(message.chat.id, photo)

@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.send_message(message.chat.id,"""
	/game: Guessing the number game\n
	/age: Receive date of birth and calculating age\n 
	/voice: Convert text to sound\n
	/max: Print the largest number of the list\n
	/argmax: Print the index of the largest number from the list\n
	/qrcode: Convert a test to a qrcode
	""")

bot.infinity_polling()
