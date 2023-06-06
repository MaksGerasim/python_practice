 # Определить индексы элементов массива (списка),
 # значения которых принадлежат заданному диапазону
 # (т.е. не меньше заданного минимума и не больше заданного максимума)

import random
len_arr = int(input('введите длину списка _'))
arr_rand = [random.randint(1, 10) for _ in range(len_arr)]
first_num = int(input('введите минимальное значение'))
second_num = int(input('введите максимальное значение'))
print(arr_rand)
index_list = []
current_index = 0
for i in arr_rand:
    if (i >= first_num) and (i <= second_num):
        index_list.append(current_index)
    current_index += 1
print(index_list)



