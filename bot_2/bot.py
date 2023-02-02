"""Doc."""
import telebot
import game
import calculator as c
from config import TOKEN
import log_generate as lg
import logging

bot = telebot.TeleBot(TOKEN)
chat_id = ''
dic = {}

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
    filename='bot.log', filemode='a', encoding='utf=8'
)
logger = logging.getLogger(__name__)


@bot.message_handler(commands=['start'])
def start(message):
    """Doc."""
    logging.info(
        msg=f'Бот получил команду "{message.text}"')
    lg.write_data(f'Бот получил команду "{message.text}"')
    bot.send_message(
        message.chat.id, f'Привет, {message.from_user.first_name}!')
    bot.send_message(message.chat.id, 'Я еще только учусь и знаю несколько '
                     'слов:\n'
                                      'поиграем\nпосчитаем\nпомощь')
    bot.send_message(message.chat.id, 'Чем займемся?')


@ bot.message_handler(commands=['help'])
def help(message):
    """Doc."""
    lg.write_data(f'Бот получил команду "{message.text}"')
    bot.send_message(chat_id, 'Я еще только учусь и понимаю слова:\n'
                              '/start - команда приветствия\n'
                              'поиграем - игра в крестики-нолики;\n'
                              'посичитаем - могу считать примеры записанные в '
                              'одну строку например: 35*(75/5);\n'
                              '/help - вывод известных мне слов;')


@ bot.message_handler()
def get_user_text(message):
    """Выбор функций бота."""
    lg.write_data(f'Бот получил команду "{message.text}"')
    mes = message
    global chat_id
    chat_id = mes.chat.id
    if mes.text.lower() == 'поиграем':
        bot.send_message(chat_id, 'Класс! Я умею играть в крестики-нолики!')
        bot.send_message(
            chat_id, 'Давай играть! Чур у меня нолики! Хочешь ходить первым?')
        lg.write_data('Начинается игра "крестики-нолики"')
        global dic
        dic = {'1': '.', '2': '.', '3': '.', '4': '.',
               '5': '.', '6': '.', '7': '.', '8': '.', '9': '.'}
        lg.write_data('Словарь заполнен точками')
        bot.register_next_step_handler(mes, start_game)
    elif mes.text.lower() == 'посчитаем':
        bot.send_message(chat_id, 'Хорошо! Вводи пример!')
        lg.write_data('Получаем пример для решения')
        bot.register_next_step_handler(mes, count_example)
    else:
        lg.write_data('Зафиксирована неизвестная команда')
        bot.send_message(
            message.chat.id, 'Я тебя не понимаю! '
            'Воспользуйся командой "/help"!')


def start_game(message):
    """Функция определения, кто будет ходить первым."""
    if message.text == 'да':
        lg.write_data('Пользователь принял решение ходить первым')
        bot.send_message(chat_id, 'Выбери клетку!')
        bot.register_next_step_handler(message, user_check)
    elif message.text == 'нет':
        lg.write_data('Бот ходит первым')
        bot.send_message(chat_id, 'Хорошо, я начинаю!')
        pc_check()
    else:
        lg.write_data(
            'В функции определения хода зафиксирована неизвестная команда '
            f'"{message.text}"')
        bot.send_message(chat_id, 'Я тебя не пониманию! Скажи еще раз!')
        bot.register_next_step_handler(message, start_game)


def user_check(message):
    """Ход пользователя."""
    global dic
    lg.write_data('Начался ход пользователя')
    player_turn = message.text
    if player_turn in (
            '1', '2', '3', '4', '5', '6', '7', '8', '9') and dic.get(
                player_turn) == '.':
        dic[player_turn] = 'x'
        lg.write_data(f'Пользователь выбрал клетку: {player_turn}')
        if game.check_winner(dic):
            lg.write_data('Пользователь победил в игре')
            bot.send_message(chat_id, 'Ты выиграл!')
        elif '.' not in dic.values():
            lg.write_data('Игра завершилась ничьей')
            bot.send_message(chat_id, 'Ой, у нас ничья!')
        else:
            bot.send_message(chat_id, game.print_dic(dic))
            pc_check()
    else:
        lg.write_data(
            'На ходе пользователя зафиксирован не корректный ввод: '
            f'{player_turn}')
        bot.send_message(chat_id, 'Ты что-то не то ввел! Попробуй еще раз!')
        bot.register_next_step_handler(message, user_check)


def pc_check():
    """Ход бота."""
    global dic
    lg.write_data('Начался ход бота')
    bot.send_message(chat_id, 'Мой ход:')
    bot_choice = game.pc_choice(dic)
    lg.write_data(f'Бот выбирает клетку {bot_choice}')
    dic[bot_choice] = '0'
    bot.send_message(chat_id, game.print_dic(dic))
    if game.check_winner(dic):
        lg.write_data('Бот победил в игре')
        bot.send_message(chat_id, 'Я победил!')
    elif '.' not in dic.values():
        lg.write_data('Игра завершилась ничьей')
        bot.send_message(chat_id, 'Ой у нас ничья!')
    else:
        message = bot.send_message(chat_id, 'Твой ход!')
        bot.register_next_step_handler(message, user_check)


def count_example(message):
    """Функиця решения примера."""
    example, example_list = c.get_nums(message.text)
    lg.write_data(f'Пользователь ввел пример: {example}')
    result = c.get_result(example_list)
    lg.write_data(f'Получен ответ: {result}')
    bot.send_message(chat_id, f'{example} = {result}')


def start_bot():
    """Doc."""
    print('server start')
    bot.polling(none_stop=True)
