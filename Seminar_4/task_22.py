# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества.
# m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.
import random
len_arr = int(input('введите длину списка _'))
arr_1 = [random.randint(1, 10) for _ in range(len_arr)]
len_arr = int(input('введите длину списка _'))
arr_2 = [random.randint(1, 10) for _ in range(len_arr)]
print(arr_1)
print(arr_2)
arr_con = []
for i in arr_1:
    for j in arr_2:
        if i == j:
            arr_con.append(i)

arr_con = list(set(arr_con))
arr_con.sort()
print(arr_con)