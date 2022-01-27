# implement a linked list
'''class Node():
    def __init__(self,data,next):
        self.data=data
        self.next=next
class List():
    def __init__(self):
        self.Head=None
    def addfront(self,data):
        self.Head=Node(data,self.Head)
    def addrear(self,data):
        if self.Head==None:
            self.Head=Node(data,None)
        else:
            itr=self.Head
            while itr:
                if itr.next==None:
                    itr.next=Node(data,None)
                    break
                itr=itr.next
    def addatpos(self,pos,data):
        if pos==0:
            self.addfront(data)
        else:
            itr=self.Head
            index=0
            while itr:
                if index==pos-1:
                    new=Node(data,itr.next)
                    itr.next=new
                    break
                index+=1
                itr=itr.next
    def removeatpos(self,pos):
        if pos==0:
            self.removehead()
        else:
            itr=self.Head
            index=0
            while itr:
                if index==pos-1:
                    data=itr.next.data
                    itr.next=itr.next.next
                    print(data," removed at position ",pos)
                    break
                index+=1
                itr=itr.next
    def removehead(self):
        self.Head=self.Head.next
    def removeRear(self):
        itr=self.Head
        while itr:
            if itr.next.next==None:
                itr.next=None
                break
            itr=itr.next
    def size(self):
        count=0
        itr=self.Head
        while itr:
            count+=1
            itr=itr.next
        print("size of the list is ",count)
    def prints(self):
        if self.Head==None:
            print("List is empty!")
        else:
            lls=""
            itr=self.Head
            while itr:
                lls+=str(itr.data)+"-->"
                itr=itr.next
            print(lls)
ll1=List()
# ll1.addfront(5)
# ll1.addfront(4)
# ll1.addfront(3)
# ll1.addrear(6)
# ll1.addrear(7)
for i in range(1,6):
    ll1.addrear(i)
ll1.prints()
# ll1.removehead()
# ll1.prints()
# ll1.removeRear()
# ll1.prints()
ll1.addatpos(5,3.5)
ll1.prints()
ll1.removeatpos(2)
ll1.prints()
ll1.size()

# implement stack and queue using linked list
# stack
# top , pop and push
class Node2():
    def __init__(self,data,next):
        self.data=data
        self.next=next
class List2():
    top=-1
    def __init__(self):
        self.Head=None
    def isempty(self):
        if self.top<0:
            print("stack is empty!")
        else:
            itr=self.Head
            stack=""
            while itr:
                stack+= str(itr.data)+", "
                itr=itr.next
            print(stack)
    def push(self,data):
        self.Head=Node2(data,self.Head)
        self.top+=1
    def pop(self):
        if self.top<0:
            print("Stack is empty!")
        else:
            self.Head=self.Head.next
            self.top-=1
    def display(self):
        self.isempty()
    def clearstack(self):
        self.Head=None
ll2=List2()
ll2.isempty()
ll2.push(5)
ll2.push(4)
ll2.push(3)
ll2.display()
ll2.pop()
ll2.pop()
ll2.pop()
ll2.display()'''

# queue using a linked list
# front,rear,enque and deque

class Node3():
    def __init__(self,data,next):
        self.data=data
        self.next=next
class List():
    def __init__(self):
        self.Head=None
    def isempty(self):
        if self.Head==None:
            print("queue is empty!")
        else:
            itr=self.Head
            queue=""
            while itr:
                queue+= str(itr.data)+", "
                itr=itr.next
            print(queue) 
    def enqueue(self,data):
        self.Head=Node3(data,self.Head)
    def deque(self):
        if self.Head==None:
            print("queue is empty")
            return
        if self.Head.next==None:
            self.Head=None
        else:
            itr=self.Head
            while itr:
                if itr.next.next==None:
                    data= itr.next.data
                    itr.next=None
                    print(data," removed")
                    break
                itr=itr.next
    def display(self):
        self.isempty()
ll3=List()
ll3.isempty()
ll3.enqueue(5)
ll3.enqueue(4)
ll3.enqueue(3)
ll3.display()
ll3.deque()
ll3.display()