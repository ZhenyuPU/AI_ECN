
from file_pile import File
from file_pile import Pile

'''
Simuler une file avec deux piles
'''
class File_:
    def __init__(self):
        self.stack1 = Pile()
        self.stack2 = Pile()

    def enqueue(self, value):
        self.stack1.push(value)
    
    def dequeue(self):
        if self.stack1 is None and self.stack2 is None:
            return None
        for _ in range(len(self.stack1.contents)):
            self.stack2.push(self.stack1.pop_())
        return self.stack2.pop_()
    
    def is_empty(self):
        return (not self.stack1) and (not self.stack2)
        
'''
Simuler une pile avec deux files
'''

class Pile_:
    def __init__(self):
        self.queue1 = File()
        self.queue2 = File()
    
    def push(self, value):
        self.queue1.enqueue(value)
    
    def pop_(self):
        if not self.queue1.is_empty():
            while len(self.queue1.contents) > 1:
                self.queue2.enqueue(self.queue1.dequeue())
            return self.queue1.dequeue()
        elif not self.queue2.is_empty():
            while len(self.queue2.contents) > 1:
                self.queue1.enqueue(self.queue2.dequeue())
            return self.queue2.dequeue()