# практика 1. множество

# n = int(input())
# used = set()
# for i in range(n):
#     promo = input()
#     if promo in used:  # проверка на промо
#         print('Промо такой уже был использовал')
#     else:
#         used.add(promo)
# print(len(used))

# практика 2. множество
# уникальные имена

# company1 = int(input())
# cl1 = []
# for i in range(company1):
#     name = input()
#     cl1.append(name)
# uc1 = set(cl1)
#
# company2 = int(input())
# cl2 = []
# for i in range(company2):
#     name = input()
#     cl2.append(name)
# uc2 = set(cl2)
#
# #print(uc1.union(uc2)) # объедение множеств
# print(uc1.intersection(uc2)) # разность множеств

#Задание 1

n = int(input('Кол-во элементов: '))
my_list = list(map(int, input('Введите элементы списка: ').split()))[:n]
set(my_list)
print('Кол-во элементов в списке: ', len(my_list))


#Задание 2

n = int(input('список1: '))
my_list = []
for i in range(n):
    numbers = int(input())
    my_list.append(numbers)
list_new = set(my_list)

n2 = int(input('список 2: '))
my_list2 = []
for i in range(n2):
    numbers = int(input())
    my_list2.append(numbers)
list_new2 = set(my_list2)

print('Кол-во одинаковых элементов: ', len(list_new.intersection(list_new2)))

#Задание 3

print('Введите последовательность чисел через пробел: ')
el = map(int, input().split())
my_list = set()
for i in el:
    if i in my_list:
        print('Yes')
    else:
        print('No')
        my_list.add(i)
print(my_list)
