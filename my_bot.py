
import telebot
from my_token import my_first_token
token = my_first_token
bot=telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start_message(message):
  bot.send_message(message.chat.id,"Привет ✌️ ")

@bot.message_handler(commands=['как дела?'])
def watsupp(message):
  bot.send_message(message.chat.id,"Хорошо ")
bot.infinity_polling()