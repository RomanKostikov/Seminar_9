"""Функции игры крестики-нолики."""

import random


def print_dic(dicti):  # Печать матрицы
    return f'| {dicti["1"]} | {dicti["2"]} | {dicti["3"]} |\n' \
           f'{" " + "-" * 13}\n' \
           f'| {dicti["4"]} | {dicti["5"]} | {dicti["6"]} |\n' \
           f'{" " + "-" * 13}\n' \
           f'| {dicti["7"]} | {dicti["8"]} | {dicti["9"]} |'


def check_winner(dicti):  # Проверка победителя
    if (dicti.get('1') == '0' and dicti.get('2') == '0' and dicti.get('3') == '0') or \
            (dicti.get('1') == 'x' and dicti.get('2') == 'x' and dicti.get('3') == 'x') or \
            (dicti.get('4') == '0' and dicti.get('5') == '0' and dicti.get('6') == '0') or \
            (dicti.get('4') == 'x' and dicti.get('5') == 'x' and dicti.get('6') == 'x') or \
            (dicti.get('7') == '0' and dicti.get('8') == '0' and dicti.get('9') == '0') or \
            (dicti.get('7') == 'x' and dicti.get('8') == 'x' and dicti.get('9') == 'x') or \
            (dicti.get('1') == '0' and dicti.get('5') == '0' and dicti.get('9') == '0') or \
            (dicti.get('1') == 'x' and dicti.get('5') == 'x' and dicti.get('9') == 'x') or \
            (dicti.get('3') == '0' and dicti.get('5') == '0' and dicti.get('7') == '0') or \
            (dicti.get('3') == 'x' and dicti.get('5') == 'x' and dicti.get('7') == 'x') or \
            (dicti.get('3') == '0' and dicti.get('6') == '0' and dicti.get('9') == '0') or \
            (dicti.get('3') == 'x' and dicti.get('6') == 'x' and dicti.get('9') == 'x') or \
            (dicti.get('2') == '0' and dicti.get('5') == '0' and dicti.get('8') == '0') or \
            (dicti.get('2') == 'x' and dicti.get('5') == 'x' and dicti.get('8') == 'x') or \
            (dicti.get('1') == '0' and dicti.get('4') == '0' and dicti.get('7') == '0') or \
            (dicti.get('1') == 'x' and dicti.get('4') == 'x' and dicti.get('7') == 'x'):
        return True
    else:
        return False


def pc_choice(dic):  # Игра против ПК
    # Для проверки 2-х "0" в ряд
    # Проверка клетки 3
    if ((dic['1'] == '0' and dic['2'] == '0') or (dic['7'] == '0' and dic['5'] == '0') or
            (dic['6'] == '0' and dic['9'] == '0')) and dic['3'] == '.':
        return '3'
    # Проверка клетки 6
    elif ((dic['4'] == '0' and dic['5'] == '0') or (dic['3'] == '0' and dic['9'] == '0')) and dic['6'] == '.':
        return '6'
    # Проверка клетки 9
    elif ((dic['7'] == '0' and dic['8'] == '0') or (dic['1'] == '0' and dic['5'] == '0') or
          (dic['3'] == '0' and dic['6'] == '0')) and dic['9'] == '.':
        return '9'
    # Проверка клетки 2
    elif ((dic['5'] == '0' and dic['8'] == '0') or (dic['1'] == '0' and dic['3'] == '0')) and dic['2'] == '.':
        return '2'
    # Проверка клетки 5
    elif ((dic['2'] == '0' and dic['8'] == '0') or (dic['4'] == '0' and dic['6'] == '0') or
          (dic['3'] == '0' and dic['7'] == '0') or (dic['1'] == '0' and dic['9'] == '0')) and dic['5'] == '.':
        return '5'
    # Проверка клетки 8
    elif ((dic['7'] == '0' and dic['9'] == '0') or (dic['2'] == '0' and dic['5'] == '0')) and dic['8'] == '.':
        return '8'
    # Проверка клетки 1
    elif ((dic['2'] == '0' and dic['3'] == '0') or (dic['5'] == '0' and dic['9'] == '0') or
          (dic['4'] == '0' and dic['7'] == '0')) and dic['1'] == '.':
        return '1'
    # Проверка клетки 4
    elif ((dic['1'] == '0' and dic['7'] == '0') or (dic['5'] == '0' and dic['6'] == '0')) and dic['4'] == '.':
        return '4'
    # Проверка клетки 7
    elif ((dic['1'] == '0' and dic['4'] == '0') or (dic['5'] == '0' and dic['3'] == '0') or
          (dic['8'] == '0' and dic['9'] == '0')) and dic['7'] == '.':
        return '7'
    # Для проверки 2-х "Х" в ряд
    # Проверка клетки 3
    elif ((dic['1'] == 'x' and dic['2'] == 'x') or (dic['7'] == 'x' and dic['5'] == 'x') or
          (dic['6'] == 'x' and dic['9'] == 'x')) and dic['3'] == '.':
        return '3'
    # Проверка клетки 6
    elif ((dic['4'] == 'x' and dic['5'] == 'x') or (dic['3'] == 'x' and dic['9'] == 'x')) and dic['6'] == '.':
        return '6'
    # Проверка клетки 9
    elif ((dic['7'] == 'x' and dic['8'] == 'x') or (dic['1'] == 'x' and dic['5'] == 'x') or
          (dic['3'] == 'x' and dic['6'] == 'x')) and dic['9'] == '.':
        return '9'
    # Проверка клетки 2
    elif ((dic['5'] == 'x' and dic['8'] == 'x') or (dic['1'] == 'x' and dic['3'] == 'x')) and dic['2'] == '.':
        return '2'
    # Проверка клетки 5
    elif ((dic['2'] == 'x' and dic['8'] == 'x') or (dic['4'] == 'x' and dic['6'] == 'x') or
          (dic['3'] == 'x' and dic['7'] == 'x') or (dic['1'] == 'x' and dic['9'] == 'x')) and dic['5'] == '.':
        return '5'
    # Проверка клетки 8
    elif ((dic['7'] == 'x' and dic['9'] == 'x') or (dic['2'] == 'x' and dic['5'] == 'x')) and dic['8'] == '.':
        return '8'
    # Проверка клетки 1
    elif ((dic['2'] == 'x' and dic['3'] == 'x') or (dic['5'] == 'x' and dic['9'] == 'x') or
          (dic['4'] == 'x' and dic['7'] == 'x')) and dic['1'] == '.':
        return '1'
    # Проверка клетки 4
    elif ((dic['1'] == 'x' and dic['7'] == 'x') or (dic['5'] == 'x' and dic['6'] == 'x')) and dic['4'] == '.':
        return '4'
    # Проверка клетки 7
    elif ((dic['1'] == 'x' and dic['4'] == 'x') or (dic['5'] == 'x' and dic['3'] == 'x') or
          (dic['8'] == 'x' and dic['9'] == 'x')) and dic['7'] == '.':
        return '7'

    else:
        pc_takes = random.randint(1, 9)
        while dic[str(pc_takes)] != '.':
            pc_takes = random.randint(1, 9)
        return str(pc_takes)
