import telebot

TOKEN = "5440983165:AAFd3q62UQmJTlZpT3az87cvdDo0_37I58o"

bot = telebot.TeleBot(TOKEN)

# Обрабатываются все сообщения, содержащие команды '/start' or '/help'.
@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    print(message.text)
    bot.reply_to(message, f"Welcome, {message.chat.username}")
@bot.message_handler(content_types=['document', 'audio', 'photo'])
def handle_docs_photo(message):
    bot.reply_to(message, 'Nice meme XDD')


# @bot.message_handler(content_types=['voice','document', 'audio', 'text'])
# def repeat(message: telebot.types.Message):
#     print(message.text)
#     bot.send_message(message.chat.id, 'Я тебя слышу')
#
# @bot.message_handler(commands=['start', 'help'])
# def send_welcome(message: telebot.types.Message):
#     bot.reply_to(message, "Howdy, how are you doing?")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.send_message(message.chat.id, message.text)

bot.polling(none_stop=True)