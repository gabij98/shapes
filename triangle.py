from shape import Shape
import numpy as np
import pygame

game_screen = pygame.display.set_mode((800, 480))

class Triangle(Shape):
    """
    Triangle shape.
    """

    a = None
    b = None
    _alpha = None

    def __init__(self, a, b, alpha):
        super().__init__()
        self.a = a
        self.b = b
        self._alpha = np.pi / 180 * alpha

    @property
    def alpha(self):
        return round(self._alpha * 180 / np.pi, 1)

    def area(self):
        AB = np.array([self.a, 0])
        AC = np.array([self.b * np.cos(self._alpha), self.b * np.sin(self._alpha)])
        d = np.array([AB, AC])
        return round(1/2 * np.absolute(np.linalg.det(d)), 2)

    def perimeter(self):
        AB = np.array([self.a, 0])
        AC = np.array([self.b * np.cos(self._alpha), self.b * np.sin(self._alpha)])
        BC = np.subtract(AC, AB)
        return round(np.linalg.norm(AB) + np.linalg.norm(AC) + np.linalg.norm(BC), 2)

    def __str__(self):
        return "Triangle with sides {0.a} and {0.b} and angle between them {0.alpha}°".format(self)

    def __repr__(self):
        return "Triangle({0.a}, {0.b}, {0.alpha})".format(self)

    def draw(self):
        d = self.b * np.cos(self._alpha)
        h = self.b * np.sin(self._alpha)
        return pygame.draw.polygon(game_screen, (128, 128, 0), [[100, 370], [100 + d, 370 - h], [100 + self.a, 370]], 3)
