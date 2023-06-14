import csv

f = open('telephone_directory.csv', 'r', encoding='utf-8')
file = f.readlines()

for x in file:
    x.replace(" ", "")
    print(x)
    list_x = x.split(',')
    print(list_x)
    new_x = "".join(list_x)
    print(new_x)
    new_x.replace(" ", "")
    print(new_x)

f.close()



f.close()



    # text_poem = input('введите текст_ ')
    # result_text = text_poem.ljust(len(text_poem) + 1, ' ')
    # guide_ru = {"а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я"}
    # count_let = []
    # count = 0
    # for i in result_text:
    #     if (i.isspace()) != True:
    #         if i in guide_ru:
    #             count += 1
    #     else:
    #         count_let.append(count)
    #         count = 0
    # print(count_let)
    # sum_el = 0
    # for el in count_let:
    #     sum_el += el
    # if sum_el / len(count_let) == el:
    #     print('“Парам пам-пам”')
    # else:
    #     print('“Пам парам”')


# Иванов, Иван, 67777777
# Петров, Петр, 98888888
# Семенов, Семен, 89999999