##  Speeding Up Motif Finding 

from utility import readFastaFileList

def kmp(seq):
    result = [0]*len(seq)
    for i in range(1,len(seq)):
        j = result[i-1]
        while j>0 and seq[i]!=seq[j]:
            j = result[j-1]
        if seq[i] == seq[j]:
            j += 1
        result[i] = j
    return result

import time

seq = readFastaFileList("test.txt")[0]
print(kmp(seq))

# with open("result.txt",'w') as f:
#     for i in range(len(a)):
#         f.write(f"{a[i]} ")
