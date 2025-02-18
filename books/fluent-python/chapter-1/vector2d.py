"""
Simple class demonstrating special methods for numeric types
It lacks proper error handling especially for addition and multiplication
"""

import math

class Vector:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Vector({self.x!r}, {self.y!r})'

    def __abs__(self):
        """
        >>> v = Vector(3, 4)
        >>> abs(v)
        5.0
        """
        return math.hypot(self.x, self. y)

    def __add__(self, other):
        """
        >>> v1, v2 = Vector(2, 4), Vector(2, 1)
        >>> v1 + v2
        Vector(4, 5)
        """
        x, y = self.x+other.x, self.y+other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        """
        >>> v = Vector(2, 5)
        >>> v*3
        Vector(6, 15)
        """
        return Vector(self.x*scalar, self.y*scalar)

    def __rmul__(self, scalar):
        """
        >>> v = Vector(2, 5)
        >>> 3*v
        Vector(6, 15)
        """
        return Vector(self.x*scalar, self.y*scalar)

    def __bool__(self):
        return bool(self.x or self.y)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
