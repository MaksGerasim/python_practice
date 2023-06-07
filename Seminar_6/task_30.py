# Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.


def progression(a1=int(input('a1 = ')), n=int(input('n = ')), d=int(input('d = '))):
    list_progression = []
    while n > 0:
        n -= 1
        an = a1 + n * d
        list_progression.append(an)
    return list_progression

print(progression())