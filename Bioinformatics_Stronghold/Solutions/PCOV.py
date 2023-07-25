##  Genome Assembly with Perfect Coverage

"""
Problem
A circular string is a string that does not have an initial or terminal element; instead, the string is viewed as a necklace of symbols. We can represent a circular string as a string enclosed in parentheses. For example, consider the circular DNA string (ACGTAC), and note that because the string "wraps around" at the end, this circular string can equally be represented by (CGTACA), (GTACAC), (TACACG), (ACACGT), and (CACGTA). The definitions of substrings and superstrings are easy to generalize to the case of circular strings (keeping in mind that substrings are allowed to wrap around).

Given: A collection of (error-free) DNA k
-mers (k≤50
) taken from the same strand of a circular chromosome. In this dataset, all k
-mers from this strand of the chromosome are present, and their de Bruijn graph consists of exactly one simple cycle.

Return: A cyclic superstring of minimal length containing the reads (thus corresponding to a candidate cyclic chromosome).

Sample Dataset
ATTAC
TACAG
GATTA
ACAGA
CAGAT
TTACA
AGATT

Sample Output
GATTACA
"""


with open("../datasets/PCOV_dataset.txt","r") as f:
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

##  print result
print(seq)