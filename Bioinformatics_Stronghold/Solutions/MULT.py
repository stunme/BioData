##     Multiple Alignment 

# recursion depth limit is 1000

from utility import readFastaFileList


def mult(seqList):    
    def traceDown(i,j):
        """Trace back to generate all possible alignments. 
           Will need global var traceDic, m and copySL"""
        if (i,j) not in traceDic:
            traceDic[(i,j)] = []
            print(i,j)
            if i*j == 0:
                y = copySL.copy()
                y[m]='-'*i+copySL[m][:j]
                for n in range(m):
                    y[n] = '-'*j+copySL[n][:i]
                traceDic[(i,j)].append(y)
            else:
                for x in tracker[i][j]:
                    if x == 0:
                        for y in traceDown(i-1,j-1):
                            y = y.copy()
                            y[m] += copySL[m][j-1]
                            for n in range(m):
                                y[n] += copySL[n][i-1]
                            traceDic[(i,j)].append(y)    
                    if x == 1:
                        for y in traceDown(i-1,j):
                            y = y.copy()
                            y[m] += '-'
                            for n in range(m):
                                y[n] += copySL[n][i-1]
                            traceDic[(i,j)].append(y)    
                    if x == 2:
                        for y in traceDown(i,j-1):
                            y = y.copy()
                            y[m] += copySL[m][j-1]
                            for n in range(m):
                                y[n] += '-'
                            traceDic[(i,j)].append(y)    
        return traceDic[(i,j)]
    
    totalScore = 0
    stack = [seqList.copy()]
    for m in range(1,len(seqList)):
        maxScore = -1000000
        tmpStack = []
        for copySL in stack:
            lenI = len(copySL[m-1])+1
            lenJ = len(copySL[m])+1
            arr = []
            tracker = []
            for i in range(lenI): 
                arr.append([0]*lenJ)
                tracker.append([0]*lenJ)
            for i in range(1,lenI):
                arr[i][0] = arr[i-1][0]-len([x for x in range(m) if copySL[x][i-1]!='-'])
            for j in range(1,lenJ):
                arr[0][j] = -m*j
            for i in range(1,lenI):
                for j in range(1,lenJ):
                    a = arr[i-1][j-1]-len([x for x in range(m) if copySL[x][i-1]!=copySL[m][j-1]])
                    b = arr[i-1][j]+arr[i][0]-arr[i-1][0]
                    c = arr[i][j-1]-m
                    arr[i][j] = max(a,b,c)
                    tracker[i][j] = []
                    if arr[i][j] == a:
                        tracker[i][j].append(0)
                    if arr[i][j] == b:
                        tracker[i][j].append(1)
                    if arr[i][j] == c:
                        tracker[i][j].append(2)
            
            ## Track back to get all possible aligment only when current score is the max scores ever
            if arr[i][j]<maxScore:
                continue
            elif arr[i][j] > maxScore:
                maxScore = arr[i][j]
                tmpStack = []
            traceDic = {}
            for x in traceDown(i,j):
                tmpStack.append(x)
        stack = tmpStack.copy()
        totalScore += maxScore
    print(totalScore)
    return stack[0]

seqList = readFastaFileList("test.txt")
sl = mult(seqList)
print("\n".join(i for i in sl))


