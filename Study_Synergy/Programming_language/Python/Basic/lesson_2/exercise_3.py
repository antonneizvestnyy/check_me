#Задание 1

print('Привет, для регистрации в вет.клиники необходимо ответить на пару вопросов!\nВид питомца?')
breed = input()
print('Возраст питомца?')
age = int(input())
print('Кличка питомца?')
name = input()
#
# print(f'Это {breed} по кличке "{name}". Возраст: {age} год(а).')
print('Это ' + breed + ' по кличке ' + name + '.Возраст ' + str(age) + ' год(а).')


# Задание №2

a1 = 'Australopithecus'
a2 = 'Homo habilis'
a3 = 'Homo erectus'
a4 = 'Homo sapiens'
a5 = 'Homo neanderthalensis'
a6 = 'Homo sapiens sapiens'
print(a1, a2, a3, a4, a5, a6, sep='=>')

