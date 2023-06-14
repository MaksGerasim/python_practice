import csv


# f_search = open('telephone_directory.csv', 'r+', encoding='utf-8')
# file = csv.reader(f_search)
# data_search = {'Петров', 'Петр'}
#
# for x in file:
#     if (x[0] in data_search) and (x[1] in data_search):
#         print(f'номер телефона: {x}')
        #f_search.write(x)

f = open('telephone_directory.csv', 'r', encoding='utf-8')
file = f.readlines()
f.close()
f = open('telephone_directory.csv', 'w', encoding='utf-8')
data_search = {input('введите фамилию_'), input('введите имя_')}
for x in file:
    list_x = x.split(',')
    if (list_x[0] in data_search) and (list_x[1] in data_search):
        print(x)
        print('Ведите обновленные данные пользователя:')
        list_x[0] = input('фамилия: ') + ','
        list_x[1] = input('имя: ') + ','
        list_x[2] = input('номер телефона: ') + '\n'
        new_x = "".join(list_x)
        print(f'запись сохранена: {new_x}')
        f.write(new_x)
    else:
        f.write(x)
f.close()


