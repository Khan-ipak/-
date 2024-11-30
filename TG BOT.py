import telebot
import buttons


bot = telebot.TeleBot('7684540340:AAGl6p10m49UZkSI8s-9w4KC4B850ip1BLA')



@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    bot.send_message(user_id, f'Добро пожаловать, @{message.from_user.username}!', reply_markup=telebot.types.ReplyKeyboardRemove())


@bot.message_handler(commands=['geophone'])
def geophone(message):
    keyboard = geophone.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_phone = geophone.KeyboardButton(text="Отправить номер телефона", request_contact=True)
    button_geo = geophone.KeyboardButton(text="Отправить местоположение", request_location=True)
    keyboard.add(button_phone, button_geo)
    bot.send_message(message.chat.id,
                     "Отправь мне свой номер телефона или поделись местоположением, жалкий человечишка!",
                     reply_markup=keyboard)



@bot.message_handler(content_types=['text'])
def get_name(message):
    user_id = message.from_user.id
    user_name = message.text
    bot.send_message(user_id, 'Отлично! Теперь отправь свой номер!',
                     reply_markup=buttons.num_button())
    bot.register_next_step_handler(message, get_num, user_name)


def get_num(message, user_name):
    user_id = message.from_user.id
    if message.contact:
        bot.send_message(user_id, 'Регистрация прошла успешно!',
                         reply_markup=telebot.types.ReplyKeyboardRemove())
    else:
        bot.send_message(user_id, 'Отправьте контакт по кнопке или отправьте контакт через скрепку!')
        bot.register_next_step_handler(message, get_num, user_name)

bot.polling(non_stop=True)
