##  Finding the Longest Multiple Repeat

with open("test.txt","r") as f:
    seq = f.readline().strip()
    k = int(f.readline().strip())
    nodeList = [i.strip().split() for i in f.readlines()]

childIdxDic = {}
childIdxDic["node1"] = {"parent":"","pos":0,"len":0, "sumN":0}
for i in nodeList:
    childIdxDic[i[1]] = {"parent":i[0],"pos":int(i[2])-1,"len":int(i[3]), "sumN":0}

for i in nodeList:
    if seq[int(i[2])+int(i[3])-2] == "$":
        cur = i[1]
        childIdxDic["node1"]["sumN"] += 1
        while childIdxDic[cur]["parent"] != "":
            childIdxDic[cur]["sumN"] += 1
            cur = childIdxDic[cur]["parent"]

maxLenSeq = ""
for i in childIdxDic:
    if childIdxDic[i]["sumN"]>=k:
        cur = i
        curLenSeq = ""
        while childIdxDic[cur]["parent"] != "":
            curLenSeq = seq[childIdxDic[cur]["pos"]:childIdxDic[cur]["pos"]+childIdxDic[cur]["len"]] +  curLenSeq
            if len(maxLenSeq)<len(curLenSeq):
                maxLenSeq = curLenSeq
            cur = childIdxDic[cur]["parent"]

print(maxLenSeq)
