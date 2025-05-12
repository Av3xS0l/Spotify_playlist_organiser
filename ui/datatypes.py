'''
Class that houses all utility datatypes
'''


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