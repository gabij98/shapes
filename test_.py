from unittest import TestCase
import numpy as np

from rectangles import Rectangle, Square
from parallelograms import Parallelogram, Diamond
from triangle import Triangle
from circle import Circle

class TestRectangle(TestCase):

    def test_area(self):
        rect = Rectangle(8, 3)
        self.assertEqual(24, rect.area())

    def test_perimeter(self):
        rect = Rectangle(2, 5)
        self.assertEqual(14, rect.perimeter())

class TestSquare(TestCase):

    def test_area(self):
        sq = Square(4)
        self.assertEqual(16, sq.area())

    def test_perimeter(self):
        sq = Square(5)
        self.assertEqual(20, sq.perimeter())

class TestParallelogram(TestCase):

    def test_area(self):
        parall = Parallelogram(2, 5, 30)
        self.assertEqual(5, parall.area())

    def test_perimeter(self):
        parall = Parallelogram(2, 5, 30)
        self.assertEqual(14, parall.perimeter())

class TestDiamond(TestCase):

    def test_area(self):
        diam = Diamond(4, 30)
        self.assertEqual(8, diam.area())

    def test_perimeter(self):
        diam = Diamond(4, 45)
        self.assertEqual(16, diam.perimeter())

class TestTriangle(TestCase):

    def test_area(self):
        tria = Triangle(3, 4, 30)
        self.assertEqual(3, tria.area())

    def test_perimeter(self):
        tria = Triangle(3, 4, 90)
        self.assertEqual(12, tria.perimeter())

class TestCircle(TestCase):

    def test_area(self):
        cir = Circle(3)
        self.assertEqual(28.27, cir.area())

    def test_perimeter(self):
        cir = Circle(3)
        self.assertEqual(18.85, cir.perimeter())