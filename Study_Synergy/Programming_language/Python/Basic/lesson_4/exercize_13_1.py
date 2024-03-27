import random

print('Введите координаты x,y: ')
x = int(input())
y = int(input())

matrix_1=[[random.randint(1, 11) for j in range(x)] for i in range(y)]
print('Матрица 1: ')

for i in range(x):
    print(matrix_1[i])

matrix_2 = [[ random.randint(1, 11) for j in range(x)] for i in range(y)]
print('Матрица 2: ')

for i in range(y):
    print(matrix_2[i])

result = [[matrix_1[i][j] + matrix_2[i][j] for j in range(len(matrix_1[0]))] for i in range(len(matrix_1))]

print("Результат сложения двух матриц: ")
for i in result:
    print(i)