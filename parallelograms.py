from shape import Shape
import numpy as np

class Parallelogram(Shape):
    """
    Parallelogram shape
    """

    a = None
    b = None
    _alpha = None

    def __init__(self, a, b, alpha):
        super().__init__()
        self.a = a
        self.b = b
        self._alpha = np.pi / 180 * alpha

        if self.alpha > 90 or self.alpha < 0:
            raise ValueError("The angle has to be in the interval (0°, 90°)")

    @property
    def alpha(self):
        return round(self._alpha * 180 / np.pi, 1)

    def area(self):
        return round(self.a * self.b * np.sin(self._alpha), 2)

    def perimeter(self):
        return 2 * (self.a + self.b)

    def __str__(self):
        return "Parallelogram with dimensions {0.a} x {0.b} and angle {0.alpha}°".format(self)

    def __repr__(self):
        return "Parallelogram({0.a}, {0.b}, {0.alpha})".format(self)

class Diamond(Parallelogram):
    """
    Diamond shape as a specific parallelogram.
    """

    def __init__(self, a, alpha):
        super().__init__(a, a, alpha)

    def __str__(self):
        return "Diamond with side {0.a} and angle {0.alpha}°".format(self)

    def __repr__(self):
        return "Diamond({0.a}, {0.alpha})".format(self)