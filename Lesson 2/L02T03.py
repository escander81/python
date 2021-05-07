seasons = {'winter': [1, 2, 12],
           'spring': [3, 4, 5],
           'summer': [6, 7, 8],
           'autumn': [9, 10, 11]}

for key in seasons:
    print(key, seasons[key])

month = int(input('введите порядковый номер месяца: '))
if month in sum(seasons.values(), []):
    for i in seasons.items():
        if month in i[1]:
            print(i[0])

