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
    


class CommandQueue:
    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.queue = [None]*maxSize
        self.next = 0
        self.size = 0

    def add(self, item):
        if self.size < self.maxSize:
            self.size += 1
        self.queue[self.next] = item
        self.next = (self.next + 1) % self.maxSize
    
    def get(self):
        if self.size < self.maxSize:
            return [None]*(self.maxSize-self.size) + self.queue[:self.next]
        return self.queue[self.next:] + self.queue[:self.next]