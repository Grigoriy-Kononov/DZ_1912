import telebot
import random
from config import TOKEN
from coding import *

bot = telebot.TeleBot(TOKEN)


"""Команда СТАРТ"""

@bot.message_handler(commands=['start'])
def welcome(message):
              markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)

              item1 = telebot.types.KeyboardButton('Рандомное число')
              item2 = telebot.types.KeyboardButton('Кинуть кость')
              item3 = telebot.types.KeyboardButton('Кодировать текст')
              item4 = telebot.types.KeyboardButton('Декодировать текст')

              markup.add(item1, item2, item3, item4)

              bot.send_message(message.chat.id, 'Добро пожаловать! Выберите нужный вам пункт меню: ', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def send_text(message):
              if message.text == 'Привет':
                            bot.send_message(message.chat.id, 'Привет, как дела?')
              elif message.text == 'Рандомное число':
                            bot.send_message(message.chat.id, str(random.randint(1, 10)))
              elif message.text == 'Кинуть кость':
                            bot.send_message(message.chat.id, f'Вам выпало {(str(random.randint(1, 6)))}')
              elif message.text == 'Кодировать текст':
                            bot.send_message(message.chat.id, 'Введите текст')
                            if message.text == '':
                                          bot.send_message(message.chat.id, rle_code(message.text))
              elif message.text == 'Декодировать текст':
                            bot.send_message(message.chat.id, 'Введите текст')
                            if message.text == '':
                                          bot.send_message(message.chat.id, rle_decode(message.text))
              else:
                            bot.send_message(message.chat.id, 'Данный функционал находится в разработке.')



bot.polling(none_stop=True)