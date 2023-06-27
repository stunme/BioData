##  Interleaving Two Motifs
## same mapping stratage to lcsq, but add seq at every step of traceback

def scsp(seqI, seqJ):
    lenI, lenJ = len(seqI)+1, len(seqJ)+1
    arr = []
    arr.append([0]*lenJ)
    for i in range(1,lenI):
        arr.append([0]*lenJ)
        for j in range(1,lenJ):
           if seqI[i-1] == seqJ[j-1]:
               arr[i][j] = arr[i-1][j-1]+1
           else:
               arr[i][j] = max(arr[i-1][j],arr[i][j-1])

    seq = ""
    while i*j!=0:
        if arr[i][j] == arr[i-1][j]:
            i -= 1
            seq = seqI[i]+seq
        elif arr[i][j] == arr[i][j-1]:
            j -= 1
            seq = seqJ[j]+seq
        else:
            i -=1
            seq = seqI[i]+seq
            j -=1
    
    return seqI[:i]+seqJ[:j]+seq

with open("test.txt",'r') as f:
    seq1 = f.readline().strip()
    seq2 = f.readline().strip()
print(scsp(seq1,seq2))

