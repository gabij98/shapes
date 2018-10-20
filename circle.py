from shape import Shape
import numpy as np
import pygame

game_screen = pygame.display.set_mode((800, 480))

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

    def draw(self):
        return pygame.draw.circle(game_screen, (0, 0, 255), (650, 100), self.r, 3)