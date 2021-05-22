try:
	import os
	import telebot
	import info
        from random import randint 
except:
	os.system('pip3 install pyTelegramBotAPI')

token = info.token
bot = telebot.TeleBot(token) # Conectando nosso programa com o bot


@bot.message_handler(commands=['start', 'help'])
def msg(message):
	bot.send_message(message.chat.id, f'Ola, {message.from_user.first_name}!\n Sou um bot totalmente desenvolvido em python e criado pelo <seu nome>.')



@bot.message_handler(commands=['game'])
def jg(message):
	m = (message.text).replace('/game','').replace(' ', '')
	sorteado = str(randint(0, 10))
	try:
		if m == sorteado:
			result = f'''
>>> Partida inicializada <<<

Bot: {sorteado}
{message.from_user.first_name}:  {m}

Vencedor: {message.from_user.first_name}'''
		else:
			result = f'''
>>> Partida inicializada <<<

Bot: {sorteado}
{message.from_user.first_name}:  {m}

Vencedor: Bot hehehehe!''' 
		bot.send_message(message.chat.id, result)
	except:
		print('Alguem invocou um erro mestre ;-;')




bot.polling(none_stop=True)
bot.polling(interval=3)
