##  Using the Spectrum Graph to Infer Peptides

"""
Problem
For a weighted alphabet A
 and a collection L
 of positive real numbers, the spectrum graph of L
 is a digraph constructed in the following way. First, create a node for every real number in L
. Then, connect a pair of nodes with a directed edge (u,v)
 if v>u
 and v−u
 is equal to the weight of a single symbol in A
. We may then label the edge with this symbol.

In this problem, we say that a weighted string s=s1s2⋯sn
 matches L
 if there is some increasing sequence of positive real numbers (w1,w2,…,wn+1)
 in L
 such that w(s1)=w2−w1
, w(s2)=w3−w2
, ..., and w(sn)=wn+1−wn
.

Given: A list L
 (of length at most 100) containing positive real numbers.

Return: The longest protein string that matches the spectrum graph of L
 (if multiple solutions exist, you may output any one of them). Consult the monoisotopic mass table.

Sample Dataset
3524.8542
3623.5245
3710.9335
3841.974
3929.00603
3970.0326
4026.05879
4057.0646
4083.08025

Sample Output
WMSPG
"""

HOH = 18.01056 
dic = {
    'A':   71.03711,
    'C':  103.00919,
    'D':   115.02694,
    'E':   129.04259,
    'F':   147.06841,
    'G':   57.02146,
    'H':   137.05891,
    'I':   113.08406,
    'K':   128.09496,
    'L':   113.08406,
    'M':   131.04049,
    'N':   114.04293,
    'P':   97.05276,
    'Q':   128.05858,
    'R':   156.10111,
    'S':   87.03203,
    'T':   101.04768,
    'V':   99.06841,
    'W':   186.07931,
    'Y':   163.06333 }
## creat a dict for index amino acid by mass
massDic = {}
for k,v in dic.items():
    massDic[round(v,2)] = k

## read the input file
with open("../datasets/SGRA_dataset.txt","r") as f:
    massList = [float(i.strip()) for i in f.readlines()]

## not sure the orginal data is sorted or not.
massList.sort(reverse = True)

aaDic = {}
treeDic = {}
#creat all potential edges
for i in range(len(massList)):
    for j in range(i+1,len(massList)):
        tmp = round(massList[i]-massList[j],2)
        if tmp in massDic:
            if j in treeDic:
                treeDic[j].append(i)
            else:
                treeDic[j] = [i]
            aaDic[(j,i)] = massDic[tmp]

# find longest peptide
def longestPeptide(start, seq):
    if start ==0 or start not in treeDic:
        return seq
    maxLen = 0
    curSeq = ""
    for i in treeDic[start]:
        tmp = longestPeptide(i,aaDic[start,i])
        if len(tmp)> maxLen:
            maxLen = len(tmp)
            curSeq = tmp
    return seq+curSeq
    
print(longestPeptide(len(massList)-1,""))
