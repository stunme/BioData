##  Alignment-Based Phylogeny 

import re
from collections import Counter

with open("test.txt",'r') as f:
    treeStr = f.readline().strip().replace(";","")
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

def dHStr(sList):
    result = ''
    for i in range(len(sList[0])):
        dic = {}

class node():
    def __init__(self, taxa) -> None:
        self.taxa = taxa
        self.child = None
        self.parent = None

tokens =re.split("([(),])",treeStr)
print(tokens)
stack = [[]]
cur = None
for i in range(len(tokens)):
    if tokens[i] == '(':
        stack.append([])
    elif tokens[i] == ')':
        cur = stack.pop()
    elif tokens[i].isalpha():
        stack[-1].append(node(tokens[i]))
        if not cur:
            root = stack[-1][-1]
            root.child = cur
            print(root.taxa)
            cur = None

def traceDown(nd):
    if nd.child:
        print(nd.taxa)
    else:
        traceDown(nd.child[0])
        traceDown(nd.child[1])
        
traceDown(root)