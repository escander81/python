my_list = list(input('введите цифры: '))
for i in range (1, len(my_list), 2):
    my_list[i-1], my_list[i] = my_list[i], my_list[i-1]
print(my_list)
# newlist = my_list.reverse(2)






# num = input('какое количество данных вы хотите ввести? ')
# digits = 0
# num_new = []
# print(True if num.isdigit() else input('вы некорретно ввели цифру, попробуйте еще раз. какое количество данных вы хотите ввести? '))
#
# for i in range (0, num):
#     digits.append(num_new)
#
# while True:
#     step += 1

# a = num if num.isdigit else input('вы некорретно ввели цифру, попробуйте еще раз. какое количество данных вы хотите ввести? ')
# print (a)

# a = []
# list = ()
# # b = int(input('введите элемент: '))
# while True:
#     b = int(input('введите элемент: '))
#     list = a.append(list)
# else
#     break
# print(b)