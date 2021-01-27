from LinkedList import  LinkedList as linked
class Queue:
    def __init__(self):
        self.q=linked()
    def enqueue(self,d):
        self.q.insert(d)
    def dequeue(self):
        return self.q.deleteFist()
    def isEmpty(self):
        return self.q.size==0



