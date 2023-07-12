##  Quartet Distance

#Copy code from SPTD.py

import re
def ctbl(treeStr):
    tokens = re.split('([(),])',treeStr)
    charTable = [['1']]
    stack = [[1]]
    curLeft = 1
    for t in tokens:
        if t == '(':
            stack += [[curLeft]]
        elif t not in ',()':
            stack[-1].append(t)
        elif t == ')':
            cur = stack.pop()
            left,cur = cur[0], cur[1:]
            for i in range(len(cur)):
                charTable += [['0']*len(charTable[-1])]
                charTable[-1][0] = cur[i]
            curLeft += len(cur)
            for i in range(left):
                charTable[i].append('0')
            for i in range(left,curLeft):
                charTable[i].append('1')
    charTable.sort()
    for i in charTable:
        i.pop()
    return charTable[1:]

with open("test.txt",'r') as f:
    taxas = f.readline().strip().split()
    taxaTree1 = f.readline().strip().replace(";",'')
    taxaTree2 = f.readline().strip().replace(";",'')

ctbl1 = ctbl(taxaTree1)
ctbl2 = ctbl(taxaTree2)

set1 = set()
set2 = set()

for i in range(1,len(ctbl1[0])):
    set1.add("".join((j[i]) for j in ctbl1))
    set2.add("".join((j[i]) for j in ctbl2))

print(set1)
print(set2)
print(len(set1), len(set2))
print(len(set1&set2))
# print(set1&set2)
# Copy code from QRT.py. 

import itertools as it
from math import factorial as fa

same = 0
diff = 0

idx = [i for i in range(len(taxas))]
count = 0
print(int(fa(len(taxas))/fa(len(taxas)-4)/fa(4)))
for i in it.combinations(idx,4):
    for a in set1:
        if sum([int(a[x]) for x in i]) == 2:
            break
    for b in set2:
        if sum([int(b[x]) for x in i]) == 2:
            break

    mapping = str.maketrans("01","10")
    a = "".join(a[x] for x in i)
    b = "".join(b[x] for x in i)
    if a==b or a==b.translate(mapping):
        same +=1
    else:
        diff +=1
    if count%100000 ==0:
        with open("result.txt",'a') as f:
            f.write(f"Finished {count}\tcombinations, same = {same} pairs\tdiff = {diff} pairs.\n")
    count+=1
print(same, diff)
















# def qrt(seq):
#     charOn = [i for i in range(len(seq)) if seq[i]=="1"]
#     charOff = [i for i in range(len(seq)) if seq[i]=="0"]
#     for x in it.combinations(charOn,2):
#         for y in it.combinations(charOff,2):
#             yield x,y
# qrtSet1 = set()
# qrtSet2 = set()
# count = 0




















# for c in set1:
#     for x,y in qrt(c):
#         if (x,y) not in qrtSet1 and (y,x) not in qrtSet1:
#             qrtSet1.add((x,y))
#     with open("result.txt",'a') as f:
#         f.write(f"qrtSet1 has done {count} charTable string. The total of qrtSet1 is {len(qrtSet1)}")
#     count+=1
# count = 0
# for c in set2:
#     for x,y in qrt(c):
#         if (x,y) not in qrtSet2 and (y,x) not in qrtSet2:
#             qrtSet2.add((x,y))
#     with open("result.txt",'a') as f:
#         f.write(f"qrtSet2 has done {count} charTable string. The total of qrtSet2 is {len(qrtSet2)}")
#     count+=1

# print(len(qrtSet1),len(qrtSet2),len(qrtSet1&qrtSet2))

# print(2*int(fa(len(taxas))/fa(len(taxas)-4)/fa(4) - len(qrtSet)))