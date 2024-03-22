# #матрица
# практика 1
# def test(x):
#     for i in x:
#         print(i)
#         #print(*i) - без скобок
#
#
# n = int(input())
# tmp = []
# for i in range(n):
#     a = list(map(int, input().split()))
#     tmp.append(a)
# test(tmp)

#Задание 1
import random
def matrix(x):
    for i in x:
        print(i)
        #print(*i) # без скобок

print('matrix1\n')
matrix1 = [[random.randint(-10, 10) for i in range(10)] for i in range(10)]
matrix(matrix1)

print('\nmatrix2\n')
matrix2 = [[random.randint(-10, 10) for i in range(10)] for i in range(10)]
matrix(matrix2)

print('\nmatrix3\n')
matrix3 = [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]
matrix(matrix3)