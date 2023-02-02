"""Doc."""
import telebot
import working_with_datebase as wd
import log_generate as lg
from config import TOKEN

bot = telebot.TeleBot(TOKEN)
chat_id = ''
surname = ''
name = ''
patronymic = ''
email_address = ''
telephone = ''


@bot.message_handler(commands=['start'])
def start(message):
    """Doc."""
    lg.write_data(f'Бот получил команду "{message.text}"')
    global chat_id
    chat_id = message.chat.id
    bot.send_message(chat_id, f'Привет, {message.from_user.first_name}!\n'
                              f'Я умею работать с телефонным справочником.')
    bot.send_message(chat_id, 'Что будем делать?\n'
                              '1. Добавить контакт\n'
                              '2. Найти контакт\n'
                              '3. Удалить контакт\n'
                              '4. Показать справочник\n'
                              '5. Импортировать справочник\n'
                              '6. Экспортировать справочник\n'
                              'Для повторного вывода меню введи /help\n'
                              'Введи цифру!')


@bot.message_handler(commands=['help'])
def help(message):
    """Doc."""
    lg.write_data(f'Бот получил команду "{message.text}"')
    bot.send_message(chat_id, 'Что будем делать?\n'
                              '1. Добавить контакт\n'
                              '2. Найти контакт\n'
                              '3. Удалить контакт\n'
                              '4. Показать справочник\n'
                              '5. Импортировать справочник\n'
                              '6. Экспортировать справочник\n'
                              'Для повторного вывода меню введи /help\n'
                              'Введи цифру!')


@bot.message_handler()
def choice(message):
    """Doc."""
    lg.write_data(f'Бот получил команду "{message.text}"')
    global chat_id
    chat_id = message.chat.id
    if message.text == '1':
        lg.write_data('Начато создание контакта')
        get_name()
    elif message.text == '2':
        lg.write_data('Запущен поиск контакта')
        bot.send_message(chat_id, 'Введите одно из данных для поиска')
        bot.register_next_step_handler(message, find_contact)
    elif message.text == '3':  # Удалить контакт
        lg.write_data('Запущено удаление контакта')
        bot.send_message(chat_id, 'Выбери контакт из списка и введи цифру!')
        bot.send_message(chat_id, wd.print_book())
        lg.write_data('Пользователю выведен справочник')
        bot.register_next_step_handler(message, del_contact)
    elif message.text == '4':  # Вывод справочника
        lg.write_data('Запущен вывод справочника')
        bot.send_message(chat_id, wd.print_book())
    elif message.text == '5':  # Импорт данных из получаемого файла
        lg.write_data('Запущен импорт словаря из внешнего файла')
        bot.send_message(chat_id, 'Отправьте мне файл .txt')
        bot.register_next_step_handler(message, import_base)
    elif message.text == '6':
        lg.write_data('Запущен экспорт справочника')
        bot.send_message(chat_id, 'В каком формате отправить справочник?\n'
                                  '1. Одна запись - на одной строке;\n'
                                  '2. Каждое значение на отдельной строке\n'
                                  'Введите цифру!')
        bot.register_next_step_handler(message, export_base)
    else:
        lg.write_data('Зафиксирована неизвестная команда')
        bot.send_message(chat_id, 'Ты ввел что-то не то!')


def get_name():
    """Запрашиваем имя."""
    mess = bot.send_message(chat_id, 'Введите имя')
    bot.register_next_step_handler(mess, get_surname)


def get_surname(mess):
    """Заносим в переменную имя и запрашиваем фамилию."""
    global name
    name = mess.text
    lg.write_data(f'Получено имя контакта {name}')
    bot.send_message(chat_id, 'Введите фамилию')
    bot.register_next_step_handler(mess, get_patronymic)


def get_patronymic(mess):
    """Заносим в переменную фамилию и запрашиваем отчество."""
    global surname
    surname = mess.text
    lg.write_data(f'Получена фамилия контакта {surname}')
    bot.send_message(chat_id, 'Введите отчество')
    bot.register_next_step_handler(mess, get_email)


def get_email(mess):
    """Заносим в переменную отчество и запрашиваем email."""
    global patronymic
    patronymic = mess.text
    lg.write_data(f'Получено отчество контакта {patronymic}')
    bot.send_message(chat_id, 'Введите email')
    bot.register_next_step_handler(mess, get_telephone)


def get_telephone(mess):
    """Заносим в переменную email и запрашиваем телефон."""
    global email_address
    email_address = mess.text
    lg.write_data(f'Получен email контакта {email_address}')
    bot.send_message(chat_id, 'Введите телефон')
    bot.register_next_step_handler(mess, set_data)


def set_data(mess):
    """Заносим в переменную телефон и записываем контакт в базу."""
    global telephone
    telephone = mess.text
    lg.write_data(f'Получен телефон контакта {telephone}')
    wd.add_contact(surname, name, patronymic, email_address, telephone)
    bot.send_message(chat_id, 'Контакт добавлен')


def find_contact(mess):
    """Поиск контакта в справочнике."""
    text = mess.text
    lg.write_data(f'Для поиска от пользователя получены данные: {text}')
    text = wd.find_in_book(text)
    if text:
        lg.write_data(f'Найдены данные:\n {surname}')
        bot.send_message(chat_id, text)
    else:
        lg.write_data('Поиск ни чего не нашел')
        bot.send_message(chat_id, 'Ни чего не нашел')


def del_contact(message):
    """Удаление контакта."""
    key = message.text
    if key.isdigit() and int(key) in wd.book.keys():
        lg.write_data(f'От пользователя получен ключ: {key}')
        del wd.book[int(key)]
        lg.write_data('Контакт удален из справочника')
        bot.send_message(chat_id, 'Контакт удален')
    else:
        lg.write_data(
            f'От пользователя получен ключ: {key}, контакт не найден!')
        bot.send_message(chat_id, 'Контакт не найден!')


def import_base(message):
    """Импортирование БД."""
    file_info = bot.get_file(message.document.file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    src = 'C:/Users/roman/Desktop/Work for IT/GeekBrains/seminars/Python'\
        '/Seminar_9/bot_3/files/' + \
        message.document.file_name
    with open(src, 'wb') as new_file:
        new_file.write(downloaded_file)
    lg.write_data('Файл получен и сохранен')
    wd.import_base(src)
    lg.write_data('Импорт завершен')
    bot.send_message(chat_id, 'Импорт данных завершен!')


def export_base(message):
    """Экспортирование БД."""
    if message.text == '1':
        lg.write_data('Запущен экспорт по первому правилу')
        wd.ex_base(message.text)
        bot.send_document(chat_id, open(
            r'C:/Users/roman/Desktop/Work for IT'
            r'/GeekBrains/seminars/Python'
            r'/Seminar_9/bot_3/export_data.csv', 'rb'))
    elif message.text == '2':
        lg.write_data('Запущен экспорт по второму правилу')
        wd.ex_base(message.text)
        bot.send_document(chat_id, open(
            r'C:/Users/roman/Desktop/Work for IT'
            r'/GeekBrains/seminars/Python'
            r'/Seminar_9/bot_3/export_data_2.csv', 'rb'))
    else:
        lg.write_data(f'Зафиксирован не корректный ввод: {message.text}')
        bot.send_message(chat_id, 'Введите верно комманду')


def start_bot():
    """Doc."""
    print('server start')
    bot.polling(none_stop=True)
