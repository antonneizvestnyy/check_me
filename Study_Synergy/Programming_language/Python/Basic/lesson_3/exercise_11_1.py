#задание 1

def fact(num):
    if num == 1:
        return num
    else:
        return num * fact(num - 1)

# n = int(input('напиши число: '))
n = 3
res = fact(n)
print(res)

test = []
number1 = res
for i in range(1, number1):
    number1 *= i
    test.append(number1)
test.reverse()
print(test)

