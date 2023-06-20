##  Introduction to Random Strings 

import math

with open("test.txt","r") as f:
    s = f.readline().strip()
    A = [float(i) for i in f.readline().strip().split(" ")]
B = []
for i in range(len(A)):
    dic = {"G":math.log(A[i]/2,10),
           "C":math.log(A[i]/2,10),
           "A":math.log((1-A[i])/2,10),
           "T":math.log((1-A[i])/2,10)
        }
    probability = 0
    for n in s:
        probability += dic[n] 
    B.append(round(probability,3))

print(" ".join(str(i) for i in B))

