# #практическое занятие
#
# # def natural(a):
# #     if a % 2 == 0:
# #         return True
# #     # else:
# #     return False
# #
# # print(natural(5))
# #
# # def tmp(name):
# #     text = f'Hello, {name}'
# #     print(text)
# #
# # tmp('Mark')
# #
# # def year_visok(year):
# #     if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
# #         return True
# #     return False
# #
# # y = int(input())
# # print(year_visok(y))
#
# def nechet(n):
#     return (n % 2 != 0)
#
# def res(l):
#     for el in l:
#         if nechet(el):
#             print(el)
#
#
# tmp = [1, 2, 3, 4 , 6 , 7]
# res(tmp)
#
#
#
# #Задание 1

my_list = []
def fact(z):
    if z == 0:
        return 1
    return fact(z - 1) * z

n = int(input())

for i in range(n, 0, -1):
    my_list.append(fact(i))
print(my_list)



# #Задание 2
#
#
#
# def create():
#     pass
#
# def read():
#     pass
#
# def update():
#     pass
#
# def update():
#     pass
#
# def delete():
#     pass