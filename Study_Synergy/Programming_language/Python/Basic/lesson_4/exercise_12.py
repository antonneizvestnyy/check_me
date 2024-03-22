#Практика сортировки
#сортировка пузырьком

a = [1, 2, 5, 2, 9, 16, 15]
n = len(a)
for i in range(n):
    for j in range(n - 1 - i):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
print(*a)