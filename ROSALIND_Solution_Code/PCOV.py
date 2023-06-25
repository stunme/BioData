##  Genome Assembly with Perfect Coverage

with open("test.txt","r") as f:
    seqList = set([s.strip() for s in f.readlines()])

dic = {}

for s in seqList:
    dic[s[:-1]] = s[1:]

tmp = dic.popitem()
cur = tmp[1]
seq = cur[-1]
for i in range(len(dic)):
    seq += dic[cur][-1]
    cur = dic[cur]

print(seq)