import math
"""Задание 1
Решите квадратное уравнение 5x2-10x-400=0 последовательно
сохраняя переменные a, b, c, d, x1 и x2.
Попробуйте решить уравнения с другими значениями a, b, c.
"""

import math
# version 1
# a = 5
# b = 10
# c = 400
# version 2
a = 5
b = 100
c = 400
d = b ** 2 - 4 * a * c
if d < 0:
    print("Уравнение не имеет корней")
elif d > 0:
    print("Уравнение имеет два корня")
    print(f"x1 = {round((-b - math.sqrt(d)) / (2 * a),3)} ; x2 = {round((-b + math.sqrt(d)) / (2 * a),3)} ")
else:
    print("Уравнение имеет один корень")
    print(f"x = {-b / 2 * a}")

"""
Задание 2
Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей. 
Дано a, b, c - стороны предполагаемого треугольника. 
Требуется сравнить длину каждого отрезка-стороны с суммой двух других. 
Если хотя бы в одном случае отрезок окажется больше суммы двух других, 
то треугольника с такими сторонами не существует. 
Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.
"""

try:
    a = int(input("Введите целое число для стороны a: "))
    b = int(input("Введите целое число для стороны b: "))
    c = int(input("Введите целое число для стороны c: "))
except ValueError:
    print("Ошибка ввода значения. Запустите программу еще раз")
else:
    print("Данные введены успешно")
    if a + b > c and a + c > b and b + c > a:
        print("Ура. Треугольник существует")

        print("Треугольник равносторнний" if a == b == c else "Треугольник разносторонний" if a != b != c else "Треугольник равнобедренный")
    else:
        # noinspection SpellCheckingInspection
        print("Упс. Треугольник не существует")

"""
Задание 3. 
Напишите код, который запрашивает число и сообщает является ли оно простым или составным. 
Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”. 
Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.
"""

try:
    n = int(input("Введите целое положительное число до 100 000 включительно: "))
except ValueError:
    print("Неверный формат ввода. Запустите программу еще раз")
else:
    if 0 <= n <= 100000:
        for i in range(2, int(math.sqrt(n)) + 2):
            if n % i == 0 or n == 2:
                print("Введенное число является составным")
                break
        else:
            print("Введенное число является простым")
    else:
        print("Вы ввели значение за допустимыми пределами")
