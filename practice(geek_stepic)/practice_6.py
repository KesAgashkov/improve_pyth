__all__ = ["func", "func2"]

# """
# Задание №2
# Создайте модуль с функцией внутри.
# Функция принимает на вход три целых числа:
# нижнюю и верхнюю границу и количество попыток.
# Внутри генерируется случайное число в указанных
# границах и пользователь должен угадать его за заданное число попыток.
# Функция выводит подсказки “больше” и “меньше”.
# Если число угадано, возвращается истина, а если попытки исчерпаны - ложь.
# """
# from random import randint
#
#
# def func(start, stop, count):
#     num = randint(start, stop + 1)
#     i = 0
#     while count > i:
#         u_num = int(input(f"введите число в диапазоне от {start} до {stop}:>"))
#         if u_num > num:
#             print('меньше!')
#         elif u_num < num:
#             print('больше!')
#         else:
#             print('Угадал!')
#             return True
#         i += 1
#     return False
#
#
# print(func(1, 3, 3))
#
#
# """
# Задание №3
#
# Улучшаем задачу 2.
# Добавьте возможность запуска функции “угадайки”
# из модуля в командной строке терминала.
# Строка должна принимать от 1 до 3 аргументов: параметры вызова функции.
# Для преобразования строковых аргументов командной строки в
# числовые параметры используйте генераторное выражение.
# """
#
# from random import randint
# from sys import argv
#
# def func(argums):
#     num = randint(argums[0], argums[1])
#     i = 0
#     while argums[2] > i:
#         u_num = int(input(f"введите число в диапазоне от {argums[0]} до {argums[1]}:>"))
#         if u_num > num:
#             print('меньше!')
#         elif u_num < num:
#             print('больше!')
#         else:
#             print('Угадал!')
#             return True
#         i += 1
#     return False
#
# argums = [int(el) for el in argv[1:]]
# print(func(argums))
#
# """
# Задание №4
#
# Создайте модуль с функцией внутри.
# Функция получает на вход загадку, список с возможными вариантами отгадок и количество попыток на угадывание.
# Программа возвращает номер попытки, с которой была отгадана загадка или ноль, если попытки исчерпаны.
# """
#
#
# def func(qws, ans, count):
#     print(f"загадка: {qws}")
#     print(f"варианты ответов: {ans}")
#     i = 0
#     while count >= i:
#         u_ans = input(f"введите ваш ответ:>")
#         if u_ans == ans[0]:
#             print(f'Правильно! Угадал за {i+1} попытку')
#             return i+1
#         else:
#             print('Не угадал!')
#             i += 1
#         if i == count:
#             return 0
#
#
# print(func("Не лает, не кусает, в дом не пускает",
#            ['замок', 'охранник', 'собака'], 3))
#
#
#
# """
# Задание №5
#
# Добавьте в модуль с загадками функцию, которая хранит словарь списков.
# Ключ словаря - загадка, значение - список с отгадками.
# Функция в цикле вызывает загадывающую функцию, чтобы передать ей все свои загадки.
# """
#
def func(qws, ans, count):
    print(f"загадка: {qws}")
    print(f"варианты ответов: {ans}")
    i = 0
    while count >= i:
        u_ans = input(f"введите ваш ответ:>")
        if u_ans == ans[0]:
            print(f'Правильно! Угадал за {i + 1} попытку')
            return i + 1
        else:
            print('Не угадал!')
            i += 1
        if i == count:
            return 0
#
#
# def func_2(dct):
#     for k, v in dct.items():
#         print(func(k, v, 3))
#
#
# dct = {"В чем сила: ": ['в правде', 'в деньгах', 'в силе'],
#        "Не лает, не кусает, в дом не пускает": ['замок', 'охранник', 'собака']}
#
# func_2(dct)

# Добавьте в модуль с загадками функцию, которая принимает на вход строку (текст загадки) и число
# (номер попытки, с которой она угадана).
# Функция формирует словарь с информацией о результатах отгадывания.
# Для хранения используйте защищённый словарь уровня модуля.
# Отдельно напишите функцию, которая выводит результаты угадывания из защищённого словаря в удобном для чтения виде.
# Для формирования результатов используйте генераторное выражение.


_dct ={}


def func2(que, count):
    print(que)
    a = "в правде"

    i = 0
    while count > i:
        ans = input("Напишите ответ>")
        if ans == a:
            _dct[i + 1] = "Вы угадали"
            return
        else:
            _dct[i + 1] = "Не угадали"
            i += 1


func2("В чем сила:", 3)
print(_dct)


# Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
# Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
# Для простоты договоримся, что год может быть в диапазоне [1, 9999].
# Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь.
# Проверку года на високосность вынести в отдельную защищённую функцию.

# def dat(st):
#     day, month, year = st.split(".")
#     if int(year) in range(1,9999):
#         if int(year) % 400 == 0 or int(year) % 4 == 0 and int(year) % 100 != 0 and month == "02":
#             if int(day)<=29:
#                 return True
#             else:
#                 return False
#         else:
#             if int(day) <= 28:
#                 return True
#             else:
#                 return False
#     if month in ["01", "03", "05", "07", "08", "10", "12"]:
#         if int(day) in range(1,32):
#             return True
#         else:
#             return False
#     else:
#         if int(day) in range(1, 31):
#             return True
#         else:
#             return False


# Создайте пакет с всеми модулями, которые вы создали за время занятия.
# Добавьте в __init__ пакета имена модулей внутри дандер __all__.
# В модулях создайте дандер __all__ и укажите только те функции, которые могут верно работать за пределами модуля.
