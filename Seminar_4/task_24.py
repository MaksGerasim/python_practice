#  В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке,
#  причём кусты высажены только по окружности. Таким образом, у каждого куста есть
#  ровно два соседних. Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное
#  число ягод — на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
#  Эта система состоит из управляющего модуля и нескольких собирающих модулей.
#  Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом,
#  собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать
#  за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.

import random
len_arr = int(input('введите количество кустов на грядке _'))
arr = [random.randint(1, 10) for _ in range(len_arr)]
print('урожайность сгенерирована случайно')

i = 0
arr.append(arr[i])
arr.append(arr[i + 1])

u = None
print(arr)

while u != 1:
    sum_max = 0
    start_ind = 0
    while i < len_arr:
        temp_sum = arr[i] + arr[i + 1] + arr[i + 2]
        if temp_sum > sum_max:
            sum_max = temp_sum
            start_ind = i
            print(temp_sum)
        i += 1

    if start_ind < len_arr - 2:
        print(f'кусты №{start_ind + 1}, №{start_ind + 2}, №{start_ind + 3},')
    elif start_ind == len_arr - 2:
        print(f'кусты №{start_ind + 1}, №{start_ind + 2}, №{1},')
    elif start_ind == len_arr - 1:
        print(f'кусты №{start_ind + 1}, №{1}, №{2},')

    if start_ind < len_arr - 2:
        arr[start_ind] = 0
        arr[start_ind + 1] = 0
        arr[start_ind + 2] = 0
    elif start_ind == len_arr - 2:
        arr[start_ind] = 0
        arr[start_ind + 1] = 0
        arr[start_ind + 2] = 0
        arr[start_ind + 3] = 0
        arr[0] = 0
    elif start_ind == len_arr - 1:
        arr[start_ind] = 0
        arr[start_ind + 1] = 0
        arr[start_ind + 2] = 0
        arr[0] = 0
        arr[1] = 0

    if sum_max == 0:
        u = 1

print(arr)
