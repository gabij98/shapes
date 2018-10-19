# coding: utf8
import rectangles
import parallelograms
import circle
import triangle
import pygame
import sys

pygame.init()

rectangle1 = rectangles.Rectangle(95, 50)
square1 = rectangles.Square(40)
parallelogram1 = parallelograms.Parallelogram(150, 190, 45)
diamond1 = parallelograms.Diamond(100, 60)
triangle1 = triangle.Triangle(100, 100, 60)
circle1 = circle.Circle(40)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)

    square1.draw()
    circle1.draw()
    diamond1.draw()
    parallelogram1.draw()
    rectangle1.draw()
    triangle1.draw()

    pygame.display.flip()