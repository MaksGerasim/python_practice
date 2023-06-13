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
    with open(file_csv, 'a', newline='', encoding='utf-8') as f_object:
        writer_object = writer(f_object)
        writer_object.writerow(list_data)
        f_object.close()





new_rows = create_new_rows()
writ_rows_guide(file_csv='telephone_directory.csv', list_data=new_rows)
print_guide(file_csv='telephone_directory.csv',)
