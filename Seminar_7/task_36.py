# Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца.
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть
# распечатаны. Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля). Примечание:
# бинарной операцией называется любая операция, у которой ровно два аргумента, как, например,
# у операции умножения.
# *Пример:*
# **Ввод:** `print_operation_table(lambda x, y: x * y) `
# **Вывод:**


num_rows = 3
num_columns = 3
result = 0
x = 0
y = 0
a = [[0 for x in range(num_columns)] for x in range(num_rows)]
print(a)
for i in range(len(a)):
    y = 0
    x += 1
    for j in range(len(a[i])):
        y += 1
        result = x * y
        a[i][j] = result
        print(a[i][j], end=" ")
    print()




# for i in range(len(a)):
#     for j in range(len(a[i])):
#         result += 1
#         a[i][j] = result
#         print(a[i][j], end=" ")
#     print()




