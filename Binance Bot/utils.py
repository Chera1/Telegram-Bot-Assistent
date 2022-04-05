import shelve

from config import shelve_name, database_name
from random import shuffle
from telebot import types



def get_rows_count():
    with shelve.open(shelve_name) as storage:
        rowsnum = storage['rows_count']
    return rowsnum


def set_user_game(chat_id, estimated_answer):
    with shelve.open(shelve_name) as storage:
        storage[str(chat_id)] = estimated_answer


def finish_user_game(chat_id):
    with shelve.open(shelve_name) as storage:
        del storage[str(chat_id)]


def get_answer_for_user(chat_id, text):
    with shelve.open(shelve_name) as storage:
        try:
            answer = text in storage[str(chat_id)]
            # answer = storage[str(chat_id)]
            return text
        except KeyError:
            return None


def generate_markup(menu):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    for item in menu:
        markup.add(item)
    return markup
