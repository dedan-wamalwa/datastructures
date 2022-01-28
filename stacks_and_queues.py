# implement stack using collection.deque bcoz is more efficient than a dynamic array
from collections import deque
# stack has pop and push operations
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

# queues
# has a front and rear
# operations include enque and deque
class Queue:
    def __init__(self):
        self.que=deque()
    def enqueue(self,value):
        self.que.appendleft(value)
    def deque_(self):
        self.que.pop()
    def isempty(self):
        if len(list(self.que))==0:
            return True
        return False
    def display(self):
        print(list(self.que))
q1=Queue()
q1.enqueue(5)
q1.enqueue(6)
q1.enqueue(7)
q1.enqueue(8)
q1.display()
q1.deque_()
q1.deque_()
q1.deque_()
q1.deque_()
q1.display()
print(q1.isempty())
