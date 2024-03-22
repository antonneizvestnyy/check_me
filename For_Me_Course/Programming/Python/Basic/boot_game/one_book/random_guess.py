# игра угадай число!

import random

guesTaken = 0

print('Привет, как тебя зовут!?')

myName = input()

number = random.randint(1,20)

print ('Загадываю число ' + myName + ' от 1 до 20!')

for guesTaken in range(6):
    print('Попробуй угадать!')
    guess = input()
    guess = int(guess)

    if guess < number:
        print('Твое число слишком маленькое!')

    if guess > number:
        print('Твое число слишком большое!')

    if guess == number:
        break
    
if guess == number:
    guesTaken = str(guesTaken + 1)
    print('Отлично, ' + myName + '! Ты справился(ась) за ' + guesTaken + ' попытки(ок)!')

if guess != number:
    number = str(number)
    print('Увы, не получилось, я загадал число ' + number + '.')
