import _thread
import socket
from UA import  Aplication
from UA import Aplication
from UA import User
from  er import Graph
class Server:#class srever
    def update(self):#update;dar soorate taqir emtiaz baraname ha ya ezafe shodane barname jadid
        tmp = Aplication.getGraph()
        self.graph = Graph(tmp[0])
        for i in range(len(tmp[2])):
            t = (tmp[2][i]).split(" ")
            self.graph.insert(int(t[0]), int(t[1]))
    def __init__(self):
        self.graph=None
        def inn():
            Aplication.newApp("counter","she")
            Aplication.newApp("notepad", "ali")
            Aplication.newApp("gta", "amir")
            tmp = Aplication.getGraph()
            self.graph = Graph(tmp[0])
            for i in range(len(tmp[2])):
                t = (tmp[2][i]).split(" ")
                self.graph.insert(int(t[0]), int(t[1]))
            tmp ="1"
            while tmp!="2":
                tmp = input("1)newApp2)end")
                if tmp=="1":
                    name=input("please enter the name")
                    Aplication.newApp(name,input("please enter name of programmer"))
                    self.update()

        _thread.start_new_thread(inn,())#inn rooye yek thread joda ejra mishavad
        s=socket.socket()
        s.bind(('',1234))
        s.listen(10)
        while True:#ertebat ba client ha
            c,add=s.accept()
            c.send(str.encode("please enter your name"))#payam midahad name
            name=c.recv(1024).decode('ascii')#name ra migirad
            User.newUser(name)#username misazad
            c.send(str.encode("please enter name of app"))#name app ra migirad
            appName=c.recv(1024).decode('ascii')
            index=-1
            arayyy=list(Aplication.games.getVers())
            for i in range(len(arayyy)):
                if arayyy[i]==Aplication(appName,""):#agar app peyda shod
                    index=i
                    t=[arayyy[i].name for  i in list(self.graph.vertex[i].getVers())]#barname haye mortabet
                    c.send(str.encode("\n".join(t)+"\n"+"Score in Sports:"+str(arayyy[i].scores[0])+"\nScore in Strategy:"+str(arayyy[i].scores[1])+"\nDonwload:"+str(arayyy[i].download)))
                    tt=c.recv(1024).decode('ascii')
                    if  tt== "1":#download
                        arayyy[i].download+=1
                        c.send(str.encode("App downloaded!!"))
                    if tt == "2":#score sports
                        arayyy[i].scores[0]+=1
                        c.send(str.encode("Score increased!!"))
                        self.update()#update
                    if tt == "3":#score strategy
                        arayyy[i].scores[1] += 1
                        c.send(str.encode("Score increased!!"))
                        self.update()#update
                    break
            if index==-1:#app peyda shode
                c.send(str.encode("App not found!!"))
            c.close()

s=Server()
