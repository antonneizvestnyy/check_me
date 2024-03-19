# Задание 1

number = int(input('Введите целое число: '))

a = 'Положительное четное число'
b = 'Положительное нечетное число'
c = 'Отрицательное четное число'
d = 'Отрицательное нечетное число'
e = 'Число не является четным'
f = 'Нулевое число'


if not number == 0:
    if number % 2 == 0:
        if number >= 0:
            print(a)
        else:
            print(c)
    else:
        print(e)
        if number >= 0:
            print(b)
        else:
            print(d)
else:
    print(f)

# Задание 2

word = input('Добрый день!\nВведите слово: ').lower()
vowels = 0
consonants = 0
for char in word:
    if char in 'aeiou':
        vowels += 1
    elif char in 'bcdfghjklmnpqrstvwxyz':
        consonants += 1
    else:
        print(False)
print('Гласных:', vowels, 'Согласных: ', consonants)

#задание 3

print('Введите сумму первоначально взноса!')
invest = int(input('Сумма: '))

print('Привет Майкл и Иван, вложимся в стартап?')
Mike = input('Майкл: ')
Ivan = input('Иван: ')

if (Mike in 'д') and (Ivan in 'д'):
    print(2)
    mike, ivan, = map(int, input('Введите сумму вложений, по очереди: ').split())
    sum_cash = mike + ivan
    if sum_cash >= invest:
        print('Вложились оба!')
    else:
        print('не хватило!')
elif (Mike not in 'д') or (Ivan in 'д'):
    print(1)
    print('Только Иван')
    ivan = int(input('Введите сумму: '))
    if ivan >= invest:
        print('Иван вложился')
    else:
        print('Не хватило!')
elif (Mike in 'д') or (Ivan not in 'д'):
    print(1)
    print('Только Майкл')
    mike = int(input('Введите сумму: '))
    if mike >= invest:
        print('Майкл вложился')
    else:
        print('Не хватило!')
else:
    print(0)





























