from testRectangle import Rectangle, Circle, SquareFactory

#from testRectangle2 import Square
rect_1 = Rectangle(3,4)
rect_2 = Rectangle(12,5)
rect_3 = Rectangle(4,3)

circle_1 = Circle(1)
circle_2 = Circle(2)


print(rect_1.get_area())
print(rect_2.get_area())
print(circle_1.get_area())
print(circle_2.get_area())
sc1 = SquareFactory.create_square(0)
print(sc1.area)
print(sc1.a)


