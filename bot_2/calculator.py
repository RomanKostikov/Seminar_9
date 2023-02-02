"""Модуль расчета."""


def get_nums(user_nums):
    """Получение данных от пользователя."""
    nums = user_nums.replace('+', ' + ') \
        .replace('-', ' - ') \
        .replace('*', ' * ') \
        .replace('/', ' / ') \
        .replace('(', '( ') \
        .replace(')', ' )') \
        .replace('i', 'j') \
        .split()
    nums_list = list()
    for el in nums:
        if 'j' in el:
            nums_list.append(complex(el))
        elif el.isdigit():
            nums_list.append(int(el))
        else:
            nums_list.append(el)
    return user_nums, nums_list


def calc(my_list):
    """Функция решения арифметических действий."""
    while '*' in my_list or '/' in my_list:
        for i in range(1, len(my_list), 2):
            if my_list[i] == '*':
                result = my_list.pop(i + 1) * my_list.pop(i - 1)
                my_list[i - 1] = result
                break
            elif my_list[i] == '/':
                result = my_list.pop(i - 1) / my_list.pop(i)
                my_list[i - 1] = result
                break

    while '+' in my_list or '-' in my_list:
        for i in range(1, len(my_list), 2):
            if my_list[i] == '-':
                result = my_list.pop(i - 1) - my_list.pop(i)
                my_list[i - 1] = result
                break
            elif my_list[i] == '+':
                result = my_list.pop(i + 1) + my_list.pop(i - 1)
                my_list[i - 1] = result
                break
    return my_list


def get_result(data):
    """Doc."""
    while '(' in data:  # Открытие скобок если они имеются
        first_i = len(data) - data[::-1].index('(') - 1
        second_i = first_i + data[first_i + 1:].index(')') + 1
        data = data[:first_i] + \
            calc(data[first_i + 1:second_i]) + data[second_i + 1:]
    data = calc(data)  # Вызов функции calc() после открытия скобок
    return ''.join(map(str, data))
