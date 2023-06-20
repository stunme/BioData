##Expected Number of Restriction Sites

with open("test.txt","r") as f:
    n = int(f.readline().strip())
    s = f.readline().strip()
    A = [float(i) for i in f.readline().strip().split(" ")]
    
B = []
for i in A:
    dic = {"G":i/2,
           "C":i/2,
           "A":(1-i)/2,
           "T":(1-i)/2
        }

    P = 1
    for j in s:
        P *= dic[j]
    B.append(round(P*(n-len(s)+1),3))

print(" ".join(str(i) for i in B))
