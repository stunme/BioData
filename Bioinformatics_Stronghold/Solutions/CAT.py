##  Catalan Numbers and RNA Secondary Structures

"""
Problem

Figure 3. The only two noncrossing perfect matchings of basepair edges (shown in red) for the RNA string UAGCGUGAUCAC.

Figure 4. All possible noncrossing perfect matchings in complete graphs on 2, 4, 6, and 8 nodes; the total number of such matchings are 1, 2, 5, and 14, respectively.
A matching in a graph is noncrossing if none of its edges cross each other. If we assume that the n
 nodes of this graph are arranged around a circle, and if we label these nodes with positive integers between 1 and n
, then a matching is noncrossing as long as there are not edges {i,j}
 and {k,l}
 such that i<k<j<l
.

A noncrossing matching of basepair edges in the bonding graph corresponding to an RNA string will correspond to a possible secondary structure of the underlying RNA strand that lacks pseudoknots, as shown in Figure 3.

In this problem, we will consider counting noncrossing perfect matchings of basepair edges. As a motivating example of how to count noncrossing perfect matchings, let cn
 denote the number of noncrossing perfect matchings in the complete graph K2n
. After setting c0=1
, we can see that c1
 should equal 1 as well. As for the case of a general n
, say that the nodes of K2n
 are labeled with the positive integers from 1 to 2n
. We can join node 1 to any of the remaining 2n−1
 nodes; yet once we have chosen this node (say m
), we cannot add another edge to the matching that crosses the edge {1,m}
. As a result, we must match all the edges on one side of {1,m}
 to each other. This requirement forces m
 to be even, so that we can write m=2k
 for some positive integer k
.

There are 2k−2
 nodes on one side of {1,m}
 and 2n−2k
 nodes on the other side of {1,m}
, so that in turn there will be ck−1⋅cn−k
 different ways of forming a perfect matching on the remaining nodes of K2n
. If we let m
 vary over all possible n−1
 choices of even numbers between 1 and 2n
, then we obtain the recurrence relation cn=∑nk=1ck−1⋅cn−k
. The resulting numbers cn
 counting noncrossing perfect matchings in K2n
 are called the Catalan numbers, and they appear in a huge number of other settings. See Figure 4 for an illustration counting the first four Catalan numbers.

Given: An RNA string s
 having the same number of occurrences of 'A' as 'U' and the same number of occurrences of 'C' as 'G'. The length of the string is at most 300 bp.

Return: The total number of noncrossing perfect matchings of basepair edges in the bonding graph of s
, modulo 1,000,000.

Sample Dataset
>Rosalind_57
AUAU

Sample Output
2
"""

##  define function
from utility import readFastaFileList

dicAll={}
dicMatch = {'A':'U',
            'U':'A',
            'G':'C',
            'C':'G'
            }

def catalan(start, end, mod = 1000000):
    s = seq[start:end]
    if s.count('A')!=s.count('U') or s.count('G')!=s.count('C'):
        return 0
    if end <= start + 2:
        return 1
    sum =0
    for i in range(start+1,end,2):
        if dicMatch[seq[start]] == seq[i]:
            left = (start+1,i)
            right = (i+1,end)
            if left not in dicAll:
                dicAll[left] =catalan(left[0],left[1])
            if right not in dicAll:
                dicAll[right] = catalan(right[0],right[1])
            sum += dicAll[left]*dicAll[right]%mod
            sum %= mod
    return sum%mod


##  import dataset
seq = readFastaFileList("../datasets/CAT_dataset.txt")[0]

import time
start = time.time()
print(catalan(0,len(seq)))
print(time.time()-start)

## =================================================================================================
## a short solution from Rosalind. about 4 times slower.


c = {'':1, 'A':0, 'C':0, 'G':0, 'U':0, 'AA':0, 'AC':0, 'AG':0, 'AU':1, 'CA':0, 'CC':0, 
    'CG':1, 'CU':0, 'GA':0, 'GC':1, 'GG':0, 'GU':0, 'UA':1, 'UC':0, 'UG':0, 'UU':0}
s=seq

def catalan1(s, mod= 1000000):
    if s not in c:
        if s.count('C') != s.count('G') or s.count('A') != s.count('U'):
            c[s] = 0
        else:
            c[s] = sum([catalan1(s[1:k]) * c[s[0]+s[k]] * catalan1(s[k+1:]) for k in range(1, len(s), 2)])
    return c[s]%mod

start = time.time()
print(catalan1(s))
print(time.time()-start)


## =================================================================================================
## shorten my solution according to Rosaland solution. about 1.5 times slower.

dicAll={}
dicMatch = {'A':'U',
            'U':'A',
            'G':'C',
            'C':'G'
            }
def catalan2(start, end, mod = 1000000):
    tmp = (start,end)
    if tmp not in dicAll:
        s = seq[start:end]
        if s.count('A')!=s.count('U') or s.count('G')!=s.count('C'):
            dicAll[tmp] = 0
        elif end <= start + 2:
            dicAll[tmp] = 1
        else:
            dicAll[tmp] = sum([catalan2(start+1,i)*catalan2(i+1,end)%mod for i in range(start+1,end,2) if dicMatch[seq[start]] == seq[i]])%mod
    return dicAll[tmp]


start = time.time()
print(catalan2(0,len(seq)))
print(time.time()-start)
