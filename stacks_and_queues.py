# implement stack using collection.deque bcoz is more efficient than a dynamic array
from collections import deque
class Stack:
    def __init__(self):
        self.stack=deque()
    def push(self,val):
        self.stack.append(val)
    def pop(self):
        self.stack.pop()
    def peek(self):
        return self.stack[-1]
    def isempty(self):
        return len(self.stack)==0
    def size(self):
        return len(self.stack)
    def clear(self):
        self.stack=deque()
s=Stack()  
s.push(6)
s.push(7)
s.push(8)
s.push(9)
s.pop()
print(s.isempty())
print(list(s.stack))
