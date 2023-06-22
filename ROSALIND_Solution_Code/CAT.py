##  Catalan Numbers and RNA Secondary Structures

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


seq = readFastaFileList("test.txt")[0]

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
