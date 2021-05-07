my_list = [1, 2, 3, 3, 5, 7, 9]
new_element = int(input('please input new element: '))
i = 0
for n in my_list:
    if new_element >= n:
        i += 1
my_list.insert(i, float(new_element))
print(my_list)


# if element in my_list(len()):
#     for i in my_list.items():
#         my_list.append(i, element)
#         print(my_list)

# for i in range(len(my_list)):
#     my_list.insert(element, i)
#     print(my_list)


# for element in my_list:
#     if element


# for item in my_list:
#     print(item)

# if month in sum(seasons.values(), []):
#     for i in seasons.items():
#         if month in i[1]:
#             print(i[0])