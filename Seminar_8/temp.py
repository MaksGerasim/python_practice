import csv

f = open('telephone_directory.csv', 'r', encoding='utf-8')
file = f.readlines()
print(file)
f.close()
f = open('telephone_directory.csv', 'w', encoding='utf-8')
data_search = {'Петров', 'Петр'}
for x in file:
    f.write(x)
    print(x)


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


# Ивано, Иван, 67777777
# Петров, Петр, 98888888
# Семенов, Семен, 89999999