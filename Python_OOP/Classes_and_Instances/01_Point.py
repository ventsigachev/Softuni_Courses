from math import sqrt


class Point:
    def __init__(self, x: int, y: int):
        self.x = int(x)
        self.y = int(y)

    def set_x(self, new_x: int):
        self.x = int(new_x)

    def set_y(self, new_y: int):
        self.y = int(new_y)

    def distance(self, o_x, o_y):
        distance = sqrt((self.x - o_x) ** 2 + (self.y - o_y) ** 2)
        return distance


p = Point(2, 4)
p.set_x(3)
p.set_y(5)
print(p.distance(10, 2))
