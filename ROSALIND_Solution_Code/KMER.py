##  k-Mer Composition 
##  skip data validation

import itertools as it
from utility import readFastaFileList

def KMER(seq,k):
    dic = {}
    for i in it.product('ACGT',repeat=k):
        dic[''.join(j for j in i)] = 0
    for i in range(len(seq)-k+1):
        dic[seq[i:i+k]] += 1
    return dic



seq = readFastaFileList("test.txt")[0]

print(" ".join(str(v) for k,v in KMER(seq,4).items()))