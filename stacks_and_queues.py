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

# exercise: reverse a string using a stack
class Stack2:
    def __init__(self):
        self.stack=deque()
    def push(self,val):
        for x in val:
            self.stack.append(x)
    def reverse(self):
        rev=""
        for x in list(self.stack):
            rev+=self.stack.pop()
        print("Reversed form is :"+rev)
s2=Stack2()
s2.push("my name is Dedan")
s2.reverse()

# exercise to check whether paranthesis are balanced
class Stack2:
    def __init__(self):
        self.stack=deque()
    def balanced(self,val):
        val=str(val)
        for x in val:
            if x=="[":
                self.stack.append(x)
            if x=="]":
                try:
                    self.stack.pop()
                except IndexError:
                    return False
            if x=="{":
                self.stack.append(x)
            if x=="}":
                try:
                    self.stack.pop()
                except IndexError:
                    return False
            if x=="(":
                self.stack.append(x)
            if x==")":
                try:
                    self.stack.pop()
                except IndexError:
                    return False
        if len(list(self.stack))!=0:
                return False
        return True

s3=Stack2()
print(s3.balanced("(56)67(()){}[]"))