# coding: utf8
import rectangles
import parallelograms
import circle
import triangle
import pygame
import sys

pygame.init()

# creating objects
rectangle1 = rectangles.Rectangle(95, 130)
square1 = rectangles.Square(90)
parallelogram1 = parallelograms.Parallelogram(150, 100, 45)
diamond1 = parallelograms.Diamond(100, 60)
triangle1 = triangle.Triangle(100, 100, 110)
circle1 = circle.Circle(50)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)

    # drawing objects
    square1.draw()
    circle1.draw()
    diamond1.draw()
    parallelogram1.draw()
    rectangle1.draw()
    triangle1.draw()

    pygame.display.flip()