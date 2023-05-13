import math


class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f"Vector ({self.x!r})"

    def __abs__(self):
        return math.hypot

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, number2):
        x = self.x + other.x
        y = self.y + other.y
        return Vector()

    def __mul__(self):
        return Vecotr(self.x * scalar, self.y * )
