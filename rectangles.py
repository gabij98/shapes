# coding: utf8
from shape import Shape


class Rectangle(Shape):
    """
    Rectangular shape.
    """

    a = None
    b = None

    def __init__(self, a, b):
        super().__init__()
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b

    def perimeter(self):
        return 2 * (self.a + self.b)

    def __str__(self):
        return "Rectangle with dimensions {0.a} x {0.b}".format(self)

    def __repr__(self):
        return "Rectangle({0.a}, {0.b})".format(self)

class Square(Rectangle):
    """
    Square shape as a specific rectangle.
    """

    def __init__(self, a):
        super().__init__(a, a)

    def __str__(self):
        return "Square with side {0.a}".format(self)

    def __repr__(self):
        return "Square({0.a})".format(self)