# coding: utf8


class Shape(object):
    """
    Base class for all shapes.
    """

    def area(self):
        """
        Abstract method returning area of a shape.
        """

    def perimeter(self):
        """
        Abstract method returning shape perimeter.
        """

    def summary(self):
        """
        Return summary of a shape.
        """
        return {
            'area': self.area(),
            'perimeter': self.perimeter()
        }

    def __str__(self):
        """
        Abstract method returning a name of a shape.
        """
        
    def __repr__(self):
        """
        Abstract method returning a programming represantation a shape.
        """