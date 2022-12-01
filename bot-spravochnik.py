# Создать Телефонный справочник с возможностями работы с информацией, и экспорта информации в телеграмм бот


import telebot
from random import *
import json
import requests
import act


API_TOKEN = '5952228267:AAE337fMtvBuxDvnXHnGLYRBpzWLwLjzdl8'

bot = telebot.TeleBot(API_TOKEN)

def save():
    with open("book.json", "w", encoding="utf-8") as fh:
        fh.write(json.dumps(book, ensure_ascii=False))
        print("Контакты сохранена в файле films.json")


def load():
    global book
    with open("book.json", "r", encoding="utf-8") as fh:
        book = json.load(fh)
    print("Контакты успешно загружены")


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Готов к работе!")
    bot.send_message(message.chat.id, "Будем работать со справочником?)")
    try:
        load()
        bot.send_message(message.chat.id, "Контакты успешно загружены")
    except:
        bot.send_message(message.chat.id, "Контакты успешно загружены по умолчанию")


@bot.message_handler(commands=['show'])
def show_reply(message):
    # for key, value in book.items():
    #     bot.send_message(message.chat.id, str(key) + str(value))
    bot.send_message(message.chat.id, act.option())

# @bot.message_handler(commands=['new'])
# @bot.message_handler(content_types='text')
# def new(message):
#     name = bot.send_message(message.chat.id, "Введите имя")
#     bot.register_next_step_handler(message,get_date)
#     # bot.send_message(message.chat.id, "Имя добавлено")
# def get_date(message):
#     bot.send_message(message.chat.id, "Введите дату рождения")
#     bot.register_next_step_handler(message, get_phone)
#     # bot.send_message(message.chat.id, "Дата добавлена")
# def get_phone(message):
#     bot.send_message(message.chat.id, "Введите телефон")
#     bot.register_next_step_handler(message, get_mail)
#     # bot.send_message(message.chat.id, "телефон добавлен")
# def get_mail(message):
#     bot.send_message(message.chat.id, "Введите эл. почту'")
#     # bot.send_message(message.chat.id, "почта добавлена")
#
#     value = [get_date(message), get_phone(message),get_mail(message)]
#     book[new(message)] = dict(value)
#
#     print(book)
#
# @bot.message_handler(commands=['delete'])
# def delete_message(message):
#
#
#
# @bot.message_handler(commands=['find'])
# def find_message(message):
#
#
#
# @bot.message_handler(commands=['add'])
# def add_message(message):
#
#


bot.polling()
