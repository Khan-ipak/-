import telebot
import cons

bot = telebot.TeleBot('7684540340:AAGl6p10m49UZkSI8s-9w4KC4B850ip1BLA')

users = {}


@bot.message_handler(commands=['start'])
def start(message):
        user_id = message.from_user.id
        if database.check_user(user_id):
            bot.send_message(user_id, f'Добро пожаловать, @{message.from_user.username}!',
                             reply_markup=telebot.types.ReplyKeyboardRemove())
            bot.send_message(user_id, 'Выберите пункт меню:',
                             reply_markup=buttons.main_menu(database.get_pr_buttons()))
        else:
            bot.send_message(user_id, 'Привет! Давай начнем регистрацию! \nНапиши свое имя',
                             reply_markup=telebot.types.ReplyKeyboardRemove())
            bot.register_next_step_handler(message, get_name)

def start(message):
    #Переводы
    if cons.lang == 'ru':
      start_msg = 'Здравствуйте, уважаемый клиент!\nВас приветствует бот компании!\nПожалуйста, выберите из меню то что вас интересует.'
      order_menu = 'Заказать такси'
      info_menu = 'Информация'
      exit_menu = 'Покинуть бота'
    elif cons.lang == 'uz':
       start_msg = 'Grettings.'
      order_menu = 'Order Taxi'
      info_menu = 'Information'
      exit_menu = 'Leave bot'

    start_markup = types.ReplyKeyboardMarkup(True, False)
    start_markup.row('🚕 '+cons.order_menu+' 🚕', )
    start_markup.row('ℹ️ '+cons.info_menu+' ℹ️')
    start_markup.row('Uzbek', 'Русский язык')
    start_markup.row('🚪 '+cons.exit_menu+' 🚪')
    bot.send_message(message.chat.id, cons.start_msg, reply_markup=start_markup)

@bot.message_handler(content_types=["text"])
def main(message):
    if message.text == 'Uzbek':
        cons.lang = 'uz'
        msg = bot.send_message(message.chat.id, 'Your language is -'+cons.lang+' -', reply_markup=start_markup)
        bot.register_next_step_handler(msg, start)
    elif message.text == 'Русский язык':
        cons.lang = 'ru'
        msg = bot.send_message(message.chat.id, 'Вы выбрали русский язык-'+cons.lang+' -', reply_markup=start_markup)
        bot.register_next_step_handler(msg, start)

def get_name(message):
        user_id = message.from_user.id
        user_name = message.text
        bot.send_message(user_id, 'Отлично! Теперь отправь свой номер!',
                         reply_markup=buttons.num_button())
        bot.register_next_step_handler(message, get_num, user_name)

def get_num(message, user_name):
        user_id = message.from_user.id
        if message.contact:
            user_num = message.contact.phone_number
            database.register(user_id, user_name, user_num)
            bot.send_message(user_id, 'Регистрация прошла успешно!',
                             reply_markup=telebot.types.ReplyKeyboardRemove())
        else:
            bot.send_message(user_id, 'Отправьте контакт по кнопке или отправьте контакт через скрепку!')
            bot.register_next_step_handler(message, get_num, user_name)


    bot.polling(none_stop=True)
