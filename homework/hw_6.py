import random
from sys import argv



# Задание 1
# Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
# Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
# Для простоты договоримся, что год может быть в диапазоне [1, 9999].
# Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь.
# Проверку года на високосность вынести в отдельную защищённую функцию.

def dat(st):
    day, month, year = map(int, (st.split(".")))
    if year in range(1, 10000) and month in range(1, 13) and day in range(1, 32):
        if year % 400 == 0 or year % 4 == 0 and year % 100 != 0 and month == 2:
            if day <= 29:
                return True
            else:
                return False
        if month in [1, 3, 5, 7, 8, 10, 12]:
            if day <= 31:
                return True
            else:
                return False
        elif month == 2:
            if day <= 28:
                return True
            else:
                return False
        else:
            if day <= 30:
                return True
            else:
                return False
    else:
        return False


# print(dat("29.02.2025"))

# Задание 2
# В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.

argums = argv[1]


# print(dat(argums))

# Задание 3
# Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код, решающий задачу о 8 ферзях.
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
# Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
# Если ферзи не бьют друг друга верните истину, а если бьют - ложь.
# Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для случайной расстановки
# ферзей в задаче выше. Проверяйте различный случайные варианты и выведите 4 успешных расстановки.

def quine_8_moves_ver1(n: int) -> bool:
    """Программа определяет, можно ли поставить на шахматной доске n ферзей, чтобы они не били друг друга
    :param n: количество gj
    :return : True or False
    """
    points = [list(map(int, input(f"Укажите координаты {i}-го ферзя(два целых числа от 1 до 8)> ").split())) for i in
              range(n)]
    flag = True
    i = 1
    print(f"Введенные координаты: {points}")
    board = [["." for j in range(8)] for i in range(8)]
    for po in points:
        if not flag:
            return flag
        if po[0] in range(1, 9) and po[1] in range(1, 9):
            if board[po[0] - 1][po[1] - 1] != "Q" and board[po[0] - 1][po[1] - 1] != "*":
                board[po[0] - 1][po[1] - 1] = "Q"
            else:
                return False
            for i in range(8):
                for j in range(8):
                    if board[i][j] != board[po[0] - 1][po[1] - 1]:
                        if board[i][j] != "Q":
                            if (abs(po[0] - 1 - i) == abs(po[1] - 1 - j) or po[0] - 1 == i or po[1] - 1 == j):
                                board[i][j] = "*"
                        else:
                            flag = False

        else:
            print("Вы ввелли неверные координаты одного из ферзей {po}. Попробуйте еще раз")
            print("Либо вы поставили очередного ферзя на место где был предыдудщий ферзь")
            flag = False
            return flag
            # quine_8_moves()
    else:
        print("Удачная расстановка")
        for el in board:
            print(*el)
        print(f"Удачные координаты: {points}")
        return flag


# print(quine_8_moves_ver1(2))

good_data = {}
index = 1


def quine_8_moves_ver2(n: int) -> bool:
    """Программа определяет, можно ли поставить на шахматной доске n ферзей, чтобы они не били друг друга
    :param n: количество gj
    :return : True or False
    """
    points = [[random.randint(1, 8), random.randint(1, 8)] for _ in range(n)]
    flag = True
    board = [["." for j in range(8)] for i in range(8)]
    for po in points:
        if not flag:
            return False
        if po[0] in range(1, 9) and po[1] in range(1, 9):
            if board[po[0] - 1][po[1] - 1] != "Q" and board[po[0] - 1][po[1] - 1] != "*":
                board[po[0] - 1][po[1] - 1] = "Q"
            else:
                return False
            for i in range(8):
                for j in range(8):
                    if board[i][j] != board[po[0] - 1][po[1] - 1]:
                        if board[i][j] != "Q":
                            if (abs(po[0] - 1 - i) == abs(po[1] - 1 - j) or po[0] - 1 == i or po[1] - 1 == j):
                                board[i][j] = "*"
                        else:
                            flag = False

        else:
            print("Вы ввелли неверные координаты одного из ферзей {po}. Попробуйте еще раз")
            print("Либо вы поставили очередного ферзя на место где был предыдудщий ферзь")
            quine_8_moves_ver2(4)
    else:
        print()
        print("Удачная расстановка")
        for el in board:
            print(*el)
        print(f"Удачные координаты: {points}")
        global index
        good_data[str(n) + "_" + str(index)] = points
        index += 1
        return True

# for _ in range(90500000):
#     if quine_8_moves_ver2(6) == True:
#         i += 1
#         print(quine_8_moves_ver2(6))
#     if i==4:
#         break
# print(good_data)
