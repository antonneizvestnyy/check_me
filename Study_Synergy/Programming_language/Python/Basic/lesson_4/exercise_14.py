#рекурсия
#задание 1

def recurs(x):
    if x == []:
        print('Конец списка')
    else:
        print(x.pop(0))
        recurs(x)

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

recurs(my_list)