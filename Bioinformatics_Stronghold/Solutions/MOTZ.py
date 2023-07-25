##   Motzkin Numbers and RNA Secondary Structures

"""
Problem

Figure 1. The 21 distinct ways to form a noncrossing matching on 5 labeled nodes. (Courtesy: Robertd, Wikimedia Commons User)

Figure 2. Two possible noncrossing matchings of basepair edges in the bonding graph corresponding to RNA string UAGCGUGAUCAC.
Similarly to our definition of the Catalan numbers, the n
-th Motzkin number mn
 counts the number of ways to form a (not necessarily perfect) noncrossing matching in the complete graph Kn
 containing n
 nodes. For example, Figure 1 demonstrates that m5=21
. Note in this figure that technically, the "trivial" matching that contains no edges at all is considered to be a matching, because it satisfies the defining condition that no two edges are incident to the same node.

How should we compute the Motzkin numbers? As with Catalan numbers, we will take m0=m1=1
. To calculate mn
 in general, assume that the nodes of Kn
 are labeled around the outside of a circle with the integers between 1 and n
, and consider node 1, which may or may not be involved in a matching. If node 1 is not involved in a matching, then there are mn−1
 ways of matching the remaining n−1
 nodes. If node 1 is involved in a matching, then say it is matched to node k
: this leaves k−2
 nodes on one side of edge {1,k}
 and n−k
 nodes on the other side; as with the Catalan numbers, no edge can connect the two sides, which gives us mk−2⋅mn−k
 ways of matching the remaining edges. Allowing k
 to vary between 2
 and n
 yields the following recurrence relation for the Motzkin numbers: mn=mn−1+∑nk=2mk−2⋅mn−k
.

To count all possible secondary structures of a given RNA string that do not contain pseudoknots, we need to modify the Motzkin recurrence so that it counts only matchings of basepair edges in the bonding graph corresponding to the RNA string; see Figure 2.

Given: An RNA string s
 of length at most 300 bp.

Return: The total number of noncrossing matchings of basepair edges in the bonding graph of s
, modulo 1,000,000.

Sample Dataset
>Rosalind_57
AUAU

Sample Output
7
"""

##  define function

dicMatch = {'A':'U',
            'U':'A',
            'G':'C',
            'C':'G'
            }
dicAll ={}

def Motzkin(seq, mod= 1000000):
    if seq not in dicAll:
        if len(seq) < 2:
            return 1   
        sum =Motzkin(seq[1:],mod)
        for i in range(1,len(seq)):
            if dicMatch[seq[0]] == seq[i]:
                sum += Motzkin(seq[1:i],mod)*Motzkin(seq[i+1:],mod)%mod
        dicAll[seq] = sum%mod
    return dicAll[seq]

##  import dataset
from utility import readFastaFileList
seq = readFastaFileList("../datasets/MOTz_dataset.txt")[0]

##  print result
print(Motzkin(seq))



