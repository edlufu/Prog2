"""  VA

Student: Edvin Lundberg
Mail: edvin.lundberg@gmail.com
Reviewed by: Sven-Erik Ekström
Date reviewed: 16/05
"""

import math


class Vector:
    """Not extremly useful anymore but why bother removing"""

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
        self.values = (self.x, self.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __iter__(self):
        for value in self.values:
            yield value

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return Vector(x, y)

    def __mul__(self, other):
        """Handles multiplication between vectors, dot product,
        and between vectors and scalars"""

        if isinstance(other, Vector):
            return self.x * other.x + self.y + other.y
        elif isinstance(other, (int, float)):
            x = self.x * other
            y = self.y * other
            return Vector(x, y)

    def __rmul__(self, other):
        """Allows vector multiplication on right side of operator"""
        return self.__mul__(other)

    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2)
