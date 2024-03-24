# переделал домашнее задание
# Задание 2

word = input('Введите слово с гласными буквами: ')

e = word.count('e')
a = word.count('a')
i = word.count('i')
y = word.count('y')
u = word.count('u')
o = word.count('o')

word_count_low = e + a + y + i + u + o

print('Всего гласных', word_count_low)
print('Всего согласных', len(word) - word_count_low)

if e == 0:
    print(False)
else:
    print('e = ', e)
if a == 0:
    print(False)
else:
    print('a = ', a)
if i == 0:
    print(False)
else:
    print('i = ', i)
if y == 0:
    print(False)
else:
    print('y = ', y)
if u == 0:
    print(False)
else:
    print('u = ', u)
if o == 0:
    print(False)
else:
    print('o = ', o)

# Задание 3

amount = int(input('Минимальная сумма инвестиций - '))
mike = int(input('Cколько долларов у Майкла - '))
ivan = int(input('Сколько долларов у Ивана - '))

if (mike >= amount) and (ivan >= amount):
    print(2)
elif (mike >= amount) and (ivan <= amount):
    print('Mike')
elif (mike <= amount) and (ivan >= amount):
    print('Ivan')
elif (mike <= amount) and (ivan <= amount) and ((mike + ivan) >= amount):
    print(1)
elif (mike <= amount) and (ivan <= amount) and ((mike + ivan) <= amount):
    print(0)
else:
    print('bye')
