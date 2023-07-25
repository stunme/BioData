##  Longest Increasing Subsequence
##  compare patience sorting and DP solution(about 10 times slower)

"""
Problem
A subsequence of a permutation is a collection of elements of the permutation in the order that they appear. For example, (5, 3, 4) is a subsequence of (5, 1, 3, 4, 2).

A subsequence is increasing if the elements of the subsequence increase, and decreasing if the elements decrease. For example, given the permutation (8, 2, 1, 6, 5, 7, 4, 3, 9), an increasing subsequence is (2, 6, 7, 9), and a decreasing subsequence is (8, 6, 5, 4, 3). You may verify that these two subsequences are as long as possible.

Given: A positive integer n≤10000
 followed by a permutation π
 of length n
.

Return: A longest increasing subsequence of π
, followed by a longest decreasing subsequence of π
.

Sample Dataset
5
5 1 4 2 3

Sample Output
1 2 3
5 4 2
"""

## define function

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



dataset = []
with open("../datasets/LGIS_dataset.txt", 'r') as f:
    f.readline()
    dataset = [int(j) for j in f.readline().strip().split(' ')]



import time

ascend = False
start = time.time()
LCS = findLCS2(dataset,ascend)
print(len(LCS))
print(f"DP solution      -> {time.time()-start}")

start = time.time()
LCS = findLCS1(dataset, lambda a,b: a > b)
print(len(LCS))
print(f"patience sorting -> {time.time()-start}")



print("========================================")

print(" ".join(str(i) for i in LCS))
LCS = findLCS1(dataset, lambda a,b: a < b)
print(" ".join(str(i) for i in LCS))
