# print('Задание№1')

# street_name = input('введите название улицы: ')
# block_number = int(input('введите номер дома: '))
# print('ваш адрес: ', street_name, block_number)
#
# salary = int(input('какой размер вашей текущей зарплаты: '))
# new_salary = int(input('какой размер вашей желаемой зарплаты: '))
# diff = new_salary - salary
# print("вам надо зарабатывать на ", diff, "больше")

print('Задание№2')
seconds = int(input('сколько секунд вам требуется перевести: '))
hh = seconds // 3600
mm = hh % 60
ss = seconds - seconds%hh%mm
# mm = seconds // 3600 % 60
# ss = seconds/3600/60
print('вы запросили: ', hh, 'часов', mm, 'минут', ss, 'секунд')
