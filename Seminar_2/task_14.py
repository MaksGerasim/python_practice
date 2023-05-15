# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N
number_n = int(input('ввведите максимальное расчетное число _'))
degree = 0
count = 0
while number_n > count:
    count = 2 ** degree
    if number_n < count:
        quit()
    print(count)
    degree += 1
