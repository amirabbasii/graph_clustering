from builtins import print
from LinkedList import Stack
from LinkedList import  LinkedList as linked
from Queue import Queue as Queue
import random

#class teset for mergesort
class TM:
    t=0
    nnn=0
    memory = 0

# class teset for quicksort
class TQ:
    t=0
    nnn=0
    memory=0
#class teset for insertion sort
class TS:
    t=0
    nnn=0
    memory = 0
#partion for quick sort
def partion(A,p,r):
    TQ.memory+=2
    i=p-1
    for j in range(p,r):
        TQ.t+=1
        if A[j].score<A[r].score:
            i+=1
            tmp=A[j]
            A[j]=A[i]
            A[i]=tmp
    tmp=A[r]
    A[r]=A[i+1]
    A[i+1]=tmp
    return i+1
#quick sort
def quickSort(A,p,r):

    if p<r:
        index=partion(A,p,r)
        quickSort(A,p,index-1)
        quickSort(A,index+1,r)
#merge for merge sort
def merge(x,y):
    i=0
    j=0
    home=0
    ans=[0 for i in range(len(x)+len(y))]#answer
    TM.memory+=len(x)+len(y)+3#memory
    while i<len(x) and j<len(y):
        if x[i].score<y[j].score:
            ans[home]=x[i]
            home+=1
            i+=1
        else:
            ans[home]=y[j]
            home+=1
            j+=1
        TM.t += 1
    while i<len(x):
        ans[home] = x[i]
        home += 1
        i += 1
        TM.t += 1
    while j < len(y):
        ans[home] = y[j]
        home += 1
        j += 1
        TM.t += 1
    return ans
#merge sort
def mergeSort(A):
    TM.memory+=1
    if len(A)<2:
        return A
    mid=len(A)//2
    x=mergeSort(A[0:mid])
    y=mergeSort(A[mid:])
    return  merge(x,y)
#insertion sort
def insertionSort(A):
    ans=[0 for  i in range(len(A))]
    TS.memory+=len(A)+2
    index=0
    for i in A:
        TS.t+=1
        ans[index]=A[index]
        t=index
        while t>0 and ans[t-1].score>=ans[t].score:
            TS.t+=1
            tmp=ans[t]
            ans[t]=ans[t-1]
            ans[t-1]=tmp
            t-=1
        index+=1
    return ans
#class yall
class Edge:
    def __init__(self,a,b,score,cut,cutVertex):
        self.a=a
        self.b=b
        self.score=score
        self.cut=cut
        self.cutVertex=cutVertex
    def __str__(self):
        return str(self.a)+" "+str(self.b)+":"+str(self.score)
#class tree
class Tree:
    def __init__(self,data):
        self.trees=[]
        self.data=data
    def insert(self,tr):
        self.trees.append(tr)
    #chap derakht
    def print(self):
        print(self.data)
        for i in self.trees:
            i.print()
        #ertefa
    def getHeight(self):
        def doIt(n,tre):
            if len(tre.trees)>0:
                return max([doIt(n+1,i) for i in tre.trees])
            else:
                return n
        return doIt(0,self)
    #emtiazi
    #moshahede saht ertebate do ras
    #az har ja be mabda resid falg True mishavad va shomarande shoroo be ziad shodan mishavad
    def getBase(self,a,b,n,flag):
        if self.data==b:
            print(n)
            return
        if self.data==a or flag==True:#mabda peyda shod
            for i in self.trees:
                i.getBase(a,b,n+1,True)
        else:#mabda peyda nashode
            for i in self.trees:
                i.getBase(a,b,n,False)


#class graph
class Graph:
    def __init__(self,n):#it takes n for number of vertexes
        self.vertex=[linked() for i in range(n)]
        self.matris=[[0 for i in range(n)] for j in range(n)]
    def insert(self,d1,d2):#insert an edge
        self.vertex[d1].insert(d2)
        self.vertex[d2].insert(d1)
        ###Matris###
        self.matris[d1][d2]=1
        self.matris[d2][d1] = 1
        #########

    def deleteEdge(self,a,b):#delete edge
        self.vertex[a].delete(b)
        self.vertex[b].delete(a)
        self.matris[a][b]=0
        self.matris[b][a]=0
    def print(self):
        for i in self.vertex:
            print(str(i)+":"+str(self.vertex[i]))
    #BFS
    def BFS(self,d):
        queue=Queue()
        queue.enqueue(d)
        qT=Queue()
        tree=Tree(d)
        qT.enqueue(tree)
        visited=[False for i in range(len(self.vertex))]
        visited[d]=True
        while not queue.isEmpty():
            v=queue.dequeue()
            tr=qT.dequeue()
            for i in self.vertex[v].getVers():
                if visited[i]==False:
                    queue.enqueue(i)
                    tmp=Tree(i)
                    qT.enqueue(tmp)
                    visited[i]=True
                    tr.insert(tmp)
        return tree
    #getCut edges
    #az yek stack estefade mikonad.har yal ke ezafe shavad daroone stack miravad
    #ba har ack edge yal haye daroone stack inghadr pop mishavand ke be sare back edge beresim
    def getCutEdges(self,d):
        visitedD=[False for i in range(len(self.vertex))]#aray for visited
        visitedEdge=linked()#zakhire yal haye dide shode baraye tashkise bakcedge
        stack=Stack()#stack
        def doIt(d,tr):
            visitedD[d]=True
            for i in self.vertex[d].getVers():
                if visitedD[i]==False:
                    stack.push([d,i])
                    visitedEdge.insert([d,i])
                    tt=Tree(i)
                    tr.insert(tt)
                    doIt(i,tr)
                elif  not [i,d] in list(visitedEdge.getVers()) and not [d,i] in list(visitedEdge.getVers()):#sharte bckedge
                    tt = Tree(i)
                    tr.insert(tt)
                    visitedEdge.insert([d,i])
                    tmp=None
                    if stack.peek()[0]==d:#jelogiri az hazf khodash
                        tmp=stack.peek()
                    yu = stack.pop()
                    #inghadr hazf mikonad ta be sare backedge beresad va anra ham hazf konad
                    while not stack.isEmpty() and i!=yu[0]:
                        yu = stack.pop()
                    if tmp!=None:#khodash ezafe mishavad
                        stack.push(tmp)
        tr=Tree(d)
        doIt(d,tr)
        ans=[None for i in range(stack.getSize())]
        i=0
        while not stack.isEmpty():
            ans[i]=stack.pop()
            i+=1
        return ans
    #be dasr avardane ras haye boreshi
    def getCutVertexes(self,d):
        visitedD=[False for i in range(len(self.vertex))]
        visitedEdge=linked()#zakhire ras haye boreshi
        stack=Stack()
        def doIt(d,tr):
            visitedD[d]=True
            for i in self.vertex[d].getVers():
                if visitedD[i]==False:
                    stack.push([d,i])
                    visitedEdge.insert([d,i])
                    tt=Tree(i)
                    tr.insert(tt)
                    doIt(i,tr)
                elif  not [i,d] in list(visitedEdge.getVers()) and not [d,i] in list(visitedEdge.getVers()):#sharte backedge
                    tt = Tree(i)
                    tr.insert(tt)
                    visitedEdge.insert([d,i])
                    tmp=None
                    if stack.peek()[0]==d:
                        tmp=stack.peek()
                    #inghdar hazf mikonad ta be sare backedge beresad
                    while not stack.isEmpty() and i!=stack.peek():
                        stack.pop()
                    if tmp!=None:
                        stack.push(tmp)


        tr=Tree(d)
        doIt(d,tr)
        ans=[None for i in range(stack.getSize())]
        i=0
        while not stack.isEmpty():
            ans[i]=stack.pop()[0]
            i+=1

        return ans

    #darage ras ra midahad
    def degree(self,d):
        return self.vertex[d].size
    #tedade ghesmat haye geraoh ra midahad
    #ba DFS
    def pieces(self):
        counter=0#tedade ras ha
        visited = [False for i in range(len(self.vertex))]

        def doIt(s):
            visited[s] = True
            for i in self.vertex[s].getVers():
                if not visited[i]:
                    doIt(i)
        for i in range(len(self.vertex)):
            if not visited[i]:
                counter+=1
                doIt(i)
        return counter
    #jvab
    def WriteAnswer(self):
        counter=0
        visited = [False for i in range(len(self.vertex))]
        a=Stack()
        b=Stack()
        def doIt(s):
            visited[s] = True
            if counter == 1:
                a.push(s)
            else:
                b.push(s)
            for i in self.vertex[s].getVers():
                if not visited[i]:
                    doIt(i)
        for i in range(len(self.vertex)):
            if not visited[i]:
                counter+=1
                doIt(i)

        return [[a.pop() for i in range(a.getSize())],[b.pop() for i in range(b.getSize())]]
    #dor haye be toole se
    def loop3(self):
        n = 0
        aray=[[0 for j in self.vertex] for i in self.vertex]
        status= [[[0 for z in self.vertex] for j in self.vertex] for i in self.vertex]
        for i in range(len(self.vertex)):
            for  j in list(self.vertex[i].getVers()):
                aray[i][j]=1
                n+=1
        ans = [[0 for j in self.vertex] for i in self.vertex]

        for i in range(len(self.vertex)):
            for  j in self.vertex[i].getVers():
                for t in  self.vertex[i].getVers():
                    if aray[j][t]==1 and status[i][j][t]==0:
                        status[i][j][t] = 1
                        status[i][t][j] = 1
                        status[t][j][i] = 1
                        status[t][i][j] = 1
                        status[j][i][t] = 1
                        status[j][t][i] = 1
                        ans[j][t]=+1
                        ans[j][i] += 1
                        ans[i][t] += 1
                        ans[t][j] = +1
                        ans[t][i] += 1
                        ans[i][j] += 1
        for i in range(len(aray)):
            for j in range(len(aray)):
                if ans[i][j]==0 and aray[i][j]==0:
                    ans[i][j]=-1

        return [ans,n]
def main():
    n=int(input("Pleaase enter number of vertexed:"))#tedade ras ra migirad
    graph=Graph(n)
    y=int(input("Pleaase enter number of edges:"))#tedade yal ra migirad
    ###########yal ha gerefte mishavand
    for i in range(y):
        tmp=input()
        tmp=tmp.split(" ")
        graph.insert(int(tmp[0]),int(tmp[1]))
    piece=1#tedade bakhsh haye hambandi

    while piece==1:
        b=graph.loop3()#dor be toole se
        cutEdges=graph.getCutEdges(0)
        cutVerts=graph.getCutVertexes(0)
        t=b[0]
        edges=[None for i in range(b[1]//2)]
        p=0
        for i in range(len(t)):
            for j in range(i):
                if t[i][j]!=-1:
                    cut = False
                    if [i, j] in cutEdges or [j, i] in cutEdges:
                        cut = True
                    cutV=False
                    if i in cutVerts or j in cutVerts:
                        cutV=True
                    try:
                        hj=(t[i][j]+1)/min(graph.degree(j)-1,graph.degree(i)-1)
                        edges[p]=Edge(i,j,hj,cut,cutV)
                        p+=1
                    except ZeroDivisionError:
                        edges[p] = Edge(i, j,100000000,cut,cutV)
                        p+=1

        quickSort(edges,0,len(edges)-1)#quick sort
        edges=insertionSort(edges)#insertion sort
        edges=mergeSort(edges)#merge sort
        TM.nnn=len(edges)
        TQ.nnn=len(edges)
        TS.nnn=len(edges)
        t=[i.score for i in edges]
        if not t[0] in edges[1:]:#agar avalin khane min ast
            graph.deleteEdge(edges[0].a,edges[0].b)
        else:
            stack = Stack()#stacke shamele ras haye min
            for i in edges:
                if i.score!=t[0]:#min dovom
                    break
                if i.cut==True:#agar yale boreshi ast
                    stack.push(i)
            if stack.getSize()==1:#agar boreshi peyda shode faqat yeki bood
                e=stack.pop()
                graph.deleteEdge(e.a, e.b)
            else:#vagarna dar beyne yal haye daroone stack yali ke dar rase boreshi ast hazf mikonadad
                yu=stack.pop()
                while yu.cutV==False:
                    yu=stack.pop()
                graph.deleteEdge(yu.a,yu.b)

        piece=graph.pieces()
    tmp=graph.WriteAnswer()#javab
    answer="#1:A\n"
    # har ja yek bahsad A ast
    if 1 in tmp[0]:
        societyA=tmp[0]
        societyB=tmp[1]
    else:
        societyA = tmp[1]
        societyB = tmp[0]
    #sakhee javab
    for i in societyA:
        if i!=1:
            answer+="#"+str(i)+":A\n"
    for i in societyB:
        answer+="#"+str(i)+":B\n"
    #save javab
    with open("data.txt","w") as file:
        file.write(answer)
        file.close()
    print(answer)




















