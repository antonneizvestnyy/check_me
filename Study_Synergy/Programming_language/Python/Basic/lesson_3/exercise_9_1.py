#Задание 1

my_list = set(list(map(int, input('Введите элементы списка: ').split())))
#test = set(my_list)
my_list2 = set(list(map(int, input('Введите элементы списка 2: ').split())))
#test2 = set(my_list2)
print('Кол-во различных элементов: ', my_list.intersection(my_list2))