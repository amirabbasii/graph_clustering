
class Node:
    def __init__(self, data):
        self.next=None
        self.data = data
class LinkedList:

    def __init__(self):
        self.start=None
        self.size=0
    def __str__(self):
        pointer = self.start
        ans=""
        while (pointer!= None):
            ans+=str(pointer.data)+" "
            pointer=pointer.next
        return ans
    def insert(self,data):
        pointer=self.start
        if pointer==None:
            self.start=Node(data)
        else:
            while(pointer.next!=None):
                pointer=pointer.next
            pointer.next=Node(data)
        self.size+=1
    def __contains__(self, item):
        p=self.start
        flag=False
        while p!=None:
            if p.data==item:
                flag=True
                break
        return flag

    def delete(self,d):
        p = self.start
        if p.data==d:
            self.start=p.next
        else:

            while p.next.data!=d:
                p=p.next
            p.next=p.next.next
        self.size-=1
    def getLast(self):
        p = self.start
        if self.size==1:
            return self.start.data
        else:
            while p.next!=None:
                p = p.next
        return p.data
    def deleteLast(self):
        p = self.start
        if self.start.next == None:
             self.start=None
        else:
            while p.next.next != None:
                p = p.next
            p.next=None
        self.size-=1
    def deleteFist(self):
        s=self.start
        self.delete(s.data)
        return s.data
    def getVers(self):
        p=self.start
        while p!=None:
            yield p.data
            p=p.next

class Stack:
    def __init__(self):
        self.list=LinkedList()
    def pop(self):
        ans=self.list.getLast()
        self.list.deleteLast()
        return  ans
    def push(self,d):
        self.list.insert(d)
    def isEmpty(self):
        return self.list.size==0
    def peek(self):
        return self.list.getLast()
    def getSize(self):
        return self.list.size
