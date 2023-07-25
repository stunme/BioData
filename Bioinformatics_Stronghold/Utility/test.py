with open("test.txt",'r') as f:
    while True:
        f.readline()
        a = f.readline().strip()
        if len(a) == 0:
            break
        else:
            print(a)
        


