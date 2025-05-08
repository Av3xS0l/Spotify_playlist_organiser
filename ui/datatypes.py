'''
Class that houses all utility datatypes
'''


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def __repr__(self):
        return f"Point({self.x}, {self.y})"
    
    def __add__(self, other:'Point'):
        return Point(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other:'Point'):
        return Point(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scalar: int):
        return Point(self.x * scalar, self.y * scalar)
    
    def __div__(self, scalar: int):
        return Point(self.x // scalar, self.y // scalar)