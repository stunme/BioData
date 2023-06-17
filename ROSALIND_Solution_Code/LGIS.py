##  Longest Increasing Subsequence
##  compare patience sorting and DP solution(about 10 times slower)

dataset = []
with open("test.txt", 'r') as f:
    f.readline()
    dataset = [int(j) for j in f.readline().strip().split(' ')]

def findLCS1( dataset, ascend = True):
    """patience sorting"""
    piles = []
    for i in dataset:
        try:
            if ascend:
                idx = next(j for j in range(len(piles)) if piles[j][-1][0]<i)
            else:
                idx = next(j for j in range(len(piles)) if piles[j][-1][0]>i)
            piles[idx].append((i,len(piles[idx-1]) if idx > 0 else -1))
        except StopIteration:
            piles.append( [(i,len(piles[-1]) if piles else -1)])
        #print(piles)
    result = []
    bp = -1
    for i in range(len(piles)-1,-1,-1):
        result.append(piles[i][bp][0])
        bp = piles[i][bp][1]-1
        #print(result)

    return result[::-1]

def findLCS2(dataset, ascend = True):
    """DP solution"""
    result = [[dataset[0]]]
   
    for i in range(1,len(dataset)):
        tmp = []
        maxLen = 0
        pre_j = [-1]*len(result[0])
        for j in result:
            if len(j)+1<maxLen:
                break
            for w in range(len(j)-1,-1,-1):
                if j[w] == pre_j[w]:
                     w = 0
                     break
                if ascend:
                    if dataset[i]>j[w]:
                        w += 1
                        break
                else:
                    if dataset[i]<j[w]:
                        w += 1
                        break
            pre_j = j  
            w +=1
            if w > maxLen:
                maxLen = w
                tmp = j[:w-1]+[dataset[i]]

        k = 0
        flag = True
        insert_k = -1
        if ascend:
            while k<len(result):
                if len(result[k])>maxLen:
                    if result[k][-1]<tmp[-1]:
                        flag = False
                        break
                elif len(result[k])== maxLen:
                    if result[k][-1]<tmp[-1]:
                        flag = False
                        break
                    else:
                        insert_k = k
                        del result[k]
                else:
                    if insert_k<0:
                        insert_k = k
                    if result[k] == tmp[:-2]:
                        del result[k]
                k +=1
        else:
            while k<len(result):
                if len(result[k])>maxLen:
                    if result[k][-1]>tmp[-1]:
                        flag = False
                        break      
                elif len(result[k])== maxLen:
                    if result[k][-1]>tmp[-1]:
                        flag = False
                        break
                    else:    
                        insert_k = k
                        del result[k]
                else:
                    if insert_k<0:
                        insert_k = k
                    if result[k] == tmp[:-2]:
                        del result[k]
                k +=1
        if flag:
            if insert_k<0:
                result.append(tmp)
            else:
                result.insert(insert_k,tmp)
    return max(result,key =len)

import time

ascend = False
start = time.time()
LCS = findLCS2(dataset,ascend)
print(len(LCS))
print(time.time()-start)

start = time.time()
LCS = findLCS1(dataset, lambda a,b: a > b)
print(len(LCS))
print(time.time()-start)



print("========================================")

print(" ".join(str(i) for i in LCS))
LCS = findLCS1(dataset, lambda a,b: a < b)
print(" ".join(str(i) for i in LCS))
