#Задание 1

zero = 0
n = int(input('Введите число: '))
for i in range(n):
    if i % 2 == 0:
        zero += 1
print(zero)

#Задание 2

n = int(input('Введите число: '))
a = 0
for i in range(1, n + 1):
    if n % i == 0:
        a += 1
print(a)

# задание 3

a, b = map(int, input('Введите числа 2 числа: через пробел: ').split())
for i in range(a, b):
    if (i % 2 == 0) and (a <= b):
        print(i, end=' ')