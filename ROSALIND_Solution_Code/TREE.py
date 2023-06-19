##  Completing a Tree
##  With no circle adjacency, a complete tree should have n nodes and n-1 edges 

dataset = []
with open("test.txt","r") as f:
    size = int(f.readline())
    for i in f.readlines():
        dataset.append(int(j) for j in i.strip().split(" "))

print(size-1-len(dataset))
