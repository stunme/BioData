##  Alignment-Based Phylogeny 

import re

with open("test.txt",'r') as f:
    treeStr = f.readline().strip()
    taxaDict = {}
    cur = ""
    for i in f.readlines():
        i = i.strip()
        if ">" in i:
            cur = i.replace(">","")
            taxaDict[cur] = ""
        else:
            taxaDict[cur]+=i

def dH(s1, s2):
    return sum(a!=b for a,b in zip(s1,s2))

def dHStr(s1,s2):
    result = ''
    for a,b in zip(s1,s2):
        if a==b:
            result

itaxaDict={}

tokens =re.split("([(),])",treeStr)
print(tokens)
stack = [[]]
taxa = ""
for t in tokens:
    if t == '(':
        stack.append([])
    elif t == ')':
        cur = stack.pop()
        print(cur)
        print(dH(taxaDict[cur[0]],taxaDict[cur[1]]))
    elif t == ',':
        pass
    elif t!='':
        stack[-1].append(t)