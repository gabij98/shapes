from shape import Shape
import numpy as np

class Circle(Shape):
    """
    Circle shape
    """

    r = None

    def __init__(self, r):
        super().__init__()
        self.r = r

    def area(self):
        return round(np.pi * self.r ** 2, 2)

    def perimeter(self):
        return round(2 * np.pi * self.r, 2)

    def __str__(self):
        return "Circle with a radius {0.r}".format(self)

    def __repr__(self):
        return "Circle({0.r})".format(self)