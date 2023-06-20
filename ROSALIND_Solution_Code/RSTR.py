
##  Matching Random Motifs

with open("test.txt","r") as f:
    num = f.readline().strip().split(" ")
    N = int(num[0])
    x = float(num[1])
    s = f.readline().strip()


dic = {"G":x/2,
       "C":x/2,
       "A":(1-x)/2,
       "T":(1-x)/2
    }
P = 1
for n in s:
    P *= dic[n] 
    

print(round(1-(1-P)**N,3))

