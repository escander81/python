dictionary = {}
while True:
    print('Введите название Товара, затем введите его значение. Если пустой ввод - выход.')
    goods = input('Название Товара: ')
    if goods=='':
        break

    description = input('Введите описание товара: ')
    dictionary[goods] = description
    # return dictionary

print(dictionary)
# d.setdefault(3, 3)
# for x in d:
# print(x)
#   if ...  and number !='5