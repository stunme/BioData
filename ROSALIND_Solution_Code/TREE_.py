##  Completing a Tree


dataset = []
with open("test.txt","r") as f:
    for i in f.readlines():
        dataset.append(i.strip())

size = dataset[0]
connections = []
for i in range(1,len(dataset)):
    connections.append(dataset[i].split(" "))

groups = [set([])]

for link in connections:
    for g in len(groups):
        if set(link)&groups[g]:
            groups[g] = set(link)|groups[g]
        else:
            groups.append