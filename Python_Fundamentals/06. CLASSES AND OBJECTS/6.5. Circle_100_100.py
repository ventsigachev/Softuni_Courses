class Circle:
    __pi = 3.14

    def __init__(self, diameter):
        self.diameter = diameter
        self.radius = diameter / 2

    def calculate_circumference(self):
        return self.__pi * self.diameter

    def calculate_area(self):
        return self.__pi * self.radius * self.radius

    def calculate_area_of_sector(self, ang):
        return self.calculate_area() * ang / 360


circle = Circle(int(input()))
angle = int(input())

print(f"{circle.calculate_circumference():.2f}")
print(f"{circle.calculate_area():.2f}")
print(f"{circle.calculate_area_of_sector(angle):.2f}")
