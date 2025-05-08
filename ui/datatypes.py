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
    

# A doubly linked list implementation of a queue
# Allows for O(1) enqueue and dequeue operations
class QueueNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.back = None
        self.size = 0
    
    def is_empty(self):
        return self.size == 0

    def enqueue(self, data):
        new_node = QueueNode(data)
        if self.is_empty():
            self.front = self.back = new_node
        else:
            self.back.next = new_node
            self.back = new_node
        self.size += 1
    
    def peek(self):
        current = self.front
        if current is None:
            raise Exception("Queue is empty")
        while current is not None:
            yield current.data
            current = current.next

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        data = self.front.data
        self.front = self.front.next
        self.size -= 1
        if self.is_empty():
            self.back = None
        return data