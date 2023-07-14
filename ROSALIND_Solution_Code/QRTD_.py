##  Quartet Distance

# copy code from SPTD.py. get the different of charTable first.

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


def fa(n,m):
    res = 1
    for i in range(n,n-m,-1):
        res *= i
    return res

sum = 0
for i in set1&set2:
    one = i.count('1')
    sum += fa(one,2)/fa(2,2) * fa(len(i)-one,2)/fa(2,2)
print(sum)
sum = 0
for i in set2-set1:
    one = i.count('1')
    sum += fa(one,2)/fa(2,2) * fa(len(i)-one,2)/fa(2,2)
print(sum)
# print(len(taxas),fa(len(taxas),4))
# print(int(fa(len(taxas),4)/fa(4,4)))
# print(int(sum/3)*2*2)




# print(len(set1),len(set2))

# def reverse(seq):
#     mapping = str.maketrans("01","10")
#     return seq.translate(mapping)

# subSet1 =set1-set2
# subSet2 =set2-set1

# # for i in set1:
# #     if i not in set2 and reverse(i) not in set2:
# #         subSet1.add(i)
# # for i in set2:
# #     if i not in set1 and reverse(i) not in set1:
# #         subSet2.add(i)


# # print(subSet1)
# # print(subSet2)
# print(len(subSet1),len(subSet2))

# def findIt(x,y):
#     AA = []
#     BB = []
#     AB = []
#     BA = []
#     for i in range(len(x)):
#         if x[i] == '1':
#             if y[i] == '1':
#                 AA.append(i)
#             else:
#                 AB.append(i)
#         else:
#             if y[i] == '1':
#                 BA.append(i)
#             else:
#                 BB.append(i)
#     result = []
#     if len(AA)*len(AB)*len(BB)*len(BA) ==0:
#         return result
#     for aa in AA:
#         for ab in AB:
#             for ba in BA:
#                 for bb in BB:
#                     tmp = [aa,ab,ba,bb]
#                     tmp.sort()
#                     result.append(''.join(str(i) for i in tmp))
#     # if(len(result)!=0):
#     #     print(f">     {len(result)}")
#     return result

# result = set()
# count = 0
# for x in subSet1:
#     result =set()
#     for y in subSet2:
#         tmp = set(findIt(x,y))
#         if len(tmp)!=0:
#             result |= tmp
#             # print(len(result)) 
#         count+=1
            
#     print(count//len(subSet1),len(result))

# print(len(result)*2)













# #### Copy code from QRT.py. get the distance of quartet from distance of split distance. 


# import itertools as it

# def qrt(seq):
#     charOn = [i for i in range(len(seq)) if seq[i]=="1"]
#     charOff = [i for i in range(len(seq)) if seq[i]=="0"]
#     for x in it.combinations(charOn,2):
#         for y in it.combinations(charOff,2):
#             yield x,y

# qrtSet1 = set()

# for c in subSet1:
#     for x,y in qrt(c):
#         if (x,y) not in qrtSet1 and (y,x) not in qrtSet1:
#             qrtSet1.add((x,y))

# qrtSet2 = set()

# for c in subSet2:
#     for x,y in qrt(c):
#         if (x,y) not in qrtSet2 and (y,x) not in qrtSet2:
#             qrtSet2.add((x,y))
        




