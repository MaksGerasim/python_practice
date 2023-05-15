# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой,
# а некоторые – гербом. Определите минимальное число монеток, которые нужно
# перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть

coins_list = []
quant_coins = int(input('введите число монет _'))
for i in range(quant_coins):
    n = int(input("введите сторону монеты 1 или 0 _"))
    coins_list.append(n)
print(coins_list)
side_0 = 0
side_1 = 0
for i in coins_list:
    if i == 0:
        side_0 += 1
    elif i == 1:
        side_1 += 1
    else:
        print('Error')
        quit()
if side_0 != side_1:
    if side_0 < side_1:
        print(f'минимальное число монет = {side_0}')
    else:
        print(f'минимальное число монет = {side_1}')
else:
    print(f'минимальное число монет = {side_0}')
