# float, int и арифметические операции

'''
Задание1.
Пользователь вводит стороны прямоугольника, выведите его площадь и периметр. 
На вход программе могут подаваться как целые числа, так и вещественные
'''

s1, s2 = map(float, input().split())
s = s1 * s2
p = 2 * (s1 + s2)
print('Площадь: ' + str(s) + ' ' + 'Периметр: ' + str(p))
# print(f"Площадь: {s} Периметр: {p}")


'''
Задание2.
Дано пятизначное целое число. Напишите алгоритм, который возведёт количество десятков в степень количества единиц. Затем умножит это число на количество сотен. 
И делит получившееся число на разность количества десятков тысяч и количества тысяч
Например, есть число 46275
Необходимо возвести 7 (десятки) в степень 5 (единицы), 
умножить получившееся число на 2 (сотни), и разделить на разность между 4 (десятки тысяч) 
и 6 (тысячи) то есть (4-6)
В результате необходимо получить вещественное число. В нашем примере это будет: -16807.0
'''

number = int(input()) # 46275
ones = number % 10
tens = (number // 10) % 10
hundreds = (number // 100) % 10
thousands = (number // 1000) % 10
tens_of_thousands = (number // 10000) % 10

result1 = tens ** ones
print(result1)
result1 = result1 * hundreds # result1 *= hundreds 
print(result1)
result1 = result1 / (tens_of_thousands - thousands) # result1 /= (tens_of_thousands - thousands) 
print(result1)
