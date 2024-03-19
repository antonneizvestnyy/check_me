#словари
#практика 1

# bank = dict()
# n = int(input('Кол-во запросов в банк: '))
# for i in range(n):
#     req = input()
#     if req == 'create':
#         k = input()
#         bank[k] = 0
#     elif req == 'add':
#         k = input()
#         amount = int(input())
#         if k in bank.keys():
#             bank[k] += amount
#         else:
#             print('sorry, ho such key')
#     else:
#         print('sorry, bad request')
# print(bank)
#
# #практика 2
#
# tmp = {'k1': 1, 'k2': 2, 'k3': 3}
# for v in tmp.values():
#     print(v)

#Задание 1

pets = {}
pets2 = {}

while True:
    k = input('Введите имя питомца: ')

    if k == '':
        break
    else:
        k1 = input('Вид питомца: ')
        k2 = int(input('Возраст питомца: '))
        year_case = ''
            # Проверка
        if (k2 % 10 == 1) and (k2 != 11) and (k2 % 100 != 11):
            year_case = 'год'
        elif (1 < k2 % 10 <= 4) and (k2 != 12) and (k2 != 13) and (k2 != 14):
            year_case = 'года'
        else:
            year_case = 'лет'

        k3 = input('Имя владельца:  ')



        pets2 = {'Вид питомца:': k1, 'Возраст питомца:': k2, 'Имя владельца:': k3}
        pets[k] = pets2
        #print(pets)

    print(f'Это {k1} по кличке "{k}". Возраст питомца:{k2} {year_case}. Имя владельца:{k3}')



#Задание 2

new_dict = {}

for n in range(10, -6, -1):

    new_dict[n] = n ** n

print(new_dict)




