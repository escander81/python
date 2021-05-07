print('L02T01')
list = ('text', (5+6j), 2, 2.2, True, {2: "two"}, None, (2,3,4), ['two', 'three', 'four'], {2,3,4}, frozenset(), b"text", bytearray((b"text")) )
for i, v in enumerate (list):
    print(i, type(v))




# my_list = list()
# print(my_list)
# new_list = my_list.append(int(input('введите что нибудь: ')))
# print(new_list)

# my_list = [] # создал пустой список
# new_list = int(input('введите что-нибудь: '))
# for i in range (new_list):
#     add_element = int(input('введите еще что-нибудь: '))
#     my_list.append(add_element)
#
# print(type(my_list))