#Циклы for and while


"""

---- Для себя -----

a = int(input("Введите целое число N: "))
for i in range(a):
    print(i)

"""


"""
Задание №1

Сначала вводится число N, затем вводится ровно N целых чисел. 
Подсчитайте, сколько из них равны нулю, и выведите это количество.

"""

b = int(input("Введите целое число: "))
c = 0
for i in range(b): # идут числа до введенного числа. автоматически проставляется +1
    if i % 2 == 0: #если делится то выполняем условие
        c += 1 # прибавляем кол-во сколько раз делится 
        #print(i)
print("Сколько раз из чисел N равно 0: ", c)


"""
Задание №2

Вводится натуральное число X. 
Подсчитайте количество натуральных делителей числа X (включая 1 и само число). 
x ≤ 2e9 (2 миллиарда)

"""

x = int(input("Введите натуральное число: "))

if x == 1:
    c = 1
else:
    c = 2
    for i in range(2, int((x/2) + 1)):
        if x % i == 0:
            c += 1

print(c)


"""
Задание №3

Вводятся целые числа A и B. Гарантируется, что A ≤ B. 
Выведите все четные числа на заданном отрезке через пробел.

"""