##  Counting Quartets

# another pure math question. Pick any four taxas from the collection will guarantee to have one quartet.
from math import factorial as fa

with open("test.txt",'r') as f:
    n = int(f.readline().strip())
print(int(fa(n)/fa(n-4)/fa(4)%10**6))



# Another solution by recursion calculate every branch.
# Practice for count quartet distance 



#mimic a unrooted binary tree, with root has three child as starting point

def tree(newickSeq):
    class node():
        def __init__(self,parent) -> None:
            self.child = []
            self.count = 0
            self.name = ""
            self.parent = parent

    stack = [[]]
    taxa = ""
    root = node(None)
    cur = root
    for i in newickSeq:
        if i == "(":
            stack.append([])
            cur.child.append(node(cur))
            cur = cur.child[-1]
        elif i == ")":
            tmp = stack.pop()
            if taxa != "":
                tmp.append(taxa)
            taxa = ""
            # print(tmp)
            for t in tmp:
                cur.child.append(node(cur))
                cur.child[-1].name = t
                cur.child[-1].count = 1
            cur.count += len(tmp)
            cur.parent.count += cur.count
            cur = cur.parent
            
        elif i == ",":
            if taxa!="":
                stack[-1].append(taxa)
            taxa = ""
        else:
            taxa += i
    return root.child[0]

#recursion calculate child node

def count(node, n):
    if len(node.child)<2:
        return 0
    node1 = node.child[0]
    node2 = node.child[1]
    sum = 0
    if node1.count > 1:
        sum += (node1.count * (node1.count-1) / 2) %10**6 * (node2.count*n) % 10**6
    if node2.count > 1:
        sum += (node2.count * (node2.count-1) / 2) %10**6 * (node1.count*n) % 10**6
    if node1.count>1 and node2.count>1:
        sum += (node1.count * (node1.count-1) / 2) %10**6 * (node2.count * (node2.count-1) / 2) % 10**6
    sum += count(node1,n+node2.count)
    sum += count(node2,n+node1.count)
    return sum % 10**6

with open("test.txt",'r') as f:
    n = int(f.readline().strip())
    seq = f.readline().strip()

root = tree(seq)
total = 0

subCount = []

# count three root childs

for i in root.child:
    subCount.append(i.count)
    total += count(i,n-i.count)

if subCount[0]>1:
    total += (subCount[0] * (subCount[0]-1) /2)% 10**6 * (subCount[1]*subCount[2]) % 10**6
    total %= 10**6
if subCount[1]>1:
    total += (subCount[1] * (subCount[1]-1) /2)% 10**6 * (subCount[0]*subCount[2]) % 10**6
    total %= 10**6
if subCount[2]>1:
    total += (subCount[2] * (subCount[2]-1) /2)% 10**6 * (subCount[1]*subCount[0]) % 10**6
    total %= 10**6
if subCount[1]>1 and subCount[2]>1:
    total += (subCount[1] * (subCount[1]-1) /2)% 10**6 * (subCount[2] * (subCount[2]-1) /2) % 10**6 
    total %= 10**6
if subCount[1]>1 and subCount[0]>1:
    total += (subCount[1] * (subCount[1]-1) /2)% 10**6 * (subCount[0] * (subCount[0]-1) /2) % 10**6
    total %= 10**6
if subCount[0]>1 and subCount[2]>1:
    total += (subCount[0] * (subCount[0]-1) /2)% 10**6 * (subCount[2] * (subCount[2]-1) /2) % 10**6
    total %= 10**6

print(int(total))