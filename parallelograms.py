from shape import Shape
import numpy as np
import pygame

game_screen = pygame.display.set_mode((800, 480))

class Parallelogram(Shape):
    """
    Parallelogram shape.
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

    def draw(self):
        h = self.b * np.sin(self._alpha)
        d = self.b * np.cos(self._alpha)
        return pygame.draw.polygon(game_screen, (75, 0, 130), [[300, 370], [300+d, 370-h], [300+d+self.a, 370-h], [300+self.a, 370]], 3)

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

    def draw(self):
        e = 2 * self.a * np.cos(self._alpha/2)
        f = 2 * self.a * np.sin(self._alpha/2)
        return pygame.draw.polygon(game_screen, (255, 0, 0), [[50, 100], [50+(e/2), 100-(f/2)], [50+e, 100], [50+(e/2), 100+(f/2)]], 3)