#Задание 1
class Transport:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def Autobus(self):
        print(f'Название автомобиля: {self.name} Скорость: {self.max_speed} Пробег: {self.mileage}')


auto1 = Transport('Renaul Logan', 180, 12)
auto2 = Transport('BMW', 260, 56)

auto1.Autobus()
auto2.Autobus()

#Задание 2

class Transport:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage


class Autobus(Transport):

    def __init__(self, name, max_speed, mileage):
        super().__init__(name, max_speed, mileage)

    def seating_capacity(self, capacity=50):
        return f'Вместимость одного автобуса {self.name} {capacity} пассажиров'


auto3 = Autobus('Renaul Logan', 180, 12)
print(auto3.seating_capacity())


