# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

len_arr = int(input('введите величинцу массива _'))
import random
arr = [random.randint(1, 10) for _ in range(len_arr)]
print(arr)
x = int(input('введите значение x = '))
x_count_plus = float('inf')
ind_plus = float('inf')
x_count_minus = float('inf')
ind_minus = float('inf')

for i in arr:
    if i - x == 0:
        print(x)
        quit()
    elif i - x < 0:
        if(i - x) * -1 < ind_minus:
            ind_minus = (i - x) * -1
            x_count_minus = i
    elif i - x > 0:
        if(i - x) < ind_plus:
            ind_plus = i - x
            x_count_plus = i
if ind_plus < ind_minus:
    print(x_count_plus)
elif ind_minus < ind_plus:
    print(x_count_minus)
elif ind_plus == ind_minus:
    print(x_count_minus, x_count_plus)

