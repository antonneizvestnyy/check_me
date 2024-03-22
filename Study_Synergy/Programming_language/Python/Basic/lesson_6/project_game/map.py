#карта
# двумерный список
#хранение числа
# 0 - поле
# 1 - дерево
# 2 - река
# 3 - госпиталь
# 4 = апргрейд шоп
# 5 - огонь

from utils import randbool, randcell, randcell2


CELL_TYPES = '🟩🎄🌊🏥🏪🔥'
TREE_BONUS = 100
UPGRADE_COST = 5000
LIFE_COST = 5000

class Map:

    def __init__(self, weight, height):
        self.weight = weight
        self.height = height
        self.cells = [[0 for i in range(weight)] for j in range(height)]
        self.gen_forest(5, 10)
        #self.cells[1][1] = 1
        #self.cells[2][2] = 2
        self.gen_river(10)
        self.gen_upgrade_shop()
        self.gen_hospital()

    def check_pounds(self, x, y):
        if (x < 0) or (y < 0) or (x >= self.height) or (y >= self.weight):
            return False
        else:
            return True

    def print_map(self, helico, clouds):
        print('⬛' * (self.weight + 2))
        for ri in range(self.height):
            print('⬛', end='')
            for ci in range(self.weight): #перебираение клеточки
                cell = self.cells[ri][ci]
                if (clouds.cells[ri][ci] == 1):
                    print('⚪', end='') # белый кружок - облако
                elif (clouds.cells[ri][ci] == 2):
                    print('⭕️', end='') # красный кружок - гроза
                elif (helico.x == ri) and (helico.y == ci):
                    print('🚁', end='')
                elif (cell >= 0) and (cell < (len(CELL_TYPES))): # оптимизация кода
                    print(CELL_TYPES[cell], end='')
            print('⬛')
        print('⬛' * (self.weight + 2))

    def gen_river(self, l):
        rc = randcell(self.weight, self.height)
        rx, ry = rc[0], rc[1]
        self.cells[rx][ry] = 2
        while l > 0:
            rc2 = randcell2(rx, ry)
            rx2, ry2 = rc2[0], rc2[1]
            if (self.check_pounds(rx2, ry2)):
                self.cells[rx2][ry2] = 2
                rx, ry = rx2, ry2
                l -= 1

    def gen_forest(self, r, mxr):
        for ri in range(self.height):
            for ci in range(self.weight):
                if randbool(r, mxr):
                    self.cells[ri][ci] = 1

    def gen_tree(self):
        c = randcell(self.weight, self.height)
        cx, cy = c[0], c[1]
        if (self.cells[cx][cy] == 0):
            self.cells[cx][cy] = 1

    def gen_upgrade_shop(self):
        c = randcell(self.weight, self.height)
        cx, cy = c[0], c[1]
        self.cells[cx][cy] = 4

    def gen_hospital(self):
        c = randcell(self.weight, self.height)
        cx, cy = c[0], c[1]
        if self.cells[cx][cy] != 4:
            self.cells[cx][cy] = 3
        else:
            self.gen_hospital()

    def add_fire(self):
        c = randcell(self.weight, self.height)
        cx, cy = c[0], c[1]
        if self.cells[cx][cy] == 1:
            self.cells[cx][cy] = 5

    def update_fires(self):
        for ri in range(self.height):
            for ci in range(self.weight):
                cell = self.cells[ri][ci]
                if cell == 5:
                    self.cells[ri][ci] = 0
        for i in range(8):
            self.add_fire()

    def proc_heli(self, helico, clouds):
        c = self.cells[helico.x][helico.y]
        d = clouds.cells[helico.x][helico.y]
        #d = self.
        if (c == 2):
            helico.tank = helico.mxtank
        if (c == 5) and (helico.tank > 0):
            helico.tank -= 1
            helico.score += TREE_BONUS
            self.cells[helico.x][helico.y] = 1
        if (c == 4) and (helico.score >= UPGRADE_COST):
            helico.mxtank += 1
            helico.score -= UPGRADE_COST
        if (c == 3) and (helico.score >= LIFE_COST):
            helico.lives += 10
            helico.score -= LIFE_COST
        if (d == 2):
            helico.lives -= 1
            if (helico.lives == 0):
                helico.game_over()

        
    def export_data(self):
        return {'cells': self.cells}
        
    
    def import_data(self, data):
        self.cells = data['cells'] or [[0 for i in range(self.weight)] for j in range(self.height)]


        

