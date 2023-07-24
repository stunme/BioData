##  Quartets 

import itertools as it

def qrt(seq):
    charOn = [i for i in range(len(seq)) if seq[i]=="1"]
    charOff = [i for i in range(len(seq)) if seq[i]=="0"]
    for x in it.combinations(charOn,2):
        for y in it.combinations(charOff,2):
            yield x,y

with open("test.txt",'r') as f:
    taxaList = f.readline().strip().split()
    charTable = [i.strip() for i in f.readlines()]

qrtSet = set()
with open("result.txt",'w') as f:
    for c in charTable:
        for x,y in qrt(c):
            if (x,y) not in qrtSet and (y,x) not in qrtSet:
                f.write(f"{{{taxaList[x[0]]}, {taxaList[x[1]]}}} {{{taxaList[y[0]]}, {taxaList[y[1]]}}}\n")
                qrtSet.add((x,y))