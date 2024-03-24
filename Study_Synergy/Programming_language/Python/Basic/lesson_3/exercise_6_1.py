# Задание 3

a, b = map(int, input('Введите числа 2 числа: через пробел: ').split())
for i in range(a, b + 1):  # включительно + 1
    if (i % 2 == 0) and (a <= b):
        print(i, end=' ')
