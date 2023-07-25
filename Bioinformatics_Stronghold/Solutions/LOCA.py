##  Local Alignment with Scoring Matrix

""" 
Problem
A local alignment of two strings s
 and t
 is an alignment of substrings r
 and u
 of s
 and t
, respectively. Let opt(r,u)
 denote the score of an optimal alignment of r
 and u
 with respect to some predetermined alignment score.

Given: Two protein strings s
 and t
 in FASTA format (each having length at most 1000 aa).

Return: A maximum alignment score along with substrings r
 and u
 of s
 and t
, respectively, which produce this maximum alignment score (multiple solutions may exist, in which case you may output any one). Use:

The PAM250 scoring matrix.
Linear gap penalty equal to 5.
Sample Dataset
>Rosalind_80
MEANLYPRTEINSTRING
>Rosalind_21
PLEASANTLYEINSTEIN

Sample Output
23
LYPRTEINSTRIN
LYEINSTEIN
"""

##  define functions
from utility import readFastaFileList

def loca(seq1, seq2, scoreMatrixm, gap):
    lenI, lenJ = len(seq1)+1, len(seq2)+1
    arr = []
    tracker = []
    for i in range(lenI):
        arr.append([0]*lenJ)
        tracker.append([0]*lenJ)

    max_x, max_y = 0,0
    for i in range(1, lenI):
        for j in range(1, lenJ):
            tmp = [ arr[i-1][j-1] + scoreMatrixm[seq1[i-1]+seq2[j-1]],
                    arr[i-1][j] + gap,
                    arr[i][j-1] + gap,
                    0]
            arr[i][j] = max(tmp)
            tracker[i][j] = tmp.index(arr[i][j])
            if arr[max_x][max_y]<arr[i][j]:
                max_x, max_y = i,j

    i, j = max_x, max_y 
    while tracker[i][j] != 3 and i * j != 0:
        match tracker[i][j]:
            case 2:
                j -= 1
            case 1:
                i -= 1
            case 0:
                i -= 1
                j -= 1  
                
    return arr[max_x][max_y], seq1[i:max_x],seq2[j:max_y]
    

## construct BLOSUM62 scoring dict
with open("PAM250.txt","r") as f:
    aa = f.readline().strip().split()
    m = [l.strip().split() for l in f.readlines()]
scoreMatrixm = {}
for i in range(len(aa)):
   for j in range(1,len(aa)+1):
      scoreMatrixm[aa[i]+aa[j-1]] = int(m[i][j])


##  import dataset
gap = -5
seq = readFastaFileList("../datasets/LOCA_dataset.txt")


##  print result
result = loca(seq[0],seq[1],scoreMatrixm,gap)
print("\n".join(str(i) for i in result))
