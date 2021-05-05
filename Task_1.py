print('Задание № 1')

street_name = input('введите название улицы: ')
block_number = int(input('введите номер дома: '))
print('вы ищите адрес: ', street_name, block_number)

salary = int(input('какой размер вашей текущей зарплаты: '))
new_salary = int(input('какой размер вашей желаемой зарплаты: '))
diff = new_salary - salary
dif = new_salary / salary
print("вам надо зарабатывать на ", diff, "больше.")
print('хотел вывести расчет сколько нужен рост в процентах и не смог разобраться как это сделать')

print('Задание № 2')
seconds = int(input('сколько секунд вам требуется перевести: '))
hh = seconds // 3600
mm = seconds // 60 - hh * 60
ss = seconds % 60
# print('вы запросили: ', hh, 'часов', mm, 'минут', ss, 'секунд')
print('вы запросили ' f"{hh:02}часов:{mm:02}минут:{ss:02}секунд")

print('Задание № 3')
#
a = input('введите число "n" > 0, все остальное мы сделаем за вас: ')

# q = int(a) + int(a + a) + int(a + a + a)
# print(q)
print(f"{a} + {a + a} + {a + a + a} = {int(a) + int(a + a) + int(a + a + a)}")


print('Задание № 4')
num = int(input('введите целое положительное число, а мы найдем наибольшую цифру: '))
big_num = 0

while num > 0:
    i = num % 10
    if i > big_num:
            big_num = i
    num = num // 10
print(f"цифра {big_num} самая большая в заданном числе {num}")

print('Задание № 5')
a = int(input('укажите размер выручки: '))
b = int(input('укажите размер издержек: '))
c = int(input('укажите число сотрудников: '))
result = a - b
if result > 0:
    print(f"Вы успешны. компания показала результат {result}")
    print(f"Рентабельность составила {100 * result/a:.2f}%")
    print(f"каждый сотрудник может получить {result / c:.2f}")
elif result < 0:
    print(f"могли бы и лучше. ваш результат минусовой и равен {-result}")
else:
    print('отработали в ноль')

print('Задание № 6')
while True:
    day = 1
    a = float(input('сколько км бегаешь сейчас? '))
    b = float(input('сколько км хочешь пробегать? '))
    if a<=0 or b <0:
        print("укажите верное значение")
    else:
        while a < b:
            a += a * 0.1
            day += 1
        print(f"вам требуется {day} дней")
        break


