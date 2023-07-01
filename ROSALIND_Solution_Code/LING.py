##  Linguistic Complexity of a Genome


## suffix tree solution. counting how many $ in the trees as sub(s)


## math brute force solution

import math

def ling(seq):
    n = len(seq)
    m = 0
    lg = int(math.log(n,4))
    for i in range(1,lg+1):
        m += 4**i
    for i in range(1,n-lg+1):
        m += i
    
    sub = 0
    # for i in range(1,n+1):
    #     sub += len(set([seq[s:s+i] for s in range(n-i+1)]))
   
    return sub/m

with open("test.txt",'r') as f:
    seq = f.readline().strip()

print(ling(seq))
