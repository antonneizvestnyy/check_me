#задание 1

class Kassa():

    def __init__(self, get_buy):
        self.get_buy = get_buy

    def top_up(self, x):
        self.get_buy += x
        return f"в кассе {x}"

    def count_1000(self):
        return self.get_buy // 1000

    def take_away(self, x):
        if x <= self.get_buy:
            self.get_buy -= x
        else:
            print(f'не достаточно денег')

client=Kassa(100)

print(client.top_up(100))
print(client.count_1000())
client.take_away(1000)

#задание 2

class Turtle:

    def __init__(self, x, y, s):
        self.x = x
        self.y = y
        self.s = s

    def go_up(self):
        self.y += self.s
        return self.y

    def go_down(self):
        self.y -= self.s
        return self.y

    def go_left(self):
        self.x -= self.s
        return self.x

    def go_right(self):
        self.x += self.s
        return self.y

    def evolve(self):
        self.s += 1
        return self.s

    def degrade(self):
        if self.s <= 0:
            print('s = 0')
            return
        self.s -= 1
        return self.s

    def count_moves(self, x2, y2):
        return self.x - x2, self.y - y2


r = Turtle(2, 6, 34)

print(r.go_up())
print(r.go_down())
print(r.go_left())
print(r.go_right())
print(r.evolve())
print(r.degrade())
print(r.count_moves(12,10))


