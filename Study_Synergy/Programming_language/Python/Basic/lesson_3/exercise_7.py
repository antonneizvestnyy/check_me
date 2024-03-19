#Задание 1

word = input('Введите слово: ')
revers = word[::-1]
if word == revers:
    print('Yes')
else:
    print('No')

#Задание 2

text = input('Привет, напиши строку')
if len(text) > 1000:
    print('строка больше 1000 символов!')
else:
    print(''.join(text.split()))