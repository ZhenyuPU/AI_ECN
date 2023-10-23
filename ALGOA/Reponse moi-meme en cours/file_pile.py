'''
file:

enqueue

dequeue

is_empty
'''
class File:
    def __init__(self):
        self.contents = []
    
    def enqueue(self, l):
        self.contents.append(l)
    
    def dequeue(self):
        x = self.contents[0]
        self.contents.pop(0)
        return x
    
    def is_empty(self) -> bool:
        return not self.contents
    
'''
pile:

push 

pop_

top

is_empty
'''

class Pile:
    def __init__(self):
        self.contents = []

    def push_(self, value):
        self.contents.append(value)
    
    def pop_(self):
        pos = len(self.contents) - 1
        x = self.contents[pos]
        self.contents.pop(pos)
        return x
    
    def top(self):
        return self.contents[len(self.contents) - 1]
    
    def is_empty(self):
        return not self.contents