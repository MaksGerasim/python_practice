# Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать
# функционал для изменения и удаления данных

import csv
def print_guide(file_csv):
    print_f = open(file_csv, 'r', encoding='utf-8')
    print(print_f.read())
    print_f.close()

def create_new_rows():
    new_rows = []
    new_rows.append(input('введите фамилию_'))
    new_rows.append(input('введите имя_'))
    new_rows.append(input('введите номер телефона_'))
    return (new_rows)

def writ_rows_guide(file_csv, list_data):
    from csv import writer
    with open(file_csv, 'a', newline='', encoding='utf-8') as f:
        writer_object = writer(f)
        writer_object.writerow(list_data)
        f.close()

def telephone_number_search(file_csv):
    f = open(file_csv, 'r', encoding='utf-8')
    file = csv.reader(f)
    data_search = {input('введите фамилию_'), input('введите имя_')}
    for x in file:
        if (x[0] in data_search) and (x[1] in data_search):
            print(f'номер телефона: {x[2]}  - {x[0]} {x[1]}')

def delete_rows_guide(file_csv):
    f = open(file_csv, 'r', encoding='utf-8')
    file = f.readlines()
    f.close()
    f = open(file_csv, 'w', encoding='utf-8')
    data_search = {input('введите фамилию_'), input('введите имя_')}
    for x in file:
        list_x = x.split(',')
        if (list_x[0] not in data_search) and (list_x[1] not in data_search):
            f.write(x)
        else:
            print(f'запись (_{list_x[0]}, {list_x[1]}_) удалена')
    f.close()

def change_rows(file_csv):
    f = open(file_csv, 'r', encoding='utf-8')
    file = f.readlines()
    f.close()
    f = open(file_csv, 'w', encoding='utf-8')
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

new_rows = create_new_rows()
writ_rows_guide(file_csv='telephone_directory.csv', list_data=new_rows)
print_guide(file_csv='telephone_directory.csv')
#telephone_number_search(file_csv='telephone_directory.csv')
delete_rows_guide('telephone_directory.csv')
# print_guide(file_csv='telephone_directory.csv')