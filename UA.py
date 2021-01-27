import  math
from LinkedList import Stack
from LinkedList import LinkedList
#class application
class Aplication:
    games=LinkedList()
    def __init__(self,name,programmer):
        self.name=name#name
        self.programmer=programmer#programmer
        self.download=0#download
        self.scores=[0,0]#score
    def __eq__(self, other):
        if self.name==other.name:
            return True
        else:
            return False
    @staticmethod
    def newApp(name,programmer):#bazi jadid
        Aplication.games.insert(Aplication(name,programmer))
    @staticmethod
    def getGraph():#geraph;az fasele oghlidesi estefade mikonad;agar az 0.2 bozorgtar bashad...
        aray=[[0 for j in range(Aplication.games.size)] for i in range(Aplication.games.size)]
        for i in range(Aplication.games.size):
            app=list(Aplication.games.getVers())[i]
            sc1 = app.scores
            for j in range(Aplication.games.size):
                sc2=list(Aplication.games.getVers())[j].scores
                dp=(sc1[0]-sc2[0])**2+(sc1[1]-sc2[1])**2
                same=1/(1+math.sqrt(dp))
                if same>=0.2:#fasele oghlidesi
                    aray[i][j]=1
                else:
                    aray[i][j]=0

        vertexes = len(aray)
        stack = Stack()
        for i in range(len(aray)):
            for j in range(i):
                if aray[i][j] == 1:
                    stack.push(str(i) + " " + str(j))
        edges = [stack.pop() for i in range(stack.getSize())]
        return [vertexes, len(edges), edges]
#class user
class User:
    users=LinkedList()#link liste userha
    def __init__(self,name):
        self.name=name
        self.appliactions=LinkedList()
    #download
    def download(self,app):
        self.appliactions.insert(app)
    @staticmethod
    def newUser(name):#user jadid
        User.users.insert(User(name))


