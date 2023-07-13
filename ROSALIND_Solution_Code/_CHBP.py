##  Character-Based Phylogeny 

def chbp(taxaList, charTableList):
    class node():
        def __init__(self) -> None:
            self.child = []

    nodes = []
    splits = {}
    for ct in charTableList:
        nd = node()
        nd.child = [set(),set()]
        for i in range(len(ct)):
            if ct[i] == '0':
                nd.child[0].add(i)                   
            else:
                nd.child[1].add(i)       
        nodes.append(nd)
        splits[tuple(nd.child[0])] = nd
        splits[tuple(nd.child[1])] = nd
    
    for nd in nodes:

    








# def chbp(taxaList, charTableList):
#     class node():
#         def __init__(self, content) -> None:
#             self.content = content
#             self.child = []

#     idxList = set([i for i in range(len(taxaList))])
#     root = node(idxList)
#     nodes = []
    
#     a = set()
#     b = set()
#     c = set()
#     d = set()
#     for i in range(len(taxaList)):
#         if charTableList[11][i] == '0':
#             a.add(i)                   
#         else:
#             b.add(i)
#         if charTableList[10][i] == '0':
#             c.add(i)                   
#         else:
#             d.add(i)

#     # if len(a&c) != 0:
#     # elif len(a&d) != 0:
#     # elif len(a&c) != 0:
#     # elif len(a&c) != 0:
#     print(len(a&c),len(a-c),len(c-a),len(b),len(d))    
#     print(len(a&d),len(a-d),len(d-a),len(b),len(c))    
#     print(len(b&c),len(b-c),len(c-b),len(a),len(d))    
#     print(len(b&d),len(b-d),len(d-b),len(a),len(b))    







#     for ct in charTableList:
#         setOne = set()
#         setZero = set()
#         for i in range(len(ct)):
#             if ct[i] == '0':
#                 setZero.add(i)                   
#             else:
#                 setOne.add(i)
#         stack = []
#         for i in nodes:
#             subOne = i.content&setOne
#             subZero = i.content&setZero
#             if len(subOne) * len(subZero) != 0:
#                 nodeOne = node(subOne)
#                 nodeZero = node(subZero)
#                 i.child.append(nodeOne)
#                 i.child.append(nodeZero)
#                 if len(subOne)>2:
#                     nodes.append(nodeOne)
#                 if len(subZero)>2:
#                     nodes.append(nodeZero)
#                 stack.append(i)
#                 break
#         for i in stack:
#             nodes.remove(i)
#     return root

def printTree(node):
    if len(node.content)==1:
        return taxaList[node.content.pop()]
    elif len(node.content) == 2:
        tmp = list(node.content)
        return f"({taxaList[tmp[0]]},{taxaList[tmp[1]]})"
    else:
        return f"({printTree(node.child[0])},{printTree(node.child[1])})"

with open("test1.txt",'r') as f:
    taxaList = f.readline().strip().split()
    charTableList = [i.strip() for i in f.readlines()] 

chbp(taxaList, charTableList)
# root = chbp(taxaList, charTableList)

# with open("test.txt",'w') as f:
    # f.write(f"{printTree(root)};")

