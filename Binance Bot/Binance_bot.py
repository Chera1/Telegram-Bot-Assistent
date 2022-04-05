import config
import telebot
from SQLighter import SQLighter
import time
import os
import random
from telebot import types
import utils
from test_binance import main as binance

bot = telebot.TeleBot(config.token_telegram)
menu = ['Спотовый кошелек Binance',
        'Тинькофф Инвестиции']


@bot.message_handler(commands=['main'])
def main(message):
    utils.set_user_game(message.chat.id, menu)
    markup = utils.generate_markup(menu)
    bot.send_message(message.chat.id, 'Выберите пункт меню', reply_markup=markup)


@bot.message_handler(commands=['binance'])
def binance_main(message):
    myBalance = binance(config.api_key_binance, config.api_secret_binance)
    bot.send_message(message.chat.id, myBalance)


@bot.message_handler(func=lambda message: True, content_types=['text'])
def check_answer(message):
    answer = utils.get_answer_for_user(message.chat.id, message.text)

    if not answer:
        bot.send_message(message.chat.id, 'Добро пожаловать /main')
    else:
        if answer == menu[0]:
            binance_main(message)
        else:
            main(message)
        # utils.finish_user_game(message.chat.id)


# @bot.message_handler(commands=['test'])
# def find_file_ids(message):
#     for file in os.listdir('music/'):
#         if file.split('.')[-1] == 'ogg':
#             f = open('music/' + file, 'rb')
#             res = bot.send_voice(message.chat.id, f, None)
#             bot.send_message(message.chat.id, res.voice.file_id, reply_to_message_id=res.message_id)
#             print(res)
#         time.sleep(3)


if __name__ == '__main__':
    # utils.count_rows()
    random.seed()
    bot.infinity_polling()
