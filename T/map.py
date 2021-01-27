import matplotlib.pyplot as sysAmir
with open("mergeSort.txt","r")as file:

    s=file.readlines()
    x = [0 for i in range(len(s))]
    y = [0 for i in range(len(s))]
    for i in range(len(s)):
        tmp=s[i].split(":")
        x[i]=int(tmp[0])
        y[i]=int(tmp[1])
    file.close()
    sysAmir.plot(x,y)
    sysAmir.show()

    with open("quick.txt", "r")as file:

        s = file.readlines()
        x = [0 for i in range(len(s))]
        y = [0 for i in range(len(s))]
        for i in range(len(s)):
            tmp = s[i].split(":")
            x[i] = int(tmp[0])
            y[i] = int(tmp[1])
        file.close()
        sysAmir.plot(x, y)
        sysAmir.show()

    with open("insertion.txt", "r")as file:

        s = file.readlines()
        x = [0 for i in range(len(s))]
        y = [0 for i in range(len(s))]
        for i in range(len(s)):
            tmp = s[i].split(":")
            x[i] = int(tmp[0])
            y[i] = int(tmp[1])
        file.close()
        sysAmir.plot(x, y)
        sysAmir.show()

    with open("mergeSort.txt", "r")as file:

        s = file.readlines()
        x = [0 for i in range(len(s))]
        y = [0 for i in range(len(s))]
        for i in range(len(s)):
            tmp = s[i].split(":")
            x[i] = int(tmp[0])
            y[i] = int(tmp[2])
        file.close()
        sysAmir.plot(x, y)
        sysAmir.show()

        with open("quick.txt", "r")as file:

            s = file.readlines()
            x = [0 for i in range(len(s))]
            y = [0 for i in range(len(s))]
            for i in range(len(s)):
                tmp = s[i].split(":")
                x[i] = int(tmp[0])
                y[i] = int(tmp[2])
            file.close()
            sysAmir.plot(x, y)
            sysAmir.show()

        with open("insertion.txt", "r")as file:

            s = file.readlines()
            x = [0 for i in range(len(s))]
            y = [0 for i in range(len(s))]
            for i in range(len(s)):
                tmp = s[i].split(":")
                x[i] = int(tmp[0])
                y[i] = int(tmp[2])
            file.close()
            sysAmir.plot(x, y)
            sysAmir.show()


