import er
from er import TM,TS,TQ
er.main()#ejraye hgesmate aval proje
#######nevetshtane hazini memort va ejra dar file###############
tmppp=""
with open("T\mergeSort.txt","r") as file:
    tmppp=file.read()
    file.close()
with open("T\mergeSort.txt","w") as file:
    file.write(tmppp+"\n"+str(TM.nnn)+":"+str(TM.t)+":"+str(TM.memory))
    file.close()
with open("T\quick.txt","r") as file:
    tmppp=file.read()
    file.close()
with open("T\quick.txt","w") as file:
    file.write(tmppp+"\n"+str(TQ.nnn)+":"+str(TQ.t)+":"+str(TQ.memory))
    file.close()
with open("T\insertion.txt","r") as file:
    tmppp=file.read()
    file.close()
with open("T\insertion.txt","w") as file:
    file.write(tmppp+"\n"+str(TS.nnn)+":"+str(TS.t)+":"+str(TS.memory))
    file.close()
####################################################################