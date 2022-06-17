from testRectangle2 import Square
class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def get_area(self):
        return self.a * self.b
    def __eq__(self, other):
        return self.a == other.a and self.b == other.b


class Circle:
    def __init__(self, radius):
        self.radius = radius
    def get_area(self):
        return 3.14 * self.radius ** 2


class SquareFactory:
    @staticmethod
    def create_square(a):
        return Square(a)