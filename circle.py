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
        return 2 * np.pi * self.r