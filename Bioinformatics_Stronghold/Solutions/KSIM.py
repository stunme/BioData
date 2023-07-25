##  Finding a Motif with Modifications

"""
Problem
Given: A positive integer k
 (k≤50
), a DNA string s
 of length at most 5 kbp representing a motif, and a DNA string t
 of length at most 50 kbp representing a genome.

Return: All substrings t′
 of t
 such that the edit distance dE(s,t′)
 is less than or equal to k
. Each substring should be encoded by a pair containing its location in t
 followed by its length.

Sample Dataset
2
ACGTAG
ACGGATCGGCATCGT

Sample Output
1 4
1 5
1 6
"""


from utility import readFastaFileList

# two direction search

def ksim(seqT, seqS, k):
    k += 1
    lenT, lenS = len(seqT)+1, len(seqS)+1
    seqTr,seqSr = seqT[::-1], seqS[::-1]
    cache = []
    cur = [j for j in range(lenS)]
    for i in range(0,lenT-1):
        pre = cur.copy()
        for j in range(1,lenS):
            j_ = j - 1
            if seqTr[i]==seqSr[j_]:
                cur[j] = pre[j_]
            else:                        
                cur[j] = min(pre[j_],pre[j],cur[j_])+1
        if cur[j]<k:
            cache.append(lenT-i-2)

    result = []
    pre_super = [j for j in range(lenS)]
    for c in cache[::-1]:
        pre = pre_super.copy()
        cur = [k]*lenS
        subSeqT = seqT[c:]
        for i in range(0,min(len(subSeqT),lenS+k-1)):
            cur[0] = pre[0]+1
            for j in range(max(1,i-k+2),min(lenS,i+k+1)):
                j_ = j-1
                if subSeqT[i] == seqS[j_]:
                    cur[j] = pre[j_]
                else:
                    cur[j] = min(pre[j_],pre[j],cur[j_])+1
            if cur[-1]<k:
                result.append((c+1,i+1))
            pre = cur.copy()
    return result

with open("../datasets/KSIM_dataset.txt",'r') as f:
    k = int(f.readline().strip())
    motif = f.readline().strip()
    genome = f.readline().strip()

with open("result.txt",'w') as f:
    for i in ksim(genome,motif,k):
        f.write(' '.join(str(j) for j in i))
        f.write('\n')

###################################################################################
# one direction search, save all starting location

def ksim__(seqT, seqS, k):
    k += 1
    lenT, lenS = len(seqT)+1, len(seqS)+1
    aligns = set()
    cur = [j for j in range(lenS)]
    curPos = [{j} for j in range(lenS)]
    for i in range(0,lenT-1):
        pre = cur.copy()
        prePos = curPos
        curPos = [{i}]
        for j in range(1,lenS):
            j_ = j - 1
            if seqT[i]==seqS[j_]:
                cur[j] = pre[j_]
                curPos.append(prePos[j_].copy())
            else:                        
                a = pre[j_]
                b = pre[j]
                c = cur[j_]
                cur[j] = min(a,b,c)
                curPos.append(set())
                if cur[j]<k:
                    pass
                    if cur[j] == a:
                        curPos[j] |= prePos[j_]
                    if cur[j] == b:
                        curPos[j] |= prePos[j]
                    if cur[j] == c:
                        curPos[j] |= curPos[j_]
                cur[j] += 1
        if cur[j]<k:
            for m in curPos[j]:
                aligns.add((m+1,i-m))
                for n in range(1,k-cur[j]):
                    aligns.add((m+1+n,i-m-n))
                    aligns.add((max(1,m+1-n),i-m+n))
    return aligns

##  ======================================================================
# 2x faster and works for no overlap match (e.g. Rosaland samples)
def ksim_(seqT, seqS, k):
    k += 1
    lenT = len(seqT)+1
    lenS = len(seqS)+1
    aligns = []
    tracker = []
    for i in range(lenT):
        tracker.append([0]*lenS)
    cur = [j for j in range(lenS)]
    for i in range(1,lenT):
        pre = cur
        cur = [0]+[k]*(lenS-1)
        for j in range(1,lenS):
            if seqT[i-1]==seqS[j-1]:
                cur[j] = pre[j-1]

            else:
                cur[j] = min(pre[j-1],
                                 pre[j],
                                 cur[j-1])
                if cur[j] == k:
                    continue
                if cur[j] == pre[j]:
                    tracker[i][j] = 1
                elif cur[j] == cur[j-1]:
                    tracker[i][j] = 2
                cur[j] +=1
        if cur[j]<k:
            aligns.append((i,cur[j]))
    result = set()
    for a,b in aligns:
        i = a
        j = lenS-1
        while i*j !=0:
            if tracker[i][j] == 0:
                i -=1
                j -=1
            elif tracker[i][j] == 1:
                i -=1
            elif tracker[i][j] == 2:
                j -=1
        result.add((i+1,a-i))
        for m in range(1,k-b):
                result.add((i+1+m,a-i-m))
                result.add((max(1,i+1-m),a-i+m))
    return result


# with open("result.txt",'w') as f:
#     for i in ksim_(genome,motif,k):
#         f.write(' '.join(str(j) for j in i))
#         f.write('\n')
