from math import sqrt
# Задание №1
# ✔ Пользователь вводит строку из четырёх
# или более целых чисел, разделённых символом “/”.
# Сформируйте словарь, где:
# ✔второе и третье число являются ключами.
# ✔первое число является значением для первого ключа.
# ✔четвертое и все возможные последующие числа
# хранятся в кортеже как значения второго ключа.

# a, b, c, *d = input('введите строку из четырёх или более целых чисел, разделённых символом “/”:> ').split('/')
# print({b: a, c: tuple(d)})

# Задание №2
# ✔ Самостоятельно сохраните в переменной строку текста.
# ✔ Создайте из строки словарь, где ключ — буква, а значение — код буквы.
# ✔ Напишите преобразование в одну строку.

# print({i: ord(i) for i in input('введите text:> ')})

"""
Задание №3
✔ Продолжаем развивать задачу 2.
✔ Возьмите словарь, который вы получили.
Сохраните его итераторатор.
✔ Далее выведите первые 5 пар ключ-значение,
обращаясь к итератору, а не к словарю.
"""

# dct_iter = iter({i: ord(i) for i in input('введите text:> ')}.items())
#
# for i in range(5):
#     print(next(dct_iter))

"""
Задание №4
✔ Создайте генератор чётных чисел от нуля до 100.
✔ Из последовательности исключите
числа, сумма цифр которых равна 8.
✔ Решение в одну строку.
"""
# print(*(i for i in range(0, 101, 2) if i % 10 + i // 10 != 8))

# print(*(i for i in range(0, 101, 2) if sum([int(i) for i in str(i)]) != 8))

# sum([int(i) for i in str(i).split()])


# Задание №5
# ✔ Напишите программу, которая выводит
# на экран числа от 1 до 100.
# ✔ При этом вместо чисел, кратных трем,
# программа должна выводить слово «Fizz»
# ✔ Вместо чисел, кратных пяти — слово «Buzz».
# ✔ Если число кратно и 3, и 5, то программа
# должна выводить слово «FizzBuzz».
# ✔ *Превратите решение в генераторное выражение.

# print(*("FizzBuzz" if i % 3 == 0 and i % 5 == 0 else "Buzz" if i % 5 == 0 else "Fizz" if i % 3 == 0 else i for i in
#         range(1, 101)),sep="\n")

# Задание №6
# ✔ Выведите в консоль таблицу умножения
# от 2х2 до 9х10 как на школьной тетрадке.
# ✔ Таблицу создайте в виде однострочного
# генератора, где каждый элемент генератора —
# отдельный пример таблицы умножения.
# ✔ Для вывода результата используйте «принт»
# без перехода на новую строку.


# gen = (f"\n" if j == 10 else f" {j} * {i} = {i * j} ".ljust(15) for i in range(2, 11) for j in range(2, 11))
# print(*gen)


"""
Задание №7
✔ Создайте функцию-генератор.
✔ Функция генерирует N простых чисел,
начиная с числа 2.
✔ Для проверки числа на простоту используйте
правило: «число является простым, если делится
нацело только на единицу и на себя».
"""

# def generate_prime(n):
#     count = 0
#     num = 1
#     is_prime = True
#     while count < n:
#         num += 1
#         for j in range(2, int(sqrt(num) + 1)):
#             if num % j == 0:
#                 is_prime = False
#                 break
#             else:
#                 is_prime = True
#         if is_prime:
#             count += 1
#             yield num
#
#
# for item, i in enumerate(generate_prime(n=10000), start=1):
#     print(f'{item}:  {i}')