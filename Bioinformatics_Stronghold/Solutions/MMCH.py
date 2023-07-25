##  aximum Matchings and RNA Secondary Structures

"""
Problem

Figure 1. The bonding graph of s = UAGCGUGAUCAC (left) has a perfect matching of basepair edges, but this is not the case for t = CAGCGUGAUCAC (right), in which one symbol has been replaced.

Figure 2. A maximum matching (highlighted in red) is shown in each of the three graphs above. You can verify that no other matching can contain more edges. (Courtesy: Miym, Wikimedia Commons User)

Figure 3. A red maximum matching of basepair edges in the bonding graph for t = CAGCGUGAUCAC.
The graph theoretical analogue of the quandary stated in the introduction above is that if we have an RNA string s
 that does not have the same number of occurrences of 'C' as 'G' and the same number of occurrences of 'A' as 'U', then the bonding graph of s
 cannot possibly possess a perfect matching among its basepair edges. For example, see Figure 1; in fact, most bonding graphs will not contain a perfect matching.

In light of this fact, we define a maximum matching in a graph as a matching containing as many edges as possible. See Figure 2 for three maximum matchings in graphs.

A maximum matching of basepair edges will correspond to a way of forming as many base pairs as possible in an RNA string, as shown in Figure 3.

Given: An RNA string s
 of length at most 100.

Return: The total possible number of maximum matchings of basepair edges in the bonding graph of s
.

Sample Dataset
>Rosalind_92
AUGCUUC

Sample Output
6
"""

## import and process data 
from utility import readFastaFileList
import math

seq = readFastaFileList("../datasets/MMCH_dataset.txt")[0]

dic = {"A":0,
       "U":0,
       "G":0,
       "C":0,
    }

for i in seq:
    dic[i] += 1


if dic["A"]>dic["U"]:
    prob = math.factorial(dic["A"])/math.factorial(dic["A"]-dic["U"])
else:
    prob = math.factorial(dic["U"])/math.factorial(dic["U"]-dic["A"])

if dic["G"]>dic["C"]:
    prob *= math.factorial(dic["G"])/math.factorial(dic["G"]-dic["C"])
else:
    prob *= math.factorial(dic["C"])/math.factorial(dic["C"]-dic["G"])

##  print result
print(prob)
