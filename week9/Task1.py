import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def circumference(self):
        return 2 * math.pi * self.radius


if __name__ == '__main__':
    circle = Circle(4)
    print('Area:', circle.area())
    print('Circumference:', circle.circumference())
