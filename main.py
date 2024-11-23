# import telebot
# import buttons
import requests

# bot = telebot.TeleBot('7684540340:AAGl6p10m49UZkSI8s-9w4KC4B850ip1BLA')
# url = 'https://cbu.uz/ru/arkhiv-kursov-valyut/json/'
# USD = requests.get(url).json()[0]['Rate']
# EUR = requests.get(url).json()[1]['Rate']
# RUB = requests.get(url).json()[2]['Rate']



#Обработчик команды /start
# @bot.message_handler(commands=['start'])
# def start(message):
#     user_id = message.from_user.id
#     bot.send_message(user_id, 'Здравствуйте!',)
#
#
# @bot.message_handler(commands=['help'])
# def text(message):
#     user_id = message.from_user.id
#     bot.send_message(user_id, 'Этот бот назначен для курсы валют , Вас интересует данная информация?')


# @bot.message_handler(content_types=['text'])
# def text(message):
#     user_id = message.from_user.id
#     if message.text.title() == '$':
#         bot.send_message(user_id, 'Введите сумму в UZS', reply_markup=telebot.types.ReplyKeyboardMarkup())
#         bot.register_next_step_handler(message, usd)
#     elif message.text.title() == '€':
#         bot.send_message(user_id, 'Введите сумму в UZS', reply_markup=telebot.types.ReplyKeyboardMarkup())
#         bot.register_next_step_handler(message, eur)
#     elif message.text.title() == '₽':
#         bot.send_message(user_id, 'Введите сумму в UZS')
#         bot.register_next_step_handler(message, rub)
#     else:
#         bot.send_message(user_id, 'Что-то не пошло не так, попробуйте нажимать /start')
#
#
# def usd(message):
#     user_id = message.from_user.id
#     if message.text.isnumeric():
#         bot.send_message(user_id, f'{int(message.text)/float(USD)}')
#     else:
#         bot.send_message(user_id, 'Пишите только цифры!')
#         bot.register_next_step_handler(message, usd)
#
# def eur(message):
#     user_id = message.from_user.id
#     if message.text.isnumeric():
#         bot.send_message(user_id, f'{int(message.text)/float(EUR)}')
#     else:
#         bot.send_message(user_id, 'Пишите только цифры!')
#         bot.register_next_step_handler(message, eur)
#
# def rub(message):
#     user_id = message.from_user.id
#     if message.text.title():
#         bot.send_message(user_id, f'{int(message.text)/float(RUB)}')
#     else:
#         bot.send_message(user_id, 'Пишите только цифры!')
#         bot.register_next_step_handler(message, rub)



# bot.polling() #Запуск бота