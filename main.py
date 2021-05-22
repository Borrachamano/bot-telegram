try:
	import os
	import telebot
	import info
	from pytube import YouTube
except:
	os.system('pip3 install pyTelegramBotAPI')

token = info.token
bot = telebot.TeleBot(token) # Conectando nosso programa com o bot


@bot.message_handler(commands=['start', 'help'])
def msg(message):
	bot.send_message(message.chat.id, f'Ola, {message.from_user.first_name}!\n Sou um bot totalmente desenvolvido em python e criado pelo <seu nome>.')


bot.polling(none_stop=True)
bot.polling(interval=3)
