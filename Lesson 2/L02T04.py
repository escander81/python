string = input('введите несколько слов: ')

revised_string = string.split()
# revised_string = revised_string[:10]

print(revised_string)
for i, shortened in enumerate(revised_string, 1):

    print(i, shortened[:10])

