#вертолетик, сколько жизней

#знать координаты xy, очков, кол-во ведер
from utils import randcell
import os

class Helicopter:
    def __init__(self, weight, height):
        rc = randcell(weight, height)
        rx, ry = rc[0], rc[1]
        self.x = rx
        self.y = ry
        self.height = height
        self.weight = weight
        self.tank = 0 # сколько сейчас находится воды
        self.mxtank = 1 # вместительность бака
        self.score = 0
        self.lives = 20
        

    def move(self, dx, dy):
        nx, ny = dx + self.x, dy + self.y
        if (nx >= 0) or (ny >= 0) and (nx < self.height) and (ny < self.weight):
            self.x, self.y = nx, ny


    def print_stats(self):
        print('🚰 ', self.tank, '/', self.mxtank, sep='', end = ' | ')
        print('🏆', self.score, end=' | ')
        print('❤️ ', self.lives)

    
    def game_over(self):
        os.system('clear')
        print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
        print('----------------------------------')
        print('X   Game Over, Your Score is', self.score, '  X')
        print('----------------------------------')
        print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
        exit(0)

    def export_data(self):
        return {'score': self.score,
                'lives': self.lives,
                'x': self.x, 'y': self.y, 
                'tank': self.tank, 'mxtank': self.mxtank}
    
    def import_data(self, data):
        self.score = data['score'] or 0
        self.lives = data['lives'] or 3
        self.x = data['x'] or 0
        self.y = data['y'] or 0
        self.tank = data['tank'] or 0
        self.mxtank = data['mxtank'] or 1
        
        

