from telebot import types



def num_button():

    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)

    num = types.KeyboardButton('Отправить номер📞', request_contact=True)

    kb.add(num)

    return kb

