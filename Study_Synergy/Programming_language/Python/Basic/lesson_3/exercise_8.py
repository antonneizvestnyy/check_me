#Задание 1

n = int(input('Введите кол-во элементов в списке: '))
my_list = list(map(int, input('Введите значение в списке: ').split()))
my_list.reverse()
print(my_list)

#Задание 2

b = int(input('Введите кол-во элементов в списке: '))
my_list = list(map(int, input('Введите значение в списке: ').split()))
my_list.insert(0, my_list.pop())
print(my_list)

#Задание 3