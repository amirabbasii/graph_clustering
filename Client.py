import socket
class Client:#client
    def __init__(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((socket.gethostname(),1234))
        print(s.recv(1024).decode('ascii'))#payam migirad
        s.send(str.encode(input()))#javab midahad
        print(s.recv(1024).decode('ascii'))#payam migirad
        s.send(str.encode(input()))#javab midadhad
        tmp=s.recv(1024).decode('ascii')
        if tmp!="App not found!!":
            print("1)Download\n2)Scoring in Sport\n3)Scoring in Strategy\nsuggested games:\n"+tmp)
            s.send(str.encode(input()))
            print(s.recv(1024).decode('ascii'))
c=Client()