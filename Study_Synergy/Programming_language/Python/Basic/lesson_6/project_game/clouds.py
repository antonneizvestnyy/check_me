from map import Map
from utils import randbool

class Clouds:
    def __init__(self, weight, height):
        self.weight = weight
        self.height = height
        self.cells = [[0 for i in range(weight)] for j in range(height)]
    
    def update(self, r = 1, mxr = 20, g = 1, mxg = 10):
        for i in range(self.height):
            for j in range(self.weight):
                if randbool(r, mxr):
                    self.cells[i][j] = 1
                    if randbool(g, mxg):
                        self.cells[i][j] = 2
                else:
                    self.cells[i][j] = 0

    def export_data(self):
        return {'cells': self.cells}
    
    def import_data(self, data):
        self.cells = data['cells'] or [[0 for i in range(self.weight)] for j in range(self.height)]